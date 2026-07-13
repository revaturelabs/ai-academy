---
name: reading-critic
description: "Validate the reading artifact: length budget, citations, no forward references, faithfulness to corpus, tone fit."
---

# reading-critic

## Inputs
- `reading_path` — `<topic-dir>/artifacts/reading.md`
- `meta_path` — `<topic-dir>/artifacts/reading.meta.json`
- `corpus_path` — for faithfulness check
- `resources_path`, `sequence_index_path`, `target_word_range`, `target_minute_range`

## Checks

0. **Format discipline (hard fail).**
   - **No frontmatter.** `reading.md`'s first non-empty line must be the `# <title>` H1 — a leading `---` YAML block is a fail (`frontmatter_present`). Learner-facing file must be clean; metadata lives in the sidecar.
   - **Sidecar present.** `reading.meta.json` must exist beside the reading and parse, carrying `word_count`, `estimated_read_minutes`, `citations_used`, `sections`. Missing/invalid → `meta_sidecar_missing`.
   - **Fixed six sections.** The reading must contain exactly these `##` headings, in this order, none added/renamed/dropped: `Overview`, `Key Concepts`, `Worked Example`, `In Practice`, `Key Takeaways`, `References` (References may be absent ONLY if zero citations exist). Deviation → `section_template_violation` with the diff.

1. **Length.** Word count in `target_word_range`; reading-aloud minutes (`words / 230`) in `target_minute_range`. Fail both under and over.

2. **Citations.** Every `primary` resource cited at least once. Bibliography at end matches inline markers. No orphan markers; no orphan bibliography entries.

3. **No forward references.** Same rule as corpus critic.

4. **Faithfulness.** Every assertion in the reading must trace to the corpus. Sample 8–12 assertions across the reading and verify they appear (verbatim or paraphrased) in the corpus. **Fail if > 2 unsupported assertions.**

5. **Tone fit.** Quick heuristic pass: average sentence length should be under 25 words; hedging phrases ("It is generally considered", "many experts believe", "various studies have shown") should be < 3 occurrences total. The reading is plainspoken — flag academic register.

## Output
Same shape as `corpus.critic.json`. Verdict cites specific paragraphs by line range when something fails.
