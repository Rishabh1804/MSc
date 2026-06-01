# Destination Master Enrichment Strategy v1

Status: v1 of the master enrichment strategy. Created 2026-05-18 to close NEXT_ACTIONS priority 5 (design master enrichment strategy before scoring) and to unblock the downstream scoring layer (NEXT_ACTIONS priority 6).

Owner: CodeMike (workspace) — Cipher review for architecture; Aurelius for governance entries.

Scope: this document is the **dimensions + heuristic formulas + per-row assignment workflow** specification for enriching `destinations_master_v2.csv` (359 rows) into the next layer down the pipeline. It does not commit Planner-side scoring formulas (that is NEXT_ACTIONS priority 6, a separate document downstream of this one).

---

## 0. Why this document exists

The master dataset is **structurally valid but not Planner-ready** (`master_structurally_valid_not_planner_ready`, per the validation report dated 2026-05-12). Closing the gap between *structurally valid* and *Planner-ready* requires four things:

1. A controlled set of **enrichment dimensions** — origin-fit, family/infant suitability decomposed, travel-fatigue decomposed, planning-complexity decomposed, medical-access confidence, season/weather caution — defined once and reused everywhere.
2. **Heuristic derivation formulas** that produce conservative first-pass values from the inputs that exist today, with provenance tracked per field.
3. A **per-row assignment workflow** that batches enrichment, requires sign-off at the right cadence, and protects against the asymmetric cost of a wrong "Planner-ready" promotion (Topic 4 §3 framing: a wrong promotion has much higher downstream cost than a slow promotion).
4. An honest accounting of **what enrichment cannot close** — the residual blockers that keep a row in `needs_verification` even after the full v1 enrichment pass runs.

This document specifies all four. It is opinionated where decisions need to be made and explicitly limited where uncertainty exists.

## 1. Scope and non-goals

### In scope

- The **enriched data layer** that sits between `destinations_master_v2.csv` and any Planner-side scoring or recommendation.
- **All 359 master rows** (134 seed + 225 normalised_candidate). No row is excluded a priori; rows may exit the pipeline by being marked `retired` after manual review.
- **Two origin instances** for the v1 pass: CCU (Kolkata) and IXR (Ranchi) — the two origins relevant to current Planner use. The framework is extensible to additional origins (BLR, DEL, BOM, MAA) without re-architecting; only data is added.
- **Heuristic derivation** from existing master fields plus controlled lookup tables. No live API calls in v1.
- **Manual review discipline** for the batches that the heuristic cannot decide with sufficient confidence.

### Out of scope

- Planner-side **recommendation scoring** (how the enriched fields combine into a single recommendation score for a specific trip request) — that is NEXT_ACTIONS priority 6, downstream of this document.
- **Live travel-truth verification** (route feasibility, current permits, current visa rules, current flight schedules, current safety advisories) — every enrichment field is explicitly *not* a live travel fact.
- **Source verification at the per-fact level** beyond declaring `source_confidence` for the row as a whole; the destination_sources_v1 file (per database_v2_strategy §Core Tables 4) is a separate workstream.
- **Real-time refresh** of enriched values — v1 is a one-shot enrichment pass, versioned, with a documented refresh cadence (§13) but no auto-refresh.
- **Translation / multi-language fields** — deferred to v2.x per Lab 05 F-W3C-1.

### Asymmetric cost framing (Topic 4 §3 carry-over)

The cost of marking a row `enriched_unverified` when it should have been `enriched_with_concerns` is small (a reviewer reads a wrong-but-conservative band and digs deeper). The cost of marking a row `planner_ready` when it should not be is large (a real travel decision gets made on bad data). Therefore: **every enrichment formula in §10 biases conservative**, and the workflow in §12 requires explicit sign-off before any row crosses the `planner_ready` line.

## 2. Architecture — storage shape

### Decision: separate enriched layer

`destinations_master_v2.csv` stays the **immutable structural-master reference layer**. The enriched data lives in a new sibling file:

```text
datasets/reference/destinations_master_v2_enriched.csv
```

Joins on `destination_master_id` (the stable `DST2-NNNNNN` ID from the master). One row per master row.

This matches the layered model in `datasets/reference/destination_database_v2_strategy.md` §Database Layers:

```text
seed destinations
→ expansion backlog
→ enriched destinations          ← this strategy targets this layer
→ verified destinations
→ Planner scoring dataset
```

### Rationale

- **Provenance separation**: structural facts about a destination (it is a town, in this state, with these vibes) live in master; derived/judgement facts (this destination has high travel fatigue from CCU, medium infant suitability) live in enriched. Different validation rules apply to each.
- **Roll-back safety**: a bad enrichment pass can be replaced by a previous version of the enriched file without touching the master. The asymmetric-cost framing demands this.
- **Versioning hygiene**: the enriched layer can iterate (v1 → v1.1 → v2) without bumping the master schema. Conversely, a master schema migration does not invalidate prior enrichment work, as long as the join column is stable.
- **Layered reads downstream**: the Planner-side scoring layer reads the join; the master browser (`docs/destination-master-browser.html`) continues to read master only, and a future "enriched browser" reads the join.

### What happens to the existing `family_suitability`, `access_complexity`, `best_season_hint` columns already in master?

These columns are populated for the 134 seed rows (inherited from `india_region_destinations_seed.csv` at promotion time) and blank for the 225 normalised_candidate rows. They stay in the master schema, with a frozen interpretation:

**Invariant**: master `family_suitability`, `access_complexity`, `best_season_hint` are **seed-lineage informational fields**. They are *not authoritative*. They represent the source data as it arrived at master-promotion time. Once enrichment v1 runs, the **authoritative values** live in the enriched layer:

- master `family_suitability` is superseded by enriched `family_suitability_decomposed` (a four-axis decomposition — see §5)
- master `access_complexity` is superseded by enriched `access_complexity_decomposed` and the origin-fit fields (see §4)
- master `best_season_hint` is superseded by enriched `season_window` plus weather-caution fields (see §10.6)

The master columns remain for three reasons: (a) source-lineage transparency — anyone reading the master alone can see what the seed claimed; (b) reproducibility — re-running master promotion from sources produces the same file; (c) audit — if the enriched layer is missing a value for a row, the seed-lineage value is the documented fallback (clearly marked as lineage, never as truth).

**Read order for any downstream consumer**:

```text
1. Read enriched layer's authoritative field
2. If missing, read master layer's lineage field with explicit `value_origin = "seed_lineage"` annotation
3. If both missing, treat as unknown (never default to a value)
```

This matches Cipher's "no orphan artifacts" principle — the master columns retain meaning as lineage but lose authority.

## 3. Enrichment field catalogue

The enriched layer adds the following columns. Each field carries provenance metadata in §9.

### 3.1 Identity and lineage

| Column | Type | Required | Description |
|---|---|---:|---|
| `destination_master_id` | string | yes | Join key to master; e.g. `DST2-000001` |
| `enrichment_version` | string | yes | e.g. `v1.0`, `v1.1` |
| `enrichment_pass_date` | date | yes | When this row's enrichment was last computed |
| `enrichment_method` | string | yes | `heuristic_v1` or `manual_review_v1` or `manual_review_v1.1` etc. |

### 3.2 Origin fit (per-origin)

