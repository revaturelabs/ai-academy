---
topic_id: "5.1"
title: "Real AI failure cases — healthcare misdiagnosis, hiring bias, deepfake harm"
position_in_module: 1
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Real AI failure cases — healthcare misdiagnosis, hiring bias, deepfake harm — Topic Corpus

## 2. Prerequisites

This topic builds on concepts introduced in prior topics. You should be familiar with:

- **1.3** — Probabilistic systems — same input can give different outputs
- **3.8** — The jagged frontier — tasks AI is superhuman at vs tasks where it is unreliable
- **3.9** — Hallucination — what it is and why it happens
- **2.6** — When NOT to use AI — privacy, precision, legal accountability

These prior topics establish that AI does not always produce correct or consistent answers, and that some tasks carry higher stakes than others. You do not need to re-read them now, but recall that AI can be wrong — and that being wrong in some situations hurts real people.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Describe at least two documented cases of AI failure in healthcare, hiring, and deepfakes, and explain the real harm each caused.
- Identify the specific mechanism — data problem, design flaw, or misuse — that led to each failure.
- Explain what "AI bias" means using a concrete example, without falling back on vague language.
- Distinguish between an AI system that is technically working and one that is causing harm.
- Explain why the people and organizations that deploy an AI system bear responsibility for its outcomes, even when the AI produces the output.

## 4. Introduction

Imagine a doctor uses an AI tool to read a patient's X-ray. The AI says the lung is clear. The doctor, trusting the tool, tells the patient everything is fine. Six months later, the patient is diagnosed with late-stage lung cancer — something that was visible in that original X-ray.

The AI did not intend to mislead anyone. It was not "trying" to harm the patient. But the harm was real.

This is what an AI failure looks like in practice. It is not a robot going rogue. It is a system that learned from imperfect data, or was built for one purpose and used in another, or was deployed without enough checks — and someone paid the price.

This topic examines three domains where AI failures have caused documented, real-world harm: healthcare misdiagnosis, hiring bias, and deepfake identity attacks. For each domain, you will see what happened, why the AI failed, and what harm resulted.

Knowing these cases matters for every person who will ever use, buy, recommend, or build an AI system — which, in today's world, means almost everyone in a professional role.

## 5. Core Concepts

### 5.1 What an AI failure is — and what it is not

Before looking at specific cases, it helps to define the term clearly.

**AI failure** — a situation where an AI system produces an output that causes harm, unfairness, or a significant error, even though the system appeared to be working as designed.

This definition has two parts worth noting. First, the harm is real — someone is hurt, disadvantaged, or put at risk. Second, the system may have appeared to work. The failure is not always a crash or an obvious error message. Sometimes the failure is a confident, plausible-sounding wrong answer. You saw an example of this in topic 3.9 when you learned about hallucination — AI stating falsehoods with confidence.

AI failures are not rare edge cases. They happen across industries, at scale, every day. A single AI model deployed to thousands of hospitals, or used to screen millions of job applications, can fail in the same way for every single one of those cases simultaneously.

### 5.2 Healthcare misdiagnosis — when AI reads the wrong pattern

**Diagnostic AI** — an AI system trained to look at medical images, such as X-rays, CT scans, or photographs of skin, and identify signs of disease. Doctors use these tools to help catch problems they might otherwise miss, or to speed up review when they have thousands of images to check.

A **radiologist** is the specialist who normally reads and interprets medical scans. Diagnostic AI is often compared to this role.

Diagnostic AI can be genuinely useful. Some systems can detect certain cancers in images with accuracy that matches or exceeds a trained radiologist. But these same systems can also fail in specific, patterned ways. When they fail, patients can receive the wrong diagnosis, the wrong treatment, or no treatment at all.

**Why do diagnostic AI systems fail?**

The most common reason is the data they were trained on. AI systems learn by finding patterns in large collections of examples. If those examples are skewed — if they do not represent all patients equally — the model will learn skewed patterns.

**Training data bias** — when the dataset used to train an AI system does not fairly represent the population the system will later serve. The model learns patterns from the data it saw, not from reality as a whole.

