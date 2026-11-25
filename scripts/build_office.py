#!/usr/bin/env python3
"""Build fillable Word forms and the Excel AI Inventory from the Markdown sources.

The Markdown files stay the source of truth. Edit them, then run:
    pip install python-docx openpyxl
    python3 scripts/build_office.py

Outputs:
    forms/word/<Form-Name>.docx   one per forms/*.md, with content controls
                                  (checkboxes and "click to enter text" fields)
    inventory/AI-Inventory.xlsx   Tools, Use Cases and Pre-approved Log sheets with
                                  dropdowns, plus the field guide

How Markdown becomes form fields:
    ☐ option            a checkbox content control
    [placeholder]       a text field showing the placeholder as its hint
    empty table cell    a text field
    "Label:" at the end of a line, or before "·" or "☐"   a text field after it
    numbered question with no checkboxes                  an answer field below it
    **Label:** · **Label:** header line                   a two-column field table
"""
import csv
import os
import re

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
FORMS_DIR = os.path.join(ROOT, "forms")
WORD_DIR = os.path.join(FORMS_DIR, "word")
INV_DIR = os.path.join(ROOT, "inventory")

FONT = "Calibri"
NAVY = RGBColor(0x1F, 0x38, 0x64)
GREY = RGBColor(0x59, 0x59, 0x59)
FOOTER = "CAGovAI · CC BY 4.0 · Generated from the Markdown form; check the repository for the current version."

# Paragraphs that are questions without a trailing colon or number. Matched by prefix.
ANSWER_PROMPTS = (
    "Why the requirement cannot be met now",
    "What could go wrong while the requirement",
    "How affected employees were consulted",
    "What will be tracked",
    "Describe the test data",
)
# Forms with wide tables are laid out in landscape.
LANDSCAPE = {"Rating-Scales", "AI-Impact-Assessment", "Approved-Uses-Register", "Risk-Acceptance", "Workforce-Impact-Assessment"}


# =========================================================================
# Word: content controls
# =========================================================================
_sdt_id = [1000]


def _next_id():
    _sdt_id[0] += 1
    return str(_sdt_id[0])


def _run(text, bold=False, italic=False, color=None, size=None, font=None):
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    if font:
        f = OxmlElement("w:rFonts")
        for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            f.set(qn(a), font)
        rpr.append(f)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    if color:
        c = OxmlElement("w:color")
        c.set(qn("w:val"), color)
        rpr.append(c)
    if size:
        s = OxmlElement("w:sz")
        s.set(qn("w:val"), str(int(size * 2)))
        rpr.append(s)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    r.append(t)
    return r


def checkbox(label=""):
    sdt = OxmlElement("w:sdt")
    pr = OxmlElement("w:sdtPr")
    if label:
        tag = OxmlElement("w:tag")
        tag.set(qn("w:val"), label[:60])
        pr.append(tag)
    i = OxmlElement("w:id")
    i.set(qn("w:val"), _next_id())
    pr.append(i)
    cb = OxmlElement("w14:checkbox")
    for name, val in (("w14:checked", "0"),):
        e = OxmlElement(name)
        e.set(qn("w14:val"), val)
        cb.append(e)
    for name, code in (("w14:checkedState", "2612"), ("w14:uncheckedState", "2610")):
        e = OxmlElement(name)
        e.set(qn("w14:val"), code)
        e.set(qn("w14:font"), "MS Gothic")
        cb.append(e)
    pr.append(cb)
    sdt.append(pr)
    content = OxmlElement("w:sdtContent")
    content.append(_run("☐", font="MS Gothic"))
    sdt.append(content)
    return sdt


def text_field(hint="Click or tap to enter text.", label="", multiline=True):
    sdt = OxmlElement("w:sdt")
    pr = OxmlElement("w:sdtPr")
    if label:
        tag = OxmlElement("w:tag")
        tag.set(qn("w:val"), label[:60])
        pr.append(tag)
    i = OxmlElement("w:id")
    i.set(qn("w:val"), _next_id())
    pr.append(i)
    pr.append(OxmlElement("w:showingPlcHdr"))
    t = OxmlElement("w:text")
    if multiline:
        t.set(qn("w:multiLine"), "1")
    pr.append(t)
    sdt.append(pr)
    content = OxmlElement("w:sdtContent")
    content.append(_run(hint, color="7F7F7F"))
    sdt.append(content)
    return sdt


