# datasets/reference/

Reference datasets live here.

These are curated knowledge/data assets used to support repeated analysis, recommendation scoring, dashboards, or transfer into product projects.

## Rules

- Reference datasets are not automatically factual authority.
- Records should include a verification status.
- Time-sensitive fields such as visa rules, flight routes, hotel pricing, safety, or weather should be verified before real use.
- Prefer stable descriptive fields in the seed database.
- Avoid committing private or sensitive data.

## Current Reference Datasets

| Dataset | File | Purpose | Status |
|---|---|---|---|
| India + near-India destination seed | `india_region_destinations_seed.csv` | Broad location database for Planner-style destination scoring | seed_unverified |

## Verification Status Values

- `seed_unverified` — initial curated entry; useful for prototyping only
- `source_verified` — checked against a reliable source
- `product_ready` — validated enough for transfer to a product workflow
- `retired` — no longer recommended for use
