---
topic_id: "4.2"
title: "Fine-tuning — adapting a foundation model on domain-specific data"
position_in_module: 2
generated_at: "2026-06-16T00:00:00Z"
resource_count: 3
---

# 1. Fine-tuning — adapting a foundation model on domain-specific data — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **4.1 — Foundation models — trained once at scale, usable for many tasks:** introduced the concept of a foundation model, what "trained once at scale" means, and the idea of adaptation as a layer on top of the base model. Terms such as foundation model, adaptation, multimodal model, and generalisation from broad training are used here without re-defining them.

Topic 4.1 is a hard prerequisite — fine-tuning is one of the adaptation methods introduced there and explored fully here.

## 3. Learning Objectives

By the end of this topic, you should be able to:

1. Define fine-tuning in plain language and explain how it differs from training a model from scratch.
2. Explain what "domain-specific data" means and give two examples of a domain and its corresponding data.
3. Describe the general sequence of steps involved in fine-tuning a foundation model.
4. Identify at least two real-world scenarios where fine-tuning is the appropriate adaptation choice.
5. Explain the trade-off between fine-tuning and using a foundation model without any adaptation (zero-shot use).
6. Recognise when fine-tuning may not be the right tool — for example, when the task changes frequently or when labelled data is unavailable.

## 4. Introduction

Imagine you hire a highly educated generalist — someone who has read widely across law, medicine, finance, science, and literature. On day one, they can hold a conversation on almost any topic. But if you need them to handle your hospital's patient intake process, there is a gap: they do not know your hospital's terminology, your specific forms, or the way your staff communicates. You do not send them back to university for four years. Instead, you give them a focused training period — your hospital's procedures, your document templates, your frequently asked questions — and after a few weeks they are effective in your specific context.

Fine-tuning works the same way for AI models.

A foundation model, as introduced in topic 4.1, is trained once on enormous, general data. It knows a lot about language and the world in general. But "a lot about everything in general" is not always what a business needs. A legal firm needs a model that understands contract clauses. A hospital needs one that interprets clinical notes. A software company needs one that writes code in their internal style. [1]

Fine-tuning is the process of taking a foundation model that already exists and continuing its training — but now on a much smaller, focused dataset that reflects the specific domain or task you care about. The result is a model that keeps its broad general knowledge and adds specialist capability on top. [2]

This topic explains what fine-tuning is, how it works at a conceptual level, when to use it, and what its limits are. It is one of several adaptation methods covered in week 4; the others — RAG, agents, and tool use — are introduced in topics 4.3–4.5.

## 5. Core Concepts

### 5.1 What is fine-tuning?

**Fine-tuning** — the process of taking a pre-trained foundation model and continuing its training on a new, smaller, domain-specific dataset so that the model's behaviour is adjusted to better suit a particular task or domain. [1]

To understand fine-tuning, it helps to recall how the original training worked (from topic 4.1 and earlier topics). During pre-training, the model was exposed to an enormous dataset — billions of web pages, books, and other text — and its internal parameters (the billions of numerical settings that store what the model has learned) were adjusted repeatedly to get better at predicting patterns in that data. That process ran for weeks on specialised hardware and cost millions of dollars.

Fine-tuning does not repeat that entire process. Instead, it starts where pre-training ended — it picks up the already-trained model and runs additional training on the new, smaller dataset. Because the model already has a strong general foundation, this additional training is much shorter, cheaper, and requires far less data. [2]

Think of it this way: the model already "knows" language and concepts in general. Fine-tuning teaches it the vocabulary, patterns, and priorities of a specific domain. [3]

A few terms introduced in this section:

- **Pre-trained model** — the foundation model as it exists after its original large-scale training; the starting point for fine-tuning. The word "pre-trained" simply means "already trained" — it was trained before you started fine-tuning it. [1]
- **Domain** — a specific area of knowledge or activity, such as healthcare, legal services, finance, or software engineering.
- **Domain-specific data** — training examples drawn from that domain; for example, medical records and clinical guidelines (healthcare domain), or contract templates and case summaries (legal domain). [1]

### 5.2 How fine-tuning differs from pre-training

It is important not to confuse fine-tuning with training a model from scratch. The table below makes the contrast clear:

| Aspect | Pre-training (original training) | Fine-tuning |
|---|---|---|
| Starting point | Random parameters — the model knows nothing | A fully trained foundation model |
| Dataset size | Massive — trillions of words or equivalent | Small to medium — thousands to millions of examples |
| Time and cost | Weeks of compute, tens of millions of dollars | Hours to days of compute, a fraction of the cost |
| Who does it | Large technology companies, research labs | Businesses, developers, teams with domain expertise |
| Goal | Teach the model language, concepts, and general knowledge | Adjust the model's behaviour for a specific domain or task |

