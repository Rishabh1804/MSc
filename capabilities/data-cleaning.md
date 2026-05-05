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

Level 1 — Draft method.

The checklist exists, but CodeMike has not yet applied it to a real or synthetic dataset.

## Evidence

No evidence yet.

First evidence target:

- Apply the checklist to a synthetic dataset.
- Record findings in an EDA notebook.
- Update `DATASETS.md` and `EVIDENCE.md`.

## Limitations

- No real dataset tested yet.
- No automated cleaning functions yet.
- No data dictionary pattern yet.
- No edge-case library yet.

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

Create or select a small synthetic dataset and run a first data cleaning exercise.
