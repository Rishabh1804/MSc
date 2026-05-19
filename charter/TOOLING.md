# TOOLING.md — CodeMike Tooling Register

This file tracks tools CodeMike uses, evaluates, proposes, approves, or retires.

## Tooling Principle

A paid tool is justified only when it improves learning, evidence, reproducibility, transfer, or project capability more than the free/default option.

## Rules

- CodeMike may recommend tools.
- CodeMike must not purchase, subscribe, upload private data, or connect paid services without explicit approval.
- Prefer open-source and free-tier options first.
- Avoid overlapping subscriptions unless there is a clear capability reason.
- Every paid tool should produce an artifact, capability, benchmark, or transfer.

## Tool Evaluation Criteria

A tool is worth considering if it improves at least one of:

- learning speed
- experiment quality
- reproducibility
- project transfer
- benchmarking
- deployment
- research quality
- documentation quality
- collaboration or review quality

## Tool Register

| Tool | Purpose | Cost | Status | Decision |
|---|---|---:|---|---|
| GitHub | Repository hosting and version control | Existing | active | Use |
| ChatGPT | AI-assisted planning, drafting, review, and implementation | Existing | active | Use |

## Free-tier source candidates — pre-approved for P19 / P20 / P21 (added 2026-05-18 per §19.3 + §19.6)

Pre-approved free-tier sources for the destination-enrichment v2 workstream. Approval is *evaluation-stage* — each source must pass the source coverage matrix (`datasets/reference/destination_source_coverage_matrix_v1.md`, P19 deliverable) before entering the v2 strategy doc. No subscription / no API-key tier crossed; if a candidate is later found to gate a needed field behind a paid tier, the upgrade is a separate `charter/BUDGET.md` proposal.

Tier classification per strategy doc §19.3:

- **Tier 1** — government / official / authoritative APIs (preferred)
- **Tier 2** — reputable open datasets (accepted)
- **Tier 3** — reputable scraped sources with provenance (accepted; provenance + scrape-date mandatory)
- **Tier 4** — workspace-curated synthesis of Tier 1–3 with citations per derived value (accepted)
- *Rejected* — workspace judgement, opinionated heuristics, regional stereotypes (the v1.0 enrichment shape)

| Source | Tier | Purpose | Cost | Auth | Rate limit | Status | Decision |
|---|---|---|---:|---|---|---|---|
| OpenFlights (`openflights.org/data.html`) | 2 | Airport + route reference; CCU / IXR catchment derivation; route-distance baseline (stable-derived layer) | Free (dataset download) | None | n/a (static dataset; refresh on dataset version bump) | pre-approved | Evaluate as stable-derived input |
| OurAirports (`ourairports.com/data/`) | 2 | Airport metadata complement to OpenFlights; runway + IATA/ICAO reconciliation | Free (CSV download) | None | n/a | pre-approved | Evaluate as stable-derived input |
| OpenStreetMap Overpass API (`overpass-api.de`) | 2 | Hospital POI distances (medical-access field); altitude / DEM-adjacent queries (stable-derived layer) | Free | None | Public instance: fair-use; recommend self-hosted Overpass or batch via Geofabrik extracts if request volume grows | pre-approved | Evaluate as stable-derived input; respect public-instance fair-use |
| IMD CDS (India Meteorological Department — Climate Data Services, `cdsp.imdpune.gov.in`) | 1 | Baseline climatology (decadal averages, seasonality bands) — stable-derived layer | Free | Account registration (free-tier) | per-account; check current policy | pre-approved | Evaluate as Tier 1 climatology input |
| ECMWF Copernicus / reanalysis free-tier (`cds.climate.copernicus.eu`) | 1 | Complementary baseline climatology + reanalysis for fields IMD doesn't cover | Free (Copernicus free-tier) | CDS API key (free) | per-account quotas | pre-approved | Evaluate as Tier 1 climatology complement |
| Government-portal scrape — MoHFW / MEA / state tourism / Indian Railways / RBI (per §19.3 Tier 1 list) | 3 | Live + stable fields where no API exists: visa rules (MEA), permit data (state tourism), medical access (MoHFW), monetary policy / forex disclosures (RBI) | Free | None for public pages | Site-by-site; throttle politely; honour `robots.txt` | pre-approved (with provenance discipline) | Each scraped value carries source URL + fetch date + parse rule reference; Tier 3 acceptance is conditional on provenance attached at the record level |
| UNESCO + GADM + Natural Earth + World Bank open datasets | 2 | Boundary / classification / index supports; UNESCO listing for tier-1 destination flagging | Free | None | n/a (static datasets) | pre-approved | Evaluate as boundary / classification inputs |
| SRTM / free DEM tiles (NASA SRTM via USGS / OpenTopography free-tier) | 2 | Altitude profile (stable-derived layer per §19.6) | Free | None / OpenTopography free-tier registration | per-account | pre-approved | Evaluate as altitude input |

**Out of scope for v1 (named for the audit trail — not approved):**

- Aviation APIs (Aviationstack, FlightAware, OAG) — current flight availability is the canonical live-volatile dimension but the paid APIs gate that data; deferred to a paid-tier budget proposal when Planner usage warrants
- Paid climate APIs (OpenWeather paid tiers beyond free, AccuWeather) — same reason; free tiers (CDS / IMD) cover stable-derived climatology, current weather is the live-volatile gap that may need a paid upgrade
- Paid permit / visa data services — no free authoritative substitute for live visa-rule changes; MEA scrape covers static rules; live changes ship as `unknown_pending_research` until a paid-tier upgrade is authorised

**Per-source documentation requirement:** when each source enters production (P19), the source registry (`datasets/reference/destination_sources_v1.csv`) records: source_id, source_url, tier, auth_method, rate_limit, refresh_cadence, last_verified_date, free_tier_ceiling, paid_upgrade_path. This pre-approval entry exists so the workstream is not blocked on budget discussions for free-tier evaluation; production use is gated by the coverage-matrix pass.

## Proposed Tool Template

```md
## Tool: <name>

Status: proposed / approved / active / retired
Cost:
Billing type:
Purpose:
Capability improved:
Project supported:
Free alternative considered:
Expected use:
Expected artifact:
Review date:
Decision:
```
