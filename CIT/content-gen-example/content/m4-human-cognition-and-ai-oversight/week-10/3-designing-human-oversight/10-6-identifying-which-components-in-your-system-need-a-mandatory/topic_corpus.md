---
topic_id: "10.6"
title: "Identifying which components in your system need a mandatory human checkpoint"
position_in_module: 2
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. Identifying Which Components in Your System Need a Mandatory Human Checkpoint — Topic Corpus

## 2. Prerequisites

This topic builds directly on vocabulary introduced earlier in week 10 and in week 9. Every term below is used without re-definition — revisit the listed topic if anything feels unfamiliar.

- **9.7–9.9 — The Judgment Framework (Q1, Q2, Q3)**: the three-question test that tells you how much human involvement a decision requires. Q1: what is the cost of being wrong? Q2: can I verify this without the AI? Q3: who is accountable?
- **9.10 — Acceptable error / failure threshold**: the highest failure rate a use case can tolerate before harm becomes unacceptable.
- **9.11 — High-stakes domains**: medical, legal, and safety contexts where AI must not have the final word.
- **9.5 — Automation bias**: the tendency to trust an automated system's output over your own judgment, even when the system is wrong.
- **10.4 — Automation complacency, accuracy paradox, vigilance decay, trust calibration**: why high accuracy makes human oversight harder to sustain.
- **10.5 — HITL, HOTL, HOOTL, checkpoint, confidence routing, escalation trigger, checkpoint matrix**: the three oversight modes and the mechanism for assigning each one to a component.

## 3. Learning Objectives

By the end of this topic you should be able to:

1. Explain what it means to identify a "component" in an AI system and why different components carry different risk levels.
2. Apply all three Judgment Framework questions to an individual system component and reach a justified oversight assignment (HITL, HOTL, or HOOTL).
3. Define **risk-tiered component mapping** and produce a simple component map for a described AI system.
4. Use the EU AI Act Article 14 requirements as a reference to confirm whether a component's oversight design meets a regulatory minimum [1].
5. Identify at least two signals that indicate a component's oversight assignment needs to be upgraded from HOTL or HOOTL to HITL.
6. Explain why the same AI component can require different oversight levels in different contexts, and name the context variables that cause the shift.

## 4. Introduction

You have already learned that some AI decisions need a human in the loop, some need a human on the loop, and some can run without any direct human involvement. Topic 10.5 gave you the three oversight modes and a checkpoint matrix for choosing between them.

But real systems are not single decisions. They are chains of decisions, running one after another. A loan application system might check your identity, verify your income, score your credit history, check for fraud signals, and then produce a final recommendation — five distinct steps, each doing something different, each carrying different consequences if it goes wrong.

The question this topic answers is precise: **which specific components in a chain like that are the ones that need a mandatory human checkpoint?** Not the whole system — the components. Not a general feeling that "this is high-stakes" — a step-by-step method that produces a defensible answer for each component.

This matters for Assessment 3, where you are asked to apply all three Judgment Framework questions to a technical AI system in your domain with quantified acceptable error thresholds. The method in this topic is the engine for that task.

## 5. Core Concepts

### 5.1 What Is a Component?

Before you can identify which components need mandatory checkpoints, you need a clear definition of what a component is.

**Component** — a distinct step in an AI system's processing chain that takes a defined input, applies a specific operation, and produces an output that feeds the next step. Each component can fail independently of the others.

A simple way to recognise a component boundary: if you can describe what the step does in one sentence, and a different person or team could be responsible for that step failing, it is a component.

Consider a medical triage AI system. It might contain these components:

| Component | Input | What it does | Output |
|---|---|---|---|
| Document intake | Patient record PDF | Extracts structured fields | Name, age, chief complaint |
| Symptom classifier | Chief complaint text | Categorises the symptom type | Symptom category |
| Urgency scorer | Symptom category + age + vitals | Assigns a priority score 1–5 | Urgency score |
| Routing decision | Urgency score | Assigns patient to a care pathway | "Immediate", "Urgent", "Routine" |
| Documentation writer | All fields | Generates a draft clinical note | Clinical note text |

