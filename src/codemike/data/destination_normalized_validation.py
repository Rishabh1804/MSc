"""Validate the normalised India destination backlog.

This validator checks the normalised output produced by
`destination_backlog_normalization.py` before rows are promoted into
`destinations_master_v2.csv`.

Input:
    datasets/reference/destination_expansion_backlog_india_v1_normalized.csv

Output report:
    reports/evidence/destination-normalized-backlog-validation-v1.md

Status:
    Prototype validation utility for destination database v2.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


INPUT_PATH = Path("datasets/reference/destination_expansion_backlog_india_v1_normalized.csv")
REPORT_PATH = Path("reports/evidence/destination-normalized-backlog-validation-v1.md")


VALID_DESTINATION_TYPES = {
    "metro_city", "city", "global_city", "capital_city", "heritage_city", "culture_city", "culture_town",
    "spiritual_city", "temple_city", "pilgrim_city", "planned_city", "coastal_city",
    "hill_city", "mountain_city", "gateway_city", "city_gateway", "business_city",
    "education_city", "food_city", "craft_city",
    "hill_station", "lake_hill_station", "hill_town", "hill_region", "mountain_town", "mountain_region", "mountain_resort",
    "high_altitude", "valley", "lake_city", "lake_region", "river_town", "river_region",
    "waterfall_site", "canyon_region", "desert_region", "forest_region", "rainforest_region",
    "meadow_region", "plateau_region", "tea_region", "coffee_region", "spice_region",
    "beach_town", "beach_resort", "beach_region", "beach_state", "coastal_town",
    "coastal_region", "coastal_capital", "island_gateway", "island_beach", "island_region",
    "island_resort", "local_island", "river_island", "marine_region",
    "wildlife_reserve", "national_park", "tiger_reserve", "birding_site",
    "mangrove_wildlife_region", "forest_reserve", "biosphere_reserve", "wetland_site",
    "heritage_site", "heritage_town", "heritage_gateway", "heritage_region", "fort_town",
    "fort_site", "palace_city", "palace_site", "archaeological_site", "cave_heritage_site",
    "rock_carving_site", "craft_village", "museum_district", "old_quarter",
    "pilgrim_town", "pilgrim_region", "pilgrim_coastal_town", "monastery_town",
    "monastery_region", "spiritual_retreat", "buddhist_site", "jain_site",
    "sikh_pilgrimage_site", "char_dham_site", "temple_cluster",
    "resort_town", "resort_region", "backwater_region", "backwater_resort", "wellness_region",
    "wine_region", "tea_resort_region", "coffee_resort_region", "theme_park_zone",
    "shopping_district",
}


VALID_VIBES = {
    "heritage", "culture", "food", "shopping", "urban", "architecture", "history",
    "spiritual", "pilgrimage", "slow_travel", "family", "luxury", "budget", "wellness",
    "romantic", "nightlife", "business", "education", "art", "craft", "music", "festival",
    "photography", "viewpoint", "local_life", "hills", "mountains", "valley", "lakes",
    "river", "waterfalls", "forest", "rainforest", "rain", "desert", "snow", "tea", "coffee",
    "spice", "backwaters", "gardens", "meadows", "caves", "mangrove", "wetland",
    "birding", "flowers", "landscape", "sunrise", "sunset", "beach", "coast", "islands",
    "marine", "diving", "snorkelling", "water", "resort", "lagoon", "coral", "cruise",
    "houseboat", "adventure", "trekking", "safari", "ski", "rafting", "paragliding",
    "camping", "road_trip", "cycling", "boating", "theme_parks", "water_sports",
    "desert_safari", "buddhist", "jain", "sikh", "monastery", "temples", "forts", "palace", "rock_carving", "wine",
    "textiles", "handicrafts", "wildlife", "tiger", "rhino", "elephant", "marine_life",
    "colonial", "french_quarter", "silk_route", "nature",
}


VALID_TRIP_STYLE_TAGS = {
    "weekend_getaway", "long_weekend", "short_break", "slow_trip", "luxury_escape",
    "budget_escape", "family_vacation", "pilgrimage_trip", "wildlife_trip", "heritage_circuit",
    "beach_holiday", "hill_retreat", "food_trip", "shopping_trip", "wellness_retreat",
    "adventure_trip", "road_trip", "honeymoon_style", "offbeat_trip", "monsoon_trip",
    "winter_trip", "summer_escape",
}


VALID_CONTEXT_TAGS = {
    "gateway_context", "remote_context", "border_context",
}


VALID_CAUTION_TAGS = {
    "monsoon_check", "heat_check", "winter_road_weather_check", "rainfall_season_check",
    "cyclone_check", "flooding_check", "fog_delay_check", "humidity_check", "snow_closure_check",
    "altitude_check", "motion_sickness_check", "long_road_transfer_check", "medical_access_check",
    "mobility_access_check", "infant_food_access_check", "elderly_travel_check", "permit_check",
    "passport_check", "visa_rules_check", "local_transport_check", "route_verification_check",
    "flight_schedule_check", "ferry_schedule_check", "seasonal_closure_check", "crowd_check",
    "festival_crowd_check", "safety_check", "border_area_check",
}


VALID_PROMOTION_STATUSES = {
    "candidate", "qa_pending", "dedupe_pending", "enrichment_pending", "source_pending",
    "review_ready", "planner_candidate", "planner_ready", "retired",
}


REQUIRED_COLUMNS = [
    "candidate_id", "name", "country", "macro_region", "state_or_area", "district_or_area",
    "proposed_location_type", "proposed_vibe_1", "proposed_vibe_2", "proposed_vibe_3",
    "priority_tier", "verification_status", "notes", "normalized_location_type",
    "normalized_vibe_1", "normalized_vibe_2", "normalized_vibe_3", "trip_style_tags",
    "context_tags", "caution_tags", "destination_scale_hint", "normalisation_notes",
    "promotion_status",
]


def read_rows(path: Path = INPUT_PATH) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def split_tags(value: str) -> list[str]:
    if not value:
        return []
    return [tag.strip() for tag in value.split(";") if tag.strip()]


def duplicates(values: Iterable[str]) -> list[str]:
    counts = Counter(values)
    return sorted([value for value, count in counts.items() if count > 1])


def invalid_tag_map(rows: list[dict[str, str]], fields: list[str], valid_values: set[str]) -> dict[str, list[str]]:
    invalid: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        for field in fields:
            for tag in split_tags(row.get(field, "")):
                if tag not in valid_values:
                    invalid[tag].append(row["candidate_id"])
    return dict(sorted(invalid.items()))


def validate(rows: list[dict[str, str]]) -> dict[str, object]:
    if not rows:
        raise ValueError("normalised backlog is empty")

    columns = set(rows[0].keys())
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in columns]

    ids = [row["candidate_id"] for row in rows]
    name_country_keys = [f"{row['name']}|{row['country']}" for row in rows]
    name_state_keys = [f"{row['name']}|{row['state_or_area']}" for row in rows]

    invalid_types = defaultdict(list)
    invalid_promotion = defaultdict(list)

    for row in rows:
        if row["normalized_location_type"] not in VALID_DESTINATION_TYPES:
            invalid_types[row["normalized_location_type"]].append(row["candidate_id"])
        if row["promotion_status"] not in VALID_PROMOTION_STATUSES:
            invalid_promotion[row["promotion_status"]].append(row["candidate_id"])

    invalid_vibes = invalid_tag_map(
        rows,
        ["normalized_vibe_1", "normalized_vibe_2", "normalized_vibe_3"],
        VALID_VIBES,
    )
    invalid_trip_styles = invalid_tag_map(rows, ["trip_style_tags"], VALID_TRIP_STYLE_TAGS)
    invalid_context_tags = invalid_tag_map(rows, ["context_tags"], VALID_CONTEXT_TAGS)
    invalid_caution_tags = invalid_tag_map(rows, ["caution_tags"], VALID_CAUTION_TAGS)

    rows_with_notes = [row for row in rows if row["normalisation_notes"]]
    rows_with_trip_styles = [row for row in rows if row["trip_style_tags"]]
    rows_with_context = [row for row in rows if row["context_tags"]]
    rows_with_cautions = [row for row in rows if row["caution_tags"]]

    return {
        "row_count": len(rows),
        "missing_columns": missing_columns,
        "unique_candidate_ids": len(set(ids)),
        "duplicate_candidate_ids": duplicates(ids),
        "duplicate_name_country_keys": duplicates(name_country_keys),
        "duplicate_name_state_keys": duplicates(name_state_keys),
        "invalid_types": dict(sorted(invalid_types.items())),
        "invalid_vibes": invalid_vibes,
        "invalid_trip_styles": invalid_trip_styles,
        "invalid_context_tags": invalid_context_tags,
        "invalid_caution_tags": invalid_caution_tags,
        "invalid_promotion_statuses": dict(sorted(invalid_promotion.items())),
        "macro_region_counts": dict(sorted(Counter(row["macro_region"] for row in rows).items())),
        "promotion_status_counts": dict(sorted(Counter(row["promotion_status"] for row in rows).items())),
        "rows_with_notes": len(rows_with_notes),
        "rows_with_trip_styles": len(rows_with_trip_styles),
        "rows_with_context": len(rows_with_context),
        "rows_with_cautions": len(rows_with_cautions),
    }


def format_mapping(mapping: dict[str, object]) -> str:
    if not mapping:
        return "- None\n"
    return "".join(f"- `{key}`: {value}\n" for key, value in mapping.items())


def write_report(result: dict[str, object], path: Path = REPORT_PATH) -> None:
    clean_enough = (
        not result["missing_columns"]
        and not result["duplicate_candidate_ids"]
        and not result["duplicate_name_country_keys"]
        and not result["duplicate_name_state_keys"]
        and not result["invalid_types"]
        and not result["invalid_vibes"]
        and not result["invalid_trip_styles"]
        and not result["invalid_context_tags"]
        and not result["invalid_caution_tags"]
        and not result["invalid_promotion_statuses"]
    )

    readiness = "clean_enough_for_master_promotion_design" if clean_enough else "needs_followup_before_master_promotion"

    content = f"""# Evidence Report — Destination Normalized Backlog Validation v1

