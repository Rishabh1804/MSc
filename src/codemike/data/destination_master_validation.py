"""Validate destinations_master_v2.csv against the master schema.

Input:
    datasets/reference/destinations_master_v2.csv

Output:
    reports/evidence/destination-master-v2-validation-report.md

This validator checks structural integrity only. It does not verify live travel
facts such as routes, permits, visa rules, safety, weather, or medical access.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


MASTER_PATH = Path("datasets/reference/destinations_master_v2.csv")
REPORT_PATH = Path("reports/evidence/destination-master-v2-validation-report.md")
EXPECTED_ROW_COUNT = 359

REQUIRED_COLUMNS = [
    "destination_master_id",
    "source_layer",
    "source_id",
    "source_file",
    "canonical_name",
    "alias_names",
    "country",
    "macro_region",
    "state_or_area",
    "district_or_area",
    "destination_scale",
    "location_type",
    "vibe_1",
    "vibe_2",
    "vibe_3",
    "trip_style_tags",
    "context_tags",
    "caution_tags",
    "budget_band",
    "family_suitability",
    "access_complexity",
    "best_season_hint",
    "verification_status",
    "promotion_status",
    "planner_use_status",
    "source_confidence",
    "source_notes",
    "normalisation_notes",
    "master_notes",
]

VALID_SOURCE_LAYERS = {"seed", "normalized_candidate"}
VALID_DESTINATION_SCALES = {
    "city", "town", "village", "district", "region", "circuit", "site", "park",
    "island", "resort_zone", "route", "unknown",
}
VALID_VERIFICATION_STATUSES = {
    "candidate", "seed_unverified", "enriched_unverified", "source_verified", "planner_ready", "retired",
}
VALID_PROMOTION_STATUSES = {
    "candidate", "qa_pending", "dedupe_pending", "enrichment_pending", "source_pending",
    "review_ready", "planner_candidate", "planner_ready", "retired",
}
VALID_PLANNER_USE_STATUSES = {
    "candidate", "needs_verification", "transfer_candidate", "planner_ready", "retired",
}
VALID_SOURCE_CONFIDENCE = {"none", "low", "medium", "high", "official"}

CRITICAL_NON_BLANK_COLUMNS = [
    "destination_master_id",
    "source_layer",
    "source_id",
    "source_file",
    "canonical_name",
    "country",
    "macro_region",
    "state_or_area",
    "destination_scale",
    "location_type",
    "verification_status",
    "promotion_status",
    "planner_use_status",
    "source_confidence",
]


VALID_DESTINATION_TYPES = {
    "metro_city", "city", "global_city", "capital_city", "heritage_city", "culture_city", "culture_town",
    "spiritual_city", "temple_city", "pilgrim_city", "planned_city", "coastal_city", "beach_city",
    "hill_city", "hill_heritage_city", "mountain_city", "mountain_capital", "lake_mountain_city", "gateway_city", "city_gateway",
    "northern_city", "business_city", "education_city", "food_city", "craft_city", "heritage_capital",
    "lake_heritage_city", "desert_town",
    "hill_station", "lake_hill_station", "hill_town", "culture_hill_town", "hill_region", "mountain_town", "mountain_region", "mountain_resort",
    "mountain_valley", "high_altitude", "valley", "lake_city", "lake_region", "lake_valley", "river_town", "river_region", "river_spiritual_town",
    "waterfall_site", "canyon_region", "desert_region", "forest_region", "rainforest_region",
    "meadow_region", "plateau_region", "tea_region", "coffee_region", "spice_region", "hill_valley",
    "beach_town", "beach_resort", "beach_region", "beach_state", "coastal_town", "coastal_city",
    "coastal_region", "coastal_capital", "coastal_heritage_city", "coastal_heritage_town", "metro_coastal_city", "desert_beach_emirate",
    "island_gateway", "island_beach", "island_region", "island_resort", "island_resort_district", "island_heritage_city", "local_island", "river_island", "marine_region",
    "wildlife_reserve", "wildlife_region", "national_park", "tiger_reserve", "birding_site",
    "mangrove_wildlife_region", "forest_reserve", "biosphere_reserve", "wetland_site", "wildlife_hill_region",
    "heritage_site", "heritage_town", "heritage_gateway", "heritage_region", "fort_town",
    "fort_site", "palace_city", "palace_site", "archaeological_site", "cave_heritage_site",
    "rock_carving_site", "craft_village", "museum_district", "old_quarter", "wine_heritage_city",
    "pilgrim_town", "pilgrim_region", "pilgrim_coastal_town", "pilgrim_beach_town", "monastery_town",
    "monastery_region", "spiritual_retreat", "buddhist_site", "jain_site",
    "sikh_pilgrimage_site", "char_dham_site", "temple_cluster",
    "resort_town", "resort_region", "backwater_region", "backwater_resort", "wellness_region",
    "wine_region", "tea_resort_region", "coffee_resort_region", "theme_park_zone", "shopping_district",
    "city_valley",
}

VALID_VIBES = {
    "heritage", "culture", "food", "shopping", "urban", "city", "architecture", "history",
    "spiritual", "pilgrimage", "slow_travel", "family", "luxury", "budget", "wellness",
    "romantic", "relaxation", "nightlife", "business", "education", "art", "craft", "music", "festival",
    "photography", "viewpoint", "local_life", "museums", "stopover", "hills", "mountains", "valley", "lakes",
    "river", "waterfalls", "forest", "rainforest", "rain", "monsoon", "desert", "snow", "tea", "coffee",
    "spice", "backwaters", "gardens", "meadows", "caves", "limestone", "mangrove", "wetland",
    "birding", "flowers", "landscape", "sunrise", "sunset", "beach", "coast", "islands",
    "marine", "diving", "snorkelling", "water", "resort", "villa", "lagoon", "coral", "cruise",
    "houseboat", "adventure", "trekking", "safari", "ski", "rafting", "paragliding",
    "camping", "road_trip", "cycling", "boating", "theme_parks", "water_sports",
    "desert_safari", "buddhist", "jain", "sikh", "monastery", "temples", "temple", "forts", "palace", "rock_carving", "wine",
    "textiles", "handicrafts", "wildlife", "tiger", "rhino", "elephant", "marine_life",
    "colonial", "french_quarter", "silk_route", "nature", "gateway", "weekend", "strawberries", "views", "lake",
}
VALID_TRIP_STYLE_TAGS = {
    "weekend_getaway", "long_weekend", "short_break", "slow_trip", "luxury_escape",
    "budget_escape", "family_vacation", "pilgrimage_trip", "wildlife_trip", "heritage_circuit",
    "beach_holiday", "hill_retreat", "food_trip", "shopping_trip", "wellness_retreat",
    "adventure_trip", "road_trip", "honeymoon_style", "offbeat_trip", "monsoon_trip",
    "winter_trip", "summer_escape",
}
VALID_CONTEXT_TAGS = {"gateway_context", "remote_context", "border_context"}
VALID_CAUTION_TAGS = {
    "monsoon_check", "heat_check", "winter_road_weather_check", "rainfall_season_check",
    "cyclone_check", "flooding_check", "fog_delay_check", "humidity_check", "snow_closure_check",
    "altitude_check", "motion_sickness_check", "long_road_transfer_check", "medical_access_check",
    "mobility_access_check", "infant_food_access_check", "elderly_travel_check", "permit_check",
    "passport_check", "visa_rules_check", "local_transport_check", "route_verification_check",
    "flight_schedule_check", "ferry_schedule_check", "seasonal_closure_check", "crowd_check",
    "festival_crowd_check", "safety_check", "border_area_check",
}


def read_rows(path: Path = MASTER_PATH) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def split_tags(value: str) -> list[str]:
    if not value:
        return []
    return [tag.strip() for tag in value.split(";") if tag.strip()]


def normalized_key(value: str) -> str:
    return " ".join(value.strip().lower().split())


def duplicate_values(values: Iterable[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def invalid_scalar_map(rows: list[dict[str, str]], field: str, valid_values: set[str]) -> dict[str, list[str]]:
    invalid: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        value = row.get(field, "")
        if value not in valid_values:
            invalid[value].append(row["destination_master_id"])
    return dict(sorted(invalid.items()))


def invalid_tag_map(rows: list[dict[str, str]], fields: list[str], valid_values: set[str]) -> dict[str, list[str]]:
    invalid: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        for field in fields:
            for tag in split_tags(row.get(field, "")):
                if tag not in valid_values:
                    invalid[tag].append(row["destination_master_id"])
    return dict(sorted(invalid.items()))


def blank_critical_map(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    blank: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        for column in CRITICAL_NON_BLANK_COLUMNS:
            if not row.get(column, "").strip():
                blank[column].append(row.get("destination_master_id", "unknown"))
    return dict(sorted(blank.items()))


def validate(rows: list[dict[str, str]]) -> dict[str, object]:
    if not rows:
        raise ValueError("master dataset is empty")

    columns = set(rows[0].keys())
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in columns]
    extra_columns = [column for column in rows[0].keys() if column not in REQUIRED_COLUMNS]

    master_ids = [row["destination_master_id"] for row in rows]
    lineage_keys = [f"{row['source_layer']}|{row['source_id']}" for row in rows]
    name_country_keys = [f"{normalized_key(row['canonical_name'])}|{normalized_key(row['country'])}" for row in rows]
    name_state_keys = [f"{normalized_key(row['canonical_name'])}|{normalized_key(row['state_or_area'])}" for row in rows]

    return {
        "row_count": len(rows),
        "expected_row_count": EXPECTED_ROW_COUNT,
        "missing_columns": missing_columns,
        "extra_columns": extra_columns,
        "duplicate_master_ids": duplicate_values(master_ids),
        "duplicate_lineage_keys": duplicate_values(lineage_keys),
        "duplicate_name_country_keys": duplicate_values(name_country_keys),
        "duplicate_name_state_keys": duplicate_values(name_state_keys),
        "blank_critical_fields": blank_critical_map(rows),
        "invalid_source_layers": invalid_scalar_map(rows, "source_layer", VALID_SOURCE_LAYERS),
        "invalid_destination_scales": invalid_scalar_map(rows, "destination_scale", VALID_DESTINATION_SCALES),
        "invalid_location_types": invalid_scalar_map(rows, "location_type", VALID_DESTINATION_TYPES),
        "invalid_vibes": invalid_tag_map(rows, ["vibe_1", "vibe_2", "vibe_3"], VALID_VIBES),
        "invalid_trip_style_tags": invalid_tag_map(rows, ["trip_style_tags"], VALID_TRIP_STYLE_TAGS),
        "invalid_context_tags": invalid_tag_map(rows, ["context_tags"], VALID_CONTEXT_TAGS),
        "invalid_caution_tags": invalid_tag_map(rows, ["caution_tags"], VALID_CAUTION_TAGS),
        "invalid_verification_statuses": invalid_scalar_map(rows, "verification_status", VALID_VERIFICATION_STATUSES),
        "invalid_promotion_statuses": invalid_scalar_map(rows, "promotion_status", VALID_PROMOTION_STATUSES),
        "invalid_planner_use_statuses": invalid_scalar_map(rows, "planner_use_status", VALID_PLANNER_USE_STATUSES),
        "invalid_source_confidence": invalid_scalar_map(rows, "source_confidence", VALID_SOURCE_CONFIDENCE),
        "source_layer_counts": dict(sorted(Counter(row["source_layer"] for row in rows).items())),
        "verification_status_counts": dict(sorted(Counter(row["verification_status"] for row in rows).items())),
        "promotion_status_counts": dict(sorted(Counter(row["promotion_status"] for row in rows).items())),
        "planner_use_status_counts": dict(sorted(Counter(row["planner_use_status"] for row in rows).items())),
        "destination_scale_counts": dict(sorted(Counter(row["destination_scale"] for row in rows).items())),
    }


def format_mapping(mapping: dict[str, object]) -> str:
    if not mapping:
        return "- None\n"
    return "".join(f"- `{key}`: {value}\n" for key, value in mapping.items())


def is_clean(result: dict[str, object]) -> bool:
    return (
        result["row_count"] == result["expected_row_count"]
        and not result["missing_columns"]
        and not result["extra_columns"]
        and not result["duplicate_master_ids"]
        and not result["duplicate_lineage_keys"]
        and not result["duplicate_name_country_keys"]
        and not result["duplicate_name_state_keys"]
        and not result["blank_critical_fields"]
        and not result["invalid_source_layers"]
        and not result["invalid_destination_scales"]
        and not result["invalid_location_types"]
        and not result["invalid_vibes"]
        and not result["invalid_trip_style_tags"]
        and not result["invalid_context_tags"]
        and not result["invalid_caution_tags"]
        and not result["invalid_verification_statuses"]
        and not result["invalid_promotion_statuses"]
        and not result["invalid_planner_use_statuses"]
        and not result["invalid_source_confidence"]
    )


def write_report(result: dict[str, object], path: Path = REPORT_PATH) -> None:
    readiness = "master_structurally_valid_not_planner_ready" if is_clean(result) else "master_needs_structural_cleanup"

    content = f"""# Evidence Report — Destinations Master v2 Validation

