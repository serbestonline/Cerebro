---
name: flashcard-generator
description: Central flashcard generation rules for all courses. Defines card types (Cerebro Basic, Cerebro Cloze, Cerebro Type, Cerebro Type Code), Minimum Information Principle enforcement, 3-tier tagging, TSV output format, and quality standards. All course-specific flashcard skills inherit from this file.
---

# Flashcard Generator — Central Rules

All course-specific flashcard skills inherit from this document. Course skills define **what** to extract (exam format, content scope, glossary rules). This file defines **how** to produce cards (structure, format, quality).

---

## Card Types

### 1. Cerebro Basic — Question / Answer

**When:** Definitions, arguments, mechanisms, comparisons, "why/how" questions.
Approximately 70% of cards.

**Fields:**

| Column | Field | Content |
|--------|-------|---------|
| 1 | Notetype | `Cerebro Basic` |
| 2 | Front | Clear, single-point question |
| 3 | Back | Minimal answer — max 10-15 words |
| 4 | Context | Original extended explanation (collapsible) |
| 5 | Image | Leave empty unless visual reference exists |
| 6 | Tags | 3-tier tags, space-separated |

**Back field rules:**
- Max 10-15 words
- Concept fragments, not full sentences: `A → B · C · D`
- Formulas, names, regions — concrete, not abstract
- One idea only. "A and B" → two separate cards.

**Avoid in Back:**
- "This demonstrates that..." style explanations
- Long parenthetical definitions
- Multiple thoughts in one back

**Context field rules:**
- The original, uncut explanation goes here
- Provides study depth without polluting the Back
- Always populated for non-trivial cards

---

### 2. Cerebro Cloze — Fill-in-the-blank

**When:** Name-date pairings, specific terms, formulas, paired concepts (A ↔ B).
Approximately 10% of cards.

**Fields:**

| Column | Field | Content |
|--------|-------|---------|
| 1 | Notetype | `Cerebro Cloze` |
| 2 | Text | Sentence with `{{c1::blank}}` syntax |
| 3 | Context | Extended explanation (collapsible) |
| 4 | Image | Leave empty unless visual reference exists |
| 5 | Tags | 3-tier tags, space-separated |

**Cloze rules:**
- Prefer single deletion per card
- Multiple deletions only for directly related concepts
- Each gap: max 2-4 words — a hook, not a sentence
- Sufficient context around the gap so only one correct answer is possible

**Good cloze examples:**
- `Kanwisher ({{c1::1997}}) identified FFA as a face processing module`
- `Lashley's two principles: {{c1::mass action}} and {{c1::equipotentiality}}`

**Bad cloze:**
- `{{c1::Kanwisher}} identified FFA` — not enough context, many researchers study FFA

---

### 3. Cloze Overview — List / Argument Group (MANDATORY RULE)

**When:** Any list, argument group, reason set, type list, step sequence, or property set with 3 or more items.
Approximately 5% of cards.

**RULE:** When such content is found, FIRST produce a Cloze Overview card, THEN produce individual Cerebro Basic cards for each item. Both work together — the overview provides the big picture, the basic cards drill the details.

**Format:**
```
Cerebro Cloze	[Topic]: {{c1::item1}} · {{c2::item2}} · {{c3::item3}}	[Context]	[Image]	[Tags]
```

**Production order for list content:**
1. Cloze Overview card (big picture)
2. Cerebro Basic cards (one per item)
3. Regular Cloze cards (name/date pairings)

**Splitting rule:** Max 6 gaps per overview. If 7+ items, split into two overview cards: "X properties (1-4)" + "X properties (5-7)".

---

### 4. Cerebro Type — Type Your Answer

**When:** Concepts requiring active recall through typing. Definitions that must be reproduced precisely, key terms the student must be able to spell and define.
Approximately 10% of cards.

**Fields:**

| Column | Field | Content |
|--------|-------|---------|
| 1 | Notetype | `Cerebro Type` |
| 2 | Front | Question prompt |
| 3 | Back | Exact answer the student types |
| 4 | Context | Extended explanation (collapsible) |
| 5 | Code | Leave empty (no code context) |
| 6 | Image | Leave empty unless visual reference exists |
| 7 | Tags | 3-tier tags, space-separated |

---

### 5. Cerebro Type Code — Type Code Answer

**When:** Programming and code-based content. R functions, syntax, operators, short code snippets.
Used primarily by r-programming-flashcards. Approximately 70-85% of cards in code-heavy courses.

**Fields:**