Date: 2026-05-12  
Author: CodeMike  
Dataset: `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`  
Validator: `src/codemike/data/destination_normalized_validation.py`

## 1. Objective

Validate the normalised 225-row India destination backlog before designing `destinations_master_v2.csv`.

## 2. Validation Summary

| Check | Result |
|---|---:|
| Rows checked | {result['row_count']} |
| Unique candidate IDs | {result['unique_candidate_ids']} |
| Missing required columns | {len(result['missing_columns'])} |
| Duplicate candidate IDs | {len(result['duplicate_candidate_ids'])} |
| Duplicate name-country keys | {len(result['duplicate_name_country_keys'])} |
| Duplicate name-state keys | {len(result['duplicate_name_state_keys'])} |
| Invalid normalized destination types | {len(result['invalid_types'])} |
| Invalid normalized vibe tags | {len(result['invalid_vibes'])} |
| Invalid trip-style tags | {len(result['invalid_trip_styles'])} |
| Invalid context tags | {len(result['invalid_context_tags'])} |
| Invalid caution tags | {len(result['invalid_caution_tags'])} |
| Invalid promotion statuses | {len(result['invalid_promotion_statuses'])} |

Readiness:

```text
{readiness}
```

## 3. Normalisation Effect

| Metric | Rows |
|---|---:|
| Rows with normalisation notes | {result['rows_with_notes']} |
| Rows with trip-style tags | {result['rows_with_trip_styles']} |
| Rows with context tags | {result['rows_with_context']} |
| Rows with caution tags | {result['rows_with_cautions']} |