Date: 2026-05-12  
Author: CodeMike  
Dataset: `datasets/reference/destinations_master_v2.csv`  
Validator: `src/codemike/data/destination_master_validation.py`

## 1. Objective

Validate `destinations_master_v2.csv` against the master v2 schema before creating a browser or downstream scoring layer.

This validation checks structural integrity only. It does not verify live travel facts.

## 2. Validation Summary

| Check | Result |
|---|---:|
| Rows checked | {result['row_count']} |
| Expected rows | {result['expected_row_count']} |
| Missing required columns | {len(result['missing_columns'])} |
| Extra columns | {len(result['extra_columns'])} |
| Duplicate master IDs | {len(result['duplicate_master_ids'])} |
| Duplicate lineage keys | {len(result['duplicate_lineage_keys'])} |
| Duplicate name-country keys | {len(result['duplicate_name_country_keys'])} |
| Duplicate name-state keys | {len(result['duplicate_name_state_keys'])} |
| Critical fields with blanks | {len(result['blank_critical_fields'])} |
| Invalid source layers | {len(result['invalid_source_layers'])} |
| Invalid destination scales | {len(result['invalid_destination_scales'])} |
| Invalid location types | {len(result['invalid_location_types'])} |
| Invalid vibe tags | {len(result['invalid_vibes'])} |
| Invalid trip-style tags | {len(result['invalid_trip_style_tags'])} |
| Invalid context tags | {len(result['invalid_context_tags'])} |
| Invalid caution tags | {len(result['invalid_caution_tags'])} |
| Invalid verification statuses | {len(result['invalid_verification_statuses'])} |
| Invalid promotion statuses | {len(result['invalid_promotion_statuses'])} |
| Invalid planner-use statuses | {len(result['invalid_planner_use_statuses'])} |
| Invalid source-confidence values | {len(result['invalid_source_confidence'])} |

