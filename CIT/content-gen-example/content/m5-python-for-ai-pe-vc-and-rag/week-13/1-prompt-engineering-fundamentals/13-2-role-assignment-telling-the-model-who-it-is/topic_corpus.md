---
topic_id: "13.2"
title: "Role assignment — telling the model who it is"
position_in_module: 2
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. Role Assignment — Telling the Model Who It Is — Topic Corpus

## 2. Prerequisites

- **13.1 — System prompt, user prompt, and prompt structure**: students know what a system prompt is, that it carries persistent context, and that it has higher authority than the user prompt. This topic builds directly on that knowledge by introducing the most common thing placed in a system prompt.
- **12.10 / 12.11 — Anthropic API calls**: students can make a `client.messages.create()` call and understand the `system` parameter. Code examples here use that call shape.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** role assignment and explain what placing a role statement in a system prompt tells the model.
2. **Write** a basic role statement using the "You are a [role]" pattern and insert it into the `system` parameter of an Anthropic API call.
3. **Explain** how a role statement changes a model's tone, vocabulary, and level of expertise in its replies.
4. **Distinguish** situations where role assignment improves output quality from situations where it has little or no measurable effect.
5. **Identify** two common mistakes made when writing role statements and state how to avoid them.

## 4. Introduction

Imagine you are calling a customer service line. The moment the agent says, "Hi, I'm Alex, a senior technical support engineer," you shift your expectations. You expect precise answers, technical vocabulary, and calm professionalism — not a casual chat.

You can do the same thing with an AI model. Before the conversation starts, you tell the model: "You are a senior technical support engineer." From that point on, the model frames every answer from that perspective. This is **role assignment** — placing a statement in the system prompt that tells the model what kind of expert, persona, or character it should behave like [1].

You already know (from 13.1) that the system prompt is the place for persistent context that shapes the entire conversation. A role statement is the most direct way to use that space. It is the first line many professional prompt engineers write when they open a new system prompt.

This topic teaches you what a role statement does, how to write one, and — just as importantly — when it genuinely helps versus when it makes no real difference.

## 5. Core Concepts

### 5.1 What a role statement is

A **role statement** is a sentence in the system prompt that declares an identity or persona for the model to adopt during the conversation [1]. The simplest form is:

> "You are a [role]."

Examples:
- "You are a Python tutor for beginners."
- "You are a financial advisor specializing in personal budgeting."
- "You are a friendly customer support agent for an e-commerce store."

The phrase is short and direct. It tells the model three things at once:
1. **Who** it is (the identity label).
2. **What kind of knowledge** it should draw on (the domain).
3. **How** it should speak to the user (the implied tone and **register** — the level of formality and technical detail in language, for example academic versus conversational).

The model uses this information to calibrate every response that follows [1][2].

To understand why this matters, think about how a human expert adapts. A cardiologist explaining a heart condition to a medical colleague uses Latin terminology, assumes shared anatomical knowledge, and skips basic definitions. The same cardiologist talking to a patient uses plain words, relies on analogies, and checks for understanding repeatedly. The underlying expertise is identical — what changes is the register and framing. A role statement instructs the model to make exactly that kind of adjustment.

Without any role statement, the model defaults to a general-purpose assistant register — helpful but not calibrated. It does not know if you are a student, a professional, or an expert. It cannot guess whether you want a quick summary or a deep technical breakdown. The role statement solves that uncertainty up front.

Contrast these two opening lines:

| System prompt opening | What the model infers |
|---|---|
| (nothing — blank system prompt) | General assistant, unknown audience, neutral register |
| "You are a tax accountant advising small business owners." | Domain is tax law, audience is non-specialist business owners, register should be professional but accessible |

The second line hands the model a complete interpretive frame before the user even types their first message. Every reply the model gives is then filtered through that frame.

### 5.2 How the model uses a role statement

When the model reads a role statement, it does not become a different program. It is still the same LLM (Large Language Model — a type of AI that predicts text by learning patterns from enormous amounts of written language). What changes is how it selects and frames its words.

