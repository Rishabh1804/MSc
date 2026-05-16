# Pattern — Data Cleaning Checklist

## Purpose

Use this pattern before analysis, modelling, dashboards, or optimisation work.

The goal is to make data usable, explainable, and safe enough for the intended decision.

## When to Use

Use this when CodeMike receives or creates a dataset.

## Inputs

- Dataset path or source
- Dataset purpose
- Expected schema, if known
- Privacy classification
- Target analysis or project

## Checklist

## 1. Register the Dataset

- [ ] Dataset is listed in `DATASETS.md`
- [ ] Source is recorded
- [ ] Synthetic/real status is recorded
- [ ] Privacy level is classified
- [ ] Allowed use is clear

## 2. Inspect Structure

- [ ] Row count checked
- [ ] Column count checked
- [ ] Column names reviewed
- [ ] Data types inspected
- [ ] Units identified where relevant
- [ ] Primary key or unique identifier identified where relevant

## 3. Check Missingness

- [ ] Missing values counted by column
- [ ] Missing values interpreted, not just removed
- [ ] Missingness pattern checked
- [ ] Imputation/removal decision documented

## 4. Check Duplicates

- [ ] Exact duplicate rows checked
- [ ] Duplicate identifiers checked
- [ ] Duplicate meaning clarified
- [ ] Removal/retention decision documented

## 5. Check Validity

- [ ] Numeric ranges checked
- [ ] Dates parsed and checked
- [ ] Categories standardised
- [ ] Units normalised
- [ ] Impossible values flagged
- [ ] Outliers reviewed, not blindly removed

## 6. Check Consistency

- [ ] Naming conventions standardised
- [ ] Category spelling/casing standardised
- [ ] Time zones/date formats handled if relevant
- [ ] Currency/unit formats handled if relevant
- [ ] Referential consistency checked if multiple tables exist

## 7. Check Leakage and Bias

- [ ] Target leakage considered for modelling work
- [ ] Sensitive or proxy attributes identified
- [ ] Sampling bias considered
- [ ] Excluded groups or missing segments noted

## 8. Produce Clean Output

- [ ] Cleaning steps are reproducible
- [ ] Cleaned dataset path recorded
- [ ] Data dictionary drafted if needed
- [ ] Assumptions documented
- [ ] Limitations documented

## Output

A cleaned or analysis-ready dataset with documented assumptions, limitations, and lineage.

## Evidence to Produce

- Notebook section
- Cleaning script
- Data quality report
- `DATASETS.md` update

## Common Failures

- Dropping missing rows without understanding meaning
- Treating outliers as errors automatically
- Ignoring units
- Mixing raw and cleaned data
- Forgetting privacy classification
- Creating silent transformations that cannot be reproduced

## Related Files

- `DATASETS.md`
- `DATA_POLICY.md`
- `QA_CHECKLIST.md`
- `FAILURE_LOG.md`
