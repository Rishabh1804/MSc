# Destination Master Enrichment Strategy v2 — No-Assumption, Source-Backed, Live-Data

**Status:** active spec for the enrichment workstream going forward.
**Supersedes:** §§0–17 of `destination_master_enrichment_strategy.md` (v1). The v1 doc's §18 (calibration findings) and §19 (policy transition) are *preserved and binding* — §19 is the charter this document executes.
**Authored:** 2026-06-01 (CodeMike).
**Closes:** NEXT_ACTIONS priority 20.
**Blocks / sequencing:** the per-field source assignments in §7 are *candidate* until confirmed by the P19 source-coverage matrix (`datasets/reference/destination_source_coverage_matrix_v1.md`); the v2 enrichment service (P21) implements this spec. See §16.

---

## 0. Why this document exists

The v1 enrichment cycle shipped a deterministic heuristic pass (E1: 359 rows, validator-clean) and then surfaced — through its own §18 calibration findings — that workspace-judgement heuristics (regional season defaults, scale-as-medical-access proxies, stacked suitability adjustments) are not the discipline this course is for. Rishabh's directive (v1 §19): *"this is a big data + HPC course; we will be taking in live data wherever needed. No assumptions going forward. We have data for everything; we just need to store, refine, categorise, analyse — principles of big data."*

v1 §19 captured the **rule** and the **architecture decision**. This document is the **executable spec**: which source backs which field, on which refresh tier, with which derivation rule, and what happens when the source is silent.

This document does **not** re-derive the rule (v1 §19.1), the forward-only scope (v1 §19.2), the source-tier policy (v1 §19.3), the live-refresh intent (v1 §19.4), the unknown discipline (v1 §19.5), or the two-tier architecture decision (v1 §19.6). It cites them and operationalises them.

---

## 1. The governing rule (restated, not re-decided)

> **No workspace-judgement values in enrichment. Every field is either source-backed or `unknown`. When a value is needed and no source data is available for that row, the field is `unknown` and the row is flagged `manual_research_needed = true`. The downstream consumer surfaces both states honestly.** — v1 §19.1

Two corollaries this document leans on heavily:

- **C1 — No hidden judgement (v1 §19.1).** No static stereotype lookups, no scale-as-proxy formulas, no keyword-matched caution tags, no stacked-heuristic composites.
- **C2 — No-assumption ≠ no-judgement (v1 §19.9).** Choosing *which* source, *how* to combine multiple sources, and *what threshold* counts as (e.g.) "monsoon month" are still judgement calls. The rule's job is to convert **hidden** judgement (heuristics buried in code) into **visible** judgement (a cited source + a documented threshold). Every threshold in this document is written down and attributed.

---

## 2. Scope and non-goals

### In scope (v2.0)

- A two-tier source-backed enriched layer for the 359-row destination master, origins **CCU (Kolkata)** and **IXR (Ranchi)**.
- **Free-tier sources only** (v1 §19.3). The binding constraint on architecture is free-tier rate limits (v1 §19.6).
- Per-field provenance: every value carries `source_id` + `fetched_at` (or `derived_at`) + derivation reference.
- The three-state model: `known` / `unknown_pending_research` / `not_applicable`.

### Out of scope (v2.0)

- **Paid data sources.** Any field that only a paid tier can fill stays `unknown_pending_research` in v2.0; a paid upgrade is a separate `charter/BUDGET.md` proposal (v1 §19.9, TOOLING.md §Excluded).
- **Composite suitability/recommendation scores.** Moved to the scoring/derived-view layer — see §6 (this is the one substantive v2 design change vs the v1 §3 catalogue, flagged for review).
- **Multi-origin coverage beyond CCU + IXR.** Same field machinery; more origins is a v2.x catalogue extension.
- **Per-fact human verification → `planner_ready`.** Source-backed ≠ human-verified. The promotion gate (v1 §11.3, §12.4) is unchanged: no row reaches `planner_ready` without explicit sign-off.

### Asymmetric-cost framing (carried from v1 §0 / Topic 4)

Where a source is ambiguous, bias toward the **safer-for-the-traveller** reading and lower the confidence rather than guess optimistically. Under-promising a destination is recoverable; over-promising medical access or a clear road is not.

