<!-- nav:top:start -->
[⬅ Previous: 2.7 — Writing specifications across five domains](../../2-7-writing-specifications-across-five-domains-health-transport/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.9 — Iterating a specification based on output gaps ➡](../../2-9-iterating-a-specification-based-on-output-gaps/artifacts/reading.md)
<!-- nav:top:end -->

---

# Testing a specification — how to verify the AI did exactly what you asked

## Overview

You have learned how to write a clear, detailed specification — one that is testable, bounded, and observable. You know how to name the inputs, expected outputs, and failure conditions of a task. The next question is a practical one: after you send the specification and the AI gives you a result, how do you actually check whether it did what you asked? This topic gives you a three-question check, a pass/fail table, and a simple classification that turns a vague "looks about right" into a precise, recorded finding [1].

## Key Concepts

### What "testing a specification" means

**Testing a specification** means comparing the AI's actual output to what you wrote in your specification, part by part, and recording whether each part was met.

It is not an opinion. You are not asking "do I like this?" You are asking a precise question: "Does this output match what I specified?"

Two things are being compared:

- **The specification** — what you wrote: the task statement, constraints, and expected output format.
- **The actual output** — what the AI produced in response.

This step is called a **verification**. You are *verifying* — confirming — that the output matches the instruction. Verification sits between writing the specification and deciding what to do next [2].

**Why it matters.** A powerful AI will nearly always produce output that *looks* reasonable. "Looks reasonable" can hide real gaps. Without a check, you might miss an AI that:

- Followed most of your constraints but quietly ignored one.
- Used the right format but drifted off-topic partway through.
- Produced the right number of items but included content you explicitly excluded.

With a verification step, you catch these gaps immediately — before you act on a flawed output [1][3].

---

### The three-question verification check

Every time you receive an AI output, run three questions against it in order. Each question checks a different part of your specification [1][2][3].

**Question 1 — Did I get the format I asked for?**

Look at the *structure* of the output. Does it match what you specified?

- If you asked for a numbered list, is it a numbered list?
- If you asked for three bullet points, are there exactly three?
- If you asked for a table with two columns, does it have two columns?
- If you asked for a response under 80 words, is it under 80 words?

Format requirements are the easiest to check — they are visible at a glance. If the output has a different shape from what you specified, that is called **format drift**.

**Question 2 — Did it stay within the constraints?**

Look at the *content* of the output. Does it respect the limits you set?

- If you specified a topic boundary ("cover only X, not Y"), did the AI stay within that boundary?
- If you included an exclusion ("do not include Z"), does Z appear in the output?
- If you set a domain or audience constraint, does the content match?

If the output includes content outside your specified scope, that is called **constraint overflow**.

**Question 3 — Does the output match the task statement?**

Step back from the details and look at the big picture. Did the AI do the *task* you asked for?

- If you asked for a summary, does the output summarise?
- If you asked for a set of instructions, does the output instruct?
- If you asked for a recommendation for a specific domain, is the recommendation actually for that domain?

This question catches the case where the output looks correct in format and follows some constraints, but the core task has shifted. That shift is called **task drift** — the hardest failure to catch, because a drifted output can look polished while still being the wrong thing [3].

**All three questions together:**

| Question | What part of the spec it checks | The failure it catches |
|---|---|---|
| Q1 — Format | Format and output structure | Format drift |
| Q2 — Constraints | Constraints and exclusions | Constraint overflow |
| Q3 — Task statement | Core task description | Task drift |

A complete verification always runs all three — not just the easiest one [1].

---

### Pass, partial pass, and full fail

After running the three questions, classify the result [1][2]:

**Full pass** — All three questions answered "yes." Format is correct, every constraint is respected, and the output matches the task statement. You can act on the output as-is.

**Partial pass** — One or two questions answered "yes" and one or two answered "no." A partial pass is *not* a pass — it means the specification was not fully met. It is still useful: you know exactly which parts were and were not met.

**Full fail** — All three questions answered "no," or the output is so far from the specification that it cannot be categorised part by part.

An important point: acting on a partial pass as if it were a full pass means working with a known problem. Recording a partial pass gives you a specific, fixable finding [3].

---

### Recording the result — the pass/fail table

A test result is only useful if you write it down. Noticing a problem is not the same as documenting it. A recorded test tells you exactly what passed, what failed, and where to focus [1].

**The pass/fail table** is a simple grid. Each row is one component of your specification. The columns are: the component name, what you specified, what the output contained, and the result (Pass / Fail).

