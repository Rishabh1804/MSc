# Quiz 05 — Answer Key

Guideline answers. A response that says the same thing differently — particularly grounded in the Destination Master Browser — scores equally.

## 1. Definition + distinction

HCD is the **standards-grade lifecycle** (ISO 9241-210) of designing interactive systems so that they fit the human, not the other way around. It is defined as a four-activity iterative cycle (Context of use → User requirements → Design solutions → Evaluation) governed by six principles. It is **not** a workshop, a methodology, or a single technique — it is a *lifecycle specification* that says what must be done, not how. Distinct from design thinking (the *loop run within HCD when problems aren't well-framed*) and from UX design (the *practice of producing journey maps + criteria that satisfies HCD's user-requirements activity*).

## 2. Four ISO 9241-210 activities + artifacts

| Activity | Artifact |
|---|---|
| Understand the context of use | Context-of-use description, environmental + technical constraints, task descriptions |
| Specify the user requirements | User-need statements, usability + accessibility requirements, success criteria |
| Produce design solutions | Wireframes, prototypes, specifications, implementations |
| Evaluate against requirements | Evaluation reports, identified gaps, prioritised changes |

The lifecycle is iterative; outputs of Evaluate feed back into Context-of-use.

## 3. Three principles + single-person translation

- **Principle 2** (Users involved throughout): solo workspace = three-persona synthesis (first-time/power/accessibility-need) as the substitute; *honest mitigation* names the limitation that no real users have been involved yet.
- **Principle 4** (Process is iterative): solo workspace inherits naturally — the work happens across PRs and the loop continues. Same discipline as ISO; just no team to convene per iteration.
- **Principle 6** (Multidisciplinary team): solo workspace's most-stretched principle. Translation = consciously adopt different lenses (designer / engineer / domain-reviewer / accessibility-need user) within one person. Lab 04's three-persona synthesis is the worked example.

Other valid choices:
- Principle 1 (Explicit understanding) → three-persona synthesis fills the explicit-understanding role
- Principle 3 (User-centred evaluation) → Playwright walkthrough + future Sponsor Reviewer
- Principle 5 (Whole UX) → the four-depth trust signal + the seven-step journey already address this

## 4. W3C triad + non-inclusive example

The triad: **usability** (works for typical users in typical contexts), **accessibility** (works for users with disabilities), **inclusion** (works across the full diversity of users — language, culture, age, device, context, ability).

Non-inclusive example (usable + accessible but not inclusive): the v1.1 browser today. Usable for a English-speaking reviewer on a desktop. Accessible (focus rings, ARIA, keyboard nav, screen-reader support post-PR #12). But not yet *inclusive*: copy is only in English; reviewer-role assumed to be familiar with terms like "Planner-ready" and "verified" without explanation; no consideration for low-bandwidth contexts; mobile layout exists but isn't tested as a primary use case.

## 5. Canonical hierarchy

```text
Topic 5 — HCD (umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   └─ Topic 2 — UI design (the components)
```

HCD is the lifecycle spec; Topics 2/3/4 are sub-disciplines that produce artifacts mapping to HCD's four activities. Every Topic 2/3/4 artifact serves at least one ISO activity.

## 6. Norman's *HCD Considered Harmful?* critique

Norman argues that HCD risks over-centring the *individual* user at the cost of *systems thinking* — the systems within which the user operates (their team, their workflow, their organisational context) can be more important than the individual experience. He's not arguing against HCD; he's warning that "centring the user" can blind designers to the wider system the user inhabits.

ISO 9241-210's **context-of-use** activity addresses this directly. The activity isn't just "describe the user"; it's "understand and specify the *context*" — which includes the user's task, their environment, their equipment, their organisational constraints, and the system the user interacts with. A context-of-use description that's only "the user is a reviewer" is incomplete; a full context-of-use names the reviewer's organisation, workflow, downstream consumers (Planner), and the asymmetric-cost constraint (from Lab 04). Done properly, the context-of-use activity *is* the systems-thinking Norman argues for.

## 7. Artifact-to-activity mapping

| Artifact | ISO activity |
|---|---|
| Topic 3 §6 user-need extraction (`design/foundations/topic-03-ux-design-journey-map.md` §Step 3) | Context of use + Specify user requirements |
| Topic 3 `ux-acceptance-criteria.md` (14 criteria) | Specify user requirements |
| Topic 2 `ui-design-component-rules.md` (rule sheet) | Produce design solutions |
| Topic 4 Lab 04 Loop 1 output (`topic-04-design-thinking-loop.md`) | Loop runs across all four activities (Empathize→Context; Define→Requirements; Ideate+Prototype→Design solutions; Test spec→Evaluate) |
| v1.1 `destination-master-browser.html` | Produce design solutions (the implementation) |
| 19-gate Playwright walkthrough | Evaluate (machine-grade; future Sponsor Reviewer adds human-grade) |

**Under-served activities**: Evaluate at the *human* level (no real users have tested v1.1 yet). Context-of-use at the *systems* level (the workflow downstream — what Planner does with promoted records — is documented in passing but not as a full context-of-use specification).

## 8. Which context-of-use to centre when contexts diverge

ISO 9241-210 says you specify **all relevant contexts of use**, not just one. The three reviewer personas (first-time / power / accessibility-need) all get their context described; the design must serve all three. Lab 04 §2's three-persona synthesis and its convergence finding ("the modal must work for any-N batches") is HCD-compliant: it centred all three contexts and found the requirement that serves all of them.

When contexts genuinely conflict (a feature good for the power user is bad for the first-time user), HCD says: name the conflict explicitly, choose the resolution with a documented reason (often: serve the *most-vulnerable* user, then *layer* additional affordances for other users). HCD's discipline is to make the trade-off visible rather than to silently optimise for one persona.

## 9. HCD anti-pattern for single-person workspaces

**Treating self as user (introspection-as-context)**. The solo designer fills in *context of use* by writing what they themselves do, which collapses HCD's four activities into one (the designer's own experience). Even with three-persona synthesis (Topic 4 mitigation), the synthesis is *the designer's imagination of three personas*, not real users in real contexts.

The honest mitigation is to *name* the limitation explicitly in the context-of-use description: "the v1.1 context of use is synthesised from designer introspection + three imagined personas; real Sponsor Reviewer testing is the next milestone." Naming the limitation is HCD-compliant; pretending it isn't there is not.

Other valid anti-patterns:
- Skipping the *evaluate* activity ("we shipped, that's enough") — common in solo workspaces with no team to demo to.
- Treating accessibility as a post-hoc audit rather than a *user requirement* set during Activity 2.
- Defining the user as "the user" without naming personas, contexts, or task differences.
- Confusing *user requirements* (what the user must be able to do) with *features* (what the system has).

## 10. HCD self-audit gate

> *"For this v1.2 backlog item, can I name (a) the context of use it serves, (b) the user requirement it satisfies, (c) the design solution shape, and (d) the evaluation that would confirm it works? If any of the four is empty, the item is not yet HCD-ready — return it to the activity that's missing."*

A wrong answer is immediately visible: any empty cell. A right answer cites concrete sources for each cell: context-of-use from the three-persona synthesis; user-requirement in GOV.UK form (Topic 3); design-solution shape in the rule sheet (Topic 2) or a Lab 04 loop output; evaluation as a walkthrough criterion + a falsification trigger.

The gate's value is that it *can't* be passed by a backlog item that skipped an HCD activity. It enforces the lifecycle at the per-item level.
