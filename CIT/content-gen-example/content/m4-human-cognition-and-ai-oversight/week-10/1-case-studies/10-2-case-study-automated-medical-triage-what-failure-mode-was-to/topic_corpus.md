---
topic_id: "10.2"
title: "Case study: Automated medical triage — what failure mode was tolerated?"
position_in_module: 2
generated_at: "2026-06-12T00:00:00Z"
resource_count: 3
---

# 1. Case study: Automated medical triage — what failure mode was tolerated? — Topic Corpus

## 2. Prerequisites

This topic builds directly on the following prior topics. Each concept is reused here without re-definition — revisit the listed topic if anything feels unfamiliar before continuing.

- **9.5 — Automation bias**: the tendency to trust automated outputs even when your own judgment raises doubt.
- **9.7 — Judgment Framework Q1**: What is the cost of a wrong output? Used here to assess the stakes of a mis-scored patient.
- **9.8 — Judgment Framework Q2**: Is the model's error visible before harm occurs? Used here to examine why triage errors are invisible until it is too late.
- **9.9 — Judgment Framework Q3**: Is there a genuine human in the loop? Used here to test whether the clinician's override role was real or theatrical.
- **9.11 — High-stakes domains where AI must not have the final word**: the principle that in life-or-death settings, a human must remain accountable for the final decision.
- **10.1 — Holistic review, pipeline, human override point, override as theater, calibration, holistic review collapse, training data**: the vocabulary for how a triage pipeline is structured and where human involvement can become hollow.

## 3. Learning Objectives

By the end of this topic you should be able to:

1. Describe what an AI-assisted medical triage system does and what decision it makes.
2. Identify the specific failure mode that was tolerated in real-world triage deployments and explain what made it systematic rather than random.
3. Explain why that failure mode persisted — naming the governance gaps and the cognitive bias that compounded them.
4. Apply the Judgment Framework (Q1, Q2, Q3) to the triage case and state what each question reveals about where the system fell short.
5. Name at least two concrete governance controls that would have caught the failure before harm accumulated, and explain how each one works.
6. Use the six-step diagnostic procedure from this topic to analyse any AI system for a tolerated failure mode.

## 4. Introduction

Picture a hospital emergency department at 11 pm on a Friday. Forty patients are waiting. The triage nurse has been on shift for eight hours. A new patient walks in, breathing fast, chest tight, telling the nurse she "just feels off." The nurse types the patient's details into the triage system. The system outputs: **priority 3 — non-urgent**. The nurse is tired. The queue is long. She accepts the score and directs the patient to the non-urgent waiting area.

Two hours later, the patient is rushed to intensive care with a cardiac event.

Was that a freak accident? Or was there a pattern — dozens of patients like her, over months, all scored too low, all waiting too long?

This is the question this topic is built around. Not whether the AI system ever made a mistake — every system does — but whether the pattern of mistakes was known, or knowable, and tolerated anyway.

Peer-reviewed evidence from real-world AI triage deployments answers that question directly: yes, systematic failure modes existed, yes, they were detectable with available data, and yes, they persisted because of compounding governance gaps and a cognitive bias you already know — automation bias [1]. The organisations did not fail because they had bad people. They failed because they had a pipeline with no checkpoint designed to catch that specific kind of failure.

By the end of this topic you will be able to name the failure mode precisely, explain why four specific governance gaps let it persist, apply the Judgment Framework to show what was missing, and name the control that would have caught it earliest.

Why does this matter right now? Because this week's lab asks you to apply exactly this analysis to your own domain system — and Assessment 3 is due this week. This topic gives you the analytical template.

## 5. Core Concepts

### 5.1 What is automated medical triage?

**Triage** — from the French word meaning "to sort" — is the process of quickly assessing patients and ranking them by urgency. It is the first decision a hospital makes about you when you arrive at an emergency department: should you be seen immediately, or can you wait?

Traditionally, a trained nurse does this by asking questions, observing your appearance, checking your vital signs (heart rate, blood pressure, temperature, oxygen level), and assigning a score on a standardised scale. It is fast, but it depends on the individual nurse's experience and can vary across shifts and nurses.

