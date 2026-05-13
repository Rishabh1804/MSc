# Destination Tag Dictionary v2

This file defines controlled vocabulary for the destination database.

Use this to prevent inconsistent tags such as `beach`, `beaches`, `coastal`, `sea`, and `seaside` from fragmenting the dataset.

## Principles

- Use lowercase snake_case.
- Prefer stable descriptive tags over time-sensitive claims.
- Do not add a new tag if an existing tag captures the same meaning.
- Separate destination type, vibe, traveller fit, risk, logistics, and verification fields.
- Keep live claims such as visa, weather, safety, flight, and pricing outside unverified tags.

## Destination Scale

Use this to clarify whether a row is a single place, city, circuit, region, or product zone.

| Tag | Meaning |
|---|---|
| `city` | Single city |
| `town` | Smaller urban/tourism town |
| `village` | Village or small settlement |
| `district` | District-level travel area |
| `region` | Broad multi-place area |
| `circuit` | Multi-stop linked itinerary zone |
| `site` | Single attraction or heritage/nature site |
| `park` | Protected park/reserve |
| `island` | Island destination |
| `resort_zone` | Resort-heavy zone rather than one town |
| `route` | Route-based travel experience |

## Destination Types

### Cities and Towns

- `metro_city`
- `city`
- `global_city`
- `capital_city`
- `heritage_city`
- `culture_city`
- `culture_town`
- `spiritual_city`
- `temple_city`
- `pilgrim_city`
- `planned_city`
- `coastal_city`
- `beach_city`
- `hill_city`
- `hill_heritage_city`
- `mountain_city`
- `mountain_capital`
- `lake_mountain_city`
- `gateway_city`
- `city_gateway`
- `northern_city`
- `business_city`
- `education_city`
- `food_city`
- `craft_city`
- `heritage_capital`

### Nature and Landscapes

- `hill_station`
- `lake_hill_station`
- `hill_town`
- `culture_hill_town`
- `hill_region`
- `mountain_town`
- `mountain_region`
- `mountain_resort`
- `mountain_valley`
- `high_altitude`
- `valley`
- `lake_city`
- `lake_region`
- `river_town`
- `river_region`
- `waterfall_site`
- `canyon_region`
- `desert_region`
- `forest_region`
- `rainforest_region`
- `meadow_region`
- `plateau_region`
- `tea_region`
- `coffee_region`
- `spice_region`

### Beaches and Islands

- `beach_town`
- `beach_resort`
- `beach_region`
- `beach_state`
- `coastal_town`
- `coastal_region`
- `coastal_capital`
- `desert_beach_emirate`
- `island_gateway`
- `island_beach`
- `island_region`
- `island_resort`
- `island_resort_district`
- `island_heritage_city`
- `local_island`
- `river_island`
- `marine_region`

### Wildlife and Protected Areas

- `wildlife_reserve`
- `wildlife_region`
- `national_park`
- `tiger_reserve`
- `birding_site`
- `mangrove_wildlife_region`
- `forest_reserve`
- `biosphere_reserve`
- `wetland_site`

### Heritage and Culture

- `heritage_site`
- `heritage_town`
- `heritage_city`
- `heritage_gateway`
- `heritage_region`
- `fort_town`
- `fort_site`
- `palace_city`
- `palace_site`
- `archaeological_site`
- `cave_heritage_site`
- `rock_carving_site`
- `craft_village`
- `museum_district`
- `old_quarter`

### Religious / Pilgrimage

- `pilgrim_town`
- `pilgrim_region`
- `pilgrim_coastal_town`
- `monastery_town`
- `monastery_region`
- `spiritual_retreat`
- `buddhist_site`
- `jain_site`
- `sikh_pilgrimage_site`
- `char_dham_site`
- `temple_cluster`

### Resort and Leisure Zones

- `resort_town`
- `resort_region`
- `backwater_region`
- `backwater_resort`
- `wellness_region`
- `wine_region`
- `tea_resort_region`
- `coffee_resort_region`
- `theme_park_zone`
- `shopping_district`

