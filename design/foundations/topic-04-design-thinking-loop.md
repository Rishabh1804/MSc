# Topic 4 — Design Thinking Loop 1 (Worked example)

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-04-design-thinking-loop.md`
Source topic: `design/foundations/topic-04-design-thinking.md`
Loop number: **Loop 1** (the first time the workspace runs design thinking against the Destination Master Browser).
Date: 2026-05-17.

This is a single loop run end-to-end with evidence at every stage. The discipline isn't tested by the *result* — it's tested by whether every stage produced a tangible artifact and whether the Test specification includes falsification criteria. Both tests should be visible below.

---

## Step 1 — Pain-point choice

### Choice

**Confirm modal for destructive batch actions** — specifically: *promote-N-records-to-Planner-with-confirm-and-undo*.

### Rejection rationale for two alternatives

| Alternative considered | Why rejected for Loop 1 |
|---|---|
| **Collapsible filter panel** | Sized fine for one loop, but the underlying need is *less ambiguous* than batch actions — reviewers can already see the chip-row + dropdown combination is functional in v1.1. Belongs to a later loop when filter UX has been observed under load. |
| **Faceted filter panel** | Too large for one loop. A faceted-filter design opens questions about facet hierarchy, multi-select semantics, and cross-facet interactions. Sized at Loop 3+ once the workspace has more reviewer evidence. |

The chosen pain-point (batch-promote-with-confirm) is sized right: one decision-shaped problem, several plausible candidates, real consequence (destructive action against the master CSV), no upstream blockers other than the data-model question (which the loop itself will surface).

---

## Step 2 — Empathize (3-perspective synthesis)

Single-person workspace; using the three-persona synthesis substitute per the deep-reading doc §11 anti-pattern 3.

### Perspective 1 — First-time reviewer

A reviewer using the browser for the first time hits *batch action* friction first: they don't know which records they "own" the right to promote, and they don't know what *promote* even does inside the workflow. When they accidentally click *promote* on a record they were merely reading, they will panic. The first-time reviewer needs **two safety nets**: a clear pre-action confirmation that names the records, AND a post-action undo window. The first is more critical than the second; once they understand what *promote* means, the undo becomes optional polish.

### Perspective 2 — Power reviewer

A reviewer who has used the browser for weeks promotes records in batches of 5–20 at a time. They have built an internal model of which records are promote-ready (the `planner-ready` trust state) and trust their own filter combinations. For the power reviewer, the confirm modal is **friction**: it interrupts their flow with information they already know ("yes, I want to promote these 12 records, that's why I clicked the button"). The power reviewer needs **density**: list the records in the modal so they can scan-verify in one glance, and let *Enter* confirm — keyboard not mouse. A modal that takes more than 3 seconds to scan-and-confirm is too heavy for the power-user case.

### Perspective 3 — Accessibility-need reviewer

A reviewer using a screen reader needs the modal to announce *what is about to happen*, *which records are affected*, and *how many*. The modal must trap focus when it opens (so Tab cycles inside the modal), restore focus when it closes (to the row/button that opened it), and be dismissable by Esc. The screen-reader experience must include the *consequence*, not just the verb — "Confirm: promote 12 records to Planner. This action sends them downstream. You can undo within 30 seconds." beats "Confirm action?" by an order of magnitude.

### Cross-perspective synthesis

The three perspectives converge on a non-obvious finding: **the modal must work for batches of size 1**, not just size N. The first-time reviewer's accident-click case is one record; the power-reviewer case is many; the accessibility-need case wants the same affordance for any N. Designing the modal for the "interesting" case (large batch) and bolting on the small-batch case is the easy trap. The right move is to design for *any-N* from the start.

Other shared finding: **all three perspectives want the records listed by name in the modal**, not just by count. "Confirm promotion of 12 records" is weaker than "Confirm promotion: Mumbai, Goa, Pondicherry, … (+9 more)". The count-only form is a hidden-affordance failure — the reviewer can't verify what they're about to do.

---

## Step 3 — Define

### POV statement, attempt 1

> *A reviewer needs a way to confirm batch promotions because promoting the wrong record silently is irreversible.*

This is too solution-shaped: "confirm" presupposes a confirm-modal mechanism. Rewrite.

### POV statement, attempt 2

> *A reviewer needs a way to verify which records are about to be promoted, and to recover if the action was a mistake, because batch promotion is destructive within the surrounding workflow.*

Better — names the user need (verify + recover) without presupposing the UI. But still misses the *insight* from Empathize.

### POV statement, attempt 3 (locked)

> **A reviewer (any persona) needs a way to (a) see exactly which records are about to enter the Planner downstream + (b) reverse a wrong action within a short window, because batch promotion is irreversible at the source CSV level and the cost of a wrong promotion (un-vetted record shipped to Planner) is asymmetric — much higher than the cost of an interruption to a correct one.**

Sharper. The insight is *asymmetric cost*: the right reviewer flow is to optimise for catching the wrong action, not for minimising friction on the correct one. That's the design constraint the candidates will be triaged against.

### How-might-we questions

- HMW make the records visible *before* the destructive action without slowing the power-user flow?
- HMW make the action reversible at low cost for *any-N*, not just large batches?
- HMW signal the asymmetric cost in the UI itself (so the reviewer knows this action is special)?

---

## Step 4 — Ideate (≥ 3 meaningfully different candidates)

### Candidate A — Inline preview row + Enter-to-confirm

Selecting records for batch-promote inserts a *preview row* above the toolbar that lists the names of selected records and a count. The action button reads "Promote N records to Planner". Pressing it triggers a 3-second toast at the bottom: "Promoted N records. **Undo**." Click Undo within 3s to reverse; otherwise the action commits. No modal.

### Candidate B — Two-stage confirm modal with named records

Click *promote* → modal opens, listing the first 5 record names + "+N more", with the asymmetric-cost insight surfaced in the body ("This action sends records downstream. The cost of a wrong promotion is much higher than the cost of cancelling here."). Buttons: *Cancel* (focused by default) and *Promote N records*. Esc cancels. The modal traps focus; restores focus to the trigger button on close.

### Candidate C — Approval-step with explicit pause

Click *promote* → records enter a *pending-promotion* state visible in the side panel (`N pending`). The reviewer can leave, return, change their mind, then click *Commit pending* to actually promote — or *Cancel pending* to drop. No time-bounded undo. The pause is workflow-shaped, not modal-shaped.

### Candidate D — Single-record-only, no batch (eliminate the problem)

Remove batch promotion entirely. Each record is promoted individually; the workflow forces one-at-a-time. The asymmetric-cost is mitigated by friction (each promote requires a click), making batch errors mathematically impossible.

---

## Step 5 — Triage with the three constraints

| Candidate | Desirability | Feasibility | Viability | Verdict |
|---|---|---|---|---|
| **A. Inline preview + toast undo** | Strong for power reviewer (no modal interruption); medium for first-time (toast may be missed if attention is elsewhere); weak for accessibility-need (toasts are notoriously bad for screen readers; 3-second window may be too short with assistive tech latency) | Strong — toasts already in v1.1's component vocabulary (rule sheet §1); inline preview is a CSS row | Medium — requires a post-action undo path in the data layer (CSV row state must be "pending-rollback" for 3s); not yet in master schema | **Refine** — viability concern is real; ship-now would require schema change |
| **B. Two-stage confirm modal with named records** | Strong for first-time (clear pre-action verify); strong for accessibility-need (focus-trap, named records, asymmetric-cost message); medium for power reviewer (interruption is friction, but Enter-confirm + records-on-screen makes it scannable) | Strong — modal in Topic 2 rule sheet §3.5; aria-modal=true (this IS a modal, unlike the drawer); focus restoration already implemented in v1.1 (PR #12) | Strong — no schema change; the workflow state ("promoted") already exists in the master CSV; the modal is pure UI | **Proceed** — passes all three constraints |
| **C. Approval-step with explicit pause** | Medium for first-time (less direct than a confirm); medium for power (the pause is workflow-shaped, may feel slower); weak for accessibility-need (multi-step processes are harder to navigate with screen readers) | Medium — requires a "pending-promotion" state in the master CSV schema | Medium — adds a workflow stage that doesn't yet exist; the surrounding data pipeline doesn't know how to handle pending-promotions | **Refine** — would be the *better* long-term solution but requires Topic 5 (HCD)-level workflow redesign |
| **D. Eliminate batch promotion** | **Weak** — power reviewers explicitly want batch (Empathize evidence); removing it solves the cost-asymmetry problem by removing the user need | Strong — already the default, just remove the batch action | Strong — fits the current pipeline | **Drop** — solves the wrong problem; removes a real reviewer-task affordance |

**Chosen candidate: B (two-stage confirm modal with named records).**

**Comparative reasoning:** Candidate B beats A because A's viability concern is real (schema change for the rollback window) and the accessibility-need persona is poorly served by toasts. Candidate B beats C because B is shippable in v1.2 against the current schema; C requires Topic 5-level workflow rework and could be the v2.x successor. Candidate B beats D because D removes the user need rather than serving it — the right move for a power-reviewer-supporting tool is to make the batch action *safe*, not to remove it.

Candidate C is the **best long-term answer** if the workflow itself moves to an approval-stage model. That's a future loop's input, not Loop 1's output.

---

## Step 6 — Prototype (cheap form: ASCII walkthrough)

### Interaction script

1. Reviewer applies filters until they see the records they intend to promote.
2. Reviewer multi-selects rows via row-checkbox (added in v1.2 alongside this work) OR via Shift+click range OR via "Select all visible matching" header button.
3. Toolbar shows a contextual action bar: `N records selected · [Promote to Planner] [Clear selection]`. The action bar uses the existing toolbar grid slot (no new layout).
4. Reviewer clicks **Promote to Planner**.
5. Modal opens — focused by default on **Cancel**.

### Modal anatomy (ASCII layout)

```text
+----------------------------------------------+
| Confirm: promote 12 records to Planner       |  <- aria-labelledby
+----------------------------------------------+
|                                              |
| You are about to send these records          |
| downstream to the Planner:                   |
|                                              |
|  · Mumbai (DST2-006)                         |
|  · Goa (DST2-008)                            |
|  · Pondicherry (DST2-010)                    |
|  · Manali (DST2-001)                         |
|  · Leh (DST2-009)                            |
|  + 7 more (scroll to see all)                |
|                                              |
| Once promoted, the records appear in         |
| Planner's record-of-truth. Cancelling now    |
| keeps them unchanged in the reference layer. |
|                                              |
| The cost of a wrong promotion is much        |  <- the Topic 4 §3 insight
| higher than the cost of cancelling here.     |     made explicit in copy
|                                              |
+----------------------------------------------+
| [Cancel]  (focused)        [Promote 12]      |  <- both keyboard-reachable;
+----------------------------------------------+      Esc = Cancel; Enter on
                                                      Promote = confirm
