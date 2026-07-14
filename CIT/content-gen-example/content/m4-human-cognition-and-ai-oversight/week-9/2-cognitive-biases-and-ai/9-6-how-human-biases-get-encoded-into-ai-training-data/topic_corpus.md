---
topic_id: "9.6"
title: "How human biases get encoded into AI training data"
position_in_module: 4
generated_at: "2026-06-12T00:00:00Z"
resource_count: 3
---

# 1. How Human Biases Get Encoded into AI Training Data — Topic Corpus

## 2. Prerequisites

This topic builds on concepts introduced in earlier sessions of Week 9:

- **9.3** — Confirmation bias, selective search, biased interpretation, selective memory, motivated reasoning
- **9.4** — Anchoring bias, the anchor, the adjustment heuristic, insufficient adjustment
- **9.5** — Automation bias, omission error, commission error, cognitive offloading, complacency, calibrated trust

No programming background is assumed. Everything here is about how human judgment shapes data — and how that data shapes AI.

## 3. Learning Objectives

By the end of this topic, you should be able to:

- Explain what it means for a bias to be "encoded" into an AI system's training data.
- Describe the four main encoding mechanisms: labelling bias, historical bias, selection bias, and feedback loop amplification.
- Give at least one concrete real-world example for each encoding mechanism.
- Explain how confirmation bias (9.3) and automation bias (9.5) in human practitioners reinforce the encoding problem.
- Identify the difference between a bias that enters once and a feedback loop that makes bias grow over time.
- Name the Judgment Framework as a structured approach covered in Topics 9.7–9.9.

## 4. Introduction

Imagine a teacher who always marks quiet students lower on class participation, even when their written work is excellent. Now imagine that teacher's grade-book is handed to a computer program, which learns to predict which students will "do well." The program has no idea the teacher was unfair — it just sees the numbers. From now on the program will predict that quiet students do poorly, because that is what the data says. The teacher's bias has been baked into the machine.

This is, in a nutshell, how human biases get encoded into AI training data. AI systems learn by example [1]. Feed them good, fair examples, and they tend to produce good, fair outputs. Feed them examples that reflect human prejudice, historical inequality, or careless data collection, and they learn those patterns just as faithfully — sometimes more faithfully than any human would notice [1][2].

This matters because almost every AI tool you will use in your career was trained on data that humans produced. That data carries human fingerprints: the choices people made about what to record, how to label it, and whose experiences to include. Understanding *how* bias enters the data is the first step toward noticing it when it affects you — or when you are the person producing data that will train the next system [3].

## 5. Core Concepts

### 5.1 What "encoding" means

**Encoding** — in this context, capturing something into a form a computer can store and learn from.

When a bias is "encoded" into training data, the bias has been turned into a pattern inside a dataset. The AI does not see a human making a prejudiced decision. It sees numbers, labels, and text. If those numbers, labels, and text reflect a prejudiced pattern, the AI treats that pattern as a fact about the world [1].

Think of it like a photograph. A camera does not judge — it records what is in front of the lens. But if the photographer always photographs one neighbourhood and never another, the photo archive will make the first neighbourhood look like "normal" and the second look invisible. The camera had no bias; the choices behind the camera did.

**Training data** — the set of examples an AI system learns from before it is deployed. Just as a student learns from textbooks, an AI learns from training data. Whatever is in that data shapes what the AI "knows" [1][2].

---

### 5.2 Labelling bias

**Labelling** — the act of attaching a tag or category to a piece of data. A photo of a cat is *labelled* "cat" so the AI knows what it is looking at.

**Labelling bias** — when the tags or categories attached to data reflect the prejudices or assumptions of the people doing the labelling, rather than objective reality [2].

#### How it enters the data

Most large AI datasets are labelled by human workers — sometimes thousands of people hired through online platforms. Those workers bring their own cultural backgrounds, assumptions, and blind spots. When a worker labels an image, scores a piece of writing, or tags an emotion in a sentence, they make a judgment call. Judgment calls are subject to all the biases covered in 9.3–9.5 [2][3].

#### Concrete example 1 — Sentiment labelling