## Vibe Tags

Use these in `vibe_1`, `vibe_2`, `vibe_3`, and future multi-tag fields.

### Core Vibes

- `heritage`
- `culture`
- `food`
- `shopping`
- `urban`
- `city`
- `architecture`
- `history`
- `spiritual`
- `pilgrimage`
- `slow_travel`
- `family`
- `luxury`
- `budget`
- `wellness`
- `romantic`
- `relaxation`
- `nightlife`
- `business`
- `education`
- `art`
- `craft`
- `music`
- `festival`
- `photography`
- `viewpoint`
- `local_life`
- `museums`
- `stopover`

### Nature Vibes

- `hills`
- `mountains`
- `valley`
- `lakes`
- `river`
- `waterfalls`
- `forest`
- `rainforest`
- `rain`
- `monsoon`
- `desert`
- `snow`
- `tea`
- `coffee`
- `spice`
- `backwaters`
- `gardens`
- `meadows`
- `caves`
- `limestone`
- `mangrove`
- `wetland`
- `birding`
- `flowers`
- `landscape`
- `sunrise`
- `sunset`

### Coast and Islands

- `beach`
- `coast`
- `islands`
- `marine`
- `diving`
- `snorkelling`
- `water`
- `resort`
- `villa`
- `lagoon`
- `coral`
- `cruise`
- `houseboat`

### Adventure / Activity

- `adventure`
- `trekking`
- `safari`
- `ski`
- `rafting`
- `paragliding`
- `camping`
- `road_trip`
- `cycling`
- `boating`
- `theme_parks`
- `water_sports`
- `desert_safari`

### Special Interest

- `buddhist`
- `jain`
- `sikh`
- `monastery`
- `temples`
- `forts`
- `palace`
- `caves`
- `rock_carving`
- `wine`
- `textiles`
- `handicrafts`
- `wildlife`
- `tiger`
- `rhino`
- `elephant`
- `marine_life`
- `colonial`
- `french_quarter`
- `silk_route`

## Seed Compatibility Vocabulary

These values are accepted because they exist in the original seed dataset. They are structurally valid for master ingestion, but should be reviewed during future enrichment and normalisation.

### Seed-Compatible Location Types

- `beach_city`
- `culture_hill_town`
- `desert_beach_emirate`
- `heritage_capital`
- `hill_heritage_city`
- `island_heritage_city`
- `island_resort_district`
- `lake_mountain_city`
- `mountain_capital`
- `mountain_valley`
- `northern_city`
- `wildlife_region`

### Seed-Compatible Vibe Tags

- `city`
- `limestone`
- `monsoon`
- `museums`
- `relaxation`
- `stopover`
- `villa`

## Traveller Fit Tags

These should be used for future multi-value traveller-fit fields.

- `infant_friendly`
- `toddler_friendly`
- `child_friendly`
- `senior_friendly`
- `couple_friendly`
- `family_friendly`
- `solo_friendly`
- `group_friendly`
- `workation_friendly`
- `luxury_friendly`
- `budget_friendly`
- `mobility_sensitive`
- `medical_sensitive`
- `crowd_sensitive`
- `heat_sensitive`
- `altitude_sensitive`

## Trip Style Tags

- `weekend_getaway`
- `long_weekend`
- `short_break`
- `slow_trip`
- `luxury_escape`
- `budget_escape`
- `family_vacation`
- `pilgrimage_trip`
- `wildlife_trip`
- `heritage_circuit`
- `beach_holiday`
- `hill_retreat`
- `food_trip`
- `shopping_trip`
- `wellness_retreat`
- `adventure_trip`
- `road_trip`
- `honeymoon_style`
- `offbeat_trip`
- `monsoon_trip`
- `winter_trip`
- `summer_escape`

## Budget Bands

| Tag | Meaning |
|---|---|
| `budget` | Lower-cost destination or stay patterns available |
| `budget_mid` | Budget to mid-range options common |
| `mid` | Broad mid-range destination |
| `mid_premium` | Mid-range possible but quality options trend premium |
| `premium` | Premium-heavy destination |
| `luxury` | Luxury-led destination; budget options limited or lower fit |

