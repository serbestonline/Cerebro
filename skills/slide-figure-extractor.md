---
name: slide-figure-extractor
description: Extract figures from lecture slide PDFs and embed them into Anki flashcard Fronts. Detects the figure region on each slide, crops away the title and citation, renders it as JPEG, attaches it to the matching card, and installs the media into Anki. Course-agnostic. Inherits card and TSV rules from flashcard-generator.md.
inherits: flashcard-generator.md
---

# Slide Figure Extractor

Lecture slides carry diagrams, micrographs, waveforms, scans, and formulas that a text-only card cannot replace. This skill puts the lecturer's actual figure on the card Front.

The core idea: **crop the figure, not the slide.** Pasting a whole page drags in the title (which usually states the answer), bullet text, and citation lines. What belongs on the card is the figure region alone.

---

## Requirements

```bash
pip install pymupdf pillow    # see requirements.txt
```

`pdfimages` / `pdftoppm` (poppler) are not needed — PyMuPDF handles detection and rendering.

---

## The Cropper

Save as `assets/slide_figure_cropper.py` and import it; do not re-implement page rendering by hand.

```python
import fitz, re

CITE = re.compile(r'(et al|\b(19|20)\d{2}\b|Journal|NeuroImage|Neuroscience|Nobel)', re.I)


def figure_bbox(page):
    """Bounding box of the figure region on a slide, or None if the slide is text-only."""
    pr = page.rect
    parea = pr.get_area()
    H = pr.height
    boxes = []

    # embedded raster images (photos, micrographs, screenshots)
    for img in page.get_images(full=True):
        for r in page.get_image_rects(img[0]):
            if 0.004 * parea < r.get_area() < 0.92 * parea:
                boxes.append(r)

    # vector drawings (flow charts, plots, arrows drawn in PowerPoint)
    for dr in page.get_drawings():
        r = dr["rect"]
        if 0.002 * parea < r.get_area() < 0.92 * parea:
            boxes.append(r)

    if not boxes:
        return None

    F = boxes[0]
    for b in boxes[1:]:
        F = F | b
    F = F & pr

    blocks = [b for b in page.get_text("blocks") if b[4].strip()]

    # 1) clip away the slide title bleeding into the top of the figure
    for x0, y0, x1, y1, txt, *_ in blocks:
        if y0 < 0.25 * H and y1 > F.y0 - 5 and y1 < F.y0 + 0.14 * F.height:
            F.y0 = max(F.y0, y1 + 3)

    # 2) clip away the citation line at the bottom
    for x0, y0, x1, y1, txt, *_ in blocks:
        if y1 > 0.84 * H and CITE.search(txt) and y0 < F.y1 and y0 > F.y1 - 0.30 * F.height:
            F.y1 = min(F.y1, y0 - 2)

    # 3) pull in annotation labels that hug the figure (axis labels, R values, arrows)
    near = fitz.Rect(F.x0 - 30, F.y0 - 8, F.x1 + 30, F.y1 + 8)
    for x0, y0, x1, y1, txt, *_ in blocks:
        r = fitz.Rect(x0, y0, x1, y1)
        if y0 < 0.16 * H or (y1 > 0.84 * H and CITE.search(txt)):
            continue
        if r.intersects(near) and r.get_area() < 0.25 * parea:
            F = F | r

    return (F & pr) if F.height > 40 and F.width > 40 else None


def crop(pdf, pno, dest, dpi=150, pad=6, quality=86):
    """Render page `pno` (1-based) cropped to its figure. Returns dest, or None if no figure."""
    d = fitz.open(pdf)
    p = d[pno - 1]
    F = figure_bbox(p)
    if F is None:
        return None
    F = fitz.Rect(F.x0 - pad, F.y0 - pad, F.x1 + pad, F.y1 + pad) & p.rect
    p.get_pixmap(dpi=dpi, clip=F).pil_save(dest, format="JPEG", quality=quality, optimize=True)
    return dest
```

**Why these thresholds:** the area filters drop page-background rectangles (>92%) and decorative bullets or logos (<0.4%). The title clip handles the common case where a picture box starts underneath the title text. Step 3 matters more than it looks — without it, axis labels and annotations like `R > +0.6` get sliced off, because they are text objects sitting outside the image rectangle.

---

## Workflow

