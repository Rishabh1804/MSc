# Master Browser Design Checklist

Artifact under review:

```text
docs/destination-master-browser-v1.html
```

Purpose:

Use this checklist before redesigning the destination master browser. It translates design foundations into concrete review criteria.

## 1. Artifact Purpose

The browser must support this product definition:

```text
A QA/review interface for inspecting 359 structurally valid but unverified destination master records.
```

The browser must not imply that records are source-verified or Planner-ready.

## 2. Primary User Tasks

The interface should help the user:

- understand dataset status
- search destinations
- filter by source, region, scale, verification status, and Planner status
- distinguish seed rows from normalized candidate rows
- inspect a full record when needed
- identify records that need enrichment or verification
- avoid over-trusting unverified travel data

## 3. Hierarchy Checklist

| Check | Pass criteria |
|---|---|
| Page purpose visible | Title and subtitle clearly explain what the browser is |
| Data status visible | Validation and not-Planner-ready status are near the top |
| Row count visible | Total and filtered row count are obvious |
| Primary actions visible | Search/filter controls are easy to find |
| Record hierarchy clear | Name, place, type, scale, and status are easier to scan than raw metadata |
| Warnings visible | Warnings are stronger than ordinary metadata |

## 4. Progressive Disclosure Checklist

| Check | Pass criteria |
|---|---|
| Summary first | Cards show only the fields needed for browsing |
| Detail available | Full row details can be inspected on demand |
| Complex fields hidden | Source notes, normalisation notes, and master notes are not always exposed |
| Table mode available | QA users can switch to dense table view when needed |
| No field dumping | The same page does not show every field everywhere |

## 5. Consistency Checklist

| Check | Pass criteria |
|---|---|
| Cards consistent | Every card follows the same section order |
| Chips consistent | Vibe, trip, context, and caution chips have stable styling |
| Status consistent | Verification, promotion, and Planner statuses are styled consistently |
| Filters consistent | Similar filters behave the same way |
| Labels consistent | Field labels use the same naming across card/table/drawer |

## 6. Contrast Checklist

| Check | Pass criteria |
|---|---|
| Text contrast | Body and metadata text are readable |
| Warning contrast | Not-Planner-ready warning stands out |
| Status contrast | Status chips are distinguishable from neutral tags |
| Focus contrast | Focus states are visible |
| No colour overload | Too many colours are not competing for attention |

## 7. Accessibility Checklist

| Check | Pass criteria |
|---|---|
| Touch targets | Controls are at least 44px high |
| Mobile layout | No unnecessary horizontal scrolling on mobile |
| Text labels | Status is not represented by colour alone |
| Keyboard path | Native inputs/selects/buttons remain usable |
| Responsive cards | Cards collapse cleanly on narrow screens |
| Empty/error states | Loading and error states are readable and actionable |

## 8. Proximity and Grouping Checklist

| Check | Pass criteria |
|---|---|
| Geography grouped | Country/state/district are grouped together |
| Taxonomy grouped | Type/scale/vibes/tags are grouped together |
| Workflow grouped | Verification/promotion/Planner status are grouped together |
| Lineage grouped | Source layer/source ID/source file are grouped together |
| Risk grouped | Caution tags and not-ready warnings are separate from positive tags |

## 9. Alignment and Layout Checklist

| Check | Pass criteria |
|---|---|
| Grid structure | Page uses a clear responsive grid |
| Card alignment | Cards have predictable internal alignment |
| Filter alignment | Controls align in rows/sections rather than floating randomly |
| Table alignment | Table columns are scannable and not chaotic |
| Side panel alignment | Summary panel has clear rows and labels |

## 10. Interaction Design Checklist

| Check | Pass criteria |
|---|---|
| Search immediate | Search updates results predictably |
| Filters predictable | Filters combine logically |
| Reset available | User can reset filters quickly |
| Sort available | User can sort by common fields |
| View toggle available | User can switch card/table mode |
| Inspect available | User can open full record details |
| Close available | Drawer/modal can be closed clearly |

## 11. Data Trust Checklist

| Check | Pass criteria |
|---|---|
| Not Planner-ready visible | The warning appears before records |
| Planner-ready count visible | Count shows zero unless records are actually ready |
| Source confidence visible | Source-confidence value can be inspected |
| Verification status visible | Verification status appears in card/table/detail view |
| Live-truth limitation stated | Page says travel facts are not verified |
| No unsafe claims | Interface does not claim route/visa/weather/safety accuracy |

## 12. Mobile Checklist

| Check | Pass criteria |
|---|---|
| Header not too tall | Search/filter area does not consume the full screen permanently |
| Filters collapsible | Advanced filters can collapse |
| Cards readable | Destination names and status remain visible |
| Drawer usable | Detail drawer/modal fits phone screens |
| Table fallback | Table mode has horizontal scroll or mobile-safe columns |

## 13. v1 Current Audit

Initial status based on the current functional browser:

| Area | Current status | Notes |
|---|---|---|
| Data loading | pass | CSV loads from raw GitHub URL |
| Search | pass | Basic search works |
| Filters | partial | Filters exist but are not grouped/collapsible |
| Hierarchy | partial | Page has title and warning, but cards remain generic |
| Progressive disclosure | fail | No detail drawer or table/card toggle yet |
| Consistency | partial | Cards are consistent, but status semantics can improve |
| Accessibility | partial | Controls are large, but mobile header/filter area may be heavy |
| Data trust | pass/partial | Warning exists; should be repeated in drawer/table context |
| QA efficiency | partial | Needs sort, quick chips, table mode, and inspection drawer |

## 14. Required v1.1 Changes

Minimum principle-aware upgrade:

```text
1. Add collapsible filter panel
2. Add quick-filter chips
3. Add sort control
4. Add card/table view toggle
5. Add click-to-inspect full-record drawer/modal
6. Add reset filters button
7. Improve card field grouping
8. Improve warning/status visual hierarchy
9. Improve mobile handling
10. Improve empty/error/loading states
```

## 15. Definition of Done for v1.1

Browser v1.1 is acceptable when:

- it still loads all 359 records
- search and filters still work
- user can reset filters
- user can sort results
- user can switch between card and table view
- user can inspect full row details
- the not-Planner-ready warning remains unmistakable
- mobile layout does not break basic use
- no redesign hides source/verification uncertainty

## 16. Design Decision Gate

Before implementing any change, answer:

```text
Which user task does this improve?
Which design principle supports it?
What risk does it reduce?
```

Changes that cannot answer those questions should be deferred.
