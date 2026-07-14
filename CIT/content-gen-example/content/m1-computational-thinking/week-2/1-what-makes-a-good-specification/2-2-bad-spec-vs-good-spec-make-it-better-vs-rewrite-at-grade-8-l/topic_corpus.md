---
topic_id: "2.2"
title: "Bad spec vs good spec — 'make it better' vs 'rewrite at Grade 8 level, max 80 words'"
position_in_module: 2
generated_at: "2026-06-16T00:00:00Z"
resource_count: 3
---

# 1. Bad spec vs good spec — 'make it better' vs 'rewrite at Grade 8 level, max 80 words' — Topic Corpus

## 2. Prerequisites

This topic builds directly on **2.1 — Specification, testable, bounded, observable, actionable (four-property checklist)**. You should be comfortable with the four properties of a good specification: testable, bounded, observable, and actionable. Those properties are the diagnostic lens used throughout this topic.

Concepts from Week 1 that appear here: decomposition (breaking a task into parts), abstraction (focusing on what matters), and algorithms (step-by-step instructions). You do not need to re-learn those; they are referenced by name only.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Identify which of the four properties (testable, bounded, observable, actionable) a bad specification fails.
- Distinguish between an incremental fix ("make it better") and a full rewrite using the Grade 8 / 80-word rule.
- Apply the four-property checklist to diagnose exactly what is wrong with a given specification.
- Rewrite a vague specification using the Grade 8 / 80-word constraint.
- Choose the right repair strategy — incremental fix or full rewrite — based on how many properties a specification fails.

## 4. Introduction

You have a specification. You give it to an AI tool. The AI produces something that misses the point entirely. Sound familiar?

Most of the time the problem is not the AI. The problem is the specification. A bad specification is like giving someone directions that say "go somewhere nice." The destination is unclear, there is no distance limit, and there is no way to know when you have arrived. The AI fills in the blanks — and not necessarily the way you intended [1].

Topic 2.1 gave you a checklist of four properties a good specification must have: testable, bounded, observable, and actionable. This topic puts that checklist to work. You will learn how to look at a real specification and spot exactly which property it fails. Then you will learn two repair strategies: a quick incremental fix for minor problems, and a full rewrite for specs that are broken at their core.

By the end of this topic you will be able to take a bad specification, diagnose it, fix it, and know which fix was the right choice.

## 5. Core Concepts

### 5.1 Diagnosing a bad specification: which property fails?

Before you fix anything, you need to know what is broken. A bad specification fails one or more of the four properties from topic 2.1 — each with a recognisable pattern: a spec is **not testable** when its success criterion is vague ("good," "nice," "clear"), **not bounded** when the scope is unlimited ("explain machine learning" — covers an entire field), **not observable** when the output type is unspecified ("give me feedback" — feedback in what form?), or **not actionable** when there is nothing concrete to begin on ("help me" — no task, no subject, no direction) [2].

A specification can fail more than one property at once. When more than two properties fail, the spec is not just weak — it is broken, and patching it word by word will not help. That distinction drives the choice between the two repair strategies [3].

Run through the four properties in order — testable, bounded, observable, actionable — and write "yes" or "no" for each. Every "no" is a defect to repair [2].

### 5.2 The "make it better" strategy — incremental repair

The **incremental repair strategy** means you keep the existing specification and add or change specific words to fix one failing property at a time.

Use this strategy when:
- Only **one or two** of the four properties fail.
- The core task is correct — only a constraint or a format is missing.
- The fix is a small addition, not a structural change.

**How to apply it:**

1. Check the four properties: testable, bounded, observable, actionable — mark each yes or no.
2. Identify the one or two that are "no."
3. For each failing property, add the missing constraint directly to the specification.
4. Re-check all four properties on the revised version to confirm they now pass.

**Example — fixing a single failing property:**

Original: *"Summarise the article."*

Diagnostic:
- Testable? No — "summarise" has no length or accuracy threshold.
- Bounded? No — no word limit.
- Observable? Partly — output is prose, but length is unknown.
- Actionable? Yes — there is a clear verb and a subject.

Two properties fail (testable and bounded). The core task is clear and correct, so an incremental fix is appropriate [1].

Incremental fix: *"Summarise the article in no more than 50 words."*

Re-check:
- Testable? Yes — the summary can be counted against 50 words.
- Bounded? Yes — 50-word limit.
- Observable? Yes — prose output, measurable length.
- Actionable? Yes.

All four pass. One targeted addition fixed two properties at once [1].

### 5.3 The "Grade 8 / 80-word rewrite" strategy — full rewrite

Sometimes the specification is not just missing a constraint — it is structurally vague. The vocabulary is too complex, the intent is buried, or so many things are wrong that patching each one in turn will take longer than starting fresh.

The **Grade 8 / 80-word rewrite strategy** is a full replacement. You throw out the original wording and write a new specification from scratch, following two hard constraints [3]:

- **Grade 8 reading level** — plain words, short sentences. Imagine explaining the task to a capable 13-year-old. Avoid jargon, technical shorthand, and words that carry multiple possible meanings.
- **Maximum 80 words** — brevity forces clarity. If you cannot say what you want in 80 words, you have not finished thinking about what you want.

These two constraints work together. Keeping sentences short forces you to be specific. Using plain words forces you to name the actual task rather than hiding behind vague verbs like "help," "discuss," or "address." [3]

**When to use the full rewrite:**

| Situation | Strategy |
|---|---|
| One property fails | Incremental fix |
| Two properties fail but the core task is clear | Incremental fix |
| Three or four properties fail | Full rewrite |
| The existing wording is ambiguous beyond repair | Full rewrite |
| The spec uses jargon or domain terms that need unpacking | Full rewrite |
| You have tried incremental fixes twice and the spec still fails | Full rewrite |

The full rewrite is not an admission of failure. It is the faster path when the foundation is unsound [3].

### 5.4 Worked before/after pairs

The following pairs show both strategies applied to real-world situations. Each pair includes the diagnostic step so you can see why a particular strategy was chosen [1][2][3].

---

**Pair 1 — Incremental fix (one failing property)**

Before: *"Write a professional email."*

Diagnostic:
- Testable? No — "professional" is a judgment call with no threshold.
- Bounded? Partly — email is a format, but there is no word limit.
- Observable? Yes — output is an email.
- Actionable? Partly — but to whom? About what?

Two properties fail (testable, actionable) but the type of output is correct. The core task is recognisable. Incremental fix is appropriate [2].

After: *"Write a 100-word professional email to a new client, thanking them for signing up and offering one next step they can take today."*

What changed: added a word count (bounded, testable), a recipient ("new client," actionable), a purpose ("thanking them"), and a specific output requirement ("one next step"). Four properties now pass [2].

---

**Pair 2 — Full rewrite (three properties fail)**

Before: *"Help me with my project."*

Diagnostic:
- Testable? No — "help" has no measurable outcome.
- Bounded? No — "project" could be anything.
- Observable? No — no output format.
- Actionable? No — no concrete task.

All four properties fail. Incremental repair would mean rewriting nearly every word. A full rewrite is faster and cleaner [1][3].

Full rewrite: *"List five steps to plan a 10-minute presentation for a school science project. Each step should take no more than two sentences to describe."*

Grade 8 check: short words, one idea per sentence, no jargon.
80-word check: the rewrite is 31 words. Pass.

All four properties pass:
- Testable — you can count five steps.
- Bounded — "10-minute presentation," "no more than two sentences."
- Observable — numbered list.
- Actionable — "List five steps to plan..." [1][3].

---

**Pair 3 — Full rewrite (scope too wide + jargon)**

Before: *"Provide a comprehensive overview of machine learning paradigms, including supervised, unsupervised, and reinforcement learning, with emphasis on practical applications and theoretical underpinnings."*

Diagnostic:
- Testable? No — "comprehensive overview" has no scope limit.
- Bounded? No — three entire subfields of machine learning.
- Observable? No — no format, no length.
- Actionable? Partially — but "with emphasis on both X and Y" gives conflicting priorities.

Three properties fail, and the vocabulary ("paradigms," "theoretical underpinnings") is far above Grade 8 level [1][3].

Full rewrite: *"Explain what machine learning is in plain English. Use one real-life example. Keep the answer under 150 words."*

Grade 8 check: every word is common. One idea per sentence.
80-word check (the spec itself): the rewrite is 23 words. Pass.

All four properties pass: "explain what machine learning is" (actionable), "under 150 words" (bounded, testable), "plain English, one example" (observable) [1][3].

---

### 5.5 The decision rule — which strategy to use

Choosing between the two strategies comes down to a single question: **How many of the four properties fail?**

```
Run four-property diagnostic
        |
  0 properties fail ──→ Specification is good. No repair needed.
        |
  1–2 properties fail ──→ Incremental fix: add the missing constraint(s).
        |
  3–4 properties fail ──→ Full rewrite: Grade 8 level, max 80 words.
```

A second trigger for a full rewrite: if after two rounds of incremental fixing the diagnostic still shows failures, stop patching and rewrite [3].

**Why Grade 8 and 80 words specifically?**

- Grade 8 reading level is roughly the complexity of a clear newspaper article. It is plain enough that any reader — human or AI — can parse it without ambiguity.
- 80 words is long enough to include a task, a constraint, and an output format, but short enough to force you to cut anything vague. If your rewrite exceeds 80 words, that is a signal you are still trying to do too many things at once [3].

These are not arbitrary numbers. They are practical thresholds that correlate with specifications that produce reliable, predictable outputs from AI tools [2][3].

## 6. Implementation

### Step-by-step: applying the repair process

Follow these steps whenever you encounter a specification you are unsure about:

1. **Write out the specification.** Put the exact wording in front of you — do not work from memory.

2. **Run the four-question diagnostic.**
   - Ask each of the four questions (testable? bounded? observable? actionable?).
   - Mark each property pass or fail.

