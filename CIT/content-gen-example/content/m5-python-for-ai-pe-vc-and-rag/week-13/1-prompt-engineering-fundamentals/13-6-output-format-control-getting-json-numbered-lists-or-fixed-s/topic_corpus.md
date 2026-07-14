---
topic_id: "13.6"
title: "Output format control — getting JSON, numbered lists, or fixed structure through the prompt"
position_in_module: 6
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Output Format Control — Getting JSON, Numbered Lists, or Fixed Structure Through the Prompt — Topic Corpus

## 2. Prerequisites

- **13.1 — System prompt vs user prompt**: students know the system prompt holds persistent, authoritative instructions and the user prompt carries the live request. Format instructions belong in the system prompt so every response follows the same shape.
- **13.2 — Role assignment**: students can write a role statement. The role shapes persona; format instructions shape the *shape* of the output — they work together.
- **13.5 — Constraints**: students know how to tell the model what *not* to do, including format constraints ("do not use bullet points"). This topic extends that skill into precise, structured format specifications.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** why a language model (LLM) produces inconsistently formatted output when given no format instruction, and why that inconsistency matters in a Python program.
2. **Write** a prompt instruction that requests a specific output format — JSON object, numbered list, or fixed text template — using exact, testable language.
3. **Apply** the three format-specification strategies (inline declaration, format example, and template echo) to a prompt of your own.
4. **Identify** format drift in a model response by comparing it against the declared format contract.
5. **Describe** the output validator pattern — checking format after a response and retrying once before returning a fallback — and explain why it is needed even when format instructions are present.

## 4. Introduction

Imagine you ask a model to extract the name and price of a product from a customer review and your Python program expects a JSON object like `{"name": "...", "price": "..."}`. The model answers: "The product is called SuperBlend Pro and it costs $29.99." That is helpful to a human reader. It is useless to your program.

This is the **format mismatch problem**. A language model is trained to produce fluent, helpful prose — not to guarantee a machine-readable shape. Every time you call the model, it makes a fresh decision about how to structure its answer. Without explicit format instructions, that decision is influenced by whatever the training data did most often in similar contexts. Sometimes that means a JSON block. Sometimes that means prose. Often it means something in between.

For applications — chatbots, automated pipelines, portfolio projects — format consistency is not optional. If your program expects a numbered list and the model returns bullet points, your parser breaks. If it expects a JSON key called `"name"` and the model writes `"product_name"`, your code throws a `KeyError`.

Output format control is the set of prompting techniques you use to declare the exact shape of a response and hold the model to it [1][2]. It works entirely through what you write in the prompt — no special API settings required. This topic covers three core strategies, how to spot when format has drifted, and how to build a simple validator that retries when the model goes off-spec.

## 5. Core Concepts

### 5.1 Why LLMs produce inconsistent format by default

A language model (LLM — Large Language Model) is trained on enormous amounts of text from the internet: articles, books, forum posts, code, emails, and more. That text was written by humans for humans, not by machines for machines. Human writing is stylistically varied — sometimes a list, sometimes a paragraph, sometimes a table — and the model learned all of those styles equally [1].

When you ask a question, the model predicts the most probable next tokens (small chunks of text, roughly one word each) given everything in the prompt. If the prompt does not specify a format, the model picks whatever style best matches the pattern it has seen most often for that kind of question [1].

That pattern is inconsistent across calls because:

- Small differences in phrasing change which training examples the model "resembles" most [1].
- The model samples from a probability distribution — even identical prompts can produce different styles on different runs [2].
- Different models, and different versions of the same model, have different stylistic defaults [3].

The result: two calls with the same question can produce a JSON block one time and a paragraph the next.

### 5.2 Format specification — the core technique

**Format specification** is the act of writing a clear, explicit instruction in your prompt that tells the model the exact shape its response must take [1][2]. It is a type of constraint (from topic 13.5), but targeted specifically at output structure rather than topic or tone.

A format specification answers three questions:

