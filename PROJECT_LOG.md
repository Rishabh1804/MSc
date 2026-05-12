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
- `PROJECT_LOG.md`

Evidence produced:

- repository identity and operating model
- six-month roadmap direction
- student orientation index

Next action:

Create active capability files and scaffold folders.
