# Authority Crosswalk

Where each State requirement and NIST AI RMF function is met in this framework. Check every citation against the current official text before adoption; SAM and SIMM are revised often.

## California law and policy
| Authority | Requirement (summary) | Where met |
|---|---|---|
| Executive Order N-12-23 | Safe, ethical, responsible GenAI adoption; workforce support | [Policy](../policy/AI-Governance-Policy.md) §1, §3; [Workforce Impact Assessment](../forms/Workforce-Impact-Assessment.md) |
| GC 11546.45.5 (AB 302) | CDT inventories high-risk automated decision systems and reports annually to the Legislature; each state agency files CDT's data collection, even if it has none | [Procedure 02](../procedures/02-AI-Inventory.md) §6; inventory field `high_risk_ads` |
| GC 11549.63–11549.66 (SB 896) | GenAI risk analysis; disclaimer and human-contact information when GenAI communicates directly about services and benefits (the opt-out comes from SAM 4986.10). AB 2412 (2025–26) would widen 11549.66 to all public communications; check its status | [Policy](../policy/AI-Governance-Policy.md) §4.9; [Acceptable Use Standard](../standards/Acceptable-Use-Standard.md) §3.4; [Autonomy Standard](../standards/Autonomy-and-Agent-Standard.md) §6 |
| Civil Code 3110–3111 (AB 2013) | Developers post training-data documentation for public GenAI; SAM 4986.4 applies the duty to State Entities and Civil Code 3111 supplies the required elements | [Procedure 02](../procedures/02-AI-Inventory.md) §6 |
| AB 2885; SAM 4819.2 | Definition of AI | [Glossary](../GLOSSARY.md) "AI" |
| Civil Code 1798 et seq. (Information Practices Act) | Protect personal information | [Data and Tier Floor Standard](../standards/Data-and-Tier-Floor-Standard.md) |
| GC 7920.000 et seq. (CPRA); GC 12270–12279 (State Records Management Act); SAM 1600 | Public records and retention | [Policy](../policy/AI-Governance-Policy.md) §4.10 |
| GC 7929.210; GC 8592.45 | Information security records exempt where disclosure would reveal vulnerabilities (case by case) | [Procedure 01](../procedures/01-Request-and-Approval.md) §6; [Procedure 02](../procedures/02-AI-Inventory.md) §6 |
| GC 11135; GC 11546.7 | Non-discrimination and accessibility | [Acceptable Use Standard](../standards/Acceptable-Use-Standard.md) P6; accessibility review in Assessment Package |
| GC 3512 et seq. (Dills Act) | Meet-and-confer on matters within scope of representation | [Workforce Impact Assessment](../forms/Workforce-Impact-Assessment.md) §3 |
| SAM 4986.1–.2 | Scope and definitions | [Policy](../policy/AI-Governance-Policy.md) §2 |
| SAM 4986.3 | Identify GenAI uses; inventory high-risk uses; submit to CDT on request | [Procedure 01](../procedures/01-Request-and-Approval.md); [Procedure 02](../procedures/02-AI-Inventory.md) |
| SAM 4986.4 | Training-data transparency posting | [Procedure 02](../procedures/02-AI-Inventory.md) §6 |
| SAM 4986.5; SAM 4983.1; SIMM 22, 140, 141 | Cloud and hosting requirements | [Policy](../policy/AI-Governance-Policy.md) §4.8; security review in Assessment Package |
| SAM 4986.6 | POC in CDT sandbox with public data; MVP in approved production | [Policy](../policy/AI-Governance-Policy.md) §4.8; [Procedure 01](../procedures/01-Request-and-Approval.md) C3 |
| SAM 4986.7–.8; SIMM 19H, 45 | Assessments before IT projects; Project Delivery Lifecycle | [Procedure 01](../procedures/01-Request-and-Approval.md) F3 |
| SAM 4986.9(A); SCM Vol. 2 Ch. 23; SIMM 71B | GenAI procurement: disclosure clause, 5305-F before award, CDT consult for Moderate/High, PTA/PIA, multidisciplinary governance team | [Policy](../policy/AI-Governance-Policy.md) §4.6–4.7; [Charter](../policy/AI-Governance-Committee-Charter.md) §1; ADR-0004 |
| CDT PS-033 (6/30/2026) | SITeS GenAI office-productivity procurement: Low not submitted to CDT; Moderate reviewed; High mandatory consultation | [Procedure 01](../procedures/01-Request-and-Approval.md) §4 |
| SAM 4986.9(B) | Vendor evaluation for Moderate/High | Assessment Package "Vendor evaluation" |
| SAM 4986.10 | Privacy and disclosure | [Data and Tier Floor Standard](../standards/Data-and-Tier-Floor-Standard.md) §4; [Policy](../policy/AI-Governance-Policy.md) §4.9 |
| SAM 4986.11; SIMM 5340-A, 5340-C; SAM 5335 | Incident reporting; NIST AI RMF; risk register; SSP; monitoring; Zero Trust | [Procedure 03](../procedures/03-Monitoring-and-Re-review.md); [Procedure 04](../procedures/04-AI-Incident-Handling.md) |
| SAM 4986.12 | Acceptable use; prohibited content; human verification | [Acceptable Use Standard](../standards/Acceptable-Use-Standard.md) |
| SAM 4986.13 | Role-based GenAI training | [Acceptable Use Standard](../standards/Acceptable-Use-Standard.md) §2; [Workforce Impact Assessment](../forms/Workforce-Impact-Assessment.md) §5 |
| SAM 5305.5 | Inventory and classify information assets; FIPS 199 categorisation; personal and medical information at least FIPS 199 Moderate | [Data and Tier Floor Standard](../standards/Data-and-Tier-Floor-Standard.md) §1 |
| SIMM 5305-F | GenAI risk assessment, all tiers; Part 2 for Moderate/High; CIO/ISO signatures; Labor Relations copy; CDT submission by tier and route | [Procedure 01](../procedures/01-Request-and-Approval.md) Stage D; ADR-0001 |
| SIMM 150 | Office-productivity GenAI assessment | [Procedure 01](../procedures/01-Request-and-Approval.md) D1; [Approved Uses Register](../forms/Approved-Uses-Register.md) |
| SIMM 5310-C | Privacy Threshold and Impact Assessments | [Data and Tier Floor Standard](../standards/Data-and-Tier-Floor-Standard.md) §4 |

