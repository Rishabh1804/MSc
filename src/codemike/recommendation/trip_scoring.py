"""Reusable trip-option recommendation scoring utilities.

This module converts the first synthetic trip-options scoring experiment into
reusable Python functions. It is intentionally simple and transparent.

The functions operate on dictionaries so they can be used with csv.DictReader,
pandas records, JSON-like payloads, or future PWA/API integrations.

Status:
    Prototype utility extracted from EXP-001 and EXP-002.

Limitations:
    - Designed around the synthetic Planner trip-options schema.
    - Weights and penalties are provisional.
    - Real travel decisions require live validation and human review.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping


ScoreWeights = Mapping[str, float]
TripRow = Mapping[str, object]


V1_WEIGHTS: dict[str, float] = {
    "risk_adjusted_comfort_score": 0.30,
    "travel_fatigue_score": 0.20,
    "cost_score": 0.20,
    "visa_score": 0.10,
    "planning_confidence_score": 0.10,
    "novelty_score": 0.10,
}


DEFAULT_SCENARIOS: dict[str, dict[str, float]] = {
    "family_comfort": {
        "risk_adjusted_comfort_score": 0.35,
        "travel_fatigue_score": 0.25,
        "cost_score": 0.15,
        "visa_score": 0.10,
        "planning_confidence_score": 0.10,
        "novelty_score": 0.05,
    },
    "budget_sensitive": {
        "risk_adjusted_comfort_score": 0.25,
        "travel_fatigue_score": 0.15,
        "cost_score": 0.35,
        "visa_score": 0.10,
        "planning_confidence_score": 0.10,
        "novelty_score": 0.05,
    },
    "premium_comfort": {
        "risk_adjusted_comfort_score": 0.45,
        "travel_fatigue_score": 0.15,
        "cost_score": 0.05,
        "visa_score": 0.10,
        "planning_confidence_score": 0.15,
        "novelty_score": 0.10,
    },
    "low_fatigue": {
        "risk_adjusted_comfort_score": 0.25,
        "travel_fatigue_score": 0.35,
        "cost_score": 0.15,
        "visa_score": 0.10,
        "planning_confidence_score": 0.10,
        "novelty_score": 0.05,
    },
    "novelty_heavy": {
        "risk_adjusted_comfort_score": 0.20,
        "travel_fatigue_score": 0.15,
        "cost_score": 0.15,
        "visa_score": 0.10,
        "planning_confidence_score": 0.10,
        "novelty_score": 0.30,
    },
}


@dataclass(frozen=True)
class ScoreResult:
    """Scoring result for one trip option."""

    option_id: str
    weighted_score: float
    penalty_points: float
    recommendation_score: float
    penalty_reasons: tuple[str, ...]


def _as_float(row: TripRow, field: str, default: float = 0.0) -> float:
    """Safely read a numeric field from a mapping."""

    value = row.get(field, default)
    if value is None or value == "":
        return default
    return float(value)


def _as_text(row: TripRow, field: str, default: str = "") -> str:
    """Safely read a text field from a mapping."""

    value = row.get(field, default)
    if value is None:
        return default
    return str(value)


def validate_weights(weights: ScoreWeights) -> None:
    """Validate that weights are non-negative and sum to approximately 1.0."""

    if not weights:
        raise ValueError("weights must not be empty")

    negative = {key: value for key, value in weights.items() if value < 0}
    if negative:
        raise ValueError(f"weights must be non-negative: {negative}")

    total = sum(weights.values())
    if abs(total - 1.0) > 0.001:
        raise ValueError(f"weights must sum to 1.0, got {total:.4f}")


def calculate_cost_score(cost_inr: float, min_cost: float, max_cost: float) -> float:
    """Return a 0-100 score where lower cost is better."""

    if max_cost <= min_cost:
        return 100.0
    score = 100.0 * (max_cost - cost_inr) / (max_cost - min_cost)
    return round(max(0.0, min(100.0, score)), 2)


def calculate_visa_score(visa_complexity: str) -> float:
    """Map visa complexity to a simple 0-100 score."""

    mapping = {
        "easy": 100.0,
        "moderate": 70.0,
        "complex": 35.0,
    }
    return mapping.get(visa_complexity.lower().strip(), 50.0)


def calculate_penalties(row: TripRow) -> tuple[float, tuple[str, ...]]:
    """Calculate penalty points and reasons for one trip option."""

    penalty_points = 0.0
    reasons: list[str] = []

    estimated_cost = _as_float(row, "estimated_cost_inr")
    flight_hours = _as_float(row, "flight_hours")
    weather_risk = _as_float(row, "weather_risk_score")
    visa_complexity = _as_text(row, "visa_complexity").lower().strip()

    if estimated_cost > 700_000:
        penalty_points += 3.0
        reasons.append("high_cost")
    if flight_hours > 8:
        penalty_points += 5.0
        reasons.append("high_fatigue")
    if visa_complexity == "moderate":
        penalty_points += 3.0
        reasons.append("visa_friction")
    if weather_risk > 55:
        penalty_points += 4.0
        reasons.append("weather_risk")

    return penalty_points, tuple(reasons)


def calculate_score(row: TripRow, weights: ScoreWeights = V1_WEIGHTS) -> ScoreResult:
    """Calculate a recommendation score for one row.

    The row is expected to contain derived fields such as
    `risk_adjusted_comfort_score`, `travel_fatigue_score`, `cost_score`, and
    `visa_score`. Missing fields default to zero, which makes missing data
    visible by lowering score rather than silently inventing value.
    """

    validate_weights(weights)

    weighted_score = sum(_as_float(row, field) * weight for field, weight in weights.items())
    penalty_points, reasons = calculate_penalties(row)
    recommendation_score = weighted_score - penalty_points

    return ScoreResult(
        option_id=_as_text(row, "option_id", "UNKNOWN"),
        weighted_score=round(weighted_score, 2),
        penalty_points=round(penalty_points, 2),
        recommendation_score=round(recommendation_score, 2),
        penalty_reasons=reasons,
    )


def rank_options(rows: Iterable[TripRow], weights: ScoreWeights = V1_WEIGHTS) -> list[tuple[int, TripRow, ScoreResult]]:
    """Rank trip options by recommendation score.

    Returns a list of tuples:
        (rank, original_row, score_result)
    """

    scored = [(row, calculate_score(row, weights)) for row in rows]
    scored.sort(key=lambda item: item[1].recommendation_score, reverse=True)
    return [(rank, row, score) for rank, (row, score) in enumerate(scored, start=1)]


def scenario_sensitivity(
    rows: Iterable[TripRow],
    scenarios: Mapping[str, ScoreWeights] = DEFAULT_SCENARIOS,
) -> dict[str, list[tuple[int, TripRow, ScoreResult]]]:
    """Rank options under multiple weighting scenarios."""

    row_list = list(rows)
    return {
        scenario_name: rank_options(row_list, weights)
        for scenario_name, weights in scenarios.items()
    }
