<!-- nav:top:start -->
[⬅ Previous: 9.10 — Acceptable error](../../9-10-acceptable-error-defining-the-failure-threshold-tolerable-fo/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 10.1 — Case study: AI in college admissions ➡](../../../../week-10/1-case-studies/10-1-case-study-ai-in-college-admissions-where-was-the-human-over/artifacts/reading.md)
<!-- nav:top:end -->

---

# High-stakes domains where AI must not have the final word — medical, legal, safety

## Overview

Some AI errors are annoying. Others are catastrophic. This topic is about the second kind. In medicine, law, and safety-critical engineering, a wrong AI decision can end a life, take away someone's freedom, or bring down a bridge — and those outcomes cannot be undone. Week 9 has shown you how humans over-rely on automated systems, how accountability chains must end with a named person, and how every system has an error threshold below which harm becomes intolerable. This topic names the three domains where that threshold is already breached — and explains why, in those domains, a human must always have the final word.

## Key Concepts

### What makes a domain "high-stakes"?

Consider two AI systems. One recommends a film you end up disliking. The other recommends a cancer treatment that turns out to be wrong. These are not the same kind of mistake.

A **high-stakes domain** is one where a wrong decision causes severe, often irreversible harm to a real person — harm that cannot be compensated for after the fact [1].

Three signals tell you whether you are in high-stakes territory:

| Signal | What it means | Example |
|---|---|---|
| **Irreversibility** | The decision cannot be undone | A wrongful conviction; a surgery on the wrong patient |
| **Direct impact on fundamental interests** | The decision affects health, liberty, or safety — not preference | A missed cancer diagnosis; detention before trial |
| **Asymmetric error cost** | One type of error causes catastrophic harm | Missing a real tumour (false negative) versus flagging a healthy scan (false positive) |

These three signals connect directly to the Judgment Framework you saw in topics 9.7 and 9.10. Q1 asks: what is the cost if the AI is wrong? The failure threshold concept asks: how much error can we tolerate? In a high-stakes domain, the cost is catastrophic and the tolerable error rate is effectively zero — lower than any current AI system can reliably achieve [1].

### The three named domains

The EU AI Act — the European Union Artificial Intelligence Act, the EU's 2024 regulation on artificial intelligence — formally lists categories it calls **high-risk AI**. Three domains appear in that list more consistently than any others: medicine, law, and safety-critical engineering [3].

![High-stakes domains and the human final authority principle](./diagram.png)
*Three domains where AI must serve as decision support — and the human must retain final authority.*

#### Medicine

AI systems in medicine review images, recommend drug dosages, triage patients, and suggest diagnoses. Each of these outputs can be genuinely useful — but only as **decision support**, meaning a tool that helps a clinician think, not one that replaces the clinician's judgment [2].

When AI makes the final call in medicine and gets it wrong:

1. A patient receives the wrong treatment, causing direct physical harm.
2. The error may not surface until the damage is already irreversible.
3. No named human made the decision — so the accountability chain (from topic 9.9) breaks entirely [1].

MRI (Magnetic Resonance Imaging) scans, CT (computed tomography) scans, and pathology slides are among the image types AI tools now analyse. In every case, the correct model is: AI reviews, human decides.

#### Law

In legal settings, the most documented AI application is **recidivism prediction** — estimating the probability that a convicted person will reoffend. The best-known tool is COMPAS (Correctional Offender Management Profiling for Alternative Sanctions), a commercial system used in US courts to generate risk scores for bail and sentencing decisions [1].

A wrongful detention is irreversible in the moment it occurs. The time a person spends detained before an error is corrected cannot be returned. Research — including a widely cited 2016 ProPublica investigation — documented that COMPAS produced systematically different error rates across demographic groups [1].

The EU AI Act classifies AI used in law enforcement and the administration of justice as high-risk, requiring human oversight of every decision [3].

#### Safety-critical engineering

**Safety-critical** refers to any engineered system whose failure could directly cost human lives: aircraft, railways, chemical plants, nuclear facilities.

Modern aircraft are highly automated. Autopilot systems handle most routine flying. Yet every aviation authority — including the FAA (United States Federal Aviation Administration) and EASA (European Union Aviation Safety Agency) — requires pilots to retain manual override capability and exercise final authority when a situation falls outside the system's designed parameters [2].

