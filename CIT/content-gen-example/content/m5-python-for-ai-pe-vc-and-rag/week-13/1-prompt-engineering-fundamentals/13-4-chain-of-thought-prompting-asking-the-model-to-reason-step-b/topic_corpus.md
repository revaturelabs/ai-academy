---
topic_id: "13.4"
title: "Chain-of-thought prompting — asking the model to reason step by step"
position_in_module: 4
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. Chain-of-Thought Prompting — Asking the Model to Reason Step by Step — Topic Corpus

## 2. Prerequisites

- **13.1 — System prompt vs user prompt**: students know how system prompts carry persistent context and that user prompts carry the live request. Chain-of-thought (CoT) instructions can sit in either location depending on the use case.
- **13.2 — Role assignment**: students can write a role statement that shapes the model's persona and behaviour. CoT builds on top of role assignment — the role sets *who* the model is; CoT instructs *how* the model should work through a problem.
- **13.3 — Few-shot prompting**: students know how to embed example input-output pairs in a prompt. CoT extends this: CoT examples show not just the final output but also the intermediate reasoning steps that lead to it.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** chain-of-thought (CoT) prompting and explain in plain language why asking a model to reason step by step improves output quality on multi-step problems.
2. **Distinguish** zero-shot CoT from few-shot CoT and state when each is appropriate.
3. **Write** a zero-shot CoT prompt by adding a step-by-step reasoning instruction to a user message or system prompt.
4. **Write** a few-shot CoT prompt that includes at least two input-reasoning-answer triples as examples.
5. **Identify** the types of tasks where CoT prompting helps most and the types where it adds overhead without benefit.
6. **Apply** CoT prompting in a Python `client.messages.create()` call using the Anthropic API.

## 4. Introduction

Imagine you ask a friend: "Should I take the highway or the side roads to get to the airport on time?" If they just say "highway" without explaining anything, you have no way to check their reasoning — maybe they forgot about the construction that starts at 4 p.m. But if they say "Well, it's 3:30 now, the highway has construction until 5, the side roads add 10 minutes but avoid the jam, so take the side roads," you can follow each step and trust — or challenge — the conclusion.

Large language models (LLMs) face the same problem. When you ask a model a question that involves multiple steps — some arithmetic, a logical deduction, a comparison across several options — the model may jump straight to an answer without working through the intermediate steps. That shortcut sometimes produces a correct answer. Often, especially on harder questions, it produces a confidently wrong one.

**Chain-of-thought (CoT) prompting** is a technique where you explicitly ask the model to work through its reasoning step by step before stating a final answer [1]. The key insight is simple: showing the intermediate steps forces the model to allocate attention to each sub-problem rather than pattern-matching directly to an answer. The result is more accurate outputs on tasks that genuinely require multi-step thinking [1][2].

You already know how to frame a model's identity (13.2) and how to show it example input-output pairs (13.3). CoT adds a third tool: showing the model *how to think*, not just what kind of output to produce.

## 5. Core Concepts

### 5.1 What chain-of-thought means

A **chain of thought** is a sequence of intermediate reasoning steps that connect a question to an answer [1]. Instead of going directly from "question → answer," the model produces "question → step 1 → step 2 → step 3 → answer."

The word "chain" is literal: each step builds on the previous one, forming an unbroken chain from the original problem to the conclusion. The model essentially writes out a scratchpad — a visible working — before committing to a final answer.

Here is a simple before-and-after comparison for a word problem:

**Without CoT:**
```
User: A store has 48 apples. It sells 3 bags of 5 apples each and receives a delivery of 20 apples.
      How many apples does the store have now?

Model: 53 apples.
```

**With CoT (zero-shot):**
```
User: A store has 48 apples. It sells 3 bags of 5 apples each and receives a delivery of 20 apples.
      How many apples does the store have now? Think through this step by step.

Model: Step 1 — Start with 48 apples.
       Step 2 — 3 bags of 5 apples = 15 apples sold. 48 − 15 = 33 apples remaining.
       Step 3 — Add the delivery: 33 + 20 = 53 apples.
       Answer: 53 apples.
```

