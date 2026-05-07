# Evidence Report — Synthetic Planner Trip Options EDA

Date: 2026-05-05  
Author: CodeMike  
Dataset: `datasets/synthetic/trip_options_sample.csv`  
Processed output: `datasets/processed/trip_options_flagged.csv`  
Linked scaffold: `notebooks/00-foundations/trip-options-eda.md`  
Linked capabilities:

- `capabilities/data-cleaning.md`
- `capabilities/exploratory-analysis.md`
- `capabilities/recommendation-scoring.md`, partial
- `capabilities/dashboard-insight-design.md`, partial

## 1. Objective

Run the first computed evidence pass on a synthetic Planner-style trip options dataset.

The aim is to validate the dataset, identify quality issues, derive first analysis fields, and prepare the ground for recommendation scoring and dashboard design.

## 2. Dataset Shape

| Metric | Value |
|---|---:|
| Rows | 24 |
| Columns | 13 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Invalid/suspicious rows flagged | 3 |
| Scoreable rows after quality flagging | 21 |

## 3. Dataset Composition

### Experience tiers

| Tier | Options |
|---|---:|
| comfort | 12 |
| high_quality | 8 |
| premium | 4 |

### Visa complexity

| Visa complexity | Options |
|---|---:|
| easy | 17 |
| moderate | 7 |
| complex | 0 |

## 4. Quality Issues Found

| Option | Issue | Interpretation | Handling |
|---|---|---|---|
| `TRIP-005` | `planning_confidence_score = 0` | Suspicious, not automatically impossible | Flagged as `suspicious_zero_confidence`; excluded from scoreable set for now |
| `TRIP-009` | `weather_risk_score = 105` | Invalid because score should be 0–100 | Flagged as `invalid_weather_risk_score`; risk-adjusted scoring left blank |
| `TRIP-013` | `flight_hours = -1.0` | Invalid because duration cannot be negative | Flagged as `invalid_flight_hours`; fatigue score left blank |

## 5. Derived Fields

The processed dataset adds:

| Field | Meaning |
|---|---|
| `data_quality_flag` | Semicolon-separated quality issue labels |
| `is_scoreable` | `True` only if no quality issue was flagged |
| `travel_fatigue_score` | Higher is better; derived from flight hours and layover penalty |
| `risk_adjusted_comfort_score` | Weighted blend of infant friendliness, comfort, and inverse weather risk |
| `value_score` | Risk-adjusted comfort divided by cost in lakhs |

## 6. Tier-Level Summary

| Tier | Options | Average cost INR | Average comfort | Average infant friendliness | Average flight hours |
|---|---:|---:|---:|---:|---:|
| comfort | 12 | 305,550 | 74.1 | 78.8 | 5.1 |
| high_quality | 8 | 518,204 | 77.4 | 77.4 | 6.4 |
| premium | 4 | 800,068 | 92.0 | 77.5 | 7.4 |

## 7. Top Options by Risk-Adjusted Comfort

Among scoreable rows:

| Rank | Option | Destination | Tier | Cost INR | Risk-adjusted comfort | Travel fatigue score | Value score |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | `TRIP-018` | Singapore | premium | 701,820 | 90.9 | 84.4 | 12.95 |
| 2 | `TRIP-015` | Maldives | high_quality | 685,125 | 82.2 | 43.0 | 12.00 |
| 3 | `TRIP-004` | Bali | comfort | 308,393 | 80.9 | 44.2 | 26.23 |
| 4 | `TRIP-017` | Phuket | high_quality | 451,440 | 80.4 | 53.2 | 17.81 |
| 5 | `TRIP-014` | Goa | comfort | 198,400 | 80.2 | 86.8 | 40.42 |

## 8. Early Interpretation

1. `TRIP-018` is the strongest comfort-led option: very high risk-adjusted comfort and low travel fatigue, but premium cost.
2. `TRIP-014` is the strongest value-led option among top performers: high risk-adjusted comfort, excellent fatigue score, and low cost.
3. Premium options improve comfort on average, but the cost jump is large.
4. High-quality options are not automatically better; some have long travel time or moderate visa complexity.
5. Data quality flags must be handled before recommendation scoring, otherwise invalid rows can distort rankings.

## 9. Dashboard KPI Candidates Confirmed

This first pass confirms these KPIs are useful:

| KPI | Why it matters |
|---|---|
| Scoreable option count | Shows whether enough valid options exist for recommendation |
| Flagged option count | Prevents blind use of bad data |
| Average cost by tier | Shows budget impact of tier choice |
| Average comfort by tier | Shows whether tier upgrade gives experience value |
| Low-fatigue high-comfort options | Identifies family-friendly shortlist |
| Top value score options | Balances comfort against cost |

## 10. Limitations

- Dataset is synthetic and small.
- Derived scores are simple heuristics, not validated recommendation logic.
- Weights for `risk_adjusted_comfort_score` are provisional.
- Real travel pricing, availability, weather, visas, and infant comfort would need external validation.
- No visual charts have been committed yet.

## 11. Capability Impact

This report supports moving these capabilities from Level 1 to Level 2:

- Data Cleaning: a synthetic dataset was validated and flagged.
- Exploratory Analysis: a first computed EDA summary was produced.

Recommendation Scoring and Dashboard Insight Design remain partial because no final scoring system or dashboard has been implemented yet.

## 12. Next Actions

1. Update `EVIDENCE.md` with this computed evidence.
2. Update `capabilities/data-cleaning.md` to Level 2.
3. Update `capabilities/exploratory-analysis.md` to Level 2.
4. Create a first recommendation scoring experiment using the scoreable rows.
5. Add a simple dashboard KPI specification based on this report.
