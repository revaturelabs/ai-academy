---
topic_id: "9.3"
title: "Confirmation bias — seeking information that confirms existing beliefs"
position_in_module: 1
generated_at: "2026-06-12T00:00:00Z"
resource_count: 3
---

# 1. Confirmation Bias — Topic Corpus

## 2. Prerequisites

- **Topic 9.1 — System 1 thinking:** Introduced automatic, fast, heuristic-driven processing — the mental autopilot that runs beneath conscious attention; confirmation bias is largely a product of this automatic layer.
- **Topic 9.2 — System 2 thinking:** Introduced deliberate, effortful processing and the concept of cognitive load; System 2 is the mode that *should* catch confirmation bias, but as this topic shows, it often does not.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** confirmation bias in plain language and identify it as a systematic (not random) tendency of human cognition.
2. **Describe** the three mechanisms through which confirmation bias operates: selective search, biased interpretation, and selective memory.
3. **Explain** why confirmation bias is automatic and effortless by connecting it to System 1 heuristic processing introduced in topic 9.1.
4. **Recall** Peter Wason's 2-4-6 task as experimental evidence that people seek confirming rather than disconfirming evidence.
5. **Apply** the concept of confirmation bias to the context of evaluating AI outputs, identifying at least one way the bias can cause a practitioner to misjudge an AI system's quality.
6. **Recognise** that awareness of a bias does not automatically eliminate it, and that motivated reasoning can persist even under deliberate (System 2) thinking.

## 4. Introduction

Picture this: a student in a coding bootcamp starts using an AI code assistant for the first time. After a few sessions they form an opinion — "this tool is pretty reliable." From that moment on, something subtle happens. When they test the tool, they reach for the kinds of problems they already feel comfortable with — the ones where they can judge the output quickly. When the output looks almost right, they assume it is right. Later, chatting with a classmate, they remember the times the tool worked brilliantly but draw a blank on the two occasions it gave them completely wrong advice.

That sequence — testing only familiar ground, reading borderline outputs charitably, and remembering the wins more than the losses — is **confirmation bias** in action. They were not being dishonest or careless. Their brain was doing exactly what human brains are built to do: look for patterns that confirm what they already believe.

Confirmation bias is one of the most thoroughly studied tendencies in cognitive psychology. It shows up in medical diagnoses, legal decisions, financial forecasting, and — as you will see in this topic — in how practitioners evaluate AI systems. Understanding it is the first step toward compensating for it, which is why it opens this module on cognitive biases and AI oversight [1][2].

## 5. Core Concepts

### What is confirmation bias?

Confirmation bias is the tendency to **seek out, interpret, and remember information in a way that confirms beliefs you already hold** [1]. It is not about being stubborn or dishonest. It is a systematic quirk in how the human brain gathers and processes evidence — and it affects virtually everyone, regardless of intelligence or education [1].

The word *systematic* is important. A random error in judgment is unpredictable — sometimes it makes you overconfident, sometimes underconfident. Confirmation bias is not random: it consistently pushes in one direction, toward whatever you already believe. That one-directional pull is what makes it dangerous in high-stakes decisions.

### The three mechanisms

Researchers have identified three distinct ways confirmation bias shows up in practice [1][2]:

#### Mechanism 1 — Selective search

When people look for information to test a belief, they tend to search for *confirming* evidence rather than *disconfirming* evidence. In other words, instead of asking "what would prove me wrong?", the natural impulse is to ask "what supports what I already think?" [1][2].

The classic experimental demonstration of this is the **Wason 2-4-6 task**, designed by psychologist Peter Wason in the 1960s [2]. Participants are told that the sequence "2, 4, 6" follows a secret rule. Their job is to discover the rule by proposing other number sequences; the experimenter tells them whether each new sequence follows the rule or not.

