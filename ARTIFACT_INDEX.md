# ARTIFACT_INDEX.md — CodeMike Artifact Index

This file indexes important CodeMike artifacts so the workspace remains navigable as datasets, reports, scripts, and HTML review pages grow.

## Artifact Types

| Type | Meaning |
|---|---|
| Source data | Human-curated or primary project data |
| Generated data | Produced by scripts or transformation steps |
| Taxonomy | Controlled vocabulary or schema reference |
| Schema | Canonical field and mapping definition |
| Script | Reusable code utility |
| Evidence report | QA, analysis, or validation output |
| HTML artifact | Browser/review interface served through GitHub Pages |
| Tracker | Operational progress tracker |
| Decision log | Rationale for project design decisions |

## GitHub Pages Artifacts

| Artifact | URL | Source file | Status |
|---|---|---|---|
| CodeMike artifact landing page | `https://rishabh1804.github.io/MSc/` | `docs/index.html` | Active |
| Destination Browser v1 | `https://rishabh1804.github.io/MSc/destination-browser-v1.html` | `docs/destination-browser-v1.html` | Active, basic |
| Destination Browser v2 | `https://rishabh1804.github.io/MSc/destination-browser-v2.html` | `docs/destination-browser-v2.html` | Active, enriched prototype |
| Destination Tag Dictionary Browser | `https://rishabh1804.github.io/MSc/destination-tag-dictionary.html` | `docs/destination-tag-dictionary.html` | Active, taxonomy review |

## Destination Database Data Artifacts

| Artifact | Path | Type | Status | Notes |
|---|---|---|---|---|
| India and near-India seed database | `datasets/reference/india_region_destinations_seed.csv` | Source data | Active seed | 134 rows; seed-unverified |
| India expansion backlog v1 | `datasets/reference/destination_expansion_backlog_india_v1.csv` | Source/candidate data | Active backlog | 225 India-only candidate rows |
| Normalized India expansion backlog v1 | `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv` | Generated data | Generated | Produced by normalisation utility; clean validation completed |
| Destinations master v2 schema | `datasets/reference/destinations_master_v2_schema.md` | Schema | Active | Defines canonical master dataset fields and promotion rules |
| Destination database v2 strategy | `datasets/reference/destination_database_v2_strategy.md` | Strategy | Active | Defines scale-up architecture |
| Destination tag dictionary v2 | `datasets/reference/destination_tag_dictionary.md` | Taxonomy | Active | Controlled vocabulary for destination work |

## Destination Database Scripts

| Script | Path | Purpose | Status |
|---|---|---|---|
| Candidate backlog taxonomy validator | `src/codemike/data/destination_taxonomy_validation.py` | Validates raw candidate backlog against taxonomy | Active prototype |
| Candidate backlog normaliser | `src/codemike/data/destination_backlog_normalization.py` | Produces normalized backlog CSV | Active prototype |
| Normalized backlog validator | `src/codemike/data/destination_normalized_validation.py` | Validates normalized backlog fields | Active prototype; clean report generated |
| Master promotion script | `src/codemike/data/destination_master_promotion.py` | Promotes seed + normalized candidates into master CSV | Pending |

## Destination Database Evidence Reports

| Report | Path | Status | Notes |
|---|---|---|---|
| Destination database QA v1 | `reports/evidence/destination-database-qa-v1.md` | Active | QA of seed database and enrichment strategy |
| Candidate backlog taxonomy QA v1 | `reports/evidence/destination-candidate-backlog-taxonomy-qa-v1.md` | Active | First validation pass on raw 225-row candidate backlog |
| Candidate backlog normalisation v1 | `reports/evidence/destination-candidate-backlog-normalisation-v1.md` | Active | Documents normalisation utility and rules |
| Normalized backlog validation v1 | `reports/evidence/destination-normalized-backlog-validation-v1.md` | Active, clean | Confirms normalized backlog is clean enough for master promotion design |
| Destination database work-done report v1 | `reports/work-done/code-mike-destination-database-work-done-v1.md` | Active checkpoint | Summarises work done so far |

## Trackers and Operating Files

| File | Path | Purpose | Status |
|---|---|---|---|
| Destination database build tracker | `trackers/destination-database-build-tracker.md` | Tracks data pipeline progress | Active |
| Next actions | `NEXT_ACTIONS.md` | Operational queue | Active |
| Decision log | `DECISIONS.md` | Records project rationale | Active |
| Project log | `PROJECT_LOG.md` | Chronological milestone log | Active |
| Dataset registry | `DATASETS.md` | Dataset-level registry | Active |

## Current Source-of-Truth Rules

- Markdown strategy and taxonomy files define intent and vocabulary.
- Markdown schema files define canonical data shape.
- CSV files define data layers.
- Python scripts define repeatable transformations and validation.
- Evidence reports document observed results.
- HTML artifacts are review interfaces, not source of truth.
- Generated files should be reproducible from committed scripts wherever practical.

## Immediate Gaps

- Master promotion script does not exist yet.
- Master destination CSV does not exist yet.
- Master validation report does not exist yet.
- HTML QA browser for normalized/master records does not exist yet.
- Scoring module for destination selection does not exist yet.
