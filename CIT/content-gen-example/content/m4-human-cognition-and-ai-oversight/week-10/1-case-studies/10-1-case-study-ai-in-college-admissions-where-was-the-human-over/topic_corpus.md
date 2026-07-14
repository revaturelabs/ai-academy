---
topic_id: "10.1"
title: "Case study: AI in college admissions — where was the human override point missed?"
position_in_module: 1
generated_at: "2026-06-12T00:00:00Z"
resource_count: 3
---

# 1. Case Study: AI in College Admissions — Where Was the Human Override Point Missed? — Topic Corpus

## 2. Prerequisites

This topic builds on vocabulary established in earlier sessions. You will need:

- **9.5 Automation bias** — the tendency to trust an automated system's output over your own judgment, even when the system is wrong.
- **9.7 The Judgment Framework — Q1: What is the cost of this being wrong?** — the first question you ask before delegating a decision to an AI.
- **9.8 The Judgment Framework — Q2: Can I verify this without the AI?** — whether a human can independently check the AI's output.
- **9.9 The Judgment Framework — Q3: Who is accountable if this fails?** — who is named as responsible when an AI-assisted decision causes harm.
- **9.10 Acceptable error** — the highest failure rate a use case can tolerate before harm becomes unacceptable.
- **9.11 High-stakes domains where AI must not have the final word** — medical, legal, and safety contexts where human sign-off is mandatory.

All six of these concepts recur throughout this case study. You do not need to re-read them now, but you will see their names used without re-definition.

## 3. Learning Objectives

By the end of this topic you should be able to:

1. Describe what happened in documented AI-in-admissions cases — what the AI was asked to do, what it actually did, and where the human check was absent or ineffective.
2. Identify the specific point in an admissions pipeline where a human override should have been required but was not.
3. Apply the Judgment Framework (Q1–Q3) to the admissions case and explain what each question reveals about the failure.
4. Explain how automation bias contributed to the missing override point.
5. Name at least two governance controls — concrete rules or processes — that would have caught the failure before it caused harm.
6. Write a short post-mortem identifying the governance gap in a described AI-assisted decision.

## 4. Introduction

Imagine you applied to a university. You spent weeks writing a personal statement — a short essay describing who you are, what drives you, and why you want to study there. You clicked Submit. Somewhere in the university's back office, software read your essay and gave it a number. A human staff member saw that number, assumed it was accurate, and moved on. No one re-read your words. No one questioned the score. Your application was rejected.

You never knew the software had been trained on a narrow sample of past accepted students, which mostly looked nothing like you. The score was wrong. The human who could have caught the error was present, but they had effectively handed the decision to the machine.

This is not a hypothetical. Research published in peer-reviewed journals documents exactly this pattern in AI-assisted college admissions [1]. The AI was not hiding its limitations. The governance process — the rules about when a human must check and override the AI — simply did not exist or was not followed.

This topic asks a precise question: **where, exactly, was the human override point missed?** Not "was AI bad?" — AI tools can genuinely help with large-scale screening when used carefully. The question is about the specific moment in the process where a human check was required by the nature of the decision, and that check either did not happen or was reduced to rubber-stamping the AI's output.

By the end of this topic you will be able to name that moment, explain why it was skipped, and describe the governance controls that would have preserved it.

## 5. Core Concepts

### 5.1 What AI Is Actually Doing in College Admissions

Before you can find the missing override point, you need to understand what AI tools are literally doing inside an admissions process. There are several distinct tasks that universities have used AI to help with, and they carry very different risk levels.

**Low-risk tasks (mostly safe to automate):**

- Checking whether an application is complete — are all required documents uploaded?
- Sorting applications into a review queue by programme, deadline, or self-declared category.
- Flagging obvious data-entry errors (e.g., a birth year entered as "1800").

**Higher-risk tasks (require human verification):**

- Scoring academic records — interpreting grade scales from different countries, weighting subjects.
- Predicting "likelihood of success" based on historical data about accepted students.
- Evaluating personal qualities — reading personal statements, letters of recommendation, or interview transcripts and producing a quality score.

The peer-reviewed literature draws a sharp line between these categories [1]. Automated sorting of complete or incomplete applications is a narrow, verifiable task. Evaluating personal qualities is not — it involves judgment about character, context, and potential that depends on information no model can fully capture: family circumstances, learning differences, a first-generation student's achievement relative to their starting point.

