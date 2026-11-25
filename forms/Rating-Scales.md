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

## Risk tolerance and who accepts residual risk
This table is [State Entity]'s documented **AI risk tolerance**. NIST AI RMF expects each organisation to set and document its own tolerance (GOVERN 1.3, MAP 1.5), and SAM 5305.6 requires "a clear expression of risk tolerance for the organization". Adjust it if your entity's tolerance differs.

The Director is accountable for all risks to [State Entity] (SAM 5305.1; SIMM 5305-B), and NIST AI RMF GOVERN 2.3 places decisions about AI risk with executive leadership. Under the [Committee Charter](../policy/AI-Governance-Committee-Charter.md), the Triage Panel and the Committee decide on the Director's behalf for Low and Moderate Requests, so they accept residual risk within this tolerance as part of their decision. Anything above it goes to the Director.

| Residual Level | Within tolerance? | Handling | Accepted by, and where it is recorded |
|---|---|---|---|
| Low | Yes | Accept. Monitor through normal Re-review. | The decider for the Request's tier, as part of the decision. Recorded in the assessment. |
| Medium | Yes, with controls | Accept only with a named owner for each mitigation and a measure in the monitoring plan, checked at Re-review (NIST AI RMF MANAGE 1.3, MANAGE 1.4). | The decider for the Request's tier, as part of the decision. Recorded on the Decision Record, with the risk owner named. |
| High | No | Do not proceed until the risk is brought to Medium or below; NIST AI RMF says development and deployment "should cease in a safe manner until risks can be sufficiently managed". The usual answer is "Proceed with conditions" that bring it down before go-live. | Only the Director can accept a High residual risk, in writing on the Decision Record, for a set period no longer than the next Re-review. |

Information security and privacy risks that remain at Medium or High also go on [State Entity]'s Risk Register and Plan of Action and Milestones (SIMM 5305-B), kept by the ISO, with a risk owner and review date (SAM 4986.11, SAM 5305.1). SIMM 5305-B rates risks on a five-level scale (Very Low to Very High, after NIST SP 800-30). When the ISO enters an AI risk there, map Low to Low, Medium to Moderate and High to High, and use the register's own chart if it gives a different result.

A recorded dissent by the ISO (or by the Privacy Officer or Chief Counsel on a matter within their legal duties) is handled separately: the approval waits for a Director-signed [Risk Acceptance](./Risk-Acceptance.md) whatever the Level (Committee Charter, section 4.3).
