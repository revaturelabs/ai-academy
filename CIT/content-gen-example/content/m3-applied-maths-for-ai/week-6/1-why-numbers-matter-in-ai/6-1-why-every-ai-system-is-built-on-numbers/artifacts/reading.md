<!-- nav:top:start -->
[⬅ Previous: 5.13 — Knowing which governance framework applies to your system](../../../../../m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-13-knowing-which-governance-framework-applies-to-your-system/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 6.2 — Scalars ➡](../../../2-scalars-vectors-and-matrices/6-2-scalars-a-single-number-representing-one-property/artifacts/reading.md)
<!-- nav:top:end -->

---

# Why every AI system is built on numbers

## Overview

Every AI system ever built — whether it recognises faces, translates languages, recommends music, or generates text — works entirely with numbers at its core [1]. Your words, photos, and sounds are converted into numbers before any AI can touch them. Understanding this single fact unlocks everything else in this module: how AI finds similarities, how it learns from data, and why it makes the mistakes it does.

## Key Concepts

### Computers only understand numbers

A computer is, at its most fundamental level, a machine that stores and moves numbers [1]. Every character you type, every pixel on your screen, every second of audio — all of it is stored as a number.

Specifically, computers store everything as sequences of 0s and 1s, a system called **binary** — a way of writing any number using only two digits: 0 and 1. Electronic circuits can reliably distinguish two states: on (1) and off (0). That physical reality is what binary is built on [1].

**The key implication:** if you want a computer to do anything with a piece of data, that data must first be expressed as numbers. There is no other path.

### Real-world information is not already numbers

When you look at a photograph, you see a scene. When you hear a song, you hear melody and rhythm. When you read a sentence, you understand meaning. None of these arrive as numbers.

Before any AI system can work with a photo, a song, or a sentence, that information must be converted into numbers [2]. This conversion step is not optional — it is one of the foundational engineering challenges of building AI.

Here is how three common data types become numbers:

- **Images → numbers.** A digital photograph is a grid of tiny squares called **pixels** (picture elements). Each pixel stores a colour, recorded as three numbers: one for red, one for green, one for blue. A standard smartphone photo might contain 12,000,000 pixels — meaning one photo equals 36,000,000 numbers [3].
- **Audio → numbers.** Sound is a wave — air pressure rising and falling over time. A microphone measures those changes at thousands of moments per second. Each measurement is a number. One second of standard-quality audio contains roughly 44,100 numbers [3].
- **Text → numbers.** Computers assign letters to numbers using agreed-upon tables — the letter "A" is conventionally stored as the number 65. Modern AI uses a richer conversion for words and context; you will explore how that works in topics 6.7 and 6.8. For now: text, too, becomes numbers [2].

### A single number language is powerful

Once every data type — images, audio, text, sensor readings, medical records — is expressed as numbers, the same mathematical tools work on all of it [1]. An AI system does not need one engine for images and a completely separate engine for text.

This is why modern AI systems can handle multiple data types within the same framework. The diversity of real-world data types collapses into a single shared language: numbers [2].

### Numbers allow pattern-finding at scale

An AI finds patterns by looking at many examples and noticing regularities — but it does this with numbers, at a scale no human can match.

During training, an AI is shown millions of examples [1]. Each example is a set of numbers (the input — for instance, the pixel values of a photo) paired with a correct answer (the label — for instance, "cat," also stored as a number). The AI adjusts its internal numbers — called **parameters**, also known as **weights** — until its outputs match the correct answers as often as possible.

- **Parameter** — a number inside an AI model that gets adjusted during training.
- **Weight** — another name for a parameter; it reflects how much influence a particular input has on the output.

A large language model (LLM — a type of AI trained on vast amounts of text) may have billions of parameters. The pattern-finding is entirely arithmetic [1].

### Number-representations can carry meaning

When AI systems are trained on large amounts of data, the numbers they learn end up encoding relationships between concepts — relationships the AI was never explicitly told about [2]. You will explore exactly how this works in topics 6.5 through 6.9. The point for this topic: numbers are not just a technical necessity. They turn out to be a surprisingly expressive medium.

## Worked Example