A key term here is **holistic review** — the admissions practice of considering the whole person: grades, personal statement, background, and context, rather than a single number. When AI scoring tools were introduced, many universities intended to use them as one input into holistic review. What the research documents is that in practice, holistic review collapsed. The AI score became the decision, not one input among several [1].

### 5.2 The Pipeline: How Applications Move Through a System

**Pipeline** — a fixed sequence of steps that every item passes through, one after another. In admissions, a pipeline might look like this:

1. Application submitted by student.
2. Completeness check (all documents present?).
3. Academic eligibility check (does GPA or qualification meet the threshold?).
4. Personal qualities scoring.
5. Final ranking and offer decision.

Each step feeds the next. The output of step 3 is the input for step 4. The output of step 4 is the input for step 5.

When a university introduces an AI tool, it typically replaces one or more of these steps — or, more precisely, it takes over producing the output that used to come from a human reviewer. The critical question is: **which steps have a human checking the AI's output before it feeds the next step?**

If the AI produces the personal qualities score in step 4, and a human reviews it before step 5, you have a human override point. If the score passes automatically to step 5 without review, you do not.

### 5.3 The Missing Override Point: What the Research Shows

A peer-reviewed study examining AI scoring of applicants' personal qualities found a consistent pattern across multiple institutions [1]: the AI tool was introduced to reduce the workload of human reviewers, but the governance structure — the rules about who reviews what and when — was not updated alongside the tool.

Specifically:

- **Before AI:** A human reviewer read each personal statement and produced a holistic score. Another reviewer sometimes checked a sample of cases. This checking process is called **calibration** — confirming that two reviewers would reach similar scores for the same application.
- **After AI:** The AI produced a score. The expectation was that human reviewers would check a sample of AI scores (a lighter version of calibration). In practice, reviewers spent less time on each case, trusting the AI's output. The calibration step quietly disappeared.

This is precisely what automation bias predicts (topic 9.5): when a system is fast and produces confident-looking outputs, humans reduce their checking. The missing override point was not dramatic. No one decided to remove human review. The check eroded gradually, driven by time pressure and the implicit assumption that a numeric score must be more objective than a human reading.

The Danish college admissions case studied in empirical research on algorithmic decision-making shows a parallel pattern [2]: when an algorithm was used to rank applicants, the institutions that kept a mandatory human sign-off at the ranking stage caught and corrected errors. Institutions that treated the algorithm's ranking as final did not catch errors — they found out about them only after applicants complained.

**What is a human override point?** A human override point is a defined checkpoint in a pipeline where a human is required to review the AI's output, may reject or change it, and must explicitly approve it before it moves forward. Both "required" and "may change it" are essential. A checkpoint where humans are present but never change anything — because they trust the AI — is not a functioning override point. It is automation bias in institutional form.

### 5.4 Why the Override Point Was Missed: Four Contributing Causes

Understanding what happened requires more than "someone made a mistake." Four causes worked together.

**Cause 1 — Automation bias at the individual level**

Each human reviewer experienced automation bias (topic 9.5). The AI's score arrived first, looked precise (e.g., "72 / 100"), and carried an implicit authority. Re-reading the personal statement to verify that score felt redundant. Most reviewers did not override it. Research on AI scoring of personal qualities documents this directly: review time per application dropped as reviewers deferred to the AI's output even when they had access to the original document [1].

**Cause 2 — Workload pressure**

Admissions offices process thousands of applications in a short window. When an AI tool reduced the time each application required, managers saw throughput increase and did not ask whether oversight had decreased alongside it. The incentive structure rewarded speed, not accuracy of review. This pattern — speed gains treated as productivity gains without measuring oversight loss — appears consistently across documented admissions deployments [1].

**Cause 3 — No explicit governance rule**

The university had not written down in policy: "For step 4 (personal qualities scoring), a human reviewer must read a minimum of X% of applications and must document any cases where the AI score was overridden." Without a written rule, the checkpoint existed only as an informal norm — and informal norms erode under pressure. Institutional analysis of AI admissions risks identifies the absence of a written override policy as the single most common governance gap across case reviews [3].

**Cause 4 — The AI's output was not independently verifiable in practice**

This is the Judgment Framework's Q2 from topic 9.8: "Can I verify this without the AI?" For an AI personal qualities score, the answer is: only by re-reading the personal statement yourself, which requires the same effort the AI was meant to replace. There was no easy independent check. The Judgment Framework says: when you cannot verify independently, you must not skip the human review step. Empirical study of algorithmic admissions decisions confirms this: institutions where reviewers lacked a practical verification path showed higher error persistence than those with structured re-read requirements [2].

