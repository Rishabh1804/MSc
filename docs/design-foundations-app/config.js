window.DES001_CONFIG = {
  assignmentId: 'DES-001',
  title: 'Design Foundations Study Dashboard',
  eyebrow: 'CodeMike Design Foundation · DES-001',
  version: 'v2',
  primaryArtifact: 'docs/design-foundations.html',
  legacyArtifact: 'docs/design-foundations-v1.html',
  sourcePolicy: 'Every deep-reading topic requires at least three sources: one high-authority/primary where possible, one practical/applied, and one cross-checking or alternative framing source.',
  curriculumNote: 'Topic 1 is fully digested and has an extra further-reading extension. Remaining topics keep their source scaffolds until they receive the same deep-reading treatment.',
  workflow: [
    ['1. Read', 'Use 3+ sources per topic.'],
    ['2. Compare', 'Identify overlap, bias, and omissions.'],
    ['3. Generate notes', 'Summaries, anti-patterns, and further reading.'],
    ['4. Translate', 'Convert findings into browser criteria.'],
    ['5. Implement', 'Only build changes tied to criteria.']
  ],
  rules: [
    {
      title: 'Deep reading standard',
      items: [
        'At least three sources per topic.',
        'At least one high-authority or primary source where possible.',
        'At least one practical implementation source.',
        'At least one cross-checking or alternative framing source.',
        'Notes must include further reading suggestions.'
      ]
    },
    {
      title: 'Required note outputs',
      items: [
        'Topic summary and key principles.',
        'Source comparison and disagreements.',
        'CodeMike interpretation.',
        'Application to the destination browser.',
        'Anti-patterns to avoid.',
        'Implementation implications and checklist updates.'
      ]
    }
  ],
  synthesis: {
    title: 'Current synthesis after Topic 1',
    paragraphs: [
      '<strong>UI vs UX changes the redesign gate:</strong> the destination master browser cannot be judged by visual polish alone. UI quality covers visible controls, layout, states, hierarchy, and affordances. UX quality covers whether the reviewer can complete the full inspection journey safely: understand dataset status, filter, inspect, compare, detect uncertainty, and avoid mistaking structural validity for Planner-readiness.',
      '<strong>Further-reading extension added:</strong> <a href="https://github.com/Rishabh1804/MSc/blob/main/design/foundations/ui-vs-ux-further-reading.md">DES-001 Topic 1 — UI vs UX Further Reading Ladder</a> expands this topic through usability heuristics, UX honeycomb scoring, GOV.UK user-needs discipline, W3C accessibility framing, and applied browser audit exercises.',
      'Before editing <code>docs/destination-master-browser-v1.html</code>, every proposed change must answer: <code>Which reviewer task improves? Which interface element supports it? Which trust or workflow risk is reduced?</code>'
    ]
  }
};
