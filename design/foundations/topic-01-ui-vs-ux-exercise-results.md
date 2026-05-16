# DES-001 Topic 1 — UI vs UX Exercise Results

Status: Executed  
Lab: `courses/des-001-design-foundations/labs/lab-01-ui-vs-ux-browser-audit.md`  
Target artifact: `docs/destination-master-browser-v1.0.html`  
Supporting reading: `design/foundations/ui-vs-ux-further-reading.md`  
Checklist: `design/checklists/master-browser-design-checklist.md`

## Executive summary

The Destination Master Browser v1 already supports the core QA/review workflow at a basic level. It communicates that the dataset is structurally valid but not Planner-ready, loads the 359-row CSV, supports search and filtering, displays status counts, and renders destination cards with metadata and chips.

The main UX gap is not lack of visual polish. The main gap is review-depth and recovery. A reviewer can browse and filter records, but cannot yet reset filters quickly, sort records, switch to dense table mode, inspect a full record, or keep data-trust warnings visible inside deeper inspection contexts. Therefore v1 is a credible first QA surface but not yet a complete reviewer workflow.

---

## Exercise A — UI inventory

| UI element | UX task supported | If removed | Risk reduced |
|---|---|---|---|
| Header sticky container | Keeps title, status, and controls visible during browsing | User loses orientation while scrolling | Orientation loss during review |
| CodeMike Destination System badge | Identifies the product/system context | Page feels detached from project system | Context ambiguity |
| Structurally valid / not Planner-ready badge | Signals dataset status immediately | User may over-trust the data | False confidence in unverified records |
| Page title | Defines the artifact as the master browser | User may not know what dataset is being inspected | Purpose ambiguity |
| Subtitle | Explains 359-row reference layer and QA-only use | User may treat data as recommendation-ready | Misuse of dataset |
| Search input | Finds destination records by text | User must manually scan all records | Review slowdown |
| Source layer filter | Separates seed and normalized candidate records | User cannot isolate provenance groups | Poor traceability |
| Macro region filter | Narrows geography | User must scan broad result sets | Cognitive load |
| Scale filter | Narrows by destination scale | User cannot compare like-with-like | Weak QA segmentation |
| Planner status filter | Isolates readiness state | User cannot focus on not-ready rows | Readiness ambiguity |
| Verification filter | Isolates verification state | User cannot focus on unverified/candidate rows | Source-trust ambiguity |
| QA warning notice | States that travel facts are not live truth | User may rely on unverified visa/route/safety claims | Unsafe interpretation |
| Stats cards | Show current filtered count and status summary | User lacks system status feedback | Poor situational awareness |
| Dataset snapshot side panel | Summarises filtered rows, source split, verification and planner status | User cannot see aggregate state while browsing | Reduced QA overview |
| Top destination scales panel | Shows scale distribution | User cannot understand result mix | Weak dataset profiling |
| Source files panel | Shows seed/candidate split | Source structure is hidden | Provenance ambiguity |
| Destination cards | Present browsable record summaries | User cannot scan records | Core browser failure |
| Card ID/source layer line | Shows record identity and provenance | User cannot reference record reliably | Poor audit traceability |
| Destination name/place | Gives primary recognition target | User cannot identify destination quickly | Recognition failure |
| Planner status pill | Makes readiness visible per card | User may infer readiness incorrectly | Trust error |
| Metadata blocks | Show type, scale, region, verification, promotion, source ID | User lacks key review fields | Incomplete QA context |
| Vibe/trip/context/caution chips | Summarise categorisation and risk tags | User loses quick semantic scan | Reduced comparison speed |
| Empty state | Tells user no records match filters | User may think app broke | Recovery confusion |
| Loading state | Shows CSV is being loaded | User sees blank app during fetch | System-status ambiguity |
| Error state | Shows CSV load failure and message | User cannot diagnose failed data load | Silent failure |

### UI inventory conclusion

Most visible UI elements support real UX tasks. The weak points are missing controls rather than decorative excess: reset, sort, table mode, detail inspection, collapsible filters, and stronger repeated data-trust context.

---

## Exercise B — UX journey map

| Step | Reviewer goal | Current UI support | Friction | Required improvement |
|---|---|---|---|---|
| 1. Understand dataset status | Know whether records are safe to use | Header badge, subtitle, QA warning, stats | Trust message may disappear from focus during card review | Repeat trust status in card/table/detail contexts |
| 2. Search or filter records | Narrow the 359-row dataset | Search input and five filters | No quick filters, no collapsible filter panel, no reset button | Add reset, quick filters, collapsible advanced filters |
| 3. Compare visible records | Compare names, locations, scale, source and status | Two-column cards and metadata grid | Card view is not ideal for dense QA comparison | Add table mode and sort control |
| 4. Inspect one record deeply | Review full row fields and notes | Summary cards only | No full-record drawer/modal | Add click-to-inspect detail drawer |
| 5. Identify uncertainty or enrichment need | Find records needing verification/enrichment | Verification/planner status fields and caution chips | Source confidence and source notes are not exposed in summary | Add detail drawer with source confidence, notes, and missing fields |
| 6. Reset/change direction | Recover after filtering | Manual clearing of each input | Slow recovery and friction | Add reset filters button and active-filter summary |
| 7. Leave with correct trust level | Avoid over-trusting the master | Warning and counts | Warning is page-level, not embedded in export/detail contexts | Add persistent not-Planner-ready status in each inspection mode |

