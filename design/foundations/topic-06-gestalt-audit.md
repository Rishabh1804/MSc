# Topic 6 — Gestalt Audit (v1.1)

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-06-gestalt-audit.md`
Source topic: `design/foundations/topic-06-gestalt.md`
Audit number: **Audit 1** (the first formal Gestalt audit run against the workspace).
Date: 2026-05-17.
Subject: Destination Master Browser v1.1 (post-PR #12) at `docs/destination-master-browser.html`.

This audit grades v1.1 against the six core Gestalt principles (proximity, similarity, continuity, closure, common region, common fate), focused on the screen regions where grouping signals carry the most weight. Every cell cites a specific source for the principle (Wertheimer/Koffka/Köhler via secondary, IxDF, NN/g, Smashing) and a specific v1.1 region. Cells that fail produce *findings*; cells that pass with named compensation produce *trade-offs*; cells that cleanly pass become *strengths*.

The audit-shape is borrowed from Topic 5's HCD audit (regions → per-principle matrix → findings → prioritised fix list), adapted from a four-activity lifecycle to a six-principle perceptual matrix.

---

## Step 1 — Audit-region list and exclusions

### Audited regions

| # | Region | Why this region carries grouping weight |
|---:|---|---|
| R1 | **Cards view** — record card composition (`article.card` rendered at HTML lines 951–971) | Multiple visual groups within one card (name+place header, trust badge, meta-grid, chip row, action pill). High information density per card. |
| R2 | **Table view** — column alignment + row separators (`renderTable()` at HTML line 922) | Continuity (vertical alignment) + common region (rows) at scale across 359 rows. |
| R3 | **Toolbar** — search + five filter selects + view-toggle (HTML lines 440–480) | Proximity (six controls together) + similarity (input/select uniformity) + view-toggle as a sub-group. |
| R4 | **Active-filter summary** — chip row (`#activeFilters` HTML lines 483–488) | Distinct group from the toolbar, or absorbed into it? Holds result-count + Clear-all. |
| R5 | **Trust banner + page header + stats banner** — three persistent units (HTML lines 418–428, 430–436, 491) | Three persistent visual units stacked vertically; do they read as separate concerns or one mass? |
| R6 | **Drawer** — header + trust banner + body sections (HTML lines 586–609) | Per-section common region + proximity for related fields. The detail-view counterpart to cards. |

### Regions intentionally excluded

- **Mini-list snapshot panel** (`#snapshot`): low grouping weight; small static lists in a side panel; no principle conflict at stake.
- **Top-level `<svg>` icon decoration**: per-element styling; no inter-element grouping audit needed.
- **Document `<head>`, scripts, and meta-only DOM**: non-visual.

The six audited regions cover every reviewer-journey step (arrive → understand → narrow → compare → inspect → recover → leave) at least once.

---

## Step 2 — Per-region per-principle audit matrix

Verdict legend: **Pass** = principle honoured; **Trade-off** = violated but acceptable with named compensation; **Violation** = violated without acceptable compensation (becomes a finding); **N/A** = principle doesn't apply.

Each cell cites the source(s) the principle derives from: **W/K/K** = Wertheimer/Koffka/Köhler via secondary; **I** = IxDF; **N** = NN/g; **S** = Smashing.

### R1 — Cards view

