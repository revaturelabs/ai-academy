<!-- nav:top:start -->
[⬅ Previous: 1.11 — The four properties of a good algorithm](../../../4-algorithmic-thinking/1-11-the-four-properties-of-a-good-algorithm-finite-definite-inpu/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.1 — What makes a good specification ➡](../../../../week-2/1-what-makes-a-good-specification/2-1-what-makes-a-good-specification-testable-bounded-observable/artifacts/reading.md)
<!-- nav:top:end -->

---

# Choosing your domain — writing a 3-sentence problem statement

## Overview

Before you write a single line of pseudocode or draw a flowchart, you need to know exactly what problem you are solving. Jumping straight to solutions is the most common mistake in computing — and the hardest to recover from later. A **problem statement** is a short, focused piece of writing — exactly three sentences — that pins down the problem before any solution thinking begins [1]. Getting this right gives you a stable foundation to decompose and abstract from throughout the rest of the course.

## Key Concepts

Every problem statement has two building blocks: a **problem domain** and the statement itself. These are easy to confuse, so let's take them one at a time.

### 1. Problem domain

A **problem domain** is the specific area of real-world activity your project addresses. It is not a technology or a tool — it is a slice of real life.

- Examples of domains: healthcare, student revision, local transport, food waste, personal finance.
- A domain is the setting. The problem is what goes wrong inside that setting.
- You pick one domain and return to it all semester — so choose something you find genuinely interesting.

**Why it matters:** a domain that is too broad ("technology in society") gives you nowhere to stand. A specific domain ("secondary school exam revision") gives you a real group of people and a real situation to study [2].

### 2. Problem statement

A **problem statement** is a short written description of who is affected, what specifically goes wrong, and why it matters. It is not a solution proposal — it must not mention apps, systems, or fixes of any kind [1].

Three rules before you write a single word:

- **Specific, not general.** "Elderly patients living alone" is a group. "Everyone" is not.
- **One problem, not a list.** If you wrote "and also…" in your draft, split it into two and pick the stronger one.
- **No solution embedded.** If your sentence says "I will build an app that…", stop and rewrite it as a problem [3].

### 3. The 3-sentence format

Each sentence does exactly one job. Nothing more.

![3-sentence problem statement format](./diagram.png)
*Three-slot pipeline: each sentence carries one piece of information — context, specific problem, impact.*

| Sentence | Job | Question it answers |
|---|---|---|
| **Sentence 1 — Context** | Sets the scene | Who is affected, and in what situation? |
| **Sentence 2 — Specific problem** | Names what goes wrong | What exactly is the problem? |
| **Sentence 3 — Impact** | States the consequence | What real-world harm or cost does this cause? |

Think of it as three slots. Each slot holds one idea. A sentence that tries to fill two slots usually does neither well [2].

## Worked Example

Here is a complete problem statement for a student revision domain:

> "Secondary school students preparing for public examinations often have no reliable way to know which topics they understand well and which they are still weak on. As a result, they frequently over-revise familiar material and under-revise the areas that would most improve their grade. A solution to this problem would need to track understanding across topics and surface the weakest areas for a student without requiring a teacher to be present."

Apply the three quality tests:

- Specific group? **Yes** — "secondary school students preparing for public examinations."
- One problem? **Yes** — the inability to judge their own topic-level understanding.
- No solution named? **Yes** — Sentence 3 describes what a solution would need to do, not what it is.

Now look at a counter-example:

> "Healthcare has a lot of problems. Technology could help make things better for everyone."

What is wrong?

- No specific group — "everyone" is not a group.
- No specific problem — "a lot of problems" names nothing.
- No consequence — nothing about what harm this causes.

This is two vague sentences, not a problem statement. It fails all three quality tests [3].

## In Practice

Use this five-step checklist each time you write a problem statement [1][2]:

1. **Choose your domain.** Pick one area of real life that genuinely interests you — you will work with it all semester.
2. **Name who is specifically affected.** Identify a real group of people, not "everyone" or "society."
3. **State what exactly goes wrong.** One problem only — be precise enough that someone outside your domain would understand it.
4. **State the consequence.** What harm, cost, or frustration does this problem cause?
5. **Write the three sentences, then run the quality tests.**

**Quality test checklist:**

- Is the affected group specific enough to picture? (Not "people" — which people, where, when?)
- Is there exactly one problem in Sentence 2? (If "and" appears, split and pick one.)
- Does any sentence name or imply a technology fix? (If yes, cut it.)

A strong problem statement is not a long one. Three sentences that pass all three tests are worth far more than a paragraph that drifts into solutions [3].

## Key Takeaways

- **Problem domain** = the real-world area you are working in; **problem statement** = three sentences covering context, specific problem, and impact.
- Each sentence does exactly one job — mixing jobs into one sentence weakens both.
- Three quality tests: specific group, one problem only, no solution embedded [1].
- A problem statement that passes all three tests gives you a stable base to apply decomposition (breaking the problem into sub-tasks) and abstraction (focusing on what matters, ignoring what does not).
- Vague problem statements produce vague designs — precision here saves rework at every stage that follows [2].

## References

1. National University LibGuides, "Structured Problem Statement Guide." <https://resources.nu.edu/c.php?g=1013602&p=7638573>
2. BetterUp, "How to Write a Problem Statement." <https://www.betterup.com/blog/problem-statement>
3. Notion, "How to Write Problem Statements." <https://www.notion.com/blog/problem-statements>

---
<!-- nav:bottom:start -->
[⬅ Previous: 1.11 — The four properties of a good algorithm](../../../4-algorithmic-thinking/1-11-the-four-properties-of-a-good-algorithm-finite-definite-inpu/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.1 — What makes a good specification ➡](../../../../week-2/1-what-makes-a-good-specification/2-1-what-makes-a-good-specification-testable-bounded-observable/artifacts/reading.md)
<!-- nav:bottom:end -->
