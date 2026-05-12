# Destination Tag Dictionary v1

This file defines controlled vocabulary for the destination database.

Use this to prevent inconsistent tags such as `beach`, `beaches`, `coastal`, `sea`, and `seaside` from fragmenting the dataset.

## Destination Types

Use lowercase snake_case.

### Cities and Towns

- `metro_city`
- `city`
- `global_city`
- `heritage_city`
- `spiritual_city`
- `temple_city`
- `pilgrim_city`
- `planned_city`
- `coastal_city`
- `hill_city`
- `mountain_city`
- `gateway_city`

### Nature and Landscapes

- `hill_station`
- `hill_town`
- `hill_region`
- `mountain_town`
- `mountain_region`
- `valley`
- `lake_city`
- `lake_region`
- `river_town`
- `desert_region`
- `forest_region`
- `rainforest_region`

### Beaches and Islands

- `beach_town`
- `beach_resort`
- `beach_region`
- `coastal_town`
- `coastal_region`
- `island_gateway`
- `island_beach`
- `island_region`
- `island_resort`

### Wildlife and Protected Areas

- `wildlife_reserve`
- `national_park`
- `tiger_reserve`
- `birding_site`
- `mangrove_wildlife_region`

### Heritage and Culture

- `heritage_site`
- `heritage_town`
- `heritage_gateway`
- `heritage_region`
- `fort_town`
- `palace_city`
- `archaeological_site`
- `cave_heritage_site`

### Religious / Pilgrimage

- `pilgrim_town`
- `pilgrim_region`
- `pilgrim_coastal_town`
- `monastery_town`
- `spiritual_retreat`

### Resort and Leisure Zones

- `resort_town`
- `backwater_region`
- `backwater_resort`
- `wellness_region`
- `wine_region`
- `tea_region`
- `coffee_region`

## Vibe Tags

Use these in `vibe_1`, `vibe_2`, `vibe_3`, and future multi-tag fields.

### Core Vibes

- `heritage`
- `culture`
- `food`
- `shopping`
- `urban`
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

### Nature Vibes

- `hills`
- `mountains`
- `valley`
- `lakes`
- `river`
- `waterfalls`
- `forest`
- `rainforest`
- `desert`
- `snow`
- `tea`
- `coffee`
- `backwaters`
- `gardens`

### Coast and Islands

- `beach`
- `coast`
- `islands`
- `marine`
- `diving`
- `water`
- `resort`

### Adventure / Activity

- `adventure`
- `trekking`
- `safari`
- `ski`
- `theme_parks`
- `music`
- `craft`
- `wine`

## Budget Bands

- `budget`
- `budget_mid`
- `mid`
- `mid_premium`
- `premium`
- `luxury`

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

- `monsoon_check`
- `heat_check`
- `winter_road_weather_check`
- `rainfall_season_check`
- `altitude_check`
- `permit_check`
- `medical_access_check`
- `safety_check`
- `route_verification_check`
- `visa_rules_check`

## Rule

When adding a new tag, first check whether an existing tag already captures the meaning. Add new tags only when needed for filtering, scoring, or decision quality.