Here is a concrete example. Many early diagnostic AI systems were trained almost entirely on images from large research hospitals in wealthy countries [1]. Those hospitals served patient populations that were predominantly lighter-skinned. As a result, the model learned what disease looks like on lighter skin tones. When the same model was later used on patients with darker skin tones, its accuracy dropped significantly [1]. The model was not malicious. It simply had never seen enough examples to learn the right patterns for that group.

The AI Standard of Care Misdiagnosis Case Tracker documents ongoing and closed cases involving diagnostic AI failures, lawsuits, and litigation across multiple healthcare settings [1]. These cases show that diagnostic AI failures are not theoretical — they result in delayed diagnoses, incorrect treatments, and patient deaths. The tracker includes cases involving AI tools for reading chest X-rays, detecting diabetic eye disease, and flagging skin lesions. In each documented category, failures cluster in specific patient subgroups — often patients whose demographic characteristics were underrepresented in the training data [1].

**What harm does healthcare misdiagnosis cause?**

- A patient with a treatable disease is told they are fine. They do not receive treatment. The disease progresses.
- A patient without disease is flagged as sick. They undergo unnecessary tests, procedures, or surgery.
- A patient from a demographic group underrepresented in training data receives systematically worse AI-assisted care than patients from other groups [1].

That last point is important. When a bias exists in a system deployed at scale, it does not affect one patient. It affects every patient from that group who encounters the system. The harm multiplies.

**Who is responsible?**

The AI system itself does not make legal or ethical decisions — people and organizations do. When an AI-assisted diagnosis is wrong, responsibility falls on the team that designed the system, the organization that deployed it, and the clinician who acted on its output without appropriate verification. The concept of accountability — who is answerable for an outcome — is something you will explore more deeply in topic 5.4 and the topics that follow.

### 5.3 Hiring bias — when an algorithm learns to discriminate

In 2014, Amazon — the large technology and retail company — began building an AI system to help screen job applications. The goal was to sort through the hundreds of thousands of CVs the company received and surface the best candidates automatically. By 2018, Amazon had abandoned the project entirely. The reason: the system had learned to penalize applications from women [2].

**How did this happen?**

Amazon trained the model on ten years of its own hiring history — applications the company had received and decisions it had made about those applicants. Over those ten years, Amazon, like most technology companies at the time, had hired far more men than women [2]. The model learned from that pattern.

The result was not subtle. The system actively downgraded CVs that contained words like "women's" — as in, "president of the women's chess club." It rated graduates of all-women's colleges lower than other candidates. The model had not been told to do any of this. It had learned what a "successful Amazon hire" looked like, based on historical data — and the historical data said that successful hires were mostly men [2].

This is an example of **algorithmic bias** — a systematic, unfair pattern in an AI system's outputs that results from biased training data, biased design choices, or both. Algorithmic bias is a type of AI failure because the system appears to work — it is ranking candidates — while causing harm to a specific group.

**The mechanism: historical data carries historical discrimination**

If you train a model to replicate past human decisions, and those past decisions were discriminatory, the model will replicate the discrimination. This is not a subtle or theoretical risk. When you train an AI on historically biased decisions, it replicates those biases — a pattern you will explore more deeply when you study the training techniques behind these systems in a later topic.

The phrase "garbage in, garbage out" captures this. It means that bad inputs produce bad outputs. For AI hiring tools, the "garbage" is historical hiring data that reflects past discrimination [2]. If women were less likely to be hired in the past — for reasons of bias rather than merit — a model trained on that history will perpetuate that bias going forward.

The Amazon case became famous because it was reported publicly by MIT Technology Review [2]. But hiring AI is used by hundreds of companies worldwide to screen CVs, rank candidates, and make shortlisting decisions. Studies have found similar patterns in many of these systems: preference for male candidates in technical roles, lower scores for names associated with certain ethnic groups, and filtering out of candidates from historically underrepresented groups [2].

**What harm does hiring bias cause?**

- Qualified candidates from disadvantaged groups are filtered out before a human ever sees their application.
- The bias is invisible to the applicant. They receive a rejection — or no response — with no explanation.
- Because the AI processes thousands of applications simultaneously, the scale of harm is large. One biased model, deployed by one company, can systematically block thousands of qualified candidates.
- The system can appear fair on the surface — "it's just an algorithm" — making the bias harder to challenge or correct.

### 5.4 Deepfake harm — when AI is used as a weapon