1. **What structure?** (JSON, numbered list, table, fixed template, plain sentence…)
2. **What fields or positions?** (exactly which keys in the JSON, exactly which step labels in the list…)
3. **Nothing else?** (should the model add commentary, a preamble, a sign-off — or just the structure?)

Leaving any of these three questions unanswered is where drift starts.

**Example — under-specified:**

```
Extract the product name and price from the review below.
```

The model has no format guidance. It may respond with a sentence, a list, a JSON block, or a combination.

**Example — fully specified:**

```
Extract the product name and price from the review below.
Respond with a JSON object in exactly this shape:
{"name": "<product name>", "price": "<price with currency symbol>"}
Output the JSON object only. Do not add any explanation before or after it.
```

The difference is the precision of the instruction. The second version answers all three format questions. [1][2]

### 5.3 Three format-specification strategies

There are three practical ways to communicate the desired format to the model. Real prompts often combine two or more.

---

**Strategy 1 — Inline declaration**

You state the format in plain language, usually one or two sentences. This is the simplest approach and works well for common formats.

Examples:

- "Respond with a numbered list. Each item is one sentence. Output the list only."
- "Return a JSON object with the keys `task`, `priority`, and `deadline`. Output JSON only, no surrounding text."
- "Write your answer as three paragraphs: (1) Problem, (2) Cause, (3) Fix. Use those exact headings."

Inline declarations are easy to write and easy to read back. They work well when the format is straightforward and when you can trust the model knows what "JSON object" or "numbered list" means [2][3].

---

**Strategy 2 — Format example**

You show the model a single concrete example of the output shape you want. This is the format-focused application of the few-shot technique from topic 13.3.

Example:

```
Classify the sentiment of each review below.
Output format (follow this exactly):
Review 1: Positive
Review 2: Negative

Now classify:
Review 1: "The packaging was great but the product broke on day one."
Review 2: "Absolutely love it — would buy again."
```

By providing one filled-in example, you show the model the exact field names, punctuation, capitalisation, and line structure you expect. This is more reliable than an inline declaration for unusual or precise formats [1][2].

---

**Strategy 3 — Template echo**

You provide the output template with placeholders and instruct the model to fill in the placeholders and return the completed template — nothing else.

Example:

```
Fill in the template below. Replace each <placeholder> with the correct value.
Do not change the template structure. Return only the filled-in template.

Template:
Customer name: <name>
Issue category: <category>
Recommended action: <action>
Priority: <High|Medium|Low>
```

Template echo is especially useful when the output must integrate with downstream text processing (such as parsing fixed-position fields) or when the format is complex enough that an inline declaration would be ambiguous [2][3].

### 5.4 Requesting JSON output

JSON (JavaScript Object Notation — a text format for structured data used widely in web and application development) is the most common machine-readable format requested from LLMs in Python applications, because Python can parse it directly with `json.loads()`.

Three things make a JSON format instruction reliable:

1. **Name the format explicitly.** Write "JSON object" or "JSON array", not just "structured data".
2. **Show the exact keys.** Either write an inline example or use the template-echo strategy.
3. **Suppress surrounding text.** Add: "Output the JSON only. Do not include any text before or after the JSON block."

Example prompt:

```
You are a data extraction assistant.
Given a product review, extract the following fields.
Return a JSON object in exactly this format:
{
  "product_name": "<string>",
  "sentiment": "positive" | "negative" | "neutral",
  "key_issues": ["<issue1>", "<issue2>"]
}
Output the JSON object only. No explanation, no preamble.
```

