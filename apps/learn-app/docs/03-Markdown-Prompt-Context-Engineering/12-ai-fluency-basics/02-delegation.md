---
sidebar_position: 2
title: "Delegation: Deciding What AI Should Do"
description: "Learn the delegation decision framework to determine which tasks AI should handle, using Jake Heller's prompts-as-specifications insight and the three interaction modes"
keywords:
  [
    "AI delegation",
    "task delegation",
    "AI collaboration",
    "prompts as specifications",
    "automation vs augmentation",
    "AI fluency",
    "Jake Heller",
    "Casetext",
    "decision framework",
  ]
chapter: 12
lesson: 2
duration_minutes: 30

skills:
  - name: "AI Delegation Decision-Making"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can apply the delegation decision tree to classify 5 different tasks as AI-suitable or human-only with correct justification"

  - name: "Interaction Mode Selection"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain the difference between Automation, Augmentation, and Agency modes with correct examples for each"

  - name: "Risk Assessment for AI Tasks"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can identify high-risk tasks that should not be delegated to AI and explain why human oversight is required"

  - name: "Specification Thinking"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can distinguish between WHAT (specification) and HOW (implementation) when framing AI requests"

learning_objectives:
  - objective: "Apply the Delegation decision framework (Can AI help? Should AI help?)"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Given 5 task scenarios, student correctly classifies each using the decision tree with written justification"

  - objective: "Identify tasks suitable for AI collaboration vs. human-only tasks"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student categorizes 8 tasks into AI-suitable and human-only buckets with 80%+ accuracy"

  - objective: "Recognize the three interaction modes (Automation, Augmentation, Agency)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student matches 6 task examples to correct interaction modes with explanations"

  - objective: "Evaluate tasks using risk/reward framework"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student identifies risk factors in 4 scenarios and recommends appropriate human oversight levels"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (delegation decision tree, three modes, WHAT vs HOW, risk assessment, prompts-as-specs, iteration mindset) within A2 limit (5-7 concepts) - at upper boundary but manageable with progressive introduction"

differentiation:
  extension_for_advanced: "Research the Casetext CoCounsel system and analyze how Jake Heller's team achieved 97% accuracy through systematic prompt refinement"
  remedial_for_struggling: "Focus on the three interaction modes first with concrete examples before introducing the full decision tree"
---

# Delegation: Deciding What AI Should Do

You've opened Claude Code. The cursor blinks. Your project has a hundred tasks waiting.

Where do you start?

Most people start by asking AI to do *something*—whatever feels urgent. They type a vague request, get a mediocre response, and conclude that AI tools are overhyped. Meanwhile, developers who understand delegation are producing production-quality code in a fraction of the time.

The difference isn't the AI. It's knowing which tasks to give it—and which to keep for yourself.

This is the insight that made Jake Heller's legal AI company Casetext worth $650 million: **the most important skill in AI collaboration isn't prompting—it's delegation**. Before you write a single prompt, you need to decide what AI should do, what you should do, and how the two of you will work together.

## The Prompts-as-Specifications Insight

Jake Heller founded Casetext and built CoCounsel, an AI legal assistant that achieved a 97% pass rate on complex legal evaluations. When Thomson Reuters acquired Casetext for $650 million in 2023, they weren't buying code—they were buying encoded legal expertise.

In a 2024 Y Combinator talk, Heller shared the insight that made this possible:

> "Spend weeks tweaking prompts to get from 60% accuracy to 97%+. Most people quit too early."
> — Jake Heller, Founder of Casetext (Y Combinator talk, 2024)

This isn't about clever prompt tricks. Heller's team treated prompts as **specifications**—precise documents defining exactly what output should look like. They iterated for weeks, not minutes. They measured accuracy rigorously. They treated prompt development like software development.

**The paradigm shift**: Prompts aren't casual requests. They're specifications that define the contract between you and AI.

This insight transforms how you think about delegation. Before asking "How do I prompt this?", ask: "Is this the right task for AI? And if so, what specification would define success?"