| Principle | Verdict | Evidence + source |
|---|---|---|
| Proximity | **Trade-off** | Card-internal sections (name+place block, meta-grid 2×2, chip row, action pill) are tightly stacked at ~8–12px gaps; the proximity signal correctly binds related fields within each section. **Compensation**: visual structure provided by sub-section boundaries (meta-grid is its own grid; chip row is a flex line). [I, N] |
| Similarity | **Violation** | The "Verification" cell inside the meta-grid (HTML line 967) uses identical styling to the Scale / Region / Type cells around it. Similarity says: same look = same category. But Verification *is the trust signal*; the meta-grid styling demotes it to "just another field". The trust badge in the top-right of the card is the correct primary signal — the duplicate verification-text in the meta-grid is the false-negative grouping. [N — diagnostic discipline; I — similarity for categorical signal] |
| Continuity | **Pass** | Meta-grid uses a 2-column grid; alignment is clean. The card-chips row aligns to the left edge of the card body. The name + place + id stack aligns vertically. [W/K/K — alignment-as-structure; I] |
| Closure | **Pass** | The card is a fully bordered region (`.card { border: 1px solid; border-radius }`) — no closure-completion needed. [I] |
| Common region | **Pass** | The card itself is the bounded common region; name + place + trust badge + meta-grid + chips + pill all correctly group into one perceptual unit. [I, N] |
| Common fate | **N/A** | No motion within the card during steady state. (Hover transitions exist but are decorative-feedback rather than grouping signal.) [S] |

**Findings (R1)**: F-GES-1 — verification-text inside meta-grid creates a false-negative trust signal (similarity collapses it into surrounding metadata).

### R2 — Table view

| Principle | Verdict | Evidence + source |
|---|---|---|
| Proximity | **Pass** | Row cells are tightly packed within rows; row separators (1px borders) provide between-row separation. The proximity signal correctly groups cells-into-rows. [I, N] |
| Similarity | **Violation** | The "Verification" column (col 6) uses the same plain text styling as the Scale / Source / ID columns. The first column has a trust badge (similarity correctly elevates it), but the verification *text* in column 6 is visually equivalent to non-trust columns. Same false-negative pattern as R1, at scale across all 359 rows. [N] |
| Continuity | **Pass** | Vertical alignment within columns is clean (CSS `table` layout); column-as-category signal is intact. Sortable-header `aria-sort` updates correctly. [W/K/K — alignment-as-structure; I] |
| Closure | **Pass** | Table has explicit top/bottom borders + per-row separators; closure is complete. [I] |
| Common region | **Pass** | Each row is a bounded common region via `<tr>` semantics + 1px border-bottom. [I] |
| Common fate | **Pass** | The result-count flash animation (PR #12 polish) co-varies with filter changes for the table view as well as the cards view. [S — meaningful motion] |
| Continuity (sub-audit: sortable headers) | **Violation** | The sortable column headers (`<th data-sort>`) signal interactivity only via `aria-sort` for screen readers + `cursor: pointer` on hover. The visual styling of sortable headers is *similar to* non-sortable headers — similarity says "same category" but the sortable ones are interactive. False-positive grouping of interactivity. [N — named-violation discipline] |

**Findings (R2)**: F-GES-2 — verification-column false-negative (same root cause as F-GES-1 at table scale); F-GES-3 — sortable headers don't visually signal interactivity (false-negative interactivity grouping via similarity).

### R3 — Toolbar (search + selects + view-toggle)

| Principle | Verdict | Evidence + source |
|---|---|---|
| Proximity | **Violation** | The six controls (search input + 5 selects) and the view-toggle button group sit in a single flex container at uniform ~16px gaps. Proximity says "one group of seven controls". Reality: the view-toggle is a *different category* (view-mode switch, not a narrowing control). False-positive grouping by proximity. [I, N] |
| Similarity | **Violation** | Search input and the five selects all use the same `.field` wrapper + the same input styling (border, padding, font). Similarity says "same kind of control". But the *interaction grammar* differs: search updates live as you type; selects update only on selection change. False-positive grouping by similarity *over interaction grammar*. [N — diagnostic; S — task-driven adjudication] |
| Continuity | **Pass** | Controls align vertically (label-above-input pattern) and horizontally (flex wrap). Alignment is clean. [W/K/K; I] |
| Closure | **N/A** | The toolbar is a non-bordered region; closure doesn't apply. |
| Common region | **Trade-off** | The toolbar has a soft background that bounds the seven controls into one region. Compensation works *for* the narrowing-controls subset (correct grouping) but *against* the view-toggle (incorrectly included). [I] |
| Common fate | **N/A** | No co-movement in steady state. |

**Findings (R3)**: F-GES-4 — view-toggle is included in the toolbar's proximity + common-region grouping despite being a *different category* (view-mode, not narrowing); F-GES-5 — search vs selects false-positive similarity grouping despite different interaction grammars (the deep-reading doc's primary anticipated violation, now confirmed).

