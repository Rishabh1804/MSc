# Quiz 05 — Answers

Answer date: 2026-05-17. Written from the lecture, the four required Topic 5 sources, and the deep-reading doc at `design/foundations/topic-05-hcd.md`, then cross-checked against `quiz-05-human-centered-design-answer-key.md`. Examples are drawn from the Destination Master Browser v1.1.

## 1. Definition + distinction

HCD is the **standards-grade lifecycle** (ISO 9241-210) of designing interactive systems so that they fit the human, not the other way around. Defined as a four-activity iterative cycle (Context of use → User requirements → Design solutions → Evaluation) governed by six principles, and paired with the W3C accessibility / usability / inclusion triad. It is **not** a workshop, a methodology, or a single technique — it's a lifecycle specification that says what must be done, not how.

Distinct from design thinking (Topic 4): design thinking is the *loop* run within HCD when the problem isn't well-framed; HCD is the lifecycle the loop sits inside. Distinct from UX design (Topic 3): UX design *produces artifacts* (journey + criteria); HCD *audits* whether those artifacts satisfy a standards-grade lifecycle.

## 2. Four ISO 9241-210 activities + artifacts

| Activity | Artifact |
|---|---|
| Understand the context of use | Context-of-use description, environmental + technical constraints, task descriptions |
| Specify the user requirements | User-need statements (GOV.UK form), usability + accessibility requirements, success criteria |
| Produce design solutions | Wireframes, prototypes, specifications, implementations |
| Evaluate against requirements | Evaluation reports, identified gaps, prioritised changes |

The lifecycle is iterative; outputs of Evaluate feed back into Context-of-use.

## 3. Three principles + single-person translation

- **Principle 1** (Explicit understanding of users, tasks, environments): solo workspace = three-persona synthesis (first-time / power / accessibility-need) as the explicit-understanding substitute; *honestly name* that no real users have been involved yet.
- **Principle 3** (User-centred evaluation): solo workspace = machine-grade walkthrough (the 19-gate Playwright run) as the lower bound; *honestly name* that human-grade evaluation is the gap to close in v1.2 once a Sponsor Reviewer is recruited.
- **Principle 6** (Multidisciplinary team): solo workspace's most-stretched principle. Translation = consciously adopt different lenses (designer / engineer / domain-reviewer / accessibility-need user) within one person. The Lab 04 three-persona synthesis is the worked example. *Honestly name* the limitation that the same person plays all roles.

Each translation works when the limitation is named explicitly. Pretending the principle is fully satisfied when it isn't is HCD non-compliance.

## 4. W3C triad + non-inclusive example

The triad: **usability** (works for typical users in typical contexts), **accessibility** (works for users with disabilities), **inclusion** (works across the full diversity of users — language, culture, age, device, context, ability).