| Column | Type | Required | Description |
|---|---|---:|---|
| `origin_fit_ccu` | category | yes | `strong` / `moderate` / `weak` / `unknown` — fit from Kolkata |
| `origin_fit_ccu_basis` | string | yes | Short prose reason (e.g. "direct flight + 4h drive") |
| `origin_fit_ccu_confidence` | category | yes | `low` / `medium` / `high` — how confident the value is |
| `origin_fit_ixr` | category | yes | `strong` / `moderate` / `weak` / `unknown` — fit from Ranchi |
| `origin_fit_ixr_basis` | string | yes | Short prose reason |
| `origin_fit_ixr_confidence` | category | yes | `low` / `medium` / `high` |

See §4 for derivation rules and controlled values.

### 3.3 Suitability decomposed

| Column | Type | Required | Description |
|---|---|---:|---|
| `infant_suitability_score` | integer | yes | 0–100; conservative-leaning composite |
| `infant_suitability_band` | category | yes | `low` / `low_medium` / `medium` / `high` |
| `family_suitability_band` | category | yes | `low` / `low_medium` / `medium` / `high` |
| `senior_suitability_band` | category | yes | `low` / `low_medium` / `medium` / `high` |
| `couple_suitability_band` | category | yes | `low` / `low_medium` / `medium` / `high` |
| `suitability_basis` | string | yes | One-sentence reason summarising the driving factors |

See §5 for decomposition and derivation rules.

### 3.4 Travel fatigue decomposed

| Column | Type | Required | Description |
|---|---|---:|---|
| `travel_fatigue_band` | category | yes | `low` / `medium` / `high` / `very_high` |
| `travel_fatigue_drivers` | string | yes | Semicolon-separated drivers (e.g. `long_road_transfer; altitude; multi_leg`) |
| `transfer_complexity_hint` | category | yes | `simple` / `multi_leg` / `complex` — used as a fatigue input |

See §6.

### 3.5 Planning complexity decomposed

| Column | Type | Required | Description |
|---|---|---:|---|
| `planning_complexity_band` | category | yes | `low` / `medium` / `high` |
| `planning_complexity_drivers` | string | yes | Semicolon-separated drivers (e.g. `permit_required; ferry_schedule; seasonal_closure`) |
| `permit_or_visa_hint` | string | no | Short hint, never legal advice (e.g. `inner_line_permit_required_for_indian_nationals`) |

See §7.

### 3.6 Medical access

| Column | Type | Required | Description |
|---|---|---:|---|
| `medical_access_confidence` | category | yes | `low` / `medium` / `high` / `unknown` |
| `medical_access_basis` | string | yes | Short prose reason (e.g. "district hospital within 15km; no tertiary care within 100km") |
| `pediatric_access_confidence` | category | no | `low` / `medium` / `high` / `unknown` — additional axis for infant/family trips |

See §8.

### 3.7 Season and weather

| Column | Type | Required | Description |
|---|---|---:|---|
| `season_window` | string | yes | e.g. `Oct-Mar`; broader than master's `best_season_hint`; conservative |
| `monsoon_caution` | category | yes | `none` / `check` / `avoid` |
| `heat_caution` | category | yes | `none` / `check` / `avoid` |
| `winter_road_caution` | category | yes | `none` / `check` / `avoid` |
| `altitude_caution` | category | yes | `none` / `check` / `avoid` |
| `weather_basis` | string | no | Short note on the dominant caution if any |

See §10.6.

### 3.8 Resort and density

| Column | Type | Required | Description |
|---|---|---:|---|
| `resort_family_density` | category | no | `low` / `medium` / `high` / `unknown` |
| `accommodation_breadth` | category | no | `narrow` / `moderate` / `broad` — how many tiers of stay exist |

### 3.9 Verification and promotion (enriched-layer view)

| Column | Type | Required | Description |
|---|---|---:|---|
| `verification_status` | category | yes | `enriched_unverified` (default after enrichment), `enriched_with_concerns`, `source_verified`, `planner_ready`, `retired` |
| `planner_use_status` | category | yes | `needs_verification` (default), `planner_candidate`, `planner_ready`, `retired` |
| `source_confidence` | category | yes | `none` / `low` / `medium` / `high` / `official` |
| `enrichment_notes` | string | no | Free-text notes; flagged concerns; references to manual-review tickets |

Default after v1 heuristic pass: `verification_status = enriched_unverified`, `planner_use_status = needs_verification`. No row crosses to `planner_ready` without manual review sign-off per §12.

## 4. Origin-fit dimensions

### 4.1 Why CCU and IXR specifically

Rishabh's two travel origins for the Planner v1 use cases are Kolkata (CCU) and Ranchi (IXR). v1 enrichment computes origin-fit for these two origins. Other origins are a data-only extension: add columns `origin_fit_<IATA>`, `origin_fit_<IATA>_basis`, `origin_fit_<IATA>_confidence`; no schema redesign.

### 4.2 Controlled values

```text
strong    — direct or one-leg access, short transfer, low fatigue from this origin
moderate  — one-leg or two-leg access; moderate transfer; some fatigue
weak      — multi-leg access OR long transfer OR significant fatigue; possible but costly
unknown   — heuristic cannot decide with sufficient confidence; manual review queued
```

### 4.3 Heuristic derivation (v1)

For each row × each origin, compute origin_fit using the following decision table. Inputs available from master: `country`, `macro_region`, `state_or_area`, `destination_scale`, `location_type`, plus the tag dictionary's static "near-CCU" / "near-IXR" lookup table (§4.4).

```text
INPUT: row r, origin o ∈ {CCU, IXR}
OUTPUT: origin_fit_<o>, basis, confidence

if r.country != "India":
    → fit = "weak" (international leg required)
    → confidence = "medium"
    → basis = "international destination from <o>"
elif r.macro_region matches the origin's "primary catchment" (see §4.4):
    → fit = "strong"
    → confidence = "high"
    → basis = "<region> is within <o> primary catchment"
elif r.macro_region matches the origin's "secondary catchment":
    → fit = "moderate"
    → confidence = "medium"
    → basis = "<region> is within <o> secondary catchment"
elif r.destination_scale ∈ {"island", "high_altitude"} OR location_type contains "high_altitude":
    → fit = "weak"
    → confidence = "medium"
    → basis = "remote/high-access destination"
else:
    → fit = "unknown"
    → confidence = "low"
    → basis = "heuristic insufficient; manual review required"
    → queue row for manual-review batch O (see §12)
```

### 4.4 Catchment tables (v1)

CCU primary catchment (strong-fit candidate macro-regions): `East India`, `North-East India`.
CCU secondary catchment (moderate-fit candidate macro-regions): `Bhutan`, `Bangladesh-adjacent`, `Sikkim`, `Andamans gateway zones`, `Eastern Himalaya`.

IXR primary catchment: `East India` (subsets reachable by overnight train / short flight), `Jharkhand`, parts of `West Bengal`, parts of `Odisha`.
IXR secondary catchment: `Bhutan`, `Sikkim-via-Bagdogra`, `Eastern Himalaya gateways`.

These tables are v1 heuristic — not verified flight/train data. They live in `datasets/reference/origin_catchment_v1.yaml` (new file in the enrichment-script PR; format TBD; YAML preferred for human-editability) and are versioned with enrichment_version.

### 4.5 Honest limitation

Origin-fit is a *static* heuristic in v1. It does not account for live flight schedules, seasonal route changes, fare elasticity, or the actual feasibility of a specific date. It is good enough for a *first-pass narrowing* in the Planner; it is not good enough to decide a trip. The `enriched_unverified` status names this honestly.

## 5. Infant / family / senior / couple suitability decomposed

### 5.1 Why decomposed