The suppression instruction ("Output the JSON only") is important. Without it, many models wrap the JSON in a sentence like "Here is the extracted data:" or a code fence marker (the triple backtick ` ``` ` that opens a fenced code block) like ` ```json `. Both break a straightforward `json.loads()` call [1][2].

### 5.5 Requesting numbered lists and fixed templates

The same three principles apply to list formats:

1. Name the format explicitly ("a numbered list", "a bullet list", "a three-column table").
2. Specify length or depth ("exactly five items", "one sentence per item").
3. Suppress extras ("list items only, no introduction or conclusion").

Example:

```
List the three main causes of the problem described below.
Use a numbered list. Each item is a single sentence.
Output the list only — no preamble, no follow-up commentary.
```

For fixed-template formats (forms, reports, structured emails), the template-echo strategy is most reliable. You write the template once, tell the model to fill it in, and the output is ready to store or display [3].

### 5.6 Format drift — recognising when the model goes off-spec

**Format drift** is when a model response does not match the format you declared [2]. It is the most common failure mode in format control [1][3]. Examples:

- You asked for JSON, and the model returned JSON wrapped inside a sentence ("Here is the result: {…}") [1].
- You asked for a numbered list, and the model returned bullet points or a prose paragraph [2].
- You asked for exactly three items, and the model returned four.
- A key in the JSON is spelled differently from what you specified (`"productName"` instead of `"product_name"`) [3].

Format drift happens because:

- The model treats format instructions as strong suggestions, not hard rules [1][2].
- A long prompt or a complex task can push format instructions out of the model's effective attention [2].
- Certain questions naturally pattern-match to prose in the training data, and that pull competes with your instruction [1].

You detect format drift by checking the response against your format contract before you use it. The next section shows how to do that in Python.

### 5.7 The output validator pattern

Even well-written format instructions do not eliminate drift entirely [1][2]. The professional practice is to validate the response format and retry once if it fails — rather than passing a malformed response to the rest of your program [2][3].

The **output validator pattern** works like this:

1. Call the model with your format-specified prompt [1].
2. Check the response against the expected format [2].
3. If the check passes, use the response.
4. If the check fails, retry once — with a corrective follow-up message ("Your last response was not in the required JSON format. Please return only a JSON object with the keys: …") [2][3].
5. If the retry also fails, return a safe fallback (an empty structure, a default value, or an error flag) [3].

The validator itself can be as simple as a `try/except` around `json.loads()` for JSON, or a line-count check for a numbered list. The key insight is that the validator must run *before* the rest of your program processes the response [2].

## 6. Implementation

The following steps describe how to add format control to a prompt and back it with a simple validator in Python [1][2].

**Step 1 — Choose your format.**
Decide what shape the output needs to be for downstream use [1]. If your program will parse it, use JSON. If it will display it to a user, a numbered list or fixed template may be clearer [2].

**Step 2 — Write the format instruction using one or more strategies.**
For JSON, use inline declaration and suppress surrounding text [1][2]. For a numbered list, use inline declaration and specify length [2]. For a complex template, use template echo [3].

**Step 3 — Test the format instruction.**
Call the model five to ten times with realistic inputs [1]. Check each response manually: does it match the declared format exactly? Note any drift patterns [2].

**Step 4 — Write a format validator.**
Write a short function that takes the model's response string and returns `(True, parsed_value)` if valid or `(False, None)` if not [2][3].

```python
import json

def validate_json_response(response: str, required_keys: list) -> tuple:
    """
    Returns (True, parsed_dict) if response is valid JSON with all required keys.
    Returns (False, None) otherwise.
    """
    try:
        # Strip code fence markers (the triple backtick ``` that opens a fenced code block) if present
        text = response.strip()
        if text.startswith("```"):
            lines = text.splitlines()
            text = "\n".join(lines[1:-1])  # drop first and last line
        data = json.loads(text)
        for key in required_keys:
            if key not in data:
                return False, None
        return True, data
    except json.JSONDecodeError:
        return False, None
```

**Step 5 — Add the retry loop.**

```python
def call_with_format_retry(client, system_prompt, user_message, required_keys):
    """
    Calls the model. If the response fails format validation, retries once
    with a corrective instruction. Returns the parsed dict or None.
    """
    response = client.call(system_prompt, user_message)  # your Week 12 API call here
    valid, data = validate_json_response(response, required_keys)

    if valid:
        return data

    # One retry with a corrective message
    correction = (
        "Your previous response was not in the required JSON format. "
        "Return only a JSON object with these keys: "
        + ", ".join(required_keys)
        + ". No surrounding text."
    )
    response2 = client.call(system_prompt, correction)
    valid2, data2 = validate_json_response(response2, required_keys)

    if valid2:
        return data2

    return None  # fallback: caller handles the None case
