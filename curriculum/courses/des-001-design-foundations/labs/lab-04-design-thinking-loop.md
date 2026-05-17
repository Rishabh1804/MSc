# Lab 04 — Design Thinking Loop (single pain-point end-to-end)

## Lab objective

Run **one full design-thinking loop** (Empathize → Define → Ideate → Prototype → Test) on a single Destination Master Browser pain point, producing evidence at every stage. The lab demonstrates the process discipline Topic 4 specifies, not the *result* of running design thinking at scale. One loop, well-evidenced, beats five loops half-done.

Target artifact:

```text
docs/destination-master-browser.html  (canonical v1.1; loop's pain-point lives in this build)
```

## Materials

- `curriculum/courses/des-001-design-foundations/lectures/lecture-04-design-thinking.md`
- `curriculum/courses/des-001-design-foundations/readings/topic-04-design-thinking-reading-pack.md`
- `design/foundations/topic-04-design-thinking.md` (deep-reading doc, PR A)
- Lab 01 findings (`design/foundations/topic-01-ui-vs-ux-exercise-results.md`) — source of candidate pain points
- Topic 2 rule sheet + Topic 3 acceptance-criteria sheet — to triage outputs against existing v1.1 commitments

## Lab steps

### Step 1 — Pick the pain point

Choose **one** v1.1 / v1.2-scope pain point from Lab 01 or v1.1 walk-through findings. The pain point must be:

- Sized to fit one loop (one decision-shaped problem, not "the browser is bad")
- Not already fully resolved by v1.1's shipped components (would be ceremony)
- Not so large that it requires v1.2's full backlog (would not finish in one loop)

Record the choice + the rejection rationale for two other candidate pain points (so the choice is visible, not implicit).

### Step 2 — Empathize

Produce field notes about the reviewer experiencing this pain point. Acceptable forms in the single-person workspace:

- *Introspection note*: what I, as the designer-reviewer, experience when I hit this pain point
- *Three-persona synthesis*: imagined first-time reviewer + imagined power-reviewer + imagined accessibility-need reviewer; what each would experience
- *Adjacent-tool comparison*: how does a tool I admire handle this pain point? (Linear, Notion, GitHub PR review, Carbon's data table)

Output: 100–300 words of captured observation, *not* "I thought about it". Three perspectives minimum.

### Step 3 — Define

Frame the pain point as a **POV statement** in the d.school form:

```text
[User] needs a way to [need] because [insight].
```

Plus one or two "how might we" (HMW) questions that open the problem for Ideate without naming the solution.

The Define output is the most under-done stage in practice. Spend disproportionate time here: re-write the POV statement at least twice. Each re-write should sharpen the *insight* (the surprise the team learned in Empathize).

### Step 4 — Ideate

Generate at least **three meaningfully different** candidate solutions. *Meaningfully different* means: not three variants of the same approach. If all three candidates are "add a button somewhere", they aren't meaningfully different.

For each candidate, record one or two lines per candidate. Candidate descriptions should be component-light, behaviour-heavy.

### Step 5 — Triage with the three constraints

Run each candidate through Tim Brown's three-constraint filter:

| Candidate | Desirability | Feasibility | Viability | Verdict |
|---|---|---|---|---|
| 1 | … | … | … | proceed / refine / drop |
| 2 | … | … | … | … |
| 3 | … | … | … | … |

Pick **one** candidate to Prototype. Record the comparative reason ("Candidate 2 over Candidate 1 because …"). If no candidate clearly wins, return to Ideate.

### Step 6 — Prototype

Make the chosen candidate concrete. Choose the cheapest form that lets a tester evaluate it:

- A written walkthrough (numbered interaction script + expected UI states)
- A simple sketch (ASCII / Markdown table of the UI states)
- A small inline HTML snippet (only if the cost is low)
- A role-play script (for interactions that involve more than one screen)

The prototype's job is to be cheap enough to throw away. **Do not build the production version here.** That's v1.2 implementation work, not Lab 04 scope.

### Step 7 — Test (specification)

Specify the test even if the lab doesn't run it on a real reviewer (real-reviewer test = future v1.2 user-testing). The test specification must include:

- *Who* would test (which persona, why)
- *What task* they would attempt (one observable task)
- *What we'd watch for* (success / time / errors / where they got stuck)
- *What would change our mind* — explicit falsification criteria. "If the reviewer takes > 30s to find X" → re-frame. "If two reviewers prefer Candidate 2's approach" → re-think the chosen candidate.

A test without falsification criteria is a rubber-stamp, not a test.

### Step 8 — Loop result and decision

Close the loop with three lines:

- **What changed in our understanding** — one sentence about what we now know that we didn't before the loop
- **What the next loop would do** — if this loop produced "we should test with real reviewers", say so; if it produced "the chosen candidate is ready for Topic 3 criteria-writing", say so
- **Decision** — Ship to v1.2 backlog (with handoff note to Topic 3 / Topic 2) / Re-run the loop / Defer (with reason)

## Expected outputs

```text
design/foundations/topic-04-design-thinking-loop.md
  ├─ Step 1: pain-point choice + two-rejection rationale
  ├─ Step 2: Empathize evidence (3-perspective synthesis)
  ├─ Step 3: POV + HMW
  ├─ Step 4: ≥3 candidate solutions
  ├─ Step 5: triage table
  ├─ Step 6: prototype (cheap form)
  ├─ Step 7: test specification with falsification criteria
  └─ Step 8: loop result + decision

curriculum/courses/des-001-design-foundations/submissions/
  lab-04-design-thinking-loop-results.md
    Formal lab submission with exec summary, key findings, decision-gate
    satisfaction, and four reusable design capabilities extracted (or note
    that no new capabilities emerged — both are honest outcomes).

design/checklists/master-browser-design-checklist.md
  Topic 4 section appended (§23 + §24): gates + anti-patterns.
```

## Submission checklist

- [ ] Pain point picked + two-rejection rationale recorded (Step 1)
- [ ] Empathize evidence at 100–300 words, three perspectives minimum (Step 2)
- [ ] POV statement + ≥1 HMW question; POV rewritten at least twice (Step 3)
- [ ] ≥3 meaningfully different candidates (Step 4)
- [ ] Triage table with comparative reasoning (Step 5)
- [ ] Prototype in a cheap form, not production code (Step 6)
- [ ] Test specification with explicit falsification criteria (Step 7)
- [ ] Loop result + decision (Step 8)
- [ ] Master-browser checklist Topic 4 section appended

## Rubric alignment

- *Multi-source coverage* — every loop stage cites the source(s) that constrain it
- *Application to CodeMike/browser* — the loop runs against a real browser pain point, not a hypothetical
- *Checklist/actionability* — outputs feed into v1.2 backlog or back into Topic 3 criteria-writing
- *Academic discipline* — the loop is versioned (Loop 1) so future loops can be tracked

## Decision gate before closing the lab

Lab 04 is complete when:

1. Every stage has produced its evidence artifact (no evidence-free stages)
2. The Ideate stage produced ≥ 3 meaningfully different candidates
3. The triage shows comparative reasoning, not "we picked this one"
4. The Test specification names explicit falsification criteria
5. The loop's decision is one of {Ship / Re-run / Defer} with a reason

Failure on any of these means re-run the relevant stage. This is the *evidence-per-stage* discipline Topic 4 insists on.