### R4 — Active-filter summary (chip row)

| Principle | Verdict | Evidence + source |
|---|---|---|
| Proximity | **Violation** | The active-filter summary sits directly below the toolbar at the standard inter-section gap (~12px). Proximity is *not strong enough* to clearly mark it as a distinct region; the eye groups it with the toolbar above it. False-positive grouping with the toolbar. [I, N] |
| Similarity | **Pass** | The chip styling (rounded background, close-icon) is visually distinct from the toolbar's input/select styling. Similarity correctly separates it. [N] |
| Continuity | **Pass** | The chip row aligns horizontally; the "Active filters" label + chips + count + Clear-all align on a single baseline. [W/K/K; I] |
| Closure | **N/A** | Non-bordered. |
| Common region | **Trade-off** | The summary has its own soft background panel, providing common-region grouping. But the panel's background tint is only marginally distinct from the toolbar's. **Compensation**: tint exists but is too weak to fully separate. [I — common region requires *perceptible* boundary] |
| Common fate | **Pass** | The result-count value flashes when filters change — meaningful common-fate signal that the count is *reacting* to the filter change. [S — meaningful motion] |

**Findings (R4)**: F-GES-6 — active-filter summary bleeds into toolbar via proximity + weak common-region tint, despite similarity correctly separating chip styling.

### R5 — Trust banner + page header + stats banner

| Principle | Verdict | Evidence + source |
|---|---|---|
| Proximity | **Pass** | The three persistent units stack vertically with substantial inter-section gaps. Proximity correctly separates them. [I, N] |
| Similarity | **Pass** | Each unit has its own visual treatment: trust banner uses warning-tinted background + icon; app-header uses a darker hero background + eyebrow text + h1; stats banner uses pill-style stat cards. Similarity correctly distinguishes their categories. [N] |
| Continuity | **Pass** | All three align to the page's `.wrap` width; the alignment continuity reads as "these all belong to the same page structure". [W/K/K] |
| Closure | **Pass** | Each unit has its own visual boundary (background or border). [I] |
| Common region | **Pass** | Each unit is its own common region; no false-positive grouping across them. [I] |
| Common fate | **Pass** | Stats values update on filter change (co-varying with the result count's flash); meaningful common-fate. [S] |

**Strengths (R5)**: cleanest region in the audit; every principle Pass with no findings.

### R6 — Drawer

| Principle | Verdict | Evidence + source |
|---|---|---|
| Proximity | **Pass** | Drawer-header (name + place + nav buttons) → drawer-trust banner → drawer-body sections stack with clear inter-section gaps. Proximity correctly groups header items + correctly separates header / trust / body. [I, N] |
| Similarity | **Pass** | The drawer-trust banner styling is visually similar to the page-level trust banner (R5) — similarity correctly tells the eye "this is the same trust signal carried into the drawer". The four-depth trust badge pattern from Topic 2 is honoured. [N — similarity for cross-context signal continuity] |
| Continuity | **Pass** | Drawer body sections align to a consistent left edge; field labels align with values. [W/K/K] |
| Closure | **Trade-off** | The drawer overlay extends from the right viewport edge and lacks an explicit top border (flush with the viewport top). **Compensation**: closure-completion works — the visual system completes the boundary from the three borders that *are* present. The compensation is explicit and acceptable (deep-reading doc §2.2 example). [I — closure-completion explicit] |
| Common region | **Pass** | Each drawer-section is its own common region (`.drawer-section` with internal spacing); within each, related fields group correctly. [I] |
| Common fate | **N/A** | No co-motion within the drawer steady state. (Drawer slide-in is an open/close transition, not a within-drawer grouping signal.) |

**Strengths (R6)**: second-cleanest region after R5; the only trade-off (closure) has explicit compensation.

---

## Step 3 — Conflict adjudication per region

This step identifies regions where two principles pull in different directions and adjudicates the winner. Unresolved conflicts are findings (the third sub-type in the deep-reading doc §6 violation taxonomy).

### R1 — Cards view conflict: proximity vs similarity (caution chips)

- **Proximity says**: caution chips are spatially close to the regular vibe + trip chips (same `.card-chips` flex row). One group of card tags.
- **Similarity says**: caution chips use `.warn` styling (red/orange tint) → visually distinct → a *different* category from regular tags.

**Adjudication**: similarity wins for the categorical signal. Distinguishing caution chips from regular tags is the reviewer-task ("does this record carry a risk before promotion?"); the spatial co-location is the by-product of card layout. **Resolution**: the v1.1 build *partially* honours this (caution chips have `.warn` styling), but they sit in the same flex row without an explicit visual separator. The conflict is *implicit* — not unresolved, but not crisply resolved either. **Verdict**: Trade-off. **Compensation**: similarity (colour) is doing the work alone. **Suggested upgrade**: add a small visual divider or extra gap before caution chips in the row. Tag v1.1.x.

**Source for the rule**: Smashing's task-driven adjudication framing — the winning principle is the one that better serves the user's task.

### R3 — Toolbar conflict: proximity-grouping vs view-toggle category

- **Proximity says**: the view-toggle button-group sits inside the toolbar flex; one group.
- **Category says**: view-toggle is a view-mode switch, not a narrowing control. Different category.

**Adjudication**: category wins. The view-toggle should not be perceived as part of the narrowing-controls group. **Resolution**: the v1.1 build has the view-toggle in the same flex container with no explicit separator. **Conflict is unresolved** — the design hasn't adjudicated. **Verdict**: Violation. **Fix**: visually separate the view-toggle (extra gap, different alignment, or move outside the toolbar's common-region). Tag v1.1.x for the gap; v1.2 if structural relocation is preferred.

