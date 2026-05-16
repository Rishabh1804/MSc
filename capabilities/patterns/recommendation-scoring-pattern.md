# Pattern — Recommendation Scoring

## Purpose

Use this pattern when CodeMike needs to rank options using criteria, weights, constraints, penalties, and explainable tradeoffs.

This is especially relevant for Planner, vendor selection, dashboards, product comparisons, routing, budgeting, and decision engines.

## Core Principle

A recommendation should explain why an option ranks well, what tradeoffs it makes, and what assumptions drive the score.

## When to Use

Use this when there are:

- multiple options
- multiple criteria
- user preferences
- constraints
- imperfect tradeoffs
- need for explainable ranking

## Inputs

- Options table
- Criteria list
- User preferences
- Constraints
- Weighting scheme
- Penalty rules
- Explainability requirements

## Step 1 — Define the Decision

```md
Decision:
User/audience:
Options being compared:
Decision deadline:
High-stakes? yes/no
Human review required? yes/no
```

## Step 2 — Define Criteria

Example criteria:

- cost
- comfort
- duration
- quality
- reliability
- risk
- convenience
- fatigue
- safety
- strategic fit
- confidence

For each criterion:

```md
Criterion:
Direction: higher is better / lower is better
Required or optional:
Measurement:
Known limitation:
```

## Step 3 — Define Constraints

Hard constraints remove options or mark them infeasible.

Examples:

- budget cap
- date availability
- visa feasibility
- minimum quality
- safety threshold
- delivery deadline

```md
Constraint:
Rule:
Consequence if violated:
```

## Step 4 — Normalise Scores

Convert raw values into comparable scores, usually 0–100.

Document the transformation.

```md
Raw field:
Scoring rule:
Reason:
Limitations:
```

## Step 5 — Apply Weights

Weights should reflect user priorities.

```md
Criterion | Weight | Reason
---|---:|---
Cost | 0.25 | Budget matters but is not the only driver
Quality | 0.35 | User prefers better experience
Convenience | 0.25 | Reduces execution friction
Risk | 0.15 | Avoids fragile options
```

Weights should normally sum to 1.0.

## Step 6 — Apply Penalties

Penalties should capture hidden tradeoffs.

Examples:

- excessive travel fatigue
- low confidence data
- poor review quality
- operational complexity
- hidden cost
- narrow availability

```md
Penalty:
Trigger:
Score impact:
Reason:
```

## Step 7 — Compute Score

Recommended structure:

```text
final_score = weighted_score - penalties
```

Also preserve component scores for explanation.

## Step 8 — Explain the Ranking

For each top option:

```md
Option:
Final score:
Why it ranks well:
Main tradeoff:
Risk:
Best for:
Not ideal if:
```

## Step 9 — Sensitivity Check

Ask:

- Does ranking change if weights shift?
- Which criterion dominates?
- Are results robust or fragile?
- Is there an option that is second-best but safer?

## Step 10 — Human Review

Recommendation systems should support decisions, not replace judgement.

Record:

- confidence level
- assumptions
- missing data
- required human decision

## Completion Criteria

- [ ] Decision is defined
- [ ] Criteria are documented
- [ ] Constraints are explicit
- [ ] Weights are justified
- [ ] Penalties are documented
- [ ] Scores are explainable
- [ ] Sensitivity checked
- [ ] Human review boundary clear

## Common Failures

- Hard-coded scores with no explanation
- Too many criteria
- Arbitrary weights
- No sensitivity analysis
- Treating ranking as truth
- Hiding infeasible options without explanation

## Related Files

- `decision-science/`
- `RESPONSIBLE_AI.md`
- `TRANSFER_LOG.md`
- `capabilities/`
