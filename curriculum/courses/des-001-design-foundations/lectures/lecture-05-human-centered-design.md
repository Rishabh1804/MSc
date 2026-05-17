# Lecture 05 — Human-centred design

## Learning objectives

By the end of this lecture, CodeMike should be able to:

- define human-centred design (HCD) as a standards-grade discipline distinct from design thinking and from UX design
- name the **four activities** of ISO 9241-210's HCD lifecycle and explain what each produces
- explain how HCD pairs with Topic 3 (UX criteria) and Topic 4 (design-thinking loops)
- distinguish *user* from *stakeholder* from *operator* — each gets considered in HCD; only the user gets centred
- name the W3C accessibility / usability / inclusion triad and explain why accessibility is a *precondition* of HCD, not a feature of it
- engage Norman's argument that HCD is the only framing that doesn't drift into "designer-centred design"
- run an HCD audit of a product against the four ISO activities + the W3C inclusion triad

## Core distinction

Human-centred design is the **standards-grade discipline** of designing interactive systems so that they fit the human, not the other way around. It is defined formally by **ISO 9241-210** as a four-activity lifecycle:

```text
1. Understand and specify the CONTEXT OF USE
2. Specify the USER REQUIREMENTS
3. Produce DESIGN SOLUTIONS that meet those requirements
4. EVALUATE the designs against the requirements
```

The lifecycle is **iterative**: outputs of Evaluate feed back into Context-of-use; outputs of any stage can trigger a return to any earlier stage.

HCD is distinct from neighbouring disciplines:

- **vs Topic 3 (UX design)**: UX design is the *practice* of producing journey maps + acceptance criteria. HCD is the *standards-grade frame* that names the four activities and ensures every UX project includes all four. Topic 3 is "we wrote criteria"; HCD is "we wrote criteria AND named the context, requirements, and evaluation cycle".
- **vs Topic 4 (Design thinking)**: Design thinking is the *iterative loop* run when the problem isn't well-framed. HCD is the *lifecycle frame* that runs around all design work — including design-thinking loops. Topic 4 is "we ran a loop"; HCD is "we ran a loop within a lifecycle that ensures context-of-use is properly understood".
- **vs Topic 2 (UI design)**: UI design is the substrate. HCD is the discipline that ensures the substrate is correct for the user *in their context*.

HCD is **the umbrella**. Topics 2, 3, 4 are sub-disciplines that operate within it. The standards-grade framing matters because it makes the lifecycle *auditable* — the four activities can be checked off, not just declared.

## The four ISO 9241-210 activities

| Activity | What it answers | Artifact it produces |
|---|---|---|
| **Understand the context of use** | Who is the user? What are they doing? Where? With what equipment? Under what constraints? | Context-of-use description, environmental and technical constraints, task descriptions |
| **Specify the user requirements** | What must the system enable the user to achieve? At what cost? With what accessibility? | User-need statements, usability + accessibility requirements, success criteria |
| **Produce design solutions** | What designs would meet those requirements? | Wireframes, prototypes, specifications, implementations |
| **Evaluate against requirements** | Does the design meet the requirements when tested with real users in the actual context? | Evaluation reports, identified gaps, prioritised changes |

ISO 9241-210 names six principles that any HCD process must embody:

1. The design is based on an explicit understanding of users, tasks, and environments
2. Users are involved throughout design and development
3. The design is driven and refined by user-centred evaluation
4. The process is iterative
5. The design addresses the whole user experience
6. The design team includes multidisciplinary skills and perspectives

For a single-person workspace (CodeMike), the six principles still apply — they translate, they don't disappear. Principle 6 (multidisciplinary) is the most stretched in solo work; mitigation is to consciously adopt different lenses (designer / engineer / domain-reviewer / accessibility-need user) when running the loop.

## The W3C accessibility / usability / inclusion triad

W3C's *Accessibility, Usability, and Inclusion* note frames three overlapping concerns:

- **Usability**: the design works for *most* users in *typical* contexts
- **Accessibility**: the design works for users with *disabilities* (including assistive technology)
- **Inclusion**: the design works across the *full diversity* of users (language, culture, age, device, context, ability)

