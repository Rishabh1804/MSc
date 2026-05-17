# Lecture 06 — Gestalt principles

## Learning objectives

By the end of this lecture, CodeMike should be able to:

- explain what the Gestalt psychologists discovered about visual perception (Wertheimer, Koffka, Köhler), and why the original research still constrains modern UI design 100+ years later
- name and apply the **six core Gestalt principles** commonly used in interface design (proximity, similarity, continuity, closure, common region, common fate)
- identify a *Gestalt violation* in a UI: when the visual arrangement implies a relationship that doesn't exist, or hides a relationship that does
- run a Gestalt audit of a screen against the six principles, marking each violation against a specific v1.1 fix
- distinguish Gestalt principles (perceptual) from Topic 2's component rules (compositional) and Topic 3's UX criteria (behavioural)
- engage the critique that Gestalt principles can become *aesthetic rules of thumb* rather than *perceptual constraints*

## Core distinction

Gestalt principles are **perceptual constraints on how the human visual system groups visual elements**. They were discovered experimentally by the Berlin-school Gestalt psychologists in the early 20th century (Wertheimer's 1912 paper on apparent motion is often cited as the founding moment) and have been validated repeatedly since. They are not opinions, conventions, or aesthetic preferences — they are facts about human perception that any visual interface must accommodate.

The fundamental Gestalt claim, the *Prägnanz* principle (translated as "good figure" or "good form"):

> The visual system organises perception toward the simplest, most stable, most symmetric interpretation available.

Every specific Gestalt principle is a corollary of *Prägnanz*. The visual system prefers to perceive groups, continuities, closed shapes, and shared properties — because perceiving them is computationally cheaper than perceiving everything as isolated parts.

For UI design, this means: **the human will perceive grouping whether you intended it or not**. If two visual elements are close together, the user will perceive them as related. If two are visually similar, the user will perceive them as belonging to the same category. The designer's job is to make perceived grouping match intended grouping.

A *Gestalt violation* is the gap between the two: the visual arrangement implies a relationship that doesn't exist (false positive — user expects related elements to behave together but they don't), or hides a relationship that does (false negative — user fails to see that two elements are related).

Gestalt is distinct from neighbouring disciplines:

- **vs Topic 2 (UI design — components)**: components are *compositional* (which elements appear); Gestalt is *perceptual* (how those elements are visually grouped by the viewer's perception system).
- **vs Topic 3 (UX design — criteria)**: UX criteria are *behavioural* (what the reviewer can do); Gestalt is the perceptual layer that determines whether the visual arrangement helps or hinders the behaviour.
- **vs Topic 7 (Fitts' law — future)**: both are *perceptual constraints*; Fitts is about pointing-task time as a function of distance/size; Gestalt is about grouping.

Gestalt is a *constraint layer* underneath both component and behaviour layers. A design that satisfies Topic 2 + Topic 3 but violates Gestalt principles will *behave* correctly but *feel* wrong — the user will mis-read the visual hierarchy and have to consciously correct their initial perception.

## The six core Gestalt principles for interface design

| # | Principle | What it says | UI consequence |
|---:|---|---|---|
| 1 | **Proximity** | Elements close together are perceived as a group | Spacing is meaning. White space between unrelated elements; tight space within related ones. |
| 2 | **Similarity** | Elements that share visual properties (colour, shape, size, font) are perceived as related | Visual similarity implies functional similarity. Use it for category; break it for distinction. |
| 3 | **Continuity** | The eye follows the smoothest path; aligned elements are perceived as a continuous group | Alignment is structure. Mis-aligned elements signal "different category"; aligned signals "part of the same set". |
| 4 | **Closure** | The eye completes incomplete shapes into recognisable wholes | Partial information triggers completion. A frame with one open side is still perceived as a frame. |
| 5 | **Common region** | Elements within a bounded area are perceived as a group | A card, panel, or bordered region creates a perceived group regardless of element similarity. |
| 6 | **Common fate** | Elements that move together are perceived as a group | Motion is grouping. Animation that moves two elements together implies relationship. |

Additional principles sometimes cited (figure/ground, symmetry, parallelism, focal point) refine the six above but don't add fundamentally different perceptual rules.

## CodeMike interpretation — Gestalt as the perceptual constraint layer

For the CodeMike workspace, Gestalt sits at the layer where Topic 2's component choices and Topic 3's behavioural criteria *meet the user's eye*. The component rule sheet says *which components appear*; the acceptance-criteria sheet says *what behaviours those components must produce*; Gestalt says *how the visual arrangement of those components will be perceived* — and where the perception diverges from the intention.

The canonical hierarchy now extends:

```text
Topic 5 — HCD (the umbrella; ISO 9241-210 + W3C triad)
   ├─ Topic 4 — Design thinking (the loop, when problem isn't well-framed)
   ├─ Topic 3 — UX design (the criteria + journey)
   ├─ Topic 2 — UI design (the components)
   └─ Topic 6 — Gestalt (the perceptual constraint layer underneath the visual treatment of Topic 2's components)
```

Topic 6 doesn't replace Topic 2's component rules; it adds a *perceptual audit* to them. A well-specified component (Topic 2) implemented correctly (the build) can still violate Gestalt if its visual treatment groups elements wrongly.

## Common misconception

The most common misconception is that Gestalt principles are *aesthetic rules of thumb* — "use whitespace generously", "align things". Stated that way, they sound like style advice. They aren't — they're constraints on what the human perceptual system *will* do regardless of designer intent. A design that ignores them produces a screen where the user *will* mis-perceive grouping; the question is only whether the designer designed the mis-perception deliberately or accidentally.

The discipline: when a Gestalt principle conflicts with another constraint (component placement, content density, screen size), name the conflict explicitly and document the resolution. Silent violation is the failure mode; explicit trade-off is acceptable.

## Application to the Destination Master Browser

For DES-001, Lab 06 will run a Gestalt audit of v1.1 against the six principles, focusing on the screen regions where grouping signals carry the most weight:

- **Cards view**: do related fields group via proximity? Are statuses + badges similar enough to be perceived as belonging to the same category?
- **Table view**: do columns align (continuity)? Do row separators establish common region without overwhelming?
- **Toolbar**: is the active-filter summary perceived as a group separate from the toolbar controls?
- **Trust banner + stats**: do they read as a system-status group (common region), or do they bleed into the header content?
- **Drawer**: does the drawer header + trust banner + body read as a single information unit (proximity + common region)?

The audit produces a per-region violation list and a v1.1.x / v1.2 fix list.

## Discussion questions

1. The Gestalt psychologists worked in the 1910s–1930s on still-image and motion experiments. Why do their findings still constrain modern UI design 100 years later?
2. The *Prägnanz* principle says the visual system prefers the simplest interpretation. Where in v1.1 is the simplest interpretation *also* the correct interpretation? Where might the simplest interpretation mislead the reviewer?
3. The six principles can conflict: proximity says "group these"; similarity says "these aren't grouped". When they conflict, which one wins, and why?
4. Gestalt principles are *perceptual constraints*, not aesthetic rules. What's the operational difference between treating them as one vs the other?
5. Topic 2's component rule sheet specifies *which components exist*; Gestalt audits *how those components are visually grouped*. Give one v1.1 component whose Topic 2 specification is correct but whose Gestalt treatment could be improved.
6. The execution plan flags Topic 6 as "moderate effort" (~4–5h, smaller than Topic 4/5). Why is Topic 6 lighter despite being a fundamental constraint? What does the smaller size *not* let the topic cover?
7. The critique that Gestalt principles can become "aesthetic rules of thumb" — defend or attack. Cite either way.

## Key takeaway

Gestalt principles are **perceptual constraints** — facts about how the human visual system groups visual elements regardless of designer intent. The six core principles (proximity, similarity, continuity, closure, common region, common fate) are the most-used in interface design. A Gestalt violation is the gap between perceived and intended grouping; the audit's job is to find the gaps. Gestalt sits *underneath* Topic 2's component rules — Topic 2 says which components; Gestalt audits how they will be perceived together.
