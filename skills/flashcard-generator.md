---
name: flashcard-generator
description: Central flashcard generation rules for all courses. Defines the question-front / explanatory-back card architecture, card types (Cerebro Basic, Cerebro Cloze, Cerebro Type, Cerebro Type Code), 3-tier tagging, slide-figure embedding, TSV output format, and quality standards. All course-specific flashcard skills inherit from this file.
---

# Flashcard Generator — Central Rules

All course-specific flashcard skills inherit from this document. Course skills define **what** to extract (exam format, content scope, glossary rules). This file defines **how** to produce cards (structure, format, quality).

---

## Card Architecture (CRITICAL — read this first)

Every card is built from three moving parts. Getting these right matters more than any other rule here.

### 1. Front — a clear, self-contained question

The Front must tell the learner exactly what is being asked, without any other context. Someone who sees only the Front should know what kind of answer is expected.

**Required form:** a real question, ending in a question mark.

```
GOOD  What is the physiological mechanism behind Electrodermal Activity (EDA)?
GOOD  Which autonomic branch innervates electrodermal activity (EDA)?
GOOD  How does an SSVEP-based BCI determine which target the user is looking at?
GOOD  Why must a brain radiotracer be lipophilic?
```

**Never ship these:**

```
BAD   Stokes shift                                    ← bare topic label, asks nothing
BAD   Fluorescence mechanism                          ← bare topic label
BAD   Motor imagery EEG signature                     ← bare topic label
BAD   PET: positron emitters ↔ SPECT: gamma emitters  ← the answer IS the front
BAD   Radiotracer = carrier molecule + isotope        ← the answer IS the front
BAD   Electrophysiology Definitions: Current ↔ Potential
```

A statement-front is a broken card: there is nothing to retrieve, so the review teaches nothing. If the source material gives you a topic label, convert it: `Stokes shift` → `What is the Stokes shift and why does it matter?`

Two questions in one Front means two cards. Split them.

### 2. Back — compact but complete explanation

The Back states the answer **and** the mechanism or reason behind it, in readable prose. It is not a keyword fragment and not an essay.

- **Target: 1-2 sentences, roughly 20-35 words.** Hard ceiling ~40 words.
- Full sentences. The learner should be able to read it aloud and have it make sense.
- Answer first, then the "why" that makes it stick.
- Numeric substance (resolutions, latencies, half-lives, doses, percentages) belongs **in the Back** — it is part of the answer, not an extra.

```
GOOD  Inverse: alpha acts as an inhibitory gate. High alpha goes with low BOLD, low
      spiking, and small MEPs; suppressing alpha releases the cortex into an excitable state.

GOOD  Because the Na+ channels just behind the traveling spike are temporarily inactivated —
      the refractory period. The depolarization can therefore only regenerate forward.
```

**Two failure modes, avoid both:**

```
BAD (too dry)   Alpha ↓ → excitability ↑ · gate · BOLD ↓
                Telegraphic fragments teach nothing. Banned.

BAD (too long)  Alpha power and cortical excitability are inversely related. This is because
                alpha functions as an inhibitory gate for sensory information. When alpha is
                high, the BOLD signal is low, spiking is reduced, and MEPs are small. When
                alpha drops, the cortex is released from inhibition and becomes more excitable,
                which is why gamma activity increases...
                Three-plus sentences of restatement. Squeeze it.
```

Cut anything that merely repeats the Front, hedges ("it can be said that"), or announces itself ("This demonstrates that…").

### 3. Context — usually empty

Context is a collapsible panel, not a second answer. Leave it **empty** unless there is genuine extra material that does not belong in a tight Back:

- a formula (`E_ion = (RT/zF) * ln([ion]ext/[ion]int)`)
- a set of reference values that would bloat the Back
- a caveat, exception, or a second worked example

If you find yourself moving half the explanation into Context to keep the Back short, the split is wrong — tighten the Back instead.

### Quality test for every card

> Reading only the Front, do I know what is being asked and could I produce one correct answer?
> Reading only the Back, do I understand *why* the answer is true?

If the first fails, the Front is a label or too vague. If the second fails, the Back is a fragment.

---

## Slide Figures on the Front

When the lecture ships a PDF or slide deck, cards should carry the figure the lecturer actually showed. A cropped diagram, micrograph, waveform, scan, or formula does more for recall than another sentence of prose.

**Rules:**

