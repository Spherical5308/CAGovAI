# Procedure 01: AI Request and Approval

| | |
|---|---|
| **Authority** | [AI Governance Policy](../policy/AI-Governance-Policy.md) sections 4.1–4.8; SAM 4986.3, 4986.6, 4986.7, 4986.9; SIMM 5305-F, 150, 5310-C |
| **Owner** | AI Governance Coordinator |
| **Effective date** | [date] |
| **Map** | [PROCEDURE-MAP.md](../PROCEDURE-MAP.md) steps 1–14 |

## 1. Purpose
How a business unit gets approval to use AI, from first idea to an approved **Request ID**.

## 2. When to use this procedure
Use it whenever a Use Case is not **Pre-approved**: the Tool is new, the use is outside the Tool's **Approved Uses**, or any **Trigger** in the [Data and Tier Floor Standard](../standards/Data-and-Tier-Floor-Standard.md#2-triggers) applies. It also applies to:
- renewals or upgrades that add GenAI features (SIMM 5305-F requires a new assessment when new GenAI features are enabled);
- a vendor's GenAI disclosure under SCM Vol. 2 Ch. 23 (the Procurement Officer opens the Request);
- registering a **Legacy Use** during the 90-day window.

## 3. Steps

### Stage A: Pre-approved check
| Step | Who | Action |
|---|---|---|
| A1 | Requester | Look up the Tool in the [AI Inventory](../inventory/) and its [Approved Uses Register](../forms/Approved-Uses-Register.md). |
| A2 | Requester | If the use is listed and no Trigger applies, confirm training and Acceptable Use acknowledgment are current. |
| A3 | Manager | Attest in the Pre-approved log (name, Tool, Approved Use, unit, date). Use may begin. **End.** |

