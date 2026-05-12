# codemike.recommendation

Reusable recommendation and decision-scoring utilities live here.

## Current Module

`trip_scoring.py` extracts the scoring logic from:

- `EXP-001` — Trip Options Recommendation Scoring v1
- `EXP-002` — Trip Options Sensitivity Analysis v1.1

## Status

Prototype utility.

The module is useful for repeatable experiments and future transfer planning, but it is not yet production-ready.

## What It Provides

- v1 default weights
- default sensitivity scenarios
- cost score helper
- visa score helper
- penalty calculation
- single-row scoring
- ranked option output
- multi-scenario sensitivity ranking

## Limitations

- Designed around the synthetic Planner trip-options schema.
- Penalty rules are hard-coded.
- Scenario weights are hand-authored.
- No test suite yet.
- No CLI wrapper yet.
- No PWA/API integration yet.
- Real travel decisions require live validation and human review.

## Next Engineering Steps

1. Add unit tests.
2. Add a small CLI runner.
3. Add schema validation.
4. Add configurable weights and penalty thresholds.
5. Create a Planner transfer candidate.