In this example the final answer is the same, but the intermediate steps are now visible and checkable. For harder problems — ones where the model would have made an error on the "direct jump" — the step-by-step process catches those errors before they propagate to the final answer [1][2].

### 5.2 Why reasoning out loud helps

When a model generates a response, it produces tokens (roughly, words or word-pieces) one at a time, with each token informed by everything that came before it. When you ask the model to reason step by step, the earlier reasoning steps become part of the model's own context as it continues generating. Each correctly reasoned step literally provides the right information for the next step [1].

Think of it this way: if a model writes "Step 1: 3 × 5 = 15" in its response, then when it generates "Step 2," it can see the 15 it just wrote. By contrast, if it had to jump straight to the answer, it never wrote that 15 down and had to rely on a single internal computation — which is harder and more error-prone for complex chains [1][2].

This is not the model "thinking" the way humans do. It is a characteristic of how auto-regressive text generation works: more visible intermediate context leads to better subsequent tokens. CoT exploits this property deliberately.

### 5.3 Zero-shot CoT

**Zero-shot CoT** is the simplest form of chain-of-thought prompting. You add a phrase asking the model to reason step by step — without providing any example of what those reasoning steps should look like [1][2].

Common zero-shot CoT trigger phrases:
- "Think through this step by step."
- "Let's work through this carefully."
- "Reason step by step before giving your final answer."
- "Think step by step."

The phrase acts as an instruction to the model to activate its step-by-step generation mode. Research showed that even adding "Let's think step by step." to the end of a question dramatically improved accuracy on multi-step reasoning benchmarks compared to asking the same question with no such instruction [1].

**When to use zero-shot CoT:**
- You do not have example reasoning chains ready.
- The task is new and you want to see what kind of reasoning the model produces before deciding whether to refine it with examples.
- The task is straightforward enough that a general instruction is sufficient.

**Zero-shot CoT prompt example (Anthropic API):**

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    system="You are a helpful assistant. When solving problems, think step by step before giving your final answer.",
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

Placing the instruction in the system prompt ("think step by step before giving your final answer") makes it apply to every user message in the session. Adding it again at the end of the user message reinforces the instruction for that specific question — both are common practices [1][3].

### 5.4 Few-shot CoT

**Few-shot CoT** combines the example-pair technique from topic 13.3 with chain-of-thought reasoning. Instead of showing the model just an input and a final output, you show it an input, a full chain of reasoning steps, and then the answer [1].

Each example in a few-shot CoT prompt has three parts:
1. **The input** — the question or problem.
2. **The reasoning chain** — the step-by-step working.
3. **The final answer** — the conclusion drawn from the reasoning.

Together these three parts form a **reasoning triple** [1].

**Why use few-shot CoT instead of zero-shot CoT?**

Zero-shot CoT asks the model to produce *some* chain of thought, but does not specify what that chain should look like — how detailed, in what format, how many steps. Few-shot CoT shows the model the exact style of reasoning you want, making output more consistent and controllable [1][2].

Few-shot CoT is particularly useful when:
- The reasoning steps need to follow a specific domain logic (for example, legal analysis, financial calculation, or diagnostic flowchart).
- You want the model to decompose the problem in a particular way.
- Output consistency matters — for instance, when downstream code parses the model's response.

**Few-shot CoT example:**

```python
import anthropic

client = anthropic.Anthropic()

few_shot_cot_prompt = """You are a maths tutor. When solving word problems, always show your working step by step, then state the final answer on its own line starting with "Answer:".

Example 1
Problem: A train travels at 60 km/h. How far does it travel in 2.5 hours?
Working:
Step 1 — Distance = speed × time.
Step 2 — Distance = 60 × 2.5 = 150 km.
Answer: 150 km.

Example 2
Problem: A shop buys 200 items for $4 each and sells them for $6.50 each. What is the total profit?
Working:
Step 1 — Total cost = 200 × $4 = $800.
Step 2 — Total revenue = 200 × $6.50 = $1,300.
Step 3 — Profit = $1,300 − $800 = $500.
Answer: $500."""

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    system=few_shot_cot_prompt,
    messages=[
        {
            "role": "user",
            "content": (
                "Problem: A cyclist rides 15 km at 12 km/h, "
                "then rests for 20 minutes, then rides another 10 km at 15 km/h. "
                "How long does the whole journey take?"
            )
        }
    ]
)

print(response.content[0].text)
```