**AI-assisted triage** (AI-supported triage) replaces or supplements that initial scoring step with a machine learning model. Here is how it works at a high level:

1. The patient's data — age, reported symptoms, vital signs, past diagnoses — is entered into the system.
2. The model, trained on thousands of historical patient records, compares the new patient's data to patterns it learned from similar past cases.
3. The model outputs a priority score: for example, 1 (critical), 2 (urgent), 3 (non-urgent).
4. That score enters the **pipeline** (topic 10.1) — the chain of steps that determines queue position, and therefore when the patient sees a doctor.

The AI does not diagnose the patient. It decides how long the patient can safely wait. That is a narrower task than full diagnosis, but it is still a consequential one. Getting it wrong by even one priority level can mean a one-hour delay versus a six-hour delay — and in some conditions, that gap is fatal.

### 5.2 The failure mode: systematic under-scoring

A **failure mode** is a specific, repeatable way a system produces wrong outputs. The keyword is "repeatable." A single wrong score is a one-off error. A failure mode is a pattern — the same kind of wrong output happening again and again under the same conditions.

The failure mode documented in real-world AI triage systems is **systematic under-scoring of specific patient groups** [1]. The model assigns priority scores that are too low — telling the queue "this patient can wait" when clinical signs indicate otherwise. This is not distributed randomly across all patients. It concentrates in identifiable groups:

- **Elderly patients**: models trained on data where younger patients more frequently received high-urgency labels learn to associate "elderly" with lower urgency — even when the clinical presentation is serious [1].
- **Patients using non-standard symptom language**: models trained on text descriptions learn from the phrasing patterns most common in their training data. A patient who describes chest tightness as "my heart feels heavy" rather than "chest pain" may be scored lower because the exact phrase is less frequent in the training corpus [3].
- **Night-shift patients**: data quality from night shifts is often lower — incomplete vital signs, faster entry, fewer recorded observations. Models trained on incomplete data learn to treat night-shift inputs with less confidence, producing more conservative (lower) scores [1].

Why does this matter? Because systematic under-scoring means the harm is not spread randomly — it falls disproportionately on patients who are already vulnerable. And because it is systematic, it compounds: the model is wrong in the same direction, for the same groups, day after day, month after month [2].

### 5.3 Why "tolerated"? What that word means in this context

Saying the failure mode was "tolerated" does not mean the hospital staff were indifferent to patient welfare. It means the failure mode persisted inside the organisation without being corrected, even though the conditions to detect it existed.

"Tolerated" can happen in three ways:

1. **Deliberately accepted**: leaders knew about the problem and decided it was not worth fixing. This is rare and usually the last explanation to reach for.
2. **Unknowingly sustained**: nobody looked for the problem in the right place, so it was never seen. This is the most common form.
3. **Seen but dismissed**: individual clinicians noticed something was off but lacked the authority, the data, or the organisational channel to escalate it. This is the hardest to surface and the most damaging to morale.

The evidence from real triage deployments shows all three forms, but (2) and (3) dominate [1][3]. The organisations had data that would have revealed the pattern. They simply did not run the analysis that would have shown it — because no one was assigned the job of running it.

### 5.4 The four governance gaps

A **governance gap** is a missing rule, role, or process that an organisation should have in place to catch a problem. Four gaps are documented consistently across real triage deployments [1][2][3].

**Gap 1 — Evaluation design**

The system was evaluated on overall accuracy: "How often does the AI's score match the eventual clinical outcome, across all patients?" This number can look acceptable — say, 87% accuracy — even when the model is significantly worse for a specific sub-group. If elderly patients are scored correctly only 70% of the time but younger patients are scored correctly 92% of the time, the overall number hides the elderly patients' experience entirely.

The missing piece is **sub-group evaluation**: breaking the accuracy number down by patient category from day one of deployment [3]. Without it, the aggregate metric acts as a cover.