| Column | Field | Content |
|--------|-------|---------|
| 1 | Notetype | `Cerebro Type Code` |
| 2 | Front | Question with concrete scenario |
| 3 | Back | Exact code the student types |
| 4 | Context | Mechanism explanation |
| 5 | Code | Reference code snippet if needed |
| 6 | Image | Leave empty |
| 7 | Tags | 3-tier tags, space-separated |

**Rules:**
- Never ask "what function does X?" in isolation — always embed in a concrete scenario
- Back must be the exact string the student types
- HTML allowed in Front: `<code>`, `<b>`, `<div>` only

---

## Minimum Information Principle (CRITICAL)

This is the single most important rule. Every card must test exactly **one** piece of knowledge.

### Core Rules

1. **One card = one idea.** "What are A and B?" → two separate cards.
2. **Back is minimal.** Max 10-15 words. The Context field holds the full explanation.
3. **Lists become Cloze Overview + individual Basic cards.** Never put a list in a single Basic card's Back.
4. **Answers are hooks, not essays.** `Neural causation · Penfield · Cross-species · AI` — not full sentences explaining each.
5. **If you can't answer without seeing the Back, the Front is too broad.** Split it.

### Quality Test

For every card, ask:
> "Reading only the Front, could I produce exactly one correct answer?"

- **No** → Front is too vague. Narrow it.
- **Yes but Back is 3+ lines** → Back is too heavy. Move detail to Context, keep Back minimal.

### Enumeration Pattern (for lists)

When a concept has N components:

```
Card 0 (anchor):  "How many defining properties does a Fodorian module have?" → 7
Card 1:           "Modularity property: module processes only one input type = ?" → Domain-specificity
Card 2:           "Modularity property: processing cannot be influenced by other systems = ?" → Encapsulation
...
Card N:           [one per item]
Overview:         Cloze Overview card with all N items as gaps
```

---

## 3-Tier Tagging System

Every card receives tags from three tiers, space-separated in the Tags column.

### Tier 1 — Domain / Theme

Broad conceptual domains. Kept moderately flexible — not too strict (fragments usefulness) and not too loose (loses cross-lecture visibility).

Examples:
```
philosophy-of-mind    language           memory
visual-cognition      spatial-cognition  attention
consciousness         methodology        neural-plasticity
statistics            computational-modeling
emotion               perception         motor-control
```

These are shared across all courses. When filtering by a Tier 1 tag, you see that concept from every course and every lecture.

### Tier 2 — Week

Which lecture week the card comes from:
```
Week-1   Week-2   Week-3   Week-4   Week-5
Week-6   Week-7   Week-8   ...
```

The deck hierarchy already identifies the course, so the tag only needs the week number.

### Tier 3 — Specific Concept

The precise concept tested:
```
dualism              materialism         modularity
broca-aphasia        prosopagnosia       anterograde-amnesia
equipotentiality     double-dissociation encapsulation
t-test               p-value             linear-regression
```

### Tag Format in TSV

Tags are space-separated in a single column:
```
philosophy-of-mind Week-1 dualism
memory Week-4 anterograde-amnesia
statistics Week-3 t-test
```

---

## Back Minimization Templates

Regardless of how long the source text is, the Back field is reduced to one of these templates:

**Definition cards:**
```
[Core concept] = [essence] → [critical consequence]
```
Example: `Dualism = mind + body separate substances → interaction problem`

**Argument cards (individual, after Cloze Overview):**
```
[Hook phrase] → [mechanism/evidence]
```
Example: `Penfield experiment → brain stimulation arrested speech → mind is physical`

**Comparison cards:**
```
[A]: [essence] ↔ [B]: [essence]
```
Example: `Kanwisher: FFA = dedicated module ↔ Haxby: distributed network`

**Mechanism cards:**
```
[Start] → [mechanism] → [outcome]
```
Example: `Wernicke ↔ Broca disconnected → repetition impaired, comprehension intact`

---

## TSV Output Format

### Header (always present)

```
#separator:tab
#html:false
#notetype column:1
#tags column:6
```

**Do NOT include a deck column.** The user selects the target deck during Anki import. Hardcoding deck names in the TSV creates inflexibility.

Adjust `#tags column` based on card type — it must point to the actual last column containing tags.

### Row Structures

**Cerebro Basic:**
```
Cerebro Basic	[Front]	[Back]	[Context]	[Image]	[Tags]
```

**Cerebro Cloze:**
```
Cerebro Cloze	[Text with {{c1::gaps}}]	[Context]	[Image]	[Tags]
```

**Cerebro Type:**
```
Cerebro Type	[Front]	[Back]	[Context]	[Code]	[Image]	[Tags]
```

