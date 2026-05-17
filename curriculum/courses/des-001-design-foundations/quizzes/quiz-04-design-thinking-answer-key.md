# Quiz 04 — Answer Key

Guideline answers. A response that says the same thing differently — particularly grounded in the Destination Master Browser — scores equally.

## 1. Definition + non-definition

Design thinking is the **process** of moving from a fuzzy human problem to a tested solution, by iteratively understanding the user → framing the right problem → generating many candidates → making something concrete → testing it with real users. The verbs are load-bearing; "thinking about design" is not design thinking. Design thinking is **not** a worldview, a stance, "being creative", "having a workshop", or any single-stage activity — it is the *artifact-producing iterative loop* and the *evidence per stage* that distinguishes it from design-by-opinion.

## 2. Stages and mapping

| d.school (5-stage) | IBM Loop (3-activity) |
|---|---|
| Empathize | Observe |
| Define | Reflect |
| Ideate | Reflect (with Make at the boundary) |
| Prototype | Make |
| Test | Observe (with Reflect at the boundary) |

The IBM compression is honest: the boundary stages (Define↔Ideate, Test↔Empathize-next-loop) are where the heavy thinking happens. d.school's five-stage is better for teaching the discrete artifacts; IBM Loop is better for team cadence.

## 3. Tim Brown's three constraints applied to the browser

- **Desirability** — *Does the reviewer actually want this?* Example: a confirm-modal-with-undo for batch-promote-to-Planner is desirable because reviewers fear silently shipping the wrong record. A side-panel showing recent commits is not desirable because no reviewer asked for it.
- **Feasibility** — *Can it be built?* Example: sortable table columns are feasible in the single-file canonical HTML pattern. A live-collab cursor (reviewer A sees reviewer B's selection) is not feasible without a server.
- **Viability** — *Does it fit the surrounding context?* Example: trust badges fit the data-trust constraint that v1.1 is "structurally valid but not Planner-ready". An "approve and export to Planner" button does not fit, because the workflow doesn't yet support approval-as-state.

## 4. Healthy vs evidence-skipping iteration

**Healthy:**
- Test → Empathize: testing the prototype with a reviewer surfaces a need we didn't know about; we go back to learn more.
- Test → Define: testing reveals we were solving the wrong problem; we re-frame.
- Prototype → Ideate: while making the prototype, we see a better candidate; we ideate one more round.

**Evidence-skipping:**
- Empathize → Prototype (jumping over Define + Ideate): "we already know what to build". Commits to the first plausible solution without framing the problem or generating alternatives. This is the most common practical failure.

## 5. Evidence per stage + evidence-free failures

| Stage | Evidence | Evidence-free failure |
|---|---|---|
| Empathize | Field notes, interview transcripts, observation summaries | "We talked to some users" — no captured notes; the next stage runs on the team's memory and biases |
| Define | POV statement, "how might we" question, problem statement | "The problem is the browser is bad" — non-specific, untestable, doesn't constrain Ideate |
| Ideate | Numbered list of candidates with one-line each | "We brainstormed" — no captured list; next stage picks "the obvious one" by default |
| Prototype | The thing itself (sketch, mock, code, video, role-play) | "We described what we'd build" — no tangible artifact; Test runs on imagination |
| Test | Feedback notes, observed behaviour, decisions about what to keep/change | "Users liked it" — no captured feedback; next loop has no input |

## 6. Norman's "Useful Myth" critique

Norman's argument (2010 essay + later): "design thinking" risks being a *brand* for what skilled designers already do, and risks devaluing *domain expertise* — implying that with the right process, anyone can solve any problem. He's not dismissive — he calls it a "useful myth" because the myth gets non-designers to take design seriously. But the myth is dangerous when it lets organisations skip hiring people with deep domain knowledge.

**Verdict: sharpens.** The critique is useful because it tells the discipline what to defend against: replacing skilled designers with workshop attendance, claiming the process substitutes for domain expertise, treating "design thinking" as a solved problem rather than as a continuing practice. Sources that ignore Norman's critique (some consulting-flavoured ones) end up overselling.

## 7. User need vs POV statement

A **user need** (Topic 3 / GOV.UK form): `As a [reviewer], I need [outcome], so that [goal]` — outcome-shaped, mechanism-free, testable as behaviour. Produced when the user is *known* and the team is moving toward design.

A **POV statement** (Topic 4 / d.school form): `[User] needs a way to [need] because [insight]` — *insight*-shaped, frames the problem with a sharp surprise the team learned during Empathize. Produced when the user is *being learned* and the team is moving toward Ideate.

The POV is the bridge between Empathize (learning) and Ideate (generating). The user-need statement is the bridge between Define (or known user-research) and Design (criteria-writing). Same intent: avoid solution-shape. Different stage of the loop.

## 8. Single-person-workspace anti-pattern

**Skipping Empathize because "I am the user".** In CodeMike's case the same person designs the browser, reviews destination records, and writes the journey criteria. The temptation is to use introspection as data. The risk: the designer-reviewer is *not representative* of the future reviewer pool (a fresher reviewer; a domain-expert reviewer; an accessibility-need reviewer). Mitigation: write down what *I, today, with full context* would do — then explicitly imagine and write down what a *first-time reviewer* would do, what a *power-reviewer* would want, what an *accessibility-need reviewer* would experience. Three personas synthesised in writing are better than introspection-as-data.

Other valid anti-patterns:
- Doing the loop once and shipping (no iteration).
- Skipping Ideate (committing to the first candidate).
- Writing the prototype directly as code (sunk-cost dependency on the first attempt).
- Treating Test as a rubber-stamp (no falsification criteria defined).

## 9. Topic 4 first vs Topic 3 first

**Topic 4 first** when the problem isn't well-framed. Example: "reviewers are slow on Planner-promotion" — *we don't know what makes them slow*. Run an Empathize → Define loop to learn whether it's batch-size, cognitive load on trust assessment, or filter friction. Then Topic 3 turns the finding into criteria.

**Skip to Topic 3** when the problem is well-framed and the user need is known. Example: "the empty state silently fails — fix it" (from Lab 03). The need is clear; the criterion (`U-REC-1`: recovery in ≤ 1 interaction) follows directly. Going through a full design-thinking loop here would be ceremony — Empathize would just restate what Lab 03 already documented.

The rule: do Topic 4 when the cost of a loop is less than the cost of building the wrong thing. For small, well-framed changes, Topic 3 alone is enough. For large or ambiguous changes, Topic 4 first.

## 10. Design-decision gate before exiting Ideate

> *"We are about to commit one candidate to Prototype. Have we generated at least three meaningfully different candidates, AND can each one be evaluated against desirability / feasibility / viability with concrete evidence, AND have we written down why the chosen candidate beats the other two?"*

A wrong answer is immediately visible: a single candidate; or three near-identical candidates; or "we just like this one"; or the desirability assessment is "users will love it" with no source. A right answer cites three distinct candidates, a per-candidate triage row, and a comparative reason for the chosen one — ideally including what *would change our mind* during Test.
