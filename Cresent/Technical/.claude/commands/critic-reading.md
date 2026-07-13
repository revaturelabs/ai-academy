---
description: Run the reading critic — length, citations, prereq alignment, forward-reference discipline.
allowed-tools: [Read, Write, Bash, Task]
argument-hint: "<topic-id>"
---

# /critic-reading

Dispatch the **reading-critic** subagent.

## Refuse if
- `gates.reading_generated` is not true.
- Caveman not active.

## What to check
0. **Format discipline (hard fail).** `reading.md` has NO frontmatter (first non-empty line is the `# <title>` H1); the sidecar `reading.meta.json` exists + parses; the reading carries exactly the six fixed sections in order (`Overview` / `Key Concepts` / `Worked Example` / `In Practice` / `Key Takeaways` / `References`, References optional only when zero citations).
1. **Length budget compliance.** Word count must fall in `artifact_plan.reading.target_word_range`. Reading-aloud-time estimate (≈230 wpm) must fall in the minute range. Both under and over → flag.
2. **Citation discipline.** Every `primary` resource cited at least once. Each citation is footnote-style with a bibliography at the bottom.
3. **No forward references.** Same rule as the corpus critic: only concepts from prior topics + this topic's corpus.
4. **Tone fit.** AI-native engineering program — readings should bias toward concrete examples, plain language, and 8th-grade specification voice. Flag wall-of-text definitions, jargon dumps, or hedging.
5. **Faithfulness to corpus.** No new claims introduced by the reading that aren't in the corpus. The reading is curated walkthrough, not new content.

## Output `<topic-dir>/critic-reports/reading.critic.json` with the same shape as corpus.critic.json.

## On result
- Pass: `set reading_critic_passed true`, stage `reading_approved`, suggest next command.
- Fail: log the verdict, ask whether to auto-rerun `/generate-reading` with the critic's notes attached.