Master's `family_suitability` is a single-axis label (`low` / `medium` / `high`) that conflates four distinct questions. A destination that is "good for couples" (Pondicherry, say) can be "moderate for families" and "weak for infants". A destination that is "good for families with school-age kids" (Jaipur, say) can be "weak for infants" (heat + crowds + medical access). Collapsing these is a Topic 5 §3 Principle 5 (Iteration) failure: the data hides decisions that the Planner later has to re-derive.

v1 enrichment decomposes into four bands plus one numeric score:

```text
infant_suitability_score   ∈ 0..100   (the most cautious axis; numeric)
infant_suitability_band    ∈ {low, low_medium, medium, high}
family_suitability_band    ∈ {low, low_medium, medium, high}
senior_suitability_band    ∈ {low, low_medium, medium, high}
couple_suitability_band    ∈ {low, low_medium, medium, high}
```

Why infant gets a score and not just a band: infant suitability is the most cost-asymmetric of the four. The numeric score allows finer downstream filtering and the explicit visibility of "this destination is at 38 out of 100 — review the drivers before booking".

### 5.2 Infant suitability — derivation formula (v1)

```text
INPUT: row r
OUTPUT: infant_suitability_score (0-100), infant_suitability_band

Start at base score = 60 (neutral-conservative midpoint).

Adjustments (signed integers; saturate at [0, 100]):

  +10  if r.access_complexity == "easy"
   -5  if r.access_complexity == "moderate"
  -15  if r.access_complexity == "hard"

  +10  if r.medical_access_confidence == "high"            (note: enriched value, computed first; circular handling in §10.3)
   -5  if r.medical_access_confidence == "medium"
  -15  if r.medical_access_confidence == "low"
   -5  if r.medical_access_confidence == "unknown"

  +5   if "infant_friendly" in r.context_tags
  +5   if r.budget_band ∈ {"mid", "mid_premium", "premium", "luxury"}     (broader accommodation options)
  -10  if "altitude_check" in r.caution_tags
  -10  if "heat_check" in r.caution_tags
  -10  if "long_road_transfer_check" in r.caution_tags
  -10  if "infant_food_access_check" in r.caution_tags
   -5  if "monsoon_check" in r.caution_tags
   -5  if "crowd_check" in r.caution_tags
   -5  if "permit_check" in r.caution_tags
  -10  if r.destination_scale ∈ {"high_altitude", "park", "island"} AND no "infant_friendly" override

Floor: if any "avoid" caution applies (e.g. altitude > 3500m + medical_access_confidence == "low"), score floored at 25.

Band mapping:
  score < 30          → "low"
  30 ≤ score < 50     → "low_medium"
  50 ≤ score < 75     → "medium"
  score ≥ 75          → "high"
```

### 5.3 Family / senior / couple — derivation formulas (v1)

Each is a band, computed from a similar additive formula but with different weights:

**Family band** (school-age children assumed; infant excluded from this axis):

```text
Start band = "medium".
Bump up by one band if: access_complexity == "easy" AND "family_friendly" in context_tags AND resort_family_density ∈ {"medium","high"}.
Bump down by one band if: access_complexity == "hard" OR "permit_check" in caution_tags OR destination_scale == "high_altitude".
Floor at "low" if "altitude_check" in caution_tags AND no family_friendly override.
```

**Senior band** (mobility-sensitive assumed):

```text
Start band = "medium".
Bump up if: access_complexity == "easy" AND "senior_friendly" in context_tags AND medical_access_confidence ∈ {"medium","high"}.
Bump down if: access_complexity == "hard" OR "altitude_check" in caution_tags OR "mobility_access_check" in caution_tags.
Floor at "low" if "altitude_check" AND "mobility_access_check" both present.
```

**Couple band** (broadest tolerance; rarely "low"):

```text
Start band = "medium".
Bump up if: vibe_1 ∈ {"romantic","relaxation","wellness"} OR "couple_friendly" in context_tags OR destination_scale == "resort_zone".
Bump down if: "crowd_check" in caution_tags AND vibe_1 NOT ∈ {"festival","local_life"} (the latter is crowd-as-feature).
Floor at "low_medium" — couple-fit rarely falls below this without manual review.
```

### 5.4 Edge cases handled by manual review batch S

The heuristic queues a row for **manual review batch S (suitability)** if any of the following:

- The seed-lineage `family_suitability` value (master column) disagrees with the heuristic-computed `family_suitability_band` by **two or more bands** (e.g. seed says `high`, heuristic computes `low_medium`). Disagreement of one band is acceptable as the cost of decomposition; two-band disagreement is a signal that something is wrong.
- `infant_suitability_score` is **between 45 and 55** (the boundary between `low_medium` and `medium`); for the asymmetric-cost axis, manual review decides the boundary.
- All four bands compute to the same value (all `medium`, say) — high probability of heuristic flattening; worth a sanity check.

## 6. Travel fatigue dimensions

### 6.1 Controlled values

```text
low        — short, comfortable transfer; one leg; no special conditions
medium     — half-day transfer; two legs; manageable for most travellers
high       — full-day transfer OR two-leg with long layover OR overnight train
very_high  — multi-day OR remote AND high-altitude AND multi-leg
```

### 6.2 Drivers (one or more; semicolon-separated)

```text
long_road_transfer       — > 4h drive after last public transport
multi_leg                — 2+ flights/trains required
overnight_journey        — train or bus overnight
altitude                 — destination at altitude requiring acclimatisation
remoteness               — last leg requires permit / chartered transport
ferry_dependent          — schedule-tied; weather-cancellable
high_road_difficulty     — bad road, motion sickness risk
```

### 6.3 Heuristic derivation (v1)

```text
INPUT: row r
OUTPUT: travel_fatigue_band, travel_fatigue_drivers

drivers = []

if r.access_complexity == "hard":
    drivers += ["long_road_transfer", "high_road_difficulty"]
if "long_road_transfer_check" in r.caution_tags:
    drivers += ["long_road_transfer"]
if "altitude_check" in r.caution_tags OR r.location_type contains "high_altitude":
    drivers += ["altitude"]
if r.destination_scale == "island" OR "ferry_schedule_check" in r.caution_tags:
    drivers += ["ferry_dependent"]
if "border_area_check" in r.caution_tags OR "permit_check" in r.caution_tags:
    drivers += ["remoteness"]
if r.macro_region in long-haul-from-east-india set (§4.4) AND r.country == "India":
    drivers += ["multi_leg"]
if r.country != "India":
    drivers += ["multi_leg"]

band:
  if len(drivers) == 0 AND r.access_complexity == "easy":  → "low"
  elif len(drivers) == 1 AND r.access_complexity == "easy": → "low"  (single driver, easy primary access)
  elif len(drivers) ≤ 2 AND r.access_complexity != "hard": → "medium"
  elif len(drivers) ≥ 3 OR ("altitude" in drivers AND "remoteness" in drivers): → "very_high"
  else: → "high"
```

### 6.4 Honest limitation

Travel fatigue is highly traveller-dependent: a backpacker tolerates very_high; a family with an infant struggles at high. The band is the destination's *intrinsic* fatigue; the Planner-side scoring (out of scope here) combines this with the traveller profile.

## 7. Planning complexity dimensions

### 7.1 Controlled values

```text
low      — book and go; no permits, no scheduling, no season-criticality
medium   — needs season planning OR booking lead time OR one-permit-equivalent
high     — needs multiple permits OR seasonal-closure-awareness OR multi-leg coordination
```

### 7.2 Drivers (one or more)

```text
permit_required             — domestic ILP / restricted area
visa_required               — non-domestic
ferry_schedule              — ferry-dependent transit
seasonal_closure            — closed in monsoon / winter
booking_lead_time           — > 1 month for accommodation in season
multi_leg                   — 2+ legs requiring coordination
medical_prep                — altitude, remote, requires medical prep
weather_critical            — narrow weather window
```

