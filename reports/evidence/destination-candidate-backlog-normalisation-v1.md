# Evidence Report — Destination Candidate Backlog Normalisation v1

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
| Rows processed | 225 |
| Rows with normalisation notes | 40 |
| Rows with trip-style tags created | 15 |
| Rows with context tags created | 17 |
| Rows with caution tags created | 3 |
| Rows with destination-scale hint | 1 |

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
