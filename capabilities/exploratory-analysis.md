# Capability — Exploratory Analysis

## What this capability does

Uses structured exploratory data analysis to understand dataset quality, distributions, relationships, patterns, risks, and decision-relevant findings.

## Inputs

- Registered dataset
- Data cleaning notes
- Analysis objective
- Decision or research question
- Privacy classification

## Outputs

- EDA notebook or report
- Key findings
- Visual or tabular summaries
- Data quality observations
- Limitations
- Next action recommendation

## Method

Use `patterns/eda-notebook-template.md`.

Core sections:

1. Objective
2. Dataset summary
3. Load and inspect data
4. Schema and data quality review
5. Univariate exploration
6. Relationship exploration
7. Visual analysis
8. Key findings
9. Risks and limitations
10. Next actions

## Current maturity

Level 2 — Example reproduced / applied on synthetic data.

CodeMike produced a first computed EDA report from a synthetic Planner-style trip options dataset.

## Evidence

Primary evidence:

- `reports/evidence/trip-options-eda-report.md`
- `notebooks/00-foundations/trip-options-eda.md`
- `datasets/processed/trip_options_flagged.csv`
- `EVIDENCE.md` entry: `2026-05-05 — Synthetic trip options computed EDA`

What was proven:

- Dataset composition was summarised.
- Tier and visa distributions were interpreted.
- Data quality issues were connected to scoring readiness.
- Early decision-support findings were generated.
- Dashboard KPI candidates were identified.

## Limitations

- No visual charts have been committed yet.
- EDA was performed on a small synthetic dataset.
- No reusable Python EDA helper exists yet.
- No real-world dataset has been analysed.

## Reusable in

- data cleaning
- dashboard design
- model feature discovery
- anomaly investigation
- business reporting
- manufacturing/process analytics
- recommendation scoring

## Transfer history

No transfers yet.

## Next action

Create a first recommendation scoring experiment using the scoreable rows from the processed dataset.
