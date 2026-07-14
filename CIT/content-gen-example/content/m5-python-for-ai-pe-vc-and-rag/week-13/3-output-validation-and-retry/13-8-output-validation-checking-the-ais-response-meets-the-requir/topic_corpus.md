---
topic_id: "13.8"
title: "Output validation — checking the AI's response meets the required format"
position_in_module: 1
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Output Validation — Checking the AI's Response Meets the Required Format — Topic Corpus

## 2. Prerequisites

This topic builds directly on two earlier topics:

- **13.6 — Output format control** introduced the problem of format mismatch and the output validator pattern. You learned how to write a Rubric (a set of rules for what the AI must produce) and include it in a prompt.
- **13.7 — The 5-role context framework** introduced the Rubric role, which is the place in your prompt where you spell out exact format requirements. The Rubric role is the source of your validation checklist.

You do not need any prior Python experience beyond what the course has introduced. Familiarity with Python functions, `if` statements, and dictionaries is assumed.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. **Define** output validation and explain in plain language why AI responses cannot be assumed to follow a format.
2. **Identify** the format rules in a Rubric role that become the checklist for a validator.
3. **Write** a Python function that checks an AI response against at least two format constraints and returns `True` or `False`.
4. **Interpret** the result of a validation check and describe what the result means for the next step.
5. **Recognise** at least three common mistakes beginners make when writing validators.

## 4. Introduction

Imagine you ask a friend to fill out a paper form for you. They write something down and hand it back. Before you submit the form, you glance at it to make sure they filled in every required box and used the right format — date as DD/MM/YYYY, not "June 14th." That quick check *before* you submit is output validation.

When you ask an AI model to produce a response, you are in exactly the same situation. You specified a format in your prompt (back in topics 13.6 and 13.7). The model wrote something. Now you need to check whether it actually followed your instructions. The model is confident — it does not tell you when it breaks your rules. It just returns text.

**Output validation** is the step where your Python code plays the role of the careful form-reviewer. It reads the response, checks it against the rules you set, and reports pass or fail. This is not about whether the answer is *correct* — it is about whether the answer is in the *right shape* so the rest of your program can use it [1].

This matters for Assessment 4 (A4 — Python and Prompt Engineering Portfolio, due this week, 20% of your grade). A4 requires an output validator that retries when the format check fails. This topic covers the validation half. When validation fails, you can retry — you will cover that in topic 13.9.

## 5. Core Concepts

### 5a. What output validation is

**Output validation** means checking an AI's response against a set of expected format rules after the response has been returned [1].

Key word: *after*. The model has already produced its answer. You are not changing the prompt at this stage. You are inspecting what came back.

Think of the AI as a vending machine. You press the button for a chocolate bar (your format request). The machine delivers something. Validation is you looking at what dropped into the tray and confirming: "Yes, this is a chocolate bar, it is sealed, and it is the right size." If the machine delivered crisps instead, your validator notices.

Two important points:

1. **Validation is not about meaning.** You are not checking whether the AI gave a good recipe or a true fact. You are checking whether the response has the right *structure* — the right keys, the right types, the right length.
2. **Validation is automatic.** You write a Python function once. Every time a response comes back, you call the function. This is faster and more reliable than reading every response by eye.

### 5b. The format check function

A **format check function** (also called a **validation function**) is a Python function that takes one input — the AI's response — and returns one of two values [1][2]:

- `True` — the response passed all the format checks.
- `False` — at least one check failed.

Here is the simplest possible structure:

```python
def validate_response(response):
    # check something
    if <condition is not met>:
        return False
    return True
```

When the function returns `False`, your program knows something went wrong. When it returns `True`, your program knows it is safe to use the response.

A more useful pattern returns both the pass/fail result and a reason when something fails [1]:

```python
def validate_response(response):
    if <condition is not met>:
        return False, "reason the check failed"
    return True, "all checks passed"
```

This two-value return makes it much easier to debug problems later.

### 5c. Common things to check

What exactly should a validation function look for? The answer comes directly from the **Rubric role** you wrote in your prompt (topic 13.7). Every rule in the Rubric becomes one check in your validator [1][3].

The most common checks are:

**1. Is it valid JSON?**

JSON (JavaScript Object Notation) is a standard text format for structured data that looks like a Python dictionary. If your prompt asks for JSON and the response is plain text instead, no amount of further processing will work. You check for this by trying to parse the text and catching the error if it fails.

```python
import json

try:
    data = json.loads(response_text)
except json.JSONDecodeError:
    return False, "response is not valid JSON"
```

**2. Does it have the required keys?**

If your Rubric said "return a dictionary with the keys `dish_name`, `steps`, and `cooking_time`", you check that all three keys exist.

```python
required_keys = {"dish_name", "steps", "cooking_time"}
if not required_keys.issubset(data.keys()):
    return False, "missing required keys"
```

**3. Does it match a length constraint?**

If your Rubric said "steps must be a list of at least 2 items", you check the length.

```python
if len(data["steps"]) < 2:
    return False, "steps list is too short"
```

**4. Is it the right data type?**

If your Rubric said "`cooking_time` must be a number", you check the type.

```python
if not isinstance(data["cooking_time"], (int, float)):
    return False, "cooking_time must be a number"
```

A **schema check** is the name for checking structure all at once — types, required keys, and constraints together [1][3]. For A4, you write these checks yourself in plain Python. Libraries like Pydantic handle this automatically — you will encounter them in later topics.

