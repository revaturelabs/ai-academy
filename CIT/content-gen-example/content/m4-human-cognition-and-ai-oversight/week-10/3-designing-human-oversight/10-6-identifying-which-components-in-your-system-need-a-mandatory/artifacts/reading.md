<!-- nav:top:start -->
[⬅ Previous: 10.5 — Designing human-in-the-loop checkpoints](../../10-5-designing-human-in-the-loop-checkpoints-when-to-require-sign/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 10.7 — Writing a post-mortem ➡](../../../4-post-mortem-writing/10-7-writing-a-post-mortem-what-failed-why-who-was-accountable-wh/artifacts/reading.md)
<!-- nav:top:end -->

---

# Identifying Which Components in Your System Need a Mandatory Human Checkpoint

## Overview

A real AI system is not a single decision — it is a chain of steps, each doing something different, each capable of failing in its own way. Deciding that "a human must oversee this system" is not enough. You need to know *which steps* need a human checkpoint and *why*. This topic gives you a structured, step-by-step method for making that decision for every component in a chain — producing a defensible answer, not a gut feeling.

## Key Concepts

### What Is a Component?

Imagine an AI system as an assembly line. Each station on the line does one job. A component is one of those stations.

**Component** — a distinct step in an AI system's processing chain that takes a defined input, applies a specific operation, and produces an output that feeds the next step.

A simple test: if you can describe what a step does in one sentence, and a different person could be responsible if that step fails, it is a component.

Here is how a medical triage AI breaks into components:

| Component | What it does | Output |
|---|---|---|
| Document intake | Reads patient record PDF and pulls out key fields | Name, age, chief complaint |
| Symptom classifier | Labels the symptom type from the complaint text | Symptom category |
| Urgency scorer | Assigns a priority score from 1 to 5 | Urgency score |
| Routing decision | Maps the score to a care pathway | "Immediate", "Urgent", or "Routine" |
| Documentation writer | Drafts a clinical note from all the fields | Clinical note text |

These five components are parts of one system, but they are not equal. Each can be wrong in a different way. Each carries a different cost of being wrong.

### Why Component-Level Thinking Beats a Blanket Policy

A common mistake is to assign one oversight level to the whole system. "This is a high-risk system — every output must be reviewed by a human." That sounds rigorous. In practice it is not.

Why does this matter? Because if a system produces 500 outputs per day and a human must review every one, the reviews quickly become superficial. Reviewers stop looking carefully. They override almost nothing. The checkpoint becomes what you learned in topic 10.1: **override-as-theater** — a human is nominally present but cognitively absent. This is the automation complacency pattern from topic 10.4 happening at scale.

**Risk-tiered component mapping** — the process of assigning each component its own oversight level based on its individual risk profile, rather than applying a single policy to the whole system — solves this by concentrating human attention where it earns its cost.

Regulatory frameworks recognise this. EU AI Act Article 14 specifies that oversight mechanisms must be appropriate to the specific risk and function of each component — not uniform across the whole system [1]. Even within a high-risk system, lower-risk components may legitimately run without direct human involvement if their errors are easily caught and reversed.

### The Judgment Framework Applied to Each Component

You already know the three Judgment Framework questions from topics 9.7–9.9. You used them to decide whether a system needed human oversight at all. Now you apply them one component at a time.

**Q1 — What is the cost if this component's output is wrong?**

This question has two parts:

- **Severity**: How harmful is the consequence to the person affected? A wrong urgency score in a medical system can delay treatment. A wrong category in a document routing system delays a reply. These are not the same level of harm.
- **Reversibility**: Can the error be corrected before harm occurs? If a human reviews the output before any action is taken, the error is correctable. If the output directly triggers an irreversible action — money moves, a record is permanently flagged, a door locks — the error cannot be undone downstream.

A component is a mandatory checkpoint candidate when severity is high, or reversibility is low. When both are true, the case for a mandatory checkpoint is strong.

**Q2 — Can a human verify this component's output without re-running the AI?**

This question checks whether a human checkpoint can function as a genuine check. A checkpoint where the reviewer has no realistic way to verify the output is not a check — it is theater.

Verification is practical when the human can:
- Directly inspect the underlying evidence (re-read the document, check the raw data).
- Cross-reference a second source the AI did not use.
- Apply domain expertise that is independent of the AI's logic.

Verification is impractical when the evidence is too large to inspect in the time available, or when the human would need the AI's own reasoning to make sense of the output [2]. When verification is impractical, the component needs a structural fix first — for example, surfacing a confidence score or a plain-language explanation — before a checkpoint can function.

**Q3 — Who is accountable if this component's output causes harm?**

Name a job title, not a system. "The clinical director is accountable for urgency scores assigned on this pathway" is a real answer. "The AI vendor is responsible" is not. The vendor is accountable for the tool meeting its specification — not for the clinical outcome.

If no single human role can be named as accountable, the component must not run without a mandatory checkpoint. Diffuse accountability — where everyone and no one is responsible — is the pattern from topic 10.3 that lets systematic errors go uncorrected.

