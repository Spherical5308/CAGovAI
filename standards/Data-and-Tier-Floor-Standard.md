# [State Entity] AI Data and Tier Floor Standard

| | |
|---|---|
| **Authority** | [AI Governance Policy](../policy/AI-Governance-Policy.md) sections 4.1–4.2; SAM 5305.5; SAM 4986.10; SIMM 5305-F |
| **Owner** | AI Governance Coordinator, with the ISO and Privacy Officer |
| **Effective date** | [date] |

This Standard decides two things: **when** a Use Case needs a Request, and the **minimum Risk Tier** that Request can receive.

## 1. Data classes
SAM 5305.5 requires [State Entity] to classify its information assets and give each a FIPS 199 categorisation, with personal and medical information at least FIPS 199 Moderate. It does not prescribe class names. This Standard uses the classes below, which follow the SIMM 5305-F data types and the "confidential, proprietary and sensitive" wording of SAM 4986.10; map them to [State Entity]'s own scheme if it differs.

| Class | Examples (SIMM 5305-F data types) |
|---|---|
| **Public** | Information not exempt under the CPRA; aggregated statistics; published policy |
| **Internal** | Operational information not intended for release but not exempt (drafts, internal procedures) |
| **Confidential / Sensitive** | CPRA-exempt information; attorney-client material; controlled technical information (network diagrams, logs, keys); proprietary and intellectual property |
| **Personal** | Personal information under Civil Code 1798.3 and 1798.29: names with identifiers, SSN, DOB, addresses, financial, medical, biometric, education, employment, credentials |
| **Federally restricted** | FTI (IRS Pub. 1075), CJI (CJIS), PHI/EHR (HIPAA), FERPA records, CUI, CDI, ITAR/EAR data |

When a Use Case touches more than one class, the highest class governs. Prompts, retrieved documents, outputs, training or fine-tuning data and logs all count.

## 2. Triggers
A Use Case needs a **Request**, even when its Tool is approved, if **any** of these is true:

| # | Trigger |
|---|---|
| T1 | The Tool is not approved, or the Use Case is outside the Tool's Approved Uses |
| T2 | It uses Confidential/Sensitive, Personal or Federally restricted data |
| T3 | Its output goes to the public or to people outside [State Entity] |
| T4 | It informs or makes decisions about specific people (eligibility, benefits, services, enforcement, licensing, employment, discipline) |
| T5 | Its Autonomy Level is A2 or A3 (see the [Autonomy and Agent Standard](./Autonomy-and-Agent-Standard.md)) |
| T6 | A vendor has disclosed GenAI use under SCM Vol. 2 Ch. 23 |
| T7 | It affects employees' terms and conditions of employment, or how their work is monitored or evaluated |
| T8 | It will be used by or about minors |

If unsure, submit a Request. The Coordinator will close it as Pre-approved if no Trigger applies.

## 3. Tier Floors
The Risk Tier is the **highest** of the SIMM 5305-F (or SIMM 150) result and every floor below that applies.

| Factor | Tier Floor |
|---|---|
| Any prohibited use in the [Acceptable Use Standard](./Acceptable-Use-Standard.md#4-prohibited-uses) | **Prohibited** |
| Public or Internal data, Autonomy Level A0–A1, internal audience | none (Low unless SIMM 5305-F says otherwise) |
| Code analysis or generation tools, chatbots, or output supporting decisions in public programs (SIMM 5305-F "Moderate" examples) | **Moderate** |
| Public-facing output or interaction (T3) | **Moderate** |
| Confidential/Sensitive or Personal data (T2) | **Moderate** |
| A2 or A3 acting on production systems | **Moderate** |
| Affects employees' terms, conditions or monitoring (T7) | **Moderate** |
| Decisions about specific people (T4), or a high-risk automated decision system under GC 11546.45.5 | **High** |
| Access to housing, education, employment, credit, health care or criminal justice (SIMM 5305-F Part 2, Ensuring Equity) | **High** |
| Public safety or critical infrastructure decisions | **High** |
| Federally restricted data | **High** |
| Used by or about minors (T8) | **High** |
| A3 touching Confidential/Sensitive or Personal data, or acting toward the public or external parties | **High** |

## 4. Privacy assessments
1. Every Request above Pre-approved includes a SIMM 5310-C **Privacy Threshold Assessment** (SAM 4986.9, 4986.10).
2. A SIMM 5310-C **Privacy Impact Assessment** is completed when the PTA requires one. It is always required at High.
3. The Privacy Officer may require a PIA at any tier.

## 5. Minimum data controls by class
| Class | Minimum controls before approval |
|---|---|
| Public / Internal | Approved Tool; training opt-out; State identity (SSO) |
| Confidential / Sensitive | Above, plus: encryption per SAM 5350.1; data stays in the United States (SIMM 140); vendor contractually barred from training on or retaining data beyond service delivery; DLP on inputs and outputs |
| Personal | Above, plus: data minimisation (only fields the task needs); purpose limitation; access by least privilege; PIA if required; breach terms under SIMM 5340-C |
| Federally restricted | Above, plus: the federal program's own requirements (e.g., IRS Pub. 1075, CJIS Security Policy, HIPAA); written confirmation from the data owner that AI processing is permitted; private network connectivity, no public ingress |
