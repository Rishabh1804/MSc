# Capability — Seven-step Reviewer-Journey Template

## What this capability does

Models a data-review tool's user journey as seven discrete steps, with goal / cost-budget / failure-mode / trust-check per step. Replaces ad-hoc "let's add a feature" thinking with a deliberate journey-first design move: name the steps, define the budgets, identify the failure modes, and only then design the components.

Origin: DES-001 Topic 3 (UX design). First applied to the Destination Master Browser v1.1 (TRANSFER_LOG Transfer 1; 19/19 walk-through pass).

## Inputs

- A data-review tool (existing or planned)
- A named reviewer role (who is doing the review, for what downstream decision)
- A trust-state vocabulary for the underlying records (often a state machine; for the master browser: `verified` / `planner-ready` / `unverified` / `blocked` / `missing-fields` / `conflict` / `unassigned`)
- The Topic 2 component rule sheet (`design/foundations/ui-design-component-rules.md`) — the journey template pairs with it

## Outputs

- A seven-step journey table with `goal / cost budget / failure mode / trust check / current state / gap` per step
- A user-need statement per step in GOV.UK form (`As a [reviewer], I need [outcome], so that [goal]`)
- An acceptance-criteria sheet (one or more behavioural criteria per step) that becomes the implementation gate
- A gap analysis vs prior heuristic / informal audits

## Method

### The seven steps (canonical)

```text
1. Arrive       — orient to the tool and dataset within seconds
2. Understand   — read the dataset's overall trust state
3. Narrow       — constrain the result set along any facet
4. Compare      — scan many records along common attributes
5. Inspect      — read one record's full detail keeping list context
6. Recover      — escape over-filtered state without losing orientation
7. Leave        — exit with an accurate mental model of what was reviewed
```

These are not arbitrary. They map onto Norman's seven-stage action model collapsed into the reviewer-task domain, with explicit trust-checking inserted because data-review tools are trust-shaped. For non-review tools (e.g. a transactional service) some steps collapse — but the journey-first discipline transfers.

### Per-step fields

For each step, capture:

- **Goal** — written as `As a [reviewer], I need [outcome], so that [goal]`. **No UI mechanism named.** (Without this rule, journeys drift into feature lists.)
- **Cost budget** — interactions, seconds, or cognitive units. If the step costs more than the budget, the design has failed the step.
- **Failure mode** — what goes wrong if the step is poorly supported. Often this is *what the user does when the step is too expensive* (e.g. abandons, over-trusts, gets the wrong answer).
- **Trust check** — what trust signal must be visible at this depth. The four-depth trust spec (page banner / list row / inspect detail / confirm modal) maps onto journey steps; every step should appear in the four-depth audit.
- **Current state** — Pass / Partial / Fail for the existing implementation.
- **Gap vs prior audit** — what does the journey row add beyond what a heuristic audit already said? (Helps prevent rework.)

### Producing the acceptance criteria

For each step, write 1–3 acceptance criteria. Each must be:

- **Testable** — two evaluators applying it to a design produce the same verdict
- **Behavioural** — describes what the reviewer can do, not what the UI looks like
- **Mechanism-independent** — does not name dropdowns, chips, drawers, etc.
- **Measurable** — has a budget where applicable

The criteria become the implementation gate. A component that doesn't satisfy at least one criterion has no justification.

### Implementation order

```text
1. Sketch the seven steps for the target tool. State the goal in user-need form.
2. Set cost budgets. Be specific (≤ 5s, ≤ 1 interaction).
3. Name failure modes. Name trust checks.
4. Audit the current implementation. Pass / Partial / Fail per step.
5. Write 1–3 acceptance criteria per step.
6. Map each criterion to a Topic 2 rule-sheet component.
7. Build the implementation against the criteria.
8. Verify via a reproducible walk-through (Playwright or equivalent).
9. Confirm 100% of criteria pass before shipping.
```

## Current maturity

**Level 4 — Transferred to project.** The template was applied to Destination Master Browser v1.1, shipped 2026-05-16, and verified by a 19-gate Playwright walk-through that includes the four polish behavioural tests (TRANSFER_LOG Transfer 1).

Maturity 5 (Maintained capability with examples and limitations) unlocks when the template is applied to a second project and the cross-project insights are captured here.

## Evidence

- `design/foundations/topic-03-ux-design.md` §7 — the topic-level definition
- `design/foundations/topic-03-ux-design-journey-map.md` — the journey applied to the Destination Master Browser
- `design/foundations/ux-acceptance-criteria.md` — the 14 criteria produced by the journey
- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/walkthrough.js` — the reproducible 19-gate Playwright walk-through
- `curriculum/courses/des-001-design-foundations/verification/v1.1-walkthrough/walkthrough-results.json` — machine-evidenced verification results
- `operations/TRANSFER_LOG.md` Transfer 1 — the formal transfer record

## Limitations

- **Tuned for data-review tools.** The seven steps reflect QA / review work. Transactional services (apply, pay, book) have different journey shapes — typically more steps and fewer trust depths. The journey-first discipline transfers; the seven-step structure may not.
- **Trust-check column is data-review-specific.** Tools that don't carry trust state (e.g. a search interface for public content) can replace this column with another invariant the journey must preserve, but the column shouldn't be silently dropped.
- **Cost budgets are designer estimates until measured.** The 60-second budget for Compare (and others) come from cognitive-load literature plus designer judgement. They should be validated against real reviewer behaviour once the implementation has users; the v1.1 walk-through measures system response time, not human cognitive time.
- **The capability is `Package`-level discipline, not `Build`-level code.** It tells you what to build; it doesn't write the code. Topic 2's component rule sheet handles the `Build` side. Both are required.
- **One transfer to date.** Generalisability beyond data-review tools is unproven until a second transfer happens.

## Reusable in

- Datasets browser (planned)
- Validator review tool (planned)
- Planner review tool (planned)
- Any future internal QA / review tool with a record-list + record-detail + trust-state structure
- *Tentatively*: any tool with a seven-step-shaped journey, by adapting the column set

## Transfer history

| # | Date | Target | Outcome |
|---:|---|---|---|
| 1 | 2026-05-16 | Destination Master Browser v1.1 | 19/19 walk-through pass; all 11 Lab 01 findings closed; trust state preserved across four depths |

## Next action

Apply to a second data-review tool when one comes into scope. At that point, capture cross-project insights here and bump maturity to 5. Until then, this card is the workspace's canonical statement of the capability and the model for future formal capability cards (per CAPABILITIES.md template).
