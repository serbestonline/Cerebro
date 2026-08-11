---
name: investigating-brain-functions-flashcards
description: Generate Anki flashcards from Techniques for Investigating Brain Functions (UNIGE, Masters). Inherits all card architecture, card type, tagging, and format rules from flashcard-generator.md. This file defines the course-specific scope, essay exam format (5 open questions), and technical content rules.
inherits: ../flashcard-generator.md
---

# Investigating Brain Functions Flashcards

**Course:** Techniques for Investigating Brain Functions (UNIGE, Masters)
**Instructor language:** English
**Deck:** User selects during Anki import — do not hardcode in TSV

---

## Exam Format

**Type:** Written exam.

**Structure:**
- **5 open questions** (one-page essay for each question)
- **Duration:** 2 hours (10:15 - 12:15)
- **Nature of Questions:** Typically asks to explain the physical principles, physiological basis, signal source, spatial/temporal resolution, advantages/disadvantages, or experimental application of a given technique (e.g., EEG, fMRI, PET, Optogenetics) or compare two techniques.

### Implications for Card Design

- **Technique Profiling**: For every brain investigation technique (EEG, MEG, MRI, fMRI, PET, Optogenetics, etc.), there must be cards detailing:
  1. **Physical Principle / Mechanism** (How does it work?)
  2. **Physiological Signal** (What biological change does it measure?)
  3. **Spatial & Temporal Resolution** (And why it has those characteristics)
  4. **Pros & Cons / Limitations** (Invasiveness, depth, cost, safety, etc.)
  5. **Clinical & Research Application** (When is it used?)
- **Comparison & Contrast**: Cards comparing overlapping methods (e.g., EEG vs. MEG, PET vs. fMRI, structural vs. functional imaging).
- **Essay Prep**: All cards should target details needed to construct a well-structured, one-page essay answer.

---

## Previous Year Exam Questions

These questions illustrate the expected depth and focus of the 5 open-question exam:

- **Q1 (Psychophysiology / Autonomic Systems)**: A friend of yours wants to use electrodermal conductivity recordings and pupillometry at the same time while presenting pleasant, unpleasant and neutral images. Give 2 reasons why it is a bad idea. Explain what would be the expected responses for both techniques with 1) pleasant 2) neutral and 3) unpleasant stimuli.
- **Q2 (Electrophysiology / Membrane Potential)**: Describe what are the ion flows and the constituents that participates to the membrane potential. How is resting membrane potential maintained?
- **Q3 (EEG / BCI)**: Provide 2 EEG/ERP signatures, what they are, in what experimental condition or pathologies they can be triggered and modified. For each of these 2 signatures, illustrate a real world BCI (brain-computer interface) implementation that could be done.
- **Q4 (fMRI / Hemodynamic Response)**: Give a definition of the hemodynamic response function. Explain its shape and its use in fMRI data analysis.

*(Note: The question regarding iEEG has been excluded as there is no iEEG lecture in the current year's curriculum.)*

---

## Input Materials

Each lecture folder contains:
- **Lecture slides PDF** — slides covering specific techniques
- **Lecture transcript** (`.txt` or `.srt`/`.vtt`) — rich details on physical principles and experimental design
- **Flashcards** (`.tsv` file) — previously generated flashcard deck (to be audited and checked for coverage)

---

## Card Types for This Course

All card types from `flashcard-generator.md` apply. Course-specific emphasis:

### 1. Technique Overview (Cerebro Basic)
- Summarizes the core definition of the technique.
- Front: `What is the core principle of [Technique]?`
- Back: Concise 2-sentence explanation of how it functions and what it measures.

### 2. Physical & Physiological Basis (Cerebro Basic)
- Front: `What is the physical signal measured in [Technique]?` or `How does [Technique] generate [Signal]?`
- Back: Detail the physics and biology (e.g., LFP for EEG, BOLD for fMRI, annihilation photons for PET).

### 3. Resolution & Parameters (Cerebro Basic)
- Front: `What is the spatial/temporal resolution of [Technique] and why?`
- Back: Specific limits (e.g., milliseconds for EEG, millimeters for fMRI) and their physical/biological constraints.

### 4. Method Comparison (Cerebro Basic)
- Front: `What are the key differences between [Technique A] and [Technique B] regarding [Property]?`
- Back: Comparison points (e.g., MEG magnetic fields are less distorted by skull than EEG electric fields).

### 5. Research/Clinical Application (Cerebro Basic)
- Front: `What makes [Technique] uniquely suited for studying [Topic]?`
- Back: Specific experimental advantage (e.g., fMRI for whole-brain mapping, single-cell recording for spike timing).

---

## Practice Questions (End of Output)

For each lecture/technique, generate practice exam questions at the end of the output that mirror the real exam format:
- **Format**: `Practice: [Technique / Question]` -> structured essay outline.
- **Answer Structure**:
  1. **Introduction/Core Definition** (1-2 sentences)
  2. **Underlying Physics/Biology** (2-3 bullet points)
  3. **Technical Specs (Resolution, signal)** (2 bullet points)
  4. **Advantages & Limitations** (2-3 bullet points)
  5. **Representative Application** (1-2 sentences)

---

## Content Exclusions

- Minor administrative details from slides
- Unrelated history notes
- Personal issues or jokes. 
---

## Coverage Verification

Before finalizing a study deck, verify:
- All 5 profiling aspects (physics, signal, resolution, pros/cons, applications) have cards for every technique introduced.
- Comparisons of closely related methods are present.
- Glossary terms or key bolded definitions from the slides are covered.
