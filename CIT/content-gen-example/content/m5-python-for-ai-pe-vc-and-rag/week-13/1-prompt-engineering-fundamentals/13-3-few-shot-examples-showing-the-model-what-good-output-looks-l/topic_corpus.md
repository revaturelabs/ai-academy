---
topic_id: "13.3"
title: "Few-shot examples — showing the model what good output looks like"
position_in_module: 3
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. Few-Shot Examples — Showing the Model What Good Output Looks Like — Topic Corpus

## 2. Prerequisites

- **13.1 — System prompt vs user prompt**: students know the system prompt carries persistent, session-wide instructions and that the user prompt carries the live request. Few-shot examples sit inside this structure, typically in the system prompt or at the start of the message history.
- **13.2 — Role assignment**: students know how to tell the model who it is via a role statement in the system prompt. Few-shot examples complement role assignment — they show the model *how* to behave, whereas a role statement tells the model *who* it is.
- **12.10 / 12.11 — Anthropic API calls**: students can construct a `client.messages.create()` call with `system` and `messages` parameters. Code examples here extend that call shape.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** few-shot prompting and explain the difference between zero-shot, one-shot, and few-shot prompting in plain language.
2. **Identify** what makes a good example — correct format, correct tone, and correct level of detail — versus a weak or misleading example.
3. **Write** a few-shot prompt with two to four input-output example pairs embedded in the system prompt or user prompt.
4. **Explain** why few-shot examples change model output quality and what the model is actually doing when it sees them.
5. **Apply** the placement rule — deciding whether examples belong in the system prompt or in the user message — for a given use case.
6. **Describe** two common mistakes when writing few-shot examples and state how to fix each one.

## 4. Introduction

Imagine you are training a new employee to write short product descriptions for your online store. You could hand them a style guide and hope for the best. Or you could hand them three finished examples — "here is what a great product description looks like for us" — and let them match the pattern. Most people learn faster from examples than from rules.

The same principle applies to an AI model. You can tell a model exactly what output you want using rules and instructions, but sometimes the clearest instruction is simply to show the model a finished example of what you mean. This technique is called **few-shot prompting** [1].

You already know (from 13.1 and 13.2) how to set a model's persistent context and give it a role. Few-shot prompting adds the next layer: concrete examples of the exact output quality, format, and tone you expect. With the right examples in place, a model that was producing good-but-generic responses often starts producing responses that match your exact house style — without any further tuning or technical setup [2].

This topic focuses entirely on what few-shot examples are, why they work, and how to write them well. You will not be training or fine-tuning a model — that is a different, more advanced skill. Everything here happens inside the prompt itself, using the API calls you already know how to make.

## 5. Core Concepts

### 5.1 Zero-shot, one-shot, and few-shot — what the terms mean

The word "shot" in this context means "example" — a single demonstration of the task [2]. The three terms differ only in how many examples you include:

| Term | Number of examples | What it means |
|---|---|---|
| **Zero-shot** | 0 | You give the model a task description with no examples at all. |
| **One-shot** | 1 | You give the model a task description plus one worked example. |
| **Few-shot** | 2–8 (typically) | You give the model a task description plus several worked examples. |

**Zero-shot** is what you have been doing so far whenever you write a plain system prompt plus a user request. The model relies entirely on its training to guess the format and style you want. This works well for common tasks where the expected output is obvious, but it often falls short when you need a specific format, a particular tone, or a consistent structure that differs from the model's default [1].

**One-shot** is often enough to anchor the model's style for simple tasks. For example, one good email template can teach the model your company's email tone.

**Few-shot** is useful when your task is more nuanced, when the format has multiple parts that all need to be right, or when you want the model to generalise a pattern rather than copy a single example [1][2].

### 5.2 What the model is actually doing with examples

When a model sees your examples, it is not storing them as rules. Instead it reads the examples as part of its input and notices the pattern — the structure, the vocabulary, the level of detail, and the format — then continues that pattern into its answer [2].

Think of it like completing a sequence. If you show someone:

> Apple → Fruit
> Carrot → Vegetable
> Salmon → ?

Most people answer "Fish" — they recognised the pattern. The model does something similar: it reads your input-output pairs, identifies the underlying task pattern, and applies that pattern to the new input you give it.

This is sometimes called **in-context learning** — the model picking up a task pattern from examples provided in the prompt, without any retraining or changes to its internal parameters. No training is happening. The examples simply inform the model's next response [2].

Once the conversation ends, the model has not "kept" that learning. Next time you use it, it starts fresh. The examples need to be present in every new call where you want the pattern applied.

### 5.3 Anatomy of a few-shot example pair

Each example in a few-shot prompt has two parts:

1. **The input** — the kind of user request or raw material you expect to receive.
2. **The output** — the exact response you want the model to produce for that input.

Together, an input and its matching output make one **example pair** [1].

