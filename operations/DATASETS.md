# DATASETS.md — Dataset Registry

This file records datasets used by CodeMike.

## Dataset Rules

- Do not commit private, sensitive, or confidential raw data without explicit approval.
- Prefer synthetic datasets for learning and reproducible experiments.
- Record source, privacy level, purpose, and limitations.
- Every dataset used for evidence should be traceable.

## Privacy Levels

| Level | Meaning | Default Handling |
|---|---|---|
| Public | Publicly available data | Cite source and licence |
| Synthetic | Artificially generated data | Safe for learning, still document assumptions |
| Internal | Business/project data not public | Do not commit raw data without approval |
| Confidential | Sensitive organisational data | Avoid committing; use summaries or synthetic substitutes |
| Sensitive | Personal, health, financial, legal, or vulnerable-user data | Avoid unless explicitly approved and protected |
| Restricted | Credentials, secrets, highly regulated data | Never commit |

## Registered Datasets

| Dataset | Path | Type | Source | Purpose | Limitations |
|---|---|---|---|---|---|
| India destination expansion backlog v1 | `datasets/reference/destination_expansion_backlog_india_v1.csv` | Reference candidate backlog | Curated candidate list | Large India-only expansion backlog for destination database v2; 225 candidate rows for cleaning, enrichment, deduplication, and staged promotion | Candidate/unverified; not Planner-ready; may include duplicates, circuits, subdestinations, and inconsistent granularity |
| Destination tag dictionary v1 | `datasets/reference/destination_tag_dictionary.md` | Reference taxonomy | Curated controlled vocabulary | Controlled vocabulary for destination types, vibes, suitability values, fatigue bands, planning complexity, caution tags, and verification statuses | Taxonomy v1; may expand as product needs evolve |
| Destination database v2 strategy | `datasets/reference/destination_database_v2_strategy.md` | Reference strategy | CodeMike planning document | Strategy for scaling destination database from seed list to large Planner-ready database | Strategy document only; not data |
| India and near-India destination seed | `datasets/reference/india_region_destinations_seed.csv` | Reference seed | Curated seed list | Broad location database for Planner-style destination filtering, clustering, scoring, dashboards, and future PWA transfer | Seed-unverified; not suitable for live visa, safety, weather, flight, permit, or pricing decisions without current verification |
| Planner trip options sample | `datasets/synthetic/trip_options_sample.csv` | Synthetic | `synthetic-data/trip_options_generator.py` | First evidence path for data cleaning, EDA, recommendation scoring, and dashboard KPI thinking | Fictional values; intentionally includes invalid/suspicious rows; not suitable for real travel pricing or booking decisions |

## Destination Database Scale Snapshot

Current structured destination assets:

| Asset | Rows |
|---|---:|
| Seed destinations | 134 |
| India expansion candidates | 225 |
| Combined seed + candidate coverage | 359 |

The expansion backlog is deliberately separate from the seed database until QA, deduplication, enrichment, and verification improve row quality.

## Dataset Entry Template

```md
## Dataset Name

Path:
Type:
Source:
Privacy level:
Purpose:
Fields:
Limitations:
Allowed use:
Evidence linked:
```