The model will follow the two demonstrated examples: show step-by-step working, then state the answer on its own line beginning with "Answer:". The format is now a contract, not a guess [1].

### 5.5 When CoT helps and when it does not

CoT prompting improves quality on tasks that involve **multi-step reasoning** — tasks where the correct answer depends on a chain of intermediate conclusions. It does not uniformly improve all tasks, and adding a "think step by step" instruction to every prompt is unnecessary overhead for simple tasks [1][2][3].

**Tasks where CoT helps most:**

| Task type | Example |
|---|---|
| Arithmetic and maths word problems | Multi-step calculations, unit conversions, profit/loss scenarios |
| Logical deduction | "If A is true and B implies C, what follows?" |
| Planning and ordering | "What order should I perform these steps in?" |
| Code debugging | "What is wrong with this code and why?" |
| Comparative reasoning | "Which option is better, and why?" |

**Tasks where CoT adds little or no benefit:**

| Task type | Why CoT is unnecessary |
|---|---|
| Simple factual lookup | "What is the capital of France?" — no reasoning chain needed |
| Single-step classification | Assigning a sentiment label to a sentence |
| Creative generation | Writing a short poem — there is no correct reasoning chain |
| Direct format conversion | "Convert this CSV to JSON" |

A practical rule of thumb: if you could solve the task yourself in one mental step, the model probably does not need CoT. If you would write out intermediate steps on paper to solve it correctly, CoT is likely to help [2][3].

### 5.6 Extracting just the final answer

When you use CoT, the model's response contains both the reasoning chain and the final answer. For many applications you want to display or use only the final answer, not the full working.

Two common strategies:

**Strategy 1 — Ask the model to mark the final answer clearly.**

Instruct the model (in the system prompt or in the example) to put the final answer on a separate line in a predictable format — for example, "Answer: X" or "FINAL ANSWER: X". You can then split the response string on that marker.

```python
# Extract the final answer from a response that ends with "Answer: <value>"
answer_line = [
    line for line in response.content[0].text.splitlines()
    if line.startswith("Answer:")
]
final_answer = answer_line[0].replace("Answer:", "").strip() if answer_line else None
```

**Strategy 2 — Two-turn conversation.**

In the first turn, ask the model to reason step by step. In the second turn, ask it to state just the final answer. This two-step approach is less efficient (two API calls) but gives very clean extraction when the answer format is complex.

For your assessment portfolio, Strategy 1 is simpler and is the recommended starting point.

## 6. Implementation

### Step-by-step: adding CoT to a Python prompt

**Step 1 — Decide: zero-shot or few-shot?**

If you are exploring a new task and want to see what reasoning the model produces, start with zero-shot. If you need consistent formatting or the task has a specific reasoning pattern, use few-shot.

**Step 2 — Write the CoT instruction or examples.**

For zero-shot, add a trigger phrase to the system prompt:
```python
system = "Always think step by step before giving your final answer."
```

For few-shot, write two to three reasoning triples (input, step-by-step working, answer) as shown in section 5.4.

**Step 3 — Design a final-answer marker.**

Pick a consistent format your code can parse — for example, "Answer: <value>". Embed this marker in your system prompt instruction or in every example output.

**Step 4 — Make the API call.**

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system=(
        "You are a careful analyst. "
        "When answering questions, reason step by step. "
        "End every response with a line that starts with 'Answer:' followed by your conclusion."
    ),
    messages=[
        {
            "role": "user",
            "content": (
                "If I invest $1,000 at 5% annual interest compounded yearly for 3 years, "
                "how much will I have? Show your working."
            )
        }
    ]
)

