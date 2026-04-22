---
name: lecture-summary
description: Generate a comprehensive lecture summary and a before-starting report from lecture materials (transcript, slides, reading PDF). Use when a new lecture has been processed and the student needs an overview before studying flashcards. Produces two files — lecture_summary.md in the lecture folder and before_starting_report.md in the Flashcards/ subfolder.
---

# Lecture Summary Generator

Produces two outputs from lecture materials:
1. **`lecture_summary.md`** — comprehensive lecture overview for general study
2. **`before_starting_report.md`** — flashcard-oriented preview placed in the Flashcards/ directory

---

## Input

Any combination of:
- Lecture transcript (.txt)
- Lecture slides (PDF)
- Reading PDF (if available)
- Previously generated flashcards.tsv (for before-starting report)

---

## Output 1: lecture_summary.md

Placed in the lecture folder root (not in Flashcards/).

### Structure

```markdown
# Lecture [N] — [Topic Title]

## Overview
[2-3 paragraphs summarizing the lecture's main argument and flow. Not a list of topics — a narrative that explains what the lecture is about and why it matters.]

## Key Themes
1. **[Theme 1]** — [1-sentence description]
2. **[Theme 2]** — [1-sentence description]
3. **[Theme 3]** — [1-sentence description]

## Core Concepts
[For each major concept, a structured entry:]

### [Concept Name]
- **Definition:** [1-2 sentences]
- **Why it matters:** [1 sentence connecting to the broader lecture narrative]
- **Key details:** [2-3 bullet points with the essential facts]

[Repeat for each concept]

## Connections to Previous Lectures
- **Lecture [X] ([Topic]):** [How this lecture builds on or contrasts with earlier material]
- [Repeat for each relevant connection]

## Clinical / Practical Applications
[If applicable — real-world relevance of the lecture content]

## Glossary Terms
[If the course has a glossary — list all terms from this lecture]
- Term 1, Term 2, Term 3, ...

## Open Questions
[Any unresolved debates, controversies, or topics the lecturer flagged as ongoing research]
```

### Writing Style
- Clear, direct academic prose
- No filler or padding
- Explain relationships between concepts, not just list them
- Write as if the reader has attended the lecture but needs a structured reference

---

## Output 2: before_starting_report.md

Placed in `[Lecture Folder]/Flashcards/before_starting_report.md`.

**Generated LAST in the pipeline** — after flashcards, supplementary cards, and mindmap all exist. This is the most comprehensive document in the system. It is the student's study guide.

### Required Inputs (all must exist before generating)

- `lecture_summary.md` — for lecture narrative and concept relationships
- `flashcards.tsv` — for card statistics, tags, and content analysis
- `flashcards_supplementary.tsv` — for gap analysis results (if exists)
- `flashcard_mindmap.html` — for concept grouping structure
- Course-specific flashcard skill — for exam format and previous year questions
- Source materials (transcript, slides) — for depth and accuracy

### Structure

