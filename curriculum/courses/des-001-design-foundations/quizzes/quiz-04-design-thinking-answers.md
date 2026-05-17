# Quiz 04 — Answers

Answer date: 2026-05-17. Written from the lecture, the four required Topic 4 sources, and the deep-reading doc at `design/foundations/topic-04-design-thinking.md`, then cross-checked against `quiz-04-design-thinking-answer-key.md`. Examples are drawn from the Destination Master Browser v1.1.

## 1. Definition + non-definition

Design thinking is the **iterative process** of moving from a fuzzy human problem to a tested solution, by repeatedly understanding the user → framing the right problem → generating many candidates → making something concrete → testing it with real users. The verbs are load-bearing; the loop is the point; each stage produces an artifact. It is **not** "thinking about design", "being creative", "having a workshop", or any single-stage activity — those are inputs or symptoms, not the discipline itself.

## 2. Stages and mapping

| d.school 5-stage | IBM Loop 3-activity |
|---|---|
| Empathize | Observe |
| Define | Reflect |
| Ideate | Reflect (Make boundary) |
| Prototype | Make |
| Test | Observe (next loop's input) |

The IBM compression is honest about where the *thinking* happens — at the boundary moments (Reflect → Make, Make → Observe). The d.school 5-stage is better for teaching discrete artifacts; the IBM 3-activity is better for team cadence.

## 3. Tim Brown's three constraints, browser-applied

- **Desirability** — *Does the reviewer actually want this?* Example: a confirm-modal-with-undo for batch-promote-to-Planner is desirable because reviewers fear silently shipping the wrong record.
- **Feasibility** — *Can it be built?* Example: sortable columns in v1.1's table fit the single-file canonical pattern; live-collab cursors don't (need a server).
- **Viability** — *Does it fit the surrounding context?* Example: trust badges fit the data-trust constraint that v1.1 is "structurally valid but not Planner-ready"; an "approve and export to Planner" button doesn't, because the workflow doesn't yet support approval-as-state.

## 4. Iteration jumps — healthy vs evidence-skipping

**Healthy:**
- **Test → Empathize** — testing the prototype with a reviewer surfaces a need we didn't know about; we return to learn more.
- **Prototype → Ideate** — while making, a better candidate becomes visible; we ideate once more before committing.

**Evidence-skipping:**
- **Empathize → Prototype** (jumping over Define + Ideate) — "we already know what to build". The most common practical failure. Commits to the first plausible solution without framing the problem or generating alternatives.

## 5. Evidence per stage + an evidence-free failure for each

| Stage | Evidence | Evidence-free failure |
|---|---|---|
| Empathize | Field notes / interview transcripts / observation summaries | "We talked to some users" — no captured notes; next stage runs on memory + biases |
| Define | POV statement / "how might we" question / problem statement | "The problem is the browser is bad" — non-specific, untestable, doesn't constrain Ideate |
| Ideate | Numbered candidate list | "We brainstormed" — no captured list; next stage picks the obvious one |
| Prototype | The thing itself (sketch, mock, code, video, role-play) | "We described what we'd build" — no tangible artifact; Test runs on imagination |
| Test | Feedback notes / observed behaviour / decisions | "Users liked it" — no captured feedback; next loop has no input |

## 6. Norman's "Useful Myth" critique

Norman argues design thinking risks being a *brand* for what skilled designers already do, and risks *devaluing domain expertise* by implying that the right process substitutes for years of practice. He's not dismissive — he calls it a "useful myth" because the myth gets non-designers to take design seriously — but he warns the myth becomes dangerous when it substitutes for hiring people with real expertise.

**Verdict: sharpens the discipline.** The critique tells the discipline what to defend against: replacing skilled designers with workshop attendance; claiming process substitutes for domain knowledge; treating design thinking as a *solved* method rather than a *continuing* practice. Sources that ignore Norman end up overselling. For CodeMike specifically: design thinking complements deep domain knowledge of the data-review work, it doesn't replace it.

## 7. User need vs POV statement

A **user need** (Topic 3 / GOV.UK form): `As a [reviewer], I need [outcome], so that [goal]` — outcome-shaped, mechanism-free, testable as behaviour. Produced when the user is *known* and the team is moving toward design.

A **POV statement** (Topic 4 / d.school form): `[User] needs a way to [need] because [insight]` — *insight*-shaped, frames the problem with the surprise the team learned during Empathize. Produced when the user is *being learned* and the team is moving toward Ideate.

The POV is the bridge between Empathize (learning) and Ideate (generating). The user-need statement is the bridge between Define (or known research) and Design (criteria-writing). Same intent — avoid solution-shape language — at different points in the loop.

## 8. Single-person-workspace anti-pattern

**Empathy-by-introspection.** In CodeMike's case the same person designs, reviews, and writes criteria. The temptation is to treat self as data ("I am the user"). The risk: the designer-reviewer is *not representative* of the future reviewer pool (a fresher reviewer, a domain-expert reviewer, an accessibility-need reviewer). Mitigation: explicitly synthesise *three personas in writing* — first-time, power, accessibility-need — and let each one's expected experience shape Empathize evidence. Three written personas beat one introspection-of-self.

## 9. Topic 4 first vs Topic 3 first

**Topic 4 first** when the problem isn't well-framed. Example: "reviewers feel slow on Planner-promotion" — *we don't know what makes them slow*. Run an Empathize → Define loop to learn whether it's batch-size cognitive load, trust-assessment friction, or filter friction. Then Topic 3 turns the finding into a criterion.

**Skip to Topic 3** when the problem is well-framed and the user need is known. Example: "the empty state silently fails — fix it" (Lab 03 finding). The need is clear; the criterion (`U-REC-1`: recovery in ≤ 1 interaction) follows directly. A full design-thinking loop here would be ceremony.

The rule: do Topic 4 when the cost of a loop is less than the cost of building the wrong thing. For small, well-framed changes, Topic 3 alone is enough. For large or ambiguous changes, Topic 4 first.

## 10. Design-decision gate before exiting Ideate

> *"Have we generated at least three meaningfully different candidates, AND can each one be evaluated against desirability / feasibility / viability with sourced evidence (not opinions), AND have we written down the comparative reason why the chosen candidate beats the other two?"*

A wrong answer is immediately visible: a single candidate; three near-identical candidates; "we just like this one"; a desirability cell saying "users will love it" with no source; a chosen candidate without a comparative reason. A right answer cites three distinct candidates, a per-candidate triage row with sourced evidence, and a comparative-reasoning sentence — ideally including *what would change our mind* during Test.

## Self-mark

Cross-checked against `quiz-04-design-thinking-answer-key.md`. All ten answers are grounded in the deep-reading doc and at least one Topic 4 source. The two answers that diverge slightly:

- **Q4 (iteration jumps)** — my answer names two healthy jumps (Test→Empathize, Prototype→Ideate) where the key listed three. Equivalent on the evidence-gathering principle.
- **Q9 (Topic 4 vs Topic 3 routing)** — my framing emphasises *cost* of the loop; the key emphasises *whether the problem is well-framed*. Same rule, different vocabulary.

No corrections needed.