[1][2]

The key insight is that fine-tuning is only possible because pre-training happened first. The foundation is what makes the fine-tuning fast and affordable. Without a pre-trained model to start from, you would need the same massive resources as the original training run. [2]

### 5.3 What "domain-specific data" means

The phrase "domain-specific data" appears in the topic title and is central to understanding fine-tuning.

**Domain-specific data** is a set of examples — usually pairs of input and desired output, or collections of relevant documents — that represent the target domain and show how the model should behave in it. [1]

Examples across different domains:

- **Customer support (e-commerce company):** Thousands of past customer enquiries paired with the approved responses the company gives. The model learns the company's tone, policies, and product-specific language.
- **Healthcare:** Clinical notes, medical guidelines, and question-answer pairs written by medical professionals. The model learns clinical terminology and how to interpret patient records.
- **Legal:** Contracts, court judgements, and legal Q&A pairs. The model learns formal legal language and jurisdiction-specific conventions.
- **Software engineering:** A company's internal codebase, documentation, and code-review comments. The model learns the team's coding style and internal API names. [3]

A key characteristic of good fine-tuning data: it is **labelled** — meaning each example shows not just an input, but the correct or preferred output. The model learns by comparing its own output to the labelled correct output and adjusting its parameters to reduce the gap. [2]

**Labelled data** — training examples where a human (or another trusted process) has already provided the correct answer or desired output. For example: a customer question paired with the correct answer, or a medical note paired with the correct diagnostic category. [2]

The quality and relevance of the labelled data is the single biggest factor in whether fine-tuning succeeds. A model fine-tuned on poor-quality or off-topic data will perform poorly — no matter how good the starting foundation model was. [3]

### 5.4 The fine-tuning process — conceptual steps

Fine-tuning follows a recognisable sequence. You do not need to know how to implement each step technically (this course has no coding), but understanding the sequence helps you reason about what fine-tuning involves and what can go wrong. [1]

**Step 1 — Choose a foundation model.**
You start with a pre-trained foundation model that is appropriate for your domain. If your task involves text, you choose an LLM (Large Language Model). If it involves images and text together, you choose a multimodal model. The choice matters: a model pre-trained on general web text will adapt more readily to language tasks than to image tasks. [1]

**Step 2 — Assemble a domain-specific dataset.**
You collect, clean, and label examples from your target domain. This is often the most time-consuming part. The dataset does not need to be enormous — a few thousand high-quality examples can be enough — but it must be representative of the real inputs the model will receive and the real outputs you want. [2][3]

**Step 3 — Run the additional training.**
You feed the domain-specific dataset into the pre-trained model and run additional training rounds. The model's parameters are updated — but only slightly, and guided by the new examples. The general knowledge from pre-training is largely preserved; the domain-specific patterns are added on top. [1][2]

**Step 4 — Evaluate the fine-tuned model.**
You test the fine-tuned model against examples it has not seen before — a held-out test set. You measure whether its outputs are better for your domain than the original foundation model would have been. If the results are good enough, the fine-tuned model is ready for use. [2]

**Step 5 — Deploy and monitor.**
The fine-tuned model is integrated into an application or service. Ongoing monitoring checks that it continues to perform well as real-world inputs arrive and as the domain evolves.

### 5.5 Why fine-tuning improves performance in a domain

A natural question: why does continuing training on a small domain-specific dataset improve performance? Why doesn't the model simply forget what it already knows?

The answer has two parts.

First, the model does not start from a blank state — its parameters already encode broad knowledge. The fine-tuning process adjusts those parameters in ways that emphasise domain-relevant patterns without overwriting the rest. Think of it as recalibrating an instrument, not rebuilding it from parts. [2]

Second, the model learns a new kind of signal from labelled domain data: what "correct" looks like in this specific context. Before fine-tuning, the model might produce technically accurate but tonally wrong, or too generic, responses for a specialist domain. After fine-tuning, it has learned from examples of what the domain's users and experts actually consider a good response. [3]

There is a risk called **catastrophic forgetting** — a phenomenon where a model trained heavily on new data loses some of its previously learned general abilities. Good fine-tuning practice minimises this risk by using a small, targeted dataset and careful training settings. This risk is why fine-tuning is not simply "more training" — it requires care. [2]

