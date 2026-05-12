"""Normalise destination expansion backlog rows before promotion.

This utility converts the raw India candidate backlog into a cleaner intermediate
file. It keeps the original row identity but normalises obvious tag issues and
moves context-like values into explicit fields.

Input:
    datasets/reference/destination_expansion_backlog_india_v1.csv

Output:
    datasets/reference/destination_expansion_backlog_india_v1_normalized.csv

Status:
    Prototype normaliser for destination database v2.
"""

from __future__ import annotations

import csv
from pathlib import Path


INPUT_PATH = Path("datasets/reference/destination_expansion_backlog_india_v1.csv")
OUTPUT_PATH = Path("datasets/reference/destination_expansion_backlog_india_v1_normalized.csv")
REPORT_PATH = Path("reports/evidence/destination-candidate-backlog-normalisation-v1.md")


VIBE_REPLACEMENTS = {
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
}


VIBE_TO_TRIP_STYLE = {
    "weekend": "weekend_getaway",
}


VIBE_TO_CONTEXT = {
    "gateway": "gateway_context",
    "remote": "remote_context",
    "border": "border_context",
}


VIBE_TO_CAUTION = {
    "remote": "route_verification_check",
    "border": "border_area_check",
}


REVIEW_VALUES = {
    "marble": "review_landscape_or_geology_tag",
    "parks": "review_gardens_family_or_urban_tag",
}


TYPE_REPLACEMENTS = {
    "village": "craft_village",
}


TYPE_TO_SCALE_HINT = {
    "village": "village",
}


EXTRA_COLUMNS = [
    "normalized_location_type",
    "normalized_vibe_1",
    "normalized_vibe_2",
    "normalized_vibe_3",
    "trip_style_tags",
    "context_tags",
    "caution_tags",
    "destination_scale_hint",
    "normalisation_notes",
    "promotion_status",
]


def read_rows(path: Path = INPUT_PATH) -> list[dict[str, str]]:
    """Read raw backlog rows."""

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def unique_join(values: list[str]) -> str:
    """Return sorted unique semicolon-separated non-empty values."""

    return ";".join(sorted({value for value in values if value}))


def normalise_vibe(value: str) -> tuple[str, list[str], list[str], list[str], list[str]]:
    """Normalise one vibe value.

    Returns:
        normalized_vibe, trip_styles, context_tags, caution_tags, notes
    """

    value = value.strip()
    trip_styles: list[str] = []
    context_tags: list[str] = []
    caution_tags: list[str] = []
    notes: list[str] = []

    if not value:
        return "", trip_styles, context_tags, caution_tags, notes

    if value in VIBE_REPLACEMENTS:
        replacement = VIBE_REPLACEMENTS[value]
        notes.append(f"vibe:{value}->{replacement}")
        return replacement, trip_styles, context_tags, caution_tags, notes

    if value in VIBE_TO_TRIP_STYLE:
        trip_styles.append(VIBE_TO_TRIP_STYLE[value])
        notes.append(f"vibe:{value}->trip_style:{VIBE_TO_TRIP_STYLE[value]}")
        return "", trip_styles, context_tags, caution_tags, notes

    if value in VIBE_TO_CONTEXT:
        context_tags.append(VIBE_TO_CONTEXT[value])
        if value in VIBE_TO_CAUTION:
            caution_tags.append(VIBE_TO_CAUTION[value])
        notes.append(f"vibe:{value}->context")
        return "", trip_styles, context_tags, caution_tags, notes

    if value in REVIEW_VALUES:
        notes.append(f"vibe:{value}->{REVIEW_VALUES[value]}")
        return "", trip_styles, context_tags, caution_tags, notes

    return value, trip_styles, context_tags, caution_tags, notes


def normalise_row(row: dict[str, str]) -> dict[str, str]:
    """Return one normalised row with appended normalisation columns."""

    result = dict(row)
    raw_type = row["proposed_location_type"].strip()
    notes: list[str] = []
    trip_styles: list[str] = []
    context_tags: list[str] = []
    caution_tags: list[str] = []
    destination_scale_hints: list[str] = []

    normalized_type = TYPE_REPLACEMENTS.get(raw_type, raw_type)
    if normalized_type != raw_type:
        notes.append(f"type:{raw_type}->{normalized_type}")
    if raw_type in TYPE_TO_SCALE_HINT:
        destination_scale_hints.append(TYPE_TO_SCALE_HINT[raw_type])

    normalized_vibes: list[str] = []
    for field in ["proposed_vibe_1", "proposed_vibe_2", "proposed_vibe_3"]:
        normalized, moved_trip_styles, moved_context, moved_cautions, vibe_notes = normalise_vibe(row[field])
        if normalized:
            normalized_vibes.append(normalized)
        trip_styles.extend(moved_trip_styles)
        context_tags.extend(moved_context)
        caution_tags.extend(moved_cautions)
        notes.extend(vibe_notes)

    # Preserve at most three vibe columns after removing context-only values.
    normalized_vibes = list(dict.fromkeys(normalized_vibes))
    while len(normalized_vibes) < 3:
        normalized_vibes.append("")

    result["normalized_location_type"] = normalized_type
    result["normalized_vibe_1"] = normalized_vibes[0]
    result["normalized_vibe_2"] = normalized_vibes[1]
    result["normalized_vibe_3"] = normalized_vibes[2]
    result["trip_style_tags"] = unique_join(trip_styles)
    result["context_tags"] = unique_join(context_tags)
    result["caution_tags"] = unique_join(caution_tags)
    result["destination_scale_hint"] = unique_join(destination_scale_hints)
    result["normalisation_notes"] = unique_join(notes)
    result["promotion_status"] = "dedupe_pending"

    return result


