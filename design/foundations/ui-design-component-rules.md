# UI Design Component Rules — Destination Master Browser

Origin: Lab 02 Steps 4–6 (`curriculum/courses/des-001-design-foundations/labs/lab-02-ui-design-component-inventory.md`)
Source topic: `design/foundations/topic-02-what-is-ui-design.md`
Companion inventory: `design/foundations/topic-02-ui-design-component-inventory.md`
Status: v1 of the consolidated rule sheet. This is the canonical input for Destination Master Browser v1.1.

This sheet is reproducible: a second reviewer applying these rules to two new records in the dataset should reach the same container and filter choices.

---

## 1. Element vocabulary (reference)

From Topic 2's lecture and deep-reading doc:

| Category | Examples | Browser examples (v1 + v1.1) |
|---|---|---|
| Controls | button, input, toggle, select, slider, chip-as-control | search input, source/region/scale/status/verification selects, future card/table toggle, future Clear-all-filters button, future filter chips |
| Containers | card, panel, drawer, modal, accordion | record card, dataset snapshot side panel, future record-detail drawer, future confirm modal for destructive batch actions |
| Navigation | menu, tabs, breadcrumbs, pagination | toolbar row (functional), future tabs for "all / verified / planner-ready" scope, future pagination if result sets grow |
| Data display | table, list, grid, tree, badge, chip-as-tag | record card grid (v1); future table mode; status pill; trust badge; vibe/trip/context/caution chips |
| Feedback | toast, banner, progress, validation, skeleton | top-of-page warning notice; future inline error banner; future skeleton loaders; future toast on filter change |
| Editorial | heading, body, caption, link | page header, subtitle, footer note, future help copy in empty state |

---

## 2. State requirements (per category)

Every interactive must implement (or explicitly N/A) all nine standard states. *Loading / empty / error* are first-class — their absence is a finding, not an omission.

| Category | Required states |
|---|---|
| Controls (interactive) | default, hover, focus, active, disabled, success-where-applicable |
| Containers (clickable, e.g. card-as-row) | default, hover, focus, active, disabled |
| Containers (non-interactive) | default only |
| Data display (collections — list, grid, table) | default, loading, empty, error |
| Data display (atomic — badge, chip, pill) | default + per-state variant |
| Feedback (toast, banner) | default + per-severity variant |
| Editorial | default only |

A "disabled" state may be N/A where no business logic disables the control. Mark it N/A explicitly; do not leave the cell blank.

---

## 3. Container-selection rules

Five containers, with explicit "when to use" and "when *not* to use" — GOV.UK-style. Each rule cites the source that primarily supports it.

### 3.1 Card

**Use when**:
- the record is a rich, mixed-format object that the reviewer wants to scan one at a time
- the reviewer task is *browse and inspect* rather than *compare across*
- there are 5–50 records on screen at once (fewer feels sparse; more loses scanability)

**Do not use when**:
- the reviewer task is *compare an attribute across many records* — use a table
- the reviewer task is *sort by an attribute* — use a table
- the result set is > 100 records on screen — cards become a scanability failure

**Sources**: Material (Card component), NN/g (card design articles), Smashing (cards-vs-tables essays).

**Browser application**: keep cards as a *secondary* view for record-as-rich-object browsing. Cards are the right container when the reviewer is looking at 10–20 records and wants the chip set + metadata + status visible at once.

### 3.2 Table

**Use when**:
- the reviewer task is *compare an ordered or numeric attribute across many records*
- the reviewer task is *sort by a column*
- the reviewer task is *batch-select* (future: promote multiple records to Planner)
- the result set is > 30 records

**Do not use when**:
- each record is so rich that one row cannot represent it without truncation that erases the comparison
- the reviewer task is purely *inspect one record* with no comparison — use a drawer or page instead

**Sources**: Carbon Data Table (primary), Material Tables, GOV.UK Tables (light).

**Browser application**: **table is the default main view** in v1.1. Sortable columns. Sticky header. Optional row expansion. The columns are: Trust badge, Name, Place, Scale, Source layer, Verification, Planner status, Last-updated. The card view remains available via a toggle in the toolbar.

### 3.3 List (simple bulleted)

**Use when**:
- the items are short, homogeneous, and need no per-item interaction beyond reading
- a tag/chip set or scale-breakdown summary is being shown

**Do not use when**:
- the reader needs to interact with each item — use a table or card grid
- the items are heterogeneous — use a card grid