---

## 3. Relationship to v1 (preserved vs changed)

| v1 artifact | v2 disposition |
|---|---|
| `destinations_master_v2_enriched.csv` (heuristic) | **Preserved** as the heuristic baseline / diff target (v1 §19.7). Not the source of truth. |
| `destination_master_enrichment_v1.py` | **Renamed** to `destination_master_enrichment_v0_heuristic.py` when P21 lands (v1 §19.8, NEXT_ACTIONS P21). Preserved as diff baseline. |
| v1 §3 field catalogue | **Mostly carried**; composites demoted to the scoring layer (§6). Atomic fields gain source assignments (§7). |
| v1 §9 provenance model | **Extended** — per-field `source_id` + `fetched_at` added on top of the row-level `source_confidence` (§10). |
| v1 §11–§12 manual-review + promotion discipline | **Unchanged.** Source-backed rows still need sign-off to reach `planner_ready`. |
| v1 §19 policy block | **Binding charter** for this doc. |

**Diff-baseline experiment (planned, v1 §19.7):** once v2.0 produces source-backed values, compute the per-field disagreement rate between `heuristic_v1` and `source_backed_v2`. That disagreement distribution is the evidence that "no assumptions" was the right call. Logged as a future `operations/EXPERIMENTS.md` item.

---

## 4. Architecture — two-tier (finalised from v1 §19.6)

v1 §19.6 ratified **Option (b) two-tier**. This document finalises the layer boundary and names the persisted artifacts.

### 4.1 Stable-derived layer

- **Artifact:** `datasets/reference/destinations_master_v2_derived.csv` (persisted, sub-millisecond read).
- **Refresh:** batch cadence (initial target monthly; on-demand re-run when an upstream source has a known update event).
- **Contains:** fields whose real-world freshness is measured in months — route/road distance from CCU & IXR, nearest-hospital distance, altitude, baseline climatology (multi-year monthly means), heritage/classification flags, accommodation/POI density.
- **Discipline:** deterministic (§13) — same inputs + same source snapshot ⇒ byte-identical output (modulo `derived_at`).

### 4.2 Live-volatile layer

- **Artifact:** none persisted — a per-query service interface (`destination_master_enrichment_v2/live.py` in P21).
- **Refresh:** fetched per Planner query, **never cached** (v1 §19.4; the TTL-cache option (d) was rejected).
- **Contains:** fields a traveller would never want stale — current flight availability, current weather window, current permit/visa status, current park-closure / reserve-booking-window status.
- **Discipline:** every value tagged `fetched_at` + `source_id`; on rate-limit/5xx ⇒ `unknown_pending_research` + reason (never a stale fallback).

### 4.3 Join at query time (from v1 §19.6, reproduced for the implementer)

```text
Planner query (search / filter / Drawer-open / Promote-confirm)
   |
   v
Read row's stable-derived fields from destinations_master_v2_derived.csv   (sub-ms)
   |
   v
For each live-volatile field needed:
   - Hit source API / scraped endpoint                  (rate-limited)
   - success      -> populate; tag fetched_at + source_id
   - rate-limit/5xx/no-source -> unknown_pending_research + reason
   |
   v
Join stable + live -> return enriched row.
```

### 4.4 Rate-limit budget (from v1 §19.6, binding on P21)

- ~4 live calls per Planner query (one per live-volatile field).
- ~1000 free-tier calls/day ⇒ ~250 Planner queries/day before live fields start returning rate-limit `unknown_pending_research`.
- Stable-layer refresh is a separate monthly batch budget per upstream source.
- Sustainable for single-user + early Planner usage; paid upgrade is a budget question above ~200 queries/day sustained.

---

## 5. Source ladder and the pre-approved source set

The tier ladder is v1 §19.3 (Tier 1 official APIs → Tier 2 reputable open datasets → Tier 3 reputable scrapes with provenance → Tier 4 workspace synthesis of 1–3 with per-value citation; **workspace judgement rejected**).