## The Delegation Decision Tree

Not every task belongs to AI. The delegation decision tree helps you decide:

```
                    ┌─────────────────────┐
                    │  New Task Arrives   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   CAN AI help?      │
                    │ (Capability check)  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │ NO             │                │ YES
              ▼                │                ▼
    ┌─────────────────┐        │      ┌─────────────────┐
    │ Human-only task │        │      │  SHOULD AI help?│
    │ (Use manual     │        │      │  (Value check)  │
    │  skills)        │        │      └────────┬────────┘
    └─────────────────┘        │               │
                               │    ┌──────────┼──────────┐
                               │    │ NO       │          │ YES
                               │    ▼          │          ▼
                               │  ┌────────────┴──┐  ┌────────────────┐
                               │  │ Human handles │  │  HOW should AI │
                               │  │ (Risk/control │  │  help?         │
                               │  │  requires it) │  │  (Mode select) │
                               │  └───────────────┘  └───────┬────────┘
                                                             │
                                         ┌───────────────────┼───────────────────┐
                                         │                   │                   │
                                         ▼                   ▼                   ▼
                                  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
                                  │ AUTOMATION  │     │AUGMENTATION │     │   AGENCY    │
                                  │ AI acts     │     │ AI assists  │     │ AI takes    │
                                  │ alone       │     │ human       │     │ initiative  │
                                  └─────────────┘     └─────────────┘     └─────────────┘
```

### Stage 1: CAN AI Help?

The first question is capability: does AI have the skills to contribute meaningfully?

**AI CAN help when the task involves:**
- Pattern recognition (code patterns, document structures, data formats)
- Text generation (documentation, code, explanations)
- Information synthesis (research summaries, comparisons)
- Transformation (converting between formats, refactoring)
- Analysis (reviewing code, identifying issues)

