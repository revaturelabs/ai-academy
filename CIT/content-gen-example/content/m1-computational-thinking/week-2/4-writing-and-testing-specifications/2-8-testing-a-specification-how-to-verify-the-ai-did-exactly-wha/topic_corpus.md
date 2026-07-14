---
topic_id: "2.8"
title: "Testing a specification — how to verify the AI did exactly what you asked"
position_in_module: 2
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Testing a Specification — How to Verify the AI Did Exactly What You Asked — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **2.1 — What makes a good specification — testable, bounded, observable, actionable.** The four-property checklist (testable, bounded, observable, actionable) is the quality bar used throughout this topic. The concept of a **testable specification** — one where you can check the output against a clear standard — is central here.
- **2.3 — How to identify the inputs, expected outputs, and failure conditions of a task.** The six-component specification structure (task description, inputs, expected outputs, format and constraints, failure conditions, success criteria) is what you test against in this topic. Being able to name those components is required.
- **2.7 — Domain-specific specification.** The worked examples in this topic use the four-part spec structure from topic 2.7 (task statement, context, constraints, expected output format). Familiarity with that structure makes the examples easier to follow.

No programming knowledge is needed. All testing in this topic is done by reading and comparing — not by writing code.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Explain what "testing a specification" means — comparing actual AI output to what you specified.
- Apply the three-question verification check to any AI output to decide whether it passes.
- Classify a test result as full pass, partial pass, or full fail, and describe what each looks like.
- Record a test result using a simple pass/fail table mapped to each part of the specification.
- Identify three common failure patterns — format drift, constraint overflow, and task drift — and explain what causes each.
- Work through a complete test on a real specification and its AI output across two domains.

## 4. Introduction

You have now learned how to write clear, detailed specifications for AI tools. You know how to make them testable, bounded, and observable. You know how to identify inputs, expected outputs, and failure conditions. You have practised writing four-part specifications for specific domains.

Here is the question that comes next: after you send the specification and get a result back, how do you actually check whether the AI did what you asked?

This step is called **testing a specification**. It is the moment where you compare what you received against what you specified. Most people skip this step — they glance at the output, decide it "looks about right," and move on. But "looks about right" is not the same as "matches what I asked for." A specification is only useful if you close the loop and verify the result [1].

Think of it like ordering food at a restaurant. You told the server exactly what you wanted: no nuts, medium rare, no sauce. When the plate arrives, you do not just start eating — you check. Is it medium rare? Is there a sauce? You are testing your specification against the output before you accept it [2].

Testing a specification does not require technical skills. It requires one habit: comparing each part of your specification, piece by piece, to the output you received, and recording what matched and what did not. This topic gives you the three questions to ask and the simple table to record your answers [3].

## 5. Core Concepts

### 5.1 What "Testing a Specification" Means

**Testing a specification** means comparing the AI's actual output to what you wrote in your specification, part by part, and recording whether each part was met.

It is not an opinion. You are not asking "do I like this output?" You are asking a more precise question: "Does this output match what I specified?"

The two things you are comparing are:

- **The specification** — what you wrote, including the task statement, constraints, and expected output format.
- **The actual output** — what the AI produced in response.

The comparison is direct: each item in your specification either appears in the output, or it does not. Each constraint in your specification is either respected, or it is not. Each format requirement is either satisfied, or it is not [1].

This is called a **verification** step. You are verifying — confirming — that the output matches the instruction. Verification is distinct from writing the specification and distinct from revising it. It is the step in between: you wrote the spec, sent it, got a result, and now you check the result before doing anything else [2].

**Why this step matters.** A powerful AI will nearly always produce an output that *looks* reasonable. The problem is that "looks reasonable" can hide gaps. An AI might:
- Follow most of your constraints but ignore one.
- Use the right format but drift off-topic partway through.
- Produce the right number of items but include content you explicitly excluded.

Without a verification step, these gaps pass unnoticed. With a verification step, you catch them immediately — and cheaply, before you act on a flawed output [1][3].

---

### 5.2 The Three-Question Verification Check

Every time you receive an AI output, run three questions against it. These questions map directly onto the parts of your specification [1][2][3].

**Question 1: Did I get the format I asked for?**

Look at the structure of the output. Does it match what you specified for format?

