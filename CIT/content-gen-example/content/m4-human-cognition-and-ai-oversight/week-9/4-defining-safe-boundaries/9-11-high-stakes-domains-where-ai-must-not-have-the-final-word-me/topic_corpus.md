---
topic_id: "9.11"
title: "High-stakes domains where AI must not have the final word — medical, legal, safety"
position_in_module: 2
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. High-Stakes Domains Where AI Must Not Have the Final Word — Topic Corpus

## 2. Prerequisites

This topic is the capstone of the Week 9 Judgment Framework sequence. It draws directly on:

- **9.7 — Judgment Framework Q1 — cost of error**: the idea that some decisions carry consequences so severe that no acceptable error threshold exists for autonomous AI action. This topic applies that reasoning to three named domains.
- **9.9 — Judgment Framework Q3 — who is accountable?**: the concept of an accountability chain — a traceable line from a decision to a named, responsible human. This topic argues that in high-stakes domains, that chain must end with a human, never with an AI system.
- **9.10 — Acceptable error — failure threshold**: the concept that every system has a failure threshold — a maximum tolerable error rate. This topic argues that in certain domains, no AI failure threshold is low enough to justify removing the human from the final decision.

Earlier topics (9.1–9.6) introduced the cognitive mechanisms — System 1 and System 2 thinking, automation bias, confirmation bias — that explain *why* humans sometimes relinquish that final decision inappropriately. Those concepts are referenced here as established vocabulary, not re-introduced.

No programming background is required. This topic is about governance, accountability, and human judgment — not technology.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

1. **Define** the term "high-stakes domain" and explain what distinguishes it from a lower-stakes setting where AI autonomous decisions are more acceptable.
2. **Identify** at least two reasons — one from cognitive science and one from law or regulation — why humans must retain the final word in medical, legal, and safety-critical decisions.
3. **Apply** the Judgment Framework (Q1, Q3, and failure threshold) to a real or hypothetical AI deployment in a high-stakes domain to determine whether human final authority is required.
4. **Explain** what the EU AI Act's (European Union Artificial Intelligence Act's) "high-risk AI" category means and how it relates to mandatory human oversight.
5. **Describe** at least one concrete accountability failure that can occur when AI is allowed to make the final call in a high-stakes domain.

---

## 4. Introduction

A cancer screening algorithm reviews ten thousand chest X-rays overnight. By morning it has flagged 47 as suspicious. A radiologist opens the dashboard and — pressed for time — approves all 47 flags and dismisses the rest without looking at any individual image. One dismissed image contained an early-stage tumour the algorithm missed.

Is the algorithm to blame? Is the radiologist? The hospital? The company that sold the software?

This question is not hypothetical. It is the kind of question courts, regulators, and hospital boards are wrestling with right now — and it does not have a clean answer, because a critical boundary was crossed: the human stopped being the decision-maker and became a rubber stamp for the machine. [1]

This topic is about that boundary. We call it the **final word** — the point in a decision process where someone or something makes an irreversible call that affects a real person's health, freedom, or safety. The evidence — from cognitive science, law, and engineering — says that in certain domains, that final word must come from a human. Not because AI is always wrong, but because when AI is wrong in these domains, the cost is catastrophic, the error is often invisible until it is too late, and no one can be held accountable in any meaningful sense if there is no human in the chain. [1][2][3]

Week 9 has been building toward this conclusion. You have seen how humans over-rely on automated systems (automation bias, 9.5), how accountability chains must end somewhere (9.9), and how every system has a failure threshold below which errors become intolerable (9.10). This topic names the domains where those thresholds are already breached — where no AI error rate is acceptable enough to justify removing the human.

---

## 5. Core Concepts

### 5.1 What Makes a Domain "High-Stakes"?

Not every AI decision is equally consequential. An AI system that recommends a movie gets it wrong and you watch something you do not enjoy. An AI system that recommends a cancer treatment gets it wrong and a patient receives harmful therapy. These are not the same.

A **high-stakes domain** is one where a wrong decision can cause severe, often irreversible harm to a person — and where the harm is significant enough that it cannot be compensated for after the fact. [1]

Three signals identify a high-stakes domain:

**Signal 1 — Irreversibility.** The decision cannot be easily undone. A wrongful conviction, a surgical procedure performed on the wrong patient, a bridge cleared for use that then collapses: these outcomes cannot be rewound.

**Signal 2 — Direct impact on a person's fundamental interests.** The decision affects someone's physical health, liberty, financial survival, or safety — not just convenience or preference.

