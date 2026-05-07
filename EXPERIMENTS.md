# EXPERIMENTS.md — CodeMike Experiment Register

This file records experiments, tests, prototypes, and structured investigations.

## Experiment Rule

An experiment should answer a question, compare against a baseline where possible, and produce an interpretable result.

## Experiment Entry Template

```md
## Experiment: <title>

ID:
Date:
Question:
Dataset:
Baseline:
Method:
Metric:
Result:
Interpretation:
Limitations:
Evidence path:
Next step:
```

## Experiment Register

## Experiment: Trip Options Recommendation Scoring v1

ID: EXP-001  
Date: 2026-05-05  
Question: Can CodeMike produce an explainable first-pass recommendation ranking for synthetic Planner-style trip options using criteria, weights, constraints, and penalties?  
Dataset: `datasets/processed/trip_options_flagged.csv`  
Output: `datasets/processed/trip_options_scored_v1.csv`  
Baseline: Data-quality-filtered scoreable rows ranked by a transparent weighted formula. A richer baseline comparison is still pending.  
Method: Weighted scoring with documented criteria, normalised cost score, visa score, fatigue score, risk-adjusted comfort, confidence, novelty, and penalty rules.  
Metric: `recommendation_score_v1`  
Result: Top five ranked options were `TRIP-014` Goa, `TRIP-008` Phuket, `TRIP-012` Kuala Lumpur, `TRIP-002` Singapore, and `TRIP-019` Dubai.  
Interpretation: The v1 formula favours practical family travel over pure luxury. Comfort-tier options dominated because they combine low cost, low fatigue, and easy visa complexity.  
Limitations: Synthetic data; provisional weights; hand-authored penalties; no sensitivity analysis; no live travel validation.  
Evidence path: `reports/experiment-reports/trip-options-recommendation-scoring-v1.md`  
Next step: Run sensitivity analysis as v1.1 and consider Planner OptionCard transfer after robustness checks.
