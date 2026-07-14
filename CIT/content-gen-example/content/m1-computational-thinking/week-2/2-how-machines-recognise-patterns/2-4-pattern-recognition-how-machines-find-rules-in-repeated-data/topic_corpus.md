---
topic_id: "2.4"
title: "Pattern recognition — how machines find rules in repeated data"
position_in_module: 1
generated_at: "2026-06-16T00:00:00Z"
resource_count: 3
---

# 1. Pattern recognition — how machines find rules in repeated data — Topic Corpus

## 2. Prerequisites

- **1.4** — Pattern recognition (surface introduction): the idea that humans and machines look for regularities.
- **2.1** — Specification writing: testable, bounded, observable, actionable properties.
- **2.3** — Six-component specification checklist: inputs, expected outputs, failure conditions, success criteria.

## 3. Learning Objectives

- Explain the difference between a rule-based system and a pattern-recognition system in plain terms.
- Describe how a machine learns rules from repeated examples (training on labeled data).
- Define the terms **feature**, **label**, and **classification** as used in pattern recognition.
- Explain why a machine trained on data gives probabilistic (not certain) outputs.
- Describe at least two consequences of probabilistic outputs for writing specifications.
- Identify whether a given specification is appropriately bounded for an AI system whose output is a probability.

## 4. Introduction

You already know that pattern recognition means finding regularities — spotting that something keeps happening the same way [1]. In Week 1, the example was a human looking at many images of cats and noticing what makes a cat a cat: pointy ears, whiskers, a certain shape.

Now ask a harder question: how does a *machine* do the same thing, without any human hand-coding every rule? The answer is that it looks at many, many repeated examples and extracts the rules itself. That process is the subject of this topic.

Understanding it matters right now because your upcoming assessment (A1, Specification Portfolio) asks you to write specifications for AI-powered tasks. A specification that works fine for a calculator — "output is always 42 when you input 6 × 7" — breaks badly when applied to a pattern-recognition system whose answer is never guaranteed to be exactly right. You need to understand *why* AI outputs work differently before you can write specifications that handle them properly.

## 5. Core Concepts

### 5.1 Rule-based systems vs pattern-recognition systems

Before AI, programmers handled decisions by writing rules by hand. A **rule-based system** — also called an expert system — is a program where a human expert writes every decision as an explicit IF/THEN instruction [3].

Example of a hand-written rule:

> IF the email contains the word "lottery" AND the sender is unknown → mark as spam.

This works, but only as far as the human's rules reach. If spammers start spelling it "l0ttery", the rule fails immediately — nobody updated it. Writing complete rules for a complex real-world problem turns out to be extremely hard [1].

A **pattern-recognition system** takes a different approach. Instead of hand-writing rules, you show the system thousands of examples. The machine studies those examples and figures out the rules itself. The rules are not written by a human — they are *discovered* from data [1][3].

| Feature | Rule-based system | Pattern-recognition system |
|---|---|---|
| Who writes the rules? | A human programmer | The machine, from examples |
| What happens when the world changes? | A human must update the rules | The system can be retrained on new examples |
| Can handle messy real-world inputs? | Only what the rules cover | Yes — it generalises from what it has seen |
| Output | Deterministic (same input → same answer always) | Probabilistic (same input → a confidence score) |

The shift from rule-based to pattern-recognition systems is one of the reasons modern AI can handle tasks like understanding speech, reading handwriting, or flagging unusual transactions — tasks where no human could write enough rules to cover every case [3].

### 5.2 How machines learn: training on labeled data

The process of a machine learning rules from examples is called **training** [2].

Training needs two things:

1. **Examples** — a large collection of inputs. These are often called the **training data** or **dataset**.
2. **Labels** — the correct answer for each example, provided by a human in advance.

A **label** is simply the tag that tells the machine what an example actually is [2]. In a spam-detection system, every email in the training data is labeled either "spam" or "not spam". In a handwriting-recognition system, every image of a digit is labeled "0", "1", "2", … "9".

The machine studies the labeled examples over and over — this repetition is the "repeated data" in the topic title. Each time it looks at an example, it adjusts its internal understanding to fit what the label says. After enough examples, the machine has built up a set of internal rules that generally match the labels it was shown [2].

