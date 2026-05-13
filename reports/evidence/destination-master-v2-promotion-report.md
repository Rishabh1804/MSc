# Evidence Report — Destinations Master v2 Promotion

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
| Seed rows read | 134 |
| Normalized candidate rows read | 225 |
| Master rows written | 359 |
| Duplicate name-country keys flagged | 0 |
| Duplicate name-state keys flagged | 0 |

## 3. Readiness Status

```text
master_reference_created_not_planner_ready
```

No master row is Planner-ready yet. All rows require verification or enrichment before live travel recommendation use.

## 4. Source Layer Counts

- `normalized_candidate`: 225
- `seed`: 134

## 5. Verification Status Counts

- `candidate`: 225
- `seed_unverified`: 134

## 6. Promotion Status Counts

- `dedupe_pending`: 225
- `enrichment_pending`: 134

## 7. Planner Use Status Counts

- `needs_verification`: 359

## 8. Destination Scale Counts

- `town`: 104
- `city`: 102
- `region`: 53
- `site`: 26
- `park`: 23
- `unknown`: 21
- `island`: 20
- `resort_zone`: 8
- `village`: 2

## 9. Duplicate Name-Country Keys

- None

## 10. Duplicate Name-State Keys

- None

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