The Boeing 737 MAX accidents of 2018 and 2019 show what happens when that principle fails. The MCAS (Maneuvering Characteristics Augmentation System) — an automated flight control feature — repeatedly pushed the nose of the aircraft down after a faulty sensor triggered it. Pilots attempted to override. The system overrode the override. 346 people died. Investigators found that pilots had not been adequately trained to understand or override MCAS [2].

The lesson is not "remove the automation." It is: never remove the human's ability to override.

### The core principle: AI as decision support, human as final authority

The phrase "humans must have the final word" does not mean AI is useless in these domains. It means the roles must be clearly separated:

- **AI role — decision support**: narrows the field, flags anomalies, prioritises cases, surfaces information the human might miss.
- **Human role — final authority**: evaluates the AI's output against the full picture and makes the call.

"AI as tool, human as authority." This is the operating principle in every high-stakes domain [2].

Four separate arguments — each independently defensible — explain why this division is required:

1. **Cost-of-error argument** (from Judgment Framework Q1): severity is catastrophic, detectability is low, recovery is near-zero. No failure threshold is low enough to justify removing the human [1][3].
2. **Accountability argument** (from Judgment Framework Q3): AI systems cannot lose a licence, go to prison, or be sanctioned professionally. When AI makes the final call, no named human made the decision — the accountability chain breaks [1].
3. **Explainability argument** (from EU AI Act requirements): XAI — explainable artificial intelligence — refers to AI outputs that a human can trace and understand. Many AI systems are not fully explainable. A human reviewer who cannot understand the reason for a decision cannot meaningfully evaluate it — they can only approve a number [3].
4. **Cognitive bias argument** (from topics 9.1–9.6): automation bias means humans systematically defer to automated outputs under time pressure, fatigue, and information overload. Saying "a human must review" is not enough on its own [2].

### Meaningful oversight vs nominal oversight

A human signature on an AI output is not the same as human judgment applied to it. The radiologist who approves 47 AI flags without examining a single image has provided a nominal checkpoint — not real oversight.

For oversight to be **meaningful**, four conditions must hold:

1. The reviewer has enough time to evaluate the AI output independently.
2. The reviewer has access to the underlying data — not just the AI's conclusion.
3. The reviewer is trained and empowered to override the system.
4. Overriding is easy, not laborious — it must be designed in [1][2].

A human who cannot realistically override — because of time pressure, missing data, or organisational culture — provides accountability in name only.

## Worked Example

### The radiologist rubber-stamp scenario: applying the four-argument logic

**Setup.** A hospital deploys an AI system that reviews chest X-rays overnight and flags suspicious cases. By morning, 47 X-rays are flagged as requiring attention. A radiologist, pressed for time, opens the dashboard, approves all 47 flags, and dismisses the rest — without examining any individual image. One dismissed image contained an early-stage tumour the algorithm missed [1].

Walk through the four arguments:

**Step 1 — Cost-of-error (Q1).**
Ask: if the AI is wrong, what is the cost?
- Severity: catastrophic. A missed tumour means delayed treatment, which can be fatal.
- Detectability: low. The patient leaves without diagnosis. The error surfaces only when the disease progresses.
- Recovery: near-zero. You cannot restore time lost before correct treatment begins.

Verdict: the cost-of-error threshold has been crossed. Human final authority is required.

**Step 2 — Accountability (Q3).**
Ask: who made the decision?
- The AI flagged and dismissed cases. The radiologist approved the flags without examining the dismissals.
- No named human evaluated the dismissed image. The accountability chain is broken [1].

Verdict: if this reaches litigation, the court will look for a human to hold responsible. No clear candidate exists.

**Step 3 — Explainability.**
Ask: could the radiologist have evaluated the AI's reasoning?
- Most medical imaging AI systems are not fully explainable. The radiologist saw flags and dismissals — not the reasoning behind them.
- Without access to the AI's logic, independent evaluation was not possible. The "review" was rubber-stamping [3].

Verdict: the explainability condition for meaningful oversight was not met.

**Step 4 — Cognitive bias.**
Ask: was the oversight structured to counteract automation bias?
- The radiologist was time-pressured. The AI output was prominent. No easy mechanism existed to examine dismissed cases efficiently.
- These are precisely the conditions under which automation bias operates (topic 9.5): deference to the automated output rather than independent judgment [2].

Verdict: the deployment design actively encouraged rubber-stamping rather than preventing it.

