# Capability — Optimisation Modelling

## What this capability does

Converts practical decision problems into optimisation models with clear variables, objectives, constraints, baselines, feasibility checks, and explainable outputs.

## Inputs

- Plain-language decision problem
- Decision variables
- Objective
- Constraints
- Input parameters
- Baseline method
- Evaluation metric

## Outputs

- Optimisation problem statement
- Variable and constraint definitions
- Baseline comparison
- Solution method selection
- Sensitivity notes
- Explainable recommendation

## Method

Use `patterns/optimisation-problem-template.md`.

Core sections:

1. Plain-language problem
2. Decision variables
3. Objective
4. Constraints
5. Inputs and parameters
6. Feasibility check
7. Baseline
8. Solution method
9. Evaluation
10. Sensitivity analysis
11. Explainability

## Current maturity

Level 1 — Draft method.

The template exists, but CodeMike has not yet modelled or solved a concrete optimisation example.

## Evidence

No evidence yet.

First evidence target:

- Write one optimisation problem using a synthetic business, Planner, logistics, or manufacturing example.
- Compare a simple baseline with an improved solution.
- Record result in `EXPERIMENTS.md`.

## Limitations

- No solver selected yet.
- No Python implementation yet.
- No sensitivity analysis example yet.
- Constraint modelling still untested.

## Reusable in

- Planner recommendation refinement
- production scheduling
- logistics routing
- budget allocation
- inventory planning
- plating/process optimisation
- business operations

## Transfer history

No transfers yet.

## Next action

Create a tiny optimisation exercise with explicit variables, objective, constraints, and baseline.