- If you asked for a numbered list, is it a numbered list?
- If you asked for three bullet points, are there exactly three?
- If you asked for a table with two columns, does it have two columns?
- If you asked for a paragraph under 80 words, is it under 80 words?

Format requirements are the easiest to check because they are visible at a glance. Count. Look at the structure. If the output has a different shape from what you specified, that is a **format drift** — one of the three common failure patterns described in Section 5.5 [1].

**Question 2: Did it stay within the constraints?**

Look at the content of the output. Does it respect the limits you set?

- If you specified a topic boundary ("cover only X, not Y"), did the AI stay within that boundary?
- If you included an exclusion ("do not include Z"), does Z appear in the output?
- If you set a domain or audience constraint, does the content match?

Constraints are the boundaries you drew around the task. Checking Question 2 means reading the output carefully and comparing it against every constraint in your specification. If the output includes content outside your specified scope, that is a **constraint overflow** — the second failure pattern [2].

**Question 3: Does the output match the task statement?**

Step back from the details and look at the big picture. Did the AI do the task you actually asked it to do?

- If you asked for a summary, does the output summarise?
- If you asked for a set of instructions, does the output instruct?
- If you asked for a recommendation for a specific domain, is the recommendation actually for that domain?

This question catches a failure where the output looks correct in format and follows some constraints, but the core task has shifted. That is called **task drift** — the third failure pattern. It is the hardest to catch because a drifted output can look polished and well-formed while still being the wrong thing [3].

**Running all three questions together.** Each question covers a different part of your specification:

| Question | What part of the spec it checks | The failure it catches |
|---|---|---|
| Q1 — Format | Format and constraints section | Format drift |
| Q2 — Constraints | Constraints and exclusions | Constraint overflow |
| Q3 — Task statement | Task description / task statement | Task drift |

A complete verification runs all three questions — not just the one that is easiest [1].

---

### 5.3 Pass, Partial Pass, and Full Fail

After running the three-question check, classify the result. There are three possible classifications [1][2]:

**Full pass.** All three questions are answered "yes." The format is correct, every constraint is respected, and the output matches the task statement. You can act on the output as-is.

**Partial pass.** One or two questions are answered "yes" and one or two are answered "no." The output is partly correct — it meets some of the specification but not all of it. A partial pass is useful information: you know exactly which parts of the specification were and were not met. You do not act on the output as-is.

**Full fail.** All three questions are answered "no," or the output is so far from the specification that it cannot be categorised part by part. This is uncommon with a well-written specification — full fails usually signal that the specification itself had a significant gap rather than that the AI made a large error.

**An important note about partial passes.** A partial pass is not a "kind of pass." It means the output does not meet the specification. The distinction between a partial pass and a full pass matters because:

- Acting on a partial pass as if it were a full pass means working with output that has a known problem.
- Recording a partial pass gives you a specific, fixable finding — which part of the specification was not met.

What you do with a partial pass result — whether you revise the specification, adjust your approach, or accept the output with a known limitation — is covered in the next topic (2.9). For now, the goal is to classify accurately [3].

---

### 5.4 Recording a Test Result — The Pass/Fail Table

A test result is only useful if you record it. Reading and noticing a problem is not the same as recording it. A recorded test result tells you exactly what passed, what failed, and where to focus your attention [1][2].

**The pass/fail table** is a simple grid. Each row is one component of your specification. The columns are: the component name, what you specified, what the output contained, and the result (Pass / Fail).

Here is the template:

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | [your task] | [what the output actually did] | Pass / Fail |
| Format | [your format requirement] | [the format of the output] | Pass / Fail |
| Constraint 1 | [your constraint] | [whether it was respected] | Pass / Fail |
| Constraint 2 | [your constraint] | [whether it was respected] | Pass / Fail |
| Expected output content | [what you expected] | [what you received] | Pass / Fail |

You do not need to fill in every row for every specification — only the components that your specification included. If your specification had two constraints, you have two constraint rows. If it had no explicit format requirement, you skip that row [3].

**How to read the table.** Count the Pass and Fail entries.

- All Pass → Full pass.
- Mix of Pass and Fail → Partial pass. The Fail entries identify the specific gaps.
- All Fail → Full fail.

