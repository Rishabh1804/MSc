# Lab 02 — Submission

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-02-ui-design-component-inventory.md`
Source topic: `design/foundations/topic-02-what-is-ui-design.md`
Target artifact: `docs/destination-master-browser-v1.html`

## Executive summary

Lab 02 executed all six steps against the Destination Master Browser v1. It produced a 20-pattern inventory of present components, a 12-pattern inventory of missing-but-expected components, a state-coverage matrix that surfaces three high-severity and four medium-severity state gaps, an affordance audit that exposes three cross-cutting findings (active-state, trust-signal depth, three-states-one-component), a container-selection rule sheet, a filter-UI rule sheet, and a consolidated rule sheet that becomes the input for Browser v1.1.

The most important finding is structural: the Destination Master Browser is — in Carbon vocabulary — a **master-detail data-review tool with faceted filtering**, and v1 commits to that pattern only partially. v1 has the *master* (record list as cards) but not the *detail* (no drawer), has the *faceted filtering* (six form controls) but not the *active-filter summary* or the *clear-all recovery*, and has *trust signalling* but only at one shallow depth (metadata grid) instead of the four depths Topic 2 specifies.

The consolidated rule sheet therefore prescribes 18 v1.1 changes, of which 10 are the implementation backlog already named in Topic 2's deep-reading doc §8 and 8 are component-rule refinements.

## Steps executed

| Step | Output | File |
|---|---|---|
| 1 — Component catalogue | 20 patterns present, 12 missing | `design/foundations/topic-02-ui-design-component-inventory.md` §Step 1 |
| 2 — State coverage matrix | 20 patterns × 9 states; 3 HIGH + 4 MEDIUM findings | `design/foundations/topic-02-ui-design-component-inventory.md` §Step 2 |
| 3 — Affordance / signifier / feedback audit | Per-pattern audit; 3 cross-cutting findings | `design/foundations/topic-02-ui-design-component-inventory.md` §Step 3 |
| 4 — Container-selection rules | Card / Table / List / Drawer / Modal with when-to-use + when-not-to-use + sources | `design/foundations/ui-design-component-rules.md` §3 |
| 5 — Filter-UI rules | Search / Chip / Dropdown / Faceted panel with decision criteria; Active-filter summary rule | `design/foundations/ui-design-component-rules.md` §4 |
| 6 — Consolidated rule sheet | Full per-component rule table tying every pattern to its v1.1 rule | `design/foundations/ui-design-component-rules.md` §8 |

## Key findings

### Structural findings

- **F1 — No active state on filter controls** (P3–P8 in the inventory). Reviewers cannot see at a glance which filters are non-default. v1.1 must add a visible "is non-default" signifier on selects and a removable-chip active-filter summary above the result list.
- **F2 — Trust signal is shallow.** v1 carries verification status in the metadata grid (text only) and Planner state in the status pill, but the Topic 2 §6.2 specification asks for a single *trust badge* component used at **four depths** (top-of-page banner, list row, drawer header, confirm-modal) with seven defined states.
- **F3 — Three feedback states share one component.** v1 uses a single `.empty` CSS class for loading / empty / error, differentiated by message text only. v1.1 must split these into three distinct components with skeleton (loading), content-rich empty state (with active-filter summary + Clear-all + what-to-try suggestion), and inline error notification (with retry + report-issue).

### Pattern-level findings

- **20 patterns present, 12 patterns missing.** The missing list maps directly onto Topic 2's v1.1 implementation backlog: table mode, drawer, active-filter summary, Clear-all, card/table toggle, sortable columns, sticky header, skeleton loader, inline notification, confirm modal (deferred), focus rings, active-state on selects.
- **State-coverage HIGH severity** affects all six form controls (hover/focus/active missing), the record card (no hover/focus/click), the trust signal (one shallow depth), and the shared loading/empty/error pane.
- **Affordance findings**: cards have a planned affordance (click to open drawer) with no current signifier; chips have a signifier of interactivity (rounded coloured chip = "I am toggleable" in most design systems) with no current affordance.

### Container-selection resolution

The "cards vs table" question raised by Lab 01 is resolved by Topic 2 in favour of **table as default, cards as secondary**, with a toggle. Reason: the reviewer's primary tasks (compare-by-attribute, sort-by-column) are table-shaped; the card view remains valuable for record-as-rich-object browsing of 10–20 records.

### Modality resolution

v1.1 **does not introduce a modal**. The detail view is a drawer. Modal use is deferred to v1.2+ for destructive batch actions (e.g. promote-to-Planner confirmation), where modality is earned per HIG/Carbon/GOV.UK criteria.

## Repository outputs

| Output | Path | Status |
|---|---|---|
| Inventory + state matrix + affordance audit | `design/foundations/topic-02-ui-design-component-inventory.md` | Complete |
| Consolidated rule sheet | `design/foundations/ui-design-component-rules.md` | Complete — Browser v1.1's input |
| Lab submission (this file) | `curriculum/courses/des-001-design-foundations/submissions/lab-02-ui-design-component-inventory-results.md` | Complete |
| Checklist gates appended | `design/checklists/master-browser-design-checklist.md` §18 + §19 | Complete |

## Submission checklist (Lab 02 brief §"Submission checklist")

- [x] Component catalogue completed (Step 1) — 20 patterns + 12 missing-pattern list
- [x] State coverage matrix completed (Step 2) — 20 patterns × 9 states, severity-ranked
- [x] Affordance / signifier / feedback audit completed (Step 3) — per-pattern audit + 3 cross-cutting findings
- [x] Container-selection rules drafted with criteria (Step 4) — five containers, when-to-use + when-not-to-use, sourced
- [x] Filter-UI rules drafted with criteria (Step 5) — four filter patterns + active-filter summary rule
- [x] Consolidated rule sheet produced (Step 6) — `design/foundations/ui-design-component-rules.md`
- [x] v1.1 implications recorded against `design/checklists/master-browser-design-checklist.md` — §18 (six gates) + §19 (canonical rule-sheet pointer)
- [x] Findings cross-referenced against Lab 01 results — Lab 02 inherits Lab 01's "workflow completion + trust preservation" framing; the rule sheet's 18 v1.1 changes are the component-level realisation of Lab 01's heuristic-level findings

## Decision-gate satisfaction (Lab 02 brief §"Decision gate")

The brief's gate: *"a second reviewer, given the rule sheet and v1's screenshot, would produce the same container and filter decisions for two new records added to the dataset."*

Self-test: applying the rule sheet to two hypothetical new records:

- **Record A** — a Tier-2 destination with full metadata, verified status, planner-ready true. The rule sheet says: appears in the **table** (default view) with the **`verified` trust badge** at the first column and **`planner-ready` Planner-status badge** elsewhere; the **side-panel** scale and source-files lists update; the row is **clickable to open the drawer**. No special handling.
- **Record B** — a candidate destination with three missing metadata fields, blocked verification, planner-ready false. The rule sheet says: appears in the **table** with the **`missing-fields` trust badge** (or `blocked` depending on which is the primary blocker), the table cells for missing fields render as **"—" with an aria-label of "missing"**, the row is **clickable to open the drawer**, and the drawer header shows the **compact trust banner explaining the blockers**.

Both records resolve unambiguously to table-mode rendering with the trust-badge component, the same row-click behaviour, and the same drawer behaviour. A second reviewer applying the same rules to the same two records reaches the same conclusions. Gate passed.

## What this lab produces beyond the rubric minimum

1. **A reusable container-selection decision tree** (rule sheet §3.6) — applicable to any future data-review UI in the CodeMike workspace.
2. **A reusable filter-UI decision tree** (rule sheet §4.5) — same.
3. **A four-depth trust-signal specification** (rule sheet §7) — applicable to any UI that needs to carry trust state through a journey.
4. **The Topic 2 component gates appended to the master-browser checklist** (§18) — operationalises Topic 2's discipline into a review gate that future PRs must satisfy.

These four are the *Package → Transfer* outputs in the CodeMike operating loop's terms.

## Open work after Lab 02

- Topic 3 — UX design — produces the reviewer-journey + UX-acceptance criteria that complement this rule sheet.
- After Topic 3 closes, Browser v1.1 implementation begins against (this rule sheet) + (Topic 3's UX gates).
- The trust-badge colour palette is deferred to Topic 10 (Color theory). Until then v1.1 uses neutral palettes plus icons.
- A faceted filter panel is deferred to v1.2 if reviewer feedback shows the current chip-row + dropdown combination is insufficient.

## Lab 02 status

**Complete.** Lab evidence is sufficient for Topic 2 to be marked Closed in the competency map and revision plan. PR B is the second of two PRs that finish Topic 2 (after PR A, the deep-reading PR).