### 7.3 Heuristic derivation (v1)

```text
INPUT: row r
OUTPUT: planning_complexity_band, planning_complexity_drivers, permit_or_visa_hint

drivers = []
permit_or_visa_hint = ""

if "permit_check" in r.caution_tags OR r.state_or_area in ILP_states (Arunachal, Mizoram, Nagaland, Manipur, parts of Sikkim, Lakshadweep):
    drivers += ["permit_required"]
    permit_or_visa_hint = "inner_line_permit_or_equivalent_required_check_current_rules"
if r.country != "India":
    drivers += ["visa_required"]
    permit_or_visa_hint = "international_visa_or_passport_required_check_current_rules"
if r.destination_scale == "island":
    drivers += ["ferry_schedule"]
if "snow_closure_check" in r.caution_tags OR "monsoon_check" in r.caution_tags:
    drivers += ["seasonal_closure"]
if r.destination_scale in {"park", "wildlife_reserve"}:
    drivers += ["seasonal_closure", "booking_lead_time"]
if "altitude" in travel_fatigue_drivers:
    drivers += ["medical_prep"]
if "ferry_dependent" in travel_fatigue_drivers OR "remoteness" in travel_fatigue_drivers:
    drivers += ["weather_critical"]

band:
  if len(drivers) == 0:  → "low"
  elif len(drivers) ≤ 2: → "medium"
  else: → "high"
```

`permit_or_visa_hint` is **always** annotated `…_check_current_rules` — it is never a legal claim, per database_v2_strategy "Avoided Mistakes" rule (no unverified live claims). The Planner UI must surface this caveat anywhere the hint is shown.

## 8. Medical access confidence

### 8.1 Controlled values

```text
low      — no district hospital within 50km AND no tertiary care within 200km
medium   — district hospital within 50km; tertiary within 200km
high     — tertiary care within 50km; multiple providers
unknown  — heuristic cannot decide; manual review required
```

### 8.2 Heuristic derivation (v1)

The v1 heuristic uses **destination scale + macro-region urban density** as a proxy, not actual hospital data:

```text
INPUT: row r
OUTPUT: medical_access_confidence, medical_access_basis, pediatric_access_confidence

if r.destination_scale in {"metro_city", "city"} AND r.location_type in well-served-cities-list:
    → "high"
    basis = "metro/major-city tier; tertiary care assumed available"

elif r.destination_scale in {"town", "heritage_city", "pilgrim_city"} AND r.country == "India":
    → "medium"
    basis = "town/secondary-city tier; district-level care assumed"

elif r.destination_scale in {"village", "site", "park", "high_altitude"} OR "remoteness" in fatigue_drivers:
    → "low"
    basis = "remote/small-settlement tier; medical access limited"

elif r.country != "India":
    → "unknown"
    basis = "international destination; medical access depends on country and region; manual review"
    queue for manual review batch M

else:
    → "unknown"
    basis = "heuristic insufficient"
    queue for manual review batch M

# Pediatric subset:
pediatric_access_confidence = medical_access_confidence
if "infant_food_access_check" in r.caution_tags AND medical_access_confidence ∈ {"medium","high"}:
    pediatric_access_confidence = downgrade by one band (medium → low; high → medium)
```

### 8.3 Honest limitation

This is the **weakest heuristic** in v1. It uses destination-scale as a proxy for medical access, which is a known oversimplification: a hill town near a major medical hub (e.g. Lonavala near Pune) has better medical access than its scale alone suggests; a remote site near a tertiary city is closer than its scale suggests. **Every row whose `infant_suitability_score < 50` MUST have manual medical-access review (batch M) before the score is treated as decision-grade.** The heuristic provides the first-pass band; the manual review provides the authority.

### 8.4 Circular dependency note

§5.2 uses `medical_access_confidence` as an input to `infant_suitability_score`, and §8.2 uses `pediatric_access_confidence` derived from caution tags. There is no circular computation: medical_access_confidence is computed *first* in the pipeline (§10.1), infant_suitability_score is computed *after* it.

## 9. Verification / source requirements

### 9.1 Per-field provenance tracking

Every enriched-layer row carries:

```text
enrichment_method   ∈ {"heuristic_v1", "manual_review_v1", "manual_review_v1.x", "imported_from_seed"}
enrichment_version  ∈ {"v1.0", "v1.1", "v2.0", ...}
enrichment_pass_date
source_confidence   ∈ {"none", "low", "medium", "high", "official"}
```

For v1 heuristic-pass rows: `source_confidence = "low"`. The heuristic produces structured judgement, not source-backed truth.

For manual-review-promoted rows: `source_confidence` reflects what evidence the reviewer found. Default `medium` for reviewer judgement without source citation; `high` only when at least one `reputable_travel_guide` or `government` source is cited in `enrichment_notes`; `official` only when an `official_tourism` or `unesco_or_heritage_body` source is cited.

### 9.2 Per-row source citation file

Heavier source verification (per database_v2_strategy §Core Tables 4) lives in `datasets/reference/destination_sources_v1.csv`, a separate workstream. The enriched layer references source IDs from that file via `enrichment_notes`; it does not duplicate source content.

### 9.3 What "enriched_unverified" means precisely

A row at `verification_status = enriched_unverified` has:

- gone through the v1 heuristic pass — all required enriched fields populated with derived values
- **not** had per-fact verification against external sources
- **not** received a manual reviewer's sign-off
- `source_confidence = "low"`
- `planner_use_status = "needs_verification"`

It can be used in the **master browser** (filtering, exploring, narrowing) but not in any decision that an actual traveller acts on.

## 10. Heuristic derivation — execution order and dependencies

### 10.1 Pipeline order

The enrichment script must compute fields in this order to respect dependencies:

```text
Step 1: copy identity fields from master         (destination_master_id, etc.)
Step 2: compute origin_fit_ccu / origin_fit_ixr  (§4) — depends on master only
Step 3: compute medical_access_confidence        (§8) — depends on master + fatigue (deferred to step 4)
Step 4: compute travel_fatigue_band              (§6) — depends on master + access_complexity (master) + origin_fit (step 2)
Step 5: re-compute medical_access_confidence     — now with fatigue_drivers available (cheap rerun)
Step 6: compute planning_complexity_band         (§7) — depends on travel_fatigue_band (step 4)
Step 7: compute weather / season fields          (§10.6)
Step 8: compute suitability scores & bands       (§5) — depends on medical_access_confidence (step 5), caution_tags (master)
Step 9: set verification_status, planner_use_status, source_confidence defaults
Step 10: emit manual-review queue batches O/S/M  (see §12)
```

### 10.2 Reproducibility requirement

The pipeline must be **deterministic**: given the same master CSV + same catchment YAML + same heuristic version, re-running produces a byte-identical enriched CSV (modulo `enrichment_pass_date`). This is Cipher discipline.

### 10.3 Why pediatric access is downgraded based on `infant_food_access_check`

The `infant_food_access_check` caution tag means the destination has limited infant-food availability (formula, baby food, hygienic prep). This is independent of *medical* access but correlates with *infant overall safety*; downgrading pediatric_access_confidence captures the second-order risk without conflating it with medical-care availability.

### 10.4 Why infant score saturates at [0,100] instead of having a hard cap