![Risk-Tiered Component Mapping](./diagram.png)
*The diagram shows how each component moves through the Q1, Q2, and Q3 gates to reach a HITL, HOTL, or HOOTL assignment, and which signals trigger an upgrade.*

### The 7-Step Risk-Tiered Component Mapping Method

Apply these steps to every component in your system. This is the engine for producing a defensible component map.

1. **List every component.** Write out the chain from input to output. Each step that does something distinct is one component. Four to eight components is typical for a domain-level AI system.

2. **Apply Q1 to each component.** What is the worst-case consequence if this component's output is wrong? Assign a severity label — low, medium, or high — and note whether the error is reversible or irreversible. Any component labelled high + irreversible is a mandatory checkpoint candidate.

3. **Apply Q2 to each component.** Can a human realistically verify this output without re-running the AI? If yes, a checkpoint can function as a genuine check. If no, name the structural change that would make verification practical.

4. **Apply Q3 to each component.** Name the human role accountable for this component's output. If you cannot name one, the component must have a mandatory checkpoint.

5. **Assign the oversight mode.** Using the checkpoint matrix from topic 10.5, assign each component HITL (Human-in-the-Loop), HOTL (Human-on-the-Loop), or HOOTL (Human-out-of-the-Loop). For any HITL component, write out all four mandatory checkpoint properties explicitly (see below).

6. **State the acceptable error threshold.** For each HITL component, state the maximum error rate that is acceptable given the harm identified in Q1. This is the quantified threshold — a concrete number, not a feeling. It comes from the acceptable error / failure threshold concept you learned in topic 9.10.

7. **Apply the upgrade test.** For each component assigned HOTL or HOOTL, write the three signals that would cause you to upgrade it to a higher oversight level. This makes the assignment conditional rather than permanent.

### Mandatory vs Optional Checkpoints

Not all checkpoints are the same kind. This topic is about **mandatory checkpoints** — defined in policy, required by process, and enforced so the system cannot proceed without human sign-off.

An **optional checkpoint** is one where a human may review but is not required to. Optional checkpoints rely on the reviewer's initiative. They are insufficient for high-risk components because automation bias and vigilance decay — covered in topics 9.5 and 10.4 — reliably erode optional review over time [2].

A mandatory checkpoint has four structural properties that distinguish it from an optional one:

| Property | What it means |
|---|---|
| **Blocking** | The system cannot proceed to the next step without explicit human action — an approval, a logged decision, or a confirmed override. |
| **Logged** | Every review is recorded: who reviewed, what the AI output was, what the human decided, and when. |
| **Empowered** | The reviewer has genuine authority to override. No manager approval is needed. Overriding is not penalised. |
| **Monitored** | The override rate and review time are tracked on a schedule. A rate that drops to near zero triggers an audit, not a celebration. |

The EU AI Act Article 14 maps directly onto these four properties. "Decide not to use the output" is the empowerment property. "Intervene and correct" is the blocking property. "Monitor in real time" requires logging in sufficient detail for meaningful review [1].

### Upgrade Signals: When to Revisit an Assignment

An oversight assignment is not permanent. Three signals indicate that a component's oversight level needs to be upgraded [2][3]:

**Signal 1 — The human override rate is near zero.** If a checkpoint exists and overrides are near zero, one of two things is true: the AI is extraordinarily accurate, or the checkpoint has become theater. Without an independent audit confirming the former, near-zero is evidence for the latter.

**Signal 2 — The confidence distribution has narrowed.** Many AI components produce a confidence score alongside their output. A healthy distribution shows variation — some decisions are uncertain, and those get routed to human review. When the distribution narrows to near-uniform high confidence, the model's uncertainty estimates may have become miscalibrated. A component routing 15% of its outputs to human review that now routes 2%, with no change in inputs, needs examination.

**Signal 3 — A new context variable has appeared.** The same component can require different oversight in different contexts because the answers to Q1–Q3 depend on context. An income verification component might be HOTL for standard employed applicants — documents are machine-readable and consistent — and HITL for self-employed applicants with non-standard records, where the evidence is harder to verify and errors carry the same downstream cost [3]. If the proportion of self-employed applicants rises from 10% to 40%, the oversight assignment needs revisiting even though the AI has not changed.

## Worked Example

The AI loan approval system from topic 10.3 had six components. Apply the 7-step method to the two most consequential ones.

**The pipeline:**

| # | Component | What it does |
|---|---|---|
| 1 | Identity verification | Confirms the applicant is who they claim to be |
| 2 | Income verification | Extracts and validates income from uploaded documents |
| 3 | Credit score retrieval | Fetches the credit bureau score |
| 4 | Fraud signal detection | Flags patterns associated with fraudulent applications |
| 5 | Risk scoring | Combines all inputs into a single creditworthiness score |
| 6 | Decision output | Translates the score to Approve / Refer / Decline |

**Component 5 — Risk scoring**

