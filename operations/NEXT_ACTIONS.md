# NEXT_ACTIONS.md — CodeMike Operational Queue

This file tracks the current operational queue for CodeMike. It is intentionally practical and action-oriented.

## Status Legend

| Status | Meaning |
|---|---|
| `todo` | Not started |
| `doing` | In progress |
| `blocked` | Waiting on another step/tool/user action |
| `done` | Completed |
| `deferred` | Intentionally later |

## Immediate Actions

| Priority | Action | Owner/Mode | Status | Notes |
|---:|---|---|---|---|
| 1 | Master validation report clean | User + Assistant | done | `master_structurally_valid_not_planner_ready` |
| 2 | Create master HTML browser | Assistant / GitHub connector | done | `docs/destination-master-browser.html` |
| 3 | Verify GitHub Pages render at canonical URLs | User / Browser | doing | **2026-05-18 update**: static-HTML fetch from the session confirms both URLs serve 200; canonical eyebrow reads **v1.2** ✓ (latest deploy is live); trust banner + header + stats banner present. Two open items remain: (a) **live browser verification still required** — static fetch cannot execute JS, so it cannot confirm the client-side dataset fetch actually populates records; saw both "Loading…" and "Couldn't load the master dataset" text in the static markup which is likely hidden state-toggle DOM, but browser-verify confirms; (b) see new priority 15 (F-ARC-1) for the archive-page label gap surfaced in the same check. |
| 4 | Implement Destination Master Browser v1.1 | Assistant / CodeMike | **done** | Landed across two PRs (#10 core + this PR polish/walk-through). Canonical at `docs/destination-master-browser.html`; v1 archived at `-v1.0.html`. Full 13-gate Playwright walk-through: **15/15 pass** with zero console errors. Capability transfer recorded in `operations/TRANSFER_LOG.md` (Transfer 1); SKILL_MAP UI/UX skill promoted to level 5; six CAPABILITIES rows promoted to maturity 4. |
| 5 | Design master enrichment strategy | Assistant / CodeMike | **done** | Strategy v1 landed at `datasets/reference/destination_master_enrichment_strategy.md` (~540 lines). Defines: storage shape (separate enriched layer `destinations_master_v2_enriched.csv`; in-master `family_suitability` / `access_complexity` / `best_season_hint` columns reclassified as **frozen seed-lineage** — informational, not authoritative); enrichment field catalogue (origin-fit per-origin, suitability decomposed into infant/family/senior/couple, fatigue/complexity decomposed by drivers, medical access with pediatric subset, season/weather decomposed); heuristic derivation formulas with explicit asymmetric-cost biasing (Topic 4 §3); three-batch manual-review discipline (O origin / S suitability / M medical) with anchor-pattern reviewer notes (Lyra pattern, PRs #20–24); three-phase rollout (E1 script → E2 manual review × 3 sessions → E3 source-verified promotion, demand-driven). Names six honest limitations that remain blocked from `planner_ready` (live facts, per-fact source verification, real-user evaluation, multi-origin coverage, accessibility-specific enrichment, multi-language enrichment). Audit-shape rules for data-layer PRs added (distribution-diff reports on every formula bump). CCU + IXR named as v1 concrete origins. |
| 6 | Start destination scoring v1 | Assistant / CodeMike | deferred | Unblocked after the enriched layer (priority 15 — E1) is built and at least one manual-review batch (E2) completes. Reads the enriched layer; combines fields into Planner-side recommendation scores. Out of scope for the enrichment strategy doc. |
| 7 | DES-001 grade report v3 | Assistant / CodeMike | doing | Cumulative DES-001 grade after Topics 1–6 (the three-topic push closure). Lives at `feedback/DES-001-grade-report-v3.md`. Includes HCD compliance verdict from Topic 5 + Gestalt compliance verdict from Topic 6 + scope-incompleteness adjustment scaled down from −6 toward 0 as 6/12 topics now closed. Ships in this same PR. |
| 8 | Browser v1.1.x polish PR — Lab 06 visual-treatment fixes | Assistant / CodeMike | **done** | All six v1.1.x fixes shipped in the v1.1.x polish PR: Fix #1 verif-pill (closes F-GES-1 + F-GES-2); Fix #2 view-toggle separator (F-GES-4); Fix #3 active-filter summary tint (F-GES-6); Fix #4 sortable-header ↕ glyph (F-GES-3); Fix #5a search-vs-selects separator (F-GES-5 visual half); Fix #6 caution-chip divider (R1 Trade-off → Pass). After-screenshots + computed leverage scores landed in `design/foundations/topic-06-gestalt-audit.md` audit addendum. Zero walk-through regression (19/19 pass). Fix #5b stays deferred to v1.2 (see priority 10). |
| 9 | Recruit Sponsor Reviewer for v1.2 | Rishabh / Assistant | doing | **Framework landed**: `design/foundations/sponsor-reviewer-brief.md` defines profile + 3-hour session shape (orient / two scoped tasks / structured debrief) + feedback-format + closure mapping. Rishabh decides recruitment source (internal network / Codex network / paid hire / self-as-Sponsor fallback). U-CONF-1..4 acceptance criteria now landed in `ux-acceptance-criteria.md` per the brief's evaluation targets — closes Lab 05 F-REQ-1. Open work: first recruitment ask + first session. |
| 10 | Browser v1.2 implementation PR (batch-promote-confirm subset) | Assistant / CodeMike | **done** (subset) | Lab 04 Loop 1 batch-promote-confirm modal shipped to `docs/destination-master-browser.html`. U-CONF-1..4 walkthrough 10/10 pass. v1.1 walkthrough 19/19 pass (zero regression). Transfer 3 recorded. Open: the other v1.2 inheritance items (Lab 05 systems-context-of-use doc + inclusion-lens requirements + Lab 06 Fix #5b grammar unification) remain *deferred* pending Sponsor Reviewer (priority 9) — they're not part of this PR's scope. |
| 11 | Audit 2 trigger — Gestalt + HCD re-audit after v1.2 ships | Assistant / Lyra | deferred | Per audit doc honest limitations: future Audit 2 should compare against Audit 1's findings to verify the v1.2 closures actually closed the v1.1 violations. Triggers after the v1.2 implementation PR ships. |
| 12 | F-MOB-2 mobile table layout — horizontal-scroll on narrow viewports | Assistant / CodeMike | deferred | The 8-column records table + new v1.2 select-checkbox column = 9 columns. On ~360px mobile viewports the table overflows horizontally; reviewer must scroll right to see what they're selecting then scroll left to find the batch action bar. Surfaced 2026-05-18 by real-device user screenshots. Structural fix is mobile-friendly table layout (collapsing-to-cards / horizontal-scroll-container with sticky first column / responsive column hide) — v2.x scope per Lab 05 inclusion-lens F-W3C-1 (device sub-dimension). Cosmetic workaround: switch to Cards view on mobile (no multi-select there). |
| 13 | F-MOB-5 mobile-viewport variant for capture-fixes.js / walkthrough scripts | Assistant / CodeMike | deferred | Provisional rule landed in `topic-06-gestalt-audit.md` Audit Addendum 2 + `operations/FAILURE_LOG.md` (Unicode-glyph failure): every visual-treatment change with a CSS-content-character OR position:absolute change gets a mobile-viewport screenshot before merge. Implementation: extend `verification/v1.1.x-polish/capture-fixes.js` with a `viewport=360x640` variant; same for future polish PRs. Defer until the next polish PR cycle is in scope. |
| 14 | DES-001 Topics 7–12 | Assistant / CodeMike | deferred | The remaining six DES-001 topics (Fitts' law / Button states / Typography / Color theory / Web design / grid layout / Design systems) per the execution plan. **Currently STOPPED per the ratified three-topic-push goal — do not start without an explicit user instruction.** |
| 15 | Build E1 enrichment script + validator + manual-review queues | Assistant / CodeMike | **done** | E1 pass landed. Files: `src/codemike/data/destination_master_enrichment_v1.py` (deterministic heuristic pipeline; ~640 lines stdlib-only); `src/codemike/data/destination_master_enrichment_validation.py` (structural + controlled-values + band-vs-score + pediatric-vs-medical + heuristic-default-state checks); `datasets/reference/origin_catchment_v1.json` (CCU + IXR lookup; format changed from YAML to JSON per pure-stdlib discipline, noted in §18.7 of the strategy doc). Outputs: `datasets/reference/destinations_master_v2_enriched.csv` (359 rows; every row at `verification_status=enriched_unverified` + `planner_use_status=needs_verification` + `source_confidence=low`); `reports/evidence/destination-master-v2-enrichment-report.md` (full distributions); `reports/evidence/destination-master-v2-enrichment-validation-report.md` (readiness=`enriched_structurally_valid_not_planner_ready`; 0 violations); three manual-review queue CSVs at `reports/evidence/destination-master-v2-enrichment-manual-review-queues/{O,S,M}.csv`. Strategy doc §18 (v1 implementation amendments) added covering data-inspection findings, catchment tuning, queue-size calibration findings, fatigue-band skew, and reproducibility note. **Queue sizes**: O=0 ✓ (after catchment tuning), S=155 (>>25/session cap), M=257 (>>20/session cap) — calibration findings recommend v1.1 spec changes (see priority 18). |
| 16 | F-ARC-1: v1.0 archive page lacks a version banner | Assistant / CodeMike | todo | Surfaced 2026-05-18 by Pages-verification static fetch. `destination-master-browser-v1.0.html` renders, but the page title reads "Destinations Master v2 Browser" and there is no visible v1.0 / archive label, so a user landing on the URL cannot distinguish it from the canonical v1.2 page. Fix: add an "Archived — v1.0 (current is v1.2 → link)" banner near the page header. Small visual-treatment PR; should run the post-v1.2.1 mobile-viewport capture (audit-shape rule). |
| 17 | E2 — manual-review sessions O / S / M | Rishabh / Reviewer | **on hold** | On hold per strategy doc §19.8 (policy transition to no-assumption + live-data). The three queues are retained as **research-priority signals** — rows the v1.0 heuristic was least confident about are likely candidates for manual source-research in the v2 workstream. Re-evaluate after P20 (v2 strategy doc) lands; the v2 enrichment may render some queue entries moot. |
| 18 | ~~E1 v1.1 calibration spec changes~~ | Assistant / CodeMike | **superseded** | Superseded 2026-05-18 by strategy doc §19 (no-assumption + live-data rule). All four v1.1 recommendations from §18.3–§18.5 (drop "all four bands identical" trigger; add region/resort_zone medical branch; split M into critical/standard; rebalance fatigue bands) were calibration moves under the heuristic regime — moot under no-assumption. Replaced by priorities 19 / 20 / 21 below. |
| 19 | Source registry + free-tier ETL layer (stable + live split) | Assistant / CodeMike | todo | Per §19.6 two-tier architecture: build (a) the **stable-derived layer** as a batch ETL producing `destinations_master_v2_derived.csv` from free-tier sources — route distance from CCU/IXR via OpenFlights+OurAirports, hospital POI distances via OSM Overpass, baseline climatology via IMD/ECMWF, altitude profile via SRTM/free DEM; (b) the **live-volatile fetch layer** as a per-query service interface for current flight availability, current weather, current permit/visa, current park closure — never cached. Also build `destination_sources_v1.csv` (the source registry the v2 database strategy §Core Tables 4 named). Each output field carries a `source_id` + `fetched_at`. Each source's free-tier rate-limit + endpoint + auth method documented. |
| 20 | v2 no-assumption enrichment strategy doc | Assistant / CodeMike | todo | New document at `datasets/reference/destination_master_enrichment_strategy_v2.md`. Supersedes §§0–17 of the v1 strategy. **Unblocked** by §19.6 decision (Option b two-tier ratified 2026-05-18). Specifies: no-assumption pipeline per §19.1; source ladder per §19.3 (free-tier-only in v1); live-refresh discipline per §19.4; unknown + `manual_research_needed` discipline per §19.5; two-tier architecture per §19.6. Each field in the v2 catalogue gets: (a) chosen source(s); (b) refresh tier (stable-derived vs live-volatile); (c) derivation rule; (d) `unknown_pending_research` fallback condition. |
| 21 | v2 source-backed enrichment service | Assistant / CodeMike | todo | Implements the v2 strategy (P20). New package at `src/codemike/data/destination_master_enrichment_v2/` (broken up because the pipeline is bigger than v1.0). The v1.0 script (`destination_master_enrichment_v1.py`) is renamed to `destination_master_enrichment_v0_heuristic.py` and preserved as the diff-baseline per §19.2. The v2 service produces a refreshed enriched layer (two-tier per §19.6) with per-row + per-field source citations + `manual_research_needed` flags. Blocked on P19 + P20. |

## Current Blocking Item

```text
Verify destination-master-browser.html on GitHub Pages
```

Open:

```text
https://rishabh1804.github.io/MSc/destination-master-browser.html
```

Also available from:

```text
https://rishabh1804.github.io/MSc/
```

## Current Master Dataset Summary

Created:

```text
datasets/reference/destinations_master_v2.csv
reports/evidence/destination-master-v2-promotion-report.md
reports/evidence/destination-master-v2-validation-report.md
docs/destination-master-browser.html
```

Master validation:

```text
Rows checked: 359
Invalid location types: 0
Invalid vibe tags: 0
Readiness: master_structurally_valid_not_planner_ready
```

## Next Design Step

Closed 2026-05-18: master enrichment strategy v1 landed at `datasets/reference/destination_master_enrichment_strategy.md` (NEXT_ACTIONS priority 5 → done). The strategy doc defines: enrichment fields catalogue (§3), origin-fit dimensions (§4 — CCU + IXR named), infant/family/senior/couple suitability decomposed (§5), travel-fatigue with drivers (§6), planning-complexity with drivers (§7), medical-access confidence with pediatric subset (§8), verification/source requirements with per-field provenance (§9), three-batch manual-review discipline (§11), per-row assignment workflow E1→E2→E3 (§12), and six honest limitations that remain blocked from `planner_ready` (§14).

**Update 2026-05-18 (E1 ship)**: priority 15 (E1 script + validator + JSON catchment + enriched CSV + queues + reports) landed. Outputs: 359 enriched rows, validator clean (`enriched_structurally_valid_not_planner_ready`), three manual-review queues (O=0 ✓, S=155, M=257). Strategy doc §18 amended with calibration findings.

**Update 2026-05-18 (policy transition)**: strategy doc §19 added — no-assumption + live-data rule adopted. v1.0 enrichment retained as heuristic baseline (no rollback). P18 (calibration) **superseded**; P17 (E2 sessions) **on hold**. New P19 (source registry / free-tier ETL), P20 (v2 strategy doc), P21 (v2 enrichment service).

Next design step now: §19.6 architecture **decided 2026-05-18** — Option (b) two-tier (stable-derived layer refreshed on batch cadence + live-volatile fields fetched per Planner query, never cached). Reasoning + rate-limit math recorded in strategy doc §19.6. P20 (v2 strategy doc) is unblocked; it should be the next deliverable on a fresh branch. P19 source registry scope can be drafted alongside P20.

## Deferred Later Actions

| Action | Reason for deferral |
|---|---|
| Final PDF report | Better after master browser and enrichment strategy exist |
| Formal portfolio pack | Better after scoring module exists |
| PWA layer | Better after data model stabilises |
| Verified travel facts | Requires source verification workflow and possibly current web research |
