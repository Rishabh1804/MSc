# Destination Database Build Tracker

This tracker records the build state of CodeMike's destination database system.

## Current Status Summary

```text
Current phase: master validation
Next major phase: master HTML browser
Current structured coverage: 359 master rows
Planner-ready rows: 0
```

## Build Pipeline

| Stage | Artifact | Status | Owner/Mode | Notes |
|---|---|---|---|---|
| Seed database | `datasets/reference/india_region_destinations_seed.csv` | done | Assistant | 134 rows; seed-unverified |
| Browser v1 | `docs/destination-browser-v1.html` | done | Assistant | Basic Pages browser |
| Browser v2 | `docs/destination-browser-v2.html` | done | Assistant | Client-side heuristic enrichment |
| QA report for seed | `reports/evidence/destination-database-qa-v1.md` | done | Assistant | Documents limitations and enrichment strategy |
| V2 strategy | `datasets/reference/destination_database_v2_strategy.md` | done | Assistant | Scale-up architecture |
| Tag dictionary v2 | `datasets/reference/destination_tag_dictionary.md` | done | Assistant | Expanded taxonomy |
| Tag dictionary browser | `docs/destination-tag-dictionary.html` | done | Assistant | HTML review artifact |
| India candidate backlog | `datasets/reference/destination_expansion_backlog_india_v1.csv` | done | Assistant | 225 candidate rows |
| Raw backlog taxonomy validator | `src/codemike/data/destination_taxonomy_validation.py` | done | Assistant | Validates raw candidate backlog |
| Raw backlog QA report | `reports/evidence/destination-candidate-backlog-taxonomy-qa-v1.md` | done | Assistant | First-pass taxonomy QA |
| Backlog normaliser | `src/codemike/data/destination_backlog_normalization.py` | done | Assistant | Normalises raw backlog |
| Normalised backlog | `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv` | done | User / Termux | Generated and pushed |
| Normalised backlog validator | `src/codemike/data/destination_normalized_validation.py` | done | Assistant | Updated for final six concepts |
| Clean normalised validation report | `reports/evidence/destination-normalized-backlog-validation-v1.md` | done | User / Termux | Clean enough for master promotion design |
| Master schema | `datasets/reference/destinations_master_v2_schema.md` | done | Assistant | Canonical schema and mapping rules created |
| Master promotion script | `src/codemike/data/destination_master_promotion.py` | done | Assistant | Ready for Termux generation |
| Master dataset | `datasets/reference/destinations_master_v2.csv` | done | User / Termux | 359 rows generated and pushed |
| Master promotion report | `reports/evidence/destination-master-v2-promotion-report.md` | done | User / Termux | Confirms 359 rows, no exact duplicate name keys |
| Master validation script | `src/codemike/data/destination_master_validation.py` | done | Assistant | Ready for Termux validation |
| Master validation report | `reports/evidence/destination-master-v2-validation-report.md` | todo | User / Termux | Needs computed run |
| Master HTML browser | TBD | todo | Assistant | Review layer for master dataset |
| Destination scoring v1 | `src/codemike/recommendation/destination_scoring.py` | deferred | Assistant | After master browser exists |
| Planner transfer report | TBD | deferred | Assistant | After scoring evidence |

## Data Quality Gates

A row should not move to master without:

- stable ID
- valid normalized destination type
- valid normalized vibe tags
- explicit promotion status
- verification status
- source confidence placeholder
- no exact duplicate destination key

A row should not move to Planner-ready without:

- source verification
- current safety/route/visa/permit review where applicable
- medical access confidence review
- infant/family suitability review
- scoring evidence

## Current Build Requirement

Run:

```text
src/codemike/data/destination_master_validation.py
```

The script should generate:

```text
reports/evidence/destination-master-v2-validation-report.md
```

Expected readiness if clean:

```text
master_structurally_valid_not_planner_ready
```

## Next Termux Command

```bash
cd ~/projects/MSc
git pull
python src/codemike/data/destination_master_validation.py
git status
git add reports/evidence/destination-master-v2-validation-report.md
git commit -m "Generate destinations master v2 validation report"
git push
```

## Milestone Criteria

### Master Schema Ready

- clean normalised validation report exists
- master schema is documented
- promotion mapping is clear

Status: done.

### Master Dataset Ready

- master CSV generated
- seed + candidate lineage preserved
- exact duplicates checked
- statuses clear

Status: done.

### Master Browser Ready

- master validation clean or known issues documented
- HTML browser created
- Pages index updated

Status: pending.

### Planner Candidate Ready

- enriched fields exist
- scoring module exists
- evidence report exists
- unverified rows remain blocked from live/travel-truth use

Status: deferred.
