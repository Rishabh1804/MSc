# Lab 01 Submission — UI vs UX Browser Audit

Status: Submitted

Primary evidence file:

```text
design/foundations/topic-01-ui-vs-ux-exercise-results.md
```

Target artifact audited:

```text
docs/destination-master-browser-v1.0.html
```

## Submission summary

Lab 01 executed the Topic 1 UI vs UX exercises against the Destination Master Browser v1.

The audit found that v1 already provides a credible first QA/review surface through:

- dataset status messaging
- search
- source/region/scale/planner/verification filters
- stats
- side snapshot
- destination cards
- metadata blocks
- status pills
- semantic chips
- loading, empty, and error states

The audit also found that v1 is not yet a complete reviewer workflow. The main gaps are:

- no reset filters button
- no active-filter summary
- no sort control
- no table mode
- no full-record inspection drawer/modal
- no repeated trust warning inside deeper inspection contexts
- limited recovery guidance after empty states

## Exercise completion

| Exercise | Status | Evidence |
|---|---|---|
| Exercise A — UI inventory | Complete | UI element/task/risk table in primary evidence file |
| Exercise B — UX journey map | Complete | 7-step reviewer journey table in primary evidence file |
| Exercise C — Nielsen heuristic mini-audit | Complete | 10-heuristic audit table in primary evidence file |
| Exercise D — UX Honeycomb score | Complete | 7-facet scoring table in primary evidence file |

## Key recommendation

Destination Master Browser v1.1 should prioritise workflow completion before aesthetic expansion:

```text
browse → narrow → compare → inspect → recover → leave with correct trust level
```

## v1.1 priority actions

1. Add reset filters button.
2. Add active-filter summary chips.
3. Add sort control.
4. Add card/table view toggle.
5. Add click-to-inspect detail drawer/modal.
6. Repeat not-Planner-ready and verification status in card/table/detail contexts.
7. Add source/status legend for raw values.
8. Add collapsible advanced filters for mobile and small screens.
9. Improve empty state with reset guidance.
10. Add keyboard/focus verification before v1.1 acceptance.

## Submission conclusion

Lab 01 is complete. Topic 1 has now moved from reading-only evidence to executed coursework evidence.
