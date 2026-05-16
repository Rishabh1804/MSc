# 00-foundations — speaker notes

Notes for the sample deck `slides.html`. These travel with the deck, not in `slides.html` itself, so changes here don't risk muddying the slides' data contract.

## Slide-by-slide

1. **Title.** Five-second intro: what module, what date, what audience.
2. **What this deck is.** Explain the HR-MSc-9 contract out loud: every data-bearing slide fetches its source at runtime, so the deck is always honest about what the workspace currently says.
3. **Current skill map.** Talk to the file — point out maturity levels, then what's missing. If the slide is empty, the workflow that staged the data failed; fall back to opening `operations/SKILL_MAP.md` on the screen.
4. **Six-month roadmap.** Same pattern: read the source, comment.
5. **Next actions.** Treat as a to-do; pick the top three to walk through.
6. **Speaker notes.** Tell the audience this file exists.

## How to add a data slide

```html
<section data-source="../../../operations/<FILE>.md">
  <h2>Slide heading</h2>
  <pre class="cm-source-content cm-loading">Loading operations/&lt;FILE&gt;.md&hellip;</pre>
  <span class="cm-source-note">source: operations/&lt;FILE&gt;.md</span>
</section>
```

`deck-data-fetch.js` (already loaded by `slides.html`) populates the `<pre class="cm-source-content">` on `Reveal.on('ready')`.
