---
topic_id: "12.10"
title: "The Anthropic API — model, messages array, system prompt, user prompt, authentication"
position_in_module: 2
generated_at: "2026-06-15T00:00:00Z"
resource_count: 3
---

# 1. The Anthropic API — model, messages array, system prompt, user prompt, authentication — Topic Corpus

## 2. Prerequisites

This topic builds directly on topic 12.9 — "What an API is — a door into another system; request and response." You need to know what an API is, what a request and response look like, what an API key does, and what JSON is before reading this topic. All of those concepts were introduced in 12.9.

You also need the Python basics from topics 12.1–12.5: functions, dictionaries, and lists. The messages array is a Python list of dictionaries, so those concepts will appear in examples here.

## 3. Learning Objectives

By the end of this topic you should be able to:

- Identify the five parts of an Anthropic API call: the model name, the messages array, the system prompt, the user prompt, and the API key.
- Describe what the `messages` array is, and explain why each item in that array must have a `role` field and a `content` field.
- Explain the difference between a system prompt and a user prompt, and state when you would use each.
- Describe what the `model` parameter controls and give an example of a valid model name.
- Explain what an API key is, why it must be kept secret, and how it is used to authenticate a request.
- Read a skeleton request structure and correctly label each field.

## 4. Introduction

You have already learned that an API is a door into another system. When you call the Anthropic API, you are sending a request through that door to a Claude model running on Anthropic's servers. Claude reads your request, generates a response, and sends it back to your Python program.

The tricky part is not the concept — it is the format. Anthropic's API has a specific shape it expects every request to take. If you send the wrong shape, the API refuses the request and returns an error. If you send the right shape, Claude responds.

This topic is entirely about that shape. By the end you will know exactly what fields go inside a request and why each one is there. You are not going to write the Python code to send the request yet — that is topic 12.11. Right now you are learning the anatomy: what the parts are called, what they mean, and how they fit together.

Think of it like filling in a form before you post it. You need to understand every blank on the form before you can fill it in correctly. This topic is the form.

## 5. Core Concepts

### 5.1 The Messages API

The Anthropic API uses an endpoint called the **Messages API**. An endpoint (defined in topic 12.9) is a specific address you send your request to. The Messages API endpoint accepts a POST request — meaning you are sending data to it — and returns a response containing Claude's reply [1].

Every request to the Messages API must include at least these four things:

1. The **model** you want to use.
2. The **messages array** containing the conversation.
3. A **system prompt** that sets the context and rules for Claude's behavior.
4. An **API key** that authenticates you as the caller.

The API also requires some additional parameters (such as reply-length limits) that are introduced in topic 12.11.

Each of these is explained in its own sub-section below.

---

### 5.2 The `model` Parameter

**`model`** — the name of the specific Claude model version you want to use for this request.

Anthropic runs several different versions of Claude. Each version has a name — a string like `"claude-opus-4-5"` or `"claude-haiku-3-5"`. When you send a request you must say exactly which version you want. You cannot just say "give me Claude" — you have to be specific [1].

#### Why does this matter?

Different model versions have different capabilities and costs. Larger, more capable models generate higher-quality responses but cost more per request and take slightly longer to reply. Smaller, faster models are cheaper and quicker, which matters if you are processing thousands of requests. By requiring you to name a specific model, the API guarantees that the behavior of your program is predictable — if Anthropic releases a new model version, your existing code keeps using the version you named rather than switching automatically.

**Example model names** (as of the knowledge cutoff):

| Model name | Typical use |
|---|---|
| `claude-opus-4-5` | Highest quality, complex reasoning tasks |
| `claude-sonnet-4-5` | Balanced quality and speed |
| `claude-haiku-3-5` | Fast and low cost, simpler tasks |

In your Python code, `model` is just a string. You pass it as a key-value pair, like any other dictionary entry:

```python
# Selecting the model — a string value in a dictionary key
model_choice = "claude-haiku-3-5"
```

You will see exactly how to pass it inside a live API call in topic 12.11.

