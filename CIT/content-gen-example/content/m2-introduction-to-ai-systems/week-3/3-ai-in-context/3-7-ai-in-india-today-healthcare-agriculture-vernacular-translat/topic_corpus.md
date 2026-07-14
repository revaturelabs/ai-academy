---
topic_id: "3.7"
title: "AI in India today — healthcare, agriculture, vernacular translation"
position_in_module: 1
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. AI in India Today — Healthcare, Agriculture, Vernacular Translation — Topic Corpus

## 2. Prerequisites

Topics 3.1 and 3.2 should be read first.

- **3.1** — Machine Learning, Deep Learning, Artificial Neural Networks, Supervised Learning: these topics explain how an AI system learns from data, which is the foundation for everything deployed in the field.
- **3.2** — Large Language Models (LLMs), Transformers, Hallucination, Prompt: these concepts explain the text-based AI tools that power vernacular chatbots and agricultural advisory systems.

## 3. Learning Objectives

By the end of this topic, learners should be able to:

1. Describe at least two real AI deployments in Indian healthcare and explain what problem each solves for patients or clinicians.
2. Explain how AI is being used in Indian agriculture, including what inputs the system uses and what outputs farmers receive.
3. Define vernacular NLP and explain why building multilingual AI for India is harder than building English-only AI.
4. Identify the IndiaAI Mission and BharatGen as government-backed initiatives and state their goals.
5. Recognise the digital divide as a limiting factor and give a concrete example of how it affects who benefits from AI in India.

## 4. Introduction

Imagine a farmer in rural Telangana whose crop has a yellow fungal spot spreading across the leaves. She has never heard the word "agronomist." The nearest agricultural extension officer is two hours away by bus. But she has a cheap smartphone with mobile data. She takes a photo, opens a government chatbot — and in Telugu, within seconds, gets a diagnosis and a recommended treatment plan.

That scenario is not science fiction. As of 2025, versions of it are happening across India — in hospitals, on farms, and on the phones of hundreds of millions of people whose first language is not English.

India's scale makes it one of the most consequential test-beds for AI in the world: 1.4 billion people, 22 constitutionally recognised languages, a shortage of trained doctors in rural areas, smallholder farming that feeds a sixth of humanity, and a government that has explicitly committed to making AI a national infrastructure priority. This topic looks at what is actually being deployed, who benefits, and where the gaps remain.

## 5. Core Concepts

### 5.1 Computer Vision in Medical Diagnosis

**Computer vision** is the branch of AI that enables computers to interpret and act on visual information — photographs, scans, live video. In medical settings, computer vision models are trained on large libraries of annotated images (X-rays labeled by radiologists, retinal scans labeled by ophthalmologists) and learn to spot the same patterns a specialist would look for.

India has a significant shortage of specialist doctors, especially outside major cities. AI-assisted diagnosis is one response. The Indian government's **IndiaAI Mission** — a national programme announced in 2023 and funded through 2028 — identifies healthcare as a priority sector and supports infrastructure for AI deployment in public health systems [1].

