---
name: lecture-ingest
description: End-to-end pipeline for processing a new lecture. Takes a video file (or pre-existing transcript + materials), runs Whisper transcription, generates lecture summary, produces flashcards via the course-specific skill, runs coverage analysis, and generates mindmap. Use when new lecture materials arrive.
---

# Lecture Ingest Pipeline

Automates the full processing of a new lecture from raw video to study-ready materials.

---

## Pipeline Steps

```
Step 1: Whisper Transcription (skip if transcript exists)
    ↓
Step 2: Lecture Summary (lecture_summary.md only)
    ↓
Step 3: Flashcard Generation (flashcards.tsv)
    ↓
Step 4: Coverage Analysis (flashcards_supplementary.tsv if gaps)
    ↓
Step 5: Mindmap Generation (flashcard_mindmap.html)
    ↓
Step 6: Before-Starting Report (after ALL materials exist)
```

---

## Step 1: Whisper Transcription

### Pre-Check (IMPORTANT)
Before running Whisper, scan the lecture folder for existing `.txt` files. Many lectures already have pre-existing transcripts.

**Skip this step entirely if:**
- Any `.txt` file already exists in the lecture folder (regardless of filename)
- The existing transcript is non-empty (> 1 KB)

**Run this step only if:**
- No `.txt` file exists AND a video file (`.m4v`, `.mp4`, `.mov`) is present

### Command (only when needed)
```bash
whisper "[video_file]" --model small --language en --output_format txt --condition_on_previous_text False --fp16 False
```

### Output
```
[Lecture Folder]/
└── [same name as video].txt
```

---

## Step 2: Lecture Summary

### Invoke
`lecture-summary` skill with all available materials:
- Transcript (.txt) from Step 1 or pre-existing
- Lecture slides PDF (if present)
- Reading PDF (if present)

### Output
```
[Lecture Folder]/
└── lecture_summary.md
```

**Note:** `before_starting_report.md` is NOT generated here. It is generated in Step 6, after flashcards, supplementary cards, and mindmap all exist. The before-starting report needs full knowledge of the final card set.

---

## Step 3: Flashcard Generation

### Course Detection
Determine which course this lecture belongs to dynamically:
1. Identify the parent course folder from `courses/`
2. Scan `skills/flashcard-generators/` for `.md` files
3. Read each skill's frontmatter `description` to find the one that matches this course
4. If no match is found, ask the user which skill to use — or fall back to `flashcard-generator.md` central rules only

### Invoke
The appropriate course-specific flashcard skill from `skills/flashcard-generators/`.

### Input
All available materials:
- Transcript (.txt)
- Slides PDF
- Reading PDF (if present)
- RMD files (for AA Statistics)
- PPTX files (for AA Statistics)

### Output
```
[Lecture Folder]/
└── Flashcards/
    └── flashcards.tsv
```

---

## Step 4: Coverage Analysis

### Invoke
`flashcard-coverage-checker` skill with:
- Source materials (transcript, slides, reading PDF)
- Generated `flashcards.tsv` from Step 3

### Output (conditional)
If gaps are found:
```
[Lecture Folder]/
└── Flashcards/
    └── flashcards_supplementary.tsv
```

If no gaps: no file produced. The analysis is done silently.

---

## Step 5: Mindmap Generation

### Invoke
`mindmap-generator` skill with:
- `flashcards.tsv` (and `flashcards_supplementary.tsv` if it exists)
- Source materials for writing context descriptions
- `lecture_summary.md` for concept relationships

### Output
```
[Lecture Folder]/
└── Flashcards/
    └── flashcard_mindmap.html
```

---

## Step 6: Before-Starting Report

### Why Last?
The before-starting report is the most comprehensive output. It needs to know:
- What the lecture covers (from lecture_summary.md)
- What flashcards exist (from flashcards.tsv + supplementary)
- What gaps were found and filled (from coverage analysis)
- How concepts are structured (from the mindmap grouping)
- What the exam format looks like (from the course-specific skill)

Generating it before all this exists produces a shallow, incomplete report.

### Invoke
`lecture-summary` skill's before-starting report section, with ALL generated materials as input:
- `lecture_summary.md` (from Step 2)
- `flashcards.tsv` (from Step 3)
- `flashcards_supplementary.tsv` (from Step 4, if exists)
- `flashcard_mindmap.html` (from Step 5 — for concept grouping structure)
- The course-specific flashcard skill (for exam format)
- Source materials (transcript, slides)

### Output
```
[Lecture Folder]/
└── Flashcards/
    └── before_starting_report.md
```

---

## Final State

After the full pipeline, the lecture folder looks like:

```
[Date] - Lecture [N]/
├── [video].m4v                              ← original (untouched)
├── [video].txt                              ← Step 1: whisper transcript
├── [slides].pdf                             ← original (untouched)
├── [reading].pdf                            ← original (if exists, untouched)
├── lecture_summary.md                       ← Step 2: comprehensive summary
└── Flashcards/
    ├── flashcards.tsv                       ← Step 3: main flashcards
    ├── flashcards_supplementary.tsv         ← Step 4: gap-filling cards (if needed)
    ├── flashcard_mindmap.html              ← Step 5: interactive mindmap
    └── before_starting_report.md            ← Step 6: comprehensive study guide
```

---

## Error Handling

- If Whisper fails → report the error, skip to Step 2 if a transcript already exists
- If no slides PDF exists → proceed with transcript only, note reduced coverage
- If the course cannot be detected → ask the user which flashcard skill to use
- If coverage checker finds no gaps → skip supplementary file, proceed to mindmap

---

## Usage

The user triggers this pipeline by saying:
- "New lecture arrived, process it"
- "Ingest Lecture 8"
- "Run the pipeline on this folder"
- Or any equivalent request to process a new lecture's materials

The pipeline runs all 5 steps sequentially. Each step's output feeds the next.

---

## What NOT to Do

- Never skip Step 2 (summary) — the before-starting report is essential for study orientation
- Never run Step 5 (mindmap) without flashcards — the mindmap requires card data
- Never modify original files (video, PDF, reading PDF)
- Never produce output outside the lecture folder structure defined above
- Never run the pipeline on an empty folder — at minimum, a video or transcript must exist