**Sources**: GOV.UK Summary list, Carbon Structured list.

**Browser application**: kept for the dataset-snapshot side panel's scale breakdown and source-files breakdown. Not used for records.

### 3.4 Drawer (side panel, non-modal)

**Use when**:
- the reviewer wants to inspect one record while the list / table remains as peripheral context
- the inspection includes reading, not heavy editing
- the reviewer might want to navigate between adjacent records without re-opening

**Do not use when**:
- the task must block the rest of the UI — use a modal
- the task has its own substructure (multi-step form, document editing) — use a full-page detail
- the screen is narrow (mobile) — fall back to full-page or bottom-sheet

**Sources**: Carbon Side panel (primary), HIG sheets (translated to web), Material Navigation drawer (different use, but related anatomy).

**Browser application**: **drawer is the default for "open record"** in v1.1. Drawer opens on row click (or card click). Persistent trust banner at the top of the drawer header. Close affordance: explicit close button (top-right), Esc key, click outside. Adjacent-record navigation via Prev/Next buttons in the drawer header.

### 3.5 Modal

**Use when**:
- the action is *destructive* and the reviewer must confirm or cancel before proceeding
- the action is *must-finish-or-cancel* (e.g. a multi-step edit that the user explicitly started)
- the action requires the reviewer's full attention because the wrong outcome is irreversible

**Do not use when**:
- the task is browsing, inspecting, or filtering — those are non-blocking
- the only reason to use a modal is "we needed somewhere to put the form" — that's a drawer (or page) job
- the modal blocks an action that is reversible — drawer is sufficient

**Sources**: HIG Modality (primary), Carbon Modal (with usage gates), GOV.UK (avoid where possible), Material Dialog (the more permissive position, used as a counterweight).

**Browser application**: **reserved for v1.2+** confirmation of batch-promote-to-Planner, batch-block, and other destructive actions. Not used in v1.1 because v1.1 does not introduce destructive actions yet.

### 3.6 Container selection — decision tree

```text
Reviewer wants to ...
├─ scan many records by attribute / sort / batch-select ──────────► TABLE  (default v1.1)
├─ browse rich records 10–20 at a time ──────────────────────────► CARD GRID  (secondary v1.1)
├─ read full fields of one record while keeping list context ────► DRAWER  (default for "open record")
├─ confirm a destructive batch action ───────────────────────────► MODAL  (deferred to v1.2+)
├─ edit a record across multiple steps with its own substructure ► FULL-PAGE DETAIL  (out of scope v1.1)
└─ read a short homogeneous summary (scale breakdown, etc.) ─────► LIST  (kept in side panel)
```

---

## 4. Filter-UI selection rules

Four filter patterns; each with usage criteria.

### 4.1 Search input (free-text)

**Use when**:
- the user knows what they're looking for (name, place fragment, ID)
- the field is high-cardinality (any of 359+ destination names)

**Do not use when**:
- the user is exploring (does not know the search target) — use chips/dropdowns for facet browsing

**Browser application**: keep the search input for free-text name/place narrowing. Improve in v1.1: a clear-button when content is present, a label rather than a placeholder, and an inline result count ("Showing 42 of 359") under the input.

### 4.2 Filter chip (toggleable)

**Use when**:
- the facet is *low-cardinality* (2–7 values)
- the user gains from seeing all values at once
- the user might combine multiple values within a facet (OR-logic across chips of the same facet)

**Do not use when**:
- the facet has > 8 values — use a dropdown to keep visual weight manageable
- the facet is hierarchical — use a tree or grouped dropdown

**Browser application**: **chip rows in v1.1** for:
- *Source layer* (seed / candidate)
- *Verification* (verified / unverified / blocked / unassigned)
- *Planner status* (planner-ready / not-ready)

Each chip has explicit default / hover / focus / active states. The chip's *active* state is unambiguous: filled background, checkmark icon, and the result count updates on toggle.

### 4.3 Dropdown (single-select)

**Use when**:
- the facet has > 8 values (e.g. macro-region: 9+ regions)
- the user typically picks one value at a time

**Do not use when**:
- the facet has 2–7 values — use chips
- the user needs to combine multiple values — use a multi-select with a chip-summary

**Browser application**: dropdowns kept for *Macro-region* and *Scale*. In v1.1 they gain a visible "is non-default" indicator (a small accent dot on the right edge of the select) and a "Clear" affordance inside the dropdown panel.

