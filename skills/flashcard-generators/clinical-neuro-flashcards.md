---
name: clinical-neuro-flashcards
description: Generate Anki flashcards from Clinical and Cognitive Neuropsychology lecture materials (AD course, UNIGE). Inherits all card type, MIP, tagging, and format rules from flashcard-generator.md. This file defines only the course-specific scope, exam format, and content rules.
inherits: ../flashcard-generator.md
---

# Clinical Neuropsychology Flashcards

**Course:** AD — Clinical and Cognitive Neuropsychology (UNIGE, Masters)
**Instructor language:** English
**Deck:** User selects during Anki import — do not hardcode in TSV

---

## Exam Format

**Type:** Written exam (not oral).

**Structure:**
- **4 essay questions** — each worth **6 points**
  - Expected length: **400-500 words** per answer
  - Typical format: a concept is given, then the student is asked to provide **3 examples**, describe mechanisms, compare hypotheses, or give neurological evidence
  - Grading is granular: e.g., if 3 examples are requested and only 2 given → max ~4/6 points
- **6 definition questions** — each requiring a **2-sentence definition**
  - These **generally but not always** come from the glossary at the end of each lecture PDF
  - The lecturer reserves the right to ask definitions outside the glossary

### Implications for Card Design

- Every glossary term → `Cerebro Basic` card with `What is [X]?` front and a precise 2-sentence back that could stand alone as an exam answer
- Every major mechanism/model/debate → broken-down cards sufficient to scaffold a 400-500 word essay
- Argument cards must cover enough material to provide **3 distinct examples** when asked
- Definition cards must be exam-ready — precise, complete, standalone

---

## Previous Year Exam Questions

**Definition questions (2-sentence answers):**
- Q1: Define Paramnesia.
- Q2: Define Phonological Alexia.
- Q3: Define Hemispheric Rivalry.
- Q4: Define Achromatopsia.
- Q5: Define Blindsight.

**Essay questions (~400-500 words, 6 points each):**
- Q6: What is hemiplegic anosognosia? Give 3 hypotheses explaining how anosognosia could occur.
- Q7: Describe 3 main differences between organic and dissociative amnesia and provide a neurological accounting of these.
- Q8: Describe the dual pathway used for writing. Provide 2 examples of disorders that induce writing issues.
- Q9: What are mirror neurons? Explain why mirroring mechanisms are important for compassion and social interactions.

### Patterns Observed
- Definition questions target glossary terms and similar clinical/theoretical concepts
- Essay questions follow: **"What is X? + specific task"** (give N examples, describe N differences, explain why)
- Essay questions can span multiple lectures
- The number of examples/differences requested (2-3) directly maps to the grading rubric

---

## Input Materials

Each lecture folder typically contains:
- **Lecture slides PDF** — main content, glossary on last page(s)
- **Lecture transcript** (.txt) — full spoken content from the lecture recording
- **Reading PDF** — supplementary academic reading

Process all three together in a single pass. The transcript is the richest source for mechanisms and examples. The PDF provides structure and the glossary. The reading PDF adds depth.

---

## Glossary Extraction (Course-Specific Rule)

This course has a glossary on the last page(s) of each lecture's slide PDF.

### Detection
- If a PDF page is labeled "Glossary" or "Course Glossary", treat it as the official definition-question source
- Parse all listed terms from every lecture PDF

### Required Action
- Generate one `Cerebro Basic` card per glossary term:
  - Front: `What is [TERM]?`
  - Back: Precise 2-sentence definition, exam-ready
  - Context: Extended explanation from transcript
- Glossary cards are **mandatory** — they override normal filtering rules
- Never merge glossary terms into shared cards
- Never skip a glossary term

### Verification
Before finalizing output, confirm every glossary term detected in the PDF has a dedicated card. No unresolved missing glossary terms may remain.

---

## Card Types for This Course

All card types from `flashcard-generator.md` apply. Course-specific emphasis:

### Definition Cards (Cerebro Basic) — highest priority
- Every named concept, syndrome, disorder, principle, or theory
- Format: `What is [X]?` → 1-2 sentence answer
- Every glossary term gets one

### Mechanism Cards (Cerebro Basic)
- Processes, models, multi-step explanations
- Break into atomic cards — one mechanism/step/hypothesis per card

### Argument/Comparison Cards (Cerebro Basic)
- "Arguments for/against X", "differences between X and Y"
- Maps to essay questions
- Cover both sides when applicable

### Empirical Study Cards (Cerebro Basic)
- Named studies or experimental findings
- Format: `What did [Author et al., year] demonstrate?`
- State finding AND theoretical significance

### Clinical Case Cards (Cerebro Basic)
- Named patients (e.g., H.M.) or patient types
- Format: `What does the case of [X] demonstrate?`
- State deficit AND theoretical implication

### Anecdote → Concept Cards (Cerebro Basic)
- The lecturer frequently uses everyday anecdotes
- The **question targets the concept**, not the anecdote
- Wrong: `What is the anecdote about color perception?`
- Right: `Why is subjective experience a challenge for reductive materialism?`
- The anecdote appears in Context, not in the question

### Cloze Overview (Cerebro Cloze)
- Inherited from central rules — mandatory for any list of 3+ items

---

## Practice Questions (End of Output)

Generate practice questions as a separate section at the end of the flashcard output.

### Question Design
- Mirror the style of previous-year essay questions (Q6-Q9)
- Style: short orienting clause ("What is X?") + specific task ("Give 3 hypotheses / Describe 2 disorders / Explain why")
- Each answerable in ~400-500 words
- Generate from actual lecture content — never recycle previous-year questions

### Question Types (priority order)
1. **Mechanism** — "Explain how X works"
2. **Hypothesis comparison** — "Compare hypothesis A and B for X"
3. **Clinical implication** — "What does disorder X reveal about mechanism Y?"
4. **Evidence-based argument** — "What evidence supports/challenges X?"

### Answer Structure (Back)
1. Core mechanism/definition (1-2 sentences)
2. Key arguments or hypotheses (bullet, one clause each)
3. Empirical evidence or clinical example (1-2 sentences)
4. Conclusion or theoretical implication (1 sentence)

### Format
```
Cerebro Basic	Practice: [prompt]	[structured answer]	[extended context]		[Tags]
```

---

## Content Exclusions (Course-Specific)

- Purely biographical details about historical figures unless theoretically relevant
- Numerical values unless conceptually essential (e.g., exact ms timings)
- Content that won't appear on a definition or essay exam

---

## Coverage Verification

Before finalizing output:
- Every glossary term has a dedicated `What is X?` card
- Every named concept, syndrome, or disorder has a definition card
- Every argument for/against a major approach has a card
- Every clinical case used as a teaching example has a card
- No named concept from the slides is missing
