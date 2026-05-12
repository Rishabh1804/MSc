"""Destination database QA and enrichment utilities.

This module enriches the seed destination database with Planner-oriented fields.

Status:
    Heuristic prototype. Values are useful for prototyping and filtering, not
    for live travel decisions.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


SEED_PATH = Path("datasets/reference/india_region_destinations_seed.csv")
OUTPUT_PATH = Path("datasets/reference/india_region_destinations_enriched_v1.csv")


NEAR_INDIA_COUNTRIES = {"Nepal", "Bhutan", "Sri Lanka"}
INDIAN_OCEAN_COUNTRIES = {"Maldives", "Mauritius", "Seychelles"}
SE_ASIA_COUNTRIES = {"Thailand", "Singapore", "Malaysia", "Indonesia", "Vietnam", "Cambodia", "Laos"}
MIDDLE_EAST_COUNTRIES = {"United Arab Emirates", "Qatar", "Oman"}
EXTENDED_REGION_COUNTRIES = {"Azerbaijan", "Georgia", "Armenia", "Kazakhstan", "Uzbekistan"}


DOMESTIC_NEAR_EAST_REGIONS = {"East India", "North East India"}
DOMESTIC_MODERATE_REGIONS = {"North India", "Central India"}
DOMESTIC_FAR_REGIONS = {"West India", "South India", "Island India"}


AIRPORT_HINTS_BY_NAME = {
    "Delhi NCR": "Delhi DEL",
    "Agra": "Delhi DEL / Agra AGR",
    "Jaipur": "Jaipur JAI",
    "Udaipur": "Udaipur UDR",
    "Jodhpur": "Jodhpur JDH",
    "Jaisalmer": "Jaisalmer JSA",
    "Amritsar": "Amritsar ATQ",
    "Chandigarh": "Chandigarh IXC",
    "Mumbai": "Mumbai BOM",
    "Pune": "Pune PNQ",
    "Goa": "Goa GOI/GOX",
    "Ahmedabad": "Ahmedabad AMD",
    "Bengaluru": "Bengaluru BLR",
    "Hyderabad": "Hyderabad HYD",
    "Chennai": "Chennai MAA",
    "Kochi": "Kochi COK",
    "Kolkata": "Kolkata CCU",
    "Bhubaneswar": "Bhubaneswar BBI",
    "Visakhapatnam": "Visakhapatnam VTZ",
    "Guwahati": "Guwahati GAU",
    "Port Blair": "Port Blair IXZ",
    "Kathmandu": "Kathmandu KTM",
    "Pokhara": "Pokhara PKR",
    "Thimphu": "Paro PBH",
    "Paro": "Paro PBH",
    "Colombo": "Colombo CMB",
    "Maldives Resort Islands": "Male MLE + seaplane/speedboat",
    "Maafushi": "Male MLE + speedboat",
    "Mauritius": "Mauritius MRU",
    "Seychelles": "Seychelles SEZ",
    "Dubai": "Dubai DXB",
    "Abu Dhabi": "Abu Dhabi AUH",
    "Doha": "Doha DOH",
    "Muscat": "Muscat MCT",
    "Bangkok": "Bangkok BKK/DMK",
    "Phuket": "Phuket HKT",
    "Krabi": "Krabi KBV",
    "Koh Samui": "Koh Samui USM",
    "Singapore": "Singapore SIN",
    "Sentosa": "Singapore SIN",
    "Kuala Lumpur": "Kuala Lumpur KUL",
    "Langkawi": "Langkawi LGK",
    "Penang": "Penang PEN",
    "Bali": "Denpasar DPS",
    "Ubud": "Denpasar DPS + road transfer",
    "Hanoi": "Hanoi HAN",
    "Ho Chi Minh City": "Ho Chi Minh SGN",
    "Da Nang": "Da Nang DAD",
    "Hoi An": "Da Nang DAD + road transfer",
    "Siem Reap": "Siem Reap SAI",
    "Baku": "Baku GYD",
    "Tbilisi": "Tbilisi TBS",
    "Yerevan": "Yerevan EVN",
    "Almaty": "Almaty ALA",
    "Tashkent": "Tashkent TAS",
    "Samarkand": "Samarkand SKD",
}


def read_rows(path: Path = SEED_PATH) -> list[dict[str, str]]:
    """Read destination seed rows."""

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def write_rows(rows: Iterable[dict[str, str]], path: Path = OUTPUT_PATH) -> None:
    """Write enriched destination rows."""

    rows = list(rows)
    if not rows:
        raise ValueError("no rows to write")

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def origin_fit_ccu(row: dict[str, str]) -> str:
    """Rough origin fit from Kolkata (CCU)."""

    country = row["country"]
    region = row["macro_region"]

    if country == "India" and region in DOMESTIC_NEAR_EAST_REGIONS:
        return "strong"
    if country == "India" and region in DOMESTIC_MODERATE_REGIONS:
        return "moderate"
    if country in NEAR_INDIA_COUNTRIES or country in SE_ASIA_COUNTRIES:
        return "moderate"
    if country == "India" and region in DOMESTIC_FAR_REGIONS:
        return "moderate"
    if country in MIDDLE_EAST_COUNTRIES or country in INDIAN_OCEAN_COUNTRIES:
        return "moderate"
    return "weak"


def origin_fit_ixr(row: dict[str, str]) -> str:
    """Rough origin fit from Ranchi (IXR)."""

    country = row["country"]
    region = row["macro_region"]

    if country == "India" and region in {"East India", "Central India", "North India"}:
        return "strong"
    if country == "India" and region in {"West India", "South India", "North East India"}:
        return "moderate"
    if country in NEAR_INDIA_COUNTRIES:
        return "moderate"
    if country in SE_ASIA_COUNTRIES or country in MIDDLE_EAST_COUNTRIES:
        return "weak"
    return "weak"


def passport_or_permit_hint(row: dict[str, str]) -> str:
    """Return broad document/permit hint. Not legal advice."""

    country = row["country"]
    state_area = row["state_or_area"]
    if country == "India":
        if state_area in {"Ladakh", "Jammu and Kashmir", "Sikkim", "Arunachal Pradesh", "Andaman and Nicobar", "Lakshadweep"}:
            return "domestic_with_possible_permit_or_local_rules_check"
        return "domestic"
    if country in NEAR_INDIA_COUNTRIES:
        return "passport_or_regional_entry_rules_check"
    return "passport_and_visa_rules_check"


def fatigue_band(row: dict[str, str]) -> str:
    """Estimate broad travel fatigue from origin complexity and destination type."""

    country = row["country"]
    access = row["access_complexity"]
    location_type = row["location_type"]
    region = row["macro_region"]

    if access == "hard" or "island" in location_type or region in {"Central Asia", "Caucasus"}:
        return "very_high"
    if country != "India" and country not in NEAR_INDIA_COUNTRIES:
        return "high"
    if access == "moderate":
        return "medium"
    return "low"


def planning_complexity(row: dict[str, str]) -> str:
    """Estimate planning complexity from access, documents, and destination type."""

    access = row["access_complexity"]
    document_hint = passport_or_permit_hint(row)
    location_type = row["location_type"]

    if access == "hard" or "permit" in document_hint or "island" in location_type:
        return "high"
    if access == "moderate" or "visa" in document_hint or "passport" in document_hint:
        return "medium"
    return "low"


def infant_suitability_score(row: dict[str, str]) -> int:
    """Return a conservative initial infant/family suitability proxy."""

    family = row["family_suitability"]
    access = row["access_complexity"]
    budget = row["budget_band"]
    location_type = row["location_type"]

    base = {
        "high": 82,
        "medium": 65,
        "low_medium": 52,
        "low": 35,
    }.get(family, 55)

    if access == "hard":
        base -= 18
    elif access == "moderate":
        base -= 7

    if "high_altitude" in location_type:
        base -= 20
    if "wildlife" in location_type:
        base -= 8
    if "island" in location_type and access != "easy":
        base -= 8
    if budget == "premium":
        base += 3

    return max(10, min(95, base))


def weather_caution(row: dict[str, str]) -> str:
    """Return broad weather caution tags."""

    destination_type = row["location_type"]
    vibe_values = {row["vibe_1"], row["vibe_2"], row["vibe_3"]}
    season = row["best_season_hint"].lower()

    cautions: list[str] = []
    if "beach" in destination_type or "island" in destination_type or "coast" in vibe_values:
        cautions.append("monsoon_check")
    if "hill" in destination_type or "mountain" in destination_type or "snow" in vibe_values:
        cautions.append("winter_road_weather_check")
    if "desert" in destination_type or "desert" in vibe_values:
        cautions.append("heat_check")
    if "jun-sep" in season or "rain" in vibe_values or "monsoon" in vibe_values:
        cautions.append("rainfall_season_check")

    return ";".join(sorted(set(cautions))) if cautions else "standard_season_check"


def medical_access_confidence(row: dict[str, str]) -> str:
    """Estimate medical access confidence."""

    location_type = row["location_type"]
    access = row["access_complexity"]

    if access == "easy" and any(token in location_type for token in ["city", "metro", "global"]):
        return "high"
    if access == "hard" or "island" in location_type or "wildlife" in location_type or "high_altitude" in location_type:
        return "low"
    return "medium"


def resort_family_density(row: dict[str, str]) -> str:
    """Estimate resort/family stay density."""

    location_type = row["location_type"]
    vibes = {row["vibe_1"], row["vibe_2"], row["vibe_3"]}
    if "resort" in location_type or "resort" in vibes or "family" in vibes or "beach" in vibes:
        return "high"
    if "city" in location_type or "heritage" in location_type or "hill" in location_type:
        return "medium"
    return "low"


def nearest_airport_hint(row: dict[str, str]) -> str:
    """Return known airport hint or fallback to destination/country gateway."""

    name = row["name"]
    if name in AIRPORT_HINTS_BY_NAME:
        return AIRPORT_HINTS_BY_NAME[name]
    if row["country"] == "India":
        return "nearest_regional_airport_to_verify"
    return "primary_international_gateway_to_verify"


def enrich_row(row: dict[str, str]) -> dict[str, str]:
    """Return one enriched destination row."""

    enriched = dict(row)
    enriched["nearest_airport_hint"] = nearest_airport_hint(row)
    enriched["origin_fit_ccu"] = origin_fit_ccu(row)
    enriched["origin_fit_ixr"] = origin_fit_ixr(row)
    enriched["origin_fit_notes"] = "heuristic_origin_fit_requires_route_verification"
    enriched["passport_or_permit_hint"] = passport_or_permit_hint(row)
    enriched["infant_suitability_score"] = str(infant_suitability_score(row))
    enriched["travel_fatigue_band"] = fatigue_band(row)
    enriched["planning_complexity_band"] = planning_complexity(row)
    enriched["monsoon_or_weather_caution"] = weather_caution(row)
    enriched["medical_access_confidence"] = medical_access_confidence(row)
    enriched["resort_family_density"] = resort_family_density(row)
    enriched["planner_use_status"] = "needs_verification"
    return enriched


def enrich_rows(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    """Enrich multiple destination rows."""

    return [enrich_row(row) for row in rows]


def validate_seed_rows(rows: list[dict[str, str]]) -> dict[str, object]:
    """Return basic QA results for the seed dataset."""

    ids = [row["destination_id"] for row in rows]
    name_country_pairs = [(row["name"], row["country"]) for row in rows]

    return {
        "row_count": len(rows),
        "unique_destination_ids": len(set(ids)),
        "duplicate_destination_ids": sorted({item for item in ids if ids.count(item) > 1}),
        "unique_name_country_pairs": len(set(name_country_pairs)),
        "duplicate_name_country_pairs": sorted({item for item in name_country_pairs if name_country_pairs.count(item) > 1}),
        "macro_regions": sorted({row["macro_region"] for row in rows}),
        "countries": sorted({row["country"] for row in rows}),
    }


def main() -> None:
    """Generate enriched destination database."""

    rows = read_rows()
    qa = validate_seed_rows(rows)
    enriched = enrich_rows(rows)
    write_rows(enriched)

    print("Destination seed QA:")
    for key, value in qa.items():
        print(f"- {key}: {value}")
    print(f"Wrote {len(enriched)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
