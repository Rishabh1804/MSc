# Topic 3 — UX Design Journey Map and Gap Analysis

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-03-ux-design-journey-map.md`
Target artifact: `docs/destination-master-browser-v1.html`
Source topic: `design/foundations/topic-03-ux-design.md`
Companion topic (UI design): `design/foundations/topic-02-what-is-ui-design.md` and `design/foundations/ui-design-component-rules.md`

Steps 1–4 of Lab 03 are executed here. Step 5 (the consolidated acceptance-criteria sheet) lives in `design/foundations/ux-acceptance-criteria.md`. The formal lab submission with executive summary lives at `curriculum/courses/des-001-design-foundations/submissions/lab-03-ux-design-journey-map-results.md`. Step 6 (master-browser checklist Topic 3 section) is appended to `design/checklists/master-browser-design-checklist.md`.

---

## Step 1 — Full reviewer journey map

The seven-step journey for the Destination Master Browser, with each step's goal (in GOV.UK user-need form), cost budget, failure mode, trust check, current v1 state, and gap vs Lab 01.

### Step 1: Arrive

| Field | Content |
|---|---|
| **Goal** | *As a reviewer, I need to orient to the tool and the dataset within seconds, so that I can start work without confusion.* |
| **Cost budget** | ≤ 5 seconds, no interactions |
| **Failure mode** | Reviewer can't tell what tool they're using, what dataset is loaded, or what state the dataset is in |
| **Trust check** | Top-of-page dataset-trust banner visible (not-Planner-ready statement) |
| **Current v1 state** | **Partial** — Page title, subtitle, and warning notice are present in the header. The "Structurally valid / not Planner-ready" badge and the QA-only-use note are visible without scrolling. Failure: the dataset-trust statement is not styled as a *Notification banner* (Topic 2 rule sheet), so it competes visually with the rest of the header rather than being unambiguous. |
| **Gap vs Lab 01** | Lab 01 noted "User can scroll past the warning into cards"; Lab 03 specifies the persistent-on-scroll requirement as the criterion that closes this. |

### Step 2: Understand

| Field | Content |
|---|---|
| **Goal** | *As a reviewer, I need to read the dataset's overall trust state, so that I treat the records appropriately and don't over-trust or under-trust them.* |
| **Cost budget** | ≤ 10 seconds, no interactions |
| **Failure mode** | Reviewer either over-trusts ("looks Planner-ready") or under-trusts ("this tool is broken — leave") |
| **Trust check** | Dataset-trust statement is unambiguous: text + colour + icon. Says what the dataset *is* (reference layer) and what it *is not* (Planner-ready), without ambiguity. |
| **Current v1 state** | **Partial** — Trust statement is in the warning notice but written more as informational copy than as a status. Reviewer can read it correctly but might also read it as a one-time disclaimer rather than an active state. |
| **Gap vs Lab 01** | Lab 01 framed this as "data credibility is a UX concern"; Lab 03 specifies the trust-as-state framing (with icon + colour reinforcing text) as the criterion that closes this. |

### Step 3: Narrow

| Field | Content |
|---|---|
| **Goal** | *As a reviewer, I need to constrain the result set along any facet (source layer, region, scale, Planner status, verification), so that I focus on the records I want to review.* |
| **Cost budget** | ≤ 3 interactions per facet; ≤ 30 seconds total to apply a multi-facet narrowing |
| **Failure mode** | Filter applied but reviewer cannot tell which filters are active, cannot remove them individually, and cannot recover quickly |
| **Trust check** | Trust badge remains visible on each record after narrowing (does not disappear into the filtered view) |
| **Current v1 state** | **Partial-to-fail** — Six form controls (search + 5 selects) apply correctly. Failure: no active-filter summary; no individual filter removal; selects show no "is non-default" state; reviewer must scan back to the toolbar to see what's applied. Lab 02 finding F1. |
| **Gap vs Lab 01** | Lab 01 said "no quick filters, no collapsible filter panel, no reset"; Lab 03 specifies the active-filter summary + per-filter removal as the criterion that closes this. |

### Step 4: Compare

| Field | Content |
|---|---|
| **Goal** | *As a reviewer, I need to scan many records along common attributes (e.g. trust state, scale, verification date), so that I find outliers, duplicates, or promotion candidates.* |
| **Cost budget** | ≤ 60 seconds for the first comparison pass over a filtered result set |
| **Failure mode** | Cards-only forces serial reading; sort is missing; reviewer cannot scan an attribute across records efficiently |
| **Trust check** | Trust badge in the first column of any table mode (Topic 2 rule sheet §7) |
| **Current v1 state** | **Fail** — No table mode. No sort. Cards-only. The Compare step is the worst-served step in v1; this is the central reviewer-task failure Topic 2 + Topic 3 are correcting. |
| **Gap vs Lab 01** | Lab 01 said "Card view is not ideal for dense QA comparison; add table mode and sort control"; Lab 03 specifies the cost budget (≤ 60s for first pass) and the column requirements as the criteria that close this. Topic 2 §3.2 specifies the implementation. |

### Step 5: Inspect

| Field | Content |
|---|---|
| **Goal** | *As a reviewer, I need to read a record's full detail while keeping the list in peripheral context, so that I do not lose my place in the review.* |
| **Cost budget** | ≤ 2 interactions to open; ≤ 5 seconds to render full content; ≤ 1 interaction to close and return to the list at the same scroll position |
| **Failure mode** | Modal blocks the list (HIG anti-pattern); full-page navigation breaks context and forces back-button + scroll-restore work; reviewer loses their place |
| **Trust check** | Trust banner persistent in drawer header (does not scroll out of view) |
| **Current v1 state** | **Fail** — No drawer; no full-detail view at all. Cards expose all on-card metadata but there is no "open record" action. The reviewer cannot Inspect any record beyond what the card shows; full-record detail requires re-running the CSV by hand. |
| **Gap vs Lab 01** | Lab 01 said "Add click-to-inspect detail drawer"; Lab 03 specifies the drawer-not-modal choice (sourced from HIG + Carbon + GOV.UK majority position), the cost budget, and the trust-banner persistence as the criteria that close this. Topic 2 §3.4 specifies the implementation. |

### Step 6: Recover

| Field | Content |
|---|---|
| **Goal** | *As a reviewer, I need to escape an over-filtered state and adjust filters individually without losing orientation, so that I keep working efficiently rather than restarting.* |
| **Cost budget** | ≤ 1 interaction to clear all filters; ≤ 1 interaction per filter to remove individually |
| **Failure mode** | Reset is hidden or absent; no active-filter summary; reviewer scrolls to the toolbar, hunts for each control, and re-selects defaults manually |
| **Trust check** | Trust badge survives the recovery sequence (still shown on records after narrow → empty → recover) |
| **Current v1 state** | **Fail** — No reset, no Clear-all, no active-filter summary. Empty state is one shared `.empty` text message ("No records match the current filters") with no recovery action. Reviewer must manually reset each of the six controls. |
| **Gap vs Lab 01** | Lab 01 said "Add reset and active-filter summary"; Lab 03 specifies the ≤1-interaction recovery budget and the content-rich empty state as the criteria that close this. Topic 2 §8 specifies the implementation (empty state row + active-filter summary row). |

### Step 7: Leave

| Field | Content |
|---|---|
| **Goal** | *As a reviewer, I need to leave with an accurate mental model of which records I reviewed and what their trust state was, so that downstream decisions (promote to Planner, mark for enrichment, reject) are correct.* |
| **Cost budget** | Not interaction-bounded; bounded by whether the reviewer's mental model at the end matches reality |
| **Failure mode** | Reviewer leaves over-confident — they think they reviewed verified records when some were unverified; or under-confident — they think nothing is safe |
| **Trust check** | The final trust state visible during the journey was honest at every depth; no step in the journey dropped the trust signal silently |
| **Current v1 state** | **Partial** — The top warning is correct but trust state during the journey is shallow (Lab 02 finding F2). Reviewers reading only the card view can drift toward over-confidence in records that have no warning chip. |
| **Gap vs Lab 01** | Lab 01 said "Trust message may disappear from focus during card review"; Lab 03 specifies the trust-signal-survives-every-step criterion as the closure. Topic 2 §6.2 specifies the four-depth implementation. |

### Journey-map summary

- **Pass-or-better steps in v1**: 0 of 7 (none cleanly pass)
- **Partial in v1**: 3 of 7 (Arrive, Understand, Leave)
- **Partial-to-fail**: 1 of 7 (Narrow)
- **Fail**: 3 of 7 (Compare, Inspect, Recover)

The three Fail steps are the central reviewer-task gaps Topic 2 + Topic 3 + v1.1 must close. The Partial-to-fail step (Narrow) closes with the active-filter summary work. The Partial steps close with persistence-and-styling work on existing components.

---

## Step 2 — UX acceptance criteria (per-step)

For each journey step, 1–3 testable, behavioural, mechanism-independent criteria. Each criterion is cross-referenced to:
- **Topic 2 rule sheet component(s)** that implement it
- **Lab 01 finding(s)** it closes

### Arrive

| ID | Criterion | Topic 2 ref | Lab 01 ref |
|---|---|---|---|
| **U-ARR-1** | The reviewer can identify the tool, the dataset, and the dataset trust state within 5 seconds of arriving on the page, without scrolling and without interaction. | Top-level notification banner (§7) | Lab 01 Exercise A: "Header / subtitle / notice exist but compete visually" |
| **U-ARR-2** | The dataset trust state remains visible during scroll (sticky banner or equivalent persistence). | Notification banner persistence (§7) | Lab 01 Exercise C heuristic finding on "visibility of system status" |

### Understand

| ID | Criterion | Topic 2 ref | Lab 01 ref |
|---|---|---|---|
| **U-UND-1** | The dataset trust state is unambiguously communicated via text + colour + icon — colour alone is insufficient. The statement names both what the dataset *is* (reference layer) and what it *is not* (Planner-ready). | Notification banner spec (§7); colour-plus-icon-plus-text rule (§5 anti-pattern 4) | Lab 01: "data credibility is a UX concern" |

### Narrow

| ID | Criterion | Topic 2 ref | Lab 01 ref |
|---|---|---|---|
| **U-NAR-1** | The reviewer can apply, combine, and remove filters along any facet without leaving the result-list view. Every applied filter is visible without scrolling and is individually removable. The result-count updates within 300ms of each interaction and the change is perceptible. | Active-filter summary (§8); filter chips / dropdowns / search (§4) | Lab 01 Exercise B step 2 + Exercise C heuristic "user control and freedom" |
| **U-NAR-2** | Filter controls visibly distinguish their default state from their applied state (non-default selects show an accent indicator; active chips show filled/checked styling). | Selects rule (§8) + chip-active rule (§4.2) | Lab 02 finding F1 |
| **U-NAR-3** | The trust badge remains visible on each record across the result list after narrowing — it does not collapse or hide as the result set changes. | Trust badge persistence (§7) | Lab 01: "trust signal disappearing in deeper contexts" |

### Compare

| ID | Criterion | Topic 2 ref | Lab 01 ref |
|---|---|---|---|
| **U-COM-1** | The reviewer can perform a comparison pass over the filtered result set (scan an attribute across rows, identify outliers or candidates) within 60 seconds. Sortable columns are present for the high-frequency attributes (trust state, scale, verification, Planner status). | Table view (§3.2 + §8); sortable columns (§8) | Lab 01: "Card view is not ideal for dense QA comparison" |
| **U-COM-2** | The reviewer can switch between table and card view via a single toolbar control. The default view in v1.1 is table. | Card/table toggle (§8) | Lab 01: "add card/table view toggle" |

### Inspect

| ID | Criterion | Topic 2 ref | Lab 01 ref |
|---|---|---|---|
| **U-INS-1** | The reviewer can open a record's full detail in ≤ 2 interactions (typically 1 click from a row or card), keeping the list visible behind the detail. The detail closes in 1 interaction (close button, Esc, or click-outside) and returns the reviewer to the list at the same scroll position. | Record-detail drawer (§3.4 + §8) | Lab 01: "Add click-to-inspect detail drawer" |
| **U-INS-2** | The trust state visible at the list level is also visible at the drawer-header level, in a persistent banner that does not scroll out. | Trust banner in drawer header (§7) | Lab 01: "Trust message disappears during card review" |
| **U-INS-3** | The reviewer can navigate to the adjacent record (Prev/Next) from inside the drawer without re-opening from the list. | Drawer navigation (§3.4 browser application) | Lab 01: "add full-record drawer with persistent context" (refinement) |

### Recover

| ID | Criterion | Topic 2 ref | Lab 01 ref |
|---|---|---|---|
| **U-REC-1** | From any empty-result state, the reviewer can return to a non-empty result set in ≤ 1 interaction. The active filters are listed in the empty state and are individually removable. A "Clear all" action is the explicit recovery affordance. | Empty state component (§3 + §8); active-filter summary (§8) | Lab 01: "no reset, no recovery" |
| **U-REC-2** | The empty state is content-rich, not silent: it lists the active filters, offers a Clear-all action, and suggests what to try next. Tone is factual, not apologetic. | Empty state spec (§7 anti-pattern 5; §8) | Lab 02 finding F3 |

### Leave

| ID | Criterion | Topic 2 ref | Lab 01 ref |
|---|---|---|---|
| **U-LEA-1** | The trust state visible during every journey step is consistent and accurate. The reviewer never encounters a step where the trust signal silently disappears or contradicts the list-level state. | Trust badge four-depth spec (§7) | Lab 01: "trust signal must survive the journey" |

### Acceptance-criterion summary

- **12 criteria across 7 steps** (1–3 per step; cost budgets explicit where applicable)
- Every criterion is **behavioural** (the reviewer can do X)
- Every criterion is **mechanism-independent** (no UI mechanism named — components are referenced via the rule sheet)
- Every criterion is **measurable** (interaction count, time budget, or visibility requirement)
- Every criterion is **traceable** to at least one Topic 2 rule and one Lab 01 finding

The full criteria sheet (with the v1.1 UX gates subset marked) lives at `design/foundations/ux-acceptance-criteria.md`.

---

## Step 3 — User-need extraction (need / request / solution-shape audit)

Every currently-implemented browser feature and every v1.1 backlog item is audited. The discipline: produce the user need in GOV.UK form, then classify how the feature/backlog item arrived.

### v1 features — user-need extraction

| Feature | User-need form | Classification |
|---|---|---|
| Search input | *As a reviewer, I need to find a destination by name or place fragment, so that I can jump to a known record quickly.* | **Need** (outcome named; "search input" is one valid implementation) |
| Source-layer / region / scale / Planner-status / verification selects | *As a reviewer, I need to narrow the result set along [facet], so that I focus on records I want to review.* | **Need** per facet (outcome named; "select" is one of several valid implementations) |
| "Not Planner-ready" notice | *As a reviewer, I need to read the dataset's overall trust state, so that I treat records appropriately.* | **Need** (Topic 1 / U-UND-1 traceable) |
| Stats banner | *As a reviewer, I need to see the result-set composition (count, status mix) so that I have aggregate context while browsing.* | **Need** |
| Dataset snapshot side panel | *As a reviewer, I need to see the result-set composition by scale and source while browsing, so that I understand the distribution.* | **Need** (related to stats banner; could be merged in v1.2 if reviewer feedback shows redundancy) |
| Record cards | *As a reviewer, I need to browse rich-record information one record at a time when scanning for candidates.* | **Need** (specific to one subset of journey work — Inspect-adjacent, not Compare) |
| Status pill (Planner state) | *As a reviewer, I need to see each record's Planner-readiness at the list level.* | **Need** (rule-sheet aligns this with the Planner-status badge, distinct from trust badge) |
| Vibe/trip/context/caution chips | *As a reviewer, I need to see each record's tag-set at the list level for fast semantic scanning.* | **Need** (distinguish display chips from filter chips per rule sheet §4.2 anti-pattern) |
| `.empty` shared pane | *As a reviewer, I need to see what's happening when results aren't shown (loading / empty / error).* | **Need underneath; implementation is solution-shape** — one shared component for three distinct states is a designer-assumption shortcut, not a true response to the need |

### v1.1 backlog (Topic 2 §8 + Lab 02 rule sheet §8) — user-need check

| Backlog item | User-need form | Classification |
|---|---|---|
| Table mode | *As a reviewer, I need to scan many records along common attributes, so that I find outliers and candidates.* | **Need** (U-COM-1 traceable) |
| Record-detail drawer | *As a reviewer, I need to read full record fields while keeping the list visible, so that I don't lose my place.* | **Need** (U-INS-1) |
| Active-filter summary | *As a reviewer, I need to see and individually remove filters I've applied, so that I can adjust narrowing without restarting.* | **Need** (U-NAR-1) |
| Clear-all-filters action | *As a reviewer, I need to recover from an over-filtered state quickly without losing orientation.* | **Need** (U-REC-1; this was the "Reset button" user request, rewritten as a need) |
| Card/table toggle | *As a reviewer, I need to switch between scan-by-attribute and read-rich-record views depending on my current task.* | **Need** (U-COM-2) |
| Sortable column headers | *As a reviewer, I need to order records by an attribute, so that comparison is structured.* | **Need** (U-COM-1) |
| Sticky header / sticky toolbar | *As a reviewer, I need to keep the controls reachable while scrolling a long result set.* | **Need** |
| Skeleton loader | *As a reviewer, I need to know the system is fetching data (not broken) and roughly where content will appear.* | **Need** (Norman gulf-of-evaluation closure) |
| Inline error notification | *As a reviewer, I need to know what failed and what to do about it.* | **Need** |
| Focus rings | *As a reviewer using keyboard or assistive tech, I need to see which control has focus.* | **Need** (accessibility-grounded) |
| Active-state styling on selects | *As a reviewer, I need to see which filters are at their default vs which have been changed.* | **Need** (U-NAR-2) |
| Trust-badge component (7 states, 4 depths) | *As a reviewer, I need to see each record's trust state at every step of my review, so that I do not over-trust or under-trust records.* | **Need** (the highest-leverage need; multiple criteria depend on it) |
| Confirm modal (deferred to v1.2+) | *As a reviewer, I need to confirm destructive actions before they execute.* | **Need** (deferral is principled — destructive batch actions are not in v1.1 scope) |

### Audit summary

- All 9 v1 features map to a clean user need.
- All 13 v1.1 backlog items map to a clean user need.
- One v1 implementation choice is solution-shape (the shared `.empty` pane). v1.1 splits it into three distinct components per the rule sheet.
- The Reset-button class of user-request was correctly rewritten in v1.1 as a Clear-all + active-filter summary need rather than ported as-is.

The audit confirms v1's underlying needs are sound. The shortcomings are at the *implementation* layer (Topic 2) and at the *journey-completion* layer (Topic 3), not at the user-need layer.

---

## Step 4 — Lab 01 → Lab 03 gap analysis

For each Lab 01 finding, state whether Lab 03 confirms / refines / contradicts, the Topic 3 criterion that closes it, and the post-v1.1 status.

| # | Lab 01 finding | Lab 03 treatment | Closure criterion | Closed by v1.1? |
|---|---|---|---|---|
| 1 | "User cannot easily undo a filter combination — no reset" | **Refines** (cost budget = ≤ 1 interaction; recovery is in empty state, not only in toolbar) | U-REC-1 | **Yes** (rule sheet empty state + active-filter summary) |
| 2 | "Card view not ideal for dense QA comparison — add table mode" | **Confirms + refines** (table is default in v1.1, not a toggle preference) | U-COM-1 + U-COM-2 | **Yes** (rule sheet table view + toggle) |
| 3 | "No full-record drawer/modal" | **Refines** (specifically drawer, not modal — HIG/Carbon/GOV.UK majority position) | U-INS-1 + U-INS-2 + U-INS-3 | **Yes** (rule sheet drawer; deferred-modal-to-v1.2 also from rule sheet) |
| 4 | "Trust message may disappear from focus during card review" | **Confirms + extends** (Topic 2 §6.2 four-depth spec; U-LEA-1 makes it journey-level) | U-LEA-1 + U-INS-2 + U-NAR-3 | **Yes** (rule sheet trust-badge + notification banner persistence) |
| 5 | "Filter controls exist but are not grouped/collapsible" | **Refines** (collapsible deferred to v1.2 if needed; active-filter summary is the higher-priority fix) | U-NAR-1 + U-NAR-2 | **Yes** for the higher-priority fix; **deferred** for collapsible (not in v1.1 scope) |
| 6 | "Loading and error states are readable but minimal" | **Refines** (three distinct components, not one shared pane — Lab 02 F3) | U-REC-2 implied (loading is implicitly covered by skeleton-loader rule) | **Yes** (rule sheet split + skeleton + inline error) |
| 7 | "Hierarchy: cards remain generic — status semantics can improve" | **Refines** (Planner-status badge + trust-badge are now distinct components; cards no longer carry conflated status) | U-NAR-3 + U-LEA-1 | **Yes** (rule sheet trust-badge separation) |
| 8 | "Status semantics can be improved" | **Refines** (seven trust states + Planner-status set; no overlap) | U-LEA-1 | **Yes** |
| 9 | "Empty/error states are readable and actionable" (Lab 01 pass) | **Disagrees** at the implementation level (Lab 01 marked pass; Lab 02 + Lab 03 mark fail — silent text-only is not actionable) | U-REC-1 + U-REC-2 | **Yes** (this is the upgrade Lab 03 specifies) |
| 10 | "Drawer/modal can be closed clearly" (Lab 01: pass anticipating future drawer) | **Refines** (close button + Esc + click-outside; return to same scroll position) | U-INS-1 | **Yes** |
| UX Honeycomb facets (Lab 01) | **Findable + Credible + Useful** were the three weakest facets; all three are closed by the Topic 3 criteria | U-NAR-1 (findable), U-LEA-1 (credible), U-COM-1 (useful) | **Yes** |

### Gap-closure summary

- **11 Lab 01 findings tracked**; **all 11 closeable by v1.1** with Topic 2 + Topic 3 implementation.
- **1 disagreement** with Lab 01's heuristic verdict (item 9, empty/error states): Lab 01 marked pass; Labs 02 + 03 mark fail. The disagreement is honest — the heuristic audit's standard for "actionable" is lower than the acceptance-criterion's standard. Both audits agree the implementation is *minimal*; the disagreement is whether minimal counts as a finding. Topic 3 treats it as a finding.
- **Findings deferred to v1.2+**: collapsible filter panel (item 5 sub-element); confirm modal for destructive batch actions; faceted-filter panel.

The disagreement at item 9 is the kind of thing the topic structure produces by design: heuristic audits and acceptance criteria evaluate at different granularities. Lab 01 was right at heuristic granularity; Lab 03 is right at criterion granularity. The v1.1 implementation honours the stricter standard.

---

## Decision-gate readiness

Per the lab brief: *"Lab 03 is complete when a second evaluator, given the acceptance-criteria sheet and the v1 browser, would produce the same pass/fail verdict for each criterion."*

Each of the 12 criteria in §Step 2 is testable as a pass/fail behaviour:

- U-ARR-1: ≤ 5s, no scroll, no interaction. **Test:** open the page, look for title + dataset + trust statement; pass if all three are visible without scrolling.
- U-ARR-2: trust banner persistent on scroll. **Test:** scroll the page; pass if banner remains visible.
- U-UND-1: trust state has text + colour + icon. **Test:** screenshot the trust statement; pass if all three signifiers are present and reading-age-appropriate.
- U-NAR-1: filters individually removable with ≤ 300ms feedback. **Test:** apply 3 filters; remove 1; pass if active-filter summary updates and result count animates within 300ms.
- U-NAR-2: applied selects visually distinct from default. **Test:** change one select; pass if the visual state is unambiguously "non-default".
- U-NAR-3: trust badge visible across the result list. **Test:** apply a narrowing; pass if every result row has the trust badge.
- U-COM-1: 60s for first comparison pass + sortable high-frequency columns. **Test:** ask a reviewer to find the most-recently-verified record in a 30-row set; pass if completed under 60s.
- U-COM-2: card/table toggle present, table is default. **Test:** open the page; pass if table view renders by default and toggle is visible in toolbar.
- U-INS-1: drawer opens ≤ 2 interactions, closes 1 interaction, returns to scroll position. **Test:** open + close + verify scroll position.
- U-INS-2: trust banner in drawer header. **Test:** open drawer; pass if banner is present and persistent.
- U-INS-3: Prev/Next in drawer. **Test:** open drawer; pass if navigation works without returning to list.
- U-REC-1: ≤ 1 interaction recovery from any empty state. **Test:** force an empty state via filter combination; pass if Clear-all is visible and returns to non-empty state in 1 click.
- U-REC-2: content-rich empty state. **Test:** force empty state; pass if active filters listed, Clear-all visible, suggestion present.
- U-LEA-1: trust signal consistent across all steps. **Test:** walk the journey end-to-end; pass if no step drops or contradicts the trust state.

Each criterion has a clear pass/fail test. Two evaluators applying these tests to the same v1.1 build reach the same verdicts by construction. The decision gate is satisfied.

---

## Findings carried into Step 5 (the consolidated sheet) and Step 6 (the checklist)

- The 12 criteria in §Step 2 become the canonical UX acceptance-criteria sheet at `design/foundations/ux-acceptance-criteria.md`, with v1.1 UX gates (the must-pass subset) marked.
- The four UX gates and four UX anti-patterns are appended to `design/checklists/master-browser-design-checklist.md` as §20 and §21.
- The user-need audit (Step 3) becomes the canonical record of how each feature is justified; future v1.2+ additions must produce a new row.
- The Lab 01 → Lab 03 gap analysis (Step 4) is the audit trail from heuristic-level findings to criterion-level closures.
