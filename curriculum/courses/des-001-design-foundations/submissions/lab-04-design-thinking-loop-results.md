# Lab 04 — Submission

Lab brief: `curriculum/courses/des-001-design-foundations/labs/lab-04-design-thinking-loop.md`
Source topic: `design/foundations/topic-04-design-thinking.md`
Loop output: `design/foundations/topic-04-design-thinking-loop.md`
Target artifact: `docs/destination-master-browser.html` (canonical v1.1; v1.2 pain-point lives in this build)

## Executive summary

Lab 04 ran one full design-thinking loop end-to-end against a single v1.2-candidate pain point — **confirm modal for destructive batch actions** (specifically: *promote-N-records-to-Planner-with-confirm-and-undo*). The loop produced evidence at every stage, generated four meaningfully different candidates, triaged them against Tim Brown's three constraints, selected Candidate B (two-stage confirm modal with named records), prototyped it as an ASCII anatomy, and specified the test that would falsify it.

The single most important insight: **the modal must work for any-N batches from the start**. Designing for a "main" batch size and bolting on the rest is the easy trap; Loop 1 avoided it by synthesising three personas (first-time / power / accessibility-need) and finding they converge on this requirement.

The single most important *meta* finding: Loop 1 ran honestly inside a solo workspace. The three-persona synthesis is a real substitute for facilitated empathy work; it doesn't replace real Sponsor-Reviewer testing, which becomes Loop 2's input when v1.2 ships.

The chosen candidate is signed off for the v1.2 backlog with explicit Topic 3 acceptance criteria + Topic 2 component rules + the six falsification criteria that would trigger Loop 2.

## Steps executed

| Step | Output | File |
|---|---|---|
| 1 — Pick the pain-point | Chose batch-promote-confirm; rejected collapsible-filter and faceted-panel for Loop 1 with reasons | `design/foundations/topic-04-design-thinking-loop.md` §Step 1 |
| 2 — Empathize | Three-perspective synthesis (first-time / power / accessibility-need) + cross-perspective convergence on *any-N* requirement | Loop doc §Step 2 |
| 3 — Define | POV statement, three attempts (each sharpening the *insight* — asymmetric cost) + one HMW question per shaping dimension | Loop doc §Step 3 |
| 4 — Ideate | Four meaningfully different candidates (inline-preview-toast / two-stage modal / approval-step / eliminate batch) | Loop doc §Step 4 |
| 5 — Triage | All four candidates × three constraints (desirability / feasibility / viability) with comparative reasoning | Loop doc §Step 5 |
| 6 — Prototype | ASCII anatomy of the chosen candidate; state machine; accessibility commitments | Loop doc §Step 6 |
| 7 — Test specification | Three personas + five testable metrics + six falsification criteria | Loop doc §Step 7 |
| 8 — Loop result + decision | Decision: Ship Candidate B to v1.2 backlog with handoff notes; Candidate C noted as long-term successor | Loop doc §Step 8 |

## Key findings

### Design findings

- **Asymmetric cost as the design constraint.** The right modal-design optimises for catching wrong actions, not for minimising friction on correct ones. The reviewer's cost of a wrong promotion (un-vetted record downstream) is much higher than the cost of an interruption to a correct one.
- **Three personas converge on *any-N*.** First-time, power, and accessibility-need reviewers all want the same modal to work for batches of 1, 5, or 50. Designing for the "interesting" case and bolting on the rest is the easy trap.
- **Names beat counts.** "Confirm promotion: Mumbai, Goa, Pondicherry, ... (+9 more)" beats "Confirm promotion of 12 records" by an order of magnitude — the count-only form is a hidden-affordance failure.
- **Cancel-as-default.** All three personas benefit from Cancel-being-default-focused. The power reviewer can still confirm via Enter on the Promote button; the first-time reviewer is protected from accidental confirmation; the accessibility-need reviewer hears the safe default first.

### Process findings

- **Four candidates with one dropped.** Candidate D (eliminate batch promotion) solved the wrong problem — it removed a real reviewer task affordance rather than serving it. Naming it explicitly as Dropped (not just absent) honoured the Ideate discipline of generating *meaningfully different* options.
- **The "best long-term answer" was not the chosen candidate.** Candidate C (approval-step with explicit pause) would be the better solution if the workflow itself moved toward an approval-stage model — but it requires Topic 5-level workflow redesign and isn't shippable in v1.2 against the current schema. Choosing B (shippable now) over C (better but needs workflow redesign) is the kind of explicit *shortest-path* decision Brown's triage forces.
- **Three POV rewrites.** Each rewrite sharpened the insight; the third locked the asymmetric-cost framing that became the design constraint. Spending disproportionate time on Define paid off in Ideate.