# =========================================================================
# Word: inline Markdown
# =========================================================================
LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
TOKEN = re.compile(r"(\*\*.+?\*\*|\*[^*\s][^*]*\*|\[[^\]]*\]|☐|↦[^·☐]*)")


def add_inline(p, text, base_bold=False, size=None):
    """Append Markdown inline text to paragraph p, turning checkboxes, [placeholders]
    and label colons into content controls."""
    text = LINK.sub(r"\1", text).replace("`", "")
    parts = [x for x in TOKEN.split(text) if x]
    for k, part in enumerate(parts):
        prev = parts[k - 1] if k else ""
        nxt = parts[k + 1] if k + 1 < len(parts) else ""
        if part == "☐":
            p._p.append(checkbox())
        elif part.startswith("**") and part.endswith("**"):
            p._p.append(_run(part[2:-2], bold=True, size=size))
        elif len(part) > 2 and part.startswith("*") and part.endswith("*"):
            p._p.append(_run(part[1:-1], italic=True, bold=base_bold, size=size))
        elif part.startswith("[") and part.endswith("]"):
            hint = part[1:-1].strip()
            if hint.endswith(":"):  # "[Request ID: ]" -> label + field
                p._p.append(_run(hint + " ", size=size))
                p._p.append(text_field("enter", multiline=False))
            else:
                p._p.append(text_field(hint or "enter", multiline=False))
        elif part.startswith("↦"):
            p._p.append(_run(part.rstrip() + " ", italic=True, color="7F7F7F", size=(size or 10.5) - 1.5))
        else:
            after_placeholder = prev.startswith("[") and prev.endswith("]")
            # "label: · next label" inside the text
            bits = re.split(r"(:\s*·)", part)
            for m, bit in enumerate(bits):
                if re.fullmatch(r":\s*·", bit):
                    p._p.append(_run(":  ", bold=base_bold, size=size))
                    p._p.append(text_field(multiline=False))
                    p._p.append(_run("   ·", bold=base_bold, size=size))
                    continue
                if not bit:
                    continue
                is_last = m == len(bits) - 1
                ends_colon = re.search(r":\s*$", bit) is not None
                # a colon opens a field at the end of a line, before "·", or after a
                # checkbox option such as "☐ Yes — describe:" followed by more options
                opens_field = (is_last and ends_colon
                               and (nxt == "" or nxt.lstrip().startswith("·") or (nxt == "☐" and prev == "☐"))
                               and not (after_placeholder and bit.strip() == ":"))
                p._p.append(_run(bit.rstrip() + " " if opens_field else bit, bold=base_bold, size=size))
                if opens_field:
                    p._p.append(text_field(multiline=nxt == ""))
                    if nxt == "☐":
                        p._p.append(_run("   ", size=size))


# =========================================================================
# Word: blocks
# =========================================================================
PPR_AFTER_SHD = ("w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap", "w:overflowPunct",
                 "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN", "w:bidi", "w:adjustRightInd",
                 "w:snapToGrid", "w:spacing", "w:ind", "w:contextualSpacing", "w:mirrorIndents",
                 "w:suppressOverlap", "w:jc", "w:textDirection", "w:textAlignment",
                 "w:textboxTightWrap", "w:outlineLvl", "w:divId", "w:cnfStyle", "w:rPr",
                 "w:sectPr", "w:pPrChange")


def ppr_insert(p, el):
    """Insert a pPr child in schema order (Word rejects out-of-order elements)."""
    ppr = p._p.get_or_add_pPr()
    order = ("w:pBdr", "w:shd") + PPR_AFTER_SHD
    tag = el.tag
    idx = [qn(t) for t in order].index(tag)
    ppr.insert_element_before(el, *order[idx + 1:])


def set_color(r_el, hexval):
    rpr = r_el.find(qn("w:rPr"))
    rpr.get_or_add_color().set(qn("w:val"), hexval)


def shade(cell, fill):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcpr.append(shd)


def para_border_shade(p, fill="EEF3FA", border="8EA9DB"):
    bdr = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "18")
    left.set(qn("w:space"), "6")
    left.set(qn("w:color"), border)
    bdr.append(left)
    ppr_insert(p, bdr)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    ppr_insert(p, shd)