Follow one photo through the full pipeline to see the principle in action.

1. **You snap a photo.** Your phone's camera captures a 4,000 × 3,000 grid of pixels — 12,000,000 pixels in total.
2. **Each pixel becomes three numbers.** A pixel with a warm orange colour might be stored as (220, 110, 30) — high red, medium green, low blue. Every pixel in the photo gets its own three-number description.
3. **The full photo is now 36,000,000 numbers.** This long list of numbers is the input the AI actually receives.
4. **The AI applies arithmetic.** Using its learned parameters (weights), it performs calculations on those 36,000,000 numbers.
5. **The output is a number.** The AI might produce a number close to 1 (meaning "cat detected") or close to 0 (meaning "no cat").
6. **The number is converted back.** Your app displays the label "Cat" — the human-readable result of entirely numeric computation [1].

Nothing in this chain required the AI to "see" a face or "understand" a photo. It manipulated numbers from start to finish.

## In Practice

The number-as-universal-language principle is not confined to research labs. Every AI product in daily use depends on it [3]:

- **Search engines** convert your query (words → numbers) and each webpage (words → numbers), then find the pages whose numbers are most similar to your query's numbers.
- **Music recommendation systems** represent each song as numbers encoding tempo, key, mood, and listening history, then recommend songs whose numbers are closest to songs you already liked [1].
- **Medical imaging AI** converts X-ray pixels into numbers and compares them to labelled examples to flag potential issues.
- **Spam filters** convert email text into numbers and check whether those numbers resemble numbers from past spam messages.

In each case the flow is identical: real-world data → numbers → arithmetic → output → convert back to human-readable form [3].

**Why the conversion itself matters:**

| Principle | Why it matters |
|---|---|
| Represent data in a way that preserves the structure you care about | If your number-representation throws away important information, no AI algorithm can recover it later. |
| Do not confuse the representation with the thing itself | An AI working with numbers that represent faces does not "see" faces — it manipulates numbers. Keeping this distinction clear prevents over-attributing human-like understanding to AI. |
| Garbage in, garbage out | If the numbers fed to an AI are noisy, biased, or poorly designed, the outputs will be too — regardless of how sophisticated the algorithm is [2]. |

How you convert data to numbers matters enormously. Two different representations of the same data can make the same AI model wildly more or less accurate [2].

## Key Takeaways

- **Every AI system operates on numbers.** Text, images, audio, and any other data type must be converted into numbers before an AI can process them. This is a hard constraint of how computers work, not a design preference [1].
- **Conversion is not trivial.** How real-world data is expressed as numbers determines what patterns an AI can — and cannot — find. Poor representations produce poor models [2].
- **Numbers are a universal language for data.** Expressing all data types as numbers means the same mathematical tools work across images, text, audio, and more [1].
- **Pattern-finding happens through arithmetic.** An AI's ability to recognise, predict, and generate is the result of mathematical operations on numbers — not human-like understanding. The parameters (weights) inside a model are numbers learned from millions of examples [2].
- **Number-representations can carry meaning.** When AI models are trained on large data, the numbers they learn end up encoding relationships between concepts — the deeper explanation starts at topic 6.5 [2].

## References

1. Labelbox. "Inside the Matrix: A Look into the Math Behind AI." https://labelbox.com/blog/inside-the-matrix-a-look-into-the-math-behind-ai/
2. Towards AI. "The Matrix: Mathematics Behind AI — How LLMs Think Through Linear Algebra." https://towardsai.net/p/machine-learning/the-matrix-mathematics-behind-ai-how-llms-think-through-linear-algebra
3. Techietory. "Understanding Matrices and Vectors in AI Applications." https://techietory.com/ai/understanding-matrices-and-vectors-in-ai-applications/

---
<!-- nav:bottom:start -->
[⬅ Previous: 5.13 — Knowing which governance framework applies to your system](../../../../../m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-13-knowing-which-governance-framework-applies-to-your-system/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 6.2 — Scalars ➡](../../../2-scalars-vectors-and-matrices/6-2-scalars-a-single-number-representing-one-property/artifacts/reading.md)
<!-- nav:bottom:end -->
