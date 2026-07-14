---
topic_id: "2.9"
title: "Iterating a specification based on output gaps"
position_in_module: 3
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Iterating a specification based on output gaps — Topic Corpus

## 2. Prerequisites

- **2.1** — Testable specification, bounded specification, observable output, observable failure, specification quality.
- **2.3** — Input identification, expected output, failure condition, specification template.
- **2.8** — Testing a specification, three-question verification check, full pass, partial pass, full fail, pass/fail table, format drift, constraint overflow, task drift.

## 3. Learning Objectives

- Define what "iterating a specification" means: making one targeted change to the specific part that caused a test failure.
- Name the three gap types (format drift, constraint overflow, task drift) and match each to its correct fix.
- Apply the four-step iteration cycle (test → name the gap → patch the failing part → retest) to a given spec and test result.
- Explain the "minimum viable patch" principle: change only the part of the spec that caused the failure.
- Decide when to stop iterating: full pass achieved, or diminishing returns accepted with a documented limitation.

## 4. Introduction

You have written a specification. You tested it using the three-question check from topic 2.8. The result came back as a partial pass or a full fail. Now what?

Many people make the same mistake here: they throw the whole spec away and start again. That wastes time and usually produces the same gap in a different place. The smarter move is to look at exactly *what* went wrong and fix only that part [1].

This process is called **iteration** — making a focused, targeted change based on a specific gap you found, then testing again to see whether the change worked. It sounds simple, but doing it well requires a clear method. Without a method, you end up changing too many things at once, and you lose track of what actually fixed the problem [2].

Think of it like adjusting a recipe. If your soup is too salty, you do not tear up the entire recipe. You find the one step that added too much salt and change only that step. The same logic applies to specifications.

This topic gives you that method. By the end, you will have a repeatable loop you can use on any specification that does not pass its first test. Your Specification Portfolio (Assessment A1, due Week 3) asks you to show evidence of iterating on your specs — the skills here apply directly to that work.

## 5. Core Concepts

### 5.1 What "iterating" means

**Iteration** — making one focused change to a specific part of a specification, based on a specific gap identified in a test result, then retesting [1].

The word "iterating" comes from the Latin for "again." You go through the test-and-fix cycle again — but not from scratch. You go through it with new information: the gap you just found.

Two things make an iteration valid:

1. **It is targeted.** You change the part of the spec that caused the failure. You do not touch the parts that passed.
2. **It is grounded.** The change is driven by the gap you observed in the output, not by a guess [2].

An iteration that changes three things at once is not a valid iteration. If the second test passes, you cannot tell which of the three changes fixed it. If it fails, you have made the problem harder to trace. Change one thing. Retest. Repeat.

### 5.2 The three gap types and their fixes

In topic 2.8, you learned that a failing test result usually falls into one of three patterns. Each pattern has a name and a specific fix [1][2][3].

| Gap type | What it means | Which spec part caused it | The fix |
|---|---|---|---|
| **Format drift** | The output had the right content but the wrong shape, structure, or length | The spec's format instruction (or lack of one) | Add or tighten the format instruction |
| **Constraint overflow** | The output included content the spec did not explicitly forbid | A constraint was missing or too loose | Add a new constraint, or make an existing one more specific |
| **Task drift** | The output solved a different task than the one you intended | The task statement itself was too vague or ambiguous | Rewrite the task statement to be more precise |

Each fix is applied to a different part of the spec. This is why naming the gap type first matters — it points you straight to which part needs changing.

**Format drift — format fix.** The AI gave you the right information but presented it in the wrong way. For example: you asked for a list and got a paragraph. The fix is not to re-explain the task — it is to add a format instruction: "Present the output as a numbered list with exactly three items." [2]

**Constraint overflow — constraint fix.** The AI included something you did not want. For example: you asked for a three-sentence summary and got five sentences with extra commentary. The fix is to add or tighten a constraint: "Do not include commentary or explanation. Stop after three sentences." [1][3]

**Task drift — task statement fix.** The AI solved a different problem than you meant. For example: you asked it to "describe the process" and it described a different process because "the process" was ambiguous. The fix is to rewrite the task statement to remove the ambiguity: "Describe only the four-step order-fulfilment process defined above." [1][2]

### 5.3 The minimum viable patch principle

**Minimum viable patch** — the smallest change to the spec that directly addresses the gap you found, without touching any part that is already working [1][2].

This principle has three rules:

1. **Change one part only.** If the gap is in the format instruction, change the format instruction. Do not also rewrite the task statement "just in case."
2. **Make the change as small as possible.** If adding four words to a constraint fixes the problem, do not rewrite the whole constraint.
3. **Leave passing parts untouched.** If two out of three test questions passed, the parts of the spec behind those passes are doing their job. Do not disturb them.

