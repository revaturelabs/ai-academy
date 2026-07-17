#!/usr/bin/env python3
"""
Generate the Cresent 'view' pages for the AI content shared with CIT.

SINGLE SOURCE OF TRUTH: the CIT readings under CIT/content-gen-example/content/.
This script never copies content by hand — it reads each mapped CIT reading,
strips CIT's own nav block, wraps the body in Cresent Prev/TOC/Next navigation,
and writes a GENERATED reading.md into the matching scaffolded Cresent topic
folder. It also regenerates the "Part B" section of the Cresent README between
the <!-- part-b:start --> / <!-- part-b:end --> markers.

To change shared content: edit the CIT reading, then re-run this script.
Never hand-edit the generated Cresent reading.md files.

    python Cresent/Technical/tools/generate_shared_readings.py

The whole mapping (Cresent topic -> CIT reading ids) lives ONLY in this file.
"""
from __future__ import annotations

import os
import re
import sys

# ---------------------------------------------------------------------------
# Path anchors. This file lives at Cresent/Technical/tools/ ; repo root is 3 up.
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
CIT_CONTENT = os.path.join(REPO_ROOT, "CIT", "content-gen-example", "content")
CRESENT_TECH = os.path.join(REPO_ROOT, "Cresent", "Technical")
CRESENT_CONTENT = os.path.join(CRESENT_TECH, "content", "ai_native_engineering_foundations")
README = os.path.join(CRESENT_TECH, "README.md")

