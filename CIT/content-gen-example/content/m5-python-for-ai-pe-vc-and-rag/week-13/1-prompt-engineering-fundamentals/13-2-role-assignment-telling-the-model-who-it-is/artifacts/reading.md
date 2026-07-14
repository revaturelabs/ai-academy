<!-- nav:top:start -->
[⬅ Previous: 13.1 — System prompt vs user prompt](../../13-1-system-prompt-vs-user-prompt-context-setting-vs-the-live-req/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.3 — Few-shot examples ➡](../../13-3-few-shot-examples-showing-the-model-what-good-output-looks-l/artifacts/reading.md)
<!-- nav:top:end -->

---

# Role Assignment — Telling the Model Who It Is

## Overview

When you place a sentence like "You are a Python tutor for beginners" at the top of a system prompt, you are doing **role assignment** — giving the model an identity to adopt for the entire conversation. This single instruction shapes the model's vocabulary, tone, and focus before the user types a single word. Understanding role assignment well is a core prompt-engineering skill because it is the most direct way to calibrate how a model responds to any audience or task.

## Key Concepts

### What a role statement is

A **role statement** is a sentence in the system prompt that declares an identity or persona for the model to adopt [1]. The simplest and most common form is:

> "You are a [role]."

For example:
- "You are a Python tutor for beginners."
- "You are a financial advisor specializing in personal budgeting."
- "You are a friendly customer support agent for an e-commerce store."

Short as it looks, a role statement tells the model three things at once:

1. **Who it is** — the identity label.
2. **What domain of knowledge to draw on** — the subject area.
3. **How to speak** — the implied tone and **register** (register means the level of formality and technical detail in language, for example academic versus conversational).

Think of it like a costume, not a transplant. The model is still the same LLM (Large Language Model — a type of AI that predicts text by learning patterns from enormous amounts of written language). What the role changes is how it selects and frames its words. The same actor can play a doctor or a pirate; the underlying person is unchanged, but the costume shapes how they walk, talk, and behave on stage.

### How a role statement changes model output

Without any role statement, the model defaults to a general-purpose assistant register — helpful but not calibrated. It does not know whether you are a student, a professional, or an expert. A role statement solves that uncertainty up front [1].

| What changes | Without a role statement | With "You are a Python tutor for beginners" |
|---|---|---|
| **Vocabulary level** | May use advanced terms without explanation | Avoids jargon; explains terms step by step |
| **Tone** | Neutral, general | Encouraging, patient, educational |
| **Focus** | Draws on all its knowledge | Stays in the Python-for-beginners lane |

Research confirms this effect is real, though it varies by task [3]. Role assignment measurably shifts output quality for tasks that benefit from a specific expertise lens — tutoring, legal drafting, creative writing, domain-specific support. For tasks already well-scoped by the user prompt (for example, "translate this sentence to French"), the role statement adds little [2][3].

### Where the role statement goes

The role statement belongs at the **start of the system prompt** [1]. You already know from topic 13.1 that the system prompt is the place for persistent context with higher authority than the user prompt. The role is the first thing you write there — everything else (instructions, constraints, additional context) follows after it.

This placement matters. The model reads the system prompt from top to bottom, and the role sets the interpretive frame for every instruction that comes after it. Putting the role at the end forces the model to reconcile its identity with instructions it already started reading in a different frame. Putting the role first means every subsequent instruction is read through the established identity.

In an Anthropic API call (which you built in topic 12.10), the system prompt sits in the `system` parameter:

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    system="You are a Python tutor for beginners. Explain concepts clearly and use simple code examples.",
    messages=[
        {"role": "user", "content": "What is a list in Python?"}
    ]
)

