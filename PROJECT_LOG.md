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