print(response.content[0].text)
```

**Step 5 — Evaluate and iterate.**

Test on five to ten problems where you know the correct answer. Check: (a) Is the final answer correct? (b) Are the reasoning steps logically sound? (c) Is the format consistent? If the model skips steps or produces an inconsistent format, add a few-shot example that demonstrates the expected structure.

## 7. Real-World Patterns

### Where CoT prompting appears in working systems

**Code review and debugging tools.** When an AI assistant analyses a code snippet for bugs, a CoT prompt instructs it to trace through the code line by line before stating the problem. This produces more accurate bug identification than asking "what is wrong with this code?" directly, because the step-by-step trace catches logic errors that a pattern-match might miss [2][3].

**Decision support.** Tools that help users make choices — comparing insurance plans, evaluating job offers, selecting between technical architectures — use CoT prompts to ensure the model surfaces the key comparison criteria before making a recommendation. The visible reasoning also makes the output auditable: a user can check whether the model considered the factors that matter to them [1].

**Automated grading and feedback.** Educational tools that assess student answers often use CoT to have the model work through the expected solution before comparing it against the student's response. This reduces false negatives where a technically correct but differently worded answer is marked wrong [2].

**Data validation pipelines.** When a model is used to check whether a record meets a complex rule — for example, "does this loan application satisfy all compliance criteria?" — CoT forces the model to check each criterion explicitly rather than guess at the overall verdict. The reasoning chain also serves as an audit log [3].

## 8. Best Practices

### Do

- **Use a clear, consistent final-answer marker.** Phrases like "Answer:", "Final answer:", or "RESULT:" give you a reliable extraction point. Embed the same marker in every few-shot example so the model learns the convention [1][2].
- **Put the step-by-step instruction in the system prompt when you want it applied to every message in the session.** For one-off calls, putting it in the user message is fine.
- **Match your example reasoning depth to the real task.** If a task normally takes three steps, your examples should show three steps — not two (too sparse) or seven (too verbose and hard to follow).
- **Test your CoT prompt against problems where you already know the right answer.** This is the only reliable way to verify the reasoning chain is sound, not just plausible-sounding.
- **Use `max_tokens` generously when using CoT.** Reasoning chains use more tokens than direct answers. A `max_tokens` that is too low will cut off the chain mid-step [2].

### Do not

- **Do not add "think step by step" to every prompt indiscriminately.** For simple, single-step tasks it wastes tokens, increases latency, and can make the response more verbose without improving accuracy [1].
- **Do not accept a plausible-looking reasoning chain without checking it.** A model can produce confident-sounding but logically flawed intermediate steps. The chain of thought makes errors *visible*, but you still need to read it.
- **Do not use CoT as a substitute for providing the model with the right information.** If the model is wrong because it lacks a key fact, CoT will produce a well-structured wrong answer. CoT helps the model reason better with what it has; it does not supply missing knowledge.
- **Do not write examples where the reasoning steps jump over sub-problems.** If your example skips a step that is not obvious, the model will learn to skip it too.

## 9. Hands-On Exercise

**Sketch:** Apply CoT to the domain you are using for Assessment A4 (Python and Prompt Engineering Portfolio, due this week).

1. Pick one question or decision from your domain that genuinely requires multiple steps to answer — for example, calculating a value, ranking options, or diagnosing a problem.
2. Write a zero-shot CoT prompt: add "Think step by step before giving your final answer." to your existing system prompt.
3. Run the prompt and read the reasoning chain the model produces. Identify any step where the reasoning is wrong or jumps too far.
4. Convert to few-shot CoT: write two example reasoning triples (input → step-by-step working → final answer) that demonstrate the correct reasoning structure for your domain.
5. Compare zero-shot vs few-shot on three test inputs. Note which version produces more reliable final answers.

This exercise maps directly to the week's lab activity (testing three prompt versions on ten domain-relevant inputs each).

## 10. Key Takeaways

- **Chain-of-thought (CoT) prompting asks the model to reason step by step before giving a final answer.** Visible intermediate steps reduce errors on multi-step tasks by giving the model's generation process the right context at each stage.
- **Zero-shot CoT adds a trigger phrase ("think step by step") with no examples.** It is the fastest way to get step-by-step reasoning and works well for exploratory use.
- **Few-shot CoT provides example reasoning triples (input → working → answer).** It produces more consistent formatting and domain-specific reasoning structure than zero-shot CoT.
- **CoT helps most on arithmetic, logical deduction, planning, and comparative reasoning.** It adds little value on simple factual lookups or single-step tasks.
- **Always design a clear final-answer marker** so your Python code can extract the conclusion from the full reasoning response reliably.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