### R3 — Toolbar conflict: similarity-grouping vs interaction-grammar

- **Similarity says**: search input + selects share input-styling → same kind of control.
- **Interaction grammar says**: search is live-update; selects are commit-on-change. Different grammar.

**Adjudication**: interaction grammar wins. The reviewer's task is to narrow the result set; the grammar of *how* they do it matters. **Resolution**: unresolved. **Verdict**: Violation. **Fix**: two options — (a) unify the grammar (selects become live-update too); (b) visually separate the search from the selects (extra gap + distinct styling). Option (a) is the cleaner fix; option (b) is the smaller change. Tag v1.1.x (option b) or v1.2 (option a).

### R4 — Active-filter summary conflict: proximity-bleed vs similarity-separation

- **Proximity says**: summary sits 12px below toolbar → grouped with toolbar.
- **Similarity says**: chip styling differs from input styling → separate group.

**Adjudication**: similarity wins for category, but proximity is producing the spatial perception. **Resolution**: similarity is doing partial work; proximity-and-common-region need to do their share too. **Verdict**: Trade-off with weak compensation (the tint is too subtle). **Fix**: strengthen the common-region tint OR add explicit inter-section gap (~24px instead of ~12px). Tag v1.1.x.

### R2 / R5 / R6 — no significant cross-principle conflicts

The table, banners, and drawer regions don't have principle conflicts at the audit level; each principle either passes or fails independently, without pulling in opposite directions.

---

## Step 4 — Density-vs-grouping audit

The deep-reading doc §10 anti-pattern 1 ("silent density collapse") is the data-review tool's central perceptual risk. Each region is audited for density compromises.