### Capability findings

Three new reusable design capabilities extracted (Loop doc §8):

1. **Three-persona synthesis pattern** (first-time / power / accessibility-need) — the solo-workspace substitute for real Empathize methods
2. **Asymmetric-cost framing** as a design-constraint generator for destructive actions
3. **Topic 4 → Topic 3 handoff format** (chosen candidate + acceptance criteria + Topic 2 component rules + falsification criteria) as the canonical way Loop output becomes implementation input

Combined with Topic 4 deep-reading doc §14's three, the workspace now has **fifteen** reusable design capabilities at maturity ≥ 3.

## Repository outputs

| Output | Path | Status |
|---|---|---|
| Loop output (Steps 1–8 evidence) | `design/foundations/topic-04-design-thinking-loop.md` | Complete |
| Lab submission (this file) | `curriculum/courses/des-001-design-foundations/submissions/lab-04-design-thinking-loop-results.md` | Complete |
| Master-browser checklist Topic 4 gates + anti-patterns | `design/checklists/master-browser-design-checklist.md` §23 + §24 | Complete |

## Submission checklist (per the lab brief)

- [x] Pain-point picked + two-rejection rationale recorded (Step 1) — batch-promote-confirm chosen; collapsible-filter and faceted-panel rejected for Loop 1 with reasons
- [x] Empathize evidence at 100–300 words, three perspectives minimum (Step 2) — three personas synthesised; cross-perspective convergence captured
- [x] POV statement + ≥ 1 HMW question; POV rewritten at least twice (Step 3) — three POV attempts; three HMW questions
- [x] ≥ 3 meaningfully different candidates (Step 4) — four candidates: inline-preview-toast, two-stage modal, approval-step, eliminate batch
- [x] Triage table with comparative reasoning (Step 5) — all four × three constraints with sourced cells; Candidate B chosen with comparative reasoning vs A, C, D
- [x] Prototype in cheap form, not production code (Step 6) — ASCII anatomy + state machine + accessibility commitments
- [x] Test specification with explicit falsification criteria (Step 7) — three personas, five testable metrics, six falsification criteria
- [x] Loop result + decision (Step 8) — Ship Candidate B to v1.2 backlog with handoff notes
- [x] Master-browser checklist Topic 4 section appended (§23 + §24)

## Decision-gate satisfaction (per the lab brief)

The brief's gate: *"Every stage produced its evidence artifact; Ideate produced ≥ 3 meaningfully different candidates; triage shows comparative reasoning; Test specification names explicit falsification criteria; the loop's decision is one of {Ship / Re-run / Defer}."*

All five conditions satisfied:

1. ✓ Every stage has its artifact (Steps 1–8 each produced a captured output)
2. ✓ Ideate produced four candidates (≥ 3 required), with explicit "meaningfully different" justification
3. ✓ Triage table cites sourced evidence in each cell + comparative reasoning sentence
4. ✓ Test specification names six falsification criteria
5. ✓ Decision: Ship Candidate B to v1.2 backlog (not Re-run; not Defer)

The decision-gate is satisfied.

## What this lab produces beyond the rubric minimum

- A **handoff format** (Step 8) that connects Loop output to Topic 3 criteria-writing and Topic 2 component rules — reusable for every future loop
- A worked **asymmetric-cost framing** that other destructive-action designs can inherit
- A worked **three-persona synthesis** as the solo-workspace pattern for any future Empathize work
- A worked **falsification-criteria-driven test spec** that turns "we tested it" into "we tested it against criteria that would have failed it"

## Open work after Lab 04

- Start **Topic 5 (Human-centred design)** — the standards-grade frame that pairs Topic 3 and Topic 4 (per the ratified three-topic push)
- When v1.2 starts, write Topic 3 acceptance criteria `U-CONF-1` through `U-CONF-4` (Loop doc §Step 8) and implement Candidate B with the falsification criteria as the test plan
- When a real Sponsor Reviewer becomes available, run Loop 2 against the v1.2 implementation; the six falsification criteria from Step 7 are the trigger conditions

## Lab 04 status

**Complete.** Lab evidence is sufficient for Topic 4 to be marked Closed in the competency map. PR B is the second of two PRs that close Topic 4. After PR B merges, Topic 4 closes and Topic 5 (HCD) begins.