A company building a customer-service AI hires labellers to tag customer reviews as "positive," "negative," or "neutral." One group of labellers consistently tags sarcastic reviews as "positive" because they miss the tone. Another group tags reviews using unfamiliar slang as "negative" because the language feels aggressive to them. The AI trains on these labels and inherits both errors: it now misclassifies sarcasm and unfamiliar dialects in exactly the same way the human labellers did [2].

#### Concrete example 2 — Medical imaging labels

Doctors labelling chest X-rays as "healthy" or "abnormal" may systematically apply different thresholds to patients from different demographic groups — not because of deliberate intent, but because of implicit assumptions. The AI trained on those labels will reproduce the doctors' threshold differences. Patients in under-served groups may receive fewer "abnormal" flags, not because they are healthier, but because the labels reflected the labellers' assumptions [1][3].

---

### 5.3 Historical bias

**Historical bias** — when training data accurately reflects a past that was itself unfair or unequal, and that unfairness gets carried forward into the AI's decisions as if it were a natural law [1].

#### Why accurate data is not always fair data

This is a common surprise: a dataset can be completely accurate and still encode bias. If the data is an honest record of the past, and the past was discriminatory, then accuracy and unfairness come bundled together.

#### Concrete example 1 — Hiring algorithms

Several large companies tried to automate parts of their hiring process by training AI on years of historical hires. The historical record showed that most senior positions had been filled by men. The AI concluded that "male candidate" was a positive signal for senior-role success and began down-ranking women's resumes — not because it was told to, but because the historical data said that was the pattern [1][3]. The AI was right about the past. It was wrong to treat the past as a template for the future.

#### Concrete example 2 — Loan approval

Historical loan data shows higher default rates in certain zip codes. Those zip codes may have higher default rates partly *because* past lending practices denied credit to those neighbourhoods, trapping residents in cycles of financial hardship. An AI trained on that data will refuse loans to residents of those zip codes, reinforcing the same inequality that created the high default rate in the first place [1][2].

#### The key insight

Historical bias does not require anyone to have made a biased decision *today*. The bias is already preserved inside the data like a fossil in rock. The AI excavates it and presents it as fresh evidence.

---

### 5.4 Selection bias (also called representation bias)

**Selection bias** — when the training data does not represent all the groups or situations the AI will later be used on. Some groups are over-represented; others are under-represented or completely absent [1][2].

**Representation bias** is another name for the same problem, emphasising the side that is missing rather than the sampling process that missed it.

#### How it enters the data

Training data is collected by someone. That someone decides what to collect, where to collect it, and whose contributions to include. Those decisions are human decisions, subject to convenience, cost, existing networks, and unconscious assumptions about who "counts" as a typical user [2][3].

#### Concrete example 1 — Facial recognition

Early commercial facial recognition systems were trained primarily on photos of light-skinned male faces — partly because public photo datasets (scraped from the internet in the 2010s) over-represented that demographic. When deployed, these systems performed well on light-skinned men and had measurably higher error rates on darker-skinned women. Research found error rates for darker-skinned women were significantly higher than for lighter-skinned men [1][3]. The AI was not intentionally discriminatory — it was under-trained on certain groups, and that gap showed up as performance disparity.

#### Concrete example 2 — Voice recognition

Voice-controlled devices trained predominantly on recordings of native English speakers from a narrow range of accents. People with strong regional or non-native accents found these devices misunderstood them far more often. The training data had selected for one kind of speech, and anyone who did not fit that pattern paid the cost [2].

#### Why this matters beyond fairness

Selection bias does not only cause harm to under-represented groups. It also makes AI systems unreliable. If the people who actually use an AI are different from the people who appear in its training data, the AI's real-world performance will be worse than its creators measured — because they measured it on people like the training set [1].

---

### 5.5 Feedback loop amplification

The three mechanisms above (labelling bias, historical bias, selection bias) describe how bias *enters* training data. The feedback loop describes what happens when an AI system is deployed and then its outputs become inputs for future training. This is where a small initial bias can grow into a large structural problem [1][3].

**Feedback loop** — a cycle where the output of a system feeds back in as an input, influencing the next cycle's output. In biased AI, the cycle often amplifies rather than corrects the original bias.

#### How the loop forms

