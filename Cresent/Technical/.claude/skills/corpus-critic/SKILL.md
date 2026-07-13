---
name: corpus-critic
description: "Hard-gate the topic corpus against required-section presence, citation density, forward-reference discipline, and length sanity."
---

# corpus-critic

You validate that a freshly generated `topic_corpus.md` is good enough to ground every downstream artifact. The team agreed: hard-block on fail.

## Inputs
- `corpus_path`, `resources_path` (`topic.resources.json`), `sequence_index_path` (`curriculum/sequence.index.json`), `topic_id`, `position_in_sequence`, `output_path` (`critic-reports/corpus.critic.json`)

## Checks

### 1. Required sections present + non-trivial
Sections 3, 4, 5, 10 must exist with ≥100 words (section 5) / ≥50 words (others). The literal placeholder strings (e.g. `_No formal prerequisites._`) only count for optional sections, never required ones.

### 2. Citation density (depends on `resources_source`)
Read `topic.resources.json.resources_source`:

- **`"human"` or `"web_search"`** — strict: every `primary` resource must be cited at least once (`[N]` marker). For sections 5, 6, 7: ≥60% of standalone factual assertions carry a citation marker. Fail on miss.
- **`"narrative_seed_only"`** — degraded grounding (author skipped resources, no WebSearch). Skip the citation-density hard check; emit a single soft finding `low_grounding: corpus built from narrative seed only, no external citations` so the per-topic HITL #3 gate (artifact approval) sees it — and rolls up at HITL #4. Still fail if the corpus contains FAKE citations (`[N]` markers that don't resolve to any resource) — fabricated citations are always a hard fail.

### 3. Sequence drift (forward references)
- Extract every technical noun phrase from the corpus.
- For each, check whether it appears in either:
  - This topic's `concepts_introduced` (defined here), OR
  - Any prior topic's `concepts_introduced` (per `sequence_index.json`, filtered to topics with delivery position < this topic's).
- **Fail with the list of unknown / forward-referenced terms.**

### 4. Length sanity
- Word count must fall in the depth profile's range (from `.claude/config/artifact-mix.json`):
  - atomic: 1500–2400
  - standard: 3000–4400
  - deep: 5000–6000
- The corpus-builder reports its `suggested_profile`; use that. If the count is more than 30% outside the range, fail.

## Output
Same shape as the other critic reports — `passed`, per-check results, verdict, `at` timestamp. List forward-referenced terms explicitly in the verdict so the corpus-builder knows what to revise.
