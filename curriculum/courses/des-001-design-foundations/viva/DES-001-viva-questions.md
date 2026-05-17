# DES-001 Viva Questions

## Topic 1 — UI vs UX

1. Why is UI not equivalent to UX?
2. Which source gave the broadest definition of UX?
3. Why is data credibility a UX concern in the Destination Master Browser?
4. What is one example of attractive UI causing poor UX?
5. Which browser feature is most justified by Topic 1?
6. How should uncertainty be represented in a data-review interface?
7. Why should accessibility be treated as part of UX?
8. What would you revise in the browser after completing the heuristic audit?

## Topic 2 — What is UI design

1. Define UI design as a discipline and explain why visual design is a sub-skill rather than a synonym.
2. Name the nine standard component states. Which three are most commonly missing in data-review tools, and why?
3. Distinguish affordance, signifier, and feedback. Why does Norman argue that the signifier does most of the design work in digital interfaces?
4. The five required Topic 2 sources differ less on definition than on emphasis. Name two specific emphasis differences that change a v1.1 design decision.
5. For the Destination Master Browser, when should a record open in a drawer rather than a modal? When does the choice flip?
6. Why does the topic argue that the unit of design is the *pattern* (master-detail, faceted search) rather than the *component*?
7. Give one example of a Topic 2 anti-pattern that v1 commits, and the v1.1 fix.
8. The topic adds a "when not to use" gate to the master-browser checklist. Why is that gate more important than a "when to use" rule?

## Topic 3 — UX design

1. Define UX design and explain why "thinking about users" is not by itself UX design.
2. Norman names two "gulfs". What are they, and which gulf does v1's `.empty` shared loading/empty/error pane sit on?
3. GOV.UK enforces a specific form for user needs. State the form and explain what design failure it prevents.
4. The five required Topic 3 sources agree on the *what* of UX design but differ on *emphasis*. Name two emphasis differences that change a v1.1 design decision.
5. State the seven steps of the Destination Master Browser reviewer journey and the cost budget for the most cognitively-expensive one.
6. A reviewer says: "I'd love a way to compare three records side-by-side". Classify this and produce the underlying user need in GOV.UK form.
7. Topic 2 ended at a component rule sheet; Topic 3 ends at an acceptance-criteria sheet. Give one v1.1 decision that needs both, and explain what fails if either is missing.
8. The Topic 3 "happy path only" anti-pattern is specifically dangerous in data-review tools. Why?

## Topic 4 — Design thinking

1. Define design thinking as a discipline (not a worldview). What does it *produce* that "thinking about design" does not?
2. The d.school 5-stage and IBM Loop 3-activity describe the same process at different compressions. Where does each framing's *structure* help, and where does it hide something the other surfaces?
3. State Tim Brown's three constraints. For a v1.2-candidate of your choice on the Destination Master Browser, walk it through the triage and report the constraint it is weakest on.
4. NN/g insists the process is iterative and non-linear. Name one healthy jump and one evidence-skipping jump, and explain the principle that distinguishes them.
5. Don Norman's *Useful Myth* critique argues design thinking risks devaluing domain expertise. Does the critique sharpen the discipline or undermine it? Defend either position.
6. The execution plan pairs Topic 4 with Topic 3: do a design-thinking loop when the problem isn't well-framed; skip to criteria-writing when it is. What test would tell you a problem is "well-framed enough" to skip Topic 4?
7. The CodeMike workspace is single-person today. Which Topic 4 disciplines transfer directly to single-person work, and which need translation?
8. Give one example of an evidence-free version of any of the five stages, and explain what the *next* stage suffers as a consequence.

## Topic 5 — Human-centred design

1. Define HCD as a discipline. Distinguish it from design thinking (Topic 4) and from UX design (Topic 3).
2. Name the four ISO 9241-210 activities. For each, name one artifact the Destination Master Browser work has already produced that maps to it.
3. State three of the six ISO principles and explain how each translates to a single-person workspace.
4. The W3C triad (usability / accessibility / inclusion) overlaps heavily. Where on v1.1 are the three lenses well-served? Where is the worst-served lens, and what does that gap look like concretely?
5. Norman's *HCD Considered Harmful?* argues HCD can over-centre the individual user at the cost of systems thinking. Defend or attack the position; cite either way.
6. The hierarchy says HCD is the umbrella over Topics 2 / 3 / 4. Which of the four activities does Topic 4 (design thinking loop) most directly exercise? Which one does Topic 4 under-serve, requiring HCD discipline to compensate?
7. Lab 05's audit will surface gaps. Name two anticipated gaps and explain how each would be closed in v1.2.
8. The HCD self-audit gate has four cells. Pick a v1.2 candidate (your choice) and run the gate. What's the weakest cell?

## Topic 6 — Gestalt principles

1. Define Gestalt principles as a discipline. Explain the *perceptual constraint vs aesthetic rule* distinction and why the constraint framing is operationally different from the style framing.
2. State *Prägnanz* and explain why every specific Gestalt principle is a corollary. Walk through at least three of the six principles as worked corollaries.
3. Name the six core Gestalt principles. For each, give one Destination Master Browser example where the principle is currently honoured.
4. Define a *Gestalt violation*. Give one v1.1 region where you believe a *false-positive grouping* violation exists, name the principle(s), and explain the reviewer-task consequence.
5. The six principles can conflict. Name two principles that pull in different directions in v1.1's cards view and adjudicate. State the general rule you applied and cite the source.
6. Where does Gestalt sit in the canonical hierarchy relative to Topics 2 / 3 / 4 / 5? Why is it positioned *underneath* Topic 2 rather than alongside?
7. The execution plan estimates Topic 6 at ~4–5h, smaller than Topic 4/5's 5–7h. Defend the scoping decision; name two things the smaller scope deliberately doesn't cover.
8. Lab 06 produces a per-region per-principle audit. Name two anticipated violations the audit will need to confirm/refute and the principle(s) involved in each.

## Answer file

Answers should be stored in:

```text
courses/des-001-design-foundations/viva/DES-001-viva-answers.md
```
