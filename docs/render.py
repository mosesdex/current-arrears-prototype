#!/usr/bin/env python3
"""Render docs/walkthrough.html to a paginated PDF with a stamped footer.

Chrome does the typesetting; the footer is stamped afterwards because Chrome
does not support CSS margin boxes, and a position:fixed footer lands in the
middle of the text block in paged output rather than at the foot of the page.

    python3 docs/render.py
"""
import subprocess
import sys
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
FOOTER_LEFT = 'Current — arrears platform prototype'
FOOTER_MID = 'Synthetic data throughout · not a production system'


def main() -> int:
    src, raw, out = HERE / 'walkthrough.html', HERE / '.raw.pdf', HERE / 'Current-prototype-walkthrough.pdf'
    if not Path(CHROME).exists():
        print('Chrome not found at %s' % CHROME, file=sys.stderr)
        return 1

    subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
                    '--virtual-time-budget=6000', '--print-to-pdf=%s' % raw,
                    src.as_uri()], check=True, capture_output=True)

    reader = PdfReader(raw)
    total = len(reader.pages)
    w, h = A4
    mm = 72 / 25.4
    ink, rule = Color(0.52, 0.46, 0.44), Color(0.886, 0.859, 0.851)

    writer = PdfWriter()
    for i, page in enumerate(reader.pages, start=1):
        buf = BytesIO()
        c = canvas.Canvas(buf, pagesize=A4)
        x0, x1, y = 16 * mm, w - 16 * mm, 13 * mm
        if i > 1:  # the cover carries its own rule
            c.setStrokeColor(rule)
            c.setLineWidth(0.5)
            c.line(x0, y + 3.2 * mm, x1, y + 3.2 * mm)
        c.setFillColor(ink)
        c.setFont('Helvetica', 7.2)
        c.drawString(x0, y, FOOTER_LEFT)
        c.drawCentredString(w / 2, y, FOOTER_MID)
        c.setFont('Helvetica-Bold', 7.2)
        c.drawRightString(x1, y, '%d / %d' % (i, total))
        c.save()
        buf.seek(0)
        page.merge_page(PdfReader(buf).pages[0])
        writer.add_page(page)

    writer.add_metadata({
        '/Title': 'Current — arrears platform prototype: walkthrough',
        '/Subject': 'What the prototype is, what it argues, and how to demonstrate it',
        '/Author': 'Current',
        '/Creator': 'Current',
    })
    with open(out, 'wb') as f:
        writer.write(f)
    raw.unlink(missing_ok=True)
    print('wrote %s (%d pages)' % (out.name, total))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
