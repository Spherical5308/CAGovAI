# GenAI Training Outline

> Role-based training for [State Entity], built to meet SAM 4986.13 *(EB)* (new 02/2025). SAM 4986.13 requires each Executive Branch State Entity to ensure its people complete the GenAI training their duties need, including the risks and benefits of GenAI and how to use it responsibly, and to require any mandatory GenAI training. It recommends ("should also consider") the audience-based courses that modules A, B, D, E and F below follow. Modules C and G are this framework's additions.
>
> SAM 4986.13 sets no completion deadline or refresh cycle. This outline's timing (before first use, then yearly and on major policy change) is a recommendation. Use State-provided courses where they exist ([below](#state-provided-courses)), and build only what is missing.

## State-provided courses
The State already offers general GenAI courses for most audiences. What no State course can cover is your own entity's rules: your Policy, Approved Uses, forms, Triggers and decision process. So each module below is a State course (where one exists) plus a short entity supplement that you build.

The State's catalogue is the CDT [Comprehensive GenAI Training Guide](https://www.cdt.ca.gov/wp-content/uploads/2026/10/Comprehensive-GenAI-Training-Guide-9-2026-FINAL.pdf) (September 2026 edition, linked from CDT's [GenAI training page](https://www.cdt.ca.gov/workforce-development/generative-ai-training/)). It groups courses into four audience tiers of its own and does not map them to SAM 4986.13, so the mapping below is this framework's. Offerings, dates and costs change: confirm with CalHR (Training@calhr.ca.gov), CDT (Training@state.ca.gov) and DGS CalPCA (CalPCAonline@dgs.ca.gov) before you commit.

| Module | State-provided course | Build locally |
|---|---|---|
| A. Foundations | CalHR and ODI Foundations of GenAI certificate series, listed on CalHR's [Certificate Series Collection](https://www.calhr.ca.gov/about-calhr/divisions-programs/workforce-development-division/calhr-certificate-series-collection/) page (5 courses, about 42 hours, for all State employees, including "Responsible AI for Public Professionals"). Staff enrol through CalLearns; see [CalHR Training Registration](https://www.calhr.ca.gov/about-calhr/divisions-programs/workforce-development-division/calhr-training-registration/). CDT PACe self-paced eLearning has shorter topics. | Items 3, 7, 8 and 10: your approved Tools and Approved Uses Register, records rules, Prohibited uses P1 to P11, and the acknowledgment. About 20 to 30 minutes. |
| B. Managers | No manager course specific to GenAI. The CalHR leadership course "Responsible AI: Scaling AI in Your Organization" suits senior managers. | All of module B: attestation, Triggers, T7 workforce rules and Suspensions are this framework's. |
| C. Use Case owners | None. | All of module C. |
| D. Purchasing | DGS CalPCA GenAI procurement training. The CDT guide says Designated Purchasing Authority Contacts **must** complete it. | Item 1 (Request ID gate) and your CDT submission route from Procedure 01 §4. |
| E. Project managers | CDT ["AI Project Management"](https://www.cdt.ca.gov/workforce-development/generative-ai-training/), and the GenAI Project Managers course in CDT's Project Management Leadership Academy (PMLA), on top of the Project Delivery Lifecycle course. | Item 3: building approval conditions and monitoring into the schedule. |
| F. IT and security | CDT [GenAI Technical Training](https://www.cdt.ca.gov/workforce-development/generative-ai-training/) (Security, Data Analytics, Engineering and Development, Design domains), including "AI Foundations and Use Cases for IT" and "Introduction to Agentic AI for Business Users". The CDT [GenAI Boot Camp](https://www.cdt.ca.gov/workforce-development/gen-ai-bootcamp/) (6 weeks, fee-based, needs CIO approval; the fall 2026 cohort is closed, so check for the next one) is optional depth. | Items 3 and 6: the Autonomy and Agent Standard, and your SIMM 5305-F, SIMM 150 and Risk Register practice. |
| G. Committee | None specific. CalHR "Responsible AI for Legal Professionals" suits Chief Counsel, and the CDT ITLA, PMLA and ISLA leadership academies include a GenAI course for CIO and ISO seats. | All of module G. |

[genai.ca.gov](https://www.genai.ca.gov/choose-your-journey/procure-tool/take-training/state-staff/) recommends training executives, GenAI leads, legal, labor and privacy staff first, then business owners and technical staff, then the general workforce. The [Rollout Plan](./90-Day-Rollout-Plan.md) trains all staff from Day 0 because the Policy applies to everyone from that date; start the Committee and leadership courses in Phase 1 if you can.

## Who takes what
| Audience | Modules | When | SAM 4986.13 basis |
|---|---|---|---|
| Everyone who uses AI, including contractors | A | Before first use of any AI Tool | Required: training for duties; recommended: foundational training for all |
| Managers and supervisors | A, B | Before attesting a Pre-approved use | Recommended: foundational plus role-specific |
| Use Case owners (requesters) | A, C | Before submitting a Request | Framework addition |
| Purchasing officials | A, D | Before buying any AI | Recommended: procurement training |
| Project managers on AI projects | A, E | Before project start | Recommended: Project Delivery Lifecycle training |
| IT and information security staff | A, F | Before building, configuring or securing AI | Recommended: advanced technical training |
| Committee members, delegates, Triage Panel | A, G | Before first decision | Framework addition |

Refresh: module A yearly, and every module when the Policy or a Standard changes materially. Record completion; a manager confirms it before a Pre-approved attestation ([Procedure 01](../procedures/01-Request-and-Approval.md) step A2).

## Module A: Foundations for all staff (about 60 minutes)
1. What GenAI is and is not: prediction, not understanding; why it can sound right and be wrong.
2. Benefits and risks in plain words ([Acceptable Use Standard](../standards/Acceptable-Use-Standard.md) §1): fabricated facts and citations, bias, privacy and data leakage, prompt injection, intellectual property.
3. Before you use AI: approved Tools only, the [Approved Uses Register](../forms/Approved-Uses-Register.md), and when a Request is needed (the Triggers in the [Data and Tier Floor Standard](../standards/Data-and-Tier-Floor-Standard.md#2-triggers)).
4. Data: the data classes and what never goes into a prompt; opting out of model training (SAM 4986.12).
5. Your duty to check output before you rely on it (SAM 4986.12).
6. Telling people when content is AI-generated and how to reach a person (GC 11549.66; SAM 4986.10).
7. Prompts, outputs and logs are records (Policy §4.10).
8. Prohibited uses P1 to P11 (Acceptable Use Standard §4), with examples.
9. Reporting misuse, data entered into the wrong Tool, or harmful output to the ISO.
10. Knowledge check and the Acceptable Use acknowledgment.

## Module B: Managers and supervisors (about 45 minutes)
1. Attesting Pre-approved uses: what you confirm and how it is logged.
2. Spotting a Trigger and a Material Change; when to send staff to the Coordinator.
3. Workforce effects: changes to duties, workload or monitoring need a Workforce Impact Assessment and Labor Relations (Trigger T7; GC 3512 et seq.).
4. Using AI output, usage data or logs to monitor, evaluate or discipline staff is itself Trigger T7: it needs a Request, sets a Tier Floor of at least Moderate, and needs Chief Counsel review ([Workforce Impact Assessment](../forms/Workforce-Impact-Assessment.md) §2).
5. Making sure your staff complete their training.
6. What to do if a Use Case is suspended.

## Module C: Use Case owners (about 60 minutes)
1. The process end to end ([Procedure Map](../PROCEDURE-MAP.md)) and turnaround targets.
2. Completing the [Intake Form](../forms/Intake-Form.md) and the Assessment Package for your tier.
3. Writing the [AI Impact Assessment](../forms/AI-Impact-Assessment.md): testing, harms, and the [Rating Scales](../forms/Rating-Scales.md).
4. Approval conditions, go-live checks, monitoring reports and Re-review ([Procedure 03](../procedures/03-Monitoring-and-Re-review.md)).
5. Reporting Material Changes and incidents.

## Module D: Purchasing officials (about 45 minutes)
1. No AI purchase without a Request ID (ADR-0004).
2. The GenAI disclosure clause and vendor questions (SCM Vol. 2 Ch. 23; SAM 4986.9).
3. When the SIMM 5305-F goes to CDT and when consultation must finish before award ([Procedure 01](../procedures/01-Request-and-Approval.md) §4; CDT PS-033).
4. Vendor evaluation for Moderate and High (SAM 4986.9(B)).
5. Contract terms to look for: no training on State data, retention limits, export of prompts and logs, United States data location for confidential data.
6. Spotting AI features added to software already under contract.

## Module E: Project managers (about 30 minutes, on top of the Project Delivery Lifecycle course)
1. When an AI effort is a project and which assessments come first (SAM 4986.7 to 4986.8; SIMM 19H).
2. Proofs of concept: CDT sandbox and public data only (SAM 4986.6).
3. Building approval conditions, testing thresholds and the monitoring plan into the project schedule.

## Module F: IT and information security staff (about 2 to 3 hours)
1. NIST AI RMF and the Generative AI Profile (NIST AI 600-1) risk areas.
2. Threats: prompt injection, data leakage, poisoning, model and plug-in supply chain.
3. The [Autonomy and Agent Standard](../standards/Autonomy-and-Agent-Standard.md): permissions, approvals, kill switch and logging for A2 and A3.
4. Hosting and cloud rules (SAM 4986.5; SIMM 140, 141, 22) and data controls by class.
5. Logging and monitoring (SAM 5335) and AI incident handling ([Procedure 04](../procedures/04-AI-Incident-Handling.md); SIMM 5340-A).
6. Completing and attesting SIMM 5305-F and SIMM 150; entering AI risks in the SIMM 5305-B Risk Register.

## Module G: Committee, delegates and Triage Panel (about 60 minutes)
1. Decision rights, quorum, conflicts of interest and no veto ([Charter](../policy/AI-Governance-Committee-Charter.md); ADR-0001).
2. Reading an Assessment Package; asking for what is missing instead of deferring.
3. Rating Scales, risk tolerance and who accepts residual risk (ADR-0005).
4. Conditions that work: specific, owned, dated and checkable.
5. Recording decisions and reasons on the Decision Record.
