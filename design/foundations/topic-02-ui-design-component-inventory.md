# Topic 2 — UI Design Component Inventory & State / Affordance Audit

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-02-ui-design-component-inventory.md`
Target artifact: `docs/destination-master-browser-v1.html` (671 lines, single-file dashboard)
Source topic: `design/foundations/topic-02-what-is-ui-design.md`

Steps 1–3 of Lab 02 are executed here. Steps 4–6 (container rules, filter rules, consolidated rule sheet) live in `design/foundations/ui-design-component-rules.md`. The formal lab submission with executive summary and findings lives in `curriculum/courses/des-001-design-foundations/submissions/lab-02-ui-design-component-inventory-results.md`.

---

## Step 1 — Component catalogue

Every distinct UI pattern in v1, with element category, reviewer task, and variants. Element categories are from Topic 2's lecture: **Controls / Containers / Navigation / Data display / Feedback / Editorial**.

| # | Pattern (class) | Category | Reviewer task it serves | Variants in v1 |
|---|---|---|---|---|
| P1 | Page header (`.title-group` + `.subtitle` + `.notice` + `.topline`) | Editorial + Feedback | Frames the artifact, declares dataset state, names the QA-only purpose | One; sticky-on-scroll |
| P2 | "Not Planner-ready" notice (`.notice`) | Feedback (warning) | Carries the dataset's trust state to the reviewer | Single state (warning) |
| P3 | Search input (`<input>` plain) | Control | Free-text narrow by name / place | Default + has-content (no clear button, no live state badge) |
| P4 | Source-layer select (`<select>`) | Control | Narrow by provenance (seed / candidate) | Default; no clear, no count |
| P5 | Macro-region select (`<select>`) | Control | Narrow by geography | Default; no clear |
| P6 | Scale select (`<select>`) | Control | Narrow by destination scale | Default; no clear |
| P7 | Planner-status select (`<select>`) | Control | Narrow by readiness | Default; no clear |
| P8 | Verification select (`<select>`) | Control | Narrow by trust | Default; no clear |
| P9 | Stats banner (`.stats > .stat`) | Data display | Show filtered count + status summary | Four stat cells; numbers only, no trend indicator |
| P10 | Dataset snapshot side panel (`.side-section`) | Data display | Persistent aggregate read | One panel split into sub-sections |
| P11 | Top scales mini-list (`.mini-list > .mini-row`) | Data display | Result-set composition by scale | Variable rows; no empty state for the list itself |
| P12 | Source files mini-list (`.mini-list > .mini-row`) | Data display | Seed / candidate split | Two-row list (rarely changes) |
| P13 | Record card (`.cards > .card`) | Container + Data display | Browse one record at a time | Single visual variant; no verified-vs-unverified differential styling at the card level |
| P14 | Card head (`.card-head` with `.name` + `.place` + `.id` + `.status-pill`) | Editorial + Feedback | Identity + provenance at-a-glance | One; status pill colour varies by Planner state |
| P15 | Card metadata grid (`.meta-grid`) | Data display | Six metadata fields per record | Fixed grid; field labels static |
| P16 | Status pill (`.status-pill`) | Feedback | Planner state per card | At least two visible states observed in code; uses colour + text |
| P17 | Chip set (`.chips > .chip ${cls}`) | Data display | Vibe / trip / context / caution tags per record | Variable per record; the `${cls}` template suggests sub-classes per category |
| P18 | Empty / loading / error pane (`.empty`) | Feedback | Communicates non-happy-path data states | **One CSS class used for all three states**; differentiated only by text content |
| P19 | Footer note (`.footer-note`) | Editorial | Provenance / disclaimers | One; static |
| P20 | Toolbar row (`.toolbar`) | Navigation (functional) | Groups the six form controls horizontally | One; no collapse, no overflow handling |

**Patterns absent from v1 but expected by Topic 2's pattern fit (*master-detail with faceted filtering*)**:

| Missing pattern | Category | Reviewer task it would serve | Why missing matters |
|---|---|---|---|
| Table view of records | Container + Data display | Scan-by-attribute / sort by column | Cards alone fail the *compare-many* reviewer task |
| Record-detail drawer | Container | Inspect a full record while keeping list context | v1 has no inspect target — the card is the whole record |
| Active-filter summary | Feedback + Control | Show which filters are applied; allow per-filter removal | Reviewers can lose track of accumulated filter state |
| Clear-all-filters action | Control | Recover from over-filtering | Without it, an empty-result state is hard to escape |
| Card/table view toggle | Control | Match container to task | The lack of a toggle hides the choice |
| Sortable column headers | Control | Order results by attribute | A core *compare-many* affordance |
| Sticky header / sticky filter toolbar | Container behaviour | Keep controls reachable during scroll | Long result sets currently scroll the toolbar away |
| Skeleton loader | Feedback (loading) | Preserve layout while data loads | v1 uses a single-line text message instead |
| Inline notification banner | Feedback | Surface non-modal errors and status changes | v1 only has the top notice and the shared `.empty` pane |
| Confirm modal | Container | Block-on-destructive action (e.g. batch-promote) | Reserved for v1.2+ when batch actions land |
| Focus rings | Control behaviour | Make every interactive operable by keyboard | Many v1 controls lack visible focus state |
| Active-state styling on selects | Feedback | Show which filters are non-default | Selects in v1 read the same whether default or applied |

20 patterns present; 12 patterns missing or absent. The absent list maps directly onto Topic 2's v1.1 implementation backlog.

---

## Step 2 — State coverage matrix

Rows: the 20 patterns from Step 1 that are present in v1.
Columns: the nine standard states from Topic 2's lecture and deep-reading doc.

Legend:
- ✓ = state implemented in v1
- ✗ = state should exist but is missing (finding)
- — = state does not apply to this pattern

| # | Pattern | default | hover | focus | active | disabled | loading | empty | error | success |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Page header | ✓ | — | — | — | — | — | — | — | — |
| P2 | "Not Planner-ready" notice | ✓ | — | — | — | — | — | — | — | — |
| P3 | Search input | ✓ | ✗ | ✗ | ✗ | ✗ | — | — | — | — |
| P4 | Source-layer select | ✓ | ✗ | ✗ | ✗ | ✗ | — | — | — | — |
| P5 | Macro-region select | ✓ | ✗ | ✗ | ✗ | ✗ | — | — | — | — |
| P6 | Scale select | ✓ | ✗ | ✗ | ✗ | ✗ | — | — | — | — |
| P7 | Planner-status select | ✓ | ✗ | ✗ | ✗ | ✗ | — | — | — | — |
| P8 | Verification select | ✓ | ✗ | ✗ | ✗ | ✗ | — | — | — | — |
| P9 | Stats banner | ✓ | — | — | — | — | ✗ (skeleton expected) | ✗ (zero filtered shows "0" but no narrative) | — | — |
| P10 | Dataset snapshot side panel | ✓ | — | — | — | — | ✗ | — | — | — |
| P11 | Top scales mini-list | ✓ | — | — | — | — | ✗ | ✗ | — | — |
| P12 | Source files mini-list | ✓ | — | — | — | — | ✗ | ✗ | — | — |
| P13 | Record card | ✓ | ✗ (no hover) | ✗ (not keyboard-reachable as a unit) | ✗ | ✗ (no disabled / inactive variant for blocked records) | — | — | — | — |
| P14 | Card head | ✓ | — | — | — | — | — | — | — | — |
| P15 | Card metadata grid | ✓ | — | — | — | — | — | ✗ (missing-field rendering inconsistent) | — | — |
| P16 | Status pill | ✓ (Planner states) | — | — | — | — | — | — | — | — |
| P17 | Chip set | ✓ | — | — | — | — | — | ✗ (no chips → no empty state) | — | — |
| P18 | Empty / loading / error pane | ✓ (loading text) | — | — | — | — | ✓ (text only) | ✓ (text only) | ✓ (text only) | — |
| P19 | Footer note | ✓ | — | — | — | — | — | — | — | — |
| P20 | Toolbar row | ✓ | — | — | — | — | — | — | — | — |

### State-matrix findings (ranked by severity)

**HIGH severity** — directly degrades reviewer task completion:

1. **All six form controls (P3–P8) lack visible focus, hover, and active states.** Reviewers using keyboard or assistive technology cannot tell which control has focus. Reviewers using mouse cannot see hover affordance. Reviewers cannot tell at a glance which filters are applied (no active state). Sources: Material, HIG, Carbon, GOV.UK all treat these states as first-class.
2. **Loading, empty, and error share one CSS class with text-only differentiation (P18).** This is the Norman feedback failure — the reviewer cannot tell *what* is happening without reading the message word-by-word. A skeleton loader, a content-rich empty state, and a typed error notification are different components, not three messages.
3. **Record card (P13) has no hover, focus, active, or disabled state.** The card is fully clickable in v1.1 plans but currently presents no signifier of interactivity. Norman: affordance without signifier is no affordance.
4. **Status pill (P16) varies by Planner state but verified-vs-unverified is encoded only in the metadata grid (P15).** Trust is the highest-value signal and it is the least prominent. Topic 2 §6.2 specifies a four-depth trust signal; v1 supplies one shallow signal in the wrong place.

**MEDIUM severity** — degrades trust or reviewer efficiency:

5. **Stats banner (P9) shows "0" for zero-filtered results with no narrative.** Reviewers cannot distinguish "data layer broken" from "filters narrowed correctly".
6. **Side panel (P10) and mini-lists (P11/P12) have no loading state.** During CSV fetch the panel renders pre-data labels with empty values; reviewers may treat this as "data is missing" rather than "data is still loading".
7. **Card metadata grid (P15) handles missing fields inconsistently.** Some absent values produce blanks; some produce em-dashes; none produce a "missing-field" state.
8. **Chips (P17) have no defined empty state.** A record with no tags shows nothing — indistinguishable from "tagging not yet done".

**LOW severity** — cosmetic or completeness issues:

9. Footer note, page header, toolbar, dataset snapshot are appropriately stateless or single-state.

---

## Step 3 — Affordance / signifier / feedback audit

Every interactive pattern audited on Norman's three questions. The audit checks whether the **signifier matches the affordance** and whether **feedback closes the loop** after action.

| Pattern | Affordance (what it can do) | Signifier (how the reviewer knows) | Feedback (what the reviewer sees) | Finding |
|---|---|---|---|---|
| P3 — Search input | Free-text narrows results | Default text input styling; placeholder is generic ("Search...") rather than describing the search target | Result list re-renders; stats banner updates; no count animation; no "showing X of Y" inline confirmation | **Signifier weak** (placeholder not informative); **feedback weak** (cause-and-effect is implied by stat number change but not signposted) |
| P4 — Source-layer select | Narrows by seed/candidate | Default `<select>` styling — looks pressable but does not distinguish "filter is active" from "filter is default" | Result list re-renders; stat banner updates | **Signifier broken when active** (no visible difference between "all sources" and "seed only" beyond the value-inside-the-select); **feedback weak** (the relationship between select change and stat change is not animated) |
| P5–P8 — Other selects | Same as P4 | Same as P4 | Same as P4 | Same as P4 — multiplied by five controls |
| P9 — Stats banner | Read-only (no affordance) | None (not interactive); but might be misread as clickable since cards are nearby | N/A | **No affordance, no signifier mismatch**; risk is reviewers assuming the stat cells are clickable drill-downs |
| P13 — Record card | (Planned v1.1) Click to open detail drawer | Currently nothing — no hover, no cursor pointer, no chevron icon, no border emphasis | (v1 does not open a drawer; v1.1 will) | **Hidden affordance** — even with v1.1's drawer in place, without a signifier the reviewer will not know cards are clickable |
| P16 — Status pill | Read-only (no affordance) | Coloured pill + text label | N/A | OK — but pill *looks* tappable (rounded, coloured, distinct background) so risks signalling an affordance that doesn't exist |
| P17 — Chips | Read-only display in v1 | Coloured rounded shapes — these are the visual idiom for *toggleable* filters in most design systems | N/A | **Signifier overshoots** — chips look interactive but are not; this trains the reviewer to discount actual chip interactions if v1.1 introduces them |
| P18 — Empty/loading/error pane | Read-only message + (planned v1.1) recovery action | Plain text; no icon; no recovery button | N/A | **Severe feedback gap** — without a recovery action the empty state offers no path forward; loading without skeleton offers no "system is alive" signal; error without a "retry" or "report" action is a dead end |

### Affordance findings (cross-cutting)

1. **Affordance without signifier** — the record card (P13) will be clickable in v1.1 with no current visual cue. Fix in v1.1: hover state, cursor pointer, focus ring, "open" chevron in the top-right corner of each card.
2. **Signifier without affordance** — the chips (P17) look like interactive filter chips because that's what rounded coloured chips do in Material/Carbon/HIG, but in v1 they are display-only. Fix in v1.1: either make selected chip categories filterable (preferred — gives the user a real affordance that matches the signifier) or visually distinguish *display* chips from *filter* chips.
3. **Missing feedback** — the entire pane-replacement pattern in P18 (one HTML region, three different messages) provides no animation, no progressive disclosure of detail, and no distinct visual treatment. The reviewer's mental model of *what is happening* is reconstructed entirely from reading the message text.

### Cross-state findings (Steps 2 + 3 together)

Three findings recur across multiple patterns:

- **F1 — No active state on filter controls.** Affects P3–P8. Reviewers cannot see which filters are non-default at a glance. v1.1 must add an *Active-filter summary* (chips below the toolbar, removable per filter) AND must visually distinguish "select is at its default" from "select has been changed".
- **F2 — Trust signal is shallow.** Affects P15 + P16. Verified/unverified is only in metadata text; status pill carries Planner state, not trust state. v1.1 must standardise a *trust badge component* with seven states (`verified`, `unverified`, `planner-ready`, `blocked`, `missing-fields`, `conflict`, `unassigned`) at four depths (top-of-page banner, list row, drawer header, confirm-modal). This is the Topic 2 §6.2 specification — promoting "no badge" to an explicit `unassigned` state, since Norman's feedback requirement says silence is not allowed.
- **F3 — Three feedback states share one component.** Affects P18. v1.1 must split `empty / loading / error` into three distinct components with distinct visual treatment, content rules, and (for empty and error) recovery actions.

---

## Findings summary (input to Steps 4–6)

20 patterns inventoried; 12 expected patterns missing.

**3 high-severity state findings** (focus/hover/active on controls; combined empty/loading/error pane; record-card states).

**4 medium-severity state findings** (stats-banner empty narrative; side-panel loading; metadata missing-field; chips empty state).

**3 cross-cutting affordance findings** (F1 active-state; F2 trust-signal depth; F3 three-states-one-component).

These findings drive the rule sheet in `design/foundations/ui-design-component-rules.md` (Lab 02 Steps 4–6) and the v1.1 implementation backlog in Topic 2's deep-reading doc §8.

## Decision gate

A second reviewer applying the same Topic 2 framework to the same v1 source should reach the same 20-pattern catalogue, the same 12-missing-pattern list, and the same three cross-cutting findings. The grouping (state matrix, affordance audit) is structural; the severity ranking allows narrow disagreement (HIGH vs MEDIUM) on findings 5–8 but not on findings 1–4 or F1–F3. If two reviewers diverge outside that band, a rule is missing from the rule sheet.