The three overlap heavily. A design that is *only* usable for the typical case can be inaccessible. A design that meets accessibility standards but ignores typical-case usability is technically compliant but practically poor. HCD requires *all three* — they're not three separate audits, they're three lenses on the same system.

**For DES-001**: accessibility is a *precondition* of HCD, not a feature of it. A design that fails accessibility has failed HCD's *user requirements* activity (which must specify accessibility requirements) and HCD's *evaluation* activity (which must test with accessibility users). The browser's drawer `role="dialog"` + `aria-modal="false"` + `aria-describedby` work (PR #12) is HCD work, not UI polish.

## CodeMike interpretation — where HCD sits

The four DES-001 design topics fit a clear hierarchy:

```text
Topic 5 — HCD (the umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   └─ Topic 2 — UI design (the components)

Every Topic 2/3/4 artifact should map to at least one ISO 9241-210 activity:

   Context-of-use            → Topic 3 §6 user-need extraction
   User requirements         → Topic 3 acceptance-criteria sheet
   Design solutions          → Topic 2 rule sheet + Topic 4 loop prototypes
   Evaluate                  → Topic 3 walkthrough + Topic 4 falsification criteria
```

The HCD frame's value isn't *new artifacts*; it's the *audit* that ensures every artifact ties back to the lifecycle, and that nothing is missing. An HCD audit of v1.1 (the lab work) tests the workspace's discipline against ISO's checklist.

## Common misconception

The most common misconception about HCD is that it's a *workshop* or a *methodology*. ISO 9241-210 is neither — it's a **lifecycle specification**. It says nothing about which methods to use (interviews vs surveys vs ethnography vs introspection); it says what *must be done* (context-of-use understood; requirements specified; designs produced; evaluations run). Different teams use different methods; all of them satisfy the same lifecycle.

The discipline is *what activity each artifact serves*, not *which method produced it*.

## Application to the Destination Master Browser

Lab 05 runs an HCD audit of v1.1 + Lab 04 Loop 1 against the four ISO activities. Per the execution plan:

```text
Who is the user?                 — Reviewer (with three personas from Topic 4)
What is the context of use?      — Internal QA review against destinations_master_v2.csv
What are the requirements?       — The 14 UX acceptance criteria + Topic 2 component rules
What does evaluation look like?  — The 19-gate Playwright walk-through + future Sponsor Reviewer
```

The audit will surface what's strong, what's missing, and which W3C-triad lens is least well-served. v1.1 is the test case; v1.2 work inherits the findings.

## Discussion questions

1. ISO 9241-210 names six principles. Which is the most stretched in a single-person workspace, and what's the honest mitigation?
2. The W3C triad (usability / accessibility / inclusion) overlaps heavily but isn't identical. Give one example of a design that is usable + accessible but not inclusive.
3. Topic 4 (design thinking) runs *within* HCD's lifecycle. Which of the four ISO activities does a Topic 4 loop primarily exercise? Which one(s) does it under-serve, requiring HCD discipline to compensate?
4. Norman's argument is that HCD is the only framing that doesn't drift into designer-centred design. What specific drift does each of Topics 2 / 3 / 4 risk that HCD's audit catches?
5. v1.1 was tested via the 19-gate Playwright walkthrough. Against ISO's *evaluate* activity, what's missing from that as an HCD evaluation, and what would close the gap?
6. The Destination Master Browser's user is "the reviewer" — but reviewers vary (first-time / power / accessibility-need; three personas from Topic 4). What does HCD say about whose context-of-use to centre when contexts diverge?
7. Run a quick three-line HCD self-audit on one v1.2 candidate (your choice): does each of the four ISO activities have an artifact? Where's the gap?

## Key takeaway

Human-centred design is the **standards-grade lifecycle** (ISO 9241-210, four activities, six principles) that wraps every other design discipline. Its value isn't new artifacts; it's the *audit discipline* that ensures every artifact serves one of the four activities and that no activity is silently skipped. For the Destination Master Browser, HCD is the frame that turns "we did design work" into "we did design work that satisfies a standards-grade lifecycle and we can show you the evidence per activity".
