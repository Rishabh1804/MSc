# Evidence Report — Destinations Master v2 Validation

Date: 2026-05-12  
Author: CodeMike  
Dataset: `datasets/reference/destinations_master_v2.csv`  
Validator: `src/codemike/data/destination_master_validation.py`

## 1. Objective

Validate `destinations_master_v2.csv` against the master v2 schema before creating a browser or downstream scoring layer.

This validation checks structural integrity only. It does not verify live travel facts.

## 2. Validation Summary

| Check | Result |
|---|---:|
| Rows checked | 359 |
| Expected rows | 359 |
| Missing required columns | 0 |
| Extra columns | 0 |
| Duplicate master IDs | 0 |
| Duplicate lineage keys | 0 |
| Duplicate name-country keys | 0 |
| Duplicate name-state keys | 0 |
| Critical fields with blanks | 0 |
| Invalid source layers | 0 |
| Invalid destination scales | 0 |
| Invalid location types | 12 |
| Invalid vibe tags | 7 |
| Invalid trip-style tags | 0 |
| Invalid context tags | 0 |
| Invalid caution tags | 0 |
| Invalid verification statuses | 0 |
| Invalid promotion statuses | 0 |
| Invalid planner-use statuses | 0 |
| Invalid source-confidence values | 0 |

Readiness:

```text
master_needs_structural_cleanup
```

## 3. Source Layer Counts

- `normalized_candidate`: 225
- `seed`: 134


## 4. Verification Status Counts

- `candidate`: 225
- `seed_unverified`: 134


## 5. Promotion Status Counts

- `dedupe_pending`: 225
- `enrichment_pending`: 134


## 6. Planner Use Status Counts

- `needs_verification`: 359


## 7. Destination Scale Counts

- `city`: 102
- `island`: 20
- `park`: 23
- `region`: 53
- `resort_zone`: 8
- `site`: 26
- `town`: 104
- `unknown`: 21
- `village`: 2


## 8. Invalid Location Types

- `beach_city`: ['DST2-000125']
- `culture_hill_town`: ['DST2-000120']
- `desert_beach_emirate`: ['DST2-000105']
- `heritage_capital`: ['DST2-000121']
- `hill_heritage_city`: ['DST2-000096']
- `island_heritage_city`: ['DST2-000118']
- `island_resort_district`: ['DST2-000115']
- `lake_mountain_city`: ['DST2-000091']
- `mountain_capital`: ['DST2-000093']
- `mountain_valley`: ['DST2-000094']
- `northern_city`: ['DST2-000113']
- `wildlife_region`: ['DST2-000092']


## 9. Invalid Vibe Tags

- `city`: ['DST2-000065', 'DST2-000129', 'DST2-000132']
- `limestone`: ['DST2-000111']
- `monsoon`: ['DST2-000108']
- `museums`: ['DST2-000106']
- `relaxation`: ['DST2-000091', 'DST2-000111']
- `stopover`: ['DST2-000106']
- `villa`: ['DST2-000119']


## 10. Duplicate Name-Country Keys

- None


## 11. Duplicate Name-State Keys

- None


## 12. Critical Blank Fields

- None


## 13. Interpretation

If readiness is `master_structurally_valid_not_planner_ready`, the dataset is ready for a master HTML browser and enrichment planning.

It is still not Planner-ready because live travel facts and source verification have not been completed.

## 14. Next Actions

1. Fix any structural issues found by this report.
2. Create `docs/destination-master-browser-v1.html` after validation is clean.
3. Add a master browser link to `docs/index.html`.
4. Begin enrichment fields only after the master layer is structurally clean.