def write_rows(rows: list[dict[str, str]], path: Path = OUTPUT_PATH) -> None:
    """Write normalised rows."""

    if not rows:
        raise ValueError("no rows to write")

    fieldnames = list(rows[0].keys())
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalisation_summary(rows: list[dict[str, str]]) -> dict[str, int]:
    """Return simple normalisation summary counts."""

    return {
        "rows": len(rows),
        "rows_with_notes": sum(1 for row in rows if row["normalisation_notes"]),
        "rows_with_trip_style_tags": sum(1 for row in rows if row["trip_style_tags"]),
        "rows_with_context_tags": sum(1 for row in rows if row["context_tags"]),
        "rows_with_caution_tags": sum(1 for row in rows if row["caution_tags"]),
        "rows_with_scale_hint": sum(1 for row in rows if row["destination_scale_hint"]),
    }


def write_report(rows: list[dict[str, str]], path: Path = REPORT_PATH) -> None:
    """Write a markdown report for the normalisation pass."""

    summary = normalisation_summary(rows)
    content = f"""# Evidence Report — Destination Candidate Backlog Normalisation v1

Date: 2026-05-12  
Author: CodeMike  
Input: `datasets/reference/destination_expansion_backlog_india_v1.csv`  
Output: `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`  
Normaliser: `src/codemike/data/destination_backlog_normalization.py`

## 1. Objective

Create a normalised candidate backlog that is cleaner than the raw 225-row India expansion backlog and safer to use for future promotion into `destinations_master_v2.csv`.

## 2. Summary

| Metric | Value |
|---|---:|
| Rows processed | {summary['rows']} |
| Rows with normalisation notes | {summary['rows_with_notes']} |
| Rows with trip-style tags created | {summary['rows_with_trip_style_tags']} |
| Rows with context tags created | {summary['rows_with_context_tags']} |
| Rows with caution tags created | {summary['rows_with_caution_tags']} |
| Rows with destination-scale hint | {summary['rows_with_scale_hint']} |

## 3. Normalisation Rules Applied

| Raw value | Action |
|---|---|
| `fort` | `forts` |
| `temple` | `temples` |
| `crafts` | `handicrafts` |
| `weekend` | moved to `trip_style_tags = weekend_getaway` |
| `gateway` | moved to `context_tags = gateway_context` |
| `remote` | moved to `context_tags = remote_context` and `caution_tags = route_verification_check` |
| `border` | moved to `context_tags = border_context` and `caution_tags = border_area_check` |
| `village` location type | converted to `craft_village` with `destination_scale_hint = village` |
| `marble` | removed from vibe and marked for review |
| `parks` | removed from vibe and marked for review |

## 4. Output Columns Added

- `normalized_location_type`
- `normalized_vibe_1`
- `normalized_vibe_2`
- `normalized_vibe_3`
- `trip_style_tags`
- `context_tags`
- `caution_tags`
- `destination_scale_hint`
- `normalisation_notes`
- `promotion_status`

## 5. Interpretation

This pass separates clean descriptive vibe tags from trip-style, context, and caution concepts. That reduces taxonomy contamination before master promotion.

The normalised backlog should still not be considered Planner-ready. It is one stage cleaner than candidate data, but it still needs:

1. deduplication against seed records
2. destination scale review
3. enrichment fields
4. verification source tracking
5. human review before Planner use

## 6. Next Actions

1. Run taxonomy validation on the normalised backlog.
2. Create a backlog QA HTML browser.
3. Promote selected clean records into `destinations_master_v2.csv`.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    rows = read_rows()
    normalised_rows = [normalise_row(row) for row in rows]
    write_rows(normalised_rows)
    write_report(normalised_rows)
    print(f"Normalised {len(normalised_rows)} rows")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
