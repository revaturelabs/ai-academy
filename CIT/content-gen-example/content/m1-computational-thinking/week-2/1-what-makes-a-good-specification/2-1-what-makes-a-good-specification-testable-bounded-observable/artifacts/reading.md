<!-- nav:top:start -->
[⬅ Previous: 1.12 — Choosing your domain](../../../../week-1/5-applying-it-to-your-domain/1-12-choosing-your-domain-writing-a-3-sentence-problem-statement/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.2 — Bad spec vs good spec ➡](../../2-2-bad-spec-vs-good-spec-make-it-better-vs-rewrite-at-grade-8-l/artifacts/reading.md)
<!-- nav:top:end -->

---

# What makes a good specification — testable, bounded, observable, actionable

## Overview

A specification is the instruction you give before work begins — it tells a system, a person, or an AI tool exactly what result you want. In Week 1, you learned that algorithms must be unambiguous and that AI does not always give the same answer twice. A vague instruction given to a regular program produces the same wrong result every time, but given to an AI it produces a different wrong result every time — which is much harder to fix [1]. That is why a good specification must have four properties — testable, bounded, observable, and actionable — to turn a vague request into an instruction clear enough to check, repeat, and improve [2].

## Key Concepts

Think of these four properties as four checks you run before giving an AI any instruction. Missing even one is usually why AI output does not turn out the way you hoped — not because the AI is broken, but because the instruction was not clear enough [3].

### 1. Testable

A **testable** specification means you can check — after the AI finishes — whether the output is correct or not. You need a clear pass or fail condition.

- **Good:** "List 3 camping essentials, one per bullet, each under 10 words." You can count the bullets and check the length.
- **Bad:** "Tell me what to bring camping." How many items? How much detail? There is no way to know if it gave you enough.

After writing any specification, ask: "If the AI gave me two different outputs, could I compare them to my spec and pick the better one without relying on gut feeling?" If yes, the spec is testable [1].

### 2. Bounded

A **bounded** specification sets clear limits so the AI only works on what you asked for — nothing more, nothing less.

- **Good:** "Fix only the spelling mistakes in the first paragraph; do not change any words or sentences." The AI knows exactly what to fix and what to leave alone.
- **Bad:** "Fix my paragraph." The AI might rewrite sentences, change your tone, or restructure things you never wanted touched.

Think of a bounded specification like a fence around a garden. Everything inside the fence is the job. Everything outside is not [2]. Common bounding dimensions include:

| Dimension | Example |
|---|---|
| Length | "Under 100 words" / "Exactly 5 bullets" |
| Audience | "For a 12-year-old" / "For a senior manager" |
| Scope | "Cover only X, not Y or Z" |
| Format | "Use a numbered list" / "Use a table" |

### 3. Observable

An **observable** specification produces output you can read and verify straight away — no guessing or extra work needed to figure out whether the task succeeded.

- **Good:** "Give me 3 reasons why students procrastinate, one reason per line." You can read the three lines immediately and check if it answered the question.
- **Bad:** "Explain why students procrastinate." The AI might write three paragraphs of general advice and you are left wondering whether it actually answered what you asked.

Observable is related to testable, but the two are not the same. A result can be visible — you can see the AI produced *something* — but still not testable if you cannot tell whether what it produced is *correct*. Both properties are needed [1].

Ask yourself: "What will I actually receive? Can I put it in a document, read it aloud, or count it?" If yes, the spec is observable.

### 4. Actionable

An **actionable** specification gives the AI enough detail to start the task immediately, without having to guess what you mean.

- **Good:** "Rewrite this sentence in simple English so a 10-year-old can understand it, and keep it under 20 words." The AI knows exactly what to do and where to stop.
- **Bad:** "Make this sentence better." Better how? Shorter? Simpler? More formal? The AI will guess — and its guess may not match what you wanted [3].

A human worker can ask for clarification. An AI tool, in most workflows, will not stop and ask — it will make a choice and keep going. If a critical detail is missing, the AI fills the gap with a default assumption, which may be wrong [2].

Read your specification as if you are the AI and know nothing about the situation. Do you have everything needed to begin? If you would need to ask a question first, the spec is not yet fully actionable.

## Worked Example

Let's take a poor instruction and fix it step by step.

**Starting point:** "Make this email better." — you cannot check if it worked, there are no limits on what to change, and the AI has no idea what "better" means to you.

Here is how to fix it, one step at a time:

1. **Give it a direction** — "Rewrite this email to sound more professional."
2. **Set a limit** — "...keep it under 100 words."
3. **Add a clear rule** — "...do not change the deadline date."
4. **Tell it what to give back** — "...output only the rewritten email, no extra explanation."

**Final specification:** "Rewrite this email to sound more professional, keep it under 100 words, do not change the deadline date, and output only the rewritten email with no extra explanation."

Now you can check the output with four yes/no questions:

- Does it sound professional? ✓
- Is it under 100 words? ✓
- Is the deadline date unchanged? ✓
- Is it just the email text, nothing extra? ✓

If any answer is no, you know exactly what went wrong and how to fix it [1].

## In Practice

Before submitting any specification to an AI tool, run it against these four questions:

- Can I tell if this worked or not? **(testable)**
- Did I set clear limits on what the AI should and should not touch? **(bounded)**
- Can I read the output and know straight away whether it worked? **(observable)**
- Does the AI have everything it needs to start without guessing? **(actionable)**

Missing any one of these is the most common reason AI output disappoints. Three mistakes students frequently make:

- **A longer instruction is not always a better one.** Only add words if they help with one of the four properties above. Extra words that do not serve any property make the instruction harder to follow [3].
- **One good result does not mean your specification is reliable.** Because AI can give a different answer each time, getting a good output once does not mean it will work again. Test your specification more than once before trusting it [2].
- **AI will not stop and ask you what you meant.** Unlike a classmate, it will silently fill in the gaps with its own guess — and you will have no idea it did that [1].

The four-property approach is not limited to AI. Software developers write "acceptance criteria" before building a feature — a well-known format is "Given [context], when [action], then [observable result]" — which maps directly onto testable, observable, and actionable. The same discipline turns up in data analysis, workplace delegation, and any situation where you need to communicate a task precisely to someone who cannot read your mind [2].

## Key Takeaways

- **Testable:** after every run, you should be able to say clearly — did this pass or fail? Include a condition you can check.
- **Bounded:** always set clear limits on what the AI should and should not touch so it stays within the task you gave it.
- **Observable:** the output should be something you can read and check straight away — no digging through vague responses or guessing required.
- **Actionable:** give enough detail so the AI can start the task immediately without filling in the gaps itself.
- All four properties work together — a specification needs to satisfy all four to produce a reliable result every time, not just once.

## References

1. MIT Sloan Educational Technology, "Effective Prompts for AI: The Essentials." <https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/>
2. Lakera, "The Ultimate Guide to Prompt Engineering in 2026." <https://www.lakera.ai/blog/prompt-engineering-guide>
3. Project Management Institute, "A Simple Framework for Writing Better AI Prompts." <https://www.pmi.org/blog/how-to-write-better-prompts-framework>

---
<!-- nav:bottom:start -->
[⬅ Previous: 1.12 — Choosing your domain](../../../../week-1/5-applying-it-to-your-domain/1-12-choosing-your-domain-writing-a-3-sentence-problem-statement/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.2 — Bad spec vs good spec ➡](../../2-2-bad-spec-vs-good-spec-make-it-better-vs-rewrite-at-grade-8-l/artifacts/reading.md)
<!-- nav:bottom:end -->
