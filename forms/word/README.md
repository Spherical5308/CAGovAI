# Fillable Word forms

Word versions of every form and assessment in [forms/](../). Open one in Microsoft Word (desktop or web), click a grey "Click or tap to enter text." field and type; click a ☐ to tick it. Fields grow as you type, and tables add rows the usual way (Tab in the last cell).

| Form | Word | Markdown source |
|---|---|---|
| AI Request: Intake Form | [Intake-Form.docx](./Intake-Form.docx) | [Intake-Form.md](../Intake-Form.md) |
| Approved Uses Register | [Approved-Uses-Register.docx](./Approved-Uses-Register.docx) | [Approved-Uses-Register.md](../Approved-Uses-Register.md) |
| AI Request Decision Record | [Decision-Record.docx](./Decision-Record.docx) | [Decision-Record.md](../Decision-Record.md) |
| AI Risk Acceptance | [Risk-Acceptance.docx](./Risk-Acceptance.docx) | [Risk-Acceptance.md](../Risk-Acceptance.md) |
| AI Standard Exception Request | [Exception-Request.docx](./Exception-Request.docx) | [Exception-Request.md](../Exception-Request.md) |
| AI Impact Assessment | [AI-Impact-Assessment.docx](./AI-Impact-Assessment.docx) | [AI-Impact-Assessment.md](../AI-Impact-Assessment.md) |
| AI Workforce Impact Assessment | [Workforce-Impact-Assessment.docx](./Workforce-Impact-Assessment.docx) | [Workforce-Impact-Assessment.md](../Workforce-Impact-Assessment.md) |

To download from GitHub, open the file and click **Download raw file**.

## Adapting them
- Replace `[State Entity]` in the page header (Insert → Header & Footer) and any bracketed placeholders.
- To add your own logo or letterhead, edit the copy you download; it is a normal Word document.
- The forms are not locked, so you can reword them. If you want staff to fill in only the fields, use Review → Restrict Editing → "Filling in forms" in your own copy.

## How they are made
[`scripts/build_office.py`](../../scripts/build_office.py) builds these files from the Markdown forms, which stay the source of truth: ☐ becomes a checkbox, `[placeholder]` and empty table cells become text fields, and each open question gets an answer box. To change a form, edit its Markdown and run:

```
pip install python-docx openpyxl
python3 scripts/build_office.py
```

The same script builds the [AI Inventory workbook](../../inventory/AI-Inventory.xlsx).
