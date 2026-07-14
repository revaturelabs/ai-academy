---
topic_id: "13.9"
title: "Retry logic — what to do when validation fails"
position_in_module: 2
generated_at: "2026-06-14T00:00:00Z"
resource_count: 3
---

# 1. Retry Logic — What to Do When Validation Fails — Topic Corpus

## 2. Prerequisites

This topic continues directly from **13.8 — Output validation**. You should already understand what a validation function is, what a validation error means, and why an AI response can fail a format check. If those terms are unfamiliar, revisit 13.8 before continuing.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Explain in plain English what a retry loop does when an LLM response fails validation.
- Describe the role of a corrective message in prompting the model to self-correct.
- Use a retry counter to limit how many times a retry is attempted.
- Identify when a maximum retry limit has been reached and explain why a fallback response is returned at that point.
- Read and trace a short Python retry loop and predict what it will output.

## 4. Introduction

In topic 13.8 you learned how to check whether an AI response has the shape you need — the right format, the right fields, the right structure. But checking alone does not solve the problem. What happens when the check fails?

Imagine you run your validator and it tells you: "The response is missing the required JSON key `answer`." You have two realistic options: (a) give up and return nothing useful, or (b) ask the model to try again with a clearer instruction about what went wrong. Option (b) is called a **retry**.

This pattern — detect a failure, tell the model what it did wrong, ask it again, and keep a count of how many attempts you have made — is one of the most practical tools in any LLM application. Assessment A4 (Python and Prompt Engineering Portfolio, due this week) specifically asks for an output validator that retries on format failure, so you will be building exactly this. [1]

## 5. Core Concepts

### The retry loop

A **retry loop** is a piece of code that runs a validation check, and if the check fails, automatically calls the LLM again before giving up. The loop repeats a fixed number of times until either the response passes validation or the limit is reached. [1]

Think of it like submitting a form on a website: if you leave a required field empty, the page shows you an error and lets you try again. The form does not just crash — it loops back and gives you another chance. A retry loop does the same thing for your LLM call. [3]

### The corrective message

Simply calling the model again with the exact same prompt usually does not help. If the model produced a wrong format once, nothing has changed to help it do better the second time. [1]

The key improvement is a **corrective message** — a short addition to the prompt that explains what went wrong on the previous attempt. For example:

> "Your last response was missing the JSON key `answer`. Please respond again using this exact format: `{\"answer\": \"...\", \"confidence\": \"high|medium|low\"}`."

The corrective message carries two pieces of information: what failed, and a reminder of the expected output. This gives the model a concrete target to hit on the next attempt. [1][2]

### The retry counter

A **retry counter** is a simple integer variable that tracks how many attempts the loop has made. It starts at zero and increases by one each time the loop runs another LLM call. [1]

Without a counter, a retry loop could keep running forever if the model keeps failing. The counter gives you control. [1]

### Max retries

**Max retries** is the maximum number of attempts you allow before you stop trying. Once the retry counter reaches the max retries value, the loop exits whether or not the response is valid. [1][2]

A common default for simple applications is 2 or 3 retries. Higher numbers are possible but each retry costs time and money (each LLM call is a new request). For a beginner application, 2 extra attempts beyond the first call is a practical ceiling. [1][2]

### The fallback response

When the retry counter hits the max retries limit and the response still has not passed validation, the loop cannot wait any longer. At that point the code returns a **fallback response** — a safe, pre-written default that your application can always rely on. [1]

The fallback is not a crash. It is a graceful exit: you acknowledge that the model did not cooperate this time and you return something sensible rather than nothing (or an error). A fallback might be a default JSON object, an empty result, or a user-facing message like "Unable to process your request right now." [1][2]

### How the pieces connect

These five pieces work together in a fixed sequence: [1][2]

