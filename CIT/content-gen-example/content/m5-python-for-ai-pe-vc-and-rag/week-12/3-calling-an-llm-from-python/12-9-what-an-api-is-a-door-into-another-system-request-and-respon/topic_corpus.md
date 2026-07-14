---
topic_id: "12.9"
title: "What an API is — a door into another system; request and response"
position_in_module: 1
generated_at: "2026-06-15T00:00:00Z"
resource_count: 3
---

# 1. What an API is — a door into another system; request and response — Topic Corpus

## 2. Prerequisites

This topic builds on the following concepts introduced earlier in week 12:

- **12.1–12.3** — Functions, parameters, return values, and the single-responsibility principle. You know how to define and call a reusable block of logic.
- **12.4** — Lists and for-loops. You know how to store multiple values and iterate over them.
- **12.5** — Dictionaries and key-value pairs. You know how to represent structured data as `{"key": "value"}`.
- **12.6–12.7** — Reading and writing files with `open()`.
- **12.8** — Exception handling with `try` / `except`. You know how to handle errors gracefully.

JSON (JavaScript Object Notation) is used as an example format in this topic. It looks exactly like a Python dictionary — you already know dictionaries from 12.5, so you will recognise the structure immediately. Full JSON parsing is covered later in 12.12.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. **Define** what an API (Application Programming Interface) is, using the "interface" idea to explain what the word means.
2. **Explain** the request-response cycle: a client sends a request, a server processes it, and the server sends back a response.
3. **Identify** the four components of an API request: endpoint (URL), HTTP method, headers, and body.
4. **Identify** the three components of an API response: status code, headers, and body.
5. **Explain** why LLM (Large Language Model) models like Claude are accessed through an API and how your Python code fits into that picture as the client.
6. **Explain** using the waiter analogy why an API exists as an abstraction layer between your code and the server.

## 4. Introduction

Imagine you are at a restaurant. You do not walk into the kitchen, grab ingredients, and cook your own meal. Instead, you tell the waiter what you want, the waiter carries your order to the kitchen, the kitchen prepares the food, and the waiter brings it back to you.

Your code works the same way when it needs to talk to an external system — a weather service, a payment processor, or an AI model. You cannot log into the company's internal servers. You cannot read their database. But you can send a message through a defined doorway that they have set up for exactly this purpose. That doorway is called an **API**.

In this module, you are going to call an LLM (Large Language Model) — specifically the Anthropic Claude model — from your Python code. To do that, your code will send a request to the Anthropic API and receive the model's response. Before you write a single line of that code, you need to understand what an API is, what a request and a response look like, and why this structure exists. That is what this topic is about. [1]

## 5. Core Concepts

### 5.1 What "API" means

**API** stands for **Application Programming Interface**. Each word carries meaning:

- **Application** — a piece of software, a service, or a system running somewhere.
- **Programming** — it is designed to be used by code, not by humans clicking buttons.
- **Interface** — a defined contract. Both sides agree on the rules: what you can ask for, how you ask for it, and what you will get back.

Think of the word "interface" the way you think of a plug socket. The socket in a wall has a defined shape and voltage. Any device that matches that contract — any plug that fits — can use it. The socket does not care what device is plugged in. The device does not care how electricity is generated. The interface is the agreement between them. [1]

An API works the same way. It is a published set of rules that says: "If you send me a message in this format, I will send you a response in this format." Anyone who follows the rules can use the API.

### 5.2 The client-server model

Every API interaction involves two roles:

| Role | Who it is | What it does |
|---|---|---|
| **Client** | Your Python code | Sends the request — asks for something |
| **Server** | The external system | Receives the request, processes it, sends the response |

Your code is always the client. The external system — a weather service, a database, an LLM — is the server.

The client and server can be running on completely different machines in different countries. They communicate over the internet using a set of rules called **HTTP** (HyperText Transfer Protocol). HTTP is the standard language that web browsers and servers use to talk — and it is the same language most APIs use too. [2]

You do not need to know how HTTP works at a low level. What you need to know is:
1. Your code sends an HTTP request to a URL.
2. The server at that URL processes the request.
3. The server sends an HTTP response back to your code.

### 5.3 The waiter analogy in full

The restaurant analogy maps precisely onto the API pattern:

| Restaurant | API |
|---|---|
| You (the customer) | Your Python code (the client) |
| The waiter | The API |
| The kitchen | The server / the service |
| The menu | The API documentation |
| Your order | The request |
| Your meal | The response |

Why is the waiter (the API) necessary? Because you do not need to know how the kitchen works. The kitchen can change its equipment, hire new chefs, or change recipes. As long as the waiter still takes the same kind of order and brings back the right meal, you are unaffected. This is exactly why APIs exist: they **hide the implementation** behind a stable interface. [1]

If Anthropic rewrites the internal code that runs Claude, your Python code does not break — because you are talking to the API, not to the internals. The interface stays the same even when the kitchen changes.

### 5.4 What a request looks like

An API request is your code's way of saying "I want something." Every request has four parts: [2]

**1. Endpoint (URL)**

The **endpoint** is the address of the specific capability you are calling. It is a URL (Uniform Resource Locator — the same kind of address you type into a browser). Different endpoints on the same server do different things.

Example:
```
https://api.anthropic.com/v1/messages
```

The part before `/v1/messages` is the server. The path `/v1/messages` says which specific operation you want.

**2. HTTP Method**

The **HTTP method** (sometimes called "verb") tells the server what kind of action you are taking. The two you will use most are:

| Method | Meaning | Typical use |
|---|---|---|
| **GET** | "Give me some information" | Fetching data — no data sent in body |
| **POST** | "Here is some data — process it" | Sending data to be processed or created |

When you call an LLM, you use **POST** — you are sending your prompt to the server and asking it to process it. [3]

**3. Headers**

**Headers** are metadata — extra information that travels alongside your request but is not the main content. They tell the server things like:

- What format the body is in (`Content-Type: application/json`)
- Who is making the request (your API key, used for authentication)
- What format you want back (`Accept: application/json`)

Think of headers as the envelope and labels around a letter. The letter's contents are the body; the headers are what is written on the outside. [2]

**4. Body**

The **body** (also called the **payload**) is the actual data you are sending. Not all requests have a body — a GET request typically has none. A POST request almost always does.

The body is usually formatted as **JSON** (JavaScript Object Notation — a format that looks like a Python dictionary). For example, a simplified Anthropic API request body looks like this:

```
{
  "model": "claude-3-5-sonnet-20241022",
  "messages": [
    {"role": "user", "content": "What is machine learning?"}
  ],
  "max_tokens": 256
}
```

You already know from topic 12.5 how to read key-value pairs. The body is just a dictionary sent over the internet. The exact format of the Anthropic API body — including the `messages` array and `system` prompt — is covered in topic 12.10.

**Putting the four parts together.** When you look at an API request as a whole, each part plays a distinct role. The endpoint says *where* to send the request. The method says *what kind of action* you are taking. The headers say *who you are* and *what format you are using*. The body says *what you actually want the server to do with your data*. Remove any one part and the request either fails or does the wrong thing.

Here is a side-by-side comparison of a GET request (which fetches data) and a POST request (which sends data to be processed):

| Part | GET request | POST request |
|---|---|---|
| Endpoint | `https://api.example.com/weather?city=London` | `https://api.anthropic.com/v1/messages` |
| Method | `GET` | `POST` |
| Headers | `Accept: application/json` | `Content-Type: application/json`, `x-api-key: your-key` |
| Body | (none) | JSON with your prompt and model settings |

Notice that the GET request puts its parameters in the URL itself (`?city=London`). The POST request keeps its data in the body. This separation is a convention that all modern APIs follow — and it is why you will see these two patterns repeatedly throughout the rest of this module and beyond. [1][2]

### 5.5 What a response looks like

After your request arrives, the server processes it and sends back a **response**. A response has three parts: [3]

**1. Status code**

The **status code** is a three-digit number that tells you immediately whether the request succeeded or failed. You do not have to read the whole response body to know if something went wrong.

| Code | Meaning | Example situation |
|---|---|---|
| **200** | OK — success | Your request worked; data is in the body |
| **400** | Bad Request — your fault | You sent something the server could not understand |
| **401** | Unauthorized | Your API key is missing or wrong |
| **404** | Not Found | The endpoint URL does not exist |
| **429** | Too Many Requests | You sent requests too fast (rate limit) |
| **500** | Internal Server Error | The server crashed — not your fault |

