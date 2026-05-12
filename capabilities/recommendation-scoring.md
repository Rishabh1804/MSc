# Capability — Recommendation Scoring

## What this capability does

Ranks options using explainable criteria, weights, constraints, penalties, and tradeoffs so a human can make a better decision.

## Inputs

- Option list
- Criteria
- Weights
- Constraints
- Penalty rules
- User preferences
- Data confidence notes

## Outputs

- Ranked option list
- Component scores
- Explanation of tradeoffs
- Sensitivity notes
- Human review boundary

## Method

Use `patterns/recommendation-scoring-pattern.md`.

Core steps:

1. Define the decision.
2. Define criteria.
3. Define constraints.
4. Normalise scores.
5. Apply weights.
6. Apply penalties.
7. Compute final score.
8. Explain ranking.
9. Check sensitivity.
10. Define human review requirement.

## Current maturity

Level 2 — Example reproduced / applied on synthetic data.

CodeMike created a first explainable recommendation-scoring experiment using scoreable rows from the synthetic Planner-style trip options dataset.

## Evidence

Primary evidence:

- `reports/experiment-reports/trip-options-recommendation-scoring-v1.md`
- `datasets/processed/trip_options_scored_v1.csv`
- `EXPERIMENTS.md` entry: `EXP-001`
- `EVIDENCE.md` entry: `2026-05-05 — Trip options recommendation scoring v1`

What was proven:

- A concrete scoring formula was defined.
- Criteria and weights were documented.
- Penalty rules were applied.
- Scoreable rows were ranked.
- Top results were interpreted with limitations.
- The method produced an output suitable for future Planner-style OptionCards or SignalRows.

## Limitations

- Dataset is synthetic.
- Weights are provisional.
- Penalty thresholds are hand-authored.
- No sensitivity analysis has been performed yet.
- No reusable scoring engine module exists yet.
- No transfer to Planner has occurred yet.

## Reusable in

- Planner
- business dashboards
- vendor selection
- product comparison
- budget tradeoffs
- logistics decisions
- capstone decision engine

## Transfer history

No transfers yet.

## Next action

Run sensitivity analysis as v1.1 to test whether the top recommendations are robust when weights change.
