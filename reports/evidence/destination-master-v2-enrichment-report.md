# Evidence Report — Destinations Master v2 Enrichment (E1, v1.0)

Date: 2026-05-18
Author: CodeMike
Script: `src/codemike/data/destination_master_enrichment_v1.py`
Inputs:
- `datasets/reference/destinations_master_v2.csv` (359 rows)
- `datasets/reference/origin_catchment_v1.json`
Output:
- `datasets/reference/destinations_master_v2_enriched.csv` (359 rows)
Manual-review queues:
- `reports/evidence/destination-master-v2-enrichment-manual-review-queues/O.csv` (0 rows)
- `reports/evidence/destination-master-v2-enrichment-manual-review-queues/S.csv` (155 rows)
- `reports/evidence/destination-master-v2-enrichment-manual-review-queues/M.csv` (257 rows)

## 1. Objective

E1 pass over the master dataset, implementing
`datasets/reference/destination_master_enrichment_strategy.md`.

This pass produces structured judgement, not source-backed truth. Every row defaults
to `verification_status = enriched_unverified` and `planner_use_status = needs_verification`.

## 2. Pipeline Status

| Step | Description | Result |
|---|---|---:|
| 0 | Read master + catchment | 359 rows read |
| 1a | Derive access_complexity for candidate rows | OK (heuristic per location_type / scale / state) |
| 1b | Derive caution tags from populated fields | OK (master had 3 tags total; derivation now populates per-row tags) |
| 2 | Compute origin_fit for CCU + IXR | OK |
| 3 | Compute travel_fatigue band + drivers | OK |
| 4 | Compute medical_access_confidence + pediatric subset | OK |
| 5 | Compute planning_complexity band + drivers + permit/visa hint | OK |
| 6 | Compute season window + weather cautions | OK |
| 7 | Compute suitability decomposed (infant score + 4 bands) | OK |
| 8 | Set verification/planner/source defaults | OK |
| 9 | Queue manual-review batches O/S/M | OK |

## 3. Origin-Fit Distribution

### CCU (Kolkata)

- `weak`: 142
- `moderate`: 132
- `strong`: 85

### IXR (Ranchi)

- `weak`: 151
- `moderate`: 139
- `strong`: 69

## 4. Travel-Fatigue Distribution

- `medium`: 233
- `low`: 89
- `very_high`: 34
- `high`: 3

## 5. Planning-Complexity Distribution

- `medium`: 168
- `low`: 143
- `high`: 48

## 6. Medical-Access Distribution

### medical_access_confidence

- `unknown`: 112
- `medium`: 101
- `high`: 82
- `low`: 64

### pediatric_access_confidence

- `unknown`: 112
- `medium`: 101
- `high`: 82
- `low`: 64

## 7. Suitability Distributions

### infant_suitability_score

- min: 0
- max: 80
- mean (1 dp): 45.3

### infant_suitability_band

- `low_medium`: 130
- `medium`: 119
- `low`: 79
- `high`: 31

### family_suitability_band

- `medium`: 315
- `low_medium`: 42
- `low`: 2

### senior_suitability_band

- `medium`: 322
- `low_medium`: 35
- `low`: 2

### couple_suitability_band

- `medium`: 316
- `low_medium`: 34
- `high`: 9

## 8. Verification / Planner Status (post-E1)

### verification_status

- `enriched_unverified`: 359

### planner_use_status

- `needs_verification`: 359

### source_confidence

- `low`: 359

## 9. Manual-Review Queue Sizes

| Batch | Description | Rows queued |
|---|---|---:|
| O | Origin fit (heuristic unknown) | 0 |
| S | Suitability (seed-vs-heuristic disagreement, boundary score, or band flattening) | 155 |
| M | Medical access (unknown OR infant_score < 50) | 257 |

Each queue is a CSV with destination_master_id + canonical_name + country + state + reason.

## 10. Honest Limitations

- All rows are at `source_confidence = low` — the heuristic produces structured judgement, not source-backed truth.
- The medical-access heuristic uses destination-scale as a proxy for actual medical-care availability; strategy doc §8.3 names this as the weakest formula in v1.
- caution_tags + context_tags were sparse in the master input (3 + 17 total tags across 359 rows); the script derives cautions from location_type / state_or_area / macro_region / destination_scale / vibes. This is consistent with the schema doc's note that caution_tags are heuristic-generated.
- Origin catchment tables (`origin_catchment_v1.json`) are workspace judgement, not verified flight/train data.
- No row crosses to `planner_ready` in this pass. Promotion to planner_ready is the separately-defined E3 step (strategy doc §12.4), out of scope for v1 enrichment.
- Real-user evaluation of enrichment quality is not part of this pass. Lab 05 F-PRIN-1 (Principle 2: Users involved throughout) applies; the Sponsor Reviewer cycle (NEXT_ACTIONS priority 9) should test heuristic outputs against a real planner's judgement.

## 11. Next Actions

1. Run `src/codemike/data/destination_master_enrichment_validation.py` to validate the enriched CSV structurally.
2. Schedule manual-review sessions O / S / M per strategy doc §11.1 + §12.3 (caps 30 / 25 / 20 rows per session).
3. After E2 manual-review sessions complete, NEXT_ACTIONS priority 6 (scoring v1) unblocks against a stable enriched layer.