**Conclusion.** The radiologist scenario is not a human failure alone — it is a system design failure. The hospital deployed AI in a high-stakes domain without ensuring the four conditions for meaningful oversight. Fixing it requires redesigning the process: giving the radiologist time, access to underlying images for dismissed cases, and a workflow that makes override natural rather than laborious.

## In Practice

### Pattern 1 — NHS medical imaging: AI as pre-screener, radiologist as authority

In UK National Health Service (NHS) trials of AI mammography screening, AI pre-screened images and flagged those needing urgent radiologist attention. This reduced the time radiologists spent on routine negatives and focused their attention on complex cases. The radiologist remained the decision-maker for every case that proceeded to clinical action [2][3].

This model — AI as pre-screener, human as authority — has become the standard recommended by radiological professional bodies. It improves throughput, reduces cognitive fatigue, and keeps the accountability chain intact. A named radiologist reviews every case that leads to clinical action.

### Pattern 2 — COMPAS legal risk scoring: score informs, judge decides

Courts in most US states have ruled that AI risk scores may be presented as one input among many — but that the judge must exercise independent discretion. The score cannot be the sole or determinative basis for a sentencing decision [1].

Where this has gone wrong is when risk scores were made so prominent that judges effectively rubber-stamped them — automation bias at the institutional level. The lesson: the oversight structure must be designed to counteract automation bias, not assume judges will naturally resist it [1][2].

### Pattern 3 — Boeing 737 MAX: mandatory override capability as a design requirement

After the 737 MAX accidents, regulatory changes required mandatory pilot training on MCAS, a redesigned override procedure with fewer steps under high-workload conditions, and enhanced alerting. These changes did not remove automation. They restored the conditions under which human final authority is real rather than nominal [2].

The lesson: "humans have final authority" is a design requirement. It must be engineered in — not assumed, not declared in a disclaimer.

| What went wrong | Why it failed | What was required |
|---|---|---|
| Pilots could not reliably override MCAS | Not trained on the system; override was complex under stress | Training, simplified override, clear alerts |
| Radiologist approved flags without review | Time pressure; no workflow for examining dismissals | Time allocation, access to underlying data, override-friendly design |
| COMPAS scores over-weighted in sentencing | Score made prominent; institutional pressure to follow it | Structured deliberation, explicit override step |

## Key Takeaways

- A **high-stakes domain** has three defining signals: irreversibility, direct impact on fundamental interests, and asymmetric error cost. Medicine, law, and safety-critical engineering consistently meet all three [1].
- Four arguments — cost-of-error, accountability, explainability, and cognitive bias — each independently justify mandatory human final authority in high-stakes domains [1][2][3].
- AI in these domains should function as **decision support**: it narrows, flags, and prioritises. The human evaluates and decides. "AI as tool, human as authority."
- **Meaningful oversight** requires time, access to underlying data, training to evaluate independently, and an easy override mechanism. A rubber-stamp approval does not satisfy the requirement [1][2].
- The EU AI Act classifies AI in medicine, law enforcement, and safety infrastructure as **high-risk AI**, making human oversight and XAI (explainable artificial intelligence) a legal requirement — not an optional safeguard [3].
- When AI makes the final call, the **accountability chain breaks**. There is no named human who made the decision. This is both a legal and an ethical problem [1].
- Human final authority is a **design requirement**. It must be engineered into the system — as the Boeing 737 MAX case demonstrates, nominal authority and real authority can diverge fatally [2].

## References

[1] Harvard Law & Technology — "Redefining the Standard of Human Oversight for AI Negligence." *Journal of Law and Technology at Harvard*. https://jolt.law.harvard.edu/digest/redefining-the-standard-of-human-oversight-for-ai-negligence

[2] OneReach.ai — "Human-in-the-Loop Agentic AI Systems." https://onereach.ai/blog/human-in-the-loop-agentic-ai-systems/

[3] AI Competence — "XAI in High-Stakes: When the Law Demands Answers." https://aicompetence.org/xai-in-high-stakes-when-the-law-demands-answers/

---
<!-- nav:bottom:start -->
[⬅ Previous: 9.10 — Acceptable error](../../9-10-acceptable-error-defining-the-failure-threshold-tolerable-fo/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 10.1 — Case study: AI in college admissions ➡](../../../../week-10/1-case-studies/10-1-case-study-ai-in-college-admissions-where-was-the-human-over/artifacts/reading.md)
<!-- nav:bottom:end -->