A concrete example: the All India Institute of Medical Sciences (AIIMS) network has established AI Centres of Excellence that use computer vision to assist with screening for diseases like diabetic retinopathy (damage to the eye's blood vessels caused by diabetes). A patient in a district hospital has their retina photographed; the AI flags whether the scan looks normal or needs a specialist's attention. The specialist review still happens, but the AI filters the high-volume cases so doctors can focus where the need is greatest [1].

**Telemedicine** — the delivery of medical consultations and advice remotely, typically via video call, phone, or a digital platform — is the connecting layer between AI diagnosis tools and patients who are geographically far from hospitals. India's national telemedicine service (eSanjeevani) had crossed 300 million consultations by 2025, and AI tools are being integrated to help triage patients before they reach a doctor [1].

### 5.2 AI in Agriculture — From Satellites to Chatbots

India has approximately 100 million farming households, the majority operating on holdings of less than two hectares. These smallholder farmers face three recurring challenges: not knowing when to plant (weather unpredictability), not knowing what is wrong with their crops (pest and disease identification), and not being able to access credit or market information efficiently.

AI is being applied to all three. The government's **Kisan e-Mitra** (which translates roughly as "Farmer's Friend") is a chatbot available via mobile that allows farmers to ask questions about their crops in simple language and receive advice in return [2]. It uses satellite imagery to monitor crop health at scale — satellites capture the spectral signatures (patterns of light reflected from vegetation) of agricultural land, and AI models interpret those signatures to flag drought stress, pest infestations, or nutrient deficiencies across entire districts [2].

This is an application of **supervised learning** (introduced in 3.1): the AI is trained on pairs of satellite images and known ground-truth outcomes (this image was followed by a crop failure; this one was not), and it learns to predict which patterns predict which outcomes.

The output is not just for individual farmers. State governments use aggregate AI analyses of satellite data to decide where to dispatch extension officers, pre-position inputs like fertiliser, or trigger insurance payouts. AI turns individual farm-level signal into district-level policy intelligence [2].

### 5.3 Vernacular NLP and Multilingual AI

**Vernacular NLP** (Natural Language Processing — the subfield of AI that deals with human language) refers to language AI built specifically for regional or minority languages, as opposed to major world languages like English or Mandarin that have abundant training data.

Most large language models (LLMs, introduced in 3.2) are trained overwhelmingly on English text. English makes up well over half of internet text despite being the first language of fewer than 5% of India's population. This creates a profound mismatch: the most capable AI tools speak the language of the least typical Indian user.

**Multilingual AI** refers to AI systems that can understand, process, and respond in multiple languages — ideally switching fluidly depending on what the user writes or speaks. Building multilingual AI for India is technically harder than building English-only AI for three reasons:

1. **Data scarcity.** There is far less digitised text in languages like Santali, Bodo, or Dogri than in English. Models trained on scarce data are less reliable.
2. **Script diversity.** India's languages use 11 different scripts (Devanagari, Bengali, Tamil, Telugu, Kannada, and others). Each script requires separate tokenisation handling — tokenisation being the process (introduced in 3.4) of splitting text into the units the model processes.
3. **Code-mixing.** Real Indian language use frequently blends languages in a single sentence ("Hinglish" being the most common example). Models trained only on "pure" language text struggle with this.

**BharatGen** is a government-backed initiative under the IndiaAI Mission to build foundational AI models that natively support all 22 of India's constitutionally scheduled languages [3]. Rather than retrofitting existing English-dominant models, BharatGen aims to train models from the ground up on multilingual Indian corpora, covering everything from Assamese to Urdu. As of 2025, a BharatGen LLM covering 22 languages has been released for research use [3].

Regional-language chatbots built on top of multilingual models are already deployed: agricultural advisories in Marathi and Punjabi, health information in Tamil and Bengali, and government service portals that accept voice queries in local languages [3]. A 2025 survey cited in the resource found that 75% of Indian smartphone users prefer to interact with digital services in their native language rather than in English [3] — a finding that makes a strong practical case for continued investment in vernacular AI.

### 5.4 The Digital Divide

The **digital divide** is the gap between people who have reliable access to digital technology (smartphones, internet connectivity, electricity) and those who do not. It is the most important limiting factor in AI's real-world impact in India.

Rural electrification in India is near-universal on paper, but reliable power supply is inconsistent in many districts. Mobile internet penetration has grown rapidly — India now has over 800 million internet subscribers — but connectivity is still patchy in remote tribal areas and across much of the northeast. Even where connectivity exists, the cost of data, the literacy required to use apps, and the availability of devices (not everyone in a household has a personal smartphone) shape who actually benefits from AI tools [1].

This matters for an honest assessment of AI's impact in India: deployment announcements (a chatbot launched, a diagnostic tool piloted) are not the same as adoption at scale. The digital divide is one reason AI in India tends to get more traction when it is integrated into existing channels (SMS, voice calls, government kiosks) rather than requiring users to download new apps and maintain accounts.

## 6. Implementation

This section traces the end-to-end flow for one representative deployment — AI-assisted crop health monitoring — to make the mechanics concrete.

**Step 1: Data collection.** Satellites pass over agricultural land on regular schedules (some commercial satellites provide revisit times of 1–3 days). Each pass produces a multispectral image — essentially a photo that captures not just visible light but also infrared wavelengths that vegetation absorbs or reflects differently depending on health status.

**Step 2: AI analysis.** A trained computer vision model processes the satellite imagery, pixel by pixel, and assigns each field a health status score. This is the same type of supervised learning described in 3.1: the model was trained on images paired with ground-truth data about what later happened to those fields.

**Step 3: Alert generation.** When the model flags an anomaly — drought stress or early-stage pest infestation — the system generates an alert. The alert contains the GPS coordinates of the affected area, the predicted problem, and recommended actions.

**Step 4: Delivery to farmers.** In the Kisan e-Mitra system, the alert is delivered as an SMS or chatbot message in the farmer's preferred language [2]. If the farmer replies with a follow-up question, the LLM component handles the conversational exchange, translating the AI-generated analysis into plain-language advice.

**Step 5: Human verification.** Extension officers in the relevant block receive aggregated alerts for their area. Where the AI flags widespread problems, they do physical spot checks. The AI does not make decisions; it prioritises human attention.

**Step 6: Feedback loop.** Outcomes — whether the intervention worked, what the farmer actually found in the field — are fed back as training data to improve the model over time. This is the ongoing training cycle that makes supervised learning systems improve with deployment.

## 7. Real-World Patterns

**Pattern 1 — AI-assisted retinal screening at AIIMS.** The AIIMS network's AI Centres of Excellence use computer vision models to screen for diabetic retinopathy in patients at district hospitals that do not have on-site ophthalmologists [1]. A nurse photographs the patient's retina; the AI classifies it as normal, suspect, or requiring urgent referral. This triages the caseload so specialists review only the flagged scans. Early detection of diabetic retinopathy prevents blindness; this deployment targets a population too geographically dispersed to reach through conventional specialist deployment.

**Pattern 2 — Kisan e-Mitra crop advisory.** The IndiaAI portal documents how Kisan e-Mitra allows farmers to describe a crop problem in plain language via SMS or app and receive advice [2]. The chatbot draws on agronomic knowledge bases and live satellite data. It is available in multiple Indian languages. The system routes complex cases to human experts while handling routine queries automatically — a pattern sometimes called "AI triage."

**Pattern 3 — BharatGen and the 22-language LLM.** BharatGen's foundational multilingual model, released in 2025, enables developers to build applications that work across India's language spectrum without building separate models for each language [3]. Early applications include legal aid chatbots in Hindi and Odia, and health information systems in Tamil. The model's open availability under the IndiaAI Mission means smaller NGOs and state governments can build on it without the cost of training their own models.

**Pattern 4 — Telemedicine integration with AI triage.** India's eSanjeevani platform — the world's largest government-run telemedicine service — is integrating AI to handle pre-consultation triage [1]. Before a patient reaches a doctor, an AI system collects symptoms through a structured conversation, flags red-flag symptoms for immediate priority, and pre-fills the patient record. This reduces the time a doctor spends on history-taking and increases throughput in high-demand slots.

**Pattern 5 — Voice-first vernacular interfaces.** Across multiple deployments, the practical discovery has been that text-based interfaces have limited reach when a significant share of the target population has low literacy. Voice-based AI — where the user speaks a question in their dialect and receives a spoken answer — extends reach further [3]. Agricultural advisories in states like Andhra Pradesh and Maharashtra are moving toward voice-first interfaces for this reason.

## 8. Best Practices

**Ground AI deployments in existing workflows, not on top of them.** The most successful Indian AI deployments integrate into how farmers, patients, and government workers already operate — SMS-based alerts reach farmers who already use feature phones; AI triage slots into the existing eSanjeevani call flow. AI that requires users to adopt a new workflow from scratch has high abandonment rates.

**Design for the language the user actually speaks, not a national lingua franca.** The 75% native-language preference finding [3] is a design requirement, not an aspiration. Forcing users to interact in a language they are not fluent in degrades both the quality of inputs (users describe problems less precisely) and the adoption rate.

**Keep a human in the loop for consequential decisions.** None of the deployments described here — diagnosis, crop advice, telemedicine triage — removes the human decision-maker. The AI assists and prioritises; a clinician or extension officer makes the final call. This is especially important given that LLMs can hallucinate (introduced in 3.2): an AI can produce confident, fluent, wrong advice.

**Do not conflate announcement with impact.** India has hundreds of AI pilots and platform launches. The realistic question is: does this deployment reach the intended user at a cost they can absorb, in a language they speak, over infrastructure they have? Many pilots stall at this test.

**Monitor for performance degradation across languages.** A model that performs well in Hindi may perform significantly worse in a low-resource language like Santali. Multilingual AI systems require separate quality evaluation for each language, not just aggregate benchmarks [3].

## 9. Hands-On Exercise

This exercise connects to the week's Capability Probe lab.

1. Open Claude (or any available LLM) and submit this prompt in English: *"A farmer in Maharashtra notices that their soybean leaves are turning yellow at the edges. What could be causing this, and what should the farmer do?"* Note the response.

2. Now ask the same question but insert a deliberate ambiguity: *"Leaves are yellowing. What to do?"* — no crop, no location. Observe how the model handles missing context.

3. Copy the original question, paste it through a free translation tool into Hindi, then submit the Hindi version to the same LLM. Does the quality of the response change? Is it more or less specific?

4. In your lab journal (Journal Entry #2), record: (a) what the model got right, (b) where it seemed confident but vague or potentially wrong, and (c) whether the language switch changed anything you noticed about the answer quality. This is a small version of the kind of evaluation a real AI deployment team would perform before releasing a system to users.

## 10. Key Takeaways

- AI is actively deployed in India across healthcare (diagnostic screening, telemedicine triage), agriculture (crop monitoring, farmer chatbots), and language access (multilingual and vernacular NLP tools) — these are live 2025 deployments, not future projections [1][2][3].
- The IndiaAI Mission and BharatGen represent a deliberate government strategy to build AI infrastructure designed for India's linguistic and infrastructural reality, rather than adapting Western English-first tools [3].
- Vernacular NLP is technically harder than English NLP because of data scarcity, script diversity, and code-mixing — but it is also more consequential for India's population, 75% of whom prefer to use digital services in their native language [3].
- The digital divide — gaps in connectivity, device access, literacy, and power supply — determines who actually benefits from AI deployments, not just who is targeted by them [1].
- In every domain covered here, AI acts as an assistant or triage layer, not as a final decision-maker; a doctor, extension officer, or human reviewer remains in the loop, partly because AI systems can produce confident but incorrect outputs (hallucination, introduced in 3.2).

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
