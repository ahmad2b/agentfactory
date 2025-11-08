---
description: Create Python chapters (12-29) using AIDD thinking. Students learn Python through AI partnership, specification-first mindset, validation-first practice.
---

# Python Chapter Workflow: Learning Programming Through AIDD Lens

Chapters 12-29 teach Python as a language **using AIDD principles** (from Part 1-2) applied to real code.

📖 **SAMPLE INPUT TEMPLATE**: See `.claude/commands/sp.python-chapter.SAMPLE_INPUT.md` for example invocations and responses.

⚠️ **KEY PRINCIPLES**:
- ✅ **AIDD-First**: Reinforce specification-first thinking, validation-first practice from Chapters 1-11
- ✅ **No SDD Yet**: Don't mention Spec-Driven Development (taught later in Part 6)
- ✅ **Honors User Intent**: Ask what audience/scope; never override
- ✅ **Minimal Scope**: Respect "core focus"—depth over breadth
- ✅ **Beginner-Appropriate**: 5 concepts max (chapters 12-16), 7 max (chapters 17-23), 10 max (chapters 24-29)

## AI-Native Learning Principle

Students don't memorize syntax. They:
1. **Understand the concept** (plain language)
2. **See minimal code** (what it does)
3. **Ask their AI** (explore through dialogue)
4. **Extract insight** (connect to reasoning)

Result: Portable thinking skills, not syntax cargo cult.

## 🧠 The Goal

In traditional programming classes, students often get lost memorizing syntax.
In the AI-driven classroom, our goal is different — we learn **concepts first**, then use **Claude Code** or **Gemini CLI** to generate, explain, and refine Python syntax *with understanding*.

You will **think in logic**, not just in code.

We’ll explore three foundational ideas:

1. Loops (repetition)
2. Conditionals (decision-making)
3. Functions (modular thinking)

For each, you’ll see:

* A plain-language concept explanation
* A Python example
* A colearning prompt for your AI assistant

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

## Workflow: Design Python Chapter Using AIDD Thinking

### EXECUTION LOGIC

**Step 1: Validate and Anchor on Chapter**
```
Extract from $ARGUMENTS: chapter number (12-29)

Read specs/book/chapter-index.md:
→ Validate chapter exists in Part 5 (Chapters 12-29)
→ Extract exact chapter title (this is your ANCHOR)
→ Understand chapter position (what comes before/after)

If chapter invalid → error, exit
```

**Step 2: Check for Existing Context**
```
Look in context/13_chap12_to_29_specs/:
→ Find materials matching this chapter (Lesson files, guides, examples)
→ Identify relevant pedagogical patterns
→ Note useful code examples
→ Understand learning outcomes already identified
→ Extract only what fits THIS chapter's scope

DO NOT include materials from other chapters' lessons
```

**Step 3: Ask User to Confirm Scope**
```
With chapter title as anchor:

1. Target audience? (beginner/intermediate/advanced)
   → Determines complexity tier

2. Core focus for THIS chapter? (pick ONE concept family)
   → What should students understand?
   → What fits the chapter title?
   → Don't add concepts from other chapters

3. What will students BUILD after? (testable project)
   → One real outcome students can demonstrate
   → Must fit this chapter's scope

4. From context materials, which aspects to use?
   → Existing lesson structures?
   → Code examples?
   → Real-world projects?
   → Or start fresh?

→ Honor answers; never override
→ Never let context or scope drift beyond chapter title
```

**Step 4: Design Chapter Using AIDD Principles**
```
With anchored title + user intent + context insights:

→ Create lesson outline (2-4 lessons matching THIS chapter's focus)
→ Design each lesson around AIDD pattern:
   1. What it is (concept explanation)
   2. Code idea (minimal example)
   3. Try it (student builds with concept)
   4. Why it matters (connection to AIDD thinking)
→ Verify all concepts are IN this chapter (not future chapters)
→ Identify validation points (how to test understanding)
→ Plan AI prompts students will use
→ Use Python 3.13+ docs to verify accuracy
```

