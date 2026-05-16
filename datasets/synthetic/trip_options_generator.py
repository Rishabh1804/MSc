"""Generate a synthetic Planner-style trip options dataset.

This script creates fictional travel options for CodeMike's first evidence path.
The data is synthetic and does not represent real bookings, prices, people, or vendors.

Usage:
    python synthetic-data/trip_options_generator.py

Output:
    datasets/synthetic/trip_options_sample.csv
"""

from __future__ import annotations

import csv
import random
from dataclasses import dataclass, asdict
from pathlib import Path


OUTPUT_PATH = Path("datasets/synthetic/trip_options_sample.csv")


@dataclass(frozen=True)
class TripOption:
    option_id: str
    destination: str
    experience_tier: str
    estimated_cost_inr: int
    flight_hours: float
    layovers: int
    visa_complexity: str
    infant_friendliness_score: int
    comfort_score: int
    weather_risk_score: int
    novelty_score: int
    planning_confidence_score: int
    notes: str


def generate_rows(n: int = 24, seed: int = 42) -> list[TripOption]:
    """Generate deterministic fictional trip options."""

    random.seed(seed)

    destinations = [
        "Bali",
        "Phuket",
        "Singapore",
        "Dubai",
        "Mauritius",
        "Maldives",
        "Sri Lanka",
        "Vietnam",
        "Langkawi",
        "Kuala Lumpur",
        "Goa",
        "Andaman",
    ]
    tiers = ["comfort", "high_quality", "premium"]
    visa_levels = ["easy", "moderate", "complex"]
    notes = [
        "shortlisted for family comfort",
        "strong resort availability",
        "higher transit fatigue",
        "good food and logistics",
        "weather needs checking",
        "premium option with low friction",
        "budget pressure visible",
        "good backup option",
    ]

    rows: list[TripOption] = []

    for idx in range(1, n + 1):
        destination = random.choice(destinations)
        tier = random.choice(tiers)
        tier_multiplier = {"comfort": 1.0, "high_quality": 1.35, "premium": 1.8}[tier]
        base_cost = random.randint(180_000, 520_000)
        cost = int(base_cost * tier_multiplier)

        flight_hours = round(random.uniform(2.0, 12.5), 1)
        layovers = random.choices([0, 1, 2], weights=[45, 40, 15], k=1)[0]
        visa_complexity = random.choices(visa_levels, weights=[55, 30, 15], k=1)[0]

        infant_friendliness = random.randint(45, 95)
        comfort = random.randint(50, 98)
        weather_risk = random.randint(10, 75)
        novelty = random.randint(35, 95)
        confidence = random.randint(50, 95)

        # Intentionally introduce a few realistic imperfections for cleaning exercises.
        if idx == 5:
            confidence = 0  # suspicious value requiring review
        if idx == 9:
            weather_risk = 105  # invalid out-of-range value
        if idx == 13:
            flight_hours = -1.0  # invalid value

        rows.append(
            TripOption(
                option_id=f"TRIP-{idx:03d}",
                destination=destination,
                experience_tier=tier,
                estimated_cost_inr=cost,
                flight_hours=flight_hours,
                layovers=layovers,
                visa_complexity=visa_complexity,
                infant_friendliness_score=infant_friendliness,
                comfort_score=comfort,
                weather_risk_score=weather_risk,
                novelty_score=novelty,
                planning_confidence_score=confidence,
                notes=random.choice(notes),
            )
        )

    return rows


def write_csv(rows: list[TripOption], output_path: Path = OUTPUT_PATH) -> None:
    """Write generated rows to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


if __name__ == "__main__":
    generated_rows = generate_rows()
    write_csv(generated_rows)
    print(f"Wrote {len(generated_rows)} rows to {OUTPUT_PATH}")
