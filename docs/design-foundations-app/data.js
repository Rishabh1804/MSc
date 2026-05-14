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
      ['Extension', 'CodeMike — UI vs UX further reading ladder', '../design/foundations/ui-vs-ux-further-reading.md', 'Beyond-scope extension with Nielsen heuristics, UX honeycomb, GOV.UK user-needs discipline, W3C accessibility framing, and applied audit exercises.']
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
    status: 'todo',
    summary: 'Defines interface elements, controls, navigation, feedback, visual hierarchy, and interaction surfaces.',
    sources: [
      ['Primary', 'Figma — What is UI design?', 'https://www.figma.com/resource-library/what-is-ui-design/', 'Primary design-tool explanation of UI practice.'],
      ['Applied', 'Material Design — Foundations', 'https://m3.material.io/foundations', 'Practical component and system guidance.'],
      ['Cross', 'Apple HIG — Foundations', 'https://developer.apple.com/design/human-interface-guidelines/foundations', 'Platform-oriented interface principles for comparison.']
    ],
    notes: window.DES001_PENDING_NOTES,
    further: ['Navigation patterns', 'Input controls', 'Status and feedback patterns']
  },
  {
    title: 'UX design',
    status: 'todo',
    summary: 'Frames product design around user goals, journeys, research, friction, prototypes, and validation.',
    sources: [
      ['Primary', 'Figma — What is UX design?', 'https://www.figma.com/resource-library/what-is-ux-design/', 'Primary curriculum source.'],
      ['Applied', 'Nielsen Norman Group — UX Definition', 'https://www.nngroup.com/articles/definition-user-experience/', 'Research-backed UX definition and scope.'],
      ['Cross', 'Interaction Design Foundation — UX Design', 'https://www.interaction-design.org/literature/topics/ux-design', 'Broader educational framing of UX practice.']
    ],
    notes: window.DES001_PENDING_NOTES,
    further: ['Task analysis', 'Journey mapping', 'Usability heuristics']
  }
];

window.DES001_TOPIC_STUBS = [
  'Design thinking',
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
  status: title === 'Design thinking' || title === 'Gestalt principles' ? 'partial' : 'todo',
  summary: 'Source scaffold carried forward from v1. Full deep-reading notes pending.',
  sources: [],
  notes: window.DES001_PENDING_NOTES,
  further: ['Pending topic-specific further reading.']
}));

window.DES001_TOPICS = window.DES001_TOPICS.concat(window.DES001_TOPIC_STUBS);