**Signal 3 — Asymmetric error cost.** The cost of a false negative (Type II error — missing a real problem) or a false positive (Type I error — flagging something that is not a problem) is dramatically higher in one direction than the other, and the "wrong" direction has catastrophic consequences. [1][3]

These three signals map directly onto the Judgment Framework: Q1 asks about cost of error (9.7), and the failure threshold concept (9.10) asks how much error is tolerable. In a high-stakes domain, the cost is catastrophic and the tolerable threshold is effectively zero — lower than any current AI system can achieve reliably. [1]

### 5.2 The Three Named Domains

The EU AI Act — the European Union's 2024 regulation on artificial intelligence — formally lists categories of AI use that it calls **high-risk AI**. Three domains appear in this list (and in the international literature on AI safety) more consistently than any others: medicine, law, and safety-critical engineering. [3]

These are not the only high-stakes domains. But they are the three where the consequences are most immediate, the regulatory frameworks most developed, and the case for mandatory human oversight most thoroughly established.

#### Medicine

In medicine, AI systems are now used for:
- Reviewing medical images (X-rays, MRI scans, pathology slides)
- Recommending drug dosages
- Triaging patients in emergency departments
- Suggesting diagnoses from symptom data

In each of these cases, the AI system's output is potentially useful as a decision-support tool — something that helps a clinician think, flags possibilities they might have missed, or reduces the volume of routine checks the clinician must perform manually. [2]

The critical phrase is **decision-support**. The AI helps the human decide. The AI does not decide.

Why? Because when an AI diagnosis is wrong:
- A patient may receive the wrong treatment, causing direct physical harm.
- The error may not be detectable until significant damage is done.
- The patient cannot meaningfully consent to being diagnosed by a machine alone — medical ethics requires a responsible clinician to own the diagnosis. [1][3]

**The accountability gap** is the central problem. When an AI system makes the final call in a medical decision and that call is wrong, who is responsible? The developer who trained the model? The hospital that deployed it? The clinician who was no longer in the loop? Current law in most jurisdictions does not have a clean answer — which is itself a reason to keep the human in the loop. [1]

In the radiologist example from the Introduction, the system committed what topic 9.5 called an **omission error**: it missed a real finding. But the radiologist committed an accountability failure: they no longer exercised independent judgment. The law will look for a human to hold responsible. If no human made the call, the accountability chain (9.9) breaks entirely. [1]

#### Law

In legal settings, AI systems are used for:
- Predicting recidivism (the probability that a convicted person will reoffend) to inform bail and sentencing decisions
- Flagging cases for legal aid eligibility
- Reviewing contracts for compliance
- Routing cases through court administrative systems

The most documented and controversial application is **recidivism prediction**. AI tools — the best-known being a commercial tool called COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) — have been used in US courts to generate risk scores that judges consult when deciding whether to grant bail or recommend a prison sentence. [1]

Research has shown that these tools can produce systematically different error rates across different demographic groups — incorrectly labelling some groups as high-risk at higher rates than others. This is not a hypothetical concern: it was documented in a widely-cited 2016 ProPublica investigation into COMPAS scores. [1]

The legal problem is profound: **a conviction or a period of pre-trial detention is irreversible in the moment it occurs**. If a person is wrongly denied bail because an algorithm labelled them high-risk, the time they spend detained before that error is corrected is gone. They cannot be compensated in any meaningful sense for lost freedom.

The EU AI Act classifies AI used in law enforcement and administration of justice as high-risk, requiring human oversight of all decisions. [3] The rationale is the same as in medicine: the cost of error is too high, the reversibility too low, and the accountability chain too broken to allow AI to be the final authority.

#### Safety-Critical Engineering

**Safety-critical** refers to any engineered system whose failure could directly cause loss of human life. The clearest examples include:
- Aircraft flight control systems
- Railway signalling and train control
- Industrial process control (chemical plants, nuclear facilities)
- Autonomous vehicles

In these domains, AI and automated systems have been used for decades. The aviation industry, in particular, has deep experience with the risks of over-automation — which is why its approach to human oversight is instructive.

Modern commercial aircraft are highly automated. Autopilot systems handle most of the routine flying. But every aviation authority in the world — including the EASA (European Union Aviation Safety Agency) and the FAA (United States Federal Aviation Administration) — requires that pilots remain capable of manual override and must exercise final authority in situations that fall outside the system's designed parameters. [2]