Here is a concrete illustration. Suppose you want the model to classify customer feedback as either "positive," "negative," or "neutral":

```
Input: "The delivery was faster than expected and the packaging was beautiful."
Output: positive

Input: "My order arrived damaged and customer service never replied."
Output: negative

Input: "The item arrived on time."
Output: neutral
```

Each pair shows the model: (a) what kind of text comes in, and (b) what label should come out. When you then provide a new, unseen piece of feedback, the model applies the same labelling pattern.

### 5.4 Positive and negative examples

A **positive example** shows the model what the output *should* look like [1]. Most few-shot prompts use positive examples only.

A **negative example** shows the model what the output should *not* look like — a common mistake or a wrong format — paired with a correction [1]. Negative examples are optional. Use them when a specific, predictable error keeps appearing even after you add positive examples. Adding a negative example says: "Here is the wrong way — do not do this."

Example of a negative example pair for a summarisation task:

```
Input: "Summarise this product review in one sentence."
Review: "I bought this blender six months ago. It is loud but very powerful. My only complaint is the lid leaks sometimes."

BAD output: "The blender is loud, powerful, and has a leaking lid problem, and overall the user seems satisfied with the product despite the minor issues."

GOOD output: "Powerful blender but the lid leaks."
```

The negative example explicitly flags the mistake (too long, too wordy) so the model understands exactly what to avoid.

Use negative examples sparingly — one or two at most. A prompt heavy with "do not do this" examples can confuse the model and can accidentally reinforce the bad pattern rather than suppress it [1].

### 5.5 How many examples to include

There is no universal rule, but three practical guidelines hold across most tasks [1][2]:

1. **Start with two to three positive examples** and test your prompt. Many tasks reach acceptable quality at this count.
2. **Add more examples (up to six to eight) if quality is still inconsistent** — especially if the task has multiple output components that all need to be right simultaneously.
3. **Stop adding examples when you see diminishing returns** — more examples consume more of the model's context window and add complexity without improving output quality.

**Context window** — the maximum amount of text an LLM (Large Language Model) can read and process in one call. Every token (roughly a word or part of a word) in your prompt — including all your examples — uses up part of this window. Long few-shot prompts with many examples leave less room for the model's response and for the actual task content.

The practical sweet spot for most beginner use cases is **two to four examples** [1].

### 5.6 Where to place examples in a prompt

You have two main options for where to put your examples:

**Option A — In the system prompt**

Place the examples in the system prompt when they define a persistent behaviour that should apply to every user message in the session. This is the most common placement for applications — for instance, a customer-support bot that should always reply in a particular format [1][3].

```python
system_prompt = """You are a customer support agent for a software company.
Always respond using this format:

Example 1
User: "I can't log in."
Agent: "I'm sorry to hear that. Let's fix this together. First, please try resetting your password using the link below..."

Example 2
User: "The app keeps crashing."
Agent: "That sounds frustrating. Can you tell me which version of the app you are using and what device you are on? That will help me identify the issue quickly..."""
```

**Option B — In the user message**

Place the examples in the user message when the task or format changes per request and the examples are specific to that single call. This is common in one-off scripts or notebook experiments.

```python
user_message = """Classify each sentence as positive, negative, or neutral.

Input: "Shipping was very fast."
Output: positive

Input: "The product broke after one day."
Output: negative

Input: "The colour is as shown in the photo."
Output: neutral

Input: "I was surprised by how quiet the motor is."
Output:"""
```

In both cases the structure is the same: examples appear before the live input so the model reads the pattern before it encounters the real task [1][2].

### 5.7 What makes an example good vs weak

Not all examples teach the model what you want. A weak example can mislead the model just as reliably as a good example guides it. Here is what separates the two [1][2]:

| Quality dimension | Good example | Weak example |
|---|---|---|
| **Format** | Matches the exact output format you want the model to use | Uses a different structure, inconsistent labels, or mixed formats across pairs |
| **Consistency** | All examples follow the same pattern | Examples show different tones, different lengths, or different structures |
| **Representativeness** | Covers the variety of inputs you expect in real use | Uses only the simplest cases, leaving typical edge cases unaddressed |
| **Accuracy** | The output shown is genuinely the right answer | Contains an error — the model will replicate it |
| **Length** | Output is the length you actually want | Output is much shorter or longer than the target, teaching the wrong length |

The single most common mistake is **inconsistency across examples** — one example uses a formal tone, another uses casual language, a third uses bullet points while the others use prose. The model sees inconsistency and produces output that averages across the mix, matching none of your examples well [1].

## 6. Implementation

### Step-by-step: building a few-shot prompt in Python

This walkthrough uses the Anthropic API you already know. The task: a simple sentiment classifier that returns exactly one word — "positive," "negative," or "neutral."

**Step 1 — Write your example pairs.**

Choose two to four real inputs that represent the range of cases you expect. For each, write the exact output you want.