#### Common misconception: "I can pass any string"

The `model` parameter must be one of the exact model name strings that Anthropic publishes. If you pass a string that does not match a known model name — for example `"claude-fast"` or `"claude"` — the API will return a `404` or `invalid_request_error` response. It will not guess what you meant. Always copy the model name exactly as Anthropic documents it [1].

#### What `model` does NOT control

The `model` parameter tells the API which Claude version to use. It does not control what you ask Claude, how Claude should behave, or who you are. Those are handled by the other fields.

---

### 5.3 The `messages` Array

**`messages`** — a list (array) of conversation turns, where each turn is a dictionary with exactly two required fields: `role` and `content` [1] [3].

This is the most important structural concept in the whole API.

#### Why a list of turns?

Claude is a conversational model. It is designed to participate in back-and-forth conversations, not just answer a single question in isolation. The `messages` array represents that conversation history. Each item in the list is one turn.

Even if you are only asking one question, you still pass a list — a list with one item. This consistency is intentional: the API always expects a list, whether the conversation has one turn or twenty. Your code does not need to handle single-question and multi-turn cases differently.

#### What goes inside each turn?

Every item in the `messages` list must be a dictionary with these two keys:

**`role`** — who is speaking on this turn. There are two valid values:

- `"user"` — a message sent by the human (or your program, acting as the human side of the conversation).
- `"assistant"` — a message generated by Claude.

**`content`** — the actual text of that turn. This is a string: the words the speaker is saying.

#### The simplest case: a single user turn

Here is the simplest possible `messages` array — a single user turn:

```python
messages = [
    {"role": "user", "content": "What is the capital of France?"}
]
```

This is a Python list containing one dictionary. The dictionary has two keys: `"role"` set to `"user"` and `"content"` set to the question text. Nothing more is needed for a basic single-question call.

#### Two-turn conversation with history

Here is an example with a two-turn conversation history — one user message and one prior assistant reply:

```python
messages = [
    {"role": "user",      "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user",      "content": "What is its population?"}
]
```

In this three-item list, the third message is the new question. The first two provide context — the conversation so far. Claude reads the whole list and responds to the most recent user message, taking the history into account.

This is how chatbots maintain a sense of "memory" across turns. Because the API is stateless (it does not remember anything between calls), you send the entire history every time. Claude can refer back to earlier turns because you explicitly included them in the list [3].

#### Rules for the messages array [1] [3]

Understanding the rules prevents the most common beginner errors:

- **The list must not be empty.** You must have at least one message. An empty `messages` list causes an `invalid_request_error`.
- **The first item must have `role: "user"`.** You cannot start a conversation with an assistant turn. The API will reject it with an error. This rule mirrors natural conversation: the human speaks first.
- **Turns must alternate.** The pattern must be `user`, `assistant`, `user`, `assistant`, and so on. You cannot have two `user` turns in a row without an `assistant` turn in between. Breaking the alternation is one of the most common formatting mistakes beginners make.
- **Each item must have both `role` and `content`.** Missing either field causes an error. A dictionary with only `"role"` and no `"content"` is malformed. A dictionary with only `"content"` and no `"role"` is also malformed.
- **`role` must be exactly `"user"` or `"assistant"` — nothing else.** Passing `"system"` as a role inside the messages array is an error; system instructions use a separate parameter described in section 5.4.

#### What happens when the rules are broken?

If you violate any of the rules above, the API does not try to guess what you meant. It returns an HTTP `400` status code with an error body explaining what was wrong — for example: `"messages: first message must use the 'user' role"`. Your Python program will not receive a Claude answer; it will receive an error response instead. You will need to fix the messages array and try again.

#### The simplest case you will use most often

In most beginner projects, you will send a single user message. The conversation history is just one item. You are not having a multi-turn conversation — you are asking one question and getting one answer.

```python
messages = [
    {"role": "user", "content": "Summarise this paragraph for me: ..."}
]
```

This pattern appears in nearly every beginner API call. Master this shape first, then extend it to multi-turn when you need it.

