# Rating Scales: Likelihood, Severity and Risk Level

> Use these scales wherever an AI form asks for **Likelihood**, **Severity** (or Impact) or a risk **Level**: the [AI Impact Assessment](./AI-Impact-Assessment.md) sections 4 and 7, the [Risk Acceptance](./Risk-Acceptance.md) section 2, and the [Exception Request](./Exception-Request.md) section 3. The Word versions of those forms print these scales at the end.
>
> These scales are this framework's own method. NIST AI RMF and SIMM 5305-F do not prescribe one, so [State Entity] may adjust them. They rate a single risk. They are **not** the Request's Risk Tier (Low / Moderate / High), which comes from SIMM 5305-F and the Tier Floors; to keep the two apart, these scales say **Medium**, never "Moderate".

## How to rate
1. Describe the harm in one or two sentences: who is hurt, how, and the worst *credible* outcome (not the worst imaginable).
2. Rate **Likelihood** with the controls that are already in place, before the new mitigations you are proposing.
3. Rate **Severity** for the worst credible outcome. If more than one column of the Severity table applies, use the highest.
4. Read the **Level** from the matrix.
5. Describe the mitigation, then rate Likelihood and Severity again to get the **residual Level**.
6. If you are torn between two levels, choose the higher one and give your reason in a sentence.

## Likelihood
Over the approval period, that is, until the next Re-review.

| Level | Meaning | Typical signs |
|---|---|---|
| Low | Unlikely. It would take several controls failing at once, or deliberate misuse. | Not seen in testing. Not reported for similar tools. Every output is checked by a qualified person before it is used. |
| Medium | Could happen. One control failing, or ordinary human error, would allow it. | Seen now and then in testing, or reported for similar tools. Outputs are spot-checked rather than all reviewed. Many users, or users new to the tool. |
| High | Expected, or already happening, without the proposed mitigation. | Seen repeatedly in testing or a pilot. A known weakness of this kind of AI, such as fabricated citations in open-ended drafting or prompt injection in an agent that reads outside content. Outputs used without review. Autonomy Level A2 or A3. |

## Severity (Impact)
Use the highest column that applies.

| Level | People | Data and systems | Service, legal and public trust |
|---|---|---|---|
| Low | Minor inconvenience, easily put right. No effect on anyone's rights, benefits, services, employment, health or safety. | No Confidential/Sensitive or Personal data exposed. No effect on any system. | Small rework or delay, inside the unit. No legal exposure. Not visible to the public. |
| Medium | A person or group is affected, but it can be fully corrected: a delayed service, a wrong answer that is caught and fixed, a difference in service quality that is reversed. | Limited exposure of Internal or Confidential/Sensitive data, or of a few people's personal information where no breach notice is required. Short outage of a non-critical system. | Noticeable rework, cost or disruption. Complaints. Inaccurate public information that is corrected quickly. A breach of internal policy. |
| High | Serious or hard to reverse: a wrong decision about a person's rights, benefits, liberty, employment, health or safety; unlawful discrimination; harm to children. | Exposure of Personal, Confidential/Sensitive or Federally restricted data (FTI, CJI, PHI) that may require breach notification (Civil Code 1798.29) or incident reporting (SIMM 5340-A). Compromise of a system, account or agent credential. | Breach of law or of a mandatory SAM/SIMM requirement. Widespread misinformation. Significant financial loss. Litigation likely. Serious loss of public trust. |

## Level matrix
| Likelihood ↓ · Severity → | Low | Medium | High |
|---|---|---|---|
| **Low** | Low | Low | Medium |
| **Medium** | Low | Medium | High |
| **High** | Medium | High | High |

## What a residual Level means for the decision
This handling is a recommendation of this framework, not a requirement of law or SAM/SIMM.

| Residual Level | Recommended handling | Accepted by |
|---|---|---|
| Low | Accept. Record it in the assessment. | The Use Case owner |
| Medium | Accept only with a named owner for each mitigation and a measure in the monitoring plan, checked at Re-review. | The decider for the Request's tier (Triage Panel, Committee, or Director for High) |
| High | Recommend "Do not proceed", or "Proceed with conditions" that bring it to Medium before go-live. If the decider still approves, record the reasons on the Decision Record. | The Director, and a Risk Acceptance if a voting seat dissents |