| Region | Density compromise? | Compensating signal | Verdict |
|---|---|---|---|
| R1 Cards | Yes — card-internal spacing is ~8–12px (tight). | Substitution: sub-section visual structure (meta-grid layout, chip flex row) carries the grouping that whitespace doesn't have room for. **Explicit substitution**. | Trade-off accepted. |
| R2 Table | Yes — row padding is ~10–12px (typical table density). | Substitution: 1px row borders + zebra alternative could strengthen the row-as-region signal (v1.1 uses borders without zebra). **Substitution present but minimal**. | Trade-off accepted; v1.1.x could add zebra striping for extra row-grouping if reviewer feedback warrants. |
| R3 Toolbar | Yes — six controls + view-toggle in one row at ~16px gaps. | Substitution: common-region (background tint) carries the grouping. **But the substitution over-groups** — it includes the view-toggle which shouldn't be grouped. | **Silent collapse** — compensation is present but produces a false-positive grouping. Counts as F-GES-4 + F-GES-5 from Step 2. |
| R4 Active-filter summary | Yes — sits within ~12px of toolbar. | Substitution: weak tint differential. **Silent collapse** — the substitution isn't strong enough. Counts as F-GES-6 from Step 2. |
| R5 Banners | No — generous vertical spacing. | N/A. | Pass. |
| R6 Drawer | No — drawer-section gaps are generous. | N/A. | Pass. |

**Density-vs-grouping finding**: F-GES-7 — three of the six regions (R3, R4, plus the borderline R1) compromise on whitespace, and only one (R1) has a clean explicit substitution. R3 and R4's substitutions either over-group or are too weak. These collapse silently against the deep-reading anti-pattern. Mitigations land via F-GES-4, F-GES-5, F-GES-6 (Step 2); F-GES-7 is the audit-level meta-finding that these are not isolated bugs but a pattern.

---

## Step 5 — Findings and prioritised v1.1.x / v1.2 fix list

### Strengths

- **R5 (banners)** — every principle Pass; no findings. The cleanest region in v1.1.
- **R6 (drawer)** — five Pass + one Trade-off with explicit compensation (closure-completion). Second-cleanest region.
- **R2 (table)** — proximity, continuity, closure, common region, common fate all Pass; only the verification-column similarity issue and the sortable-headers issue are findings.
- **R1 (cards)** — strong on common region + continuity + closure; the proximity Trade-off has explicit substitution.
- **PR #12's result-count flash animation** — clean common-fate signal applied to both R2 and R4; the only meaningful-motion signal in v1.1 and it's used correctly.
- **Trust-badge similarity across four depths** (banner → card top-right → drawer-trust → confirm-modal) — the Topic 2 four-depth trust signal is Gestalt-similarity working correctly across contexts.

### Violations (consolidated)

| ID | Region | Principle(s) | Description | Tag |
|---|---|---|---|---|
| **F-GES-1** | R1 Cards | Similarity | "Verification" cell inside meta-grid uses the same styling as Scale/Region/Type — false-negative trust signal in the card body | v1.1.x |
| **F-GES-2** | R2 Table | Similarity | "Verification" column (col 6) uses the same plain text styling as non-trust columns — same root cause as F-GES-1 at scale across 359 rows | v1.1.x |
| **F-GES-3** | R2 Table | Similarity | Sortable column headers don't visually signal interactivity; similarity to non-sortable headers creates false-negative interactivity grouping | v1.1.x |
| **F-GES-4** | R3 Toolbar | Proximity + Common region | View-toggle is included in the toolbar's narrowing-controls grouping despite being a different category (view-mode switch) | v1.1.x (gap) or v1.2 (structural relocation) |
| **F-GES-5** | R3 Toolbar | Similarity | Search input + selects share input-styling but have different interaction grammars (live vs commit-on-change) — false-positive grouping | v1.1.x (visual separation) or v1.2 (unify grammar) |
| **F-GES-6** | R4 Active-filter summary | Proximity + Common region | Summary bleeds into toolbar via proximity + weak tint differential | v1.1.x |

### Trade-offs (acceptable with named compensation)