---

### 5.4 The System Prompt

**System prompt** — a special set of instructions you give Claude that shapes how it behaves for the entire conversation [2].

The system prompt is separate from the messages array. It is not a `user` turn or an `assistant` turn. It is a higher-level set of instructions that Claude reads before it reads the messages. Think of it as the rulebook for this particular conversation.

#### System prompt vs user prompt — what is the difference?

| | System prompt | User prompt |
|---|---|---|
| **What it is** | Instructions for Claude | The actual question or task |
| **Who writes it** | You, the developer | The user of your application (or your program) |
| **When Claude reads it** | Before the conversation starts | As part of the conversation |
| **Typical use** | Set role, tone, topic limits, output format | Ask a specific question or give a specific task |
| **Where it lives** | Separate `system` parameter | Inside the `messages` array as a `"user"` turn |

The **user prompt** is simply the `content` field in a `"user"` turn inside the `messages` array. It is what the human side of the conversation actually says.

The **system prompt** sits outside the messages array entirely. It is passed as a separate parameter called `system` [1] [2].

#### What do you put in a system prompt?

The system prompt is where you tell Claude what kind of assistant it is for this application. Common uses:

- **Set a role.** "You are a helpful tutor who only explains topics using simple analogies."
- **Set topic limits.** "Only answer questions about cooking. If the user asks about anything else, politely say you can only help with cooking."
- **Set output format.** "Always respond in JSON with the keys 'answer' and 'confidence'."
- **Set tone.** "Use encouraging language. Keep your answers short — no more than two sentences."
- **Combine several rules.** You can include multiple instructions in a single system prompt, each on a new line.

#### Why separate system and user prompts?

In a real application, the system prompt is written by you — the developer — and it never changes between requests. The user prompt changes with every request because it is what the user typed. Keeping them separate lets you:

1. Apply consistent rules to all conversations without repeating them in every user message.
2. Prevent users from overriding your instructions by putting them in the privileged `system` field rather than the `user` field [2].
3. Make your code easier to maintain: when you want to change how the assistant behaves, you change one place — the system prompt string — not every message in your history.

#### What happens without a system prompt?

The `system` parameter is optional. If you omit it, Claude will respond as a general-purpose assistant with no special instructions. For simple experiments this is fine. For real applications, you almost always want a system prompt to make the assistant's behavior predictable and appropriate for your use case.

#### A concrete example — bookshop bot

Imagine you are building a customer-support bot for a bookshop.

**System prompt:**
```
You are a friendly assistant for Pagebinders Bookshop.
Only answer questions about books, orders, and the shop.
If someone asks about something unrelated, say: 'I can only help with bookshop questions.'
Keep answers under three sentences.
```

**User prompt (inside messages array):**
```
I ordered a book last Tuesday. Where is it?
```

Claude reads the system prompt first, understands the rules, then reads the user's question and responds within those rules.

Without the system prompt, Claude would answer as a general assistant and might discuss topics unrelated to the bookshop. With the system prompt, it behaves exactly like the bookshop bot you designed.

#### A second example — structured output bot

Imagine you need Claude to always return data in a specific format so your program can parse it:

**System prompt:**
```
You are a data extraction assistant.
Always respond with a JSON object containing two keys: "answer" and "confidence".
"answer" is a string with your response.
"confidence" is one of: "high", "medium", or "low".
Never include any text outside the JSON object.
```

**User prompt:**
```
What is the boiling point of water?
```

With this system prompt, Claude will return something like:
```json
{"answer": "100 degrees Celsius at sea level", "confidence": "high"}
```

Your Python code can then parse this JSON reliably rather than trying to extract information from free-form text.

---

### 5.5 Authentication and the API Key

**Authentication** — the process of proving to the API that you are who you say you are, and that you have permission to use it.

The Anthropic API uses an **API key** (defined in topic 12.9) for authentication. An API key is a long, randomly generated string — something like `sk-ant-api03-...`. It is unique to your account. Every time you send a request to the API, you include your key in the request headers [1].

