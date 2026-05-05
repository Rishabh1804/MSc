# Exploratory Data Analysis — Synthetic Planner Trip Options

Date: 2026-05-05  
Author: CodeMike  
Linked module: `modules/00-foundations/`, `modules/03-data-mining-visualisation/`  
Dataset: `datasets/synthetic/trip_options_sample.csv`  
Generator: `synthetic-data/trip_options_generator.py`  
Privacy level: Synthetic  
Objective: Produce the first evidence artifact for data cleaning and exploratory analysis.  
Decision supported: Early trip-option comparison and recommendation scoring design.

## 1. Objective

Understand the structure, quality issues, and decision-relevant signals in a synthetic Planner-style trip options dataset.

This exercise is intended to activate the following capabilities:

- `capabilities/data-cleaning.md`
- `capabilities/exploratory-analysis.md`
- `capabilities/recommendation-scoring.md`, partially
- `capabilities/dashboard-insight-design.md`, partially

## 2. Dataset Summary

The dataset contains fictional travel options with cost, travel friction, visa complexity, comfort, infant friendliness, weather risk, novelty, and planning confidence fields.

Important note: the dataset intentionally contains a few invalid or suspicious values so CodeMike can exercise data cleaning judgement.

## 3. Expected Schema

| Column | Meaning | Expected type | Expected range / values |
|---|---|---|---|
| `option_id` | Unique trip option identifier | string | unique |
| `destination` | Fictional destination name | string | non-empty |
| `experience_tier` | Experience category | category | comfort / high_quality / premium |
| `estimated_cost_inr` | Estimated total cost | integer | positive |
| `flight_hours` | Approximate travel duration | float | greater than 0 |
| `layovers` | Number of layovers | integer | 0, 1, or 2 |
| `visa_complexity` | Visa/planning difficulty | category | easy / moderate / complex |
| `infant_friendliness_score` | Family suitability score | integer | 0–100 |
| `comfort_score` | Comfort score | integer | 0–100 |
| `weather_risk_score` | Weather risk score | integer | 0–100, lower is better |
| `novelty_score` | Novelty/interest score | integer | 0–100 |
| `planning_confidence_score` | Confidence in planning quality | integer | 0–100 |
| `notes` | Qualitative note | string | non-empty |

## 4. Data Quality Checks

Use `patterns/data-cleaning-checklist.md`.

Initial known issues to verify:

- `TRIP-005` has `planning_confidence_score = 0`, suspicious rather than automatically invalid.
- `TRIP-009` has `weather_risk_score = 105`, invalid because the expected range is 0–100.
- `TRIP-013` has `flight_hours = -1.0`, invalid because duration cannot be negative.

## 5. Analysis Questions

1. Which options appear family-friendly and low-friction?
2. Which options are expensive but high-comfort?
3. Which options have hidden risks such as weather, visa friction, or low confidence?
4. What fields should be used in a recommendation score?
5. What KPIs would be useful in a Planner dashboard?

## 6. Candidate Derived Fields

Possible fields for future scoring:

- `cost_band`
- `travel_fatigue_score`
- `family_comfort_score`
- `risk_penalty`
- `value_score`
- `recommendation_score`

## 7. Early Findings to Confirm

These are hypotheses until code-based EDA verifies them:

1. Family-friendly options should balance infant friendliness, short travel time, easy visa complexity, and comfort.
2. Premium options tend to increase comfort but may exceed soft budget limits.
3. Data quality validation is required before recommendation scoring.
4. Dashboard design should separate summary ranking from risk explanation.

## 8. Cleaning Decisions Required

| Issue | Proposed handling | Reason |
|---|---|---|
| `weather_risk_score > 100` | flag as invalid and exclude from scoring until corrected | risk scale is bounded |
| `flight_hours <= 0` | flag as invalid and exclude from travel fatigue calculations | impossible duration |
| `planning_confidence_score = 0` | flag as suspicious, keep for review | could mean missing confidence or very low confidence |

## 9. Dashboard KPI Candidates

| KPI | Purpose |
|---|---|
| Average estimated cost by tier | Understand budget impact |
| Average comfort score by tier | Compare quality level |
| Low-fatigue option count | Identify family-suitable choices |
| Options with data quality flags | Prevent blind recommendations |
| High-comfort under soft cap | Identify practical shortlist |
| Average weather risk by destination | Surface hidden planning risks |

## 10. Next Actions

- Convert this scaffold into a runnable notebook or script.
- Apply the data cleaning checklist.
- Produce a clean dataset or flagged dataset.
- Create first EDA findings section with computed evidence.
- Update `EVIDENCE.md`.
- Consider raising data cleaning and exploratory analysis maturity from Level 1 to Level 2 only after computed evidence exists.

## Related Files

- `datasets/synthetic/trip_options_sample.csv`
- `synthetic-data/trip_options_generator.py`
- `patterns/data-cleaning-checklist.md`
- `patterns/eda-notebook-template.md`
- `patterns/recommendation-scoring-pattern.md`
- `patterns/dashboard-kpi-pattern.md`
- `capabilities/data-cleaning.md`
- `capabilities/exploratory-analysis.md`