```

### State machine (3 modal states)

```text
default     → modal open, Cancel focused, body lists records
busy        → after click on Promote; Promote button disabled, spinner; modal
              not closeable; aria-live region announces "Promoting 12 records"
done|error  → modal closes on success (toast confirms "12 records promoted to
              Planner") OR modal stays open on error (with retry + report-issue)
```

### Accessibility commitments

- `role="dialog"` + `aria-modal="true"` (this IS modal — unlike the drawer)
- `aria-labelledby` on the modal title; `aria-describedby` on the body
- Focus trap (Tab/Shift+Tab cycles inside modal)
- Focus restoration on close (returns to *Promote to Planner* button in the action bar)
- Esc cancels; clicking the overlay cancels; clicking Cancel cancels
- Enter on focused **Promote** button confirms (power-reviewer keyboard path)
- Names of all records read in source order; if > 5, "and N more" is announced

### Visual notes (no production CSS in this prototype)

- Modal width: ~440px (room for ~30-character record names + "..." truncation)
- Background dim overlay (existing `.drawer-overlay` pattern reused; class renamed to `.modal-overlay` for semantic clarity)
- Body text: not just verbs (no "Confirm action?"); names the consequence + the asymmetric-cost framing

---

## Step 7 — Test specification (with falsification criteria)

### Who would test

- **Persona 1**: a first-time reviewer (no prior use of the browser, given 5 minutes of orientation, then asked to review and promote a small batch)
- **Persona 2**: a power-reviewer-equivalent (someone who has used the browser for ≥ 30 minutes and built a mental model of the trust states)
- **Persona 3**: an accessibility-need user (screen reader: VoiceOver or NVDA; keyboard-only navigation)

### What task

Each tester is asked: *"Promote five specific records to Planner using the new batch action."* The records are pre-named so the test isn't about finding them; it's about the promote-confirm flow.

### What we would watch for

| Metric | Threshold |
|---|---|
| Time from clicking *Promote* button to closing the modal (confirm or cancel) | Median ≤ 8 seconds; 90th percentile ≤ 15 seconds |
| Time to *cancel* the action on the second tester (where we deliberately give them the wrong batch) | Median ≤ 5 seconds |
| Comprehension check after the modal closes: *"What did the action just do?"* | ≥ 80% of testers give an answer that includes "promoted records to Planner" or equivalent |
| Cancel rate on intentionally-wrong batches | ≥ 75% |
| Screen-reader-user can navigate, hear the records, and confirm or cancel without sighted assistance | Pass / fail (binary) |

### What would change our mind — falsification criteria

| Observation | What it would mean |
|---|---|
| Median confirm time > 15 seconds | Modal is too dense; consider removing the asymmetric-cost paragraph and relying on layout alone |
| Cancel rate on wrong batches < 50% | The modal is performing as a rubber-stamp; the records list is not being read; redesign |
| ≥ 2 testers cannot see the *Cancel* button or default focus is on Promote | Focus order is wrong; modal default should change |
| Screen-reader test fails (any of: doesn't announce N, doesn't announce record names, doesn't allow cancellation without sighted assistance) | The modal is not accessible; redesign before ship |
| ≥ 1 tester accidentally promotes a wrong batch | The modal hasn't done its job; design failure; re-loop |
| Power-reviewer cancel rate on correct batches > 10% | The modal is over-warning on safe batches; consider remembering "don't show this again for this session" |

A test that produces *none* of these failure-modes is a pass. A test that produces any of them is input for Loop 2.

### Constraint: no real reviewer testing in Lab 04

Lab 04 specifies the test but does not run it on real users — that's v1.2 user-testing scope, not Topic 4 lab scope. The point of specifying the falsification criteria is to make Loop 2 unambiguous if and when real testing happens.

---

## Step 8 — Loop result + decision

### What changed in our understanding

Before Loop 1, the workspace's mental model of "batch-promote-confirm" was a vague *"we should add a modal"*. After Loop 1, the workspace has:

1. The **asymmetric-cost insight** as the design constraint (the right design optimises for catching wrong actions, not for minimising friction on correct ones).
2. **Four candidates triaged against three constraints** (not picked-by-taste); Candidate B chosen with explicit comparative reasoning; Candidate C noted as the better long-term answer once workflow redesign happens.
3. **A modal anatomy** (cheap-form prototype) that names the records, surfaces the asymmetric-cost framing in copy, and addresses three personas (first-time, power, accessibility-need) symmetrically.
4. **A test specification with falsification criteria** — six concrete failure modes that would falsify the chosen design, so the next loop has unambiguous input.

The single most important insight: *the modal must work for any-N batches from the start*. Designing for a "main" batch size and bolting on the rest is the easy trap that Loop 1 avoided.

### What the next loop would do

**Loop 2**, when it runs, has three possible triggers:

1. *Real reviewer testing of the v1.2 implementation surfaces a falsification* → re-loop with the failure mode as the new Empathize input
2. *The workflow itself moves toward an approval-stage model (Candidate C territory)* → run a new loop with C as the starting candidate and Loop 1's modal as the "what we know already" baseline
3. *Reviewer feedback after some weeks of use surfaces an emergent issue not predicted by any of the three personas* → re-loop with that as the Empathize input

The single most important input Loop 2 would need is **a real Sponsor Reviewer**. Loop 1's three-persona synthesis is an honest substitute for solo workspace work, but Loop 2 should be run with at least one real reviewer testing the v1.2 implementation.

### Decision

**Ship Candidate B to the v1.2 backlog** with the following Topic 3 / Topic 2 handoff notes:

- **Topic 3 acceptance criteria** to write before implementation:
  - `U-CONF-1`: The reviewer can verify which records are about to be promoted without scrolling past the records list (modal body shows record names + count).
  - `U-CONF-2`: The reviewer can cancel a wrong batch in ≤ 1 interaction (Cancel button is default-focused; Esc cancels; overlay-click cancels).
  - `U-CONF-3`: The modal is accessible with a screen reader (announces N records, names each, allows confirm/cancel via keyboard).
  - `U-CONF-4`: The modal traps focus when open; restores focus to the trigger on close.
- **Topic 2 component rules** to add:
  - Modal anatomy: `aria-modal="true"`, focus trap, asymmetric-cost framing in body copy, default-focused Cancel button, Promote button reads "Promote N records" not "Confirm".
- **Falsification criteria** (Step 7 §"What would change our mind") become the v1.2 test plan.
- **Note in the v1.2 backlog**: Candidate C (approval-step) is the better long-term solution; revisit if the workflow itself moves toward an approval-stage model. This is a future loop's input.

**This loop is closed.** Three reusable design capabilities extracted:

1. **The three-persona synthesis pattern** (first-time / power / accessibility-need) as the solo-workspace substitute for real Empathize methods.
2. **Asymmetric-cost framing** as a design-constraint generator for destructive actions.
3. **The Topic 4 → Topic 3 handoff format** (chosen candidate + acceptance criteria + Topic 2 component rules + falsification criteria) as the canonical way Loop output becomes implementation input.

These three (combined with Topic 4 §14's three) take the workspace's reusable design-capability count to **fifteen** — three more than at the start of Lab 04.