**Cerebro Type Code:**
```
Cerebro Type Code	[Front]	[Back]	[Context]	[Code]	[Image]	[Tags]
```

### TSV Safety

- Replace literal tab characters inside fields with spaces
- No raw multiline fields — keep each card on a single line
- Empty fields are represented by consecutive tabs
- Image column is typically empty (left blank)

---

## Output Location

All flashcard output goes to a `Flashcards/` subdirectory inside the lecture folder:

```
[Lecture Folder]/
└── Flashcards/
    ├── flashcards.tsv
    ├── flashcards_supplementary.tsv    (if coverage checker finds gaps)
    ├── before_starting_report.md       (from lecture-summary skill)
    └── flashcard_mindmap.html          (from mindmap-generator skill)
```

**File name is always `flashcards.tsv`** — the lecture folder name provides the date and week context.

---

## Content Selection

### Always Include

- Every named concept, term, syndrome, disorder, model, principle, method
- Every mechanism, process, or causal chain
- Every explicitly drawn comparison or contrast
- Key empirical findings with theoretical significance
- Clinical cases that demonstrate a theoretical point
- Arguments for and against major positions

### Always Exclude

- Administrative content (logistics, scheduling, jokes)
- Purely biographical details unless theoretically relevant
- Numerical values unless conceptually essential
- Content with no exam relevance
- Duplicate information already covered in the same deck

---

## Card Production Workflow

For each lecture's material:

1. **Read all material** — full transcript, all slides, reading PDF if available
2. **Identify lists** — any group of 3+ items → mark for Cloze Overview treatment
3. **Decide card type** — use the decision table below
4. **Produce in order** — Cloze Overview → Cerebro Basic → Cerebro Cloze → Cerebro Type
5. **Minimize backs** — apply back minimization templates
6. **Move detail to Context** — long explanations go to Context, never to Back
7. **Apply tags** — Tier 1 + Tier 2 + Tier 3 for every card
8. **Write TSV** — with correct header
9. **Report card count** — `Cerebro Basic: X, Cerebro Cloze: Y, Cerebro Type: Z, Total: T`

### Card Type Decision Table

| Content Pattern | Card Type |
|----------------|-----------|
| 3+ item list, argument group, property set | **Cloze Overview** (then Basic per item) |
| "What/why/how?" question | **Cerebro Basic** |
| Name-date pairing, specific term, formula | **Cerebro Cloze** |
| Concept requiring typed recall | **Cerebro Type** |
| Code syntax, function, operator | **Cerebro Type Code** |
| Complex mechanism needing extended context | **Cerebro Basic** (with Context populated) |

---

## Cross-Card Deduplication

### Within a Single Deck

Before finalizing output, scan all cards and merge any that test the same concept from the same angle. Two cards are redundant if knowing the answer to one makes the other trivially answerable.

When merging: keep the question that best captures the testable distinction. A single well-scoped card is always better than two overlapping ones.

### Across Conversation

If generating cards across multiple exchanges in one conversation, maintain an internal memory of previously generated cards. Flag duplicates before emitting. Novelty threshold: at least 80% of emitted cards must be novel versus prior output in the same conversation.

---

## What NOT to Do

- Never put more than one idea in a single card's Back
- Never use Cloze for content that doesn't require memorizing a specific term
- Never use more than `{{c1::}}` gap type in regular Cloze — use `{{c1::}}` for all gaps. Cloze Overview is the exception (uses c1, c2, c3...).
- Never reference other cards ("as discussed in the previous card")
- Never generate cards for trivial, non-exam-relevant content
- Never produce a Back longer than 2 lines without moving the excess to Context
- Never skip the Cloze Overview when a list of 3+ items is present
- Never hardcode deck names — use the deck name provided by the course-specific skill

---

## Inheritance Model

## Inheritance Model

Course-specific flashcard skills live in `skills/flashcard-generators/`. The agent discovers them dynamically by scanning that directory and reading each skill's frontmatter (`name`, `description`) to identify which course it serves.

Each course skill extends this file by adding:

- **Exam format** — what the exam looks like, how cards should map to it
- **Content scope** — what to include/exclude for that specific course
- **Input types** — what materials the course provides (PDF, RMD, transcript, etc.)
- **Course-specific card rules** — glossary extraction, MCQ generation, practice questions, etc.

Course skills must NOT redefine card types, TSV format, tagging system, MIP rules, or back minimization templates. Those are defined here and inherited.

To add a new course: create a new `.md` file in `skills/flashcard-generators/` with `inherits: ../flashcard-generator.md` in the frontmatter and define only the course-specific rules above.