# ---------------------------------------------------------------------------
# CIT reading id -> path (relative to CIT_CONTENT). The single source files.
# ---------------------------------------------------------------------------
CIT = {
    # M1 — Computational Thinking
    "1.1": "m1-computational-thinking/week-1/1-understanding-computation/1-1-what-is-computation/artifacts/reading.md",
    "1.2": "m1-computational-thinking/week-1/1-understanding-computation/1-2-deterministic-systems-same-input-always-gives-the-same-outpu/artifacts/reading.md",
    "1.3": "m1-computational-thinking/week-1/1-understanding-computation/1-3-probabilistic-systems-same-input-can-give-different-outputs/artifacts/reading.md",
    "1.4": "m1-computational-thinking/week-1/1-understanding-computation/1-4-why-ai-gives-different-answers-to-the-same-question/artifacts/reading.md",
    "1.5": "m1-computational-thinking/week-1/2-problem-solving-foundations/1-5-decomposition-breaking-a-big-problem-into-smaller-solvable-p/artifacts/reading.md",
    "1.6": "m1-computational-thinking/week-1/2-problem-solving-foundations/1-6-abstraction-hiding-complexity-at-the-right-level/artifacts/reading.md",
    "1.7": "m1-computational-thinking/week-1/3-expressing-logic/1-7-pseudocode-writing-logic-in-plain-english-before-writing-cod/artifacts/reading.md",
    "1.8": "m1-computational-thinking/week-1/3-expressing-logic/1-8-flowcharts-visualising-logic-with-standard-shapes-and-arrows/artifacts/reading.md",
    "1.9": "m1-computational-thinking/week-1/4-algorithmic-thinking/1-9-algorithmic-thinking-what-makes-a-set-of-steps-an-algorithm/artifacts/reading.md",
    "1.10": "m1-computational-thinking/week-1/4-algorithmic-thinking/1-10-algorithms-in-everyday-life-recipes-gps-routes-sorting-queue/artifacts/reading.md",
    "1.11": "m1-computational-thinking/week-1/4-algorithmic-thinking/1-11-the-four-properties-of-a-good-algorithm-finite-definite-inpu/artifacts/reading.md",
    "1.12": "m1-computational-thinking/week-1/5-applying-it-to-your-domain/1-12-choosing-your-domain-writing-a-3-sentence-problem-statement/artifacts/reading.md",
    "2.1": "m1-computational-thinking/week-2/1-what-makes-a-good-specification/2-1-what-makes-a-good-specification-testable-bounded-observable/artifacts/reading.md",
    "2.2": "m1-computational-thinking/week-2/1-what-makes-a-good-specification/2-2-bad-spec-vs-good-spec-make-it-better-vs-rewrite-at-grade-8-l/artifacts/reading.md",
    "2.3": "m1-computational-thinking/week-2/1-what-makes-a-good-specification/2-3-how-to-identify-the-inputs-expected-outputs-and-failure-cond/artifacts/reading.md",
    "2.4": "m1-computational-thinking/week-2/2-how-machines-recognise-patterns/2-4-pattern-recognition-how-machines-find-rules-in-repeated-data/artifacts/reading.md",
    "2.5": "m1-computational-thinking/week-2/3-the-professional-rules-of-ai-use/2-5-the-70-30-rule-ai-implements-you-specify-and-verify/artifacts/reading.md",
    "2.6": "m1-computational-thinking/week-2/3-the-professional-rules-of-ai-use/2-6-when-not-to-use-ai-privacy-precision-legal-accountability/artifacts/reading.md",
    "2.7": "m1-computational-thinking/week-2/4-writing-and-testing-specifications/2-7-writing-specifications-across-five-domains-health-transport/artifacts/reading.md",
    "2.8": "m1-computational-thinking/week-2/4-writing-and-testing-specifications/2-8-testing-a-specification-how-to-verify-the-ai-did-exactly-wha/artifacts/reading.md",
    "2.9": "m1-computational-thinking/week-2/4-writing-and-testing-specifications/2-9-iterating-a-specification-based-on-output-gaps/artifacts/reading.md",
    # M2 — Introduction to AI Systems
    "3.1": "m2-introduction-to-ai-systems/week-3/1-a-brief-history-of-ai/3-1-history-of-ai-symbolic-ai-to-machine-learning-to-deep-learni/artifacts/reading.md",
    "3.2": "m2-introduction-to-ai-systems/week-3/1-a-brief-history-of-ai/3-2-the-rise-of-large-language-models-llms/artifacts/reading.md",
    "3.3": "m2-introduction-to-ai-systems/week-3/1-a-brief-history-of-ai/3-3-the-move-to-ai-agents/artifacts/reading.md",
    "3.4": "m2-introduction-to-ai-systems/week-3/2-how-llms-work/3-4-how-llms-work-tokens-training-and-inference/artifacts/reading.md",
    "3.5": "m2-introduction-to-ai-systems/week-3/2-how-llms-work/3-5-what-parameters-are-and-why-they-matter/artifacts/reading.md",
    "3.6": "m2-introduction-to-ai-systems/week-3/2-how-llms-work/3-6-temperature-and-sampling-why-the-same-question-gives-differe/artifacts/reading.md",
    "3.7": "m2-introduction-to-ai-systems/week-3/3-ai-in-context/3-7-ai-in-india-today-healthcare-agriculture-vernacular-translat/artifacts/reading.md",
    "3.8": "m2-introduction-to-ai-systems/week-3/3-ai-in-context/3-8-the-jagged-frontier-tasks-ai-is-superhuman-at-vs-tasks-where/artifacts/reading.md",
    "3.9": "m2-introduction-to-ai-systems/week-3/3-ai-in-context/3-9-hallucination-what-it-is-and-why-it-happens/artifacts/reading.md",
    "3.10": "m2-introduction-to-ai-systems/week-3/4-evaluating-ai-output/3-10-how-to-evaluate-ai-output-across-five-task-types-creative-fa/artifacts/reading.md",
    "4.1": "m2-introduction-to-ai-systems/week-4/1-foundation-models-and-adaptation/4-1-foundation-models-trained-once-at-scale-usable-for-many-task/artifacts/reading.md",
    "4.2": "m2-introduction-to-ai-systems/week-4/1-foundation-models-and-adaptation/4-2-fine-tuning-adapting-a-foundation-model-on-domain-specific-d/artifacts/reading.md",
    "4.3": "m2-introduction-to-ai-systems/week-4/2-retrieval-agents-and-tools/4-3-retrieval-augmented-generation-rag-giving-ai-access-to-exter/artifacts/reading.md",
    "4.4": "m2-introduction-to-ai-systems/week-4/2-retrieval-agents-and-tools/4-4-agents-llm-plus-memory-tools-and-a-planning-loop-conceptual/artifacts/reading.md",
    "4.5": "m2-introduction-to-ai-systems/week-4/2-retrieval-agents-and-tools/4-5-tool-use-ai-calling-search-calculator-and-code-runner/artifacts/reading.md",
    "4.6": "m2-introduction-to-ai-systems/week-4/3-multimodal-ai/4-6-multimodal-ai-working-with-text-image-audio-and-video-in-one/artifacts/reading.md",
    "4.7": "m2-introduction-to-ai-systems/week-4/4-comparing-and-evaluating-ai-tools/4-7-how-to-compare-two-ai-tools-designing-a-measurable-evaluatio/artifacts/reading.md",
    "4.8": "m2-introduction-to-ai-systems/week-4/4-comparing-and-evaluating-ai-tools/4-8-presenting-a-findings-based-recommendation-evidence-not-opin/artifacts/reading.md",
    "5.1": "m2-introduction-to-ai-systems/week-5/1-ai-failures-and-why-they-happen/5-1-real-ai-failure-cases-healthcare-misdiagnosis-hiring-bias-de/artifacts/reading.md",
    "5.2": "m2-introduction-to-ai-systems/week-5/1-ai-failures-and-why-they-happen/5-2-hallucination-why-ai-states-falsehoods-confidently/artifacts/reading.md",
    "5.3": "m2-introduction-to-ai-systems/week-5/1-ai-failures-and-why-they-happen/5-3-data-bias-how-biased-training-data-produces-biased-model-out/artifacts/reading.md",
    "5.4": "m2-introduction-to-ai-systems/week-5/2-ethical-principles/5-4-the-four-pillars-fairness-transparency-accountability-harm-p/artifacts/reading.md",
    "5.5": "m2-introduction-to-ai-systems/week-5/3-safety-practices/5-5-red-teaming-systematically-testing-your-own-system-for-failu/artifacts/reading.md",
    "5.6": "m2-introduction-to-ai-systems/week-5/3-safety-practices/5-6-prompt-injection-how-attackers-manipulate-ai-through-crafted/artifacts/reading.md",
    "5.7": "m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-7-eu-ai-act-risk-tiers-unacceptable-high-limited-minimal-risk/artifacts/reading.md",
    "5.8": "m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-8-eu-ai-act-obligations-for-high-risk-systems-documentation-te/artifacts/reading.md",
    "5.9": "m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-9-eu-ai-act-prohibited-uses-including-social-scoring-and-real/artifacts/reading.md",
    "5.10": "m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-10-nist-ai-risk-management-framework-four-functions-govern-map/artifacts/reading.md",
    "5.11": "m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-11-white-house-executive-order-on-ai-2023-key-provisions/artifacts/reading.md",
    "5.12": "m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-12-india-ai-governance-meity-advisory-guidelines/artifacts/reading.md",
    "5.13": "m2-introduction-to-ai-systems/week-5/4-governance-frameworks/5-13-knowing-which-governance-framework-applies-to-your-system/artifacts/reading.md",
    # M3 — Applied Maths (only the two probability topics Cresent folds into m2)
    "7.4": "m3-applied-maths-for-ai/week-7/2-how-llms-use-probability/7-4-why-llms-output-a-probability-distribution-not-a-single-fixe/artifacts/reading.md",
    "7.5": "m3-applied-maths-for-ai/week-7/2-how-llms-use-probability/7-5-temperature-low-picks-the-most-likely-token-high-introduces/artifacts/reading.md",
    # M5 — Prompt Engineering (only the prompting-basics topics Cresent folds into m2)
    "13.1": "m5-python-for-ai-pe-vc-and-rag/week-13/1-prompt-engineering-fundamentals/13-1-system-prompt-vs-user-prompt-context-setting-vs-the-live-req/artifacts/reading.md",
    "13.2": "m5-python-for-ai-pe-vc-and-rag/week-13/1-prompt-engineering-fundamentals/13-2-role-assignment-telling-the-model-who-it-is/artifacts/reading.md",
    "13.5": "m5-python-for-ai-pe-vc-and-rag/week-13/1-prompt-engineering-fundamentals/13-5-constraints-telling-ai-what-not-to-do/artifacts/reading.md",
    # M4 — Human Cognition and AI Oversight
    "9.1": "m4-human-cognition-and-ai-oversight/week-9/1-how-humans-think/9-1-system-1-thinking-fast-instinctive-automatic/artifacts/reading.md",
    "9.2": "m4-human-cognition-and-ai-oversight/week-9/1-how-humans-think/9-2-system-2-thinking-slow-deliberate-effortful/artifacts/reading.md",
    "9.3": "m4-human-cognition-and-ai-oversight/week-9/2-cognitive-biases-and-ai/9-3-confirmation-bias-seeking-information-that-confirms-existing/artifacts/reading.md",
    "9.4": "m4-human-cognition-and-ai-oversight/week-9/2-cognitive-biases-and-ai/9-4-anchoring-bias-over-relying-on-the-first-piece-of-informatio/artifacts/reading.md",
    "9.5": "m4-human-cognition-and-ai-oversight/week-9/2-cognitive-biases-and-ai/9-5-automation-bias-trusting-automated-systems-over-human-judgme/artifacts/reading.md",
    "9.6": "m4-human-cognition-and-ai-oversight/week-9/2-cognitive-biases-and-ai/9-6-how-human-biases-get-encoded-into-ai-training-data/artifacts/reading.md",
    "9.7": "m4-human-cognition-and-ai-oversight/week-9/3-the-judgment-framework/9-7-the-judgment-framework-q1-what-is-the-cost-of-this-being-wro/artifacts/reading.md",
    "9.8": "m4-human-cognition-and-ai-oversight/week-9/3-the-judgment-framework/9-8-the-judgment-framework-q2-can-i-verify-this-without-the-ai/artifacts/reading.md",
    "9.9": "m4-human-cognition-and-ai-oversight/week-9/3-the-judgment-framework/9-9-the-judgment-framework-q3-who-is-accountable-if-this-fails/artifacts/reading.md",
    "9.10": "m4-human-cognition-and-ai-oversight/week-9/4-defining-safe-boundaries/9-10-acceptable-error-defining-the-failure-threshold-tolerable-fo/artifacts/reading.md",
    "9.11": "m4-human-cognition-and-ai-oversight/week-9/4-defining-safe-boundaries/9-11-high-stakes-domains-where-ai-must-not-have-the-final-word-me/artifacts/reading.md",
    "10.1": "m4-human-cognition-and-ai-oversight/week-10/1-case-studies/10-1-case-study-ai-in-college-admissions-where-was-the-human-over/artifacts/reading.md",
    "10.2": "m4-human-cognition-and-ai-oversight/week-10/1-case-studies/10-2-case-study-automated-medical-triage-what-failure-mode-was-to/artifacts/reading.md",
    "10.3": "m4-human-cognition-and-ai-oversight/week-10/1-case-studies/10-3-case-study-ai-loan-approval-at-scale-who-was-accountable/artifacts/reading.md",
    "10.4": "m4-human-cognition-and-ai-oversight/week-10/2-automation-complacency/10-4-automation-complacency-how-high-accuracy-makes-humans-less-v/artifacts/reading.md",
    "10.5": "m4-human-cognition-and-ai-oversight/week-10/3-designing-human-oversight/10-5-designing-human-in-the-loop-checkpoints-when-to-require-sign/artifacts/reading.md",
    "10.6": "m4-human-cognition-and-ai-oversight/week-10/3-designing-human-oversight/10-6-identifying-which-components-in-your-system-need-a-mandatory/artifacts/reading.md",
    "10.7": "m4-human-cognition-and-ai-oversight/week-10/4-post-mortem-writing/10-7-writing-a-post-mortem-what-failed-why-who-was-accountable-wh/artifacts/reading.md",
}

