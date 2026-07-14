---
topic_id: "10.7"
title: "Writing a post-mortem — what failed, why, who was accountable, what governance would have prevented it"
position_in_module: 1
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. Writing a post-mortem — what failed, why, who was accountable, what governance would have prevented it — Topic Corpus

## 2. Prerequisites

This topic draws on concepts from the following prior topics. Each term is used here without re-definition — revisit the listed topic if anything feels unfamiliar.

- **9.7 — Judgment Framework Q1**: What is the cost of a wrong answer? Used here to establish why a post-mortem begins by characterising the harm the failure caused.
- **9.9 — Judgment Framework Q3**: Who is accountable if this is wrong? The accountability section of a post-mortem answers exactly this question.
- **9.11 — High-stakes domains where AI must not have the final say**: helps calibrate how seriously a failure should be treated.
- **10.1 — Human override point, override as theater, pipeline, holistic review collapse**: vocabulary for where oversight broke down in the college admissions case, used here as a worked post-mortem example.
- **10.2 — Failure mode, systematic under-scoring, evaluation gap, override accountability, post-market surveillance analogy**: diagnostic language used to complete the "why" section of a post-mortem.
- **10.3 — Diffuse accountability, accountability gap, adverse action notice, model documentation, accountability chain**: the accountability vocabulary the post-mortem must resolve.
- **10.4 — Automation complacency, vigilance decay, accuracy paradox**: explains why failures in high-accuracy systems are often discovered late.
- **10.5 — Human-in-the-loop (HITL), human-on-the-loop (HOTL), checkpoint, confidence routing, escalation trigger**: the oversight mechanism vocabulary needed to propose governance fixes.
- **10.6 — Risk-tiered component mapping, mandatory checkpoint, error budget, triggered oversight assignment**: the component-level framework for identifying which fix belongs where.

## 3. Learning Objectives

By the end of this topic you should be able to:

1. Define what a **post-mortem** is and state its purpose in an AI system context.
2. Describe the four sections of a post-mortem — what failed, why it failed, who was accountable, and what governance would have prevented it — and explain what belongs in each section.
3. Apply the four-section framework to one of the Week 10 case studies (college admissions, medical triage, or loan approval) and produce a structured 200-word post-mortem.
4. Distinguish between a **proximate cause** (the immediate trigger) and a **root cause** (the underlying condition that made the failure possible), and place each in the correct post-mortem section.
5. Propose a specific, named governance control — citing concepts from topics 10.5 and 10.6 — as the prevention answer for a given failure.
6. Recognise the difference between a blame-assigning post-mortem and a **no-blame post-mortem**, and explain why the no-blame approach produces more useful governance improvements.

## 4. Introduction

Imagine a team has just discovered that an AI system they deployed caused harm. Loan applicants were rejected unfairly. Medical patients were under-triaged. Students were denied admission without a human ever reviewing their files. The immediate crisis is over. Now what?

The answer is a **post-mortem** — a structured written account of what went wrong, produced after an incident so that the same failure does not happen again.

The word "post-mortem" comes from Latin and literally means "after death." In engineering and medicine it has long referred to an investigation done after something has failed. In the context of AI systems, a post-mortem is not a punishment document. It is a learning document. Its job is to capture four things in plain language:

1. What exactly failed?
2. Why did it fail?
3. Who was accountable — and was that accountability clear enough?
4. What governance control, if it had existed, would have prevented this failure?

These four questions are not academic. Assessment 3 (Maths and Cognition Lab Report, 15%, due this week) requires you to write a 200-word post-mortem applying this framework to a technical AI system. Every section of this corpus is designed to prepare you for that task.

A post-mortem is also the moment where the theoretical vocabulary you have built up across weeks 9 and 10 gets used in a single focused document. Automation complacency explains *why* the failure was tolerated. Diffuse accountability explains *who* could not be named. Human-in-the-loop checkpoints and risk-tiered component mapping provide the vocabulary for the governance fix. The post-mortem is where that vocabulary earns its keep.