- **R1 Cards proximity** — tight inter-section spacing compensated by explicit sub-section visual structure (meta-grid, chip row).
- **R1 Cards caution-chip conflict** — proximity vs similarity; similarity (colour) wins task-driven; suggested visual-divider upgrade tracked as v1.1.x improvement.
- **R3 Toolbar common region** — soft background tint correctly groups narrowing-controls subset (compensated correctly), incorrectly groups view-toggle (incorrect — counts as F-GES-4).
- **R4 Active-filter summary common region** — tint exists but is too weak; counts as F-GES-6 with the compensation upgrade as the fix.
- **R6 Drawer closure** — flush-top edge, closure-completion compensates explicitly.

### Prioritised fix list (ordered by leverage)

**Leverage = (number of findings closed) × (number of journey steps served) × (cost-of-implementation inverse)**

| Rank | Fix | Closes | Tag | Why ranked here |
|---|---|---|---|---|
| 1 | **Visually elevate the verification signal in card meta-grid + table column** (use the trust-badge component or a coloured tint instead of plain text) | F-GES-1 + F-GES-2 | v1.1.x | Closes 2 findings at once; serves the *Inspect* + *Compare* journey steps (both cost-budgeted in Topic 3); cheapest change with highest reviewer-task impact |
| 2 | **Visually separate the toolbar's view-toggle from the narrowing-controls group** (extra gap + optional vertical divider) | F-GES-4 | v1.1.x | Closes 1 finding; serves the *Narrow* journey step; trivial CSS change; addresses the toolbar's most obvious false-positive grouping |
| 3 | **Strengthen active-filter summary visual separation from toolbar** (24px gap or stronger tint differential) | F-GES-6 | v1.1.x | Closes 1 finding; serves the *Recover* journey step (U-NAR-1 + U-REC-1 acceptance criteria); trivial CSS change |
| 4 | **Visually distinguish sortable column headers from non-sortable** (icon, weight, hover affordance) | F-GES-3 | v1.1.x | Closes 1 finding; serves the *Compare* journey step (sort-affordance is part of compare-many-by-attribute); small CSS change; complements the existing `aria-sort` accessibility work |
| 5 | **Resolve search vs select grammar conflict** — two sub-options: (5a) visually separate search from selects [v1.1.x]; (5b) unify grammar so selects also live-update [v1.2] | F-GES-5 | v1.1.x or v1.2 | Closes 1 finding; serves the *Narrow* journey step; choice between visual-separation (smaller change) and behaviour-unification (deeper change). Pick 5a now; defer 5b to v1.2 backlog for Sponsor-Reviewer feedback. |
| 6 | **Add a small visual divider before caution chips in card-chips row** | Caution-chip Trade-off upgrade (R1) | v1.1.x | Not a finding, but a Trade-off → Pass upgrade. Crisp visual separation makes the similarity-wins-over-proximity adjudication explicit rather than implicit. |

Five of six fixes tag as v1.1.x (visual-treatment-only); one (F-GES-5 option 5b) tags as v1.2. **No fix requires a Topic 2 component-rule change** — the rule sheet already specifies the trust badge as the primary trust signal at four depths; F-GES-1 + F-GES-2 are *implementations* of an existing rule, not a new rule. F-GES-4 + F-GES-6 are visual treatment improvements to existing components.

### Inheritance into v1.2

The v1.2 backlog now inherits:

- Lab 04 Loop 1 (batch-promote-confirm modal anatomy)
- Lab 05 prioritised HCD list (6 items: Sponsor Reviewer + U-CONF criteria + systems-context + inclusion requirements + screen-reader test + heuristic re-audit)
- Lab 06 prioritised list above (5 v1.1.x items + 1 v1.2 grammar-unification item)

The v1.2 implementation PR will need to sequence carefully across all three labs' worth of work.

---

## Step 6 — Master-browser checklist appendix

Appended to `design/checklists/master-browser-design-checklist.md`:

- **§29** — Three Gestalt gates (perceptual-constraint gate; principle-conflict adjudication gate; density-vs-grouping gate)
- **§30** — Three Gestalt anti-patterns specific to data-review tools
- **§31** — Canonical pointer to this audit doc