Think of it like a costume, not a transplant. The same actor can play a doctor or a pirate; the underlying person is unchanged, but the costume shapes how they walk, talk, and behave on stage.

Concretely, a role statement shifts three things [1][2]:

| What changes | Without a role statement | With "You are a Python tutor for beginners" |
|---|---|---|
| **Vocabulary level** | May use advanced terms without explanation | Avoids jargon; explains terms step by step |
| **Tone** | Neutral, general | Encouraging, patient, educational |
| **Focus** | Draws on all its knowledge | Stays in the Python-for-beginners lane |

Research confirms this effect is real, though it varies by task [3]. For tasks that benefit from a specific expertise lens — tutoring, legal drafting, medical triage descriptions, creative writing — role assignment measurably shifts output quality. For tasks that are already well-scoped by the user prompt (e.g., "translate this sentence to French"), the role statement adds little [2][3].

It is worth being concrete about what "shifts output quality" means in practice. Suppose you ask "What is a variable?" with no role statement. The model might answer:

> "A variable is a named storage location in memory that holds a value which can be changed during program execution."

That is technically correct. Now ask the same question with the role statement "You are a Python tutor for complete beginners who have never written code before":

> "A variable is like a labeled box where you can store information. Imagine a box with the label 'age' written on it. You can put the number 25 in that box, and later swap it for 30. In Python, you create a variable like this: `age = 25`. That's it — Python now remembers that `age` means 25 until you change it."

Same underlying knowledge. Different role. Dramatically different output — more relatable, more appropriate for the audience, and far more likely to produce genuine understanding in a beginner.

### 5.3 Where the role statement goes

The role statement belongs at the **start of the system prompt** [1]. Everything else in the system prompt — instructions, constraints, context — follows after it. This placement matters because the model reads the system prompt top to bottom, and the role sets the interpretive frame for everything that comes after.

In an Anthropic API call (which you built in 12.10–12.11), the system prompt lives in the `system` parameter:

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

The role statement (`"You are a Python tutor for beginners."`) is the first sentence. The sentence after it (`"Explain concepts clearly…"`) adds instruction, building on the role. This is the standard pattern [1].

Why does position matter? Because the model's understanding of what it is supposed to be doing frames how it reads every instruction that follows. Consider this system prompt:

> "Be concise. Use bullet points. Always give a code example. You are a Python tutor for beginners."

Versus:

> "You are a Python tutor for beginners. Be concise. Use bullet points. Always give a code example."

Both contain the same sentences. But when the role comes last, the model has already begun building an interpretive frame from the instructions — and the role statement must then reconcile itself with that partial frame. When the role comes first, every instruction that follows is read through the established identity. Putting the role first is a matter of clarity, not magic — it matches the natural order in which context should be layered.

### 5.4 Specificity: the single most important lever

Two role statements can both be grammatically correct but produce very different results:

| Role statement | What the model has to work with |
|---|---|
| "You are an expert." | Vague — expert in what? at what level? for whom? |
| "You are a senior data analyst explaining results to a non-technical marketing team." | Specific — domain, seniority, and audience all defined |

**Specificity** is the single most important quality of a role statement [1][2]. The more detail you supply about the role's domain, expertise level, and intended audience, the more precisely the model can calibrate its response. Vague roles produce generic responses. Specific roles produce targeted ones.

Three dimensions worth specifying:
1. **Domain** — what field or subject matter (e.g., Python, tax law, pediatric medicine).
2. **Expertise level** — beginner tutor, senior engineer, specialist (signals vocabulary depth and assumed audience knowledge).
3. **Relationship to the user** — teacher, colleague, advisor, assistant (signals tone and social register — the degree of formality and assumed familiarity).

You do not have to specify all three in every case. A short interaction may only need the domain. But when output quality matters, adding expertise level and relationship often moves the needle [2].

Here is a progression that illustrates how each added dimension changes the output:

**Stage 1 — domain only:**
> "You are a nutritionist."

The model knows the subject area. It will answer questions about food and health. But it does not know if you are a professional asking for clinical detail or a college student asking how to eat better on a budget. Its answers will be competent but generic.

