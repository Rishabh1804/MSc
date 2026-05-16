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

## 3. UI vs UX Gate

Source topic: DES-001 Topic 1 — UI vs UX.

Every UI change must be justified by the UX task it improves. Visual polish is not a sufficient reason for a component, layout, colour, animation, or interaction.

| Check | Pass criteria |
|---|---|
| UI element has UX purpose | Every new visible element maps to search, filter, sort, inspect, compare, reset, understand status, or avoid over-trust |
| Visual polish is not decorative-only | Styling improves hierarchy, readability, affordance, trust signalling, or task completion |
| UX scope is larger than screen design | The redesign considers the whole review workflow, not only cards and colours |
| Data-trust UX remains explicit | Interface changes do not imply that structurally valid records are source-verified or Planner-ready |
| Reviewer journey is measurable | The user can understand status, narrow records, inspect details, and recover from empty/error states |
| UI and UX vocabulary is separated | UI notes identify controls/components/states; UX notes identify task flow, risk, friction, and confidence |

## 4. Hierarchy Checklist

| Check | Pass criteria |
|---|---|
| Page purpose visible | Title and subtitle clearly explain what the browser is |
| Data status visible | Validation and not-Planner-ready status are near the top |
| Row count visible | Total and filtered row count are obvious |
| Primary actions visible | Search/filter controls are easy to find |
| Record hierarchy clear | Name, place, type, scale, and status are easier to scan than raw metadata |
| Warnings visible | Warnings are stronger than ordinary metadata |

## 5. Progressive Disclosure Checklist

| Check | Pass criteria |
|---|---|
| Summary first | Cards show only the fields needed for browsing |
| Detail available | Full row details can be inspected on demand |
| Complex fields hidden | Source notes, normalisation notes, and master notes are not always exposed |
| Table mode available | QA users can switch to dense table view when needed |
| No field dumping | The same page does not show every field everywhere |

## 6. Consistency Checklist

| Check | Pass criteria |
|---|---|
| Cards consistent | Every card follows the same section order |
| Chips consistent | Vibe, trip, context, and caution chips have stable styling |
| Status consistent | Verification, promotion, and Planner statuses are styled consistently |
| Filters consistent | Similar filters behave the same way |
| Labels consistent | Field labels use the same naming across card/table/drawer |

## 7. Contrast Checklist

| Check | Pass criteria |
|---|---|
| Text contrast | Body and metadata text are readable |
| Warning contrast | Not-Planner-ready warning stands out |
| Status contrast | Status chips are distinguishable from neutral tags |
| Focus contrast | Focus states are visible |
| No colour overload | Too many colours are not competing for attention |

## 8. Accessibility Checklist

| Check | Pass criteria |
|---|---|
| Touch targets | Controls are at least 44px high |
| Mobile layout | No unnecessary horizontal scrolling on mobile |
| Text labels | Status is not represented by colour alone |
| Keyboard path | Native inputs/selects/buttons remain usable |
| Responsive cards | Cards collapse cleanly on narrow screens |
| Empty/error states | Loading and error states are readable and actionable |

## 9. Proximity and Grouping Checklist

| Check | Pass criteria |
|---|---|
| Geography grouped | Country/state/district are grouped together |
| Taxonomy grouped | Type/scale/vibes/tags are grouped together |
| Workflow grouped | Verification/promotion/Planner status are grouped together |
| Lineage grouped | Source layer/source ID/source file are grouped together |
| Risk grouped | Caution tags and not-ready warnings are separate from positive tags |

## 10. Alignment and Layout Checklist

| Check | Pass criteria |
|---|---|
| Grid structure | Page uses a clear responsive grid |
| Card alignment | Cards have predictable internal alignment |
| Filter alignment | Controls align in rows/sections rather than floating randomly |
| Table alignment | Table columns are scannable and not chaotic |
| Side panel alignment | Summary panel has clear rows and labels |

## 11. Interaction Design Checklist

| Check | Pass criteria |
|---|---|
| Search immediate | Search updates results predictably |
| Filters predictable | Filters combine logically |
| Reset available | User can reset filters quickly |
| Sort available | User can sort by common fields |
| View toggle available | User can switch card/table mode |
| Inspect available | User can open full record details |
| Close available | Drawer/modal can be closed clearly |

