# datasets/

Dataset storage area.

Use this folder cautiously. Prefer synthetic or public datasets.

Suggested structure:

- `raw/` — immutable source data when safe and approved
- `interim/` — intermediate working data
- `processed/` — analysis-ready derived data

All datasets should be registered in `DATASETS.md` before serious use.