## Suitability Values

- `low`
- `low_medium`
- `medium`
- `high`

## Access Complexity Values

- `easy`
- `moderate`
- `hard`

## Travel Fatigue Values

- `low`
- `medium`
- `high`
- `very_high`

## Planning Complexity Values

- `low`
- `medium`
- `high`

## Origin Fit Values

- `strong`
- `moderate`
- `weak`
- `unknown`

## Medical Access Confidence Values

- `low`
- `medium`
- `high`
- `unknown`

## Resort / Family Density Values

- `low`
- `medium`
- `high`
- `unknown`

## Verification Status Values

- `candidate`
- `seed_unverified`
- `enriched_unverified`
- `source_verified`
- `planner_ready`
- `retired`

## Planner Use Status Values

- `candidate`
- `needs_verification`
- `transfer_candidate`
- `planner_ready`
- `retired`

## Caution Tags

### Weather / Climate

- `monsoon_check`
- `heat_check`
- `winter_road_weather_check`
- `rainfall_season_check`
- `cyclone_check`
- `flooding_check`
- `fog_delay_check`
- `humidity_check`
- `snow_closure_check`

### Terrain / Health

- `altitude_check`
- `motion_sickness_check`
- `long_road_transfer_check`
- `medical_access_check`
- `mobility_access_check`
- `infant_food_access_check`
- `elderly_travel_check`

### Rules / Logistics

- `permit_check`
- `passport_check`
- `visa_rules_check`
- `local_transport_check`
- `route_verification_check`
- `flight_schedule_check`
- `ferry_schedule_check`
- `seasonal_closure_check`
- `crowd_check`
- `festival_crowd_check`
- `safety_check`
- `border_area_check`

## Source Confidence Values

- `none`
- `low`
- `medium`
- `high`
- `official`

## Source Type Tags

- `official_tourism`
- `government`
- `airport_official`
- `railway_official`
- `park_official`
- `unesco_or_heritage_body`
- `reputable_travel_guide`
- `hotel_platform`
- `map_source`
- `weather_source`
- `news_source`
- `manual_curated`

## Promotion Status

Use this for workflow movement from backlog to product-ready use.

| Status | Meaning |
|---|---|
| `candidate` | Raw candidate only |
| `qa_pending` | Added but not checked |
| `dedupe_pending` | Needs duplicate/circuit check |
| `enrichment_pending` | Needs enriched fields |
| `source_pending` | Needs source verification |
| `review_ready` | Ready for human review |
| `planner_candidate` | Can be tested in Planner scoring |
| `planner_ready` | Accepted for Planner use |
| `retired` | Removed from active use |

## Synonym / Normalisation Rules

| Incoming word | Preferred tag |
|---|---|
| `beaches` | `beach` |
| `seaside` | `coast` |
| `coastal` | `coast` |
| `mountain` | `mountains` |
| `hill` | `hills` |
| `historical` | `history` |
| `historic` | `history` |
| `religious` | `spiritual` |
| `temple` | `temples` |
| `luxurious` | `luxury` |
| `premium` | `luxury` when used as vibe; keep `premium` for budget band |
| `wild animals` | `wildlife` |
| `jungle` | `forest` |
| `falls` | `waterfalls` |
| `lake` | `lakes` |
| `riverside` | `river` |
| `handloom` | `textiles` |
| `crafts` | `handicrafts` |

## Scoring Relevance

These fields are especially important for recommendation scoring:

- `family_suitability`
- `infant_suitability_score`
- `access_complexity`
- `travel_fatigue_band`
- `planning_complexity_band`
- `origin_fit_ccu`
- `origin_fit_ixr`
- `medical_access_confidence`
- `budget_band`
- `resort_family_density`
- `verification_status`
- `planner_use_status`
- caution tags

## Rule

When adding a new tag, first check whether an existing tag already captures the meaning. Add new tags only when needed for filtering, scoring, QA, source verification, or Planner decision quality.
