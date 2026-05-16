# Pattern — Model Evaluation Template

## Purpose

Use this pattern before trusting or transferring a machine learning model, scoring model, classifier, forecaster, optimiser, or recommendation method.

## Core Principle

No model is useful until it is compared against a meaningful baseline and its limitations are understood.

## 1. Model Context

```md
Model name:
Problem type: classification / regression / forecasting / ranking / clustering / optimisation / other
Decision supported:
Users affected:
High-stakes? yes/no
Human review required? yes/no
```

## 2. Dataset

```md
Dataset:
Source:
Privacy level:
Rows:
Features:
Target variable:
Time period:
Known limitations:
```

## 3. Baseline

Define the simplest credible comparison.

Examples:

- majority class
- mean/median prediction
- previous period value
- random ranking
- simple rule-based score
- current manual process

```md
Baseline:
Reason chosen:
Baseline metric result:
```

## 4. Evaluation Metric

Choose metrics aligned with the decision.

Examples:

- accuracy
- precision
- recall
- F1
- ROC-AUC
- MAE
- RMSE
- MAPE
- top-k precision
- calibration
- business cost metric

```md
Metric:
Why this metric matters:
What it misses:
```

## 5. Data Split

```md
Split method:
Train size:
Validation size:
Test size:
Time-based split? yes/no
Leakage risk:
```

## 6. Results

```md
Model:
Metric result:
Baseline result:
Improvement:
Confidence level:
```

## 7. Error Analysis

Review where the model fails.

Questions:

- Which cases are predicted poorly?
- Are errors concentrated in a segment?
- Are false positives or false negatives more costly?
- Are errors acceptable for the decision?
- Is the model overconfident?

## 8. Robustness Checks

Check:

- overfitting
- data leakage
- class imbalance
- missing values
- outliers
- sensitivity to features
- performance across segments
- performance over time

## 9. Explainability

Record:

- important features
- direction of influence where known
- whether the model can be explained to the decision owner
- where explanation is weak

## 10. Responsible AI Review

Ask:

- Could the model harm users?
- Does it use sensitive or proxy attributes?
- Is human review required?
- Are affected users able to challenge or understand the output?
- Is the model being used outside its valid context?

## 11. Deployment / Transfer Decision

```md
Decision: reject / improve / monitor / transfer / deploy
Reason:
Required safeguards:
Maintenance need:
```

## Completion Criteria

- [ ] Baseline exists
- [ ] Metric is justified
- [ ] Split is appropriate
- [ ] Leakage checked
- [ ] Error analysis completed
- [ ] Limitations documented
- [ ] Responsible AI reviewed
- [ ] Transfer decision recorded

## Common Failures

- Reporting accuracy only
- No baseline
- Data leakage
- Ignoring class imbalance
- No error analysis
- Treating validation result as production proof
- No human review boundary

## Related Files

- `RESPONSIBLE_AI.md`
- `QA_CHECKLIST.md`
- `EXPERIMENTS.md`
- `TRANSFER_LOG.md`