The base score (60) + maximum positive adjustments (+10 + 10 + 5 + 5 = +30) caps at 90, not 100. The score reaches the >75 "high" band conservatively. The 100 ceiling exists for v2 where additional positive signals (verified infant-friendly accommodation, verified pediatric facility within 5km, etc.) will be added without redesigning the band thresholds.

### 10.5 Pseudo-randomness avoidance

No formula in this strategy uses random or pseudo-random inputs. Re-runs are deterministic; differences across runs must be traceable to input changes or formula version bumps.

### 10.6 Weather / season derivation

```text
INPUT: row r
OUTPUT: season_window, monsoon_caution, heat_caution, winter_road_caution, altitude_caution

season_window:
  - Default from master.best_season_hint if non-blank
  - If blank: heuristic by macro_region:
      "South India coastal"       → "Oct-Mar"
      "North India plains"        → "Oct-Mar"
      "Western Himalaya"          → "Apr-Jun, Sep-Oct"
      "Eastern Himalaya"          → "Oct-Apr"
      "Andaman/Lakshadweep"       → "Oct-May"
      "Goa/Konkan coast"          → "Nov-Feb"
      international               → "unknown — verify per destination"
  - Append " (verify_current_year)" suffix in all cases

monsoon_caution:
  "check"  if r.macro_region in {"Goa", "Konkan", "Kerala", "North-East India", "Eastern Himalaya"}
  "avoid"  if r.destination_scale ∈ {"high_altitude"} AND r.macro_region in NE/Eastern-Himalaya
  "none"   otherwise

heat_caution:
  "check"  if r.macro_region in {"North India plains", "Rajasthan", "South India inland"}
  "avoid"  if r.destination_scale == "desert_region"
  "none"   otherwise

winter_road_caution:
  "check"  if "snow_closure_check" in r.caution_tags
  "avoid"  if r.destination_scale == "high_altitude" AND macro_region in Western-Himalaya
  "none"   otherwise

altitude_caution:
  "check"  if "altitude_check" in r.caution_tags
  "avoid"  if r.location_type contains "high_altitude" AND no override
  "none"   otherwise
```

## 11. Manual-review rules

### 11.1 Three batches

The heuristic pass emits three manual-review queues. Each batch is reviewed by one person (Rishabh, in v1) in a single session per batch, with cap on session length to keep judgement quality high.

| Batch | Source | Cap per session | What gets reviewed |
|---|---|---:|---|
| **O** (origin) | §4.3 "unknown" branch | 30 rows | origin_fit_ccu and/or origin_fit_ixr where heuristic could not decide |
| **S** (suitability) | §5.4 edge cases | 25 rows | Rows where heuristic disagrees with seed-lineage ≥ 2 bands, OR infant score in [45,55], OR all four bands identical |
| **M** (medical) | §8.2 + §8.3 floor rule | 20 rows | Rows with medical_access_confidence = "unknown" OR infant_suitability_score < 50 |

Caps are conservative; review fatigue degrades judgement quality (Topic 5 §3 Principle 4: assessment by users + iteration). A second pass at a later session covers overflow.

### 11.2 Sign-off cadence

For each batch, the reviewer:

1. Reads the row's master fields + heuristic-computed enrichment fields
2. Reviews the basis prose
3. Either accepts (enrichment_method stays `heuristic_v1`, verification_status remains `enriched_unverified`) or overrides (enrichment_method becomes `manual_review_v1`, the overridden field is updated, an `enrichment_notes` entry records the override reason and any cited sources)
4. The row's `source_confidence` is bumped to `medium` on accept; the reviewer's identifier and date are recorded

### 11.3 No row to `planner_ready` without explicit promotion

A row only reaches `planner_use_status = "planner_ready"` via a **separate promotion step** (not part of v1 enrichment). The promotion step requires:

- All §10.1 pipeline steps complete
- Manual review for all three batches if the row qualified for any batch
- At least one external source cited for any field that is decision-critical (medical access, permit requirements)
- An explicit reviewer sign-off recorded in `enrichment_notes`

v1 enrichment does **not** promote any row to `planner_ready`. The destination of v1 is `enriched_unverified` (heuristic-default) or `enriched_with_concerns` (heuristic flagged a concern the reviewer chose not to override). Promotion to `planner_ready` is downstream of this strategy.

### 11.4 Anchor pattern for reviewer notes

Borrowed from Lyra's grade-only-with-anchor pattern (PRs #20–#24). Reviewer notes per overridden field follow:

```text
WAS: <heuristic value> (computed via <rule citation>)
NOW: <manual value>
REASON: <one-sentence why>
SOURCE: <source ID from destination_sources_v1.csv, OR "reviewer judgement, no source"; never blank>
```

The "never blank" rule prevents lazy overrides. Reviewer judgement is acceptable; *invisible* reviewer judgement is not.

## 12. Per-row assignment workflow

### 12.1 Phases

```text
E1 — Heuristic pass (script):    359 rows enriched in one batch; ~minutes wall-clock
E2 — Manual review batches O+S+M: ~3 sessions × ~25 rows = ~75 rows reviewed
E3 — Source-verified promotion:  per-row; only for rows that need to be Planner-ready;
                                  rate-limited (~5-10 rows / session); explicitly out of v1 scope
```

### 12.2 E1 — Heuristic pass

```text
Script: src/codemike/data/destination_master_enrichment_v1.py     (to be built; not part of this strategy doc PR)

Inputs:
  - datasets/reference/destinations_master_v2.csv
  - datasets/reference/origin_catchment_v1.yaml      (to be built alongside the script)
  - datasets/reference/destination_tag_dictionary.md (existing; controlled vocabulary)

Outputs:
  - datasets/reference/destinations_master_v2_enriched.csv
  - reports/evidence/destination-master-v2-enrichment-report.md     (counts, distributions, manual-review queue sizes)
  - reports/evidence/destination-master-v2-enrichment-manual-review-queues/O.csv (or similar)
  - reports/evidence/destination-master-v2-enrichment-manual-review-queues/S.csv
  - reports/evidence/destination-master-v2-enrichment-manual-review-queues/M.csv

Validation: a sibling validator (destination_master_enrichment_validation.py)
checks controlled values, required columns, score bounds, derived-field consistency,
band-vs-score mapping, and produces an enrichment-validation report parallel to the
existing master-validation report.
```

### 12.3 E2 — Manual review

Three sessions, one per batch, scheduled in week-long cadence (review fatigue mitigation):

- **Session O** (origin): ~30 rows × ~2 minutes each = ~60 minutes
- **Session S** (suitability): ~25 rows × ~3 minutes each = ~75 minutes
- **Session M** (medical): ~20 rows × ~4 minutes each = ~80 minutes (highest-stake; longest per-row)

Each session produces:

- An updated `destinations_master_v2_enriched.csv` (rows in the batch have overridden values + `enrichment_method = manual_review_v1` + reviewer notes)
- A short session log in `reports/evidence/destination-master-v2-enrichment-manual-review-session-N.md` (per-row decisions; aggregate observations; any patterns spotted)

### 12.4 E3 — Source-verified promotion (deferred)

Out of scope for v1 enrichment. Triggered per-row, on-demand, when a specific destination needs to be promoted to `planner_ready` for actual use. Each promotion requires the source-verification workstream (database_v2_strategy §Core Tables 4) to exist and to have entries for that row.

### 12.5 Cadence and refresh

- E1 re-runs on every master schema change OR every heuristic-formula version bump. Cost: minutes.
- E2 sessions re-run on every E1 re-run that changes the batch contents. Cost: hours per cycle; not free.
- E3 is per-row, on-demand. Cost: hours per row depending on source complexity.

