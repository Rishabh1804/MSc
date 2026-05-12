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

## 2026-05-05 — Trip options sensitivity analysis v1.1

Capability:

- Recommendation Scoring
- Model Evaluation, partial
- Dashboard Insight Design, partial

Artifact:

- `reports/experiment-reports/trip-options-sensitivity-v1-1.md`
- `datasets/processed/trip_options_sensitivity_v1_1.csv`
- `EXPERIMENTS.md` entry: `EXP-002`

Type:

Sensitivity analysis experiment

Status:

Complete first pass.

Summary:

Ran a five-scenario sensitivity analysis on the v1 trip-options recommendation ranking. The analysis tested family comfort, budget sensitivity, premium comfort, low fatigue, and novelty-heavy priority profiles.

What it proves:

- CodeMike can test whether recommendations are stable under changing user priorities.
- CodeMike can distinguish robust recommendations from preference-sensitive recommendations.
- CodeMike can explain why a premium option may be best for one scenario but not generally recommended.

Key findings:

- `TRIP-014` Goa, `TRIP-008` Phuket, `TRIP-002` Singapore comfort, and `TRIP-019` Dubai comfort appeared in the top five across all five scenarios.
- `TRIP-012` Kuala Lumpur appeared in four of five top-fives and remained top-ten in every scenario.
- `TRIP-018` Singapore premium ranked first under premium comfort but fell to rank 13 under budget-sensitive scoring.

Limitations:

- Dataset is synthetic.
- Scenario weights are hand-authored.
- Penalty rules were not varied.
- No user-specific calibration has been performed.
- No live travel validation exists.

Next action:

Create a Planner transfer candidate or convert scoring logic into a reusable module under `src/`.

## 2026-05-05 — Trip options recommendation scoring v1

Capability:

- Recommendation Scoring
- Model Evaluation, partial
- Dashboard Insight Design, partial

Artifact:

- `reports/experiment-reports/trip-options-recommendation-scoring-v1.md`
- `datasets/processed/trip_options_scored_v1.csv`
- `EXPERIMENTS.md` entry: `EXP-001`

Type:

Recommendation scoring experiment

Status:

Complete first pass.

Summary:

Created the first explainable recommendation-scoring experiment for synthetic Planner-style trip options. The experiment ranked 21 scoreable options using a transparent weighted formula and documented penalty rules.

What it proves:

- CodeMike can convert cleaned data into a first ranking system.
- CodeMike can define criteria, weights, constraints, penalties, and a final score.
- CodeMike can produce a ranked dataset and experiment report.
- CodeMike can explain why top options ranked well and where limitations remain.

Key findings:

- Top five ranked options were `TRIP-014` Goa, `TRIP-008` Phuket, `TRIP-012` Kuala Lumpur, `TRIP-002` Singapore, and `TRIP-019` Dubai.
- The v1 formula favours practical family travel over pure luxury.
- Premium comfort leaders can fall lower when cost and friction penalties are applied.

Limitations:

- Dataset is synthetic.
- Weights are provisional.
- Penalty thresholds are hand-authored.
- No sensitivity analysis has been performed yet.
- Real travel decisions require live validation.

Next action:

Update `capabilities/recommendation-scoring.md` to Level 2 and run sensitivity analysis as v1.1.

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
