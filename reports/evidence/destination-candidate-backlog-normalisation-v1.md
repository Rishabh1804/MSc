# Evidence Report — Destination Candidate Backlog Normalisation v1

Date: 2026-05-12  
Author: CodeMike  
Input: `datasets/reference/destination_expansion_backlog_india_v1.csv`  
Target output: `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`  
Normaliser: `src/codemike/data/destination_backlog_normalization.py`

## 1. Objective

Create a normalised candidate backlog that is cleaner than the raw 225-row India expansion backlog and safer to use for future promotion into `destinations_master_v2.csv`.

## 2. Status

The normalisation utility has been created and committed.

The generated normalised CSV is the next execution artifact. It should be produced by running:

```bash
python src/codemike/data/destination_backlog_normalization.py
```

Expected output:

```text
datasets/reference/destination_expansion_backlog_india_v1_normalized.csv
```

## 3. Normalisation Rules Implemented

| Raw value | Action |
|---|---|
| `fort` | `forts` |
| `temple` | `temples` |
| `crafts` | `handicrafts` |
| `falls` | `waterfalls` |
| `lake` | `lakes` |
| `hill` | `hills` |
| `mountain` | `mountains` |
| `historical` | `history` |
| `historic` | `history` |
| `religious` | `spiritual` |
| `handloom` | `textiles` |
| `jungle` | `forest` |
| `riverside` | `river` |
| `weekend` | moved to `trip_style_tags = weekend_getaway` |
| `gateway` | moved to `context_tags = gateway_context` |
| `remote` | moved to `context_tags = remote_context` and `caution_tags = route_verification_check` |
| `border` | moved to `context_tags = border_context` and `caution_tags = border_area_check` |
| `village` location type | converted to `craft_village` with `destination_scale_hint = village` |
| `marble` | removed from vibe and marked for review |
| `parks` | removed from vibe and marked for review |

## 4. Output Columns Added by the Script

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

## 5. Why This Matters

The raw backlog was useful for scale, but some values in `proposed_vibe_*` were not true vibes. They were actually:

- trip-style information
- route/access context
- caution flags
- destination scale hints
- review-only values

This utility separates those dimensions before we create `destinations_master_v2.csv`.

## 6. Current Pipeline Position

```text
candidate backlog
→ taxonomy QA ✅
→ normalisation utility ✅
→ generated normalised backlog ⬅ next execution artifact
→ destinations_master_v2.csv
→ enriched master
→ scoring
→ Planner transfer
```

## 7. Next Actions

1. Run `src/codemike/data/destination_backlog_normalization.py`.
2. Commit `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`.
3. Run taxonomy validation against the normalised fields.
4. Create a backlog QA HTML browser.
5. Promote selected clean records into `destinations_master_v2.csv`.

## 8. Limitation

This report documents the utility and expected normalisation logic. It is not yet a computed run report because the generated CSV has not been committed in this turn.