Template:

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | [your task] | [what the output actually did] | Pass / Fail |
| Format | [your format requirement] | [the format of the output] | Pass / Fail |
| Constraint 1 | [your constraint] | [whether it was respected] | Pass / Fail |
| Constraint 2 | [your constraint] | [whether it was respected] | Pass / Fail |

You only fill in the rows that your specification included. If your specification had two constraints, you have two constraint rows [3].

**How to read the table:** All Pass entries → full pass. Any Fail entries → partial pass. All Fail entries → full fail. The table turns a vague impression into a row-by-row account [1].

---

### The three common failure patterns

When a result is a partial pass or full fail, one of three patterns is usually responsible [2][3]:

**Format drift** — The AI produced content that is correct in substance but in the wrong shape.

- You asked for a numbered list; the AI produced paragraphs.
- You asked for three bullet points; the AI produced five.
- You asked for a response under 100 words; the AI produced 180.

Format drift is caught by Q1. It is the most common pattern — the AI optimises for clarity in its own terms, not for your explicit format instruction.

**Constraint overflow** — The AI crossed a boundary you drew in your specification. The format may be correct and the task may be right, but content appears that you explicitly excluded.

- You specified "cover only the health benefits"; the AI included cost and side effects too.
- You specified a domain (scheduling); the AI drifted into general productivity advice.

Constraint overflow is caught by Q2. It often happens when a constraint conflicts with what the AI naturally produces for a topic.

**Task drift** — The output drifted away from the core task you described, even though it looks well-formed.

- You asked for a set of evaluation questions; the AI produced a general overview instead.
- You asked for a failure-condition analysis; the AI rewrote the spec instead.

Task drift is caught by Q3. The output can look thorough and polished while completely missing the stated task [3].

| Failure pattern | Which question catches it | What it looks like |
|---|---|---|
| Format drift | Q1 — Format | Right content, wrong shape |
| Constraint overflow | Q2 — Constraints | Right task, content crossed a boundary |
| Task drift | Q3 — Task statement | Well-formed output, wrong task |

## Worked Example

Two complete specification tests are shown below — one in the health domain and one in scheduling.

---

### Example 1 — Health domain

**Specification:**

> **Task statement:** Generate a five-item daily hydration checklist for an adult who works at a desk.
>
> **Inputs:** No external document needed. Use general health guidance only.
>
> **Constraints:** Each item must be one sentence starting with a verb. Do not include advice about food, supplements, or medication. Maximum five items — no more, no fewer.
>
> **Expected output format:** A numbered list of exactly five sentences.

**AI output received:**

> 1. Drink a glass of water first thing in the morning before checking your phone.
> 2. Keep a refillable water bottle on your desk and aim to refill it twice before lunch.
> 3. Set a reminder on your phone every two hours to take a short hydration break.
> 4. Eating water-rich foods like cucumber and watermelon can help you stay hydrated throughout the day.
> 5. Reduce your intake of caffeinated drinks, which can contribute to dehydration over long periods.

**Applying the three-question check:**

- **Q1 — Format:** Numbered list of five sentences. ✓ Format matches.
- **Q2 — Constraints:** Item 4 starts with "Eating" — it is about food, which the constraint excluded. Item 5 advises reducing caffeine — another food/drink boundary issue.
- **Q3 — Task statement:** The list is about daily hydration for a desk worker. ✓ Core task matches.

**Classification: Partial pass.** Q1 and Q3 pass. Q2 fails.

**Pass/fail table:**

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | Five-item hydration checklist for desk worker | Five-item hydration checklist for desk worker | Pass |
| Format | Numbered list, exactly five sentences | Numbered list, exactly five sentences | Pass |
| Constraint: verb-first sentences | Each sentence starts with a verb | Items 1–3 start with a verb; item 4 starts with "Eating" (not a command) | Fail |
| Constraint: no food or supplement advice | No food advice | Item 4 is about food; item 5 is about caffeine intake | Fail |
| Constraint: max five items | Exactly five | Exactly five | Pass |

**Result: Partial pass — two constraint failures (items 4 and 5 include food-related content; item 4 does not use a direct-action verb).**

---

### Example 2 — Scheduling domain

**Specification:**

> **Task statement:** Write a Monday morning briefing agenda for a team of four, covering a one-hour meeting.
>
> **Inputs:** The team is working on a software project. The meeting is the first of the week.
>
> **Constraints:** Exactly four sections, each with a name and a time allocation. Total time must add up to exactly 60 minutes. No social or warm-up activities.
>
> **Expected output format:** A numbered list of four items: [Section name] — [time in minutes]. Nothing else.

**AI output received:**

