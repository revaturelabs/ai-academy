---
topic_id: "4.6"
title: "Multimodal AI — working with text, image, audio, and video in one system"
position_in_module: 1
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Multimodal AI — working with text, image, audio, and video in one system — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **4.1 Foundation models** — the concept of a multimodal model was named there; this topic is the full deep-dive on what that actually means.
- **4.2 Fine-tuning** — understanding how models adapt to new tasks helps frame why a single model can handle many types of input.
- **4.3 RAG (Retrieval-Augmented Generation)** — shows how external information is fed into a model at query time; that same idea extends to non-text inputs.
- **4.4 Agents** — the observe-think-act cycle and tool use introduced there appear again when an agent must perceive an image or listen to audio.
- **4.5 Tool use** — multimodal models often act as the reasoning core that receives outputs from image or audio tools.

## 3. Learning Objectives

By the end of this topic, you should be able to:

- Define multimodal AI and explain why combining multiple types of information in one system produces results that separate single-type systems cannot.
- Name the four main modalities — text, image, audio, and video — and give one real example of each.
- Describe, in plain language, how a multimodal model converts different types of input into a shared representation so they can be processed together.
- Identify at least three real-world applications of multimodal AI and explain what problem each one is solving.
- Explain one key limitation of multimodal AI systems that users and organisations need to keep in mind.
- Distinguish between a unimodal model and a multimodal model using a concrete scenario.

## 4. Introduction

Think about how you experience the world. When a friend sends you a voice message with a photo attached, you do not separate the two — you listen and look at the same time, and your understanding comes from both together. If the photo shows a crowded cafe but your friend says "it's so quiet here," you immediately notice the mismatch. Your brain processed text (the words), audio (the voice), and image (the photo) as one unified experience.

For most of AI's history, software did not work this way. There were systems that could read text, and different systems that could describe images, and yet other systems that could transcribe speech. Each system worked in isolation. A text-reading system could not look at a chart. An image-describing system could not hear a question spoken aloud. These isolated systems are called **unimodal** — they handle only one type of input.

Multimodal AI changes this. A **multimodal AI system** is one that can receive, understand, and generate content across more than one type of input — for example, text, images, audio, and video — all within the same model [1]. Instead of handing a question to one system and a photo to another, you hand both to one system and it reasons about them together.

You already encountered the term "multimodal model" in Topic 4.1 when foundation models were introduced. This session gives that term its full meaning. You will see what a modality actually is, how the four major modalities work, what it takes to combine them, and where multimodal AI already shows up in everyday tools [1][3].

## 5. Core Concepts

### 5.1 What is a modality?

**Modality** — a type or channel of information. Different modalities are simply different forms that information can take.

Everyday life involves many modalities at once: when you watch a news broadcast, you receive information as spoken words (audio), moving images (video), on-screen text captions (text), and sometimes a map or graph (image). Each of these is a distinct modality.

In AI, the four modalities that matter most today are:

| Modality | What it is | Common example |
|---|---|---|
| **Text** | Written or typed language — words, sentences, documents | A customer email, a news article, a typed question |
| **Image** | A still picture — photo, diagram, chart, screenshot | A medical scan, a product photo, a road-sign |
| **Audio** | Sound waves — speech, music, environmental noise | A voice message, a podcast, an alarm |
| **Video** | A sequence of images over time, usually with audio | A surveillance clip, a classroom recording, a social-media reel |

A unimodal model handles exactly one of these rows. A multimodal model handles two or more of them together [1][3].

### 5.2 The shared representation — how different inputs become comparable

This is the key mechanism behind multimodal AI, explained in plain terms.

Computers store everything as numbers. Text, images, audio, and video are all ultimately converted into lists of numbers before any AI model processes them. The challenge is that the numbers for a sentence and the numbers for a photograph are arranged in completely different ways — like two sets of building blocks that are different shapes and sizes.

A multimodal model solves this by learning to convert each modality into a **shared representation space** — think of it as a common internal language that text, images, audio, and video are all translated into before reasoning begins [2][3].

Here is an analogy. Imagine a translator booth at an international conference. One delegate speaks in French, another in Arabic, another in English. Each language is different, but the translation system converts all of them into a common protocol — earphones — that every delegate can receive. The multimodal model's shared representation space is that protocol.

Once all inputs are translated into the shared space, the model can:
- Compare a sentence to an image (for example, "does this caption match this photo?")
- Answer a question about a sound clip (for example, "what emotion does this voice express?")
- Describe what happens across video frames (for example, "summarise this one-minute clip")

The technical details of how this translation is learned — involving mechanisms named in some sources — are covered in later modules. What matters here is that the shared representation is the bridge that makes one model work across all four modalities [2].

### 5.3 Text — the backbone modality

Text was the first modality that large AI models mastered. The foundation models you met in Topic 4.1 — like early versions of GPT — were trained almost entirely on text. They learned from books, websites, code, and conversation transcripts [1].

Text remains central in multimodal systems for two reasons:

