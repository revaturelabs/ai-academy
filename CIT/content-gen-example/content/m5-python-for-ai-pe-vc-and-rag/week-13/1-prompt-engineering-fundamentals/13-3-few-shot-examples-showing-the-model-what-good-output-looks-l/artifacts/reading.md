<!-- nav:top:start -->
[⬅ Previous: 13.2 — Role assignment](../../13-2-role-assignment-telling-the-model-who-it-is/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.4 — Chain-of-thought prompting ➡](../../13-4-chain-of-thought-prompting-asking-the-model-to-reason-step-b/artifacts/reading.md)
<!-- nav:top:end -->

---

# Few-shot examples — showing the model what good output looks like

## Overview

Imagine training a new employee to write product descriptions by handing them three finished examples instead of a rulebook. Most people learn faster from examples than from rules — and so does an AI model. **Few-shot prompting** is the technique of including example input-output pairs directly in your prompt so the model can read the pattern and match it [1]. You already know how to set a system prompt and assign a role. Few-shot prompting adds the next layer: concrete examples of the exact format, tone, and structure you expect. With the right examples in place, a model that was producing generic responses often starts producing output that matches your exact requirements — without any fine-tuning or model changes.

## Key Concepts

### Zero-shot, one-shot, and few-shot — what the terms mean

The word "shot" in this context means "example" — one demonstration of the task [2]. The three terms differ only in how many examples you include:

| Term | Number of examples | When to use it |
|---|---|---|
| **Zero-shot** | 0 | Plain task description; works when the expected output is obvious. |
| **One-shot** | 1 | One example anchors the model's style for simple, single-pattern tasks. |
| **Few-shot** | 2–8 (typically) | Multiple examples; use when format has several parts or tone is specific. |

**Zero-shot prompting** is what you have been doing whenever you write a plain system prompt plus a user request. The model relies entirely on its training to guess the format you want. It works well for common tasks, but often falls short when you need a particular structure or tone that differs from the model's default [1].

### What the model actually does with examples

When a model sees your examples it is not memorising rules. It reads the examples as part of its input, notices the pattern — structure, vocabulary, level of detail — and continues that pattern into its answer.

Think of completing a sequence:

> Apple → Fruit  
> Carrot → Vegetable  
> Salmon → ?

Most people answer "Fish" — they recognised the pattern. The model does the same thing: it reads your input-output pairs, identifies the underlying task pattern, and applies that pattern to the new input you give it [2].

This is called **in-context learning** — the model picking up a task pattern from examples provided in the prompt, without any retraining or changes to its internal parameters. Once the conversation ends, the model has not "kept" that learning. Next time you call the API, it starts fresh. The examples need to be present in every new call where you want the pattern applied.

### Anatomy of an example pair

Each example in a few-shot prompt has two parts:

1. **The input** — the kind of request or raw material the model will receive.
2. **The output** — the exact response you want the model to produce for that input.

Together, these make one **example pair** [1]. Here is a concrete illustration — a three-pair prompt for classifying customer feedback:

```
Input: "The delivery was faster than expected and the packaging was beautiful."
Output: positive

Input: "My order arrived damaged and customer service never replied."
Output: negative

Input: "The item arrived on time."
Output: neutral
```

Each pair shows the model what text comes in and what label should come out. When you then provide a new piece of feedback, the model applies the same labelling pattern.

### Positive and negative examples

- A **positive example** shows the model what the output *should* look like. Most few-shot prompts use only positive examples [1].
- A **negative example** shows the model what the output should *not* look like — a common mistake paired with a correction [1]. Use a negative example only when a specific error keeps appearing after you have already added positive examples.

Use negative examples sparingly — one or two at most. Too many "do not do this" examples can accidentally reinforce the bad pattern rather than suppress it [1].

### How many examples to include

There is no universal rule, but three guidelines hold across most tasks [1][2]:

1. **Start with two to three positive examples** and test. Many tasks reach acceptable quality at this count.
2. **Add more examples (up to six to eight) if quality is still inconsistent** — especially when the output has multiple components that all need to be right at once.
3. **Stop when you see diminishing returns.** More examples consume more of the model's **context window** — the maximum amount of text an LLM can read and process in one call. Every token (roughly a word or part of a word) in your prompt uses up part of this budget. Long few-shot prompts leave less room for the actual task content and the model's response.

The practical starting point for most beginner tasks is **two to four examples** [1].

### Where to place examples

You have two options:

**In the system prompt** — use this when the format is fixed for every user message in the session. This is the most common placement for applications such as a support bot that always replies in a particular format [1][3].

