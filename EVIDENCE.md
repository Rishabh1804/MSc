# EVIDENCE.md — Evidence Register

This file records artifacts that prove CodeMike has learned, applied, or transferred a capability.

## Evidence Standard

A claim of capability requires evidence.

Acceptable evidence includes:

- notebook
- script
- dataset
- experiment report
- benchmark
- model evaluation
- dashboard prototype
- transfer log
- case study
- viva-style defence

## Evidence Entry Template

```md
## YYYY-MM-DD — Evidence Title

Capability:
Artifact:
Type:
Status:
Summary:
What it proves:
Limitations:
Next action:
```

## 2026-05-05 — Synthetic trip options computed EDA

Capability:

- Data Cleaning
- Exploratory Analysis
- Recommendation Scoring, partial
- Dashboard Insight Design, partial

Artifact:

- `reports/evidence/trip-options-eda-report.md`
- `datasets/processed/trip_options_flagged.csv`
- `datasets/synthetic/trip_options_sample.csv`

Type:

Computed EDA and processed flagged dataset

Status:

Complete first pass.

Summary:

Ran the first computed evidence pass on a synthetic Planner-style trip options dataset. The pass identified dataset shape, tier distribution, visa distribution, invalid/suspicious rows, derived quality flags, and created early decision-support interpretations.

What it proves:

- CodeMike can apply the data cleaning checklist to a concrete dataset.
- CodeMike can identify invalid/suspicious values and preserve them through explicit flags.
- CodeMike can produce an EDA report with computed summaries, early findings, and limitations.
- CodeMike can connect data analysis to recommendation scoring and dashboard KPI design.

Key findings:

- Dataset has 24 rows and 13 original columns.
- No missing values and no duplicate rows were found.
- Three rows were flagged: `TRIP-005`, `TRIP-009`, and `TRIP-013`.
- `TRIP-018` is the top comfort-led option among scoreable rows.
- `TRIP-014` is the strongest value-led option among top comfort performers.

Limitations:

- Dataset is synthetic and small.
- Scoring fields are provisional heuristics.
- No visual charts or final recommendation engine yet.
- Real travel use would require live validation of pricing, availability, visas, weather, and logistics.

Next action:

Update `capabilities/data-cleaning.md` and `capabilities/exploratory-analysis.md` to Level 2. Then create the first recommendation scoring experiment.

## 2026-05-05 — First synthetic evidence path setup

Capability:

- Data Cleaning
- Exploratory Analysis
- Recommendation Scoring, partial
- Dashboard Insight Design, partial

Artifact:

- `synthetic-data/trip_options_generator.py`
- `datasets/synthetic/trip_options_sample.csv`
- `notebooks/00-foundations/trip-options-eda.md`

Type:

Synthetic dataset + EDA scaffold

Status:

Setup complete; computed evidence now produced in `reports/evidence/trip-options-eda-report.md`.

Summary:

Created the first synthetic dataset and EDA scaffold for CodeMike. The dataset models fictional Planner-style trip options and intentionally includes invalid or suspicious values so CodeMike can exercise data cleaning judgement before scoring or dashboard work.

What it proves:

- CodeMike now has a concrete, safe dataset for first applied work.
- The data cleaning and EDA patterns have a target artifact.
- The evidence workflow has moved beyond empty templates.

Limitations:

- The setup artifact itself does not prove analysis capability; computed evidence is recorded separately.

Next action:

Use the computed EDA to begin recommendation scoring.