Readiness:

```text
{readiness}
```

## 3. Source Layer Counts

{format_mapping(result['source_layer_counts'])}

## 4. Verification Status Counts

{format_mapping(result['verification_status_counts'])}

## 5. Promotion Status Counts

{format_mapping(result['promotion_status_counts'])}

## 6. Planner Use Status Counts

{format_mapping(result['planner_use_status_counts'])}

## 7. Destination Scale Counts

{format_mapping(result['destination_scale_counts'])}

## 8. Invalid Location Types

{format_mapping(result['invalid_location_types'])}

## 9. Invalid Vibe Tags

{format_mapping(result['invalid_vibes'])}

## 10. Duplicate Name-Country Keys

{format_mapping({key: 'duplicate' for key in result['duplicate_name_country_keys']})}

## 11. Duplicate Name-State Keys

{format_mapping({key: 'duplicate' for key in result['duplicate_name_state_keys']})}

## 12. Critical Blank Fields

{format_mapping(result['blank_critical_fields'])}

## 13. Interpretation

If readiness is `master_structurally_valid_not_planner_ready`, the dataset is ready for a master HTML browser and enrichment planning.

It is still not Planner-ready because live travel facts and source verification have not been completed.

## 14. Next Actions

1. Fix any structural issues found by this report.
2. Create `docs/destination-master-browser-v1.html` after validation is clean.
3. Add a master browser link to `docs/index.html`.
4. Begin enrichment fields only after the master layer is structurally clean.
"""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    rows = read_rows()
    result = validate(rows)
    write_report(result)

    print(f"Rows checked: {result['row_count']}")
    print(f"Expected rows: {result['expected_row_count']}")
    print(f"Missing columns: {len(result['missing_columns'])}")
    print(f"Extra columns: {len(result['extra_columns'])}")
    print(f"Duplicate master IDs: {len(result['duplicate_master_ids'])}")
    print(f"Duplicate lineage keys: {len(result['duplicate_lineage_keys'])}")
    print(f"Invalid location types: {len(result['invalid_location_types'])}")
    print(f"Invalid vibe tags: {len(result['invalid_vibes'])}")
    print(f"Readiness: {'master_structurally_valid_not_planner_ready' if is_clean(result) else 'master_needs_structural_cleanup'}")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
