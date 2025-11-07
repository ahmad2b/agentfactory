---
description: Create Python chapter spec, plan, tasks with AI-native learning pedagogy. Students learn concepts through AI partnership, not syntax memorization.
---

# Python Chapter: AI-Native Learning Workflow

Create specification → plan → tasks for Python chapters (12-29) using **AI-native pedagogy**: students think through problems *with* AI as reasoning partners.

## AI-Native Learning Principle

Students don't memorize syntax. They:
1. **Understand the concept** (plain language)
2. **See minimal code** (what it does)
3. **Ask their AI** (explore through dialogue)
4. **Extract insight** (connect to reasoning)

Result: Portable thinking skills, not syntax cargo cult.

---

## Teaching Pattern (Every Concept)

```markdown
## 1. [Concept Name] — [Why it matters]

**What it is:**
Plain-language explanation (2-3 sentences).

### 💻 Code Idea

\`\`\`python
# Minimal code showing the concept
# Focus on WHAT it does
\`\`\`

### 🤖 Think With Your AI

> "What does this do?"
>
> "What changes if we...?"
>
> "How would you use this to...?"

### 🧠 The Reasoning Pattern

[Why this concept matters for thinking, not just coding]
```

**Example:**

```markdown
## 1. Variables — Storing Data

**What it is:**
A variable names a value so your program can remember it.

### 💻 Code Idea

\`\`\`python
name = "Alex"
score = 95
\`\`\`

### 🤖 Think With Your AI

> "Why do we need variables instead of just using 95?"
>
> "What breaks if we forget to name a value?"
>
> "How do AI agents use variables to track context?"

### 🧠 The Reasoning Pattern

Programs need memory. Variables let you say "remember this as X"—
exactly how reasoning chains in AI maintain state.
```

---

## Python Standards (Chapters 12-29)

**Version:** 3.13+
**Syntax:** f-strings only, match/case (17+), modern types (`list[int]`, `X | None`)
**Type hints:** None (Ch 13) → Gradual (14-26) → Mandatory (27+)

**Security (non-negotiable):**
- ❌ No `eval()`, `shell=True`, hardcoded secrets
- ✅ Environment variables, input validation, modern patterns

---

## Automated Workflow: Spec → Plan → Tasks

### EXECUTION LOGIC

**Step 1: Validate chapter number**
```
Extract from $ARGUMENTS: chapter number (12-29)
If invalid → error, exit
```

**Step 2: Ask user context questions**
```
1. Any existing teaching materials to incorporate?
2. Target audience: beginner/professional/founder?
3. Real problems students should solve?

Wait for user response(s)
```

**Step 3: AUTO-EXECUTE Phase 1 (Specification)**
```
→ Run: /sp.specify part-5-chapter-${N}
→ Pass context from Step 2 to specification command
→ User approves spec before next phase
→ Output: specs/part-5-chapter-${N}/spec.md
```

**Step 4: AUTO-EXECUTE Phase 2 (Planning)**
```
→ Run: /sp.plan
→ Input: Approved spec.md from Step 3
→ Generate lesson-by-lesson breakdown
→ Add CEFR proficiency levels per lesson
→ Define AI prompt templates for each concept
→ User approves plan before next phase
→ Output: specs/part-5-chapter-${N}/plan.md
```

**Step 5: AUTO-EXECUTE Phase 3 (Tasks)**
```
→ Run: /sp.tasks
→ Input: Approved spec.md + plan.md
→ Generate implementation checklist
→ Include AI prompt testing tasks
→ Include security validation tasks
→ User approves tasks before implementation
→ Output: specs/part-5-chapter-${N}/tasks.md
```

**Step 6: Delivery**
```
✅ All 3 files created and approved
→ specs/part-5-chapter-${N}/spec.md
→ specs/part-5-chapter-${N}/plan.md
→ specs/part-5-chapter-${N}/tasks.md

Ready to share with implementer
```

---

## Context Gathering (Before Automation)

Ask user:

**1. Existing teaching materials?**
- Teaching notes, blog posts, videos?
- Example code or lesson outlines?
- → If yes: extract concepts, transform to AI-native structure

**2. Target audience?**
- Aspiring developer (beginner)
- Professional developer (intermediate)
- Technical founder (applied focus)
→ Informs evals and real-world examples

**3. Real problems to solve?**
- What can students build after?
- What job skills does this enable?
- → Informs success evals and learning objectives

---

## Automated Spec Generation Rules

When running `/sp.specify`, ensure:

```yaml
---
chapter: N
title: "[From chapter-index.md]"
part: 5
complexity: [A: beginner (12-16) | B: intermediate (17-23) | C: advanced (24-29)]
cefr_range: [A: A1-A2 | B: A2-B1 | C: B1-B2]
python_version: "3.13+"
---

## Success Evals (From context questions)

### Students Will Understand
- 75%+ explain concepts without code
- [Other comprehension metrics from audience]

### Students Will Do
- 80%+ use AI to execute concepts
- [Skill-based metrics]

### Students Will Build
- [From "real problems" question]
- Complete capstone project using AI

## Learning Objectives
[3-5 outcomes, testable, aligned with evals]

## Lesson Structure (Fixed for all Python chapters)
1. Core concept + foundational understanding
2. Real-world application
3. Integration and synthesis
4. Error patterns and debugging
5. Capstone: student directs, AI assists

## Concepts Taught
[List with AI-native prompt template for each]

## Acceptance Criteria
- [ ] Every concept: What it is → Code Idea → Think With AI → Reasoning Pattern
- [ ] NO "run this in REPL" instructions
- [ ] Python 3.13+ syntax in all examples
- [ ] Cognitive load: 5 (beginner) / 7 (intermediate) / 10 (advanced)
- [ ] Pedagogy emphasizes thinking over syntax
```

---

## Output Files

```
specs/part-5-chapter-${N}/
  spec.md   (Spec with AI-native pedagogy)
  plan.md   (Lesson plan with prompt specs)
  tasks.md  (Implementation checklist)
```

---

## Key Differences: AI-Native Pedagogy

| Traditional | AI-Native |
|-------------|-----------|
| "Here's the syntax" | "Here's the concept" |
| Memorize patterns | Think with AI partner |
| "Run this command" | "Ask AI what this does" |
| Syntax → Understanding | Understanding → Syntax |
| Solo problem-solving | Collaborative reasoning |

---

## Example: Data Types

**Traditional approach:**
```
## Data Types
Python has int, str, bool, list, dict.
Use int for numbers: x = 5
Use str for text: name = "Ali"
```

**AI-native approach:**
```
## 1. Data Types — Programs Work With Different Kinds of Information

**What it is:**
Different information needs different containers.
A phone number (text), an age (number), and readiness (yes/no)
need to be stored differently.

### 💻 Code Idea

\`\`\`python
phone = "555-1234"    # Text keeps formatting
age = 25               # Numbers for math
is_ready = True        # Yes/no questions
\`\`\`

### 🤖 Think With Your AI

> "Why can't we store everything as text?"
>
> "What breaks if age is a string instead of a number?"
>
> "How does an AI agent distinguish between user ID and user name?"

### 🧠 The Reasoning Pattern

Type safety is about *semantic accuracy*—matching the representation
to the real world. AI systems depend on correct types to reason about data.
```

**Result:** Student understands *why* types exist, not just *what* they are.

---

## AI-Native Pedagogy Embedded

**Every lesson follows:**

