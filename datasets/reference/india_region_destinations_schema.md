# Schema — India and Near-India Destination Reference Database

Dataset: `datasets/reference/india_region_destinations_seed.csv`

## Purpose

This dataset provides a broad destination reference database for Planner-style recommendation, clustering, filtering, dashboarding, and later transfer into a PWA or travel decision engine.

The first version is a seed database. It is useful for prototyping and scoring logic, but time-sensitive fields must be verified before real planning use.

## Columns

| Column | Type | Meaning |
|---|---|---|
| `destination_id` | string | Stable unique ID for the destination row |
| `name` | string | Destination/location name |
| `country` | string | Country name |
| `macro_region` | string | Broad region bucket such as North India, Southeast Asia, Indian Ocean, Near India |
| `state_or_area` | string | Indian state/UT or international area/country grouping |
| `location_type` | string | Destination type such as hill_station, metro_city, beach_resort, wildlife_reserve |
| `vibe_1` | string | Primary vibe tag |
| `vibe_2` | string | Secondary vibe tag |
| `vibe_3` | string | Tertiary vibe tag |
| `budget_band` | string | Indicative relative budget band |
| `family_suitability` | string | Initial qualitative family suitability estimate |
| `access_complexity` | string | Initial travel/access complexity estimate |
| `best_season_hint` | string | Broad season hint; not a live weather guarantee |
| `verification_status` | string | Data verification status |

## Budget Band Values

- `budget`
- `budget_mid`
- `mid`
- `mid_premium`
- `premium`

## Family Suitability Values

- `low`
- `low_medium`
- `medium`
- `high`

## Access Complexity Values

- `easy`
- `moderate`
- `hard`

## Verification Status Values

- `seed_unverified`
- `source_verified`
- `product_ready`
- `retired`

## Important Limitations

This seed database does not verify:

- current visa rules
- flight availability
- live safety conditions
- hotel prices
- weather forecasts
- road closures
- permits
- medical suitability
- infant-specific travel constraints

For real trip planning, these must be checked separately using current sources.

## Next Expansion Fields

Future versions may add:

- nearest airport
- approximate flight time from CCU / IXR
- visa category
- passport/permit notes
- infant travel difficulty score
- monsoon risk
- heat risk
- medical access confidence
- resort density
- direct flight availability flag
- sample stay duration
- latitude/longitude
- source URLs
