# Procedure 04: AI Incident Handling

| | |
|---|---|
| **Authority** | [AI Governance Policy](../policy/AI-Governance-Policy.md) section 4.12; SAM 4986.11(A), 5340; SIMM 5340-A, 5340-C; NIST AI 100-1 Manage 4.3 |
| **Owner** | Information Security Officer |
| **Effective date** | [date] |
| **Map** | [PROCEDURE-MAP.md](../PROCEDURE-MAP.md) step 17 |

## 1. Purpose
AI incidents run through [State Entity]'s existing Incident Response Plan and Playbook (SAM 4986.11). This procedure adds what is specific to AI: what counts as an AI incident, the power to suspend, and how the Committee is involved.

## 2. What is an AI incident
Any actual or suspected event in which an AI Tool or Use Case:
1. exposes, leaks or mishandles State data, including entry of confidential, sensitive or personal data into an unapproved Tool;
2. is manipulated (prompt injection, jailbreak, poisoned data or retrieval sources, compromised agent credentials);
3. takes an action outside its approved permission table or limits;
4. produces output that causes, or could cause, harm: a wrong decision about a person, unlawful discrimination, unsafe guidance, defamatory or fabricated content released publicly;
5. is used for a Prohibited purpose, or without approval after the Legacy Use window;
6. fails in a way that disrupts a public service.

Newly identified AI threats and tactics, techniques and procedures are also reported (SAM 4986.11(A)).

## 3. Steps
| Step | Who | Action | Timing |
|---|---|---|---|
| 1 | Anyone | Report to the ISO / service desk at [contact]. | Immediately |
| 2 | ISO | Open an incident under the Incident Response Plan; classify severity. | Per IR Plan |
| 3 | ISO or CIO | Decide whether to **suspend** the Use Case (disable access, revoke agent credentials, turn off the feature). Either may act alone. | Immediately where harm is ongoing |
| 4 | ISO | Report to oversight agencies (Cal-CSIRS / CDT) as SIMM 5340-A requires. If personal information may be breached, follow SIMM 5340-C with the Privacy Officer. | Per SIMM 5340-A / C |
| 5 | Coordinator | Mark the Use Case Suspended in the AI Inventory; notify the Chair. | Same day |
| 6 | Committee | Confirm the Suspension, lift it, lift it with conditions, or order a Re-review. | Within 10 business days of Suspension |
| 7 | Use Case owner | Where people were affected by AI-assisted outcomes, identify them and, with Chief Counsel, decide on notice and correction. | Per Committee direction |
| 8 | ISO + owner | Post-incident review: root cause, control gaps, changes to the Tool, Use Case, Approved Uses or Standards. | Within 30 days of closure |
| 9 | Coordinator | Record the lessons in the AI Inventory and report to the Committee. | Next meeting |

## 4. Suspension is not a veto
A Suspension is a temporary stop to contain harm. It does not decide whether the Use Case should exist; the Committee does that in step 6 (ADR-0001). If the Committee does not act within 10 business days, the Suspension stays in place and the Chair calls a meeting.

## 5. Vendor incidents
Contracts for Moderate and High Tools require the vendor to report incidents, provide logs and cooperate in investigations (SAM 4986.9(B)). The Procurement Officer tracks vendor notifications and passes them to the ISO the same day.