These five components are parts of one system, but they are not interchangeable. Each one can be wrong in its own way. Each one has its own cost of being wrong and its own verifiability. They cannot all be given the same oversight assignment without investigation.

### 5.2 Why Component-Level Thinking Is Necessary

A common mistake in AI oversight design is to assign an oversight level to the entire system. "This is a high-risk system, so humans must be in the loop." That sounds right but is practically useless. If humans must review every step of every AI decision in a system that processes 10,000 cases per day, the oversight becomes impossible to resource — and the result is the automation complacency pattern from topic 10.4: humans are nominally present but cognitively absent.

Component-level thinking solves this by concentrating human oversight where it actually matters. The document intake step in the medical triage example above — checking whether a PDF contains all required fields — can be verified quickly by machine logic. A field is either present or absent. A human checkpoint there adds little value and costs attention. The routing decision — "immediate" versus "routine" — carries the potential for patient harm and is much harder to verify independently. That is where the human checkpoint earns its place.

The formal term for this approach is **risk-tiered component mapping**: the process of assigning each component in a system an oversight level based on its individual risk profile, rather than applying a single blanket policy to the whole system.

Regulatory frameworks recognise this distinction. The EU AI Act Article 14, which sets requirements for human oversight of high-risk AI systems, specifies that oversight mechanisms must be appropriate to the specific risk and function of each component — not uniform across the whole system [1]. This means that even within a system classified as high-risk overall, individual lower-risk components may legitimately run without direct human involvement if their outputs are readily verifiable and errors are reversible.

### 5.3 The Judgment Framework Applied at Component Level

You already know the three Judgment Framework questions from topics 9.7–9.9. At the system level, they told you whether AI-assisted decision-making was appropriate at all. At the component level, they tell you which oversight mode each component needs.

Apply the questions to each component in sequence.

**Q1 applied to a component — What is the cost if this component's output is wrong?**

This question has two sub-dimensions you must evaluate:

- **Severity**: How bad is the consequence for the person affected? A wrong urgency score in a medical system can result in delayed treatment. A wrong categorisation in a document routing system results in a slightly delayed reply. These are not the same.
- **Reversibility**: Can the error be corrected before harm occurs? If the component's output feeds a human who will review it before it becomes final, an error here is correctable. If the component's output directly triggers an irreversible action — a door locks, money moves, a record is permanently flagged — the error is not correctable downstream.

A component is a mandatory checkpoint candidate when either: the severity is high (significant harm to a person), or the reversibility is low (the action cannot be undone). When both are true, the component is a strong mandatory checkpoint candidate.

**Q2 applied to a component — Can a human verify this component's output without re-running the AI?**

This question identifies whether a human checkpoint can actually function as a genuine check. A checkpoint where the human has no realistic way to verify the output is not a genuine check — it is the override-as-theater pattern from topic 10.1.

Verification is practical when the human can:
- Directly inspect the underlying evidence (re-read the document, view the scan, check the raw data).
- Cross-reference against a second source the AI did not use.
- Apply domain expertise that operates independently of the AI's logic.

Verification is impractical when:
- The underlying evidence is too voluminous to inspect in the time available.
- The human would need the AI's own reasoning to make sense of the output.
- The verification step takes as long as re-doing the whole component would.

When verification is impractical, the component needs a structural fix before a checkpoint can be effective — for example, surfacing a confidence score or a human-readable explanation, or reducing the sample to a proportion the human can review fully rather than a large sample reviewed superficially [2].

**Q3 applied to a component — Who is accountable if this component's output causes harm?**

This question identifies who must be named as the decision-maker for this component. If no single human role can be named as accountable for a component's output, the component must not run without a human checkpoint — because diffuse accountability (topic 10.3) means no one will catch or correct systematic errors.

For each component, the answer should be a job title or a named process step, not "the system" or "the vendor." "The clinical director is accountable for the urgency score assigned to patients triaged through this pathway" is a real answer. "The AI vendor is responsible for the routing output" is not — the vendor is responsible for the tool meeting its specification, not for the clinical outcome.

### 5.4 The Signal-Based Upgrade Test

Once a component has been assigned an oversight mode, that assignment is not permanent. Three signals indicate that a component's oversight level needs to be upgraded — moved from HOOTL to HOTL, from HOTL to HITL, or confirmed as HITL with stronger enforcement.

