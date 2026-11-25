# CAGovAI: AI Governance Framework for California State Entities

An open, adoptable AI governance framework for California State Entities: policy, committee charter, standards, procedures, forms, assessments and an AI inventory, built around one workflow for a business unit to request, assess, approve and monitor a use of AI, from everyday office GenAI to autonomous agents in IT.

It is grounded in California law and policy (EO N-12-23, SAM 4986, SIMM 5305-F / 150 / 5310-C, CDT TL 25-01, GC 11546.45.5, GC 11549.66) and the NIST AI Risk Management Framework.

> **Status:** First full draft. Ready for review and adaptation; not yet adopted by any State Entity.
>
> This is not legal advice and is not an official State of California publication. Check every citation against the current SAM, SIMM, SCM and Government Code before adopting.

## Start here

| Document | What it is |
|---|---|
| [PROCEDURE-MAP.md](./PROCEDURE-MAP.md) | The whole process on a few pages: flowcharts, routing rules, tier matrix, step table |
| [GLOSSARY.md](./GLOSSARY.md) | The defined terms every document uses |
| [docs/adr/](./docs/adr/) | Short records of the key design decisions and why |
| [references/Authority-Crosswalk.md](./references/Authority-Crosswalk.md) | Where each SAM, SIMM, Government Code and NIST AI RMF requirement is met |

## The document set

| Type | Document |
|---|---|
| Policy | [AI Governance Policy](./policy/AI-Governance-Policy.md) |
| Charter | [AI Governance Committee Charter](./policy/AI-Governance-Committee-Charter.md) |
| Standard | [Acceptable Use](./standards/Acceptable-Use-Standard.md) · [Data and Tier Floor](./standards/Data-and-Tier-Floor-Standard.md) · [Autonomy and Agent](./standards/Autonomy-and-Agent-Standard.md) |
| Procedure | [01 Request and Approval](./procedures/01-Request-and-Approval.md) · [02 AI Inventory](./procedures/02-AI-Inventory.md) · [03 Monitoring and Re-review](./procedures/03-Monitoring-and-Re-review.md) · [04 AI Incident Handling](./procedures/04-AI-Incident-Handling.md) · [05 Exceptions](./procedures/05-Exceptions.md) |
| Form | [Intake Form](./forms/Intake-Form.md) · [Approved Uses Register](./forms/Approved-Uses-Register.md) · [Decision Record](./forms/Decision-Record.md) · [Risk Acceptance](./forms/Risk-Acceptance.md) · [Exception Request](./forms/Exception-Request.md) |
| Assessment | [AI Impact Assessment](./forms/AI-Impact-Assessment.md) · [Workforce Impact Assessment](./forms/Workforce-Impact-Assessment.md) · [Rating Scales](./forms/Rating-Scales.md) for Likelihood, Severity and Risk Rating · plus State forms SIMM 5305-F, SIMM 150, SIMM 5310-C (linked, not copied) |
| Inventory | [AI Inventory templates and field guide](./inventory/) |
| Word and Excel | [Fillable Word versions of every form and assessment](./forms/word/) · [AI Inventory workbook](./inventory/AI-Inventory.xlsx) |

## Key design choices
- **One front door for all AI**, with GenAI requirements layered on ([ADR-0002](./docs/adr/0002-one-front-door-for-all-ai.md)).
- **Approve Tools once**; individual uses only need a Request when a Trigger is hit ([ADR-0003](./docs/adr/0003-approve-tools-once-uses-by-trigger.md)).
- **Risk Tiers follow SIMM 5305-F** (Low / Moderate / High), plus Prohibited and Pre-approved.
- **A multidisciplinary committee decides by majority.** InfoSec votes but cannot veto; a dissent requires a Director-signed Risk Acceptance ([ADR-0001](./docs/adr/0001-iso-votes-but-cannot-veto.md)).
- **Procurement is the enforcement gate** ([ADR-0004](./docs/adr/0004-procurement-gate-requires-request-id.md)).
- **Only the Director accepts a High residual risk**, following SAM 5305.1, SIMM 5305-B and NIST AI RMF ([ADR-0005](./docs/adr/0005-director-accepts-high-residual-risk.md)).

## Adopting it
Replace bracketed placeholders such as `[State Entity]` with your own names. Sections marked *(EB)* rest on SAM chapters that bind Executive Branch State Entities. Constitutional offices and other non-Executive Branch entities should adopt the whole framework and swap in their own authority; several GenAI chapters (SAM 4986.4, .9, .10, .11) apply to every State Entity anyway. See the [Non-Executive Branch adoption note](./docs/Non-Executive-Branch-Adoption.md).

## Contributing
Corrections from practitioners keep this accurate as law and policy change. See [CONTRIBUTING.md](./CONTRIBUTING.md), the [Code of Conduct](./CODE_OF_CONDUCT.md) and, for anything sensitive, [SECURITY.md](./SECURITY.md). Changes are listed in the [CHANGELOG](./CHANGELOG.md).

## License
- Documents, forms and templates: [Creative Commons Attribution 4.0 International](./LICENSE) (CC BY 4.0).
- Scripts and code, if any: [MIT](./LICENSE-CODE).

Attribution for adapted third-party material is in [NOTICE.md](./NOTICE.md).
