---
sidebar_position: 8
title: "Compression & Multi-Session Workflows"
description: "Create checkpoint summaries, restart sessions cleanly, and design multi-session workflows for complex parallel tasks"
sidebar_label: "Compression & Multi-Session"
keywords: ["context compression", "checkpoint", "session restart", "multi-session", "context isolation", "parallel tasks"]
chapter: 12
lesson: 8
duration_minutes: 40
proficiency: "B1"

# HIDDEN SKILLS METADATA
skills:
  - name: "Context Checkpoint Creation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student creates checkpoints under 600 tokens preserving essential session intelligence"

  - name: "Session Handoff Strategy"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student restarts sessions using checkpoint restoration with verified context recovery"

  - name: "Multi-Session Workflow Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student designs multi-session workflows for complex projects with appropriate isolation"

  - name: "Context Isolation Strategy"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student applies task similarity scoring to decide session isolation vs combination"

learning_objectives:
  - objective: "Apply compression strategies including checkpoint summaries and session handoff documents"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Checkpoint document created from sample session transcript under 600 tokens"

  - objective: "Design multi-session workflows for complex projects spanning multiple work sessions"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Multi-session workflow plan with checkpoint strategy for 3+ session project"

  - objective: "Use context isolation to prevent pattern cross-contamination in parallel tasks"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Task similarity scoring and session isolation decision for task set"

  - objective: "Create effective session restart documents that restore context efficiently"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Session restart demonstrating preserved intelligence with under 1% context cost"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (checkpoint compression, session restart, multi-session workflow, context isolation, task similarity, contamination prevention) within B1 limit of 7-10"

differentiation:
  extension_for_advanced: "Research automatic summarization techniques; design hierarchical checkpoint systems for multi-week projects; analyze context switching costs from cognitive science research"
  remedial_for_struggling: "Focus on single compression: Take 10-minute conversation, identify 3 key decisions, write 3-sentence summary before learning full checkpoint methodology"
---

# Compression & Multi-Session Workflows

You've learned to design progressive loading strategies that prevent context degradation through intelligent Foundation, Current, and On-Demand allocation. Even with optimal loading, long sessions eventually approach context limits. You might be deep into valuable work---design decisions made, patterns established, progress documented---when you hit 85% utilization.

But there's another challenge: working on multiple unrelated tasks. When you mix unrelated work in the same session, patterns from Task A contaminate recommendations for Task B. Your authentication endpoint suggestions start appearing in CLI tool error handling.

**The questions**: How do you preserve session intelligence while reclaiming context space? And when should you isolate tasks into separate sessions versus working on them together?

In this lesson, you'll learn **context compression** and **multi-session workflows**: extracting key decisions into checkpoints, restarting with clean context, measuring task similarity, and designing workflows that keep context clean across complex projects.

## The Context Saturation Problem

Imagine you're 90 minutes into a development session:

```
Current session state (at 85% utilization):
- Foundation loaded: 25K tokens (CLAUDE.md, architecture.md)
- Current files: 50K tokens (3 API files, 2 test files)
- Conversation: 95K tokens (32 exchanges over 90 minutes)
- Total: 170K / 200K = 85% utilization

Work completed:
- Designed authentication flow (password + JWT)
- Decided on bcrypt hashing with 12 rounds
- Implemented rate limiting (5 attempts per hour)
- Discussed refresh token rotation strategy
- Created 3 test cases

Remaining work:
- Implement token blacklist for logout
- Add email verification flow
- Write integration tests

Problem: You're at 85% with 60+ minutes of work remaining.
```

You have three options:

**Option 1: Continue anyway** (risky)
- Context will degrade further
- AI will forget earlier decisions
- Quality drops, errors increase

**Option 2: Restart from scratch** (wasteful)
- Lose all session intelligence
- Re-explain decisions
- Rebuild context from zero

**Option 3: Create checkpoint and restart** (optimal)
- Compress session into summary
- Restart with clean context
- Restore key intelligence in under 600 tokens

This is where **checkpoint compression** becomes essential.

## The Checkpoint Structure

A checkpoint is a compressed summary of your session that preserves critical intelligence while discarding conversational noise.

### What Goes in a Checkpoint

| Section | What to Include | Why It Matters |
|---------|-----------------|----------------|
| **Architectural Decisions** | Key choices with reasoning, alternatives rejected | Prevents re-debating settled issues |
| **Progress Summary** | Features completed, current state | Shows where you are |
| **Next Steps** | Immediate tasks, blockers, dependencies | Enables seamless continuation |
| **Critical Context** | Non-obvious patterns, constraints, design principles | Captures tacit knowledge |

