---
topic_id: "2.5"
title: "The 70/30 rule — AI implements, you specify and verify"
position_in_module: 1
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. The 70/30 Rule — AI Implements, You Specify and Verify — Topic Corpus

## 2. Prerequisites

This topic builds on work done in Week 1 and earlier in Week 2:

- **1.1 What is computation** — deterministic systems follow instructions exactly as given; they do not interpret your intent.
- **1.3 Probabilistic systems** — AI produces confident-sounding answers that are not guaranteed to be correct.
- **2.1 What makes a good specification** — the four properties (testable, bounded, observable, actionable) that make an instruction precise enough to act on.
- **2.3 How to identify inputs, expected outputs, and failure conditions** — the six-component checklist for a complete specification.

No programming knowledge is needed. The 70/30 rule is a professional practice concept — it is about how humans and AI divide responsibility, not about how to write code.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Explain what the 70/30 rule is and what it says about how humans and AI should divide work.
- Describe the two human roles in the rule: specifying a task and verifying the result.
- Identify which parts of a task should stay with the human and which parts can be handed to AI.
- Apply the rule by writing a specification, sending it to an AI, and then checking whether the output meets the specification.
- Explain why verification is a required step — not an optional one — even when the AI output looks correct at first glance.

## 4. Introduction

You have been practicing how to write good specifications. Now here is the key question: once you have a specification, what do you do with it?

The 70/30 rule gives a direct answer. It says that in any AI-assisted task, roughly 70 percent of the effort is implementation — the actual doing, generating, drafting, or computing. AI is extremely good at that part. The remaining 30 percent is specification and verification — deciding exactly what you want and then checking that you got it. That part belongs to you [1].

This might feel backwards. You might expect AI to take most of the work away and leave you with only a tiny fraction. In one sense it does — AI can produce a draft report, a code outline, or a data summary in seconds. But speed is not the same as correctness. The AI does not know your context, your audience, or your standards. Only you do. Your 30 percent is not the small part — it is the part that makes the whole thing trustworthy [2].

Think of a professional chef hiring a kitchen assistant. The assistant can chop, stir, and plate at high speed. But the chef still decides the recipe, sets the quality standard, and tastes every dish before it leaves the kitchen. Removing the chef's judgment would not make the kitchen faster — it would make the food unreliable. The 70/30 rule describes the same division for AI work [3].

## 5. Core Concepts

### 5.1 What the 70/30 Rule Says

The **70/30 rule** is a professional guideline for working with AI tools [1]. It divides any AI-assisted task into two parts:

- **The 70 percent — implementation.** This is the part where work is actually produced: text is drafted, calculations are run, information is retrieved. AI handles this part. It is fast, tireless, and consistent at generating output at scale.
- **The 30 percent — specification and verification.** This is the part where a human decides what the task is, sets the standard, sends the instruction, and then checks the result. You handle this part.

The name "70/30" is a way to remember the proportion, not an exact measurement. Some tasks might be 80/20; others might be 60/40. The point is not the exact number — it is the underlying principle: **AI does the bulk of the producing; the human does all of the deciding and checking** [2].

This rule applies whether you are using AI to draft an email, summarise a document, generate a quiz question, or suggest a plan. In every case, the structure is the same: you specify, AI implements, you verify.

---

### 5.2 Your Role 1 — Specify

**Specification** is the first human role in the rule. You already know from Topics 2.1, 2.2, and 2.3 what a good specification contains. In the context of the 70/30 rule, the key insight is this: **the quality of the AI's output is almost entirely determined by the quality of your specification** [1].

If your specification is vague, the AI will produce something — but it may not be what you needed. If your specification is precise, testable, bounded, observable, and actionable, the AI has a clear target to aim at. A strong specification is not a courtesy to the AI — it is protection for yourself [2].

What does "specifying" mean in practice?