1. **Concept First** — What problem does this solve?
2. **Minimal Code** — See it in action (don't memorize)
3. **Think With AI** — Explore through dialogue
4. **Reasoning Pattern** — Why this matters for thinking

**Never:**
- ❌ "Copy-paste this command"
- ❌ "Memorize this syntax"
- ❌ "Run this in REPL"
- ❌ "Here are all 47 options"

**Always:**
- ✅ "Why would you need this?"
- ✅ "Ask your AI what happens if..."
- ✅ "How does this help you think?"
- ✅ "What's the reasoning pattern?"

---

## Success Criteria

Workflow complete when:

**Spec:**
- Evals defined (understand, do, build)
- Concepts follow AI-native structure
- No syntax-memorization framing
- Cognitive load limits enforced

**Plan:**
- 4-6 lessons with AI prompts specified
- CEFR proficiency levels assigned
- Progressive complexity validated
- Reasoning patterns identified

**Tasks:**
- Implementation checklist specific and testable
- AI prompt testing included
- Security validated

**User approved all phases**

---

## Implementation Notes

This command is **fully automated**. When you run it:

1. **Claude Code extracts** chapter number from arguments
2. **Claude Code asks** 3 context questions (existing materials, audience, problems)
3. **Claude Code invokes** `/sp.specify` with chapter context
4. **User approves** spec.md
5. **Claude Code invokes** `/sp.plan` with approved spec
6. **User approves** plan.md
7. **Claude Code invokes** `/sp.tasks` with spec + plan
8. **User approves** tasks.md
9. **Claude Code reports** completion with all 3 files ready to share

**Result:** Full specification package ready for implementer (lesson-writer subagent)

---

## How Claude Code Implements This

```
STEP 1: Parse chapter number
├─ Extract from $ARGUMENTS
├─ Validate range 12-29
└─ Exit if invalid

STEP 2: Ask user context (3 questions)
├─ Read existing materials? (offer to paste)
├─ Target audience?
├─ Real problems to solve?
└─ Store responses for next phases

STEP 3: Execute /sp.specify (SlashCommand)
├─ Pass chapter context to /sp.specify
├─ /sp.specify creates specs/part-5-chapter-${N}/spec.md
├─ User reviews and approves spec
└─ Confirm: "Spec approved, moving to planning"

STEP 4: Execute /sp.plan (SlashCommand)
├─ Read approved spec.md
├─ Run /sp.plan with spec context
├─ /sp.plan creates specs/part-5-chapter-${N}/plan.md
├─ User reviews and approves plan
└─ Confirm: "Plan approved, moving to tasks"

STEP 5: Execute /sp.tasks (SlashCommand)
├─ Read spec.md + plan.md
├─ Run /sp.tasks with full context
├─ /sp.tasks creates specs/part-5-chapter-${N}/tasks.md
├─ User reviews and approves tasks
└─ Confirm: "Tasks approved, ready for implementation"

STEP 6: Final Report
├─ List all 3 files created
├─ Show file paths
└─ Next: "Ready for lesson-writer subagent"
```

---

## Key Points

- **Automatic execution:** SlashCommand tool invokes `/sp.specify`, `/sp.plan`, `/sp.tasks` sequentially
- **Human checkpoints:** User approves each phase before proceeding
- **Full context passed:** Each phase receives outputs from previous phase
- **AI-native pedagogy enforced:** All specs follow Concept → Code → Think → Reasoning pattern
- **Python 3.13+ mandatory:** Every generated spec includes modern syntax standards
- **Security-first:** All specs include security non-negotiables checklist

**One user command.** Full spec package. Ready to implement.

---

## Master Design Template

This command operationalizes the **Python Chapter Design Template** (`.specify/templates/book/PYTHON_CHAPTER_DESIGN_TEMPLATE.md`).

All chapters created with this command follow:
- AI-native colearning philosophy (from `preface-agent-native.md`)
- Spec-Driven Development workflow (from Chapter 31-32 patterns)
- Pedagogical standards (CEFR, Bloom's, DigComp proficiency mapping)
- Python 3.13+ best practices (modern syntax, security, type hints)
- Quality gates (technical, pedagogical, constitutional alignment)

**The template is the source of truth for chapter structure, assessment, and validation.**

**Reference it whenever:**
- Designing a new Python chapter
- Reviewing chapter specifications
- Training other orchestrators to create consistent content
- Ensuring pedagogical standards compliance