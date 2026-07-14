---
topic_id: "1.4"
title: "Why AI gives different answers to the same question"
position_in_module: 4
generated_at: "2026-06-20T00:00:00Z"
resource_count: 3
---

# 1. Why AI gives different answers to the same question — Topic Corpus

## 2. Prerequisites

This topic builds directly on three prior topics in this module:

- **Topic 1.1 — What is computation**: the input / process / output model and the idea of defined steps.
- **Topic 1.2 — Deterministic systems**: same input always gives the same output; predictability and reproducibility.
- **Topic 1.3 — Probabilistic systems**: same input can give different outputs; probability, sampling, output variation, and temperature as a control on randomness.

All three concepts are used freely throughout this topic without re-explanation.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Explain, in plain language, why an AI tool can give a different answer to the same question on two separate occasions.
- Identify the role of token sampling in producing varied AI outputs.
- Describe what a probability distribution is, in everyday terms, and connect it to how an AI chooses its next word.
- Explain how the temperature setting controls the amount of variation in an AI's output.
- Distinguish situations in which AI output variation is a feature from situations in which it is a drawback.
- Predict, in general terms, whether an AI output will be more predictable or more varied based on the temperature setting in use.

## 4. Introduction

You have probably noticed this already. You ask an AI assistant a question — maybe "What is a good way to start a story?" — and it gives you a confident, interesting answer. You ask the exact same question an hour later and it gives you a completely different answer. Both answers are reasonable. Neither is wrong. But they are not the same.

If you ran that same question through a calculator or a spreadsheet formula, you would get the same result every single time. So what is different about the AI? [3]

Topics 1.2 and 1.3 gave you the framework to answer this. You now know that some systems are deterministic (same input always gives the same output) and some are probabilistic (same input can give one of several possible outputs, and which one varies). AI language tools belong to the second category — they are probabilistic systems [1][3].

This topic answers the question that follows: **why exactly?** What is happening inside the AI's process that makes variation the normal, expected result? You will see that the variation is not random chaos — it is the outcome of specific, designed choices that you can understand, and even adjust [1][2].

Understanding this matters because you will use AI tools throughout this course and in your career. Knowing why they vary helps you use them more effectively, ask better questions, and recognise when variation is useful and when you need to be more careful about relying on a single AI answer.

## 5. Core Concepts

### 5.1 How an AI language tool builds its answer — word by word

Imagine you are typing a text message and your phone suggests the next word: you type "I'll see you" and the phone suggests "tomorrow," "there," or "soon." You pick one and the phone immediately suggests the next word after that.

An AI (Artificial Intelligence) language tool — specifically an LLM (Large Language Model), which is the technology behind tools like ChatGPT, Gemini, and similar assistants — works in a strikingly similar way, but at far greater scale [1].

When you type a question or prompt, the LLM does not retrieve a stored answer. It builds its response one small piece at a time. Each piece is called a **token** [1].

**Token** — a chunk of text the model processes at one step. A token is roughly a word, though short common words are often a single token and longer or unusual words may be split into two or three [1].

The LLM reads all the tokens in your question, then predicts: *which token should come next?* It picks one, adds it to the response, then predicts the next token after that. It repeats this process — token by token — until the answer is complete [1][2].

This process is called **token sampling** — the step where the model picks the next token from a range of candidates. "Sampling" is the word from Topic 1.3: reaching into a bag of possible answers and drawing one out. Here, the "bag" is the set of possible next tokens, and sampling is the draw [1].

### 5.2 The probability distribution — which tokens are more likely

When the LLM considers which token to pick next, it does not treat all tokens as equally likely. It assigns each possible next token a **probability** — a number saying how likely that token is to be the right next word, given everything typed so far [1][2].

These probabilities together form a **probability distribution** — a complete map of which tokens are more likely and which are less likely at this exact point in the response.

**Probability distribution** — a list of possible outcomes, each paired with a number expressing how likely that outcome is. All the numbers add up to 1 (or 100%). Higher numbers mean more likely; lower numbers mean less likely [1][2].

A concrete example: the LLM is completing the phrase "The cat sat on the ___." The distribution might look roughly like this:

| Next token | Approximate likelihood |
|---|---|
| "mat" | 55% |
| "floor" | 20% |
| "chair" | 12% |
| "roof" | 8% |
| everything else combined | 5% |

"Mat" is the most likely continuation — but it is not the only possible one. On one run the model might pick "mat." On another run it might pick "floor." On a third it might pick "chair." The distribution is shaped by the input, but it does not force a single answer [1][2].