> **Monday Morning Team Briefing**
>
> 1. Team check-in and weekend highlights — 10 minutes
> 2. Sprint progress review — 20 minutes
> 3. Blockers and escalations — 15 minutes
> 4. Goals for the week — 15 minutes
>
> *Note: Starting with a brief check-in helps set a positive tone for the week.*

**Applying the three-question check:**

- **Q1 — Format:** The spec said "a numbered list of four items. Nothing else." The output added a title heading and a footnote. Format drift present.
- **Q2 — Constraints:** Item 1 is "Team check-in and weekend highlights" — a social warm-up. The footnote confirms the AI included it deliberately. Time total: 10+20+15+15 = 60. ✓ Time constraint passes, but warm-up constraint fails.
- **Q3 — Task statement:** A Monday briefing agenda, four people, one hour. ✓ Core task matches.

**Classification: Partial pass.** Q3 passes. Q1 and Q2 fail.

**Pass/fail table:**

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | Monday briefing agenda, four people, one hour | Monday briefing agenda, four people, one hour | Pass |
| Format | Numbered list of four items, nothing else | Numbered list plus a title heading and a footnote | Fail |
| Constraint: exactly four sections | Four sections | Four sections | Pass |
| Constraint: time adds to 60 minutes | Exactly 60 minutes | 10+20+15+15 = 60 | Pass |
| Constraint: no social or warm-up activities | No warm-up | Item 1 is "Team check-in and weekend highlights" | Fail |

**Result: Partial pass — format drift (unexpected heading and footnote) and constraint overflow (item 1 is a social warm-up that was explicitly excluded).**

## In Practice

The six-step process, applied every time you test a specification [1][2][3]:

1. **Re-read your specification before looking at the output.** If you read the output first, you anchor to what the AI said and find it harder to notice what is missing.
2. **Run the three-question check** — Q1 (format), Q2 (constraints), Q3 (task statement) — in order. Note your answer before moving to the next question.
3. **Build the pass/fail table.** One row per specification component. Fill in what you specified, what the output contained, and the result.
4. **Classify.** All Pass → full pass. Any Fail → partial pass. All Fail → full fail.
5. **Name the failure pattern.** Format drift, constraint overflow, or task drift? One test can show more than one pattern — both examples above had two at once.
6. **Record and stop.** Verification tells you *what happened*. What to do next — revise, re-run, or accept with a known gap — is covered in the next topic.

**Common mistakes to avoid:**

| Anti-pattern | The problem | The fix |
|---|---|---|
| "Looks good to me" review | Opinion without comparison to the spec | Run all three questions against each spec component |
| Checking Q1 only | Q2 and Q3 go unchecked | Always run all three in order |
| No recorded table | Finding noticed but not documented | Even a two-row table is a record — write it down |
| Calling a partial pass a pass | "Most of it was right" | Partial pass means the spec was not met — record it accurately |

University library guides for evaluating AI-generated content recommend checking the output against the original question as the *first* step before judging accuracy or depth [1][2]. Teams deploying AI tools in real products use the same three questions — format, constraints, task match — as the basis of structured output validation [3].

## Key Takeaways

- **Testing a specification** means comparing the AI's actual output to what you specified, part by part. It is a comparison against a written record — not an opinion about the output.
- The **three-question verification check** asks: (1) Did I get the format I asked for? (2) Did it stay within the constraints? (3) Does the output match the task statement? All three must be checked every time.
- A test result is classified as **full pass** (all three pass), **partial pass** (one or more fail), or **full fail** (all fail). A partial pass is not a pass — the specification was not fully met.
- The **pass/fail table** maps each specification component to what the output contained, with a Pass or Fail for each row. It turns a vague impression into a specific, actionable finding.
- The three common failure patterns are: **format drift** (right content, wrong shape), **constraint overflow** (content crossed an explicit boundary), and **task drift** (well-formed output, wrong task).

## References

1. CSUN University Library, "Artificial Intelligence: Evaluating AI-Generated Content." <https://libguides.csun.edu/c.php?g=1377855&p=11076059>
2. St. Catherine University Library, "Generative AI: Evaluating AI." <https://libguides.stkate.edu/generativeai/evaluatingAI>
3. VerifyWise, "AI Output Validation." <https://verifywise.ai/lexicon/ai-output-validation>

---
<!-- nav:bottom:start -->
[⬅ Previous: 2.7 — Writing specifications across five domains](../../2-7-writing-specifications-across-five-domains-health-transport/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 2.9 — Iterating a specification based on output gaps ➡](../../2-9-iterating-a-specification-based-on-output-gaps/artifacts/reading.md)
<!-- nav:bottom:end -->
