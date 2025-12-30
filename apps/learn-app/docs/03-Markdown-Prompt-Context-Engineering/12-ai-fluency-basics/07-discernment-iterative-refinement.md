---
sidebar_position: 7
title: "Discernment: Iterative Refinement"
description: "Master applied discernment through Product, Process, and Performance evaluation while recognizing context degradation symptoms"
sidebar_label: "Discernment: Iterative Refinement"
chapter: 12
lesson: 7
duration_minutes: 45
proficiency: "B1"
concepts: 7

skills:
  - name: "Applied Discernment Through Iteration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student demonstrates iterative refinement achieving 30%+ quality improvement through systematic evaluation of Product, Process, and Performance"

  - name: "Context Degradation Recognition"
    proficiency_level: "B1"
    category: "Analytical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student identifies degradation symptoms from conversation transcripts and makes appropriate session management decisions"

  - name: "Session Quality Management"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Communication & Collaboration"
    measurable_at_this_level: "Student determines when to continue, compress, or restart a session based on observed quality signals"

learning_objectives:
  - objective: "Apply discernment through Product, Process, and Performance evaluation during AI collaboration"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Live iteration session demonstrating three-component evaluation"

  - objective: "Recognize context degradation symptoms including forgetting, repetition, and vagueness"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Symptom identification from conversation transcript examples"

  - objective: "Execute multi-iteration refinement sessions that systematically improve output quality"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Documented iteration session showing 60% to 90%+ quality progression"

  - objective: "Determine when to restart versus continue a session based on degradation severity"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Session decision analysis with justification"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (three discernment components, iteration loop, four degradation symptoms, convergence criteria, restart triggers) within B1 limit of 7-10"

differentiation:
  extension_for_advanced: "Study Jake Heller's 60% to 97% accuracy improvement methodology from CoCounsel development; analyze iteration patterns correlating token position with recall accuracy; experiment with multi-round refinement tracking metrics"
  remedial_for_struggling: "Focus on experiencing single iteration cycle: Write prompt, review AI output, identify one gap, refine prompt, compare improvement; practice recognizing repetitive suggestions as primary degradation signal"
---

# Discernment: Iterative Refinement

You have learned to construct prompts with context, structure specifications, and articulate intent clearly. But here is an uncomfortable truth that separates professional AI practitioners from casual users:

**Your first prompt will not produce professional results.**

Even experienced developers rarely achieve optimal outputs on the first attempt. Jake Heller's team at Casetext discovered this building CoCounsel, the AI legal assistant that Thomson Reuters acquired for $650 million:

> "Spend weeks tweaking prompts to get from 60% accuracy to 97%+. Most people quit too early."
>
> --- Jake Heller

Most developers abandon prompts after one or two attempts. They get 60% results, conclude "AI cannot handle this," and give up. Professional developers understand that 60% is the *starting point*, not the failure point. They iterate ten to twenty times, applying systematic discernment at each step.

This lesson teaches you that discernment skill: how to evaluate AI outputs through three lenses, recognize when context is degrading, and know when to continue refining versus when to restart fresh.

---

## The Three Components of Discernment

Discernment means judging AI output quality systematically, not by gut feeling. Effective discernment evaluates three distinct components:

### Component 1: Product Evaluation

**Question**: Is the output correct and complete?

Product evaluation checks whether AI delivered what you asked for. This is the most basic form of discernment:

| Aspect | Questions to Ask |
|--------|------------------|
| **Correctness** | Does output match requirements? Are facts accurate? |
| **Completeness** | Did AI address all specified constraints? Is anything missing? |
| **Relevance** | Does output apply to your context, or is it generic? |
| **Accuracy** | For code, does it run? For data, is it factually correct? |

**Example**: You asked for a Python function to validate email addresses.

Product discernment asks:
- Does the function correctly identify valid emails? (Correctness)
- Does it handle edge cases you specified---empty strings, Unicode characters? (Completeness)
- Is validation appropriate for your use case, or overly strict? (Relevance)
- Does the regex pattern actually work when tested? (Accuracy)

### Component 2: Process Evaluation

**Question**: Did AI follow the right approach?

Process evaluation examines *how* AI reached its answer, not just *what* it produced:

| Aspect | Questions to Ask |
|--------|------------------|
| **Reasoning** | Does AI explain its logic? Can you follow the decision chain? |
| **Method** | Is the approach appropriate for the problem domain? |
| **Assumptions** | What did AI assume about your context? Were assumptions valid? |
| **Alternatives** | Did AI consider other approaches? Why choose this one? |

**Example**: AI produced email validation using regex.

Process discernment asks:
- Why regex instead of a validation library? (Method)
- What email formats did AI assume are valid---RFC 5322 standard or simpler? (Assumptions)
- Did AI consider trade-offs between strictness and usability? (Reasoning)
- Would a different approach (library, DNS check) serve better? (Alternatives)

### Component 3: Performance Evaluation

**Question**: Does output meet quality standards?

Performance evaluation checks whether output is production-ready:

| Aspect | Questions to Ask |
|--------|------------------|
| **Quality** | Is code clean, maintainable, well-documented? |
| **Efficiency** | Is the solution appropriately efficient for your scale? |
| **Robustness** | Does it handle errors gracefully? Edge cases? |
| **Integration** | Does it fit your codebase conventions, architecture? |

**Example**: AI's email validation function works correctly.

Performance discernment asks:
- Is the regex readable, or cryptic and unmaintainable? (Quality)
- Will validation become a bottleneck at 10,000 requests per second? (Efficiency)
- What happens when input is None or not a string? (Robustness)
- Does code follow your project's naming conventions? (Integration)

---

## The Iteration Loop: From 60% to 97%

Effective discernment powers an iteration loop that transforms initial outputs into professional results:

```
Initial Prompt → AI Output → Discern (PPP) → Refine Prompt → Better Output → Repeat
```

Each iteration adds precision through the Product-Process-Performance evaluation.

### Iteration 1: Start Simple

```
Create a Git commit message for my authentication changes
```

**Discernment**: Product evaluation shows output is generic ("Updated authentication system"). Missing project context. No conventions followed.

**Quality**: Approximately 40%

### Iteration 2: Add Structure

```
Create a Git commit message for authentication changes.

CHANGES MADE:
- Added JWT token refresh endpoint
- Updated token expiration from 1 hour to 24 hours
- Fixed logout race condition

CONSTRAINTS:
- Be specific about each change
- Use imperative mood ("add" not "added")
- Under 50 characters for subject line
```

**Discernment**: Product shows improvements---specific changes listed. Process shows AI followed structural constraints. Performance reveals AI used a convention you did not specify.

**Quality**: Approximately 70%

### Iteration 3: Discover and Apply Patterns

You notice AI structured output professionally. Ask:

```
This commit message structure is good. Is this following a particular convention?
What makes this format effective?
```

AI explains Conventional Commits format. Process evaluation reveals AI knows conventions you did not. This becomes refinement input.

**Quality**: Learning moment---you discovered a professional standard

### Iteration 4: Integrate Discovered Patterns

```
Generate commit message using Conventional Commits format.

CHANGES:
- Added JWT refresh endpoint
- Extended token expiration to 24h
- Fixed logout race condition

TEAM REQUIREMENTS:
- Include Jira ticket number from branch name (currently on PROJ-1234-jwt-refresh)
- Use scope "auth" for authentication changes
- Explain "why" for each change (business value, not just technical details)
```

**Discernment**: Product shows convention followed. Process shows business context integrated. Performance shows output matches team standards.

**Quality**: Approximately 90%

### Iteration 5: Final Refinement

```
Good! One refinement: our "why" explanations should focus on business value,
not technical implementation.

Example:
Instead of: "enables mobile apps to maintain sessions"
Write: "improves mobile user experience by eliminating frequent re-logins"
```

**Output**:
```
feat(auth): add JWT refresh and extend token lifetime [PROJ-1234]

- Add /auth/refresh endpoint: improves mobile UX by eliminating frequent re-logins
- Extend token expiration to 24h: reduces authentication friction for daily users
- Fix logout race condition: ensures users are fully logged out (security improvement)
```

**Discernment**: All three components pass. Product is correct and complete. Process followed appropriate conventions with your refinements. Performance meets team standards.

**Quality**: Approximately 95%---production ready

---

## When Discernment Reveals Degradation

Effective discernment also reveals when AI collaboration is breaking down. Context degradation does not announce itself with error messages. It manifests through subtle quality declines that your discernment catches.

### Symptom 1: Repetitive Suggestions

**Definition**: AI suggests the same solution multiple times without acknowledging previous explanations.