Most people quickly hypothesize "consecutive even numbers" (or a similar pattern) and then test sequences like "8, 10, 12" and "20, 22, 24" — all of which confirm the hypothesis. The actual rule is far broader: "any ascending sequence." Participants could discover this quickly by testing sequences that *violate* their hypothesis — like "1, 2, 3" or "5, 7, 100." But the overwhelming majority never try such sequences. They keep gathering confirming evidence and declare confidence in a rule they have not actually tested [1][2].

Wason's result was striking because the participants were not irrational in general — they were simply defaulting to confirmatory search rather than falsifying search. The same instinct shows up whenever someone "tests" a belief by looking only for supporting cases.

#### Mechanism 2 — Biased interpretation

Even when people encounter the same piece of evidence, they often interpret it differently depending on whether it supports or challenges their existing belief. Ambiguous evidence gets read as confirming; evidence that clearly challenges a belief gets scrutinised more heavily, dismissed as an exception, or explained away [2].

Imagine two people evaluating an AI-generated summary of a legal document. One believes the AI is trustworthy; the other is sceptical. When the summary contains a mildly imprecise sentence, the trusting evaluator reads it as "close enough — the tool got the gist right." The sceptical evaluator flags it as "a sign the AI doesn't really understand legal language." Both interpretations come from the same sentence. The difference is not the evidence — it is the prior belief each person brought to the table [2].

This mechanism explains why showing someone "the facts" rarely changes entrenched views: the same facts get processed through different interpretive lenses shaped by prior belief.

#### Mechanism 3 — Selective memory

Confirmation bias also operates in how we remember past events. People tend to recall information that is consistent with their beliefs more readily than information that contradicts those beliefs [1]. This is not deliberate forgetting — it is a byproduct of how memory works. Experiences that fit an existing mental model are stored more efficiently and retrieved more easily.

A practitioner who believes an AI tool is reliable will, when asked to reflect on their experience, naturally call up the times it worked well. The failures are not erased — but they are harder to retrieve, less vivid, and less likely to influence the overall assessment. Over time, this selective memory reinforces the original belief, making it feel more evidence-based than it actually is.

### Why confirmation bias is so automatic

You may be thinking: "Surely if I know about this bias I would just check myself — use System 2, slow down, and be thorough." That is a reasonable instinct, but research suggests it is not that simple [1][2].

The root cause of confirmation bias lies in the same cognitive architecture covered in topic 9.1: **System 1 processing**. System 1 is fast and automatic. It is constantly scanning the environment for patterns that match existing mental models. When a piece of incoming information matches a familiar pattern, System 1 flags it as relevant and trustworthy. When information contradicts the pattern, System 1 deprioritises it. This is enormously useful in everyday life — it would be exhausting to weigh every piece of evidence from scratch. But this efficiency comes at a cost: the pattern-matching is directionally biased [1].

There is also a concept called **cognitive economy**: the brain works to minimise mental effort. Confirming an existing belief requires less cognitive work than revising it. You do not have to restructure your mental model, reconcile conflicting information, or deal with the discomfort of uncertainty. Confirmation bias is, in part, the brain taking the path of least resistance [1].

### Limits of System 2 correction

Topic 9.2 introduced System 2 as the deliberate, analytical mode of thinking. In theory, System 2 should catch and correct confirmation bias: slow down, seek disconfirming evidence, interpret evidence neutrally, recall failures as well as successes. In practice, there is a catch [2].

Even when System 2 is engaged, a phenomenon called **motivated reasoning** can distort its outputs. Motivated reasoning occurs when someone unconsciously uses their analytical capacity not to find the truth but to build the best-possible case for what they already believe [2]. The critical thinking looks rigorous on the surface — they are evaluating evidence, constructing arguments — but the goal is defence of the prior belief, not impartial assessment. The result is that more intelligent or analytically skilled individuals are not necessarily less prone to confirmation bias; in some studies, they are better at constructing sophisticated justifications for their existing views [1].

This does not mean System 2 is useless — deliberate reflection does help. But it does mean that simply telling yourself "think carefully" is not a reliable cure. Structured methods are needed, and those will be explored in later topics.

### Scale and universality