1. An AI system is trained on biased data and deployed.
2. The AI makes decisions — for example: loan approvals, resume rankings, content recommendations, or patrol assignments.
3. Those decisions create real-world outcomes: who gets loans, who gets jobs, which neighbourhoods get policed more heavily.
4. Data about those outcomes is collected and used to train or update the next version of the AI.
5. The next version learns from data that reflects the *AI's* prior decisions — not just the original human decisions. The bias has now been laundered through an "objective" machine.
6. Repeat.

#### Concrete example 1 — Predictive policing

A police department uses an AI that predicts which neighbourhoods are "high risk" and directs more patrols there. Because more patrols are present, more arrests happen in those neighbourhoods (partly because the same behaviour goes unnoticed in under-patrolled areas). The arrest data is fed back into the AI as evidence that those neighbourhoods are indeed "high risk." The AI's prediction is confirmed — not because the neighbourhood is actually more dangerous, but because the AI's deployment created the data that validates it [1][3].

#### Concrete example 2 — Content recommendation

A video platform's AI recommends more content similar to what a user has already watched. If a user clicks on one extreme video out of curiosity, the AI learns that extreme content is preferred and recommends more. The user watches some of those, reinforcing the signal. Over time, the AI has self-trained into a pattern of recommending increasingly extreme content — even though the original signal was a single accidental click [2].

#### Why feedback loops are harder to see than single-pass bias

Single-pass bias is visible in the training data if you look carefully. Feedback loop bias looks, at each step, like the AI is simply learning from real-world data. It *is* learning from real-world data — but the real world has already been shaped by the AI's previous decisions. Separating what was true from what the AI made true is extremely difficult [3].

---

### 5.6 Aggregation bias

**Aggregation bias** — when training data combines groups that should be treated separately, and the AI builds one model that fits no group well [1].

#### Example

Medical research has historically gathered data on male patients and assumed findings apply equally to women. A heart disease prediction AI trained on this aggregated data may underperform for women — not because women were absent from the data, but because the data combined two populations that experience heart disease differently. The AI's single model fit both groups imperfectly, and women's outcomes were worse [1].

---

### 5.7 How cognitive biases from 9.3–9.5 reinforce encoding

The four mechanisms above describe *structural* routes for bias to enter data. But the humans doing the work — data scientists, engineers, product managers, labellers — are also subject to the individual cognitive biases covered in this module.

#### Confirmation bias (9.3) and data collection

Recall from 9.3 that confirmation bias leads people to search for, notice, and remember information that confirms what they already believe. In the context of training data:

- A practitioner who believes a certain demographic is lower-risk will tend to collect data that confirms that belief — choosing datasets that reflect it, downweighting data that contradicts it.
- When reviewing labelled data for quality, they may be more likely to flag labels that disagree with their expectations as "errors" and approve matching labels as "correct."
- This is selective search and biased interpretation (9.3) operating at the data pipeline level, not just the individual decision level [3].

#### Automation bias (9.5) and the feedback loop

Recall from 9.5 that automation bias is the tendency to over-trust automated outputs. In the feedback loop context:

- Engineers who accept the AI's outputs as authoritative — without checking whether those outputs reflect genuine world truth or the AI's prior biases — are exhibiting automation bias.
- When AI outputs are fed back as training data, automation bias prevents the humans in the loop from catching the moment when AI-made decisions become the "ground truth" for the next training cycle [1][3].
- This is the commission error variant of automation bias (9.5): acting on an AI recommendation without the critical evaluation that would expose the loop.

The point: the encoding problem is not only a technical data problem. It is also a human judgment problem. The cognitive biases that individual people exhibit in everyday decisions (9.3–9.5) create structural patterns when those people are the ones building and maintaining AI systems.

## 6. Implementation

There is no algorithm anyone deliberately runs to "encode bias." Instead, it is useful to trace the path bias travels, step by step, so you can spot the entry point.

**Tracing the bias path for any AI system — seven steps:**

1. **Identify the training data source.** Where did the data come from? Who collected it? When?
2. **Check for historical context.** Does the period or environment the data was collected from reflect known inequalities?
3. **Check for selection.** Who is represented? Who is missing? Is the absence meaningful?
4. **Check for labelling.** Who attached the tags? What instructions did they follow? Were they culturally homogeneous?
5. **Check for aggregation.** Are groups being combined that should be treated separately?
6. **Check for feedback.** Has this AI already been deployed? Is new training data coming from its own past outputs?
7. **Look for the cognitive bias layer.** At each step above, which human cognitive biases (9.3–9.5) could have influenced the decisions made?

