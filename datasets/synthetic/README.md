# datasets/synthetic/

Synthetic datasets and the generators that produce them live here. Batch 6 merged the original `/synthetic-data/` (generators) into this directory (which already held the generated samples), so generator and sample now sit side by side.

Synthetic data should be used when real data is unavailable, private, sensitive, or unnecessary for the learning objective.

## Purpose

- practise safely
- prototype analytics
- test dashboards
- avoid exposing sensitive business or personal data
- simulate edge cases

## Rules

- Synthetic datasets must not contain real personal, family, customer, employee, health, or business-sensitive data.
- Each dataset should have a generator or clear creation note.
- Each dataset should be registered in `../../operations/DATASETS.md`.
- Each dataset should include known assumptions and limitations.

## Current Synthetic Datasets

| Dataset | File | Generator | Purpose |
|---|---|---|---|
| Planner trip options sample | `trip_options_sample.csv` | `trip_options_generator.py` | First evidence path for data cleaning, EDA, recommendation scoring, and dashboard thinking |

## Generator candidates

Tracked here for future generator scope. Cross-reference with `../../operations/EXPERIMENTS.md` when one is built.

- trip options (built; see above)
- sales orders
- production batches
- inventory
- business KPIs
- plating process data