1. **Decide what task you actually need done.** Not "have AI help with the report" — but "summarise the key financial findings from pages 4–9 in five bullet points, each under 30 words, for a non-specialist reader."
2. **Set the constraints.** What format? What length? What audience? What should be excluded?
3. **Define the success condition.** What does a correct output look like? (This is testability from Topic 2.1.)
4. **Write it down.** A specification in your head is not a specification — it cannot be checked, shared, or improved.

When you complete this four-step process before sending anything to an AI, you have done the first half of your 30 percent [3].

---

### 5.3 Your Role 2 — Verify

**Verification** is the second human role in the rule. Verification means checking whether the AI's output actually meets the specification you wrote [1].

This step is not optional. Here is why: AI systems are probabilistic (you learned this in Topic 1.3). They produce outputs that are statistically likely to match the pattern they were trained on — not outputs that are guaranteed to meet your specific requirements. An output can look polished, professional, and confident while still being wrong for your purpose [2].

**Verification is not the same as reading the output.** Reading is passive — your eye moves over the text. Verification is active — you check each part of the output against each part of your specification.

Here is what verification looks like in practice:

1. **Check against your success condition.** Did the output meet the testable criterion you set? Count the bullet points. Check the word count. Confirm the format.
2. **Check the scope.** Is everything that should be included, included? Is everything that should be excluded, absent?
3. **Check for factual accuracy.** AI can state incorrect facts with total confidence. If your task involves facts — names, dates, figures, references — check them against a reliable source.
4. **Check for failure conditions.** In Topic 2.3 you learned to define failure conditions in advance. Now is when you look for them.
5. **Decide: accept, revise the output, or revise the specification.** Sometimes the output is wrong because the AI made an error. Sometimes it is wrong because the specification had a gap. If you revise and resubmit, you are doing specification work again — still your 30 percent [3].

---

### 5.4 Why the Split Matters

You might ask: why does it matter who does which part? The answer comes down to what AI is good at and what it is not good at.

AI is good at:

- Producing large amounts of text quickly.
- Following an explicit format.
- Retrieving and recombining information from patterns it was trained on.
- Being consistent across many repetitions of the same task.

AI is not good at:

- Knowing what you actually need (because it cannot read your mind).
- Knowing your audience, your standards, or your context (because those are not in the training data).
- Guaranteeing factual accuracy (because it generates statistically likely text, not verified facts).
- Knowing when it has made an error (it has no self-awareness of mistakes in the way a human does).

The 70/30 rule puts each capability where it belongs. AI handles the volume of production that it is fast and consistent at. You handle the judgment, context, and accountability that only you can provide [1][2].

**A table of the split:**

| Responsibility | Who does it | Why |
|---|---|---|
| Decide what the task is | Human | AI does not know your context or goals |
| Write the specification | Human | AI cannot set its own quality bar |
| Produce the output | AI | Fast, consistent, tireless at generation |
| Check the output against the spec | Human | AI cannot reliably audit its own output |
| Accept, reject, or revise | Human | Accountability rests with the person, not the tool |

---

### 5.5 The Verification Loop

In practice, the 70/30 rule is not a straight line — it is a loop [3].

1. You write a specification.
2. AI produces an output.
3. You verify the output.
4. If the output does not meet the specification, you do one of two things:
   - **Revise the output** — ask the AI to correct a specific part.
   - **Revise the specification** — the gap was in your original instruction, so you rewrite that part and resubmit.
5. You verify again.
6. When the output meets the specification, the loop ends.

Each pass through the loop is still your 30 percent doing its job. The loop typically takes one to three iterations for a well-written specification. It takes many more for a vague one — which is exactly why investing time in specification up front saves time overall [1].

## 6. Implementation

Use this process every time you work with an AI tool on a real task.

**Step 1 — Define the task.**
In one sentence, state what you need the AI to produce. Example: "I need a summary of this week's customer feedback."

**Step 2 — Write the full specification.**
Apply the four-property checklist from Topic 2.1:
- **Testable:** "Each piece of feedback must be categorised as positive, neutral, or negative."
- **Bounded:** "Cover only feedback received Monday through Friday this week. Do not include feedback from previous weeks."
- **Observable:** "Produce a table with three columns: date, feedback quote (under 20 words), category."
- **Actionable:** Paste the actual feedback text into the prompt, or specify clearly where the AI should find it.