The table is the record. Once it exists, you know what you have and what you do not have [1].

---

### 5.5 The Three Common Failure Patterns

When a test result is a partial pass or full fail, one of three patterns is usually responsible. Recognising the pattern helps you understand what went wrong [2][3].

**Failure Pattern 1 — Format Drift**

Format drift happens when the AI produces content that is correct in substance but in the wrong shape. The task was done, but not in the format you asked for.

Examples:
- You asked for a numbered list; the AI produced flowing paragraphs.
- You asked for three bullet points; the AI produced five.
- You asked for a table; the AI produced plain text with line breaks.
- You asked for a response under 100 words; the AI produced 180.

Format drift is caught by Question 1. It is the most common failure pattern because format requirements are easy to include in a specification but easy for an AI to partially ignore when the content pulls in a different direction. The AI is optimising for what it "thinks" makes the content clear — not for your explicit format instruction [1].

**Failure Pattern 2 — Constraint Overflow**

Constraint overflow happens when the AI crosses a boundary you drew in your specification. The format may be correct and the task may be the right one, but content appears in the output that you explicitly excluded.

Examples:
- You specified "cover only the health benefits"; the AI also included cost and side effects.
- You specified "do not give medical advice"; the AI's output ends with a recommendation to "consult your doctor."
- You specified a domain (scheduling); the AI drifted into general productivity advice.

Constraint overflow is caught by Question 2. It often happens when a constraint conflicts with what the AI "naturally" produces for a topic — the AI's trained patterns pull toward including content that your constraint explicitly excluded [2].

**Failure Pattern 3 — Task Drift**

Task drift happens when the output has drifted away from the core task you described, even though it looks well-formed. The AI produced something — but not the something you asked for.

Examples:
- You asked for a set of evaluation questions for a health app; the AI produced a general overview of health apps instead.
- You asked for a five-step daily meal plan; the AI produced a list of general healthy-eating tips.
- You asked for a failure-condition analysis of a scheduling spec; the AI produced a rewritten version of the spec.

Task drift is caught by Question 3. It is the subtlest failure pattern because the output can look thorough and polished while completely missing the stated task. It typically signals either an underspecified task statement or a constraint that inadvertently pulled the AI toward a different task [3].

**Summary of the three patterns:**

| Failure pattern | Which question catches it | What it looks like |
|---|---|---|
| Format drift | Q1 — Format | Right content, wrong shape |
| Constraint overflow | Q2 — Constraints | Right task, content crossed a boundary |
| Task drift | Q3 — Task statement | Well-formed output, wrong task |

---

### 5.6 Worked Example — Health Domain

**Specification (written using the four-part structure from topic 2.7):**

> **Task statement:** Generate a five-item daily hydration checklist for an adult who works at a desk.
>
> **Context:** No external document needed. Use general health guidance only.
>
> **Constraints:** Each item must be one sentence. Each sentence must be an action (starting with a verb). Do not include any advice about food, supplements, or medication. Maximum five items — no more, no fewer.
>
> **Expected output format:** A numbered list of exactly five sentences.

---

**AI output received:**

> 1. Drink a glass of water first thing in the morning before checking your phone.
> 2. Keep a refillable water bottle on your desk and aim to refill it twice before lunch.
> 3. Set a reminder on your phone every two hours to take a short hydration break.
> 4. Eating water-rich foods like cucumber and watermelon can help you stay hydrated throughout the day.
> 5. Reduce your intake of caffeinated drinks, which can contribute to dehydration over long periods.

---

**Applying the three-question verification check:**

- **Q1 — Format:** The output is a numbered list of five sentences. ✓ Format matches.
- **Q2 — Constraints:** Item 4 starts with "Eating" — it is about food, not hydration behaviour. The constraint said "do not include any advice about food." Item 4 violates that constraint. Item 5 is also borderline — it advises reducing caffeine, which relates to food/drink consumption. That is another constraint boundary issue.
- **Q3 — Task statement:** The list is about daily hydration for a desk worker. ✓ Core task matches.

**Classification:** Partial pass. Q1 and Q3 pass. Q2 fails.

---

