# Destinations Master v2 Schema

This schema defines the canonical destination master dataset for CodeMike's destination database v2.

Target file:

```text
datasets/reference/destinations_master_v2.csv
```

## 1. Purpose

`destinations_master_v2.csv` is the controlled consolidation layer between raw/normalised candidate records and downstream enrichment/scoring.

It should combine:

- seed destinations from `india_region_destinations_seed.csv`
- clean normalised India candidate backlog rows from `destination_expansion_backlog_india_v1_normalized.csv`

It should not claim that records are verified or Planner-ready. It is a structured master reference layer, not a live travel-truth layer.

## 2. Source Inputs

| Input | Path | Role |
|---|---|---|
| Seed destinations | `datasets/reference/india_region_destinations_seed.csv` | Existing 134-row seed database |
| Normalised candidate backlog | `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv` | 225-row India candidate backlog after taxonomy cleanup |

## 3. Output Scope

Expected initial output scale:

```text
134 seed rows + 225 normalised candidate rows = up to 359 master rows
```

Exact output row count may be lower if future duplicate checks merge or suppress rows.

## 4. Master ID Format

Master destination IDs must use:

```text
DST2-000001
DST2-000002
DST2-000003
```

Rules:

- IDs are assigned deterministically by source group and input order in v1 of the promotion script.
- IDs should remain stable after first promotion unless a formal migration is recorded.
- Source IDs must remain in lineage fields.

## 5. Required Columns

| Column | Type | Required | Description |
|---|---|---:|---|
| `destination_master_id` | string | yes | Stable master ID, e.g. `DST2-000001` |
| `source_layer` | string | yes | `seed` or `normalized_candidate` |
| `source_id` | string | yes | Original source row ID, e.g. `destination_id` or `candidate_id` |
| `source_file` | string | yes | Input file path |
| `canonical_name` | string | yes | Canonical destination name |
| `alias_names` | string | no | Semicolon-separated aliases, blank if none |
| `country` | string | yes | Country |
| `macro_region` | string | yes | High-level regional bucket |
| `state_or_area` | string | yes | State, union territory, province, or area |
| `district_or_area` | string | no | District or smaller area where available |
| `destination_scale` | string | yes | `city`, `town`, `region`, `site`, `circuit`, etc. |
| `location_type` | string | yes | Controlled destination type from tag dictionary |
| `vibe_1` | string | no | Primary controlled vibe |
| `vibe_2` | string | no | Secondary controlled vibe |
| `vibe_3` | string | no | Tertiary controlled vibe |
| `trip_style_tags` | string | no | Semicolon-separated trip style tags |
| `context_tags` | string | no | Semicolon-separated context tags |
| `caution_tags` | string | no | Semicolon-separated caution tags |
| `budget_band` | string | no | Budget band if known |
| `family_suitability` | string | no | `low`, `low_medium`, `medium`, or `high` if known |
| `access_complexity` | string | no | `easy`, `moderate`, or `hard` if known |
| `best_season_hint` | string | no | Broad season hint, not live weather truth |
| `verification_status` | string | yes | Starts as `seed_unverified`, `candidate`, or `enriched_unverified` |
| `promotion_status` | string | yes | Workflow status such as `dedupe_pending` or `enrichment_pending` |
| `planner_use_status` | string | yes | `needs_verification` by default |
| `source_confidence` | string | yes | `none`, `low`, `medium`, `high`, or `official` |
| `source_notes` | string | no | Notes about source lineage or uncertainty |
| `normalisation_notes` | string | no | Notes from candidate normalisation if applicable |
| `master_notes` | string | no | Notes added during promotion |

## 6. Controlled Values

### 6.1 `source_layer`

Allowed values:

- `seed`
- `normalized_candidate`

### 6.2 `destination_scale`

Allowed values should follow `Destination Tag Dictionary v2`:

- `city`
- `town`
- `village`
- `district`
- `region`
- `circuit`
- `site`
- `park`
- `island`
- `resort_zone`
- `route`
- `unknown`

### 6.3 `verification_status`

Allowed values:

- `candidate`
- `seed_unverified`
- `enriched_unverified`
- `source_verified`
- `planner_ready`
- `retired`

Initial master generation rules:

- seed rows keep `seed_unverified`
- normalized candidate rows keep `candidate`

### 6.4 `promotion_status`

Allowed values:

- `candidate`
- `qa_pending`
- `dedupe_pending`
- `enrichment_pending`
- `source_pending`
- `review_ready`
- `planner_candidate`
- `planner_ready`
- `retired`

Initial master generation rules:

- seed rows default to `enrichment_pending`
- normalized candidate rows preserve `dedupe_pending` unless later promoted further

### 6.5 `planner_use_status`

Allowed values:

- `candidate`
- `needs_verification`
- `transfer_candidate`
- `planner_ready`
- `retired`

Initial master generation rule:

```text
planner_use_status = needs_verification
```

No destination should become `planner_ready` without verification and downstream scoring evidence.

## 7. Destination Scale Inference Rules

The first promotion script may infer `destination_scale` from `location_type` using broad rules.

Examples:

| Location type pattern | Destination scale |
|---|---|
| contains `_city` | `city` |
| contains `_town` | `town` |
| contains `_region` | `region` |
| contains `_site` | `site` |
| contains `_reserve` or `national_park` | `park` |
| contains `island` | `island` |
| contains `circuit` | `circuit` |
| contains `resort` | `resort_zone` |
| otherwise | `unknown` |

Manual review should refine this later.

## 8. Seed Row Mapping

Seed input columns map as follows:

| Seed column | Master column |
|---|---|
| `destination_id` | `source_id` |
| `name` | `canonical_name` |
| `country` | `country` |
| `macro_region` | `macro_region` |
| `state_or_area` | `state_or_area` |
| blank | `district_or_area` |
| inferred from `location_type` | `destination_scale` |
| `location_type` | `location_type` |
| `vibe_1` | `vibe_1` |
| `vibe_2` | `vibe_2` |
| `vibe_3` | `vibe_3` |
| blank | `trip_style_tags` |
| blank | `context_tags` |
| generated from heuristics later | `caution_tags` |
| `budget_band` | `budget_band` |
| `family_suitability` | `family_suitability` |
| `access_complexity` | `access_complexity` |
| `best_season_hint` | `best_season_hint` |
| `verification_status` | `verification_status` |

## 9. Normalised Candidate Row Mapping

Normalised candidate columns map as follows:

| Normalised candidate column | Master column |
|---|---|
| `candidate_id` | `source_id` |
| `name` | `canonical_name` |
| `country` | `country` |
| `macro_region` | `macro_region` |
| `state_or_area` | `state_or_area` |
| `district_or_area` | `district_or_area` |
| `destination_scale_hint` or inferred from type | `destination_scale` |
| `normalized_location_type` | `location_type` |
| `normalized_vibe_1` | `vibe_1` |
| `normalized_vibe_2` | `vibe_2` |
| `normalized_vibe_3` | `vibe_3` |
| `trip_style_tags` | `trip_style_tags` |
| `context_tags` | `context_tags` |
| `caution_tags` | `caution_tags` |
| blank | `budget_band` |
| blank | `family_suitability` |
| blank | `access_complexity` |
| blank | `best_season_hint` |
| `verification_status` | `verification_status` |
| `promotion_status` | `promotion_status` |
| `normalisation_notes` | `normalisation_notes` |

## 10. Deduplication Rules

Initial script should not automatically drop rows unless exact duplicate keys are found and the rule is explicit.

Recommended duplicate keys:

```text
lower(canonical_name) + country
lower(canonical_name) + state_or_area
```

First promotion pass should:

- flag duplicates in report
- preserve rows unless exact duplicate suppression is explicitly enabled
- keep lineage fields intact

## 11. Safety and Verification Rules

The master dataset must preserve this principle:

```text
Structured does not mean verified.
```

Rows may be structurally valid and still unsafe for live travel use.

Before Planner-ready status, verify:

- route feasibility
- permits
- visa/passport rules
- seasonality/weather
- safety
- medical access
- infant/family suitability
- source confidence

## 12. Promotion Script Requirements

Target script:

```text
src/codemike/data/destination_master_promotion.py
```

It should:

1. read seed CSV
2. read normalised candidate CSV
3. map rows into master schema
4. infer destination scale
5. assign stable `DST2-*` IDs
6. preserve source lineage
7. write `datasets/reference/destinations_master_v2.csv`
8. write a promotion report
9. print row counts and warnings

## 13. Master Validation Requirements

A future validator should check:

- required columns present
- unique `destination_master_id`
- unique source lineage key
- valid controlled values
- no blank canonical names
- no blank country/macro-region
- no invalid location types/vibes
- expected source-layer counts
- duplicates flagged

## 14. Next Files

After this schema, create:

```text
src/codemike/data/destination_master_promotion.py
reports/evidence/destination-master-v2-promotion-report.md
datasets/reference/destinations_master_v2.csv
```

Then later:

```text
src/codemike/data/destination_master_validation.py
reports/evidence/destination-master-v2-validation-report.md
docs/destination-master-browser-v1.html
```
