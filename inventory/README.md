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

## pre-approved-log.csv
| Field | What to record | Public |
|---|---|:-:|
| `entry_date` | Date the manager attested | |
| `tool_id` | Links to tools.csv | |
| `approved_use_category` | SIMM 150 category from the Tool's Approved Uses Register | |
| `audience` | Personal / unit, Agency-wide, or Public / external (register columns) | |
| `business_unit` | Unit using the Tool | |
| `user_or_group` | Person or group covered by the attestation | |
| `manager_attesting` | Manager who attested that no Trigger applies | |
| `training_current` | Yes / No: SAM 4986.13 GenAI training is current | |
| `aup_acknowledged` | Yes / No: Acceptable Use Standard acknowledged | |

## Excel workbook
[AI-Inventory.xlsx](./AI-Inventory.xlsx) holds the same three registers as sheets, with dropdowns for fixed values (tier, Autonomy Level, status, Yes/No and so on), a `tool_id` dropdown fed from the Tools sheet, and this field guide. Public fields have a lighter blue header. It is generated from these CSV files and this page by [`scripts/build_office.py`](../scripts/build_office.py); use whichever format suits your entity.

## Exports
- **CDT high-risk inventory:** filter `risk_tier = High` or `high_risk_ads = Yes`; add any fields CDT's data call requests.
- **Public AI use summary:** the **Public** columns for rows with status Active.

Never export or publish completed SIMM 5305-F, SIMM 150 or security reviews. They are treated as confidential; see the [Policy, section 4.9](../policy/AI-Governance-Policy.md#49-transparency-and-disclosure).