The pattern is simple: **2xx = success, 4xx = problem on your side, 5xx = problem on the server's side**. [1]

**2. Response headers**

Just like the request, the response has headers — metadata about the response. They tell you things like what format the body is in and how many API credits you used. You rarely need to inspect these as a beginner.

**3. Response body**

The **response body** is the actual answer from the server. Like the request body, it is usually JSON. A simplified Anthropic API response body looks like this:

```
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Machine learning is a branch of AI where..."
    }
  ],
  "model": "claude-3-5-sonnet-20241022",
  "usage": {
    "input_tokens": 14,
    "output_tokens": 58
  }
}
```

The model's generated text is nested inside the response body — how to extract it from the JSON structure is covered in topic 12.12.

### 5.6 JSON as the common language

Almost every modern API sends and receives data in **JSON** (JavaScript Object Notation). JSON uses the same key-value structure you learned in topic 12.5 with Python dictionaries:

```
{"key": "value", "another_key": 42}
```

The main differences from a Python dict are cosmetic:
- JSON uses double quotes for strings (Python allows single or double).
- JSON uses `true` / `false` (lowercase) where Python uses `True` / `False`.

Full JSON handling — converting the response text into data your Python code can work with — is covered in topic 12.12.

The important point for now: JSON is the universal envelope that lets your Python code understand what the server sent back, and lets the server understand what you sent. [1][3]

### 5.7 Why not access the server directly?

A beginner might ask: "Why do I need an API? Why can't I just connect to the server and read the data?"

Here are the three reasons: [1]

1. **Hidden implementation.** The server's internal code, database structure, and models are private. The API exposes only what the provider chooses to share. You see the door, not the building.

2. **Stability.** A company's internal code changes constantly. If your code depended on internal details, every internal change would break you. The API is a stable promise: "We will not change how this endpoint works without telling you."

3. **Authentication and access control.** The API checks your credentials (your API key) before letting you in. This means the provider can track usage, enforce limits, and charge for access — and unauthorized code cannot simply grab data.

This is why every major AI provider — Anthropic, OpenAI, Google — exposes their models through an API rather than letting you run the model directly. You send a request; the model runs on their servers; you receive the response. Your code never touches the model itself.

## 6. Implementation

There is no code to run in this topic — this is a conceptual introduction. The next topics in this module build on these ideas:

1. **Topic 12.10** — The Anthropic API specifically: the `model`, `messages` array, `system` prompt, and authentication.
2. **Topic 12.11** — Installing the Anthropic Python library and making your first real API call.
3. **Topic 12.12** — Parsing the JSON response to extract the text.
4. **Topic 12.13** — Handling API errors (status codes 4xx and 5xx) using the `try` / `except` pattern from topic 12.8.

For now, hold this mental model: your Python code (client) → sends a POST request with a JSON body → to an endpoint URL → server processes it → server sends back a JSON response with a status code.

## 7. Real-World Patterns

APIs are everywhere in modern software. Here are four patterns you will recognise once you start looking: [1][3]

**Pattern 1 — Chained API calls (pipeline)**
A single user action can trigger multiple API calls. A travel booking app might call a flights API, then a hotels API, then a payments API — each one reading the response from the previous call and using it in the next request. In your lab, your Python code will call the Anthropic API and use the response to produce structured output.

This chaining pattern is what makes AI pipelines possible. You might first call a database API to fetch student data, then call the Anthropic API to generate a personalised summary, then write the result to a file using the file-writing skills from topics 12.6 and 12.7. Each step in the pipeline is one API call; together they form a complete workflow [1].

**Pattern 2 — Authentication via API key**
Most APIs require an **API key** — a secret string that identifies who is making the request. You send the key in a header. If the key is wrong or missing, the server returns a 401 status code. Never share your API key or put it in public code. Topic 12.10 covers how Anthropic authentication works.

An API key functions like a hotel key card. The card does not tell the hotel who you are by name, but it proves you are authorised to open a specific door. The hotel tracks which cards are used and can revoke access at any time. API providers can similarly revoke a key if it is misused or shared publicly — which is why you never embed an API key directly in code you share [2].

