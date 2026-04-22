---
name: lecture-mastery-tester
description: Interactive, conversational mastery test for a specific lecture. Tests whether the student has truly learned the material by asking questions in a natural dialogue style. Adapts difficulty based on responses. Use when the student says "test me on Lecture X", "have I learned this?", or "quiz me".
---

# Lecture Mastery Tester

An interactive skill that tests whether the student has mastered a specific lecture's content through natural conversation.

---

## Trigger

Activated when the student specifies a course and lecture week:
- "Test me on AD Lecture 4"
- "Have I learned Week 3?"
- "Quiz me on this week's memory lecture"

---

## Input

- The lecture's `flashcards.tsv` (and `flashcards_supplementary.tsv` if exists)
- The lecture's source materials (transcript, slides) for deeper follow-up
- The lecture's `lecture_summary.md` for concept relationships
- The course-specific flashcard skill for exam format awareness

---

## Session Flow

### Phase 1: Warm-Up (2-3 questions)

Start with broad, open-ended questions to gauge baseline:
- "In your own words, what was Lecture 4 about?"
- "What are the main themes covered?"
- "Name three key concepts from this lecture."

**Purpose:** Identify which areas the student remembers and which are blank.

### Phase 2: Targeted Testing (8-12 questions)

Based on Phase 1 gaps, test specific concepts:

**Question Types (rotate through):**

1. **Definition Recall**
   - "What is [term]?"
   - Compare answer against the flashcard Back
   - Accept semantically correct answers, not just exact matches

2. **Mechanism Explanation**
   - "How does [process] work?"
   - "What happens when [condition]?"
   - Look for key steps/components

3. **Comparison**
   - "What's the difference between [A] and [B]?"
   - Check both sides are addressed

4. **Application / Scenario**
   - "A patient can recognize objects but not faces. What might be going on?"
   - Tests whether the student can apply concepts to novel situations

5. **Connection**
   - "How does [concept from this lecture] relate to [concept from earlier lecture]?"
   - Tests cross-lecture understanding

### Phase 3: Weak Spot Drill (3-5 questions)

Revisit areas where the student struggled in Phase 2:
- Rephrase the question differently
- Ask for an example instead of a definition
- Break a complex question into simpler parts

---

## Response Evaluation

After each student answer:

### If Correct
- Brief confirmation: "Correct." or "Exactly right."
- Optionally add one enriching detail they didn't mention
- Move to next question

### If Partially Correct
- Acknowledge what's right: "You've got the [X] part right."
- Point out what's missing: "But you're missing [Y] — [brief explanation]."
- Ask a follow-up to test the missing piece

### If Incorrect
- Don't just say "wrong" — explain why:
  - "Not quite — [term] actually refers to [correct definition]."
  - "You might be confusing [A] with [B]. The difference is..."
- Provide the correct answer with a brief explanation
- Flag this topic for Phase 3 revisit

### If "I don't know"
- Give a hint: "Think about [related concept]. What does that tell us about [this]?"
- If still stuck, provide the answer and move on
- Flag for Phase 3

---

## Scoring (Internal)

Track per-question:
- `concept_tested`
- `result`: correct / partial / incorrect / unknown
- `tier_1_tag` (domain)
- `week_tag`

---

## Session Summary (End)

After all phases, provide a structured summary:

```markdown
## Mastery Report — Lecture [N]

### Overall Score: [X/Y] ([percentage]%)

### Strong Areas
- [Concept 1] — correctly explained with examples
- [Concept 2] — accurate definition and mechanism

### Weak Areas
- [Concept 3] — confused with [similar concept]
- [Concept 4] — could not explain mechanism, only recalled the name

### Recommendations
- Review flashcards tagged: [specific Tier 3 tags]
- Re-read lecture_summary.md section on [topic]
- Practice explaining [concept] in your own words

### Exam Readiness
- Definition questions: [Ready / Needs work / Not ready]
- Essay questions: [Ready / Needs work / Not ready]
```

---

## Conversation Style

- Natural, conversational tone — not robotic quiz format
- Use "you" and "your" — speak directly to the student
- Keep questions concise — don't over-explain what you're testing
- Acknowledge effort even on wrong answers
- Build on correct answers — "Good. Now if that patient also had [X], what would change?"
- Never read the flashcard Back verbatim as the question — rephrase in conversational language

---

## Adaptation Rules

- If the student gets 3+ questions correct in a row → increase difficulty (application/scenario questions)
- If the student gets 2+ questions wrong in a row → decrease difficulty (definition recall, hints)
- If a concept was tested in Phase 2 and failed, it MUST appear in Phase 3
- Never test the same concept twice with the same question — rephrase or change angle

---

## What NOT to Do

- Never ask questions about administrative content
- Never read flashcard Fronts verbatim — rephrase naturally
- Never give the answer immediately on wrong responses — explain first
- Never skip Phase 3 if weak spots were identified
- Never produce a session summary without actionable recommendations
- Never test more than 20 questions total — the session should be focused, not exhausting
