<!-- nav:top:start -->
[⬅ Previous: 13.3 — Few-shot examples](../../13-3-few-shot-examples-showing-the-model-what-good-output-looks-l/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.5 — Constraints ➡](../../13-5-constraints-telling-ai-what-not-to-do/artifacts/reading.md)
<!-- nav:top:end -->

---

# Chain-of-thought prompting — asking the model to reason step by step

## Overview

When you ask a model a multi-step question, it may jump straight to an answer and skip the working — and that shortcut often produces a wrong result. **Chain-of-thought (CoT) prompting** is a technique where you ask the model to write out each reasoning step before stating its final answer [1]. The visible steps force the model to work through each sub-problem in order, which leads to more accurate outputs on tasks that genuinely require multiple steps [1][2]. You already know how to set a role (13.2) and provide example pairs (13.3) — CoT adds a third tool: showing the model *how to think*, not just what output to produce.

## Key Concepts

### What a chain of thought is

A **chain of thought** — a sequence of intermediate steps connecting a question to an answer [1]. Instead of question → answer, the model produces question → step 1 → step 2 → step 3 → answer.

Each step becomes part of the model's own context as it generates the next token. If the model writes "3 × 5 = 15" in step 1, it can *see* that 15 when writing step 2. Without CoT, it had to reach the final answer without writing that intermediate value down — harder and more error-prone for complex problems [1][2].

### Zero-shot CoT

**Zero-shot CoT** — add a phrase asking the model to reason step by step, with no example of what those steps should look like [1][2].

Common trigger phrases:
- "Think through this step by step."
- "Reason step by step before giving your final answer."

When to use zero-shot CoT:
- You have no example reasoning chains ready.
- The task is new and you want to see what the model produces before refining it.
- A general instruction is enough for the task at hand.

Placing the instruction in the system prompt applies it to every message in the session. Adding it in the user message too reinforces it for that specific question [1][3].

### Few-shot CoT

**Few-shot CoT** — combine the example-pair technique from topic 13.3 with chain-of-thought. Instead of showing input → output, you show input → step-by-step working → answer [1].

Each example has three parts, forming a **reasoning triple**:

1. **Input** — the question or problem.
2. **Reasoning chain** — the step-by-step working.
3. **Final answer** — the conclusion from the reasoning.

When to use few-shot CoT [1][2]:
- The reasoning needs to follow a specific domain pattern (legal, financial, diagnostic).
- You want consistent output format — especially when downstream code parses the response.
- You need more control than a trigger phrase alone provides.

### When CoT helps — and when it does not

| **CoT helps most** | **CoT adds little benefit** |
|---|---|
| Arithmetic / maths word problems | Simple factual lookup ("capital of France?") |
| Logical deduction | Single-step classification |
| Planning and ordering tasks | Creative writing (poems, stories) |
| Code debugging | Direct format conversion (CSV → JSON) |

Rule of thumb: if you would write intermediate steps on paper to solve it, CoT will help. If you can answer in one mental step, skip CoT — unnecessary "think step by step" wastes tokens and adds no accuracy gain [2][3].

## Worked Example

This example shows a zero-shot CoT call followed by extracting just the final answer.

**The problem:** a recipe calculation requiring two arithmetic steps.

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    system="You are a helpful assistant. When solving problems, think step by step before giving your final answer. End every response with a line that starts with 'Answer:'.",
    messages=[
        {
            "role": "user",
            "content": (
                "A recipe needs 2.5 cups of flour per batch. "
                "I want to make 3 and a half batches. "
                "How many cups of flour do I need in total? "
                "Think step by step."
            )
        }
    ]
)

print(response.content[0].text)
```

A typical model response:

```
Step 1 — Cups per batch = 2.5.
Step 2 — Number of batches = 3.5.
Step 3 — Total = 2.5 × 3.5 = 8.75 cups.
Answer: 8.75 cups.
```

To extract only the final answer from that response:

```python
answer_line = [
    line for line in response.content[0].text.splitlines()
    if line.startswith("Answer:")
]
final_answer = answer_line[0].replace("Answer:", "").strip() if answer_line else None
```

The `"Answer:"` marker is a contract you set in the system prompt and keep consistent across every example. Your code can then find it reliably [1][2].

**Stepping up to few-shot CoT** — when you need a consistent domain format, provide two reasoning triples in the system prompt:

```python
few_shot_cot_prompt = """You are a maths tutor. Show working step by step, then state the final answer on its own line starting with "Answer:".

Example 1
Problem: A train travels at 60 km/h. How far does it travel in 2.5 hours?
Step 1 — Distance = speed × time.
Step 2 — Distance = 60 × 2.5 = 150 km.
Answer: 150 km.

Example 2
Problem: A shop buys 200 items for $4 each and sells them for $6.50 each. What is the total profit?
Step 1 — Total cost = 200 × $4 = $800.
Step 2 — Total revenue = 200 × $6.50 = $1,300.
Step 3 — Profit = $1,300 − $800 = $500.
Answer: $500."""
```

The model sees two reasoning triples and follows their structure for every new problem [1].

## In Practice

**Real-world patterns where CoT appears:**

- **Code debugging tools** — a CoT prompt asks the model to trace through code line by line before naming the bug. This catches logic errors that pattern-matching alone misses [2][3].
- **Decision support** — comparing options (job offers, technical architectures). CoT surfaces the comparison criteria before the recommendation, making the output auditable [1].
- **Data validation pipelines** — checking whether a record meets a multi-part rule. CoT checks each criterion explicitly; the reasoning chain also serves as an audit log [3].

**Do:**
- Use a consistent final-answer marker (`"Answer:"`, `"RESULT:"`) so your Python code can parse it reliably [1][2].
- Set `max_tokens` generously — reasoning chains use more tokens than direct answers [2].
- Test on problems where you already know the right answer — the only way to verify the chain is sound.

**Do not:**
- Add "think step by step" to every prompt — unnecessary on simple single-step tasks [1].
- Accept a plausible-looking chain without reading it — the chain makes errors *visible*, but you still need to check them.
- Use CoT as a substitute for giving the model the right information — CoT helps it reason better with what it has, not supply missing knowledge.

## Key Takeaways

- **Chain-of-thought prompting asks the model to write out intermediate reasoning steps before giving a final answer.** Visible steps reduce errors on multi-step tasks by giving the model the right context at each stage [1].
- **Zero-shot CoT** adds a trigger phrase ("think step by step") with no examples — fastest to apply, good for exploration [1][2].
- **Few-shot CoT** provides example reasoning triples (input → working → answer) — more consistent formatting and domain-specific structure [1].
- **CoT helps most on arithmetic, logical deduction, planning, and debugging.** For simple single-step tasks, skip it [2][3].
- **Design a clear final-answer marker** (`"Answer:"`) so your Python code can extract the conclusion from the full reasoning response reliably [1].

## References

1. learnprompting.org — Chain of Thought Prompting. https://learnprompting.org/docs/intermediate/chain_of_thought
2. DataCamp — Chain-of-Thought Prompting tutorial. https://www.datacamp.com/tutorial/chain-of-thought-prompting
3. AltexSoft — Chain-of-Thought Prompting. https://www.altexsoft.com/blog/chain-of-thought-prompting/

---
<!-- nav:bottom:start -->
[⬅ Previous: 13.3 — Few-shot examples](../../13-3-few-shot-examples-showing-the-model-what-good-output-looks-l/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.5 — Constraints ➡](../../13-5-constraints-telling-ai-what-not-to-do/artifacts/reading.md)
<!-- nav:bottom:end -->