1. **Queries are usually written.** Even when a user uploads an image, they typically type a question about it: "What is wrong with this X-ray?" or "Write a caption for this photo." Text is how humans most commonly express intent to the model.
2. **Answers are usually written.** Even when the model processes audio or video, the output is often a text summary, a transcript, or a written explanation.

So text is both the primary input for questions and the primary output for answers — even in systems that also handle other modalities.

### 5.4 Images — seeing the visual world

An **image** input gives the AI the ability to process still pictures. This requires the model to understand shapes, colours, spatial relationships (what is above, below, left, right), and context — a white coat in a hospital means something different from a white coat in a kitchen [1][3].

Practical applications include:

- **Medical imaging** — a multimodal model reads a doctor's written report and the corresponding scan simultaneously, flagging inconsistencies between what the text says and what the image shows.
- **Retail** — a customer uploads a photo of a broken item; the model reads the warranty text and the photo together and decides whether the claim is valid.
- **Accessibility** — an AI describes the contents of an image for a visually impaired user, combining the image with any on-screen text labels.

The image modality also includes diagrams, charts, and infographics — types of visual information that carry meaning a text-only model would completely miss [1].

### 5.5 Audio — understanding sound

**Audio** covers anything that arrives as a sound wave: speech, music, background noise, alarms, or a mix of all of them. For AI, audio input usually means one of two things:

1. **Speech recognition** — converting spoken words into text, so the rest of the model can process them as language. This is sometimes called transcription.
2. **Audio understanding** — recognising non-speech sounds, emotions in a voice, music genre, or environmental context (is that a busy street or a quiet office?).

Multimodal systems that include audio can do things a text-only system cannot:
- A model listening to a customer support call can read the customer's account history at the same time and suggest a resolution, all in one system [3].
- A meeting summariser transcribes spoken discussion and reads any slides shared on screen, producing a single coherent output.

One important note: speech recognition by itself (converting speech to text) is not the same as a full multimodal model. True audio understanding means the model reasons about the audio content, not just its transcript.

### 5.6 Video — images plus time

**Video** is the most data-rich modality. A one-minute video at standard quality contains around 1,800 individual frames (still images) plus a soundtrack. That is an enormous amount of information to process.

Video understanding requires a model to track changes over time — what was happening at second 10 versus second 40, who is speaking when, and how a scene evolves. This is significantly harder than processing a single image because the model must hold a sequence of frames in context, not just one [2][3].

Real-world uses of video understanding in multimodal AI include:

- **Security and surveillance** — automatically flagging unusual activity in a camera feed.
- **Sports analysis** — reviewing match footage to extract statistics about player movement.
- **Education** — a model watches a recorded lecture and produces a structured summary with timestamps.
- **Accessibility** — generating audio descriptions of video content for visually impaired viewers.

Because video files are large and computationally expensive to process, video understanding is often the last modality an organisation adds to a multimodal system [2].

### 5.7 Putting it together — how a multimodal model processes a mixed input

Here is a step-by-step picture of what happens when you send a typed question and an uploaded photo to a multimodal system:

1. **Receive input** — the system receives your typed question (text) and the uploaded photo (image) at the same time.
2. **Encode each modality** — each input is converted into numbers using a modality-specific encoder. The text encoder handles language; the image encoder handles pixels.
3. **Translate to shared space** — both sets of numbers are mapped into the shared representation space, where they can be compared and combined.
4. **Reason across modalities** — the core reasoning engine works over the combined representation: "The question asks about X; the image shows Y; my answer is Z."
5. **Generate output** — the model produces a response, typically as text (though some systems can also generate images or audio as output).

This five-step flow is the architecture underlying tools like GPT-4o, Google Gemini, and others when they process mixed inputs [1][3].

**Encoder** is introduced here: an **encoder** is the component of a multimodal model that converts one type of input (text, image, audio, or video) into the numbers that the model's reasoning engine can work with.

### 5.8 Unimodal versus multimodal — a direct comparison

| | **Unimodal model** | **Multimodal model** |
|---|---|---|
| Input types handled | One (e.g. text only) | Two or more (e.g. text + image + audio) |
| Example task | "Summarise this paragraph" | "Describe what is wrong in this X-ray and explain it in plain English" |
| What it misses | Any information in other modalities | Nothing (within its supported modalities) |
| Complexity | Lower — simpler to train and deploy | Higher — more data, more compute, more integration work |
| Typical use case | Chatbots, document search, translation | Medical diagnosis, accessibility tools, creative assistants |

The key benefit of multimodal AI is not just convenience — it is that some problems genuinely cannot be solved with one modality alone. A doctor asking "does the patient's verbal description match what I see in the scan?" requires both audio or text and image at the same time [1].

### 5.9 Limitations to know

Multimodal AI is powerful, but it is not infallible. Key limitations include:

**Hallucination across modalities.** You met hallucination in Topic 4.2 — models can generate plausible-sounding but incorrect output. In multimodal systems this risk extends further: a model might describe an image incorrectly, transcribe audio with errors, or misidentify what is happening in a video clip [3].