The **pre-approved free-tier source set** is `charter/TOOLING.md` §"Free-tier source candidates" (landed PR #28). v2 may only assign fields to sources on that list. The set, with the role each plays here:

| `source_id` (proposed) | Source | Tier | Role in v2 | Layer |
|---|---|---:|---|---|
| `openflights` | OpenFlights routes/airports | 2 | CCU/IXR route existence; air-distance baseline | stable |
| `ourairports` | OurAirports metadata | 2 | nearest-airport reconciliation, IATA/ICAO, coords | stable |
| `osm_overpass` | OSM Overpass API | 2 | hospital POI distance; accommodation/POI density | stable |
| `imd_cds` | IMD Climate Data Services | 1 | baseline climatology (monthly means, seasonality) | stable |
| `ecmwf_cds` | ECMWF Copernicus CDS | 1 | climatology complement where IMD is silent | stable |
| `srtm_dem` | SRTM / free DEM (USGS / OpenTopography) | 2 | altitude at centroid | stable |
| `unesco_whl` | UNESCO World Heritage list (+ GADM / Natural Earth / World Bank) | 2–3 | heritage/classification flag; boundary support | stable |
| `gov_scrape_mea` | MEA visa/permit portal scrape | 3 | inner-line-permit / visa status | live (mostly `unknown` in v2) |
| `gov_scrape_forest` | State forest-dept / reserve portals | 3 | park-closure / booking-window | live (mostly `unknown` in v2) |
| `(paid_gap)` | current-weather + current-flight-availability APIs | — | live weather window; live seat availability | live — **free-tier gap, mostly `unknown` in v2** |

> **Source-lock gate (TOOLING.md §pre-approval).** Pre-approval is *evaluation-stage*. Each source above must pass the P19 coverage matrix (`destination_source_coverage_matrix_v1.md`) before its field assignments in §7 are **locked**. Until then, §7 is the candidate design. This is the one ordering dependency for this document (§16).

---

## 6. v2 design change — atomic facts vs composites (flagged for review)

**The change.** v1 §3 stored composite judgement bands directly in the enriched layer: `infant_suitability_score`, the four `*_suitability_band` fields, `travel_fatigue_band`, `planning_complexity_band`. v1 §19.1 explicitly bans "infant-suitability composition from stacked heuristic adjustments" and "band-bumping rules." Under the rule, those composites **cannot** be computed by stacked heuristics inside enrichment.

**The resolution.** v2 enrichment stores only **atomic, source-backed facts** (a hospital distance, an altitude, a monthly-mean temperature, a route existence). All **composite bands** (suitability, fatigue, planning-complexity) move to the **scoring / derived-view layer** — NEXT_ACTIONS P6 (destination scoring v1) — where:

- the combination rule is a single **visible, documented, version-pinned** function (not buried per-field heuristics), and
- every input it consumes is a cited source-backed atomic fact (or `unknown`, which propagates honestly into the composite).

This honours C1 (no hidden judgement in enrichment) and C2 (the composition rule is visible judgement, openly attributed) while **losing no information** — the atomic facts are richer than the bands. It is also textbook big-data discipline: *store* atomic facts; *categorise/analyse* (composition) in a separate, inspectable layer.

**Why this is flagged, not silently done.** It diverges from the v1 §3 catalogue that two reviewers graded. It hands a deliverable (the composition rule) to P6. Cipher/Aurelius/Rishabh should confirm before P21 implements §7. If rejected, the fallback is to keep composites in the enriched layer but compute each *only* from source-backed inputs with the full combination rule documented inline — strictly worse for inspectability, but available.

---

## 7. v2 field catalogue — source / tier / derivation / unknown fallback

Each row: **field** · **source(s)** · **layer** (stable-derived = S, live-volatile = L) · **derivation rule (visible judgement)** · **`unknown_pending_research` condition**. Controlled values follow v1 §3 where carried.

### 7.1 Identity and lineage (carried from v1 §3.1, unchanged)

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `destination_master_id` | master | — | copied | n/a |
| `enrichment_version` | pipeline | — | `v2.0` | n/a |
| `derived_at` / `enrichment_pass_date` | pipeline | S | run timestamp | n/a |
| `enrichment_method` | pipeline | — | `source_backed_v2` (vs legacy `heuristic_v1`) | n/a |

### 7.2 Origin fit — CCU & IXR (atomic decomposition of v1 §3.2)

Origin-fit is decomposed into source-backed atoms; the `strong/moderate/weak` band moves to the scoring layer (§6).

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `road_distance_km_ccu` / `_ixr` | `ourairports` (origin coords) + OSM routing | S | road-network route origin→destination centroid | no route solvable / missing centroid ⇒ `unknown` |
| `nearest_airport_iata` + `air_distance_km` | `ourairports` | S | nearest airport to destination centroid; great-circle distance | no airport within configured radius ⇒ `unknown` |
| `route_exists_ccu` / `_ixr` (air) | `openflights` | S | route present in OpenFlights dataset (CCU/IXR → nearest_airport) | dataset silent ⇒ `unknown` |
| `direct_flight_available_ccu` / `_ixr` | `(paid_gap)` live seat API | L | per-query availability lookup | **mostly `unknown_pending_research`** (no free-tier seat API) |

> Origin-fit **band** (`strong/moderate/weak`) is computed in the scoring layer from `road_distance_km`, `route_exists`, and (when available) `direct_flight_available`, using a documented distance/connectivity threshold table.

### 7.3 Medical access (atomic decomposition of v1 §3.6)

The v1 §8 "scale-as-proxy" derivation is **deleted** (v1 §19.1). Replaced by OSM POI distance.

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `nearest_hospital_km` | `osm_overpass` (`amenity=hospital`) | S | nearest matching POI to centroid | Overpass timeout / no POI in max radius ⇒ `unknown` |
| `nearest_tertiary_hospital_km` | `osm_overpass` (`amenity=hospital` + `emergency=yes` / bed tags) | S | nearest qualifying POI | sparse tagging ⇒ **frequently `unknown`** (honest, v1 §19.9) |
| `pediatric_facility_within_radius` | `osm_overpass` (`healthcare:speciality=paediatrics`) | S | POI presence flag | very sparse tagging ⇒ **mostly `unknown`** |
| `medical_access_basis` | pipeline | S | prose summarising the distances actually found + radius searched | states "no source" if all above unknown |

> `medical_access_confidence` band moves to scoring (§6), derived from the distances above under a documented threshold (e.g. tertiary ≤ X km ⇒ high), with `unknown` inputs forcing `unknown` output (no optimistic default).

### 7.4 Altitude (was a heuristic caution in v1 §3.7)

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `altitude_m` | `srtm_dem` | S | elevation sample at destination centroid | no DEM coverage ⇒ `unknown` |
| `altitude_caution` | `srtm_dem` (derived) | S | documented bands on `altitude_m` (e.g. `>2500m ⇒ check`, `>3500m ⇒ avoid` for infants) — threshold attributed | `unknown` if `altitude_m` unknown; `not_applicable` flag retained for sea-level rows |

### 7.5 Climatology & season (replaces v1 `SEASON_DEFAULTS_BY_REGION`, banned by v1 §19.1)

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `monthly_mean_temp_c[1..12]` | `imd_cds`, `ecmwf_cds` (complement) | S | multi-year monthly mean at centroid | no climatology coverage ⇒ `unknown` |
| `monthly_precip_mm[1..12]` | `imd_cds`, `ecmwf_cds` | S | multi-year monthly mean | no coverage ⇒ `unknown` |
| `monsoon_months` | derived from `monthly_precip_mm` | S | months where precip ≥ documented threshold (e.g. ≥ 150mm) — threshold attributed | precip unknown ⇒ `unknown` |
| `heat_months` / `cold_months` | derived from `monthly_mean_temp_c` | S | months above/below documented temp thresholds | temp unknown ⇒ `unknown` |
| `season_window` | derived | S | months with no monsoon/heat/cold flag, expressed as a range; conservative | `unknown` if climatology unknown |
| `current_weather_window_ok` | `(paid_gap)` forecast API | L | per-query forecast check | **mostly `unknown_pending_research`** (free-tier current-weather is the named gap) |

> The v1 `monsoon_caution` / `heat_caution` / `winter_road_caution` categorical cautions move to scoring, derived from the month-lists above against the traveller's queried dates.

### 7.6 Planning complexity — permits & closures (atomic decomposition of v1 §3.5)

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `permit_required` | `gov_scrape_mea` / state portal | L | scrape current permit/visa rule for the admin region | no free source / scrape fails ⇒ `unknown_pending_research` (**common in v2**) |
| `permit_basis` | `gov_scrape_mea` (derived) | L | source URL + fetch date + parse-rule ref (Tier 3 provenance discipline, TOOLING §57) | as above |
| `park_closure_status` / `reserve_booking_window` | `gov_scrape_forest` | L | scrape current closure / booking window | no free source ⇒ `unknown_pending_research` (**common**) |

> `planning_complexity_band` moves to scoring, derived from `permit_required`, `park_closure_status`, transfer legs (§7.2), and ferry/seasonal flags. `permit_or_visa_hint` is **never legal advice** (carried from v1 §3.5) — it is a `permit_basis` source pointer.

### 7.7 Heritage / classification & accommodation density (carried from v1 §3.8)

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `unesco_or_heritage` | `unesco_whl` | S | destination matched to WHL / heritage-body listing | not listed ⇒ `not_applicable` (not `unknown`) |
| `accommodation_breadth` | `osm_overpass` (`tourism=hotel/guest_house/hostel`) | S | count of stay-type tiers present in radius, banded (`narrow/moderate/broad`) — band thresholds attributed | no POIs / Overpass fail ⇒ `unknown` |
| `resort_family_density` | `osm_overpass` | S | resort-class POI count, banded | no POIs ⇒ `unknown` |

### 7.8 Provenance & state (extends v1 §3.9 + §9)

| Field | Source | Layer | Derivation | Unknown |
|---|---|---|---|---|
| `<field>_source_id` (per atomic field) | pipeline | — | the `source_id` that produced the value, or `no_source_available` | — |
| `<field>_fetched_at` / `_derived_at` | pipeline | — | timestamp of the fetch (L) or batch derivation (S) | — |
| `manual_research_needed` (row-level) | pipeline | — | `true` iff any field is `unknown_pending_research` (v1 §19.5) | — |
| `verification_status` | pipeline | — | `enriched_unverified` default (v1 §3.9 values unchanged) | — |
| `planner_use_status` | pipeline | — | `needs_verification` default; never `planner_ready` without sign-off (v1 §11.3) | — |
| `source_confidence` | pipeline | — | `official` if any Tier-1 source; `high` Tier 2; `medium` Tier 3; `none` if all unknown (v1 §9.1 ladder, source-driven not reviewer-driven in v2) | — |

---

## 8. Unknown discipline — the three-state model

Operationalises v1 §19.5. Every atomic field resolves to exactly one of:

| State | Meaning | Field shape |
|---|---|---|
| `known` | source returned a value | value + `source_id` + `fetched_at`/`derived_at` |
| `unknown_pending_research` | source checked, value absent/failed | `unknown` + `source_id = no_source_available` (or the failed source) + `basis` = what was checked, what was missing |
| `not_applicable` | field structurally irrelevant to this row | `n/a` (e.g. `altitude_caution` for a sea-level beach; `unesco_or_heritage` when not listed) |

- **`unknown` is a first-class shipped value, not a skipped row** (v1 §19.5: ship-with-flag, not skip-the-row).
- The downstream consumer (Planner UI) must render the three states distinctly — `unknown_pending_research` must never look like a confident `known` (v1 §19.5; UX honesty obligation).
- `manual_research_needed = true` whenever any field is `unknown_pending_research`. These rows are the research-priority signal (v1 §19.7) — and the v1.0 heuristic O/S/M queues remain a useful prior on *which* rows the heuristic was least sure about (NEXT_ACTIONS P17, on hold).

---

## 9. Live-refresh discipline

From v1 §19.4 ("live is live, refresh on query"):

- Live-volatile fields (§7.2 `direct_flight_available`, §7.5 `current_weather_window_ok`, §7.6 `permit_required` / `park_closure_status`) are **fetched per query, never cached**. No TTL.
- On success: value + `fetched_at` + `source_id`. On rate-limit/5xx/no-source: `unknown_pending_research` + reason. **Never** a stale or assumed fallback.
- In v2.0 most live-volatile fields will resolve to `unknown_pending_research` because their free-tier sources don't exist (current weather, current flights) or aren't APIs (permits, closures). **This is the rule working as designed** (v1 §19.9), not a defect. It also bounds the §4.4 rate-budget downward in practice (fewer successful live calls).

---

## 10. Provenance & per-field metadata schema

Extends v1 §9. v1 tracked row-level `enrichment_method` / `enrichment_version` / `source_confidence`. v2 adds **per-field** provenance:

```text
For each atomic field F:
  F                      the value, or "unknown" / "n/a"
  F_source_id            ∈ source registry ∪ {"no_source_available", "derived"}
  F_fetched_at           ISO-8601, for live-volatile fields
  F_derived_at           batch run date, for stable-derived fields
  F_basis                short prose: what source said / what was missing / which threshold applied

Row-level (v1 §9.1, retained):
  enrichment_method   = "source_backed_v2"
  enrichment_version  = "v2.0"
  source_confidence   ∈ {none, low, medium, high, official}  -- source-tier-driven (§7.8)
  manual_research_needed ∈ {true, false}
  verification_status / planner_use_status  -- v1 §3.9, defaults unchanged
```

The heavier per-row source citation file is `datasets/reference/destination_sources_v1.csv` (v1 §9.2; P19). The enriched layer references `source_id`s from it; it does not duplicate source content. The registry schema (TOOLING.md §67) is:

```text
source_id, source_url, tier, auth_method, rate_limit,
refresh_cadence, last_verified_date, free_tier_ceiling, paid_upgrade_path
```

---

## 11. Source registry linkage (P19, drafted alongside)

P20 (this doc) names the `source_id`s used in §5/§7. P19 builds `destination_sources_v1.csv` populated with one row per `source_id` above, plus the **coverage matrix** (`destination_source_coverage_matrix_v1.md`) that gates each source from *pre-approved* to *locked* by recording, per source × field: does the free tier actually return the value for our region (India, CCU/IXR catchment), at what coverage %, at what rate-limit cost. The §7 assignments are candidate until that matrix passes (§16).

---

## 12. Pipeline shape for the v2 service (P21)

Implements this spec. New package `src/codemike/data/destination_master_enrichment_v2/` (broken up; bigger than the v1 single script — NEXT_ACTIONS P21):

```text
sources/        one adapter per source_id (openflights, ourairports, osm_overpass,
                imd_cds, ecmwf_cds, srtm_dem, unesco_whl, gov_scrape_*)
                — each adapter returns (value | unknown) + source_id + timestamp + basis
derive_stable.py   batch ETL -> destinations_master_v2_derived.csv  (deterministic; §13)
live.py            per-query fetch interface for live-volatile fields (never cached; §9)
join.py            stable + live -> enriched row at query time (§4.3)
validate.py        structural + controlled-value + three-state-consistency checks
                   (extends destination_master_enrichment_validation.py)
```

The v1.0 script is renamed `destination_master_enrichment_v0_heuristic.py` and preserved as the diff baseline (v1 §19.2/§19.8). P21 is blocked on P19 + this doc.

---

## 13. Reproducibility & determinism

- **Stable layer:** deterministic (Cipher discipline, v1 §10.2). Given the same master CSV + same pinned source snapshots (dataset version / Overpass query date / climatology vintage), `derive_stable.py` produces byte-identical output modulo `derived_at`. Source snapshots are version-pinned in the registry (`last_verified_date`, dataset version) so a re-run is reproducible.
- **Live layer:** **not** deterministic by design — it reflects the world at fetch time. Reproducibility for live fields means the `fetched_at` + `source_id` + `basis` triple is recorded so any value is *auditable* even though it is not *re-derivable*. This is the honest reproducibility boundary of live data.

---

## 14. What stays blocked from `planner_ready`

Source-backed is **not** human-verified. Carried from v1 §14 / §11.3 / §12.4:

- A `source_backed_v2` row sits at `verification_status = enriched_unverified`, `planner_use_status = needs_verification` until a reviewer signs it off (v1 §12.4 E3).
- Source-backed values can be **wrong** (stale OSM tags, mis-georeferenced centroid, climatology not capturing microclimate). The promotion gate exists precisely for this.
- Live-volatile `unknown_pending_research` density means many rows will *never* be `planner_ready` for live fields under free-tier — surfaced honestly, not hidden.

---

## 15. Honest limitations (Cipher discipline)

Inherited from v1 §19.9 and made concrete for this spec:

- **Free-tier gaps are real and large.** Current weather, current flight availability, current permit rules, current park closures have **no free-tier API for India**. Those fields are `unknown_pending_research` for most rows in v2.0. Paid upgrade is a `charter/BUDGET.md` decision.
- **OSM tagging sparsity.** `nearest_tertiary_hospital_km` and `pediatric_facility_within_radius` depend on OSM tags that are sparse in rural India — expect heavy `unknown`. The value is in the *honest unknown*, not a guessed number.
- **Source-availability bias.** Major cities / UNESCO sites / large parks will have rich source data; remote destinations will be `unknown`-dense. The layer reflects this bias honestly; downstream consumers must know it exists.
- **Centroid georeferencing.** Distance/altitude/POI queries use a single destination centroid. A large or elongated destination (a valley, a coastline, a district) is poorly represented by one point. A v2.x improvement is bounding-box / multi-point sampling.
- **Threshold judgement remains (C2).** "≥150mm ⇒ monsoon month", ">2500m ⇒ altitude check", "tertiary ≤ X km ⇒ high medical access" are documented judgement calls, not facts. They are visible and attributed, but they are choices, and they should be reviewed.
- **Composition deferred (§6).** Until P6 builds the scoring layer, v2 ships atomic facts with no composite suitability/fatigue/complexity bands. Consumers expecting the v1 bands must read them from the heuristic baseline (clearly labelled `heuristic_v1`) or wait for P6.

---

## 16. Open dependencies and next steps

| Step | Status | Note |
|---|---|---|
| **P19** — source registry + coverage matrix | **next** | Must land before §7 source assignments **lock**. Builds `destination_sources_v1.csv` + `destination_source_coverage_matrix_v1.md`. Confirms free-tier India coverage per source × field. |
| §6 atomic-vs-composite decision | **needs review** | Diverges from v1 §3; hands composition to P6. Confirm with Cipher / Aurelius / Rishabh before P21. |
| **P21** — v2 enrichment service | blocked | On P19 + this doc + §6 sign-off. |
| **P6** — destination scoring v1 | unblocked-after-P21 | Owns the composite bands moved out of enrichment (§6). |
| Diff-baseline experiment | planned | `heuristic_v1` vs `source_backed_v2` per-field disagreement (v1 §19.7); future `operations/EXPERIMENTS.md` item. |

**Immediate next deliverable:** P19 (source registry + coverage matrix), because it gates the §7 source-lock. P20 (this doc) is the spec it confirms against.

---

## 17. References

- `datasets/reference/destination_master_enrichment_strategy.md` — v1; §§0–17 superseded here, §18–§19 binding charter
- `charter/TOOLING.md` §"Free-tier source candidates" — the pre-approved source set (PR #28) and registry schema
- `datasets/reference/destination_sources_v1.csv` — source registry (P19, to build)
- `datasets/reference/destination_source_coverage_matrix_v1.md` — source-lock gate (P19, to build)
- `datasets/reference/destinations_master_v2_schema.md` — master schema
- `datasets/reference/destination_database_v2_strategy.md` — layered model this executes
- `datasets/reference/destination_tag_dictionary.md` — controlled vocabulary
- `src/codemike/data/destination_master_enrichment_v1.py` — v1.0 heuristic (→ `_v0_heuristic.py` at P21); diff baseline
- `operations/NEXT_ACTIONS.md` — P19 / P20 / P21 / P6 queue
- `operations/DECISIONS.md` — §19 policy + §19.6 architecture decisions
- `design/foundations/topic-04-design-thinking.md` — asymmetric-cost framing (§2)

---

End of v2.0 spec. Next: P19 source registry + coverage matrix.
