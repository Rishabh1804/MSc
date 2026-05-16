# Quiz 03 — Answers

Answer date: 2026-05-16. Written from the lecture, the five required Topic 3 sources, and the deep-reading doc at `design/foundations/topic-03-ux-design.md`, then cross-checked against `quiz-03-ux-design-answer-key.md`. Examples are drawn from the Destination Master Browser v1.

## 1. Definition

UX design is the discipline of **understanding** the user's task, **modelling** their journey through it, **designing** the interactions that make the journey succeed, and **evaluating** whether the design actually produces success for real users. It is distinct from UI design (the substrate — components, states, layout — which Topic 2 covered) and from usability evaluation (one phase of UX design — *evaluate* — not the whole). Without the *evaluate* feedback loop, UX work is design-by-opinion; without the *model* and *design* activities, UX work is research-without-output.

## 2. Four canonical UX activities and their artifacts

| Activity | Artifact |
|---|---|
| Research | Personas, contexts of use, user-need statements |
| Modelling | Task analysis, journey maps, mental models |
| Design | Wireframes, flows, prototypes, interaction specs |
| Evaluation | Usability studies, heuristic audits, task-success metrics |

DES-001 Topic 3 sits in the *modelling* activity (the seven-step reviewer journey) and produces the *bridge from modelling to design* (the UX acceptance-criteria sheet).

## 3. "I want a reset button" — classification and rewrite

This is a **solution-shaped need**. It came from a user (so it's not pure assumption), but it names a UI mechanism (a button) and the system action (reset). It does not state the underlying outcome the reviewer needs.

Rewritten in GOV.UK form:

> *"As a reviewer, I need to recover from an over-filtered state without losing my orientation, so that I can keep reviewing efficiently without restarting from scratch."*

The need leaves the designer's options open: a button is one valid implementation; a Clear-all action in the empty-state component (Topic 2 rule sheet §8) is another; chip-by-chip removal is another; the right answer is whichever serves the journey best per Lab 03's criteria.

## 4. Seven steps of the reviewer journey with failure modes

| Step | Failure mode |
|---|---|
| 1. Arrive | Reviewer can't tell what tool / what dataset / what state |
| 2. Understand | Reviewer over-trusts unverified data or under-trusts verified data |
| 3. Narrow | Filters apply but reviewer cannot tell which are active or remove them individually |
| 4. Compare | Cards-only forces serial reading; sort missing; reviewer cannot scan along an attribute |
| 5. Inspect | Modal blocks list; back-button breaks context; trust state lost inside the detail |
| 6. Recover | Reset hidden; no active-filter summary; reviewer restarts the whole journey |
| 7. Leave | Reviewer leaves with the wrong mental model about which records are safe |

## 5. UX acceptance criterion for "narrow"

> *The reviewer can apply, combine, and remove filters along any facet without leaving the result-list view. Every applied filter is visible without scrolling and is individually removable. The result-count updates within 300ms of each interaction and the change is perceptible (animated or otherwise signposted).*

The form: a testable behaviour, no UI mechanism named, with a measurable budget (300ms feedback latency, "without scrolling" as a visibility constraint). Chips, dropdowns, search-as-you-type, and faceted-panel implementations all satisfy this criterion — they just need to produce the named behaviour.

## 6. Heuristic audit vs acceptance criterion

A **heuristic audit** (Nielsen, Topic 1) is *retrospective and interpretive*: an auditor walks the design against general principles ("visibility of system status", "match between system and real world") and reports violations. Different auditors reach different findings because the heuristics are interpretive and the severity depends on judgement.

An **acceptance criterion** is *prospective and behavioural*: it states, before the design exists, what the reviewer must be able to do. Two evaluators applying the same criterion to the same design reach the same pass/fail verdict because the criterion is testable.

Acceptance criteria are **more reproducible**. Heuristic audits are better for catching things the criteria forgot to name — they remain useful as a complement, not a replacement. Topic 1's Lab 01 used heuristics; Topic 3's Lab 03 uses criteria. Both have a role.

## 7. GOV.UK's user-need discipline

GOV.UK enforces that a user need is written as `As a [user], I need [outcome], so that [goal]` — and explicitly **forbids naming a UI mechanism**. The other Topic 3 sources mention user needs but allow more flexibility ("the user wants X", "the experience should feel Y") that lets solution-shape language drift in.

The cost of GOV.UK's discipline is a slight rigidity in research language (some real user statements need rewriting before they fit the form). The benefit is that the discipline *catches* a specific class of UX failure: the case where a team designs for a request rather than an underlying need, locking the design unnecessarily. For an internal tool with a history of feature-first thinking, this is the single most important corrective in Topic 3.

## 8. Why both sheets are required before v1.1

Topic 2's rule sheet specifies **which components and what behaviour they must implement**. Topic 3's acceptance-criteria sheet specifies **what behaviour the journey as a whole must produce**. Either alone is insufficient:

- Rule sheet without criteria: components are well-specified but the journey may still fail (all components correct; reviewer still can't recover because the recovery *behaviour* was never named).
- Criteria without rule sheet: behaviours are testable but no component decision is made (everyone agrees the reviewer needs to recover; nobody decides if it's a button, a chip, or a modal).

**Example: empty-state recovery.** The rule sheet says *"content-rich empty state with active-filter summary + Clear-all button + what-to-try suggestion"* (component spec). The criterion says *"from any empty-result state, the reviewer can return to a non-empty result set in ≤ 1 interaction"* (behavioural). v1.1 needs both: the components come from the rule sheet, the behaviour from the criterion. A v1.1 design that ships the components but hides the Clear-all behind a scroll passes Topic 2 and fails Topic 3.

## 9. Topic 3 anti-pattern for data-review tools

**Designing the happy path only.** Data-review tools spend most reviewer-time in non-happy paths — empty results, conflicting records, missing fields, blocked statuses, ambiguous trust. A UX design that fully specifies "browse → find → open" and treats empty / error / loading as edge cases is a UX failure for a tool where the edge cases *are the work*. Topic 2's Lab 02 already flagged this at the component level (finding F3: one CSS class for three feedback states); Topic 3 turns it into a journey-level discipline (every journey step has criteria for non-happy-path behaviour).

Other valid Topic 3 anti-patterns from the deep-reading doc:

- Confusing user request with user need (designing for what users said, not what they need).
- Skipping evaluation (shipping a journey never tested against real reviewer behaviour).
- Ignoring the trust check at depth (Topic 1 finding carried forward — trust signal must survive every journey step).

## 10. Design-decision gate for new journey steps

> *"Which step of the reviewer journey does this new step serve, what is its cost budget, what is its failure mode and recovery, and what is the user-need form (`As a [reviewer], I need [outcome], so that [goal]`) that justifies it?"*

A wrong answer ("it would be nice to have", "competitors do it", "users asked for it") fails this question on its face. A right answer cites a journey step, a cost budget the new step must respect, a failure mode the new step prevents, and a user-need statement that does not name a UI mechanism. If a team can't produce all four parts, the step is solution-shape and is refused.

## Self-mark

Cross-checked against `quiz-03-ux-design-answer-key.md`. All ten answers are grounded in the deep-reading doc and at least one Topic 3 source. The two answers that diverge slightly in framing from the answer key:

- **Q2 (four activities)** — my answer adds where Topic 3 sits in the discipline (modelling + bridge-to-design). The key gave the bare table; my elaboration is a refinement, not a divergence.
- **Q9 (anti-pattern)** — I chose "designing the happy path only" as the primary answer with three alternatives listed; the key gave all four as equally valid. Equivalent.

No corrections needed.