Why is this necessary? Because Anthropic needs to know:

1. **Who is making the request** — so it can log usage and attribute costs to your account.
2. **Whether you are allowed to make the request** — so it can reject calls from people who do not have an account or who have exceeded their usage limits.
3. **How much to charge** — API calls cost money; the key ties the bill to the right account.

#### How the API key is sent

The API key is sent as part of the request **headers** (the metadata of the request, also defined in topic 12.9). The specific header name is `x-api-key`. When you use Anthropic's official Python library (topic 12.11), the library handles this header automatically — you just pass your key to the client object once [1].

This is what that looks like conceptually (you will write the actual code in 12.11):

```python
# Conceptual — the library takes your key and attaches it to every request header
client = AnthropicClient(api_key="sk-ant-api03-...")
```

You do not manually construct the header. The library does it for you. But understanding that the key goes in the header explains why the API can reject a request before it even reads the messages — it checks the header first.

#### Why you must keep the API key secret

Your API key is like a password. If someone else gets hold of it, they can make API calls that are billed to your account. They could run up large costs before you notice.

Rules for handling an API key:

- **Never put it directly in your code.** A file with a hardcoded key can accidentally be shared or committed to version control (a system like GitHub that tracks every change to your code). Once a key is in version control history, it is effectively public — even if you delete it from the latest version, it is still visible in the history.
- **Never share it in a screenshot, chat message, or email.**
- **Store it in an environment variable** — a named value stored by the operating system, not in your script. Your Python code reads the variable at runtime [1].
- **If it is ever exposed, regenerate it immediately** — Anthropic lets you create new keys and delete old ones in your account settings.

In Google Colab (your lab environment), you will store the key using Colab's built-in Secrets feature. You will see exactly how to do this in topic 12.11.

#### What happens without a valid key?

If you send a request with no API key, or with an invalid key, the API returns an authentication error — a response with HTTP status code `401` (Unauthorized). Your program will not get a Claude response; it will get an error message instead. Topic 12.13 covers how to handle such errors gracefully.

If you send a request with a valid key that belongs to an account with no remaining credits, you will get a `429` (rate limit or billing limit) error. This is different from an authentication error — your identity is confirmed, but you have exceeded your allowance.

---

### 5.6 Putting the Four Parts Together — The Request Shape

Every Anthropic API request is, at its core, a Python function call that passes a set of parameters. The four parts you have learned map to these parameters [1]:

| Parameter | Type | Required? | What it holds |
|---|---|---|---|
| `model` | string | Yes | Which Claude version to use |
| `messages` | list of dicts | Yes | The conversation (each dict has `role` + `content`) |
| `system` | string | No (but common) | Instructions that shape Claude's behavior |
| API key | string (header) | Yes | Your identity / authentication credential |

Topic 12.11 introduces additional required parameters needed to actually send the request.

The skeleton of a request, written as a Python dictionary to show the shape, looks like this:

```python
# This is the SHAPE of a request — not runnable code yet (see topic 12.11)
request_shape = {
    "model":   "claude-haiku-3-5",
    "system":  "You are a helpful assistant. Keep answers brief.",
    "messages": [
        {"role": "user", "content": "What does RAM stand for?"}
    ]
}
```

Every field you see there was defined in this topic. Nothing in that dictionary should surprise you now.

## 6. Implementation

The purpose of this section is to make the structure fully concrete before you write the actual API call in 12.11. You will practice reading and labeling request structures, and you will build progressively more complete examples.

### 6.1 Reading a minimal request structure

Start with the absolute minimum: just `model` and `messages`. This does not include a system prompt — it is the simplest skeleton you can construct [1].

```python
# MINIMAL request — model + messages only
minimal_request = {
    "model": "claude-haiku-3-5",
    "messages": [
        {"role": "user", "content": "What is 2 + 2?"}
    ]
}
```

**Field-by-field breakdown:**