**Example from Same Session**:

```
[00:15] YOU: How should I structure error handling for API responses?

AI: I recommend a consistent error response format:
- "status": "error"
- "message": User-friendly error description
- "code": Machine-readable error code (ERR_VALIDATION, ERR_AUTH, etc.)
- "details": Optional object with field-specific errors

[01:30] YOU: What about handling validation errors specifically?

AI: For validation errors, I recommend a consistent response format:
- "status": "error"
- "message": User-friendly description
- "code": Error code like ERR_VALIDATION
- "details": Field-specific errors
```

**Discernment**: Process evaluation reveals AI repeated nearly identical content without referencing earlier discussion. This is not refinement---it is context loss.

### Symptom 2: Forgotten Patterns

**Definition**: AI ignores or contradicts project-specific decisions established earlier.

**Example**:

```
[00:20] YOU: Our API uses camelCase for JSON keys. All responses follow this.

AI: Understood. I'll use camelCase consistently: userId, createdAt, errorMessage.

[02:00] YOU: Create an error response for invalid email format.

AI: Here's the error response:
{
  "error_message": "Invalid email format",
  "field_name": "email",
  "validation_failed": true
}
```

**Discernment**: Product evaluation catches that AI used snake_case despite agreeing to camelCase. The convention was forgotten as context filled.

### Symptom 3: Generic Responses

**Definition**: AI shifts from project-specific advice to generic best practices.

**Example**:

```
[00:30] YOU: How should I handle database connection pooling for our PostgreSQL
        setup with SQLAlchemy async?

AI: For your async SQLAlchemy setup with PostgreSQL, use asyncpg driver with
    connection pooling:
    - Set pool_size=10 for moderate traffic
    - Set max_overflow=5 for burst handling
    - Use pool_pre_ping=True to detect stale connections
    This matches your async architecture from earlier.

[02:40] YOU: How should I handle connection errors?

AI: For database connection errors, follow best practices:
    - Implement retry logic
    - Use exponential backoff
    - Log errors properly
    - Monitor connection health
    Choose an approach that fits your architecture.
```

**Discernment**: Performance evaluation reveals early response referenced your specific stack (async SQLAlchemy, PostgreSQL, asyncpg). Late response gave generic advice---"choose an approach that fits"---without remembering your architecture.

### Symptom 4: Contradictory Advice

**Definition**: AI suggests opposite approaches at different points in same session.

**Example**:

```
[00:50] YOU: Should we validate user input on client-side or server-side?

AI: Always validate on the server. Client-side validation improves UX but
    can be bypassed. Server validation is the security boundary---never
    trust client input.

[02:20] YOU: What's the best practice for validation?

AI: Client-side validation is the recommended approach. It provides immediate
    feedback and reduces unnecessary server requests. Validate on the client
    for better user experience.
```

**Discernment**: This fails all three evaluations. Product is wrong (contradictory). Process is broken (no consistency check). Performance is dangerous (security advice reversed).

---

## When to Continue vs. When to Restart

Discernment helps you decide whether to keep iterating or start fresh.

### Continue When

| Signal | Interpretation |
|--------|----------------|
| Output improving each iteration | Refinement is working |
| AI references earlier context correctly | Context still intact |
| Specific, project-aware responses | Session remains coherent |
| Steady or improving response time | No performance degradation |

### Compress or Restart When

| Signal | Severity | Action |
|--------|----------|--------|
| 1-2 symptoms observed | Mild | Continue with awareness |
| 3-4 symptoms observed | Moderate | Create checkpoint, consider restart |
| 5+ symptoms or contradictions | Severe | Restart session immediately |
| AI asks for already-provided context | Red flag | Session coherence breaking |

### The Decision Framework

When you observe degradation symptoms, ask:

1. **How critical is the current task?** High-stakes work justifies restart cost.
2. **How much context would restart lose?** If minimal, restart is cheap.
3. **Is quality declining or just plateaued?** Plateaued may not need restart.
4. **How many symptoms are accumulating?** Multiple symptoms compound.

**Rule of thumb**: If you find yourself correcting AI on information you provided earlier in the same session, restart is typically more efficient than repeated corrections.

---

## Convergence Criteria: When to Stop Iterating

Discernment also tells you when you have reached "good enough":

### Signal 1: Success Criteria Met

If you defined success criteria in your prompt:
- All constraints satisfied?
- Output passes validation tests?
- Colleague could understand without questions?