def fix_widths(t, widths):
    """Set column widths (inches) in the grid and every cell, with fixed layout,
    so Word and LibreOffice both honour them."""
    t.autofit = False
    grid = t._tbl.tblGrid
    for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(int(widths[j] * 1440)))
    for row in t.rows:
        trpr = row._tr.get_or_add_trPr()
        trpr.append(OxmlElement("w:cantSplit"))
        for j, c in enumerate(row.cells):
            c.width = Inches(widths[j])


def answer_box(doc):
    """A boxed, multi-line answer field under a question."""
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    fix_widths(t, [doc._cagov_width])
    c = t.cell(0, 0)
    p = c.paragraphs[0]
    p._p.append(text_field())
    p.paragraph_format.space_after = Pt(18)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def add_table(doc, rows, landscape):
    if doc.paragraphs:  # keep the lead-in sentence or heading on the table's page
        doc.paragraphs[-1].paragraph_format.keep_with_next = True
    header, body = rows[0], rows[2:]
    n = len(header)
    blank_header = all(h == "" for h in header)
    t = doc.add_table(rows=0, cols=n)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    if not blank_header:
        cells = t.add_row().cells
        for j, h in enumerate(header):
            p = cells[j].paragraphs[0]
            add_inline(p, h, base_bold=True, size=9.5)
            for r in p._p.iter(qn("w:r")):
                set_color(r, "FFFFFF")
            shade(cells[j], "1F3864")
        tr = t.rows[0]._tr
        trpr = tr.get_or_add_trPr()
        th = OxmlElement("w:tblHeader")
        trpr.append(th)
    for row in body:
        row = (row + [""] * n)[:n]
        cells = t.add_row().cells
        for j, val in enumerate(row):
            p = cells[j].paragraphs[0]
            if val == "":
                p._p.append(text_field("Enter text.", multiline=True))
            elif re.fullmatch(r"\[[^\]]*\]", val):
                p._p.append(text_field(val[1:-1]))
            else:
                first_col_label = blank_header and j == 0
                add_inline(p, val, base_bold=first_col_label, size=9.5)
                if val.strip() in ("☐",):
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if blank_header and j == 0:
                shade(cells[j], "EEF3FA")
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                p.paragraph_format.space_after = Pt(2)
    page_w = 9.5 if landscape else 7.0
    if blank_header and n == 2:
        widths = [2.6, page_w - 2.6]
    else:
        weights = []
        for j in range(n):
            col = [r[j] if j < len(r) else "" for r in body]
            if col and all(v == "☐" for v in col):
                weights.append(max(4, len(header[j]) + 1))
                continue
            lens = [len(LINK.sub(r"\1", v)) if v else 16 for v in col] + [len(header[j]) + 2]
            weights.append(min(55, max(9, max(lens))))
        total = sum(weights)
        widths = [page_w * w / total for w in weights]
        # no column narrower than 0.75 in, so short values like "Medium" never wrap
        short = [j for j, w in enumerate(widths) if w < 0.75]
        if short and len(short) < n:
            spare = page_w - 0.75 * len(short)
            rest = sum(weights[j] for j in range(n) if j not in short)
            widths = [0.75 if j in short else spare * weights[j] / rest for j in range(n)]
    fix_widths(t, widths)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def header_fields(doc, line, landscape):
    """**Label:** value · **Label:** value  ->  two-column field table."""
    t = doc.add_table(rows=0, cols=2)
    t.style = "Table Grid"
    for chunk in [c.strip() for c in line.split(" · ")]:
        m = re.match(r"\*\*(.+?):\*\*\s*(.*)", chunk)
        if not m:
            continue
        label, val = m.group(1), m.group(2).strip()
        cells = t.add_row().cells
        cells[0].paragraphs[0]._p.append(_run(label, bold=True, size=9.5))
        shade(cells[0], "EEF3FA")
        p = cells[1].paragraphs[0]
        if val == "":
            p._p.append(text_field(multiline=False))
        elif re.fullmatch(r"\[[^\]]*\]", val):
            p._p.append(text_field(val[1:-1], multiline=False))
        else:
            add_inline(p, val, size=9.5)
    fix_widths(t, [2.2, 4.8 if not landscape else 7.3])
    for row in t.rows:
        for c in row.cells:
            c.paragraphs[0].paragraph_format.space_after = Pt(2)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def set_cell_margins(doc):
    for t in doc.tables:
        tblpr = t._tbl.tblPr
        mar = OxmlElement("w:tblCellMar")
        for side, v in (("top", 40), ("bottom", 40), ("left", 80), ("right", 80)):
            e = OxmlElement(f"w:{side}")
            e.set(qn("w:w"), str(v))
            e.set(qn("w:type"), "dxa")
            mar.append(e)
        tblpr.insert_element_before(mar, "w:tblLook", "w:tblCaption", "w:tblDescription", "w:tblPrChange")