# ---------------------------------------------------------------------------
# Cresent curriculum (Part B), in delivery order. Each topic:
#   (cresent_id, title, cresent_folder_rel_to_CRESENT_CONTENT, [CIT ids])
# An empty CIT list => synthesis topic (a short stub page, no CIT body).
# ---------------------------------------------------------------------------
M1 = "m1-computational-thinking"
M2 = "m2-introduction-to-ai-systems"
M3 = "m3-human-cognition-ai-oversight"

TOPICS = [
    ("8.3", "What Is Computation", f"{M1}/week-8/1-computational-thinking-kickoff/8-3-what-is-computation", ["1.1", "1.2", "1.3"]),
    ("8.4", "Why AI Gives Different Answers", f"{M1}/week-8/1-computational-thinking-kickoff/8-4-why-ai-gives-different-answers", ["1.4"]),
    ("8.5", "Human vs Machine Problem-Solving", f"{M1}/week-8/1-computational-thinking-kickoff/8-5-human-vs-machine-problem-solving", ["1.9", "1.10", "1.11"]),
    ("9.1", "Core Computational Thinking Skills", f"{M1}/week-9/1-computational-thinking/9-1-core-computational-thinking-skills", ["1.5", "1.6", "2.4"]),
    ("9.2", "Expressing Logic", f"{M1}/week-9/1-computational-thinking/9-2-expressing-logic", ["1.7", "1.8"]),
    ("9.3", "Specifying for AI", f"{M1}/week-9/1-computational-thinking/9-3-specifying-for-ai", ["1.12", "2.1", "2.2", "2.3", "2.5", "2.6", "2.7", "2.8", "2.9"]),

    ("10.1", "History of AI", f"{M2}/week-10/1-what-ai-is-and-isnt/10-1-history-of-ai", ["3.1", "3.2", "3.3"]),
    ("10.2", "How LLMs Work", f"{M2}/week-10/1-what-ai-is-and-isnt/10-2-how-llms-work", ["3.4", "3.5"]),
    ("10.3", "The Jagged Frontier", f"{M2}/week-10/1-what-ai-is-and-isnt/10-3-the-jagged-frontier", ["3.8"]),
    ("10.4", "AI Today (Global and India)", f"{M2}/week-10/1-what-ai-is-and-isnt/10-4-ai-today-global-and-india", ["3.7"]),
    ("10.5", "Capability vs Hype", f"{M2}/week-10/1-what-ai-is-and-isnt/10-5-capability-vs-hype", ["3.10", "4.7", "4.8"]),
    ("11.1", "Foundation Models", f"{M2}/week-11/1-the-2026-ai-stack/11-1-foundation-models", ["4.1"]),
    ("11.2", "Fine-Tuning", f"{M2}/week-11/1-the-2026-ai-stack/11-2-fine-tuning", ["4.2"]),
    ("11.3", "RAG (Concept)", f"{M2}/week-11/1-the-2026-ai-stack/11-3-rag-concept", ["4.3"]),
    ("11.4", "Agents (Concept)", f"{M2}/week-11/1-the-2026-ai-stack/11-4-agents-concept", ["4.4"]),
    ("11.5", "Tool Use", f"{M2}/week-11/1-the-2026-ai-stack/11-5-tool-use", ["4.5"]),
    ("11.6", "Multimodal AI", f"{M2}/week-11/1-the-2026-ai-stack/11-6-multimodal-ai", ["4.6"]),
    ("12.1", "Why the Same Question Gives Different Answers", f"{M2}/week-12/1-how-llms-behave/12-1-why-the-same-question-gives-different-answers", ["3.6"]),
    ("12.2", "Temperature", f"{M2}/week-12/1-how-llms-behave/12-2-temperature", ["7.5"]),
    ("12.3", "Probability Distributions", f"{M2}/week-12/1-how-llms-behave/12-3-probability-distributions", ["7.4"]),
    ("12.4", "Hallucination", f"{M2}/week-12/1-how-llms-behave/12-4-hallucination", ["3.9", "5.2"]),
    ("12.5", "Context and Prompting Basics", f"{M2}/week-12/1-how-llms-behave/12-5-context-and-prompting-basics", ["13.1", "13.2", "13.5"]),
    ("13.1", "Real Failure Cases", f"{M2}/week-13/1-ethics-safety-governance/13-1-real-failure-cases", ["5.1"]),
    ("13.2", "Data Bias", f"{M2}/week-13/1-ethics-safety-governance/13-2-data-bias", ["5.3"]),
    ("13.3", "The Four Pillars", f"{M2}/week-13/1-ethics-safety-governance/13-3-the-four-pillars", ["5.4"]),
    ("13.4", "Red-Teaming", f"{M2}/week-13/1-ethics-safety-governance/13-4-red-teaming", ["5.5"]),
    ("13.5", "Prompt Injection", f"{M2}/week-13/1-ethics-safety-governance/13-5-prompt-injection", ["5.6"]),
    ("13.6", "Governance Frameworks", f"{M2}/week-13/1-ethics-safety-governance/13-6-governance-frameworks", ["5.7", "5.8", "5.9", "5.10", "5.11", "5.12", "5.13"]),
    ("13.7", "Engineering Takeaway", f"{M2}/week-13/1-ethics-safety-governance/13-7-engineering-takeaway", []),

    ("14.1", "How Humans Think", f"{M3}/week-14/1-human-judgment-ai-oversight/14-1-how-humans-think", ["9.1", "9.2", "9.3", "9.4", "9.5", "9.6"]),
    ("14.2", "The Judgment Framework", f"{M3}/week-14/1-human-judgment-ai-oversight/14-2-the-judgment-framework", ["9.7", "9.8", "9.9", "9.10", "9.11"]),
    ("15.1", "Case Study: College Admissions", f"{M3}/week-15/1-cognition-in-practice/15-1-case-study-1-college-admissions", ["10.1"]),
    ("15.2", "Case Study: Automated Medical Triage", f"{M3}/week-15/1-cognition-in-practice/15-2-case-study-2-automated-medical-triage", ["10.2"]),
    ("15.3", "Case Study: AI Loan Approval at Scale", f"{M3}/week-15/1-cognition-in-practice/15-3-case-study-3-ai-loan-approval-at-scale", ["10.3"]),
    ("15.4", "Automation Complacency", f"{M3}/week-15/1-cognition-in-practice/15-4-automation-complacency", ["10.4"]),
    ("15.5", "Human-in-the-Loop Checkpoints", f"{M3}/week-15/1-cognition-in-practice/15-5-human-in-the-loop-checkpoints", ["10.5", "10.6"]),
    ("15.6", "Connecting Oversight to Your Domain", f"{M3}/week-15/1-cognition-in-practice/15-6-connecting-oversight-to-your-domain", ["10.7"]),
]

