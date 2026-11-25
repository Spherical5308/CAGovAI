# Procedure 02: AI Inventory

| | |
|---|---|
| **Authority** | [AI Governance Policy](../policy/AI-Governance-Policy.md) sections 4.9, 4.11; SAM 4986.3, 4986.4, 4986.11(C); GC 11546.45.5; Civil Code 3111 |
| **Owner** | AI Governance Coordinator |
| **Effective date** | [date] |
| **Map** | [PROCEDURE-MAP.md](../PROCEDURE-MAP.md) steps 12, 19, 20 |

## 1. Purpose
Keep one complete, current record of every AI Tool and Use Case at [State Entity], and produce the reports the State and the public need from it.

## 2. What the inventory holds
The [AI Inventory](../inventory/) has two linked record types. Field definitions are in [inventory/README.md](../inventory/README.md).
- **Tool records**: one per AI product or system, with its hosting, GenAI status, Approved Uses and the Request ID that approved it.
- **Use Case records**: one per approved, Legacy, suspended or retired Use Case, linked to its Tool, with Risk Tier, Autonomy Level, data class, audience, owner, Request ID and Re-review date.

Pre-approved uses are logged in a separate Pre-approved log (Tool, Approved Use, unit, manager attestation, date). They are counted, not individually reviewed.

## 3. Keeping it current
| Event | Who | Update |
|---|---|---|
| Request approved | Coordinator | Create or update Tool and Use Case records (Procedure 01, F1) |
| Go-live | Coordinator | Status → Active |
| Material Change reported | Use Case owner | Notify Coordinator within 5 business days; Coordinator opens Re-review |
| Re-review decided | Coordinator | New decision date, tier, next Re-review date |
| Suspension or incident | Coordinator | Status → Suspended; link incident number |
| Exception granted | Coordinator | Record Exception and expiry |
| Retired | Use Case owner | Status → Retired, with retirement date; records kept per retention schedule |

## 4. Legacy Use registration (first 90 days)
1. On the Policy's effective date the Coordinator announces a 90-day registration window to all staff and contractors.
2. Each Deputy Director confirms in writing that their units have registered every AI Tool and Use Case in use, including AI features vendors have added to existing software.
3. The CIO's team runs a discovery sweep (software inventory, SaaS and browser extension logs, expense and P-card records, network logs for known AI services) and sends unregistered findings to the owning unit.
4. Registered Legacy Uses are screened for Prohibited uses within 10 business days. Prohibited Legacy Uses stop immediately. All others continue while they go through triage and assessment on a schedule the Coordinator sets, High first.
5. After 90 days, unregistered AI in use is handled as an information security incident under [Procedure 04](./04-AI-Incident-Handling.md).

## 5. Quality checks
Each quarter the Coordinator:
1. reconciles the inventory against the discovery sweep and the procurement record of Request IDs;
2. lists overdue Re-reviews, open approval conditions and Exceptions expiring in the next 90 days;
3. reports the results to the Committee.

## 6. Reports produced from the inventory
| Report | Content | Audience | When |
|---|---|---|---|
| **High-risk inventory** *(EB)* | High-tier Use Cases and high-risk automated decision systems, one submission per system, with the fields CDT requests; a nil return if there are none | CDT | CDT's annual high-risk ADS data collection, and on request (SAM 4986.3; GC 11546.45.5) |
| **Public AI use summary** | Tool, purpose in plain words, Risk Tier, whether the public interacts with it, contact for questions | Public website | Quarterly |
| **Training-data documentation** | For GenAI that [State Entity] built or substantially modified and makes available to Californians: high-level summary of datasets and the elements Civil Code 3111 requires | Public website | Initially by the SAM 4986.4 date, then annually |
| **Committee dashboard** | Counts by tier and status, turnaround against targets, overdue items | Committee | Quarterly |

Completed SIMM 5305-F, SIMM 150 and security reviews are never included in a public report (SIMM 5305-F marks completed forms confidential and possibly exempt (GC 7929.210, 8592.45); the exemption turns on whether disclosure would reveal vulnerabilities, so Chief Counsel decides on any records request).