def add_page_number(p):
    for kind, text in (("begin", None), (None, " PAGE "), ("end", None)):
        r = OxmlElement("w:r")
        if kind:
            fc = OxmlElement("w:fldChar")
            fc.set(qn("w:fldCharType"), kind)
            r.append(fc)
        else:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = text
            r.append(it)
        p._p.append(r)


def setup_document(title, landscape):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = Inches(11), Inches(8.5)
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, side, Inches(0.75))
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    st.paragraph_format.space_after = Pt(4)
    for name, size, color in (("Title", 18, NAVY), ("Heading 1", 13, NAVY), ("Heading 2", 11.5, NAVY)):
        s = doc.styles[name]
        s.font.name = FONT
        s.font.size = Pt(size)
        s.font.color.rgb = color
        s.font.bold = True
        rpr = s.element.get_or_add_rPr()
        rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts")
            rpr.append(rf)
        for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs", "w:asciiTheme", "w:hAnsiTheme"):
            if a.endswith("Theme"):
                if rf.get(qn(a)) is not None:
                    del rf.attrib[qn(a)]
            else:
                rf.set(qn(a), FONT)
        s.paragraph_format.space_before = Pt(10 if name != "Title" else 0)
        s.paragraph_format.space_after = Pt(4)
    # title style: remove the default bottom border spacing quirks
    hp = sec.header.paragraphs[0]
    hp.text = "[State Entity]  ·  " + title
    hp.runs[0].font.size = Pt(8.5)
    hp.runs[0].font.color.rgb = GREY
    fp = sec.footer.paragraphs[0]
    r = fp.add_run(FOOTER + "   Page ")
    r.font.size = Pt(8)
    r.font.color.rgb = GREY
    add_page_number(fp)
    doc._cagov_width = 9.5 if landscape else 7.0
    doc.core_properties.title = title
    doc.core_properties.author = "CAGovAI"
    doc.core_properties.comments = "Generated by scripts/build_office.py from forms/*.md (CC BY 4.0)."
    return doc


INCLUDE = re.compile(r"<!--\s*include:\s*(\S+)\s*-->")
# Reference pages built as Word documents but without answer boxes.
REFERENCE_ONLY = {"Rating-Scales"}


def expand_includes(lines, base_dir):
    """Replace <!-- include: File.md --> with that file as an appendix on a new page.
    GitHub hides the comment, so the Markdown form keeps just its link to the file."""
    out = []
    for line in lines:
        m = INCLUDE.fullmatch(line.strip())
        if not m:
            out.append(line)
            continue
        with open(os.path.join(base_dir, m.group(1)), encoding="utf-8") as fh:
            inc = fh.read().splitlines()
        out += ["<!-- pagebreak -->", "<!-- noanswers -->"]
        for l in inc:
            if l.startswith("# "):
                l = "## Appendix: " + l[2:]
            elif l.startswith("## "):
                l = "#" + l
            out.append(l)
        out.append("<!-- /noanswers -->")
    return out


