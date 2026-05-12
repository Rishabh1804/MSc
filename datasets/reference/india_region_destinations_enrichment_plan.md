# Enrichment Plan — India and Near-India Destination Database

Dataset seed: `datasets/reference/india_region_destinations_seed.csv`

## Purpose

The seed destination database is broad but intentionally shallow. This enrichment plan defines the next fields needed to make it useful for Planner-style recommendation scoring, filtering, dashboarding, and later PWA transfer.

## Current Status

- 134 destination records
- India + near-India / regionally relevant international coverage
- `verification_status = seed_unverified`
- Suitable for prototype filtering and scoring only

## QA Pass

Before enrichment, check:

- unique `destination_id`
- unique-ish destination names within country
- required fields present
- allowed category values
- macro-region coverage
- inconsistent naming
- blank values
- obvious duplicates

## Enrichment Fields v1

| Field | Type | Purpose |
|---|---|---|
| `nearest_airport_hint` | string | Human-readable airport/city access hint |
| `origin_fit_ccu` | category | Rough fit from Kolkata origin |
| `origin_fit_ixr` | category | Rough fit from Ranchi origin |
| `origin_fit_notes` | string | Short routing/access note |
| `passport_or_permit_hint` | string | Domestic / passport / permit / visa hint, not legal advice |
| `infant_suitability_score` | integer | Initial 0–100 family/infant suitability proxy |
| `travel_fatigue_band` | category | low / medium / high / very_high |
| `planning_complexity_band` | category | low / medium / high |
| `monsoon_or_weather_caution` | string | Broad caution tag |
| `medical_access_confidence` | category | low / medium / high |
| `resort_family_density` | category | low / medium / high |
| `planner_use_status` | category | seed / needs_verification / transfer_candidate / retired |

## Origin Fit Values

- `strong`
- `moderate`
- `weak`
- `unknown`

## Travel Fatigue Band Values

- `low`
- `medium`
- `high`
- `very_high`

## Planning Complexity Values

- `low`
- `medium`
- `high`

## Enrichment Rules

This first enrichment is a heuristic layer, not verified travel truth.

Rules:

- Prefer conservative estimates.
- Mark uncertain values clearly.
- Do not claim direct flights unless verified later.
- Passport/visa/permit notes are hints only.
- Do not use the enriched dataset for real travel without current verification.

## Output Target

Create:

`datasets/reference/india_region_destinations_enriched_v1.csv`

## Next Product Use

After enrichment, this database can support:

- destination shortlist generation
- family suitability filtering
- origin fit filtering
- experience tier mapping
- dashboard summaries
- Planner PWA transfer planning