**Target size**: Under 600 tokens (leaves 199K+ for fresh work)

### What Does NOT Go in a Checkpoint

**Conversational details** (wasteful):
- "At 10:15 AM, you asked..." - Discard timestamps
- "I suggested X, then you said Y..." - Discard dialogue

**Obvious information** (redundant):
- "We're building an authentication system" - Already in project docs
- "Python uses indentation" - Common knowledge

**Exploratory dead-ends** (not actionable):
- "Briefly discussed microservices" - Not part of current scope

**Principle**: Checkpoint preserves **what you need to know** to resume effectively, not a complete transcript.

## Creating a Checkpoint: Collaborative Extraction

You're 90 minutes into the authentication session. Context is at 85%. Time to compress.

**Your request:**
"We've been working for 90 minutes and we're at 85% context utilization. I need to create a checkpoint so we can restart with clean context. Help me extract key decisions and progress."

**AI's initial draft** (720 tokens - too large):

```markdown
# CHECKPOINT - Authentication Session 2025-11-18

## Architectural Decisions Made:
1. **Authentication Method**: Password + JWT tokens
   - Why: Balance security with stateless API design
   - Rejected: OAuth (too complex for MVP), session cookies

2. **Password Security**: Bcrypt hashing, 12 rounds
   - Why: Industry standard, sufficient for threat model
   - Considered: Argon2 (better but overkill for scale)

3. **Rate Limiting**: 5 login attempts per hour per IP
   - Why: Prevent brute force without blocking retries
   - Implementation: In-memory store (acceptable for MVP)

4. **Token Strategy**: 15-minute access, 7-day refresh with rotation
   - Why: Short-lived access limits exposure
   - Rotation: Invalidate old refresh token when issuing new

## Progress Summary:
- Implemented POST /auth/login endpoint
- Implemented JWT generation and validation
- Created rate limiting middleware
- Wrote 3 tests: valid login, invalid password, rate limit

## Next Steps:
1. Token blacklist for logout
2. Email verification flow
3. Integration tests
4. API documentation

## Context to Preserve:
- Rate limit is IP-based; may need user-based later
- Refresh rotation invalidates old tokens; clients must handle 401
- Password reset deferred to v2

## Files Modified:
api/auth.py, api/middleware.py, tests/test_auth.py, models/user.py
```

**Your response:**
"This is 720 tokens - too large. Target is under 600. What can we compress?"

**AI's compressed version** (487 tokens):

```markdown
# CHECKPOINT - Auth Session 2025-11-18

## Key Decisions:
1. Auth: Password + JWT (15min access, 7d refresh with rotation)
2. Security: Bcrypt 12 rounds, rate limit 5/hour per IP
3. Schema: users(id, email, password_hash, refresh_token_hash)

## Completed:
- POST /auth/login functional
- Rate limiting middleware implemented
- 3 tests passing (valid login, invalid pw, rate limit)

## Next:
1. Token blacklist for logout
2. Email verification
3. Integration tests
4. API docs

## Critical Context:
- Rate limit IP-based; may need user-based if shared IP issues
- Refresh rotation invalidates old tokens; clients handle 401
- Password reset deferred to v2

## Files: api/auth.py, api/middleware.py, tests/test_auth.py
```

Through iteration, you arrived at a checkpoint that preserves essential decisions while discarding conversational noise---30% reduction while maintaining critical intelligence.

## Session Restart Protocol

Now that you have a checkpoint, here's how to restart effectively:

### Step 1: Save and End Current Session

Save checkpoint to `CHECKPOINT.md` in project root:

```bash
# Current session: 85% utilization, degradation likely
# Action: Save checkpoint, close session
```

### Step 2: Start New Session with Checkpoint

```
I'm resuming work on authentication from a previous session. Here's my checkpoint:

[Paste CHECKPOINT.md content]

What should we tackle first?
```

**Checkpoint loaded**: ~500 tokens (0.25% utilization)
**Context reclaimed**: 170K to 0.5K tokens = 169.5K freed (99.7% recovery)

### Step 3: Verify Context Restoration

**AI's response:**
"Based on your checkpoint, I understand:
- Password + JWT authentication implemented with bcrypt and rate limiting
- Tests passing for core login functionality
- Next priorities: token blacklist, email verification, integration tests

Let's start with the token blacklist. Since this is MVP, would you prefer in-memory or Redis?"

**Validation**: AI understood session state, remembered decisions, ready to proceed.

### When to Create Checkpoints

