# CAGovAI

An open, adoptable AI governance framework for California State Entities: policy, committee charter, standards, procedures, forms, assessments and an AI inventory, built around one workflow for a business unit to request, assess, approve and monitor a use of AI, from everyday office GenAI to autonomous agents in IT.

It is grounded in California law and policy (EO N-12-23, SAM 4986, SIMM 5305-F / 150 / 5310-C, CDT TL 25-01, GC 11546.45.5, GC 11549.66) and the NIST AI Risk Management Framework.

> **Status:** Foundation. The procedure map is the agreed design; the policy, procedures and forms are being drafted from it.
>
> This is not legal advice and is not an official State of California publication. Check every citation against the current SAM, SIMM, SCM and Government Code before adopting.

## Start here

| Document | What it is |
|---|---|
| [PROCEDURE-MAP.md](./PROCEDURE-MAP.md) | The whole process: flowcharts, routing rules, tier matrix, step table, document set |
| [GLOSSARY.md](./GLOSSARY.md) | The defined terms every document uses |
| [docs/adr/](./docs/adr/) | Short records of the key design decisions and why |

## Key design choices
- **One front door for all AI**, with GenAI requirements layered on ([ADR-0002](./docs/adr/0002-one-front-door-for-all-ai.md)).
- **Approve Tools once**; individual uses only need a Request when a Trigger is hit ([ADR-0003](./docs/adr/0003-approve-tools-once-uses-by-trigger.md)).
- **Risk Tiers follow SIMM 5305-F** (Low / Moderate / High), plus Prohibited and Pre-approved.
- **A multidisciplinary committee decides by majority.** InfoSec votes but cannot veto; a dissent requires a Director-signed Risk Acceptance ([ADR-0001](./docs/adr/0001-iso-votes-but-cannot-veto.md)).
- **Procurement is the enforcement gate** ([ADR-0004](./docs/adr/0004-procurement-gate-requires-request-id.md)).

## Adopting it
Replace bracketed placeholders such as `[State Entity]` with your own names. Sections marked *(EB)* apply to Executive Branch State Entities; others may adopt them voluntarily.

## License
- Documents, forms and templates: [Creative Commons Attribution 4.0 International](./LICENSE) (CC BY 4.0).
- Scripts and code, if any: [MIT](./LICENSE-CODE).

Attribution for adapted third-party material is in [NOTICE.md](./NOTICE.md).
