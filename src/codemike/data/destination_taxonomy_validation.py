"""Validate destination candidate backlog against CodeMike destination taxonomy.

This utility is intentionally lightweight and dependency-free so it can run in
simple environments. It validates the candidate backlog before rows are promoted
into a master destination dataset.

Status:
    Prototype validator for destination database v2.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


BACKLOG_PATH = Path("datasets/reference/destination_expansion_backlog_india_v1.csv")
REPORT_PATH = Path("reports/evidence/destination-candidate-backlog-taxonomy-qa-v1.md")


VALID_DESTINATION_TYPES = {
    "metro_city", "city", "global_city", "capital_city", "heritage_city", "culture_city",
    "spiritual_city", "temple_city", "pilgrim_city", "planned_city", "coastal_city",
    "hill_city", "mountain_city", "gateway_city", "city_gateway", "business_city",
    "education_city", "food_city", "craft_city",
    "hill_station", "hill_town", "hill_region", "mountain_town", "mountain_region",
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
    "river", "waterfalls", "forest", "rainforest", "desert", "snow", "tea", "coffee",
    "spice", "backwaters", "gardens", "meadows", "caves", "mangrove", "wetland",
    "birding", "flowers", "landscape", "sunrise", "sunset", "beach", "coast", "islands",
    "marine", "diving", "snorkelling", "water", "resort", "lagoon", "coral", "cruise",
    "houseboat", "adventure", "trekking", "safari", "ski", "rafting", "paragliding",
    "camping", "road_trip", "cycling", "boating", "theme_parks", "water_sports",
    "desert_safari", "buddhist", "jain", "sikh", "temples", "forts", "palace", "wine",
    "textiles", "handicrafts", "wildlife", "tiger", "rhino", "elephant", "marine_life",
    "colonial", "french_quarter", "silk_route",
}


VALID_PRIORITY_TIERS = {"tier_1", "tier_2", "tier_3", "tier_4"}
VALID_VERIFICATION_STATUSES = {"candidate", "seed_unverified", "enriched_unverified", "source_verified", "planner_ready", "retired"}


NORMALISATION_HINTS = {
    "fort": "forts",
    "temple": "temples",
    "crafts": "handicrafts",
    "falls": "waterfalls",
    "lake": "lakes",
    "hill": "hills",
    "mountain": "mountains",
    "historical": "history",
    "historic": "history",
    "religious": "spiritual",
    "handloom": "textiles",
    "jungle": "forest",
    "riverside": "river",
    "weekend": "weekend_getaway_or_remove_from_vibe",
    "gateway": "gateway_is_context_not_vibe",
    "marble": "consider_landscape_or_heritage_context",
    "border": "border_area_check_as_caution_not_vibe",
    "remote": "route_verification_check_or_access_complexity_not_vibe",
    "parks": "gardens_or_family_context",
    "viewpoint": "viewpoint",
}


def read_rows(path: Path = BACKLOG_PATH) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def duplicates(values: Iterable[str]) -> list[str]:
    counts = Counter(values)
    return sorted([value for value, count in counts.items() if count > 1])


def validate(rows: list[dict[str, str]]) -> dict[str, object]:
    invalid_types: dict[str, list[str]] = defaultdict(list)
    invalid_vibes: dict[str, list[str]] = defaultdict(list)
    invalid_priority: list[str] = []
    invalid_status: list[str] = []

    for row in rows:
        candidate_id = row["candidate_id"]
        location_type = row["proposed_location_type"]
        if location_type not in VALID_DESTINATION_TYPES:
            invalid_types[location_type].append(candidate_id)

        for field in ["proposed_vibe_1", "proposed_vibe_2", "proposed_vibe_3"]:
            vibe = row[field]
            if vibe and vibe not in VALID_VIBES:
                invalid_vibes[vibe].append(candidate_id)

        if row["priority_tier"] not in VALID_PRIORITY_TIERS:
            invalid_priority.append(candidate_id)
        if row["verification_status"] not in VALID_VERIFICATION_STATUSES:
            invalid_status.append(candidate_id)

    name_country_keys = [f"{row['name']}|{row['country']}" for row in rows]
    name_state_keys = [f"{row['name']}|{row['state_or_area']}" for row in rows]

    return {
        "row_count": len(rows),
        "unique_candidate_ids": len(set(row["candidate_id"] for row in rows)),
        "duplicate_candidate_ids": duplicates(row["candidate_id"] for row in rows),
        "duplicate_name_country_keys": duplicates(name_country_keys),
        "duplicate_name_state_keys": duplicates(name_state_keys),
        "macro_region_counts": dict(sorted(Counter(row["macro_region"] for row in rows).items())),
        "state_counts": dict(sorted(Counter(row["state_or_area"] for row in rows).items())),
        "priority_counts": dict(sorted(Counter(row["priority_tier"] for row in rows).items())),
        "invalid_types": dict(sorted(invalid_types.items())),
        "invalid_vibes": dict(sorted(invalid_vibes.items())),
        "invalid_priority": invalid_priority,
        "invalid_status": invalid_status,
    }


def format_mapping(mapping: dict[str, object], limit: int | None = None) -> str:
    items = list(mapping.items())
    if limit is not None:
        items = items[:limit]
    if not items:
        return "- None\n"
    return "".join(f"- `{key}`: {value}\n" for key, value in items)


def write_report(result: dict[str, object], path: Path = REPORT_PATH) -> None:
    invalid_vibes = result["invalid_vibes"]
    invalid_types = result["invalid_types"]

    normalisation_lines = []
    for vibe in invalid_vibes:
        if vibe in NORMALISATION_HINTS:
            normalisation_lines.append(f"- `{vibe}` → `{NORMALISATION_HINTS[vibe]}`")
        else:
            normalisation_lines.append(f"- `{vibe}` → review whether to add to dictionary or replace")

    content = f"""# Evidence Report — Destination Candidate Backlog Taxonomy QA v1