Auto-refresh of live facts (visa, weather, schedules) is **out of scope**. All season/permit fields carry `_check_current_year` or `_check_current_rules` annotation; the Planner UI surfaces this caveat.

## 13. Three-phase rollout

| Phase | Deliverables | Status |
|---|---|---|
| **E1** | Enrichment script + enriched CSV + report + manual-review queues + validator | NEXT_ACTIONS new priority after this strategy ships |
| **E2** | Three manual-review sessions + session logs | After E1 |
| **E3** | Per-row source-verified promotion (a small number of rows; demand-driven) | After E2; demand-driven |

This strategy document is the **specification** that E1, E2, and E3 implement. No rows are enriched, reviewed, or promoted as part of *this* PR. The deliverable is the spec.

## 14. What remains blocked from Planner-ready status

Even after the full v1 enrichment pass + manual review for all three batches, the following remain blocked and must not be claimed by the workspace:

1. **Live travel facts** — flight schedules, current visa rules, current permit rules, current safety advisories, current weather, current pricing. None of these are in scope; all carry `_check_current_year` / `_check_current_rules` annotations.
2. **Per-fact source verification** — beyond the row-level `source_confidence`, claim-by-claim source citation is the destination_sources_v1 workstream, not the enrichment workstream.
3. **Real-user evaluation of enrichment quality** — Lab 05 F-PRIN-1 (Principle 2: Users involved throughout) applies here too. Whether the heuristic produces values that real planners trust is something the Sponsor Reviewer cycle (NEXT_ACTIONS priority 9) should test with at least one reviewer running a Planner-shaped task against the enriched data.
4. **Multi-origin coverage** — only CCU and IXR are computed in v1. BLR / DEL / BOM / MAA are data-only extensions but not in v1 scope.
5. **Accessibility-specific enrichment** — wheelchair access, signed information availability, sensory-environment notes — these are Lab 05 F-W3C-1 (Inclusion lens Fail) territory and are v2.x scope.
6. **Translation / multi-language enrichment** — v2.x.

Honesty discipline: any consumer of the enriched layer (UI surface, Planner-side scoring, dashboard) **must surface** that the data is `enriched_unverified` and not live travel truth. This is the equivalent of the master browser's trust banner, carried down the pipeline.

## 15. Audit-shape rules carried forward

The 2026-05-18 v1.2.1 / v1.2.2 cycles extended the audit-shape rule for visual-treatment PRs (mobile-viewport screenshot + contrast verdict). The equivalent rule for **data-layer PRs** is:

1. Every enrichment-version bump emits a **distribution-diff report**: per-field, how many rows changed value, how many crossed band boundaries, how many manual-review-queue assignments changed.
2. Every formula change records a **before/after distribution comparison** in the same PR — the formula doc + the distribution check ship together.
3. **No silent overrides**: a manual reviewer cannot change a value without §11.4 anchor-pattern notes recorded.
4. **Heuristic vs lineage disagreement is a signal, not a problem**: when heuristic disagrees with seed lineage by 1 band, that's noise; by 2+ bands, it's a batch-S queue item; never silently override the heuristic with lineage or vice versa.

## 16. Next files / next steps

This strategy doc is the spec. The following files implement it, in order:

```text
Next, in a follow-up PR:
  src/codemike/data/destination_master_enrichment_v1.py         (E1 script)
  src/codemike/data/destination_master_enrichment_validation.py (E1 validator)
  datasets/reference/origin_catchment_v1.yaml                   (lookup table)
  datasets/reference/destinations_master_v2_enriched.csv        (E1 output)
  reports/evidence/destination-master-v2-enrichment-report.md
  reports/evidence/destination-master-v2-enrichment-validation-report.md
  reports/evidence/destination-master-v2-enrichment-manual-review-queues/
```

After E1 ships, NEXT_ACTIONS gets new priorities for E2 sessions O / S / M; after E2 ships, NEXT_ACTIONS priority 6 (scoring v1) can begin against a stable enriched layer.

## 18. v1 implementation amendments (added after E1 first-pass run)

Added 2026-05-18 alongside the E1 enrichment script PR. These are findings from actually running the spec against the 359-row master, captured here so future readers of this strategy see the spec **and** the reality of the data it operates on.

### 18.1 Data-inspection findings before script could run

The master dataset has three field populations that the strategy doc above (§4–§10) reads as inputs but which are sparsely populated in practice:

| Field | Strategy doc role | Master reality |
|---|---|---|
| `caution_tags` | Major input to fatigue (§6.3), planning (§7.3), medical (§8), suitability (§5.2) | **3 tags total across 359 rows** (2 `border_area_check`, 1 `route_verification_check`) |
| `context_tags` | Used for `infant_friendly`, `family_friendly`, `senior_friendly`, `couple_friendly` band bumps (§5) | **17 tags total across 359 rows** (14 `gateway_context`, 2 `border_context`, 1 `remote_context`) — none of the suitability-relevant tags |
| `access_complexity` | Major input to fatigue (§6), suitability (§5), medical (§8) | Populated only for 134 seed rows; **blank for all 225 normalised_candidate rows** |

This is consistent with the master schema (`destinations_master_v2_schema.md` §8): caution_tags are explicitly "generated from heuristics later", not inherited.

**Amendment to §10.1 pipeline order**: insert **Step 1a** (derive `access_complexity` from `destination_scale` / `location_type` / `state_or_area` when blank) and **Step 1b** (derive caution tags from populated fields) before Step 2. The script implements both; output column `derived_caution_tags` is written alongside the spec fields so downstream consumers can audit what cautions the pipeline inferred.

### 18.2 Catchment tuning after first run

The first run of E1 produced **Queue O = 95 rows** because the original `origin_catchment_v1.json` placed only `East India` + `North East India` in CCU primary and only `Central India` + a handful of secondaries — so very-reachable regions like `North India` (97 rows in master) fell through to `unknown`.

**Calibration**: aligned the catchment JSON with the existing seed-only `destination_enrichment.py` precedent — North India and Central India sit in CCU secondary catchment; West India / South India / Island India sit in CCU weak (domestic-far). Same shape for IXR with the eastward bias. After this tuning: **Queue O = 0** (all rows now classify cleanly to strong / moderate / weak from both origins). No spec change; just the lookup table.

### 18.3 Queue S sizing (155 rows; 6× the 25/session cap)

Trigger composition (per the E1 first run):

| Reason | Rows |
|---|---:|
| All four suitability bands identical | 99 |
| Infant score at the 45 boundary | 54 |
| Infant score at the 50 boundary | 29 |
| Infant score at the 55 boundary | 25 |

The "all four bands identical" trigger is dominant. **Calibration finding**: because the suitability-context-tags (`family_friendly`, `senior_friendly`, `couple_friendly`, `infant_friendly`) are nearly empty in master, the band-bumping rules in §5.3 rarely fire, so the four bands collapse to `medium` for most rows — exactly the flattening signal §5.4 is designed to catch.

**Recommended v1.1 spec change** (not applied in this PR): keep the seed-vs-heuristic-disagreement trigger (the strongest signal); keep the boundary-score trigger (asymmetric-cost-relevant); **drop the "all four bands identical" trigger** because it fires on data noise rather than judgement noise. Future band-bumping should also derive friendliness signals from populated fields (e.g., `family_friendly` inferred from `family_suitability >= medium` in seed-lineage; `couple_friendly` inferred from `vibe ∈ {romantic, relaxation, wellness}`).

For v1.0 the spec stands as written; the calibration finding is captured here and the queue ships at 155.

### 18.4 Queue M sizing (257 rows; 13× the 20/session cap)

