---
sidebar_position: 11
title: "Chapter 12 Quiz: AI Fluency Basics"
sidebar_label: "Chapter Quiz"
---

# Chapter 12 Quiz: AI Fluency Basics

Test your understanding of the 4D Framework and AI Fluency concepts.

---

## Section 1: The 4D Framework

### Question 1
What are the four components of Anthropic's AI Fluency Framework?

- A) Design, Develop, Deploy, Debug
- B) Delegation, Description, Discernment, Diligence
- C) Define, Document, Demonstrate, Deliver
- D) Draft, Discuss, Decide, Deliver

<details>
<summary>Answer</summary>

**B) Delegation, Description, Discernment, Diligence**

The 4D Framework represents the complete workflow for AI Fluency: deciding what AI should do (Delegation), communicating intent (Description), evaluating outputs (Discernment), and ensuring responsible use (Diligence).

</details>

---

### Question 2
Which "D" addresses the question "Should AI handle this task?"

- A) Description
- B) Discernment
- C) Delegation
- D) Diligence

<details>
<summary>Answer</summary>

**C) Delegation**

Delegation is about deciding what AI should do—and what it shouldn't. It involves assessing whether a task is appropriate for AI collaboration.

</details>

---

### Question 3
What distinguishes AI Fluency from basic "prompt engineering"?

- A) AI Fluency focuses only on writing better prompts
- B) AI Fluency is a complete workflow including evaluation and responsibility
- C) Prompt engineering is more comprehensive than AI Fluency
- D) There is no difference

<details>
<summary>Answer</summary>

**B) AI Fluency is a complete workflow including evaluation and responsibility**

Prompt engineering is just one part of AI Fluency (Description). AI Fluency encompasses the entire collaboration: deciding what to delegate, how to describe it, how to evaluate outputs, and how to be responsible about results.

</details>

---

## Section 2: Delegation

### Question 4
Which of these tasks is LEAST appropriate to delegate to AI?

- A) Writing a first draft of documentation
- B) Making a final hiring decision for a candidate
- C) Summarizing meeting notes
- D) Generating test cases for a function

<details>
<summary>Answer</summary>

**B) Making a final hiring decision for a candidate**

High-stakes decisions involving people's lives and careers require human judgment, accountability, and ethical reasoning. AI can assist with research, but final decisions in sensitive areas should remain human.

</details>

---

### Question 5
What are the three modes of AI interaction?

- A) Input, Processing, Output
- B) Automation, Augmentation, Agency
- C) Simple, Medium, Complex
- D) Text, Code, Image

<details>
<summary>Answer</summary>

**B) Automation, Augmentation, Agency**

- **Automation**: AI acts independently on routine tasks
- **Augmentation**: AI assists humans who make final decisions
- **Agency**: AI takes initiative within defined boundaries

</details>

---

## Section 3: Description

### Question 6
Which of these is NOT one of Anthropic's 6 prompting techniques?

- A) Give context
- B) Show examples
- C) Use complex vocabulary
- D) Define role/tone

<details>
<summary>Answer</summary>

**C) Use complex vocabulary**

The 6 techniques are: Give context, Show examples, Specify constraints, Break into steps, Ask AI to think first, and Define role/tone. Clear, simple language is preferred over complex vocabulary.

</details>

---

### Question 7
What does the "Intent → Constraints → Success Criteria" structure accomplish?

- A) Makes prompts longer
- B) Eliminates ambiguity in AI requests
- C) Speeds up AI response time
- D) Reduces token usage

<details>
<summary>Answer</summary>

**B) Eliminates ambiguity in AI requests**

This structure ensures prompts are specifications, not vague requests. Intent defines WHAT, Constraints define MUST/MUST NOT rules, and Success Criteria define HOW you'll validate the output.

</details>

---

### Question 8
Which action verb is most appropriate for "find out why my script crashes with error code 127"?

- A) CREATE
- B) GENERATE
- C) DEBUG
- D) REFACTOR

<details>
<summary>Answer</summary>

**C) DEBUG**

DEBUG is used when code crashes, throws errors, or produces wrong output. It signals you need to identify and fix a specific problem.

</details>

---

## Section 4: Context Windows

### Question 9
What is the standard context window size for Claude Sonnet 4.5?

- A) 100K tokens
- B) 200K tokens
- C) 500K tokens
- D) 1M tokens

<details>
<summary>Answer</summary>

**B) 200K tokens**

Claude Sonnet 4.5 has a standard context of 200K tokens, with extended context up to 1M tokens available.

</details>

---

### Question 10
What is the approximate token-to-word ratio for estimating context usage?

- A) 1 word = 0.5 tokens
- B) 1 word = 1-1.2 tokens
- C) 1 word = 2 tokens
- D) 1 word = 5 tokens

<details>
<summary>Answer</summary>

**B) 1 word = 1-1.2 tokens**

For quick estimates: simple text ≈ 1 token per word, technical content with symbols ≈ 1.2 tokens per word.