**Pass/fail table:**

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | Five-item hydration checklist for desk worker | Five-item hydration checklist for desk worker | Pass |
| Format | Numbered list, exactly five sentences | Numbered list, exactly five sentences | Pass |
| Constraint: action verbs only | Each sentence starts with a verb | Items 1–3 start with a verb; item 4 starts with "Eating" (gerund, not a direct command); item 5 starts with "Reduce" (verb — borderline acceptable) | Fail |
| Constraint: no food/supplement advice | No food advice | Item 4 is about food; item 5 is about caffeine intake | Fail |
| Constraint: max five items | Exactly five | Exactly five | Pass |

**Result: Partial pass — two constraint failures (items 4 and 5 include food-related content; item 4 does not use a direct-action verb).**

---

### 5.7 Worked Example — Scheduling Domain

**Specification:**

> **Task statement:** Write a Monday morning briefing agenda for a team of four people, covering a one-hour meeting.
>
> **Context:** The team is working on a software project. The meeting is the first of the week.
>
> **Constraints:** The agenda must have exactly four sections. Each section must have a name and a time allocation. Total time must add up to exactly 60 minutes. Do not include any social or warm-up activities — this is a work meeting.
>
> **Expected output format:** A numbered list of four items in this format: [Section name] — [time in minutes]. Nothing else.

---

**AI output received:**

> **Monday Morning Team Briefing**
>
> 1. Team check-in and weekend highlights — 10 minutes
> 2. Sprint progress review — 20 minutes
> 3. Blockers and escalations — 15 minutes
> 4. Goals for the week — 15 minutes
>
> *Note: Starting with a brief check-in helps set a positive tone for the week.*

---

**Applying the three-question verification check:**

- **Q1 — Format:** The output has a title heading and a footnote that were not part of the specified format. The format required a numbered list of four items in the pattern "[Section name] — [time in minutes]. Nothing else." The heading and note are additions. Format drift present.
- **Q2 — Constraints:** Item 1 is "Team check-in and weekend highlights" — a social/warm-up activity. The constraint explicitly excluded social or warm-up activities. The footnote reinforces that the AI intentionally included this. Constraint overflow on item 1.
- **Q3 — Task statement:** The output is a Monday briefing agenda for a four-person team with a one-hour limit. ✓ Core task matches.

Also check: does the time add up to 60 minutes? 10 + 20 + 15 + 15 = 60. ✓ The time constraint passes.

**Classification:** Partial pass. Q3 passes. Q1 and Q2 fail.

---

**Pass/fail table:**

| Spec component | What I specified | What the output contained | Result |
|---|---|---|---|
| Task statement match | Monday briefing agenda, four people, one hour | Monday briefing agenda, four people, one hour | Pass |
| Format | Numbered list of four items, nothing else | Numbered list plus a title heading and a footnote | Fail |
| Constraint: exactly four sections | Four sections | Four sections | Pass |
| Constraint: time adds to 60 minutes | Exactly 60 minutes | 10+20+15+15 = 60 | Pass |
| Constraint: no social/warm-up | No warm-up activities | Item 1 is "Team check-in and weekend highlights" — social activity | Fail |

**Result: Partial pass — format drift (unexpected heading and footnote added) and constraint overflow (item 1 is a social warm-up that was explicitly excluded).**

---

## 6. Implementation

Follow these steps every time you test a specification against an AI output.

**Step 1 — Re-read your specification before looking at the output.**
Before you read the output, re-read what you specified. This primes your attention. You are about to compare two things — you need both in mind at the same time. If you read the output first, you will anchor to what the AI said and find it harder to notice what is missing [1].

**Step 2 — Run the three-question check.**
Ask Q1 (format), Q2 (constraints), Q3 (task statement), in that order. For each question, note your answer (yes or no) before moving to the next question. Do not skip a question because the output "looks fine" — that is exactly when the subtle failures hide [2].

**Step 3 — Build the pass/fail table.**
Create a row for each component of your specification. Fill in what you specified, what the output contained, and the result. Every component your specification included should have a row. The table is the record — without it, you have an opinion, not a finding [1].

**Step 4 — Classify the result.**
Count the Pass and Fail entries. All Pass → full pass. Any Fail → partial pass. Record the classification on the table.

**Step 5 — Identify the failure pattern (if any).**
If you have one or more Fail entries, name the failure pattern: format drift, constraint overflow, or task drift. One test can have more than one failure pattern — both worked examples in this topic had two failure patterns simultaneously. Naming the pattern helps you understand where to focus [3].