Trigger composition (per the E1 first run):

| Reason | Rows |
|---|---:|
| Infant score < 50 (with known medical access) | 145 |
| Medical access = unknown (international) | 45 |
| Medical access = unknown (domestic — heuristic insufficient) | 67 |

The 67 domestic-unknown rows are mostly `scale=region` / `scale=resort_zone` / `scale=island_region` — destinations the §8.2 decision table doesn't have an explicit branch for (it covers `metro_city` / `city` / `town` / `village` / `site` / `park` / `high_altitude` but not multi-place `region`-scale entities).

**Two calibration findings**:

(a) **Spec gap in §8.2**: add a `region` / `resort_zone` branch that returns `medium` (district-level care assumed within the broader area) instead of `unknown`. This would reduce the domestic-unknown bucket from 67 → ~10–15 (genuinely-remote `region` rows would still fall through). **Not applied in this PR** — recorded here so v1.1 of the script can address it.

(b) **§11.1 M-cap is too small for the score-<-50 spec in §8.3**. With 145 rows hitting that threshold from the heuristic, the M batch cannot complete in one session at the 20-row cap. **Recommended v1.1 spec change**: split M into:

- **M-critical** — rows where `medical = unknown` OR (`medical = low` AND `infant_score < 35`). Smaller; high-stakes; deserves the slow 20-row cap.
- **M-standard** — rows where `medical ∈ {medium, high}` AND `35 ≤ infant_score < 50`. Larger; bulk review; 40–50 rows per session at a faster pace.

The asymmetric-cost framing (§0, §12) still applies — M-critical is the cost-asymmetric batch that needs the slow cap; M-standard is the volume work that needs throughput. For v1.0 the spec stands; the calibration finding is captured here.

### 18.5 Travel-fatigue band distribution skew

Observed E1 distribution: `low: 89`, `medium: 233`, `high: 3`, `very_high: 34`. The `high` band almost never fires because the §6.3 formula treats 3+ drivers as `very_high` and 0–2 drivers as `medium`-or-`low`. There is essentially no path to `high` except a narrow "high road difficulty without altitude/remoteness" case.

**Recommended v1.1 spec change**: re-balance §6.3 band thresholds so `high` is reachable. One option: 0 drivers + easy access → `low`; 1 driver → `medium`; 2 drivers → `high`; 3+ drivers OR altitude+remoteness → `very_high`. Calibration only; not applied in v1.0.

### 18.6 What stayed the same as the spec

- All controlled values (§3 catalogue).
- Conservative-bias direction (every heuristic still biases towards "needs review" rather than "decision-grade").
- Default after pass: `enriched_unverified` / `needs_verification` / `source_confidence = low` for every row.
- Manual-review batches O / S / M existence and per-row anchor-pattern notes requirement.
- Three-phase rollout shape (E1 → E2 → E3).
- Six honest limitations from §14.
- §15 audit-shape rules for data-layer PRs (distribution-diff on every formula bump).

### 18.7 Reproducibility

The script (`src/codemike/data/destination_master_enrichment_v1.py`) and the catchment JSON (`datasets/reference/origin_catchment_v1.json`) together produce a byte-identical enriched CSV across runs, modulo the `enrichment_pass_date` column which moves with calendar date. This satisfies the strategy doc §10.2 reproducibility requirement.

### 18.8 Supersession notice (added 2026-05-18 alongside §19)

All v1.1 recommendations enumerated in §§18.3 / 18.4 / 18.5 (drop "all four bands identical" S trigger; add region/resort_zone medical branch; split M into critical/standard; rebalance fatigue thresholds) are **superseded** by the §19 policy change. They were valid calibration moves under the heuristic regime; under no-assumption + live-data they are moot. §18 is preserved unedited as the historical record of the heuristic cycle — it is not the path forward.

---

## 19. Policy transition — no-assumption + live-data rule

Added 2026-05-18, after the E1 v1.0 first-run review surfaced the §18 calibration findings. Rishabh's directive in response (paraphrased): *"this is a big data + HPC course; we will be taking in live data wherever needed. No assumptions going forward. We have data for everything; we just need to store, refine, categorise, analyse — principles of big data."*

This section captures the rule, its scope, what it means for the enrichment workstream, and the queue restructure that follows.

### 19.1 The rule

> **No workspace-judgement values in enrichment. Every field is either source-backed or `unknown`. When a value is needed and no source data is available for that row, the field is `unknown` and the row is flagged `manual_research_needed = true`. The Planner UI / downstream consumer surfaces both states honestly.**

Operationally, this means:

- **No** static lookup tables encoding regional stereotypes (e.g., the `SEASON_DEFAULTS_BY_REGION` map in the v1.0 script).
- **No** "destination-scale as proxy for medical access" formulas.
- **No** catchment tables built from workspace judgement.
- **No** caution-tag derivation from location_type keyword matching.
- **No** infant-suitability composition from stacked heuristic adjustments.
- **No** band-bumping rules gated on near-empty `context_tags`.

Every enriched value must be derived from external source data with provenance recorded — or it is `unknown`.

### 19.2 Scope — forward-only

**Retroactive scope rejected; forward-only scope adopted.**

- v1.0 enrichment artifacts (`destinations_master_v2_enriched.csv`, the three manual-review queues, the report, the validation report) are **retained as the heuristic baseline**. They are not deleted, not rolled back, not relabelled inside the file (the `enrichment_method = heuristic_v1` column already names them honestly).
- The v1.0 script (`src/codemike/data/destination_master_enrichment_v1.py`) is **preserved unchanged** in the codebase. It is **not the source of truth** going forward.
- The strategy doc §§0–17 are preserved as written. §18 is preserved as the calibration findings of the v1.0 cycle. §19 (this section) supersedes §§0–17 as the active spec going forward, and the v2 enrichment strategy is a separate document — **landed 2026-06-01 at `destination_master_enrichment_strategy_v2.md`** (NEXT_ACTIONS P20). This §19 block remains the binding charter that the v2 doc executes.
- v1.0 stays useful as a **diff baseline**: when v2 ships, "what does workspace-judgement get wrong vs source-backed data?" is an experiment evidence item — exactly the kind of *Improve* loop output CodeMike's operating loop is built to produce.

### 19.3 Source tier policy (v1, free-tier-only)

For v1 of the no-assumption enrichment (referred to elsewhere in this doc as v2 of the *enrichment*, but v1 of the *no-assumption-discipline*), the source ladder is:

| Tier | Source class | v1 acceptability |
|---|---|---:|
| Tier 1 | Government / official / authoritative APIs (MoHFW, IMD, MEA, Indian Railways, state tourism portals, UNESCO, RBI) | preferred |
| Tier 2 | Reputable open datasets (OpenFlights, OpenStreetMap, OurAirports, World Bank, GADM, Natural Earth) | accepted |
| Tier 3 | Reputable scraped sources with provenance (UNESCO World Heritage list, IUCN, tourism boards) | accepted |
| Tier 4 | Workspace-curated synthesis of Tier 1–3 sources | accepted, with source citations per derived value |
| (rejected) | Workspace judgement, opinionated heuristics, regional stereotypes, generated-tag lookup tables | **rejected** |

**Paid sources are out of scope for v1.** Aviation APIs (Aviationstack, FlightAware, OAG, Skyscanner), paid climate APIs, paid permit data — all out. Free-tier rate-limits of the chosen sources become the binding constraint on system architecture (see §19.6 open question).

### 19.4 Live-data refresh discipline

Rishabh's directive: *"Live is live, refresh on query."*

