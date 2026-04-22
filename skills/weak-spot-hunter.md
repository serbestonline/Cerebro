---
name: weak-spot-hunter
description: Analyze Anki review data (exported stats, deck performance) to identify weak spots — cards with low retention, high lapse count, or frequent failures. Provides targeted study recommendations. Use when the student asks "where am I weak?", "what should I focus on?", or provides Anki export data.
---

# Weak Spot Hunter

Analyzes Anki study performance data to find where the student is struggling. Different from coverage-checker — this skill looks at **how well the student knows the cards**, not whether the cards cover the material.

---

## Input

The student provides Anki data in one of these forms:

### Option 1: Anki Stats Export
- Screenshot or text of Anki's built-in statistics (review count, retention rate, intervals)

### Option 2: Card Browser Export
- Exported CSV/TSV from Anki's card browser with columns like:
  - `Due`, `Interval`, `Ease`, `Reviews`, `Lapses`, `Front`, `Back`, `Tags`, `Deck`

### Option 3: Manual Report
- Student describes what they're struggling with: "I keep getting the dissociation questions wrong"

### Option 4: Mastery Tester Results
- Output from `lecture-mastery-tester` sessions with scored results

---

## Analysis

### Metric Definitions

| Metric | What It Means | Threshold for "Weak" |
|--------|--------------|---------------------|
| **Retention Rate** | % of reviews answered correctly | < 80% |
| **Lapse Count** | Number of times a card was forgotten (relearned) | >= 3 lapses |
| **Ease Factor** | Anki's difficulty multiplier (default 250%) | < 200% |
| **Interval** | Days until next review | Cards still at < 7 days after 2+ weeks of study |
| **Mature Retention** | Retention on cards with interval > 21 days | < 85% |

### Analysis Steps

1. **Parse the data** — extract card-level metrics
2. **Flag weak cards** — any card meeting one or more weak thresholds
3. **Group by tags** — aggregate weakness by Tier 1 (domain), Tier 2 (week), Tier 3 (concept)
4. **Identify patterns:**
   - Is weakness concentrated in a specific lecture? → "Week 4 memory content needs review"
   - Is weakness in a specific domain? → "Visual cognition cards across multiple weeks are weak"
   - Is weakness in a specific card type? → "Cloze cards have lower retention than Basic"
5. **Cross-reference with exam format** — are the weak areas exam-critical?

---

## Output

```markdown
## Weak Spot Report

### Summary
- Total cards analyzed: [N]
- Cards flagged as weak: [N] ([percentage]%)
- Average retention: [X]%

### Weak Areas (by priority)

#### 1. [Topic/Tag] — [severity: critical / moderate / mild]
- Cards affected: [N]
- Average retention: [X]%
- Average lapses: [X]
- Exam relevance: [high/medium/low]
- **Key cards:**
  - "[Front text]" — [X] lapses, [Y]% retention
  - "[Front text]" — [X] lapses, [Y]% retention

#### 2. [Topic/Tag] — [severity]
- ...

### Patterns Detected
- [Pattern 1: e.g., "Week 4 cards have 2x the lapse rate of other weeks"]
- [Pattern 2: e.g., "Cloze Overview cards are well-retained but individual detail cards are not"]

### Recommendations

#### Immediate Actions
1. **Custom study session:** Filter by tags `[tag1] [tag2]` in Anki
2. **Re-read:** `lecture_summary.md` for Lecture [X], section on [topic]
3. **Drill:** Focus on these [N] specific cards (listed below)

#### Study Strategy Adjustments
- [e.g., "Your mechanism cards are weak — try explaining the mechanism out loud before revealing the answer"]
- [e.g., "Your Cloze gaps are too similar — consider whether some cards need reformulation"]

### Cards to Prioritize (sorted by weakness)

| # | Front | Deck | Lapses | Retention | Tags |
|---|-------|------|--------|-----------|------|
| 1 | [text] | [deck] | [N] | [X]% | [tags] |
| 2 | [text] | [deck] | [N] | [X]% | [tags] |
| ... |
```

---

## Integration with Other Skills

- **lecture-mastery-tester:** Weak spot data can inform which topics to test more heavily
- **flashcard-coverage-checker:** If many cards in an area are weak, it might indicate poor card quality rather than poor studying — suggest re-checking coverage
- **essay-scaffolder:** If weak spots align with likely essay topics, flag as urgent

---

## What NOT to Do

- Never diagnose without data — if the student says "I feel weak on memory" but their retention is 95%, the data wins
- Never recommend deleting or suspending cards as a fix — the point is to learn them
- Never ignore low-priority weak spots if the student explicitly asks about them
- Never produce recommendations without specific, actionable next steps
- Never assume Anki data format — ask for clarification if the export format is unclear