# README rendering structure: module heading -> ordered list of (week heading, [cresent ids])
README_STRUCTURE = [
    ("M1 — Computational Thinking", [
        ("Week 8 — Computational Thinking Kickoff", ["8.3", "8.4", "8.5"]),
        ("Week 9 — Computational Thinking", ["9.1", "9.2", "9.3"]),
    ]),
    ("M2 — Introduction to AI Systems", [
        ("Week 10 — What AI Is — and Isn't", ["10.1", "10.2", "10.3", "10.4", "10.5"]),
        ("Week 11 — The 2026 AI Stack", ["11.1", "11.2", "11.3", "11.4", "11.5", "11.6"]),
        ("Week 12 — How LLMs Behave", ["12.1", "12.2", "12.3", "12.4", "12.5"]),
        ("Week 13 — AI Ethics, Safety and Governance", ["13.1", "13.2", "13.3", "13.4", "13.5", "13.6", "13.7"]),
    ]),
    ("M3 — Human Cognition & AI Oversight", [
        ("Week 14 — Human Judgment and AI Oversight", ["14.1", "14.2"]),
        ("Week 15 — Cognition in Practice — Case Studies", ["15.1", "15.2", "15.3", "15.4", "15.5", "15.6"]),
    ]),
]

NAV_SEP = "&emsp;·&emsp;"
LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)([^)]*\))")


