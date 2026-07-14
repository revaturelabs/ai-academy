<!-- nav:top:start -->
[⬅ Previous: 2.1 — What makes a good specification](../../2-1-what-makes-a-good-specification-testable-bounded-observable/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.3 — How to identify the inputs, expected outputs, and failure conditions of a task ➡](../../2-3-how-to-identify-the-inputs-expected-outputs-and-failure-cond/artifacts/reading.md)
<!-- nav:top:end -->

---

# Bad spec vs good spec — 'make it better' vs 'rewrite at Grade 8 level, max 80 words'

## Overview

You now know the four properties a good specification must have: testable, bounded, observable, and actionable. The next question is what to do when a specification fails one or more of them. This topic gives you two repair strategies — a quick targeted fix for minor problems, and a full rewrite for specifications that are broken at their core — so you can turn a bad specification into a reliable one before the AI ever sees it [1].

## Key Concepts

### Diagnosing which property fails

Before you repair anything, you need to know exactly what is broken. A bad specification almost always fails one or more of the four properties. Use this table as a diagnostic tool [2]:

| Property | The question it asks | What a failure looks like |
|---|---|---|
| **Testable** | Can you check whether the output is correct? | "Write something good" — "good" has no measurable threshold |
| **Bounded** | Is the scope limited enough? | "Explain machine learning" — covers an entire field with no end |
| **Observable** | Is the output format specified? | "Give me feedback" — feedback as a list? As prose? On what? |
| **Actionable** | Can the AI start immediately? | "Help me" — no task, no subject, no direction |

Run the diagnostic in four questions, in order:

1. Can I write a simple test to check the output? (Testable)
2. Is there a clear finish line — a limit on length, scope, or topic? (Bounded)
3. Does the spec say what form the answer should take? (Observable)
4. Is there a concrete task the AI can start on right now? (Actionable)

Every "no" is a defect to repair [2].

### Strategy 1 — Incremental fix ("make it better")

The **incremental fix** means keeping the existing specification and adding specific words to address each failing property — one property at a time.

Use it when:
- Only **one or two** of the four properties fail.
- The core task is correct — only a constraint or a format is missing.
- The repair is an addition, not a structural change.

**How to apply it:**

1. Run the four-question diagnostic and mark each property pass or fail.
2. For each failing property, add the missing constraint directly to the specification.
3. Re-run the diagnostic on the revised version to confirm all four now pass.

One warning: adding vague words does not count as a fix. Changing "Write an email" to "Write a good email" adds a word but does not fix the testable property — "good" is still unmeasurable. Every fix must be concrete [1][2].

### Strategy 2 — Full rewrite (Grade 8 level, max 80 words)

Sometimes the specification is not just missing a constraint — the task itself is unclear, the vocabulary is too complex, or so many properties fail that patching them one by one takes longer than starting fresh [3].

The **Grade 8 / 80-word rewrite** is a complete replacement. You set aside the original wording entirely and write a new specification from scratch, following two hard constraints:

- **Grade 8 reading level** — plain words, short sentences. Imagine explaining the task to a capable 13-year-old. Avoid jargon and words that carry multiple possible meanings.
- **Maximum 80 words** — brevity forces clarity. If you cannot say what you want in 80 words, you have not finished thinking about what you want.

These two constraints work together: short sentences force you to be specific, and plain words force you to name the actual task rather than hiding behind vague verbs like "help," "discuss," or "address" [3].

**When to use the full rewrite:**

| Situation | Strategy |
|---|---|
| One or two properties fail, core task is clear | Incremental fix |
| Three or four properties fail | Full rewrite |
| Wording is ambiguous beyond repair | Full rewrite |
| Two rounds of incremental fixing have not produced a passing spec | Full rewrite |

The full rewrite is not an admission of failure — it is the faster path when the foundation is unsound [3].

### The decision rule

The choice between strategies comes down to one question: **how many of the four properties fail?**

- 0 failures — the specification is good. No repair needed.
- 1–2 failures — use the incremental fix: add the missing constraint or format.
- 3–4 failures — use the full rewrite: Grade 8 level, max 80 words.

