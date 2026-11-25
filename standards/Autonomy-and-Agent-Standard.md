# [State Entity] AI Autonomy and Agent Standard

| | |
|---|---|
| **Authority** | [AI Governance Policy](../policy/AI-Governance-Policy.md); SAM 4986.11, 4986.12; NIST AI 100-1 (Govern 3.2, Map 3.5, Manage 2.4); NIST AI 600-1 |
| **Owner** | Chief Information Officer, with the ISO |
| **Effective date** | [date] |

"Agent" means different things to different vendors. This Standard replaces the word with an **Autonomy Level** that every Request declares, and sets the controls each level needs.

## 1. Autonomy Levels
| Level | Name | What the AI does | What the person does | Examples |
|---|---|---|---|---|
| **A0** | Assist | Answers questions, explains, suggests | Does the work and decides | Chat assistant for research; code explanation |
| **A1** | Draft | Produces content, code or analysis | Reviews and edits before anything is used or sent | Drafting a memo; summarising a meeting; generating a test script |
| **A2** | Act with approval | Proposes and, once approved, carries out actions in systems | Approves each action before it happens | Agent that prepares a ticket update or email and sends it when a person clicks Approve |
| **A3** | Act autonomously | Carries out actions on its own within set limits | Sets limits, monitors, can stop it | Agent that triages and routes tickets, remediates alerts, or runs scheduled workflows without per-action approval |

Declare the **highest** level any part of the Use Case reaches. A Use Case that moves to a higher level is a **Material Change** and needs Re-review.

## 2. Tier Floors from autonomy
See the [Data and Tier Floor Standard](./Data-and-Tier-Floor-Standard.md#3-tier-floors). In summary: A2 or A3 on production systems is at least **Moderate**; A3 touching Confidential/Sensitive or Personal data, or acting toward the public or external parties, is **High**.

## 3. Tool permissions
Every A2 or A3 Use Case submits a **permission table** listing each tool, connector, API or system the AI can reach, and one setting for each:

| Setting | Meaning |
|---|---|
| **Allowed** | The AI may do this without a person. Every action is logged. (A3 only) |
| **With approval** | The AI proposes; a named person approves before it acts. |
| **Denied** | The AI cannot do this; the capability is not connected. |

Default is **Denied**. Actions that send communications outside [State Entity], move money, change access rights, delete data, or change production configuration may not be **Allowed** unless the Committee approves it explicitly.

*(The three-setting model is adapted from the aipolicytracker.org AI Agent Registry template, CC BY 4.0. See [NOTICE.md](../NOTICE.md).)*

## 4. Required controls by level
| Control | A0 | A1 | A2 | A3 |
|---|:-:|:-:|:-:|:-:|
| Approved Tool, State identity, training opt-out | ● | ● | ● | ● |
| Human verification of output before use (SAM 4986.12) | ● | ● | ● | — (replaced by the controls below) |
| Permission table (section 3) | | | ● | ● |
| Agent runs under its own non-human identity with least privilege, never a person's credentials | | | ● | ● |
| Approval step names a specific person; approvals are logged | | | ● | |
| Hard limits: rate, spend, scope, data, and time window | | | ● | ● |
| Stop control: a named person can halt the agent immediately | | | ● | ● |
| Action log in a non-proprietary format, ingested into the SIEM (SIMM 5305-F Part 2; SAM 5335) | | | ● | ● |
| Prompt-injection defences for untrusted inputs (documents, email, web) per the OWASP Top 10 for LLM Applications | | ● | ● | ● |
| Pre-production test in a non-production environment, including adversarial tests (SAM 4986.6) | | | ● | ● |
| Rollback or undo for every Allowed action, or documented reason it is not possible | | | | ● |
| Ongoing sampling: a person reviews a defined sample of autonomous actions each week | | | | ● |
| Named human owner reachable while the agent runs | | | ● | ● |

## 5. Multi-agent and chained systems
Where one AI system calls another, the combined system takes the highest Autonomy Level of any part, and the permission table covers the whole chain. An AI system may not grant itself, or another AI system, permissions beyond its approved table.

## 6. Disclosure
When an A2 or A3 system communicates with people outside [State Entity], it must identify itself as AI, give a way to reach a person, and allow opting out of interacting with AI (GC 11549.66; SAM 4986.10).