## 12. Data Trust Checklist

| Check | Pass criteria |
|---|---|
| Not Planner-ready visible | The warning appears before records |
| Planner-ready count visible | Count shows zero unless records are actually ready |
| Source confidence visible | Source-confidence value can be inspected |
| Verification status visible | Verification status appears in card/table/detail view |
| Live-truth limitation stated | Page says travel facts are not verified |
| No unsafe claims | Interface does not claim route/visa/weather/safety accuracy |

## 13. Mobile Checklist

| Check | Pass criteria |
|---|---|
| Header not too tall | Search/filter area does not consume the full screen permanently |
| Filters collapsible | Advanced filters can collapse |
| Cards readable | Destination names and status remain visible |
| Drawer usable | Detail drawer/modal fits phone screens |
| Table fallback | Table mode has horizontal scroll or mobile-safe columns |

## 14. v1 Current Audit

Initial status based on the current functional browser:

| Area | Current status | Notes |
|---|---|---|
| Data loading | pass | CSV loads from raw GitHub URL |
| Search | pass | Basic search works |
| Filters | partial | Filters exist but are not grouped/collapsible |
| UI vs UX discipline | partial | UI controls exist, but redesign gate now requires each UI change to map to reviewer UX task and data-trust risk reduction |
| Hierarchy | partial | Page has title and warning, but cards remain generic |
| Progressive disclosure | fail | No detail drawer or table/card toggle yet |
| Consistency | partial | Cards are consistent, but status semantics can improve |
| Accessibility | partial | Controls are large, but mobile header/filter area may be heavy |
| Data trust | pass/partial | Warning exists; should be repeated in drawer/table context |
| QA efficiency | partial | Needs sort, quick chips, table mode, and inspection drawer |

## 15. Required v1.1 Changes

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
11. For each new UI element, record the UX task and data-trust risk it improves
```

## 16. Definition of Done for v1.1

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
- every new UI element has a named UX purpose

## 17. Design Decision Gate

Before implementing any change, answer:

```text
Which user task does this improve?
Which UI element/component/state delivers it?
Which design principle supports it?
Which data-trust or workflow risk does it reduce?
```

Changes that cannot answer those questions should be deferred.

## 18. Topic 2 Component Gates

Source topic: DES-001 Topic 2 — What is UI design. Added 2026-05-16 from Lab 02 (`design/foundations/ui-design-component-rules.md`).

Every component change in v1.1 must pass all six gates below.

| Gate | Pass criteria | Source |
|---|---|---|
| Container-selection gate | The new container names a reviewer task and an alternative container it beat, with reason | Topic 2 deep-reading doc §7 + §3 of rule sheet |
| State-coverage gate | All nine standard states (default / hover / focus / active / disabled / loading / empty / error / success) implemented or explicitly N/A | Material, Apple HIG, Carbon, GOV.UK |
| Affordance / signifier / feedback gate | Every interactive answers Norman's three questions; an empty signifier or feedback column is a finding | Don Norman (DOET) |
| Modality gate | A modal must be either *confirm-destructive* or *must-finish-or-cancel*; any other use is rejected | HIG + Carbon + GOV.UK consensus |
| Colour-plus-text rule | Status conveyed by colour is also conveyed by icon and text label; colour-alone fails | WCAG 1.4.1 + accessibility patterns from all four design systems |
| "When-not-to-use" clause | Every component in the system has a documented "when not to use", ideally with evidence | GOV.UK negative-space discipline |

A component that fails any gate is refused — even if it passes the §3 UI-vs-UX gate. Topic 2 gates compound on top of Topic 1 gates; they do not replace them.

## 19. Component rule sheet (canonical)

The full per-component rule sheet for v1.1 lives at:

```text
design/foundations/ui-design-component-rules.md
```

That sheet is Browser v1.1's input. Any change to the seven anti-patterns, the container-selection rules, the filter-UI rules, or the trust-signal specification must update both the rule sheet and this checklist.
