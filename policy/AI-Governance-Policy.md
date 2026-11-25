# [State Entity] Artificial Intelligence Governance Policy

| | |
|---|---|
| **Policy number** | [number] |
| **Owner** | Chief Information Officer, through the AI Governance Coordinator |
| **Approved by** | [Director name], Director |
| **Effective date** | [date] |
| **Next review** | 12 months after the effective date, and whenever SAM 4986 or SIMM 5305-F is revised |
| **Supersedes** | [prior GenAI guidance, if any] |

> Template note: replace every `[bracketed]` value. Terms in **bold capitals** are defined in [GLOSSARY.md](../GLOSSARY.md). Sections marked *(EB)* are mandatory for Executive Branch State Entities; other State Entities may adopt them voluntarily.

## 1. Purpose
This policy sets how [State Entity] decides whether, and on what terms, it will acquire, build or use AI. It exists so that AI improves services to Californians while risks to the public, to State data and to the workforce are identified, owned and managed before and during use, as required by Executive Order N-12-23 and SAM 4986.

## 2. Scope
1. This policy applies to all employees, contractors, volunteers and other authorised users of [State Entity] who access, use, procure, build or manage AI on behalf of [State Entity] (SAM 4986.1).
2. It covers all **AI**, including **GenAI** and automated decision systems, whether purchased, licensed, free, open source, built in-house, or delivered as a feature inside another product (ADR-0002).
3. It covers AI used in a contractor's performance of State work when the contractor has disclosed GenAI use under the State Contracting Manual, Volume 2, Chapter 23.
4. It does not cover incidental use of AI by the public on their own devices, or AI features in web search where no State data is entered (SIMM 5305-F, Part 1 instructions).

## 3. Principles
[State Entity] uses AI only where it:
1. **Serves a defined public purpose** and augments, rather than replaces, accountable human judgment (SIMM 5305-F introduction).
2. **Is lawful**, including privacy, civil rights, accessibility, public records and labor obligations.
3. **Is safe and secure**, following the NIST AI Risk Management Framework and NIST SP 800-53 baselines from a Zero Trust perspective (SAM 4986.11).
4. **Is transparent** to the people it affects, including disclosure of AI-generated content (GC 11549.66; SAM 4986.10).
5. **Is fair**, with bias, accuracy and accessibility tested before and during use (SAM 4986.12).
6. **Has a named owner** for every **Tool** and **Use Case**, and a recorded decision for every approval.

## 4. Policy statements

### 4.1 Approval before use
1. No AI may be used for State work unless it is either (a) a **Pre-approved** Use Case of an approved Tool, or (b) approved through a **Request** under the [Request and Approval Procedure](../procedures/01-Request-and-Approval.md).
2. A Use Case that hits any **Trigger** listed in the [Data and Tier Floor Standard](../standards/Data-and-Tier-Floor-Standard.md) requires a Request even if its Tool is approved (ADR-0003).
3. Users must only use State-approved accounts on State-approved equipment, and must not enter confidential, sensitive or personal information into any AI Tool that has not been approved (SAM 4986.12).

### 4.2 Risk Tiers
Every Request receives one **Risk Tier**: Prohibited, Pre-approved, Low, Moderate or High. Low, Moderate and High follow the SIMM 5305-F GenAI Risk Assessment scale. The tier is the highest of the SIMM 5305-F result and every **Tier Floor** that applies.

