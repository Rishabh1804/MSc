# UX Acceptance Criteria — Destination Master Browser

Origin: Lab 03 Step 5 (`curriculum/courses/des-001-design-foundations/labs/lab-03-ux-design-journey-map.md`).
Source topic: `design/foundations/topic-03-ux-design.md`.
Companion sheet (component rules): `design/foundations/ui-design-component-rules.md`.
Status: v1 of the consolidated UX acceptance-criteria sheet. **This is the canonical UX gate for Destination Master Browser v1.1.** Browser v1.1 ships only when every gate criterion below produces a pass verdict from two independent evaluators.

This sheet is the *journey-level* companion to Topic 2's component rule sheet. Both are required:

```text
Topic 2 component rules    → what to build (components, states, anti-patterns)
Topic 3 acceptance criteria → what behaviour those components must produce
```

---

## 1. How to read this sheet

Every criterion has the form:

```text
[ID]   [Behavioural statement: the reviewer can ...]
       [Cost or measurability constraint]
       [Feedback / visibility requirement]

       Journey step:     [arrive / understand / narrow / compare / inspect / recover / leave]
       Rule-sheet ref:   [section of design/foundations/ui-design-component-rules.md]
       Lab 01 closure:   [Lab 01 finding the criterion closes]
       v1.1 UX gate?:    [yes / no — yes means must pass before v1.1 ships]
```

A criterion is **passed** when two independent evaluators applying the test to the same build agree the behaviour is present. A criterion is **failed** when either evaluator says no.

---

## 2. The criteria (12 total; 9 are v1.1 UX gates)

### Arrive

#### U-ARR-1 — Orient within 5 seconds

> The reviewer can identify the tool, the dataset, and the dataset trust state within 5 seconds of arriving on the page, without scrolling and without interaction.

- **Journey step**: Arrive
- **Rule-sheet ref**: §7 Trust signal — top-level notification banner
- **Lab 01 closure**: Exercise A — "Header / subtitle / notice exist but compete visually"
- **v1.1 UX gate**: **yes**

#### U-ARR-2 — Trust banner persistent on scroll

> The dataset trust state remains visible during scroll (sticky banner or equivalent persistence).

- **Journey step**: Arrive
- **Rule-sheet ref**: §7 Trust signal — persistence with page header
- **Lab 01 closure**: Exercise C heuristic finding on "visibility of system status"
- **v1.1 UX gate**: **yes**

### Understand

#### U-UND-1 — Trust state unambiguous via text + colour + icon

> The dataset trust state is communicated by text + colour + icon — never by colour alone. The statement names both what the dataset *is* (reference layer) and what it *is not* (Planner-ready).

- **Journey step**: Understand
- **Rule-sheet ref**: §7 Notification banner spec; §5 colour-plus-icon-plus-text rule; §6 anti-pattern 4
- **Lab 01 closure**: "Data credibility is a UX concern"
- **v1.1 UX gate**: **yes**

### Narrow

#### U-NAR-1 — Filters reversible without leaving the result list

> The reviewer can apply, combine, and remove filters along any facet without leaving the result-list view. Every applied filter is visible without scrolling and is individually removable. The result-count updates within 300ms of each interaction and the change is perceptible (animated or otherwise signposted).

- **Journey step**: Narrow
- **Rule-sheet ref**: §4 Filter-UI rules; §8 active-filter summary row
- **Lab 01 closure**: Exercise B step 2 + Exercise C heuristic "user control and freedom"
- **v1.1 UX gate**: **yes**

#### U-NAR-2 — Filter controls show their non-default state

> Filter controls visibly distinguish their default state from their applied state. Non-default selects show an accent indicator; active chips show filled/checked styling.

- **Journey step**: Narrow
- **Rule-sheet ref**: §8 selects row; §4.2 chip-active rule
- **Lab 01 closure**: Lab 02 finding F1 (active-state on filter controls)
- **v1.1 UX gate**: **yes**

#### U-NAR-3 — Trust badge survives the narrowing

> The trust badge remains visible on each record across the result list after narrowing. It does not collapse, hide, or change semantics as the result set changes.

- **Journey step**: Narrow
- **Rule-sheet ref**: §7 Trust signal — list-row depth
- **Lab 01 closure**: "Trust signal disappearing in deeper contexts"
- **v1.1 UX gate**: **yes**

### Compare

#### U-COM-1 — First comparison pass within 60 seconds + sortable columns

> The reviewer can perform a comparison pass over the filtered result set (scan an attribute across rows, identify outliers or candidates) within 60 seconds. Sortable columns are present for the high-frequency attributes (trust state, scale, verification date, Planner status).

- **Journey step**: Compare
- **Rule-sheet ref**: §3.2 table; §8 table view row + sortable columns
- **Lab 01 closure**: "Card view is not ideal for dense QA comparison"
- **v1.1 UX gate**: **yes**

#### U-COM-2 — Card/table toggle present; table is the default

> The reviewer can switch between table and card view via a single toolbar control. The default view in v1.1 is table.