**AI CANNOT meaningfully help when the task requires:**
- Physical world interaction (hardware debugging, in-person meetings)
- Access to private systems (your company's internal databases—unless connected via MCP)
- Real-time information (current stock prices, live events—unless web-enabled)
- Legal/medical decisions with liability (must have licensed human approval)
- Creative judgment that's uniquely yours (your artistic vision, personal values)

**Example evaluation:**

| Task | Can AI Help? | Why |
|------|--------------|-----|
| Write unit tests for a function | Yes | Pattern recognition + code generation |
| Debug a hardware sensor | No | Requires physical interaction |
| Summarize a research paper | Yes | Text analysis + synthesis |
| Decide company strategy | Partially | Can analyze data, but judgment is human |
| Fix a CSS layout issue | Yes | Pattern recognition in visual code |

### Stage 2: SHOULD AI Help?

Even when AI *can* help, you must decide if it *should*. This is a value judgment about risk, efficiency, and learning.

**AI SHOULD help when:**
- Task is repetitive but accuracy matters (boilerplate, formatting, migrations)
- Speed would otherwise bottleneck progress
- Task complexity benefits from a "second brain"
- You need to explore options quickly before committing
- Documentation or explanation would take longer than creating

**AI SHOULD NOT help when:**
- You need to learn the skill deeply (practice manually first)
- Errors have catastrophic consequences without human review
- The task requires confidential information you can't share
- Human relationship or empathy is the core value (hiring decisions, customer apologies)
- Legal, medical, or financial decisions require licensed professional approval

**The learning exception is critical**: If you delegate too early, you won't develop the mental models to evaluate AI's output. You must understand concepts through hands-on practice before collaborating with AI on them.

### Stage 3: HOW Should AI Help?

If AI can and should help, the final question is *how*. This determines the interaction mode.

## The Three Interaction Modes

Every AI collaboration falls into one of three modes. Choosing the right mode is essential for success.

### Mode 1: Automation (AI Acts Alone)

**Definition**: You specify the task, AI executes completely, you receive the finished result.

**Best for:**
- Repetitive, well-defined tasks with clear success criteria
- Tasks where you'll review output anyway (batch file renaming, format conversion)
- Low-risk operations with easily reversible results

**Examples:**
- "Convert all timestamps in this file from Unix to ISO 8601 format"
- "Generate docstrings for all public functions in this module"
- "Create a Dockerfile from this requirements.txt"

**Your role**: Define the specification precisely, review the output, approve or reject.

**Risk profile**: Low for reversible tasks, medium for permanent changes.

### Mode 2: Augmentation (AI Assists Human)

**Definition**: You remain in control. AI provides suggestions, drafts, or analysis that you actively evaluate and modify.

**Best for:**
- Complex tasks requiring human judgment
- Creative work where AI provides starting points
- Situations where you want to learn while producing output
- Tasks where context changes frequently

**Examples:**
- "Review this function and suggest improvements"
- "Draft three approaches to this architecture problem"
- "Help me debug this test failure by analyzing the stack trace"

**Your role**: Drive the process, evaluate suggestions, make decisions, integrate feedback.

**Risk profile**: Low to medium—you're reviewing everything.

### Mode 3: Agency (AI Takes Initiative)

**Definition**: AI operates with more autonomy, making decisions within boundaries you've defined, reporting back for approval on key milestones.

**Best for:**
- Multi-step tasks where you trust the AI's approach
- Exploration and research where AI should follow interesting threads
- Build/test cycles where AI can iterate independently

**Examples:**
- "Implement this feature according to the spec—run tests after each change"
- "Research these three libraries and recommend one with justification"
- "Refactor this module to reduce complexity, making commits as you go"

**Your role**: Define boundaries and success criteria, review key checkpoints, approve final results.

**Risk profile**: Medium to high—requires clear specifications and checkpoints.

## Mode Selection by Task Type

| Task Type | Recommended Mode | Why |
|-----------|------------------|-----|
| File format conversion | Automation | Well-defined, reversible |
| Code review | Augmentation | Requires your judgment |
| Feature implementation | Agency | Multi-step with clear spec |
| Debugging | Augmentation | You understand context best |
| Documentation generation | Automation | Clear template-based output |
| Architecture design | Augmentation | Needs human strategic thinking |
| Refactoring | Agency | Clear metrics (test pass, complexity) |
| Security review | Augmentation | Human must make risk decisions |

## The WHAT vs HOW Distinction

Here's the insight that separates fluent AI users from everyone else:

**You specify WHAT. AI determines HOW.**

This is the prompts-as-specifications insight applied. Your job is to define success criteria, constraints, and context. AI's job is to figure out the implementation.

**WHAT (Your Specification):**
- What problem are you solving?
- What does success look like?
- What constraints exist (performance, style, compatibility)?
- What context does AI need to understand?

**HOW (AI's Implementation):**
- Which algorithm or approach?
- What code structure?
- Which libraries or patterns?
- What intermediate steps?

**Wrong approach (specifying HOW):**
```
Write a for loop that iterates through the list, checks if each
element is greater than 10, and appends it to a new list.
```

**Right approach (specifying WHAT):**
```
Filter this list to include only values greater than 10.
Use idiomatic Python.
```

When you specify WHAT, AI can apply its full knowledge to find the best HOW. When you specify HOW, you limit AI to your preconceived solution—which may not be optimal.

**Exception**: When you need to learn specific techniques, you might ask AI to demonstrate particular approaches. But for production work, specify WHAT and let AI optimize HOW.

## Risk Assessment: What NOT to Delegate

Some tasks should never be fully delegated to AI, regardless of capability. Use this risk framework:

### High-Risk Categories

| Category | Example Tasks | Why Human Required |
|----------|---------------|-------------------|
| **Irreversible actions** | Database migrations, production deployments | Mistakes can't be undone easily |
| **Legal liability** | Contract terms, compliance statements | Licensed professionals must approve |
| **Personal data decisions** | GDPR compliance, data deletion | Regulatory requirements for human oversight |
| **Security credentials** | API keys, passwords, access controls | Trust boundaries require human judgment |
| **Financial transactions** | Billing logic, payment processing | Errors have direct monetary impact |
| **Life safety** | Medical advice, safety-critical code | Human lives may depend on decisions |

### The Risk/Reward Matrix

Before delegating, evaluate:

```
                        HIGH REWARD
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        │   AUGMENTATION     │    AGENCY with     │
        │   (AI assists,     │    checkpoints     │
        │    human decides)  │    (AI acts with   │
        │                    │     oversight)     │
        │                    │                    │
LOW ────┼────────────────────┼────────────────────┼──── HIGH
RISK    │                    │                    │     RISK
        │                    │                    │
        │   AUTOMATION       │    HUMAN ONLY      │
        │   (AI handles      │    (Too risky for  │
        │    completely)     │     delegation)    │
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                        LOW REWARD
```

**Quadrant guide:**
- **Low risk, Low reward**: Automate (batch tasks, formatting)
- **Low risk, High reward**: Use Agency with clear specs (feature development)
- **High risk, Low reward**: Augment carefully (human reviews AI suggestions)
- **High risk, High reward**: Human leads with selective AI input

## The Iteration Mindset

Remember Jake Heller's insight: "Most people quit too early."

Delegation isn't a one-shot decision. It's the start of an iterative process:

1. **Delegate** → Choose task and mode
2. **Describe** → Write your specification (Lesson 3)
3. **Discern** → Evaluate AI output (Lesson 7)
4. **Refine** → Improve specification based on results
5. **Repeat** → Until output meets your standard

The goal isn't perfection on the first try. The goal is a systematic process that converges on quality. Heller's team spent *weeks* refining prompts—not because they were slow, but because they understood that iteration IS the process.

**This is why delegation comes before prompting**: If you delegate the wrong task, no amount of prompt refinement will produce good results. Get delegation right first, then invest in the Description-Discernment loop.

## Try With AI

Use your AI companion (Claude Code, or similar) to practice delegation decisions.

### Prompt 1: Task Classification Practice

```
I want to practice the delegation decision tree. Here are 5 tasks
from my work:

1. Write unit tests for a new API endpoint
2. Decide which team member to assign to a critical project
3. Summarize meeting notes into action items
4. Review a security audit report and approve remediation steps
5. Convert a CSV file to JSON format

For each task, walk me through the decision tree:
- CAN AI help? (capability check)
- SHOULD AI help? (value check)
- If yes, which mode: Automation, Augmentation, or Agency?

Challenge my classifications if you think I'm wrong.
```

**What you're learning**: The delegation decision tree becomes second nature when you apply it to real tasks. AI helps you practice by testing your reasoning.

### Prompt 2: WHAT vs HOW Transformation

```
I tend to over-specify my prompts. Help me practice the WHAT vs HOW
distinction.

Here's a prompt I wrote:
"Write a Python function that uses a for loop to iterate through
a dictionary, checks if each value is None, and removes those
key-value pairs by creating a new dictionary without them."

Transform this into a WHAT specification instead of a HOW instruction.
Then show me both versions of the code you'd produce, and explain
why the WHAT version might give better results.
```

**What you're learning**: When you specify WHAT, AI can apply solutions you might not know. This prompt helps you see the difference concretely.

### Prompt 3: Risk Assessment

```
I'm about to delegate this task to you:
"Refactor our authentication module to use JWT tokens instead of
session cookies. The module handles login, logout, password reset,
and API access control for our production system."

Before we start:
1. What are the risk factors in this task?
2. What mode (Automation, Augmentation, Agency) would you recommend?
3. What checkpoints or human approval points should we build in?
4. What should I definitely NOT delegate to you in this task?

Be honest about limitations and risks.
```

**What you're learning**: AI can help you identify risks you might overlook. This dialogue establishes appropriate boundaries before work begins, modeling the responsible delegation practice.

### Safety Note

Delegation decisions have real consequences. When evaluating whether AI should handle a task, err on the side of human oversight for anything involving security, privacy, legal compliance, or irreversible changes. The goal is effective collaboration, not abdication of responsibility.

---
