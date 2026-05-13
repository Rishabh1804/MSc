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
| Design foundation | UI/UX learning and design criteria artifact |
| Assignment | Formal CodeMike learning/evidence assignment |
| Rubric | Marking criteria for an assignment |
| Checklist | Operational or design review checklist |
| Tracker | Operational progress tracker |
| Decision log | Rationale for project design decisions |

## GitHub Pages Artifacts

| Artifact | URL | Source file | Status |
|---|---|---|---|
| CodeMike artifact landing page | `https://rishabh1804.github.io/MSc/` | `docs/index.html` | Active |
| Design Foundations Study Dashboard | `https://rishabh1804.github.io/MSc/design-foundations.html` | `docs/design-foundations.html` | Active, assignment artifact for DES-001 |
| Destinations Master v2 Browser | `https://rishabh1804.github.io/MSc/destination-master-browser-v1.html` | `docs/destination-master-browser-v1.html` | Active, 359-row master review |
| Destination Browser v1 | `https://rishabh1804.github.io/MSc/destination-browser-v1.html` | `docs/destination-browser-v1.html` | Active, basic |
| Destination Browser v2 | `https://rishabh1804.github.io/MSc/destination-browser-v2.html` | `docs/destination-browser-v2.html` | Active, enriched prototype |
| Destination Tag Dictionary Browser | `https://rishabh1804.github.io/MSc/destination-tag-dictionary.html` | `docs/destination-tag-dictionary.html` | Active, taxonomy review |

## Assignment Artifacts

| Artifact | Path | Type | Status | Notes |
|---|---|---|---|---|
| DES-001 assignment brief | `assignments/DES-001-design-foundations-study-dashboard.md` | Assignment | Assigned | Formalises design foundations dashboard as first graded CodeMike assignment |
| DES-001 marking rubric | `assignments/rubrics/design-foundations-rubric.md` | Rubric | Active | 100-mark rubric with resubmission and benchmark rules |
| DES-001 submission v1 | `assignments/submissions/DES-001/submission-v1.md` | Assignment submission | Pending | To be created after deep-reading completion |
| DES-001 review v1 | `assignments/reviews/DES-001/review-v1.md` | Assignment review | Pending | To be created after submission |

## Design Foundation Artifacts

| Artifact | Path | Type | Status | Notes |
|---|---|---|---|---|
| Figma design basics digest | `design/foundations/figma-design-basics-digest.md` | Design foundation | Active | Captures UI principles, Gestalt, design thinking, and browser translation |
| CodeMike UI learning map | `design/foundations/code-mike-ui-learning-map.md` | Design foundation | Active | Defines design-learning sequence and competency ladder |
| Master browser design checklist | `design/checklists/master-browser-design-checklist.md` | Checklist | Active | Defines criteria for browser v1.1 redesign |

## Destination Database Data Artifacts

| Artifact | Path | Type | Status | Notes |
|---|---|---|---|---|
| India and near-India seed database | `datasets/reference/india_region_destinations_seed.csv` | Source data | Active seed | 134 rows; seed-unverified |
| India expansion backlog v1 | `datasets/reference/destination_expansion_backlog_india_v1.csv` | Source/candidate data | Active backlog | 225 India-only candidate rows |
| Normalized India expansion backlog v1 | `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv` | Generated data | Generated | Produced by normalisation utility; clean validation completed |
| Destinations master v2 schema | `datasets/reference/destinations_master_v2_schema.md` | Schema | Active | Defines canonical master dataset fields and promotion rules |
| Destinations master v2 CSV | `datasets/reference/destinations_master_v2.csv` | Generated data | Generated | 359-row master reference layer, not Planner-ready |
| Destination database v2 strategy | `datasets/reference/destination_database_v2_strategy.md` | Strategy | Active | Defines scale-up architecture |
| Destination tag dictionary v2 | `datasets/reference/destination_tag_dictionary.md` | Taxonomy | Active | Controlled vocabulary for destination work |

## Destination Database Scripts

| Script | Path | Purpose | Status |
|---|---|---|---|
| Candidate backlog taxonomy validator | `src/codemike/data/destination_taxonomy_validation.py` | Validates raw candidate backlog against taxonomy | Active prototype |
| Candidate backlog normaliser | `src/codemike/data/destination_backlog_normalization.py` | Produces normalized backlog CSV | Active prototype |
| Normalized backlog validator | `src/codemike/data/destination_normalized_validation.py` | Validates normalized backlog fields | Active prototype; clean report generated |
| Master promotion script | `src/codemike/data/destination_master_promotion.py` | Promotes seed + normalized candidates into master CSV | Active; generated master CSV |
| Master validation script | `src/codemike/data/destination_master_validation.py` | Validates master CSV against master schema | Active; clean report generated |

## Destination Database Evidence Reports

| Report | Path | Status | Notes |
|---|---|---|---|
| Destination database QA v1 | `reports/evidence/destination-database-qa-v1.md` | Active | QA of seed database and enrichment strategy |
| Candidate backlog taxonomy QA v1 | `reports/evidence/destination-candidate-backlog-taxonomy-qa-v1.md` | Active | First validation pass on raw 225-row candidate backlog |
| Candidate backlog normalisation v1 | `reports/evidence/destination-candidate-backlog-normalisation-v1.md` | Active | Documents normalisation utility and rules |
| Normalized backlog validation v1 | `reports/evidence/destination-normalized-backlog-validation-v1.md` | Active, clean | Confirms normalized backlog is clean enough for master promotion design |
| Master v2 promotion report | `reports/evidence/destination-master-v2-promotion-report.md` | Active | Confirms 359 master rows generated with no duplicate name keys |
| Master v2 validation report | `reports/evidence/destination-master-v2-validation-report.md` | Active, clean | Confirms master is structurally valid but not Planner-ready |
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

- Assignment briefs define learning tasks and expected outputs.
- Rubrics define assessment and benchmark promotion standards.
- Markdown strategy and taxonomy files define intent and vocabulary.
- Markdown schema files define canonical data shape.
- Design foundation files define UI/UX criteria before redesign.
- CSV files define data layers.
- Python scripts define repeatable transformations and validation.
- Evidence reports document observed results.
- HTML artifacts are review interfaces, not source of truth.
- Generated files should be reproducible from committed scripts wherever practical.

## Immediate Gaps

- DES-001 deep reading is not complete yet.
- DES-001 submission and review files do not exist yet.
- Current master browser has not yet been upgraded against the design checklist.
- Destination enrichment strategy for master records does not exist yet.
- Scoring module for destination selection does not exist yet.
- Planner transfer report does not exist yet.