## Worked Example

This example shows both strategies applied to real specifications, with the diagnostic step made visible.

**Incremental fix — two properties fail**

Original: *"Summarise the article."*

Diagnostic:
- Testable? No — "summarise" has no length or accuracy threshold.
- Bounded? No — no word limit.
- Observable? Partly — output is prose, but length is unknown.
- Actionable? Yes — clear verb, clear subject.

Two properties fail (testable, bounded). The core task is correct. An incremental fix is appropriate [1].

Fix: *"Summarise the article in no more than 50 words."*

Re-check: all four properties now pass. One targeted addition fixed two properties at once.

---

**Full rewrite — all four properties fail**

Original: *"Help me with my project."*

Diagnostic:
- Testable? No — "help" has no measurable outcome.
- Bounded? No — "project" could be anything.
- Observable? No — no output format.
- Actionable? No — no concrete task.

All four properties fail. Patching each one in turn would mean rewriting nearly every word — a full rewrite is faster [1][3].

Rewrite: *"List five steps to plan a 10-minute presentation for a school science project. Each step should take no more than two sentences to describe."*

Grade 8 check: short words, one idea per sentence, no jargon. Pass.
80-word check: the rewrite is 31 words. Pass.

All four properties pass:
- Testable — you can count five steps.
- Bounded — "10-minute presentation," "no more than two sentences."
- Observable — numbered list.
- Actionable — "List five steps to plan…"

## In Practice

Vague specifications cause problems in professional settings too — not just in student work. The same diagnostic and repair strategies apply wherever you are giving instructions to an AI tool [3].

**Content summarisation.** A marketing team asked an AI to "make the article shorter" and got outputs ranging from one sentence to ten paragraphs. Only one property failed (bounded). Incremental fix: "Reduce the article to 200 words, keeping the headline and the three main points." [1]

**Customer support prompts.** A support team's chatbot gave inconsistent answers because its system prompt said "be helpful and friendly." That fails testable (no accuracy threshold), bounded (no topic limit), and observable (no response format). Three properties fail — a full rewrite to "Answer customer questions about returns only. Give one direct answer in three sentences or fewer" was the right call [2][3].

**Common traps to avoid:**

- Do not use words like "comprehensive," "thorough," or "in-depth" — they are untestable by definition.
- Do not stack multiple tasks in one specification. Each task should be its own specification.
- Do not assume that adding more words makes a specification clearer. Length and clarity are not the same thing [3].
- Do not keep patching a specification that has already failed two rounds of incremental fixes. At that point, a rewrite is faster [2].

## Key Takeaways

- A bad specification almost always fails one or more of the four properties. Diagnosing which property fails is the first step of any repair.
- Use the **incremental fix** when one or two properties fail and the core task is correct — add the missing constraint without rewriting the whole specification.
- Use the **full rewrite** when three or four properties fail, when the wording is ambiguous beyond repair, or when two rounds of incremental fixing have not produced a passing specification.
- The **Grade 8 / 80-word rule** enforces precision: plain language removes ambiguity, and the 80-word limit forces you to have one clear task, one constraint, and one output format.
- The decision rule is simple: count the failures. 1–2 failures → incremental fix. 3–4 failures → full rewrite.

## References

1. Sai Charan Kummetha, "Few Examples of Bad Prompts and How to Improve Them." <https://saicharankummetha.medium.com/few-examples-of-bad-prompts-and-how-to-improve-them-e717a1087735>
2. MyGreatLearning, "5 Common Prompt Engineering Mistakes Beginners Make." <https://www.mygreatlearning.com/blog/prompt-engineering-beginners-mistakes/>
3. DigitalOcean, "Prompt Engineering Best Practices." <https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices>

---
<!-- nav:bottom:start -->
[⬅ Previous: 2.1 — What makes a good specification](../../2-1-what-makes-a-good-specification-testable-bounded-observable/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.3 — How to identify the inputs, expected outputs, and failure conditions of a task ➡](../../2-3-how-to-identify-the-inputs-expected-outputs-and-failure-cond/artifacts/reading.md)
<!-- nav:bottom:end -->
