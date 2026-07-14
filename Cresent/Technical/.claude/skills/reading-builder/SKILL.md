---
name: reading-builder
description: "Generate the primary reading artifact (markdown) from an approved topic corpus. Length scales to the topic's confirmed depth profile. Embeds the diagram artifact inline when one exists."
---

# reading-builder

You are writing the reading artifact a learner will actually consume. The corpus is the spine; you are not adding facts, you are turning the corpus into a guided walkthrough with citations and examples.

## Inputs

- `corpus_path`: path to `topic_corpus.md`
- `resources`: list of `{type, value, role, notes}` to cite
- `target_word_range`: [min, max]
- `target_minute_range`: [min, max]
- `prior_concepts`: flat list of every concept introduced before this topic (vocabulary you may use without re-defining)
- `diagram_path`: optional — relative path to `artifacts/diagram.png` if a diagram exists. If non-empty, embed it inline (see "Diagram embedding" below).
- `next_assessment`: optional — `{id, due_week, title, weight}` from `topic.manifest.json` so the reading can land the "what this prepares you for" framing.
- `output_path`: where to write `artifacts/reading.md`

## Two files out

1. **`reading.md`** — the clean, learner-facing file. **No YAML frontmatter.** The file opens directly with the `# <title>` H1. A learner (or the LMS) renders this as-is, so it must contain *only* what a learner reads — no machine metadata at the top.
2. **`reading.meta.json`** — a sidecar written beside `reading.md` in `artifacts/`, carrying everything that used to live in frontmatter (see "Sidecar metadata" below).

## Fixed structure (every topic, every time)

Every reading uses **exactly these six sections, in this order**, so the learner hits the same shape on every topic. Do not rename, reorder, add, or drop sections. If a section has thin source material, keep it short — never omit it.

```markdown
# <title>

## Overview
(2–4 sentences. Restate the topic's one-liner in the reader's frame and say why it matters —
condensed from the corpus Introduction. If `next_assessment` is present and due_week is within
~3 weeks, close with one sentence: "_This contributes to <assessment_id> — <title> (due W<NN>,
<weight>)._")

## Key Concepts
(The spine — a curated walkthrough of the corpus Core Concepts. Do NOT re-derive the corpus prose;
tighten it. Cite external resources inline as `[N]` where they back a claim. If a diagram exists,
embed it here — see "Diagram embedding" — replacing a paragraph, not adding to one.
**Formatting (required) — see Discipline #8:** lead each sub-topic paragraph with an underlined
bold label `<u>**Sub-topic label.**</u>`, and render any run-together enumeration as a Markdown
bullet list, never inline prose.)

## Worked Example
(The concrete example from the corpus Implementation / Hands-On section, shown step by step.
If the corpus has no worked example, give the single clearest concrete instance of the concept.
Keep it to one example — depth over breadth.)

## In Practice
(Condensed Real-World Patterns + Best Practices from the corpus: where this shows up, the common
do/don't. Bullets preferred over prose. If the corpus has neither, keep this to 2–3 sentences on
why the concept matters downstream — never drop the heading.)

## Key Takeaways
(3–5 bullets — mirrors the corpus Key Takeaways.)

## References
(Numbered bibliography matching the inline `[N]` markers. Omit only if zero citations exist.)
```

## Sidecar metadata

Write `reading.meta.json` beside the reading:

```json
{
  "topic_id": "<id>",
  "title": "<title>",
  "estimated_read_minutes": 7,
  "word_count": 1402,
  "generated_at": "<ISO>",
  "embeds_diagram": true,
  "citations_used": [1],
  "sections": ["Overview", "Key Concepts", "Worked Example", "In Practice", "Key Takeaways", "References"]
}
```

## Diagram embedding

If `diagram_path` is set (the topic has `artifact_plan.diagram = true` and `/generate-diagram`
has already completed), embed it inline:

```markdown
![<diagram-caption>](./diagram.png)
*<short caption explaining what the diagram shows>*
```

Use a relative path from the reading's location (the reading and the diagram both live in
`<topic-dir>/artifacts/`, so `./diagram.png` is correct).

The caption should:
- Name the concept the diagram visualizes ("RAG retrieval pipeline", "The 2026 AI stack")
- Be 1 sentence; do not duplicate the body prose.

Place the image at the point in the body where the concept is first explained — not as an
appendix at the end. Diagrams are most useful as the reader hits the named concept.

If `diagram_path` is **not** set, do not invent one. Skip the image; the reading still works.

## Discipline

1. **No new content.** Every assertion in the reading must trace to the corpus. If you want to
   add an example the corpus doesn't have, ask the parent for permission (return early with a
   `needs_example` flag).

2. **Length budget is a hard cap.** If you can't hit the corpus's depth in the word range,
   return early and flag — do not pad.

3. **Citation density.** Every `primary` resource cited at least once. Aim for ≥1 citation per
   400 words at this length.

4. **Vocabulary.** Use `prior_concepts` without defining. Use this topic's new concepts WITH a
   definition on first mention.

5. **Tone.** Plain language. Direct sentences. The reading is what a smart 8th-grade-engineering-
   aware college reader would want, not a textbook chapter.

6. **Curate, don't re-write.** The corpus is the backbone — the reading is a *tightened* pass over
   it, not a longer one. Condensing levers: lead sections with bullets where the corpus uses prose;
   merge redundant explanation; let the diagram carry structure that prose would otherwise spell
   out; keep one worked example, not three. The reading should usually be *shorter* than the
   corpus, never a padded expansion of it.

7. **External resources earn citations.** Where an external resource sharpens or backs a corpus
   claim, weave it in with an inline `[N]` and list it in References. Every `primary` resource is
   cited at least once. Citations attach to claims, not decoration.

8. **Scannable formatting (required in Key Concepts).** The learner must see at a glance what each
   part explains.
   - **Underline each sub-topic label.** Every sub-topic paragraph in Key Concepts begins with a
     bold lead-in label wrapped in an HTML underline tag: `<u>**Variables and assignment.**</u> …`.
     (Where a section introduces the sub-topic with an inline bold term instead of a lead-in label,
     underline that first-introduction term: `<u>**operator precedence**</u>`.) `<u>` renders on
     GitHub, ADO, and the LMS; it is valid inline HTML inside Markdown.
   - **Bullet every enumeration.** Any list of points that would otherwise run together in prose —
     "First… Second…", "two ways", "three kinds", a set of functions/rules/uses — is written as a
     Markdown bullet list with an intro line ending in a colon, a blank line before and after the
     list, and one point per bullet. Do NOT bury enumerated points inside a paragraph.
   - Preserve all wording, `code`, `[N]` citations, and bold inside the bullets and labels. This is
     a formatting convention, not a licence to reword.

## Return value

```json
{
  "path": "<output_path>",
  "meta_path": "<artifacts/reading.meta.json>",
  "word_count": 1380,
  "estimated_minutes": 7,
  "citations_used": [1, 2, 3],
  "embeds_diagram": true,
  "self_check": {
    "in_word_range": true,
    "every_primary_cited": true,
    "no_new_assertions": true,
    "diagram_inline": true,
    "no_frontmatter": true,
    "six_fixed_sections": true,
    "sidecar_meta_written": true
  }
}
```
