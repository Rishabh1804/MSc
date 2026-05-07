# Capability — Data Cleaning

## What this capability does

Converts raw or messy data into a documented, analysis-ready dataset while preserving lineage, assumptions, privacy classification, and known limitations.

## Inputs

- Raw dataset
- Dataset source
- Intended analysis or project
- Expected schema, if available
- Privacy classification

## Outputs

- Cleaned dataset or reproducible cleaning workflow
- Data quality notes
- Dataset registry update
- Documented assumptions and limitations

## Method

Use `patterns/data-cleaning-checklist.md`.

Core steps:

1. Register dataset.
2. Inspect structure.
3. Check missingness.
4. Check duplicates.
5. Check validity.
6. Check consistency.
7. Check leakage and bias.
8. Produce clean output.

## Current maturity

Level 2 — Example reproduced / applied on synthetic data.

CodeMike applied the data cleaning checklist to a synthetic Planner-style trip options dataset and produced explicit data-quality flags.

## Evidence

Primary evidence:

- `reports/evidence/trip-options-eda-report.md`
- `datasets/processed/trip_options_flagged.csv`
- `datasets/synthetic/trip_options_sample.csv`
- `EVIDENCE.md` entry: `2026-05-05 — Synthetic trip options computed EDA`

What was proven:

- Dataset shape was inspected.
- Missingness and duplicates were checked.
- Invalid/suspicious rows were identified.
- Quality flags were preserved in a processed dataset.
- Scoreability was separated from raw inclusion.

## Limitations

- Only synthetic data has been tested.
- No reusable Python cleaning module yet.
- No automated validation tests yet.
- No data dictionary pattern yet.
- No real-world messy dataset has been processed.

## Reusable in

- exploratory data analysis
- dashboard work
- model training
- optimisation inputs
- business analytics
- production/process analytics
- Planner data preparation

## Transfer history

No transfers yet.

## Next action

Extract the repeated validation logic into a small reusable Python function or validation checklist for future datasets.