**Signal 1 — The human override rate is near zero**

If a human checkpoint exists and the override rate is near zero, one of two things is true: the AI is extraordinarily accurate for this component, or the checkpoint has become override-as-theater. Without an independent audit confirming the former, the near-zero rate is evidence for the latter. A near-zero override rate is a trigger to investigate the component's checkpoint, not a signal of success.

Production oversight patterns from real AI systems document this consistently: a stable near-zero override rate followed by a documented error is the most common sequence in checkpoint failure case reviews [2]. When the rate is near zero and the component's cost of being wrong is high (Q1 answer), audit the component before concluding it is safe to run at HOTL or HOOTL.

**Signal 2 — The confidence distribution has shifted**

Many AI components produce a confidence score alongside their output — a number indicating how certain the model is. A healthy confidence distribution shows variation: some decisions are high-confidence, some are uncertain, and the checkpoint matrix from topic 10.5 routes the uncertain ones to human review.

When a confidence distribution narrows to near-uniform high confidence, it often signals that the model's uncertainty estimates have become miscalibrated — the model is expressing confidence it has not earned. A component that was routing 15% of its outputs to human review and is now routing 2%, with no change in the underlying inputs, needs to be examined. The narrowing is a candidate upgrade signal.

**Signal 3 — A new context variable has appeared**

Context matters for oversight assignment. The same component can be HOOTL in one context and HITL in another, because the answers to Q1–Q3 depend on context.

For example, an income verification component in a loan system might be assigned HOTL for standard employed applicants (income documents are machine-readable and consistent) and HITL for self-employed applicants with non-standard documentation (the evidence is harder to verify mechanically, and errors carry the same downstream cost). If the system's population of applicants shifts — say, the proportion of self-employed applicants rises from 10% to 40% — the oversight assignment for that component needs to be revisited even though the AI has not changed [3].

Context variables that regularly trigger reassignment include: a change in the user population the system is serving, a change in the domain the system is operating in, a regulatory change that raises the legal standard for a specific type of decision, or new evidence of error correlation with a specific sub-group.

### 5.5 Mandatory Checkpoints vs Optional Checkpoints

Not all human checkpoints are of the same kind. This topic is specifically about **mandatory checkpoints** — defined in policy, required by process, and enforced by workflow design so that the system physically cannot proceed to the next step without human sign-off.

An **optional checkpoint** is one where a human may review but is not required to. Optional checkpoints rely on the human's initiative. They are useful for low-stakes components where checking adds value occasionally. They are insufficient for high-risk components, because automation bias and vigilance decay (topics 9.5, 10.4) reliably erode optional review over time.

The EU AI Act Article 14 requirement is specifically for mandatory checkpoints: the Act requires that natural persons overseeing high-risk AI systems must be able to "understand the capacities and limitations of the high-risk AI system," "detect and address malfunctions or unexpected outcomes," and "decide not to use or disregard the output" — all of which require a checkpoint that is mandatory, not optional [1].

A mandatory checkpoint has four structural properties that distinguish it from an optional one:

1. **Blocking**: the system cannot proceed to the next step without explicit human action (an approval, a logged decision, a confirmed override).
2. **Logged**: every review is recorded with the reviewer's identity, the AI output, the human decision, and the timestamp.
3. **Empowered**: the reviewer has genuine authority to override — no manager approval is required, and overriding is not penalised.
4. **Monitored**: the override rate and review time are tracked and reviewed on a schedule. A rate that drops to near zero triggers an audit, not a celebration.

These properties come from both the EU AI Act Article 14 requirements and from production HITL implementation patterns in real systems [1][2].

### 5.6 Applying This to Your Domain System

The module narrative for this week frames the central question as: "which components in your domain system need a mandatory human checkpoint?" Assessment 3 asks you to answer it for a specific technical system with quantified error thresholds.

The method is a structured walk of every component:

**Step 1 — List every component.**
Write out the chain from input to output. Each step that does something distinct is a component. A list of 4–8 components is typical for a domain-level AI system.