```
Input: "I love how easy this tool is to use."     → Output: positive
Input: "It crashed three times in one hour."       → Output: negative
Input: "The software does what it says it does."   → Output: neutral
```

**Step 2 — Build the system prompt with the examples embedded.**

```python
system_prompt = """You are a sentiment classifier. When given a sentence, reply with exactly one word: positive, negative, or neutral.

Here are examples:

Input: "I love how easy this tool is to use."
Output: positive

Input: "It crashed three times in one hour."
Output: negative

Input: "The software does what it says it does."
Output: neutral"""
```

**Step 3 — Make the API call.**

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=10,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": 'Input: "Setup took less than five minutes."\nOutput:'
        }
    ]
)

print(response.content[0].text)
# Expected output: positive
```

**Step 4 — Evaluate and iterate.**

Run the same prompt on ten to fifteen test inputs you have labelled yourself. Count the errors. If the model consistently makes a specific type of mistake — for example, classifying mixed reviews incorrectly — add one more example pair that covers that case. Repeat until the error rate is acceptable for your use.

## 7. Real-World Patterns

### Where few-shot prompting shows up in working systems

**Content moderation and classification.** Systems that label user-generated content — flagging spam, categorising support tickets, or tagging product reviews — often rely on few-shot prompts. A small set of hand-curated examples defines the labelling standard, and the model applies it at scale without needing a separately trained classifier [3].

**Structured data extraction.** When a system needs to pull specific fields from unstructured text — for example, extracting a price, a product name, and a condition from a second-hand listing — few-shot examples show the model exactly which fields to extract and in what format. A zero-shot instruction like "extract the key details" is too vague; two or three example pairs define the exact output schema [1].

**Style and tone matching.** Marketing teams use few-shot prompts to enforce a brand voice. A few examples of approved copy teach the model the sentence length, word choice, and energy level of the brand — without anyone having to write a style guide in rule form [2].

**Agentic systems.** In systems where an AI model takes a sequence of actions (you will cover these in Week 14), few-shot examples can show the model how to format its outputs consistently. Consistent formatting matters because downstream code parses the model's output — inconsistent output breaks the parser [3].

## 8. Best Practices

### Do

- **Use real examples from your actual use case.** Invented or overly tidy examples often fail to cover the messiness of real inputs. If you have existing data, pick examples from it [1].
- **Keep output length consistent across examples.** If your target output is one sentence, every example output should be one sentence. If your target is a three-bullet list, every example output should be a three-bullet list.
- **Order your examples from simplest to most complex.** This helps the model build up to the nuanced cases rather than encountering the hardest case first [1].
- **Use the same separator format in every example and in the live task.** The label before the output ("Output:", a colon, a newline) should be identical every time.
- **Test your examples on inputs you already know the answer to.** This is the only way to verify your examples are teaching the right pattern.

### Do not

- **Do not include more than eight examples without a clear reason.** Beyond that point, length costs outweigh quality gains and you risk filling the context window [2].
- **Do not use inconsistent labels or formats across examples.** Even one inconsistent example weakens the signal for all the others.
- **Do not use examples that contain the error you are trying to prevent unless they are clearly marked as wrong.** An unmarked negative example teaches the model the wrong pattern [1].
- **Do not rely on few-shot alone when the task genuinely requires step-by-step reasoning.** You will cover that technique in topic 13.4.
- **Do not copy examples from a web tutorial without checking they match your actual output format.** Tutorial examples are written for illustration, not for your specific task.

## 9. Hands-On Exercise

**Sketch:** Build a few-shot classifier for the domain you are using for Assessment A4 (Python and Prompt Engineering Portfolio, due this week).

1. Pick a classification task in your domain — for example, classifying customer messages by urgency (high / medium / low), or categorising bug reports by type (UI / performance / data).
2. Write three to four example pairs by hand, labelling them yourself.
3. Embed the examples in a system prompt alongside a role statement from topic 13.2.
4. Test the prompt on five new inputs you have not included in the examples. Count how many the model labels correctly.
5. If any label is wrong, identify which example is missing or inconsistent, add or fix it, and re-test.

This is also a useful first step toward the accuracy-measurement exercise in the week's lab activity: testing prompt versions on ten domain-relevant inputs each.

## 10. Key Takeaways

- **Few-shot prompting means including example input-output pairs in your prompt.** Zero examples is zero-shot; one example is one-shot; two to eight examples is few-shot.
- **Examples teach the model the pattern — format, tone, length, structure — without any retraining.** The model uses in-context learning: it reads the pattern from your examples and continues it.
- **Good examples are consistent, accurate, and representative.** A single inconsistent or wrong example weakens the whole set.
- **Two to four examples is the practical starting point** for most tasks. Add more only if quality is still inconsistent after testing.
- **Placement matters.** Put examples in the system prompt when the format is fixed for the whole session; put them in the user message when the format is task-specific.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
