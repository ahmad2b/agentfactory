# Assessment Architect - User Interaction Workflow

## Step-by-Step Flow

### 1. User Input
```
User: "Generate exam for Chapter 5"
```

### 2. Skill: Scope Discovery
```
✓ Parsed: Chapter 5
✓ Found: 19 lessons
✓ Path: 02-AI-Tool-Landscape/05-claude-code-features-and-workflows/

Discovered lessons:
  1. 01-origin-story.md
  2. 02-installation-and-authentication.md
  3. 03-free-claude-setup.md
  ... (16 more)
```

### 3. Skill: Content Classification
```
✓ Analyzed: 19 lessons
✓ Content type: MIXED
  - Procedural: 42% (8 lessons)
  - Coding: 32% (6 lessons)
  - Conceptual: 26% (5 lessons)

✓ Estimated concepts: 95 (19 lessons × 5 concepts/lesson)
```

### 4. Skill: Calculate Recommendation
```
✓ Recommended questions: 95 questions
  - Time per question: ~1.0 min (mixed content)
  - Estimated time: 95 minutes (1.6 hours)
  - Maximum time: 125 minutes (2.1 hours, capped at 3hrs)
```

### 5. **ASK USER** (AskUserQuestion Tool)

```
╔════════════════════════════════════════════════════════════╗
║ Assessment Configuration                                   ║
╚════════════════════════════════════════════════════════════╝

Question 1: Question Count
┌────────────────────────────────────────────────────────────┐
│ Accept recommended 95 questions (1.6 hrs estimated)?        │
│                                                             │
│ ○ Accept 95 questions (est. 95 min / 2 hrs max)           │
│ ○ More challenging: 110 questions (est. 110 min / 2.5 hrs)│
│ ○ Quick assessment: 60 questions (est. 60 min / 1.5 hrs)  │
│ ○ Other (enter custom: 25-120)                             │
│                                                             │
│ 📝 Note: Min 25, Max 120 questions. Larger scopes          │
│    generate automatically up to 120.                        │
└────────────────────────────────────────────────────────────┘

Question 2: Output Format
┌────────────────────────────────────────────────────────────┐
│ Which format do you prefer?                                 │
│                                                             │
│ ○ DOCX (Professional document, recommended)                │
│ ○ Markdown (Easy to version control & edit)                │
│ ○ PDF (Printable)                                          │
└────────────────────────────────────────────────────────────┘
```

### 6. User Responds
```
User chooses:
✓ Question count: 110 questions (more challenging)
✓ Format: DOCX
```

### 7. Skill: Adaptive Distribution Selection
```
✓ Selected distribution: MIXED (balanced across content types)
✓ Question breakdown:
  - Precision Recall: 11 questions (10%)
  - Conceptual Distinction: 16.5 → 16 questions (15%)
  - Decision Matrix: 13.75 → 14 questions (12.5%)
  - Architecture Analysis: 13.75 → 14 questions (12.5%)
  - Specification Design: 11 questions (10%)
  - Critical Evaluation: 13.75 → 14 questions (12.5%)
  - Strategic Synthesis: 11 questions (10%)
  - Research Extension: 8.25 → 8 questions (7.5%)
  - Economic/Quantitative: 11 questions (10%)
  Total: 110 questions ✓
```

### 8. Skill: Generate Questions (AI)
```
Generating 110 questions from Chapter 5 content...

Q1 (Precision Recall): What year was Claude Code first released?
Q2 (Conceptual Distinction): Distinguish between scope and lesson files...
... (108 more questions)

✓ Generated: 110 questions with explanations
```

### 9. Skill: Validate & Remediate
```
Running bias detection...

✓ Structure: PASS (110 questions, 4 options each)
✓ Answer Distribution: PASS (A: 24%, B: 26%, C: 25%, D: 25%)
  - Position bias detected: FIXED using sequence C
✓ Length Balance: PASS (all options within ±3 words)
✓ Difficulty Distribution: PASS (Bloom levels represented)
✓ Specificity Balance: PASS (8 questions flagged for review)

Overall: PASS (with minor flags for manual review)
```

### 10. Skill: Format & Deliver
```
✓ Formatting as DOCX...
✓ Document structure:
  - Title: "Assessment: Chapter 5 - Claude Code Features"
  - Metadata: 110 questions, est. 110 min / max 2.5 hrs
  - Questions section (no answers visible)
  - Answer Key (at end)
  - Explanations (with source references)

✓ File: exam-chapter-5-claude-code.docx
✓ Ready to download/share
```

---

## Key User Interactions

### Time Estimation Logic

```
Formula: time_per_question = {
  "conceptual": 1.2 min/question,
  "procedural": 1.1 min/question,
  "coding": 1.3 min/question,
  "mixed": 1.0 min/question
}

Estimated time = question_count × time_per_question
Max time = min(estimated + 30 min buffer, 180 min / 3 hours)

Example:
  - 95 questions (mixed) = 95 × 1.0 = 95 min (1.6 hrs)
  - Max allowed = min(125 min, 180 min) = 125 min (2.1 hrs)
```

### Question Count Options

```
Default recommendation: Auto-calculated (90-120 range)

Presets offered:
- Conservative: 60% of recommended
- Recommended: 100% (default)
- Comprehensive: 115% of recommended
- Custom: User enters 25-120

All options capped at 120 maximum
```

### Format Options

```
DOCX (Default):
  - Professional formatting
  - Uses existing docx skill
  - Printable
  - Shareable

Markdown:
  - Version control friendly
  - Easy to edit
  - Light weight
  - Can be converted to DOCX later

PDF:
  - Printable
  - Read-only (good for distribution)
  - Generated from markdown via docx
```

---

## Example Question Count Calculations

| Scope | Lessons | Concepts | Recommended | Est. Time | Max Time |
|-------|---------|----------|-------------|-----------|----------|
| Small lesson | 1 | 5 | 5 | 5 min | 35 min |
| Medium lesson | 3 | 15 | 15 | 15 min | 45 min |
| Chapter 5 | 19 | 95 | 95 | 95 min | 125 min |
| Part 2 | 37 | 185 | 120 (capped) | 120 min | 180 min |
| Large part | 50+ | 250+ | 120 (capped) | 120 min | 180 min |

---

## Configuration

All calculations configurable in `scripts/config.py`:
- `MIN_QUESTIONS`: 25
- `MAX_QUESTIONS`: 120
- `MAX_TIME_MINUTES`: 180 (3 hours)
- `TIME_PER_QUESTION`: {conceptual: 1.2, ...}
- `CONCEPTS_PER_LESSON`: 5 (for estimation)
