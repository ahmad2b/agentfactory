# Python Chapter Design Template (AI-Native Pedagogy)

**Purpose**: Opinionated, reusable framework for designing Python chapters (12-29) aligned with AI-native colearning philosophy.

**Foundation**: Embedded in `preface-agent-native.md` vision + Chapter 31-32 (Spec-Driven Development) execution patterns.

---

## Master Design Principles

### 1. Core Philosophy (From Preface)

Every Python chapter must answer:

- **Why Python?** Dominates AI/agentic development (readability, flexibility, ecosystem)
- **Why this skill?** Enables AI collaboration (clear thinking → AI generation)
- **What's the student's role?** Specification writer, validator, architect (NOT syntax memorizer)
- **What's AI's role?** Syntax executor, pattern applier, implementation partner

### 2. Three-Tier Structure (Like Spec-Kit Plus Vertical Intelligence)

Every lesson follows this pattern:

```
TIER 1: CONCEPT (Human Teacher)
↓
TIER 2: CODE IDEA (Show minimal example)
↓
TIER 3: THINK WITH AI (Dialogue-driven exploration)
↓
REASONING PATTERN (Why this matters for AI development)
```

This mirrors the Spec-Kit Plus architecture:
- **Tier 1** = Human intent (specification)
- **Tier 2** = Code example (reference)
- **Tier 3** = AI collaboration (execution + validation)

### 3. Evals-First, Spec-First, AI-Native

Before writing ANY content:

1. **Define success evals** (business-goal-aligned)
   - What can students DO? (skills)
   - What will they BUILD? (application)
   - How do they COLLABORATE with AI? (partnership)

2. **Write specification** (not just outline)
   - Learning objectives tied to evals
   - Cognitive load limits (5/7/10 concepts)
   - Code examples with pedagogical purpose
   - Assessment criteria

3. **Implement lessons** (each follows template)
   - YAML frontmatter with skills metadata
   - 5-part teaching pattern
   - "Try With AI" activity
   - Cross-references to book scaffold

---

## Chapter Design Workflow

### Phase 0: Context Gathering (Ask 3 Questions)

**Extract from arguments:**
```
Chapter number (12-29)
Part within Python sequence (4-5)
Position relative to dependencies
```

**Ask user:**
1. **Existing materials?** (notes, notebooks, teaching experience)
   - If yes: Extract concepts → transform to AI-native structure
2. **Target audience?** (beginner/professional/founder)
   - Shapes evals, real-world examples, complexity
3. **Real problems to solve?** (what can students build?)
   - Informs capstone project, "Try With AI" activities

---

### Phase 1: Specification (Evals → Spec)

**Create `specs/part-5-chapter-${N}/spec.md` with this structure:**

```yaml
---
chapter: N
title: "[Title from chapter-index.md]"
part: 5
complexity: [beginner|intermediate|advanced]
cefr_range: "[A1-A2|A2-B1|B1-B2]"
python_version: "3.13+"
cognitive_load_limit: [5|7|10]  # Based on complexity tier
---

## Success Evals (Business-Goal-Aligned)

### Students Will Understand
[3-5 comprehension criteria]

### Students Will Do
[3-5 skill-based criteria]

### Students Will Build
[2-3 application/capstone criteria]

## Learning Objectives
[3-5 SMART objectives aligned with evals]

## Lesson Structure
- Lesson 1: [Topic]
- Lesson 2: [Topic]
- Lesson 3-5: [Topics]
- Capstone: [Real project]

## Concepts Taught
[List with pedagogical purpose + AI prompt template for each]

## Acceptance Criteria
- [ ] Every concept: Concept → Code → Think With AI → Reasoning
- [ ] Python 3.13+ syntax, f-strings, modern type hints
- [ ] Cognitive load ≤ limit
- [ ] No REPL examples; use "Ask your AI" instead
- [ ] Security standards met (no eval, shell=True, secrets)
- [ ] Each lesson 20-35 minutes
- [ ] "Try With AI" activities testable with Claude Code/Gemini CLI
```

**Key difference from old approach:**
- ❌ OLD: "Here's Python syntax, memorize it"
- ✅ NEW: "Here's a concept. Ask AI to generate code. Validate understanding."

---

### Phase 2: Planning (Lesson Breakdown)