def rel(from_dir: str, to_path: str) -> str:
    """POSIX-style relative link from a directory to a target path."""
    return os.path.relpath(to_path, from_dir).replace(os.sep, "/")


def extract_body(text: str) -> str:
    """Return the reading body with CIT's own nav block and the adjacent
    horizontal rules removed."""
    top_marker = "<!-- nav:top:end -->"
    bot_marker = "<!-- nav:bottom:start -->"
    start = text.find(top_marker)
    start = start + len(top_marker) if start != -1 else 0
    end = text.find(bot_marker)
    if end == -1:
        end = len(text)
    lines = text[start:end].split("\n")
    # Trim leading blanks + a leading '---' rule (separator after top nav).
    while lines and lines[0].strip() == "":
        lines.pop(0)
    if lines and lines[0].strip() == "---":
        lines.pop(0)
    while lines and lines[0].strip() == "":
        lines.pop(0)
    # Trim trailing blanks + a trailing '---' rule (separator before bottom nav).
    while lines and lines[-1].strip() == "":
        lines.pop()
    if lines and lines[-1].strip() == "---":
        lines.pop()
    while lines and lines[-1].strip() == "":
        lines.pop()
    return "\n".join(lines)


def rewrite_relative_links(body: str, cit_artifacts_dir: str, cresent_dir: str) -> str:
    """Rewrite relative image/link targets (e.g. ./diagram.png) so they still
    resolve from the Cresent page's location back to the CIT source folder.
    External URLs, anchors and mailto links are left untouched."""
    def repl(m: "re.Match[str]") -> str:
        pre, target, post = m.group(1), m.group(2), m.group(3)
        t = target.strip()
        if (re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://", t) or t.startswith("#")
                or t.startswith("mailto:") or t.startswith("/")):
            return m.group(0)
        frag = ""
        if "#" in t:
            t, frag = t.split("#", 1)
            frag = "#" + frag
        if not t:
            return m.group(0)
        resolved = os.path.normpath(os.path.join(cit_artifacts_dir, t))
        return pre + rel(cresent_dir, resolved) + frag + post
    return LINK_RE.sub(repl, body)