def build_form(md_path, out_path):
    name = os.path.splitext(os.path.basename(md_path))[0]
    landscape = name in LANDSCAPE
    with open(md_path, encoding="utf-8") as fh:
        lines = expand_includes(fh.read().splitlines(), os.path.dirname(md_path))
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), name)
    doc = setup_document(LINK.sub(r"\1", title), landscape)
    no_answers = name in REFERENCE_ONLY

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("<!--"):
            if "pagebreak" in s:
                doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            elif "/noanswers" in s:
                no_answers = name in REFERENCE_ONLY
            elif "noanswers" in s:
                no_answers = True
            i += 1
            continue
        if s.startswith("# "):
            p = doc.add_paragraph(style="Title")
            add_inline(p, s[2:])
        elif s.startswith("## "):
            doc.add_paragraph(LINK.sub(r"\1", s[3:]), style="Heading 1")
        elif s.startswith("### "):
            doc.add_paragraph(LINK.sub(r"\1", s[4:]), style="Heading 2")
        elif s == "---":
            p = doc.add_paragraph()
            pb = OxmlElement("w:pBdr")
            b = OxmlElement("w:bottom")
            for k, v in (("w:val", "single"), ("w:sz", "6"), ("w:space", "1"), ("w:color", "8EA9DB")):
                b.set(qn(k), v)
            pb.append(b)
            ppr_insert(p, pb)
        elif s.startswith(">"):
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i].strip()[1:].strip())
                i += 1
            # paragraphs split on blank ">" lines; each "- " line is its own bullet
            paras = []
            for chunk in "\n".join(block).split("\n\n"):
                for ln in chunk.split("\n"):
                    if ln.startswith("- ") or not paras or paras[-1][0] or paras[-1][1] == "":
                        paras.append([ln.startswith("- "), ln[2:] if ln.startswith("- ") else ln])
                    else:
                        paras[-1][1] += " " + ln
                paras.append([False, ""])
            for is_bullet, txt in paras:
                if not txt.strip():
                    continue
                p = doc.add_paragraph()
                if is_bullet:
                    p.paragraph_format.left_indent = Inches(0.2)
                    p.paragraph_format.first_line_indent = Inches(-0.15)
                    p.paragraph_format.space_after = Pt(1)
                    p._p.append(_run("•  ", size=9.5))
                add_inline(p, txt, size=9.5)
                for r in p._p.iter(qn("w:r")):
                    rpr = r.find(qn("w:rPr"))
                    if rpr is not None and rpr.find(qn("w:color")) is None:
                        set_color(r, "404040")
                para_border_shade(p)
            doc.add_paragraph().paragraph_format.space_after = Pt(0)
            continue
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            add_table(doc, rows, landscape)
            continue
        elif re.match(r"\*\*[^*]+:\*\*", s) and " · " in s and s.count("**") >= 4:
            header_fields(doc, s, landscape)
        elif re.match(r"\d+\.\s", s) or s.startswith("- "):
            numbered = bool(re.match(r"\d+\.\s", s))
            text = re.sub(r"^(\d+\.|-)\s+", "", s)
            num = re.match(r"(\d+)\.", s).group(1) if numbered else None
            # continuation lines belong to the item
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(
                    r"(\d+\.\s|- |#|\||>)", lines[i + 1].strip()):
                i += 1
                text += "\n" + lines[i].strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            p.paragraph_format.first_line_indent = Inches(-0.3)
            p._p.append(_run((num + ".\t") if numbered else "•\t"))
            tabs = OxmlElement("w:tabs")
            tab = OxmlElement("w:tab")
            tab.set(qn("w:val"), "left")
            tab.set(qn("w:pos"), str(int(0.3 * 1440)))
            tabs.append(tab)
            ppr_insert(p, tabs)
            for k, chunk in enumerate(text.split("\n")):
                if k:
                    p._p.append(OxmlElement("w:br"))
                add_inline(p, chunk)
            if numbered and not no_answers and "☐" not in text and not re.search(r":\s*$", text):
                p.paragraph_format.keep_with_next = True
                answer_box(doc)
        else:
            text = s
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(
                    r"(\d+\.\s|- |#|\||>)", lines[i + 1].strip()):
                i += 1
                text += " " + lines[i].strip()
            p = doc.add_paragraph()
            add_inline(p, text)
            if text.startswith(ANSWER_PROMPTS) and not no_answers:
                p.paragraph_format.keep_with_next = True
                answer_box(doc)
        i += 1
    set_cell_margins(doc)
    doc.save(out_path)


# =========================================================================
# Excel inventory
# =========================================================================
TOOL_STATUS = ["Proposed", "Active", "Suspended", "Retired"]
USE_STATUS = ["Proposed", "Approved", "Active", "Suspended", "Retired"]
YES_NO = ["Yes", "No"]
LISTS = {
    "delivery": ["SaaS", "PaaS", "IaaS", "On-premises", "Extension", "Embedded feature"],
    "risk_tier": ["Low", "Moderate", "High"],
    "autonomy_level": ["A0", "A1", "A2", "A3"],
    "audience_uc": ["Unit", "Agency-wide", "External government", "Public"],
    "decided_by": ["Triage Panel", "Committee", "Director"],
    "audience_pa": ["Personal / unit", "Agency-wide", "Public / external"],
}


