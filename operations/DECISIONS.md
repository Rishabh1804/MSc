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

## 2026-05-18 — Adopt no-assumption + live-data + free-tier-only policy for enrichment (§19)

Status: accepted

Decision:

Forward enrichment work follows a no-assumption rule. Every enriched field is either source-backed (with citation) or `unknown_pending_research`. Workspace judgement, opinionated heuristics, and regional stereotypes are rejected for v2. v1.0 enrichment artifacts are *retained as the heuristic baseline* — not deleted, not rolled back, not relabelled inside files — for ongoing use as a diff target and as a research-priority signal. Live = refresh on query per §19.4; v1 stays free-tier-only per §19.3.

Rationale:

The E1 v1.0 ship surfaced category-level calibration findings (strategy doc §18) the v1 spec did not anticipate — the Queue S + Queue M overshoots are evidence that the heuristic regime is mis-shaped for the input data shape, not a parameter-tweak problem. The Big Data Analytics module backbone (store, refine, categorise, analyse) reads as a discipline-grade prescription against substituting workspace judgement for source data when source data is reachable. The policy revision is the *Improve* step of the CodeMike operating loop, recorded as durable text rather than absorbed silently into the next ship.

Implications:

- Forward-only — v1.0 artifacts retained as heuristic baseline; no rollback
- P15 (E1 v1.0): stays `done` as heuristic baseline
- P17 (E2 manual-review sessions): **on hold** pending v2; queues retained as research-priority signals
- P18 (E1 v1.1 calibration spec changes): **superseded** — all four §18.3–§18.5 recommendations were calibration moves under the heuristic regime, moot under no-assumption
- New P19 (source registry + free-tier ETL), P20 (v2 strategy doc), P21 (v2 enrichment service)
- v1.0 script renames to `destination_master_enrichment_v0_heuristic.py` in P21 per §19.2; carries a header docstring warning that v0 logic is not a template for v2
- Free-tier source ladder (§19.3): Tier 1 government/official APIs, Tier 2 reputable open datasets, Tier 3 reputable scraped sources with provenance, Tier 4 workspace-curated synthesis of Tier 1–3 with citations per derived value. Rejected: workspace judgement / opinionated heuristics / regional stereotypes
- Unknown discipline (§19.5): rows ship with `unknown` + `field_source = "no_source_available"` + `field_manual_research_needed = true` + `field_basis` prose; downstream consumers must distinguish `known` vs `unknown_pending_research` vs not-applicable
- Free-tier coverage gaps are named honestly: live visa rules, current park closures, current permits will be `unknown_pending_research` for most rows in v2 — that's the rule working as designed, not a v2 spec failure
- Paid-tier upgrade is a future budget question through `charter/BUDGET.md` + `charter/TOOLING.md`

Related files:

- `datasets/reference/destination_master_enrichment_strategy.md` (§18 calibration findings + §19 policy transition + §19.6 architecture resolution)
- `operations/NEXT_ACTIONS.md` (P17 on hold; P18 superseded; new P19/P20/P21)
- `operations/PROJECT_LOG.md` (2026-05-18 — Policy transition entry)
- `operations/EXPERIMENTS.md` (EXP-003 — the worked experiment that produced the calibration findings)
- `charter/TOOLING.md` (free-tier source candidates pre-approved by this PR)

## 2026-05-18 — Two-tier enrichment architecture (Option b) — stable-derived + live-volatile

Status: accepted

Decision:

The v2 enrichment architecture has two layers per strategy doc §19.6: a **stable-derived layer** (route distance, hospital POIs, baseline climatology, altitude profile) refreshed on batch cadence and persisted to disk, and a **live-volatile layer** (current flight availability, current weather, current permit/visa, current park closure) fetched per Planner query and never cached. Each output field carries a tier assignment in the v2 strategy doc.

Rationale:

Three options were considered. Option (a) all-stable was implicitly rejected by §19.4 (live data must refresh on query for fields that genuinely change daily). Option (c) all-live fails the free-tier rate-limit math: ~4 live API calls per query × every dimension × every query would exhaust free-tier ceilings (50–1000 requests/day) within a handful of Planner sessions. Option (d) cached-with-TTL was rejected because TTL caching silently serves stale data for fields whose update rate in the world is faster than the TTL — a category violation of §19's no-assumption rule. Option (b) two-tier preserves the §19.4 freshness contract for the fields that genuinely change daily, caches only where caching aligns with the field's actual update rate in the world, and fits the free-tier ceiling at ~4 live API calls × 250 queries/day = 1000 requests/day (sustainable for single-user workspace + early Planner usage).

Implications:

- P19 (source registry + free-tier ETL) scope splits into (a) stable-derived batch ETL producing `destinations_master_v2_derived.csv` and (b) live-volatile per-query service interface
- P20 (v2 strategy doc) per-field tier assignment is a mandatory output — every field gets tier-stable or tier-live (no third state)
- Every output field carries a `source_id` + `fetched_at` so downstream consumers can audit which layer the value came from
- `destination_sources_v1.csv` (the source registry the v2 database strategy §Core Tables 4 named) is built alongside the stable-derived layer
- Free-tier rate-limit + endpoint + auth method for each chosen source is documented in the source registry — caps are binding architectural constraints, not advisory
- Paid-tier upgrade trigger: if Planner usage materially exceeds free-tier ceilings, the upgrade decision is a `charter/BUDGET.md` question, not a silent caching tweak
- P20 is **unblocked** by this decision

Related files:

- `datasets/reference/destination_master_enrichment_strategy.md` (§19.6 — rejected alternatives preserved for audit trail)
- `operations/NEXT_ACTIONS.md` (P19 / P20 / P21 scope updated)
- `operations/PROJECT_LOG.md` (2026-05-18 — Policy transition entry, §19.6 resolution section)