**Step 5: Generate Design Artifacts**
```
Create in specs/part-5-chapter-${N}/:

→ spec.md
  - Chapter title and position
  - Learning objectives (testable, realistic)
  - Concepts taught (count: 5 for beginner, 7 for intermediate, 10 for advanced)
  - Lesson structure
  - Success criteria (evals before specs)
  - Prerequisites (only Chapters 1-${N-1})
  - NO forward references (no Ch 30+, no SDD)

→ plan.md
  - Detailed lesson breakdown (2-4 lessons)
  - Code examples with pedagogical purpose
  - AI prompts for each lesson
  - Assessment points (how students validate)

→ tasks.md
  - Implementation checklist
  - Acceptance criteria for each lesson
  - Validation steps
```

**Step 6: Delivery**
```
✅ All 3 files created with AIDD thinking
→ specs/part-5-chapter-${N}/spec.md (what students learn in THIS chapter)
→ specs/part-5-chapter-${N}/plan.md (how to teach THIS chapter)
→ specs/part-5-chapter-${N}/tasks.md (tasks to implement THIS chapter)

CRITICAL VALIDATION:
□ All concepts belong in THIS chapter (not future chapters)
□ No prerequisite violations (only use Chapters 1-${N-1})
□ Chapter title matches chapter-index.md exactly
□ Scope matches user intent (never overridden)
□ Context was mined for insights, not allowed to expand scope
□ Ready for lesson writer
```

---

## Phase 0: Context Gathering (AIDD-Style Design)

**Apply AIDD principle 1: Specification-First**

We're designing the chapter by understanding WHO we're teaching and WHAT they need to build — not by assuming what they should learn.

### Inline Context Input (Optional but Recommended)

You can provide context directly in your prompt. Format:

```
/sp.python-chapter 13

[Optional: Inline Context Below]

Write Chapter 13: Introduction to Modern Python in Part 4

Core Context & Guiding Philosophy (Apply to entire chapter):

This chapter must reflect:
- AI-Driven Learning: Students use AI coding partners (Claude Code, Gemini CLI)
- Focus on reasoning and problem-solving, not syntax memorization
- AIDD principles: specification-first thinking, validation-first practice
- Real Python 3.13+ features and best practices

Existing Teaching Materials:
@context/13_chap12_to_29_specs/Lesson_01_Introduction_to_Python.md
- Learning outcomes already identified
- Code examples and teaching patterns
- "Try It" exercises framework

Additional Guidance:
- Target absolute beginners (no coding experience)
- Keep it short (don't overwhelm)
- Focus on fundamentals only
```

**How the command processes inline context:**

If you provide inline context:
1. Extract the chapter number from your prompt (13)
2. Read chapter-index.md Quick Lookup for exact title
3. Parse your inline context for:
   - Core philosophy and guiding principles
   - Existing teaching materials references
   - Additional guidance for this chapter
   - Learning outcomes or scope hints
4. Use this context to inform the questions
5. Proceed with Step 1 below

If you don't provide inline context:
1. Command asks you the 4 questions directly
2. You provide context via your responses
3. Same workflow, just interactive

---

**Step 1: Anchor on Chapter from chapter-index.md**
```
Read specs/book/chapter-index.md, Part 5 Quick Lookup (Chapters 12-29):
→ Extract EXACT chapter title from Quick Lookup (your ANCHOR)
→ Validate chapter number (12-29)
→ Note chapter position (prerequisites from Chapters 1-${N-1})
→ Understand chapter scope from title

Quick Lookup Reference (from chapter-index.md):
  ch13: "Introduction to Python"
  ch14: "Data Types"
  ch15: "Operators, Keywords, and Variables"
  ch17: "Control Flow and Loops"
  ch20: "Module and Functions"
  (See chapter-index.md Part 5 Quick Lookup for all 18 chapters)

Example for Chapter 13:
  Title: "Introduction to Python" (from Quick Lookup)
  After: Chapter 12 (Python UV package manager)
  Before: Chapter 14 (Data Types)
  Prerequisites: Chapters 1-12 (AIDD thinking + tools)
```

**Step 2: Process Inline Context (if provided)**
```
If user provided inline context in prompt:
→ Parse core philosophy (what should students understand?)
→ Extract guiding principles (AI-Driven Learning, AIDD, etc.)
→ Identify material references (@context/... locations)
→ Note additional guidance (audience, scope hints)
→ Use this to inform your questions and suggestions

If NO inline context:
→ Proceed directly to Step 3 (ask user)
```