**Stage 2 — domain + expertise level:**
> "You are a registered nutritionist who works with people who have no nutrition training."

Now the model knows it should avoid clinical jargon, skip assumed background knowledge, and translate complex concepts into plain language. Outputs become noticeably more accessible.

**Stage 3 — domain + expertise level + relationship to user:**
> "You are a registered nutritionist advising a busy parent who wants simple, practical meal ideas for family dinners. You keep suggestions to five ingredients or fewer."

Now the model has a complete picture: subject area (nutrition), depth level (plain language, no assumed training), audience (a busy parent), and a concrete constraint (five ingredients). Every answer it gives can be tightly calibrated to that frame.

Each added dimension narrows the space of appropriate answers — which is exactly what you want when you have a clear use case. The model's job becomes easier when the role is more specific, and your outputs become more consistent and useful.

### 5.5 When role assignment helps and when it does not

Role assignment is not magic. Evidence from practice and research shows a pattern [2][3]:

**Role assignment tends to help when:**
- The task requires a specific tone or register (e.g., formal legal language vs. friendly tutoring).
- The task is domain-specific and benefits from filtering out irrelevant knowledge.
- The user prompt is open-ended and needs focus.
- The output will be read by a specific audience (e.g., "explain this to a 10-year-old").
- The conversation will span many turns and needs a consistent voice across all of them.
- The model needs to stay within a particular style of communication (e.g., always supportive, never directive).

**Role assignment tends to have less effect when:**
- The user prompt is already highly specific and self-contained.
- The task is simple and well-defined (translation, arithmetic, format conversion).
- The role stated is so vague it gives the model no useful signal.
- The role conflicts with what the task actually needs (e.g., assigning a "creative storyteller" role for a task that requires factual, structured output).
- The task has a single correct answer that does not depend on tone or framing (e.g., "What is 2 + 2?").

A useful mental test: ask yourself, "Would a human expert's job title change how they answer this?" If yes — "a lawyer would answer differently than a comedian" — then role assignment is worth trying. If no — "a lawyer and a comedian would both say the same thing" — then role assignment is unlikely to add value.

This means role assignment is a **calibration tool**, not a universal booster. You test it, observe the outputs, and adjust [2][3].

## 6. Implementation

### Writing a role statement: step-by-step

Follow these steps to write an effective role statement for your system prompt:

1. **Identify the task domain.** What subject matter does this conversation need to stay in? (e.g., Python, customer support, medical education).

2. **Choose an expertise level.** Should the model respond as a beginner tutor, a peer, or a domain expert? Pick the level that matches what your user needs.

3. **Identify the user.** Who is asking? This helps define tone and register — the level of formality appropriate to the relationship. "Explain to a beginner" signals different language than "advise a senior engineer."

4. **Draft the role statement.** Combine domain + expertise + relationship into one or two sentences:
   - Minimal: `"You are a Python tutor."`
   - Better: `"You are a Python tutor for absolute beginners."`
   - Best (for most tasks): `"You are a Python tutor for absolute beginners. You explain concepts using simple words and short code examples, and you always check whether the learner understood before moving on."`

5. **Place it first in the system prompt.** Then add any additional instructions after it.

6. **Test with representative inputs.** Send 2–3 typical user messages and compare the outputs to what you get without the role statement. Adjust the role if the outputs are still too generic or miss the target tone or focus [2].

### Before-and-after comparison: vague role vs. specific role

This comparison shows the same task — answering a question about Python loops — under three different system prompts. The user message never changes. Only the system prompt changes.

**User message (same in all three cases):**
> "Can you explain for loops to me?"

---

**Version A — No role statement:**
```python
system = "Answer the user's questions helpfully."
```

Likely model output:
> "A for loop is a control flow statement that iterates over a sequence (such as a list, tuple, string, or range) and executes a block of code for each item. For example:
> `for i in range(5): print(i)` — this prints 0, 1, 2, 3, 4."

