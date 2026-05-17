# Lecture 04 — Design thinking

## Learning objectives

By the end of this lecture, CodeMike should be able to:

- define design thinking as a *process* not a *worldview*; distinguish it from "thinking about design"
- name the five canonical d.school stages and the three IBM Loop activities, and explain how the two map onto each other
- explain Tim Brown's three constraints (desirability / feasibility / viability) and use them as a triage filter on candidate ideas
- describe how design thinking is iterative — the loop runs many times, not once
- run one loop end-to-end on a single concrete pain point and produce evidence at every stage
- explain why "we did empathize and define, then jumped to prototype" is the most common failure mode in practice

## Core distinction

Design thinking is a **process for moving from a fuzzy human problem to a tested solution**, organised as a small set of stages that the team iterates through. The stages have different vocabularies depending on the source (d.school's five-stage, IBM's three-activity Loop) but the underlying shape is consistent: *understand the human → frame the right problem → generate many options → make something concrete → test it with real users → loop*.

It is **not** "be creative" or "think about the user" or "have a workshop". Those are inputs or symptoms. Design thinking is the *artifact-producing* discipline that turns understanding into validated change.

For DES-001, design thinking is the *research → ideate → prototype → test* loop that sits *upstream* of Topic 3's reviewer-journey work. Topic 3 specifies what the journey must produce; design thinking is how we discover what to put in the journey when we don't already know.

```text
Design thinking sits HERE in the wider design discipline:

  Topic 3 (UX design)          → "what the journey must do"
  Topic 4 (Design thinking)    → "how we figure out what the journey must do"  ← here
  Topic 5 (Human-centred d.)   → "the standards-level frame for both"
  Topic 2 (UI design)          → "the components that deliver what the journey demands"
```

## The five-stage canonical process (d.school)

```text
1. Empathize  — learn about the user through observation and conversation
2. Define     — frame the right problem as a point-of-view statement
3. Ideate     — generate many options without filtering
4. Prototype  — make a tangible thing cheap enough to throw away
5. Test       — show it to real users and observe what happens
```

**The loop is the point.** A team that empathized once, defined once, ideated once, prototyped once, and tested once has run *one* iteration. The full benefit of design thinking comes from running *many* iterations, because what you learn at Test changes what you understand at Empathize and re-frames Define. Single-pass design thinking is design thinking only by accident.

## The IBM Loop (three activities)

IBM compresses the same shape into three activities — Observe / Reflect / Make — but adds two organising principles:

- **Hills** — short, ambitious statements of the user-need-shaped outcome the team is committing to (similar to GOV.UK user-need form from Topic 3).
- **Playbacks** — regular structured demos to sponsors and users to keep the loop honest.

Use IBM Loop framing for teams; d.school framing for individuals or small explorations. Both produce the same artifacts.

## Tim Brown's three constraints

From *Change by Design* and the HBR essay: a design-thinking solution must satisfy three constraints simultaneously:

- **Desirability** — does a real user actually want this?
- **Feasibility** — can it be built with available technology / skill?
- **Viability** — does it work in the surrounding business / operational context?

A solution that satisfies one or two but not all three is a candidate to refine, not a candidate to ship. Solutions that pass all three are rare and worth building.

For an internal QA tool like the Destination Master Browser:
- Desirability = does the reviewer actually want this affordance?
- Feasibility = can it be implemented in the single-file canonical HTML without breaking the modular pattern?
- Viability = does it operate within the data-trust constraints + the existing CSV ingest pipeline?

The three constraints are a *triage filter*, not a *generation rule*. Generate freely in Ideate; triage in the transition to Prototype.

## NN/g framing — "Design Thinking 101"

NN/g's framing emphasises that design thinking is **iterative** and **non-linear**: teams routinely jump back from Test to Empathize, or from Prototype back to Define. The "linear five-stage" diagram is a teaching aid, not the actual workflow.