**Deepfake** — a piece of media, such as a video, image, or audio recording, in which a person's face, voice, or likeness has been replaced or fabricated using AI. The result looks and sounds like a real person doing or saying something they never did.

The word "deepfake" combines "deep learning" and "fake." **Deep learning** is a type of AI technique — a way of training AI systems using very large datasets and complex models inspired loosely by how the brain works. You do not need to understand the technical details of deep learning for this topic. What matters is that it is the same broad approach that powers image generators, voice cloning, and many other modern AI tools.

Deepfakes were not originally designed to cause harm. The underlying AI techniques were developed for legitimate purposes: special effects in films, dubbing content into foreign languages, creating realistic video game characters. But these same techniques were quickly adapted for harmful uses.

**What harm do deepfakes cause?**

The U.S. Department of Homeland Security (DHS) — the federal agency responsible for national security — published a report on the increasing threats posed by deepfake identity attacks [3]. The DHS report documents several categories of harm:

1. **Identity fraud.** A deepfake video or image of a real person is used to impersonate them — to open bank accounts, apply for government documents, or pass identity verification checks [3].

2. **Non-consensual intimate imagery.** A person's face is placed onto explicit content they never appeared in. This form of harm overwhelmingly targets women and has been documented as causing severe psychological harm, damage to professional reputation, and in some cases, a connection to self-harm [3].

3. **Disinformation.** A fabricated video shows a public figure — a politician, a business leader, or a well-known person — saying something they never said. The video is shared widely, and many people believe it is real [3].

4. **Financial fraud.** A deepfake audio or video of a company executive instructs employees to transfer money or share sensitive information. Several documented cases have resulted in financial losses of hundreds of thousands of dollars or more [3].

The DHS report emphasizes that deepfake tools are no longer expensive or technically complex to use [3]. In 2018, creating a convincing deepfake required significant computing resources and expertise. By the mid-2020s, tools exist that allow a person with no technical background to create a convincing deepfake video from a handful of photographs. The barrier to harm has dropped dramatically.

**Why is deepfake harm different from earlier forms of fraud?**

Fraud and identity theft existed before AI. What deepfakes change is the ease, scale, and believability of the attack. A forged signature can be compared to an original. A fabricated video of a person speaking in real time is much harder to verify, especially quickly. And harm to a victim's reputation can spread globally in minutes via social media — before any correction can reach the same audience.

### 5.5 The common thread across all three failures

These three failure domains look different on the surface. Healthcare misdiagnosis involves a technical tool making clinical errors. Hiring bias involves a recruitment system replicating discrimination. Deepfake harm involves AI being deliberately misused as a weapon. But they share two underlying patterns.

**Pattern 1: AI inherits and amplifies existing human problems.**

Diagnostic AI learned from data that underrepresented certain patient groups — reflecting historical inequities in who received care and who was studied [1]. Amazon's hiring tool learned from hiring decisions that reflected workplace discrimination [2]. Deepfake tools use the same technology that powers legitimate creative AI but amplify the potential for harm by lowering the cost and effort required.

In each case, the AI did not invent the problem. It took an existing human problem — inequity in healthcare data, discrimination in hiring history, the human capacity for deception — and made it faster, cheaper, and larger in scale.

**Pattern 2: Harm is real even when intent is absent.**

Amazon did not intend to discriminate against women. The medical AI companies did not intend to give worse care to certain patient groups. Many deepfakes are created by people who treat it as a creative exercise, without thinking carefully about the target's experience. In each case, the absence of intent does not reduce the harm. People are hurt regardless.

This matters because a common response to AI failures is: "The system didn't mean to do it." That response misses the point. When you deploy a system that causes harm, the harm exists whether or not the system — or you — intended it. This is why concepts like accountability, fairness, and harm prevention are now treated as engineering requirements, not optional considerations. You will cover those concepts beginning in topic 5.4.

### 5.6 Scope note — what this topic does not cover

This topic introduces you to documented failures and their mechanisms. The rest of Module 1 and the week's remaining topics examine:

- Why AI gets things wrong at a deeper level (topic 5.2 covers hallucination mechanisms; 5.3 covers data bias)
- The principles used to evaluate AI systems — fairness, transparency, accountability, harm prevention — covered in topic 5.4
- Governance frameworks that attempt to prevent these failures at a policy level — covered starting in topic 5.7

