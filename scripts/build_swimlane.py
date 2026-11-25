#!/usr/bin/env python3
"""Build the Request-and-Approval swimlane as a draw.io file and a matching SVG.

One layout model feeds both outputs, so they always agree. Edit NODES / EDGES below
and re-run:  python3 scripts/build_swimlane.py
Outputs: docs/diagrams/request-approval-swimlane.drawio and .svg
(You can also edit the .drawio file directly in draw.io / diagrams.net and export
SVG, PNG or VSDX from there; if you do, stop using this script for that diagram.)
"""
import html
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "diagrams")
NAME = "request-approval-swimlane"

# ---- Layout ---------------------------------------------------------------
HEADER_W = 50      # lane title band (vertical text)
PHASE_H = 34       # phase header row
LANE_H = 124
COL_W = 150
PAD_X = 16
NODE_W, NODE_H = 120, 52
DIA_W, DIA_H = 116, 74
ROW_Y = {"top": 36, "mid": 62, "low": 92}   # node centre within a lane

LANES = [
    ("Business unit", "#F5F9FF"),
    ("AI Governance Coordinator", "#FFFFFF"),
    ("Specialists", "#F5F9FF"),
    ("Triage Panel", "#FFFFFF"),
    ("AI Governance Committee", "#F5F9FF"),
    ("Director / Agency", "#FFFFFF"),
    ("CDT", "#F5F9FF"),
]
PHASES = [  # (title, first column, last column)
    ("1. Intake", 0, 3),
    ("2. Screen", 4, 5),
    ("3. Triage and assess", 6, 8),
    ("4. Decide", 9, 12),
    ("5. Approve and act", 13, 14),
    ("6. Operate", 15, 16),
]
N_COLS = 17

STYLE = {  # kind: (fill, stroke)
    "start": ("#D5E8D4", "#82B366"),
    "process": ("#DAE8FC", "#6C8EBF"),
    "decision": ("#FFF2CC", "#D6B656"),
    "good": ("#D5E8D4", "#82B366"),
    "stop": ("#F8CECC", "#B85450"),
    "note": ("#F5F5F5", "#999999"),
}

# id: (lane index, column, row, kind, label)
NODES = {
    "start":   (0, 0, "mid", "start", "AI idea, or vendor discloses GenAI"),
    "d_pre":   (0, 1, "mid", "decision", "Approved Use and no Trigger?"),
    "pre":     (0, 2, "mid", "good", "Manager attests; logged as Pre-approved"),
    "submit":  (0, 3, "mid", "process", "Submit Request (Intake Form)"),
    "complete": (1, 4, "mid", "process", "Completeness check"),
    "d_proh":  (1, 5, "mid", "decision", "Prohibited use?"),
    "counsel": (2, 5, "mid", "stop", "Chief Counsel confirms; closed (appealable)"),
    "triage":  (1, 6, "mid", "process", "Triage: Triggers, Tier Floors, Autonomy Level"),
    "package": (0, 7, "mid", "process", "Complete Assessment Package"),
    "privacy": (2, 7, "mid", "process", "Privacy Officer: PTA / PIA"),
    "attest":  (2, 8, "mid", "process", "CIO + ISO attest 5305-F / 150; copy to Labor Relations"),
    "cdt_sub": (6, 8, "mid", "process", "Submit or keep on file (by tier and route)"),
    "d_tier":  (1, 9, "mid", "decision", "Final Risk Tier?"),
    "low":     (3, 10, "mid", "process", "Decide Low"),
    "vote":    (4, 10, "mid", "process", "Vote: decide Moderate, recommend High"),
    "risk":    (5, 10, "mid", "note", "Risk Acceptance signed if ISO dissents"),
    "consent": (3, 11, "mid", "process", "Report on monthly consent agenda"),
    "cdt_rev": (6, 11, "mid", "process", "Review; consult (Moderate if asked, High required)"),
    "director": (5, 12, "mid", "process", "Director approves High (Agency optional)"),
    "issue":   (1, 13, "mid", "good", "Issue Request ID; update AI Inventory"),
    "procure": (0, 14, "mid", "process", "Procure / build; meet conditions; go live"),
    "operate": (0, 15, "mid", "process", "Operate and monitor"),
    "suspend": (2, 15, "mid", "stop", "ISO or CIO may suspend; Committee rules in 10 days"),
    "d_rr":    (1, 16, "mid", "decision", "Re-review due or Material Change?"),
}

