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

Setup complete; computed evidence pending.

Summary:

Created the first synthetic dataset and EDA scaffold for CodeMike. The dataset models fictional Planner-style trip options and intentionally includes invalid or suspicious values so CodeMike can exercise data cleaning judgement before scoring or dashboard work.

What it proves:

- CodeMike now has a concrete, safe dataset for first applied work.
- The data cleaning and EDA patterns have a target artifact.
- The evidence workflow has moved beyond empty templates.

Limitations:

- No code-based EDA has been executed yet.
- Findings are currently hypotheses/scaffolded, not computed results.
- Capability maturity should remain Level 1 until computed evidence exists.

Next action:

Run or write the first EDA/cleaning analysis, produce computed findings, and then update capability maturity if justified.
