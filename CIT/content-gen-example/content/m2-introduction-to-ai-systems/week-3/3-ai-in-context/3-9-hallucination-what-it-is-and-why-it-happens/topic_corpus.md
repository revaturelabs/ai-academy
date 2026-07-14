---
topic_id: "3.9"
title: "Hallucination — what it is and why it happens"
position_in_module: 3
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Hallucination — what it is and why it happens — Topic Corpus

## 2. Prerequisites

This topic deepens a concept first introduced in topic 3.2 ("Large Language Models and how they work"), where hallucination was named and briefly described as output that sounds plausible but is false. Topics 3.4 ("Tokens and tokenisation") and 3.6 ("Temperature and sampling") supply the mechanistic vocabulary — token, autoregressive decoding, probability distribution, temperature — used freely here without re-definition.

Relevant prior topics:
- **3.2** — LLM, hallucination (named), prompt, context window, Transformer, pre-training
- **3.4** — token, tokenisation, autoregressive decoding
- **3.6** — temperature, probability distribution over tokens, greedy decoding, sampling, logits, deterministic/stochastic output

## 3. Learning Objectives

By the end of this topic you will be able to:

1. **Define** three distinct types of AI hallucination — factual, attributional, and faithful-but-wrong — and give a concrete example of each.
2. **Explain** why the token-prediction mechanism makes hallucination a structural property of LLMs, not a bug that can be patched away [1].
3. **Describe** two contributing causes — training data gaps and RLHF incentives — that make hallucination more likely in practice [2].
4. **Identify** real-world contexts — legal, medical, academic — where hallucination has caused documented harm [3].
5. **List** three detection and mitigation strategies (verification, grounding, and retrieval-augmented generation) that reduce hallucination risk without eliminating it [2].

## 4. Introduction

Imagine you ask a knowledgeable colleague to summarise a legal case. They do so with complete confidence — dates, names, case numbers, all delivered without hesitation. Later you discover that half the citations they gave you do not exist. The cases are invented. Your colleague did not lie deliberately; they simply could not distinguish between what they remembered accurately and what they filled in from pattern.

That is, roughly, what an LLM (Large Language Model) can do. In topic 3.2 you learned that hallucination is when a model produces output that sounds plausible but is false. This topic explains **what hallucination actually is**, what forms it takes, and — most importantly — **why it happens at a structural level** so deep that it cannot be fixed by making the model bigger or smarter [1].

This matters right now because the Specification Portfolio (Assessment A1) requires you to think carefully about what AI can and cannot reliably do. Hallucination is the single most practically dangerous gap between user expectation ("AI tells me facts") and system reality ("AI generates plausible text"). Understanding it clearly is a prerequisite for using any AI tool responsibly.

## 5. Core Concepts

### 5.1 What hallucination is

**Hallucination** — in the context of AI, a model output that is factually wrong, fabricated, or misleading, but is stated with the same fluent confidence as correct output [1][2].

The word comes from the medical sense: perceiving something that is not there. An AI hallucination is similar — the model generates content as if it is grounded in real information, when in fact it has no real information to ground it.

Three distinct types exist [2][3]:

| Type | What it means | Quick example |
|---|---|---|
| **Factual hallucination** | The model states a fact that is simply wrong | "The Eiffel Tower was built in 1901." (It was 1889.) |
| **Attributional hallucination** | The model correctly describes something but credits the wrong source | "Case Smith v. Jones, 2019, ruled that ..." — the case does not exist. |
| **Faithful-but-wrong hallucination** | The model follows the logic of an incorrect premise and produces a coherent but wrong conclusion | A user gives wrong dates; the model calculates deadlines that are internally consistent but wrong in the real world. |

All three types share one feature: the model does not signal that something is wrong. The output tone, punctuation, and phrasing look identical whether the content is accurate or fabricated.

### 5.2 The structural mechanism — why hallucination is inevitable

To understand why hallucination is not a fixable bug, return to what you learned in topics 3.2 and 3.4.

An LLM does one thing at its core: **given the tokens it has seen so far, it predicts the most plausible next token.** This process — autoregressive decoding — repeats token by token to build the full response.

Here is the critical point: **"most plausible" is not the same as "most true."** The model has no internal fact-checking system. It has no database it queries. It has no way to distinguish between a statement it has seen many times in training data (and therefore assigns a high probability) and a statement that is objectively correct [1].

Think of it this way. When you read the phrase "The capital of France is ___", the word "Paris" has an extremely high probability because it appeared after similar phrases thousands of times in training data. The model produces "Paris" — and it is correct. But when someone asks "What did researcher X say in paper Y from 2023?", the model has no direct access to that paper. It generates a plausible-sounding answer by combining patterns from related text it has seen. If those patterns do not contain the exact truth, the model invents a plausible substitute — and delivers it with the same confident tone as the Paris answer.

A peer-reviewed analysis established this formally: because LLMs are trained to optimise for text that resembles their training data, any model trained on a finite dataset will inevitably produce false statements about some inputs. Hallucination is not a failure of implementation; it is a consequence of the architecture [1].

