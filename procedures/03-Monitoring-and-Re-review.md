# Procedure 03: AI Monitoring and Re-review

| | |
|---|---|
| **Authority** | [AI Governance Policy](../policy/AI-Governance-Policy.md) section 4.12; SAM 4986.9(A), 4986.11, 5335; SIMM 5305-F; NIST AI 100-1 Measure and Manage functions |
| **Owner** | AI Governance Coordinator; each Use Case owner |
| **Effective date** | [date] |
| **Map** | [PROCEDURE-MAP.md](../PROCEDURE-MAP.md) steps 15, 16 |

## 1. Purpose
Make sure an approved Use Case keeps working as approved, and that its approval is revisited when it is due or when something important changes (SAM 4986.11(C): continuously oversee and monitor new, ongoing and changing risks).

## 2. Monitoring
| What | Low | Moderate | High | Who |
|---|:-:|:-:|:-:|---|
| Security monitoring and logging per SAM 5335; logs to SIEM where the Tool supports it | ● | ● | ● | ISO |
| User-reported issues (wrong, harmful or biased output) through [channel] | ● | ● | ● | Use Case owner |
| Approval conditions tracked to closure | ● | ● | ● | Coordinator |
| Quality sampling: a qualified person reviews a defined sample of outputs | | ● monthly | ● weekly | Use Case owner |
| Accuracy, error and bias metrics against the thresholds in the AI Impact Assessment | | ● | ● | Use Case owner |
| Vendor changes: model, version, terms, subprocessors, data location | | ● | ● | Procurement, CIO |
| Public feedback and appeals of AI-assisted outcomes | | if public-facing | ● | Use Case owner |
| Monitoring report to the Coordinator | | Semi-annual | Quarterly | Use Case owner |

A2 and A3 Use Cases also follow the sampling and logging controls in the [Autonomy and Agent Standard](../standards/Autonomy-and-Agent-Standard.md#4-required-controls-by-level).

## 3. Re-review
### 3.1 Scheduled
| Tier | Re-review |
|---|---|
| Low | Only on a Material Change |
| Moderate | Every 2 years |
| High | Every year |

The Coordinator notifies the Use Case owner 60 days before a scheduled Re-review.

### 3.2 Material Changes
The Use Case owner reports any of these to the Coordinator within 5 business days, and **before** the change where it can be planned:
1. a new model, model version or vendor;
2. new GenAI features enabled (SIMM 5305-F requires a new assessment);
3. a new data class or data source;
4. a new or wider audience, including becoming public-facing;
5. a higher Autonomy Level, or a new Allowed action in the permission table;
6. a change in purpose;
7. an incident, or monitoring results outside the approved thresholds;
8. a change in law or State policy the Coordinator identifies.

### 3.3 How a Re-review runs
1. The Coordinator re-runs triage (Procedure 01, Stage C) with updated information.
2. The owner updates only the parts of the Assessment Package the change affects. A new SIMM 5305-F is required for items 1–3 and 5 above.
3. The same decider as the (new) tier decides: continue, continue with conditions, suspend, or retire.
4. The Coordinator updates the AI Inventory and sets the next Re-review date.

A Use Case that misses its Re-review by more than 60 days is placed on the Committee agenda for possible Suspension.