## 5. Core Concepts

### 5.1 What a post-mortem is (and what it is not)

A **post-mortem** (also called a **post-incident review** or **incident retrospective**) is a written document produced after an AI system incident that answers the four standard questions in a structured format [2].

What a post-mortem is:

- A factual account of what the system did, what the outcome was, and who was involved [2].
- A causal analysis — tracing the chain of events back to the conditions that made the failure possible [3].
- A governance proposal — a specific control that, if implemented, would prevent recurrence [2].
- A shared learning artefact — written so that people who were not present during the incident can understand what happened and why [2].

What a post-mortem is not:

- A list of names to blame. Assigning blame to individuals shuts down honest reporting. People stop disclosing near-misses, making the next real failure more likely [2].
- A formality. A post-mortem that lists the incident and then says "lessons learned: be more careful" has zero value. The governance fix must be specific and actionable [2].
- A complete audit. A post-mortem is fast and focused — typically 200–500 words for a single incident [2]. Deeper audits are separate work.

**No-blame post-mortem** — a framing principle that holds the *system* responsible rather than the individual person [2]. This does not mean nobody is accountable. It means accountability is directed at the *design decisions, missing controls, and oversight gaps* that made the failure inevitable — rather than at the person who happened to be at the keyboard when the alarm went off [2].

Why does the no-blame framing matter for AI systems specifically? Because AI failures rarely have a single guilty human. They result from many small decisions — training data choices, threshold settings, missing human checkpoints, unclear escalation paths — made by different people across different teams and organisations [1]. Blaming one person papers over the structural problem. The no-blame post-mortem forces you to look at the structure [1].

### 5.2 Section 1 — What failed

The first section of a post-mortem answers one question: **What exactly happened?** [2]

This section must be factual and specific [2]. It names the system, the decision or output that was wrong, the population affected, and the measurable impact. It does not assign blame. It does not explain why yet.

What to include [2]:

- **System name and function.** What was the AI system supposed to do?
- **The failure event.** What did it actually do instead?
- **Scope.** How many decisions, how many people, over what time period?
- **Observed harm.** What was the real-world consequence? (A rejected loan application, a missed triage flag, an admission denial.)

What to avoid [2]:

- Vague language. "The system performed poorly" is not a failure description. "The system rejected 34% of applicants from zip codes with median income below $40,000, compared to 12% from higher-income zip codes, despite comparable repayment histories" is a failure description.
- Jumping ahead to causes. The "what" section is pure observation. Save the causal analysis for section 2.

**Example — loan approval case (topic 10.3):** The AI loan approval system rejected applicants from lower-income zip codes at nearly three times the rate of higher-income applicants with equivalent credit histories. The disparity was not detected for an extended period after deployment. During that time, a substantial number of applicants received automated rejections that a human reviewer would likely have reversed.

### 5.3 Section 2 — Why it failed

The second section answers: **Why did this happen?** This is the causal analysis. It requires two distinct levels of explanation.

**Proximate cause** — the immediate trigger: the specific event or condition that directly produced the failure. Think of it as "the thing that broke."

**Root cause** — the underlying condition that made the failure possible. Think of it as "the reason the broken thing was allowed to exist."

The distinction matters because fixing only the proximate cause leaves the root cause in place. The same failure, or a different one with the same underlying structure, will recur.

| Level | Question it answers | Example (loan case) |
|---|---|---|
| Proximate cause | What directly caused the bad output? | Model trained on historical data that encoded past lending discrimination |
| Root cause | What condition allowed the proximate cause to exist and persist undetected? | No sub-group performance audit was run before or after deployment; no evaluation gap check was in place |

How to identify the root cause: ask "why" repeatedly until you reach a structural condition — a missing oversight mechanism, an unclear accountability chain, a governance gap — rather than a human error.

For AI systems, root causes typically fall into one of four categories [1]:

1. **Training data problem.** The data encoded a historical bias, contained errors, or did not represent the affected population.
2. **Evaluation gap.** The model was tested for average accuracy but not for sub-group fairness, edge-case performance, or real-world distribution shift.
3. **Missing checkpoint.** No human-in-the-loop gate was placed at the point where the consequential decision was made.
4. **Accountability gap.** No specific person or team was designated to own the failure mode — so nobody was watching for it and nobody was obligated to fix it [1].

Root causes often combine. The loan approval failure combined all four: biased training data produced the initial disparity; the evaluation gap let it pass deployment review; no mandatory checkpoint required human sign-off on population-level patterns; and diffuse accountability meant no one was watching for the disparity across organisations.

**Automation complacency** (topic 10.4) is frequently a contributing root cause: because the system had high average accuracy, operators stopped scrutinising its outputs. High accuracy made the failure invisible. This is the accuracy paradox introduced in topic 10.4 — it belongs in the root cause analysis whenever a system was trusted without adequate monitoring because it "worked well most of the time."

**Failure mode vs. root cause.** A failure mode (from topic 10.2) is the *pattern* of failure — the way the system tends to go wrong. A root cause is the condition that produced that failure mode. Systematic under-scoring (10.2) is a failure mode. The evaluation gap that allowed it to persist undetected is a root cause. The "why" section should name both.

### 5.4 Section 3 — Who was accountable

The third section answers: **Who was responsible, and was the accountability structure adequate?**

This is where you apply Judgment Framework Q3 (topic 9.9) — "Who is accountable if this is wrong?" — retrospectively, after the failure has already happened.

The section should identify:

1. **Who was designated as accountable** at the time of the incident. Look for: the team or person who deployed the system, the team or person who was supposed to monitor it, and the role that signed off on deployment.
2. **Whether the accountability was real or diffuse.** If multiple parties each assumed "someone else" was responsible, that is diffuse accountability (topic 10.3) — and that diffusion is itself a root cause to name.
3. **Whether the accountable party had the means to act.** Accountability without authority is not accountability. If the person responsible for model monitoring did not have the access, staffing, or budget to investigate alerts, the accountability structure was broken by design.
4. **Whether the accountability chain connected to the people harmed.** Were affected individuals able to identify who was responsible and reach them? The adverse action notice requirement (topic 10.3) is one governance mechanism that tries to create this link.

A useful test: "If the monitoring team had discovered this failure on Day 1, did they have the authority and obligation to halt the system?" If the answer is unclear, the accountability structure was inadequate regardless of what the contracts said [1].

**What "who was accountable" does not mean.** It does not mean naming the individual developer who wrote the model. In an AI system operating at scale, the accountability structure is organisational. The question is whether the right *role* had clear responsibility — not whether a particular person made a bad decision [2].

**Example — medical triage case (topic 10.2).** The triage AI was deployed by a hospital system but the model was built by a third-party vendor. The hospital's clinical team assumed the vendor had validated sub-group performance. The vendor assumed the hospital would conduct its own validation. No contract clause specified which party was responsible for post-deployment sub-group monitoring. The result: override accountability was absent (topic 10.2). Nobody was obligated to detect the systematic under-scoring of elderly patients. Nobody did.

### 5.5 Section 4 — What governance would have prevented it

The fourth section answers: **What specific control, if it had been in place, would have prevented this failure or caught it earlier?**

This is the forward-looking half of the post-mortem. It converts the analysis into an actionable proposal. The governance fix must be [1] [2]:

- **Specific.** Name the exact mechanism: a mandatory checkpoint (topic 10.5), a triggered oversight assignment (topic 10.6), a sub-group performance audit (topic 10.2), a model documentation requirement (topic 10.3). "Better oversight" is not a governance fix.
- **Placed correctly.** Use the risk-tiered component mapping framework (topic 10.6) to identify which component in the system needed the control, and at what tier it should have been set.
- **Proportionate to the root cause.** Match the fix to the failure. If the root cause was an evaluation gap, the fix is a mandatory evaluation protocol. If the root cause was an accountability gap, the fix is an explicit accountability clause [1].

**Governance control vocabulary from prior topics.** You have already learned the language you need to write this section [1] [3]:

| Root cause type | Matching governance fix |
|---|---|
| Training data problem | Mandatory sub-group performance audit before deployment (topic 10.2) [3] |
| Evaluation gap | Triggered oversight assignment when sub-group error rate exceeds error budget (topic 10.6) [3] |
| Missing checkpoint | Human-in-the-loop checkpoint at the high-stakes decision point (topic 10.5) [1] |
| Accountability gap | Named accountability role + model documentation requirement (topic 10.3) [1] |
| Automation complacency | Periodic re-calibration exercise + escalation trigger on accuracy drift (topics 10.4 and 10.5) [3] |

Your job in the post-mortem is to map the failure to the correct existing control — by name — and explain why that control would have interrupted the causal chain [1] [2].

**Example — college admissions case (topic 10.1).** The root cause was holistic review collapse: the AI condensed a multi-factor evaluation into a single score, and no human override point was meaningfully enforced. The governance fix is a mandatory human-in-the-loop checkpoint for every applicant whose AI score places them in the borderline tier — the range where the score difference is smaller than the known model uncertainty. This checkpoint requires a trained reviewer to consult the full application file before a decision is recorded. This is an HITL checkpoint placed at a confidence routing trigger (topic 10.5): when the model's confidence is insufficiently high to justify autonomous action, the decision is escalated for human review [1].

### 5.6 The no-blame framing in practice

The hardest part of writing a post-mortem is maintaining the no-blame framing while still naming real accountability failures. These feel contradictory. They are not.

No-blame means: do not assign moral fault to an individual for a structural problem. It does not mean: pretend the accountability structure worked when it did not.

A useful distinction:

- **Blame** is directed at a person's intentions or character.
- **Accountability** is directed at a role, a process, or a structure.

The post-mortem can and should say "the accountability structure was inadequate." It should not say "Person X failed."

In practice this means writing in role-based language:

- Not: "The data scientist should have caught this bias."
- Yes: "No sub-group fairness audit was required at the point of model sign-off. This is the gap the governance fix addresses."

The no-blame framing also shapes what you propose. If you catch yourself proposing "train engineers better" as a governance fix, stop. That is a blame-based fix disguised as a training recommendation. A governance fix changes the *system* — it adds a mandatory check, requires a specific sign-off, or creates an explicit accountability role. It does not depend on individuals being more careful [2] [3].

## 6. Implementation — Writing the four-section post-mortem

This section gives you a step-by-step procedure for drafting a post-mortem from scratch [2]. The output format matches the 200-word format required for Assessment 3 Part 2.

**Step 1 — Choose and name the incident.**
Write one sentence that names the AI system, its function, and the failure event [2].

*Template:* "[System name], a [what it does] tool, [what it did wrong] affecting [who] between [when] and [when], causing [harm]."

**Step 2 — Write the "what failed" paragraph (40–50 words).**
State the specific failure: what output was wrong, how many decisions were affected, and what real-world harm resulted [2]. Be concrete. Use numbers if you have them. Do not explain causes yet.

**Step 3 — Write the "why it failed" paragraph (50–60 words).**
Name the proximate cause first (what directly produced the bad output). Then name the root cause (the structural condition that allowed it) [1]. Use the four root cause categories from section 5.3 as a checklist: training data problem, evaluation gap, missing checkpoint, accountability gap [1]. Automation complacency may appear as a contributing factor.

**Step 4 — Write the "who was accountable" paragraph (40–50 words).**
Identify the designated accountable role(s) [1]. State whether the accountability was real or diffuse. If diffuse, say so explicitly [1]. Cite the specific gap: was there no model documentation requirement? No named monitoring owner? No obligation to report adverse outcomes?

**Step 5 — Write the "governance fix" paragraph (50–60 words).**
Propose one specific governance control [2]. Name it using vocabulary from topics 10.2–10.6. State where it would be placed in the system (which component, at which risk tier) [3]. Explain in one sentence why it would have interrupted the causal chain [1].