**Catastrophic forgetting** — the tendency of a model to partially overwrite previously learned knowledge when trained intensively on new data. Fine-tuning mitigates this by keeping the new dataset small and targeted. [2]

### 5.6 Fine-tuning vs. using a model without adaptation (zero-shot use)

Before fine-tuning was widely available, many users simply took a foundation model and sent it a task directly — with no adaptation at all. This is called **zero-shot use** (or "using the model out of the box").

**Zero-shot use** — prompting a foundation model with a task it was never specifically trained or adapted for, relying entirely on the general knowledge from pre-training. [2]

Zero-shot use works surprisingly well for general tasks. But it has limitations in specialist domains:

- The model may not know the specific terminology of the domain.
- It may not follow the organisation's preferred tone or format.
- It may produce plausible-sounding but inaccurate specialist content — a known failure mode of LLMs sometimes called a "hallucination."

Fine-tuning directly addresses these limitations by teaching the model the domain's specifics. [1][3]

The trade-off is cost and effort: fine-tuning requires collecting, cleaning, and labelling data, plus compute time. Zero-shot use requires neither. The choice depends on how important specialist accuracy is and whether the organisation has the data and capacity to fine-tune. [2]

**Hallucination** — when an AI model produces output that sounds confident and fluent but is factually incorrect or fabricated. Hallucinations are more common in specialist domains where the model's general training data was sparse. Fine-tuning on accurate domain data can reduce (but not eliminate) hallucinations in that domain. [3]

## 6. Implementation

Fine-tuning is a technical process that in practice is carried out by developers or data scientists using cloud platforms. In this course you will not write code, but understanding the conceptual workflow helps you evaluate tools and proposals. [1]

**A typical cloud-assisted fine-tuning workflow (conceptual):**

1. **Select a base model.** On platforms such as AWS SageMaker JumpStart, Azure AI Studio, or Google Vertex AI, you choose a pre-trained foundation model from a catalogue. [1]
2. **Upload your dataset.** You prepare your labelled domain-specific data in a supported format (typically a structured file of input-output pairs) and upload it to the platform's storage.
3. **Configure training settings.** You specify how many rounds of training to run (called **epochs** — one epoch means the model has processed every example in the dataset once), and other settings that control how strongly the parameters are updated.
4. **Launch the fine-tuning job.** The platform runs the training on its infrastructure. Depending on the dataset size and model size, this can take anywhere from minutes to several hours.
5. **Evaluate outputs.** You test the resulting model against held-out examples and compare results to the original foundation model.
6. **Deploy the fine-tuned model.** Once satisfied, you make the model available for use in an application — often as an API (Application Programming Interface) endpoint that other software can call.

[1][2]

**Epoch** — one complete pass through a training dataset. Fine-tuning typically uses a small number of epochs (often 3–10) to avoid catastrophic forgetting and overfitting. [2]

**Overfitting** — when a model learns the training examples too precisely and performs well on those specific examples but poorly on new, unseen inputs. It is a risk when fine-tuning on a very small dataset. Using a held-out test set — examples kept separate from training — helps detect overfitting. [2][3]

AWS SageMaker JumpStart, for example, provides a catalogue of pre-trained models with a guided fine-tuning interface that abstracts many of the low-level technical steps, making domain adaptation accessible to teams that are not AI specialists. [1]

## 7. Real-World Patterns

Fine-tuning is already in widespread use across industries. The pattern is consistent: an organisation has a substantial volume of domain-specific data, a clear use case, and accuracy requirements that are too demanding for zero-shot use alone. [1]

**Healthcare**
Hospitals and research institutions fine-tune LLMs on clinical notes, medical literature, and diagnostic guidelines to build tools that assist clinicians. A fine-tuned model trained on radiology reports, for example, can help draft preliminary interpretations faster than a radiologist reading from scratch — while the radiologist retains final sign-off. The model's domain-specific training means it uses correct anatomical terminology and clinical phrasing. [3]

**Legal services**
Law firms and legal-tech companies fine-tune models on contracts, legislation, and case law to build tools that can summarise documents, identify unusual clauses, or answer questions about jurisdiction-specific rules. A zero-shot general model would lack knowledge of specific legal precedents and local legal terminology. [2][3]

**Customer support**
Companies fine-tune models on their own support ticket history — past customer questions paired with approved agent responses. The result is a chatbot that knows the company's products, policies, and tone far better than a general model could. [1]

**Code and software development**
Technology companies fine-tune models on their internal code repositories, style guides, and documentation to build coding assistants that understand the company's specific frameworks and naming conventions — something a general model trained on public code cannot do as well. [2]