**Gap 2 — Checkpoint frequency**

Most triage AI systems were certified once — before deployment — and then treated as permanently approved. There was no scheduled post-deployment audit to ask: "Is the model still performing the way it did at certification? Has drift occurred?"

You know from topic 10.1 that **calibration** is the process of checking whether a model's outputs still match reality over time. Models drift because the real world changes: patient demographics shift, symptom language evolves, data entry practices change. A model that was accurate at launch can degrade within months without a scheduled check to catch it [1].

**Gap 3 — Override accountability**

In the pipeline, the clinician nominally had the power to override the AI's score. In practice, under time pressure and high volume, override became what topic 10.1 calls **override as theater**: the human is formally present in the loop but functionally rubber-stamps the AI output.

Override decisions were typically not logged with a reason. No one tracked how often overrides happened or what patterns they showed. There was no feedback loop from "nurse overrode the score" to "the AI's original score was reviewed." This meant the system received no signal that its scores were being questioned — and the organisation had no data to show that overrides were systematically concentrated in the patient groups the model was under-scoring [2].

**Gap 4 — Alert thresholds**

When a patient who had been scored "non-urgent" deteriorated in the waiting room — a clinical event called "waiting-room deterioration" — that event was not automatically linked back to the AI's original score. There was no alert of the form: "Patient scored 3 by AI, deteriorated within 90 minutes, clinical outcome classified as urgent — AI score review triggered."

Without that feedback loop, each deterioration event was treated as a one-off clinical situation, not as evidence of a model failure. The signal existed in the data. The system had no mechanism to surface it [2].

### 5.5 How automation bias amplified the gaps

You know from topic 9.5 that **automation bias** is the tendency to accept an automated output as correct, even when your own knowledge or observation suggests otherwise. It is not laziness or incompetence — it is a predictable feature of how the human brain responds to authoritative-looking system outputs.

In the triage context, automation bias worked like this:

- A nurse looked at a patient and thought "she looks more distressed than a priority 3." But the screen said "priority 3." The nurse was uncertain. The screen was certain. The nurse went with the screen.
- A doctor reviewed a patient who had waited three hours and asked "why was this patient scored non-urgent?" The answer was "the AI said so." The doctor accepted that explanation and moved on.
- A department manager noticed a small uptick in waiting-room deteriorations over a month. But the AI vendor's dashboard showed 87% accuracy. The manager concluded the deteriorations were random variation, not a pattern.

Each of these is automation bias. And each of them, individually, seems reasonable — the person trusted a system with more data than they had access to in the moment. The problem is that the system itself had a flaw, and automation bias meant the human at each step provided no corrective signal. Over months, these small acceptances accumulated into a long run of harm that nobody had individually chosen [1].

### 5.6 Applying the Judgment Framework

The Judgment Framework from topics 9.7–9.9 gives you three questions. Applied to the triage case:

**Q1 — What is the cost of a wrong output?**

A wrong triage score delays a patient's care. For time-sensitive conditions — cardiac events, strokes, sepsis, internal bleeding — a delay of one to three hours can lead to permanent harm or death. The cost is severe, irreversible, and falls entirely on a patient who had no say in the matter.

**Q2 — Is the model's error visible before the harm occurs?**

No. The patient is scored, sent to the non-urgent waiting area, and begins to deteriorate there. The queue management system sees only queue positions, not the patient's changing condition. By the time the error becomes visible — a nurse or another patient raises the alarm — the queue delay has already occurred. The error is invisible until after the harm [1].

**Q3 — Is there a genuine human in the loop who can catch this before harm occurs?**

Nominally yes. A nurse accepts or overrides the score. But the conditions of the work — high volume, time pressure, automation bias, no logging of override reasons — mean the override is theater, not a genuine checkpoint. In practice, the AI held the final say [1][2].

What does the Judgment Framework tell you? All three answers point the same direction: this is exactly the scenario where AI must not hold final authority. The cost is high and irreversible (Q1). The error is invisible before harm (Q2). The human checkpoint is theater rather than genuine review (Q3). The Framework does not say "AI should not be used in triage" — it says "AI must not be the last word for high-acuity patients without a functioning human override mechanism."