This seven-step trace does not fix the bias — that requires technical and organisational interventions covered in later topics — but it makes the encoding path visible [3].

## 7. Real-World Patterns

The four encoding mechanisms are not theoretical. They show up in AI systems deployed at scale [1][3].

**Hiring AI:** Multiple companies found their AI hiring tools had learned to down-rank women's resumes because historical hiring data reflected male-dominated workforces. Historical bias and labelling bias combined [1].

**Credit scoring:** Algorithmic credit scoring has produced racially disparate outcomes even when race is not an explicit input variable. Historical inequality in wealth and access had already encoded the disparity into **proxy variables** — indirect stand-in features, like zip code and credit history length, that correlate with a protected characteristic without naming it directly [1][2].

**Healthcare prediction:** An AI system used widely in US hospitals to identify patients needing extra care was found to systematically underestimate the needs of Black patients. The system used healthcare spending as a proxy for health needs — but because Black patients had historically been less likely to receive care, they showed lower spending for the same level of illness. Historical bias encoded through a proxy variable [1][3].

**Content moderation:** Automated moderation AI trained on English-language data performs poorly on other languages (selection bias). It also flags African American Vernacular English at higher rates than Standard American English for equivalent content (labelling bias from predominantly non-AAVE-speaking labellers) [2][3].

These examples span healthcare, finance, criminal justice, employment, and platform moderation — sectors where biased AI decisions affect millions of people's real lives.

## 8. Best Practices

These are awareness practices for anyone who uses AI outputs or produces data that could train AI. Full technical mitigation comes later in the curriculum.

**For users of AI systems:**

| Situation | What to watch for |
|---|---|
| AI makes a decision about a person | Ask: was the training data historically representative? |
| AI output is used to create new data | Watch for the feedback loop — the AI may be validating itself |
| AI performs differently for different groups | Suspect selection bias or aggregation bias |
| AI labels or scores content at scale | Suspect labelling bias from the annotation workforce |

**For anyone handling data that might train AI:**

- Treat labelling instructions as high-stakes documents. Vague instructions produce inconsistent labels; inconsistent labels produce noisy, biased models.
- Audit representation before you build. Count who is and is not in your dataset before training begins.
- Separate training data from AI-generated outputs. Do not let the model's predictions become labels for the next version without human review.
- Apply the confirmation bias check from 9.3: before finalising data collection choices, ask "what would I see if my assumption were wrong, and am I actively looking for it?"

## 9. Hands-On Exercise

**Bias trace on a familiar AI:**

Pick one AI tool you use or have heard of — a recommendation algorithm, a chatbot, a spam filter, or an autocomplete system.

1. Write one sentence describing what training data that system probably used.
2. Apply steps 1–7 from the bias trace in Section 6. Write one sentence per step.
3. Identify which encoding mechanism (labelling, historical, selection, feedback loop) is most likely present.
4. Write one sentence describing a real-world harm that could result if the bias goes uncorrected.

No special tools needed — this is a reasoning exercise. The goal is to practise seeing the encoding path rather than treating AI outputs as neutral facts.

## 10. Key Takeaways

- **Bias enters AI through human decisions, not machine intention.** The four main routes are labelling bias (prejudiced tags), historical bias (accurate records of an unfair past), selection bias (unrepresentative data collection), and feedback loop amplification (AI outputs becoming future training data).
- **Accurate data is not the same as fair data.** A dataset can faithfully record history and still encode discrimination — because the history itself was discriminatory.
- **Feedback loops are the amplifier.** A small initial bias, cycled through deployment and re-training, can grow into a large structural disparity that looks like objective evidence.
- **Cognitive biases in practitioners make encoding worse.** Confirmation bias (9.3) shapes how data is collected and reviewed; automation bias (9.5) prevents humans from catching the feedback loop in time.
- **The encoding path is traceable.** Following the seven-step trace makes invisible bias visible — which is the prerequisite for any corrective action.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