This is exactly the structure of a probabilistic system from Topic 1.3: the input shapes which outputs are likely, but the same input can still produce different specific outputs.

### 5.3 Temperature — turning the dial on variation

In Topic 1.3 you were introduced to **temperature** as a control on randomness. Here is what that means specifically for an AI language tool [1][2].

Imagine you have the probability distribution from section 5.2. The temperature setting changes how the model uses that distribution when it samples.

**Low temperature** (for example, a setting near 0):

- The model makes the already-likely tokens even more dominant.
- It almost always picks the highest-probability token.
- The output becomes very consistent — ask the same question twice and you get very similar answers.
- The trade-off: less variety, less creativity, less surprise [1][2].

**High temperature** (for example, a setting near 1 or above):

- The model spreads its choices more evenly across the distribution.
- It samples more freely — lower-probability tokens get chosen more often.
- The output becomes more varied, more creative, sometimes more surprising.
- The trade-off: answers may be less predictable, occasionally less focused [1][2].

A useful mental image: think of temperature as adjusting the shape of the bag from Topic 1.3. At low temperature, almost all the cards in the bag say "mat" — drawing anything else is rare. At high temperature, the bag has a much more even mix — "mat," "floor," "chair," and "roof" are all well-represented, so the draw is genuinely unpredictable [1][2].

The key point: **temperature does not change what answers are possible — it changes how likely the less-probable answers are to be chosen** [2].

| Temperature | Effect on sampling | Output character |
|---|---|---|
| Low (near 0) | Picks the most-likely token almost always | Consistent, predictable, less varied |
| Medium | Balances likelihood with variety | Moderate variation |
| High (near 1+) | Samples freely from the distribution | Varied, creative, less predictable |

### 5.4 Why the same question gives different answers — the full chain

You now have all the pieces. Here is the complete explanation, step by step:

1. You type a question. That is the input.
2. The LLM reads your question and builds a probability distribution over possible next tokens.
3. The model samples one token from that distribution. Which token is selected varies — it is probabilistic, not fixed.
4. The selected token is added to the response. The model now builds a new distribution over the next token, given all the text so far.
5. It samples again. And again. Token by token, until the response is complete.
6. Because each sampling step is probabilistic, the specific sequence of tokens selected can differ between runs — even with the same input.

This is why you get a different answer to the same question. It is not a bug. It is not the AI "forgetting" your previous answer. It is the normal, designed behaviour of a probabilistic system that builds answers by sampling, one token at a time [1][2][3].

### 5.5 When variation is a feature, and when it is a drawback

Because AI output variation is designed, you can reason about when it helps and when it creates problems.

**Variation is a feature when:**

- You are using the AI for creative tasks — writing, brainstorming, generating options. You want different outputs on different runs; a deterministic AI that always gave the same story or the same list of ideas would be far less useful [1][3].
- You are exploring a problem space — asking the AI to suggest approaches, generate hypotheses, or produce alternatives. Variation gives you a wider range to choose from [3].
- You are using the AI as a thinking partner and you want it to surface angles you had not considered.

**Variation is a drawback when:**

- You need a consistent, reproducible answer — for example, in a technical task where there is a single correct answer and you need to verify or audit the output [1][2].
- You share an AI-generated answer with someone else and they try to replicate it. They type the same question and get a different response — the inconsistency can be confusing or create distrust [3].
- You are relying on the AI for high-stakes decisions (medical, legal, financial) where a different answer on a different day would matter [2].

The lesson is not "variation is good" or "variation is bad." It is: variation is a property of how the system works. Understanding it lets you decide when to rely on an AI answer, when to verify it, and when to run the same prompt multiple times to explore the range of what the AI considers plausible [1][2].

## 6. Implementation

You do not need to write code to apply this concept. Here is a practical procedure for experiencing and reasoning about AI output variation directly.

**Step-by-step: observing and controlling AI variation**

1. **Choose a prompt.** Pick a question that has more than one reasonable answer — for example: "Give me one tip for studying more effectively." This is an open-ended question where the AI has a wide probability distribution to sample from.

2. **Run the prompt three times without changing it.** Copy each response into a document. Do the responses differ? How much? This shows you output variation in action [1][3].

3. **Notice the pattern of variation.** Even if the specific wording differs, do the three responses share a theme? They probably do — the input still shapes the distribution. This shows you that variation is bounded, not arbitrary [1][2].

4. **Narrow the prompt.** Try: "Tell me exactly one study tip: use a single declarative sentence starting with a verb." Run this three times. Is the variation larger or smaller? A more constrained prompt narrows the probability distribution, reducing variation [1].