- Embed the figure **directly in the Front field**, appended after the question: `<question><br><img src="filename.jpg">`
- Crop to the **figure region only** — never paste the whole slide. Titles, bullet lists, and citation lines must be excluded.
- Skip slides whose visible text spells out the answer; they turn the card into a freebie.
- Skip pure bullet-text slides. A slide with no figure adds nothing.
- One image per card. A figure may serve two cards.
- Naming: `<course>-l<lecture>-p<page>-<slug>.jpg`, e.g. `ibf-l12-p34-tms-mep-recording.jpg`
- Images live in `[Lecture Folder]/Flashcards/media/` and must be copied into Anki's `collection.media/` before import.
- The TSV header must be `#html:true` for `<img>` to render. Before flipping it, escape any bare `&` → `&amp;` and any `<` that is not an intended tag → `&lt;`.

The extraction and cropping procedure lives in [slide-figure-extractor.md](slide-figure-extractor.md). Use it — do not hand-roll page rendering.

---

## Card Types

### 1. Cerebro Basic — Question / Answer

**When:** Definitions, arguments, mechanisms, comparisons, "why/how" questions. Roughly 70% of cards.

| Column | Field | Content |
|--------|-------|---------|
| 1 | Notetype | `Cerebro Basic` |
| 2 | Front | Clear, single-point question (plus optional `<br><img …>`) |
| 3 | Back | Compact explanatory answer, 1-2 sentences |
| 4 | Context | Extra material only — usually empty |
| 5 | Image | Leave empty (figures go on the Front) |
| 6 | Tags | 3-tier tags, space-separated |

### 2. Cerebro Cloze — Fill-in-the-blank

**When:** Name-date pairings, specific terms, formulas, paired concepts (A ↔ B). Roughly 10% of cards.

| Column | Field | Content |
|--------|-------|---------|
| 1 | Notetype | `Cerebro Cloze` |
| 2 | Text | Sentence with `{{c1::blank}}` syntax (plus optional `<br><img …>`) |
| 3 | Context | Compact explanation of the fact — 1-2 sentences |
| 4 | Image | Leave empty |
| 5 | — | Empty padding so Tags lands in column 6 |
| 6 | Tags | 3-tier tags, space-separated |

**Cloze rules:**
- Prefer a single deletion per card
- Each gap: 2-4 words — a hook, not a sentence
- Enough surrounding context that only one answer is possible
- Cloze Context should explain *why*, not restate the sentence

```
GOOD  Kanwisher ({{c1::1997}}) identified FFA as a face processing module
BAD   {{c1::Kanwisher}} identified FFA        ← many researchers study FFA
```

### 3. Cloze Overview — List / Argument Group

**When:** Any list, argument group, reason set, or property set with 3+ items.

Produce the overview card **first**, then individual Basic cards for each item. The overview gives the big picture; the Basic cards drill the details.

```
Cerebro Cloze	[Topic]: {{c1::item1}} · {{c2::item2}} · {{c3::item3}}	[Context]	[Image]		[Tags]
```

Max 6 gaps per overview. If 7+ items, split into two cards.

### 4. Cerebro Type — Type Your Answer

**When:** Terms that must be reproduced precisely. Roughly 10% of cards.

Columns: `Notetype, Front, Back, Context, Code, Image, Tags`

The Back is the exact string the student types — keep it short and do not pad it with explanation. Put the explanation in Context for these cards only.

### 5. Cerebro Type Code — Type Code Answer

**When:** Programming content. R functions, syntax, operators, short snippets. Dominant in code-heavy courses.

Columns: `Notetype, Front, Back, Context, Code, Image, Tags`

- Never ask "what function does X?" in isolation — embed a concrete scenario
- Back must be the exact string the student types
- HTML allowed in Front: `<code>`, `<b>`, `<div>`

---

## 3-Tier Tagging System

Every card gets three tags, space-separated in one column.

**Tier 1 — Domain/theme**, shared across all courses so a filter shows the concept from every lecture:
```
philosophy-of-mind  language     memory       visual-cognition   attention
consciousness       methodology  statistics   electrophysiology  emotion
perception          motor-control            computational-modeling
```

**Tier 2 — Week:** `Week-1`, `Week-2`, … The deck hierarchy already encodes the course.

**Tier 3 — Specific concept:** `dualism`, `prosopagnosia`, `t-test`, `patch-clamp`, `ssvep`.

```
electrophysiology Week-2 patch-clamp
bci-neurofeedback Week-12 hebbian
```

---

## TSV Output Format

### Header

```
#separator:tab
#html:true
#notetype column:1
#tags column:6
```

Use `#html:true` whenever any field contains `<img>` or `<br>`; otherwise `#html:false` is acceptable. **Do not include a deck column** — the user selects the target deck at import time.

### Row structures