The key distinction, in plain terms:

- **What the model optimises for:** text that looks like correct, fluent output.
- **What the model does NOT optimise for:** factual truth checked against the real world.

No amount of making the model larger changes this fundamental trade-off. Scale reduces hallucination frequency; it does not eliminate it [1].

### 5.3 Contributing cause 1 — training data gaps and skew

**Training data** is the large collection of text the model learned from during pre-training (a term you met in topic 3.2). Three problems arise from that data [2]:

**Gap.** The training set does not contain everything. Events after the training cut-off date, obscure local facts, niche technical details, and minority-language content are under-represented or absent. When a user asks about a gap, the model has no true answer — but it generates one anyway, drawn from related patterns.

**Skew.** Some facts appear far more often in text than others. Popular misconceptions that circulate widely online can be over-represented relative to the actual truth. The model may assign a high probability to the wrong answer precisely because many people wrote it down.

**No provenance tracking.** The model does not store a link between a fact and its source. A claim from a peer-reviewed paper and a claim from a random blog post may have received exactly the same weight during training. The model cannot tell you where a piece of information came from, because it never stored that connection.

**Provenance** — the record of where a piece of information came from. LLMs have none; they blend all training text into shared parameters.

### 5.4 Contributing cause 2 — RLHF and overconfident output

You learned in topic 3.1 that models can be trained with human feedback. **RLHF (Reinforcement Learning from Human Feedback)** — a technique where human raters score model outputs and the model is updated to produce higher-rated responses — is widely used to make LLMs more helpful and polite.

But RLHF creates a subtle pressure toward hallucination [2]:

- Human raters often prefer responses that sound confident and complete.
- A response that says "I am not certain, but the answer might be X" is frequently rated lower than one that says "The answer is X" — even when X is wrong.
- Over many training rounds, the model learns that confident-sounding output gets rewarded.

The result: RLHF can inadvertently train a model to express more certainty than it actually has. Confidence becomes a stylistic feature the model produces to earn better ratings — not a signal of actual accuracy.

This is called **overconfidence bias** — the model's expressed certainty does not match the reliability of its output [2].

### 5.5 Detection and mitigation strategies

Hallucination cannot be eliminated, but its impact can be reduced. Three strategies reduce the risk [2]:

**Verification (external fact-checking)**
Treat AI output as a draft, not a final answer. Every factual claim — especially any citation, statistic, name, or date — must be checked against a reliable independent source before it is used or shared. This is the most basic and universally applicable mitigation.

**Grounding**
Grounding means tying the model's output to a specific set of verified documents you provide alongside the prompt. Instead of asking "What does the research say about X?", you paste the actual research text into the prompt and ask the model to answer from that text only. The model then works from a known source, not from memory. Grounding does not eliminate hallucination, but it significantly reduces it for the content covered by the provided documents.

**Retrieval-augmented generation (RAG)**
RAG is a technical architecture where an AI system automatically retrieves relevant documents from a verified knowledge base before generating a response. The generation is then grounded in current, checked information rather than training memory alone. RAG is covered in a later topic. For now, note that it is a systematic, automated form of grounding designed to reduce hallucination for factual queries.

**Confidence calibration signals**
Some systems surface uncertainty — producing phrases like "I am not confident in this" or flagging low-confidence claims. You encountered calibration in topic 3.8 as the alignment between a model's expressed certainty and its actual accuracy. A well-calibrated model matches expressed certainty to actual reliability. An over-confident model — one RLHF may inadvertently produce — is more dangerous precisely because it sounds authoritative even when it is wrong.

Summary of strategies:

| Strategy | What you do | Limitation |
|---|---|---|
| Verification | Check every factual claim independently | Time-intensive; requires knowing where to look |
| Grounding | Paste source documents into the prompt | Only works for content the documents cover |
| RAG (covered later) | Use a system that auto-retrieves verified docs | Requires technical setup; does not cover all domains |
| Calibration signals | Use systems that flag uncertainty | Not all systems provide these |

## 6. Implementation — a repeatable hallucination check

The following is a five-step process for checking whether a specific AI output contains a hallucination. This maps directly to the hands-on exercise in section 9.

1. **Request a specific, verifiable claim.** Ask the AI to state a fact, cite a source, or name a piece of research. Specific, narrow claims are easier to check than broad summaries.

2. **Record the claim exactly.** Copy the AI's output verbatim — the title, author name, date, quote, or statistic. You want to check what the AI actually said, not your paraphrase of it.

3. **Search for the source independently.** Use a search engine, a library database, or an official record. Do not ask the AI to verify its own output — a model that hallucinated a claim will typically affirm it when asked to double-check.

4. **Compare the AI claim to the found source.** Four outcomes are possible:
   - Source exists and the claim matches — no hallucination detected here.
   - Source exists but the claim is wrong (wrong date, wrong author, wrong quote) — attributional or factual hallucination.
   - Source does not exist at all — fabrication hallucination.
   - Source cannot be found — treat as suspected hallucination; flag for expert review.