### 4.4 Faceted panel (advanced filter)

**Use when**:
- there are many facets, each with its own value set, and the user combines several
- the result set is large and the user iterates

**Do not use when**:
- the facets are few — the toolbar is sufficient

**Browser application**: a faceted panel is **not** introduced in v1.1. The current toolbar plus chip rows is sufficient for the seven facets. A faceted panel will be considered in v1.2 if reviewer feedback shows current narrowing is insufficient.

### 4.5 Filter-UI decision tree

```text
Filter facet ...
├─ Free-text, high-cardinality   ───────────► SEARCH INPUT
├─ 2–7 values, may combine within ──────────► CHIP ROW
├─ > 8 values, single-pick at a time ───────► DROPDOWN
└─ Many facets, deep iteration ─────────────► FACETED PANEL (deferred to v1.2)
```

### 4.6 Active-filter summary (cross-cutting)

**Required** in v1.1 regardless of which filter pattern is in use. Appears as a removable-chip row above the result list. Shows every applied filter with its value (e.g. *Verified only ✕*, *Region: West Asia ✕*, *Scale: country ✕*). Includes a **"Clear all filters"** button at the right. The summary is the recovery affordance the v1 design lacks.

---

## 5. Affordance / signifier / feedback minimums

Every interactive on the browser must satisfy all three minimums.

### 5.1 Affordance

The action the control can perform is documented in the rule sheet entry for that pattern. A control that cannot name its affordance is rejected (decoration).

### 5.2 Signifier

The signifier requirement is *visible to a reviewer who has not seen the product before*. Pass criteria:

- Pointer-style cursor on hover for clickable elements
- Visible hover background or border change
- Visible focus ring (≥ 2px, AA contrast against background) for keyboard reachability
- An icon, label, or shape that communicates the action type (chevron for "open", × for "remove", magnifying glass for "search")
- Active/selected state visually distinct from default (filled background + icon for chips, accent dot for changed selects)

A pattern with affordance but no signifier is a *hidden affordance* finding (Norman, deep-reading doc §3.5).

### 5.3 Feedback

After action, the reviewer sees one of:

- Immediate visible state change of the control (chip toggles from outline → filled; input shows clear-button)
- Result-region update (stats animate, table re-renders with a subtle transition)
- Inline notification ("3 filters applied", "Showing 12 of 359")
- For long actions (> 300ms): a loading state in the affected region

Feedback may not be silent. A control whose only confirmation is "the list looked different next time the user scrolled" fails this minimum.

---

## 6. Anti-patterns to refuse

Seven specific anti-patterns, sourced from Topic 2's deep-reading doc §7. Each is grounded in at least two of the five required sources.

1. **Modal-as-default container.** Inspecting a record never blocks the list. Drawer-only for inspection.
2. **Cards as the *only* main list view.** Cards fail scan-by-attribute and sort-by-column. Provide a table.
3. **Decorative badges.** Badge = state. Every badge has a defined state from the trust-badge state set or the Planner-status set. No "decorative" badges.
4. **Colour-only signalling.** Status conveyed by colour is also conveyed by icon and text label. WCAG 1.4.1 hard requirement.
5. **Empty-state silence.** Zero-result states include active-filter summary, Clear-all action, and a "what to try next" message.
6. **Loading silence.** Skeleton loader for any request that takes > 300ms. Plain text loading messages are not sufficient.
7. **Inconsistent affordance.** Same action uses the same control across every context. If list row opens a drawer, table row opens a drawer, card click opens a drawer. No mixed behaviour.

---

## 7. Trust signal — four-depth specification

(Carried forward from Topic 2 deep-reading doc §6.2; this is the canonical statement of the v1.1 trust-signal requirement.)

| Depth | Component | Content | Persistence |
|---|---|---|---|
| Page | Notification banner (Carbon `Inline notification` / GOV.UK `Notification banner`) | "Reference layer — not Planner-ready" + dataset summary | Sticky with the page header |
| List row | Trust badge (one component, seven states: `verified`, `unverified`, `planner-ready`, `blocked`, `missing-fields`, `conflict`, `unassigned`) | Icon + text + colour | First column of table; top-right of card |
| Drawer header | Notification banner (compact) | Record's current trust state + one sentence of explanation | Pinned to drawer header; does not scroll |
| Confirm modal (v1.2+) | Re-statement | Current state → new state of every affected record | Inside the modal body |

