<!-- nav:top:start -->
[⬅ Previous: 2.2 — Bad spec vs good spec](../../2-2-bad-spec-vs-good-spec-make-it-better-vs-rewrite-at-grade-8-l/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.4 — Pattern recognition ➡](../../../2-how-machines-recognise-patterns/2-4-pattern-recognition-how-machines-find-rules-in-repeated-data/artifacts/reading.md)
<!-- nav:top:end -->

---

# How to identify the inputs, expected outputs, and failure conditions of a task

## Overview

You have learned that a good specification must be testable, bounded, observable, and actionable. Those four properties tell you how to judge a specification. This topic teaches you how to build one — specifically, how to find the three pieces a specification needs most: the inputs, the expected outputs, and the failure conditions. Most weak specifications are not wrong; they are incomplete. A key piece of information is missing, and the AI fills the gap with a guess [1].

## Key Concepts

A complete specification has six named parts. Each part answers one specific question about the task. This topic teaches three of those parts at full depth — the three that most directly determine whether an AI task succeeds or fails.

| Component | The question it answers |
|---|---|
| Task description | What is the AI supposed to do? |
| **Inputs** | What raw material does the AI need to start? |
| **Expected outputs** | What should the result look like? |
| Format and constraints | How should the result be structured and bounded? |
| **Failure conditions** | What counts as a problem, and how should the AI handle it? |
| Success criteria | How will I know the output is correct? |

Task description, format and constraints, and success criteria are each covered in companion topics in this module. The three in bold are the focus here.

---

### Component 1 — Inputs

**Inputs** are everything the AI needs to have — or needs to know — before it can start the task. An input is any piece of raw material, context, or data the AI will work with or work from.

Without clearly stated inputs, the AI either makes up material or applies the task to the wrong thing [1]. Both outcomes waste your time.

**Types of inputs you might specify:**

| Input type | Example |
|---|---|
| A document or text | "The email thread pasted below" |
| A data set or list | "The five product names listed here: ..." |
| Context about the audience | "The reader is a first-year university student" |
| A constraint on what to use | "Use only the paragraph above — do not use outside knowledge" |
| Background the AI needs | "The deadline is Friday. The client expects a draft, not a final version." |

An AI tool does not automatically know what document or context you mean. If you say "summarise this," the AI infers what "this" means from whatever is in front of it — which may not be what you intended. Naming the input removes that inference [2].

---

### Component 2 — Expected Outputs

**Expected outputs** describe what the AI should produce. They answer the question: "What will I actually receive when the task is done?"

Specifying the output makes the result **observable** — a property you learned in topic 2.1. An observable output is something you can read, count, or measure. An unobservable output is vague and unmeasurable [2].

Every expected output has three dimensions. All three should be explicit:

1. **Type** — What kind of thing is it? A numbered list? A paragraph? A table? A single sentence?
2. **Content** — What must the output contain? What must it not contain?
3. **Amount** — How many items, sentences, or words?

If any one dimension is left open, the AI will make a choice for you.

**A common mistake — specifying type but not content:**

*"Give me a list of ideas."*

Type is specified (a list). Content is not (ideas about what?). Amount is not (how many?). The output is still mostly unobservable because you cannot check whether the content is correct [2].

---

### Component 3 — Failure Conditions

**Failure conditions** are the situations in which the AI cannot — or should not — complete the task as specified, and what it should do instead.

This is the component most beginners leave out. Omitting it is one of the most common reasons AI outputs are unreliable in practice [3].

**Why failure conditions matter.** A human worker, when they hit a problem, stops and asks a question: "I cannot find that file — can you send it again?" An AI tool does not stop. It produces something anyway. Without failure conditions, the AI may:

- Make up missing information — a behaviour called **hallucination** (producing plausible-sounding but incorrect content).
- Silently skip a part of the task without telling you.
- Produce an output that looks complete but is based on wrong assumptions [3].

Specifying failure conditions gives the AI explicit instructions for those situations. Instead of guessing, it follows your rule.

**Three categories of failure conditions to cover:**

1. **Missing input** — What should the AI do if the input is incomplete or absent?
   - Example: *"If the product description is missing, write 'No description provided' and stop — do not invent a description."*

2. **Input outside scope** — What should the AI do if the input does not match what the task assumes?
   - Example: *"If the text is not in English, translate it first before summarising. If you cannot identify the language, state 'Language not recognised' and stop."*

3. **Ambiguous or conflicting content** — What should the AI do if the input contains contradictions or unclear information?
   - Example: *"If the complaint refers to two different orders, address only the most recent one. Flag the second by writing 'Note: a second order was mentioned but not addressed.'"*

