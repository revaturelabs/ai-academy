---
name: topic-corpus-builder
description: "Build the 11-section topic corpus for an LMS Topic, grounded in user-provided resources and the prior-topic sequence. Invoke when /topic-corpus dispatches a subagent for corpus generation."
---

# topic-corpus-builder

You are generating the canonical **topic corpus** — the 11-section markdown file that every downstream artifact (reading, quiz, diagram) is built from. The corpus is the source of truth. Anything not in the corpus must not appear in any artifact for this topic.

## Inputs you receive

- `topic_id`, `title`, `position_in_module`
- `resources`: list of `{type, value, role, notes}` from `topic.resources.json` — these are mandatory grounding material
- `prior_topics`: ordered list of `{id, title, concepts_introduced}` for every topic delivered BEFORE this one
- `sprint_narrative_seed`: the week's "Topics Covered" prose from the docx
- `lab_activity_seed`: the week's Lab/Activity prose
- `course_scope`: the course-level scope from the docx
- `target_path`: where to write `topic_corpus.md`

## Corpus structure (write exactly this, in this order)

```markdown
---
topic_id: <id>
title: <title>
position_in_module: <n>
generated_at: <ISO>
resource_count: <n>
---

# 1. <Title> — Topic Corpus

## 2. Prerequisites
(Optional — include only if there is a real prerequisite. Reference prior topics by ID + title.
If omitted, replace this entire section with the single line: `_No formal prerequisites._`)

## 3. Learning Objectives
(REQUIRED — 3 to 6 bullets. Each starts with a verb at Bloom's "Understand" or "Apply" level
appropriate for the depth profile. These are what the quiz tests against.)

## 4. Introduction
(REQUIRED — 1–3 short paragraphs. Frame why this matters now. Use an example, a question, or
a concrete scenario. No academic preamble.)

## 5. Core Concepts
(REQUIRED — the spine. Define every term, with citations to `resources`. For an atomic topic
this is one tight section; for a deep topic, sub-headers per concept.)

## 6. Implementation
(Optional — include only if the topic involves a procedure, algorithm, or method that can be
made concrete. Pseudocode or numbered steps are welcome.)

## 7. Real-World Patterns
(Optional — when this concept actually shows up in working systems. Cite `applied` resources
here. Skip if you'd be padding.)

## 8. Best Practices
(Optional — heuristics, anti-patterns, do/don't lists. Skip if there's nothing earned to say.)

## 9. Hands-On Exercise
(Optional — a 3–5 line sketch of an exercise the learner could do. NOT a separately
generated artifact in this phase. Skip unless the topic genuinely benefits from one.)

## 10. Key Takeaways
(REQUIRED — 3 to 5 bullets. Each bullet is one assertion the learner should be able to
state after reading. No fluff like "we learned about X".)

## 11. Next Steps
(System-derived. Write the literal line: `_System-derived from the next entry in
curriculum/sequence.md._` — the sequence-update step will fill this in later.)
```

## Discipline rules (these are what the corpus critic checks — pre-pass yourself)

1. **Cite every primary resource at least once** (when resources exist). Read `topic.resources.json.resources_source`:
   - `human` or `web_search` → mandatory: every `primary` resource cited at least once. If a `primary` resource can't be cited, either (a) you misunderstand it, or (b) it's mistagged — flag in your return summary.
   - `narrative_seed_only` → no `resources` array to cite. Ground the corpus from the module's `narrative_seed_by_week` and `lab_activity_seed_by_week` instead, and **emit no `[N]` citation markers**. Fabricated citations are a hard fail at the critic.

2. **No forward references.** Every technical term you use must either be defined in this corpus's Core Concepts OR already exist in `prior_topics[*].concepts_introduced`. If a needed term isn't there, define it in Core Concepts.

3. **Length budget by depth profile.**
   - Atomic: 1500–2400 words total.
   - Standard: 3000–4400 words.
   - Deep: 5000–6000 words.
   Classify yourself based on the title + signals in `.claude/config/artifact-mix.json`.

4. **Tone.** This is the AI-Native Engineering Program. Plain language, concrete examples first, definitions second. Avoid hedging ("It is generally considered that..."). Avoid academic abstraction in the Introduction.

5. **Citations.** Inline footnote-style markers like `[1]`, `[2]`. Bibliography is NOT in the corpus (the reading artifact carries it). The corpus uses bare markers; the reading turns them into formal citations.

## Return value

After writing the file, return a JSON object the parent command can parse:

```json
{
  "path": "<topic-dir>/topic_corpus.md",
  "word_count": 3210,
  "sections_written": ["3","4","5","6","8","10","11"],
  "sections_skipped": ["2","7","9"],
  "concepts_introduced": ["temperature","sampling","determinism vs stochasticity"],
  "prerequisites": ["1.1","1.2","1.3"],
  "cross_refs": [],
  "suggested_profile": "standard",
  "profile_signals": ["title is mid-length question","Core Concepts has 2 sub-concepts"],
  "requires_diagram": false,
  "primary_resources_cited": [1, 2],
  "supporting_resources_cited": [3],
  "self_pass_check": {
    "no_forward_refs": true,
    "every_primary_cited": true,
    "length_in_range": true
  }
}
```

If `self_pass_check` has any false, **also note it in the corpus's final section** so the human reviewer sees it.

## When asked to revise

If the parent passes `--revise=<section-numbers>`, only rewrite those sections in place. Preserve all other sections verbatim. Do not change concept_introduced or prerequisites lists during a partial revision unless the revised sections genuinely change them.