**Step 6 — Record and stop.**
At this stage, your job is to verify — not to fix. Record the test result. What you do next (whether to revise the specification, re-run, or accept the output) is a separate decision covered in topic 2.9. The discipline of stopping at verification before moving to revision is what keeps the two steps clean [2].

## 7. Real-World Patterns

The habit of testing a specification against an output is not unique to AI. It appears in several professional contexts at scale.

**Quality assurance in software.** In software teams, testers write "test cases" before looking at whether a feature works. Each test case specifies what input goes in and what output is expected. The tester then checks the actual output against the expected output — exactly the same logic as the pass/fail table. This practice is standard because checking against a written specification finds more defects than informal review [1].

**Academic output evaluation.** University guides for evaluating AI-generated content recommend checking the output against the original question before judging its quality. CSUN's library guide, for example, suggests asking whether the AI's output actually addresses what was requested, as a first step before evaluating accuracy or depth [1]. St. Catherine University's guide makes the same point: relevance to the original request is the first check, not the last [2].

**AI output validation in production systems.** Teams that deploy AI tools in real products use formal validation steps to check whether the model's output meets the specification that was written for the task. This is not informal review — it is a structured comparison of actual output against expected output, recorded for each run. The same three questions used in this topic (format, constraints, task match) are the basis of those validation checks [3].

## 8. Best Practices

**Do:**
- Re-read your specification before reading the output. Anchoring to the output first makes you blind to what is missing.
- Run all three questions — do not stop after Q1 if the format looks right. Constraint overflow and task drift hide behind good formatting [2].
- Fill in the pass/fail table even when the output seems correct. "Seems correct" and "is correct" are not the same. A table makes the difference visible.
- Name the failure pattern. "It failed" is less useful than "it failed because of constraint overflow on the domain boundary" [3].

**Do not:**
- Do not judge the output by its length or polish. A long, well-written output can still drift off-task or overflow a constraint.
- Do not mix testing with revision. Testing tells you what happened. Revision changes what you do next. Mixing them means you skip the clean record that testing provides [1].
- Do not skip the table for small tasks. Small tasks have small specifications with one or two constraints. A two-row table takes thirty seconds and tells you whether each constraint was met.

**Common anti-patterns:**

| Anti-pattern | The problem | The fix |
|---|---|---|
| "Looks good to me" review | Opinion without comparison to spec | Run the three questions against each part of the spec |
| Checking format only | Q1 passes, Q2 and Q3 unchecked | Always run all three questions |
| No recorded table | Finding noticed, not documented | Even a two-row table is a record — write it down |
| Classifying a partial pass as a pass | "Most of it was right" | Partial pass means the spec was not met — record it accurately |

## 9. Hands-On Exercise

Take any specification you have already written — from the lab activity or from a previous topic exercise. Run the full verification process from Section 6.

1. Re-read your specification.
2. Send it to an AI tool (or use a response you have already received).
3. Run the three-question check: format, constraints, task statement.
4. Build the pass/fail table with one row per specification component.
5. Classify the result: full pass, partial pass, or full fail.
6. If there are Fail entries, identify the failure pattern: format drift, constraint overflow, or task drift.

Compare your table with a peer's. Did you notice the same failures? Different ones? The goal is to practise the habit of comparing output to specification systematically — not to find perfect specifications.

## 10. Key Takeaways

- **Testing a specification** means comparing the AI's actual output to what you specified, part by part. It is not an opinion — it is a comparison against a written record.
- The **three-question verification check** is: (1) Did I get the format I asked for? (2) Did it stay within the constraints? (3) Does the output match the task statement? All three must be checked.
- A test result is classified as **full pass** (all questions pass), **partial pass** (some fail), or **full fail** (all fail). A partial pass is not a pass — it means the specification was not met and specific gaps can be named.
- The **pass/fail table** maps each component of your specification to the corresponding part of the output, with a Pass or Fail for each. It turns a vague impression into a specific, actionable finding.
- Three common failure patterns to recognise: **format drift** (right content, wrong shape), **constraint overflow** (content crossed an explicit boundary), and **task drift** (well-formed output, wrong task).

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