**Step 6 — Review for no-blame framing.**
Read back through sections 3 and 4. If any sentence names an individual and assigns fault, rephrase it in role-based or structural language [2]. The test: could every named party read this document and agree with the facts, even if they disagree with the conclusions?

**Full worked example — medical triage case (topic 10.2), 200-word format:**

---

*Post-Mortem: Automated Medical Triage System — Systematic Under-Scoring of Elderly Patients*

**What failed.** The triage AI assigned lower-priority scores to patients over 75 than clinical staff would have assigned using manual assessment, across a substantial number of cases over an extended operational period [3]. In documented cases, patients in this group experienced deterioration that a higher triage priority might have prevented.

**Why it failed.** The proximate cause was a training dataset that under-represented elderly patients with atypical symptom presentations, producing a systematic low-bias in scores for that group [1]. The root cause was an evaluation gap: no sub-group performance audit was required before or after deployment [1]. Automation complacency compounded the problem — because the system's overall accuracy was high, clinical staff stopped scrutinising borderline scores.

**Who was accountable.** No single party held clear accountability [1]. The hospital assumed the vendor had validated sub-group performance; the vendor assumed the hospital would [3]. Override accountability was absent: no role was designated to review population-level scoring patterns after deployment [1].

**Governance fix.** A mandatory sub-group performance audit, run on a regular cycle by a named clinical informatics owner, would have detected the age-related scoring gap within the first audit period [3]. Pairing this with a triggered oversight assignment — escalation when elderly patient scores deviate from clinical override rates beyond a defined threshold — would have prevented the failure mode from persisting undetected [1] [3].

---

This example is approximately 200 words. It names the system, states the harm, distinguishes proximate from root cause, identifies the accountability gap, and proposes a named, placed, proportionate governance fix [2]. That is the target for Assessment 3 Part 2.

## 7. Real-World Patterns

Post-mortems appear across every sector where AI systems make consequential decisions. The four-section structure developed in this topic draws on established practice in software engineering and AI governance [2] [3].

**No-blame culture in SRE practice.** Site Reliability Engineering (SRE) — the discipline of maintaining large-scale software systems — has used structured post-mortems for decades [2]. The SRE community settled on the no-blame framing after finding that blame-assigning reviews caused engineers to hide failures rather than report them [2]. The result was fewer documented incidents and more undocumented ones. The no-blame post-mortem produced more honest reporting and faster improvement [2].

**Consistent root causes across sectors.** Research tracking real AI incidents systematically shows that the four root cause categories from section 5.3 (training data problem, evaluation gap, missing checkpoint, accountability gap) appear repeatedly across healthcare, financial services, criminal justice, and education [1] [3]. The root causes are more consistent than the domains [1]. That consistency is what makes the four-section framework transferable.

**Post-mortem as governance feedback loop.** An important function of the post-mortem is that it feeds back into governance design [3]. A single post-mortem proposes one governance fix [2]. A body of post-mortems from a system's operational history builds an empirical case for which controls are missing and which are working [3]. The post-mortem is not just a retrospective exercise — it is the raw material from which governance is improved over time [3].

**The most common post-mortem failure: vagueness.** The most common failure in real post-mortems is not dishonesty — it is vagueness [2]. A post-mortem that concludes "the model performed below expectation" and proposes "more rigorous testing" has produced a document that looks like a post-mortem without functioning as one [2]. The four-section framework guards against this by forcing a specific answer at each step [2].