**India-specific context**
Several Indian enterprises and government initiatives are exploring fine-tuning to adapt general LLMs to Indian languages, regional healthcare datasets, and agricultural advisory applications — extending access to AI tools in contexts where general English-centric models fall short. [3]

## 8. Best Practices

Fine-tuning is powerful but has common pitfalls. These principles apply whether you are evaluating a vendor's proposal or thinking through a fine-tuning project at your organisation.

**Start with a strong base model.**
The quality of the fine-tuned model is bounded by the quality of the starting foundation model. Begin with the best base model you can access for your modality and language. A weak base model produces a weak fine-tuned model. [1]

**Invest in data quality over data quantity.**
A common mistake is collecting as much data as possible without ensuring it is accurate, representative, and well-labelled. A few thousand high-quality, clean, correctly labelled examples will outperform tens of thousands of noisy, inconsistent ones. [2][3]

**Keep the fine-tuning dataset targeted.**
The domain-specific dataset should closely reflect the real inputs the deployed model will receive. Fine-tuning on data that is only loosely related to your task produces a model that is only loosely adapted. [1]

**Always evaluate on held-out data.**
Never judge a fine-tuned model's quality by its performance on the training examples themselves — that will always look good, even if the model is overfitting. Reserve a portion of your dataset for testing, and evaluate on that held-out set only. [2]

**Monitor after deployment.**
Domain language evolves. New products, new regulations, new terminology — these can make a fine-tuned model go stale over time. Build in a process for periodic evaluation and re-fine-tuning when needed. [1][3]

**Know when fine-tuning is not the right tool.**
Fine-tuning requires labelled data and is most cost-effective when the task and domain are stable. If your requirements change frequently, or if you need the model to access up-to-date information that post-dates its training, other adaptation methods are more appropriate — those are covered in topics 4.3–4.5. [2]

## 9. Hands-On Exercise

**Compare zero-shot and fine-tuned outputs using a simple rubric**

This exercise connects the §5.6 comparison (zero-shot use vs. fine-tuning) to the lab activity for week 4: designing an evaluation rubric and scoring two AI approaches against it.

1. **Choose a task and a domain.** Pick one short task from a domain you know — for example: "Summarise this medical report in two sentences" or "Explain this legal clause in plain language."

2. **Draft three evaluation criteria.** Using the rubric framework from topic 4.7, write three criteria you would use to judge whether the output is good. For each criterion, write a one-sentence description of what a strong output looks like versus a weak one. Example criteria: accuracy, appropriate tone, domain-specific terminology used correctly.

3. **Predict the zero-shot result.** Before seeing any output, write one sentence predicting how a general foundation model (without fine-tuning) would perform on your task using your three criteria. What is the model likely to get right? What is it likely to miss?

4. **Predict the fine-tuned result.** Write one sentence predicting how a fine-tuned version of the same model — trained on domain-specific data for your chosen domain — would perform differently.

5. **Reflect on the trade-off.** Based on §5.6 and your predictions: under what conditions would fine-tuning be worth the cost of collecting labelled data and running additional training? Under what conditions would zero-shot use be sufficient?

You do not need to run actual models for this exercise — the goal is to apply the conceptual distinction from §5.6 to a concrete rubric-based comparison. The rubric design skill from topic 4.7 and the evidence-based recommendation skill from topic 4.8 are what make this exercise actionable.

## 10. Key Takeaways

- **Fine-tuning** is the process of continuing a foundation model's training on a smaller, domain-specific dataset — it is adaptation, not starting over. The expensive pre-training is already done; fine-tuning builds a specialist layer on top of it. [1]
- **Domain-specific data** is the central ingredient: carefully collected and labelled examples from the target area of expertise. Data quality matters more than data quantity. [2][3]
- Fine-tuning follows a consistent sequence: choose a base model, assemble labelled data, run additional training, evaluate on held-out examples, and deploy. Cloud platforms such as AWS SageMaker JumpStart make this workflow accessible to teams that are not AI specialists. [1]
- Fine-tuning outperforms zero-shot use in specialist domains because it teaches the model the domain's specific language, tone, and correct outputs — reducing generic responses and domain hallucinations. [2][3]
- Fine-tuning has limits: it requires labelled data, it is most cost-effective for stable tasks, and it carries risks such as catastrophic forgetting and overfitting if not done carefully. When requirements change frequently or up-to-date information is needed, other adaptation methods — RAG, agents, tool use — covered in topics 4.3–4.5 may be more appropriate. [2]

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