| Field | Value in this example | What it means |
|---|---|---|
| `"model"` | `"claude-haiku-3-5"` | Use the Haiku 3.5 model |
| `"messages"` | a list with one dict | The conversation has one turn |
| `messages[0]["role"]` | `"user"` | The human is speaking on this turn |
| `messages[0]["content"]` | `"What is 2 + 2?"` | This is what the human is asking |

This is valid in structure. It has a model and a messages array. In practice you would also pass a system prompt and additional parameters (introduced in 12.11), but structurally this is already a well-formed request shape.

### 6.2 Adding a system prompt

Now add the `system` parameter. Nothing else changes [1] [2]:

```python
# Request WITH system prompt
request_with_system = {
    "model":  "claude-haiku-3-5",
    "system": "You are a maths tutor for primary school students. Use simple language.",
    "messages": [
        {"role": "user", "content": "What is 2 + 2?"}
    ]
}
```

**What changed:** one new key — `"system"` — was added at the top level of the dictionary. The `messages` array is identical to the minimal example. The `system` prompt does not appear inside `messages`; it lives at the same level as `model` and `messages`.

**Consequence of adding the system prompt:** Claude will now respond as a maths tutor for primary-school students. Without it, Claude would respond as a general assistant and might use vocabulary too advanced for the intended audience.

### 6.3 Full annotated example — study assistant

Here is a more realistic example. Read through it carefully and try to label each field before reading the breakdown below [1] [2]:

```python
# Full example — annotate each field
study_assistant_request = {
    "model":  "claude-sonnet-4-5",
    "system": "You are a study assistant for CIT students. Only answer questions about the CIT curriculum. Keep answers under four sentences.",
    "messages": [
        {"role": "user", "content": "Explain what a for loop does."}
    ]
}
```

**Annotated breakdown:**

1. **`"model": "claude-sonnet-4-5"`** — Use Sonnet 4.5. This is a mid-tier model: more capable than Haiku, cheaper than Opus. A good choice for a study assistant that needs to explain things clearly.

2. **`"system": "You are a study assistant..."`** — This is the system prompt. It does three things: sets a role ("study assistant"), sets a scope limit ("only CIT curriculum"), and sets an output constraint ("under four sentences"). All three are behavioral rules that apply to the whole conversation.

3. **`"messages": [...]`** — The conversation. It is a list.

4. **`messages[0]`** — The first (and only) turn in the conversation. It is a dictionary.

5. **`messages[0]["role"]: "user"`** — The human side is speaking.

6. **`messages[0]["content"]: "Explain what a for loop does."`** — This is the user prompt — the actual question being asked.

If you can walk through a skeleton like this and describe every field without hesitation, you are ready for topic 12.11.

### 6.4 Multi-turn conversation history

If you want to provide context (previous turns) before the new question, you extend the `messages` list [1] [3]:

```python
# Multi-turn conversation — three turns
multi_turn_request = {
    "model":  "claude-sonnet-4-5",
    "system": "You are a Python tutor. Keep answers concise.",
    "messages": [
        {"role": "user",      "content": "I am studying Python. What is a function?"},
        {"role": "assistant", "content": "A function is a named block of code you can call by name. You define it with 'def'."},
        {"role": "user",      "content": "Can a function call another function?"}
    ]
}
```

**What to notice:**

- The `messages` list now has three items.
- The items alternate: `user` → `assistant` → `user`. This is the required alternating pattern.
- The last item is the new question. Items before it are the history Claude can refer to.
- The `system` prompt is still at the top level, outside `messages`. It applies to the whole conversation including all three turns.

**What Claude "sees":** Claude reads the system prompt first ("you are a Python tutor"), then reads the entire messages list from top to bottom, then generates a reply to the last user turn. The previous `user`/`assistant` turns give it context.

### 6.5 Practice labeling exercise

Read the following request structure. Before looking at the answers below, try to answer: (a) which model is being used, (b) what role Claude is playing, (c) how many turns are in the conversation, (d) what the user is asking:

```python
mystery_request = {
    "model":  "claude-opus-4-5",
    "system": "You are a travel guide specialising in Japan. Only answer questions about Japan.",
    "messages": [
        {"role": "user",      "content": "What is the best time of year to visit Kyoto?"},
        {"role": "assistant", "content": "Spring (March–May) for cherry blossoms, or autumn (October–November) for coloured leaves. Both seasons are popular and can be crowded."},
        {"role": "user",      "content": "Which is less crowded?"}
    ]
}
```

**Answers:**

(a) `"claude-opus-4-5"` — the highest-capability Opus model.
(b) A travel guide specialising in Japan, restricted to Japan-only questions.
(c) Three turns: two user turns and one assistant turn (conversation history of two turns, new question as the third).
(d) "Which is less crowded?" — asking to compare the two seasons from the previous answer.

### 6.6 Spotting a malformed structure

Here is a request with two errors. Can you spot them?

```python
# Broken — two errors
broken_request = {
    "model": "claude-haiku-3-5",
    "messages": [
        {"role": "assistant", "content": "Hello! How can I help you?"},
        {"role": "user",      "content": "Tell me about Python."}
    ]
}
```

**Errors:**

1. The first turn has `"role": "assistant"`. The messages array must start with a `"user"` turn. This will cause an `invalid_request_error`.
2. The `assistant` turn at position 0 implies Claude spoke first, which is not a valid starting state for the Messages API.

**Fixed version:**

```python
fixed_request = {
    "model": "claude-haiku-3-5",
    "messages": [
        {"role": "user", "content": "Tell me about Python."}
    ]
}
```

The assistant greeting was removed. Now the list starts with a user turn.

## 7. Real-World Patterns

### System prompts as product features

In real AI-powered products, the system prompt is often the core intellectual property of the product. Companies write carefully tuned system prompts that define their product's personality, capabilities, and limits. The user never sees the system prompt — they only see the results of it [2].

Consider a legal document summariser: the system prompt might instruct Claude to always identify the parties involved, always flag any dates and deadlines, and never provide legal advice. A generic Claude call would not do any of that automatically. The system prompt is what turns a general-purpose model into a specific, reliable tool. Well-crafted system prompts separate a generic Claude response from a response that feels tailored to a specific application.

### Model selection as a cost decision

Production applications often choose different models for different tasks within the same product. A quick text-classification task might use a fast, cheap model. A long, nuanced document analysis might use a more capable model. The `model` parameter lets you make this choice per-request — you are not locked into one model for all calls [1].

A realistic example: an e-commerce chatbot might use Haiku to classify the intent of a user's message ("is this a refund request or a product question?") and then only call Sonnet or Opus for the messages that require a detailed, high-quality answer. This keeps costs low for the high-volume simple tasks while reserving quality for the complex ones.

### Storing conversation history in the messages array

Chatbots and assistants that need to remember earlier parts of the conversation do so by appending turns to the `messages` list and sending the updated list with each new request. The API itself is stateless — it does not remember previous calls. All context must be explicitly included in the `messages` array every time [3].

This design is intentional: because the API is stateless, every request is independent. This makes it easy to build distributed systems where different servers can handle different requests. The trade-off is that you are responsible for maintaining the conversation history in your own code and passing it each time.

### Authentication as access control

Companies that build products on top of the Anthropic API do not give users direct access to the API key. Instead, the company's own server holds the API key securely, and users of the product authenticate with the company's server. The server then makes API calls on the user's behalf. This way the API key is never exposed to end users [1].

This layered approach — your app authenticates users, your server authenticates to Anthropic — is the standard pattern for production applications.

## 8. Best Practices

**API key hygiene — always:**

- Store your API key in an environment variable or a secrets manager (a secure store for credentials, separate from your code) — never hardcode it in your script. A hardcoded key in a shared notebook or a repository is a credential leak waiting to happen.
- Treat a leaked key exactly like a leaked password: revoke it and create a new one immediately. Every minute a leaked key remains active is a minute someone else can make calls at your expense.
- Never commit code that contains an API key to version control (a system like GitHub that tracks every change to your code). Even a key that has been "deleted" from the current version of the file is still visible in the repository's commit history.