def read_guide():
    """Field descriptions and Public flags from inventory/README.md tables."""
    guide = {}
    section = None
    with open(os.path.join(INV_DIR, "README.md"), encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"## (\S+\.csv)", line)
            if m:
                section = m.group(1)
                continue
            if section and line.startswith("| `"):
                cells = split_row(line)
                for f in re.findall(r"`([^`]+)`", cells[0]):
                    guide[(section, f)] = (cells[1], cells[2] if len(cells) > 2 else "")
    return guide


def approved_use_categories():
    cats = []
    with open(os.path.join(FORMS_DIR, "Approved-Uses-Register.md"), encoding="utf-8") as fh:
        in_reg = False
        for line in fh:
            if line.startswith("## Register"):
                in_reg = True
                continue
            if in_reg and line.startswith("## "):
                break
            if in_reg and line.startswith("| ") and not line.startswith("| SIMM") and "---" not in line:
                cats.append(split_row(line)[0])
    return cats


def build_inventory(out_path):
    guide = read_guide()
    wb = Workbook()
    hdr_fill = PatternFill("solid", fgColor="1F3864")
    pub_fill = PatternFill("solid", fgColor="2E75B6")
    wrap = Alignment(wrap_text=True, vertical="top")

    # ---- Lists sheet (dropdown sources)
    ws_l = wb.active
    ws_l.title = "Lists"
    lists = dict(LISTS)
    lists["yes_no"] = YES_NO
    lists["tool_status"] = TOOL_STATUS
    lists["use_status"] = USE_STATUS
    lists["approved_use_category"] = approved_use_categories()
    refs = {}
    for c, (key, vals) in enumerate(lists.items(), start=1):
        col = get_column_letter(c)
        ws_l.cell(row=1, column=c, value=key).font = Font(bold=True)
        for r, v in enumerate(vals, start=2):
            ws_l.cell(row=r, column=c, value=v)
        refs[key] = f"Lists!${col}$2:${col}${len(vals) + 1}"
        ws_l.column_dimensions[col].width = max(14, max(len(v) for v in vals) + 2)

    sheets = [
        ("Tools", "tools.csv", "Tools", {
            "delivery": "delivery", "is_genai": "yes_no", "records_export_confirmed": "yes_no",
            "status": "tool_status"}),
        ("Use Cases", "use-cases.csv", "UseCases", {
            "tool_id": "@tool_id", "risk_tier": "risk_tier", "autonomy_level": "autonomy_level",
            "audience": "audience_uc", "decisions_about_people": "yes_no", "high_risk_ads": "yes_no",
            "decided_by": "decided_by", "status": "use_status", "legacy_use": "yes_no"}),
        ("Pre-approved Log", "pre-approved-log.csv", "PreApprovedLog", {
            "tool_id": "@tool_id", "approved_use_category": "approved_use_category",
            "audience": "audience_pa", "training_current": "yes_no", "aup_acknowledged": "yes_no"}),
    ]
    readme = wb.create_sheet("Read me", 0)
    guide_ws = wb.create_sheet("Field guide", 1)
    guide_ws.append(["Sheet", "Field", "What to record", "Public"])
    for cell in guide_ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = hdr_fill

    n_rows = 500
    for title, csv_name, table_name, validations in sheets:
        ws = wb.create_sheet(title)
        with open(os.path.join(INV_DIR, csv_name), encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh))
        header, examples = rows[0], rows[1:]
        ws.append(header)
        for ex in examples:
            ws.append(ex)
        for j, h in enumerate(header, start=1):
            cell = ws.cell(row=1, column=j)
            desc, public = guide.get((csv_name, h), ("", ""))
            is_public = "●" in public
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = pub_fill if is_public else hdr_fill
            cell.alignment = Alignment(wrap_text=True, vertical="center")
            note = desc or h
            if is_public:
                note += "\n\nPublic: goes in the public AI use summary."
            elif public:
                note += f"\n\nPublic: {public}."
            cell.comment = Comment(note, "CAGovAI", width=260, height=110)
            width = max(len(h) + 4, min(40, max([len(str(r[j - 1])) for r in examples] + [10]) + 2))
            ws.column_dimensions[get_column_letter(j)].width = width
            if csv_name != "pre-approved-log.csv" or desc:
                guide_ws.append([title, h, desc, "Yes" if is_public else ("Unit only" if public else "")])
            else:
                guide_ws.append([title, h, "", ""])
            if h.endswith("_date") or h == "entry_date":
                for r in range(2, n_rows + 2):
                    ws.cell(row=r, column=j).number_format = "yyyy-mm-dd"
        for r in range(2, 2 + len(examples)):
            for j in range(1, len(header) + 1):
                ws.cell(row=r, column=j).alignment = wrap
                ws.cell(row=r, column=j).font = Font(italic=True, color="7F7F7F")
        last = get_column_letter(len(header))
        tab = Table(displayName=table_name, ref=f"A1:{last}{n_rows + 1}")
        tab.tableStyleInfo = TableStyleInfo(name="TableStyleLight9", showRowStripes=True)
        ws.add_table(tab)
        ws.freeze_panes = "B2"
        ws.row_dimensions[1].height = 30
        for field, key in validations.items():
            j = header.index(field) + 1
            col = get_column_letter(j)
            if key == "@tool_id":
                src = f"Tools!$A$2:$A${n_rows + 1}"
                dv = DataValidation(type="list", formula1=src, allow_blank=True, showErrorMessage=False)
            else:
                dv = DataValidation(type="list", formula1=refs[key], allow_blank=True,
                                    showErrorMessage=True, errorTitle="Not on the list",
                                    error="Pick a value from the dropdown. Lists are on the Lists sheet.")
            ws.add_data_validation(dv)
            dv.add(f"{col}2:{col}{n_rows + 1}")

    for col, w in zip("ABCD", (16, 30, 70, 10)):
        guide_ws.column_dimensions[col].width = w
    for row in guide_ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = wrap
    guide_ws.freeze_panes = "A2"

    readme.column_dimensions["A"].width = 110
    text = [
        ("AI Inventory: [State Entity]", Font(bold=True, size=16, color="1F3864")),
        ("The single register of AI at [State Entity] (Procedure 02, AI Inventory).", None),
        ("", None),
        ("Sheets", Font(bold=True, size=12, color="1F3864")),
        ("Tools: one row per approved (or registered Legacy) AI Tool.", None),
        ("Use Cases: one row per Use Case, linked to its Tool by tool_id (dropdown from the Tools sheet).", None),
        ("Pre-approved Log: one row per Pre-approved use attested by a manager.", None),
        ("Field guide: what to record in every column. Hover over a column header for the same note.", None),
        ("Lists: the values behind the dropdowns. Change them only if your entity changes the framework.", None),
        ("", None),
        ("How to use", Font(bold=True, size=12, color="1F3864")),
        ("1. Delete the grey example rows before use.", None),
        ("2. Lighter blue headers mark Public fields: only these go into the public AI use summary.", None),
        ("3. Keep the live inventory in an access-controlled location. It is kept by the AI Governance Coordinator.", None),
        ("4. CDT high-risk export: filter Use Cases on risk_tier = High or high_risk_ads = Yes.", None),
        ("5. Never paste completed SIMM 5305-F, SIMM 150 or security reviews here. They are confidential.", None),
        ("", None),
        ("Generated by scripts/build_office.py from inventory/*.csv and inventory/README.md (CAGovAI, CC BY 4.0).", Font(italic=True, color="7F7F7F")),
    ]
    for r, (t, f) in enumerate(text, start=1):
        c = readme.cell(row=r, column=1, value=t)
        c.alignment = Alignment(wrap_text=True)
        if f:
            c.font = f
    wb.move_sheet("Lists", offset=len(wb.sheetnames))
    wb.active = 0
    wb.properties.creator = "CAGovAI"
    wb.properties.title = "AI Inventory"
    wb.save(out_path)


def main():
    os.makedirs(WORD_DIR, exist_ok=True)
    for f in sorted(os.listdir(FORMS_DIR)):
        if f.endswith(".md") and f != "README.md":
            out = os.path.join(WORD_DIR, f[:-3] + ".docx")
            build_form(os.path.join(FORMS_DIR, f), out)
            print("wrote", os.path.relpath(out, ROOT))
    out = os.path.join(INV_DIR, "AI-Inventory.xlsx")
    build_inventory(out)
    print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