**Create `specs/part-5-chapter-${N}/plan.md` with:**

```yaml
lessons:
  - lesson_number: 1
    title: [Title]
    duration: 20-25 minutes
    concepts: [list, with, count]
    cognitive_load: X / [5|7|10]

    skills_taught:
      - skill: [Name]
        proficiency_level: [A1|A2|B1|B2]
        bloom_level: [Remember|Understand|Apply|Analyze|Evaluate|Create]
        assessment: [How to measure]

    code_examples:
      - example_id: "1.1"
        purpose: [Pedagogical purpose]
        ai_prompt_template: "[Student asks AI...]"
        validation_criteria: [How to verify output]

    try_with_ai_activity:
      - specify: "[Student tells AI...]"
      - receive: "[AI generates...]"
      - validate: "[Student checks...]"
      - extend: "[Student deepens...]"
```

**Skills Metadata (Hidden from Students, Visible to Institutions):**
- CEFR proficiency levels (A1-C2)
- Bloom's cognitive complexity
- DigComp digital competence areas
- MEASURABLE at this level (what can student actually DO?)

**Progressive Complexity:**
- Lessons 1-2: A1 (recognition, basic application)
- Lessons 3-4: A2 (application with guidance)
- Lesson 5+: B1 (independent application to new problems)

---

### Phase 3: Tasks (Implementation Checklist)

**Create `specs/part-5-chapter-${N}/tasks.md`:**

```yaml
tasks:
  - task_id: "T001"
    content: "Create chapter directory with README"
    depends_on: []

  - task_id: "T002"
    content: "[US1] Implement Lesson 1: [Title] with 5-part structure"
    depends_on: ["T001"]
    acceptance_criteria:
      - [ ] Lesson follows: Concept → Code → Think With AI → Reasoning
      - [ ] YAML frontmatter with skills metadata
      - [ ] Code examples run in Python 3.13+
      - [ ] "Try With AI" activity specified
      - [ ] Cognitive load checked (≤5 concepts)

  - task_id: "T003"
    content: "Validate all AI prompts with Claude Code / Gemini CLI"
    depends_on: ["T002"]

  - task_id: "T00X"
    content: "Run technical-reviewer validation"
    depends_on: [all lesson tasks]
```

---

## Lesson File Template

Each lesson follows this structure:

### YAML Frontmatter (Hidden Skills Metadata)

```yaml
---
chapter: N
lesson: L
title: "[Lesson Title]"
duration_minutes: 20-35

# HIDDEN SKILLS METADATA (For institutional accreditation)
skills:
  - name: "[Skill Name]"
    proficiency_level: "[A1|A2|B1|B2]"
    category: "[Technical|Conceptual|Soft]"
    bloom_level: "[Remember|Understand|Apply|Analyze|Evaluate|Create]"
    digcomp_area: "[Information Literacy|Communication & Collaboration|Digital Content Creation|etc]"
    measurable_at_this_level: "Student can... [specific, observable behavior]"

learning_objectives:
  - objective: "[SMART objective]"
    proficiency_level: "[A1|A2|B1]"
    bloom_level: "[...]"
    assessment_method: "..."

cognitive_load:
  new_concepts: X
  assessment: "X new concepts (list) within [limit] ✓"

differentiation:
  extension_for_advanced: "[For A2 students pushing toward B1]"
  remedial_for_struggling: "[For A1 students needing support]"

generated_by: "lesson-writer v3.0.0"
source_spec: "specs/part-5-chapter-${N}/spec.md"
version: "1.0.0"
---
```

### Content Structure

**Part A: Opening Hook**
```
"[Real-world scenario showing why this concept matters]"
```

**Part B: Concept Explanation**
```
## 1. [Concept Name] — [Why It Matters]

**What it is:**
[2-3 sentences, plain language]

[Philosophy/Why for AI development]

### 💻 Code Idea

\`\`\`python
# Minimal code showing concept
# Comments explain WHAT it does, not HOW syntax works
\`\`\`

### 🤖 Think With Your AI

> **Understand:** "Question that builds understanding"
>
> **Extend:** "Question that explores edge cases or variants"
>
> **Apply:** "Question linking to AI development"

### 🧠 The Reasoning Pattern

[Why this concept matters for AI reasoning, not just coding]
```