## 4. Macro-Region Coverage

{format_mapping(result['macro_region_counts'])}

## 5. Promotion Status Coverage

{format_mapping(result['promotion_status_counts'])}

## 6. Invalid Normalized Destination Types

{format_mapping(result['invalid_types'])}

## 7. Invalid Normalized Vibe Tags

{format_mapping(result['invalid_vibes'])}

## 8. Invalid Trip-Style Tags

{format_mapping(result['invalid_trip_styles'])}

## 9. Invalid Context Tags

{format_mapping(result['invalid_context_tags'])}

## 10. Invalid Caution Tags

{format_mapping(result['invalid_caution_tags'])}

## 11. Interpretation

The normalised backlog is now a better intermediate asset than the raw candidate backlog because obvious taxonomy contamination has been separated into clearer fields.

If all invalid counts are zero, the next step is not more tag cleaning. The next step is master schema design and controlled promotion.

## 12. Next Actions

1. Create `datasets/reference/destinations_master_v2_schema.md`.
2. Create `src/codemike/data/destination_master_promotion.py`.
3. Promote seed + normalised candidates into `destinations_master_v2.csv` with stable `DST2-*` IDs.
4. Add an HTML QA browser for master records.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    rows = read_rows()
    result = validate(rows)
    write_report(result)
    print(f"Validated {result['row_count']} normalised rows")
    print(f"Invalid normalized types: {len(result['invalid_types'])}")
    print(f"Invalid normalized vibes: {len(result['invalid_vibes'])}")
    print(f"Invalid trip-style tags: {len(result['invalid_trip_styles'])}")
    print(f"Invalid context tags: {len(result['invalid_context_tags'])}")
    print(f"Invalid caution tags: {len(result['invalid_caution_tags'])}")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