A **validation error** is what happens when a response fails a check [1]. You will encounter this term in error messages and documentation. In plain language: a validation error means "the response did not match the rule."

### 5d. Where does the checklist come from?

The checklist is not something you invent on the spot. It comes directly from the Rubric role you wrote in your prompt [1].

In topic 13.7 you learned that the Rubric role tells the model exactly what the output must look like — keys, types, length, format. Every item in the Rubric becomes one `if` check in your validation function [1].

This connection is important: your prompt and your validator must agree [3]. If the Rubric says "return JSON with three keys" but your validator only checks for two, you will miss errors. If your validator checks for a key that is not in the Rubric, you are checking for something the model was never told to include.

**Prompt Rubric → Validation checklist → Validation function.** That is the chain [1].

## 6. Implementation

This is a step-by-step guide to writing a validator for your own project.

### Step 1 — Read your Rubric role and list every constraint

Open your prompt. Find the Rubric role (the section you wrote in topic 13.7). Write out every rule as a bullet:

- "Response must be valid JSON."
- "Must contain the key `dish_name` (string)."
- "Must contain the key `steps` (list of strings, minimum 2 items)."
- "Must contain the key `cooking_time` (integer, minutes)."

### Step 2 — Write one `if` check per constraint

Create a function. Translate each bullet into an `if` statement.

```python
import json

def validate_recipe_response(response_text):
    # Check 1: valid JSON
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        return False, "response is not valid JSON"

    # Check 2: required keys present
    required = {"dish_name", "steps", "cooking_time"}
    missing = required - data.keys()
    if missing:
        return False, f"missing keys: {missing}"

    # Check 3: steps is a list with at least 2 items
    if not isinstance(data["steps"], list) or len(data["steps"]) < 2:
        return False, "steps must be a list with at least 2 items"

    # Check 4: cooking_time is an integer
    if not isinstance(data["cooking_time"], int):
        return False, "cooking_time must be an integer"

    return True, "all checks passed"
```

### Step 3 — Call the validator after every AI response

Using the Anthropic SDK (already introduced in this course), get a response and immediately pass it to the validator.

```python
import anthropic
import json

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": your_prompt}
    ]
)

response_text = message.content[0].text
passed, reason = validate_recipe_response(response_text)

if passed:
    data = json.loads(response_text)
    print("Valid response:", data)
else:
    print("Validation failed:", reason)
    # topic 13.9 covers what to do next (retry)
```

### Step 4 — Use the result

If `passed` is `True`, continue with the response. If `passed` is `False`, you know *why* (the `reason` string). Log the reason for debugging. In topic 13.9 you will learn how to retry when validation fails.

## 7. Real-World Patterns

Output validation is not unique to learning exercises. Production AI systems use it routinely [2][3].

**Automated pipelines.** When an AI feeds data into a database or another program, the downstream system expects a precise format. A validation layer sits between the model and the database. If the response is malformed, the validator catches it before it causes a crash or corrupts data.

**Customer-facing chatbots.** If a chatbot response is supposed to include a structured JSON payload that populates a web form, missing keys mean a broken form. Validation catches this before the user sees an error.

**Testing and prompt improvement.** During development, running a validator on every response you collect tells you how often the model follows your format. If validation fails 20% of the time, your Rubric role needs more specificity.

The pattern is always the same: model response in, validator function, True or False out, act accordingly [1][2].

## 8. Best Practices

**Test your validator with bad inputs, not just good ones.**
A common mistake is only testing the validator with a perfectly formatted response. Test it with bad inputs — plain text when you expect JSON, a response with missing keys, an empty string. Your validator should return `False` for all of these [1].

**Return a reason, not just True/False.**
Always include a reason string when returning `False`. "validation failed" without context wastes debugging time. "missing keys: {'cooking_time'}" tells you exactly what to fix.

**Keep the validator separate from the prompt-building code.**
Write the validator as its own function. Do not mix validation logic into the code that builds the prompt or calls the API. Separate responsibilities make each part easier to test and change.

**Make your validator and your Rubric agree.**
If you add a new rule to the Rubric, add the matching check to the validator. If you remove a rule, remove the check. An out-of-sync validator and Rubric is a common source of false passes and false failures [3].

**Do not swallow errors silently.**
Never write a validator that catches an error internally and returns `True` anyway. Every failed check must produce a `False` and a reason that reaches the caller.

**Do not assume the model's fault.**
Validation failure does not always mean the model did something wrong. Your format request in the Rubric might be ambiguous. Check both the model's response and your Rubric before blaming either.

## 9. Hands-On Exercise

This forms the core of Journal Entry #8 and part of A4.

1. Pick the domain for your A4 project (recipe assistant, study helper, or your own choice).
2. Open your prompt and read the Rubric role you wrote in topic 13.7.
3. Write a validation function with at least three checks drawn from the Rubric.
4. Test it on three inputs: (a) a perfectly formatted response, (b) a response with a missing key, (c) a response that is not valid JSON.
5. In Journal Entry #8, write: what did the validator catch? What would have happened if you had skipped validation?

## 10. Key Takeaways

- **Output validation** means checking an AI's response against your format rules after the response is returned — not before, and not during generation.
- The **validation function** is the Python function that does the checking. It returns `True` (pass) or `False` plus a reason (fail).
- The **checklist for your validator comes from the Rubric role** in your prompt. Every rule in the Rubric becomes one check in the validator.
- Common things to check: valid JSON, required keys present, correct data types, length constraints.
- A **validation error** means the response broke one of your rules. Knowing which rule broke is essential for debugging and for deciding whether to retry.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
