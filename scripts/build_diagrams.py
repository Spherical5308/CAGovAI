#!/usr/bin/env python3
"""Build the repository's process diagrams as draw.io files and matching SVGs.

Each diagram is one layout spec (see DIAGRAMS at the bottom). The same spec feeds both
outputs, so the editable .drawio and the .svg shown on GitHub always agree.
Edit a spec and re-run:  python3 scripts/build_diagrams.py
Outputs go to docs/diagrams/<name>.drawio and <name>.svg.

You can also edit a .drawio file directly in draw.io / diagrams.net and export SVG,
PNG, PDF or VSDX from there; if you do, remove that diagram from this script.
"""
import html
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "diagrams")

NODE_W, NODE_H = 120, 52
DIA_W, DIA_H = 116, 74
PAD_X = 16

STYLE = {  # kind: (fill, stroke)
    "start": ("#D5E8D4", "#82B366"),
    "process": ("#DAE8FC", "#6C8EBF"),
    "decision": ("#FFF2CC", "#D6B656"),
    "good": ("#D5E8D4", "#82B366"),
    "stop": ("#F8CECC", "#B85450"),
    "note": ("#F5F5F5", "#999999"),
}


class Diagram:
    """lanes: [(title, fill)]; title "" = no header band. phases: [(title, c0, c1)].
    nodes: {id: (lane, col, row, kind, label)} row in top/mid/low.
    edges: [(src, dst, label, dashed[, via])] via: "over" | "down" (vertical first, up or down)."""

    def __init__(self, name, title, lanes, phases, n_cols, nodes, edges,
                 lane_h=124, col_w=150, header_w=50, rows=None):
        self.name, self.title = name, title
        self.lanes, self.phases, self.n_cols = lanes, phases, n_cols
        self.nodes, self.edges = nodes, edges
        self.lane_h, self.col_w = lane_h, col_w
        self.header_w = header_w if any(t for t, _ in lanes) else 0
        self.phase_h = 34 if phases else 0
        self.rows = rows or {"top": 36, "mid": lane_h / 2, "low": lane_h - 32}
        self.width = self.header_w + PAD_X * 2 + col_w * n_cols
        self.height = self.phase_h + lane_h * len(lanes)

    # -- geometry --
    def lane_top(self, i):
        return self.phase_h + self.lane_h * i

    def col_x(self, c):
        return self.header_w + PAD_X + self.col_w * c

    def geom(self, nid):
        lane, col, row, kind, _ = self.nodes[nid]
        cx = self.col_x(col) + self.col_w / 2
        cy = self.lane_top(lane) + self.rows[row]
        w, h = (DIA_W, DIA_H) if kind == "decision" else (NODE_W, NODE_H)
        if row != "mid" and kind != "decision":
            h = 44
        if kind != "decision":  # grow the box to fit the wrapped label
            tw = w - (18 if kind == "start" else 10)
            h = max(h, 12.5 * len(wrap(self.nodes[nid][4], tw, 10.5)) + 12)
        return cx, cy, w, h

    def route(self, src, dst, via=None):
        sx, sy, sw, sh = self.geom(src)
        tx, ty, tw, th = self.geom(dst)
        s_lane, t_lane = self.nodes[src][0], self.nodes[dst][0]
        if via == "over":
            ch = self.lane_top(s_lane) + 8
            return [(sx, sy - sh / 2), (sx, ch), (tx, ch), (tx, ty - th / 2)]
        if via == "down":  # leave the source vertically (down or up), enter the target from the left
            return [(sx, sy + (sh if ty > sy else -sh) / 2), (sx, ty), (tx - tw / 2, ty)]
        if tx < sx - 1:  # loop back over the top of the source lane
            ch = self.lane_top(s_lane) + 8
            return [(sx, sy - sh / 2), (sx, ch), (tx, ch), (tx, ty - th / 2)]
        if abs(tx - sx) < 1:
            if ty > sy:
                return [(sx, sy + sh / 2), (tx, ty - th / 2)]
            return [(sx, sy - sh / 2), (tx, ty + th / 2)]
        if abs(ty - sy) < 1:
            return [(sx + sw / 2, sy), (tx - tw / 2, ty)]
        if s_lane == t_lane or abs(tx - sx) > self.col_w + 1:
            xm = tx - tw / 2 - 14
        else:
            xm = (sx + sw / 2 + tx - tw / 2) / 2
        return [(sx + sw / 2, sy), (xm, sy), (xm, ty), (tx - tw / 2, ty)]

    def label_pos(self, pts, via):
        (x1, y1), (x2, y2) = pts[0], pts[1]
        if via == "down":
            (ax, ay) = pts[-2]
            return ax + 4, ay - 5
        if abs(x1 - x2) < 1:
            return x1 + 5, (y1 + 14 if y2 > y1 else y1 - 6)
        if len(pts) == 4 and abs(x2 - x1) < 60:
            (vx, vy1), (_, vy2) = pts[1], pts[2]
            return vx + 5, (vy1 + vy2) / 2 + 4
        return x1 + 4, y1 - 5

    # -- SVG --
    def svg(self):
        e = html.escape
        W, H = self.width, self.height
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            'font-family="Segoe UI, Arial, Helvetica, sans-serif">',
            f"<title>{e(self.title)}</title>",
            '<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#333"/></marker></defs>',
            f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
        ]
        for title, c0, c1 in self.phases:
            x, w = self.col_x(c0), self.col_w * (c1 - c0 + 1)
            out.append(f'<rect x="{x}" y="0" width="{w}" height="{self.phase_h}" fill="#1F3864" stroke="#FFFFFF"/>')
            out.append(f'<text x="{x + w / 2}" y="{self.phase_h / 2 + 5}" text-anchor="middle" font-size="14" '
                       f'font-weight="600" fill="#FFFFFF">{e(title)}</text>')
        if self.phases:
            out.append(f'<rect x="0" y="0" width="{self.header_w + PAD_X}" height="{self.phase_h}" fill="#1F3864"/>')
        for i, (title, fill) in enumerate(self.lanes):
            y = self.lane_top(i)
            if title:
                out.append(f'<rect x="0" y="{y}" width="{W}" height="{self.lane_h}" fill="{fill}" stroke="#8C9DB5"/>')
                out.append(f'<rect x="0" y="{y}" width="{self.header_w}" height="{self.lane_h}" fill="#D9E2F3" stroke="#8C9DB5"/>')
                lines = wrap(title, self.lane_h - 10, 12)
                cx, cy = self.header_w / 2, y + self.lane_h / 2
                out.append(f'<text transform="rotate(-90 {cx} {cy})" text-anchor="middle" font-size="12" '
                           f'font-weight="600" fill="#1F3864">')
                for j, ln in enumerate(lines):
                    out.append(f'<tspan x="{cx}" y="{cy + (j - (len(lines) - 1) / 2) * 14 + 4}">{e(ln)}</tspan>')
                out.append("</text>")
        for _, c0, _ in self.phases[1:]:
            x = self.col_x(c0)
            out.append(f'<line x1="{x}" y1="{self.phase_h}" x2="{x}" y2="{H}" stroke="#C5CFDD" stroke-dasharray="4 4"/>')
        for src, dst, label, dashed, *via in self.edges:
            v = via[0] if via else None
            pts = self.route(src, dst, v)
            d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
            dash = ' stroke-dasharray="5 4"' if dashed else ""
            out.append(f'<polyline points="{d}" fill="none" stroke="#333" stroke-width="1.3"{dash} marker-end="url(#arr)"/>')
            if label:
                lx, ly = self.label_pos(pts, v)
                out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="10.5" fill="#333" paint-order="stroke" '
                           f'stroke="#FFFFFF" stroke-width="3">{e(label)}</text>')
        for nid, (lane, col, row, kind, label) in self.nodes.items():
            cx, cy, w, h = self.geom(nid)
            fill, stroke = STYLE[kind]
            if kind == "decision":
                p = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
                out.append(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>')
                tw = w * 0.62
            else:
                rx = h / 2 if kind == "start" else 6
                dash = ' stroke-dasharray="4 3"' if kind == "note" else ""
                out.append(f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="{rx}" '
                           f'fill="{fill}" stroke="{stroke}" stroke-width="1.3"{dash}/>')
                tw = w - (18 if kind == "start" else 10)
            lines = wrap(label, tw, 10.5)
            out.append('<text text-anchor="middle" font-size="10.5" fill="#111">')
            for j, ln in enumerate(lines):
                out.append(f'<tspan x="{cx}" y="{cy + (j - (len(lines) - 1) / 2) * 12.5 + 3.5:.1f}">{e(ln)}</tspan>')
            out.append("</text>")
        out.append("</svg>")
        return "\n".join(out) + "\n"

    # -- draw.io --
    def drawio(self):
        e = lambda s: html.escape(s, quote=True)
        cells = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']
        for i, (title, fill) in enumerate(self.lanes):
            if title:
                style = (f"swimlane;horizontal=0;startSize={self.header_w};fillColor=#D9E2F3;swimlaneFillColor={fill};"
                         "strokeColor=#8C9DB5;fontStyle=1;fontColor=#1F3864;html=1;whiteSpace=wrap;collapsible=0;")
            else:
                style = "rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;container=1;collapsible=0;"
            cells.append(f'<mxCell id="lane{i}" value="{e(title)}" style="{style}" vertex="1" parent="1">'
                         f'<mxGeometry x="0" y="{self.lane_top(i)}" width="{self.width}" height="{self.lane_h}" as="geometry"/></mxCell>')
        for k, (title, c0, c1) in enumerate(self.phases):
            cells.append(
                f'<mxCell id="phase{k}" value="{e(title)}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#1F3864;'
                f'strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=14;" vertex="1" parent="1">'
                f'<mxGeometry x="{self.col_x(c0)}" y="0" width="{self.col_w * (c1 - c0 + 1)}" height="{self.phase_h}" as="geometry"/></mxCell>')
        for nid, (lane, col, row, kind, label) in self.nodes.items():
            cx, cy, w, h = self.geom(nid)
            fill, stroke = STYLE[kind]
            shape = {"decision": "rhombus;", "start": "rounded=1;arcSize=50;"}.get(kind, "rounded=1;")
            dash = "dashed=1;" if kind == "note" else ""
            cells.append(
                f'<mxCell id="{nid}" value="{e(label)}" style="{shape}whiteSpace=wrap;html=1;fillColor={fill};'
                f'strokeColor={stroke};fontSize=11;{dash}" vertex="1" parent="lane{lane}">'
                f'<mxGeometry x="{cx - w / 2}" y="{cy - h / 2 - self.lane_top(lane)}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        for n, (src, dst, label, dashed, *via) in enumerate(self.edges):
            pts = self.route(src, dst, via[0] if via else None)
            mids = "".join(f'<mxPoint x="{x:.1f}" y="{y:.1f}"/>' for x, y in pts[1:-1])
            dash = "dashed=1;" if dashed else ""
            cells.append(
                f'<mxCell id="e{n}" value="{e(label)}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;'
                f'endArrow=block;endFill=1;fontSize=10;labelBackgroundColor=#FFFFFF;{dash}" edge="1" parent="1" '
                f'source="{src}" target="{dst}"><mxGeometry relative="1" as="geometry">'
                f'<Array as="points">{mids}</Array></mxGeometry></mxCell>')
        return (f'<mxfile host="CAGovAI build_diagrams.py"><diagram id="{self.name}" name="{e(self.title)}">'
                f'<mxGraphModel dx="{self.width}" dy="{self.height}" grid="1" gridSize="10" guides="1" tooltips="1" '
                f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.width}" '
                f'pageHeight="{self.height}" math="0" shadow="0"><root>{"".join(cells)}</root></mxGraphModel>'
                "</diagram></mxfile>\n")


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


# =========================================================================
# Diagram specs
# =========================================================================
SWIMLANE = Diagram(
    name="request-approval-swimlane",
    title="AI Request and Approval swimlane",
    lanes=[
        ("Business unit", "#F5F9FF"),
        ("AI Governance Coordinator", "#FFFFFF"),
        ("Specialists", "#F5F9FF"),
        ("Triage Panel", "#FFFFFF"),
        ("AI Governance Committee", "#F5F9FF"),
        ("Director / Agency", "#FFFFFF"),
        ("CDT", "#F5F9FF"),
    ],
    phases=[
        ("1. Intake", 0, 3), ("2. Screen", 4, 5), ("3. Triage and assess", 6, 8),
        ("4. Decide", 9, 12), ("5. Approve and act", 13, 14), ("6. Operate", 15, 16),
    ],
    n_cols=17,
    nodes={
        "start":    (0, 0, "mid", "start", "AI idea, or vendor discloses GenAI"),
        "d_pre":    (0, 1, "mid", "decision", "Approved Use and no Trigger?"),
        "pre":      (0, 2, "mid", "good", "Manager attests; logged as Pre-approved"),
        "submit":   (0, 3, "mid", "process", "Submit Request (Intake Form)"),
        "complete": (1, 4, "mid", "process", "Completeness check"),
        "d_proh":   (1, 5, "mid", "decision", "Prohibited use?"),
        "counsel":  (2, 5, "mid", "stop", "Chief Counsel confirms; closed (appealable)"),
        "triage":   (1, 6, "mid", "process", "Triage: Triggers, Tier Floors, Autonomy Level"),
        "package":  (0, 7, "mid", "process", "Complete Assessment Package"),
        "privacy":  (2, 7, "mid", "process", "Privacy Officer: PTA / PIA"),
        "attest":   (2, 8, "mid", "process", "CIO + ISO attest 5305-F / 150; copy to Labor Relations"),
        "cdt_sub":  (6, 8, "mid", "process", "Submit or keep on file (by tier and route)"),
        "d_tier":   (1, 9, "mid", "decision", "Final Risk Tier?"),
        "low":      (3, 10, "mid", "process", "Decide Low"),
        "vote":     (4, 10, "mid", "process", "Vote: decide Moderate, recommend High"),
        "risk":     (5, 10, "mid", "note", "Risk Acceptance signed if ISO dissents"),
        "consent":  (3, 11, "mid", "process", "Report on monthly consent agenda"),
        "cdt_rev":  (6, 11, "mid", "process", "Review; consult (Moderate if asked, High required)"),
        "director": (5, 12, "mid", "process", "Director approves High (Agency optional)"),
        "issue":    (1, 13, "mid", "good", "Issue Request ID; update AI Inventory"),
        "procure":  (0, 14, "mid", "process", "Procure / build; meet conditions; go live"),
        "operate":  (0, 15, "mid", "process", "Operate and monitor"),
        "suspend":  (2, 15, "mid", "stop", "ISO or CIO may suspend; Committee rules in 10 days"),
        "d_rr":     (1, 16, "mid", "decision", "Re-review due or Material Change?"),
    },
    edges=[
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
    ],
)

OVERVIEW = Diagram(
    name="process-overview",
    title="AI governance process overview",
    lanes=[("", "#FFFFFF"), ("", "#FFFFFF"), ("", "#FFFFFF")],
    phases=[
        ("Intake", 0, 2), ("Screen", 3, 4), ("Triage and assess", 5, 6),
        ("Decide", 7, 9), ("Approve and act", 10, 11), ("Operate", 12, 13),
    ],
    n_cols=14,
    lane_h=112,
    col_w=180,
    nodes={
        "start":   (1, 0, "mid", "start", "AI idea, or vendor discloses GenAI"),
        "d_pre":   (1, 1, "mid", "decision", "Approved Use and no Trigger?"),
        "pre":     (0, 1, "mid", "good", "Pre-approved: manager attests; logged in Inventory"),
        "submit":  (1, 2, "mid", "process", "Submit Request (Intake Form)"),
        "complete": (1, 3, "mid", "process", "Coordinator: completeness check"),
        "d_proh":  (1, 4, "mid", "decision", "Prohibited use?"),
        "proh":    (2, 4, "mid", "stop", "Prohibited: Chief Counsel confirms; closed, appealable to Committee"),
        "triage":  (1, 5, "mid", "process", "Triage: tier from Triggers, Tier Floors, Autonomy Level"),
        "package": (1, 6, "mid", "process", "Complete the tier's Assessment Package"),
        "d_tier":  (1, 7, "mid", "decision", "Risk Tier?"),
        "low":     (0, 8, "mid", "process", "Triage Panel decides Low; consent agenda"),
        "vote":    (1, 8, "mid", "process", "Committee votes (majority; ISO dissent needs Risk Acceptance)"),
        "reject":  (2, 8, "mid", "stop", "Rejected: closed and logged"),
        "cdt_m":   (2, 9, "mid", "process", "Moderate: CDT review before award"),
        "high":    (1, 9, "mid", "process", "High: CDT consultation, then Director approves"),
        "issue":   (1, 10, "mid", "good", "Approved: Request ID issued; Inventory updated"),
        "procure": (1, 11, "mid", "process", "Procure / build with Request ID; go live"),
        "operate": (1, 12, "mid", "process", "Operate and monitor (SAM 5335)"),
        "d_rr":    (1, 13, "mid", "decision", "Re-review due or Material Change?"),
        "suspend": (2, 12, "mid", "stop", "Incident: ISO or CIO may suspend; Committee rules in 10 days"),
    },
    edges=[
        ("start", "d_pre", "", False),
        ("d_pre", "pre", "Yes", False),
        ("d_pre", "submit", "No / unsure", False),
        ("submit", "complete", "", False),
        ("complete", "d_proh", "", False),
        ("d_proh", "proh", "Yes", False),
        ("d_proh", "triage", "No", False),
        ("triage", "package", "", False),
        ("package", "d_tier", "", False),
        ("d_tier", "low", "Low", False),
        ("d_tier", "vote", "Mod. / High", False),
        ("vote", "reject", "Rejected", False),
        ("vote", "cdt_m", "Moderate", False),
        ("vote", "high", "High", False),
        ("low", "issue", "", False),
        ("cdt_m", "issue", "", False),
        ("high", "issue", "", False),
        ("issue", "procure", "", False),
        ("procure", "operate", "", False),
        ("operate", "d_rr", "", False),
        ("operate", "suspend", "Incident", False),
        ("d_rr", "triage", "Yes", False),
    ],
)

LEGACY = Diagram(
    name="legacy-use-registration",
    title="Legacy Use registration (first 90 days)",
    lanes=[("", "#FFFFFF"), ("", "#FFFFFF"), ("", "#FFFFFF")],
    phases=[],
    n_cols=6,
    lane_h=110,
    nodes={
        "adopt":    (1, 0, "mid", "start", "Policy adopted"),
        "window":   (1, 1, "mid", "process", "90-day registration window opens"),
        "late":     (0, 2, "mid", "stop", "After 90 days: unregistered AI is a security incident"),
        "register": (1, 2, "mid", "process", "Units and IT register all AI in use, incl. vendor-added SaaS features"),
        "d_proh":   (1, 3, "mid", "decision", "Prohibited use?"),
        "stop":     (2, 3, "mid", "stop", "Stop the use"),
        "legacy":   (1, 4, "mid", "good", "Flag as Legacy Use; keep running"),
        "triage":   (1, 5, "mid", "process", "Normal triage and Assessment Package, High first"),
    },
    edges=[
        ("adopt", "window", "", False),
        ("window", "register", "", False),
        ("window", "late", "", True, "down"),
        ("register", "d_proh", "", False),
        ("d_proh", "stop", "Yes", False),
        ("d_proh", "legacy", "No", False),
        ("legacy", "triage", "", False),
    ],
)

DIAGRAMS = [SWIMLANE, OVERVIEW, LEGACY]

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for d in DIAGRAMS:
        with open(os.path.join(OUT_DIR, d.name + ".svg"), "w", encoding="utf-8") as fh:
            fh.write(d.svg())
        with open(os.path.join(OUT_DIR, d.name + ".drawio"), "w", encoding="utf-8") as fh:
            fh.write(d.drawio())
        print("wrote", d.name)