Date: 2026-05-12  
Author: CodeMike  
Dataset: `datasets/reference/destination_expansion_backlog_india_v1.csv`  
Taxonomy: `datasets/reference/destination_tag_dictionary.md`  
Validator: `src/codemike/data/destination_taxonomy_validation.py`

## 1. Objective

Validate the 225-row India destination candidate backlog against Destination Tag Dictionary v2 before promotion into a master destination dataset.

## 2. Summary

| Check | Result |
|---|---:|
| Rows checked | {result['row_count']} |
| Unique candidate IDs | {result['unique_candidate_ids']} |
| Duplicate candidate IDs | {len(result['duplicate_candidate_ids'])} |
| Duplicate name-country keys | {len(result['duplicate_name_country_keys'])} |
| Duplicate name-state keys | {len(result['duplicate_name_state_keys'])} |
| Invalid destination types | {len(invalid_types)} |
| Invalid vibe tags | {len(invalid_vibes)} |
| Invalid priority tiers | {len(result['invalid_priority'])} |
| Invalid verification statuses | {len(result['invalid_status'])} |

## 3. Macro-Region Coverage

{format_mapping(result['macro_region_counts'])}

## 4. Priority Tier Coverage

{format_mapping(result['priority_counts'])}

## 5. Invalid Destination Types

{format_mapping(invalid_types)}

## 6. Invalid Vibe Tags

{format_mapping(invalid_vibes)}

## 7. Normalisation Recommendations

{chr(10).join(normalisation_lines) if normalisation_lines else '- None'}

## 8. Duplicate Review

### Duplicate Candidate IDs

{format_mapping({item: 'duplicate' for item in result['duplicate_candidate_ids']})}

### Duplicate Name-Country Keys

{format_mapping({item: 'duplicate' for item in result['duplicate_name_country_keys']})}

## 9. Interpretation

The backlog is structurally useful but not yet promotion-ready. Candidate IDs are unique, but several proposed vibe values are context labels rather than controlled vibe tags. These should be normalised before creating `destinations_master_v2.csv`.

Important distinction:

- `weekend`, `gateway`, `remote`, and `border` are better treated as trip-style, context, access, or caution fields rather than vibe tags.
- `fort` should usually become `forts`.
- `temple` should usually become `temples`.
- `marble` is too specific for the current vibe dictionary and needs review.

## 10. Next Actions

1. Create a normalised backlog file: `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`.
2. Add missing approved tags only where they improve Planner filtering or scoring.
3. Create a promotion script that writes selected rows into `destinations_master_v2.csv`.
4. Add an HTML QA browser for invalid tags and promotion status.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    rows = read_rows()
    result = validate(rows)
    write_report(result)
    print(f"Validated {result['row_count']} rows")
    print(f"Invalid destination types: {len(result['invalid_types'])}")
    print(f"Invalid vibe tags: {len(result['invalid_vibes'])}")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