The Boeing 737 MAX accidents of 2018 and 2019 — in which the MCAS (Maneuvering Characteristics Augmentation System) automated flight control system repeatedly pushed the nose of the aircraft down in response to a faulty sensor reading, and pilots struggled to override it — illustrate what happens when automation is given too much authority over a safety-critical outcome. 346 people died. The investigation found, among other things, that pilots had not been adequately trained to understand or override the system. [2]

The lesson the industry drew is not "remove the automation" but "never remove the human's ability to override the automation and assume final authority."

### 5.3 Why Human Final Authority Is Required — Four Arguments

It is not enough to say "it feels safer to have a human decide." The argument for mandatory human oversight in these domains rests on four distinct and separately defensible grounds.

#### Argument 1 — The Cost-of-Error Argument (from Judgment Framework Q1)

In the Judgment Framework (9.7), Q1 asks: if this AI output is wrong, what is the cost? The framework distinguishes decisions by severity, probability, and detectability of error.

In high-stakes domains, the answers are:
- **Severity**: catastrophic (death, wrongful imprisonment, structural collapse)
- **Detectability**: often low (the error may not surface until the harm is irreversible)
- **Probability of recovery**: near zero

When all three conditions hold simultaneously, no failure threshold (9.10) is low enough to justify autonomous AI authority. Even a 99.9% accurate system failing on 0.1% of cases means — in a hospital processing 100,000 AI decisions per year — 100 potentially catastrophic errors. [1][3]

This is not a hypothetical argument about edge cases. It is the mathematical reality of operating at scale.

#### Argument 2 — The Accountability Argument (from Judgment Framework Q3)

Judgment Framework Q3 asks: if this decision goes wrong, who is accountable? (9.9)

**Accountability** requires a named human who had the authority and the information to make a different choice, and who bears the legal, professional, and ethical responsibility for the outcome. AI systems cannot be held accountable in this sense — they cannot lose their licence, go to prison, or be sanctioned professionally. [1]

When an AI makes the final call, the accountability chain breaks. The decision was made, but no one in the conventional legal sense made it. Courts have generally responded to this by trying to assign accountability to whoever deployed or designed the system — but this is an imperfect solution, particularly when the deployer argued they were just using a tool and the designer argued they could not control how it was used.

The only way to maintain a functioning accountability chain in high-stakes domains is to ensure that a named human makes the final decision, with the authority and information required to make it independently. [1]

#### Argument 3 — The Explainability Argument (from EU AI Act requirements)

The EU AI Act (European Union Artificial Intelligence Act, 2024) requires that AI systems classified as high-risk must be **explainable** — their outputs must be interpretable by the humans overseeing them. [3]

**Explainability** (sometimes called XAI — explainable artificial intelligence) refers to the property of an AI system's outputs being traceable and understandable: a human can see, in terms they can evaluate, why the system produced a particular output.

Most modern AI systems — including the large language models, deep neural networks, and complex ensemble models that produce the highest accuracy scores in benchmarks — are not fully explainable. Their internal computations involve millions or billions of numerical operations that do not map cleanly onto human-readable reasons.

This matters for high-stakes domains because a human reviewer who cannot understand the reason for a decision cannot meaningfully evaluate it. They can only approve or reject a number — which is not independent oversight; it is rubber-stamping with extra steps. [3]

The EU regulation's response is to require explainability as a precondition for deployment in high-risk categories. Where full explainability cannot be achieved, human oversight of the final decision is the required backstop. [3]

#### Argument 4 — The Cognitive Bias Argument (from 9.1–9.6)

The cognitive science topics earlier in Week 9 established that humans are systematically vulnerable to automation bias (9.5) — especially under time pressure, cognitive fatigue, and information overload. They defer to automated outputs even when they should not.

This means that stating "a human must review the AI output" is not automatically sufficient. A human review process can be a rubber stamp — a nominal checkpoint that does not actually involve independent evaluation. [2]

For human oversight to be meaningful in high-stakes domains, it must be structured to counteract automation bias:
- The reviewer must have enough time to evaluate the AI output independently.
- The reviewer must have access to the underlying data, not just the AI's conclusion.
- The reviewer must be trained and empowered to override the system.
- The system must be designed so that overriding is easy, not laborious. [1][2]

A human in the loop who cannot realistically override — because of time pressure, information asymmetry, or organisational culture — provides accountability in name only.

### 5.4 What "Human Final Word" Actually Means

