# Destination Database v2 Strategy — Massive Planner-Ready Dataset

## Purpose

The current 134-row destination seed database is useful for prototype browsing. The next goal is to grow it into a large, structured, Planner-ready destination database covering India deeply and near-India/international options selectively.

This should be done as a database system, not as one flat list of random places.

## Target Scale

| Tier | Scope | Approximate Target |
|---|---|---:|
| Tier 1 | Major travel destinations and family-relevant destinations | 250–400 rows |
| Tier 2 | State-wise India expansion with tourist circuits | 700–1,200 rows |
| Tier 3 | Enriched Planner database with airports, routing, climate windows, tags, and verification | 1,500–3,000 rows |
| Tier 4 | Product-grade database with sources and periodic refresh | 5,000+ rows |

## Database Layers

Use multiple layers instead of one overloaded CSV.

```text
seed destinations
→ expansion backlog
→ enriched destinations
→ verified destinations
→ Planner scoring dataset
```

## Core Tables / Files

### 1. Destination Master

`datasets/reference/destinations_master_v2.csv`

One row per destination/place.

### 2. Expansion Backlog

`datasets/reference/destination_expansion_backlog_india_v1.csv`

Large candidate list to be cleaned, enriched, and promoted.

### 3. Enriched Dataset

`datasets/reference/india_region_destinations_enriched_v1.csv`

Planner-ready derived fields.

### 4. Verification Sources

`datasets/reference/destination_sources_v1.csv`

Source tracking for facts that need verification.

### 5. Tag Dictionary

`datasets/reference/destination_tag_dictionary.md`

Controlled vocabulary for vibes, destination types, travel themes, and cautions.

## Destination Record Dimensions

A strong destination record should eventually include:

### Identity

- destination ID
- canonical name
- aliases
- country
- state / union territory / province
- district / area
- macro-region
- destination scale: city / town / circuit / national park / beach / island / region / resort zone

### Travel Product Fit

- destination type
- primary vibe
- secondary vibe
- tertiary vibe
- trip style tags
- family suitability
- infant suitability
- senior suitability
- couple suitability
- solo suitability

### Access and Logistics

- nearest airport
- nearest railhead
- road transfer difficulty
- origin fit from CCU
- origin fit from IXR
- estimated routing complexity
- travel fatigue band
- planning complexity band
- permit/passport/visa hint

### Season and Risk

- best season hint
- monsoon caution
- heat caution
- winter/road caution
- altitude caution
- medical access confidence
- safety verification need

### Product/Planner Fields

- budget band
- resort/family density
- minimum recommended nights
- ideal trip duration
- shortlist priority
- planner use status
- verification status
- source confidence

## Promotion Workflow

A candidate should move through stages:

```text
candidate
→ seed_unverified
→ enriched_unverified
→ source_verified
→ planner_ready
```

## Avoided Mistakes

Do not:

- put unverified live claims into product output
- mix current visa/flight/hotel claims with stable descriptive tags
- create one giant unmaintainable CSV without source tracking
- treat all destinations equally; some are circuits, some are cities, some are regions
- hard-code Planner behaviour before the taxonomy stabilises

## Immediate Next Step

Create a large India expansion backlog grouped by state/region.

This backlog should be treated as raw candidate data. It is not yet product-ready.