**Modality gaps.** A model trained heavily on text-image pairs may perform poorly on audio or video because it has seen far fewer examples of those modalities during training. Not all multimodal models handle all four modalities equally well.

**Data and compute cost.** Processing video in particular requires significant memory and computing power. This affects which organisations can build and run multimodal systems at scale.

**Privacy and consent.** Multimodal inputs often contain sensitive personal information — faces, voices, medical images. Processing this data raises legal and ethical questions that pure text systems face less acutely. The legal frameworks that govern these concerns — including the EU AI Act and NIST RMF — are covered in a later module.

## 6. Implementation

No code is required in this course. The following steps describe the conceptual process a multimodal AI system follows when handling a mixed input, so you can explain it clearly to another person:

1. **Receive** — accept inputs from the user. These may be any combination of text, image, audio, or video.
2. **Identify** — recognise what type of input each piece is (text, image, audio, video).
3. **Encode** — convert each input type into numbers using the appropriate encoder for that modality.
4. **Align** — translate all encoded inputs into the shared representation space so they are comparable.
5. **Reason** — apply the core reasoning engine to the combined representation.
6. **Generate** — produce a response, usually in text, but potentially in other modalities depending on the system.

This six-step sequence is the same whether the system is a consumer chatbot, a medical diagnostic tool, or a video summariser [2][3].

## 7. Real-World Patterns

Multimodal AI has moved from research laboratories into products used by millions of people. Three broad patterns show up repeatedly in real deployments [1][3]:

**Pattern 1 — The conversational assistant with vision.**
Tools like GPT-4o and Google Gemini accept a photo and a typed question in the same message. A user photographs a restaurant menu written in a foreign language and asks "what are the vegetarian options?" The model reads the image and the question together and answers in the user's language. This is the most widespread consumer deployment of multimodal AI today.

**Pattern 2 — The document intelligence system.**
Organisations process invoices, contracts, and reports that combine printed text, tables, charts, and logos — all on the same page. A unimodal text model would extract only the typed words and miss everything encoded in charts and tables. A multimodal model reads the whole page as one unified document, regardless of which parts are text and which are images [1].

**Pattern 3 — The accessibility layer.**
Audio description services for visually impaired users, real-time captioning for deaf or hard-of-hearing users, and image-to-speech tools all combine two or more modalities. Multimodal AI makes these tools faster, cheaper, and more accurate than previous-generation systems — and enables them to work in real time [3].

## 8. Best Practices

For anyone evaluating or deploying a multimodal AI system — relevant to your A2 AI Systems Essay and the lab evaluation activity for this week:

**Do:**
- Check which modalities a model actually supports before assuming it handles all four. Many tools marketed as "multimodal" handle only text and image.
- Test each modality with representative samples from your actual use case. A model that performs well on general photos may perform poorly on specialised images such as medical scans or engineering drawings.
- Confirm the model's knowledge cutoff (introduced in Topic 4.3) — this applies to all modalities, not just text.
- Consider data privacy obligations before uploading images, audio, or video containing identifiable people.

**Avoid:**
- Assuming accuracy is uniform across modalities. A model may transcribe speech with high accuracy but misidentify objects in images at a much lower rate.
- Ignoring hallucination risk. Multimodal hallucinations can be harder to catch because you are checking a description against an image, not just comparing text to text.
- Using a multimodal model for a task that only needs one modality. A specialised unimodal system may outperform a generalist multimodal one on a narrow task.

## 9. Hands-On Exercise

This exercise connects directly to the lab activity for Week 4 — designing a five-criteria evaluation rubric and comparing two AI tools with evidence.

**Exercise — Evaluate two AI tools on a multimodal task:**

1. Choose one multimodal task: for example, "upload a photo of a handwritten note and ask the model to transcribe and summarise it."
2. Try the task on two different AI tools — at least one should claim to be multimodal (for example, GPT-4o or Google Gemini free tier).
3. For each tool, record: (a) which modalities it accepted, (b) how accurate the output appeared, (c) what it got wrong or missed, and (d) whether the response was confident even when wrong.
4. Use your observations to draft two criteria for a comparison rubric.
5. Discuss with a partner: did having more modalities automatically produce a better result, or did quality depend on other factors?

No payment is required if you use a free-tier version of any of these tools.

## 10. Key Takeaways

- **Multimodal AI** means one model that can receive, understand, and generate content across more than one type of input — text, image, audio, and/or video — rather than being limited to a single type.
- The four main modalities are **text**, **image**, **audio**, and **video**; each carries information the others cannot. Some problems can only be solved when two or more modalities are processed together.
- Multimodal models work by converting each input type into a **shared representation space** — a common internal language — so the reasoning engine can compare and combine all inputs simultaneously.
- Real-world deployments already span consumer assistants (text and image chat), document intelligence (text and images on the same page), and accessibility tools (image, audio, and text combined).
- Key limitations — hallucination across modalities, uneven performance across input types, high compute cost for video, and significant privacy concerns — mean multimodal AI requires careful evaluation before deployment.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