### 4.3 Prohibited uses
[State Entity] will not use AI for any purpose listed in the [Acceptable Use Standard, section 4](../standards/Acceptable-Use-Standard.md#4-prohibited-uses).

### 4.4 Decision authority
| Risk Tier | Decided by |
|---|---|
| Prohibited | Stopped by the AI Governance Coordinator, confirmed by Chief Counsel; appealable to the Committee |
| Pre-approved | No decision; the requester's manager attests and the use is logged |
| Low | Triage Panel |
| Moderate | AI Governance Committee, by majority vote |
| High | AI Governance Committee recommends; the Director approves; the parent Agency may be consulted |

The AI Governance Committee is constituted by the [Committee Charter](./AI-Governance-Committee-Charter.md). No single seat, including the Information Security Officer, may veto a Committee decision. A recorded ISO dissent requires a Director-signed **Risk Acceptance** before the approval takes effect (ADR-0001).

### 4.5 Required assessments
Each Risk Tier requires the cumulative **Assessment Package** set out in the [Request and Approval Procedure](../procedures/01-Request-and-Approval.md#6-assessment-package). At a minimum, every GenAI Tool must have a SIMM 5305-F (or SIMM 150 for general office productivity) and a SIMM 5310-C Privacy Threshold Assessment, unless exempted by SAM 4986.9 (SAM 4986.11(C)).

### 4.6 CDT consultation *(EB)*
[State Entity] decides its own Requests; CDT reviews and consults but does not approve. When a completed SIMM 5305-F or SIMM 150 goes to the California Department of Technology, and whether consultation must finish before award, depends on the Risk Tier and the procurement route, as set out in [Procedure 01, section 4](../procedures/01-Request-and-Approval.md#4-cdt-submission-and-consultation) (SAM 4986.9; CDT PS-033). In summary: Low is kept on file and goes to CDT only where the route still requires it; Moderate is submitted and awaits CDT review; High is submitted and requires CDT consultation before proceeding.

### 4.7 Procurement
No purchase requisition, solicitation, renewal or contract amendment that provides or materially relies on AI may proceed without an approved **Request ID**. All IT and telecommunications solicitations and contracts include the GenAI disclosure language required by SAM 4986.9(A) (ADR-0004).

### 4.8 Hosting, proofs of concept and projects *(EB)*
GenAI Tools follow the Cloud Computing Policy (SAM 4983.1; SAM 4986.5). Proofs of concept run in a CDT-approved sandbox using public data only; minimum viable products run in a CDT-approved production environment (SAM 4986.6). IT projects that use GenAI follow the SIMM 19H Project Delivery Lifecycle (SAM 4986.7, 4986.8).

### 4.9 Transparency and disclosure
1. Content created or substantially altered by GenAI and provided to people for government services carries a disclosure, a way to contact a person, and a way to opt out of interacting with GenAI (GC 11549.66; SAM 4986.10).
2. [State Entity] publishes a public summary of its AI Use Cases from the **AI Inventory**. Where [State Entity] built or substantially modified a GenAI system made available to Californians, it posts training-data documentation and updates it annually (Civil Code 3111; SAM 4986.4).
3. Completed risk and security assessments are confidential and are not published (GC 7929.210).

### 4.10 Records
Prompts, outputs and agent action logs created in the course of State business are records. They are retained under [State Entity]'s records retention schedule (SAM 1600; GC 12270 et seq.) and are subject to the California Public Records Act. A Tool may not be approved for Moderate or High Use Cases unless it can retain and export these records.

### 4.11 Inventory
The AI Governance Coordinator maintains a single AI Inventory of all Tools and Use Cases, including **Legacy Uses**, and produces from it the high-risk inventory CDT requests (SAM 4986.3; GC 11546.45.5).

### 4.12 Monitoring, Re-review and incidents
1. Approved AI is monitored under SAM 5335 and re-reviewed on the schedule and **Material Changes** in the [Monitoring and Re-review Procedure](../procedures/03-Monitoring-and-Re-review.md).
2. AI incidents are handled under [State Entity]'s Incident Response Plan and reported as SAM 4986.11 and SIMM 5340-A require. The ISO or the CIO may impose an immediate **Suspension**; the Committee confirms or lifts it within 10 business days.

### 4.13 Workforce
1. Every user completes the GenAI training their role requires before using AI (SAM 4986.13).
2. [State Entity]'s Labor Relations Officer receives every SIMM 5305-F (SIMM 5305-F, Labor Relations Engagement) and advises the Committee on any Use Case that may affect employees' terms and conditions of employment, including any duty to meet and confer under the Ralph C. Dills Act (GC 3512 et seq.).

### 4.14 Exceptions
Departures from a Standard may be granted only through the [Exceptions Procedure](../procedures/05-Exceptions.md), for at most 12 months. There are no exceptions to this Policy.

## 5. Roles and responsibilities
| Role | Responsibility |
|---|---|
| **Director** | Approves this Policy, High-tier Requests, Risk Acceptances and Exceptions. |
| **Executive Sponsor** | Chairs the AI Governance Committee; accountable for the AI program. |
| **AI Governance Committee** | Decides Moderate Requests, recommends High Requests, confirms Suspensions, approves Exceptions, oversees the AI Inventory. |
| **AI Governance Coordinator** (CIO's office) | Runs intake, screening and triage; maintains the AI Inventory; schedules Re-reviews; publishes transparency information. |
| **Triage Panel** | Decides Low-tier Requests. |
| **Chief Information Officer** | Owns this Policy; signs SIMM 5305-F / 150 as an **Assessment Attestation**; may impose a Suspension. |
| **Information Security Officer** | Votes on the Committee; signs SIMM 5305-F / 150 as an Assessment Attestation; leads AI incident response; may impose a Suspension. |
| **Privacy Officer** | Votes on the Committee; owns the SIMM 5310-C PTA and PIA. |
| **Chief Counsel** | Votes on the Committee; confirms Prohibited determinations; advises on legal obligations. |
| **Business/Program Representative** | Votes on the Committee, representing program operations. |
| **Advisory Seats** (Labor Relations, Accessibility, Records Management, Procurement) | Review and advise; do not vote. |
| **Business unit / Use Case owner** | Submits Requests, completes the Assessment Package, operates the Use Case as approved and reports Material Changes and incidents. |
| **Managers and supervisors** | Attest Pre-approved uses; ensure staff training. |
| **All users** | Follow the [Acceptable Use Standard](../standards/Acceptable-Use-Standard.md); report misuse to the ISO. |

## 6. Compliance
Using AI outside this Policy may result in removal of access and disciplinary action consistent with applicable law and bargaining agreements. Any AI found in use without approval after the 90-day Legacy Use registration window is treated as an information security incident.

## 7. Authorities
Executive Order N-12-23; GC 11546.45.5, 11549.63–11549.66, 7929.210, 12270 et seq., 3512 et seq.; Civil Code 1798 et seq., 3110–3111; SAM 1600, 4819.2, 4983.1, 4986–4986.13, 5305.5, 5310, 5335; SIMM 19H, 140, 141, 150, 22, 5305-F, 5310-C, 5340-A, 5340-C; SCM Vol. 2 Ch. 23; NIST AI 100-1, NIST AI 600-1, NIST SP 800-53. See the [authority crosswalk](../references/Authority-Crosswalk.md).

## 8. Related documents
[Committee Charter](./AI-Governance-Committee-Charter.md) · [Standards](../standards/) · [Procedures](../procedures/) · [Forms](../forms/) · [AI Inventory](../inventory/) · [Procedure Map](../PROCEDURE-MAP.md)
