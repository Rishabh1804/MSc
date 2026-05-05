# datasets/synthetic/

Synthetic datasets live here.

Synthetic data should be used when real data is unavailable, private, sensitive, or unnecessary for the learning objective.

## Rules

- Synthetic datasets must not contain real personal, family, customer, employee, health, or business-sensitive data.
- Each dataset should have a generator or clear creation note.
- Each dataset should be registered in `DATASETS.md`.
- Each dataset should include known assumptions and limitations.

## Current Synthetic Datasets

| Dataset | File | Generator | Purpose |
|---|---|---|---|
| Planner trip options sample | `trip_options_sample.csv` | `synthetic-data/trip_options_generator.py` | First evidence path for data cleaning, EDA, recommendation scoring, and dashboard thinking |