The answer is correct. But it uses the term "control flow statement," assumes the user knows what a sequence is, and jumps straight to code with no scaffolding. A complete beginner may be confused.

---

**Version B — Vague role statement:**
```python
system = "You are an expert. Answer the user's questions."
```

Likely model output:
Very similar to Version A. "Expert" gives the model no domain information (expert in what?), no audience information (talking to whom?), and no register signal (how formal? how detailed?). The vague role adds almost nothing.

---

**Version C — Specific role statement:**
```python
system = (
    "You are a Python tutor for complete beginners who have never written code before. "
    "When explaining concepts, start with an everyday analogy, then show a short Python example, "
    "then explain what the code does line by line."
)
```

Likely model output:
> "Think of a for loop like a checklist. Imagine you have a grocery list with five items. You go through item by item — you don't skip any, and you stop when the list is done. A for loop works the same way.
>
> Here is a simple Python example:
> ```python
> fruits = ["apple", "banana", "cherry"]
> for fruit in fruits:
>     print(fruit)
> ```
> Line 1: We create a list called `fruits` with three items.
> Line 2: The for loop says 'go through each item in fruits, one at a time, and call it `fruit`.'
> Line 3: For each item, we print it. So this code prints apple, then banana, then cherry."

The user prompt is identical across all three versions. The specific role in Version C produced an output with an analogy, stepped code explanation, and zero assumed background — exactly what a beginner needs.

This before-and-after shows the practical value of moving from vague to specific. The extra twenty words in the system prompt paid off in a substantially more useful response [1].

### Example: adding a role to a prior-state prompt

**Without a role statement:**
```python
system = "Answer the user's questions."
```
User asks: "What is recursion?"
Model responds with a technically accurate but possibly dense explanation mixing beginner and advanced phrasing.

**With a specific role statement:**
```python
system = "You are a Python tutor for absolute beginners. Use simple words and at least one short code example in every answer."
```
User asks: "What is recursion?"
Model responds with a plain-English definition, an analogy, and a short Python function — calibrated to a beginner audience.

The user prompt (`"What is recursion?"`) is identical. Only the system prompt changed. The role statement did the work [1].

## 7. Real-World Patterns

Role assignment is standard practice in production AI applications. Here are patterns you will encounter [1][2]:

**Pattern 1: Customer support bots**

System prompts for customer support applications typically open with something like: "You are a helpful customer support agent for [Company]. You are friendly, concise, and always try to resolve the issue in the fewest steps possible."

The role anchors tone and focus across thousands of conversations. Without it, different sessions may feel inconsistent — sometimes formal, sometimes casual, sometimes overly technical. With it, every conversation opens with the same implied register: approachable, solution-focused, brief.

A worked example: a software company deploys a support bot for a billing product. Their system prompt opens with:

> "You are a friendly billing support specialist for Acme Software. You help customers understand their invoices, update payment methods, and resolve subscription issues. You always confirm what the customer wants before making any changes, and you escalate to a human agent if the request involves a refund over $500."

Notice how the role (billing support specialist) combines with the company name, a task scope (invoices, payment, subscriptions), a behavioral instruction (confirm before changing), and a safety boundary (escalate above $500). The role is the first anchor, and every instruction after it makes sense in that context [2].

**Pattern 2: Educational platforms**

A tutoring application may use: "You are a patient math tutor for high school students. You never give the answer directly; instead, you guide the student step by step."

The role enforces a specific teaching method the platform values — the Socratic approach of guiding rather than telling. This kind of behavioral constraint is much easier to maintain when the role establishes the identity first. A model told "You are a patient tutor" will naturally resist blurting out the answer, because that behavior conflicts with the stated identity. Without the role, the instruction "never give the answer directly" sits in isolation and is more easily overridden by an impatient user message.

**Pattern 3: Code review assistants for teams**

Development teams building internal tools often assign a role like: "You are a senior software engineer on the backend team. When reviewing code, you prioritize correctness first, then security, then readability. You are direct and specific — you do not say 'looks good' without explaining why."

