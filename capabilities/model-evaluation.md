# Capability — Model Evaluation

## What this capability does

Evaluates models, scoring rules, rankings, and predictive systems against baselines, error cases, robustness checks, and responsible AI requirements.

## Inputs

- Model or scoring method
- Dataset
- Baseline
- Evaluation metric
- Data split
- Decision context
- Responsible AI context

## Outputs

- Evaluation report
- Baseline comparison
- Error analysis
- Robustness notes
- Limitations
- Transfer/deployment decision

## Method

Use `patterns/model-evaluation-template.md`.

Core sections:

1. Model context
2. Dataset
3. Baseline
4. Evaluation metric
5. Data split
6. Results
7. Error analysis
8. Robustness checks
9. Explainability
10. Responsible AI review
11. Deployment or transfer decision

## Current maturity

Level 1 — Draft method.

The evaluation pattern exists, but no model or scoring system has yet been evaluated.

## Evidence

No evidence yet.

First evidence target:

- Evaluate a simple baseline model or recommendation scoring method.
- Include error analysis and limitations.
- Record in `EXPERIMENTS.md` and `EVIDENCE.md`.

## Limitations

- No model card pattern yet.
- No automated evaluation helper yet.
- No benchmark dataset yet.
- No fairness or calibration example yet.

## Reusable in

- machine learning module
- recommendation scoring
- dashboard alerts
- forecasting
- classification tasks
- capstone models
- responsible AI review

## Transfer history

No transfers yet.

## Next action

Evaluate the first recommendation scoring or baseline model produced by CodeMike.