print(response.content[0].text)
```

The role statement is the first sentence in `system`. The instruction that follows (`"Explain concepts clearly…"`) builds on the role — it does not need to re-establish who the model is.

### Specificity: the single most important lever

Two role statements can both be grammatically correct and produce very different results:

| Role statement | What the model has to work with |
|---|---|
| "You are an expert." | Vague — expert in what? at what level? for whom? |
| "You are a senior data analyst explaining results to a non-technical marketing team." | Specific — domain, seniority, and audience all defined |

**Specificity** is the single most important quality of a role statement [1][2]. Three dimensions are worth specifying:

1. **Domain** — what field or subject matter (e.g., Python, tax law, pediatric medicine).
2. **Expertise level** — beginner tutor, senior engineer, or specialist (signals vocabulary depth and assumed audience knowledge).
3. **Relationship to the user** — teacher, colleague, advisor, assistant (signals tone and register).

Each dimension you add narrows the space of appropriate answers — which is exactly what you want when you have a clear use case. You do not have to specify all three every time. A short interaction may only need the domain. But when output quality matters, adding expertise level and relationship often moves the needle [2].

### When role assignment helps — and when it does not

Role assignment is a calibration tool, not a universal booster [2][3].

**It tends to help when:**
- The task requires a specific tone or register (formal legal language vs. friendly tutoring).
- The task is domain-specific and benefits from filtering out irrelevant knowledge.
- The user prompt is open-ended and needs focus.
- The output is targeted at a specific audience (e.g., "explain this to a 10-year-old").
- The conversation spans many turns and needs a consistent voice throughout.

**It tends to have less effect when:**
- The user prompt is already highly specific and self-contained.
- The task is simple and well-defined (translation, arithmetic, format conversion).
- The stated role is so vague it gives the model no useful signal.
- The role conflicts with what the task actually needs.

A quick mental test: ask yourself, "Would a human expert's job title change how they answer this?" If yes — a lawyer and a comedian would answer differently — role assignment is worth trying. If no — they would both say the same thing — it is unlikely to add value.

## Worked Example

The example below shows the same user question answered under three different system prompts. The user message never changes. Only the system prompt changes.

**User message (identical in all three versions):**
> "Can you explain for loops to me?"

---

**Version A — No role statement:**
```python
system = "Answer the user's questions helpfully."
```

Likely output:
> "A for loop is a control flow statement that iterates over a sequence (such as a list, tuple, string, or range) and executes a block of code for each item. For example: `for i in range(5): print(i)` — this prints 0, 1, 2, 3, 4."

The answer is correct. But it uses the term "control flow statement," assumes the user knows what a sequence is, and jumps straight to code with no scaffolding. A complete beginner may be confused.

---

**Version B — Vague role statement:**
```python
system = "You are an expert. Answer the user's questions."
```

Likely output: very similar to Version A. "Expert" gives the model no domain, no audience, and no register signal. The vague role adds almost nothing.

---

**Version C — Specific role statement:**
```python
system = (
    "You are a Python tutor for complete beginners who have never written code before. "
    "When explaining concepts, start with an everyday analogy, then show a short Python example, "
    "then explain what the code does line by line."
)
```

Likely output:
> "Think of a for loop like a checklist. Imagine you have a grocery list with five items. You go through item by item — you don't skip any, and you stop when the list is done. A for loop works the same way.
>
> ```python
> fruits = ["apple", "banana", "cherry"]
> for fruit in fruits:
>     print(fruit)
> ```
> Line 1: We create a list called `fruits` with three items.
> Line 2: The for loop says 'go through each item in fruits, one at a time, and call it `fruit`.'
> Line 3: For each item, we print it. So this code prints apple, then banana, then cherry."

The user prompt is identical across all three versions. The extra twenty words in Version C's system prompt — a specific role with domain, audience, and a concrete instruction about structure — produced an output with an analogy, stepped code explanation, and zero assumed background. That is the practical value of specificity [1].

## In Practice

Role assignment is standard practice in production AI applications. Here are four common patterns.

**Customer support bots.** System prompts for support applications open with something like: "You are a helpful customer support agent for [Company]. You are friendly, concise, and always try to resolve the issue in the fewest steps possible." The role anchors tone and focus across thousands of conversations, keeping every session feeling consistent.

**Educational platforms.** A tutoring application may use: "You are a patient math tutor for high school students. You never give the answer directly; instead, you guide the student step by step." The role enforces a teaching method — a model told it is a patient tutor will naturally resist blurting out the answer because that behavior conflicts with the stated identity.

**Code review assistants.** Development teams often assign a role like: "You are a senior software engineer on the backend team. When reviewing code, you prioritize correctness first, then security, then readability." A junior developer submitting code gets feedback calibrated to those priorities. For instance, if a function passes unvalidated user input straight to a database query, the model flags the SQL injection risk (SQL injection is a type of cyberattack where malicious input is used to manipulate a database) before commenting on style — because security is the team's second priority after correctness [1][2].

**Content safety.** Platforms serving children often add role constraints: "You are a content assistant for a children's education platform. You respond only to topics appropriate for ages 8–12." The role is part of a safety boundary. It does not replace other safety mechanisms, but it frames how the model interprets ambiguous requests [2].

**Do / Do not — quick reference:**

| Do | Do not |
|---|---|
| Place the role at the very start of the system prompt | Use vague one-word roles like "You are an expert." |
| Specify domain, expertise level, and relationship to user | Assign a role that conflicts with the task |
| Test with real inputs and adjust | Assume the role alone is enough without further instructions |
| Keep the role aligned with the instructions that follow | Place the role at the end of a long system prompt |

Two anti-patterns to avoid:

- **The inflated title.** Prompts like "You are a world-renowned genius and top expert in all fields" rarely produce meaningful improvement and can generate overconfident or inconsistent outputs [3]. Ground your role in the actual task domain.
- **Role contradiction.** "You are a creative, free-flowing storyteller. Always answer in exactly three bullet points." These instructions fight each other. Keep role and instructions pointing in the same direction [1].

## Key Takeaways

- A **role statement** is a sentence at the start of the system prompt that tells the model what identity or persona to adopt — the simplest form is "You are a [role]" [1].
- A role statement shapes **tone, vocabulary level, and domain focus** without changing the underlying model; it works like a costume, not a transplant [1][2].
- **Specificity is the key lever.** Including domain, expertise level, and relationship to the user produces more targeted outputs than a generic label. Each dimension added narrows the space of appropriate answers.
- **Register** — the level of formality and technical detail — is one of the primary things a role statement calibrates. A well-chosen role signals the right register before the user types a word.
- Role assignment helps most on open-ended tasks that need a specific register or audience calibration; it helps less on already well-scoped, simple tasks [2][3].
- The role statement goes **first** in the system prompt; all instructions that follow build on top of it.

## References

1. Learn Prompting — Role Prompting. https://learnprompting.org/docs/advanced/zero_shot/role_prompting
2. PromptHub — Role Prompting: Does Adding Personas to Your Prompts Really Make a Difference? https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference
3. Arxiv — Role prompting research (2311.10054v3). https://arxiv.org/html/2311.10054v3

---
<!-- nav:bottom:start -->
[⬅ Previous: 13.1 — System prompt vs user prompt](../../13-1-system-prompt-vs-user-prompt-context-setting-vs-the-live-req/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.3 — Few-shot examples ➡](../../13-3-few-shot-examples-showing-the-model-what-good-output-looks-l/artifacts/reading.md)
<!-- nav:bottom:end -->