**Part C: "Try With AI" Activity**
```
## Try With Your AI Co-Teacher

**Activity Name**: [What you're building]

1. **Specify**: "Tell Claude Code: [Your specification]"
2. **Receive**: Claude generates code
3. **Validate**: Check output against intent
4. **Extend**: Modify/improve the code

[Alternative: If no code yet, dialogue-driven exploration]
```

**Part D: Checkpoint/Reflection**
```
## What You Learned

[Synthesize the concept]
[Connect to next lesson]
```

---

## Python Standards (Mandatory)

### Version & Syntax
- **Python 3.13+** (never 3.10 or earlier)
- f-strings ONLY (no % or .format())
- Modern type hints: `list[int]`, `dict[str, int]`, `X | None` (not `List`, `Dict`, `Optional`)
- match/case statements (Chapter 17+)
- Walrus operator `:=` (Chapter 17+)

### Type Hints Progression
```
Chapter 13 (Intro):      NO type hints (too early)
Chapter 14-16:           Show in examples, not required
Chapter 17-26:           Gradually increase
Chapter 27+ (Pydantic):  MANDATORY in all examples
```

### Security Non-Negotiables
- ❌ NO `eval()`, `exec()` on user input
- ❌ NO `shell=True` in subprocess
- ❌ NO hardcoded secrets/passwords
- ❌ NO SQL string concatenation
- ✅ Always: Environment variables, input validation, modern patterns

---

## Cognitive Load Management

### By Complexity Tier

| Tier | Chapters | CEFR | Concepts/Section | Examples | REPL? |
|------|----------|------|-----------------|----------|-------|
| **Beginner** | 12-16 | A1-A2 | 5 max | 1-2 per section | No; use "Ask AI" |
| **Intermediate** | 17-23 | A2-B1 | 7 max | 2-3 per section | No; use "Ask AI" |
| **Advanced** | 24-29 | B1-B2 | 10 max | 3-5 per section | No; use "Ask AI" |

### Counting Concepts

Each lesson has a **cognitive load budget**:
- 1 concept = core idea + vocabulary
- 5 concepts (beginner) = e.g., functions, parameters, return types, scope, recursion
- 7 concepts (intermediate) = e.g., above + closures, decorators, generators
- 10 concepts (advanced) = e.g., above + metaclasses, descriptors, context managers

**Formula**: New concepts this lesson < Tier limit

---

## Cross-Chapter Coherence

### Book Scaffolding

Every chapter references:
- **Prerequisites** (chapters that must come first)
- **Enables** (chapters that depend on this)
- **Concepts thread** (how concepts connect across chapters)

**Example for Chapter 13:**
```
Prerequisite: Chapter 12 (UV project structure)
Enables: Chapter 14 (Data Types), Chapter 17 (Control Flow)
Concept thread: Variables → Data Types → Control Flow → Functions
```

### Real-World Thread

Build ONE coherent project across all lessons:
- **Lesson 1**: Concept foundation
- **Lesson 2**: Mechanism understanding
- **Lesson 3-5**: Applied examples
- **Capstone**: Working, real project

**Example for Chapter 13:**
- Lesson 1: "Why Python for AI?"
- Lesson 2: "How Python executes" (bytecode)
- Lesson 3: "Modern syntax and types"
- Lesson 4: "Everything is an object" (OOP foundation)
- Lesson 5: "Duck typing" (flexibility)
- Lesson 6: "Dynamic + optional types" (balance)
- **Capstone**: Build an LLM Response Validator using all concepts

---

## Assessment & Validation

### Lesson-Level Assessment

Each "Try With AI" activity:
- ✅ **Specify**: Student expresses intent clearly
- ✅ **Receive**: AI generates code
- ✅ **Validate**: Student checks against intent
- ✅ **Extend**: Student modifies/improves

### Chapter-Level Validation

**Technical Reviewer Checklist:**
```
- [ ] All code examples run in Python 3.13+
- [ ] Type hints are syntactically correct
- [ ] No security vulnerabilities
- [ ] Each lesson cognitive load ≤ tier limit
- [ ] Reading level Grade 7+ with explanations
- [ ] Duration per lesson 20-35 minutes
- [ ] "Try With AI" activities testable
- [ ] Chapter coherence (thread + progression)
- [ ] Constitution alignment (spec-first, validation-first)
- [ ] Cross-references functional
```

