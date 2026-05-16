# Quiz 03 — Answer Key

Guideline answers. A response that says the same thing differently — particularly grounded in the Destination Master Browser — scores equally.

## 1. Definition

UX design is the discipline of **understanding** the user's task, **modelling** the journey they take through it, **designing** the interactions that make the journey succeed, and **evaluating** whether the design actually produces success for real users. It is distinct from UI design (the substrate — components, layout, states) and from usability evaluation (one phase of UX design, not the whole).

## 2. Four canonical UX activities

| Activity | Artifact |
|---|---|
| Research | Personas, contexts of use, user-need statements |
| Modelling | Task analysis, journey maps, mental models |
| Design | Wireframes, flows, prototypes, interaction specs |
| Evaluation | Usability studies, heuristic audits, task-success metrics |

## 3. Reset-button classification

It is a **solution-shaped need** — the reviewer named the UI mechanism (button) and the system action (reset), not the underlying outcome they need.

The underlying user need: *"As a reviewer, I need to recover from over-filtering without losing my orientation, so that I can keep reviewing efficiently without restarting from scratch."*

The user-need form leaves the designer free to satisfy it with a button, a clear-all action in the empty state, a chip-removal pattern, or a combination — whichever Topic 2's rule sheet supports best.

## 4. Seven journey steps with failure modes

1. **Arrive** — failure: reviewer can't tell what the tool is or what dataset is loaded
2. **Understand** — failure: reviewer over-trusts unverified data or under-trusts verified data
3. **Narrow** — failure: filters apply but reviewer cannot tell which are active
4. **Compare** — failure: reviewer cannot scan multiple records along a common attribute
5. **Inspect** — failure: reviewer opens a record and loses peripheral context, or cannot see trust state inside the detail
6. **Recover** — failure: reviewer cannot escape an over-filtered state, or cannot navigate to an adjacent record without resetting
7. **Leave** — failure: reviewer leaves with the wrong mental model about which records are safe to use

## 5. UX acceptance criterion for "narrow"

```text
The reviewer can apply, combine, and remove filters along any facet without
leaving the result-list view. Every applied filter is visible without scrolling
and is individually removable. The result-count updates within 300ms of each
interaction and the change is perceptible (animated or otherwise signposted).
```

Note the form: testable behaviour, no UI mechanism named (chip / dropdown / search input are all valid implementations).

## 6. Heuristic audit vs acceptance criterion

A **heuristic audit** (Nielsen) is a *retrospective* evaluation: the auditor walks the existing design against a set of general principles (visibility of system status, match between system and real world, etc.) and notes violations. Different auditors reach different findings because the heuristics are interpretive.

An **acceptance criterion** is *prospective and behavioural*: it states, before the design exists, what the user must be able to do. Two evaluators applying the same criterion to the same design reach the same verdict (passes / fails) because the behaviour is testable.

Acceptance criteria are more reproducible. Heuristic audits are better for catching things the criteria forgot to name.

## 7. GOV.UK's discipline

GOV.UK enforces that a user need is written as `As a [user], I need [outcome], so that [goal]` — and explicitly **does not name a UI mechanism**. Other sources allow more flexibility ("the user wants X", "the experience should feel Y"). GOV.UK's discipline is the one that prevents solution-shaped needs from passing as real needs. The cost is a slight rigidity in research language; the benefit is that the discipline catches a specific class of UX failure (designing for a request rather than a need).

## 8. Why both sheets are required

Topic 2's rule sheet specifies *which components and what behaviour they must implement*. Topic 3's acceptance-criteria sheet specifies *what behaviour the journey as a whole must produce*. Either alone is insufficient:

- Rule sheet without criteria: components are well-specified but the journey may still fail (e.g. all components are correct but the reviewer can't recover from over-filtering because the recovery path was never named as a criterion).
- Criteria without rule sheet: behaviours are testable but no component decision is made (everyone agrees the reviewer needs to recover, but is it a button? a chip? a modal?).

Example: the empty-state recovery action. The rule sheet says "content-rich empty state with active-filter summary + Clear-all button + what-to-try suggestion" (component spec). The acceptance criterion says "the reviewer can return to a non-empty result set in ≤ 1 interaction from any empty state" (behavioural). v1.1 needs both: the components from the rule sheet, the behaviour from the criterion. A v1.1 design that ships the components but fails the behaviour (e.g. Clear-all hidden behind a scroll) passes Topic 2 and fails Topic 3.

## 9. UX anti-pattern for data-review tools

**Designing the happy path only.** Data-review tools spend most of their reviewer-time in non-happy paths: empty results, conflicting records, missing fields, blocked statuses, ambiguous trust. A UX design that gives full attention to "browse → find → open" and treats the other states as edge cases is a UX failure for a tool where the edge cases are the work.

Other valid Topic 3 anti-patterns:
- *Confusing user request with user need* (designing for what users said, not what they actually need).
- *Skipping evaluation* (shipping a journey that was never tested against real reviewer behaviour).
- *Naming UI mechanisms in user-need statements* (presupposing the solution before researching the need).
- *Ignoring the trust check at depth* (Topic 1 finding carried forward).

## 10. Design-decision gate for journey additions

> "Which step of the reviewer journey does this new step serve, what is its cost budget, what is its failure mode and recovery, and what is the user-need form (as a [reviewer], I need [outcome], so that [goal]) that justifies it?"

A wrong answer ("it would be nice to have", "competitors do it", "users asked for it") fails this question on its face. A right answer cites a journey step, a cost budget the new step must respect, a failure mode the new step prevents, and a user-need statement in the GOV.UK form.