This pattern is particularly interesting because it encodes a team's review culture into the role. The model is not just a generic code reviewer — it is positioned as a teammate with the team's specific priorities. A junior developer submitting code gets feedback calibrated to those priorities rather than generic best-practice advice.

A worked example session: the user pastes a Python function that reads user input and passes it directly to a database query. With the role above, the model's first comment addresses correctness (does the function work?), then raises a security flag (SQL injection risk from unvalidated input), then mentions style. Without the role, the model might lead with style comments or skip the security issue entirely — because it has no signal that this team values security second [1][2].

**Pattern 4: Content moderation and safety**

Platforms that serve children or regulated industries often append role constraints: "You are a content assistant for a children's education platform. You respond only to topics appropriate for ages 8–12."

The role is part of a safety boundary [2]. It does not replace other safety mechanisms, but it establishes the frame from which the model interprets ambiguous requests. A request like "tell me about violence" is handled very differently by a model that has been told it is an assistant for 8-to-12-year-olds than by a model with no stated identity.

In all these cases, the role statement is the first line in the system prompt, and everything else builds on it. Removing the role statement and keeping only the instructions still works, but the tone and framing consistency tend to degrade over a multi-turn conversation [1][2].

## 8. Best Practices

**Do:**
- Place the role statement at the very start of the system prompt.
- Be specific: include domain, expertise level, and relationship to the user.
- Test your role statement with real inputs before finalizing it.
- Adjust the role when test outputs are consistently missing the target tone or focus.
- Align the role with the instructions that follow — both should point in the same direction.

**Do not:**
- Use vague one-word roles like "You are an expert." with no domain or context.
- Assign a role that conflicts with the task (e.g., "You are a creative storyteller" for a task that needs factual, structured answers).
- Assume a role statement alone is enough — follow it with concrete instructions for what to do and how to respond [1][2].
- Place the role statement at the end of a long system prompt — position matters.

**Anti-pattern: the inflated title**
Some prompts use impressive-sounding titles ("You are a world-renowned genius and top expert in all fields") hoping for better answers. Research shows this rarely produces meaningful improvement and can produce overconfident or inconsistent outputs [3]. Ground your role in the actual task domain.

**Anti-pattern: role contradiction**
If the role implies one behavior but your instructions demand another, the model has to pick. Example: "You are a creative, free-flowing storyteller. Always answer in exactly three bullet points." These instructions fight each other. Keep the role and the instructions aligned [1].

## 9. Hands-On Exercise

**Exercise: Three versions of the same system prompt**

Pick the domain you are building for Assessment 4 (e.g., a Python coding assistant, a customer support bot, a tutoring app).

1. Write three system prompts for that domain:
   - **Version A:** No role statement — just instructions.
   - **Version B:** A minimal role statement ("You are a [role].") plus the same instructions.
   - **Version C:** A specific role statement (domain + expertise level + relationship) plus the same instructions.

2. For each version, send the same 3–5 user messages using your Anthropic API setup from weeks 11–12.

3. Compare the outputs. Does the tone change? Does the vocabulary level shift? Does the model stay focused on the intended domain? Which version performs best for your use case?

This exercise maps directly to the lab activity for this week: writing multiple prompt versions and measuring them against test inputs — a skill you will use in Assessment 4.

## 10. Key Takeaways

- A **role statement** is a sentence at the start of the system prompt that tells the model what identity or persona to adopt (e.g., "You are a Python tutor for beginners") [1].
- A role statement shapes the model's **tone, vocabulary level, and domain focus** without changing the underlying model [1][2].
- **Specificity is the key lever:** including domain, expertise level, and relationship to the user produces more targeted outputs than a generic label. Each additional dimension of specificity narrows the space of appropriate answers.
- **Register** — the level of formality and technical detail in language — is one of the primary things a role statement calibrates. A well-chosen role signals the right register before the user types a single word.
- Role assignment helps most on open-ended tasks that need a specific register or audience calibration. It helps less on already well-scoped, simple tasks [2][3].
- The role statement goes **first** in the system prompt; instructions that follow build on top of it.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