Why does this matter? Because a spec is a connected set of parts. Changing one part can affect another. If you rewrite more than you need to, you risk breaking something that was already working [2][3].

A common mistake is to react to a bad test result by rewriting the entire spec. This feels productive, but it almost always makes things harder: you cannot tell which change helped, you may introduce new gaps, and you lose the parts that were already working.

### 5.4 The iteration cycle

The iteration cycle is a four-step loop [1][2][3]:

1. **Test.** Run your current spec through the three-question verification check (from topic 2.8). Record the result: full pass, partial pass, or full fail. If full pass, stop — you are done.
2. **Name the gap.** Look at what the test result shows. Decide which gap type it is: format drift, constraint overflow, or task drift. Write the gap type down before you change anything.
3. **Patch the right part.** Apply the minimum viable patch to the spec part that caused the gap. Do not change anything else.
4. **Retest.** Run the three-question check again on the updated spec. If full pass, stop. If not, return to step 2 with the new test result.

This loop can run multiple times. Each time through, the spec improves by one patch. After two or three cycles, most specs reach a full pass.

### 5.5 When to stop iterating

You stop when one of two conditions is met [1][2]:

**Condition 1 — Full pass.** The spec passes all three questions of the verification check with no partial results. This is the target. Stop here and document the final spec.

**Condition 2 — Diminishing returns.** You have run two or three iteration cycles and the spec is not reaching a full pass. Each cycle is producing smaller improvements, or the remaining gap is in something you cannot control within a specification (for example, a very specific domain detail the AI consistently misses). In this case:

- Document the remaining limitation clearly. Write one sentence stating what the spec does not fully control and why.
- Accept the spec as-is with a known limitation.
- Do not keep iterating in hope of a perfect result that may not be achievable [3].

A spec with a documented known limitation is better than a spec that is never finished because it never reached 100% [2].

Two to three cycles is a practical guideline, not a hard rule. The signal to stop is not the cycle count — it is whether each new cycle is producing meaningful improvement. If the remaining gap is a small format detail that does not affect the core task, accept it. If the remaining gap means the spec still does the wrong job, keep iterating or reconsider the task statement.

## 6. Implementation

The iteration cycle applied step by step.

**Step 1: Test the current spec.**
Run the spec through the three-question verification check. Write down each question, the result (pass / partial pass / fail), and what the actual output showed. This evidence is what you will diagnose from.

**Step 2: Name the gap — before touching the spec.**
Look at the failing or partially-passing question. Ask:

- Did the output have the right content but wrong shape? → **Format drift.**
- Did the output include content you did not ask for or explicitly forbid? → **Constraint overflow.**
- Did the output do something different from the task you intended? → **Task drift.**

Write the gap type as a single phrase. Do not start editing yet.

**Step 3: Identify which spec part caused it.**
Match the gap type to the spec part:

- Format drift → look at (or add) a format instruction.
- Constraint overflow → look at your constraint list.
- Task drift → look at your task statement.

**Step 4: Write the minimum viable patch.**
Make the smallest change that addresses the named gap. Write the patched version of that one spec part. Leave everything else exactly as it was.

**Step 5: Retest.**
Run the updated spec through the three-question check again. Record the new result. If full pass, document the final spec. If not, return to Step 2 with the new result.

### Worked example — three iteration cycles

**Task:** Ask an AI to produce study tips for an exam.

---

**Version 1 — first draft:**

> "Give me tips for studying for an exam."

**Test result:**

| Question | Result | What the output showed |
|---|---|---|
| Q1 — Did the output match what was expected? | Partial pass | Tips are about studying but there are seven of them, not three |
| Q2 — Did the AI respect all constraints? | Fail | One tip mentioned "pulling an all-nighter" — no constraint was set |
| Q3 — Is the output in the right format? | Fail | Output is a paragraph; no format was specified |

**Named gap:** Task drift (no count specified), constraint overflow (all-nighter included), format drift (no list format). The root cause is the task statement — it specified almost nothing. Fix the task statement first.

**Minimum viable patch — cycle 1:** Rewrite the task statement to add count, audience, format, and the exclusion constraint.

---

**Version 2 — after cycle 1 patch:**

> "Give me exactly 3 tips for studying for an exam, written for a teenager, as a numbered list. Do not include any tips about staying up late or pulling an all-nighter."

**Test result:**