```
Cerebro Basic	[Front]	[Back]	[Context]	[Image]	[Tags]
Cerebro Cloze	[Text]	[Context]	[Image]		[Tags]
Cerebro Type	[Front]	[Back]	[Context]	[Code]	[Image]	[Tags]
Cerebro Type Code	[Front]	[Back]	[Context]	[Code]	[Image]	[Tags]
```

Every Basic and Cloze row must end up with **exactly 6 tab-separated columns** — pad Cloze rows with an empty column so Tags always lands in column 6, matching the header.

### Safety

- Replace literal tabs inside fields with spaces
- One line per card, no raw multiline fields, no blank rows
- Empty fields are consecutive tabs
- Verify before shipping:
  ```bash
  awk -F'\t' '!/^#/ && NF>0 {print NF, $1}' flashcards.tsv | sort | uniq -c
  ```

---

## Output Location

```
[Lecture Folder]/
└── Flashcards/
    ├── flashcards.tsv                  ← always this name
    ├── flashcards_supplementary.tsv    ← only if the coverage checker finds gaps
    ├── media/                          ← cropped slide figures
    ├── before_starting_report.md
    └── flashcard_mindmap.html
```

---

## Content Selection

**Always include:** every named concept, term, syndrome, model, principle, or method; every mechanism or causal chain; every explicit comparison; key empirical findings with theoretical weight; clinical cases that demonstrate a point; arguments for and against major positions.

**Always exclude:** administrative content and logistics; biographical trivia; numbers with no conceptual role; anything with no exam relevance; content already covered by another card in the deck.

---

## Production Workflow

1. **Read all material** — full transcript, all slides, reading PDF
2. **Inventory topics** — every distinct testable unit
3. **Identify lists** — 3+ items → Cloze Overview plus one Basic per item
4. **Draft Fronts as questions** — never as labels; re-read the banned list above
5. **Write compact Backs** — answer + why, 1-2 sentences, numbers included
6. **Leave Context empty** unless there is real extra material
7. **Extract and attach slide figures** — see slide-figure-extractor.md
8. **Apply 3-tier tags**
9. **Write the TSV** and run the column check
10. **Report counts** — `Cerebro Basic: X, Cerebro Cloze: Y, Total: T`

### Card type decision table

| Content pattern | Card type |
|-----------------|-----------|
| 3+ item list, argument group, property set | **Cloze Overview**, then Basic per item |
| "What / why / how?" question | **Cerebro Basic** |
| Name-date pairing, specific term, formula | **Cerebro Cloze** |
| Term requiring typed recall | **Cerebro Type** |
| Code syntax, function, operator | **Cerebro Type Code** |

---

## Revising an Existing Deck

When reformatting a deck that already exists in the user's Anki collection, Front text is the identity key Anki matches on:

- **Back/Context changes only** → import with "Existing notes: Update"; scheduling is preserved.
- **Front changes** → Anki treats the card as a new note. The old copy remains, so after import run Browse → Notes → Find Duplicates on the Front field and delete the stale versions. Warn the user before doing this at scale.
- Always keep Cloze `Text` fields byte-identical unless you intend to reset them.
- Back up the previous TSV before overwriting.

---

## Deduplication

Before finalizing, scan all cards and merge any that test the same concept from the same angle. Two cards are redundant if knowing one makes the other trivial. Keep the question that best captures the testable distinction.

Across a multi-turn conversation, track what you already emitted; at least 80% of new output must be novel.

---

## What NOT to Do

- Never ship a Front that is a topic label, a statement, or that contains its own answer
- Never write a Back as telegraphic fragments (`A → B · C`)
- Never write a Back longer than ~40 words outside Practice cards
- Never split an explanation across Back and Context to game the length rule
- Never paste a whole slide as the card image — crop to the figure
- Never attach a figure whose text gives away the answer
- Never put more than one idea in a single card
- Never use Cloze for content that does not require memorizing a specific term
- Never reference other cards ("as discussed previously")
- Never skip the Cloze Overview when a list of 3+ items is present
- Never hardcode deck names in the TSV

---

## Inheritance Model

Course-specific skills live in `skills/flashcard-generators/` and are discovered dynamically by reading each file's frontmatter. Each course skill adds only:

- **Exam format** — what the exam looks like, how cards map to it
- **Content scope** — course-specific include/exclude rules
- **Input types** — PDF, RMD, transcript, etc.
- **Course-specific card rules** — glossary extraction, MCQ generation, practice questions

Course skills must **not** redefine card types, the TSV format, the tagging system, the card architecture, or the figure rules. Those are defined here and inherited.