This is different from a human being told the rules. The machine was never told "spam emails tend to mention money". It discovered a version of that rule itself, by observing thousands of examples where "money-related words" and "spam" appeared together.

### 5.3 Features: what the machine actually looks at

A machine cannot look at a raw email or image the way you do. It needs the information broken into measurable pieces. A **feature** is one measurable property of an input that the machine can examine [1][2].

Examples of features:

- For an email: the number of times the word "free" appears; the sender's domain; whether the email contains a link.
- For a photo: the brightness of each pixel; the presence of a horizontal edge at a certain location.
- For a customer transaction: the amount in dollars; the hour of day; the country the transaction was made in.

The machine looks at many features at once. It learns which features tend to predict which label [1]. Features that appear consistently with a label get "weighted" more heavily; features that appear randomly get weighted less. The system of weights the machine builds up is what we informally call the rules it has learned.

Choosing which features to measure is an important design step — it happens before training begins. This step is called **feature selection** or **feature extraction** [2]. Getting it wrong (measuring things that don't matter) makes the learned rules useless.

### 5.4 Classification: the output of pattern recognition

Once the machine has trained on labeled examples, it can look at a *new* example it has never seen before and decide which label fits best. This decision is called **classification** [1][2].

**Classification** — deciding which category a new input belongs to, based on the rules the machine learned during training.

Example: after training on 50,000 labeled emails, the machine sees a brand-new email it has never encountered. It measures the features, applies the rules it learned, and outputs a classification: "spam" or "not spam".

Not every pattern-recognition task is binary (two categories). A digit-recognition system classifies into 10 categories (0–9). A product-recommendation system might classify customer interests into hundreds of categories [1][3].

The key point is that classification is always a *comparison against patterns seen before*. The machine cannot handle situations that are completely unlike anything in its training data. This is one reason why the quality and coverage of training data matters so much [2].

### 5.5 Why outputs are probabilistic, not deterministic

This is the most important concept in this topic for your specification work.

A **deterministic** system always produces the same output for the same input, with no uncertainty. A calculator is deterministic: 6 × 7 is always 42 [3].

A pattern-recognition system is **probabilistic** — it produces a *confidence score* or *probability* rather than a guaranteed answer [3].

Why? Because the machine is not following a perfect set of rules. It is generalising from examples it has seen to inputs it has not seen before. There will always be cases where the learned rules are ambiguous — where the features of a new input sit somewhere between two categories.

When a machine classifies an email as spam, it might say internally: "I am 87% confident this is spam." If the threshold is set at 80%, it marks it spam. But it is not 100% certain. Another email might score 52% — it could go either way [3].

This is not a flaw. It is an honest reflection of how pattern recognition works: the machine is matching inputs to patterns, not solving equations. Uncertainty is inherent [1][2].

Consequences for you as someone who writes specifications:

- You cannot write "the system must always classify this email correctly." Correct for whom? Against what ground truth? The machine does not have access to ground truth on new data.
- You can write "the system must classify spam emails with a precision of at least 90% when tested against a labeled validation set of 1,000 emails."
- The second version is testable, bounded, and accounts for probabilistic output. The first version is not testable for an AI system.

This is the bridge back to topics 2.1–2.3: the four properties (testable, bounded, observable, actionable) and the six-component checklist were designed with exactly this kind of system in mind.

### 5.6 The training–deployment gap

One practical consequence of probabilistic outputs is that a machine trained on past data may perform differently on future data. The data the machine sees after it is deployed (put into production) may differ from the data it was trained on [2][3].

If the pattern of spam emails changes after training — new keywords, new tactics — the machine's learned rules become less accurate over time. This is called model drift and is covered in a later module.

For now, the key takeaway is: a specification for an AI system should state *when* and *on what test data* a performance claim is being made. "Achieves 95% accuracy" means very little without specifying the test set and the date.

## 6. Implementation

Pattern recognition follows a repeatable sequence of steps. You do not need to implement this yourself right now, but understanding the sequence helps you write better specifications — because each step is a place where something could go wrong, and your specification should reflect that.

**The five steps of a pattern-recognition pipeline:**

1. **Collect examples.** Gather a dataset of inputs — emails, images, transactions, sentences. The larger and more representative, the better [2].

2. **Label the examples.** A human (or group of humans) tags each example with its correct category. This is slow, costly, and the most common source of errors in the pipeline [2].

3. **Extract features.** Break each example into the measurable properties the machine will examine. Decide which features matter. Discard noise [1][2].

4. **Train the model.** Show the labeled, feature-extracted examples to the machine repeatedly. Let it adjust its internal rules until it classifies the training examples well [2].

5. **Classify new inputs.** Deploy the trained model. Give it new, unseen examples. It applies the learned rules and outputs a classification with a confidence score [1][2][3].

When you write a specification for an AI task, you are almost always specifying the behaviour of **step 5** — the classification of new inputs. But steps 1–4 affect whether step 5 is reliable. A good specification acknowledges this by stating the conditions under which the performance claim holds.

## 7. Real-World Patterns

Pattern recognition is at the core of almost every AI product you already use [1][3]:

- **Email spam filters.** Every email client trains on labeled examples of spam and non-spam, extracts features (words, sender behaviour), and classifies new emails [3].
- **Face unlock on your phone.** The phone trains on labeled images of your face. It extracts features (distances between facial landmarks). When you hold it up, it classifies: "this face matches" or "this face does not match" [1][2].
- **Fraud detection.** Banks train on labeled past transactions (fraud / not fraud). The model watches for patterns in new transactions that resemble the fraud examples [3].
- **Voice assistants.** When you say "Hey Siri" or "OK Google", the device is classifying your audio: does this audio match the wake-word pattern? It learned the pattern from thousands of recorded examples [1].
- **Medical diagnosis support.** A model trained on thousands of labeled medical images can flag patterns that might indicate disease — not with certainty, but with a confidence score for the doctor to review [3].

In every case, notice the same structure: labeled training data → features → learned rules → probabilistic classification on new inputs.

## 8. Best Practices

### When writing specifications for AI pattern-recognition systems

**Do this:**
- State the expected output as a rate or threshold, not a guarantee. Example: "The system must achieve a spam-detection precision of at least 85%."
- Name the test dataset. Example: "…measured on a held-out validation set of 500 labeled emails not seen during training."
- Include a failure condition. Example: "If precision falls below 75%, the system must route flagged emails to human review rather than automatic deletion."
- State success criteria in observable, measurable terms. Example: "A batch of 100 manually labeled test emails is run; at least 85 of the 100 spam emails are correctly classified."

**Avoid this:**
- "The system must always correctly identify spam." — Not testable for a probabilistic system.
- "The AI must be accurate." — "Accurate" is undefined. Accurate to what level? On what data?
- "The system must never make a mistake." — Impossible to guarantee for any pattern-recognition system.

### When evaluating any AI claim

| Question to ask | Why it matters |
|---|---|
| What was it trained on? | Training data shapes what patterns the model learned. |
| How was accuracy measured? | A test set of 10 examples is meaningless. |
| How recent is the training data? | Model drift means past performance may not hold today. |
| What happens when it is wrong? | Probabilistic systems will be wrong sometimes. The spec must say what to do. |

## 9. Hands-On Exercise

Look at the spam filter in any email application you use (Gmail, Outlook, or similar).

1. Find five emails that were correctly moved to your spam folder. List two or three features each email has in common (words, sender type, content style).
2. Find one email that ended up in spam by mistake (a false positive). What features might have caused the system to misclassify it?
3. Rewrite the following vague specification as a testable, bounded one: "The spam filter must work well." Use the six-component checklist from topic 2.3 as your guide.

This exercise connects pattern recognition directly to specification writing — the two skills this session is building together.

## 10. Key Takeaways

- A pattern-recognition system discovers rules from labeled examples; a rule-based system has rules written in by a human. The key difference is where the rules come from.
- Training means showing a machine thousands of labeled examples repeatedly so it can build its own internal rules. Features are the measurable properties it uses to learn.
- Classification is the machine's output: assigning a new input to the category whose learned pattern it most closely matches.
- Pattern-recognition systems give probabilistic outputs — a confidence score, not a guarantee. This is not a bug; it is how learning from data works.
- Because outputs are probabilistic, specifications for AI systems must state performance thresholds, test conditions, and fallback behaviours — not absolute guarantees.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