**Step 3: Check Context for This Chapter**
```
Look in context/13_chap12_to_29_specs/ (if not provided inline):
→ Find lesson files matching THIS chapter only
→ Extract pedagogical insights that fit the title
→ Note useful code examples and teaching patterns
→ Identify learning outcomes already developed
→ Respect chapter scope (don't pull in other chapters' lessons)

CRITICAL: Never cross chapter boundaries
  - Extract Ch 13 context for Ch 13 chapter design
  - Ignore Ch 14, 15, etc. materials
  - Ignore lessons from Ch 12 (already taught)
```

**Step 4: Selective Context Extraction (CRITICAL)**

**WHEN CHAPTER SCOPE IS SPECIFIC, FILTER CONTEXT RUTHLESSLY:**

Example 1: Chapter 13 is "Introduction to Python"
```
Context contains:
  ✅ "What is Python?" → USE (intro concept)
  ✅ "Your first program" → USE (intro outcome)
  ✅ "How to run code" → USE (intro skill)
  ✅ "Variables basics" → MAYBE (depends on scope)
  ❌ "Functions" → SKIP (Ch 20 topic)
  ❌ "Classes" → SKIP (Ch 24+ topic)
  ❌ "Async/await" → SKIP (Ch 28 topic)
  ❌ "Type hints" → SKIP (advanced, not intro)
```

Example 2: Chapter 17 is "Control Flow and Loops"
```
Context contains:
  ✅ "if/elif/else statements" → USE (chapter focus)
  ✅ "for loops" → USE (chapter focus)
  ✅ "while loops" → USE (chapter focus)
  ✅ "break/continue" → USE (loop control)
  ❌ "Functions" → SKIP (Ch 20 topic)
  ❌ "List comprehensions" → SKIP (advanced, separate concept)
  ❌ "Recursion" → SKIP (advanced control flow)
  ❌ "Exception handling" → SKIP (Ch 21 topic)
```

Example 3: Chapter 20 is "Module and Functions"
```
Context contains:
  ✅ "Defining functions" → USE (chapter focus)
  ✅ "Parameters and arguments" → USE (chapter focus)
  ✅ "Return values" → USE (chapter focus)
  ✅ "Variable scope" → USE (function scope)
  ✅ "Modules/imports" → USE (chapter focus)
  ❌ "Decorators" → SKIP (advanced, separate concept)
  ❌ "Lambda functions" → SKIP (advanced, separate concept)
  ❌ "Generators" → SKIP (Ch 28+ topic)
  ❌ "Async functions" → SKIP (Ch 28 topic)
```

**DECISION RULE:**
```
IF context concept fits THIS chapter's title → EXTRACT
IF context concept belongs to Ch N+1 or later → SKIP
IF context concept is "advanced variation" of this chapter → SKIP
IF context concept requires prerequisites from future chapters → SKIP
IF context concept is tangential (not core focus) → SKIP
```

**Step 5: Extract and Filter Context (Extract Relevant Aspects)**
1. Chapter title defines the target (your ANCHOR)
2. Extract pedagogical insights that fit THIS chapter ONLY
3. Identify useful code examples relevant to chapter scope
4. Note learning outcomes already identified
5. Understand prerequisites (only Chapters 1-${N-1})
6. **RUTHLESSLY IGNORE everything outside this chapter's scope**
7. **Filter functions/classes/advanced concepts even if in context**
8. **Never let context expand scope beyond chapter title**

**ASK USER (honor their answers, never override):**

**Q1: Who are we teaching?**
Pick ONE audience:
- **Absolute beginner** (no coding; might fear Python)
- **Beginner with some coding** (tried JavaScript or similar)
- **Intermediate** (comfortable with basics; wants depth)

→ This determines complexity tier (A1/A2/B1)

