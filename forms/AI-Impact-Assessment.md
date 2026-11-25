# AI Impact Assessment

> Required for Moderate and High Requests. It covers what SIMM 5305-F and SIMM 5310-C do not: whether the AI works well enough for its purpose, who it could harm, and how people stay in control. It follows the NIST AI RMF **Map** and **Measure** functions and the NIST AI 600-1 Generative AI Profile.
>
> Section structure is adapted from the aipolicytracker.org AI Impact Assessment template (CC BY 4.0); changes were made. See [NOTICE.md](../NOTICE.md).

> **How to complete this form**
> - **Who:** the Use Case owner, with the people who know the system. The Privacy Officer and the ISO may add to sections 4 and 5.
> - **When:** after the Coordinator issues your Assessment Package (Procedure 01, step C2). The decision clock starts only when the whole package is complete.
> - **Send to:** the AI Governance Coordinator, with the rest of the Assessment Package.
> - Answer every question in plain language. If something does not apply, write "Not applicable" and say why; do not leave it blank.
> - **Ratings** in sections 4 and 7 use the [Rating Scales](./Rating-Scales.md), printed at the end of the Word version.
> - Describe security weaknesses in general terms. Technical detail belongs in the security review, which is kept confidential.

**Request number:** · **Use Case:** · **Risk Tier:** · **Prepared by:** · **Date:**

## 1. Context (NIST Map 1)
1. Purpose and intended use, in one paragraph.
2. Uses that are **out of scope** and must not happen (e.g. "not for final eligibility determinations").
3. The legal authority for the program activity the AI supports.
4. Alternatives considered, including not using AI, and why this one was chosen.

## 2. Affected people (NIST Map 5)
1. Who is directly affected (users, the public, applicants, employees)?
2. Who is indirectly affected?
3. Which groups could be affected differently (language, disability, age, race or ethnicity, income, geography, digital access)?
4. How were affected people or their representatives consulted? What changed as a result?

## 3. Performance (NIST Measure 2)
| Measure | Method | Threshold to go live | Threshold that triggers Re-review | Result |
|---|---|---|---|---|
| Accuracy / factual correctness | e.g. expert review of N sampled outputs | | | |
| Hallucination / fabricated citations | | | | |
| Consistency across groups (bias) | e.g. compare error rates across languages or groups | | | |
| Robustness to manipulation (prompt injection) | adversarial test set | | | |
| Accessibility of outputs and interface | WCAG 2.1 AA review | | | |
| Other: | | | | |

Describe the test data and how it represents real use. For a POC, testing uses public data only (SAM 4986.6).

## 4. Harm analysis (NIST Map 5.1; AI 600-1 risk areas)
Mark each area relevant or not. For each relevant one, describe the harm, rate its Likelihood and Severity (Low / Medium / High), read the Risk Rating from the matrix, and describe the mitigation. Use the [Rating Scales](./Rating-Scales.md). Rate with the controls already in place; the residual rating after mitigation goes in section 7.

| Area | Relevant? | Harm | Likelihood | Severity | Risk Rating | Mitigation | Owner |
|---|:-:|---|---|---|---|---|---|
| Confabulation (wrong or invented output relied on) | | | | | | | |
| Harmful bias or unequal treatment | | | | | | | |
| Privacy (exposure, inference, re-identification) | | | | | | | |
| Information security (injection, data leakage, poisoning) | | | | | | | |
| Harmful or dangerous content | | | | | | | |
| Information integrity (misinformation released publicly) | | | | | | | |
| Intellectual property | | | | | | | |
| Human-AI configuration (over-reliance, automation bias) | | | | | | | |
| Environmental and cost | | | | | | | |
| Value chain (vendor, model or data dependency) | | | | | | | |
| Workforce effects (see Workforce Impact Assessment) | | | | | | | |
| Access to services (people who cannot or will not use AI) | | | | | | | |

## 5. Human oversight (NIST Govern 3.2, Map 3.5, Manage 2.4)
1. Autonomy Level and why it is the lowest that meets the need.
2. Who reviews output or approves actions; their qualifications; how long they have to do it.
3. How someone affected can question, correct or appeal an AI-assisted outcome (SIMM 5305-F Part 2, Transparency (d)).
4. How the use can be stopped quickly, and by whom.

## 6. Transparency
1. How people are told they are interacting with AI or receiving AI-generated content (GC 11549.66).
2. How people can reach a person or opt out.
3. What goes in the public AI use summary.

## 7. Residual risk and recommendation
List each risk still Medium or High after mitigation. Rate it again with the [Rating Scales](./Rating-Scales.md); the scales also say who should accept each Risk Rating.

| Residual risk | Risk Rating | Accepted by |
|---|---|---|
| | | |

Recommendation: ☐ Proceed ☐ Proceed with conditions: ☐ Do not proceed

| Use Case owner | Signature | Date |
|---|---|---|
| | | |

<!-- include: Rating-Scales.md -->