### 1. Inventory the deck's PDF

```python
import fitz
d = fitz.open(pdf_path)
for i, p in enumerate(d):
    print(i + 1, len(p.get_images(full=True)), " ".join(p.get_text().split())[:70])
```

This tells you which slides carry figures and what each one is about. Pages showing `0` images may still hold vector diagrams — the cropper finds those.

### 2. Map pages to cards

Read the deck and pair each figure slide with the card it supports. Judgment rules:

- **Map** genuine figures: diagrams, micrographs, waveforms, scans, molecular structures, equipment photos, formulas, plotted results.
- **Skip** pure bullet-text slides — nothing to show.
- **Skip** slides whose visible text spells out the card's answer. A slide titled "The four advantages of neurofeedback" with all four listed turns its cloze card into a freebie. Record these as deliberate skips.
- A figure may serve two cards; a card takes at most one figure.
- Expect roughly 50-75% coverage. Leaving text-only cards without images is the correct outcome, not a failure.

### 3. Generate the crops

```python
crop(pdf, page_no, f"Flashcards/media/{course}-l{lec:02d}-p{page_no:02d}-{slug}.jpg")
```

Naming: `ibf-l12-p34-tms-mep-recording.jpg` — course prefix, lecture, zero-padded page, short kebab slug. The course prefix keeps filenames unique inside Anki's flat shared `collection.media/`.

Expect roughly 40-100 KB per figure at 150 dpi / quality 86.

### 4. Verify visually — do not skip this

Open 3-4 of the generated JPEGs and confirm:

- the figure is complete and not sliced through
- no slide title bleeding in at the top
- axis labels, legends, and annotations are inside the frame
- the crop is not just a stray logo or a blank region

If a crop is bad, drop that page rather than shipping a broken image.

### 5. Embed into the Front

Append to the end of column 2 (Front for Basic, Text for Cloze):

```
<question text><br><img src="ibf-l12-p34-tms-mep-recording.jpg">
```

Leave the Back, Context, and Tags untouched. The `Image` field (column 5) stays empty — that field renders inside a collapsible "Remember Image" panel, which is not what we want for a figure that should be visible with the question.

### 6. Flip the HTML flag

Change the header to `#html:true`, otherwise Anki escapes the tag and the learner sees raw markup.

Before flipping, audit the file for characters that HTML would swallow:

```bash
grep -n '&' flashcards.tsv
grep -n '<' flashcards.tsv
```

Escape any bare `&` → `&amp;`, and any `<` that is not an intended tag (`<100ms` → `&lt;100ms`). Existing `<br>` inside Practice cards is fine and will now render as an actual line break.

### 7. Install the media into Anki

```bash
cp Flashcards/media/*.jpg ~/Library/Application\ Support/Anki2/<Profile>/collection.media/
```

Pick the **active** profile — if several exist, the one whose `collection.anki2` has the most recent mtime:

```bash
cd ~/Library/Application\ Support/Anki2
for p in */; do [ -f "$p/collection.anki2" ] && echo "$p $(stat -f '%Sm' "$p/collection.anki2")"; done
```

If images do not appear after import, run Tools → Check Media in Anki.

### 8. Verify the deck still parses

```bash
awk -F'\t' '!/^#/ && NF>0 {print NF, $1}' flashcards.tsv | sort | uniq -c   # all rows = 6
```

Then confirm every `img src` referenced in the TSV exists both in `Flashcards/media/` and in `collection.media/`.

---

## Output

```
[Lecture Folder]/Flashcards/
├── flashcards.tsv          ← #html:true, figures embedded in Fronts
└── media/
    ├── ibf-l12-p02-motor-imagery-beta-erd.jpg
    ├── ibf-l12-p05-closed-loop-diagram.jpg
    └── …
```

Report: number of cards, how many received a figure, the page→card mapping, and the list of slides deliberately skipped with reasons.

---

## What NOT to Do

- Never paste a whole slide page as the card image
- Never attach a figure whose visible text answers the card
- Never ship a crop you have not looked at
- Never write images into the `Image` field when the intent is a visible figure — use the Front
- Never flip `#html:true` without auditing for bare `&` and `<`
- Never copy media into an inactive Anki profile
- Never use generic filenames (`p12.jpg`) — `collection.media` is shared across every deck