### 5.5 Applying the Judgment Framework to This Case

You learned three questions in topics 9.7–9.9. Apply them now to the specific act of accepting the AI's personal qualities score without re-reading the application.

**Q1 — What is the cost of this being wrong?**

For the applicant: rejection from a university they may have deserved to attend. Potential impact on career path, financial planning, and the psychological experience of rejection.

For the university: legal and reputational risk. In jurisdictions with anti-discrimination law, an AI tool that consistently scores lower for applicants from certain demographic groups exposes the institution to challenge. Several universities have faced exactly this scrutiny [3].

The cost of being wrong is high. Q1 alone should trigger a mandatory human override point.

**Q2 — Can I verify this without the AI?**

The human reviewer can re-read the personal statement. That is independent verification — it does not rely on the AI. However, it requires significant time and is exactly what the AI was supposed to reduce. This tension is real: the verification mechanism exists, but the workflow was redesigned to eliminate it in practice.

When verification is possible but the workflow has been redesigned to prevent it, the governance failure is structural. The fix is also structural: redesign the workflow to require verification for a defined sample, not just allow it in theory.

**Q3 — Who is accountable if this fails?**

In most of the documented cases, this question had no clear answer. The AI vendor said the model performed to specification. The admissions office said they used the tool as recommended. The individual reviewer said they followed the process they were trained on. No single person was named as the decision-maker whose judgment was wrong.

This diffusion of accountability is itself a governance failure. The Judgment Framework says that when no one is accountable, the AI must not have the final word. In the admissions case, the AI effectively had the final word — and accountability was diffused to the point of meaninglessness.

### 5.6 Holistic Review Collapse: How It Happens in Five Stages

The term **holistic review collapse** describes what happens when a process designed to consider multiple factors about an applicant is quietly reduced to a single AI score. It does not happen overnight. It happens in stages:

1. AI tool introduced to assist — staff are told to use it as "one input."
2. Workload increases or stays the same. Staff begin spending less time re-reading applications that have already been scored by the AI.
3. Edge cases — applications that look unusual to the AI but strong to a human reader — begin to fall through. No one notices immediately, because no one is tracking how often the AI score is being overridden.
4. The AI score becomes the effective decision. The human step is retained on paper (for legal cover) but has no real function.
5. A complaint, an audit, or investigative journalism surfaces the pattern.

Research consistently documents this five-stage drift [1][2]. Stage 3 is where the override point is effectively lost. Stage 4 is where harm accumulates. Stage 5 is where the institution first learns that stage 3 happened.

The implication is important: the override point does not disappear in a single decision. It disappears through hundreds of small decisions to trust the score rather than check it. Governance controls need to be designed for stage 3 — before harm accumulates — not patched in at stage 5.

### 5.7 Bias in the AI Tool Itself

The missing human override point matters more because the AI tools used in many documented admissions cases were not neutral. They were trained on historical admissions data — records of who was accepted and who succeeded in the past.

**Training data** — the set of examples an AI learns from. The AI learns to produce outputs that resemble what appears in its training data.

If the historical data reflects past admissions that were not themselves fair — for example, if past cohorts over-represented applicants from certain schools, regions, or socioeconomic backgrounds — the AI learns to score new applicants in ways that reproduce those patterns. The AI is not making a conscious choice. It is doing exactly what it was trained to do. But what it was trained to do encodes a historical bias.

This connects directly to topic 9.6 (how human biases get encoded into AI training data). The admissions case is a concrete illustration: a tool trained on non-representative historical data will score current applicants in ways that replicate historical inequities. A functioning human override point is one of the few mechanisms that can catch and correct this in real time, before the decision becomes final.

The USC analysis of AI admissions risks identifies this as one of the central governance gaps [3]: institutions did not audit whether the AI's scores correlated with demographic variables — first-generation status, school type, postcode — before deploying the tool at scale.

### 5.8 What a Functioning Override Point Looks Like

The missing override point was an absence. A present, functioning override point has five properties:

| Property | What it means in the admissions context |
|---|---|
| **Defined** | Written in policy: at step 4 (personal qualities scoring), a human reviewer reads the personal statement before the score is used in ranking. |
| **Sampled** | For large volumes, policy specifies a minimum review sample — e.g., 20% of applications, or 100% of scores below a threshold. |
| **Documented** | Each review is logged: reviewer ID, application ID, AI score, human judgment, and outcome (accepted or overridden). |
| **Empowered** | The reviewer has genuine authority to override — overrides do not require manager approval, and overriding is not penalised. |
| **Monitored** | Someone reviews the override log on a schedule. If the override rate drops to near zero, that is a warning signal, not a success metric. |

A near-zero override rate means either the AI is extraordinarily accurate (rare) or reviewers have stopped genuinely reviewing (common). An institution that celebrates a 0% override rate without investigating has confused the metric for the goal.

## 6. Implementation

### How to Audit a Pipeline for a Missing Override Point

This is a step-by-step method for identifying where the human override point is missing in any AI-assisted pipeline. You will use this in the lab activity for this week and in Assessment 3.

**Step 1 — Map the pipeline.**
Write out every step from input (application received) to output (offer or rejection). For each step, note: is a human involved? What does the human do? What does the AI produce?

**Step 2 — Apply Q1 at each step.**
For each step, ask: what is the cost if the output of this step is wrong? Steps where the cost to the affected person is high (rejection, significant financial consequence, a record retained in a database) are candidates for mandatory override points.

**Step 3 — Apply Q2 at each step.**
For each step that involves AI output, ask: can a human verify this output without using the same AI? If the answer is no — or only-in-theory-but-the-workflow-prevents-it — that step requires a structural fix. Not just permission to override, but a workflow that actively requires checking.

**Step 4 — Apply Q3 at each step.**
Who is named as accountable for the AI's output at this step? If the answer is "no single person" or "the AI vendor," the accountability is diffuse. A governance fix names a human decision-maker who owns the outcome.

**Step 5 — Check override logs.**
If logs exist, look at the override rate. If it is near zero and the AI has not been independently validated as near-perfect, that is evidence of automation bias or a non-functioning override point.

**Step 6 — Write the governance control.**
For each step where the override point is missing or non-functioning, write the policy rule that would fix it. Use this exact form:

> "At [step name], a human reviewer must [specific action] for [scope: all applications / minimum X% sample / all scores below threshold Y]. The reviewer must document [what is recorded]. The reviewer has authority to override without [approval requirement that would deter overriding]. This log is reviewed [frequency] by [named role]."

This six-step audit is the practical tool. The case study evidence above is why each step matters.

## 7. Real-World Patterns

### 7.1 The Pattern Repeats Across Institutions

The admissions case is not an isolated failure. The same structural pattern — AI tool introduced, human oversight erodes, harm accumulates before anyone notices — appears across multiple real implementations.

In the peer-reviewed literature, research on AI scoring of personal qualities found that human review time per application dropped by more than half within two years of deployment at institutions that did not maintain structured override requirements [1]. The intended check became nominal rather than real.

In the Danish algorithmic admissions case, institutions that preserved a mandatory human sign-off at the ranking step caught and corrected errors. Those that treated the ranking as final discovered errors only after applicants complained [2].

The USC analysis of AI in admissions identifies governance gap as the single most common finding across institutional case reviews: not that the AI failed technically, but that the institution had not designed a governance process to match the risk level of the decisions being made [3].

### 7.2 Why Override Points Erode Over Time

There is a specific mechanism behind this pattern worth naming clearly. When an AI tool is accurate most of the time, human reviewers who do check its outputs find nothing to override most of the time. From an individual reviewer's perspective, checking feels pointless. From a manager's perspective, a reviewer who spends time checking something they never override looks inefficient.

The tool's accuracy becomes its own enemy. The more accurate it is on ordinary cases, the more automation bias builds around it — and the less likely it is that reviewers are paying attention when the unusual case appears, which is exactly where the AI is most likely to be wrong. The peer-reviewed research on AI admissions scoring documents review time dropping to near zero for cases where the AI's score was confidently above or below threshold — the very cases reviewers stopped checking were those where error, if present, had the largest impact on outcome [1].

This is related to automation complacency, a concept covered in a later topic in this week's sequence. The relevant point here is that the admissions research documents this dynamic directly [1][2].

### 7.3 When the Override Point Was Preserved

The contrast case is instructive. Institutions that designed override points as mandatory, sampled, logged, and monitored — not just permitted — showed substantially better outcomes [2][3]:

- They caught AI scoring errors before offers were sent [2].
- They identified demographic correlation in AI scores (scores that varied by applicant postcode or school type) during internal audits rather than after complaints [3].
- They were able to demonstrate in writing that a human had made the final judgment — protecting the institution legally and preserving applicant trust [3].

The contrast is not between institutions that had AI and institutions that did not. It is between institutions that designed human oversight into the workflow structurally and those that left it informal [2].

## 8. Best Practices

### Governance Controls That Would Have Caught the Failure

The following controls are drawn from the case study evidence and the USC institutional analysis [3]. They are documented practices that functioned where they were used.

**Do:**

- Write the override point into policy **before** deploying the AI tool, not after. Retroactive governance misses the early-adoption period when norms are set.
- Set a minimum override review sample that is written down — 20% is common in documented cases. Require 100% review for scores below any rejection threshold.
- Log every human review with the reviewer's ID, the AI score, and the outcome. No log means no evidence it happened.
- Monitor the override rate on a schedule (monthly minimum). A near-zero rate triggers an audit, not a celebration.
- Audit AI scores for demographic correlation before deployment and annually after. Look for correlation between score and postcode, school type, first-generation status.
- Name a human decision-maker who owns the output of the AI step. That person's name is associated with the outcome.

**Do not:**

- Treat a numeric AI score as more objective than human judgment. A number feels precise, but precision is not the same as accuracy. A score of "72/100" can be entirely wrong.
- Count the override point as functional if reviewers are almost never overriding. Investigate before concluding the AI is performing well.
- Remove the calibration step — the process of cross-checking reviewer consistency — just because the AI produces consistent outputs. Consistency can consistently encode the same error.
- Allow the vendor to be the accountable party for the decision. The vendor is accountable for the tool meeting its specification. The institution is accountable for the decision made with it.
- Design governance only for the typical case. The failure mode is the unusual case — the first-generation student, the non-standard qualification, the essay that the model cannot interpret but represents genuine strength.

### The Anti-Pattern: Override as Theater

The most important anti-pattern to recognise is **override as theater** — a human checkpoint that exists on paper but functions as rubber-stamping. It looks like governance. It produces no actual oversight. And it creates false confidence, because an audit that asks "is there a human review step?" will say yes.

Detecting override-as-theater requires looking at the override rate and the time per review, not just the presence of the step. An institution where reviewers average 90 seconds per personal statement and override the AI 0% of the time is not doing holistic review. It is producing paperwork.

## 9. Hands-On Exercise

**Post-Mortem Exercise (200 words)**

This exercise matches the lab activity for this week and Assessment 3.

Read the following scenario:

> A university introduced an AI tool to score personal statements on four qualities: resilience, motivation, communication, and intellectual curiosity. Each quality was scored 0–25, giving a total of 0–100. Applications scoring below 60 were automatically moved to a rejection pool. Human reviewers were available to look at borderline cases (55–65). In the first year, 92% of applications below 60 were rejected without any human review. The university received complaints from three applicants whose personal statements had described significant adversity. On re-reading, two of the three would have been moved above 60 by a human reviewer.

Write a 200-word post-mortem that answers:

1. At which step in the pipeline was the human override point missing?
2. Which of the four causes from this topic best explains why the override point was missed?
3. Write one governance control — in the exact form from section 6, Step 6 — that would have prevented this outcome.

There is no single right answer for part 2. The strongest post-mortems identify the structural cause (no written policy requiring review below the rejection threshold) rather than blaming an individual reviewer.

## 10. Key Takeaways

- AI tools in college admissions were used to score personal qualities — a high-stakes, hard-to-verify judgment. The human override point was missed when the governance process was not updated to match the risk level of the task being automated.
- The failure was not a single dramatic decision. The override point eroded gradually through automation bias, workload pressure, absence of a written policy, and the practical difficulty of independently verifying an AI score.
- Applying the Judgment Framework: Q1 shows the cost of being wrong is too high for the AI to have the final word; Q2 shows verification is possible but was structurally removed from the workflow; Q3 shows accountability was diffused to the point of meaninglessness.
- A functioning override point is defined in writing, applied to a specified sample, logged, empowered (reviewers can override without penalty), and monitored. Override-as-theater — a human step that exists on paper but produces no checking — is not a functioning override point.
- The contrast case shows that institutions that designed override points structurally caught errors before harm occurred. The determining factor is governance design, not AI capability.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