3. **Count the failures.**
   - 0 failures → done. The spec is good.
   - 1–2 failures → go to step 4 (incremental fix).
   - 3–4 failures → go to step 5 (full rewrite).

4. **Incremental fix.**
   - For each failing property, identify the specific word or phrase that causes the failure.
   - Add a constraint that directly addresses that property.
   - Re-run the diagnostic. If all four pass, stop. If any still fail, check whether the count has risen — if so, switch to a full rewrite.

5. **Full rewrite (Grade 8, max 80 words).**
   - Set aside the original wording entirely.
   - Ask yourself: what is the one thing I want the AI to do?
   - Write that task in one short sentence.
   - Add one constraint sentence (word count, format, or scope limit).
   - Add one output-format sentence if not already clear.
   - Count the words. Trim to 80 or under.
   - Re-run the four-question diagnostic. All four should now pass.

6. **Test the repaired specification.**
   - Give the repaired spec to an AI tool.
   - Does the output match what you expected? If not, run the diagnostic again — the problem may be in the output, not the spec.

## 7. Real-World Patterns

In professional settings, vague specifications appear all the time — not just with AI tools but with any collaborator (a developer, a designer, a copy-writer). The same diagnostic and repair strategies apply [3].

**Customer support prompts.** A support team using an AI chatbot found their bot gave inconsistent answers because the system prompt said "be helpful and friendly." That fails testable (no accuracy threshold), bounded (no topic limit), and observable (no response format). A rewrite to "Answer customer questions about returns only. Give one direct answer in three sentences or fewer" fixed three failing properties at once [2][3].

**Content summarisation.** A marketing team asking an AI to "make the article shorter" got outputs ranging from one sentence to ten paragraphs. Incremental fix: "Reduce the article to 200 words, keeping the headline and the three main points." One failing property (bounded) was the only defect [1].

**Data requests.** An analyst asked an AI to "pull the important data." Three properties fail immediately. A full rewrite: "List the five highest sales figures from last month's spreadsheet. Show the product name and the amount for each one. Use a numbered list." Bounded (five items), observable (numbered list with two fields), actionable (list), testable (verifiable against the spreadsheet) [2][3].

These examples confirm the pattern: the incremental fix works when the task is clear and only a constraint is missing. The full rewrite is needed when the task itself is unclear or uses language that carries too many possible meanings [1][2][3].

## 8. Best Practices

**Do:**
- Run the four-question diagnostic before deciding on a repair strategy. Guessing which property fails wastes time.
- Write the Grade 8 / 80-word spec as if you are explaining the task to a smart, motivated person who knows nothing about your domain.
- Use a word count tool. "Under 80 words" is easy to misjudge without counting.
- Treat the 80-word limit as a compression exercise. Every word that survives must earn its place.
- Re-run the diagnostic on the repaired spec. A fix that patches one property can accidentally break another.

**Don't:**
- Do not use words like "comprehensive," "thorough," "in-depth," or "holistic" — they are untestable by definition.
- Do not stack multiple tasks in one specification ("write, analyse, and summarise"). Each task should be its own specification.
- Do not assume that adding more words makes a specification clearer. Length and clarity are not the same thing [3].
- Do not skip the diagnostic and go straight to a rewrite. Sometimes an incremental fix is all that is needed, and a full rewrite takes more time than necessary [2].
- Do not keep patching a specification that has failed two rounds of incremental fixes. At that point a rewrite is faster [3].

**A common trap — adding vague qualifiers:**

A beginner attempting to fix "Write an email" might produce "Write a good email." That adds a word but does not fix the testable property — "good" is still unmeasurable. The fix must be concrete: "Write a 50-word email introducing the product to a new subscriber. End with one question." [1][2]

## 9. Hands-On Exercise

Take the following three specifications. For each one:

1. Run the four-question diagnostic and note which properties fail.
2. Choose the repair strategy (incremental fix or full rewrite) and state why.
3. Write the repaired specification.

**Spec A:** *"Make the presentation better."*

**Spec B:** *"Translate this paragraph into simple English."*

**Spec C:** *"Provide a detailed analysis of the competitive landscape, including key players, market share, recent developments, and strategic implications for our business unit."*

After writing your repairs, count the words in each repaired spec. If any exceeds 80 words, trim it down while keeping all four properties intact.

## 10. Key Takeaways

- A bad specification almost always fails one or more of the four properties: testable, bounded, observable, actionable. Diagnosing which property fails is the first step of any repair.
- Use the **incremental fix** when one or two properties fail and the core task is correct — add the missing constraint without rewriting the whole spec.
- Use the **full rewrite** when three or four properties fail, when the wording is ambiguous beyond repair, or when two rounds of incremental fixing have not produced a passing spec.
- The **Grade 8 / 80-word rule** forces precision: plain language removes ambiguity; the 80-word limit forces you to have one clear task, one constraint, and one output format.
- The decision rule is simple: count the failures. 1–2 failures → incremental fix. 3–4 failures → full rewrite.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