**In the user message** — use this when the task or format changes per request and the examples are specific to that single call. This suits one-off scripts or notebook experiments.

In both cases the examples appear *before* the live input, so the model reads the pattern before it encounters the real task [1][2].

### What makes an example good vs weak

A weak example can mislead the model just as reliably as a good example guides it [1][2]:

| Quality dimension | Good example | Weak example |
|---|---|---|
| **Format** | Matches the exact output format you want | Uses a different structure or inconsistent labels |
| **Consistency** | All examples follow the same pattern | Different tones, lengths, or structures across pairs |
| **Accuracy** | The shown output is genuinely correct | Contains an error — the model will replicate it |
| **Length** | Output length matches your target | Output is much shorter or longer than the target |

The single most common mistake is **inconsistency across examples** — one example uses a formal tone, another is casual, a third uses bullet points while the others use prose. The model averages across the mix and matches none of them well [1].

## Worked Example

The task: build a sentiment classifier that returns exactly one word — "positive," "negative," or "neutral" — using the Anthropic API you already know.

**Step 1 — Write your example pairs.**

Choose two to four real inputs covering the range of cases you expect. For each, write the exact output you want:

```
Input: "I love how easy this tool is to use."     → Output: positive
Input: "It crashed three times in one hour."       → Output: negative
Input: "The software does what it says it does."   → Output: neutral
```

**Step 2 — Embed the examples in the system prompt.**

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

<!-- nav:top:start -->
[⬅ Previous: 13.2 — Role assignment](../../13-2-role-assignment-telling-the-model-who-it-is/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.4 — Chain-of-thought prompting ➡](../../13-4-chain-of-thought-prompting-asking-the-model-to-reason-step-b/artifacts/reading.md)
<!-- nav:top:end -->

---
```

**Step 4 — Evaluate and iterate.**

Run the prompt on ten to fifteen test inputs you have labelled yourself. Count the errors. If the model consistently makes a specific type of mistake — say, mislabelling mixed reviews — add one more example pair that covers that case and re-test.

## In Practice

Few-shot prompting shows up across many real working systems [1][2][3]:

- **Classification tasks** — labelling support tickets, flagging spam, or tagging product reviews. A small set of hand-curated examples defines the standard; the model applies it at scale.
- **Structured data extraction** — pulling specific fields from unstructured text (price, product name, condition). Zero-shot instructions like "extract the key details" are too vague; two or three example pairs define the exact output schema.
- **Style and tone matching** — marketing teams use few-shot prompts to enforce a brand voice. A few approved copy samples teach the model sentence length, word choice, and energy level without anyone writing a rulebook.

Key do/don't summary:

- **Do** use real examples from your actual use case — invented examples often miss the messiness of real inputs [1].
- **Do** keep output length consistent across all examples. One-sentence target? Every example output is one sentence.
- **Do** order examples from simplest to most complex so the model builds up to nuanced cases [1].
- **Do not** exceed eight examples without a clear reason — length costs outweigh quality gains past that point [2].
- **Do not** use inconsistent labels or formats; even one inconsistent example weakens the whole set [1].
- **Do not** rely on few-shot alone when the task requires step-by-step reasoning — that is a separate technique you will meet in topic 13.4.

## Key Takeaways

- **Few-shot prompting means including example input-output pairs in your prompt.** Zero examples is zero-shot; one is one-shot; two to eight is few-shot.
- **Examples teach the model the pattern — format, tone, length, structure — without any retraining.** This is called in-context learning: the model reads your examples and continues the pattern.
- **Good examples are consistent, accurate, and representative.** A single inconsistent or wrong example weakens the entire set [1].
- **Two to four examples is the practical starting point** for most tasks. Add more only if quality is still inconsistent after testing.
- **Placement matters.** Put examples in the system prompt when the format is fixed for the whole session; put them in the user message when the format is task-specific.

## References

1. PromptHub, "The Few-Shot Prompting Guide." <https://www.prompthub.us/blog/the-few-shot-prompting-guide>
2. Learn Prompting, "Few Shot Prompting." <https://learnprompting.org/docs/basics/few_shot>
3. Comet, "Few-Shot Prompting." <https://www.comet.com/site/blog/few-shot-prompting/>

---
<!-- nav:bottom:start -->
[⬅ Previous: 13.2 — Role assignment](../../13-2-role-assignment-telling-the-model-who-it-is/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.4 — Chain-of-thought prompting ➡](../../13-4-chain-of-thought-prompting-asking-the-model-to-reason-step-b/artifacts/reading.md)
<!-- nav:bottom:end -->
