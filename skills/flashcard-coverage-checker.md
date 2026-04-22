---
name: flashcard-coverage-checker
description: Compare existing Anki flashcard decks against lecture source materials to identify uncovered topics and generate supplementary cards. Course-agnostic — works with any course. Inherits card format rules from flashcard-generator.md for supplementary card generation.
inherits: flashcard-generator.md
---

# Flashcard Coverage Checker

Compares existing flashcards against source materials. Identifies gaps. Generates `flashcards_supplementary.tsv` for uncovered content. Also maps cross-lecture concept connections within a course.

---

## Inputs

### 1. Flashcard Files
Previously generated TSV files (`flashcards.tsv`, or any `*flashcard*` file).
Recognized by `#separator:tab` header or Cerebro notetype names.

### 2. Lecture Source Materials
One or more of:
- Lecture slides PDF
- Lecture transcript (.txt)
- Reading PDF
- RMD files (for statistics course)

### Multi-File Mapping
When multiple sources and decks are provided:
1. Use explicit user mapping if given
2. Match by filename/date/lecture ID tokens
3. Match by strongest topic overlap
4. If confidence is low, state assumptions in one line before analysis

---

## Analysis Workflow

### Step 1 — Extract Lecture Topics

Build a flat topic inventory. A topic is a distinct, testable knowledge unit:
- Named concepts, terms, definitions
- Methods, algorithms, techniques
- Syndromes/disorders/brain regions
- Explicitly drawn comparisons
- Key mechanisms or processes
- Emphasized findings/paradigms
- Decision rules or classification criteria

For each topic:
- `topic_id`
- `topic_label` (short name)
- `source_hint` (slide/page/time)
- `priority` (`high` / `medium` / `low`)

Priority rules:
- `high`: named concept likely to be on exam (title, repeated, emphasized, in glossary)
- `medium`: supporting mechanism or secondary but testable distinction
- `low`: tangential aside or low-emphasis mention

Skip: administrative content, logistics, greetings, out-of-scope material.

### Step 2 — Extract Flashcard Coverage

Parse all flashcard files. For each card:
- Front/prompt
- Back/answer
- Tested concept
- Testing angle: `definition`, `mechanism`, `comparison`, `application`, `code`

Build `covered_concepts` list.

### Step 3 — Match Topics to Cards

For each topic, assign exactly one status:

**COVERED** — at least one card tests the topic as primary target in the Front, and at least one required angle is tested.

**PARTIALLY COVERED** — topic appears only as secondary context/answer mention, or the topic is tested but a required angle is missing.

**UNCOVERED** — no card tests or meaningfully references the topic.

Matching is semantic, not exact keyword matching.

### Step 4 — Generate Supplementary Cards

Generate supplementary cards **only** for unresolved `high` or `medium` gaps.

**Rules:**
- Follow all rules from `flashcard-generator.md` (MIP, Cerebro types, 3-tier tags, back minimization)
- Mirror the existing deck's conventions (deck name, tag patterns)
- For `PARTIALLY COVERED`, generate only the missing angle
- Do not regenerate already covered topics
- Enforce deduplication against existing deck AND newly generated cards

**Output:**
```
[Lecture Folder]/Flashcards/flashcards_supplementary.tsv
```

Same TSV format as the main flashcards file. Same header.

**When NOT to generate supplementary cards:**
- Coverage is >= 90% and all remaining gaps are `low` priority
- User explicitly requests analysis-only mode

---

## Cross-Lecture Concept Map

When analyzing a course with multiple lectures processed, identify concepts that appear across weeks:

```
"Dissociation" concept:
  Week 1: Definition + double dissociation logic (foundation)
  Week 2: Aphasia dissociations (Broca vs Wernicke)
  Week 3: Reading dissociations (surface vs phonological alexia)
  Week 5: Visual agnosia dissociations (prosopagnosia vs object agnosia)
  → Spans 4 lectures — strong essay question candidate
```

This information feeds into the `before_starting_report.md` exam relevance section.

---

## Calibration

This is a coverage check, not a perfectionist audit.
- One well-scoped card may cover a cluster of tightly related sub-points
- Brief passing mentions are `low` priority
- Emphasis signals raise priority (title, repetition, explicit "important")
- Purely illustrative anecdotes do not require standalone cards

---

## What NOT to Do

- Never regenerate the entire deck — only fill true gaps
- Never critique card quality — this skill checks coverage only
- Never hallucinate topics not present in source materials
- Never split every transcript sentence into separate topics
- Never produce supplementary cards that violate MIP (one idea per card)
- Never skip the cross-lecture concept map when multiple lectures are available