| Condition | Action |
|-----------|--------|
| Utilization > 80% AND session > 60 minutes | Create checkpoint NOW |
| Utilization > 70% AND remaining work > 30 minutes | Plan checkpoint soon |
| Degradation symptoms detected | Create checkpoint regardless |
| Utilization < 70% | Continue working |

**Principle**: Create checkpoints **before** degradation becomes severe, not after.

## The Context Pollution Problem

There's another reason to manage sessions carefully: **context pollution**.

Imagine working on two tasks in the same session:

```
TASK A (10:00-10:45): Implement REST API authentication
- Pattern: HTTP endpoints, JWT tokens, bcrypt hashing
- Files: api/auth.py, middleware/rate_limit.py

TASK B (10:45-11:30): Write CLI tool for data import
- Pattern: Command-line arguments, file parsing, batch processing
- Files: cli/import.py, parsers/csv_parser.py

At 11:30, you ask: "What's the best way to handle errors?"

AI's confused response:
"For error handling, you could return HTTP 401 for authentication
failures, or use exit codes for CLI errors, or log to stderr...
Which context are you asking about?"
```

**The problem**: Task A and Task B have **completely different patterns**. Mixing them creates:

1. **Contaminated recommendations**: AI suggests HTTP responses for CLI errors
2. **Lost focus**: AI can't distinguish which context applies
3. **Degraded quality**: Mixed patterns dilute specificity

**The solution**: **Context isolation**---use separate sessions for unrelated tasks.

## Task Similarity Scoring

Not all tasks need isolation. Some share enough patterns that working together **improves** context quality. The key is measuring **task similarity**.

### The Similarity Framework

| Characteristic | Points | Example |
|---------------|--------|---------|
| **Same domain** | +30 | Both authentication tasks |
| **Same data models** | +20 | Both work with User model |
| **Same service/component** | +20 | Both modify auth service |
| **Same file routes** | +15 | Both work in api/ folder |
| **Same test patterns** | +15 | Both need integration tests |

**Total possible**: 100 points

**Decision threshold**:
- **50+ points**: Work together (shared context adds value)
- **Under 50 points**: Isolate (patterns interfere)

### Scoring Examples

**High Similarity (Work Together)**:

```
Task A: Add password reset endpoint
Task B: Add email verification endpoint

Similarity Score:
- Same domain (authentication): +30
- Same data models (User): +20
- Same service (auth): +20
- Same files (api/auth.py): +15
- Same tests (API integration): +15
= 100 points --> WORK TOGETHER
```

**Low Similarity (Isolate)**:

```
Task A: REST API authentication (JWT)
Task B: CLI data import tool (CSV parsing)

Similarity Score:
- Same domain: 0 (API vs CLI)
- Same models: 0 (User vs CSV records)
- Same service: 0 (auth vs import)
- Same files: 0 (api/ vs cli/)
- Same tests: 0 (different patterns)
= 0 points --> ISOLATE
```

**Borderline (Judgment Call)**:

```
Task A: User profile endpoint (GET /users/:id)
Task B: Product search endpoint (GET /products/search)

Similarity Score:
- Same domain: 0 (users vs products)
- Same models: 0 (different)
- Same service: +20 (both API)
- Same files: +15 (both api/)
- Same tests: +15 (API tests)
= 50 points --> BORDERLINE

Decision: Acceptable together for short sessions, isolate for long ones.
```

## Multi-Session Workflow Patterns

When tasks require isolation, choose the right workflow pattern:

### Pattern 1: Sequential Isolation

**Use when**: Tasks are unrelated and can be done in any order.

```
Session 1: Complete Task A (authentication)
     |
   Close
     |
Session 2: Complete Task B (CLI import)
     |
   Close
```

### Pattern 2: Parallel with Checkpoints

**Use when**: Both tasks are long and need multiple sittings.

```
Session 1: Authentication work
     |
  Checkpoint (85% utilization)
     |
Session 2: CLI import work (fresh context)
     |
  Checkpoint
     |
Session 1 (resumed): Continue auth from checkpoint
```

### Pattern 3: Convergent Isolation

**Use when**: Tasks start isolated but need integration later.

```
Session 1: Authentication API (isolated)
     |                              |
  Checkpoint                  Session 2: Admin dashboard (isolated)
     |                              |
     +----------+----------+ Checkpoint
                |
          Session 3: Integration
           (loads BOTH checkpoints)
```

**Example use case**: Building authentication service and admin dashboard separately, then integrating admin authentication in a final session.

## Decision Framework Template

Use this framework when planning multi-session work:

```markdown
# Multi-Session Planning

## Step 1: Score Task Similarity
| Task Pair | Domain | Models | Service | Files | Tests | Total |
|-----------|--------|--------|---------|-------|-------|-------|
| A + B     | +30/0  | +20/0  | +20/0   | +15/0 | +15/0 | [?]   |
| A + C     | +30/0  | +20/0  | +20/0   | +15/0 | +15/0 | [?]   |

## Step 2: Apply Threshold
- 50+ points: Work together
- Under 50: Isolate

## Step 3: Choose Workflow Pattern
- Sequential: Unrelated, any order
- Parallel: Both long, need checkpoints
- Convergent: Isolated then integrated

## Step 4: Plan Checkpoints
- When will utilization approach 80%?
- What decisions must survive restart?
- What files for each session's Foundation/Current?
```

## Practice Exercises

### Exercise 1: Extract Checkpoint from Session

You're 2 hours into a session with this summary:

```
Session: API Documentation Generator

Decisions:
- OpenAPI spec as input format
- Markdown output (one file per endpoint)
- Group by resource: users/, products/, orders/
- Flag incomplete descriptions (don't generate placeholders)
- Code examples deferred to v2

Completed:
- OpenAPI parser (extracts endpoints, parameters, responses)
- Markdown template (Description, Parameters, Responses, Examples)
- 2 tests passing (basic endpoint, authenticated endpoint)

Remaining:
- Handle edge cases
- Add test coverage
- Support query parameters

Files: parser.py, template.py, tests/test_parser.py
Utilization: 88%
```

**Your assignment**:
1. Create checkpoint under 600 tokens
2. Identify what to KEEP vs DISCARD
3. Structure: Decisions, Progress, Next Steps, Critical Context
4. Estimate token count (~5 tokens per word)

### Exercise 2: Design Multi-Session Workflow

You're building an e-commerce platform:

```
Component A: Authentication service (2-3 hours)
Component B: Product catalog API (3-4 hours)
Component C: Shopping cart service (2-3 hours)
Component D: Payment integration (4-5 hours)
Component E: Admin dashboard (3-4 hours)

Dependencies:
- Payment (D) depends on Cart (C)
- Admin dashboard (E) needs Authentication (A)
```

**Your assignment**:
1. Calculate similarity scores between components
2. Identify dependency order
3. Design multi-session workflow:
   - How many sessions?
   - Which components per session?
   - When to use convergent pattern?
4. Plan checkpoint strategy

### Exercise 3: Diagnose Context Pollution

Read this mixed-task session:

```
[00:10] YOU: Implement user authentication with JWT.
AI: [Implements endpoint]

[00:45] YOU: Now implement CSV import for products.
AI: [Implements parser]

[01:15] YOU: Add error handling.
AI: For errors, you could:
1. Return HTTP 401/403 for auth failures
2. Log to stderr for import failures
3. Store failed rows in error.csv
Which context?

[01:20] YOU: I meant import.
AI: OK, logging to stderr. Also add token refresh?

[01:25] YOU: Yes.
AI: Token refresh for... JWT auth or import progress tracking?
```

**Your assignment**:
1. Identify pollution symptoms (where AI gets confused)
2. Calculate similarity score for auth vs import
3. Recommend session structure
4. Rewrite session plan using isolation

## Try With AI

Practice compression and multi-session strategies with Claude Code.

### Setup
Open Claude Code with a long development session or planned multi-task work.

### Prompt 1: Request Checkpoint Extraction

```
We've been working for [N] minutes and context utilization is at [X%].
I need a checkpoint to preserve progress before restarting.

Extract:
1. Key architectural decisions (with reasoning)
2. What we completed
3. What's remaining
4. Critical context that shouldn't be forgotten

Target: under 600 tokens while preserving everything essential.
```

**What you're learning**: How to distinguish essential decisions from conversational noise---the core skill of checkpoint creation.

### Prompt 2: Task Similarity Analysis

```
I have [N] tasks to complete:
1. [Task A]
2. [Task B]
3. [Task C]

Calculate similarity scores:
- Same domain: +30
- Same data models: +20
- Same service/component: +20
- Same file routes: +15
- Same test patterns: +15

For each pair, recommend work together (50+) or isolate (under 50).
```

**What you're learning**: How to systematically evaluate whether tasks will benefit from shared context or suffer from pollution.

### Prompt 3: Test Session Restart

```
[In NEW session]

I'm resuming work from a previous session. Here's my checkpoint:
[Paste checkpoint]

What's our current state, and what should we work on next?
```

**What you're learning**: How to verify checkpoint quality---does AI understand context immediately, or does it need clarification?

**Note on safety**: When starting fresh sessions with checkpoints, verify AI's understanding before proceeding with complex work. If restoration feels incomplete, your checkpoint may need more detail about constraints and decisions.
