# Reading Pack — Topic 05 Human-centred design

## Required readings

| Source | Role |
|---|---|
| **ISO 9241-210** — *Ergonomics of human-system interaction — Human-centred design for interactive systems* (most recent edition; the 2019 revision is the current canonical version) | Primary standards-grade source. Defines the four-activity lifecycle (Context of use → User requirements → Design solutions → Evaluation) and the six principles every HCD process must embody. The discipline's auditable spec. |
| **Don Norman** — HCD essays at NN/g (*Human-Centered Design Considered Harmful?*; *The Future of Design: When You Come to a Fork in the Road, Take It*; chapter introductions in *The Design of Everyday Things*) | Primary conceptual source. The argument that HCD is the only framing that doesn't drift into "designer-centred design". The honest engagement with the critique that HCD can over-centre individual users at the cost of systems thinking. |
| **IDEO** — *The Field Guide to Human-Centered Design* (HCD-specific chapters: *Mindsets, Methods, Case Studies* — different from Topic 3's journey-mapping chapters and Topic 4's design-thinking method chapters) | Applied / practical source. The most-cited operational handbook for running HCD work in the field; specific methods per activity. |
| **W3C** — *Accessibility, Usability, and Inclusion* (WAI's note on the three overlapping concerns) | Cross-check / standards-grade source. Frames accessibility as *part of* HCD, not separate from it. The argument that the three lenses overlap heavily and that any HCD process must address all three. |

## Extension readings

| Source | Role |
|---|---|
| ISO 9241-11 — *Usability: Definitions and concepts* | The definition of usability that ISO 9241-210 inherits and operationalises. |
| WCAG 2.2 (revisited from Topic 2) — specific success criteria | The technical accessibility requirements that any HCD-evaluated design must meet. |
| Don Norman & Jakob Nielsen — *The Definition of User Experience* (revisited from Topic 1) | The UX scope that HCD's requirements activity must address. |
| Microsoft Inclusive Design Toolkit | A concrete operationalisation of the W3C inclusion lens; useful as a worked example of how to specify inclusion requirements. |
| Jakob Nielsen — *Why You Only Need to Test with 5 Users* | The empirical basis for HCD's *evaluate* activity in practice; how much testing is enough. |
| GOV.UK Service Manual — *Accessibility and assisted digital* chapter | Public-sector operationalisation of W3C's accessibility-as-part-of-HCD framing. |

## Reading questions

1. ISO 9241-210 names four activities and six principles. Walk through each activity and each principle and ask: does the Destination Master Browser v1.1 work satisfy it? Where are the gaps?
2. Norman's *Human-Centered Design Considered Harmful?* makes a specific argument about HCD potentially over-centring the individual user. State the argument and explain how ISO 9241-210's *context of use* activity addresses it.
3. The W3C triad — usability, accessibility, inclusion — overlaps heavily. Where does each of the four required sources land on whether the three are *separate audits* or *three lenses on one audit*?
4. How does HCD differ from design thinking (Topic 4)? Where do they overlap; where does each go that the other doesn't?
5. The six ISO principles include "the design team includes multidisciplinary skills and perspectives". For a single-person workspace, what's the honest mitigation that satisfies the spirit of the principle without faking team-size?
6. Topic 3's UX acceptance-criteria sheet, Topic 4's design-thinking loop, and Topic 2's component rule sheet all produce artifacts. Map each artifact to its ISO 9241-210 activity. Are any activities under-served?
7. Each required source has a position on *evaluation*. Where do they agree, and where do they differ on what "enough evaluation" means?
8. What does each source omit or under-emphasise that the others surface? Compile a per-source omission list.

## Extraction target

The reading should produce:

- topic definition (with verbs); explicit non-definition (what HCD *isn't*)
- the four ISO 9241-210 activities with per-activity artifacts and browser-applied examples
- the six ISO principles with single-person-workspace translation for each
- the W3C accessibility / usability / inclusion triad explained and applied
- source-by-source notes (what each teaches / what it omits / strongest takeaway)
- structured source comparison (agreement table + difference-by-emphasis table + per-source omissions)
- the Norman *HCD Considered Harmful?* critique + how the other sources implicitly respond
- CodeMike interpretation — HCD as the umbrella over Topics 2 / 3 / 4
- application to the Destination Master Browser: HCD audit of v1.1 + Lab 04 Loop 1 against the four activities
- anti-patterns specific to HCD in small-team / single-person workspaces
- implementation implications for the v1.2+ roadmap and for grade-report v3
- further reading + applied exercises
- checklist updates for the master-browser checklist (Topic 5 gates)

## Linked extension

```text
design/foundations/topic-05-hcd-audit.md
```

The Lab 05 output: a full HCD audit of v1.1 (post-PR #12) + Lab 04 Loop 1 against ISO 9241-210's four activities, six principles, and the W3C triad. The audit produces a per-activity evidence table, gap analysis, and a prioritised list of HCD findings to address in v1.2.