**Step 2 — Apply Q1 to each component.**
What is the worst-case consequence if this component's output is wrong? Assign a severity label — low, medium, high — and note whether the error is reversible or irreversible. Any component labelled high + irreversible is a mandatory checkpoint candidate.

**Step 3 — Apply Q2 to each component.**
Can a human realistically verify this output without re-running the AI? If yes, a checkpoint can function as a genuine check. If no, name the structural change that would make verification practical.

**Step 4 — Apply Q3 to each component.**
Name the human role accountable for this component's output. If you cannot name one, the component cannot run without a mandatory checkpoint.

**Step 5 — Assign the oversight mode.**
Using the checkpoint matrix from topic 10.5, assign each component HITL, HOTL, or HOOTL. For any HITL component, write out all four mandatory checkpoint properties explicitly.

**Step 6 — State the acceptable error threshold.**
For each HITL component, state the maximum error rate that is acceptable given the harm identified in Q1. This is your quantified threshold — the number Assessment 3 Part 2 asks for. Base it on the acceptable error / failure threshold concept from topic 9.10.

**Step 7 — Apply the upgrade test.**
For each component assigned HOTL or HOOTL, write the three signals that would cause you to upgrade it to a higher oversight level. This makes the assignment conditional rather than permanent.

### 5.7 The Acceptable Error Threshold in Practice

A mandatory human checkpoint is not just about whether to review — it is about what standard the component must meet. The acceptable error threshold sets that standard explicitly.

When you set an acceptable error threshold for a component, you are making a concrete claim: "We have decided that this component can be wrong at most X% of the time. Above that rate, a human must review every output." That claim is then verifiable — you can measure the component's actual error rate and compare it to the threshold.

This is what "quantified" means in Assessment 3. The threshold is not "the error rate should be low." It is "the urgency scorer must not misclassify more than 1 in 500 patients as routine when they are actually immediate" — and that number comes from the harm analysis in Q1, combined with the consequences your organisation has determined are acceptable.

Production AI governance frameworks call this the **error budget** for a component: the organisation decides in advance how much error it will accept, and the mandatory checkpoint is triggered when the error rate approaches or exceeds that budget [2].

Regulatory frameworks operationalise this similarly. The EU AI Act requires that high-risk AI systems be designed with defined performance metrics, including accuracy targets, and that human oversight mechanisms be calibrated to those targets [1]. The checkpoint is not just a governance formality — it is the enforcement mechanism for the error budget.

## 6. Implementation

### Worked Example: Identifying Mandatory Checkpoints in an AI Loan Approval System

You studied the AI loan approval case in topic 10.3. Apply the component-level method to it now.

Assume the system has the following pipeline:

| # | Component | What it does |
|---|---|---|
| 1 | Identity verification | Confirms the applicant is who they claim to be |
| 2 | Income verification | Extracts and validates income from uploaded documents |
| 3 | Credit score retrieval | Fetches credit bureau score |
| 4 | Fraud signal detection | Flags patterns associated with fraudulent applications |
| 5 | Risk scoring | Combines all inputs into a single creditworthiness score |
| 6 | Decision output | Translates the score to Approve / Refer / Decline |

Apply the three questions to components 5 and 6, which are the most consequential.

**Component 5 — Risk scoring**

- Q1: Severity is high — someone denied credit they qualify for, or approved for credit they cannot afford. Reversibility is partial — the decision can be appealed, but harm from waiting occurs even if the decision is eventually corrected.
- Q2: Verifiable. The score is produced by combining multiple inputs. A human can examine the individual inputs (income figure, credit score, fraud flags) and form an independent view.
- Q3: The credit officer or underwriting manager should be named. If the answer is "the model," that is a governance failure.
- Assignment: **HITL** for all applications where the risk score falls within a defined margin of the decision threshold (for example, within 15 points of the Refer/Decline boundary). **HOTL** for scores far above the Approve threshold or far below the Decline threshold.
- Acceptable error threshold: "The risk scorer must not misclassify more than 2 in 1,000 applications that are genuinely creditworthy as Decline."

**Component 6 — Decision output**