def nav_bar(idx: int, cresent_dir: str) -> str:
    prev_part = "Previous: —"
    if idx > 0:
        pid, ptitle, pfolder, _ = TOPICS[idx - 1]
        ppath = os.path.join(CRESENT_CONTENT, pfolder, "reading.md")
        prev_part = f"Previous: [⬅ {pid} — {ptitle}]({rel(cresent_dir, ppath)})"

    toc = f"[⬆ Table of Contents]({rel(cresent_dir, README)}#part-b)"

    next_part = "Next: —"
    if idx < len(TOPICS) - 1:
        nid, ntitle, nfolder, _ = TOPICS[idx + 1]
        npath = os.path.join(CRESENT_CONTENT, nfolder, "reading.md")
        next_part = f"[{nid} — {ntitle} ➡]({rel(cresent_dir, npath)})"

    return NAV_SEP.join([prev_part, toc, next_part])


def build_body(cid: str, title: str, cit_ids: list, cresent_dir: str) -> str:
    if not cit_ids:
        return (f"# {title}\n\n"
                f"> **Synthesis topic — no dedicated CIT reading.**\n"
                f"> Revisit this week's readings (especially *13.6 — Governance Frameworks*) "
                f"and connect them to your own domain project.")
    chunks = []
    for cit_id in cit_ids:
        cit_path = os.path.join(CIT_CONTENT, CIT[cit_id])
        with open(cit_path, encoding="utf-8") as fh:
            raw = fh.read()
        body = extract_body(raw)
        body = rewrite_relative_links(body, os.path.dirname(cit_path), cresent_dir)
        chunks.append(body)
    return "\n\n---\n\n".join(chunks)


