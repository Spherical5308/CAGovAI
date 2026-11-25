# Diagrams

| File | What it is |
|---|---|
| [request-approval-swimlane.svg](./request-approval-swimlane.svg) | The Request and Approval swimlane as an image. Shown in the [Procedure Map](../../PROCEDURE-MAP.md). Insert it straight into PowerPoint, Word or Visio (Insert → Pictures); it stays sharp at any size. |
| [request-approval-swimlane.drawio](./request-approval-swimlane.drawio) | The same diagram, editable. |

## Editing in draw.io, Visio or PowerPoint
1. Download the `.drawio` file (open it on GitHub and click **Download raw file**).
2. Open it at [app.diagrams.net](https://app.diagrams.net) (free, nothing to install) or in the draw.io desktop app. Lanes, shapes and connectors are all editable.
3. To hand it to someone else, use **File → Export as**:
   - **VSDX** for Microsoft Visio,
   - **PNG** or **SVG** for PowerPoint and Word,
   - **PDF** for printing.

## Regenerating from the script
The SVG and `.drawio` files are both produced by [`scripts/build_swimlane.py`](../../scripts/build_swimlane.py) from one layout, so they always match. To change a step, lane or connector, edit the `NODES` and `EDGES` lists in that script and run:

```
python3 scripts/build_swimlane.py
```

If you would rather edit by hand in draw.io, that is fine: export a new SVG over the old one and note in your pull request that the script is no longer the source for this diagram.