```markdown
# Before Starting — Lecture [N] Flashcards

## Lecture Narrative
[A 3-4 paragraph narrative that tells the STORY of this lecture. Not a bullet list — a flowing explanation of what the lecturer argued, why they argued it, and how the pieces fit together. Written as if you're explaining to a friend what the lecture was about over coffee. This is the most important section — it provides the mental framework that makes individual flashcards meaningful.]

## Concept Architecture
[A visual/structured representation of how concepts relate to each other. Use arrows, indentation, or a structured hierarchy. Show causation, dependency, and contrast.]

Example:
```
FOUNDATION: What is the mind?
├── Dualism (Descartes) → mind ≠ body → PROBLEM: interaction
│   └── Failed: no mechanism for non-physical → physical causation
├── Materialism → mind = brain → SOLUTION: enables scientific study
│   ├── Evidence: neural causation (Penfield)
│   ├── Evidence: cross-species similarity
│   ├── Evidence: AI replication
│   └── Consequence: cognitive neuropsychology becomes possible
│
HOW TO STUDY THE MIND:
├── Failed approaches
│   ├── Psychometrics → measures abilities, ignores architecture
│   ├── Behaviorism → rejects internal states entirely
│   └── Lashley → wrong conclusions (mass action, equipotentiality)
├── Successful framework: Modularity (Fodor)
│   ├── 7 properties (domain-specific, encapsulated, ...)
│   ├── Prediction: selective deficits after brain damage
│   └── Challenge: neural reuse (not strictly modular)
│
HOW TO TEST IT:
├── Dissociations → single (weak) vs double (strong)
├── Assumptions → universality (all brains same architecture)
└── Neuroimaging → correlation ≠ causation
```

## What You Will Learn (Card Inventory)
[For each major topic cluster in the flashcard set, describe what the cards cover and how many there are. Reference the mindmap's grouping structure.]

| Topic Cluster | Cards | Key Concepts |
|---------------|-------|-------------|
| Philosophy of Mind | [N] | dualism, materialism, interaction problem, Penfield |
| Historical Approaches | [N] | psychometrics, behaviorism, Lashley, equipotentiality |
| Modularity | [N] | 7 properties, domain-specificity, encapsulation, neural reuse |
| Methods | [N] | dissociation, double dissociation, universality, fMRI limitations |

**Total: [N] cards** (Cerebro Basic: [N], Cerebro Cloze: [N], Cerebro Type: [N])
**Supplementary cards: [N]** (gaps filled by coverage checker)

## Exam Relevance Analysis

### How This Lecture Maps to the Exam
[Read the course-specific flashcard skill's exam format section. Explain specifically how this lecture's content could appear on the exam.]

### High-Probability Definition Questions
[For each likely term, explain WHY it's likely — not just that it exists.]

| Term | Why Likely | Confidence |
|------|-----------|------------|
| [Term] | In glossary + heavily emphasized + tested similar concept last year (Q3) | High |
| [Term] | In glossary, core definition for the course framework | High |
| [Term] | Not in glossary but lecturer spent 10 minutes explaining it, used the word "important" | Medium |

### High-Probability Essay Topics
[For each likely essay topic, explain the question pattern it fits and what the student would need to cover.]

| Topic | Likely Question Pattern | What You'd Need |
|-------|------------------------|-----------------|
| [Topic] | "What is X? Give 3 examples" (matches Q6 style) | Definition + 3 distinct examples with mechanisms |
| [Topic] | "Describe differences between X and Y" (matches Q7 style) | Side-by-side comparison + neurological basis |

### Cross-Lecture Essay Potential
[Identify concepts from THIS lecture that connect to OTHER lectures and could form a cross-lecture essay question.]

- [Concept] appears in Week [X] (as [context]) and Week [Y] (as [context]) — strong candidate for "compare approaches across domains" essay

### Previous Year Question Mapping
[If previous year questions are available in the course skill, map which ones this lecture's content could answer.]

- **Q[N]** from last year: This lecture provides [what exactly] for answering this question
- This lecture alone could NOT answer Q[N] — would also need content from Lecture [X]

## Difficulty Forecast
[Based on the content density, concept abstractness, and number of similar/confusable terms, rate how hard this lecture will be to study.]

### Easy Wins (learn these first)
- [Concept] — straightforward definition, unlikely to confuse with anything
- [Concept] — concrete example makes it memorable

### Tricky Distinctions (spend extra time here)
- [Concept A] vs [Concept B] — similar names/ideas but critically different because [reason]
- [List of N items] — need to memorize all N, easy to forget 1-2

### Conceptual Leaps (hardest to master)
- [Concept] — requires understanding [prerequisite] first, then applying to [context]
- [Mechanism] — multi-step chain, if one step is wrong the whole answer falls apart

## Study Strategy for This Lecture

### Recommended Order
1. Read this report fully (you're doing this now)
2. Open `flashcard_mindmap.html` — explore the concept map, hover over contexts
3. Start with Cloze Overview cards — get the big picture of each topic
4. Drill individual Cerebro Basic cards by topic cluster
5. Focus extra time on "Tricky Distinctions" section above
6. After first pass, filter by tags you struggled with and repeat

### Time Estimate
- First pass through all [N] cards: ~[estimate based on card count] minutes
- Review of tricky distinctions: ~[estimate] minutes
- Total recommended study time for this lecture: ~[estimate] minutes

## Tags Reference
- **Tier 1 (Domain):** [list all unique Tier 1 tags from this lecture's cards]
- **Tier 2 (Week):** Week-[N]
- **Tier 3 (Concepts):** [list all unique Tier 3 tags]

To filter in Anki: `tag:[tier1-tag]` shows that concept across ALL lectures. `tag:Week-[N]` shows only this lecture.
```

---

## Workflow

1. Read all available materials (transcript, slides, reading PDF)
2. Identify themes, concepts, and their relationships
3. Write `lecture_summary.md` → save to lecture folder root
4. If flashcards.tsv exists, read it for card statistics and tags
5. Write `before_starting_report.md` → save to `Flashcards/`

---

## What NOT to Do

- Never produce a bullet-point dump without narrative connections
- Never copy-paste transcript segments as summaries
- Never include administrative content (scheduling, logistics)
- Never make exam predictions without grounding them in the exam format and lecture emphasis
- Never write the summary without reading the full material first