The trust badge is **one component used at multiple depths**, not three different badges. Consistency reduces cognitive load (Topic 2 deep-reading doc §1, sources S1–S5 agreement).

Colour palette for the seven states is deferred to Topic 10 (Color theory) — until then, the rule is "colour + icon + text, never colour alone".

---

## 8. Per-component rules (the catalogue, formalised)

Each row binds an inventory pattern (from `topic-02-ui-design-component-inventory.md`) to its v1.1 rule.

| Pattern | v1 state | v1.1 rule |
|---|---|---|
| P1 Page header | Present | Add the dataset-trust notification banner inside the header; persist on scroll |
| P3 Search input | Present, weak states | Add label (replace placeholder), clear-button when has content, inline result count below |
| P4–P8 Selects | Present, no active state | Add accent-dot when value ≠ default; ensure focus ring; add "Clear" affordance inside the panel |
| New: Filter chip row | — | Add three chip rows: Source layer, Verification, Planner status. Active state = filled + checkmark. Toggleable; multi-select within row |
| New: Active-filter summary | — | Removable-chip row above results; "Clear all" button at the right |
| P9 Stats banner | Present, numeric | Add narrative for zero-filtered ("0 of 359 — try clearing filters"); add skeleton loading state |
| P10 Side panel | Present, no loading | Add skeleton during fetch; section labels stay; values render as skeleton blocks |
| P13 Record card | Present, no hover/focus/click | Add hover (background tint), focus ring, cursor pointer, "open" chevron top-right; clicking opens the drawer |
| New: Table view | — | Sortable columns: Trust, Name, Place, Scale, Source, Verification, Planner status, Last-updated. Sticky header. Click row → drawer |
| New: Card/table toggle | — | Toggle in toolbar right slot. Default in v1.1: **table** |
| P16 Status pill | Planner-state only | Repurpose to *Planner-status* badge only; trust state moves to the new trust badge component |
| New: Trust badge | — | One component, seven states; used at top banner, list row, card top-right, drawer header |
| P17 Chip set | Display-only | Keep as display chips; visually distinguished from filter chips (smaller, neutral tone) |
| New: Empty state | One shared `.empty` | Distinct component. Content: active-filter summary inline + "Clear all" CTA + "Try removing X filter" suggestion |
| New: Loading state | Text-only | Skeleton loader for cards/table; spinner only for global page load |
| New: Error notification | Text-only via `.empty` | Inline error banner inside result region: what failed + retry button + report-issue link |
| New: Record-detail drawer | — | Side-panel, non-modal, with sticky trust banner, Prev/Next, close affordance (button + Esc + click-outside) |
| P19 Footer note | Present | Unchanged |
| P20 Toolbar | Present | Adds: card/table toggle, Clear-all filters; chips wrap below selects on narrow widths |

---

## 9. Definition of done for the rule sheet

The rule sheet is "done" when:

- Every pattern in `topic-02-ui-design-component-inventory.md` has a corresponding v1.1 rule (table in §8).
- Every container selection has a "when to use" + "when not to use" + a sourced rationale.
- Every filter pattern has a decision criterion that two reviewers applying it produce the same outcome.
- The seven anti-patterns are explicit and each is sourced from ≥ 2 of the five required Topic 2 sources.
- The trust-signal specification names a component, the seven states, the four depths, and the colour-plus-icon-plus-text rule.

All five criteria are met. The sheet is signed off for v1.1 input.

## 10. Hand-off to Browser v1.1

The v1.1 implementation begins after Topic 3 (UX design) produces the reviewer-journey + UX-acceptance-criteria companion. Both this sheet and Topic 3's output are required before v1.1 code lands — Topic 2 gives the *what* (components and rules); Topic 3 gives the *why* (journey gates).

Implementation order (already in the deep-reading doc §8, restated for clarity):

1. Table mode + card/table toggle
2. Record-detail drawer
3. Active-filter summary + Clear-all
4. Empty state (distinct component)
5. Skeleton loading
6. Inline error notification
7. Top-level trust notification banner
8. Unified trust badge component (seven states, four depths)
9. Focus rings + keyboard navigation
10. Defer all decorative additions until 1–9 are complete

Browser v1.1 success criteria are inherited from the master-browser checklist §16 plus the six Topic 2 gates appended in §18 of that checklist.