# (source, target, label, dashed[, via]) via: "over" = leave by the top and run along the lane top;
#   "down" = leave by the bottom and turn into the target from the left
EDGES = [
    ("start", "d_pre", "", False),
    ("d_pre", "pre", "Yes", False),
    ("d_pre", "submit", "No / unsure", False, "over"),
    ("submit", "complete", "", False),
    ("complete", "d_proh", "", False),
    ("d_proh", "counsel", "Yes", False),
    ("d_proh", "triage", "No", False),
    ("triage", "package", "", False),
    ("package", "privacy", "", False),
    ("privacy", "attest", "", False),
    ("attest", "cdt_sub", "", False),
    ("attest", "d_tier", "", False),
    ("d_tier", "low", "Low", False, "down"),
    ("d_tier", "vote", "Moderate / High", False, "down"),
    ("low", "consent", "", False),
    ("consent", "issue", "", False),
    ("vote", "risk", "ISO dissent", True),
    ("vote", "cdt_rev", "", False),
    ("cdt_sub", "cdt_rev", "Moderate / High", True),
    ("cdt_rev", "director", "High", False),
    ("cdt_rev", "issue", "Moderate", False),
    ("director", "issue", "", False),
    ("issue", "procure", "", False),
    ("procure", "operate", "", False),
    ("operate", "d_rr", "", False),
    ("operate", "suspend", "Incident", False),
    ("d_rr", "triage", "Yes", False),
]

WIDTH = HEADER_W + PAD_X * 2 + COL_W * N_COLS
HEIGHT = PHASE_H + LANE_H * len(LANES)


def lane_top(i):
    return PHASE_H + LANE_H * i


def geom(nid):
    lane, col, row, kind, _ = NODES[nid]
    cx = HEADER_W + PAD_X + COL_W * col + COL_W / 2
    cy = lane_top(lane) + ROW_Y[row]
    w, h = (DIA_W, DIA_H) if kind == "decision" else (NODE_W, NODE_H)
    if row != "mid" and kind != "decision":
        h = 44
    return cx, cy, w, h


def route(src, dst, via=None):
    """Orthogonal path between two nodes, as a list of points."""
    sx, sy, sw, sh = geom(src)
    tx, ty, tw, th = geom(dst)
    s_lane, t_lane = NODES[src][0], NODES[dst][0]
    if via == "over":
        ch = lane_top(s_lane) + 8
        return [(sx, sy - sh / 2), (sx, ch), (tx, ch), (tx, ty - th / 2)]
    if via == "down":
        return [(sx, sy + sh / 2), (sx, ty), (tx - tw / 2, ty)]
    if tx < sx - 1:  # loop back: over the top of the source lane
        ch = lane_top(s_lane) + 8
        return [(sx, sy - sh / 2), (sx, ch), (tx, ch), (tx, ty - th / 2)]
    if abs(tx - sx) < 1:  # same column: straight up or down
        if ty > sy:
            return [(sx, sy + sh / 2), (tx, ty - th / 2)]
        return [(sx, sy - sh / 2), (tx, ty + th / 2)]
    if abs(ty - sy) < 1:  # same row: straight across
        return [(sx + sw / 2, sy), (tx - tw / 2, ty)]
    if s_lane == t_lane or abs(tx - sx) > COL_W + 1:
        xm = tx - tw / 2 - 14  # bend just before the target
    else:
        xm = (sx + sw / 2 + tx - tw / 2) / 2
    return [(sx + sw / 2, sy), (xm, sy), (xm, ty), (tx - tw / 2, ty)]


def wrap(text, width_px, size):
    max_chars = max(6, int(width_px / (size * 0.56)))
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > max_chars:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)
    return lines


