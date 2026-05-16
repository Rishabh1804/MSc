# PROJECT_LOG.md — CodeMike Project Log

This file records material progress, decisions, setup work, and milestone changes for the MSc CodeMike workspace.

## Log Rules

Add an entry when:

- a root governance file changes materially
- a new module or folder is created
- a capability becomes reusable
- an experiment produces evidence
- a skill maturity level changes
- a paid tool is proposed or approved
- a capability transfers to another project
- a risk, failure, or important limitation is identified

## Entry Template

```md
## YYYY-MM-DD — Title

Type: setup / learning / experiment / capability / transfer / review / risk / budget

Summary:

Files changed:

Evidence produced:

Next action:
```

## 2026-05-16 — DES-001 Topic 2 closed (deep reading + Lab 02 + rule sheet)

Type: learning / assignment / capability

Summary:

Closed DES-001 Topic 2 — What is UI design. Two PRs land the topic: PR A produces the deep-reading evidence (source-by-source notes across Material Design 3, Apple HIG, IBM Carbon, GOV.UK Design System, Don Norman; source comparison; CodeMike interpretation; browser application; anti-patterns; v1.1 implementation backlog; checklist updates). PR B executes Lab 02 (20-pattern inventory + state-coverage matrix + affordance/signifier/feedback audit + container-selection rules + filter-UI rules + consolidated rule sheet) and appends six Topic 2 component gates to the master-browser checklist.

Structural insight from the topic: the Destination Master Browser is a *master-detail data-review tool with faceted filtering* (Carbon pattern vocabulary). Naming the pattern fixes most v1.1 component choices: table by default with cards as secondary, drawer for detail (never modal), filter chips + dropdowns + search for narrowing, content-rich empty state with Clear-all recovery, skeleton loading, inline error notification, and a four-depth trust signal (top banner + list row + drawer header + future confirm-modal).

The five required sources differ less on definition than on emphasis — modality (Material permissive vs HIG/Carbon/GOV.UK restrictive), data-table prominence (Carbon first-class vs others light), and "when not to use" discipline (GOV.UK explicit vs others implicit). For this product, the HIG/Carbon/GOV.UK majority position wins on modality; Carbon's table-and-pattern vocabulary wins on the central reviewer task; GOV.UK's negative-space discipline becomes a checklist gate.

Files changed:

- `design/foundations/topic-02-what-is-ui-design.md` (new — 13-section deep-reading doc)
- `design/foundations/topic-02-ui-design-component-inventory.md` (new — Lab 02 Steps 1–3)
- `design/foundations/ui-design-component-rules.md` (new — Lab 02 Steps 4–6; Browser v1.1's input)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-02-what-is-ui-design-answers.md` (new — ten worked answers)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-questions.md` + `-answers.md` (Topic 2 questions and answers appended)
- `curriculum/courses/des-001-design-foundations/submissions/lab-02-ui-design-component-inventory-results.md` (new — formal Lab 02 submission)
- `design/checklists/master-browser-design-checklist.md` (§18 six Topic 2 gates + §19 canonical rule-sheet pointer)
- `docs/design-foundations-app/data.js` (Topic 2 module flipped to `done`; sources expanded from three to six; full notes object attached; Playwright re-verified)
- `curriculum/courses/des-001-design-foundations/competency-map.md`, `weekly-plan.md`, `learning-log.md`, `submissions/DES-001-submission.md`, `revisions/DES-001-revision-plan-v1.md`, `feedback/DES-001-grade-report-v1.md` (tracking files updated; Topic 2 marked closed; revision item 5 closed)

Evidence produced:

- 20-pattern v1 component inventory with element-category classification
- 12-pattern missing-pattern list (the v1.1 backlog)
- 20 × 9 state-coverage matrix with severity-ranked findings (3 HIGH + 4 MEDIUM)
- Affordance / signifier / feedback audit per interactive pattern; three cross-cutting findings (F1 active-state, F2 trust-signal depth, F3 three-states-one-component)
- Container-selection rule sheet (card / table / list / drawer / modal) with when-to-use + when-not-to-use + sources + decision tree
- Filter-UI rule sheet (search / chip / dropdown / faceted panel) with decision tree
- Four-depth trust-signal specification with seven trust states
- Six Topic 2 checklist gates appended to the master-browser checklist
- Three reusable CodeMike design capabilities extracted from the topic (master-detail-with-faceted-search pattern card; nine-state interactive checklist; affordance-signifier-feedback triple-check)

Next action:

Start Topic 3 — UX design. Browser v1.1 implementation remains gated on Topic 3 closing per the ratified execution plan.

## 2026-05-16 — DES-001 execution plan ratified and Topic 1 close-out

Type: learning / assignment / assessment / governance

Summary:

Ratified the DES-001 execution plan (all four §1 decisions confirmed as the recommended option: full 12-topic scope, per-topic sequencing, Browser v1.1 implementation after Topic 3, dashboard rename). Closed four of the six required revisions from the Topic 1 grade report.

Live visual verification of the modular dashboard ran under Playwright/Chromium against `file://` URLs in the remote execution container. All six promotion-rule conditions from `docs/design-foundations-app/README.md` passed: rendering, CSS, zero console errors, Topic 1 extension link, sync.js validation, layout equivalence with the legacy single-file dashboard. The rename then executed: `docs/design-foundations-v2.html` → `docs/design-foundations.html` (canonical, matching the assignment brief); `docs/design-foundations.html` (the 418-line monolithic predecessor) → `docs/design-foundations-v1.html` (archived). A second Playwright run against the canonical filename confirmed the rename did not break the relative `design-foundations-app/` script paths. Topic 1 quiz answers and viva answers were written to round out the close-out.

Files changed:

- `docs/design-foundations.html` (formerly `design-foundations-v2.html`)
- `docs/design-foundations-v1.html` (formerly `design-foundations.html`)
- `docs/design-foundations-app/config.js` (primaryArtifact and legacyArtifact paths swapped; version label updated)
- `docs/design-foundations-app/README.md` (Promotion rule section closed; verification result recorded)
- `curriculum/courses/des-001-design-foundations/verification/` (new — verification report and screenshots)
- `curriculum/courses/des-001-design-foundations/quizzes/quiz-01-ui-vs-ux-answers.md` (new)
- `curriculum/courses/des-001-design-foundations/viva/DES-001-viva-answers.md` (new)
- `curriculum/courses/des-001-design-foundations/feedback/DES-001-grade-report-v1.md` (items 1–4 of Required revisions marked closed)
- `curriculum/courses/des-001-design-foundations/revisions/DES-001-revision-plan-v1.md` (items 1–3 closed; revision-log rows added)
- `README.md`, `docs/repo-map.html`, `curriculum/courses/README.md`, course-level `README.md`/`syllabus.md`/`learning-log.md`/`submissions/DES-001-submission.md` (all `design-foundations-v2.html` references updated to the canonical filename)

Evidence produced:

- Playwright verification report at `curriculum/courses/des-001-design-foundations/verification/dashboard-visual-verification-2026-05-16.md`
- Three full-page screenshots (pre-rename v2, pre-rename above-the-fold, post-rename canonical) in `curriculum/courses/des-001-design-foundations/verification/`
- Defensible viva answers covering all eight Topic 1 questions with examiner-push follow-ups
- Self-marked quiz answers grounded in the Destination Master Browser

Next action:

Open the PR for this close-out work. After it merges, execute Topic 2 (the scaffold landed in PR #3): five-source deep reading, source comparison, and Lab 02 — producing the component rule sheet that becomes Browser v1.1's input.

## 2026-05-12 — DES-001 assignment and rubric created

Type: learning / assignment / assessment

Summary:

Formalised the Design Foundations Study Dashboard as CodeMike's first graded assignment: DES-001. The assignment frames `docs/design-foundations.html` as a reviewable university-style submission with multi-source deep reading, notes generation, further reading suggestions, grading, resubmission rules, and benchmark-promotion criteria.

Files changed:

- `assignments/DES-001-design-foundations-study-dashboard.md`
- `assignments/rubrics/design-foundations-rubric.md`
- `ARTIFACT_INDEX.md`

Evidence produced:

- DES-001 assignment brief
- 100-mark marking rubric
- grading bands: Fail, Pass, Good, Excellent, Benchmark
- automatic cap rules for weak source comparison or unsafe claims
- benchmark eligibility criteria
- resubmission rules

Next action:

Begin DES-001 deep reading with Topic 1: UI vs UX. Update `docs/design-foundations.html` with notes, source comparison, browser implications, anti-patterns, and further reading.

## 2026-05-12 — Seed compatibility cleanup completed

Type: taxonomy / validation / QA

Summary:

Updated the destination tag dictionary and master validator to accept legitimate legacy seed concepts found in the original 134-row seed dataset. These values are now treated as seed-compatible vocabulary: structurally valid for master ingestion, but still subject to future enrichment and normalization review.

Files changed:

- `datasets/reference/destination_tag_dictionary.md`
- `src/codemike/data/destination_master_validation.py`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- accepted seed-compatible location types including `beach_city`, `culture_hill_town`, `desert_beach_emirate`, `heritage_capital`, `hill_heritage_city`, `island_heritage_city`, `island_resort_district`, `lake_mountain_city`, `mountain_capital`, `mountain_valley`, `northern_city`, and `wildlife_region`
- accepted seed-compatible vibe tags including `city`, `limestone`, `monsoon`, `museums`, `relaxation`, `stopover`, and `villa`

Next action:

Rerun `python src/codemike/data/destination_master_validation.py` in Termux and commit the regenerated clean validation report.

## 2026-05-12 — Destinations master v2 validation utility created

Type: dataset / validation / QA

Summary:

Created the master validation utility for `destinations_master_v2.csv`. The validator checks row count, required columns, unique master IDs, source lineage keys, duplicate name keys, critical blanks, controlled statuses, destination scales, location types, vibe tags, trip-style tags, context tags, caution tags, and source-confidence values.

Files changed:

- `src/codemike/data/destination_master_validation.py`
- `reports/evidence/destination-master-v2-validation-report.md`
- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- reusable master validation script
- validation report scaffold
- Termux command path for computed validation

Next action:

Run the master validation script in Termux and commit the computed validation report. If structurally clean, create a master HTML browser.

## 2026-05-12 — Destinations master v2 promotion script created

Type: dataset / script / promotion

Summary:

Created the master promotion utility that will combine the 134-row seed dataset and 225-row clean normalized candidate backlog into `destinations_master_v2.csv`. The script maps both sources into the master schema, assigns stable `DST2-*` IDs, preserves source lineage, infers destination scale, and writes a promotion report.

Files changed:

- `src/codemike/data/destination_master_promotion.py`
- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- reusable master promotion script
- generated-output plan for `datasets/reference/destinations_master_v2.csv`
- generated-output plan for `reports/evidence/destination-master-v2-promotion-report.md`

Next action:

Run the master promotion script in Termux and commit the generated master CSV and promotion report.

## 2026-05-12 — Destinations master v2 schema created

Type: dataset / schema / promotion

Summary:

Created the canonical master schema for consolidating the 134-row seed dataset and 225-row clean normalized candidate backlog into `destinations_master_v2.csv`. The schema defines stable master IDs, lineage fields, destination scale, taxonomy fields, workflow statuses, verification placeholders, Planner-use status, and promotion rules.

Files changed:

- `datasets/reference/destinations_master_v2_schema.md`
- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`

Evidence produced:

- master field definition
- seed-to-master mapping
- normalized-candidate-to-master mapping
- initial deduplication and safety rules
- promotion script requirements

Next action:

Create `src/codemike/data/destination_master_promotion.py`, then generate `datasets/reference/destinations_master_v2.csv` from Termux.

## 2026-05-12 — Artifact-management layer created

Type: artifact / tracker / governance

Summary:

Created a lightweight artifact-management layer for the CodeMike destination database work. This adds a central artifact index, operational next-actions tracker, decision log, destination database build tracker, and a work-done checkpoint report.

Files changed:

- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `DECISIONS.md`
- `trackers/destination-database-build-tracker.md`
- `reports/work-done/code-mike-destination-database-work-done-v1.md`

Evidence produced:

- central map of source data, generated data, scripts, reports, trackers, and HTML review artifacts
- decision rationale for layered data architecture, taxonomy-first build, unverified-data handling, and Termux execution
- operational queue for the next validation and master-schema steps
- checkpoint report summarising the destination database work completed so far

Next action:

Run the clean normalized backlog validation in Termux, then proceed to `datasets/reference/destinations_master_v2_schema.md`.

## 2026-05-12 — Remaining destination taxonomy cleanup completed

Type: taxonomy / validation / QA

Summary:

Added the six remaining normalized backlog concepts to the destination taxonomy and normalized backlog validator so the next validation run can reach zero invalid destination types and zero invalid vibe tags.

Files changed:

- `datasets/reference/destination_tag_dictionary.md`
- `src/codemike/data/destination_normalized_validation.py`

Evidence produced:

- accepted destination types: `culture_town`, `lake_hill_station`, `mountain_resort`
- accepted vibe tags: `monastery`, `rain`, `rock_carving`

Next action:

Run `python src/codemike/data/destination_normalized_validation.py` and commit the regenerated computed validation report. If clean, proceed to `datasets/reference/destinations_master_v2_schema.md`.

## 2026-05-12 — Normalized destination backlog validation utility created

Type: dataset / QA / validation

Summary:

Created a validation utility for the normalized 225-row India destination backlog. The validator checks required columns, duplicate keys, normalized destination types, normalized vibes, trip-style tags, context tags, and promotion statuses before master schema design.

Files changed:

- `src/codemike/data/destination_normalized_validation.py`
- `reports/evidence/destination-normalized-backlog-validation-v1.md`

Evidence produced:

- normalized backlog validation readiness rule
- report scaffold for computed validation output

Next action:

Run the validator and commit the regenerated computed report if it changes. Then create `datasets/reference/destinations_master_v2_schema.md`.

## 2026-05-12 — Destination backlog normalisation utility created

Type: dataset / QA / normalisation

Summary:

Created the destination backlog normalisation utility for converting the raw 225-row India expansion backlog into a cleaner intermediate file before master promotion. The utility separates true vibes from trip-style tags, context tags, caution tags, and destination-scale hints.

Files changed:

- `src/codemike/data/destination_backlog_normalization.py`
- `reports/evidence/destination-candidate-backlog-normalisation-v1.md`

Evidence produced:

- normalisation rules for raw candidate values such as `fort`, `temple`, `weekend`, `gateway`, `remote`, and `border`
- report documenting the expected output and next execution artifact

Next action:

Run the normalisation script and commit `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`.

## 2026-05-12 — Destination candidate backlog taxonomy QA created

Type: dataset / QA / taxonomy

Summary:

Created the first taxonomy validation utility and QA report for the 225-row India destination candidate backlog. The pass checks candidate IDs, duplicate name keys, destination types, vibe tags, priority tiers, and verification statuses against Destination Tag Dictionary v2.

Files changed:

- `src/codemike/data/destination_taxonomy_validation.py`
- `reports/evidence/destination-candidate-backlog-taxonomy-qa-v1.md`

Evidence produced:

- first candidate backlog taxonomy QA report
- identified tag normalisation issues before master promotion
- confirmed candidate ID uniqueness and no exact name-country/name-state duplicates in the first pass

Next action:

Create `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv` before building `destinations_master_v2.csv`.

## 2026-05-12 — Destination tag dictionary v2 and HTML browser created

Type: taxonomy / artifact / interface

Summary:

Expanded the destination tag dictionary into v2 and created a GitHub Pages HTML browser for taxonomy review. The taxonomy now covers destination scale, destination types, vibes, traveller fit, trip styles, caution tags, source confidence, source types, and workflow statuses.

Files changed:

- `datasets/reference/destination_tag_dictionary.md`
- `docs/destination-tag-dictionary.html`
- `docs/index.html`

Evidence produced:

- expanded controlled vocabulary for destination database v2
- interactive taxonomy browser
- Pages landing page link for tag dictionary review

Next action:

Use the tag dictionary to validate the 225-row India candidate backlog and identify non-standard tags before promotion.

## 2026-05-12 — Destination database v2 massive expansion setup

Type: dataset / reference / strategy

Summary:

Started the destination database v2 scale-up. Added a strategy document for building a massive Planner-ready destination database, a controlled tag dictionary, and a 225-row India-only expansion backlog. The system now separates seed destinations from candidate backlog entries so the database can grow without contaminating Planner-ready records.

Files changed:

- `datasets/reference/destination_database_v2_strategy.md`
- `datasets/reference/destination_tag_dictionary.md`
- `datasets/reference/destination_expansion_backlog_india_v1.csv`
- `DATASETS.md`

Evidence produced:

- target scale strategy from 250 rows to 5,000+ rows
- controlled destination vocabulary
- 225 India expansion candidates
- dataset registry scale snapshot showing 359 total seed + candidate records

Next action:

Create a QA/deduplication and promotion pipeline that converts selected backlog candidates into enriched destination records.

## 2026-05-12 — Destination browser v2 and QA report created

Type: artifact / evidence / interface

Summary:

Created a destination database QA report and a GitHub Pages-compatible enriched destination browser v2. Browser v2 loads the 134-row destination seed CSV and applies client-side heuristic enrichment for Planner-style review.

Files changed:

- `reports/evidence/destination-database-qa-v1.md`
- `docs/destination-browser-v2.html`
- `docs/index.html`

Evidence produced:

- destination database QA v1 report
- enriched browser with origin-fit, infant-suitability, fatigue, planning-complexity, medical-access, and Planner-readiness filters
- Pages landing page updated with v2 link

Next action:

Stabilise enrichment rules into a committed enriched CSV or add destination scoring v1 using the v2 enrichment fields.

## 2026-05-05 — HTML artifact layer and destination browser created

Type: artifact / interface

Summary:

Added CodeMike's HTML artifact layer and created the first standalone HTML review artifact: a filterable destination browser for the India and near-India seed database.

Files changed:

- `HTML_ARTIFACTS.md`
- `artifacts/html/README.md`
- `artifacts/html/destination-browser-v1.html`

Evidence produced:

- HTML artifact operating guide
- standalone interactive browser for destination seed review
- visual inspection layer for region, country, type, budget, family suitability, and access complexity

Next action:

Create an enriched destination dataset and update the browser to use enrichment fields such as origin fit, infant suitability, travel fatigue, and planner use status.

## 2026-05-05 — Destination reference database seed created

Type: dataset / reference

Summary:

Started expanding CodeMike's destination database beyond the synthetic trip-options experiment. Added a reference dataset area, schema, and a 134-row seed database covering India and nearby/regionally relevant international destinations.

Files changed:

- `datasets/reference/README.md`
- `datasets/reference/india_region_destinations_schema.md`
- `datasets/reference/india_region_destinations_seed.csv`
- `DATASETS.md`

Evidence produced:

- reference destination schema
- 134-row India and near-India destination seed dataset
- dataset registry entry

Next action:

Create a destination database QA/enrichment pass: region coverage check, duplicate check, schema validation, and fields for nearest airport, origin fit, infant suitability, and verification sources.

## 2026-05-05 — Recommendation scoring source module extracted

Type: productisation / capability

Summary:

Converted the trip-options scoring logic from EXP-001 and EXP-002 into a reusable Python module under `src/codemike/recommendation/`. This begins the productisation path from experiment to reusable source code.

Files changed:

- `src/codemike/__init__.py`
- `src/codemike/recommendation/__init__.py`
- `src/codemike/recommendation/trip_scoring.py`
- `src/codemike/recommendation/README.md`
- `EVIDENCE.md`

Evidence produced:

- reusable source module for scoring and sensitivity ranking
- module documentation
- evidence entry for module extraction

Next action:

Add unit tests and a small CLI/example runner before Planner transfer.

## 2026-05-05 — Recommendation sensitivity analysis v1.1 completed

Type: experiment / evidence

Summary:

Completed sensitivity analysis for the trip-options recommendation scoring experiment. Tested five priority scenarios and identified stable versus preference-sensitive recommendations.

Files changed:

- `datasets/processed/trip_options_sensitivity_v1_1.csv`
- `reports/experiment-reports/trip-options-sensitivity-v1-1.md`
- `EXPERIMENTS.md`
- `EVIDENCE.md`

Evidence produced:

- EXP-002 sensitivity analysis
- scenario-ranked dataset
- stable top recommendation set
- preference-sensitive premium option insight

Next action:

Create a Planner transfer candidate or convert scoring logic into a reusable module under `src/`.

## 2026-05-05 — Recommendation scoring v1 completed

Type: experiment / capability

Summary:

Completed the first recommendation-scoring experiment on the synthetic Planner-style trip options dataset. Produced a scored dataset, experiment report, experiment register entry, evidence register entry, and moved Recommendation Scoring from Level 1 to Level 2.

Files changed:

- `datasets/processed/trip_options_scored_v1.csv`
- `reports/experiment-reports/trip-options-recommendation-scoring-v1.md`
- `EXPERIMENTS.md`
- `EVIDENCE.md`
- `capabilities/recommendation-scoring.md`

Evidence produced:

- EXP-001 recommendation scoring experiment
- ranked dataset of 21 scoreable options
- documented weighted formula and penalty rules
- capability maturity update to Level 2 for Recommendation Scoring

Next action:

Run sensitivity analysis as v1.1 before considering transfer to Planner.

## 2026-05-05 — Computed trip-options EDA completed

Type: evidence / capability

Summary:

Completed the first computed evidence pass on the synthetic Planner-style trip options dataset. Created a processed flagged dataset, an evidence report, updated the evidence register, and moved Data Cleaning plus Exploratory Analysis from Level 1 to Level 2.

Files changed:

- `datasets/processed/README.md`
- `datasets/processed/trip_options_flagged.csv`
- `reports/evidence/trip-options-eda-report.md`
- `EVIDENCE.md`
- `capabilities/data-cleaning.md`
- `capabilities/exploratory-analysis.md`

Evidence produced:

- computed data quality checks
- processed flagged dataset
- EDA evidence report
- capability maturity update to Level 2 for Data Cleaning and Exploratory Analysis

Next action:

Create the first recommendation scoring experiment using the scoreable trip options.

## 2026-05-05 — First synthetic evidence path set up

Type: setup / evidence

Summary:

Created the first concrete evidence path for CodeMike using a synthetic Planner-style trip options dataset. This path is designed to exercise data cleaning, exploratory analysis, recommendation scoring readiness, and dashboard KPI thinking.

Files changed:

- `datasets/synthetic/README.md`
- `datasets/synthetic/trip_options_sample.csv`
- `synthetic-data/trip_options_generator.py`
- `notebooks/00-foundations/README.md`
- `notebooks/00-foundations/trip-options-eda.md`
- `DATASETS.md`
- `EVIDENCE.md`

Evidence produced:

- synthetic dataset generator
- synthetic CSV sample
- EDA scaffold
- dataset registry entry
- evidence register entry

Next action:

Run or write the first computed EDA and cleaning analysis, then update capability maturity where justified.

## 2026-05-05 — First capability cards created

Type: setup / capability

Summary:

Created CodeMike's first eight capability cards and linked them to the reusable pattern library. Each card starts at maturity Level 1 because the method exists but evidence has not yet been produced.

Files changed:

- `capabilities/data-cleaning.md`
- `capabilities/exploratory-analysis.md`
- `capabilities/research-synthesis.md`
- `capabilities/recommendation-scoring.md`
- `capabilities/optimisation-modelling.md`
- `capabilities/model-evaluation.md`
- `capabilities/dashboard-insight-design.md`
- `capabilities/project-transfer.md`
- `capabilities/README.md`

Evidence produced:

- first capability catalogue
- pattern-to-capability mapping
- maturity and evidence requirements for each capability

Next action:

Produce the first evidence artifact using a synthetic dataset and update capability maturity where justified.

## 2026-05-05 — First reusable pattern library created

Type: setup / pattern

Summary:

Created CodeMike's first reusable pattern library. These patterns cover the initial working pipeline from data cleaning and exploratory analysis through research summary, recommendation scoring, optimisation framing, model evaluation, dashboard KPI design, and project transfer planning.

Files changed:

- `patterns/data-cleaning-checklist.md`
- `patterns/eda-notebook-template.md`
- `patterns/research-paper-summary-template.md`
- `patterns/recommendation-scoring-pattern.md`
- `patterns/optimisation-problem-template.md`
- `patterns/model-evaluation-template.md`
- `patterns/dashboard-kpi-pattern.md`
- `patterns/transfer-plan-template.md`
- `patterns/README.md`

Evidence produced:

- first reusable method library
- pattern index
- future candidate pattern list

Next action:

Create first capability cards that reference the pattern library.

## 2026-05-05 — Orientation induction pack created

Type: setup / orientation

Summary:

Created CodeMike's student-life and university induction layer. This gives the AI Postgraduate a non-technical foundation covering academic culture, integrity, conduct, legal/compliance awareness, wellbeing, employability, international context, inclusion, research ethics, professional behaviour, HR readiness, and city/culture awareness.

Files changed:

- `orientation/university-life.md`
- `orientation/academic-integrity.md`
- `orientation/student-conduct.md`
- `orientation/legal-and-compliance.md`
- `orientation/wellbeing-and-support.md`
- `orientation/careers-and-employability.md`
- `orientation/international-student-context.md`
- `orientation/equality-diversity-inclusion.md`
- `orientation/research-ethics.md`
- `orientation/professional-behaviour.md`
- `orientation/hr-and-workplace-readiness.md`
- `orientation/city-and-culture.md`

Evidence produced:

- complete first-pass orientation framework
- cross-links to policy, evidence, responsible AI, supervision, QA, portfolio, and transfer files

Next action:

Begin first capability cards or first reusable patterns.

## 2026-05-05 — Milestone 0 started

Type: setup

Summary:

Initialised CodeMike as the AI Postgraduate capability system for the MSc workspace. Established the repository direction: hybrid now, institutional later.

Files changed:

- `README.md`
- `CLAUDE.md`
- `CODEMIKE.md`
- `STUDENT_LIFE.md`
- `ROADMAP.md`

Evidence produced:

- repository identity and operating model
- six-month roadmap direction

Next action:

Create active capability files and scaffold folders.
