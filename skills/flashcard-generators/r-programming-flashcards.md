---
name: r-programming-flashcards
description: Generate Anki flashcards from Introduction to Applied Statistics lecture materials (AA course, UNIGE). Inherits all card type, MIP, tagging, and format rules from flashcard-generator.md. This file defines the course-specific scope, dual-layer input (RMD primary + PPTX/transcript secondary), code card rules, and content targets.
inherits: ../flashcard-generator.md
---

# R Programming & Applied Statistics Flashcards

**Course:** AA — Introduction to Applied Statistics for Health Data Analysis (UNIGE, Masters)
**Instructor language:** English
**Deck:** User selects during Anki import — do not hardcode in TSV

---

## Exam Format

This course combines R programming skills with statistical theory. Exam details to be confirmed — card design covers both code fluency and conceptual understanding.

---

## Input Materials — Dual-Layer System

This course provides two distinct types of material. Each layer produces different card types.

### Layer 1: RMD Files (Primary for Code Cards)

R Markdown files (`.Rmd`) contain:
- R code chunks with executable examples
- Function demonstrations with input/output
- Data manipulation exercises
- Exercise solutions (correction files)

**Card output:** Primarily `Cerebro Type Code` (70-85%) + `Cerebro Basic` (15-30%)

### Layer 2: PPTX + Transcript (Primary for Theory Cards)

PowerPoint slides (`.pptx`) and lecture transcripts (`.txt`) contain:
- Statistical concepts (p-value, hypothesis testing, confidence intervals)
- Theoretical foundations
- Interpretation guidelines

**Card output:** Primarily `Cerebro Basic` + `Cerebro Cloze`

### Combined Input

When both layers are provided together, produce a balanced mix. Do not duplicate concepts across layers — if a concept appears in both RMD and PPTX, merge into one card using the richer source.

---

## Card Type Distribution

### When input is RMD-heavy:
- `Cerebro Type Code`: 70-85%
- `Cerebro Basic`: 15-30%

### When input is PPTX/transcript-heavy:
- `Cerebro Basic`: 60-70%
- `Cerebro Cloze`: 15-25%
- `Cerebro Type Code`: 10-15% (for any code examples in slides)

### Distribution Audit
Before finalizing each batch, verify the distribution. If outside thresholds, rebalance by converting edge-case cards.

---

## Cerebro Type Code Rules (Course-Specific)

### Front Design
- Never ask "what function does X?" in isolation
- Always embed the function in a **concrete scenario** with specific values
- Use `<b>bold</b>` on key variable names or values
- Use `<code>` tags for inline code references

### Back Design
- The exact string the student must type — nothing more
- Code must be written exactly as it would appear in R

### HTML Rules
- Allowed tags: `<b>`, `<code>`, `<div>` only
- Set `#html:true` in TSV header for this course (code cards need HTML rendering)

### Examples

**Good:**
```
Cerebro Type CodeWrite the code to check the type of <b>"plouf"</b>.	class("plouf")	class() returns the type of an R object as a character string.		statistics Week-2 class-function
```

**Good:**
```
Cerebro Type CodeWrite the code to assign the value <b>2</b> to variable <b>x</b>.	x <- 2	The <- operator is R's standard assignment operator.		statistics Week-2 assignment
```

**Bad:**
```
Cerebro Type CodeWhat function checks types in R?	class()	...
```
(Too vague — no concrete scenario)

---

## Cerebro Basic Rules for Theory Cards

### Statistical Concept Cards
- Format: `What is [concept]?` → precise definition
- Include when-to-use context in the Context field
- Connect concepts to R implementation when relevant

### Interpretation Cards
- Format: `How do you interpret [result]?` or `What does a p-value of 0.03 mean?`
- Back: the correct statistical interpretation, not the common misconception
- Context: common misconceptions and why they're wrong

### Error/Mechanism Cards (Cerebro Basic)
- R-specific edge cases and error behavior
- Format: code in `<code>` tags + "What does this return and why?"
- Back: mechanism-first explanation

| Scenario | Expected Behavior |
|----------|-------------------|
| `"5" + 10` | Error — character + numeric not allowed |
| `TRUE + 1L` | Works — logical coerces to integer (TRUE=1) |
| `1L + 1.5` | Works — integer promotes to double |
| `x[n]` where n > length(x) | Returns NA, not an error |
| `factor` in arithmetic | Error or unexpected |
| `as.numeric("abc")` | Returns NA with a warning |

---

## R-Specific Card Targets

### Always generate cards for these when present:
- Assignment operators: `<-`, `=`, `->` and usage
- Data types: `numeric`, `character`, `factor`, `logical` — definitions and `class()` output
- Type coercion functions: `as.numeric()`, `as.character()`, `as.factor()`
- Vector creation: `c()`, named vectors, `1:n` range syntax
- Vector indexing: single `[i]`, multiple `[c(i,j)]`, range `[i:j]`, named `["name"]`
- Data frame operations: `$`, `[]`, `[[]]`, `filter()`, `select()`, `mutate()`
- dplyr/tidyverse functions when taught
- Statistical functions: `t.test()`, `cor()`, `lm()`, `summary()`
- Plotting: `ggplot()`, `aes()`, `geom_*()` when taught

---

## TSV Header Override

This course uses `#html:true` because code cards require HTML rendering:

```
#separator:tab
#html:true
#notetype column:1
#tags column:7
```

---

## Content Exclusions

- IDE instructions (panel locations, button clicks, RStudio UI)
- Course administrative content
- Package installation commands (`install.packages()`)
- Content about setting up the R environment

---

## Coverage Verification

Before finalizing output:
- Every named R function demonstrated in the material has a card
- Every statistical concept has a definition card
- Every error/edge-case scenario shown has a mechanism card
- Every data type and coercion path demonstrated has a card
- Card distribution is within thresholds