**Pattern 3 — Rate limits**
Servers protect themselves by limiting how many requests a single client can send per minute or per day. If you exceed the limit, you receive a 429 response ("Too Many Requests"). Well-written code detects this and waits before retrying. Topic 12.13 covers error handling strategies including 429 responses.

Rate limits are not a punishment — they are a safety mechanism. They prevent one busy or buggy client from overwhelming the server and degrading service for everyone else. As a beginner, you are unlikely to hit rate limits during development. But understanding that they exist is important: if you see a 429 in your response, the fix is to slow down your requests, not to re-send the same request immediately [3].

**Pattern 4 — Versioned endpoints**
Notice that the Anthropic API endpoint includes `/v1/messages`. The `v1` is a version number. When an API provider makes breaking changes to how the request or response is structured, they release a new version (`v2`, `v3`) rather than changing the existing one. This means code written against `v1` keeps working even after `v2` is released. You do not need to immediately update your code every time the API evolves. As a beginner, always use the version shown in the documentation — do not guess at version numbers [1].

## 8. Best Practices

**Always check the status code first.**
Before you try to read the response body, check whether the status code is 200. If it is 4xx or 5xx, something went wrong. Trying to parse a body from a failed request often causes confusing errors. Think of the status code as the subject line of an email — it gives you the verdict before you read the detail. You learned to handle errors gracefully in topic 12.8; that same `try / except` pattern applies directly to API calls when the status code indicates a failure.

**Keep your API key out of your code.**
An API key is like a password. Do not paste it directly into your script. Store it as an environment variable or in a configuration file that is not shared. This is covered in topic 12.10. As a practical rule: if you can see your API key in the same file as your Python code, it is in the wrong place.

**Read the error message in the response body.**
When a request fails (4xx), the server almost always includes a human-readable explanation in the response body. Read it — it usually tells you exactly what was wrong (missing field, wrong format, exceeded limit). A 400 Bad Request, for example, often includes text like `"missing required field: model"` which immediately tells you what to fix. Do not just retry a failed request without reading why it failed. [2]

**Do not guess at the request format — read the documentation.**
The API documentation (the "menu") tells you exactly what fields the body must contain, which method to use, and what the response will look like. Guessing wastes time. For the Anthropic API, the documentation is at `docs.anthropic.com`. Good documentation also lists every possible error code and what causes each one — reading it once saves hours of debugging later.

**One request, one responsibility.**
A good API call does one thing: it asks for one piece of information or sends one unit of work. Keep your request bodies focused. This aligns with the single-responsibility principle you learned in topic 12.3. If you find yourself trying to pack multiple unrelated questions into one API call, split them into separate calls — the responses will be cleaner and easier to handle.

**Treat the API as a black box.**
You cannot inspect the server's internal code, and you should not need to. The API contract — the documentation — is the complete specification of what you can ask for and what you will receive. If the documentation says a certain field will always be present in a 200 response, trust that. If it says a field is optional, defend against its absence with the dictionary `.get()` method you learned in topic 12.5. [1][3]

## 9. Hands-On Exercise

You do not need to write code for this exercise. Use it to build your mental model.

1. Think of one real-world app you use (a weather app, a banking app, a social feed). Write down in plain English what request you imagine your phone sends and what response the server likely sends back. What is the endpoint doing? Is it probably a GET or a POST?
2. Draw the request-response cycle from memory: client → request (with its four parts) → server → response (with its three parts) → client. Label every box and arrow.
3. Look at the JSON example in section 5.4. Map each key to the Python dictionary syntax you know from topic 12.5. They should feel identical.

This mental model is what you will use every time you write an API call for the rest of the module and for lab Part 2.

## 10. Key Takeaways

- An **API** (Application Programming Interface) is a defined contract that lets two programs communicate. Your code is the client; the external system is the server.
- Every API interaction follows the **request-response cycle**: client sends a request → server processes it → server sends a response.
- A request has four parts: **endpoint** (URL), **HTTP method** (GET or POST), **headers** (metadata), and **body** (the actual data, usually JSON).
- A response has three parts: **status code** (200 = success, 4xx = client error, 5xx = server error), **headers**, and **body** (usually JSON).
- LLM models like Claude are accessed via API. Your Python code is the client; Anthropic's server runs the model. You send a POST request with your prompt; you receive a JSON response containing the generated text.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
