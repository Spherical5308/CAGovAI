# Diagrams

Each diagram comes as an **SVG** (shown in the [Procedure Map](../../PROCEDURE-MAP.md); insert it straight into PowerPoint, Word or Visio with Insert → Pictures, and it stays sharp at any size) and an editable **.drawio** file.

| Diagram | Image | Editable | Where it is used |
|---|---|---|---|
| Process overview | [SVG](./process-overview.svg) | [draw.io](./process-overview.drawio) | Procedure Map §1 |
| Request and Approval swimlane | [SVG](./request-approval-swimlane.svg) | [draw.io](./request-approval-swimlane.drawio) | Procedure Map §2 |
| Legacy Use registration | [SVG](./legacy-use-registration.svg) | [draw.io](./legacy-use-registration.drawio) | Procedure Map §6.2 |

## Editing in draw.io, Visio or PowerPoint
1. Download the `.drawio` file (open it on GitHub and click **Download raw file**).
2. Open it at [app.diagrams.net](https://app.diagrams.net) (free, nothing to install) or in the draw.io desktop app. Lanes, shapes and connectors are all editable.
3. To hand it to someone else, use **File → Export as**:
   - **VSDX** for Microsoft Visio,
   - **PNG** or **SVG** for PowerPoint and Word,
   - **PDF** for printing.

## Regenerating from the script
All SVG and `.drawio` files are produced by [`scripts/build_diagrams.py`](../../scripts/build_diagrams.py). Each diagram is one layout spec in that script (lanes, phases, nodes and edges), and both files come from the same spec, so they always match. To change a step, lane or connector, edit the spec and run:

```
python3 scripts/build_diagrams.py
```

If you would rather edit one diagram by hand in draw.io, that is fine: export a new SVG over the old one, remove that diagram from the script's `DIAGRAMS` list, and say so in your pull request.
