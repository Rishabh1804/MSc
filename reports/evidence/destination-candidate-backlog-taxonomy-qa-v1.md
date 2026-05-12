# Evidence Report — Destination Candidate Backlog Taxonomy QA v1

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
| Rows checked | 225 |
| Unique candidate IDs | 225 |
| Duplicate candidate IDs | 0 |
| Duplicate name-country keys | 0 |
| Duplicate name-state keys | 0 |
| Invalid destination types | 4 |
| Invalid vibe tags | 10 |
| Invalid priority tiers | 0 |
| Invalid verification statuses | 0 |

## 3. Macro-Region Coverage

| Macro region | Rows |
|---|---:|
| North India | 73 |
| Central India | 17 |
| West India | 24 |
| South India | 40 |
| East India | 36 |
| North East India | 30 |
| Island India | 5 |

## 4. Priority Tier Coverage

| Priority tier | Rows |
|---|---:|
| `tier_1` | 110 |
| `tier_2` | 93 |
| `tier_3` | 22 |
| `tier_4` | 0 |

## 5. Invalid Destination Types

The following proposed location types are not currently in Destination Tag Dictionary v2:

| Invalid type | Candidate IDs | Recommendation |
|---|---|---|
| `waterfall_site` | `CAND-0087`, `CAND-0152` | Already added to v2 taxonomy; if validator shows invalid, sync validator constants |
| `river_island` | `CAND-0191`, `CAND-0192` | Already added to v2 taxonomy; if validator shows invalid, sync validator constants |
| `village` | `CAND-0200` | Use destination scale `village`; choose a destination type such as `culture_town` or add `culture_village` |
| `palace_site` | `CAND-0219`, `CAND-0220` | Already added to v2 taxonomy; if validator shows invalid, sync validator constants |

## 6. Invalid Vibe Tags

| Invalid vibe | Candidate IDs | Recommendation |
|---|---|---|
| `fort` | Multiple | Normalise to `forts` |
| `weekend` | Multiple | Move to trip style `weekend_getaway`; remove from vibe field |
| `gateway` | Multiple | Treat as route/access context; remove from vibe field or use location type `gateway_city` |
| `temple` | One or more | Normalise to `temples` |
| `craft` | Some rows | Either keep as accepted core vibe if validator updated, or normalise to `handicrafts` when object-specific |
| `marble` | Bhedaghat-style row | Review; consider `landscape`, `river`, or add a specific geology/landscape tag later |
| `border` | Dawki/Champhai-style rows | Move to caution `border_area_check` rather than vibe |
| `remote` | Remote island/valley rows | Move to access/planning caution rather than vibe |
| `parks` | City rows | Use `gardens`, `family`, or `urban` depending on intent |
| `viewpoint` | Some rows | Already added to v2 taxonomy; if validator shows invalid, sync validator constants |

## 7. Interpretation

The backlog is structurally strong enough to continue, but it should not yet be promoted directly into `destinations_master_v2.csv`.

Important findings:

1. Candidate IDs are unique.
2. No exact name-country or name-state duplicates were identified in the first QA pass.
3. The main quality issue is tag normalisation, not row duplication.
4. Some values currently placed in `proposed_vibe_*` are better modelled as trip-style tags, access context, caution tags, or destination scale.
5. This is expected because the backlog was created before the v2 tag dictionary was expanded.

## 8. Promotion Readiness

Current status:

```text
candidate backlog: usable for review
normalised backlog: pending
master promotion: not ready
Planner scoring: not ready
```

## 9. Next Actions

1. Create `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`.
2. Replace obvious non-standard vibes:
   - `fort` → `forts`
   - `temple` → `temples`
   - `weekend` → remove from vibe and later add as trip-style
   - `gateway` → remove from vibe if already represented in location type
   - `border` → move to caution tag later
   - `remote` → move to access/planning caution later
3. Add a QA browser for backlog validation results.
4. Build `destinations_master_v2.csv` only after normalisation.

## 10. Limitations

This QA report is a first-pass static report. A future run should compute results directly in CI or a local script, write a machine-readable QA JSON, and generate this markdown report automatically.
