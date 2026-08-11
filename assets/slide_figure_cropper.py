import fitz, re
CITE = re.compile(r'(et al|\b(19|20)\d{2}\b|Journal|NeuroImage|Neuroscience|Nobel)', re.I)

def figure_bbox(page):
    pr = page.rect; parea = pr.get_area(); H = pr.height
    boxes = []
    for img in page.get_images(full=True):
        for r in page.get_image_rects(img[0]):
            if 0.004*parea < r.get_area() < 0.92*parea: boxes.append(r)
    for dr in page.get_drawings():
        r = dr["rect"]
        if 0.002*parea < r.get_area() < 0.92*parea: boxes.append(r)
    if not boxes: return None
    F = boxes[0]
    for b in boxes[1:]: F = F | b
    F = F & pr

    blocks = [b for b in page.get_text("blocks") if b[4].strip()]
    # 1) clip away title text sitting in the top band
    for x0, y0, x1, y1, txt, *_ in blocks:
        if y0 < 0.25*H and y1 > F.y0 - 5 and y1 < F.y0 + 0.14*F.height:
            F.y0 = max(F.y0, y1 + 3)
    # 2) clip away citation text in the bottom band
    for x0, y0, x1, y1, txt, *_ in blocks:
        if y1 > 0.84*H and CITE.search(txt) and y0 < F.y1 and y0 > F.y1 - 0.30*F.height:
            F.y1 = min(F.y1, y0 - 2)
    # 3) pull in annotation labels that hug the figure
    near = fitz.Rect(F.x0-30, F.y0-8, F.x1+30, F.y1+8)
    for x0, y0, x1, y1, txt, *_ in blocks:
        r = fitz.Rect(x0, y0, x1, y1)
        if y0 < 0.16*H or (y1 > 0.84*H and CITE.search(txt)): continue
        if r.intersects(near) and r.get_area() < 0.25*parea: F = F | r
    return (F & pr) if F.height > 40 and F.width > 40 else None

def crop(pdf, pno, dest, dpi=150, pad=6, quality=86):
    d = fitz.open(pdf); p = d[pno-1]; F = figure_bbox(p)
    if F is None: return None
    F = fitz.Rect(F.x0-pad, F.y0-pad, F.x1+pad, F.y1+pad) & p.rect
    pix = p.get_pixmap(dpi=dpi, clip=F)
    pix.pil_save(dest, format="JPEG", quality=quality, optimize=True)
    return dest
