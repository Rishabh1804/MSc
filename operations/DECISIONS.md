# DECISIONS.md — CodeMike Decision Log

This file records important project decisions and the rationale behind them.

## Decision Record Template

```md
## YYYY-MM-DD — Decision title

Status: proposed / accepted / superseded

Decision:

Rationale:

Implications:

Related files:
```

## 2026-05-12 — Use layered destination database architecture

Status: accepted

Decision:

The destination database will use layered data assets rather than one giant CSV.

```text
seed destinations
→ candidate backlog
→ normalized backlog
→ master dataset
→ enriched master
→ scored Planner dataset
```

Rationale:

A single flat file would mix unverified candidates, generated fields, normalized fields, and Planner-ready rows. That would make quality control difficult and create a high risk of using unverified travel information in downstream products.

Implications:

- Candidate rows can grow aggressively without polluting the master dataset.
- Master rows require explicit promotion.
- Generated files should be reproducible from scripts.
- HTML browsers are review interfaces, not source of truth.

Related files:

- `datasets/reference/destination_database_v2_strategy.md`
- `datasets/reference/destination_expansion_backlog_india_v1.csv`
- `datasets/reference/destination_expansion_backlog_india_v1_normalized.csv`

## 2026-05-12 — Keep unverified travel data out of Planner-ready status

Status: accepted

Decision:

Destination records should not be marked Planner-ready until they pass source verification and QA.

Rationale:

Travel data can become unsafe or inaccurate quickly, especially visa rules, permits, medical access, flight routes, safety, seasonality, weather, and local restrictions.

Implications:

- Seed and candidate records remain explicitly unverified.
- Planner output must not treat this database as live travel truth yet.
- Verification status and planner use status are mandatory dimensions.

Related files:

- `datasets/reference/destination_tag_dictionary.md`
- `reports/evidence/destination-database-qa-v1.md`

## 2026-05-12 — Build taxonomy before scoring

Status: accepted

Decision:

Destination taxonomy must stabilise before recommendation scoring is expanded.

Rationale:

Scoring depends on clean fields. If tags are inconsistent, scoring will reward or penalise rows incorrectly.

Implications:

- Destination type, vibe, trip-style, caution, context, and workflow tags are separated.
- Tag dictionary is a core source of truth.
- Validation scripts must check taxonomy conformity before promotion.

Related files:

- `datasets/reference/destination_tag_dictionary.md`
- `docs/destination-tag-dictionary.html`
- `src/codemike/data/destination_taxonomy_validation.py`
- `src/codemike/data/destination_normalized_validation.py`

## 2026-05-12 — Use Termux for local execution artifacts

Status: accepted

Decision:

Scripts that generate files should be run locally in Termux when the GitHub connector cannot execute code in the repository.

Rationale:

The GitHub connector can edit files but cannot run repository scripts. Termux provides a practical local execution environment from Android.

Implications:

- The assistant creates scripts and scaffolds.
- The user runs generation/validation commands locally.
- Generated files are committed and pushed back to GitHub.

Related files:

- `NEXT_ACTIONS.md`
- `src/codemike/data/destination_backlog_normalization.py`
- `src/codemike/data/destination_normalized_validation.py`

## 2026-05-12 — Create lightweight work reports before formal PDFs

Status: accepted

Decision:

Create Markdown trackers and work-done reports now, but defer polished PDFs and portfolio reports until the master dataset and browser are stable.

Rationale:

The project has enough moving parts to need operational visibility now, but a final report would churn too often before the data model stabilises.

Implications:

- `ARTIFACT_INDEX.md`, `NEXT_ACTIONS.md`, trackers, and work-done reports are appropriate now.
- Final PDF/report pack is deferred.
- Formal portfolio material should follow scoring and Planner transfer.

Related files:

- `ARTIFACT_INDEX.md`
- `NEXT_ACTIONS.md`
- `trackers/destination-database-build-tracker.md`
- `reports/work-done/code-mike-destination-database-work-done-v1.md`