In topic 2.1 you learned that AI tools are probabilistic — they do not always give the same answer twice. Failure conditions reduce that variability at the edges of a task, where the input is messy or incomplete [2][3].

## Worked Example

**Task:** You want an AI to write a brief summary of a job applicant's cover letter for a hiring manager to read before an interview.

Here is how you identify and write the three components step by step.

---

**Step 1 — Identify the inputs.**

Ask: "What does the AI need to have before it can start?"

- The full text of the cover letter (pasted below the specification).
- Context: the role is a junior data analyst position. The hiring manager has 3 minutes to read the summary before the interview.

Both pieces are included because the AI needs the raw material (the letter) and the context (the role and time constraint) to do the task correctly [1].

---

**Step 2 — Describe the expected output.**

Ask: "What will I actually receive — type, content, and amount?"

- **Type:** three bullet points.
- **Content:** each bullet covers one thing in order — (1) the applicant's relevant experience, (2) their stated motivation for applying, (3) one specific skill or achievement they highlight.
- **Amount:** each bullet is one sentence.

All three dimensions are named, so the output is observable and checkable [2].

---

**Step 3 — Write the failure conditions.**

Ask: "What could go wrong with the input?"

- If the cover letter does not mention relevant experience, write "No relevant experience mentioned" for bullet 1.
- If the cover letter is fewer than 50 words, write "Cover letter too short to summarise reliably" and stop.
- If the cover letter is not in English, state "Cover letter is not in English — translation required" and stop.

Each failure condition names a concrete situation and a concrete response. The AI cannot guess when any of these situations occurs [3].

---

With these three components identified and written, the specification has no gaps in the areas that most directly affect whether the task succeeds or fails.

## In Practice

The six-component approach is used by professional software teams, data science teams, and AI product teams — not just for individual prompts, but for building the instructions that run AI systems continuously [1].

**Common anti-patterns to avoid:**

| Anti-pattern | The problem | The fix |
|---|---|---|
| No inputs stated | AI guesses what to work with | Name every piece of raw material explicitly |
| Output type only, no content | "A list" without specifying what it must contain | Add content and amount alongside type |
| No failure conditions | AI hallucinates or silently skips steps | Add at least one rule per failure category |

**Do:**

- Write inputs, expected outputs, and failure conditions every time — even for small tasks. Skipping a component because the task "seems simple" is how gaps appear.
- Write failure conditions *before* you send the specification. It is easier to think about what could go wrong when you are not yet looking at a bad output.
- Re-read your specification as if you are the AI and know nothing else. Every question you find yourself asking is a gap to fill [1].

**Don't:**

- Do not assume the AI will ask for clarification when inputs are missing. Most AI tools will proceed and guess. Write the failure condition yourself [3].
- Do not leave expected outputs vague — "give me a list" without specifying content or length is still incomplete.

Production AI systems — customer-service assistants, summarisation tools, classification systems — use explicit failure conditions as a reliability mechanism. Without them, a system handling thousands of queries per day will encounter unusual inputs, missing data, or off-topic questions and produce unpredictable outputs [2]. Research into AI agent failures shows that many trace back to missing inputs, no rule for when to stop, and outputs that look correct but violate an unstated constraint [3].

## Key Takeaways

- A complete specification has six components. This topic focuses on the three that most directly determine success: **inputs**, **expected outputs**, and **failure conditions**.
- Inputs tell the AI what raw material to work with. Without them, the AI guesses — often incorrectly.
- Expected outputs make the result observable. Specify the type, content, and amount of what you expect to receive.
- Failure conditions are the most commonly skipped component and the one most directly responsible for AI unreliability. An AI without failure conditions will guess when inputs are missing, ambiguous, or out of scope.
- Writing all three components together closes the most common gaps that cause AI tasks to produce wrong or unpredictable outputs [1][2][3].

## References

1. Mohit Wani, "Specification-Driven Development." <https://medium.com/@wanimohit1/specification-driven-development-how-ai-is-transforming-software-engineering-c01510ea03e3>
2. LaunchDarkly, "Prompt Engineering Best Practices." <https://launchdarkly.com/blog/prompt-engineering-best-practices/>
3. Galileo AI, "AI Agent Failure Modes Guide." <https://galileo.ai/blog/agent-failure-modes-guide>

---
<!-- nav:bottom:start -->
[⬅ Previous: 2.2 — Bad spec vs good spec](../../2-2-bad-spec-vs-good-spec-make-it-better-vs-rewrite-at-grade-8-l/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.4 — Pattern recognition ➡](../../../2-how-machines-recognise-patterns/2-4-pattern-recognition-how-machines-find-rules-in-repeated-data/artifacts/reading.md)
<!-- nav:bottom:end -->
