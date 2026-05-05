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
| Planner trip options sample | `datasets/synthetic/trip_options_sample.csv` | Synthetic | `synthetic-data/trip_options_generator.py` | First evidence path for data cleaning, EDA, recommendation scoring, and dashboard KPI thinking | Fictional values; intentionally includes invalid/suspicious rows; not suitable for real travel pricing or booking decisions |

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
