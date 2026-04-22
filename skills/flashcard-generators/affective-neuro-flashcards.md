---
name: affective-neuro-flashcards
description: Generate Anki flashcards from Affective and Cognitive Neuroscience lecture materials (AB course, UNIGE). Inherits all card type, MIP, tagging, and format rules from flashcard-generator.md. This file defines only the course-specific scope, exam format, scenario-based practice questions, and content rules.
inherits: ../flashcard-generator.md
---

# Affective Neuroscience Flashcards

**Course:** AB — Affective and Cognitive Neuroscience (UNIGE, Masters)
**Instructor language:** English
**Deck:** User selects during Anki import — do not hardcode in TSV

---

## Exam Format

**Type:** Written exam with scenario-based questions.

The exam presents real-world scenarios and asks students to explain what happened in terms of brain areas, functions, mechanisms, and empirical evidence.

### Implications for Card Design
- Cards must connect brain regions to functions and to observable behavior
- Mechanism chains (stimulus → processing → outcome) are critical
- Empirical evidence with citations is required in answers
- Students need to apply knowledge to novel scenarios, not just recall definitions

---

## Known Exam Questions

These define the scope and style of the exam. Use them to calibrate card depth and practice question design.

**Q1:** Mark takes an unripe green mango instead of a ripe yellow one in a dimly lit kitchen. Describe what could have happened in terms of brain areas and functions. List all possibilities.

**Q2:** Debate about sensory-based vs task-based definitions of primary sensory cortices. Your opponent argues sound could never trigger a response in V1. What could you answer? What could they answer back?

**Q3:** Hannah and Sarah are monozygotic twins. Hannah started violin at age 6, Sarah did not. Explain expected differences in brain function and morphology at age 10, 20, and old age. Provide empirical examples and mechanisms.

**Q4:** Three patients: visual agnosia, aphasia, central semantic deficit. Describe neuropsychological tests to differentiate them. Expected responses by condition. Brain correlates.

**Q5:** Charlie was bitten by a dog and now fears all dogs. Explain with Pavlovian conditioning. Why is the original Rescorla-Wagner formula insufficient? How can it be improved?

**Q6:** Students speed up lecture playback. Around 2.5-3x they can't follow. Using Giraud and Poeppel (2012), explain why speech processing has upper limits.

---

## Input Materials

Each lecture folder typically contains:
- **Lecture slides PDF** — structured content with slide organization
- **Lecture transcript** (.txt) — spoken elaboration and mechanistic reasoning
- **Subtitle files** (.srt, .vtt) — alternative transcript source

Process all available materials together in a single pass. The transcript provides the richest mechanistic detail. The PDF provides structure and concept boundaries.

---

## Card Types for This Course

### Definition Cards (Cerebro Basic)
- Every named concept, syndrome, disorder, principle, or theory
- Every brain region ↔ function mapping

### Mechanism Cards (Cerebro Basic) — highest priority for this course
- Causal chains: stimulus → brain region → processing → behavioral outcome
- Multi-step processes (e.g., fear conditioning pathway)
- Break complex mechanisms into atomic cards

### Brain Region ↔ Function Cards (Cerebro Basic)
- Critical for this course — the exam requires knowing which brain areas do what
- Format: `What is the role of [region] in [function]?`
- Back: state the function, then the evidence

### Empirical Study Cards (Cerebro Basic)
- Named studies with author and year
- Format: `What did [Author et al., year] demonstrate?`
- Back: manipulation → finding → theoretical significance
- Citations are required for key findings

### Comparison Cards (Cerebro Basic)
- Competing theories or models
- Format: `What is the key difference between [theory A] and [theory B]?`

### Clinical/Patient Cards (Cerebro Basic)
- Patient types or conditions used as examples
- Deficit AND what it reveals about the system

### Cloze Overview (Cerebro Cloze)
- Inherited — mandatory for 3+ item lists

### Standard Cloze (Cerebro Cloze)
- Brain region names, key dates, researcher names tied to findings

---

## Practice Questions (End of Output)

Generate scenario-based practice questions that mirror the exam style (Q1-Q6 above).

### Design Rules
- Each practice question presents a **novel scenario** (not copied from Q1-Q6)
- The scenario requires applying knowledge of brain regions, mechanisms, and empirical evidence
- Each question must be answerable using content from the processed lecture
- Map each practice question to one or more exam questions (Q1-Q6) by style

### Format
```
Cerebro Basic	Practice (Q#): [scenario]	[answer with mechanism + evidence]	[extended context]		[Tags]
```

### Density Rule
- Default: 1 practice question per completed lecture
- Generate 2 if the lecture covers 5+ distinct core concepts or is particularly dense

---

## Content Selection (Course-Specific)

### Include
- Every named concept, disorder, syndrome, model
- All brain region ↔ function mappings
- Mechanisms and causal chains
- Named empirical studies with theoretical significance
- Clinical conditions with neural correlates
- Contrasts between competing theories
- Plasticity mechanisms and developmental changes

### Exclude
- Administrative or organizational content
- Anecdotes with low conceptual value
- Duplicated content already covered in the same set
- Details without exam relevance

---

## Coverage Verification

Before finalizing output:
- Every named concept/syndrome/disorder has at least one definition card
- Every major argument contrast has a comparison card
- Every brain region mentioned with a function has a region ↔ function card
- Every named model has cards for purpose + components + implication
- Every high-yield empirical study has an evidence card with citation
- At least one practice question is included per lecture