def generate_pages() -> int:
    written = 0
    for idx, (cid, title, folder, cit_ids) in enumerate(TOPICS):
        cresent_dir = os.path.join(CRESENT_CONTENT, folder)
        if not os.path.isdir(cresent_dir):
            print(f"  ! missing Cresent folder for {cid}: {folder}", file=sys.stderr)
            continue
        for cit_id in cit_ids:
            if cit_id not in CIT:
                raise KeyError(f"{cid}: unknown CIT id {cit_id}")
            if not os.path.isfile(os.path.join(CIT_CONTENT, CIT[cit_id])):
                raise FileNotFoundError(f"{cid}: CIT source missing for {cit_id}")
        sources = ", ".join(f"CIT {c}" for c in cit_ids) if cit_ids else "none (synthesis topic)"
        banner = ("<!-- GENERATED FILE — DO NOT EDIT BY HAND.\n"
                  f"     Cresent view of {cid} — {title}.\n"
                  f"     Source of truth: {sources}.\n"
                  "     Regenerate: python Cresent/Technical/tools/generate_shared_readings.py -->")
        nav = nav_bar(idx, cresent_dir)
        body = build_body(cid, title, cit_ids, cresent_dir)
        page = (f"{banner}\n"
                f"<!-- nav:top:start -->\n{nav}\n<!-- nav:top:end -->\n\n"
                f"---\n\n{body}\n\n---\n"
                f"<!-- nav:bottom:start -->\n{nav}\n<!-- nav:bottom:end -->\n")
        with open(os.path.join(cresent_dir, "reading.md"), "w", encoding="utf-8") as fh:
            fh.write(page)
        written += 1
    return written


