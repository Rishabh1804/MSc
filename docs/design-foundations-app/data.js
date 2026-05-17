window.DES001_PENDING_NOTES = {
  summary: 'Pending deep reading. Source scaffold is present, but the topic is not yet considered digested.',
  principles: ['Read all listed sources before extracting principles.'],
  comparison: 'Pending source comparison.',
  disagreements: 'Pending disagreement and emphasis analysis.',
  interpretation: 'Pending CodeMike interpretation.',
  application: 'Pending browser-specific application.',
  antiPatterns: ['Do not implement this topic before the deep-reading notes exist.'],
  implementation: ['No implementation implications accepted yet.'],
  checklist: ['No checklist update yet.']
};

window.DES001_TOPICS = [
  {
    title: 'UI vs UX',
    status: 'done',
    summary: 'Distinguishes the interface layer from the wider end-to-end experience, then translates that distinction into reviewer workflow criteria for the destination master browser.',
    sources: [
      ['Primary', 'Figma — Difference between UI and UX', 'https://www.figma.com/resource-library/difference-between-ui-and-ux/', 'Defines UI as interactivity/look/feel of product screens and UX as the broader product or website experience; useful because it matches the design-tool curriculum.'],
      ['Authority', 'NN/g / Don Norman — Definition of User Experience', 'https://www.nngroup.com/articles/definition-user-experience/', 'High-authority framing: UX covers all aspects of the end-user interaction with the company, services, and products.'],
      ['Cross', 'Interaction Design Foundation — UX vs UI', 'https://www.interaction-design.org/literature/article/ux-vs-ui-what-s-the-difference', 'Alternative educational framing that separates UX research/task flow from UI elements such as buttons, icons, lists, and text fields.'],
      ['Applied', 'UXDT Government Guidelines — Differences Between UI and UX', 'https://www.uxdt.nic.in/guidelines/understanding-ux/differences-between-ui-and-ux/', 'Practical public-service framing: UI covers visual/interactive elements; UX covers usability, accessibility, intuitiveness, and user response.'],
      ['Extension', 'CodeMike — UI vs UX further reading ladder', 'https://github.com/Rishabh1804/MSc/blob/main/design/foundations/ui-vs-ux-further-reading.md', 'Beyond-scope extension with Nielsen heuristics, UX honeycomb, GOV.UK user-needs discipline, W3C accessibility framing, and applied audit exercises.']
    ],
    notes: {
      summary: 'UI is the user-facing interaction surface: screens, controls, layout, labels, visual hierarchy, feedback, affordance, and component states. UX is the broader experience of accomplishing a goal through the product or service: user needs, information architecture, task flow, trust, accessibility, error recovery, efficiency, and emotional confidence. UI strongly affects UX, but UI is not the same as UX. For CodeMike, this means a redesigned browser is not successful merely because it looks cleaner; it is successful only if the reviewer can complete the inspection workflow with lower cognitive load and lower risk of over-trusting unverified data.',
      principles: [
        'Treat UI as the concrete interface layer: layout, controls, components, labels, states, contrast, typography, and interaction feedback.',
        'Treat UX as the full task journey: why the user is here, what they need to decide, what can go wrong, and how the interface helps them recover.',
        'Do not equate visual polish with usability, trust, accessibility, or task success.',
        'Good UI should make the intended UX possible; good UX should define what the UI must prioritize.',
        'For data-review tools, UX includes data-trust signalling, source uncertainty, verification status, and safe interpretation of the dataset.'
      ],
      comparison: 'All sources agree that UI and UX overlap but are not interchangeable. Figma frames UI as a specialized subset of UX and emphasizes product screens, interactive elements, visual choices, wireframes, prototypes, and iterative updates. NN/g/Don Norman gives the broadest authority frame: UX covers the whole end-user relationship with the company, service, and product, which makes it stronger for scope control. IxDF explains the discipline split through roles, research, psychology, task completion, and visible interface elements. UXDT gives the most practical checklist-like split for implementation. The CodeMike extension goes beyond definition sources by adding evaluation frameworks and browser-specific audit exercises.',
      disagreements: 'The sources mostly differ by emphasis rather than direct contradiction. Figma is product-tool oriented. NN/g is broader and more strategic. IxDF is educational and role-oriented. UXDT is implementation-friendly but simpler than NN/g. The extension deliberately adds external evaluation lenses so the topic does not stop at conceptual comparison.',
      interpretation: 'CodeMike should use UI vs UX as a design decision gate. UI work answers: what component, label, state, grouping, or layout is visible? UX work answers: does this help the reviewer inspect, filter, compare, verify, and avoid unsafe assumptions?',
      application: 'For the destination master browser, UI includes the search box, filter selects, warning badges, stats cards, destination cards, chips, metadata groups, table/card mode, reset control, sort control, and future detail drawer. UX includes the complete review flow: understand that 359 rows are structurally valid but unverified; identify the row set; filter by source/status/region/scale; inspect a full record; distinguish seed rows from normalized candidates; understand Planner-readiness; and leave with a correct sense of what still needs verification.',
      antiPatterns: [
        'Making the browser prettier while leaving the review task unchanged.',
        'Adding decorative colours, cards, gradients, or animation that do not improve inspection, filtering, trust, or comprehension.',
        'Hiding the not-Planner-ready warning below visually attractive content.',
        'Treating UI polish as evidence that the underlying destination data is source-verified.',
        'Using ambiguous badges or colour-only status indicators without text labels.',
        'Optimising for a screenshot instead of a repeatable QA workflow.'
      ],
      implementation: [
        'Keep the not-Planner-ready and verification warning visible before records and repeated inside detail/table contexts where needed.',
        'Add reset, sort, card/table view toggle, quick filters, and detail inspection only where each maps to a user task.',
        'Group controls by task: search, narrow, sort, switch view, inspect, reset.',
        'Make UI states explicit: selected filters, active view, empty results, loading failure, disabled/unavailable actions.',
        'Evaluate redesign success by reviewer task completion and data-trust clarity, not by visual novelty.',
        'Use the further-reading extension to run a UI inventory, UX journey map, Nielsen heuristic mini-audit, and UX honeycomb score before browser v1.1 implementation.'
      ],
      checklist: [
        'Add a UI-vs-UX gate to the master browser checklist: every UI change must identify the UX task it supports.',
        'Add a visual-polish anti-pattern check: no component should exist only because it looks impressive.',
        'Add a data-trust UX check: interface changes must not imply Planner-readiness or source verification.',
        'Reference the UI vs UX further-reading extension during final DES-001 submission as evidence of extra applied study.'
      ]
    },
    further: ['Nielsen Norman Group — usability heuristics', 'Peter Morville — UX honeycomb', 'GOV.UK user-needs discipline', 'W3C accessibility, usability, and inclusion', 'CodeMike extension note: design/foundations/ui-vs-ux-further-reading.md']
  },
  {
    title: 'What is UI design',
    status: 'done',
    summary: 'UI design is the discipline of choosing, arranging, specifying the behaviour of, and visually treating interface elements so that a user can complete a task with low cognitive cost and unambiguous feedback. Visual design is a sub-skill within UI design, not the discipline itself. State is first-class: every interactive lives in a small state machine of default / hover / focus / active / disabled / loading / empty / error / success.',
    sources: [
      ['Applied', 'Material Design 3 — Foundations & Components', 'https://m3.material.io/foundations', 'Most widely deployed component library on the web. Strong on density, motion, elevation, and per-component state guidance. Under-specifies "when not to use" and is light on data tables.'],
      ['Applied', 'Apple Human Interface Guidelines — Foundations & Components', 'https://developer.apple.com/design/human-interface-guidelines/foundations', 'Platform-led, behaviour-rule-heavy. Strong on clarity, deference, and modality discipline ("a modal must be earned"). Under-specifies dense data and web translation.'],
      ['Applied', 'IBM Carbon — Component patterns & Usage guidelines', 'https://carbondesignsystem.com/', 'Enterprise-grade. Treats the data table as a first-class primitive and ships master-detail / faceted-search as named patterns. Accessibility is built into every component spec. Under-specifies consumer surfaces.'],
      ['Applied', 'GOV.UK Design System — Components & Patterns', 'https://design-system.service.gov.uk/', 'Public-sector, content-first, accessibility-first. Distinctive for "when NOT to use this component" guidance and research links per component. Small component set by intent. Under-specifies enterprise data tools.'],
      ['Primary', 'Don Norman — The Design of Everyday Things (affordances/signifiers/feedback)', 'https://www.basicbooks.com/titles/don-norman/the-design-of-everyday-things/9780465050659/', 'Conceptual foundation the four design systems silently inherit. Without it the systems read like style guides. Pre-dates modern web vocabulary so requires translation.'],
      ['Extension', 'CodeMike — Topic 2 deep reading + source comparison', 'https://github.com/Rishabh1804/MSc/blob/main/design/foundations/topic-02-what-is-ui-design.md', 'Beyond-scope source comparison across the five required sources plus five extension sources (Refactoring UI, NN/g pattern articles, Atomic Design, WCAG / ARIA APG, Smashing pattern essays).']
    ],
    notes: {
      summary: 'UI design is decision work: choose container, choose elements inside the container, specify all nine states (default / hover / focus / active / disabled / loading / empty / error / success), verify affordance + signifier + feedback for each interactive, and defend each component against a "when not to use" gate. Visual treatment (colour, type, illustration) is downstream of these decisions, not the design discipline itself. The five required sources differ less on definition than on emphasis: Material is permissive about modality; Apple HIG, Carbon, and GOV.UK are restrictive. Carbon alone treats the data table as a first-class enterprise primitive. GOV.UK alone publishes per-component research evidence and "when not to use" guidance. Norman supplies the underlying affordance/signifier/feedback model the others silently inherit.',
      principles: [
        'A component is a system (anatomy + states + behaviour + content rules + accessibility), not a shape.',
        'States are first-class. Loading, empty, and error are the three most commonly missing — and the three a reviewer most needs when the data layer is being honest.',
        'Modality is a cost. A modal must be either confirm-destructive or must-finish-or-cancel; any other use is rejected.',
        'Consistency reduces cognitive load. The same action must look and behave the same wherever it appears.',
        'Accessibility is part of the component, not an audit. Colour-only signalling fails; status is reinforced by icon and text.',
        'The unit of design is the pattern (master-detail, faceted-search, table-with-batch-actions) — not the individual component.',
        'Every component must have a documented "when not to use" — the GOV.UK negative-space gate.'
      ],
      comparison: 'All five sources agree that a component is a system, not a shape, and that consistency reduces cognitive load. They disagree by emphasis. Material has the highest component count and richest visual system (density, motion, elevation) but is permissive about modality and light on data tables. Apple HIG is platform-led, strict on consistency with platform conventions, and unusually firm on modality discipline. Carbon is enterprise-grade with the strongest data-table and master-detail vocabulary; it treats the pattern as the unit of design. GOV.UK is the most disciplined on negative space: every component lists "when NOT to use" and links to user research. Norman supplies the conceptual ground (affordance, signifier, feedback) that all four design systems silently inherit. For a reviewer-facing data-review tool, Carbon and GOV.UK do most of the work; Material supplies visual treatment; HIG supplies modality discipline; Norman supplies the per-interactive review item.',
      disagreements: 'Modality: Material permissive vs HIG/Carbon/GOV.UK restrictive. Data tables: Carbon heavy vs the others light. "When not to use" guidance: GOV.UK explicit vs Material implicit. Reading age and content discipline: GOV.UK explicit vs others largely silent. Component count: Material ~80 vs GOV.UK ~24, reflecting opposite philosophies ("we have a component for that" vs "if it is not published you probably do not need it"). For the Destination Master Browser the HIG/Carbon/GOV.UK majority position is the right default; Material is consulted for visual treatment of chosen components.',
      interpretation: 'CodeMike treats UI design as: choose pattern → choose container → choose elements inside container → specify all nine states → verify affordance/signifier/feedback for each interactive → defend against a "when not to use" gate. Each component must name (a) the reviewer task it serves and (b) a less-costly alternative it beat, with the reason. A component that fails either test is decoration and is refused.',
      application: 'The Destination Master Browser is a master-detail data-review tool with faceted filtering. That phrase (Carbon vocabulary) fixes most component choices: table by default (cards as secondary), drawer for record inspection (never modal), filter chips for low-cardinality facets / dropdowns for high-cardinality / search input for free-text, Carbon Status Indicator for trust signalling at every depth, skeleton loaders not spinners, content-rich empty state with "Clear all" recovery, inline error notification with what-happened-and-what-to-do. Modality is reserved for destructive or must-finish actions like batch-promote-to-Planner.',
      antiPatterns: [
        'Modal-as-default container: inspecting a record should not block the list. Use a drawer.',
        'Cards as the only main list view: cards fail "scan by attribute" and "sort by column". Provide a table.',
        'Decorative badges: a badge with no operational meaning trains reviewers to ignore badges. Every badge must have a defined state.',
        'Colour-only signalling: fails reviewers with low-contrast displays, colour-vision difference, or screen readers. Colour is reinforced by icon and text.',
        'Empty-state silence: a zero-result filter combination must show the active filters, a clear-all action, and a what-to-try-next message.',
        'Loading silence: a request in flight must render a skeleton. Blank waiting time is a Norman feedback failure.',
        'Inconsistent affordance: the same action must use the same control across every context. Mixed list-click behaviours are findings.'
      ],
      implementation: [
        'Add a table mode alongside cards. Card/table toggle in the list-header right slot. Sortable columns, sticky header, optional row expansion.',
        'Add a record-detail drawer that opens on row click. Persistent trust banner in the drawer header. Non-modal; the list scrolls behind it.',
        'Add an active-filter summary above the result list — removable chips per applied filter.',
        'Add a "Clear all filters" recovery action in the empty state when filters return zero records.',
        'Add skeleton loading states for the result region. Spinners only for global page loads.',
        'Add an inline error notification for failed CSV loads — what failed, why, what to do.',
        'Add a top-level dataset-trust notification banner that persists with the header.',
        'Standardise the trust badge — one component, six states (verified / unverified / planner-ready / blocked / missing-fields / conflict / unassigned), used at row + drawer + confirm-modal.',
        'Add focus rings to every interactive. Keyboard navigation works for every list action.',
        'Defer decorative additions until items 1–9 are complete. No new colour palette, type scale, illustration, or animation in v1.1.'
      ],
      checklist: [
        'Add a container-selection gate: every new top-level container must name the reviewer task it serves and the existing container it could replace.',
        'Add a state-coverage gate: every interactive implements or explicitly N/As all nine standard states; missing-state findings block release.',
        'Add an affordance/signifier/feedback gate: every interactive answers Norman\'s three questions; an empty signifier or feedback column is a finding.',
        'Add a modality gate: a modal must be either confirm-destructive or must-finish-or-cancel; any other use is rejected.',
        'Add a colour-plus-text rule: status conveyed by colour is also conveyed by icon and text.',
        'Add a "when not to use" clause to every component in the system (GOV.UK posture).'
      ]
    },
    further: ['design/foundations/topic-02-what-is-ui-design.md — Topic 2 deep reading + source comparison', 'Brad Frost — Atomic Design', 'WCAG 2.2 / W3C ARIA Authoring Practices', 'Schoger & Wathan — Refactoring UI', 'NN/g pattern articles (card / table / modal)', 'Smashing — when to use cards vs tables']
  },
  {
    title: 'UX design',
    status: 'done',
    summary: 'UX design is the discipline of understanding the user task, modelling the journey, designing the interactions that make the journey succeed, and evaluating whether the design produces success for real users. Distinct from UI design (the substrate) and usability evaluation (one phase). Topic 2 ended at component rules; Topic 3 ends at a UX acceptance-criteria sheet. Both are required before Browser v1.1 ships.',
    sources: [
      ['Primary', 'Don Norman — The Design of Everyday Things', 'https://www.basicbooks.com/titles/don-norman/the-design-of-everyday-things/9780465050659/', 'Conceptual foundation: the gulfs of execution and evaluation, the seven-stage action model, errors as design failures. Pre-dates modern journey-map practice but supplies the underlying ergonomic theory.'],
      ['Primary', 'Nielsen Norman Group — Definition of UX + 10 Usability Heuristics', 'https://www.nngroup.com/articles/definition-user-experience/', 'Broadest UX scope ("all aspects of the end-user interaction with the company, services, and products") plus the most-cited evaluation framework. Breadth is also a risk: if everything is UX, nothing diagnoses what to fix — so the heuristics provide the diagnostic grain.'],
      ['Applied', 'IDEO — The Field Guide to Human-Centered Design (Methods)', 'https://www.designkit.org/resources/1', 'Practical synthesis methods, journey-mapping technique with emotional state per step, "how might we" reframing. Consumer-shaped; emotional-state column is repurposed to trust-state for data-review tools.'],
      ['Applied', 'GOV.UK Service Manual — Learning about users + Map a user\'s journey', 'https://www.gov.uk/service-manual/user-research', 'Strictest source on user-need form (As a [user], I need [outcome], so that [goal] — with no UI mechanism named). Catches solution-shape language that other sources permit. Public-service-strict; transactional-shaped, but the discipline transfers.'],
      ['Cross', 'Interaction Design Foundation — UX Design (foundations)', 'https://www.interaction-design.org/literature/topics/ux-design', 'Educational cross-check on the integrated UX discipline (interaction design + IA + usability + accessibility). Useful for confirming the integrated picture from the other four sources is not idiosyncratic.'],
      ['Extension', 'CodeMike — Topic 3 deep reading + journey map + acceptance criteria', 'https://github.com/Rishabh1804/MSc/blob/main/design/foundations/topic-03-ux-design.md', 'Beyond-scope source comparison plus the seven-step Destination Master Browser reviewer journey with goal / cost / failure / trust per step.']
    ],
    notes: {
      summary: 'UX design is decision work that converts user understanding into testable behavioural criteria the UI must produce. The four canonical activities (research, modelling, design, evaluation) translate to artifacts: personas + needs, journey maps + mental models, wireframes + interaction specs, usability studies + heuristic audits. Topic 3 sits in the modelling activity and produces the bridge from modelling to design (the UX acceptance-criteria sheet). The seven-step reviewer journey (arrive / understand / narrow / compare / inspect / recover / leave) is the Destination Master Browser\'s canonical journey, with goal / cost / failure-mode / trust-check per step.',
      principles: [
        'UX design is broader than UI: it includes the journey, the trust state, the recovery path, and the user\'s mental model at the end.',
        'A user need must be written without naming a UI mechanism (GOV.UK form: "As a [user], I need [outcome], so that [goal]").',
        'A UX acceptance criterion is testable, behavioural, and independent of UI mechanism. Two evaluators applying it reach the same verdict.',
        'Every journey step has a goal, a cost budget, a failure mode, and a trust check.',
        'Data-review tools spend most reviewer-time in non-happy paths (empty, conflict, missing-field, blocked). Happy-path-only design is a UX failure for this product category.',
        'Trust state replaces emotional state in journey maps for data-review tools.',
        'Topic 2\'s component rule sheet and Topic 3\'s acceptance-criteria sheet are both required before v1.1 ships — neither alone is sufficient.'
      ],
      comparison: 'All five sources agree that UX is broader than UI, that research must back design decisions, and that journey maps are the canonical modelling artifact. They differ on emphasis: Norman supplies the underlying ergonomic theory (the two gulfs, the seven-stage action model); NN/g supplies the broadest scope and the most-cited evaluation framework; IDEO supplies methods and emotional-state-per-step journey maps; GOV.UK supplies the strictest user-need discipline and forbids solution-shape language; IxDF cross-checks the integrated picture. For the Destination Master Browser, GOV.UK\'s user-need form is the most operationally important corrective (prevents feature-first thinking) and IDEO\'s journey-map shape (with trust-state replacing emotional-state) is the most transferable artifact.',
      disagreements: 'User-need discipline: GOV.UK very strict; others loose. Emotional state in journey maps: IDEO explicit; others absent. Process formality: IDEO and GOV.UK high (methods and rules); Norman and NN/g loose (concepts and findings). Reading-age and content discipline: GOV.UK very strict; others permissive. Coverage of data-review tools: all five are light; the topic synthesises rather than relies on any one source\'s direct guidance.',
      interpretation: 'CodeMike treats UX design as: extract user needs in GOV.UK form, model the journey with goal/cost/failure/trust per step, write testable acceptance criteria per step, verify the design produces those criteria, and audit the design against UX anti-patterns. Every feature has a user-need statement; every journey step has at least one acceptance criterion. The discipline produces the UX gate that Topic 2\'s rule sheet does not.',
      application: 'The Destination Master Browser\'s reviewer journey has seven steps. The high-priority v1.1 UX gates: arrive within 5s with dataset trust state visible; narrow with active-filter summary visible and individually removable in ≤ 3 interactions per facet; compare in table mode with sortable columns; inspect opens a drawer in ≤ 2 interactions with list context preserved and trust banner in drawer header; recover from any empty-result state in ≤ 1 interaction; trust signal survives every depth (list row, table row, drawer header). The full set lives in design/foundations/ux-acceptance-criteria.md.',
      antiPatterns: [
        'Designing the happy path only: data-review tools spend most reviewer-time in non-happy paths; treating empty/error/loading as edge cases is a UX failure for this category.',
        'Confusing user request with user need: a request names a mechanism; a need names an outcome. Designing for the request locks the design unnecessarily.',
        'Skipping evaluation: shipping a journey that was never tested against real reviewer behaviour. Acceptance criteria are the minimum evaluation gate; user testing is the next step.',
        'Ignoring the trust check at depth: trust state must survive every journey step, not just the list. Topic 1 finding carried forward at journey level.'
      ],
      implementation: [
        'Add a Need column to the v1.1 backlog — every backlog item has a user need in GOV.UK form.',
        'Add an Acceptance-criterion column to the v1.1 backlog — every item has at least one criterion from ux-acceptance-criteria.md.',
        'Add a reviewer-walk-through test before any v1.1 PR merges — seven journey steps × all criteria; design passes only if all are satisfied.',
        'Add an empty / loading / error verification step — each non-happy-path state must be intentionally triggered and verified.',
        'Defer all v1.1 features not justified by an acceptance criterion (visual polish, additional filter facets, batch actions, dashboards).'
      ],
      checklist: [
        'Add a criterion-presence gate: every v1.1 component must reference at least one UX acceptance criterion it implements.',
        'Add a behaviour-testability gate: every criterion must be testable by two evaluators reaching the same pass/fail verdict.',
        'Add a need-vs-request audit: every feature must produce a user need in GOV.UK form (no UI mechanism named).',
        'Add a journey-completeness gate: every reviewer-journey step has at least one criterion; empty / loading / error are first-class.'
      ]
    },
    further: ['design/foundations/topic-03-ux-design.md — Topic 3 deep reading + source comparison', 'design/foundations/ux-acceptance-criteria.md — Lab 03 acceptance-criteria sheet (Browser v1.1 UX gate; PR B)', 'Kim Goodwin — Designing for the Digital Age (personas + scenarios)', 'Indi Young — Mental Models', 'Jeff Patton — User Story Mapping', 'ISO 9241-210 — Human-centred design lifecycle']
  },
  {
    title: 'Design thinking',
    status: 'done',
    summary: 'Design thinking is the iterative process of moving from a fuzzy human problem to a tested solution. Five canonical stages (Empathize / Define / Ideate / Prototype / Test) or three IBM Loop activities (Observe / Reflect / Make); evidence-per-stage discipline (NN/g); three-constraint triage (desirability / feasibility / viability — Brown). The loop is the point: single-pass design thinking is design thinking only by accident. Sits upstream of Topic 3 — used when the problem is NOT well-framed; skipped when Topic 3 criteria can be written directly.',
    sources: [
      ['Primary', 'Stanford d.school — Bootleg Bootcamp (method cards)', 'https://dschool.stanford.edu/resources/the-bootcamp-bootleg', 'Canonical 5-stage diagram plus per-stage methods catalogue. Most-cited single source on the discipline; equips the loop with concrete techniques (5 Whys, "I like / I wish / what if", bodystorm).'],
      ['Applied', 'IBM Design Thinking — The Loop, Hills, Playbacks', 'https://www.ibm.com/design/thinking/', 'Compresses 5 stages into 3 (Observe / Reflect / Make) and adds team-coordination devices: Hills (outcome statements), Playbacks (demo gates), Sponsor Users (embedded domain experts). Enterprise-scale operationalisation.'],
      ['Primary', 'Tim Brown — Change by Design + HBR essay "Design Thinking" (2008)', 'https://hbr.org/2008/06/design-thinking', 'The three-constraint frame: desirability / feasibility / viability. The most-cited disciplining device for the Ideate → Prototype transition.'],
      ['Cross', 'Nielsen Norman Group — Design Thinking 101', 'https://www.nngroup.com/articles/design-thinking/', 'The iterative/non-linear discipline: the loop is the point, not the linear diagram. Evidence-per-stage rule: a stage that produced no artifact has not been done.'],
      ['Extension', 'CodeMike — Topic 4 deep reading', 'https://github.com/Rishabh1804/MSc/blob/main/design/foundations/topic-04-design-thinking.md', 'Beyond-scope source comparison plus the Norman Useful-Myth critique, IDEO/Liedtka/Goodwin extensions, and the Topic 4-vs-Topic 3 routing rule.']
    ],
    notes: {
      summary: 'Design thinking is decision-shaped process work that turns fuzzy human problems into tested solutions. The process is iterative (the loop is the point), evidence-shaped at every stage (NN/g rule), and disciplined by the three-constraint triage (Brown). Stages: Empathize / Define / Ideate / Prototype / Test (d.school) or Observe / Reflect / Make (IBM compression). For CodeMike, design thinking is the upstream pairing for Topic 3 — run a loop when the problem is not well-framed; skip to criteria-writing when it is.',
      principles: [
        'The loop is the point — one pass is design thinking only by accident.',
        'Every stage produces an artifact (NN/g evidence rule); a stage that produced no artifact has not been done.',
        'Generate ≥ 3 meaningfully different candidates in Ideate; "we already know what to build" is the most common practical failure (skipping Ideate).',
        'Use Tim Brown\'s three-constraint triage (desirability / feasibility / viability) to disciplining the Ideate → Prototype transition.',
        'Test specifications must include falsification criteria — what would change our mind. A Test without falsification criteria is a rubber-stamp.',
        'For single-person workspaces: empathy-by-introspection is the default failure; mitigate with three-persona synthesis (first-time / power / accessibility-need).',
        'Design thinking complements deep domain knowledge; it does not substitute for it (Norman Useful-Myth critique).'
      ],
      comparison: 'All four required sources agree on the shape (understand → frame → generate → make → test) and on iteration as central. They differ on emphasis: d.school is operational (Bootleg method cards), IBM is organisational (Hills + Playbacks + Sponsor Users), Brown is strategic (three constraints), NN/g is epistemic (iteration + evidence). The four together cover the topic; one or two would have known gaps. The Norman extension (Useful Myth) functions as a critique that sharpens the discipline by naming what it must defend against (branding hazard, domain-expertise hazard).',
      disagreements: 'Stage count: d.school 5 vs IBM 3 vs (Brown implicit) vs NN/g 5. Iteration emphasis: NN/g explicit + diagrammed jumps vs others implicit. Team scale: IBM enterprise vs d.school small/co-located vs Brown strategic/cross-functional vs NN/g operational. Per-stage method catalogue: only d.school publishes named time-boxed methods. Three-constraint frame: only Brown publishes it. For solo CodeMike workspace, d.school + Brown + NN/g matter most; IBM is translated (Hills/Playbacks become "regular self-imposed check-in artifacts").',
      interpretation: 'CodeMike treats design thinking as: identify the problem, check well-framed conditions (user-need form writable + tested success answerable + criterion measurable). If well-framed → Topic 3 (skip Topic 4). If not → Topic 4 loop (Empathize → Define → Ideate ≥3 candidates → triage by 3 constraints → Prototype cheap form → Test specification with falsification criteria → loop result). Every stage produces an artifact or the stage hasn\'t been done.',
      application: 'The v1.2 backlog has three candidates from Lab 03\'s deferred list (collapsible filter panel, confirm modal for destructive batch actions, faceted filter panel) — all three need Topic 4 loops first because their underlying problems are not yet well-framed. The v1.1 polish items + acceptance-criteria sheet items go straight to Topic 3 criteria-writing when v1.2 starts. Lab 04 picks ONE of the three Topic-4 candidates and runs a full worked loop; the other two stay in the v1.2 backlog with "needs Topic 4 loop" annotation. Pairing with Topic 5 (HCD): HCD will provide the standards-grade vocabulary that names the same four activities; Topic 4 provides the practical toolkit.',
      antiPatterns: [
        'Skipping Ideate — committing to the first plausible solution. The single most common practical failure. Discipline: always generate ≥ 3 meaningfully different candidates.',
        'Single-pass design thinking — doing one loop and shipping. The full benefit compounds across loops.',
        'Empathy-by-introspection — single-person workspaces are particularly prone to "I am the user". Mitigation: three-persona synthesis in writing.',
        'Workshop theatre — producing no per-stage evidence. NN/g evidence-per-stage rule is the corrective.',
        'Triage by taste — picking the chosen candidate without sourced desirability / feasibility / viability assessment. Brown three-constraint frame is the corrective.'
      ],
      implementation: [
        'Add a "Topic 4 first?" gate to the v1.2 backlog — every candidate annotated well-framed (Topic 3 only) or not well-framed (Topic 4 loop first).',
        'Adopt the three-constraint triage as the default decision form for choosing between v1.2 candidates.',
        'Adopt the evidence-per-stage rule for any loop run in the workspace.',
        'Add a Sponsor Reviewer concept to v1.2 (IBM translation for solo workspace) — if no real Sponsor Reviewer available, stay in self-as-user mode and name the limitation explicitly.',
        'Run Lab 04 on one chosen pain point from the deferred v1.2 candidates as the worked example.'
      ],
      checklist: [
        'Add a problem-framing gate: every v1.2 backlog item annotated well-framed (skip Topic 4) or not well-framed (run a loop first).',
        'Add a "≥3 meaningfully different candidates" gate at the Ideate → Prototype boundary; <3 candidates means re-ideate.',
        'Add a sourced-triage gate: desirability / feasibility / viability cells must cite evidence, not opinion.',
        'Add a falsification-criteria gate to Test specifications: a Test without "what would change our mind" criteria is a rubber-stamp.'
      ]
    },
    further: ['design/foundations/topic-04-design-thinking.md — Topic 4 deep reading + source comparison', 'design/foundations/topic-04-design-thinking-loop.md — Lab 04 single-pain-point loop (PR B)', 'IDEO Field Guide (different chapters than Topic 3)', 'Jeanne Liedtka — Design Thinking for the Greater Good', 'Kim Goodwin — Designing for the Digital Age (scenarios + personas)', 'Don Norman — Design Thinking: A Useful Myth (2010 essay; critique)', 'GOV.UK Service Manual — Discovery phase']
  }
];

window.DES001_TOPIC_STUBS = [
  'Human-centered design',
  'Gestalt principles',
  "Fitts' law",
  'Button states',
  'Typography',
  'Color theory',
  'Web design / grid layout',
  'Design systems'
].map((title) => ({
  title,
  status: title === 'Gestalt principles' ? 'partial' : 'todo',
  summary: 'Source scaffold carried forward from v1. Full deep-reading notes pending.',
  sources: [],
  notes: window.DES001_PENDING_NOTES,
  further: ['Pending topic-specific further reading.']
}));

window.DES001_TOPICS = window.DES001_TOPICS.concat(window.DES001_TOPIC_STUBS);