### 5.7 The governance control that would have caught it earliest

Two controls are cited across the evidence as the ones that would have surfaced the failure mode soonest.

**Control 1 — Sub-group performance audit (scheduled, recurring)**

A sub-group performance audit is a scheduled review — monthly, for example — that computes the model's accuracy separately for each patient category the organisation cares about: age bands, shift (day/night), primary language, and symptom entry method [3].

This is not a complex analysis. It requires only that the organisation (a) log which patients were scored by the AI, (b) log the eventual clinical outcome, and (c) run a comparison. The data was there in every deployment that failed. The analysis was not [3].

A sub-group audit would have shown — within one to three months of deployment — that elderly patients were being under-scored at a rate significantly above the system average. That finding would have triggered a review. The review would have revealed the model's training data bias. The bias would have been corrected before it accumulated into mass harm.

**Control 2 — Deterioration-contradiction alert (automated)**

A deterioration-contradiction alert is a software rule: when a patient who was scored "non-urgent" or "priority 3" clinically deteriorates within a defined window (say, 120 minutes of being assigned to the non-urgent queue), an alert is generated that flags the original AI score for review [2].

Over dozens of such events, a pattern becomes statistically clear. If elderly patients account for 60% of deterioration-contradiction alerts while comprising only 25% of the non-urgent queue, the model's failure mode is visible without anyone having to look for it — the data surfaces it automatically.

Both controls share a common requirement: **someone accountable for the pipeline as a whole** — not just for their step inside it. This is the governance gap behind the governance gaps. In the organisations that tolerated the failure mode, no individual role was assigned the question "is this system causing harm across its full output distribution?" That question was everyone's and no one's, which is the same as no one's [1].

## 6. Implementation

Use this six-step procedure to analyse any AI system for a tolerated failure mode. It is the template for your lab post-mortem and for Assessment 3.

1. **Describe the system's decision in one sentence.** "The system reads [inputs] and outputs [decision], which causes [consequence] to happen." For triage: "The system reads patient vitals and symptoms and outputs a priority score, which determines how long the patient waits."

2. **Name the failure mode precisely.** Not "it made errors" but the specific pattern. For triage: "It systematically under-scored elderly patients and patients whose symptoms were entered in non-standard language."

3. **Ask: was the failure visible with existing data?** Could the organisation have detected it by analysing data they already had? If yes — and no one did — that is a failure of evaluation design, not a failure of data availability.

4. **Apply Q1/Q2/Q3 from the Judgment Framework.**
   - Q1: What is the cost of a wrong output? (Reversible or irreversible? Individual or systemic?)
   - Q2: Is the error visible before harm? (Or only after?)
   - Q3: Is there a genuine human checkpoint, or is override theater?

5. **Identify the governance gap.** Choose from: (a) evaluation design — wrong metric or no sub-group breakdown; (b) checkpoint frequency — no post-deployment audits; (c) override accountability — overrides unlogged and unreviewed; (d) alert threshold — no feedback loop from outcome to AI score.

6. **Name one specific control that would have caught the failure earliest.** Not "better oversight" but the exact mechanism: "A sub-group accuracy audit run monthly, broken down by age band and shift, with results reviewed by a named role."

## 7. Real-World Patterns

The failure structure documented in the triage case appears across any domain where an AI scoring system feeds into a consequential queue. The same four gaps — evaluation design, checkpoint frequency, override accountability, alert threshold — surface in credit scoring systems, hiring algorithms, and content moderation queues [2].

What makes medical triage the clearest teaching case is two features: the severity of the outcome makes the stakes undeniable, and medical records provide ground truth that traces the AI's score to the eventual outcome. This traceability is what makes the evidence peer-reviewable and the failure mode documentable [1].

Two patterns hold consistently across the triage literature:

**High-volume environments accelerate tolerance.** When a system processes thousands of patients per week, each individual clinician sees only a slice. A nurse on day shift never sees the night-shift data. A department manager reviews weekly averages. No single person accumulates enough direct experience with the failure pattern to raise an alarm. The scale of the pipeline is its own cover [1].

**Post-market surveillance is the standard analogy.** When a pharmaceutical company receives approval to sell a drug, that approval does not last forever without conditions. The company must run ongoing safety monitoring — called post-market surveillance — and report adverse events. If a pattern of adverse events emerges, the drug is reviewed and potentially withdrawn.

The same concept — mandatory, continuous post-deployment performance monitoring for clinical AI — is now being proposed as the regulatory standard for AI systems used in patient care [1]. The triage failures documented in this case study are among the evidence driving that regulatory push.

## 8. Best Practices

These heuristics summarise the responsible deployment posture that would have prevented the tolerated failure mode:

| Do | Do not |
|---|---|
| Measure accuracy by patient sub-group from day one of deployment | Rely on overall accuracy as the only measure of system health |
| Log every human override with the reason and the eventual outcome | Treat override decisions as informal, untracked events |
| Assign a named role or team accountability for pipeline-level outcomes | Spread accountability across steps so no one owns the full picture |
| Schedule recurring post-deployment audits at fixed intervals | Treat deployment certification as permanent approval |
| Wire a deterioration-contradiction alert into the workflow | Assume launch-time accuracy predicts ongoing accuracy |
| Apply the Judgment Framework to set the AI's authority before deployment | Let time pressure and convenience decide how much authority the AI holds in practice |
| Require that sub-group audit results are reviewed by someone outside the deployment team | Allow the vendor or deployment team to self-assess without external scrutiny |

The anti-pattern to memorise: **one-time certification, no ongoing accountability.** In every documented case of tolerated failure mode, the organisation treated the AI system as a product that was "done" once deployed. It was not done. It was running, drifting, scoring patients, and accumulating harm. Certification is the beginning of oversight, not the end of it [3].

## 9. Hands-On Exercise

This exercise is preparation for the lab post-mortem, which feeds Assessment 3.

1. Without looking at the corpus, write down the six steps of the diagnostic procedure from section 6. Check your list against the text.

2. Apply all six steps to the triage case, writing your answers in full sentences. Do not copy — paraphrase from memory.

3. For step 6 (name one specific control), write a 50-word justification for why the control you named would have surfaced the failure mode before harm accumulated.

4. Now draft your full 200-word post-mortem: "What governance control would have prevented the failure?" Your post-mortem should name the control, explain how it works, explain why it would have surfaced the failure mode, and state who would have been responsible for running it.

## 10. Key Takeaways

- An AI-assisted triage system assigns urgency scores that determine how long a patient waits. A systematically wrong score in a high-stakes case — where errors are invisible before harm — can directly cause preventable death or permanent injury.
- The documented failure mode is systematic under-scoring of specific patient groups (elderly patients, patients using non-standard symptom language, night-shift patients) — a pattern that was detectable with available data but was hidden by aggregate accuracy metrics [1][3].
- The failure persisted because of four compounding governance gaps: flawed evaluation design, absent post-deployment audits, override as theater, and no deterioration-contradiction alerts [1][2].
- Automation bias (topic 9.5) turned each clinician's acceptance of the AI score into a silent validation of the failure pattern, preventing the corrective signal that a genuine human override would have provided.
- The Judgment Framework (Q1/Q2/Q3) applied to triage shows that all three conditions for removing AI from final authority were present: the cost of a wrong output is irreversible (Q1), the error is invisible before harm (Q2), and the human checkpoint was theater, not genuine review (Q3) [1].
- A sub-group performance audit — breaking accuracy down by patient category, run on a fixed schedule — is the single control most consistently cited as the earliest detection mechanism [3]. A deterioration-contradiction alert is the automated complement that makes the feedback loop continuous [2].
- The governance gap behind the gaps was structural: no named person or body was accountable for asking "is this pipeline causing harm across its full output distribution?" Distributed accountability is functional non-accountability [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