### Stage B: Submit and screen
| Step | Who | Action | Target |
|---|---|---|---|
| B1 | Requester | Submit the [Intake Form](../forms/Intake-Form.md) through [channel]. Business owner must be at manager level or above. | — |
| B2 | Coordinator | Check completeness. Return incomplete Requests with a list of what is missing. Assign a Request number. | 2 business days |
| B3 | Coordinator | Run the [Prohibited-Use Screen](../forms/Intake-Form.md#part-c-prohibited-use-screen). | with B2 |
| B4 | Chief Counsel | If any screen answer is "Yes" or "Unsure", confirm or clear within 5 business days. If confirmed: **Prohibited**, Request closed, reasons recorded. Requester may appeal to the Committee within 20 business days. | 5 business days |

### Stage C: Triage
| Step | Who | Action | Target |
|---|---|---|---|
| C1 | Coordinator | Apply the Tier Floors and Autonomy Level to set a **provisional Risk Tier**. | 3 business days |
| C2 | Coordinator | Issue the Assessment Package checklist for that tier (section 5) and name the reviewers. | with C1 |
| C3 | Coordinator | If the Request is a proof of concept, confirm a CDT-approved sandbox and public data only (SAM 4986.6). | with C1 |

### Stage D: Assess
| Step | Who | Action |
|---|---|---|
| D1 | Requester + CIO's team | Complete SIMM 5305-F Part 1 (or SIMM 150 if every use falls in a general office productivity category). Complete Part 2 if the result is Moderate or High. |
| D2 | ISO | Complete the FIPS 199 categorisation in SIMM 5305-F. |
| D3 | Privacy Officer | Complete or review the SIMM 5310-C PTA, and the PIA if required. |
| D4 | Requester | Complete the remaining items for the tier (section 5). |
| D5 | CIO + ISO | Sign SIMM 5305-F / 150 as an **Assessment Attestation**. |
| D6 | CIO | Send a copy of the SIMM 5305-F to the Labor Relations Officer and tick the Labor Relations acknowledgment. |
| D7 | Coordinator | Confirm the package is complete. The **final Risk Tier** is the highest of the SIMM 5305-F result and the Tier Floors. Turnaround clock starts. |
| D8 | Coordinator | Submit the SIMM 5305-F / 150 to CDT through the New Technology Consultation and Assessment request in the CDT IT Service Portal (all tiers, *(EB)*). |

### Stage E: Decide
| Tier | Who | Action | Target |
|---|---|---|---|
| Low | Triage Panel | Approve, approve with conditions, reject, or escalate to the Committee. Record on the [Decision Record](../forms/Decision-Record.md). Placed on the next Committee consent agenda. | 10 business days |
| Moderate | Committee | Vote under the [Charter](../policy/AI-Governance-Committee-Charter.md#4-decisions). If approved, complete CDT consultation before any contract award (SAM 4986.9). | 30 business days |
| High | Committee → Director | Committee votes a recommendation. Complete CDT consultation. Director approves or rejects; Director may consult the parent Agency. | 60 business days |

If the ISO dissents on an approved item, the approval waits for a Director-signed [Risk Acceptance](../forms/Risk-Acceptance.md).

### Stage F: Approve and act
| Step | Who | Action |
|---|---|---|
| F1 | Coordinator | Issue the **Request ID**. Create or update the Tool and Use Case records in the AI Inventory, with conditions, owners and Re-review date. |
| F2 | Procurement | Accept the Request ID on the requisition. Include GenAI disclosure language and GenAI special provisions (SAM 4986.9; SCM Vol. 2 Ch. 23). Complete SIMM 71B if required. |
| F3 | CIO / PMO | For an IT project, follow SIMM 19H Project Delivery Lifecycle (SAM 4986.7, 4986.8). |
| F4 | Requester | Before go-live, show the Coordinator that every approval condition is met and that required public disclosures are in place (GC 11549.66). |
| F5 | Coordinator | Mark the Use Case **Active**. |

## 4. New Tools and Approved Uses
A Request that introduces a Tool also proposes that Tool's **Approved Uses**, using the [Approved Uses Register](../forms/Approved-Uses-Register.md). The Tool is tiered on its riskiest Approved Use. Once approved, any later Use Case inside those Approved Uses with no Trigger is Pre-approved. Adding or widening an Approved Use is a Committee decision.

## 5. Assessment Package
Each tier includes everything from the tiers to its left.

| Item | Pre-approved | Low | Moderate | High | Owner |
|---|:-:|:-:|:-:|:-:|---|
| Acceptable Use acknowledgment and role training (SAM 4986.12–.13) | ● | ● | ● | ● | Requester |
| [Intake Form](../forms/Intake-Form.md) | | ● | ● | ● | Requester |
| SIMM 5305-F Part 1, or SIMM 150 | | ● | ● | ● | CIO, ISO |
| SIMM 5305-F Part 2 | | | ● | ● | CIO, ISO |
| SIMM 5310-C Privacy Threshold Assessment | | ● | ● | ● | Privacy Officer |
| SIMM 5310-C Privacy Impact Assessment | | | if PTA requires | ● | Privacy Officer |
| [AI Impact Assessment](../forms/AI-Impact-Assessment.md) | | | ● | ● | Requester |
| Security review: SIMM 140, SIMM 141, SIMM 22 (cloud/SaaS) | | | ● | ● | ISO, CIO |
| Vendor evaluation against SAM 4986.9(B) | | | ● (if procured) | ● (if procured) | Procurement, ISO |
| Records retention and export confirmation | | | ● | ● | Records Officer |
| Permission table ([Autonomy Standard](../standards/Autonomy-and-Agent-Standard.md#3-tool-permissions)) | | if A2/A3 | if A2/A3 | if A2/A3 | Requester, CIO |
| [Workforce Impact Assessment](../forms/Workforce-Impact-Assessment.md) | | | if T7 | ● | Requester, Labor Relations |
| Accessibility review | | | if public-facing | ● | Accessibility Coordinator |
| Test plan and results; POC in CDT sandbox, MVP in approved production (SAM 4986.6) | | | | ● | Requester, CIO |
| Monitoring plan ([Procedure 03](./03-Monitoring-and-Re-review.md)) | | | | ● | Requester |
| Public disclosure plan (GC 11549.66) | | | if public-facing | ● | Requester |
| High-risk automated decision system inventory fields | | | | ● | Coordinator |

## 6. Records
The Request, Assessment Package, decision and Request ID are kept with the Use Case record. Completed SIMM 5305-F, SIMM 150 and security reviews are confidential (GC 7929.210) and are kept in a restricted location.