# ---- SVG ------------------------------------------------------------------
def svg():
    e = html.escape
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'width="{WIDTH}" height="{HEIGHT}" font-family="Segoe UI, Arial, Helvetica, sans-serif">',
        "<title>AI Request and Approval swimlane</title>",
        '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#333"/></marker></defs>',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#FFFFFF"/>',
    ]
    # phase header
    for title, c0, c1 in PHASES:
        x = HEADER_W + PAD_X + COL_W * c0
        w = COL_W * (c1 - c0 + 1)
        out.append(f'<rect x="{x}" y="0" width="{w}" height="{PHASE_H}" fill="#1F3864" stroke="#FFFFFF"/>')
        out.append(f'<text x="{x + w / 2}" y="{PHASE_H / 2 + 5}" text-anchor="middle" font-size="14" '
                   f'font-weight="600" fill="#FFFFFF">{e(title)}</text>')
    out.append(f'<rect x="0" y="0" width="{HEADER_W + PAD_X}" height="{PHASE_H}" fill="#1F3864"/>')
    # lanes
    for i, (title, fill) in enumerate(LANES):
        y = lane_top(i)
        out.append(f'<rect x="0" y="{y}" width="{WIDTH}" height="{LANE_H}" fill="{fill}" stroke="#8C9DB5"/>')
        out.append(f'<rect x="0" y="{y}" width="{HEADER_W}" height="{LANE_H}" fill="#D9E2F3" stroke="#8C9DB5"/>')
        lines = wrap(title, LANE_H - 10, 12)
        cx, cy = HEADER_W / 2, y + LANE_H / 2
        out.append(f'<text transform="rotate(-90 {cx} {cy})" text-anchor="middle" font-size="12" '
                   f'font-weight="600" fill="#1F3864">')
        for j, ln in enumerate(lines):
            dy = (j - (len(lines) - 1) / 2) * 14 + 4
            out.append(f'<tspan x="{cx}" y="{cy + dy}">{e(ln)}</tspan>')
        out.append("</text>")
    # phase dividers
    for _, c0, _ in PHASES[1:]:
        x = HEADER_W + PAD_X + COL_W * c0
        out.append(f'<line x1="{x}" y1="{PHASE_H}" x2="{x}" y2="{HEIGHT}" stroke="#C5CFDD" stroke-dasharray="4 4"/>')
    # edges
    for src, dst, label, dashed, *via in EDGES:
        pts = route(src, dst, *via)
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        dash = ' stroke-dasharray="5 4"' if dashed else ""
        out.append(f'<polyline points="{d}" fill="none" stroke="#333" stroke-width="1.3"{dash} marker-end="url(#arr)"/>')
        if label:
            # Label sits just after the edge leaves its source, so the target never hides it.
            (x1, y1), (x2, y2) = pts[0], pts[1]
            anchor = "start"
            if via == ["down"]:  # label the final leg into the target
                (ax, ay), (bx, _) = pts[-2], pts[-1]
                lx, ly = ax + 4, ay - 5
            elif abs(x1 - x2) < 1:  # vertical first segment
                lx = x1 + 5
                ly = y1 + 14 if y2 > y1 else y1 - 6
            elif len(pts) == 4 and abs(x2 - x1) < 60:  # short stub: label the vertical leg
                (vx, vy1), (_, vy2) = pts[1], pts[2]
                lx, ly = vx + 5, (vy1 + vy2) / 2 + 4
            else:  # horizontal first segment
                lx, ly = x1 + 4, y1 - 5
            out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" font-size="10.5" '
                       f'fill="#333" paint-order="stroke" stroke="#FFFFFF" stroke-width="3">{e(label)}</text>')
    # nodes
    for nid, (lane, col, row, kind, label) in NODES.items():
        cx, cy, w, h = geom(nid)
        fill, stroke = STYLE[kind]
        if kind == "decision":
            p = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
            out.append(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>')
            tw = w * 0.62
        elif kind == "start":
            out.append(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="{h / 2}" '
                       f'fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>')
            tw = w - 18
        else:
            dash = ' stroke-dasharray="4 3"' if kind == "note" else ""
            out.append(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="6" '
                       f'fill="{fill}" stroke="{stroke}" stroke-width="1.3"{dash}/>')
            tw = w - 10
        size = 10.5
        lines = wrap(label, tw, size)
        out.append(f'<text text-anchor="middle" font-size="{size}" fill="#111">')
        for j, ln in enumerate(lines):
            dy = (j - (len(lines) - 1) / 2) * 12.5 + 3.5
            out.append(f'<tspan x="{cx}" y="{cy + dy:.1f}">{e(ln)}</tspan>')
        out.append("</text>")
    out.append("</svg>")
    return "\n".join(out)


# ---- draw.io --------------------------------------------------------------
def drawio():
    e = lambda s: html.escape(s, quote=True)
    cells = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']
    for i, (title, fill) in enumerate(LANES):
        cells.append(
            f'<mxCell id="lane{i}" value="{e(title)}" style="swimlane;horizontal=0;startSize={HEADER_W};'
            f'fillColor=#D9E2F3;swimlaneFillColor={fill};strokeColor=#8C9DB5;fontStyle=1;fontColor=#1F3864;'
            f'html=1;whiteSpace=wrap;collapsible=0;" vertex="1" parent="1">'
            f'<mxGeometry x="0" y="{lane_top(i)}" width="{WIDTH}" height="{LANE_H}" as="geometry"/></mxCell>')
    for k, (title, c0, c1) in enumerate(PHASES):
        x = HEADER_W + PAD_X + COL_W * c0
        cells.append(
            f'<mxCell id="phase{k}" value="{e(title)}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#1F3864;'
            f'strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=14;" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="0" width="{COL_W * (c1 - c0 + 1)}" height="{PHASE_H}" as="geometry"/></mxCell>')
    for nid, (lane, col, row, kind, label) in NODES.items():
        cx, cy, w, h = geom(nid)
        fill, stroke = STYLE[kind]
        shape = {"decision": "rhombus;", "start": "rounded=1;arcSize=50;"}.get(kind, "rounded=1;")
        dash = "dashed=1;" if kind == "note" else ""
        # child of its lane: coordinates relative to the lane
        cells.append(
            f'<mxCell id="{nid}" value="{e(label)}" style="{shape}whiteSpace=wrap;html=1;fillColor={fill};'
            f'strokeColor={stroke};fontSize=11;{dash}" vertex="1" parent="lane{lane}">'
            f'<mxGeometry x="{cx - w / 2}" y="{cy - h / 2 - lane_top(lane)}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    for n, (src, dst, label, dashed, *via) in enumerate(EDGES):
        pts = route(src, dst, *via)
        mids = "".join(f'<mxPoint x="{x:.1f}" y="{y:.1f}"/>' for x, y in pts[1:-1])
        dash = "dashed=1;" if dashed else ""
        cells.append(
            f'<mxCell id="e{n}" value="{e(label)}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;'
            f'endArrow=block;endFill=1;fontSize=10;labelBackgroundColor=#FFFFFF;{dash}" edge="1" parent="1" '
            f'source="{src}" target="{dst}"><mxGeometry relative="1" as="geometry">'
            f'<mxPoint x="{pts[0][0]:.1f}" y="{pts[0][1]:.1f}" as="sourcePoint"/>'
            f'<mxPoint x="{pts[-1][0]:.1f}" y="{pts[-1][1]:.1f}" as="targetPoint"/>'
            f'<Array as="points">{mids}</Array></mxGeometry></mxCell>')
    body = "".join(cells)
    return (
        '<mxfile host="CAGovAI build_swimlane.py">'
        f'<diagram id="request-approval" name="Request and Approval">'
        f'<mxGraphModel dx="{WIDTH}" dy="{HEIGHT}" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" '
        f'arrows="1" fold="1" page="1" pageScale="1" pageWidth="{WIDTH}" pageHeight="{HEIGHT}" math="0" shadow="0">'
        f"<root>{body}</root></mxGraphModel></diagram></mxfile>\n"
    )


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, NAME + ".svg"), "w", encoding="utf-8") as fh:
        fh.write(svg() + "\n")
    with open(os.path.join(OUT_DIR, NAME + ".drawio"), "w", encoding="utf-8") as fh:
        fh.write(drawio())
    print("wrote", NAME + ".svg", "and", NAME + ".drawio")