The phrase **"humans must have the final word"** is sometimes misread as "AI is useless in these domains." That is the opposite of the intended meaning.

In high-stakes domains, the appropriate role for AI is **decision support**: the AI narrows the field, flags anomalies, prioritises cases, and surfaces information the human might have missed. The human then evaluates that support and makes the call. [2]

The clearest statement of this principle in practice comes from the medical imaging literature: AI tools that perform at or above radiologist level in controlled benchmark tests consistently underperform when deployed in real clinical environments, because real clinical environments involve edge cases, ambiguous presentations, and contextual information that the benchmark did not include. The radiologist's role is not to confirm what the AI says — it is to evaluate the AI's output against the full clinical picture that only a human can integrate. [2][3]

The same logic applies in law: a risk score from a recidivism-prediction tool may be one input into a sentencing recommendation. The judge integrates that score with direct observation of the defendant, the case history, and the broader legal context. The score does not sentence; the judge sentences.

And in safety-critical engineering: the autopilot handles routine flight. The pilot handles the situations the autopilot was not designed for — and retains the authority and capability to assume full manual control at any moment.

**AI as tool, human as authority.** This is the operating principle in high-stakes domains.

---

## 6. Implementation

### Applying the Judgment Framework to a High-Stakes Domain

The Judgment Framework provides a structured way to determine whether a given AI application requires mandatory human final authority. Here is how to apply it when you are evaluating an AI system in or adjacent to a high-stakes domain.

**Step 1 — Answer Q1: What is the cost of error?**

Work through the three dimensions from 9.7:
- How severe is the worst-case harm if the AI is wrong? (Score: low / significant / catastrophic)
- How likely is that harm to go undetected until it is irreversible?
- Can the harm be compensated or corrected after the fact?

If the answer is "catastrophic harm, hard to detect, irreversible" — you are in high-stakes territory. Human final authority is required. Do not proceed to a cost-benefit calculation; the threshold has already been crossed.

**Step 2 — Answer Q3: Who is accountable?**

From 9.9, trace the accountability chain:
- If the AI decision is wrong, who is the named human who could have made a different choice?
- Does that person have the information, authority, and time to actually evaluate the decision independently?
- Is their accountability legally and professionally recognised?

If no named human can be identified, or if the named human was not in a position to exercise real oversight, the accountability chain is broken. Redesign the process to put a real human in a real position of authority before deployment.

**Step 3 — Check the failure threshold**

From 9.10, estimate the system's realistic error rate in this deployment context (not the benchmark accuracy, but the real-world operational accuracy, which is typically lower).

Ask: is this error rate below the threshold at which errors in this domain become catastrophic?

In medicine, law, and safety: if even a small fraction of errors produce catastrophic outcomes, and the error rate is non-zero (which it always is), the answer is no — human oversight is required.

**Step 4 — Assess whether the human oversight is meaningful**

A nominal human reviewer does not satisfy the requirement. Ask:
- Does the reviewer have enough time?
- Does the reviewer have access to the underlying data, or only the AI's conclusion?
- Is the reviewer trained to evaluate this class of decision independently?
- Is overriding the AI system easy and culturally supported?

If any of these answers is no, the oversight process needs to be redesigned before deployment.

**Step 5 — Check for regulatory classification**

Consult applicable regulations. Under the EU AI Act, if the AI system falls into a listed high-risk category (medicine, law enforcement, safety infrastructure, education, employment), mandatory human oversight is a legal requirement, not an optional safeguard. [3]

Document the regulatory classification and the specific oversight requirement as part of the deployment record.

---

## 7. Real-World Patterns

### Pattern 1 — Medical Imaging: AI as Triage Tool, Radiologist as Authority

AI-powered tools for reading medical images (X-rays, CT scans, mammograms, pathology slides) are among the most mature and widely deployed AI systems in healthcare. The best of these systems achieve accuracy rates in controlled studies that match or exceed individual radiologists on specific tasks.

Yet the consistent finding from real-world deployment is that AI performs better as a triage tool than as a sole decision-maker. In the UK National Health Service (NHS) trials of AI mammography screening, AI was used to pre-screen images and flag those requiring urgent radiologist attention — reducing the time radiologists spent on routine negatives and focusing their attention on complex cases. The radiologist remained the decision-maker for every case that proceeded to clinical action. [2]

This model — AI as pre-screener, human as authority — has become the standard recommended by radiological professional bodies internationally. It improves throughput, reduces cognitive fatigue, and maintains accountability. It does not eliminate human judgment; it focuses it. [2][3]