| Question | Result | What the output showed |
|---|---|---|
| Q1 — Did the output match what was expected? | Pass | Three tips, appropriate for a teenager |
| Q2 — Did the AI respect all constraints? | Pass | No all-nighter tip |
| Q3 — Is the output in the right format? | Partial pass | Numbered list — but each item is 3–4 sentences, not a short tip |

**Named gap:** Format drift — items are too long. Fix: tighten the format instruction.

**Minimum viable patch — cycle 2:** Add "Each tip must be one sentence only."

---

**Version 3 — after cycle 2 patch:**

> "Give me exactly 3 tips for studying for an exam, written for a teenager, as a numbered list. Each tip must be one sentence only. Do not include any tips about staying up late or pulling an all-nighter."

**Test result:**

| Question | Result | What the output showed |
|---|---|---|
| Q1 — Did the output match what was expected? | Pass | Three tips, correct audience |
| Q2 — Did the AI respect all constraints? | Pass | No forbidden content |
| Q3 — Is the output in the right format? | Pass | Numbered list, one sentence per item |

**Result: Full pass. Iteration complete.**

**Iteration log:**

- Cycle 1: task drift + constraint overflow + format drift → rewrote task statement (root cause).
- Cycle 2: format drift (items too long) → added "Each tip must be one sentence only."
- Cycle 3: full pass. Final spec is version 3.

Notice what never changed: once the task statement was fixed in cycle 1, it was not touched again. Only the format instruction was updated in cycle 2, because that was the only remaining gap [1][2][3].

## 7. Real-World Patterns

This same cycle — test, find gap, patch, retest — is exactly how professionals refine AI instructions in real work. IBM's guide on iterative prompting describes it as an "assess → identify gap → modify" loop [1]. The vocabulary differs (they say "prompt" where we say "specification") but the structure is identical.

What separates an experienced AI user from a beginner is not that the experienced person writes perfect specifications on the first try. It is that they diagnose gaps faster and make more precise patches [2].

One structured approach to iteration is the REFINE framework, described in educational contexts. After each output, you Review the result, Evaluate where it diverged from your intent, Focus on the specific part that caused the divergence, Iterate by patching that part, and Note the change before evaluating again [3]. The underlying logic is the same as the four-step cycle in Section 5.4.

For your Specification Portfolio (A1), showing iteration history — version 1, the named gap, the patch, version 2, the new result — is direct evidence of the skill this topic teaches. The portfolio does not just ask for a final spec; it asks for evidence that you improved specs through deliberate iteration [3].

## 8. Best Practices

**Do this:**

| Action | Why it matters |
|---|---|
| Name the gap type before touching the spec | Diagnosis first; fixing without diagnosis produces guesses |
| Change one part per cycle | You cannot learn which fix worked if you change three things at once |
| Write down the old version and the new version side by side | Creates a change log; shows iteration in your portfolio |
| Record every test result in the pass/fail table from 2.8 | Turns iteration into visible evidence |
| Stop at full pass | Iterating beyond a pass introduces new risk |

**Avoid this:**

| Mistake | What goes wrong |
|---|---|
| Rewriting the whole spec because one part failed | You break parts that were working; you cannot trace what changed |
| Fixing a format-drift gap by changing the task statement | Wrong part; the gap will likely remain |
| Accepting a known limitation on a task-drift failure | The spec still does the wrong job — that is not a small limitation |
| Running more than three cycles without re-reading the full spec | After three failures, the root cause may be in the task statement even if earlier gaps looked like format issues |

## 9. Hands-On Exercise

Take a specification you wrote in a previous topic (or write this one fresh: "Write a 3-sentence summary of a news article about technology, aimed at a 10-year-old, using no technical words").

1. Test it. Record the result for each question: pass, partial pass, or fail.
2. If the result is not a full pass: name the gap type, identify the exact line causing it, and write a minimum viable patch to that part only.
3. Retest. Record the new result.
4. Repeat for up to three rounds.
5. After three rounds (or when you hit full pass): write one-line notes between each version ("Gap: [type]. Patch: [what I changed].").

This is exactly the format A1 asks you to show for each spec in your portfolio.

## 10. Key Takeaways

- Iterating a spec means making one targeted change to the specific part that caused a test failure — not rewriting the whole spec from scratch.
- There are three gap types: format drift (wrong shape), constraint overflow (unwanted content), and task drift (wrong task). Each gap type maps to a different spec part to fix.
- The iteration cycle has four steps: test → name the gap → patch the right part → retest. Each cycle produces one improvement.
- The minimum viable patch principle says: change only what caused the failure; leave everything that passed untouched.
- Stop when you reach a full pass, or when further cycles produce no meaningful improvement — then document the remaining limitation and move on.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
