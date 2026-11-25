# AI Inventory

The single register of AI at [State Entity] ([Procedure 02](../procedures/02-AI-Inventory.md)). Three CSV files you can open in any spreadsheet tool or load into a database or SharePoint list:

| File | One row per | Kept by |
|---|---|---|
| [tools.csv](./tools.csv) | approved (or registered Legacy) AI Tool | Coordinator |
| [use-cases.csv](./use-cases.csv) | Use Case, linked to its Tool by `tool_id` | Coordinator |
| [pre-approved-log.csv](./pre-approved-log.csv) | Pre-approved use attested by a manager | Coordinator (from manager attestations) |

The example rows are illustrations; delete them before use. Store the live inventory in an access-controlled location. Only the columns marked **Public** go into the public AI use summary.

## tools.csv
| Field | What to record | Public |
|---|---|:-:|
| `tool_id` | Unique ID, e.g. T-0001 | ● |
| `tool_name` | Common name | ● |
| `vendor` | Supplier, or "In-house" | ● |
| `product_and_model` | Product, model and version (SIMM 5305-F (b), (c)) | |
| `licence_tier` | Free, enterprise, etc. (SIMM 5305-F (d)) | |
| `delivery` | SaaS / PaaS / IaaS / On-premises / Extension / Embedded feature | |
| `hosting` | CDT offering, DGS SLP, CDT-approved data center, etc. (SAM 4986.5) | |
| `is_genai` | Yes / No | ● |
| `approved_data_classes` | Highest data classes approved, `;`-separated | |
| `approved_uses_register` | Link to the Tool's Approved Uses Register | |
| `records_export_confirmed` | Yes / No: can retain and export prompts, outputs and logs | |
| `approval_request_id` | Request ID that approved the Tool | |
| `approval_date` | | |
| `tool_owner` | Accountable person | |
| `status` | Proposed / Active / Suspended / Retired | ● |
| `notes` | | |

## use-cases.csv
| Field | What to record | Public |
|---|---|:-:|
| `use_case_id` | Unique ID, e.g. U-0001 | ● |
| `tool_id` | Links to tools.csv | ● |
| `title` | Short name | ● |
| `purpose_plain_language` | What it does and what output or decision it produces | ● |
| `business_unit`, `business_owner` | | unit only |
| `risk_tier` | Low / Moderate / High | ● |
| `autonomy_level` | A0–A3 | ● |
| `data_classes` | `;`-separated | |
| `audience` | Unit / Agency-wide / External government / Public | ● |
| `decisions_about_people` | Yes / No | ● |
| `high_risk_ads` | Yes / No: high-risk automated decision system under GC 11546.45.5 | ● |
| `request_id`, `decided_by`, `decision_date` | | |
| `conditions_open` | Number of open approval conditions | |
| `iso_dissent_risk_acceptance` | No / Yes, with Risk Acceptance reference | |
| `exceptions` | Exception numbers and expiry dates | |
| `status` | Proposed / Approved / Active / Suspended / Retired | ● |
| `legacy_use` | Yes / No | |
| `go_live_date`, `last_review_date`, `next_review_date` | | |
| `public_summary` | One sentence for the public page | ● |
| `notes` | | |

## Exports
- **CDT high-risk inventory:** filter `risk_tier = High` or `high_risk_ads = Yes`; add any fields CDT's data call requests.
- **Public AI use summary:** the **Public** columns for rows with status Active.

Never export or publish completed SIMM 5305-F, SIMM 150 or security reviews (GC 7929.210).