</details>

---

### Question 11
At what utilization percentage should you consider creating a checkpoint?

- A) 30-40%
- B) 50-60%
- C) 70-85%
- D) 95-100%

<details>
<summary>Answer</summary>

**C) 70-85%**

The Yellow Zone (70-85%) indicates you're approaching limits. Plan to create a checkpoint soon. Above 85% (Red Zone), you should create a checkpoint immediately.

</details>

---

## Section 5: The Description-Discernment Loop

### Question 12
What triggers moving from Description to Discernment in the loop?

- A) Running out of ideas
- B) AI generates output that needs evaluation
- C) The user gets tired
- D) Token limit is reached

<details>
<summary>Answer</summary>

**B) AI generates output that needs evaluation**

After you Describe (communicate intent) and AI Generates output, you enter Discernment to evaluate whether the output meets your criteria. The loop continues until convergence.

</details>

---

### Question 13
When should you stop iterating through the Description-Discernment loop?

- A) After exactly 5 iterations
- B) When success criteria are met or returns diminish below 5%
- C) Only when the AI says it's done
- D) After 1 hour of work

<details>
<summary>Answer</summary>

**B) When success criteria are met or returns diminish below 5%**

Termination criteria include: success criteria met, diminishing returns (< 5% improvement per iteration), or time budget exceeded.

</details>

---

## Section 6: Discernment

### Question 14
Which symptom indicates context degradation in the Red Zone?

- A) AI suggests improvements you hadn't considered
- B) AI repeats the same suggestion multiple times
- C) AI asks clarifying questions
- D) AI provides detailed explanations

<details>
<summary>Answer</summary>

**B) AI repeats the same suggestion multiple times**

Red Zone symptoms include: AI forgetting earlier patterns, repeating suggestions, generic responses, and asking you to re-explain information already provided.

</details>

---

### Question 15
According to Jake Heller, what accuracy does a typical first prompt achieve?

- A) 20%
- B) 40%
- C) 60%
- D) 90%

<details>
<summary>Answer</summary>

**C) 60%**

Jake Heller found that first prompts typically achieve 60% accuracy. Professional results (97%+) require iterative refinement over weeks. "Most people quit too early."

</details>

---

## Section 7: Diligence

### Question 16
What are the three areas of Diligence in AI collaboration?

- A) Speed, Quality, Cost
- B) Creation, Transparency, Deployment
- C) Input, Process, Output
- D) Planning, Execution, Review

<details>
<summary>Answer</summary>

**B) Creation, Transparency, Deployment**

- **Creation**: Fact-checking, source verification, quality gates
- **Transparency**: Attribution, disclosure, documentation
- **Deployment**: Impact assessment, monitoring, feedback loops

</details>

---

### Question 17
When should you NOT use AI for a task?

- A) When you're in a hurry
- B) When the task is repetitive
- C) When high-stakes decisions require human judgment
- D) When you're learning something new

<details>
<summary>Answer</summary>

**C) When high-stakes decisions require human judgment**

Avoid using AI for: high-stakes decisions requiring human judgment, situations with ethical ambiguity, tasks requiring emotional intelligence, and legal/medical advice without professional oversight.

</details>

---

## Section 8: Memory Files & Multi-Session

### Question 18
What is the purpose of a CLAUDE.md file?

- A) Store temporary session data
- B) Persist project rules and context across sessions
- C) Log errors and debugging information
- D) Track token usage

<details>
<summary>Answer</summary>

**B) Persist project rules and context across sessions**

CLAUDE.md (or project memory files) store project-specific rules, patterns, and decisions that should persist across multiple AI sessions.

</details>

---

### Question 19
What is the primary purpose of context isolation?

- A) To save money on API calls
- B) To prevent pattern cross-contamination between unrelated tasks
- C) To make AI responses faster
- D) To increase context window size

<details>
<summary>Answer</summary>

**B) To prevent pattern cross-contamination between unrelated tasks**

Context isolation (using separate sessions for unrelated work) prevents one task's patterns from interfering with another, maintaining quality across parallel workstreams.

</details>

---

### Question 20
Which loading phase includes files that AI always needs?

- A) On-Demand
- B) Current Focus
- C) Foundation
- D) Extended

<details>
<summary>Answer</summary>

**C) Foundation**

The three-phase loading strategy:
- **Foundation**: What AI always needs (project rules, core patterns)
- **Current Focus**: Active working files
- **On-Demand**: Load when referenced

</details>

---

## Scoring Guide

- **18-20 correct**: Excellent! You've mastered AI Fluency fundamentals
- **14-17 correct**: Good understanding, review areas you missed
- **10-13 correct**: Revisit the lessons for deeper understanding
- **Below 10**: Restart the chapter with focused attention

---

**Next Steps**: Apply the 4D Framework in your next AI collaboration session. Track your Delegation decisions, structure your Descriptions, practice Discernment through iteration, and maintain Diligence in your outputs.