1. Call the model and get a response.
2. Run the validation function (from 13.8) on the response.
3. If validation passes — return the response. Done.
4. If validation fails — compose a corrective message, increment the retry counter, check whether the counter has reached max retries.
5. If counter < max retries — go back to step 1 with the corrective message added.
6. If counter >= max retries — return the fallback response. Done.

## 6. Implementation

Below is a minimal Python illustration. It is simplified on purpose — the goal is to see the structure clearly, not to build a production system.

```python
def call_with_retry(prompt, max_retries=2):
    attempts = 0
    message = prompt

    while attempts <= max_retries:
        response = call_llm(message)          # send prompt to the model
        if is_valid(response):                # run the validator (from 13.8)
            return response                   # validation passed — return it

        # validation failed — compose a corrective message
        attempts += 1
        if attempts > max_retries:
            break
        message = (
            prompt
            + "\n\nYour last response failed validation. "
            + "Please try again and ensure your output matches the required format exactly."
        )

    return {"error": "max retries exceeded", "result": None}  # fallback
```

Walk through what this code does:

- `attempts` is the retry counter, starting at 0.
- Each time through the `while` loop, it calls the model and validates the response.
- If the response is valid, it returns immediately.
- If the response is not valid, it increments `attempts` and adds a corrective message to the prompt before trying again.
- Once `attempts` exceeds `max_retries`, the loop breaks and returns the fallback dictionary. [1][3]

You do not need to memorise every line. The pattern to remember is: **check → fail → correct → retry → limit → fallback**.

## 7. Real-World Patterns

In real LLM applications, retry logic appears wherever structured output is required. Common examples include:

- A chatbot that must always return JSON so the frontend can parse it — if the model returns plain text instead, the retry adds "You MUST respond only with valid JSON."
- A document classifier that must return one of three category labels — if the model returns an explanation instead of a label, the retry reminds it: "Respond with only one word: `positive`, `negative`, or `neutral`."
- A data extraction tool that pulls key fields out of a contract — if a required field is missing, the retry names the missing field explicitly. [2][3]

In all these cases the retry loop follows the same five-part structure. What changes is the corrective message content.

You will see more advanced techniques — such as exponential backoff and structured output libraries — in later topics and courses. The concepts here are the foundation.

## 8. Best Practices

**Do**
- Always set a max retries limit. Never let a loop retry indefinitely.
- Make the corrective message specific. Tell the model *what* failed, not just "try again."
- Include the expected format in the corrective message — paste the template or an example.
- Return a meaningful fallback, not an empty crash. Your application should always be able to continue.

**Do not**
- Repeat the exact same prompt without any change. If the model failed once, an identical prompt will likely fail again.
- Set max retries higher than 3 for a beginner project. Each call costs time and may cost money.
- Use the retry loop as a substitute for a well-written original prompt. Fix the prompt first; add retry logic as a safety net, not a primary strategy.

## 9. Hands-On Exercise

This exercise maps directly to Assessment A4.

1. Write a validation function (from your work in 13.8) that checks whether an LLM response contains a specific JSON key — for example, `"answer"`.
2. Write a `call_with_retry` function that calls a model, runs the validator, and retries up to 2 times with a corrective message if validation fails.
3. Test it deliberately: pass a prompt that is likely to produce a poorly formatted response (e.g., a prompt that does not mention JSON at all) and observe whether the retry corrects it.
4. Document in a comment or a short note: what did the validator catch? How many retries were needed?

## 10. Key Takeaways

- A retry loop detects a validation failure and calls the model again rather than giving up immediately.
- A corrective message tells the model what went wrong and restates the expected format — this is what makes the second attempt more likely to succeed than simply repeating the original prompt.
- A retry counter tracks attempts and enforces a maximum retry limit so the loop cannot run forever.
- When the maximum retry limit is reached without a passing response, the code returns a fallback response — a safe, pre-written default.
- The full pattern is: **call → validate → pass (return) or fail → correct → retry → max reached → fallback**.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