The intent is no stale data: values used in a Planner decision should reflect what the source said now, not what it said last week. Operationally this has architectural consequences (§19.6) but the policy intent is unambiguous: **enriched values are not a static CSV that ages**.

### 19.5 Unknown discipline

When source data is unavailable for a specific row × field combination, the rule is **ship-with-unknown-flag, not skip-the-row**:

```text
field_value = "unknown"
field_source = "no_source_available"
field_manual_research_needed = true
field_basis = "<short prose explaining what source was checked and what was missing>"
```

The Planner UI / downstream consumer must distinguish:

- `known` (value present + source cited)
- `unknown_pending_research` (no source; flagged for human follow-up)
- not-applicable (field is structurally not relevant to this row, e.g., altitude_caution for a sea-level destination)

Every enriched-layer row carries a row-level `manual_research_needed` boolean equal to "any field is unknown_pending_research".

### 19.6 Architecture decision — refresh granularity (resolved 2026-05-18)

"Live, refresh on query" is implemented as **Option (b) — two-tier**, decided by Rishabh on 2026-05-18 after the trade-off analysis below.

**Two layers**:

1. **Stable-derived layer** (`destinations_master_v2_derived.csv` — name placeholder; the v2 strategy doc finalises): route distance from each named origin, nearest hospital distance, baseline climatology (multi-year monthly means), altitude profile, OSM POI density. Refreshed on a **batch cadence** (initial target: monthly; on-demand re-runs supported when an upstream source has a known update event). Persisted; readable in sub-millisecond.
2. **Live-volatile layer** — fetched per Planner query, never cached: current flight availability, current weather window, current permit/visa status, current park closure / wildlife-reserve booking-window status. Each fetch carries a `fetched_at` timestamp and a `source_id` citation.

**Planner query flow**:

```text
Planner query (search / filter / Drawer-open / Promote-confirm)
   |
   v
Read row's stable-derived fields from cached layer    (sub-ms)
   |
   v
For each live-volatile field needed:
   - Hit the source API / scraped endpoint            (rate-limited)
   - On success: populate; tag with fetched_at + source_id
   - On rate-limit / 5xx: unknown_pending_research + reason
   |
   v
Join stable + live; return enriched row.
```

**Rate-limit math (free-tier, decided thresholds)**:

- Each Planner query consumes ~4 live API calls (one per live-volatile field).
- 1000 calls/day free-tier ceiling ≈ 250 Planner queries/day before any field starts returning rate-limit-induced `unknown_pending_research`.
- Stable layer refresh is a separate batch budget (one run / month per upstream source).
- This is sustainable for a single-user workspace + early Planner usage. Paid-tier upgrade becomes a budget question once Planner crosses ~200 queries/day sustained.

**Why this honours "live is live, refresh on query"**:

- Live-volatile fields — the fields a real traveller would never want stale (flight availability, current weather, current permit rules) — are fetched per query, never cached.
- Stable-derived fields — fields where "freshness" is measured in months not minutes (route distance from CCU to a destination doesn't change daily; hospital locations don't move daily) — are refreshed on a cadence that matches their actual refresh-rate-in-the-world.
- Caching only happens for fields where caching aligns with the underlying truth. There is **no** TTL-cache on live-volatile fields. The (d) cached-with-TTL option was rejected.

**Rejected alternatives** (preserved for audit):

- **(c) All-live** — every query re-fetches every field. Rejected: ~8 calls × ~25 rows × ~5 queries/day = 1000+ calls per moderate session, blowing free-tier ceilings within the first day of any real usage. Most fields would return `unknown_pending_research` from rate-limit kick-in by mid-day. Operationally unusable.
- **(d) Cached-with-short-TTL** — every field cached for 15–60 min. Rejected: violates the rule's letter ("refresh on query" → no TTL on the live fields).

This decision **unblocks P20** (v2 no-assumption strategy doc). P20 opens with this resolved.

### 19.7 What v1.0 stays useful for

- **Heuristic baseline / diff target** — when v2 ships, we can compute per-field disagreement rates between heuristic and source-backed values. That disagreement distribution is the evidence that "no assumptions" was the right call.
- **Manual-research priority queue** — the v1.0 queues (O / S / M) are still meaningful as *which rows the heuristic was least confident about*; those rows are likely candidates for manual research where source data is sparse.
- **Postgraduate evidence** — the v1.0 cycle (spec → ship → calibration findings → policy revision) is itself a Research Methods / Big Data Analytics worked example. Captured.

### 19.8 Queue restructure

| Previous priority | New status | Replacement |
|---|---|---|
| P15 (E1 v1.0 script) | stays **done** | retained as heuristic baseline; no rollback |
| P18 (E1 v1.1 calibration spec changes) | **superseded** | replaced by no-assumption v2 workstream |
| P17 (E2 manual-review sessions) | **on hold** | re-evaluated after v2 lands; the manual-review batches may still be valid as research-priority queues |
| (new) P19 | source registry | build `datasets/reference/destination_sources_v1.csv` + ETL layer for free-tier sources |
| (new) P20 | v2 no-assumption strategy doc | new document at `datasets/reference/destination_master_enrichment_strategy_v2.md` — supersedes §§0–17 of this doc |
| (new) P21 | v2 enrichment service | source-backed pipeline implementing v2 strategy; rename of the v1.0 script preserved as `destination_master_enrichment_v0_heuristic.py` |

### 19.9 Honest limitations of the policy itself

Surfaced for the audit-trail (Cipher discipline):

- **Free-tier coverage gaps**: some dimensions (live visa rules, current park closures, current permit availability) genuinely don't have free-tier sources for India. Under the rule those fields will be `unknown_pending_research` for most rows in v2 — that's the rule working as designed, not a failure.
- **Rate-limit ceiling**: free-tier APIs cap throughput. If Planner gains real usage, paid-tier upgrade becomes a budget question (per `charter/BUDGET.md`).
- **Source-availability bias**: well-studied destinations (major cities, UNESCO sites, large parks) will have rich source data; remote / niche destinations will have heavy `unknown` density. The enriched layer will reflect that bias honestly — but the bias is real, and downstream consumers should know.
- **No-assumption is not the same as no-judgement**: choosing *which* sources to trust, *how* to combine them (e.g., monthly-mean temperature vs daily-extreme), and *what threshold* counts as "medical access" are still judgement calls. The rule reduces hidden judgement (heuristics) to visible judgement (source-tier picks + threshold definitions). Judgement-free enrichment is impossible; well-cited judgement is the goal.

---

## 20. References

- `datasets/reference/destinations_master_v2_schema.md` — master schema; storage-shape decision in §2 above carries it forward
- `datasets/reference/destination_database_v2_strategy.md` — layered model that this strategy executes
- `datasets/reference/destination_tag_dictionary.md` — controlled vocabulary used throughout §§4–10
- `datasets/reference/india_region_destinations_enrichment_plan.md` — seed-only predecessor; superseded by this strategy for v2 master scope (kept as historical reference)
- `reports/evidence/destination-master-v2-validation-report.md` — readiness baseline this strategy starts from
- `reports/evidence/destination-master-v2-promotion-report.md` — promotion lineage this strategy extends
- `operations/NEXT_ACTIONS.md` — queue this strategy closes (priority 5) and extends (E1/E2/E3 follow-ups)
- `operations/FAILURE_LOG.md` — audit-shape rules referenced in §15
- `design/foundations/topic-04-design-thinking.md` — asymmetric-cost framing applied in §0 and §12
- `design/foundations/topic-05-hcd.md` — HCD discipline applied in §11 (manual review = users involved throughout)

---

End of v1.