NN/g also insists that the process produces **evidence**, not just feelings. Each stage has a tangible artifact:

| Stage | Evidence |
|---|---|
| Empathize | Field notes, interview transcripts, observation summaries |
| Define | Point-of-view statement, *how might we* question, problem statement |
| Ideate | Brainstorm output, sketches, idea list |
| Prototype | The thing itself (paper, code, mock, video, role-play) |
| Test | Feedback notes, observed behaviour, decisions about what to keep/change |

Evidence-producing design thinking is the kind we want; evidence-free design thinking is workshop theatre.

## CodeMike interpretation

For the CodeMike workspace, design thinking is the **upstream pairing for Topic 3**. Topic 3 produces *acceptance criteria* that the journey must satisfy; design thinking is the process that *figures out what criteria to write* when the team doesn't already know the user well enough.

```text
For a known reviewer task → Topic 3 (write the criteria; check against existing
                            heuristics + rule sheet).

For an unknown reviewer task → Topic 4 (run a loop; come back with a defined
                              problem + a tested prototype; THEN Topic 3 turns
                              the result into criteria).
```

The two are sequenced: do Topic 4 first when the problem isn't yet well-framed; do Topic 3 first when it is.

## Common misconception

The most common practical failure is to **collapse the loop into "empathize → define → straight to prototype"**, skipping Ideate as "we already know what to build". Skipping Ideate means the team commits to the first plausible solution rather than choosing the best from a generated set. The cost is mostly invisible (you don't see the better solutions you didn't generate) but it's the single most common reason design-thinking projects ship mediocre work.

The discipline: always generate at least three candidate solutions in Ideate before picking one to prototype. If only one comes to mind, the team hasn't ideated yet.

## Application to the Destination Master Browser

For DES-001, Lab 04 will run one full loop on a single browser pain point chosen from Lab 01's findings. The pain point is sized to fit one loop (not all of v1.1; not all of v1.2). The output is:

- An *Empathize* note (what we learned about the reviewer)
- A *Define* statement (the framed problem in a POV / "how might we" form)
- An *Ideate* list (≥ 3 candidate solutions)
- A *Prototype* — the chosen candidate made concrete (could be a sketch, a code mock, a written walkthrough)
- A *Test* note (what we'd test, with whom, and what would change our mind)
- A loop-result section (what changed in our understanding; what the next loop would do)

The lab does not require running the test with a real reviewer — that's `v1.2` user-testing scope. The lab does require *naming what we would test and what would change our mind*, which is the discipline that prevents Test from being a rubber-stamp.

## Discussion questions

1. The d.school 5-stage and IBM Loop describe the same process at different granularities. Which is the right level of detail for a one-person workspace like CodeMike's? Which for a larger team?
2. Tim Brown's three constraints — desirability, feasibility, viability — apply to *every* candidate solution. But they don't say *how much* of each constraint is enough. How would you adjudicate "feasible-but-barely" vs "very feasible but only mildly desirable"?
3. Topic 3's "user-need form" (GOV.UK strict) and Topic 4's "Define" stage are doing related work. What's the difference between a user-need statement and a *point-of-view* statement?
4. NN/g says the diagram is a teaching aid and the workflow is non-linear. What kinds of jumps are healthy (Test → Empathize) vs unhealthy (Prototype → Test without Define)?
5. The execution-plan pairing — Topic 4 *or* Topic 3 first, depending on whether the problem is well-framed — assumes you can tell. How do you know when a problem is "well-framed enough" to skip Empathize → Define and start at criteria-writing?
6. Run a quick triage: name one browser-v1.2 candidate, then walk it through desirability / feasibility / viability. Which constraint is it weakest on?

## Key takeaway

Design thinking is a *process* that produces *evidence at every stage* and *runs many iterations*. It is the discipline that turns "we should improve the browser" into "we tested three options on a specific pain point and the winning one was X for these reasons, here's the prototype". Skipping Ideate is the most common failure; running only one loop is the next most common.