One important point worth making explicitly: confirmation bias is not a flaw in poorly educated, low-intelligence, or particularly emotional people. It is a feature of normal human cognition [1]. Every person — including trained scientists, experienced engineers, expert clinicians — shows it in experimental settings. Intelligence, domain expertise, and even training in critical thinking reduce its impact somewhat but do not eliminate it. This fact matters because it means dismissing the bias as something that only affects "other people" is itself a form of confirmation bias.

## 6. Worked Example

**Scenario:** A junior developer is evaluating a new AI code assistant before recommending it to their team. They believe, based on early demos, that the tool is strong.

**Step 1 — Selective search in action.**
To test the tool, the developer picks problems from areas they already know well: basic string manipulation, simple sorting algorithms, standard API call patterns. These are tasks where they can judge output quality quickly. They do not pick problems in areas where they have less experience — database query optimisation, concurrency bugs, edge cases in library behaviour — because those are harder to evaluate. The result: the tool is tested only on the ground where it is most likely to succeed, and the developer never realises this.

**Step 2 — Biased interpretation in action.**
One of the generated functions returns a result that is technically correct but uses a deprecated library method. The developer notices the deprecated method but thinks: "It still works — the AI just used an older style, which is fine for now." A neutral evaluator might flag this as a signal that the tool's training data is outdated. The developer's interpretation is coloured by the prior belief that the tool is reliable.

**Step 3 — Selective memory in action.**
At the end of the week, the developer writes up their recommendation. They recall five or six examples where the tool produced clean, correct code immediately. They have a vague sense that "there were a couple of rough ones" but cannot remember the details clearly. In their write-up, the wins are vivid and specific; the failures are acknowledged in passing ("occasional minor issues"). The recommendation is strongly positive.

**The outcome:** The team adopts the tool based on a biased evaluation. The tool performs well on routine tasks (what it was tested on) but struggles with the complex cases the developer never probed. The confirmation bias was not dishonesty — it was invisible to the developer throughout the process.

## 7. Common Misconceptions

**Misconception 1: "I don't have confirmation bias — I'm analytical and evidence-driven."**

This is probably the most common response when people first encounter the concept, and it is also the one most clearly contradicted by research. Analytical ability and scientific training reduce some effects of some biases in some domains, but no study has found a group of people immune to confirmation bias [1]. In fact, some findings suggest that motivated reasoning — using analytical skills to defend a prior belief — can be *stronger* in people who are more confident in their reasoning ability, because they have more tools to construct a convincing argument for what they already think. The belief that "I'm too smart for this bias" is itself a warning sign.

**Misconception 2: "Confirmation bias only affects opinions and politics — not factual or technical questions."**

Confirmation bias was first formally studied in factual, logical tasks — the Wason 2-4-6 experiment used purely abstract number sequences, not emotionally charged political topics [2]. The bias operates in technical domains just as readily as in social ones. Developers evaluating code tools, analysts assessing model accuracy, engineers judging system reliability — all are susceptible. The emotional temperature of a topic can amplify the bias, but it is not a prerequisite for the bias to appear.

**Misconception 3: "Once you're aware of confirmation bias, you can compensate for it."**

Awareness is genuinely useful — it opens the door to better practices — but it does not switch off the underlying mechanism [1][2]. System 1 processing and cognitive economy operate below conscious awareness. Knowing that your brain defaults to confirmatory search does not automatically make you search for disconfirming evidence. Structured techniques (checklists, adversarial testing protocols, pre-mortems) are more effective than unaided self-awareness. Believing that awareness alone is sufficient can create a false sense of security, which is arguably worse than not knowing about the bias at all.

## 8. Connection to AI Context

Confirmation bias does not disappear when a practitioner sits down to evaluate an AI system. In many ways, the AI context makes it more dangerous.

