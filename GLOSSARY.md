# California State Entity AI Governance

The language used across this repository's policy, procedures, forms and inventory for governing how a California State Entity requests, assesses, approves and monitors uses of AI.

## Organisation

**State Entity**:
A California department, board, commission or office that adopts this governance framework; the level at which governance decisions are made (SAM 4986.2).
_Avoid_: Agency (when meaning a department), department, organisation

**Agency**:
The parent super-agency over a State Entity (e.g. GovOps, CalHHS); an optional escalation point for High-risk decisions, never the default decider.
_Avoid_: using "Agency" to mean the State Entity itself

**AI Governance Committee**:
The multidisciplinary body of a State Entity that decides on AI requests by majority vote of its voting seats.
_Avoid_: AI board, review board, steering committee

**Voting Seat**:
A committee seat whose holder votes: Executive Sponsor (chair), Business/Program representative, Chief Counsel, Privacy Officer, CIO, ISO.
_Avoid_: member (ambiguous with advisory)

**Advisory Seat**:
A committee seat that informs but does not vote: HR/Labor Relations, Accessibility, Records Management, Procurement.
_Avoid_: non-voting member, observer

**AI Governance Coordinator**:
The role in the CIO's office that receives every Request, runs screening and triage, prepares the committee agenda and maintains the AI Inventory.
_Avoid_: AI program office, intake desk, gatekeeper

**Triage Panel**:
The Coordinator plus ISO and Privacy Officer designees, who decide Low-tier Requests and report them to the committee as a consent agenda.
_Avoid_: subcommittee, working group

**Risk Acceptance**:
A Director-signed record accepting residual risk, required when a request is approved over the ISO's recorded dissent.
_Avoid_: waiver, exception

**Assessment Attestation**:
The CIO's and ISO's signatures on SIMM 5305-F / SIMM 150, attesting the assessment is complete and its risks accurately stated; it is not an approval.
_Avoid_: sign-off, ISO approval

## What is governed

**AI**:
Any engineered or machine-based system as defined in AB 2885 / SAM 4819.2, including but not limited to GenAI and automated decision systems.
_Avoid_: GenAI (when meaning all AI)

**GenAI**:
AI that generates derived synthetic content (GC 11549.64); triggers the additional SAM 4986 requirements.
_Avoid_: LLM, chatbot (as synonyms)

**Tool**:
A specific AI product or system the State Entity licenses, builds or enables (e.g. an enterprise copilot), approved once with a list of Approved Uses.
_Avoid_: platform, solution, application

**Use Case**:
A specific business purpose for which a business unit applies a Tool.
_Avoid_: use, project, request (the Request is the vehicle; the Use Case is the subject)

**Approved Use**:
A category of Use Case pre-authorised for a given Tool, needing no Request as long as no Trigger is hit.
_Avoid_: allowed use, whitelisted use

**Trigger**:
A condition that takes a Use Case outside its Tool's Approved Uses and requires a Request (e.g. sensitive/personal data, public-facing output, decisions about people, autonomous action).
_Avoid_: red flag, escalation criterion

**Request**:
A business unit's formal submission seeking approval of a Use Case (and, if needed, a new Tool).
_Avoid_: intake (the step), ticket, application

## Risk

**Risk Tier**:
The outcome of triage and assessment: Prohibited, Pre-approved, Low, Moderate or High. Low/Moderate/High match SIMM 5305-F.
_Avoid_: risk level, category, class

**Prohibited**:
A Risk Tier for Use Cases the State Entity may not pursue (e.g. SAM 4986.12 banned uses); the Request stops at screening.
_Avoid_: rejected (a Request can be rejected at any tier)

**Pre-approved**:
A Risk Tier for a Use Case inside an Approved Use of an approved Tool; it is registered, not reviewed.
_Avoid_: exempt, low-risk

**Autonomy Level**:
How far a Use Case lets AI act without a person: A0 Assist, A1 Draft, A2 Act with approval, A3 Act autonomously.
_Avoid_: agent vs. non-agent, automation level

**Tier Floor**:
The minimum Risk Tier a Trigger forces regardless of other answers (e.g. personal data sets a floor of Moderate).
_Avoid_: override, bump

## Lifecycle

**Assessment Package**:
The cumulative set of forms and assessments a Risk Tier requires; each tier's package contains the tier below's.
_Avoid_: submission, paperwork

**Request ID**:
The identifier of an approved Request, required on any AI-related purchase requisition or solicitation.
_Avoid_: approval number, ticket number

**Legacy Use**:
A Use Case already in operation before adoption, registered during the 90-day registration window and allowed to continue under review unless Prohibited.
_Avoid_: grandfathered, amnesty item

**Re-review**:
A fresh committee or panel decision on an approved Use Case, due on schedule (High yearly, Moderate every 2 years) or on a Material Change.
_Avoid_: recertification, renewal

**Material Change**:
A change that forces Re-review: new model or version, new data, new audience, higher Autonomy Level, or an incident.
_Avoid_: update, modification

**Suspension**:
An immediate, temporary stop of an approved Use Case by the ISO or CIO, which the committee confirms or lifts within 10 business days; not a veto.
_Avoid_: shutdown, revocation

**Exception**:
A time-limited (max 12 months) committee-approved, Director-signed departure from a Standard, never from the Policy.
_Avoid_: waiver, Risk Acceptance (which accepts risk, not a departure from a Standard)

**AI Inventory**:
The single register of Tool records and linked Use Case records from which the CDT high-risk export and the public transparency page are produced.
_Avoid_: AI register, catalogue, ADS list
