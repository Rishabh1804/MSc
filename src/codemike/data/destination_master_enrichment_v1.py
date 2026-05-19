"""E1 enrichment pass over destinations_master_v2.csv.

Implements the v1 enrichment strategy at
`datasets/reference/destination_master_enrichment_strategy.md`.

Inputs:

1. datasets/reference/destinations_master_v2.csv             (359 master rows)
2. datasets/reference/origin_catchment_v1.json               (CCU + IXR lookup)

Outputs:

1. datasets/reference/destinations_master_v2_enriched.csv
2. reports/evidence/destination-master-v2-enrichment-report.md
3. reports/evidence/destination-master-v2-enrichment-manual-review-queues/O.csv
4. reports/evidence/destination-master-v2-enrichment-manual-review-queues/S.csv
5. reports/evidence/destination-master-v2-enrichment-manual-review-queues/M.csv

Pipeline (per strategy doc §10.1, amended in §18 for the data-inspection findings):

  Step 0   Read master CSV + catchment.
  Step 1a  Derive access_complexity for candidate rows (master has it blank).
  Step 1b  Derive caution tags from location_type / state_or_area / macro_region
           / destination_scale / vibes (master has caution_tags blank).
  Step 2   Compute origin_fit per origin (CCU + IXR).
  Step 3   Compute travel_fatigue band + drivers.
  Step 4   Compute medical_access_confidence; recompute pediatric subset.
  Step 5   Compute planning_complexity band + drivers + permit/visa hint.
  Step 6   Compute season window + weather cautions.
  Step 7   Compute suitability decomposed (infant score + 4 bands).
  Step 8   Set verification_status / planner_use_status / source_confidence defaults.
  Step 9   Queue rows for manual-review batches O / S / M.

The script is deterministic per Cipher discipline (strategy doc §10.2): given the
same inputs + same heuristic version, output is byte-identical modulo
enrichment_pass_date.

Default after this pass: every row carries verification_status="enriched_unverified",
planner_use_status="needs_verification", source_confidence="low". No row crosses to
planner_ready in v1 enrichment.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Iterable


MASTER_PATH = Path("datasets/reference/destinations_master_v2.csv")
CATCHMENT_PATH = Path("datasets/reference/origin_catchment_v1.json")
ENRICHED_PATH = Path("datasets/reference/destinations_master_v2_enriched.csv")
REPORT_PATH = Path("reports/evidence/destination-master-v2-enrichment-report.md")
QUEUE_DIR = Path("reports/evidence/destination-master-v2-enrichment-manual-review-queues")
QUEUE_O_PATH = QUEUE_DIR / "O.csv"
QUEUE_S_PATH = QUEUE_DIR / "S.csv"
QUEUE_M_PATH = QUEUE_DIR / "M.csv"

ENRICHMENT_VERSION = "v1.0"

OUTPUT_COLUMNS = [
    "destination_master_id",
    "enrichment_version",
    "enrichment_pass_date",
    "enrichment_method",
    "origin_fit_ccu",
    "origin_fit_ccu_basis",
    "origin_fit_ccu_confidence",
    "origin_fit_ixr",
    "origin_fit_ixr_basis",
    "origin_fit_ixr_confidence",
    "infant_suitability_score",
    "infant_suitability_band",
    "family_suitability_band",
    "senior_suitability_band",
    "couple_suitability_band",
    "suitability_basis",
    "travel_fatigue_band",
    "travel_fatigue_drivers",
    "transfer_complexity_hint",
    "planning_complexity_band",
    "planning_complexity_drivers",
    "permit_or_visa_hint",
    "medical_access_confidence",
    "medical_access_basis",
    "pediatric_access_confidence",
    "season_window",
    "monsoon_caution",
    "heat_caution",
    "winter_road_caution",
    "altitude_caution",
    "weather_basis",
    "resort_family_density",
    "accommodation_breadth",
    "derived_access_complexity",
    "derived_caution_tags",
    "verification_status",
    "planner_use_status",
    "source_confidence",
    "enrichment_notes",
]


# Static lookups derived from the tag dictionary and master inspection.
ALTITUDE_LOCATION_KEYWORDS = ("high_altitude",)
ISLAND_LOCATION_KEYWORDS = ("island",)
DESERT_LOCATION_KEYWORDS = ("desert",)
HILL_LOCATION_KEYWORDS = ("hill", "mountain")
COASTAL_LOCATION_KEYWORDS = ("beach", "coast")
WILDLIFE_LOCATION_KEYWORDS = ("wildlife", "national_park", "tiger_reserve", "biosphere", "park")
PILGRIM_LOCATION_KEYWORDS = ("pilgrim", "spiritual", "temple", "monastery", "char_dham", "jain", "buddhist", "sikh")
CITY_LOCATION_KEYWORDS = ("metro_city", "global_city", "capital_city", "business_city", "gateway", "global", "business")

HEAT_MACRO_REGIONS = {"North India", "Central India", "West India"}
MONSOON_HEAVY_MACRO_REGIONS = {"South India", "North East India", "Island India"}
WESTERN_HIMALAYA_STATES = {"Himachal Pradesh", "Uttarakhand", "Ladakh", "Jammu and Kashmir"}
EASTERN_HIMALAYA_STATES = {"Sikkim", "Arunachal Pradesh"}
BORDER_AREA_STATES = {
    "Arunachal Pradesh",
    "Mizoram",
    "Nagaland",
    "Manipur",
    "Sikkim",
    "Ladakh",
    "Jammu and Kashmir",
}

DOMESTIC_BIG_CITIES_LIST = {
    "Delhi NCR",
    "Mumbai",
    "Bengaluru",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Pune",
    "Ahmedabad",
}


def load_catchment(path: Path = CATCHMENT_PATH) -> dict:
    """Load the origin-catchment lookup as a dict."""

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def read_master(path: Path = MASTER_PATH) -> list[dict[str, str]]:
    """Read the master destination CSV as a list of dicts."""

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


# ---------------------------------------------------------------------------
# Step 1a — derive access_complexity for candidate rows
# ---------------------------------------------------------------------------


def derive_access_complexity(row: dict[str, str]) -> str:
    """Return the row's access_complexity, deriving for candidate rows.

    Seed rows carry access_complexity from the seed dataset; candidate rows are
    blank and need a heuristic value.
    """

    existing = (row.get("access_complexity") or "").strip()
    if existing in {"easy", "moderate", "hard"}:
        return existing

    scale = (row.get("destination_scale") or "").lower()
    location_type = (row.get("location_type") or "").lower()
    state = (row.get("state_or_area") or "")
    country = (row.get("country") or "")

    if any(token in location_type for token in ALTITUDE_LOCATION_KEYWORDS):
        return "hard"
    if scale in {"island", "high_altitude"}:
        return "hard"
    if state in BORDER_AREA_STATES:
        return "hard"
    if scale in {"village", "site"} and country == "India":
        return "moderate"
    if any(token in location_type for token in WILDLIFE_LOCATION_KEYWORDS):
        return "moderate"
    if any(token in location_type for token in CITY_LOCATION_KEYWORDS):
        return "easy"
    if scale in {"city"}:
        return "easy"
    return "moderate"


# ---------------------------------------------------------------------------
# Step 1b — derive caution tags from populated fields
# ---------------------------------------------------------------------------


def derive_cautions(row: dict[str, str], access: str) -> list[str]:
    """Return a list of caution tags derived from populated fields.

    Master rows have caution_tags effectively blank (3 tags across 359 rows).
    This step generates the cautions that downstream heuristics consume.
    Existing caution_tags from master are preserved and merged in.
    """

    cautions: set[str] = set()

    existing = (row.get("caution_tags") or "").strip()
    if existing:
        cautions.update(t.strip() for t in existing.split(";") if t.strip())

    macro_region = row.get("macro_region") or ""
    state = row.get("state_or_area") or ""
    scale = (row.get("destination_scale") or "").lower()
    location_type = (row.get("location_type") or "").lower()
    country = row.get("country") or ""
    vibes = {(row.get("vibe_1") or "").lower(),
             (row.get("vibe_2") or "").lower(),
             (row.get("vibe_3") or "").lower()}

    # Altitude
    if any(token in location_type for token in ALTITUDE_LOCATION_KEYWORDS):
        cautions.add("altitude_check")
    if state in {"Ladakh", "Sikkim"} and scale in {"high_altitude", "village", "site"}:
        cautions.add("altitude_check")

    # Heat
    if macro_region in HEAT_MACRO_REGIONS:
        cautions.add("heat_check")
    if "desert" in vibes or any(token in location_type for token in DESERT_LOCATION_KEYWORDS):
        cautions.add("heat_check")

    # Monsoon
    if macro_region in MONSOON_HEAVY_MACRO_REGIONS:
        cautions.add("monsoon_check")
    if state in {"Goa", "Kerala"}:
        cautions.add("monsoon_check")
    if "monsoon" in vibes or "rain" in vibes:
        cautions.add("monsoon_check")

    # Winter / road / snow
    if state in WESTERN_HIMALAYA_STATES and any(t in location_type for t in HILL_LOCATION_KEYWORDS + ALTITUDE_LOCATION_KEYWORDS):
        cautions.add("winter_road_weather_check")
        cautions.add("snow_closure_check")
    if state in EASTERN_HIMALAYA_STATES and any(t in location_type for t in HILL_LOCATION_KEYWORDS + ALTITUDE_LOCATION_KEYWORDS):
        cautions.add("winter_road_weather_check")

    # Long road transfers + road difficulty
    if access == "hard":
        cautions.add("long_road_transfer_check")

    # Infant food access (small/remote settlements)
    if scale in {"village", "site", "park"} or any(t in location_type for t in WILDLIFE_LOCATION_KEYWORDS):
        cautions.add("infant_food_access_check")
    if any(t in location_type for t in ALTITUDE_LOCATION_KEYWORDS):
        cautions.add("infant_food_access_check")

    # Permit / border (ILP states + adjacent)
    if state in BORDER_AREA_STATES:
        cautions.add("permit_check")
        cautions.add("border_area_check")

    # Crowd (pilgrim sites, popular metros during festival vibes)
    if any(t in location_type for t in PILGRIM_LOCATION_KEYWORDS):
        cautions.add("crowd_check")
    if "festival" in vibes:
        cautions.add("festival_crowd_check")

    # Ferry / island
    if scale == "island" or "island" in location_type:
        cautions.add("ferry_schedule_check")

    # Passport / visa (international)
    if country and country != "India":
        cautions.add("visa_rules_check")
        cautions.add("passport_check")

    # Mobility (high-altitude or remote terrain)
    if any(t in location_type for t in ALTITUDE_LOCATION_KEYWORDS) or scale == "high_altitude":
        cautions.add("mobility_access_check")

    return sorted(cautions)


# ---------------------------------------------------------------------------
# Step 2 — origin fit
# ---------------------------------------------------------------------------


def compute_origin_fit(row: dict[str, str], origin_key: str, catchment: dict) -> tuple[str, str, str, bool]:
    """Return (fit, basis, confidence, needs_review) for the given origin.

    needs_review=True signals the row should be queued for manual-review batch O
    (strategy doc §11.1).
    """

    origin = catchment["origins"][origin_key]
    city = origin["city"]
    macro_region = row.get("macro_region") or ""
    state = row.get("state_or_area") or ""
    country = row.get("country") or ""
    scale = (row.get("destination_scale") or "").lower()
    location_type = (row.get("location_type") or "").lower()

    if country != "India":
        # International — uniformly weak from either origin in v1.
        return ("weak", f"international destination ({country}); multi-leg from {city}", "medium", False)

    if state in origin.get("state_overrides_strong", []):
        return ("strong", f"{state} (state-level) is within {city} primary catchment", "high", False)
    if state in origin.get("state_overrides_secondary", []):
        return ("moderate", f"{state} (state-level) is within {city} secondary catchment", "medium", False)

    if macro_region in origin["primary_macro_regions"]:
        return ("strong", f"{macro_region} is within {city} primary catchment", "high", False)
    if macro_region in origin["secondary_macro_regions"]:
        return ("moderate", f"{macro_region} is within {city} secondary catchment", "medium", False)
    if macro_region in origin.get("weak_macro_regions", []):
        return ("weak", f"{macro_region} is outside {city} regular catchment", "medium", False)
    if macro_region in origin.get("domestic_far_macro_regions", []):
        return ("weak", f"{macro_region} requires long-haul domestic leg from {city}", "medium", False)
    if any(t in location_type for t in ALTITUDE_LOCATION_KEYWORDS) or scale in {"island", "high_altitude"}:
        return ("weak", f"remote/high-access destination ({location_type or scale})", "medium", False)

    # Heuristic insufficient — queue for manual review.
    return ("unknown", "heuristic insufficient; manual review required", "low", True)


# ---------------------------------------------------------------------------
# Step 3 — travel fatigue
# ---------------------------------------------------------------------------


def compute_travel_fatigue(row: dict[str, str], access: str, cautions: list[str], country: str, macro_region: str) -> tuple[str, list[str], str]:
    """Return (band, drivers, transfer_complexity_hint) per strategy doc §6.3."""

    drivers: list[str] = []
    location_type = (row.get("location_type") or "").lower()
    scale = (row.get("destination_scale") or "").lower()

    if access == "hard":
        drivers.append("long_road_transfer")
        drivers.append("high_road_difficulty")
    if "long_road_transfer_check" in cautions and "long_road_transfer" not in drivers:
        drivers.append("long_road_transfer")
    if "altitude_check" in cautions or any(t in location_type for t in ALTITUDE_LOCATION_KEYWORDS):
        drivers.append("altitude")
    if scale == "island" or "ferry_schedule_check" in cautions:
        drivers.append("ferry_dependent")
    if "border_area_check" in cautions or "permit_check" in cautions:
        drivers.append("remoteness")
    if country != "India":
        drivers.append("multi_leg")
    elif macro_region in {"West India", "South India", "Island India"}:
        # East-India-origin assumption per CCU/IXR; far-domestic = multi_leg from these origins.
        drivers.append("multi_leg")

    # De-dup preserving order
    seen: set[str] = set()
    drivers = [d for d in drivers if not (d in seen or seen.add(d))]

    # Transfer complexity
    if scale == "island" or country != "India":
        transfer_hint = "multi_leg"
    elif access == "hard" or "remoteness" in drivers:
        transfer_hint = "complex"
    else:
        transfer_hint = "simple"

    # Band
    if len(drivers) == 0 and access == "easy":
        band = "low"
    elif len(drivers) == 1 and access == "easy":
        band = "low"
    elif len(drivers) <= 2 and access != "hard":
        band = "medium"
    elif len(drivers) >= 3 or ("altitude" in drivers and "remoteness" in drivers):
        band = "very_high"
    else:
        band = "high"

    return (band, drivers, transfer_hint)


# ---------------------------------------------------------------------------
# Step 4 — medical access
# ---------------------------------------------------------------------------


def compute_medical_access(row: dict[str, str], cautions: list[str], fatigue_drivers: list[str]) -> tuple[str, str, str, bool]:
    """Return (confidence, basis, pediatric_confidence, needs_review)."""

    scale = (row.get("destination_scale") or "").lower()
    location_type = (row.get("location_type") or "").lower()
    country = row.get("country") or ""
    canonical_name = row.get("canonical_name") or ""

    needs_review = False

    if country != "India":
        confidence = "unknown"
        basis = f"international destination ({country}); medical access depends on local context; manual review"
        needs_review = True
    elif scale == "metro_city" or any(t in location_type for t in ("metro_city", "global_city", "global")) or canonical_name in DOMESTIC_BIG_CITIES_LIST:
        confidence = "high"
        basis = "metro/major-city tier; tertiary care assumed available"
    elif scale == "city" or any(t in location_type for t in ("capital_city", "business_city", "education_city", "heritage_capital")):
        confidence = "high"
        basis = "major-city tier; tertiary care assumed available"
    elif scale in {"town"} or any(t in location_type for t in ("city",)):
        confidence = "medium"
        basis = "town/secondary-city tier; district-level care assumed"
    elif scale in {"village", "site", "park", "high_altitude"} or "remoteness" in fatigue_drivers:
        confidence = "low"
        basis = "remote/small-settlement tier; medical access limited"
    else:
        confidence = "unknown"
        basis = "heuristic insufficient; manual review required"
        needs_review = True

    # Pediatric subset — downgrade by one if infant-food access is constrained.
    pediatric = confidence
    if "infant_food_access_check" in cautions and confidence in {"medium", "high"}:
        pediatric = "medium" if confidence == "high" else "low"

    return (confidence, basis, pediatric, needs_review)


# ---------------------------------------------------------------------------
# Step 5 — planning complexity
# ---------------------------------------------------------------------------


def compute_planning_complexity(row: dict[str, str], fatigue_drivers: list[str], cautions: list[str]) -> tuple[str, list[str], str]:
    """Return (band, drivers, permit_or_visa_hint)."""

    drivers: list[str] = []
    permit_hint = ""

    country = row.get("country") or ""
    scale = (row.get("destination_scale") or "").lower()
    location_type = (row.get("location_type") or "").lower()

    if "permit_check" in cautions:
        drivers.append("permit_required")
        permit_hint = "inner_line_permit_or_equivalent_required_check_current_rules"
    if country and country != "India":
        drivers.append("visa_required")
        permit_hint = "international_visa_or_passport_required_check_current_rules"
    if scale == "island" or "ferry_dependent" in fatigue_drivers:
        drivers.append("ferry_schedule")
    if "snow_closure_check" in cautions or "monsoon_check" in cautions:
        drivers.append("seasonal_closure")
    if any(t in location_type for t in WILDLIFE_LOCATION_KEYWORDS):
        if "seasonal_closure" not in drivers:
            drivers.append("seasonal_closure")
        drivers.append("booking_lead_time")
    if "altitude" in fatigue_drivers:
        drivers.append("medical_prep")
    if "ferry_dependent" in fatigue_drivers or "remoteness" in fatigue_drivers:
        drivers.append("weather_critical")

    # De-dup preserving order
    seen: set[str] = set()
    drivers = [d for d in drivers if not (d in seen or seen.add(d))]

    if len(drivers) == 0:
        band = "low"
    elif len(drivers) <= 2:
        band = "medium"
    else:
        band = "high"

    return (band, drivers, permit_hint)


# ---------------------------------------------------------------------------
# Step 6 — season + weather cautions
# ---------------------------------------------------------------------------


SEASON_DEFAULTS_BY_REGION = {
    "South India": "Oct-Mar",
    "North India": "Oct-Mar",
    "Central India": "Oct-Mar",
    "East India": "Oct-Mar",
    "West India": "Oct-Mar",
    "North East India": "Oct-Apr",
    "Island India": "Oct-May",
    "Near India": "Oct-Apr",
    "Southeast Asia": "Nov-Feb",
    "Middle East": "Nov-Mar",
    "Indian Ocean": "Nov-Apr",
    "Central Asia": "Apr-Oct",
    "Caucasus": "May-Oct",
    "West Asia": "Oct-Apr",
}


def compute_season_and_weather(row: dict[str, str], cautions: list[str]) -> tuple[str, str, str, str, str, str]:
    """Return (season_window, monsoon, heat, winter_road, altitude, weather_basis)."""

    existing_season = (row.get("best_season_hint") or "").strip()
    macro_region = row.get("macro_region") or ""
    state = row.get("state_or_area") or ""
    scale = (row.get("destination_scale") or "").lower()
    location_type = (row.get("location_type") or "").lower()

    if existing_season:
        season_window = f"{existing_season} (verify_current_year)"
    else:
        default = SEASON_DEFAULTS_BY_REGION.get(macro_region, "unknown")
        if default == "unknown":
            season_window = "unknown — verify per destination"
        else:
            season_window = f"{default} (verify_current_year)"

    # Monsoon
    if "monsoon_check" in cautions and (scale == "high_altitude" and macro_region in {"North East India"}):
        monsoon = "avoid"
    elif "monsoon_check" in cautions:
        monsoon = "check"
    else:
        monsoon = "none"

    # Heat
    if scale == "desert_region" or "desert" in location_type:
        heat = "avoid"
    elif "heat_check" in cautions:
        heat = "check"
    else:
        heat = "none"

    # Winter road
    if state in WESTERN_HIMALAYA_STATES and (any(t in location_type for t in ALTITUDE_LOCATION_KEYWORDS) or "snow_closure_check" in cautions):
        winter_road = "avoid"
    elif "snow_closure_check" in cautions or "winter_road_weather_check" in cautions:
        winter_road = "check"
    else:
        winter_road = "none"

    # Altitude
    if any(t in location_type for t in ALTITUDE_LOCATION_KEYWORDS) or scale == "high_altitude":
        altitude = "avoid"
    elif "altitude_check" in cautions:
        altitude = "check"
    else:
        altitude = "none"

    # Weather basis — name the dominant caution if any
    dominant: list[str] = []
    if monsoon != "none":
        dominant.append(f"monsoon:{monsoon}")
    if heat != "none":
        dominant.append(f"heat:{heat}")
    if winter_road != "none":
        dominant.append(f"winter_road:{winter_road}")
    if altitude != "none":
        dominant.append(f"altitude:{altitude}")
    basis = ";".join(dominant) if dominant else "no major weather caution"

    return (season_window, monsoon, heat, winter_road, altitude, basis)


# ---------------------------------------------------------------------------
# Step 7 — suitability decomposed
# ---------------------------------------------------------------------------


def compute_infant_score(row: dict[str, str], medical: str, cautions: list[str], access: str) -> int:
    """Return infant_suitability_score in [0, 100] per strategy doc §5.2."""

    score = 60

    if access == "easy":
        score += 10
    elif access == "moderate":
        score -= 5
    elif access == "hard":
        score -= 15

    if medical == "high":
        score += 10
    elif medical == "medium":
        score -= 5
    elif medical == "low":
        score -= 15
    elif medical == "unknown":
        score -= 5

    if "infant_friendly" in (row.get("context_tags") or ""):
        score += 5

    budget = row.get("budget_band") or ""
    if budget in {"mid", "mid_premium", "premium", "luxury"}:
        score += 5

    if "altitude_check" in cautions:
        score -= 10
    if "heat_check" in cautions:
        score -= 10
    if "long_road_transfer_check" in cautions:
        score -= 10
    if "infant_food_access_check" in cautions:
        score -= 10
    if "monsoon_check" in cautions:
        score -= 5
    if "crowd_check" in cautions:
        score -= 5
    if "permit_check" in cautions:
        score -= 5

    scale = (row.get("destination_scale") or "").lower()
    if scale in {"high_altitude", "park", "island"} and "infant_friendly" not in (row.get("context_tags") or ""):
        score -= 10

    # Floor: if altitude + low medical access, hard-floor at 25
    if "altitude_check" in cautions and medical == "low":
        score = max(score, 25) if score >= 25 else 25

    return max(0, min(100, score))


def band_from_score(score: int) -> str:
    """Map infant_suitability_score to a band per strategy doc §5.2."""

    if score < 30:
        return "low"
    if score < 50:
        return "low_medium"
    if score < 75:
        return "medium"
    return "high"


BAND_ORDER = ["low", "low_medium", "medium", "high"]


def bump_band(band: str, delta: int) -> str:
    """Bump a band up (+1) or down (-1), saturating at endpoints."""

    if band not in BAND_ORDER:
        return "medium"
    idx = BAND_ORDER.index(band)
    new_idx = max(0, min(len(BAND_ORDER) - 1, idx + delta))
    return BAND_ORDER[new_idx]


def compute_family_band(row: dict[str, str], access: str, cautions: list[str]) -> str:
    """Family band (school-age children); per strategy doc §5.3."""

    band = "medium"
    context = row.get("context_tags") or ""
    if access == "easy" and "family_friendly" in context:
        band = bump_band(band, 1)
    if access == "hard" or "permit_check" in cautions or (row.get("destination_scale") or "").lower() == "high_altitude":
        band = bump_band(band, -1)
    if "altitude_check" in cautions and "family_friendly" not in context:
        band = "low"
    return band


def compute_senior_band(row: dict[str, str], access: str, cautions: list[str], medical: str) -> str:
    """Senior band (mobility-sensitive); per strategy doc §5.3."""

    band = "medium"
    context = row.get("context_tags") or ""
    if access == "easy" and "senior_friendly" in context and medical in {"medium", "high"}:
        band = bump_band(band, 1)
    if access == "hard" or "altitude_check" in cautions or "mobility_access_check" in cautions:
        band = bump_band(band, -1)
    if "altitude_check" in cautions and "mobility_access_check" in cautions:
        band = "low"
    return band


def compute_couple_band(row: dict[str, str], cautions: list[str]) -> str:
    """Couple band; per strategy doc §5.3."""

    band = "medium"
    vibe_1 = (row.get("vibe_1") or "").lower()
    context = row.get("context_tags") or ""
    scale = (row.get("destination_scale") or "").lower()
    if vibe_1 in {"romantic", "relaxation", "wellness"} or "couple_friendly" in context or scale == "resort_zone":
        band = bump_band(band, 1)
    if "crowd_check" in cautions and vibe_1 not in {"festival", "local_life"}:
        band = bump_band(band, -1)
    # Floor at low_medium per spec
    if BAND_ORDER.index(band) < BAND_ORDER.index("low_medium"):
        band = "low_medium"
    return band


def compute_resort_density_and_breadth(row: dict[str, str]) -> tuple[str, str]:
    """Return (resort_family_density, accommodation_breadth)."""

    scale = (row.get("destination_scale") or "").lower()
    location_type = (row.get("location_type") or "").lower()
    vibes = {(row.get("vibe_1") or "").lower(),
             (row.get("vibe_2") or "").lower(),
             (row.get("vibe_3") or "").lower()}

    if scale == "resort_zone" or "resort" in location_type or "resort" in vibes:
        density = "high"
        breadth = "broad"
    elif any(t in location_type for t in CITY_LOCATION_KEYWORDS) or scale in {"city", "metro_city"}:
        density = "medium"
        breadth = "broad"
    elif any(t in location_type for t in COASTAL_LOCATION_KEYWORDS + HILL_LOCATION_KEYWORDS):
        density = "medium"
        breadth = "moderate"
    elif scale in {"village", "site"}:
        density = "low"
        breadth = "narrow"
    else:
        density = "unknown"
        breadth = "moderate"
    return (density, breadth)


# ---------------------------------------------------------------------------
# Step 9 — manual-review queue assignment
# ---------------------------------------------------------------------------


def needs_suitability_review(row: dict[str, str], infant_score: int, family_band: str, senior_band: str, couple_band: str) -> tuple[bool, str]:
    """Return (needs_review, reason)."""

    reasons: list[str] = []
    seed_family = (row.get("family_suitability") or "").strip()
    if seed_family in BAND_ORDER and family_band in BAND_ORDER:
        diff = abs(BAND_ORDER.index(seed_family) - BAND_ORDER.index(family_band))
        if diff >= 2:
            reasons.append(f"seed family_suitability='{seed_family}' vs heuristic '{family_band}' (>=2 bands apart)")
    if 45 <= infant_score <= 55:
        reasons.append(f"infant_score={infant_score} at low_medium/medium boundary")
    if len({family_band, senior_band, couple_band, band_from_score(infant_score)}) == 1:
        reasons.append("all four suitability bands identical (heuristic flattening risk)")

    return (bool(reasons), "; ".join(reasons))


def needs_medical_review(medical: str, infant_score: int) -> tuple[bool, str]:
    """Return (needs_review, reason)."""

    reasons: list[str] = []
    if medical == "unknown":
        reasons.append("medical_access_confidence=unknown")
    if infant_score < 50:
        reasons.append(f"infant_score={infant_score} requires medical-access verification before treating as decision-grade")
    return (bool(reasons), "; ".join(reasons))


# ---------------------------------------------------------------------------
# Per-row pipeline orchestration
# ---------------------------------------------------------------------------


def enrich_row(row: dict[str, str], catchment: dict, pass_date: str) -> tuple[dict[str, str], dict[str, bool]]:
    """Enrich one row; return (enriched_row, review_flags)."""

    # Step 1a
    access = derive_access_complexity(row)

    # Step 1b
    cautions = derive_cautions(row, access)

    # Step 2
    ccu_fit, ccu_basis, ccu_conf, ccu_review = compute_origin_fit(row, "CCU", catchment)
    ixr_fit, ixr_basis, ixr_conf, ixr_review = compute_origin_fit(row, "IXR", catchment)

    # Step 3
    fatigue_band, fatigue_drivers, transfer_hint = compute_travel_fatigue(
        row, access, cautions, row.get("country") or "", row.get("macro_region") or ""
    )

    # Step 4
    medical, medical_basis, pediatric, medical_review = compute_medical_access(row, cautions, fatigue_drivers)

    # Step 5
    plan_band, plan_drivers, permit_hint = compute_planning_complexity(row, fatigue_drivers, cautions)

    # Step 6
    season, monsoon, heat, winter_road, altitude, weather_basis = compute_season_and_weather(row, cautions)

    # Step 7
    infant_score = compute_infant_score(row, medical, cautions, access)
    infant_band = band_from_score(infant_score)
    family_band = compute_family_band(row, access, cautions)
    senior_band = compute_senior_band(row, access, cautions, medical)
    couple_band = compute_couple_band(row, cautions)
    suitability_basis = (
        f"access={access}; medical={medical}; "
        f"cautions={','.join(sorted(set(c.replace('_check','') for c in cautions))) or 'none'}"
    )

    # Step 7b — resort/density
    resort_density, accommodation_breadth = compute_resort_density_and_breadth(row)

    # Step 9 — review flags
    suit_review, suit_reason = needs_suitability_review(row, infant_score, family_band, senior_band, couple_band)
    med_review_flag, med_reason = needs_medical_review(medical, infant_score)

    review_flags = {
        "O": ccu_review or ixr_review,
        "S": suit_review,
        "M": medical_review or med_review_flag,
    }
    review_reasons = {
        "O": f"CCU:{ccu_basis if ccu_review else 'ok'} | IXR:{ixr_basis if ixr_review else 'ok'}",
        "S": suit_reason,
        "M": medical_basis if medical_review else med_reason,
    }

    notes_parts: list[str] = []
    for batch in ("O", "S", "M"):
        if review_flags[batch]:
            notes_parts.append(f"queued_for_batch_{batch}: {review_reasons[batch]}")

    enriched = {
        "destination_master_id": row["destination_master_id"],
        "enrichment_version": ENRICHMENT_VERSION,
        "enrichment_pass_date": pass_date,
        "enrichment_method": "heuristic_v1",
        "origin_fit_ccu": ccu_fit,
        "origin_fit_ccu_basis": ccu_basis,
        "origin_fit_ccu_confidence": ccu_conf,
        "origin_fit_ixr": ixr_fit,
        "origin_fit_ixr_basis": ixr_basis,
        "origin_fit_ixr_confidence": ixr_conf,
        "infant_suitability_score": str(infant_score),
        "infant_suitability_band": infant_band,
        "family_suitability_band": family_band,
        "senior_suitability_band": senior_band,
        "couple_suitability_band": couple_band,
        "suitability_basis": suitability_basis,
        "travel_fatigue_band": fatigue_band,
        "travel_fatigue_drivers": ";".join(fatigue_drivers),
        "transfer_complexity_hint": transfer_hint,
        "planning_complexity_band": plan_band,
        "planning_complexity_drivers": ";".join(plan_drivers),
        "permit_or_visa_hint": permit_hint,
        "medical_access_confidence": medical,
        "medical_access_basis": medical_basis,
        "pediatric_access_confidence": pediatric,
        "season_window": season,
        "monsoon_caution": monsoon,
        "heat_caution": heat,
        "winter_road_caution": winter_road,
        "altitude_caution": altitude,
        "weather_basis": weather_basis,
        "resort_family_density": resort_density,
        "accommodation_breadth": accommodation_breadth,
        "derived_access_complexity": access,
        "derived_caution_tags": ";".join(cautions),
        "verification_status": "enriched_unverified",
        "planner_use_status": "needs_verification",
        "source_confidence": "low",
        "enrichment_notes": " | ".join(notes_parts),
    }

    return enriched, review_flags


# ---------------------------------------------------------------------------
# IO helpers
# ---------------------------------------------------------------------------


def write_enriched(rows: list[dict[str, str]], path: Path = ENRICHED_PATH) -> None:
    """Write enriched destination rows."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def write_queue(queue_rows: list[dict[str, str]], path: Path) -> None:
    """Write a manual-review queue CSV (destination_master_id + canonical_name + reason)."""

    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["destination_master_id", "canonical_name", "country", "state_or_area", "reason"]
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(queue_rows)