When a practitioner believes an AI system is reliable, they tend to: test it on familiar or easy inputs (selective search), interpret borderline or ambiguous outputs as correct (biased interpretation), and remember successful outputs more vividly than failures (selective memory). When the AI produces a plausible-sounding but wrong answer — which AI systems do with some regularity — System 1 pattern-matching and confirmation bias form a powerful combination: the output *looks* right to a fast, pattern-matching scan, and the evaluator's prior belief fills in the rest [3].

The reverse is equally true. A practitioner who has decided an AI tool is unreliable will find failures everywhere, downplay successes, and arrive at an unfairly negative assessment. In both cases, the evaluation reflects the prior belief as much as the actual evidence [3].

This matters for AI oversight: a practitioner who thinks they are rigorously evaluating a system may actually be constructing evidence for a verdict they already reached. How this bias connects to the way it can become embedded in AI training data is covered in topic 9.6. The Judgment Framework introduced in topics 9.7–9.9 gives a structured approach designed to counteract exactly this kind of bias.

## 9. Hands-On / Reflection Prompt

Take a few minutes to answer these questions honestly — there are no right or wrong answers, only useful ones:

1. **Think of an AI tool you currently use** (a code assistant, a writing tool, a search feature). What would convince you that this tool is *unreliable*? Write down two or three specific things that would change your mind. Then ask yourself: have you actively looked for any of those things, or have you mostly noticed examples of the tool working well?

2. **Recall a recent case where you evaluated something and concluded it was good** (a tool, a piece of work, a process). Without judging yourself, try to identify whether any of the three mechanisms appeared: Did you look mainly for evidence that it was good? Did you interpret ambiguous signals charitably? Did you find it easier to remember the successes than the failures?

3. **For your domain system** (the system you will analyse in the lab): what are the three hardest questions you could ask it — the ones most likely to expose a failure? If you have not tried those questions yet, what has stopped you?

## 10. Key Vocabulary

| Term | Definition |
|---|---|
| **Confirmation bias** | The tendency to seek out, interpret, and remember information in a way that confirms existing beliefs, rather than challenging them. |
| **Selective search** | The mechanism by which people look for confirming evidence when testing a belief, rather than actively seeking disconfirming evidence. |
| **Biased interpretation** | The mechanism by which ambiguous evidence is read as supporting an existing belief, while challenging evidence receives greater scrutiny or is explained away. |
| **Selective memory** | The mechanism by which information consistent with an existing belief is more easily recalled than information that contradicts it. |
| **Motivated reasoning** | A form of thinking in which analytical effort is unconsciously directed toward defending a prior belief rather than finding the truth; can persist even under deliberate System 2 processing. |
| **Cognitive economy** | The brain's tendency to minimise mental effort; one reason confirmation bias is automatic — confirming an existing belief requires less cognitive work than revising it. |
| **Wason 2-4-6 task** | A classic psychology experiment by Peter Wason in which participants are given a number sequence and asked to discover the rule; demonstrates that people default to confirmatory rather than falsifying search. |
| **Disconfirming evidence** | Evidence that would prove a belief wrong; actively seeking this kind of evidence is the antidote to selective search, but it runs against the natural inclination of System 1 processing. |

## 11. Further Reading

1. **Simply Psychology — Confirmation Bias** (https://www.simplypsychology.org/confirmation-bias.html)
   A clear, accessible psychology explainer covering the definition, the Wason 2-4-6 task in detail, and all three mechanisms (selective exposure, biased interpretation, selective memory) — the primary grounding resource for this topic.

2. **Britannica — Confirmation Bias** (https://www.britannica.com/science/confirmation-bias)
   An authoritative encyclopaedia entry providing historical context, Peter Wason's original 1960s research background, and a concise account of the underlying mechanisms — useful for verifying definitions and understanding the concept's scientific provenance.

3. **CogBias — Measuring and Mitigating Confirmation Bias in LLMs** (https://arxiv.org/abs/2604.01366)
   A research paper that measures confirmation bias in large language models and proposes mitigation strategies — directly bridges the human cognitive bias covered in this topic to AI systems, providing evidence that the bias manifests in AI as well as in the humans evaluating AI.