**Step 3 — Send the specification to the AI and receive the output.**
This is the AI's 70 percent. Do not edit the output yet — receive it first.

**Step 4 — Verify the output against your specification.**
Check every criterion. Use the failure conditions you defined in Topic 2.3 as your failure checklist.

**Step 5 — Accept, revise-output, or revise-specification.**
- If the output meets the specification: you are done.
- If the output has a specific error: ask the AI to correct that error (revise output).
- If you realise your specification had a gap: fix the specification and resubmit (revise specification).

Repeat steps 3–5 until the output meets the specification [2][3].

## 7. Real-World Patterns

The 70/30 principle appears in many professional settings beyond AI tools.

**Software testing.** Developers use automated tools to run thousands of test cases (the 70 percent — implementation). But a human engineer still writes the test cases, defines what "pass" and "fail" mean, and decides whether the results are acceptable [1].

**Data journalism.** A journalist uses a tool to process a large dataset and generate charts. The tool does the number-crunching. The journalist specifies which data to include, verifies that the charts are accurate, and decides whether the findings tell the story they were expecting [2].

**Healthcare support tools.** An AI diagnostic assistant flags potential conditions based on patient data. A qualified clinician specifies the parameters, reviews the flags, and makes the final medical judgment. The AI handles scale; the clinician handles accountability [3].

In each case, the pattern is identical: a human sets the standard, a system does the production, and the human checks the result. The technology changes; the division of responsibility does not.

## 8. Best Practices

**Do:**
- Write your specification before you open the AI tool — not while you are typing in the prompt box.
- Treat every piece of AI output as a draft that requires verification, not as a finished product.
- When the AI output is wrong, ask first: "Is this a specification gap or an AI error?" The answer determines your next step.
- Keep a record of your specification alongside your final output — you may need to defend your process later, especially for assessed work [1].

**Do not:**
- Skip verification because the output "looks right." Looking right is not the same as being right.
- Use the AI's output before running it through your success condition check.
- Assume that a second AI run on the same prompt will catch the errors from the first run — it may produce different errors instead.
- Outsource the specification itself to AI. "Tell me what to ask you" transfers your 30 percent to the AI, which cannot perform it reliably [2][3].

**Do/Don't summary:**

| Do | Do not |
|---|---|
| Write the spec before prompting | Wing it and fix later |
| Verify output against each criterion | Skim for plausibility |
| Revise the spec when you find a gap | Blame the AI and give up |
| Own the final output as yours | Treat AI output as automatically authoritative |

## 9. Hands-On Exercise

Choose one task from your upcoming assessment — for example, specifying how a transport app should handle a delayed bus. Write the full specification using the six-component checklist from Topic 2.3. Then send it to an AI tool and receive the output. Work through the five-step verification process in Section 6. For each criterion in your specification, mark it as pass or fail. If any criterion fails, decide whether to revise the output or revise the specification, and do one iteration. Write a two-sentence note on what changed between your first output and your verified final output. This is the skill your Specification Portfolio (assessment A1) will test.

## 10. Key Takeaways

- The **70/30 rule** says that AI handles roughly 70 percent of an AI-assisted task (implementation — generating output), while the human handles roughly 30 percent (specification and verification — deciding what is needed and checking the result).
- Your two roles are **specifying** (writing a clear, bounded, testable instruction before you prompt the AI) and **verifying** (checking the output against that specification after you receive it).
- Verification is not optional. AI output looks confident even when it is wrong. Only a human checking against a specification can catch the gap.
- The 70/30 split is not about reducing your effort — it is about placing human judgment and accountability exactly where AI cannot substitute for them.
- The process is a **loop**: specify → implement (AI) → verify → revise specification or output → verify again. A strong specification shortens the loop; a vague one lengthens it.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
