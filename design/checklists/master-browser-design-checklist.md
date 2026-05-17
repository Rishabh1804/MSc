# Master Browser Design Checklist

Artifact under review:

```text
docs/destination-master-browser-v1.0.html
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

## 20. Topic 3 UX gates

Source topic: DES-001 Topic 3 — UX design. Added 2026-05-16 from Lab 03 (`design/foundations/ux-acceptance-criteria.md`).

Every v1.1 implementation decision must pass all four gates. They are the journey-level companion to §18's component gates; both apply.

| Gate | Pass criteria | Source |
|---|---|---|
| Criterion-presence gate | Every new component or backlog item references at least one UX acceptance criterion from `ux-acceptance-criteria.md` § 2 | Topic 3 deep-reading doc §8 + §10.2 |
| Behaviour-testability gate | Every criterion is testable by two evaluators reaching the same pass/fail verdict; the gate-test for each is documented in `ux-acceptance-criteria.md` §5 | Topic 3 deep-reading doc §1 + §8 |
| Need-vs-request audit | Every feature produces a user need in GOV.UK form (`As a [user], I need [outcome], so that [goal]`) with **no UI mechanism named**. Requests and solution-shapes are rewritten before being added to the backlog. | GOV.UK Service Manual — *Learning about users* |
| Journey-completeness gate | Every reviewer-journey step has at least one acceptance criterion; empty / loading / error are first-class journey states, not edge cases | Topic 3 deep-reading doc §7 + §11 anti-pattern 1 |

A v1.1 PR that fails any of these gates does not merge. The gates compound on top of §3 (UI-vs-UX gate) and §18 (Topic 2 component gates) — they do not replace them.

## 21. Topic 3 UX anti-patterns

Four UX anti-patterns specific to data-review tools. Every v1.1 implementation decision must refuse all four.

1. **Designing the happy path only.** Data-review tools spend most reviewer-time in non-happy paths (empty, conflict, missing-field, blocked). Empty / loading / error are first-class. (Sources: Norman gulfs; Lab 02 finding F3.)
2. **Confusing user request with user need.** A request names a mechanism; a need names an outcome. Designing for a request locks the design unnecessarily. (Source: GOV.UK Service Manual.)
3. **Skipping evaluation.** The 13-gate test plan in `ux-acceptance-criteria.md` §5 is the *minimum* evaluation gate; user testing with real reviewers is the next step. A v1.1 PR that does not test against the criteria is not v1.1-ready. (Sources: NN/g + Norman.)
4. **Ignoring the trust check at depth.** Trust state must survive every journey step. A design that drops the trust signal in inspection, after filtering, or in an empty state is a journey UX failure. (Sources: Topic 1 framing; Topic 2 §6.2 four-depth spec.)

## 22. UX acceptance-criteria sheet (canonical)

The full UX acceptance-criteria sheet for v1.1 lives at:

```text
design/foundations/ux-acceptance-criteria.md
```

That sheet is Browser v1.1's UX gate. Together with `design/foundations/ui-design-component-rules.md` (the component gate), it forms the complete v1.1 specification. Any change to the 14 criteria, the 13 gate-tests, or the four anti-patterns must update both the sheet and this checklist.

## 23. Topic 4 design-thinking-loop gates

Source topic: DES-001 Topic 4 — Design thinking. Added 2026-05-17 from Lab 04 (`design/foundations/topic-04-design-thinking-loop.md`).

Every v1.2+ backlog item must pass all four gates. They are the process-level companion to §3 (Topic 1 UI-vs-UX gate), §18 (Topic 2 component gates), and §20 (Topic 3 UX gates).

| Gate | Pass criteria | Source |
|---|---|---|
| Problem-framing gate | Every backlog item is annotated either *well-framed* (skip Topic 4; write Topic 3 criterion directly) or *not well-framed* (run a Topic 4 loop first). The three well-framed conditions are: user-need statement writable without speculation; "what would tested success look like" answerable; criterion measurable. | Topic 4 deep-reading doc §9 (decision tree) |
| Ideate-count gate | Every loop that reaches Prototype has documented ≥ 3 meaningfully different candidates at the Ideate → Prototype boundary. "Meaningfully different" means not three variants of the same approach. | Topic 4 deep-reading doc §11 anti-pattern 1 + Lab 04 §Step 4 |
| Sourced-triage gate | Every triage table cites *sourced evidence* in the desirability / feasibility / viability cells, not opinion. A cell saying "users will love it" without an Empathize source is a finding. | Brown's three-constraint frame + NN/g evidence-per-stage rule |
| Falsification-criteria gate | Every Test specification names explicit falsification criteria — concrete observations that would change the design's verdict. A Test without falsification criteria is a rubber-stamp. | Topic 4 deep-reading doc §11 anti-pattern 4 + Lab 04 §Step 7 |

A loop that fails any gate is incomplete; the gate's stage must be re-run before the loop closes. These gates compound on top of §3 / §18 / §20 — they do not replace them.

## 24. Topic 4 design-thinking anti-patterns

Five anti-patterns specific to design thinking, with attention to the single-person-workspace case. Every loop must refuse all five.

1. **Skipping Ideate** — committing to the first plausible solution. The most common practical failure. Discipline: always generate ≥ 3 meaningfully different candidates.
2. **Single-pass design thinking** — doing one loop and shipping. The full benefit compounds across loops; one loop is design thinking only by accident.
3. **Empathy-by-introspection** — single-person workspaces are prone to "I am the user" using self as data. Mitigation: three-persona synthesis in writing (first-time / power / accessibility-need).
4. **Workshop theatre** — producing no per-stage evidence. NN/g evidence-per-stage rule is the corrective.
5. **Triage by taste** — picking the chosen candidate without sourced desirability / feasibility / viability assessment. Brown three-constraint frame is the corrective.

Each is sourced from Topic 4 deep-reading doc §11 (which cites ≥ 1 of the four required Topic 4 sources per anti-pattern).

## 25. Design-thinking loop output (canonical example)

The canonical worked example of a loop output lives at:

```text
design/foundations/topic-04-design-thinking-loop.md
```

Loop 1 (batch-promote-confirm modal) is the workspace's first run of the discipline. Future loops follow the same eight-step shape (Pick → Empathize → Define → Ideate → Triage → Prototype → Test-spec → Decision) and produce the same handoff format to Topic 3 criteria + Topic 2 components. Lab 04's submission (`submissions/lab-04-design-thinking-loop-results.md`) is the formal lab evidence for Loop 1.

## 26. Topic 5 HCD gates

Source topic: DES-001 Topic 5 — Human-centred design. Added 2026-05-17 from Lab 05 (`design/foundations/topic-05-hcd-audit.md`).

Every v1.2+ backlog item must pass all four gates. They are the lifecycle-level companion to §3 (Topic 1 UI-vs-UX), §18 (Topic 2 components), §20 (Topic 3 UX), §23 (Topic 4 design-thinking).

| Gate | Pass criteria | Source |
|---|---|---|
| HCD self-audit gate (four cells) | Every backlog item names (a) context of use, (b) user requirement, (c) design solution shape, (d) evaluation that would confirm it works. Any empty cell = return to the missing activity. | Topic 5 deep-reading doc §10 + Lab 05 §Step 7 |
| Per-PR activity gate | Every PR that changes the browser names which ISO activity its work serves, and which activity it leaves under-served. | ISO 9241-210 + Lab 05 §Step 7 |
| W3C triad lens gate | Every v1.2 feature is evaluated against all three lenses (usability / accessibility / inclusion); the worst-served lens is named. | W3C Accessibility, Usability, and Inclusion + Lab 05 §Step 6 |
| Sponsor-Reviewer presence gate | If no Sponsor Reviewer is recruited, the PR description explicitly names the absence and what the next-loop input would need to confirm. Pretending a Sponsor Reviewer exists when one doesn't is HCD non-compliance. | ISO 9241-210 Principle 2 + Norman *HCD Considered Harmful?* |

A backlog item or PR that fails any gate is incomplete; the gate's stage must be re-run before merge. These gates compound on top of §3 / §18 / §20 / §23 — they don't replace them.

## 27. Topic 5 HCD anti-patterns

Four HCD anti-patterns specific to single-person workspaces. Every backlog item / PR must refuse all four.

1. **Treating self as user (introspection-as-context)** — filling Activity 1 with the designer's own experience. Mitigation: three-persona synthesis + explicit naming of the limitation.
2. **Skipping the evaluate activity** — "we shipped, that's enough". Mitigation: machine-grade walkthrough as minimum + named human-grade gap.
3. **Treating accessibility as a post-hoc audit** — adding ARIA / keyboard / focus *after* the design is done, instead of specifying them as user requirements in Activity 2. Mitigation: accessibility appears in the requirements sheet, not only in the implementation.
4. **Defining the user as "the user"** — treating the user as monolithic, without personas or context. Mitigation: name personas explicitly; describe contexts per persona; surface persona-conflicts when they happen.

Each is sourced from Topic 5 deep-reading doc §11 (which cites ≥ 1 of the four required Topic 5 sources per anti-pattern).

## 28. HCD audit canonical pointer

The canonical HCD audit lives at:

```text
design/foundations/topic-05-hcd-audit.md
```

Audit 1 (v1.1 + Lab 04 Loop 1) is the workspace's first formal HCD audit. Future audits follow the same seven-step shape (Activity 1 / 2 / 3 / 4 / six-principle / W3C-triad / Findings + prioritised list) and produce the same prioritised-by-leverage closure list. Lab 05's submission (`submissions/lab-05-hcd-audit-results.md`) is the formal lab evidence for Audit 1.

The prioritised v1.2 HCD list from Audit 1 (Sponsor Reviewer + U-CONF criteria landing + systems-context-of-use doc + inclusion requirements + screen-reader test + heuristic re-audit) is inherited work for the v1.2 implementation PR.

## 29. Topic 6 Gestalt gates

Source topic: DES-001 Topic 6 — Gestalt principles. Added 2026-05-17 from Lab 06 (`design/foundations/topic-06-gestalt-audit.md`).

Every visual-treatment change must pass all three gates. They are the perceptual-layer companion to §3 (Topic 1 UI-vs-UX), §18 (Topic 2 components), §20 (Topic 3 UX), §23 (Topic 4 design-thinking), §26 (Topic 5 HCD). Gestalt sits *underneath* Topic 2 in the canonical hierarchy — these gates audit how Topic 2's components will be perceived together by the visual system.

| Gate | Pass criteria | Source |
|---|---|---|
| Perceptual-constraint gate | Every visual-treatment change names (a) the Gestalt principle(s) the change satisfies AND (b) the Gestalt principle(s) the change violates. Empty either cell = the change is taste-driven and returned. | Topic 6 deep-reading doc §1 + §7 (perceptual constraint vs aesthetic rule); quiz Q10 |
| Principle-conflict adjudication gate | For every region with competing principles (e.g., proximity vs similarity), the winning principle is named with a comparative reason rooted in the user's task. Unresolved conflicts are findings (deep-reading doc §6 violation taxonomy sub-type 3). | Smashing — task-driven adjudication; Topic 6 deep-reading doc §6 |
| Density-vs-grouping gate | For any region where whitespace is compressed (data-density requirement), the compensating grouping signal (divider, tint, alignment) must be named explicitly. Silent collapse is refused. | Smashing — density-vs-grouping framing; Topic 6 deep-reading doc §10 anti-pattern 1 |

A visual-treatment PR that fails any gate does not merge. These gates compound on top of §3 / §18 / §20 / §23 / §26 — they don't replace them. The four-cell perceptual-constraint check (principle satisfied + principle violated + compensating signal for any violation + user task served by the trade-off) is the operational shape; quiz Q10 captures the full form.

## 30. Topic 6 Gestalt anti-patterns

Three Gestalt anti-patterns specific to data-review tools. Every visual-treatment decision must refuse all three.

1. **Silent density collapse** — compressing whitespace silently to fit more information; proximity-based grouping degrades; user gets a denser screen but a weaker grouping signal. Mitigation: when whitespace must compress, substitute a different grouping signal (divider, tint, alignment) and *name* the substitution. (Source: Smashing; deep-reading doc §10.)
2. **Decorative motion** — animation used for visual polish rather than as a grouping or feedback signal. Violates common-fate (motion implies relationship). Mitigation: every animation must serve grouping or feedback; decorative-only motion is refused. The PR #12 result-count flash is the canonical correct example. (Source: Smashing; deep-reading doc §10.)
3. **Too many similarity signals** — using colour / shape / size for too many categories at once; collapses the categorical signal because the user can no longer distinguish which similarity-difference matters. Mitigation: the rule is *fewer categories, more distinct* — a small palette of similarity-classes beats a large one where the differences blur. (Source: NN/g + Smashing; deep-reading doc §10.)

A fourth implicit anti-pattern — *treating Gestalt as aesthetic rule* (stripping the principles of perceptual-constraint authority and reducing them to style advice) — is caught by §29's perceptual-constraint gate at the per-change level. Each is sourced from Topic 6 deep-reading doc §10 (which cites ≥ 1 of the four required Topic 6 sources per anti-pattern).

## 31. Gestalt audit canonical pointer

The canonical Gestalt audit lives at:

```text
design/foundations/topic-06-gestalt-audit.md
```

Audit 1 (v1.1) is the workspace's first formal Gestalt audit. Future audits follow the same six-step shape (region selection → per-region per-principle matrix → conflict adjudication → density-vs-grouping audit → findings + prioritised v1.1.x/v1.2 fix list → checklist appendix) and produce the same leverage-ranked closure list. Lab 06's submission (`submissions/lab-06-gestalt-audit-results.md`) is the formal lab evidence for Audit 1.

The prioritised Lab 06 fix list (verification-signal elevation + view-toggle separation + active-filter summary separation + sortable-header affordance + search-vs-selects separation + caution-chip divider) is inherited work for the v1.1.x polish PR, joining the Lab 04 + Lab 05 v1.2 inherited work for the v1.2 implementation PR. Five of six fixes tag as v1.1.x (visual-treatment-only); one (search-vs-select grammar unification) tags as v1.2 pending Sponsor Reviewer input.