```

The `client.call` above is a placeholder for the actual LLM API call you learned in Week 12 — the pattern wraps whatever client library you are using [2][3].

**Step 6 — Document what the validator caught.**
As you test, log each validation failure: what the model returned, why it failed, and whether the retry succeeded [2]. This log is valuable evidence of your format instruction's precision and helps you iterate on the prompt wording [1][3].

## 7. Real-World Patterns

Format control through the prompt is ubiquitous in production LLM applications.

**Automated data extraction pipelines** use JSON format instructions to pull structured fields (names, dates, prices, classifications) from unstructured text. The extracted JSON is then inserted directly into a database or passed to another function. Without format control, every extraction result would require custom parsing [1][2].

**Customer-service routing systems** use fixed-template prompts to classify incoming messages — returning a structured result like `{"category": "refund", "urgency": "high", "language": "en"}` — so the response can be routed programmatically without a human reading it [2].

**Report generation** uses template-echo prompts to produce consistently structured summaries. The template defines the sections (Executive Summary, Key Findings, Recommended Actions) and the model fills in the content. Every report comes out in the same shape, ready to insert into a fixed-layout document [3].

In all three patterns, the validator-with-retry sits between the model call and the rest of the application. It is not optional in production: format drift happens even with excellent prompts, and an unvalidated malformed response reaching application code produces bugs that are hard to trace [2].

## 8. Best Practices

**Do**

- Be explicit about the exact keys, positions, or headings you need — do not assume the model will infer structure from context [1][2].
- Add a suppression instruction ("Output the JSON only") whenever the output must be machine-parsed. This is the single most impactful addition to a format instruction [2].
- Use the format-example strategy (Strategy 2) for unusual or highly specific formats where plain-language descriptions are ambiguous.
- Validate the response before passing it to the rest of your program — even a simple `try/except` is better than nothing.
- Log format failures during development. Patterns in failures tell you which part of your format instruction is unclear.

**Do not**

- Write format instructions that contradict each other ("Return JSON" alongside "Write your answer in prose paragraphs") — contradictions produce unpredictable output.
- Assume a format instruction in the user message is as reliable as one in the system prompt. Persistent format requirements belong in the system prompt (from 13.1).
- Use vague format language: "structured format", "clean output", "machine-readable" without specifying what structure, what clean means, or which machine format. The model cannot act on vague format instructions reliably [1][3].
- Skip the validator in code that will run in production. Format drift happens in testing, not just in edge cases.

## 9. Hands-On Exercise

1. Take one of the prompts you have already written for your domain application (from the lab exercises in topics 13.1 through 13.5).
2. Add a format instruction to request a JSON object with at least three keys relevant to your domain (for example: `{"topic": "...", "confidence": "high|medium|low", "response": "..."}`).
3. Call the model ten times with realistic inputs. Record how many responses pass `json.loads()` without error and contain all required keys.
4. Write a validator function (based on the Step 4 template above) and a retry loop (Step 5). Re-run your ten inputs through the full validator-with-retry pipeline.
5. Document what the validator caught: how many first-call failures? How many retries succeeded? How many fell through to the fallback?
6. Compare the pass rate before and after adding the format instruction and note how format specification affected consistency.

## 10. Key Takeaways

- LLMs produce inconsistent output format by default because they are trained on stylistically varied text and sample from a probability distribution — without a format instruction, the shape of the response is unpredictable [1].
- **Format specification** — writing an explicit instruction that declares the structure, fields, and suppression of surrounding text — is the core technique for controlling output shape through the prompt [1][2].
- Three strategies cover most cases: **inline declaration** (state the format in words), **format example** (show one filled-in example), and **template echo** (provide the template with placeholders) — they can be combined [2][3].
- **Format drift** (the response not matching the declared format) happens even with good instructions because the model treats format instructions as strong suggestions rather than hard rules; always validate the response before using it in code [1][2].
- The **output validator pattern** — validate, retry once with a corrective message on failure, return a fallback if the retry also fails — is the standard practice that separates test-grade prompts from production-grade prompts [2][3].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
