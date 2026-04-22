---
name: mindmap-generator
description: Generate an interactive dark-mode Markmap HTML mindmap where EVERY flashcard is visible as a Front → Back node pair, and EVERY category node shows a rich CONTEXT tooltip on hover explaining how the flashcards beneath connect. Use after flashcards have been generated for a lecture.
---

# Mindmap Generator

**Reference implementation:** `assets/mindmap_reference.html` — open this file in a browser BEFORE generating. It is the gold standard. Your output must match its structure, styling, and interactivity exactly.

---

## What This Produces

A self-contained `.html` file that opens in any browser with:

1. **Every single flashcard** visible as two connected nodes: Front (question) → Back (answer)
2. **Every category node** (theme, subtopic) shows a green `CONTEXT` tooltip on hover — the narrative glue that explains WHY these flashcards are grouped and HOW they relate
3. **Dark mode** styling — `#0d1117` background, light text, no white flash
4. **Interactive** — zoom, pan, click to expand/collapse branches
5. **Color-coded branches** — each major theme gets a distinct color

---

## Node Hierarchy (CRITICAL)

```
# Lecture Title                           ← root (h1)
## Theme                                  ← category node with CONTEXT tooltip (h2)
### Subtopic                              ← category node with CONTEXT tooltip (h3)
#### [SB] What is dualism?                ← flashcard FRONT (h4)
- Mind and body are separate substances   ← flashcard BACK (leaf, bullet)
```

### Rules

- **h1** = Lecture title (root node)
- **h2** = Major theme (e.g., "Philosophy of Mind", "Modularity — Fodor", "Methods")
- **h3** = Subtopic within a theme (e.g., "Dualism", "Core Properties", "Dissociations")
- **h4** = Flashcard **Front** — always prefixed with card type label
- **bullet (-)** = Flashcard **Back** — always a direct child of h4, always a leaf

### Card Type Labels

- `[SB]` = Cerebro Basic
- `[SC]` = Cerebro Cloze
- `[ST]` = Cerebro Type
- `[STC]` = Cerebro Type Code

### Every Flashcard Must Appear

Do NOT summarize or skip cards. If `flashcards.tsv` has 45 cards, the mindmap has 45 Front→Back pairs. No exceptions.

---

## Context Tooltip System (CRITICAL)

Every node that is NOT a flashcard (not starting with `[SB]`, `[SC]`, `[ST]`, `[STC]`) MUST have a context entry in the JavaScript `contexts` object.

### What Context Is

Context is NOT a summary of the flashcards below. Context is the **narrative glue** — it explains:
- **Why** these flashcards are grouped together
- **How** they relate to each other
- **What story** they tell when read as a sequence
- **Why this matters** for the broader lecture

### Context Quality Standard

**Bad context:** "This section covers dualism and its key concepts."
**Good context:** "Descartes proposed mind and body are separate substances. This raises the core question: if they are different kinds of stuff, how do they interact? This unsolved interaction problem motivates the shift to materialism."

Each context: 2-4 sentences. Written as if explaining to a student why they should care about this cluster of cards.

### Context for EVERY Level

- The **root node** (h1) gets context explaining what the entire lecture is about and why it matters
- Each **theme** (h2) gets context explaining the theme's role in the lecture
- Each **subtopic** (h3) gets context explaining how the cards beneath connect

No category node may exist without a context entry.

---

## Markmap Configuration

```yaml
markmap:
  colorFreezeLevel: 3
  maxWidth: 420
  initialExpandLevel: 2
```

- `initialExpandLevel: 2` — on load, themes (h2) and subtopics (h3) are visible, but individual flashcards (h4 + bullets) are collapsed. Student clicks to reveal.
- `colorFreezeLevel: 3` — each theme branch keeps a consistent color
- `maxWidth: 420` — prevents text from stretching too wide

---

## HTML Template

The output file has exactly three parts. Follow the reference implementation (`assets/mindmap_reference.html`) for exact code.

### Part 1: Head — Dark Mode CSS + Tooltip Styles

```css
body { background: #0d1117; }
svg.markmap { width: 100%; height: 100vh; background: #0d1117; }

#tooltip {
  background: #161b22;
  border: 1px solid #30363d;
  color: #e6edf3;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
  /* green CONTEXT badge */
}
.tt-label { background: #23883833; color: #3fb950; }
.tt-title { color: #f0f6fc; border-bottom: 1px solid #21262d; }
.tt-body { color: #9da5b0; }
```

### Part 2: Body — Markmap Template

The `<div class="markmap"><script type="text/template">` block containing the indented markdown with:
- h1 root
- h2 themes
- h3 subtopics
- h4 flashcard fronts with `[SB]`/`[SC]` prefix
- bullet flashcard backs

### Part 3: Script — Context Tooltip JavaScript

```javascript
const contexts = {
  "Theme Name": "Context description...",
  "Subtopic Name": "Context description...",
  // ... one entry per non-flashcard node
};
```

Plus the tooltip show/hide/position functions and the MutationObserver that:
1. Waits for markmap to render
2. Finds all foreignObject elements in the SVG
3. Skips nodes starting with `[SB]`, `[SC]`, `[ST]`, `[STC]`
4. Attaches mouseenter/mouseleave listeners to category nodes
5. Keeps observing for re-renders (expand/collapse triggers re-render)

---

## Input

- **Required:** `flashcards.tsv` (and `flashcards_supplementary.tsv` if exists)
- **Required:** Source material (transcript, slides) for writing context descriptions
- **Optional:** `lecture_summary.md` for concept relationships

---

## Output

**File:** `flashcard_mindmap.html`
**Location:** `[Lecture Folder]/Flashcards/flashcard_mindmap.html`

---

## Workflow

1. Read `flashcards.tsv` — extract every card's Front, Back, card type, and tags
2. Group cards by Tier 1 tag → these become h2 theme branches
3. Within each theme, cluster by related Tier 3 tags or conceptual proximity → these become h3 subtopics
4. For each card: create h4 (Front with label) and bullet (Back)
5. Read source material (transcript, slides, lecture_summary.md)
6. Write context descriptions for EVERY h1, h2, and h3 node
7. Build the HTML: CSS + markmap template + JavaScript contexts object + tooltip system
8. Save to `Flashcards/flashcard_mindmap.html`

### Grouping Rules

- A subtopic should contain 2-8 flashcards. More than 8 → split into sub-subtopics.
- Fewer than 2 → merge with a neighboring subtopic.
- Group by conceptual relationship, NEVER alphabetically.
- The grouping should tell a story — the student should be able to read top-to-bottom and understand the lecture's logical flow.

---

## What NOT to Do

- **Never omit a flashcard** — if it's in the TSV, it's in the mindmap
- **Never omit context** for any category node — every non-flashcard node needs a tooltip
- **Never put Back text in the Front node** — they are separate hierarchy levels
- **Never use emoji labels** — always `[SB]`, `[SC]`, `[ST]`, `[STC]`
- **Never produce a flat list** — the hierarchy must have themes and subtopics
- **Never skip the JavaScript tooltip system** — it's what makes the mindmap interactive and useful
- **Never use light mode** — always dark mode (`#0d1117`)
- **Never deviate from the reference implementation's structure** — read `assets/mindmap_reference.html` first