**System prompt discipline:**

- Write the system prompt as clear, direct instructions. Avoid vague phrasing like "be nice" — instead write "respond in an encouraging tone and avoid negative language." The more specific your instruction, the more reliably Claude will follow it [2].
- Keep the system prompt focused on behavior and constraints, not on the specific task — the task goes in the user message. Mixing them makes it hard to reuse the system prompt across different user queries.
- Test your system prompt with edge-case user messages to make sure Claude respects your constraints. Common edge cases: the user asks about a topic outside your intended scope; the user asks Claude to ignore its instructions; the user sends an empty message.

**Messages array correctness:**

- Always start with a `user` turn — the API will reject a messages array that starts with an `assistant` turn.
- Do not leave `role` or `content` blank. Both fields are required for every item. An empty string for `content` is technically valid, but almost always a sign of a bug.
- Keep the conversation history as short as needed — very long histories increase both the response time and the cost. If the conversation has grown to dozens of turns, consider summarising older turns into a single message rather than sending them all.

**Model selection:**

- For learning and experimentation, start with a smaller, cheaper model (e.g., Haiku) — you will iterate many times, and iteration cost adds up quickly.
- Switch to a larger model only when you need the additional quality and have confirmed the smaller model is insufficient for your use case. The right question is not "which model is best?" but "which model is good enough for this task at the lowest cost?"

## 9. Hands-On Exercise

Open a Python notebook (Google Colab works fine) and practice building the request structure without actually sending it to the API.

**Exercise A — Minimal structure:**

1. Create a Python dictionary called `my_request` with the keys `model`, `system`, and `messages`.
2. Set `model` to any valid Claude model name string from the table in section 5.2.
3. Set `system` to a one-sentence instruction that defines a role (for example: "You are a friendly tutor who only uses analogies.").
4. Set `messages` to a list containing one dictionary with `role: "user"` and `content` set to any question you would ask Claude.
5. Print `my_request` and verify every field is present and correctly typed.

You are not calling the API yet — just practising the shape.

**Exercise B — Add conversation history:**

1. Copy `my_request` into a new variable `my_multi_request`.
2. Extend the `messages` list with a second turn: `{"role": "assistant", "content": "Here is a sample answer."}`.
3. Add a third turn: `{"role": "user", "content": "Can you say more?"}`.
4. Verify the roles alternate correctly: user, assistant, user.
5. Print the full structure and count the number of turns.

**Exercise C — Spot the bug:**

Look at this structure and identify the problem before running it:

```python
buggy = {
    "model": "claude-haiku-3-5",
    "messages": [
        {"role": "user", "content": "Hello"},
        {"role": "user", "content": "What is Python?"}
    ]
}
```

*Hint: check the alternation rule from section 5.3.*

**Answer:** Two consecutive `"user"` turns without an `"assistant"` turn in between violates the alternation rule. The API will reject this with an `invalid_request_error`. Fix: either remove the first `"user"` turn or insert an `"assistant"` turn between them.

**Verification:** After completing all three exercises, you should be able to describe every field in a request shape without looking at notes. If you can do that, you are ready for topic 12.11.

## 10. Key Takeaways

- The Anthropic Messages API expects every request to include at minimum: a `model` string, a `messages` array, and your API key in the request headers for authentication. Additional required parameters are introduced in topic 12.11.
- The `messages` array is a Python list of dictionaries. Each dictionary must have exactly two keys: `role` (either `"user"` or `"assistant"`) and `content` (the text of that turn). Turns must alternate and the first turn must be a `"user"` turn.
- The `system` prompt sits outside the `messages` array and is used to give Claude persistent instructions — its role, tone, output format, and topic limits — for the whole conversation.
- A user prompt is the `content` of a `"user"` turn inside `messages`; a system prompt is the separate `system` parameter. They are different fields with different purposes.
- Your API key authenticates every request. It must be kept secret, never hardcoded in source files, and stored in an environment variable or secrets manager (a secure store for credentials, separate from your code).

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
