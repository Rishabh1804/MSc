# Experiment Report — Trip Options Recommendation Scoring v1

Date: 2026-05-05  
Author: CodeMike  
Experiment ID: EXP-001  
Source dataset: `datasets/processed/trip_options_flagged.csv`  
Output dataset: `datasets/processed/trip_options_scored_v1.csv`  
Linked capability: `capabilities/recommendation-scoring.md`  
Linked pattern: `patterns/recommendation-scoring-pattern.md`

## 1. Question

Can CodeMike produce an explainable first-pass recommendation ranking for synthetic Planner-style trip options using criteria, weights, constraints, and penalties?

## 2. Decision Context

The decision context is family-oriented trip option shortlisting.

The ranking should prefer options that balance:

- family comfort
- lower travel fatigue
- lower cost
- easier visa/planning complexity
- planning confidence
- novelty

## 3. Input Scope

The experiment uses only rows marked as scoreable in `datasets/processed/trip_options_flagged.csv`.

| Input condition | Value |
|---|---:|
| Total rows in flagged dataset | 24 |
| Scoreable rows used | 21 |
| Excluded rows | 3 |

Excluded rows:

- `TRIP-005` — suspicious zero confidence
- `TRIP-009` — invalid weather risk score
- `TRIP-013` — invalid flight hours

## 4. Scoring Formula

The v1 weighted score is:

```text
weighted_score =
  0.30 * risk_adjusted_comfort_score
+ 0.20 * travel_fatigue_score
+ 0.20 * cost_score
+ 0.10 * visa_score
+ 0.10 * planning_confidence_score
+ 0.10 * novelty_score
```

Final score is:

```text
recommendation_score_v1 = weighted_score - penalty_points
```

## 5. Criteria

| Criterion | Direction | Weight | Reason |
|---|---|---:|---|
| Risk-adjusted comfort | Higher is better | 0.30 | Family comfort is the main decision driver |
| Travel fatigue score | Higher is better | 0.20 | Lower fatigue matters for family travel |
| Cost score | Higher is better | 0.20 | Lower cost improves practical feasibility |
| Visa score | Higher is better | 0.10 | Lower planning friction improves execution |
| Planning confidence | Higher is better | 0.10 | Low-confidence plans should rank lower |
| Novelty | Higher is better | 0.10 | Experience quality includes interest/novelty |

## 6. Penalty Rules

| Penalty | Trigger | Points |
|---|---|---:|
| `high_cost` | Estimated cost above ₹700,000 | 3 |
| `high_fatigue` | Flight hours above 8 | 5 |
| `visa_friction` | Visa complexity is moderate | 3 |
| `weather_risk` | Weather risk score above 55 | 4 |

## 7. Top 10 Results

| Rank | Option | Destination | Tier | Cost INR | Weighted score | Penalties | Final score | Interpretation |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | `TRIP-014` | Goa | comfort | 198,400 | 84.48 | 0 | 84.48 | Best value-led family option |
| 2 | `TRIP-008` | Phuket | comfort | 266,997 | 82.97 | 0 | 82.97 | Strong resort/novelty option |
| 3 | `TRIP-012` | Kuala Lumpur | comfort | 224,900 | 81.05 | 0 | 81.05 | Practical low-friction option |
| 4 | `TRIP-002` | Singapore | comfort | 388,496 | 80.10 | 0 | 80.10 | Very low fatigue and high confidence |
| 5 | `TRIP-019` | Dubai | comfort | 359,760 | 79.26 | 0 | 79.26 | Comfortable low-friction option |
| 6 | `TRIP-021` | Sri Lanka | high_quality | 367,875 | 77.54 | 0 | 77.54 | Good balanced option with weather note |
| 7 | `TRIP-023` | Langkawi | comfort | 302,150 | 76.58 | 0 | 76.58 | Good backup/resort option |
| 8 | `TRIP-024` | Andaman | comfort | 286,600 | 77.72 | 3 | 74.72 | Strong but visa friction reduces score |
| 9 | `TRIP-017` | Phuket | high_quality | 451,440 | 73.44 | 0 | 73.44 | High-quality family shortlist candidate |
| 10 | `TRIP-018` | Singapore | premium | 701,820 | 75.81 | 3 | 72.81 | Comfort leader, penalised for high cost |

## 8. Interpretation

The v1 formula favours practical family travel rather than pure luxury.

Key observations:

1. Comfort-tier options dominate the top five because they combine lower cost, low fatigue, and easy visa complexity.
2. `TRIP-018` is the comfort leader, but it falls to rank 10 because the v1 formula applies cost pressure.
3. `TRIP-014` ranks first because it combines low cost, low fatigue, strong infant friendliness, and no penalty triggers.
4. Long-haul or high-cost premium options are not excluded, but they need very strong comfort advantages to overcome penalties.
5. The output is explainable enough for a Planner-style OptionCard or SignalRow.

## 9. Limitations

- This is a synthetic dataset.
- Weights are provisional and reflect a family-comfort/value scenario.
- Penalty thresholds are hand-authored.
- No user-specific preference calibration has been performed.
- No sensitivity analysis has been performed yet.
- Real travel use would require live price, route, weather, visa, and availability checks.

## 10. Responsible AI / Human Review

This ranking is decision support only.

A human should review:

- real destination feasibility
- current visa requirements
- medical/family travel constraints
- budget limits
- weather seasonality
- flight timings and layovers
- infant-specific needs

## 11. Capability Impact

This experiment supports moving `Recommendation Scoring` from Level 1 to Level 2.

Reason:

- A concrete scoring formula was defined.
- Scoreable rows were ranked.
- Weights and penalties were documented.
- Results were interpreted with limitations.
- Output dataset was created.

## 12. Next Actions

1. Update `EXPERIMENTS.md`.
2. Update `EVIDENCE.md`.
3. Update `capabilities/recommendation-scoring.md` to Level 2.
4. Add sensitivity analysis as v1.1.
5. Consider creating a Planner OptionCard transfer candidate after sensitivity analysis.
