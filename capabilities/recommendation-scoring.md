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

Level 1 — Draft method.

The scoring pattern exists, but no working scoring implementation has been built yet.

## Evidence

No evidence yet.

First evidence target:

- Build a small scoring table for Planner-style trip options or vendor/product comparison.
- Include sensitivity notes.
- Record result in `EXPERIMENTS.md`.

## Limitations

- No scoring engine yet.
- No standard normalisation helpers yet.
- No sensitivity-analysis notebook yet.
- Risk of arbitrary weights if user priorities are vague.

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

Create a simple synthetic option table and score it using the pattern.
