<!-- nav:top:start -->
[⬅ Previous: 3.8 — The jagged frontier](../../3-8-the-jagged-frontier-tasks-ai-is-superhuman-at-vs-tasks-where/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.10 — How to evaluate AI output across five task types ➡](../../../4-evaluating-ai-output/3-10-how-to-evaluate-ai-output-across-five-task-types-creative-fa/artifacts/reading.md)
<!-- nav:top:end -->

---

# Hallucination â€” What It Is and Why It Happens

## Overview

In topic 3.2 you were introduced to the idea that an LLM (Large Language Model) can produce output that sounds plausible but is false â€” this is called **hallucination**. This topic goes deeper: you will learn what hallucination actually looks like, why it is built into the way LLMs work, and what you can do to reduce its impact. Understanding hallucination is one of the most practically important things you can know before using any AI tool on real work.

## Key Concepts

### Three Types of Hallucination

Not all hallucinations are the same. Three distinct types appear in practice, and each requires a different kind of check [2][3]:

| Type | What it means | Quick example |
|---|---|---|
| **Factual hallucination** | The model states a fact that is simply wrong | "The Eiffel Tower was built in 1901." (It was 1889.) |
| **Attributional hallucination** | The model correctly describes something but credits the wrong source | "Case Smith v. Jones, 2019, ruled that â€¦" â€” the case does not exist. |
| **Faithful-but-wrong hallucination** | The model follows the logic of an incorrect premise and produces a coherent but wrong conclusion | A user provides wrong project dates; the model calculates milestones that are internally consistent but wrong in the real world. |

All three types share one critical feature: the model's tone, phrasing, and punctuation look identical whether the content is accurate or fabricated. There is no obvious "tells you something is wrong" signal in the output itself.

### The Structural Mechanism â€” Why Hallucination Cannot Be Patched Away

To understand why hallucination is not a fixable bug, return to what you learned in topics 3.2 and 3.4. An LLM does one thing at its core: **given the tokens it has seen so far, it predicts the most plausible next token.** This process â€” autoregressive decoding â€” repeats token by token to build the full response.

Here is the critical point: **"most plausible" is not the same as "most true."**

The model has no internal fact-checking system. It has no database it queries before answering. It cannot distinguish between a statement it has seen many times in training data (and therefore assigns a high probability) and a statement that is objectively correct [1].

Consider a simple case. When the model sees "The capital of France is ___", the word "Paris" has an extremely high probability because that pattern appeared thousands of times in training data. The model produces "Paris" â€” and it is correct. But when someone asks "What did researcher X say in paper Y from 2023?", the model has no direct access to that paper. It generates a plausible-sounding answer by combining patterns from related text it has seen. If those patterns do not contain the exact truth, the model invents a plausible substitute â€” and delivers it with the same confident tone as the Paris answer.

A peer-reviewed analysis confirmed this formally: because LLMs are trained to optimise for text that resembles their training data, any model trained on a finite dataset will inevitably produce false statements for some inputs. Hallucination is not a failure of implementation; it is a consequence of the architecture [1]. Scale reduces hallucination frequency â€” it does not eliminate it [1].

![Hallucination Flow Diagram](./diagram.png)
*How token-by-token prediction leads to hallucination: the model optimises for plausibility, not truth, and grounding or RAG can intervene to reduce that gap.*

### Contributing Cause 1 â€” Training Data Gaps

**Training data** is the large collection of text the model learned from during pre-training. Three problems arise from that data [2]:

- **Gap.** The training set does not contain everything. Events after the training cut-off date, obscure local facts, and niche technical details are under-represented or absent. When a user asks about a gap, the model has no true answer â€” but it generates one anyway, drawn from related patterns.
- **Skew.** Popular misconceptions that circulate widely online can be over-represented relative to the actual truth. The model may assign a high probability to the wrong answer precisely because many people wrote it down.
- **No provenance tracking.** **Provenance** â€” the record of where a piece of information came from â€” is something LLMs do not store. A claim from a peer-reviewed paper and a claim from a random blog post may have received exactly the same weight during training. The model cannot tell you where a fact came from, because it never stored that connection.

### Contributing Cause 2 â€” RLHF and Overconfidence Bias

**RLHF (Reinforcement Learning from Human Feedback)** is a technique where human raters score model outputs and the model is updated to produce higher-rated responses. It is widely used to make LLMs more helpful and polite.

But RLHF creates a subtle pressure toward hallucination [2]:

1. Human raters often prefer responses that sound confident and complete.
2. A response that says "I am not certain, but the answer might be X" is frequently rated lower than one that says "The answer is X" â€” even when X is wrong.
3. Over many training rounds, the model learns that confident-sounding output earns better ratings.

The result is **overconfidence bias** â€” the model's expressed certainty does not match the reliability of its output [2]. Confidence becomes a stylistic feature, not a signal of accuracy. This matters because it means the model will state a hallucinated fact with exactly the same assured tone as a correct one.

### Mitigation Strategies

Hallucination cannot be eliminated, but three strategies reduce its impact [2]:

| Strategy | What you do | Limitation |
|---|---|---|
| **Verification** | Check every factual claim independently against a reliable source | Time-intensive; you must know where to look |
| **Grounding** | Paste verified source documents into the prompt so the model works from known text | Only helps for content the documents cover |
| **RAG (Retrieval-Augmented Generation)** | A system automatically retrieves verified documents before generating | Requires technical setup; covered in a later topic |
| **Calibration signals** | Use systems that flag uncertainty explicitly | Not all systems provide these; topic 3.8 covers calibration |