These are named here as orientation only. They are not defined in this topic.

## 6. Implementation

This topic does not involve a technical procedure. There is no algorithm to implement. However, analyzing an AI failure follows a consistent structure you can apply to any reported case. When you encounter a reported AI failure, ask these questions in order:

1. **What did the AI system do?** Describe the specific output that caused harm — a wrong diagnosis, a rejected application, a fabricated video.
2. **Who was harmed, and how?** Name the real-world consequence: a patient did not receive treatment, a candidate was filtered out, a person's reputation was damaged.
3. **Why did the AI produce that output?** Identify the mechanism: biased training data, design flaw, deliberate misuse, or deployment in a context the system was not designed for.
4. **Who is accountable?** Identify the organization, team, or individual responsible for the outcome. The AI system itself has no legal standing.
5. **What should change?** What would prevent this harm — better data, better design, human oversight, regulation, or some combination?

This five-question structure is the basis of the lab exercise for this week.

## 7. Real-World Patterns

**Healthcare AI failures are being tracked and litigated.** The AI Standard of Care Misdiagnosis Case Tracker [1] is one of the first systematic attempts to compile AI-related diagnostic failure cases from hospitals and litigation records. As diagnostic AI tools move from research into clinical practice, the legal and regulatory questions around their failures are being tested in real cases. Hospitals, AI vendors, and regulators are all working to determine who bears liability when an AI-assisted diagnosis is wrong.

**Hiring AI is widespread and largely unregulated in most countries.** The Amazon case [2] was unusual because it became public. Most corporate hiring AI tools operate with little transparency. Several jurisdictions — including New York City — have passed laws requiring employers to audit hiring algorithms for bias before use. These are early attempts at governance in a space that is otherwise largely self-regulated.

**Deepfake harms are scaling faster than defenses.** The DHS report [3] notes that detection tools — systems designed to identify whether a video is a deepfake — are in an ongoing competition with generation tools. As generation improves, detection must keep pace. Currently, detection tools are not reliable enough to serve as the sole defense against deepfake harm.

## 8. Best Practices

These are not technical rules for building AI. They are the analytical habits a professional should apply when evaluating any AI system for deployment or use.

| Practice | Why it matters |
|---|---|
| Ask "Who was in the training data?" before trusting an AI system | If the data underrepresents your users, the model underserves them |
| Treat a confident AI output as a recommendation, not a decision | Especially in high-stakes domains — a human must verify |
| Check whether the AI is being used for its intended purpose | Many failures happen when a tool is deployed in a context it was not designed for |
| Ask "Who is accountable if this is wrong?" before deploying | If no clear answer exists, the system should not be deployed |
| Do not assume "the algorithm decided" removes human responsibility | The people who chose, deployed, and used the system are accountable |

**Anti-pattern to avoid:** Treating accuracy statistics as a guarantee. A system that is "95% accurate" is wrong 1 in 20 times. In healthcare at scale, 1 in 20 is a very large number of patients.

## 9. Hands-On Exercise

This exercise is the foundation for your lab activity this week.

Pick one of the three failure domains covered in this topic — healthcare misdiagnosis, hiring bias, or deepfake harm. Find one additional real case from a news report, a published study, or a documented lawsuit that you can verify.

For your case, answer the five questions from Section 6:
1. What did the AI system do?
2. Who was harmed, and how?
3. Why did the AI produce that output?
4. Who is accountable?
5. What should change?

Write your answers in 200–300 words. You will use this case in your 500-word lab essay and your 3-minute presentation.

## 10. Key Takeaways

- AI failures in healthcare, hiring, and deepfakes are documented, recurring, and cause real harm to real people — patients, job candidates, and individuals whose identities are used without consent.
- The most common root cause is **training data bias** — AI systems learn from historical data that reflects past human inequity, and then replicate and amplify those inequities at scale.
- A system can appear to work correctly — producing confident, plausible outputs — while causing systematic harm to specific groups. Technical accuracy and ethical safety are not the same thing.
- Deepfake tools have lowered the cost of identity-based harm dramatically, making attacks that once required significant resources trivially easy to execute.
- The absence of intent does not reduce harm. Accountability belongs to the people and organizations that design, deploy, and use AI systems — not to the AI itself.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