The accountability structure is clear: a named radiologist reviews every flagged case and every case that proceeds to clinical action. If a case is missed, the radiologist is the responsible professional.

### Pattern 2 — Legal Risk Scoring: Tools Without Final Authority

AI recidivism-prediction tools — most prominently COMPAS in the United States — have been in use in courts for over a decade. They generate risk scores that are presented to judges alongside case summaries and prosecution and defence arguments.

The critical design principle that separates legitimate use from illegitimate use is: **the score informs the judge; the judge decides**. Courts in most US states have ruled that AI risk scores may be presented as one input among many, but that the judge must exercise independent discretion — the score cannot be the sole or determinative basis for a sentencing decision. [1]

Where this has gone wrong is in systems that made risk scores so prominent, or that created institutional pressure to follow them, that judges effectively rubber-stamped them. This is automation bias at the institutional level: the nominal human authority became a formal checkpoint rather than a genuine deliberative step.

The lesson is not that risk scores are impermissible — it is that the oversight structure must be designed to counteract automation bias, not assume judges will naturally resist it. [1][2]

### Pattern 3 — Aviation: The MCAS Case and Mandatory Override Capability

The Boeing 737 MAX MCAS system — the automated flight control system implicated in the 2018 and 2019 crashes — was designed to activate automatically when sensors detected a risk of aerodynamic stall. In the accident flights, a faulty angle-of-attack sensor triggered repeated MCAS activations. The system pushed the nose of the aircraft down. Pilots attempted to override. The system overrode the override. [2]

The formal finding of the accident investigations was that pilots had not been adequately informed that the system existed, how it operated, or what the override procedure required. Human final authority had been nominally preserved — pilots could in principle override MCAS — but the conditions for meaningful override had not been met: pilots lacked the knowledge, and the override procedure was non-obvious under stress. [2]

Regulatory changes following the accidents included mandatory pilot training on MCAS, redesign of the override procedure to require a smaller number of steps under high-workload conditions, and enhanced alerting requirements. These changes did not remove automation — they restored the conditions under which human final authority is real rather than nominal.

This case illustrates that "humans have final authority" is a design requirement, not a legal disclaimer. It must be engineered into the system.

---

## 8. Common Misconceptions

**Misconception 1: "AI is too accurate to need human oversight in high-stakes domains."**

Accuracy in a benchmark test and accuracy in real-world deployment are different. Benchmarks use curated datasets with known ground truth. Real deployments encounter edge cases, distribution shifts (situations the model was not trained on), ambiguous inputs, and novel presentations. AI systems that achieve 95%+ accuracy in benchmarks routinely show significantly lower accuracy in operational environments — and in high-stakes domains, the cases most likely to fall outside the benchmark distribution are precisely the hardest, most consequential cases. [1][3]

Even if the accuracy were genuinely equivalent, 1% of errors at hospital scale is thousands of patients per year.

**Misconception 2: "Requiring human oversight just slows everything down and costs more."**

This argument compares the cost of human oversight to the cost of not having it — but misidentifies what "not having it" costs. The direct costs of a missed cancer diagnosis, a wrongful conviction, or an aircraft accident dwarf the staffing costs of a human review process. Legal liability costs, regulatory fines, reputational damage, and — most importantly — harm to people are the actual counterfactual. [1][2]

There is also a false dichotomy embedded in this misconception: human oversight does not mean humans repeat all the AI's work. A well-designed process uses AI to reduce the volume and complexity of what humans must evaluate, so the human's time is focused on the cases that genuinely require independent judgment.

**Misconception 3: "If a human approves the AI's output, the human is responsible — so the AI company isn't liable."**

This is an argument made by some AI system vendors and is contested in courts and regulatory bodies. The legal and ethical reality is more complex: if the AI system was designed or deployed in a way that made meaningful human review practically impossible, the vendor or deploying organisation may retain liability even if a nominal human approval step existed. [1][3]

The EU AI Act takes this position explicitly: it places obligations on both developers and deployers of high-risk AI systems, regardless of whether a human approval step exists. "A human clicked approve" is not a sufficient defence if the system was designed so that clicking approve was the only realistic option.

**Misconception 4: "This only applies to AI that makes decisions autonomously — our system just makes recommendations."**

