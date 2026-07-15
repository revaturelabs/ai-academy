<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Cresent view of 10.4 — AI Today (Global and India).
     Source of truth: CIT 3.7.
     Regenerate: python Cresent/Technical/tools/generate_shared_readings.py -->
<!-- nav:top:start -->
Previous: [⬅ 10.3 — The Jagged Frontier](../10-3-the-jagged-frontier/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[10.5 — Capability vs Hype ➡](../10-5-capability-vs-hype/reading.md)
<!-- nav:top:end -->

---

# AI in India Today — Healthcare, Agriculture, Vernacular Translation

## Overview

India is one of the world's most important test-beds for AI: 1.4 billion people, 22 constitutionally recognised languages, a rural doctor shortage, and roughly 100 million smallholder farming households. AI is already deployed here — not as a future projection but as live 2025 systems — in hospitals, on farms, and on the phones of hundreds of millions of people [1][2][3]. This topic examines what those systems actually do, how they work at a high level, and who still gets left out.

## Key Concepts

### Computer Vision in Healthcare

**Computer vision** is the branch of AI that enables computers to interpret visual information — photographs, scans, or video. In medicine, a computer vision model is trained on large libraries of labelled images (for example, retinal scans labelled by eye specialists) so that it learns to spot the same patterns an expert would look for.

India faces a significant shortage of specialist doctors outside major cities. The government's **IndiaAI Mission** — a national programme announced in 2023 and funded through 2028 — identifies healthcare as a priority sector and supports the infrastructure needed to deploy AI in public health settings [1].

A concrete example is AI-assisted screening at the All India Institute of Medical Sciences (AIIMS) network. Patients at district hospitals — far from any ophthalmologist — have their retina photographed by a nurse. The computer vision model classifies the scan as normal, suspicious, or urgently needing specialist attention. Specialists then review only the flagged scans instead of every image. Early detection of diabetic retinopathy (damage to the eye's blood vessels caused by diabetes) prevents blindness; this system gets that screening to populations a specialist could never physically reach [1].

**Telemedicine** — the delivery of medical care remotely via phone, video call, or a digital platform — is the connecting layer between AI tools and geographically distant patients. India's national telemedicine service, eSanjeevani, passed 300 million consultations by 2025. AI triage tools are now integrated into eSanjeevani to collect symptoms before the patient reaches a doctor, flag red-alert cases for immediate priority, and pre-fill patient records — reducing the time a doctor spends on history-taking and increasing the number of patients seen per session [1].

### AI in Agriculture — Satellites to Chatbots

Smallholder farmers — those working less than two hectares — face three recurring problems: unpredictable weather, crop disease and pest identification, and limited access to market or credit information.

**Kisan e-Mitra** (meaning "Farmer's Friend") is a government-backed mobile chatbot that lets farmers ask questions about their crops in plain language and receive advice in return [2]. Here is how the system works:

1. Satellites pass over agricultural land every one to three days, capturing multispectral images — photographs that measure not just visible light but also infrared wavelengths that healthy and unhealthy vegetation reflect differently.
2. A computer vision model trained using **supervised learning** (introduced in 3.1) processes the imagery and assigns each field a health-status score. The model was trained on historical image–outcome pairs: this pattern later produced a crop failure; that pattern did not.
3. When the model flags drought stress, pest infestation, or nutrient deficiency, the system generates an alert with GPS coordinates and recommended actions.
4. The alert is delivered to the farmer as an SMS or chatbot message in their preferred language [2].
5. Aggregated alerts also go to agricultural extension officers for their district, helping them decide where to deploy limited staff or pre-position fertiliser.

The AI does not make the final decision. It prioritises human attention — a pattern sometimes called AI triage.

### Vernacular NLP and Multilingual AI

**Vernacular NLP** (Natural Language Processing — the subfield of AI that deals with human language) refers to language AI built for regional or minority languages rather than major world languages like English.

Most large language models (LLMs, introduced in 3.2) are trained overwhelmingly on English text. English represents the first language of fewer than 5% of India's population, yet it dominates training data. This mismatch means the most capable AI tools speak the language of the least typical Indian user.

**Multilingual AI** refers to AI systems that can understand, process, and respond in more than one language — ideally switching depending on what the user writes or speaks. Building multilingual AI for India is technically harder than building English-only AI for three reasons:

| Challenge | What it means |
|---|---|
| **Data scarcity** | Far less digitised text exists for languages like Santali, Bodo, or Dogri than for English. Models trained on scarce data are less reliable. |
| **Script diversity** | India's languages use 11 different scripts. Each requires its own **tokenisation** handling — tokenisation being the process (introduced in 3.4) of splitting text into units the model can process. |
| **Code-mixing** | Real Indian language use frequently blends languages within a single sentence ("Hinglish" is the most common example). Models trained only on "pure" text struggle with this. |

**BharatGen** is a government-backed initiative under the IndiaAI Mission to build foundational AI models that natively support all 22 of India's constitutionally scheduled languages [3]. Rather than retrofitting existing English-dominant models, BharatGen trains models from scratch on multilingual Indian corpora covering everything from Assamese to Urdu. A BharatGen LLM covering all 22 languages was released for research use in 2025 [3]. A 2025 survey found that 75% of Indian smartphone users prefer to interact with digital services in their native language rather than English [3] — making this not just a policy goal but a design requirement.

### The Digital Divide

The **digital divide** is the gap between people who have reliable access to smartphones, internet connectivity, and electricity and those who do not. It is the most important limiting factor on AI's real-world impact in India [1].

India has over 800 million internet subscribers, but connectivity is patchy in remote areas. Even where it exists, data costs, literacy requirements, and shared household devices shape who actually benefits. This is why successful Indian AI deployments tend to integrate into existing channels — SMS, voice calls, government kiosks — rather than requiring users to download new apps.

It also means deployment announcements are not the same as adoption at scale. An AI chatbot "launched" is not an AI chatbot "used by 10 million rural farmers."

## Worked Example

A farmer in Maharashtra notices that some of her soybean leaves have turned yellow at the edges. Here is what happens from satellite to solution.

**Step 1 — Satellite captures the field.**
A satellite passes over her district, producing a multispectral image of the agricultural area. The image captures how her field's vegetation is reflecting light differently from healthy fields nearby.

**Step 2 — AI flags a problem.**
The Kisan e-Mitra computer vision model processes the image and detects a pattern consistent with early nitrogen deficiency combined with a fungal stress marker. It generates an alert for her field coordinates.

**Step 3 — Alert reaches the farmer in Marathi.**
The farmer receives an SMS in Marathi: "Your soybean field shows signs of nutrient stress and possible early-stage leaf blight. Recommended action: apply urea at 20 kg/acre within 3 days and inspect for yellow-brown spots on the underside of leaves."

**Step 4 — She asks a follow-up question.**
She replies to the chatbot: "How much will urea cost?" The LLM component of Kisan e-Mitra handles the conversational exchange, drawing on agronomic knowledge bases and local market data to give a price estimate [2].

**Step 5 — Extension officer follows up.**
The aggregated alerts for her block show that a cluster of fifteen fields has the same flag. The local agricultural extension officer receives a priority list. She visits three representative farms that day to do physical spot-checks — confirming the AI diagnosis and authorising a subsidised input distribution.

**Step 6 — Outcome feeds back into the model.**
Two weeks later, farmers who applied the recommended treatment report their outcomes through the platform. This outcome data becomes new training data, improving the model's predictions over time.

Notice the pattern: the AI identifies, prioritises, and informs. The human verifies and decides. No crop advice is acted on solely because an AI said so.

## In Practice

**Keep humans in the loop for consequential decisions.**
None of the deployments in this topic — retinal screening, crop advisory, telemedicine triage — removes the human decision-maker. The AI assists and prioritises; a clinician or extension officer makes the final call. This is especially important because LLMs can **hallucinate** (introduced in 3.2): produce confident, fluent, but incorrect outputs. An AI crop advisory that confidently recommends the wrong pesticide at scale causes real harm.

**Design for the language the user actually speaks, not a national lingua franca.**
The 75% native-language preference finding [3] is a practical design requirement. Users who interact in a language they are not fluent in describe their problems less precisely, receive advice they may misread, and abandon the system more quickly. Forcing Hindi on a Tamil-speaking farmer degrades input quality and reduces adoption.

**Treat announcement as the starting point, not the finish line.**
India has hundreds of AI pilots. The realistic question is: does this deployment reach the intended user at a cost they can absorb, in a language they speak, over infrastructure they actually have? Many pilots pass the first test and fail the second and third.

**Monitor performance separately per language.**
A multilingual model that performs well in Hindi may perform significantly worse in a low-resource language like Santali [3]. Aggregate benchmarks hide these gaps. Separate quality evaluations per language are essential before a system is deployed at scale.

## Key Takeaways

- AI is actively deployed in India in 2025 across healthcare (computer vision retinal screening, eSanjeevani telemedicine triage), agriculture (Kisan e-Mitra satellite monitoring and multilingual chatbots), and language access (BharatGen's 22-language LLM) [1][2][3].
- The **IndiaAI Mission** and **BharatGen** represent a deliberate national strategy to build AI infrastructure designed around India's linguistic and infrastructural reality rather than adapting English-first tools built elsewhere [3].
- **Vernacular NLP** is technically harder than English NLP because of data scarcity, script diversity, and code-mixing — and it is also more consequential, since 75% of Indian smartphone users prefer native-language digital interactions [3].
- The **digital divide** — gaps in connectivity, device access, literacy, and power — determines who actually benefits from AI deployments, not just who is targeted by them [1].
- In every domain covered here, AI acts as an assistant or triage layer, not as a final decision-maker; a doctor, extension officer, or human reviewer remains in the loop because AI systems can produce incorrect outputs.

## References

[1] World Economic Forum. "India's Healthcare AI Innovation." *WEF Stories*, April 2025. https://www.weforum.org/stories/2025/04/india-healthcare-ai-innovation/

[2] IndiaAI. "AI in Agriculture in 2025: Transforming Indian Farms for a Sustainable Future." *IndiaAI Portal*, 2025. https://indiaai.gov.in/article/ai-in-agriculture-in-2025-transforming-indian-farms-for-a-sustainable-future

[3] Net Zero India. "Vernacular AI Apps India 2025." *NetZeroIndia.org*, 2025. https://netzeroindia.org/vernacular-ai-apps-india-2025/

---
<!-- nav:bottom:start -->
Previous: [⬅ 10.3 — The Jagged Frontier](../10-3-the-jagged-frontier/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[10.5 — Capability vs Hype ➡](../10-5-capability-vs-hype/reading.md)
<!-- nav:bottom:end -->