**If all yes**: Done.

### Signal 2: Diminishing Returns

Track improvement across iterations:
- Iteration 1 to 2: 40% to 70% (30% improvement)
- Iteration 2 to 3: 70% to 85% (15% improvement)
- Iteration 3 to 4: 85% to 88% (3% improvement)

**When improvement drops below 5% per iteration**: Done, or reconsider approach.

### Signal 3: Time Budget Exceeded

Set iteration budgets by task complexity:

| Task Type | Iterations | Time Budget |
|-----------|------------|-------------|
| Simple (commit message, quick doc) | 3-5 | 10 minutes |
| Medium (script creation, refactoring) | 5-10 | 30 minutes |
| Complex (architecture design, spec writing) | 10-20 | Hours to days |

**When budget exhausted**: Use best result or escalate complexity.

---

## Common Discernment Failures

### Failure 1: Quitting Too Early

**Pattern**: First prompt does not work perfectly. Conclude "AI cannot do this."

**Correction**: Commit to at least five iterations before judging capability. First attempts get 60%. Professional results require iteration.

### Failure 2: Ignoring Patterns AI Suggests

**Pattern**: AI returns output with improvements you did not request. You force AI back to your original (inferior) approach.

**Correction**: When AI suggests better patterns, investigate. Ask "Why did you use this format?" AI may know conventions you do not.

### Failure 3: Not Providing Your Context

**Pattern**: AI keeps producing generic output. You regenerate without explaining requirements.

**Correction**: Teach AI your context. "Our project uses Bash, not Python. We follow Google Shell Style Guide. Logs go to /var/log/."

### Failure 4: Changing Too Many Things at Once

**Pattern**: Output is wrong. You rewrite prompt with ten new constraints. New output is different but still wrong.

**Correction**: Iterate one or two constraints at a time. This reveals which changes help versus which create new problems.

---

## Try With AI

Now practice applied discernment through a structured iteration session.

### Setup

Open your AI coding assistant (Claude, ChatGPT, Gemini, or similar). You will iterate on a Git commit message, applying Product-Process-Performance evaluation at each step.

### Part 1: Initial Request

Submit a minimal prompt:

```
Create a Git commit message for my changes to backup.sh
```

**Observe**: What does AI return? Note quality estimate (likely 40-60%).

### Part 2: Product Evaluation

Evaluate the product component:
- Does the message explain *what* changed?
- Does it explain *why* changes were made?
- Would a teammate understand without reading the diff?
- Did AI use any structure you did not specify?

If AI used an unfamiliar convention, ask AI to explain it.

**What you are learning**: Product discernment separates correct outputs from outputs that merely exist.

### Part 3: Process Evaluation and Context Teaching

Now add your project-specific requirements:

```
Good start, but we use this commit format:
- First line: [ticket-id] type: brief description
- Body: bullet list of changes with business value explanation

Our standards:
- Include Jira ticket from branch name
- Types: feat, fix, docs, refactor
- Explain "why" for each change (business value, not technical details)

Try again with these requirements.
```

**Observe**: Does AI adapt to your constraints? This tests whether AI's process can incorporate your standards.

**What you are learning**: Process discernment evaluates whether AI followed appropriate methods and integrated your context correctly.

### Part 4: Performance Evaluation and Iteration

Continue refining with one or two constraints per iteration:

Possible refinements:
- "Subject line must be under 50 characters"
- "Include breaking changes in footer if any"
- "Reference documentation link for architectural changes"

Track improvement: What was quality at iteration 1? At iteration 3? At iteration 5?

**What you are learning**: Performance discernment validates whether outputs meet production standards for your specific environment.

### Part 5: Degradation Watch

If your session extends beyond 30 minutes, watch for degradation symptoms:
- Does AI repeat earlier explanations?
- Does AI forget conventions you established?
- Do responses become generic instead of project-specific?

If you observe symptoms, note them. Decide: continue or restart?

**What you are learning**: Discernment applies not just to individual outputs but to session quality over time. Recognizing degradation prevents wasted iteration on a degrading context.

**Safety reminder**: When iterating with AI, verify factual claims before accepting (AI may hallucinate statistics or technical details), test all code in a safe environment, and avoid sharing sensitive credentials in prompts. Discernment includes verifying that AI's confident-sounding outputs are actually correct.