### Journey conclusion

v1 supports the beginning of the reviewer journey but does not yet complete the middle and recovery stages. The next version should prioritise inspection, reset, sorting, table comparison, and repeated trust context.

---

## Exercise C — Nielsen heuristic mini-audit

| Heuristic | Status | Evidence | Severity | Recommendation |
|---|---|---|---|---|
| Visibility of system status | Partial | Loading, error, empty, filtered count and stats exist; active filters are not summarised | Medium | Add active-filter summary and reset button |
| Match between system and real world | Partial | User-facing labels exist, but raw values like `needs_verification`, `seed_unverified`, and `normalized_candidate` remain visible | Medium | Add human-readable labels while preserving raw values in details |
| User control and freedom | Partial | Filters can be changed, but no one-click reset or undo | Medium | Add reset filters and clear individual filter chips |
| Consistency and standards | Partial | Cards and chips are consistent; status semantics can be clearer | Low/Medium | Standardise status chip language and severity styling |
| Error prevention | Partial | Strong warning exists, but trust context is not repeated in each record/detail state | High | Repeat not-Planner-ready and verification status in card/table/detail views |
| Recognition rather than recall | Partial | Summary fields are visible; raw status values require interpretation | Medium | Add tooltips/help text or status legend |
| Flexibility and efficiency | Partial | Search and filters support basic use; power-user tools missing | Medium | Add sort, table mode, quick filters, keyboard-friendly detail inspection |
| Aesthetic and minimalist design | Pass/Partial | Visual design is controlled and not overloaded; header/filter area can become heavy | Low | Collapse advanced filters on small screens |
| Help users recognise/recover from errors | Partial | CSV fetch error and empty result state exist | Low/Medium | Add actionable next steps in empty state, such as reset filters |
| Help and documentation | Partial | Subtitle and notice explain limitations | Medium | Add source/status legend and link to checklist or methodology |

### Heuristic conclusion

The highest-severity issue is not visual design. It is trust preservation across the full workflow. The browser must make it difficult to accidentally treat structurally valid records as verified travel recommendations.

---

## Exercise D — UX Honeycomb score

| Facet | Score | Reason | Improvement needed |
|---|---:|---|---|
| Useful | 4 | The browser supports QA browsing of the destination master and exposes major review fields | Add full-record inspection and table mode |
| Usable | 3 | Search/filter/card browsing works, but recovery and power-user review are incomplete | Add reset, active-filter summary, sort, detail drawer |
| Desirable | 3 | Dark dashboard style is coherent and purposeful | Improve hierarchy without adding decorative noise |
| Findable | 3 | Search and filters make records findable | Add quick filters, sort, and table mode |
| Accessible | 3 | Native inputs/selects and 44px controls help; colour is not the only status signal | Verify keyboard path, focus states, contrast, and mobile header load |
| Credible | 3 | QA warning and status fields are present | Repeat data-trust warnings in every inspection context |
| Valuable | 4 | The browser reduces raw CSV inspection effort and supports future enrichment workflow | Add action-oriented review states and enrichment flags |

Average score: 3.29 / 5

### Honeycomb conclusion

The browser is useful and valuable, but not yet strong enough in usability, findability, accessibility, and credibility to be treated as a mature QA tool. v1.1 should focus on workflow completion rather than aesthetic expansion.

---

## Improvement actions for Destination Master Browser v1.1

Priority order:

1. Add reset filters button.
2. Add active-filter summary chips.
3. Add sort control.
4. Add card/table view toggle.
5. Add click-to-inspect detail drawer/modal.
6. Repeat not-Planner-ready and verification status inside card/table/detail contexts.
7. Add source/status legend for raw values.
8. Add collapsible advanced filters for mobile and small screens.
9. Improve empty state with clear next action: reset filters.
10. Add source confidence, source notes, and full record fields to detail inspection.
11. Add keyboard/focus verification pass before final v1.1 acceptance.

---

## Checklist implications

The existing checklist already anticipates many v1.1 needs. Lab 01 confirms these additions or emphasis changes:

- Treat reset filters as a required user-control feature, not a nice-to-have.
- Treat table mode as required for dense QA comparison.
- Treat detail drawer/modal as required for full-record inspection.
- Treat repeated trust/status messaging as a data-credibility requirement.
- Add active-filter summary to visibility-of-system-status checks.
- Add human-readable status labels while preserving raw data values.
- Add keyboard/focus verification to the v1.1 acceptance process.

---

## Evidence-based recommendations

For v1.1, do not begin with cosmetic redesign. Begin with workflow completion:

```text
browse → narrow → compare → inspect → recover → leave with correct trust level
```

Every new UI element should satisfy the existing design decision gate:

```text
Which user task does this improve?
Which UI element/component/state delivers it?
Which design principle supports it?
Which data-trust or workflow risk does it reduce?
```

## Lab status

DES-001 Lab 01 is complete at the audit/evidence level. Implementation changes to the browser remain future work for Destination Master Browser v1.1.