**Q2: What's the ONE core focus for THIS chapter?**
Pick ONE concept family (don't add extras, don't cross chapter boundaries):
- For Ch 13: Just intro concepts and basic syntax?
- For Ch 14: Data types focus?
- For Ch 17: Control flow and loops?
- [Always: What fits THIS chapter's title from chapter-index.md?]

→ This determines scope (5/7/10 concepts max for THIS chapter)
→ NEVER include concepts from other chapters (Ch 14+)

**Q3: What can students actually BUILD after THIS chapter?**
(Make it testable — they'll validate understanding this way)
- Something using THIS chapter's concepts only
- Don't require concepts from future chapters
- Real outcome students can demonstrate
- [Or: from context, describe specific project]

→ This determines learning objective (real outcome for THIS chapter)

**Q4: From context materials, which aspects fit THIS chapter?**
- Existing lesson structures (for THIS chapter only)?
- Code examples (relevant to THIS chapter)?
- Real-world projects (achievable with THIS chapter alone)?
- Or start fresh?

→ We'll extract from context/13_chap12_to_29_specs/ what fits
→ Ignore lessons from other chapters
→ Never let context expand scope beyond chapter title

**CRITICAL WORKFLOW**:
1. Chapter title from chapter-index.md is the ANCHOR (never deviate)
2. Respect chapter boundaries (don't pull in future chapters)
3. Honor user's stated intent (audience, scope, outcome)
4. Extract relevant insights from THIS chapter's context
5. Use Python docs + AI intelligence for teaching approach
6. Never let context override user's explicit answers
7. Design optimal AIDD-powered Python learning FOR THIS CHAPTER

---

## Example: Inline Context Input for Chapter 13

### What You Type:
```
/sp.python-chapter 13

Write Chapter 13: Introduction to Modern Python in Part 4 of the book.

Core Context & Guiding Philosophy (Apply to entire chapter):

This chapter must be written as part of a modern AIDD Programming era designed
for the AI-Driven Development Era. The content must reflect this core philosophy:

AI-Driven Learning: Assume students are using Agentic Coding Assistants
(like Gemini CLI or Claude Code) as their primary coding partners. The focus
must be on reasoning and problem-solving, not on syntax memorization.

Specification-First Mindset: Students should learn to clarify what they want
BEFORE writing code.

Validation-First Practice: Students learn to test their understanding, not
just memorize syntax.

Existing Teaching Materials:
@context/13_chap12_to_29_specs/Lesson_01_Introduction_to_Python.md
@context/13_chap12_to_29_specs/Lesson_01_Introduction_to_Python.ipynb

These materials provide:
- Learning outcomes already identified
- Code examples and teaching patterns
- "Try It" exercises framework
- Student assessment approaches

Additional Guidance:
- Target: Absolute beginners (no coding experience)
- Complexity: Keep it focused (don't overwhelm)
- Scope: Introduction fundamentals only (not data types — that's Ch 14)
- Length: 3-4 lessons maximum
```

### What the Command Does:

1. **Extracts chapter number**: 13
2. **Reads chapter-index.md**: Gets "Introduction to Python" (ANCHOR)
3. **Parses inline context**:
   - Philosophy: AI-Driven Learning + AIDD thinking
   - Materials: Lesson_01_Introduction_to_Python (md + ipynb)
   - Guidance: Absolute beginners, 3-4 lessons, fundamentals only
4. **Validates boundaries**: Confirms no Ch 14 (Data Types) concepts
5. **Prepares questions** informed by your context
6. **Asks user** the 4 questions (with your context already in mind)
7. **Generates** spec/plan/tasks respecting your guiding philosophy

### Minimal Inline Context (Also Works):

```
/sp.python-chapter 13

Core Philosophy: AI-Driven Learning (use Claude Code/Gemini CLI as partners)
Target Audience: Absolute beginners
Scope: Introduction fundamentals only
Materials: @context/13_chap12_to_29_specs/Lesson_01_Introduction_to_Python.md
```

Command will:
- Read the core philosophy
- Know the target audience
- Understand the scope
- Reference the materials
- Ask questions informed by this context

### No Inline Context (Also Works):

```
/sp.python-chapter 13
```

Command will:
- Ask you all 4 questions interactively
- You provide context via your responses
- Same result, just different input method

---

## Using Python Docs + AI Intelligence for Design

**When designing the chapter:**

1. **Python Docs** (authoritative source)
   - Verify current Python 3.13+ syntax
   - Check official best practices
   - Understand language features accurately

2. **AI Intelligence** (pedagogical design)
   - Create explanations that work for target audience
   - Find real-world examples and use cases
   - Design progression from simple → complex
   - Generate code examples that demonstrate concepts
   - Create exercises that build toward final project

3. **AIDD Thinking** (learning approach)
   - Specification-first: Explain the problem before the code
   - Validation-first: How students test their understanding
   - AI-partnership: What students ask their AI to explore
   - Real outcomes: What they actually build

---

## Phase 1: Design Specification (AIDD-Driven)

**Apply AIDD principle 2: Specification-Driven**

Create spec.md describing the CHAPTER DESIGN (not a formal SDD spec yet—we don't teach that until Part 6).

This spec answers: "What will students learn? Why? How will they know they learned it?"

**Use Python docs for accuracy. Use AI intelligence for pedagogy. Use AIDD thinking for the learning model.**

```yaml
---
chapter: N
title: "[From chapter-index.md - exact]"
part: 5
target_audience: "[From user answer - EXACT, don't override]"
core_focus: "[From user answer - EXACT, don't add extras]"
complexity: "[beginner|intermediate|advanced based on audience]"
python_version: "3.13+"
---

## Success Criteria (From User Input)

### Students Can BUILD
[From user answer to "What can they build?"]

### Students Understand
[3-5 concepts ONLY - matching user's "core focus" answer]
[VALIDATE: Total concepts ≤ 5 for beginner, ≤7 for intermediate, ≤10 for advanced]

### VALIDATION: Chapters 30+ (SDD) Not Mentioned; AIDD Already Taught
✅ Does this mention Chapters 30+ or SDD? NO
✅ Does this reinforce AIDD concepts (Ch 1-11)? YES, when relevant
✅ Does this mention unknown methodologies? NO

**What this means**:
- ❌ Don't forward-reference SDD (it's not taught until Part 6)
- ✅ DO reinforce AIDD: "Apply specification-first thinking..."
- ✅ DO reinforce validation-first: "Test your code before shipping..."
- ✅ Connect Python to AIDD: "Remember the nine pillars? They apply to functions too..."

## Prerequisites
[Only chapters that come BEFORE this one]

## Learning Objectives
[3-5 SMART objectives using ONLY concepts taught in chapters 1-N]

## Content Structure

### Lesson 1: [Topic from core focus]
Lesson duration: 15-20 min (beginner), 25-30 min (intermediate)
Concepts: [1-2 from the list above]
Code examples: [1-2 simple examples]
Student activity: [Build something small with Concept 1]

### Lesson 2: [Topic from core focus]
[Same structure]

### Lesson 3: [Topic from core focus - ONLY if in scope]
[Same structure - DON'T add lessons beyond user's scope]

## TOTAL CONCEPTS TAUGHT
[Count them. Verify ≤ tier limit]

## Acceptance Criteria
- [ ] Scope matches user's "core focus" answer EXACTLY
- [ ] Target audience matches user answer (NOT overridden)
- [ ] Zero forward references (no Chapter 30+, no SDD, no methodology)
- [ ] Concept count ≤ tier limit (5/7/10)
- [ ] Each lesson 15-35 min
- [ ] Python 3.13+ syntax
- [ ] Students can actually build the promised project
```

---

## Phase 2: Lesson Plan (AIDD-Driven)

**Apply AIDD principle 3: Quality-Gated Design**

Create plan.md describing HOW we'll teach each concept (lesson by lesson).

For each lesson:
- What concept(s) it teaches
- The AIDD learning pattern: What → Code → Try → Why
- AI prompts students will use
- How students validate understanding

## Phase 3: Implementation Tasks (MINIMAL, NO CLUTTER)

Create ONLY:
```
specs/part-5-chapter-${N}/
  spec.md   (What students learn + success criteria)
  plan.md   (How we teach it, lesson by lesson)
  tasks.md  (Implementation checklist for content writer)
```

**DO NOT CREATE:**
- ❌ index.md
- ❌ _templates/ directory
- ❌ _assets/ directory
- ❌ _code-examples/ directory
- ❌ lesson-template.md
- ❌ capstone-rubric.md
- ❌ Any scaffolding beyond these 3 files

**Minimal structure = cleaner projects, no clutter.**

---

## How Python Chapters Teach Through AIDD Lens

| Traditional Programming Teaching | AIDD-First Python Learning |
|-----------------------------------|---------------------------|
| "Memorize Python syntax" | "Understand concepts first, then use code as a tool" |
| "Here's all 47 string methods" | "Here's what you need; your AI shows how when needed" |
| Syntax-first (memorize, then apply) | Understanding-first (understand, then code) |
| Solo manual coding | Partnered reasoning with AI |
| Code-first (write, debug, test) | Specification-first (clarify intent, then code) |
| "Read the documentation" | "Ask your AI to explain and explore" |

**Result**: Students learn AIDD mindset in practice. They think problems through, partner with AI to solve them, validate the solution. This builds **transferable thinking** instead of syntax memorization.

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

## ORCHESTRATED WORKFLOW: Full SpecKit Plus Loop

This command **fully automates** the SpecKit Plus SDD workflow (Spec → Plan → Tasks → Implement).

### Execution Flow

When you run `/sp.python-chapter [N]`:

**PHASE 0: CONTEXT GATHERING**
```
1. Parse chapter number from [N]
2. Validate chapter range (12-29) and read chapter-index.md
3. Ask user 4 clarifying questions:
   - Who are we teaching? (audience)
   - What's the core focus for THIS chapter? (scope)
   - What can students BUILD? (outcome)
   - Which context aspects fit THIS chapter? (materials)
4. Store all responses for next phases
```

**PHASE 1: SPECIFICATION** (Automated)
```
→ Invoke: /sp.specify [chapter-context]
  ├─ Pass all user answers + chapter title
  ├─ /sp.specify creates: specs/part-5-chapter-[N]/spec.md
  └─ Report: "Spec created. Review and confirm to proceed."

WAIT: User reviews spec.md
→ User confirms: "Spec approved" or provides feedback
  ├─ If feedback: Update spec.md, then proceed
  └─ If approved: Continue to PHASE 2
```

**PHASE 2: PLANNING** (Automated)
```
→ Invoke: /sp.plan [spec-context]
  ├─ Read: specs/part-5-chapter-[N]/spec.md
  ├─ /sp.plan creates: specs/part-5-chapter-[N]/plan.md
  └─ Report: "Plan created. Review and confirm to proceed."

WAIT: User reviews plan.md
→ User confirms: "Plan approved" or provides feedback
  ├─ If feedback: Update plan.md, then proceed
  └─ If approved: Continue to PHASE 3
```

**PHASE 3: TASKS** (Automated)
```
→ Invoke: /sp.tasks [spec+plan-context]
  ├─ Read: specs/part-5-chapter-[N]/spec.md + plan.md
  ├─ /sp.tasks creates: specs/part-5-chapter-[N]/tasks.md
  └─ Report: "Tasks created. Review and confirm to proceed."

WAIT: User reviews tasks.md
→ User confirms: "Tasks approved" or provides feedback
  ├─ If feedback: Update tasks.md, then proceed
  └─ If approved: Continue to PHASE 4 (optional)
```

**PHASE 4: IMPLEMENTATION** (Optional)
```
→ Option 1: Invoke lesson-writer subagent
  ├─ Pass: spec.md + plan.md + tasks.md
  ├─ lesson-writer creates: Lesson content files (01-lesson-1.md, etc.)
  └─ Report: "Implementation complete. Ready for validation."

→ Option 2: Manual implementation
  └─ User implements lessons manually using tasks.md as guide

→ Report final status:
  ├─ All 3 design files (spec/plan/tasks) ✅
  ├─ Lesson content files ✅ (if implemented)
  └─ Ready for technical-reviewer validation
```

### Key Automation Points

**Automatic Execution** (No user action needed):
- ✅ Phase 0 → Phase 1 transition: Questions answered, `/sp.specify` invoked automatically
- ✅ Phase 1 → Phase 2 transition: After approval, `/sp.plan` invoked automatically
- ✅ Phase 2 → Phase 3 transition: After approval, `/sp.tasks` invoked automatically
- ✅ Phase 3 → Phase 4 (optional): After approval, ask user if they want implementation

**Human Checkpoints** (User approval required):
- ⏸ After spec.md created: Review + approve before planning
- ⏸ After plan.md created: Review + approve before tasks
- ⏸ After tasks.md created: Review + approve before implementation
- ⏸ After implementation (if chosen): Ready for validation

### What Gets Created

**By End of Phase 3** (required):
```
specs/part-5-chapter-[N]/
  ├─ spec.md       (What students learn)
  ├─ plan.md       (How we teach it, lesson-by-lesson)
  └─ tasks.md      (Implementation checklist)
```

**By End of Phase 4** (if implemented):
```
docs/part-5/chapter-[N]/
  ├─ 01-lesson-1.md
  ├─ 02-lesson-2.md
  ├─ 03-lesson-3.md
  ├─ 04-lesson-4.md (or more, based on plan)
  └─ index.md        (auto-generated TOC)
```

### Command Execution Template

**What the user sees**:

```
> /sp.python-chapter 13

⏺ PHASE 0: Context Gathering

Chapter 13: "Introduction to Python" (Part 5)

Q1: Who are we teaching?
→ [User answers]

Q2: What's the core focus for THIS chapter?
→ [User answers]

Q3: What can students BUILD after this chapter?
→ [User answers]

Q4: Which context aspects fit THIS chapter?
→ [User answers]

✅ Context gathered. Moving to Phase 1...

---

⏺ PHASE 1: Specification (Automated)

Invoking: /sp.specify with chapter context...

[/sp.specify creates spec.md]

📋 Spec created: specs/part-5-chapter-13/spec.md

Please review the specification and confirm:
- Does this match your vision for Chapter 13?
- Are learning objectives clear?
- Is scope appropriate (not too broad)?

Reply with: "✅ Spec approved" or provide feedback

→ [User reviews and approves]

---

⏺ PHASE 2: Planning (Automated)

Invoking: /sp.plan with approved spec...

[/sp.plan creates plan.md]

📋 Plan created: specs/part-5-chapter-13/plan.md

Please review the lesson breakdown:
- Are 4 lessons appropriate?
- Is AI prompt specified for each lesson?
- Are proficiency levels correct (CEFR)?

Reply with: "✅ Plan approved" or provide feedback

→ [User reviews and approves]

---

⏺ PHASE 3: Tasks (Automated)

Invoking: /sp.tasks with spec + plan...

[/sp.tasks creates tasks.md]

📋 Tasks created: specs/part-5-chapter-13/tasks.md

Please review the implementation checklist:
- Are acceptance criteria clear?
- Is testing included?
- Are all phases represented?

Reply with: "✅ Tasks approved" or provide feedback

→ [User reviews and approves]

---

⏺ PHASE 4: Implementation (Optional)

3 design files ready:
  ✅ specs/part-5-chapter-13/spec.md
  ✅ specs/part-5-chapter-13/plan.md
  ✅ specs/part-5-chapter-13/tasks.md

Ready to implement lesson content?

Options:
A) "Implement with lesson-writer subagent" → Automatic lesson creation
B) "Manual implementation" → You implement using tasks.md as guide
C) "Done" → Keep design files, skip implementation for now

→ [User chooses option]

If A: Invokes lesson-writer subagent, creates lesson files
If B/C: Reports completion status and next steps

✅ WORKFLOW COMPLETE

Final Report:
  ✅ Chapter 13 specification ready
  ✅ Lesson plan approved
  ✅ Implementation tasks defined
  ✅ All 3 design artifacts in: specs/part-5-chapter-13/

Next: Share with lesson-writer subagent for implementation
```

---

## How to Implement Orchestration (For Claude Code)

The `/sp.python-chapter` command must use **SlashCommand tool** to invoke each phase automatically.

### Implementation Pattern (Pseudocode)

```python
# MAIN COMMAND EXECUTION

def sp_python_chapter(chapter_num):
    # PHASE 0: Context Gathering
    chapter_title = read_chapter_index(chapter_num)
    validate_chapter_range(chapter_num)  # 12-29 only

    user_answers = ask_user_four_questions()
    # Stores: audience, scope, outcome, context_materials

    # PHASE 1: Specification (AUTOMATED)
    context = prepare_context_for_spec(
        chapter_num=chapter_num,
        chapter_title=chapter_title,
        user_answers=user_answers
    )

    SlashCommand.invoke("/sp.specify", context=context)
    # → Creates: specs/part-5-chapter-[N]/spec.md

    print("📋 Spec created. Review and approve before proceeding.")
    wait_for_user_approval()  # User: "✅ Spec approved"

    # PHASE 2: Planning (AUTOMATED)
    spec_content = Read("specs/part-5-chapter-{N}/spec.md")
    context = prepare_context_for_plan(
        spec=spec_content,
        chapter_title=chapter_title
    )

    SlashCommand.invoke("/sp.plan", context=context)
    # → Creates: specs/part-5-chapter-[N]/plan.md

    print("📋 Plan created. Review and approve before proceeding.")
    wait_for_user_approval()  # User: "✅ Plan approved"

    # PHASE 3: Tasks (AUTOMATED)
    plan_content = Read("specs/part-5-chapter-{N}/plan.md")
    context = prepare_context_for_tasks(
        spec=spec_content,
        plan=plan_content,
        chapter_title=chapter_title
    )

    SlashCommand.invoke("/sp.tasks", context=context)
    # → Creates: specs/part-5-chapter-[N]/tasks.md

    print("📋 Tasks created. Review and approve before proceeding.")
    wait_for_user_approval()  # User: "✅ Tasks approved"

    # PHASE 4: Implementation (OPTIONAL)
    print("Ready to implement lesson content?")
    user_choice = ask_user([
        "A) Implement with lesson-writer subagent",
        "B) Manual implementation",
        "C) Done for now"
    ])

    if user_choice == "A":
        Task.invoke(
            subagent_type="lesson-writer",
            spec=spec_content,
            plan=plan_content,
            tasks=tasks_content
        )
        # → Creates: docs/part-5/chapter-[N]/{01,02,03,04}-lesson-*.md

    # Final Report
    report_completion(chapter_num, files_created)
```

### Key Points

- **Automatic execution:** SlashCommand tool invokes `/sp.specify`, `/sp.plan`, `/sp.tasks` sequentially
- **Human checkpoints:** User approves each phase before proceeding
- **Full context passed:** Each phase receives outputs from previous phase
- **Context filtering:** Ruthless filtering applied at each phase (no Ch 14+ concepts, no advanced variations)
- **AI-native pedagogy enforced:** All specs follow Concept → Code → Think → Reasoning pattern
- **Python 3.13+ mandatory:** Every generated spec includes modern syntax standards
- **Security-first:** All specs include security non-negotiables checklist

**One user command.** Full spec → plan → tasks → implementation package. Ready for validation.

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

---

## CRITICAL VALIDATION (Before Finalizing Spec)

**Before generating spec.md, verify ALL of these:**

```
□ Target audience MATCHES user answer (no override)
□ Core focus MATCHES user answer exactly
□ Scope does NOT add beyond what user asked
□ No chapters 30+ mentioned anywhere
□ No "Spec-Driven Development" mentioned
□ AIDD references (Ch 1-11) used when relevant to reinforce prior learning
□ No methodology/pedagogy names mentioned (except AIDD for reinforcement)
□ Concept count COUNTED and ≤ tier limit (5/7/10)
□ Prerequisites ONLY chapters before this one (Ch 1-11 known; Ch 12+ if building on Python)
□ Learning objectives testable and realistic
□ Students CAN actually build promised project
□ Only 3 files will be created (spec/plan/tasks)
□ No index.md, templates, assets directories
□ **CRITICAL**: Context filtered ruthlessly
  □ Functions from future chapters SKIPPED (even if in context)
  □ Classes/OOP from future chapters SKIPPED
  □ Advanced variations of concepts SKIPPED
  □ Tangential concepts SKIPPED
  □ Only chapter-specific content EXTRACTED
```

**If ANY check fails → ASK USER FOR CLARIFICATION, don't assume.**

---

## FIXES THIS COMMAND IMPLEMENTS

✅ **Problem 1: Part mismatch** - Now validates from chapter-index.md, doesn't override
✅ **Problem 2: Forward references** - Zero mentions of Chapter 30+, SDD, methodology
✅ **Problem 3: Content overload** - Respects "core focus" answer, doesn't add extras
✅ **Problem 4: File clutter** - Creates ONLY spec/plan/tasks, no scaffolding
✅ **Problem 5: Audience mismatch** - Asks user, honors their answer, no override
✅ **Problem 6: Wrong methodology** - No self-referential rules, user-driven scope

**Result: Beginner-appropriate, AIID First, focused chapters without circular dependencies.**