- **Journey step**: Compare
- **Rule-sheet ref**: §8 card/table toggle row
- **Lab 01 closure**: "Add card/table view toggle"
- **v1.1 UX gate**: **yes**

### Inspect

#### U-INS-1 — Drawer open ≤ 2 interactions, close 1 interaction, scroll preserved

> The reviewer can open a record's full detail in ≤ 2 interactions (typically 1 click from a row or card), keeping the list visible behind the detail. The detail closes in 1 interaction (close button, Esc key, or click outside) and returns the reviewer to the list at the same scroll position.

- **Journey step**: Inspect
- **Rule-sheet ref**: §3.4 drawer; §8 record-detail drawer row
- **Lab 01 closure**: "Add click-to-inspect detail drawer"
- **v1.1 UX gate**: **yes**

#### U-INS-2 — Trust banner persistent in drawer header

> The trust state visible at the list level is also visible at the drawer-header level, in a persistent banner that does not scroll out of view.

- **Journey step**: Inspect
- **Rule-sheet ref**: §7 Trust signal — drawer-header depth
- **Lab 01 closure**: "Trust message disappears during card review"
- **v1.1 UX gate**: **yes**

#### U-INS-3 — Prev/Next navigation inside the drawer

> The reviewer can navigate to the adjacent record (Prev/Next) from inside the drawer without re-opening from the list.

- **Journey step**: Inspect
- **Rule-sheet ref**: §3.4 drawer browser application — adjacent-record navigation
- **Lab 01 closure**: "Add full-record drawer with persistent context" (refinement)
- **v1.1 UX gate**: no — desirable but deferrable to v1.1.x if it adds implementation risk

### Recover

#### U-REC-1 — Recovery from empty state in ≤ 1 interaction

> From any empty-result state, the reviewer can return to a non-empty result set in ≤ 1 interaction. The active filters are listed in the empty state and are individually removable. A "Clear all" action is the explicit recovery affordance.

- **Journey step**: Recover
- **Rule-sheet ref**: §3 containers; §8 empty state row
- **Lab 01 closure**: "No reset, no recovery"
- **v1.1 UX gate**: **yes**

#### U-REC-2 — Empty state is content-rich, not silent

> The empty state is content-rich: it lists the active filters, offers a Clear-all action, and suggests what to try next. Tone is factual, not apologetic. Loading and error states are distinct components (skeleton; inline error banner with retry).

- **Journey step**: Recover (also Arrive/Narrow when loading)
- **Rule-sheet ref**: §6 anti-pattern 5; §8 empty state + loading state + error notification rows
- **Lab 01 closure**: Lab 02 finding F3 (three-states-one-component)
- **v1.1 UX gate**: **yes**

### Leave

#### U-LEA-1 — Trust signal consistent across the journey

> The trust state visible during every journey step is consistent and accurate. The reviewer never encounters a step where the trust signal silently disappears or contradicts the list-level state.

- **Journey step**: Leave (cross-cutting verification across all steps)
- **Rule-sheet ref**: §7 Trust badge four-depth spec
- **Lab 01 closure**: "Trust signal must survive the journey"
- **v1.1 UX gate**: **yes**

---

## 3. v1.1 UX gates — the must-pass subset

These are the criteria v1.1 **must** pass before shipping. If any of these fail, v1.1 is not ready.

```text
U-ARR-1   Orient within 5 seconds
U-ARR-2   Trust banner persistent on scroll
U-UND-1   Trust state unambiguous (text + colour + icon)
U-NAR-1   Filters reversible without leaving the result list
U-NAR-2   Filter controls show their non-default state
U-NAR-3   Trust badge survives the narrowing
U-COM-1   First comparison pass within 60s + sortable columns
U-COM-2   Card/table toggle present; table is the default
U-INS-1   Drawer ≤2 open, 1 close, scroll preserved
U-INS-2   Trust banner persistent in drawer header
U-REC-1   Recovery from empty state in ≤1 interaction
U-REC-2   Empty state is content-rich; loading and error are distinct
U-LEA-1   Trust signal consistent across the journey
```

13 of the 12 listed criteria? — U-LEA-1 is the cross-cutting verification, so 12 distinct + 1 cross-cutting = 13 gate-tests. **All 13 must pass.**

(U-INS-3 — Prev/Next in drawer — is desirable but not gated. If implementation cost is high it can defer to v1.1.x without blocking v1.1 ship.)

---

## 4. Sources and traceability

Every criterion is traceable to at least one Topic 3 source, one Topic 2 rule, and one Lab 01 finding. The traceability table:

| Criterion | Primary Topic 3 source(s) | Rule-sheet ref | Lab 01 closure |
|---|---|---|---|
| U-ARR-1 | Norman (gulfs); IDEO journey-mapping | §7 banner | Header competing visually |
| U-ARR-2 | NN/g visibility-of-status heuristic | §7 persistence | Visibility-of-status finding |
| U-UND-1 | GOV.UK content discipline; NN/g | §5 / §7 | Data-credibility finding |
| U-NAR-1 | GOV.UK journey mapping; NN/g | §4 / §8 | Reset finding + user-control heuristic |
| U-NAR-2 | Norman gulf-of-evaluation | §8 selects | Lab 02 F1 |
| U-NAR-3 | Topic 1 trust framing; Topic 2 §6.2 | §7 | Trust-disappears finding |
| U-COM-1 | Norman action-stages; IDEO methods | §3.2 / §8 | Card-view finding |
| U-COM-2 | IDEO methods (task-fit) | §8 toggle | Toggle finding |
| U-INS-1 | Norman gulfs; HIG (via Topic 2); Carbon (via Topic 2) | §3.4 / §8 | Drawer finding |
| U-INS-2 | Topic 1 trust framing; Topic 2 §6.2 | §7 | Trust-disappears finding |
| U-INS-3 | IDEO methods | §3.4 application | Drawer-refinement |
| U-REC-1 | Norman gulfs; GOV.UK service-recovery | §3 / §8 | Reset/recovery finding |
| U-REC-2 | Norman gulf-of-evaluation; GOV.UK content | §6 / §8 | Lab 02 F3 |
| U-LEA-1 | Norman (mental model); Topic 1 trust framing | §7 four-depth | Trust-through-journey finding |

---

## 5. Decision-gate test plan (per criterion)

Reproduced from the journey-map doc §Decision-gate readiness for ease of reference at implementation time.

| Criterion | Test |
|---|---|
| U-ARR-1 | Open the page; verify tool + dataset + trust state visible without scroll, within 5s |
| U-ARR-2 | Scroll page; verify trust banner remains visible |
| U-UND-1 | Screenshot trust statement; verify text + colour + icon present and reading-age-appropriate |
| U-NAR-1 | Apply 3 filters; remove 1; verify active-filter summary updates and count animates within 300ms |
| U-NAR-2 | Change one select; verify visual state is unambiguously "non-default" |
| U-NAR-3 | Apply narrowing; verify every result row has trust badge |
| U-COM-1 | Ask reviewer to find most-recently-verified record in 30-row set; verify completion under 60s |
| U-COM-2 | Open page; verify table view default; verify toggle visible in toolbar |
| U-INS-1 | Open + close drawer; verify scroll position preserved |
| U-INS-2 | Open drawer; verify trust banner present and persistent in header |
| U-INS-3 | Open drawer; verify Prev/Next works without returning to list |
| U-REC-1 | Force empty state; verify Clear-all visible; verify return to non-empty in 1 click |
| U-REC-2 | Force empty state; verify active filters listed + Clear-all + what-to-try suggestion present |
| U-LEA-1 | Walk full journey; verify no step drops or contradicts trust state |

Each test has a clear pass/fail outcome. Two evaluators applying the same test reach the same verdict — that is the sheet's reproducibility guarantee.

---

## 6. Anti-patterns to refuse

Four UX anti-patterns specific to data-review tools (from Topic 3 deep-reading doc §11 and Lab 03 Step 6). Every v1.1 implementation decision must refuse all four.

1. **Designing the happy path only.** Empty / loading / error states are first-class. A design that specifies "browse → find → open" and treats the rest as edge cases is a UX failure for this product category.
2. **Confusing user request with user need.** A request names a mechanism; a need names an outcome. Every feature must produce a user need in GOV.UK form (no UI mechanism named).
3. **Skipping evaluation.** The acceptance-criteria sheet is the *minimum* evaluation gate; user testing is the next step. A v1.1 PR that does not test against these criteria is not a v1.1-ready PR.
4. **Ignoring the trust check at depth.** Trust state must survive every journey step. A design that drops the trust signal silently (during inspection, after filtering, in an empty state) is a journey UX failure.

---

## 7. Hand-off to Browser v1.1

The v1.1 implementation begins when:

- This acceptance-criteria sheet is signed off (✓ — by Lab 03 closure).
- Topic 2's component rule sheet is signed off (✓ — at `design/foundations/ui-design-component-rules.md`).
- The master-browser checklist §3, §18, and §20 gates are all referenced in the v1.1 backlog.

The v1.1 backlog adds two columns drawn from Topic 3:

| Column | Source |
|---|---|
| User need (GOV.UK form) | Topic 3 §6 user-need audit |
| Acceptance criterion ID | this sheet §2 |

Every v1.1 backlog item must populate both columns. Items that cannot are refused as decoration or solution-shape.

The v1.1 walk-through test before any v1.1 PR merges: run all 13 gate criteria against the built artifact. If any fail, the PR does not merge.

---

## 8. Versioning

| Version | Date | Change |
|---|---:|---|
| v1 | 2026-05-16 | Initial sheet — 12 criteria across 7 journey steps; 13 gate-tests; sourced and traceable |

Future versions: revisit after v1.1 ships (validate gate-tests against actual implementation), then after Topic 6 (potential additional criteria from Gestalt + Fitts'), then again at Topic 12 closure (final consolidation).
