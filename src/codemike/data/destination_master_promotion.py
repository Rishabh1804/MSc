"""Promote seed and normalized candidate destinations into master v2.

This script creates the first canonical master destination dataset by combining:

1. datasets/reference/india_region_destinations_seed.csv
2. datasets/reference/destination_expansion_backlog_india_v1_normalized.csv

Outputs:

1. datasets/reference/destinations_master_v2.csv
2. reports/evidence/destination-master-v2-promotion-report.md

The output is a structured master reference layer, not a verified travel-truth
or Planner-ready layer.
"""

from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SEED_PATH = Path("datasets/reference/india_region_destinations_seed.csv")
CANDIDATE_PATH = Path("datasets/reference/destination_expansion_backlog_india_v1_normalized.csv")
MASTER_PATH = Path("datasets/reference/destinations_master_v2.csv")
REPORT_PATH = Path("reports/evidence/destination-master-v2-promotion-report.md")

SEED_SOURCE_FILE = str(SEED_PATH)
CANDIDATE_SOURCE_FILE = str(CANDIDATE_PATH)

MASTER_COLUMNS = [
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


@dataclass(frozen=True)
class PromotionStats:
    seed_rows: int
    candidate_rows: int
    master_rows: int
    duplicate_name_country_count: int
    duplicate_name_state_count: int


def read_csv(path: Path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dictionaries."""

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    """Write master rows to CSV."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=MASTER_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def normalise_key(value: str) -> str:
    """Normalize text for duplicate key checks."""

    return " ".join(value.strip().lower().split())


def duplicate_values(values: Iterable[str]) -> list[str]:
    """Return sorted values that appear more than once."""

    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def infer_destination_scale(location_type: str, destination_scale_hint: str = "") -> str:
    """Infer a broad destination scale from location type and optional hint."""

    hint = destination_scale_hint.strip()
    if hint:
        return hint

    value = location_type.strip()
    if not value:
        return "unknown"

    if "circuit" in value:
        return "circuit"
    if "island" in value:
        return "island"
    if value == "national_park" or value.endswith("_reserve") or value in {"tiger_reserve", "wildlife_reserve"}:
        return "park"
    if value.endswith("_city") or value in {"city", "metro_city", "global_city", "capital_city", "city_gateway"}:
        return "city"
    if value.endswith("_town") or value in {"town", "hill_station", "lake_hill_station"}:
        return "town"
    if value.endswith("_village") or value == "craft_village":
        return "village"
    if value.endswith("_site") or value in {"birding_site", "waterfall_site"}:
        return "site"
    if value.endswith("_region"):
        return "region"
    if "resort" in value:
        return "resort_zone"
    if value.endswith("_route") or value == "route":
        return "route"

    return "unknown"


def clean(value: str | None) -> str:
    """Return a stripped string for CSV values."""

    return (value or "").strip()


def master_id(index: int) -> str:
    """Return stable master ID for first promotion pass."""

    return f"DST2-{index:06d}"


def map_seed_row(row: dict[str, str], index: int) -> dict[str, str]:
    """Map one seed row into the master schema."""

    location_type = clean(row.get("location_type"))
    return {
        "destination_master_id": master_id(index),
        "source_layer": "seed",
        "source_id": clean(row.get("destination_id")),
        "source_file": SEED_SOURCE_FILE,
        "canonical_name": clean(row.get("name")),
        "alias_names": "",
        "country": clean(row.get("country")),
        "macro_region": clean(row.get("macro_region")),
        "state_or_area": clean(row.get("state_or_area")),
        "district_or_area": "",
        "destination_scale": infer_destination_scale(location_type),
        "location_type": location_type,
        "vibe_1": clean(row.get("vibe_1")),
        "vibe_2": clean(row.get("vibe_2")),
        "vibe_3": clean(row.get("vibe_3")),
        "trip_style_tags": "",
        "context_tags": "",
        "caution_tags": "",
        "budget_band": clean(row.get("budget_band")),
        "family_suitability": clean(row.get("family_suitability")),
        "access_complexity": clean(row.get("access_complexity")),
        "best_season_hint": clean(row.get("best_season_hint")),
        "verification_status": clean(row.get("verification_status")) or "seed_unverified",
        "promotion_status": "enrichment_pending",
        "planner_use_status": "needs_verification",
        "source_confidence": "none",
        "source_notes": "seed row promoted into master v2; not source verified",
        "normalisation_notes": "",
        "master_notes": "initial seed promotion",
    }


def map_candidate_row(row: dict[str, str], index: int) -> dict[str, str]:
    """Map one normalized candidate row into the master schema."""

    location_type = clean(row.get("normalized_location_type"))
    scale_hint = clean(row.get("destination_scale_hint"))
    return {
        "destination_master_id": master_id(index),
        "source_layer": "normalized_candidate",
        "source_id": clean(row.get("candidate_id")),
        "source_file": CANDIDATE_SOURCE_FILE,
        "canonical_name": clean(row.get("name")),
        "alias_names": "",
        "country": clean(row.get("country")),
        "macro_region": clean(row.get("macro_region")),
        "state_or_area": clean(row.get("state_or_area")),
        "district_or_area": clean(row.get("district_or_area")),
        "destination_scale": infer_destination_scale(location_type, scale_hint),
        "location_type": location_type,
        "vibe_1": clean(row.get("normalized_vibe_1")),
        "vibe_2": clean(row.get("normalized_vibe_2")),
        "vibe_3": clean(row.get("normalized_vibe_3")),
        "trip_style_tags": clean(row.get("trip_style_tags")),
        "context_tags": clean(row.get("context_tags")),
        "caution_tags": clean(row.get("caution_tags")),
        "budget_band": "",
        "family_suitability": "",
        "access_complexity": "",
        "best_season_hint": "",
        "verification_status": clean(row.get("verification_status")) or "candidate",
        "promotion_status": clean(row.get("promotion_status")) or "dedupe_pending",
        "planner_use_status": "needs_verification",
        "source_confidence": "none",
        "source_notes": "normalized candidate promoted into master v2; not source verified",
        "normalisation_notes": clean(row.get("normalisation_notes")),
        "master_notes": "initial normalized candidate promotion",
    }


def build_master(seed_rows: list[dict[str, str]], candidate_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Build master rows in deterministic order."""

    master_rows: list[dict[str, str]] = []
    index = 1

    for row in seed_rows:
        master_rows.append(map_seed_row(row, index))
        index += 1

    for row in candidate_rows:
        master_rows.append(map_candidate_row(row, index))
        index += 1

    return master_rows


def summarize(master_rows: list[dict[str, str]], seed_rows: list[dict[str, str]], candidate_rows: list[dict[str, str]]) -> PromotionStats:
    """Return promotion stats."""

    name_country_keys = [
        f"{normalise_key(row['canonical_name'])}|{normalise_key(row['country'])}"
        for row in master_rows
    ]
    name_state_keys = [
        f"{normalise_key(row['canonical_name'])}|{normalise_key(row['state_or_area'])}"
        for row in master_rows
    ]

    return PromotionStats(
        seed_rows=len(seed_rows),
        candidate_rows=len(candidate_rows),
        master_rows=len(master_rows),
        duplicate_name_country_count=len(duplicate_values(name_country_keys)),
        duplicate_name_state_count=len(duplicate_values(name_state_keys)),
    )


def counter_markdown(title: str, values: Iterable[str]) -> str:
    """Return markdown bullet list for a value counter."""

    counts = Counter(values)
    if not counts:
        return f"## {title}\n\n- None\n"

    lines = [f"## {title}", ""]
    for key, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        display = key if key else "blank"
        lines.append(f"- `{display}`: {count}")
    lines.append("")
    return "\n".join(lines)


def duplicate_section(title: str, rows: list[dict[str, str]], mode: str) -> str:
    """Return markdown section listing duplicate keys."""

    if mode == "country":
        keys = [f"{normalise_key(row['canonical_name'])}|{normalise_key(row['country'])}" for row in rows]
    elif mode == "state":
        keys = [f"{normalise_key(row['canonical_name'])}|{normalise_key(row['state_or_area'])}" for row in rows]
    else:
        raise ValueError(f"unknown duplicate mode: {mode}")

    duplicate_keys = set(duplicate_values(keys))
    lines = [f"## {title}", ""]
    if not duplicate_keys:
        lines.append("- None")
        lines.append("")
        return "\n".join(lines)

    for row, key in zip(rows, keys):
        if key in duplicate_keys:
            lines.append(
                f"- `{key}` → `{row['destination_master_id']}` / `{row['source_layer']}` / `{row['canonical_name']}`"
            )
    lines.append("")
    return "\n".join(lines)


def write_report(master_rows: list[dict[str, str]], seed_rows: list[dict[str, str]], candidate_rows: list[dict[str, str]], path: Path = REPORT_PATH) -> None:
    """Write a markdown promotion report."""

    stats = summarize(master_rows, seed_rows, candidate_rows)
    source_layer_counts = Counter(row["source_layer"] for row in master_rows)
    verification_counts = Counter(row["verification_status"] for row in master_rows)
    promotion_counts = Counter(row["promotion_status"] for row in master_rows)
    planner_counts = Counter(row["planner_use_status"] for row in master_rows)
    scale_counts = Counter(row["destination_scale"] for row in master_rows)

    content = f"""# Evidence Report — Destinations Master v2 Promotion

Date: 2026-05-12  
Author: CodeMike  
Script: `src/codemike/data/destination_master_promotion.py`  
Output: `datasets/reference/destinations_master_v2.csv`

## 1. Objective

Promote the seed destination database and clean normalized India candidate backlog into the first canonical `destinations_master_v2.csv` reference dataset.

This is a structured master layer, not a verified travel-truth layer.

## 2. Promotion Summary

| Metric | Value |
|---|---:|
| Seed rows read | {stats.seed_rows} |
| Normalized candidate rows read | {stats.candidate_rows} |
| Master rows written | {stats.master_rows} |
| Duplicate name-country keys flagged | {stats.duplicate_name_country_count} |
| Duplicate name-state keys flagged | {stats.duplicate_name_state_count} |

## 3. Readiness Status

```text
master_reference_created_not_planner_ready
```

No master row is Planner-ready yet. All rows require verification or enrichment before live travel recommendation use.

{counter_markdown('4. Source Layer Counts', source_layer_counts.elements())}
{counter_markdown('5. Verification Status Counts', verification_counts.elements())}
{counter_markdown('6. Promotion Status Counts', promotion_counts.elements())}
{counter_markdown('7. Planner Use Status Counts', planner_counts.elements())}
{counter_markdown('8. Destination Scale Counts', scale_counts.elements())}
{duplicate_section('9. Duplicate Name-Country Keys', master_rows, 'country')}
{duplicate_section('10. Duplicate Name-State Keys', master_rows, 'state')}
## 11. Interpretation

The master dataset consolidates the two current destination layers into one canonical reference table with stable `DST2-*` IDs and explicit source lineage.

Important constraints:

- Master rows are structurally valid, not verified.
- `planner_use_status` remains `needs_verification` for all rows.
- Candidate rows remain `dedupe_pending` until a deeper duplicate/circuit review is performed.
- Seed rows are `enrichment_pending` because they need normalized candidate-style enrichment fields.

## 12. Next Actions

1. Create `src/codemike/data/destination_master_validation.py`.
2. Validate `destinations_master_v2.csv` against the master schema.
3. Create `reports/evidence/destination-master-v2-validation-report.md`.
4. Create an HTML browser for master records.
5. Begin enrichment of master records only after validation.
"""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    seed_rows = read_csv(SEED_PATH)
    candidate_rows = read_csv(CANDIDATE_PATH)
    master_rows = build_master(seed_rows, candidate_rows)

    write_csv(master_rows, MASTER_PATH)
    write_report(master_rows, seed_rows, candidate_rows)

    stats = summarize(master_rows, seed_rows, candidate_rows)
    print(f"Seed rows read: {stats.seed_rows}")
    print(f"Normalized candidate rows read: {stats.candidate_rows}")
    print(f"Master rows written: {stats.master_rows}")
    print(f"Duplicate name-country keys flagged: {stats.duplicate_name_country_count}")
    print(f"Duplicate name-state keys flagged: {stats.duplicate_name_state_count}")
    print(f"Wrote {MASTER_PATH}")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