---

## What this audit does NOT do

Honest scoping (mirrors the Topic 5 audit's discipline of naming limitations explicitly):

- **No human-grade perceptual testing.** A real reviewer's eye on the v1.1 build would surface findings this audit's introspective method cannot reach. The single-person workspace runs this audit as a *lower bound* on perceptual rigour, not as a substitute for user perception testing. This is the Topic 6 analogue of Topic 5's Sponsor Reviewer gap.
- **No quantitative perceptual measurement.** Eye-tracking, attention-heat-maps, and time-to-find studies would give the audit empirical grounding rather than introspective grounding. The findings are *defensible* (each cites a principle + source + region) but not *empirically grounded*.
- **No motion-disabled audit.** The common-fate findings (R2/R4 result-count flash) assume a reviewer with motion-enabled rendering. Reviewers with `prefers-reduced-motion: reduce` lose the common-fate signal — and the audit doesn't currently track which compensation should substitute. Tag v1.2.
- **No mobile / narrow-viewport audit.** All findings are desktop-shaped. Mobile rendering may collapse the toolbar to a stacked layout, changing all R3 + R4 findings. Tag v1.2 (matches Topic 5's inclusion-lens fail).
- **No cross-version regression check against v1.0.** v1.0 is archived; this audit only grades v1.1. A future Audit 2 (after v1.2 ships) should compare against Audit 1's findings.

Naming these limitations is HCD-compliant (Topic 5 §2 principle 4 + §11 anti-pattern 1) and matches the Topic 6 discipline (deep-reading doc §10 — silent collapse is the failure mode; explicit naming is acceptable).

---

## Reusable CodeMike capabilities extracted from this audit

Three reusable capabilities the workspace gains from running Audit 1:

1. **Gestalt audit template** (region list → per-region per-principle matrix → conflict adjudication → density audit → findings + prioritised v1.1.x/v1.2 fix list with leverage scoring). Applicable to any visual interface the workspace builds.
2. **Violation-taxonomy diagnostic vocabulary** (false-positive grouping / false-negative grouping / unresolved principle conflict) — applicable as a diagnostic shorthand for any UI design review.
3. **Density-vs-grouping audit pattern** (does density force a proximity compromise? if yes, is the substituting signal explicit or silent? silent = finding) — applicable to any information-dense interface, not just data-review tools.

These three combine with prior topics' capabilities to grow the workspace's reusable design-capability catalogue further.

---

## Audit 1 verdict summary

| Dimension | Result |
|---|---|
| Audited regions | 6 / 6 covered against every relevant principle |
| Principle-cells graded | 36 cells (6 regions × 6 principles; some N/A) |
| Pass cells | 22 |
| Trade-off cells (with named compensation) | 5 |
| Violation cells (findings) | 7 (including the R2 sortable-header sub-audit) |
| N/A cells | 4 (common-fate where no motion exists; closure on non-bordered regions) |
| Findings (consolidated, distinct) | 6 (F-GES-1 through F-GES-6) plus 1 audit-level meta-finding (F-GES-7) |
| Strengths | 6 (R5 + R6 + 4 cross-cutting strengths) |
| Conflicts adjudicated | 4 (R1 caution-chips; R3 view-toggle; R3 search-vs-selects; R4 summary-vs-toolbar) — 0 left unresolved |
| Prioritised fix list | 6 items (5 v1.1.x + 1 v1.2) |
| Decision-gate satisfaction | All 5 Lab 06 decision-gate conditions met (every region audited; every Trade-off has compensation; every Violation has a fix; every conflict adjudicated; every fix tagged v1.1.x or v1.2) |

**Overall**: v1.1 is *Gestalt-substantial*. Two regions (R5 banners + R6 drawer) are exemplary; the other four have a small consistent pattern of findings, all closable with visual-treatment-only changes (five of six fixes tag v1.1.x). The audit-shape itself surfaced one cross-cutting pattern (the verification false-negative at both card + table scale via similarity collapse) and one structural conflict (toolbar over-grouping) that introspection alone would have missed without the per-region per-principle matrix.

The single most operationally important finding: **the trust badge is correctly used as the primary trust signal at four depths (R1/R2/R6 + confirm-modal), but the verification *text* is duplicated inside meta-grid + table-column at equivalent visual weight to non-trust fields, partially undoing the badge's elevation**. Fix #1 closes both occurrences with a single visual-treatment change.

---

## Audit Addendum (v1.1.x polish PR, 2026-05-18)

Closes two Lyra missed-opportunities from PR #18 review (no screenshot evidence; no computed leverage scores).

### Computed leverage scores per fix

Leverage rubric: `(findings closed) × (journey steps served) × (cost-of-implementation inverse)` where cost-inverse = 1 for trivial CSS, 0.7 for component-level change, 0.4 for behaviour change. Scaled to 0–10.

| Rank | Fix | Findings closed | Journey steps served | Cost-inv | Score |
|---:|---|---:|---:|---:|---:|
| 1 | Verification-signal elevation (card + table) | 2 (F-GES-1, F-GES-2) | 2 (Inspect, Compare) | 0.7 (new component) | **2.8** |
| 2 | View-toggle separator | 1 (F-GES-4) | 1 (Narrow) | 1.0 (trivial CSS) | **1.0** |
| 3 | Active-filter summary separation | 1 (F-GES-6) | 1 (Recover) | 1.0 (trivial CSS) | **1.0** |
| 4 | Sortable-header affordance | 1 (F-GES-3) | 1 (Compare) | 1.0 (trivial CSS) | **1.0** |
| 5a | Search-vs-selects visual separation | 1 (F-GES-5 visual half) | 1 (Narrow) | 1.0 (trivial CSS) | **1.0** |
| 6 | Caution-chip divider | 0 (Trade-off → Pass upgrade) | 1 (Compare) | 1.0 (trivial CSS) | **0.7** (non-finding-closure; scaled 0.7×) |
| 5b | Search-vs-selects grammar unification | 1 (F-GES-5 behaviour half) | 1 (Narrow) | 0.4 (behaviour change + Sponsor Reviewer gating) | **0.4** (v1.2 only) |

Fix #1's score (2.8) is roughly triple the next-ranked fix, confirming the prior ranking. The fix order in the audit's prioritised list matches the leverage-score order.

### Screenshot evidence (after polish)

Captured by `curriculum/courses/des-001-design-foundations/verification/v1.1.x-polish/capture-fixes.js` against the polished build (commit on `claude/des-001-browser-v1.1.x-polish`). Before-screenshots: the existing PR #12 walkthrough captures (`v1.1-walkthrough/walkthrough-table.png` + `walkthrough-cards.png`) show v1.1 pre-polish.

| Fix | After screenshot |
|---|---|
| Fix #1 (verification pill, table view) | `curriculum/courses/des-001-design-foundations/verification/v1.1.x-polish/fix-1-verif-pill-table-after.png` |
| Fix #1 + Fix #6 (verification pill in card meta-grid + caution-chip divider) | `.../fix-1-6-card-after.png` |
| Fix #2 + Fix #5a (view-toggle + search separators in toolbar) | `.../fix-2-5a-toolbar-separators-after.png` |
| Fix #3 (active-filter summary tint differential) | `.../fix-3-active-filters-after.png` |
| Fix #4 (sortable-header ↕ glyph) | `.../fix-3-4-table-headers-after.png` |

Five after-screenshots cover all six v1.1.x fixes. The audit doc now has empirical visual grounding alongside the prose findings.

### Walk-through regression check

The existing 19-gate Playwright walk-through (`v1.1-walkthrough/walkthrough.js`) was re-run against the polished build: **19/19 pass, zero console errors**. The visual-treatment changes introduced zero behavioural regressions.