The distinction between "recommendation" and "decision" is thinner than it appears in practice. A recommendation presented prominently, in a time-pressured workflow, to an overloaded professional, with no easy mechanism for override, is functionally a decision. Automation bias (9.5) means that humans systematically over-accept AI recommendations in these conditions. [2]

Whether oversight is meaningful depends on the deployment context, not the label on the output.

---

## 9. Key Takeaways

- A **high-stakes domain** is one where AI errors can cause severe, irreversible harm to a person — in medicine, law, and safety-critical engineering, this threshold is consistently met.
- The Judgment Framework's three questions — cost of error (Q1), accountability (Q3), and failure threshold — together make the case for mandatory human final authority: catastrophic cost, broken accountability chains, and zero-tolerable error rates all point the same direction. [1]
- **AI in high-stakes domains should function as decision support, not as a decision-maker.** The AI narrows, flags, and prioritises. The human evaluates and decides.
- Human oversight must be **meaningful**, not nominal. A rubber-stamp approval step does not satisfy the oversight requirement — the human must have the time, information, authority, and training to evaluate independently and override easily. [2]
- The EU AI Act formally codifies these principles in law, classifying AI in medicine, law enforcement, and safety infrastructure as high-risk and requiring demonstrable human oversight and explainability. [3]
- When an AI system makes the final call, the **accountability chain breaks** — there is no named human who made the decision, and accountability cannot be meaningfully assigned. This is both a legal problem and an ethical one.
- Maintaining human final authority is a **design requirement**: it must be engineered into the process, not assumed as a cultural norm. The Boeing 737 MAX case shows what happens when nominal authority and real authority diverge.

---

## 10. Discussion Prompts

**Prompt 1 — Applying the Judgment Framework to your own domain**

Think about a system you work with or are studying — or a system you have read about — that uses AI to support decisions. Apply the Judgment Framework to it:
- Q1: What is the cost if the AI is wrong? Is the harm severe, hard to detect, and irreversible?
- Q3: Who is accountable if the decision goes wrong? Can you name a specific person with real authority and real information?
- Failure threshold: What error rate does this system actually achieve in real-world conditions? Is any error rate tolerable, given the consequences?

Based on your answers, do you think this system currently has adequate human oversight? What would you change?

This connects directly to the Lab Activity: applying the Judgment Framework per component to your domain system.

**Prompt 2 — The rubber-stamp problem**

In the radiologist example from the Introduction, the clinician approved 47 AI flags without reviewing any individual image. The hospital could argue that a human was in the loop. A regulator might disagree.

Where do you draw the line between meaningful human oversight and a rubber-stamp approval? What three structural features would you require in a medical AI review process to ensure the oversight is real?

Think about what you know from automation bias (9.5) and System 2 thinking (9.2). What conditions make genuine System 2 engagement difficult — and how would a good process design counteract those conditions?

**Prompt 3 — The COMPAS case and accountability**

A judge uses an AI risk score as one input in a sentencing decision. The defendant receives a harsher sentence than they would have received without the score. Later, the score is shown to have been systematically biased against the defendant's demographic group.

Who, if anyone, is accountable for the harm?
- The AI company that built COMPAS?
- The court system that adopted it?
- The judge who consulted it?
- The legislature that did not regulate it?

Use the accountability chain concept from 9.9 to structure your answer. Is there a way to design the process so the accountability chain remains intact?

---

## 11. Further Reading

[1] Harvard Law & Technology — "Redefining the Standard of Human Oversight for AI Negligence." _Journal of Law and Technology at Harvard_. https://jolt.law.harvard.edu/digest/redefining-the-standard-of-human-oversight-for-ai-negligence — Primary source. Argues for redefining legal negligence standards when AI systems lack mandatory human oversight in high-stakes decisions. Covers the accountability gap, the rubber-stamp problem, and the legal frameworks for assigning responsibility.

[2] OneReach.ai — "Human-in-the-Loop Agentic AI Systems." https://onereach.ai/blog/human-in-the-loop-agentic-ai-systems/ — Practical overview of human-in-the-loop (HITL) design patterns, with examples from medical imaging and legal case triage. Illustrates how "human final authority" is implemented in working systems.

[3] AI Competence — "XAI in High-Stakes: When the Law Demands Answers." https://aicompetence.org/xai-in-high-stakes-when-the-law-demands-answers/ — Covers the EU AI Act's high-risk AI category, explainability requirements (XAI), and how medicine, legal, and safety domains are classified and regulated. Connects regulatory framework to the practical question of what human oversight must include.
