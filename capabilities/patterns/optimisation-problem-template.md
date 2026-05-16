# Pattern — Optimisation Problem Template

## Purpose

Use this pattern when CodeMike needs to turn a practical decision problem into an optimisation problem.

## Core Principle

No optimiser before constraints are written plainly.

## When to Use

Use this for:

- scheduling
- routing
- allocation
- budget planning
- production planning
- inventory decisions
- trip planning
- vendor selection
- process optimisation

## 1. Plain-Language Problem

```md
Problem:
Decision owner:
Why it matters:
Deadline/time horizon:
Decision frequency:
```

## 2. Decision Variables

What can be chosen?

```md
Variable:
Meaning:
Type: binary / integer / continuous / categorical
Allowed range:
```

## 3. Objective

What are we trying to maximise or minimise?

Examples:

- minimise cost
- maximise profit
- minimise travel fatigue
- maximise service level
- minimise delay
- maximise weighted preference score

```md
Objective:
Direction: maximise / minimise
Business meaning:
Unit:
```

## 4. Constraints

Constraints define feasibility.

```md
Constraint:
Plain-language rule:
Mathematical form if known:
Hard or soft:
Consequence if violated:
```

## 5. Inputs and Parameters

```md
Parameter:
Meaning:
Source:
Unit:
Known uncertainty:
```

## 6. Feasibility Check

Before solving, ask:

- Is at least one feasible solution possible?
- Are constraints contradictory?
- Are key inputs missing?
- Is the problem too large for the chosen method?
- Are there soft constraints that should become penalties?

## 7. Baseline

Define a simple baseline before optimisation.

Examples:

- current manual approach
- cheapest option
- fastest option
- equal allocation
- first-come-first-served
- greedy heuristic

```md
Baseline:
Why chosen:
Expected weakness:
```

## 8. Solution Method

Choose method based on problem type.

Examples:

- brute force for tiny problems
- greedy heuristic
- linear programming
- integer programming
- dynamic programming
- local search
- evolutionary method
- simulation

```md
Method:
Why appropriate:
Limitations:
```

## 9. Evaluation

Compare solution against baseline.

```md
Metric:
Baseline result:
Optimised result:
Improvement:
Tradeoff:
```

## 10. Sensitivity Analysis

Check how solution changes when inputs or weights change.

Examples:

- cost changes
- demand changes
- capacity changes
- constraint relaxed/tightened
- weight changes

## 11. Explainability

For final output, explain:

- why this solution was chosen
- which constraints bind
- what tradeoffs exist
- what could change the answer
- what human review is needed

## Completion Criteria

- [ ] Problem stated plainly
- [ ] Variables defined
- [ ] Objective defined
- [ ] Constraints documented
- [ ] Inputs listed
- [ ] Feasibility checked
- [ ] Baseline defined
- [ ] Method justified
- [ ] Results compared
- [ ] Sensitivity considered

## Common Failures

- Optimising the wrong objective
- Ignoring hidden constraints
- Treating soft preferences as hard constraints
- No baseline comparison
- No feasibility check
- No explanation for decision owner

## Related Files

- `modules/07-optimisation/`
- `decision-science/`
- `EXPERIMENTS.md`
- `TRANSFER_LOG.md`