## NIST AI Risk Management Framework (AI 100-1)
| Function | What it asks | Where met |
|---|---|---|
| **Govern** | Policies, accountability, roles, culture, third-party risk | [Policy](../policy/AI-Governance-Policy.md); [Charter](../policy/AI-Governance-Committee-Charter.md); [Autonomy Standard](../standards/Autonomy-and-Agent-Standard.md); vendor evaluation |
| **Map** | Context, intended use, affected people, risk categorisation | [Intake Form](../forms/Intake-Form.md); [AI Impact Assessment](../forms/AI-Impact-Assessment.md) §1–2, §4; Tier Floors |
| **Measure** | Test, evaluate, track metrics, including bias and robustness | [AI Impact Assessment](../forms/AI-Impact-Assessment.md) §3; [Procedure 03](../procedures/03-Monitoring-and-Re-review.md) §2 |
| **Manage** | Prioritise and act on risk, respond to incidents, decommission | Decision tiers; [Risk Acceptance](../forms/Risk-Acceptance.md); [Procedure 03](../procedures/03-Monitoring-and-Re-review.md); [Procedure 04](../procedures/04-AI-Incident-Handling.md) |

NIST AI 600-1 (Generative AI Profile) risk areas are the rows of the [AI Impact Assessment](../forms/AI-Impact-Assessment.md) §4 harm table.

## Comparative references (cited, not copied)
- State of Indiana: AI Policy; State Agency AI Systems Standard; OCDO Procedure for Review of AI Submissions (v1.3, 2026): risk-scored intake routed to a multidisciplinary review team.
- State of Oregon: Responsible AI Usage Policy and attachments A–G; Copilot General Usage Procedure 107-004-200_PR: audience-based use matrix (basis for our Approved Uses Register audience columns).
- City of San José: AI policy and playbook.
- U.S. GAO-21-519SP: AI Accountability Framework (governance, data, performance, monitoring).
