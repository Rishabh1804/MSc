# Evidence Report — Destination Normalized Backlog Validation v1

Date: 2026-05-12  
Author: CodeMike  
Dataset: `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`  
Validator: `src/codemike/data/destination_normalized_validation.py`

## 1. Objective

Validate the normalised 225-row India destination backlog before designing `destinations_master_v2.csv`.

## 2. Validation Summary

| Check | Result |
|---|---:|
| Rows checked | 225 |
| Unique candidate IDs | 225 |
| Missing required columns | 0 |
| Duplicate candidate IDs | 0 |
| Duplicate name-country keys | 0 |
| Duplicate name-state keys | 0 |
| Invalid normalized destination types | 0 |
| Invalid normalized vibe tags | 0 |
| Invalid trip-style tags | 0 |
| Invalid context tags | 0 |
| Invalid caution tags | 0 |
| Invalid promotion statuses | 0 |

Readiness:

```text
clean_enough_for_master_promotion_design
```

## 3. Normalisation Effect

| Metric | Rows |
|---|---:|
| Rows with normalisation notes | 40 |
| Rows with trip-style tags | 15 |
| Rows with context tags | 17 |
| Rows with caution tags | 3 |

## 4. Macro-Region Coverage

- `Central India`: 17
- `East India`: 36
- `Island India`: 5
- `North East India`: 30
- `North India`: 73
- `South India`: 40
- `West India`: 24


## 5. Promotion Status Coverage

- `dedupe_pending`: 225


## 6. Invalid Normalized Destination Types

- None


## 7. Invalid Normalized Vibe Tags

- None


## 8. Invalid Trip-Style Tags

- None


## 9. Invalid Context Tags

- None


## 10. Invalid Caution Tags

- None


## 11. Interpretation

The normalised backlog is now a better intermediate asset than the raw candidate backlog because obvious taxonomy contamination has been separated into clearer fields.

If all invalid counts are zero, the next step is not more tag cleaning. The next step is master schema design and controlled promotion.

## 12. Next Actions

1. Create `datasets/reference/destinations_master_v2_schema.md`.
2. Create `src/codemike/data/destination_master_promotion.py`.
3. Promote seed + normalised candidates into `destinations_master_v2.csv` with stable `DST2-*` IDs.
4. Add an HTML QA browser for master records.