- **Q1:** Severity is high. Someone denied credit they qualify for, or approved for credit they cannot afford, suffers real financial harm. Reversibility is partial — an appeal can correct the decision, but harm from waiting occurs even if it is eventually reversed.
- **Q2:** Verifiable. A human can examine the individual inputs — income figure, credit score, fraud flags — and form an independent view of whether the combined score is reasonable.
- **Q3:** The credit officer or underwriting manager. "The model" is not an accountable role.
- **Assignment:** HITL for applications where the risk score falls within 15 points of the Refer/Decline boundary. HOTL for scores far above the Approve threshold or far below the Decline threshold.
- **Acceptable error threshold:** The risk scorer must not misclassify more than 2 in every 1,000 creditworthy applications as Decline.

**Component 6 — Decision output**

- **Q1:** Severity is high. An incorrect Decline carries legal obligations under financial services regulation. Reversibility is low — this is the final output; errors must be caught here or not at all.
- **Q2:** Verifiable only if the risk score from component 5 was already reviewed. The decision is a direct translation of that score.
- **Q3:** The same named credit officer who approved the component 5 review.
- **Assignment:** HITL for any application referred to human review at component 5. HOOTL for applications where component 5 produced a clear Approve with no fraud flags — the underlying risk score has already been validated by a human.

This example shows the core principle: **mandatory checkpoints concentrate at decision boundaries** — not uniformly across every step. Components 1–3 can run at HOTL or HOOTL for standard cases, with HITL triggered only when documents are non-standard or a fraud flag is raised.

## In Practice

Here is where the component-level method shows up — and where system-level blanket policies break down:

- **At chain boundaries:** where one component's output becomes another's input, a human can inspect the handoff without understanding the internal logic of either component [2].
- **Before irreversible actions:** any action that cannot be undone — sending a notification, writing to a permanent record, executing a financial transaction — is preceded by a mandatory checkpoint.
- **At the decision threshold:** the boundary between two outcome categories (Approve/Decline, Admit/Reject, Immediate/Routine) is where errors have the largest impact. Mandatory review concentrates on cases near the threshold; autonomous processing handles cases far from it [2].

**Do:**
- Apply the 7-step method before assigning any oversight mode. Blanket assignments produce over-review in low-risk areas and under-review in high-risk ones.
- Write the acceptable error threshold explicitly for every HITL component. A threshold without a number is a feeling, not a threshold.
- Make mandatory checkpoints blocking by design. Relying on humans to voluntarily stop and review is an optional checkpoint, not a mandatory one.
- Log every checkpoint review. The log is the evidence that the checkpoint functioned, and the data source for detecting vigilance decay [1].
- Write upgrade signals explicitly for every HOTL or HOOTL assignment. An assignment with no stated upgrade conditions will never be revised, even when it should be.

**Do not:**
- Treat a near-zero override rate as evidence that a checkpoint is unnecessary — investigate it first.
- Assign HOOTL solely because "the AI is accurate." Accuracy warrants HOTL. HOOTL is appropriate only when Q1 severity is low, the error is reversible, and accountability is maintained by other means.
- Retrofit checkpoints after deployment. Post-deployment oversight design is harder to enforce because the workflow has already been built without it [1].

## Key Takeaways

- A system is a chain of components. Different components carry different risk levels. A single oversight mode applied to the whole system produces over-review in low-risk areas and under-review in high-risk ones.
- The Judgment Framework questions — Q1 (cost of being wrong), Q2 (can a human verify this?), Q3 (who is accountable?) — applied at component level produce a defensible oversight assignment for each step.
- **Risk-tiered component mapping** is the 7-step structured process: list components, apply Q1–Q3, assign HITL/HOTL/HOOTL, state the acceptable error threshold for HITL components, and write upgrade signals for HOTL and HOOTL assignments.
- A mandatory checkpoint is blocking, logged, empowered, and monitored. These four properties distinguish a genuine checkpoint from override-as-theater, and they are the minimum standard the EU AI Act Article 14 requires for high-risk AI systems.
- Oversight assignments are not permanent. Three signals trigger an upgrade review: a near-zero override rate, a narrowing confidence distribution, and a shift in context variables. Writing these signals down in advance turns a static document into a living oversight design.

## References

1. AI Governance Desk, "Human-in-the-Loop Oversight Frameworks in AI Governance." <https://aigovernancedesk.com/human-in-the-loop-oversight-frameworks-ai-governance/>
2. Redis, "AI Human in the Loop." <https://redis.io/blog/ai-human-in-the-loop/>
3. Galileo, "Human-in-the-Loop Agent Oversight." <https://galileo.ai/blog/human-in-the-loop-agent-oversight>

---
<!-- nav:bottom:start -->
[⬅ Previous: 10.5 — Designing human-in-the-loop checkpoints](../../10-5-designing-human-in-the-loop-checkpoints-when-to-require-sign/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 10.7 — Writing a post-mortem ➡](../../../4-post-mortem-writing/10-7-writing-a-post-mortem-what-failed-why-who-was-accountable-wh/artifacts/reading.md)
<!-- nav:bottom:end -->
