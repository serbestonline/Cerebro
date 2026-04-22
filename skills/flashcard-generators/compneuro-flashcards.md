---
name: compneuro-flashcards
description: Generate Anki flashcards from Trends in Computational Neuroscience lecture materials (AC course, UNIGE). Inherits all card type, MIP, tagging, and format rules from flashcard-generator.md. This file defines only the course-specific scope, exam format, MCQ generation, and content rules.
inherits: ../flashcard-generator.md
---

# Computational Neuroscience Flashcards

**Course:** AC — Trends in Computational Neuroscience (UNIGE, Masters)
**Instructor:** Pouget
**Instructor language:** English
**Deck:** User selects during Anki import — do not hardcode in TSV

---

## Exam Format

**Type:** Multiple Choice Questions (MCQ) only.

**Key constraint from lecturer:** "Whatever question we ask, the answers are all on the slides." No derivations. No proofs. Understanding the principle behind a method is sufficient.

### Implications for Card Design
- Definitions must be crisp and unambiguous — MCQ distractors exploit vague understanding
- "When to use X vs Y" decisions are the highest-value card targets — natural MCQ material
- No essay scaffolding needed
- Slide content is authoritative for correct answers

---

## Input Materials

Each lecture folder typically contains:
- **Lecture slides PDF** — primary authority for exam answers
- **Lecture transcript** (.txt) — spoken elaboration and mechanistic reasoning

Cross-reference both:
- If a concept appears in the transcript but not the slides → use the transcript
- If a concept is on the slide but the transcript only glosses over it → use slide bullets as the authoritative answer
- Slide titles function as concept labels. Transcript passages provide mechanistic explanation.
- Never duplicate cards for the same concept. Merge PDF and transcript into one card per concept.

---

## Card Types for This Course

### 1. Definition Cards (Cerebro Basic) — every named method
- Every named method, concept, algorithm, or principle gets a definition card
- Format: `What is [X]?` → 1-2 sentence answer capturing what it does and what assumption or goal underlies it

### 2. Comparison Cards (Cerebro Basic) — high value
- For any two or more methods sharing a domain but differing in assumptions, use case, or behavior
- Format: `What is the key difference between X and Y?`
- Back: `X: [property]. Y: [property].` No evaluation unless the lecturer explicitly recommends one.
- Cover all pairwise comparisons the lecturer draws explicitly

### 3. When-to-Use Cards (Cerebro Basic) — highest value
- For every method discussed, generate a card targeting when to apply it
- Format: `When should you use [X] instead of [Y]?` or `In what situation is [X] appropriate?`
- Back states the triggering condition first, then the reasoning
- **These are the most important cards for this course**

### 4. Cloze Cards (Cerebro Cloze)
- Method names or acronyms that need memorization
- Comparative structures worth drilling
- Data properties that map directly to a method or principle

### 5. Cloze Overview
- Inherited from central rules — mandatory for lists of 3+ items (e.g., components of a model, steps in an algorithm)

---

## Card Philosophy (Course-Specific)

1. **Scope Rule:** Answer exactly what the question type requires. What → definition. Difference → X: property, Y: property. When → condition + reasoning.
2. **Length Rule:** 1-2 sentences default. Hard cap: 3 sentences. 3+ items → bullets, max one clause each.
3. **Content Rule:** No storytelling. No meta-commentary. State the principle directly.
4. **Stop Rule:** If the question is fully answered, stop.
5. **No-Overlap Rule:** Merge cards testing the same concept from the same angle. A single well-scoped card beats two overlapping ones.

### Include
- Every named method, algorithm, technique, or architectural type
- All key assumptions underlying each method
- Advantages and limitations when discussed
- Pairwise comparisons the lecturer draws explicitly
- Decision rules for method selection
- Conceptual frameworks (neural manifold, encoding/decoding, supervised vs unsupervised)
- Deep learning architectures (CNN, RNN, LSTM, Transformer) — definitions, properties, use cases, limitations

### Exclude
- Administrative content
- Numerical values unless conceptually essential
- Content the lecturer explicitly flags as out of scope
- Author names, paper titles, publication venues
- Slides containing only images with no textual claim

---

## End-of-Lecture MCQ Generation

Triggered **only** when explicitly requested or when the full lecture material has been processed.

### MCQ Design Rules

**Primary source: PDF slides only.** Every correct answer must be directly traceable to a slide.

- Generate **20-25 questions** per lecture
- Re-scan the full PDF after processing — don't rely only on what was emphasized during card generation
- Focus: principle behind a method, what it does and why, key distinctions, when-to-use decisions
- Each question: exactly one correct answer
- Distractors: plausible — represent common misconceptions, not obviously absurd options
- Question stem: self-contained — no references to "the slide" or "as mentioned"
- Explanation: state why the correct answer is right, not just restate it
- Never test author names or publication venues
- Never test content not on any slide

### MCQ TSV Format

```
#separator:tab
#html:false
#notetype column:1
#tags column:13
```

Row structure (13 columns):
```
Multiple Choice	[Question]		2	[Option A]	[Option B]	[Option C]	[Option D]		[answer_key]	[explanation]
```

- Column 10 (answer_key): space-separated 1/0 (e.g., `0 1 0 0` = B is correct)
- Column 11 (explanation): one sentence explaining why

### MCQ Coverage Audit

Before finalizing MCQ output:
1. Build inventory of testable items from slides
2. Map each item to at least one MCQ
3. Enforce: at least 1 MCQ per major method, 20%+ test comparisons/when-to-use, 10%+ test limitations
4. Resolve all MISSING items before export

---

## Content Exclusions (Course-Specific)

- Author names, paper titles, publication venues, study-level attribution
- Slides containing only images with no textual claim
- Numerical values unless conceptually essential
- Content the lecturer explicitly flags as out of scope

---

## Coverage Verification

Before finalizing output:
- Every named method or algorithm has a definition card
- Every comparison the lecturer draws explicitly has a comparison card
- Every method has a when-to-use card
- No named concept or technique is missing
- Every slide with substantive bullet content has been processed