def build_readme_block() -> str:
    by_id = {t[0]: t for t in TOPICS}
    out = ["# Part B — AI Foundations (shared with CIT)", "",
           "Modules **M1–M3** are the AI-Native content shared with the CIT curriculum. "
           "Each topic below is a Cresent page with its **own Prev / TOC / Next navigation**; "
           "its reading text is generated from the single canonical source in the CIT tree "
           "(`../../CIT/...`). Do not hand-edit these pages — edit the CIT reading and re-run "
           "`tools/generate_shared_readings.py`.", ""]
    for module_heading, weeks in README_STRUCTURE:
        out.append(f"## {module_heading}")
        for week_heading, ids in weeks:
            out.append(f"### {week_heading}")
            out.append("")
            for cid in ids:
                _, title, folder, cit_ids = by_id[cid]
                link = f"content/ai_native_engineering_foundations/{folder}/reading.md"
                covers = (" · _covers " + ", ".join(f"CIT {c}" for c in cit_ids) + "_"
                          if cit_ids else " · _synthesis topic_")
                out.append(f"- {cid} — [{title}]({link}){covers}")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def update_readme() -> None:
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    start = "<!-- part-b:start -->"
    end = "<!-- part-b:end -->"
    i, j = text.find(start), text.find(end)
    if i == -1 or j == -1:
        raise RuntimeError("part-b markers not found in README.md")
    new = text[:i + len(start)] + "\n" + build_readme_block() + "\n" + text[j:]
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new)


def main() -> None:
    print(f"repo root: {REPO_ROOT}")
    n = generate_pages()
    print(f"generated {n} Cresent reading pages")
    update_readme()
    print("README Part B section regenerated")


if __name__ == "__main__":
    main()
