# Lecture 03 — UX design

## Learning objectives

By the end of this lecture, CodeMike should be able to:

- define UX design as a discipline and distinguish it from UI design (revisited from Topic 1) and from usability evaluation
- name the four canonical UX activities (research, modelling, design, evaluation) and the artifact each produces
- map a reviewer journey from arrival to leaving, with each step's goal / cost / failure-mode
- write a UX acceptance criterion that is testable against an actual reviewer behaviour
- distinguish *user need* from *user request* from *user solution-shape*
- explain why UX failures are usually not UI failures, and what that means for the Destination Master Browser

## Core distinction

UX design is the discipline of **understanding the user's task, modelling their journey, designing the interaction to make the journey succeed, and evaluating whether it actually does**. It is the loop that runs *around* UI design: UI design is the substrate; UX design is the verification that the substrate produces the right outcomes for real users.

```text
UX design  =  research + modelling + interaction design + evaluation
                  ↑                       ↑                    ↑
              (Topic 4-5)             (Topic 2 + here)     (Topics 6-12)
```

Topic 1 said UI is the mechanism and UX is the journey. Topic 2 specified the components. Topic 3 specifies the journey those components must serve.

## The four canonical UX activities

| Activity | Question it answers | Artifact it produces |
|---|---|---|
| **Research** | Who is the user, what is the task, where does it happen, why does it matter? | Personas, contexts of use, user-need statements |
| **Modelling** | What is the structure of the task as the user experiences it? | Task analysis, journey maps, mental models |
| **Design** | What sequence of interactions makes the task succeed? | Wireframes, flows, prototypes, interaction specs |
| **Evaluation** | Does the design actually let the user complete the task? | Usability studies, heuristic audits, task-success metrics |

DES-001 Topic 3 focuses on the *modelling* activity (journey maps) and the bridge from modelling to *design* (acceptance criteria). Topic 1's heuristic audit covered the *evaluation* activity at a basic level.

## User need vs user request vs solution-shaped need

A standard UX failure mode is mistaking a **user request** ("I want a dropdown for region") or a **solution-shaped need** ("the system should filter by region") for a real **user need** ("I need to find all destinations in West Asia").

GOV.UK Service Manual is the strictest source on this. A genuine user need is:

```text
As a [reviewer], I need [outcome], so that [goal].
```

It does not name the UI mechanism. It names the user, what they need to be able to do, and why. The UI mechanism is the designer's choice, not the user's.

## The reviewer journey (DES-001 framing)

For the Destination Master Browser, the canonical reviewer journey has seven steps:

```text
1. Arrive — orient to the tool, understand the dataset state
2. Understand — read the trust signal, decide what is safe to use
3. Narrow — apply filters / search to constrain the result set
4. Compare — scan multiple records along common attributes
5. Inspect — open one record's full detail
6. Recover — adjust filters, navigate to a different record, reset
7. Leave — close with the correct mental model about what was reviewed
```

Each step has:
- a **goal** (what the reviewer is trying to achieve)
- a **cost** (cognitive effort, clicks, time)
- a **failure mode** (what goes wrong if the step is poorly supported)
- a **trust check** (what trust signal must be visible at this depth)

Topic 1 audited the seven steps heuristically. Topic 3 turns each step into testable acceptance criteria.

## UX acceptance criteria

A UX acceptance criterion is a *testable, behavioural* statement of what the reviewer must be able to do, expressed independently of the UI:

```text
The reviewer can narrow the result set by region in ≤ 3 interactions,
and the active filter is visible without scrolling.
```

It is not "the dropdown is present"; it is "the reviewer can do X with cost Y and feedback Z". UI changes that maintain the criterion (dropdown → chip → search-as-you-type) all pass. UI changes that break it fail.

Acceptance criteria are the *journey-level companion* to Topic 2's component rule sheet. Together they form Browser v1.1's specification: the rule sheet says *what components*; the acceptance criteria say *what behaviours those components must produce*.

## CodeMike interpretation

For the Destination Master Browser, UX design asks:

```text
For each reviewer-journey step, what is the testable behaviour the UI must produce —
and what is the cost, failure mode, and trust check at that step?
```

Topic 2 ended at the rule sheet. Topic 3 ends at the acceptance-criteria sheet. Both are required before v1.1 code lands.

## Common misconception

UX design is **not** "thinking about users" or "asking users what they want" or "running a usability test at the end". Those are inputs. UX design is the discipline that turns those inputs into a *modelled journey* with *acceptance criteria* the design can be evaluated against. A design without acceptance criteria is decoration plus opinion.

## Application to browser redesign

For each of the seven reviewer-journey steps, Lab 03 will produce:

1. The goal statement in user-need form
2. The cost budget (max interactions / time / cognitive load)
3. The failure mode and recovery affordance
4. The trust check (what trust signal is visible)
5. The acceptance criterion (testable behaviour)
6. The component(s) from Topic 2's rule sheet that deliver it
7. The Lab 01 heuristic finding it closes (if any)

## Discussion questions

1. Topic 1 mapped the reviewer journey heuristically (Lab 01 Exercise B). What does it cost a reviewer when the journey is mapped without acceptance criteria?
2. Which of the seven journey steps is currently best-served in v1? Which is worst-served?
3. A reviewer says "I want a Reset button". Is that a user need, a user request, or a solution-shape? What would you write as the underlying need?
4. The empty state (Lab 02 §3 finding) is a *constrained-success state*. What is the acceptance criterion for it?
5. Topic 2's rule sheet says "modal is reserved for v1.2+ destructive batch actions". What is the UX acceptance criterion that justifies *not* using a modal for record inspection?
6. How does an acceptance criterion change when the user's task changes (e.g. "review 5 records before lunch" vs "audit all 359 records for the Planner export")?
7. Where in the seven-step journey does data-trust signalling have the highest leverage?
8. What is the relationship between an acceptance criterion (Topic 3) and a Nielsen heuristic (Lab 01)?

## Key takeaway

UX design is the discipline of converting *understanding the user* into *testable behavioural criteria* the UI must produce. Topic 2 ended at component rules. Topic 3 ends at journey criteria. The browser is well-designed when *both* sheets are satisfied — neither alone is sufficient.
