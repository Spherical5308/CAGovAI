# Placeholder Checklist

> Every value in square brackets, such as `[State Entity]`, must be replaced before adoption ([Rollout Plan](./90-Day-Rollout-Plan.md) task 1.2). Work through the table, then run the search at the bottom to catch any you missed.

## Values to decide once
| Placeholder | Replace with | Appears in |
|---|---|---|
| `[State Entity]` | Your department's name | Almost every document, the Word form headers and the inventory workbook |
| `[Director name]` | The Director who signs | Policy header; Charter header |
| `[number]` | Your policy number | Policy header |
| `[date]` in the Policy header | The effective date (Day 0) | Policy header |
| `[prior GenAI guidance, if any]` | The guidance this Policy replaces, or "None" | Policy header |
| `[channel]` | Where Requests and monitoring reports go (mailbox, form or ticket queue) | Intake Form; Procedures 01 and 03 |
| `[contact]` | How to reach the ISO or service desk to report misuse or an incident | Acceptable Use Standard §3; Procedure 04 |

## Committee seats (Charter §2)
| Placeholder | Replace with |
|---|---|
| `[Chief Deputy Director or equivalent]` | Executive Sponsor (Chair) |
| `[Deputy Director, rotating every 12 months]` | Business/Program Representative and the rotation start date |
| `[Chief Counsel]`, `[Privacy Officer]`, `[CIO]`, `[ISO]` | Voting Seat holders, by title or name |
| `[Labor Relations Officer]`, `[Accessibility Coordinator]`, `[Records Officer]`, `[Procurement and Contracting Officer]` | Advisory Seat holders |

## Per Tool
| Placeholder | Replace with |
|---|---|
| `[Tool name]`, `[Enterprise copilot]`, `[tier]` | In each copy of the Approved Uses Register: the Tool and its licence tier |

## Leave as they are
These are fill-in fields on the forms, not adoption placeholders: `[date]` inside a form, `[assigned by Coordinator]`, `[Request ID: ]`, `[case number, date]`, `[case, date, outcome]`, `[date, not later than the next scheduled Re-review]`, and the example wording `[text/image/audio/video]` in the Acceptable Use Standard's disclosure label. In the Word forms they are already "click to enter" fields.

## Also
- **Inventory:** delete the example rows in the CSV files or the [Excel workbook](../inventory/AI-Inventory.xlsx).
- **Word forms:** after replacing `[State Entity]` in the Markdown, rebuild with `python3 scripts/build_office.py`, or edit the header in your own copy of each Word file (Insert → Header & Footer).
- **Optional choices to confirm:** the extra Prohibited uses P8 to P10 (Acceptable Use Standard), the Rating Scales and risk tolerance, and the turnaround targets (Charter §6).

## Catch anything missed
From the repository folder, list every remaining bracketed value that is not a link:

```
grep -rnoE "\[[^]]+\]($|[^(])" --include=*.md policy standards procedures forms inventory | grep -v "\[ \]"
```

Anything left that is not in "Leave as they are" still needs a value.