- Q1: Severity is high — an incorrect Decline carries legal obligations under financial services regulation. Reversibility is low — the decision is the final output; errors must be caught here or not at all.
- Q2: Verifiable only if the risk score from component 5 was reviewed. The decision is a direct translation of that score. The checkpoint here is most valuable as a final confirmation that the score-to-decision mapping was applied correctly.
- Q3: The named credit officer who approved the component 5 review should also own this decision.
- Assignment: **HITL** for any application referred to human review at component 5. **HOOTL** for applications where component 5 produced a clear Approve with no fraud flags — the human has already validated the underlying risk score.

This example illustrates a principle: **mandatory checkpoints concentrate at decision boundaries**, not uniformly across every step. Components 1–3 can run at HOTL or HOOTL for standard cases, with HITL triggered only when documents are non-standard or a fraud flag is raised.

## 7. Real-World Patterns

### 7.1 The EU AI Act Article 14 Standard

The EU AI Act's Article 14 sets out the minimum design requirements for human oversight of high-risk AI systems [1]. It is the most specific regulatory benchmark currently available for what a mandatory checkpoint must look like.

Article 14 requires that the natural persons overseeing high-risk AI systems be able to:

- Fully understand what the system is doing and what its limitations are.
- Monitor the system's operation in real time.
- Detect and address unexpected outputs or malfunctions.
- Intervene, correct, or halt the system.
- Decide not to use the system's output.

The Article 14 language maps directly onto the four mandatory checkpoint properties from section 5.5. "Decide not to use the output" is the empowerment property. "Intervene and correct" is the blocking property. "Monitor in real time" implies logging with sufficient detail for meaningful review. The enforcement timelines in the EU AI Act — phased in from 2024 through 2027 — mean that many AI systems currently in production in Europe are already subject to these requirements or will be within the near term [1].

For Assessment 3, the EU AI Act framework provides a ready-made reference: if your domain system operates in a regulated context (healthcare, financial services, education) in the EU, the Article 14 standard is a real design constraint.

### 7.2 Where Production Systems Place Mandatory Checkpoints

In production AI systems, mandatory checkpoints are placed at specific architectural locations that correspond to the component categories identified by the component-level method [2][3]:

**At chain boundaries**: the point where one AI component's output becomes another component's input. If both components are high-stakes, the boundary between them is a natural checkpoint location — a human can inspect the handoff without needing to understand the internal logic of either component [2].

**Before irreversible actions**: any action that cannot be undone without additional work (sending a notification to an affected person, writing to a permanent record, executing a financial transaction) is preceded by a mandatory checkpoint. This is consistent with the reversibility dimension of Q1.

**At the decision threshold**: the boundary between two outcome categories (Approve/Decline, Admit/Reject, Immediate/Routine) is where errors have the largest impact on affected people. Production HITL patterns place mandatory review at cases that fall within a defined margin of the threshold, with autonomous processing at cases far from it [2].

**At sub-group audit triggers**: when a component's output is known to vary by demographic sub-group — for example, if an urgency scorer performs differently for patients from different age groups — mandatory checkpoints are placed at cases that belong to the sub-group where the model's accuracy is lower [3].

These placement patterns are not arbitrary. They reflect the answers to Q1–Q3 applied at scale. A production system with 50,000 decisions per day cannot have 50,000 mandatory human reviews. The checkpoint placement method concentrates human oversight at the components and cases where it adds the most value.

### 7.3 When the Same Component Needs Different Oversight in Different Contexts

A recurring finding in production HITL oversight documentation is that the correct oversight level for a component is not fixed — it depends on context [3].

The income verification component in a loan system is a useful example. For an applicant who submits a single employer's payslip in a standard format, the verification is mechanically straightforward and a HOTL assignment may be appropriate. For a self-employed applicant submitting a combination of invoices, tax returns, and bank statements across multiple currencies, the same component is performing a much more difficult task — and a HITL assignment is appropriate for that context.

The system has not changed. The AI model has not changed. What has changed is the complexity of the input, which changes the answer to Q2 (can a human verify this?) and sometimes the answer to Q1 (is the error rate higher for this input type?).

Production deployment documentation distinguishes between the **baseline oversight assignment** (the mode applied to most cases) and the **triggered oversight assignment** (the mode applied when a context variable is detected) [3]. The checkpoint matrix from topic 10.5 can be extended with context-triggered rules: "If [context variable is present], apply [triggered mode] instead of [baseline mode]."

