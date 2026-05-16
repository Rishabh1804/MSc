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

## Experiment: Trip Options Sensitivity Analysis v1.1

ID: EXP-002  
Date: 2026-05-05  
Question: Are the top recommendations from the v1 trip-options scoring experiment robust when user priorities change?  
Dataset: `datasets/processed/trip_options_scored_v1.csv`  
Output: `datasets/processed/trip_options_sensitivity_v1_1.csv`  
Baseline: EXP-001 v1 recommendation ranking.  
Method: Re-ranked scoreable trip options under five weighting scenarios: family comfort, budget sensitive, premium comfort, low fatigue, and novelty heavy. Penalty rules were held constant.  
Metric: Scenario ranks, average scenario rank, top-five scenario count, and top-ten scenario count.  
Result: Goa, Phuket, Singapore comfort, and Dubai comfort appeared in the top five across all five scenarios. Kuala Lumpur appeared in four of five top-fives and remained top-ten across all scenarios.  
Interpretation: Practical comfort-tier options are stable. Premium Singapore is preference-sensitive: rank 1 under premium comfort but rank 13 under budget-sensitive scoring.  
Limitations: Synthetic data; hand-authored scenario weights; penalty rules not varied; no live travel validation; no user calibration.  
Evidence path: `reports/experiment-reports/trip-options-sensitivity-v1-1.md`  
Next step: Create a Planner transfer candidate or convert scoring logic into a reusable module.

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