def write_report(
    enriched: list[dict[str, str]],
    queues: dict[str, list[dict[str, str]]],
    pass_date: str,
    path: Path = REPORT_PATH,
) -> None:
    """Write the enrichment report."""

    n = len(enriched)
    ccu = Counter(r["origin_fit_ccu"] for r in enriched)
    ixr = Counter(r["origin_fit_ixr"] for r in enriched)
    fatigue = Counter(r["travel_fatigue_band"] for r in enriched)
    planning = Counter(r["planning_complexity_band"] for r in enriched)
    medical = Counter(r["medical_access_confidence"] for r in enriched)
    pediatric = Counter(r["pediatric_access_confidence"] for r in enriched)
    infant_bands = Counter(r["infant_suitability_band"] for r in enriched)
    family_bands = Counter(r["family_suitability_band"] for r in enriched)
    senior_bands = Counter(r["senior_suitability_band"] for r in enriched)
    couple_bands = Counter(r["couple_suitability_band"] for r in enriched)
    verif = Counter(r["verification_status"] for r in enriched)
    planner = Counter(r["planner_use_status"] for r in enriched)
    source_conf = Counter(r["source_confidence"] for r in enriched)
    scores = [int(r["infant_suitability_score"]) for r in enriched]
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)

    def fmt_counter(c: Counter) -> str:
        return "\n".join(f"- `{k}`: {v}" for k, v in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))

    body = f"""# Evidence Report — Destinations Master v2 Enrichment (E1, v1.0)

Date: {pass_date}
Author: CodeMike
Script: `src/codemike/data/destination_master_enrichment_v1.py`
Inputs:
- `datasets/reference/destinations_master_v2.csv` ({n} rows)
- `datasets/reference/origin_catchment_v1.json`
Output:
- `datasets/reference/destinations_master_v2_enriched.csv` ({n} rows)
Manual-review queues:
- `reports/evidence/destination-master-v2-enrichment-manual-review-queues/O.csv` ({len(queues['O'])} rows)
- `reports/evidence/destination-master-v2-enrichment-manual-review-queues/S.csv` ({len(queues['S'])} rows)
- `reports/evidence/destination-master-v2-enrichment-manual-review-queues/M.csv` ({len(queues['M'])} rows)

## 1. Objective

E1 pass over the master dataset, implementing
`datasets/reference/destination_master_enrichment_strategy.md`.

This pass produces structured judgement, not source-backed truth. Every row defaults
to `verification_status = enriched_unverified` and `planner_use_status = needs_verification`.

## 2. Pipeline Status

| Step | Description | Result |
|---|---|---:|
| 0 | Read master + catchment | {n} rows read |
| 1a | Derive access_complexity for candidate rows | OK (heuristic per location_type / scale / state) |
| 1b | Derive caution tags from populated fields | OK (master had 3 tags total; derivation now populates per-row tags) |
| 2 | Compute origin_fit for CCU + IXR | OK |
| 3 | Compute travel_fatigue band + drivers | OK |
| 4 | Compute medical_access_confidence + pediatric subset | OK |
| 5 | Compute planning_complexity band + drivers + permit/visa hint | OK |
| 6 | Compute season window + weather cautions | OK |
| 7 | Compute suitability decomposed (infant score + 4 bands) | OK |
| 8 | Set verification/planner/source defaults | OK |
| 9 | Queue manual-review batches O/S/M | OK |

## 3. Origin-Fit Distribution

### CCU (Kolkata)

{fmt_counter(ccu)}

### IXR (Ranchi)

{fmt_counter(ixr)}

## 4. Travel-Fatigue Distribution

{fmt_counter(fatigue)}

## 5. Planning-Complexity Distribution

{fmt_counter(planning)}

## 6. Medical-Access Distribution

### medical_access_confidence

{fmt_counter(medical)}

### pediatric_access_confidence

{fmt_counter(pediatric)}

## 7. Suitability Distributions

### infant_suitability_score

- min: {min_score}
- max: {max_score}
- mean (1 dp): {avg_score:.1f}

### infant_suitability_band

{fmt_counter(infant_bands)}

### family_suitability_band

{fmt_counter(family_bands)}

### senior_suitability_band

{fmt_counter(senior_bands)}

### couple_suitability_band

{fmt_counter(couple_bands)}

## 8. Verification / Planner Status (post-E1)

### verification_status

{fmt_counter(verif)}

### planner_use_status

{fmt_counter(planner)}

### source_confidence

{fmt_counter(source_conf)}

## 9. Manual-Review Queue Sizes

| Batch | Description | Rows queued |
|---|---|---:|
| O | Origin fit (heuristic unknown) | {len(queues['O'])} |
| S | Suitability (seed-vs-heuristic disagreement, boundary score, or band flattening) | {len(queues['S'])} |
| M | Medical access (unknown OR infant_score < 50) | {len(queues['M'])} |

Each queue is a CSV with destination_master_id + canonical_name + country + state + reason.

## 10. Honest Limitations

- All rows are at `source_confidence = low` — the heuristic produces structured judgement, not source-backed truth.
- The medical-access heuristic uses destination-scale as a proxy for actual medical-care availability; strategy doc §8.3 names this as the weakest formula in v1.
- caution_tags + context_tags were sparse in the master input (3 + 17 total tags across 359 rows); the script derives cautions from location_type / state_or_area / macro_region / destination_scale / vibes. This is consistent with the schema doc's note that caution_tags are heuristic-generated.
- Origin catchment tables (`origin_catchment_v1.json`) are workspace judgement, not verified flight/train data.
- No row crosses to `planner_ready` in this pass. Promotion to planner_ready is the separately-defined E3 step (strategy doc §12.4), out of scope for v1 enrichment.
- Real-user evaluation of enrichment quality is not part of this pass. Lab 05 F-PRIN-1 (Principle 2: Users involved throughout) applies; the Sponsor Reviewer cycle (NEXT_ACTIONS priority 9) should test heuristic outputs against a real planner's judgement.

## 11. Next Actions

1. Run `src/codemike/data/destination_master_enrichment_validation.py` to validate the enriched CSV structurally.
2. Schedule manual-review sessions O / S / M per strategy doc §11.1 + §12.3 (caps 30 / 25 / 20 rows per session).
3. After E2 manual-review sessions complete, NEXT_ACTIONS priority 6 (scoring v1) unblocks against a stable enriched layer.
"""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the E1 enrichment pass end-to-end."""

    catchment = load_catchment()
    master_rows = read_master()
    pass_date = date.today().isoformat()

    enriched_rows: list[dict[str, str]] = []
    queues: dict[str, list[dict[str, str]]] = {"O": [], "S": [], "M": []}

    for row in master_rows:
        enriched, flags = enrich_row(row, catchment, pass_date)
        enriched_rows.append(enriched)

        for batch in ("O", "S", "M"):
            if flags[batch]:
                # Extract the per-batch reason from enrichment_notes
                reason = ""
                for chunk in enriched["enrichment_notes"].split(" | "):
                    if chunk.startswith(f"queued_for_batch_{batch}: "):
                        reason = chunk[len(f"queued_for_batch_{batch}: "):]
                        break
                queues[batch].append({
                    "destination_master_id": row["destination_master_id"],
                    "canonical_name": row["canonical_name"],
                    "country": row["country"],
                    "state_or_area": row["state_or_area"],
                    "reason": reason,
                })

    write_enriched(enriched_rows)
    write_queue(queues["O"], QUEUE_O_PATH)
    write_queue(queues["S"], QUEUE_S_PATH)
    write_queue(queues["M"], QUEUE_M_PATH)
    write_report(enriched_rows, queues, pass_date)

    print(f"E1 enrichment complete.")
    print(f"  rows enriched : {len(enriched_rows)}")
    print(f"  output        : {ENRICHED_PATH}")
    print(f"  queue O (origin)     : {len(queues['O'])} rows -> {QUEUE_O_PATH}")
    print(f"  queue S (suitability): {len(queues['S'])} rows -> {QUEUE_S_PATH}")
    print(f"  queue M (medical)    : {len(queues['M'])} rows -> {QUEUE_M_PATH}")
    print(f"  report        : {REPORT_PATH}")


if __name__ == "__main__":
    main()