**The post-mortem format in criminal justice and content moderation.** The same four-section format applies in domains beyond healthcare and finance. In criminal justice, AI-assisted risk scoring tools — systems that assign a numerical score estimating the likelihood that a person will reoffend — have been used in bail and sentencing decisions across multiple jurisdictions. A risk score is a recommendation, not a verdict; but documented cases show that human reviewers, affected by automation complacency (topic 10.4), treated the score as effectively final, making human-in-the-loop checkpoints (topic 10.5) operate as override theater rather than genuine review. Post-incident reviews of these deployments have consistently identified the same accountability chain failure (topic 10.3): no single role was designated to audit whether the human checkpoint was functioning, so the failure mode persisted undetected for extended periods [1]. In content moderation — where AI systems flag or remove online content at a scale no human workforce could manually review — documented post-mortem practices have followed the same pattern: the "what failed" section describes the category of content systematically mis-classified; the "why" section names the training data gap or evaluation gap that produced it; and the governance fix section proposes a triggered oversight assignment, routing a sample of borderline decisions to human reviewers when the model's confidence falls below a defined threshold [1] [3]. Across both domains, the governance feedback loop (topic 10.3's accountability chain concept applied at scale) is the mechanism by which individual post-mortems accumulate into improved oversight design [3].

## 8. Best Practices

**Do:**

- **Name the specific failure.** Use numbers and scopes. "High error rate" is not a failure description. "34% false-negative rate in the elderly cohort over 18 months" is.
- **Separate proximate from root cause.** If you have only one cause, you probably have not dug deep enough. Most AI failures have a surface trigger and a structural condition underneath it.
- **Propose a control from the vocabulary you already have.** HITL checkpoint, sub-group audit, error budget, mandatory checkpoint, triggered oversight assignment — these are specific mechanisms. Name the mechanism, not the aspiration.
- **Write in no-blame language throughout.** Role-based and structure-based language throughout. Avoid naming individuals in a fault-assigning way.
- **Keep it short and specific.** A 200-word post-mortem that precisely names the failure, cause, accountability gap, and governance fix is more useful than 1,000 words of general reflection.

**Don't:**

- **Don't treat "we need better AI" as a governance fix.** Better AI is not a governance control. A governance control changes the process around the AI — when it can act autonomously, who must sign off, what must be audited.
- **Don't skip the accountability section.** The temptation is to go straight from "why" to "governance fix." But if the accountability structure was inadequate — which is true in most of the Week 10 cases — the governance fix must address that gap, not just the technical one.
- **Don't propose fixes you cannot place.** Every governance fix should attach to a specific component, risk tier, and sign-off requirement. A fix that floats above the system cannot be implemented.
- **Don't conflate "no blame" with "no accountability."** The post-mortem should clearly state whether the accountability structure was adequate. No-blame means no personal fault assignment. It does not mean the system is blameless.

## 9. Hands-On Exercise

Pick one of the three Week 10 case studies — college admissions (10.1), medical triage (10.2), or loan approval (10.3) — that you have not yet used as an example in your notes.

Using the step-by-step procedure in section 6, draft a 200-word post-mortem for that case. Your draft should:

1. Name the system and the failure event in one sentence.
2. Identify both the proximate cause and at least one root cause.
3. Name the specific accountability gap — who should have been responsible but was not designated clearly.
4. Propose one named governance control (using vocabulary from topics 10.5 or 10.6) and state where in the system it would be placed.

Compare your draft to the worked example in section 6. Check: Did you use numbers? Did you separate proximate from root cause? Did you name a specific governance mechanism — not just "better oversight"? Did you maintain no-blame language throughout?

This exercise is the direct preparation task for Assessment 3 Part 2.

## 10. Key Takeaways

- A **post-mortem** is a structured written account of what went wrong in an AI incident, produced after the fact so the failure does not recur. It is a learning document, not a blame document.
- The four sections — what failed, why it failed, who was accountable, and what governance would have prevented it — force specific answers at every step. Vague answers at any step produce a post-mortem that looks complete but teaches nothing.
- **Proximate cause** is the immediate trigger; **root cause** is the structural condition that made the failure possible. Fixing only the proximate cause leaves the root cause intact. Most AI failures have root causes in at least one of four categories: training data problem, evaluation gap, missing checkpoint, or accountability gap.
- **No-blame framing** does not mean no accountability. It means accountability is directed at roles, structures, and design decisions — not at individual fault. This framing produces more honest reporting and more useful governance fixes.
- The governance fix must be **specific, placed, and proportionate**: name the mechanism, identify which component it attaches to, and explain why it would have interrupted the causal chain.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