## 8. Best Practices

### Mandatory Checkpoint Design Rules

**Do:**

- Apply the component-level method before assigning any oversight mode. Blanket system-level assignments produce over-review in low-risk areas and under-review in high-risk ones.
- Write the acceptable error threshold explicitly for every component assigned HITL. A threshold without a number is not a threshold — it is a feeling.
- Make mandatory checkpoints blocking by design: the system should be architecturally incapable of proceeding without human sign-off at a HITL component. Relying on humans to voluntarily stop and review is an optional checkpoint, not a mandatory one.
- Log every checkpoint review. The log is the evidence that the checkpoint functioned, and it is the data source for override rate monitoring that detects vigilance decay over time.
- State the upgrade signals explicitly for every component assigned HOTL or HOOTL. An oversight assignment with no stated upgrade conditions will never be revised, even when it should be.
- Cross-reference your component assignments against the EU AI Act Article 14 requirements [1] if your system operates in a regulated domain.

**Do not:**

- Treat a near-zero override rate as evidence that a checkpoint is unnecessary. Investigate it before drawing that conclusion.
- Assign HOOTL to a component solely on the grounds that "the AI is accurate." Accuracy warrants HOTL (a human can audit a sample). HOOTL is appropriate only when Q1 severity is low, the error is reversible, and accountability is maintained by other means.
- Write a checkpoint into a governance document and assume it will function without monitoring. Checkpoints that are not measured decay into override-as-theater.
- Assign the same oversight level to all components of a high-risk system. High-risk classification applies to the system overall. Oversight assignment applies to each component individually.
- Retrofit checkpoints after deployment. Post-deployment oversight design is harder to enforce because the workflow has already been built without it [1].

### The Anti-Pattern: System-Level Blanket Policy

The most common oversight design failure is the **system-level blanket policy**: "This is a high-risk system — all outputs must be reviewed by a human before they are acted on." This sounds rigorous. In practice, if the system produces 500 outputs per day and a human must review every one, the review quickly becomes superficial. Reviewers process outputs rapidly, override almost nothing, and the checkpoint becomes override-as-theater at scale.

The fix is the component-level method: identify which components need HITL (mandatory, blocking, logged), which need HOTL (monitored, audited on a sample), and which can run HOOTL. Concentrate human attention on the components where it earns its cost.

## 9. Hands-On Exercise

**Component Mapping Exercise**

Choose an AI system from your domain — or use the medical triage system from the Core Concepts section if you do not yet have a domain system in mind.

1. List 4–6 components of the system. One sentence per component: what goes in, what comes out.
2. For each component, answer Q1, Q2, and Q3 in two to three sentences each.
3. Assign each component an oversight mode (HITL, HOTL, HOOTL) and state the reason in one sentence.
4. For the component you assigned HITL, write the acceptable error threshold as a number: "This component must not produce more than ___ wrong outputs per ___ decisions."
5. For each component you assigned HOTL or HOOTL, state one context variable whose presence would trigger an upgrade to a higher oversight mode.

This exercise is the direct preparation for Assessment 3 Part 2.

## 10. Key Takeaways

- A system is a chain of components. Different components carry different risk levels. Assigning a single oversight mode to the whole system produces both over-review (wasted human attention in low-risk areas) and under-review (genuine risks missed in high-risk ones).
- The Judgment Framework questions (Q1, Q2, Q3) applied at component level produce a defensible, evidence-grounded oversight assignment for each step — not a gut feeling about the system overall.
- **Risk-tiered component mapping** is the structured process: list components, apply Q1–Q3, assign HITL/HOTL/HOOTL, state the acceptable error threshold for HITL components, and write the upgrade signals for HOTL and HOOTL ones.
- A mandatory checkpoint is blocking, logged, empowered, and monitored. These four properties distinguish a genuine checkpoint from override-as-theater. The EU AI Act Article 14 requirement formalises these properties as a regulatory minimum for high-risk AI systems.
- Oversight assignments are not permanent. Three signals trigger an upgrade review: a near-zero override rate, a narrowing confidence distribution, and a shift in context variables. Writing these signals down in advance converts a static governance document into a living oversight design.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