5. **If your AI tool exposes a temperature slider**, try the same open-ended prompt at low temperature (near 0) and at high temperature (near 1). Compare the consistency of responses. This makes the temperature effect concrete [2].

6. **Record your observations.** Write one sentence explaining what you noticed about variation and what caused it. This prepares you for AI Decision Journal Entry #1 in the lab session.

## 7. Real-World Patterns

### Creative writing assistants

Every time a user asks an AI writing tool to draft a paragraph, headline, or story idea, the tool samples from a probability distribution over possible continuations. Two writers with the same brief will get different drafts — which is the point. A deterministic assistant that always produced the same draft for the same brief would be commercially useless [1][3].

### Customer service chatbots

Many customer service AI systems are deliberately run at lower temperature to ensure that answers to "What is your return policy?" are consistent. The cost of a customer receiving contradictory information on two calls is high. Here, temperature is turned down to make the system behave more like a deterministic lookup than a free-sampling probabilistic one [2][3].

### Code generation tools

AI tools that write or complete code also use token sampling. A low-temperature setting makes them produce standard, predictable code constructs. A higher temperature can surface less conventional approaches — sometimes useful for creative solutions, sometimes producing less reliable code. Developers learn to set temperature based on the task at hand [1][2].

### Search and question-answering

Some AI-powered search tools are configured with very low temperature when answering factual questions, to reduce variation and improve consistency with known facts. The goal is to make the system behave more like a deterministic retrieval tool for fact-based queries, even though the underlying mechanism is still probabilistic [2][3].

### AI tutoring systems

Tutoring AIs that explain the same concept to different students benefit from some variation — the same explanation does not work for every learner. Moderate temperature means the system paraphrases, reorders, or reframes the concept slightly for each session, which can improve learning outcomes compared to a fixed script [3].

## 8. Best Practices

- **Run the same prompt more than once when a decision matters.** Because an AI answer is one sample from a probability distribution, a single run gives you one data point. Running the same prompt two or three times lets you see whether the answer is stable or variable — and spot cases where the AI gives contradictory responses [1][3].

- **Use a more specific prompt to reduce unwanted variation.** A vague question gives the model a wide distribution to sample from. A precise, constrained prompt narrows the distribution. If you need a consistent AI answer, make your question more specific — not just lower temperature [1][2].

- **Match temperature to your task.** Low temperature for fact-finding, consistency, and precision. Higher temperature for brainstorming, creative writing, and exploring options. When your AI tool exposes this control, use it deliberately rather than accepting the default [1][2].

- **Do not treat one AI answer as the answer.** The output is a sample, not a guaranteed correct value. Treat AI answers as a starting point — especially for important decisions. Verify, cross-check, and apply your own judgement [2][3].

- **Understand variation before troubleshooting.** If an AI gives you a different answer than it gave a colleague for the same question, do not immediately assume one of you made an error. The difference may simply be output variation. Compare the prompts carefully and run them multiple times to check [1][3].

## 9. Hands-On Exercise

This exercise links directly to AI Decision Journal — Entry #1 from the lab session.

1. Open any AI assistant you have access to. Type this prompt: "What is the most important habit for someone learning to code?" Copy the response.
2. Without changing anything, send the same prompt again. Copy the new response.
3. Send it a third time. Copy that response too.
4. Compare the three responses. Are they the same? Similar? Different in significant ways? Note whether the variation changes the advice or just the wording.
5. In your AI Decision Journal (Entry #1), write two sentences: one describing what you observed, and one explaining it using the words "probabilistic," "sampling," and "temperature." Use what you know from Topics 1.3 and 1.4.

The goal is to see output variation in practice and connect it directly to the concept.

## 10. Key Takeaways

- **AI language tools are probabilistic systems.** The same question can produce different answers because the system samples from a probability distribution of possible next tokens, and that sampling varies [1][2].
- **Token sampling is the mechanism.** The AI builds its answer one token at a time, picking each next token from a distribution shaped by the input. The pick is probabilistic — not fixed [1].
- **Temperature controls how freely the system samples.** Low temperature gives consistent, predictable output. High temperature gives varied, creative output. The right setting depends on the task [1][2].
- **Variation is not a malfunction — it is a design choice.** Understanding this lets you use AI tools more deliberately: run a prompt multiple times when it matters, adjust temperature when you can, and know when to verify a single AI response [1][2][3].
- **The input still shapes the output.** Probabilistic does not mean arbitrary. Your question determines which tokens are likely and which are not. A more specific prompt produces a narrower, more consistent distribution [1][2].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