5. **Document your finding.** Record what the AI said, what you found (or did not find), and the discrepancy. This habit turns checking into a repeatable skill.

## 7. Real-World Patterns

### Legal citations — fabricated cases in court filings

In documented cases, lawyers submitted court filings containing citations to cases that do not exist. The citations had been generated by an AI. Each fabricated case had a plausible name, a real-sounding court, a docket number, and invented quotations from judges. The filings were discovered only because opposing counsel attempted to locate the cases and found none of them [3].

Why it happened: the AI assigned high probability to text that looks like a legal citation, because legal citations appear frequently in training data. It had no mechanism to check whether those specific cases existed.

Why it matters: court filings are formal legal documents. A lawyer who submits a fabricated citation faces professional sanctions. The downstream cost of a single hallucination in this context is severe.

### Medical AI — fabricated statistics

AI-generated medical summaries have been found to contain fabricated statistics about treatment efficacy, incorrect drug interactions, and invented study results. In one class of documented errors, models stated specific numerical outcomes ("Drug X reduces risk by 34%") that appeared in no published research — the number was plausible given the surrounding text but sourced from nothing real [3].

Why it matters: a clinician or patient acting on a fabricated statistic may make harmful decisions. The output style — clinical, numbered, confident — actively discourages scepticism.

### Academic references — invented papers

Researchers testing LLMs for literature review tasks have found that models routinely produce citations to papers that do not exist. The invented papers have realistic-sounding titles, real author names (though misattributed), real journal names (though mismatched), and plausible publication years. A student who does not independently verify each reference may inadvertently include fabricated sources in their own work [3].

Why it is hard to catch: hallucinated references look identical to real ones. Format alone is not a signal of truth.

## 8. Best Practices

**Do:**
- Treat every AI-generated factual claim as unverified until you have independently checked it.
- Use grounding — paste source documents into the prompt — when accuracy matters and you have access to reliable sources.
- Check citations character by character: exact title, exact author spelling, year, journal name.
- Flag uncertainty explicitly when sharing AI-assisted work with others ("These claims were not independently verified").

**Do not:**
- Ask the AI to verify its own output. A model that hallucinated a claim will typically affirm it when asked to double-check.
- Assume that confident tone equals accurate content. Confidence is a stylistic output, not a reliability signal.
- Assume that larger or newer models do not hallucinate. Scale reduces hallucination frequency; it does not eliminate it [1].
- Use AI-generated citations in any formal document without independent verification.

| Common misconception | Reality |
|---|---|
| "If the AI sounds confident, it must be right." | Confidence is a trained style, not a reliability signal [2]. |
| "Bigger models don't hallucinate." | Larger models hallucinate less frequently, but all models hallucinate [1]. |
| "The AI will tell me when it is guessing." | By default, most models do not flag uncertainty unless specifically designed to. |
| "If I ask the AI to check itself, it will catch errors." | Models are poor at detecting their own hallucinations. |

## 9. Hands-On Exercise

**Exercise: Hunt for a hallucination**

This exercise maps to the week 3 lab. You will need access to any publicly available AI assistant and a search engine or library database.

1. Ask the AI assistant to provide a specific, verifiable citation. A good prompt: "Name a published academic paper on [any topic you find interesting] from 2022 or 2023. Give me the full citation — title, authors, journal, and year."

2. Record the exact citation the AI provides.

3. Use Google Scholar, a library search tool, or a journal website to look up the cited paper. Search first by title; then try author name plus year if the title returns nothing.

4. Record what you find:
   - Does the paper exist?
   - Are the authors correct?
   - Is the journal real?
   - Does the year match?
   - Does the abstract match what the AI claimed the paper was about?

5. Write two to three sentences summarising your finding. If the paper exists and is accurate, repeat with a more obscure topic — hallucination is more frequent when training data coverage is thin.

Expected outcome: you will find at least one discrepancy in three to five attempts. Reflect on how you would have known something was wrong without checking.

## 10. Key Takeaways

- **Hallucination is structural, not incidental.** Because LLMs predict the most plausible next token rather than the most true statement, generating false content is a built-in property of the architecture — not a bug that can be patched [1].
- **Three types exist, each requiring a different check.** Factual hallucination (wrong facts), attributional hallucination (right content, wrong source), and faithful-but-wrong hallucination (coherent but built on a bad premise) can each appear in the same response [2][3].
- **Training data gaps and RLHF incentives amplify the problem.** Under-represented facts get fabricated; confident-sounding output gets rewarded by raters, training models to overstate certainty [2].
- **High-stakes domains — legal, medical, academic — have documented real-world harm.** The common thread: hallucinated output looks identical to correct output, so format is not a reliability signal [3].
- **Mitigation is possible but requires discipline.** Verification, grounding, and retrieval-augmented generation (covered in a later topic) reduce risk; no current technique eliminates it [2].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