Non-inclusive example: the v1.1 Destination Master Browser today. Usable for an English-speaking reviewer on desktop. Accessible (focus rings, ARIA, keyboard nav, screen-reader support post-PR #12). But not yet inclusive: copy only in English; reviewer-role assumed to know terms like "Planner-ready" and "verified" without explanation; no consideration for low-bandwidth contexts; mobile layout exists but isn't tested as a primary use case.

## 5. Canonical hierarchy

```text
Topic 5 — HCD (the umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   └─ Topic 2 — UI design (the components)
```

HCD is the lifecycle spec; Topics 2/3/4 are sub-disciplines that produce artifacts mapping to HCD's four activities. Every Topic 2/3/4 artifact serves at least one ISO activity.

## 6. Norman's *HCD Considered Harmful?* critique

Norman argues that HCD risks **over-centring the individual user at the cost of systems thinking**. The user is embedded in a larger system (team, workflow, organisation, downstream consumers); designing for the individual without designing for the system can produce locally-optimal, globally-suboptimal designs.

ISO 9241-210's **context-of-use** activity addresses this directly. The activity isn't "describe the user"; it's "understand and specify the *context*" — which includes the user's organisation, workflow, equipment, downstream consumers, and the system the user interacts with. Done properly, the context-of-use activity *is* the systems-thinking Norman argues for. A context-of-use description that's only "the user is a reviewer" is incomplete; a full one names the Planner downstream, the data-engineering team upstream, and the asymmetric-cost constraint (from Lab 04) the reviewer operates under.

## 7. Artifact-to-activity mapping

| Artifact | ISO activity |
|---|---|
| Topic 2 `ui-design-component-rules.md` | Produce design solutions |
| Topic 3 `ux-acceptance-criteria.md` | Specify user requirements |
| Topic 4 Loop 1 output (`topic-04-design-thinking-loop.md`) | All four activities, compressed into one loop |
| v1.1 implementation (`destination-master-browser.html`) | Produce design solutions |

**Under-served activities** in v1.1:
- *Context of use* at the **systems** level (Norman territory) — the workflow downstream of the browser is documented in passing but not as a full context-of-use specification
- *Evaluation* at the **human** level — no real users have tested v1.1; only the machine-grade 19-gate walkthrough exists

Both gaps are honest; v1.2 work + Sponsor Reviewer recruitment closes them.

## 8. Whose context-of-use to centre when contexts diverge

ISO 9241-210 says you specify **all relevant contexts of use**, not just one. The three reviewer personas (first-time / power / accessibility-need) all get their context described; the design must serve all three. Lab 04 §2's three-persona synthesis and its convergence finding ("the modal must work for any-N batches from the start") is HCD-compliant: it centred all three contexts and found the requirement that serves all of them.

When contexts genuinely conflict (a feature good for the power user is bad for the first-time user), HCD says: name the conflict explicitly, choose the resolution with a documented reason (often: serve the *most-vulnerable* user, then *layer* additional affordances for other users). HCD's discipline is to make the trade-off visible rather than to silently optimise for one persona.

## 9. HCD anti-pattern for single-person workspaces

**Treating self as user (introspection-as-context).** The solo designer fills in *context of use* by writing what they themselves do, which collapses HCD's four activities into one (the designer's own experience). Even with three-persona synthesis (Topic 4 mitigation), the synthesis is the designer's *imagination* of three personas, not real users in real contexts.

The honest mitigation is to *name* the limitation explicitly in the context-of-use description: "the v1.1 context of use is synthesised from designer introspection + three imagined personas; real Sponsor Reviewer testing is the next milestone." Naming the limitation is HCD-compliant; pretending it isn't there is not.

Other valid anti-patterns: skipping the *evaluate* activity ("we shipped, that's enough"); treating accessibility as a post-hoc audit rather than a user requirement; defining the user as "the user" without naming personas.

## 10. HCD self-audit gate for every v1.2 backlog item

> *"For this v1.2 backlog item, can I name (a) the context of use it serves, (b) the user requirement it satisfies, (c) the design solution shape, and (d) the evaluation that would confirm it works? If any of the four cells is empty, the item is not yet HCD-ready — return it to the activity that's missing."*

A wrong answer is immediately visible: any empty cell. A right answer cites concrete sources for each cell: context-of-use from the three-persona synthesis; user-requirement in GOV.UK form (Topic 3); design-solution shape in the rule sheet (Topic 2) or a Lab 04 loop output; evaluation as a walkthrough criterion + a falsification trigger.

The gate's value is that it *can't* be passed by a backlog item that skipped an HCD activity. It enforces the lifecycle at the per-item level.

## Self-mark

Cross-checked against `quiz-05-human-centered-design-answer-key.md`. All ten answers are grounded in the deep-reading doc and at least one Topic 5 source. The answers diverge slightly from the key on Q3 (I selected Principles 1, 3, 6 — the most-stretched ones for solo work; the key uses 2, 4, 6 — equally valid choices). No corrections needed.