**Grounding** means tying the model's output to specific documents you provide â€” instead of asking "What does the research say about X?", you paste the actual research text into the prompt and ask the model to answer from that text only. **RAG** is a technical architecture that automates this process; you will encounter it in a later topic.

## Worked Example

**Scenario:** A student asks an AI assistant for a citation to include in a psychology paper.

**Prompt:** "Give me a published academic paper on cognitive load theory from 2022. Include the full citation â€” title, authors, journal, and year."

**AI response:** "Here is a relevant paper: *Cognitive Load and Working Memory in Digital Learning Environments* by Sweller, J. & Kalyuga, S. (2022). *Journal of Educational Psychology*, 114(3), 412â€“428."

The response looks exactly like a real citation. The author names are real researchers in this field. The journal is real. The year, volume, and page numbers are formatted correctly.

**The student submits it.** Their professor attempts to locate the paper. It does not exist. The volume, issue, and pages do not correspond to any real article. The authors are real, but they did not write this paper.

**Why did this happen?**

1. The model had seen many thousands of psychology citations in its training data. It learned that a citation matching the pattern *[Author], [Year], [Journal], [Volume]* is "plausible text" in this context.
2. It had no access to a journal database. It generated token by token, picking the most plausible continuation at each step â€” a real-sounding author name, a real journal name, plausible numbers.
3. RLHF trained the model to provide complete, confident answers. Saying "I cannot verify that this paper exists" would likely have been rated lower by human raters than providing a well-formatted citation.
4. The model had no provenance record. It could not flag that this specific combination of author, title, and journal was never actually in its training data â€” it simply combined familiar patterns into a new, plausible-looking whole.

The student would not have known anything was wrong without independently verifying the source. The format of a hallucinated citation is indistinguishable from the format of a real one.

## In Practice

### A Five-Step Hallucination Check

Use this process whenever an AI provides a factual claim that matters [2]:

1. **Request a specific, verifiable claim.** Ask the AI for a fact, citation, statistic, or name. Specific, narrow claims are easier to check than broad summaries.
2. **Record the claim exactly.** Copy the AI's output verbatim â€” the title, author name, date, or statistic. You want to check what the AI actually said, not your paraphrase of it.
3. **Search for the source independently.** Use a search engine, library database, or official record. Do not ask the AI to verify its own output â€” a model that hallucinated a claim will typically affirm it when asked to double-check.
4. **Compare the AI claim to what you found.** Four outcomes are possible:
   - Source exists and matches â€” no hallucination detected here.
   - Source exists but the claim is wrong (wrong date, wrong author) â€” attributional or factual hallucination.
   - Source does not exist at all â€” fabrication hallucination.
   - Source cannot be found â€” treat as suspected hallucination; flag for review.
5. **Document your finding.** Record what the AI said, what you found, and the discrepancy. This turns checking into a repeatable habit.

### Do and Don't

**Do:**
- Treat every AI-generated factual claim as unverified until you have checked it independently.
- Use grounding â€” paste source documents into the prompt â€” when accuracy matters and you have access to reliable sources.
- Check citations character by character: exact title, exact author spelling, year, journal name.

**Do not:**
- Ask the AI to verify its own output. A model that hallucinated a claim will typically affirm it when asked to double-check [2].
- Assume that confident tone equals accurate content. Confidence is a trained style, not a reliability signal [2].
- Assume that larger or newer models do not hallucinate. Scale reduces frequency; it does not eliminate hallucination [1].
- Use AI-generated citations in any formal document without independent verification [3].

## Key Takeaways

- **Hallucination is structural, not incidental.** Because LLMs predict the most plausible next token rather than the most true statement, generating false content is a built-in property of the architecture â€” not a bug that can be patched [1].
- **Three distinct types exist, each requiring its own check.** Factual hallucination (wrong facts), attributional hallucination (right content, wrong source), and faithful-but-wrong hallucination (coherent but built on a bad premise) can each appear in the same response [2][3].
- **Training data gaps and RLHF overconfidence bias amplify the problem.** Under-represented facts get fabricated; confident-sounding output gets rewarded by raters, training models to overstate certainty [2].
- **Mitigation is possible but requires discipline.** Verification, grounding, and retrieval-augmented generation reduce risk; no current technique eliminates hallucination entirely [2].
- **Format is not a reliability signal.** Hallucinated output looks identical to correct output â€” a fabricated citation is formatted exactly like a real one. Always verify independently before using AI-generated facts in consequential work [3].

## References

[1] Huang, L., et al. (2024). "A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions." *arXiv*. https://arxiv.org/abs/2401.11817

[2] Lakera. "A Guide to Hallucinations in Large Language Models." https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models

[3] MorphLLM. "AI Hallucination Examples." https://www.morphllm.com/ai-hallucination-examples

---
<!-- nav:bottom:start -->
[⬅ Previous: 3.8 — The jagged frontier](../../3-8-the-jagged-frontier-tasks-ai-is-superhuman-at-vs-tasks-where/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.10 — How to evaluate AI output across five task types ➡](../../../4-evaluating-ai-output/3-10-how-to-evaluate-ai-output-across-five-task-types-creative-fa/artifacts/reading.md)
<!-- nav:bottom:end -->