---

## Implementation Orchestration

When you run `/sp.python-chapter ${N}`:

```
Step 1: Parse chapter number → Validate (12-29) → Get chapter title

Step 2: Ask context questions
   └─ Existing materials? (transform if yes)
   └─ Target audience? (shapes evals)
   └─ Real problems? (informs capstone)

Step 3: Auto-run /sp.specify
   └─ Create spec.md with evals-first approach
   └─ Apply Python 3.13+ standards
   └─ User approves spec

Step 4: Auto-run /sp.plan
   └─ Break into 5-6 lessons
   └─ Map skills (CEFR/Bloom's/DigComp)
   └─ Design "Try With AI" prompts
   └─ User approves plan

Step 5: Auto-run /sp.tasks
   └─ Generate implementation checklist
   └─ Include validation tasks
   └─ User approves tasks

Step 6: Deliver
   └─ specs/part-5-chapter-${N}/
      ├── spec.md (with evals)
      ├── plan.md (with skills metadata)
      └── tasks.md (with acceptance criteria)
   └─ Ready for lesson-writer implementation
```

---

## Differences from Traditional Programming Books

| Traditional | AI-Native |
|-------------|-----------|
| "Learn syntax" | "Learn concepts" |
| "Memorize patterns" | "Think with AI partner" |
| "REPL first, validation" | "Specify intent, AI executes, validate" |
| "Read code examples" | "Ask AI to generate, observe, extend" |
| "Solo problem-solving" | "Collaborative reasoning" |
| "Beginner-unfriendly" | "Beginner-accessible (AI co-teacher)" |

---

## Quality Gates (Non-Negotiable)

Before publishing ANY chapter:

### Technical Quality
- ✅ Every code example tested (Python 3.13+)
- ✅ No security anti-patterns
- ✅ Type hints correct and helpful
- ✅ Cognitive load validated

### Pedagogical Quality
- ✅ Every concept → Code → Think With AI → Reasoning
- ✅ "Try With AI" activities specified (testable)
- ✅ Learning objectives measurable
- ✅ Assessment methods clear

### Constitution Alignment
- ✅ Spec-first approach (evals → spec → plan → tasks)
- ✅ Validation-first mindset (checks, not just code)
- ✅ AI-native philosophy (colearning, not memorization)
- ✅ Accessibility (Grade 7+ reading, explained terms)

---

## Usage Examples

### Example 1: Chapter 13 (Introduction to Modern Python)

```
$ /sp.python-chapter 13

→ Chapter 13: Introduction to Modern Python
→ Complexity: Beginner (A1-A2, 5 concepts/section)
→ Question 1: Existing materials? (← Reference old lesson, transform)
→ Question 2: Target audience? (← AI developers, career path)
→ Question 3: Real problems? (← Build LLM validator)

[Auto-run /sp.specify]
[Create: specs/part-5-chapter-13/spec.md with evals-first]

[User approves spec]

[Auto-run /sp.plan]
[Create: specs/part-5-chapter-13/plan.md with lesson breakdown + skills metadata]

[User approves plan]

[Auto-run /sp.tasks]
[Create: specs/part-5-chapter-13/tasks.md with implementation checklist]

[User approves tasks]

✅ Complete package ready for lesson-writer subagent
```

### Example 2: Chapter 17 (Control Flow)

```
$ /sp.python-chapter 17

→ Chapter 17: Control Flow
→ Complexity: Intermediate (A2-B1, 7 concepts/section)
→ Concepts: if/elif/else, for loops, while loops, break/continue, match/case, comprehensions, generators
→ Capstone: Build a request router (if/elif → match/case; loops for batch processing)
→ AI-native frame: "How does an AI agent route requests? How does it iterate?"

[Full workflow with intermediate complexity limits]
```

---

## Final Note

**This template embeds:**
- AI-native colearning philosophy (from preface)
- Spec-Driven Development workflow (from Chapter 31-32)
- Pedagogical standards (CEFR, Bloom's, DigComp)
- Python 3.13+ best practices
- Security and quality gates

**Result**: Any AI orchestrator can design a consistent, high-quality Python chapter using this framework. No ambiguity. No guessing. Just opinionated, pedagogically-sound education.

