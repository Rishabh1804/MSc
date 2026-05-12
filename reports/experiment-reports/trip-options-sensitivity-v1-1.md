# Experiment Report — Trip Options Sensitivity Analysis v1.1

Date: 2026-05-05  
Author: CodeMike  
Experiment ID: EXP-002  
Source dataset: `datasets/processed/trip_options_scored_v1.csv`  
Output dataset: `datasets/processed/trip_options_sensitivity_v1_1.csv`  
Linked capability: `capabilities/recommendation-scoring.md`  
Prior experiment: `EXP-001`

## 1. Question

Are the top recommendations from the v1 trip-options scoring experiment robust when user priorities change?

## 2. Method

This sensitivity analysis reranked the 21 scoreable trip options under five alternative weighting scenarios.

Penalty rules were kept the same as v1 so that the analysis isolates weight sensitivity rather than changing both weights and penalties simultaneously.

## 3. Scenarios

| Scenario | Purpose |
|---|---|
| `family_comfort` | Prioritises risk-adjusted comfort and travel fatigue |
| `budget_sensitive` | Gives stronger weight to lower estimated cost |
| `premium_comfort` | Prioritises comfort and confidence over cost |
| `low_fatigue` | Gives strongest weight to travel fatigue |
| `novelty_heavy` | Gives stronger weight to novelty/experience interest |

## 4. Scenario Top Five

### Family Comfort

| Rank | Option | Destination | Score |
|---:|---|---|---:|
| 1 | `TRIP-014` | Goa | 85.66 |
| 2 | `TRIP-008` | Phuket | 81.32 |
| 3 | `TRIP-002` | Singapore | 80.87 |
| 4 | `TRIP-012` | Kuala Lumpur | 80.74 |
| 5 | `TRIP-019` | Dubai | 79.52 |

### Budget Sensitive

| Rank | Option | Destination | Score |
|---:|---|---|---:|
| 1 | `TRIP-014` | Goa | 87.02 |
| 2 | `TRIP-008` | Phuket | 85.26 |
| 3 | `TRIP-012` | Kuala Lumpur | 84.22 |
| 4 | `TRIP-002` | Singapore | 79.54 |
| 5 | `TRIP-019` | Dubai | 79.32 |

### Premium Comfort

| Rank | Option | Destination | Score |
|---:|---|---|---:|
| 1 | `TRIP-018` | Singapore | 82.20 |
| 2 | `TRIP-014` | Goa | 81.68 |
| 3 | `TRIP-008` | Phuket | 81.66 |
| 4 | `TRIP-002` | Singapore | 80.37 |
| 5 | `TRIP-019` | Dubai | 79.94 |

### Low Fatigue

| Rank | Option | Destination | Score |
|---:|---|---|---:|
| 1 | `TRIP-014` | Goa | 86.32 |
| 2 | `TRIP-002` | Singapore | 82.23 |
| 3 | `TRIP-008` | Phuket | 80.89 |
| 4 | `TRIP-012` | Kuala Lumpur | 80.87 |
| 5 | `TRIP-019` | Dubai | 79.11 |

### Novelty Heavy

| Rank | Option | Destination | Score |
|---:|---|---|---:|
| 1 | `TRIP-008` | Phuket | 84.73 |
| 2 | `TRIP-002` | Singapore | 78.99 |
| 3 | `TRIP-019` | Dubai | 78.28 |
| 4 | `TRIP-012` | Kuala Lumpur | 77.79 |
| 5 | `TRIP-014` | Goa | 77.76 |

## 5. Stable Recommendations

The following options appeared in the top five across all five scenarios:

| Option | Destination | Tier | Average scenario rank | Top-five count |
|---|---|---|---:|---:|
| `TRIP-014` | Goa | comfort | 2.0 | 5 |
| `TRIP-008` | Phuket | comfort | 2.2 | 5 |
| `TRIP-002` | Singapore | comfort | 3.0 | 5 |
| `TRIP-019` | Dubai | comfort | 4.6 | 5 |

`TRIP-012` Kuala Lumpur appeared in four out of five top-fives and remained top-ten in every scenario.

## 6. Sensitive Recommendation

`TRIP-018` Singapore premium is highly sensitive to user preference.

It ranks:

- rank 1 under `premium_comfort`
- rank 13 under `budget_sensitive`
- top-ten in four out of five scenarios

Interpretation: this option is not a universal recommendation. It is a premium-comfort recommendation when the user explicitly values comfort over budget.

## 7. Interpretation

The v1 ranking is reasonably stable for practical comfort-tier family options.

The stable set is:

- Goa
- Phuket
- Singapore comfort
- Dubai comfort
- Kuala Lumpur as a near-stable practical option

The analysis also shows that premium options should be treated as scenario-dependent rather than generally recommended.

## 8. Limitations

- Scenario weights are hand-authored.
- Penalty rules were not varied.
- Dataset is synthetic.
- No live travel data was used.
- No user-specific preference calibration has been performed.
- No statistical uncertainty model exists yet.

## 9. Capability Impact

This strengthens the `Recommendation Scoring` capability but does not yet justify Level 3.

Reason:

- Sensitivity analysis was performed.
- Robust and fragile recommendations were distinguished.
- However, the method is still synthetic and not packaged as a reusable code module.

Recommendation Scoring remains Level 2, but with stronger evidence.

## 10. Next Actions

1. Create a Planner transfer candidate based on the stable recommendation set.
2. Convert scoring logic into reusable code under `src/`.
3. Add a dashboard KPI specification for recommendation stability.
4. Add a viva defence entry for EXP-001 and EXP-002.
