# Destination Database Build Tracker

This tracker records the build state of CodeMike's destination database system.

## Current Status Summary

```text
Current phase: normalized backlog validation cleanup
Next major phase: destinations_master_v2 schema design
Current structured coverage: 134 seed rows + 225 candidate rows = 359 rows
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
| Clean normalised validation report | `reports/evidence/destination-normalized-backlog-validation-v1.md` | todo | User / Termux | Needs rerun after taxonomy cleanup |
| Master schema | `datasets/reference/destinations_master_v2_schema.md` | todo | Assistant | Next design step |
| Master promotion script | `src/codemike/data/destination_master_promotion.py` | todo | Assistant | Will generate master CSV |
| Master dataset | `datasets/reference/destinations_master_v2.csv` | todo | User / Termux | Not created yet |
| Master QA report | TBD | todo | Assistant/User | After master CSV exists |
| Master HTML browser | TBD | todo | Assistant | Review layer for master dataset |
| Destination scoring v1 | `src/codemike/recommendation/destination_scoring.py` | deferred | Assistant | After master dataset exists |
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

## Current Clean-Up Requirement

The last computed validation report showed:

```text
Invalid normalized destination types: 3
Invalid normalized vibe tags: 3
```

The taxonomy and validator have now been updated to accept:

```text
culture_town
lake_hill_station
mountain_resort
monastery
rain
rock_carving
```

Expected next validation result:

```text
Invalid normalized destination types: 0
Invalid normalized vibe tags: 0
Readiness: clean_enough_for_master_promotion_design
```

## Next Termux Command

```bash
cd ~/projects/MSc
git pull
python src/codemike/data/destination_normalized_validation.py
git status
git add reports/evidence/destination-normalized-backlog-validation-v1.md
git commit -m "Regenerate clean normalized destination backlog validation report"
git push
```

## Milestone Criteria

### Master Schema Ready

- clean normalised validation report exists
- master schema is documented
- promotion mapping is clear

### Master Dataset Ready

- master CSV generated
- seed + candidate lineage preserved
- exact duplicates checked
- statuses clear

### Planner Candidate Ready

- enriched fields exist
- scoring module exists
- evidence report exists
- unverified rows remain blocked from live/travel-truth use
