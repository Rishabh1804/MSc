# Evidence Report — Destinations Master v2 Enrichment Validation (E1, v1.0)

Date: see enrichment_pass_date column in enriched CSV.
Author: CodeMike
Validator: `src/codemike/data/destination_master_enrichment_validation.py`
Input: `datasets/reference/destinations_master_v2_enriched.csv`

## 1. Objective

Validate the v1 enriched master against the strategy spec (structural checks only).
Does not verify live travel facts or source citations.

## 2. Validation Summary

| Check | Result |
|---|---:|
| Rows checked | 359 |
| Expected rows | 359 |
| Row count match | True |
| Missing required columns | 0 |
| Extra columns | 0 |
| Duplicate destination_master_id | 0 |
| Orphan enriched IDs (not in master) | 0 |
| Unmatched master IDs (not in enriched) | 0 |
| Total controlled-value violations | 0 |
| Infant score out of range | 0 |
| Band-vs-score mismatches | 0 |
| Heuristic-default violations | 0 |
| Pediatric > medical confidence | 0 |
| Permit/visa hint violations | 0 |
| Derived-field blanks | 0 |

Readiness:

```text
enriched_structurally_valid_not_planner_ready
```

## 3. Missing Columns

- None

## 4. Extra Columns

- None

## 5. Controlled-Value Violations (by column)

- None

## 6. Score Out-of-Range

- None

## 7. Band-vs-Score Mismatches

- None

## 8. Heuristic-Default Violations

- None

## 9. Pediatric > Medical Confidence

- None

## 10. Permit/Visa Hint Violations

- None

## 11. Derived-Field Blanks (sample)

- None

## 12. Distributions (sanity check)

### origin_fit_ccu

- `weak`: 142
- `moderate`: 132
- `strong`: 85

### origin_fit_ixr

- `weak`: 151
- `moderate`: 139
- `strong`: 69

### infant_suitability_band

- `low_medium`: 130
- `medium`: 119
- `low`: 79
- `high`: 31

### travel_fatigue_band

- `medium`: 233
- `low`: 89
- `very_high`: 34
- `high`: 3

### planning_complexity_band

- `medium`: 168
- `low`: 143
- `high`: 48

### medical_access_confidence

- `unknown`: 112
- `medium`: 101
- `high`: 82
- `low`: 64

## 13. Interpretation

If readiness is `enriched_structurally_valid_not_planner_ready`, the enriched layer
has passed all structural and controlled-value checks. It is ready for the E2
manual-review sessions (batches O / S / M).

It is still not Planner-ready because: heuristic-derived values carry
`source_confidence = low`; live travel facts have not been verified; the E3
source-verified promotion step has not been run.

## 14. Next Actions

1. If any failures above, fix the enrichment script and re-run.
2. If clean: schedule the E2 manual-review sessions per the strategy doc §11–§12.
3. After E2 completes, NEXT_ACTIONS priority 6 (scoring v1) can begin.
