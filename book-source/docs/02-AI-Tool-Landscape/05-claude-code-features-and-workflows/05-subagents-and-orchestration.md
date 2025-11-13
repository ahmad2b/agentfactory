---
sidebar_position: 5
title: "Subagents and Orchestration"
duration: "8-10 min"
---

# Subagents and Orchestration

You've installed Claude Code and run your first commands. But as you use it more, you'll encounter a fascinating behavior: Claude Code automatically delegates certain types of work to specialized agents. Understanding this pattern reveals how AI orchestration works—and prepares you for building sophisticated agent systems later.

## The Problem: Context Drift in Long Conversations

Imagine this scenario: You're working on a Python project. You ask Claude Code to help debug a function, then to explain a complex module, then to find all error handlers in the codebase. By the time you're on your fifth request, Claude Code's context contains all your previous conversations—debugging details, explanations, error handler discussions. The conversation becomes cluttered.

**What if specialized assistants automatically handled different types of work without accumulating this clutter?**

That's what **subagents** enable—and Claude Code uses them automatically behind the scenes to give you better, faster results.

---

## What Are Subagents?

**Definition**: A subagent is a specialized AI assistant that Claude Code automatically invokes (or you can invoke explicitly) for specific types of tasks. Each subagent has focused expertise and isolated context—preventing the clutter that builds up in long conversations.

Think of Claude Code as an intelligent orchestrator with a team of specialists:

- **Main Claude Code (Orchestrator)**: Handles general requests, decides which specialist to invoke
- **Explore Agent (Codebase Search Specialist)**: Fast, efficient searching across codebases to find patterns, definitions, and usage
- **Plan Agent (Multi-Step Task Specialist)**: Breaks complex tasks into phases before execution
- **Custom Agents (Advanced)**: You can create specialized agents for team-specific workflows (covered in Part 5)

**Key insight**: Most of the time, you won't explicitly request a subagent—Claude Code decides when to delegate based on your query. Your job is to recognize when delegation is happening and understand why it's beneficial.

---

## Why Subagents Matter: Context Preservation and Specialization

### Concept 1: Context Preservation

**Problem Without Subagents**: After 10 interactions in the main conversation, Claude Code's context is filled with unrelated discussions. Asking for help with a new task means Claude considers all previous context—even if it's irrelevant.

**Solution With Subagents**: Claude Code launches a fresh subagent for each focused task. Each subagent operates in clean context, without clutter from previous work.

**Example**: You ask "Where are all error handlers in this codebase?" Claude Code recognizes this as a search task and automatically invokes the Explore agent, which searches with fresh context—not burdened by your earlier conversations.

### Concept 2: Specialization and Consistency

**Problem Without Subagents**: If you work on complex, multi-step tasks repeatedly, you must re-explain your approach each time.

**Solution With Subagents**: Specialized agents encode focused instructions. They execute consistent, repeatable patterns without requiring re-explanation.

**Example**: A code review task could use a specialized agent that knows your team's style guide, type hint requirements, and security standards—applying these consistently every time.

### Concept 3: Orchestration Pattern

**Key Pattern**: Claude Code acts as an intelligent coordinator, recognizing task types and delegating to the right specialist. This is the foundation of AI orchestration.

**You don't command the delegation**—Claude Code decides. Your job is to:
1. State what you want clearly (clear specification)
2. Recognize which agent Claude invoked (observe the behavior)
3. Understand why the delegation happened (learn the pattern)

---

## The Explore Agent: Automatic Codebase Search

When you ask Claude Code to find patterns, locate definitions, or understand code structure across files, Claude Code automatically invokes the **Explore Agent**—a specialist designed for fast, efficient codebase navigation.

### When Claude Invokes Explore

Claude recognizes these patterns and invokes Explore automatically:

- **Search queries**: "Find all API endpoints in this codebase"
- **Pattern discovery**: "Where are error handlers defined?"
- **Definition lookup**: "Show me how `authenticate()` is implemented"
- **Usage analysis**: "Which functions call this utility?"
- **Rapid orientation**: "Give me a map of this project structure"

### What Explore Does

The Explore Agent:
1. **Scans rapidly** across multiple files using pattern matching (much faster than manual browsing)
2. **Identifies locations** efficiently without reading irrelevant code
3. **Returns targeted results** with file paths and context snippets
4. **Provides orientation** helping you understand code structure quickly

### How to Recognize Explore Is Working

When you ask a search or pattern-discovery question, watch for these signals:

- **Speed**: Explore returns results quickly (within seconds, not minutes)
- **Multiple files**: Results reference several files with line numbers
- **Pattern matching**: Results group related code by pattern, not just keyword
- **Targeted context**: Results show relevant code snippets with context

**Example observation**:
```
You ask: "Find all network error handlers in this codebase"

Claude Code (via Explore):
- Scans multiple files quickly
- Finds handlers in: src/api/handlers.py (lines 42-67), src/utils/network.py (lines 15-28)
- Returns summary with code context
- All done in < 5 seconds
```

**What you learned**: That was the Explore Agent at work. The speed and pattern-matching precision indicate specialized search, not a conversation response.

---

## Plan Mode: Breaking Complex Tasks Into Phases

When you ask Claude Code to handle a complex, multi-step task, Claude Code enters **Plan Mode**—automatically breaking the work into phases before execution.

### When Claude Enters Plan Mode

Claude recognizes these patterns and enters Plan Mode automatically:

- **Multi-step refactoring**: "Add user authentication to this project"
- **Feature implementation**: "Implement OAuth login with social providers"
- **Complex bug fixes**: "Debug and fix the performance issue that affects 50% of requests"
- **Architecture changes**: "Migrate from sync to async handlers"
- **Large-scale changes**: "Refactor this service to use dependency injection"

### What Plan Mode Does

In Plan Mode, Claude:
1. **Analyzes the task** holistically
2. **Breaks it into phases** with clear dependencies
3. **Identifies prerequisites** and constraints
4. **Sequences execution** optimally
5. **Iterates within each phase** (implement → validate → move to next)

### How Plan Mode Works

**Example: User Authentication Implementation**

You ask: "Add user authentication to this project"

Claude enters Plan Mode and proposes:

```
Phase 1: Foundation
- Create database schema (users table, session table)
- Set up ORM models with type hints
- Add environment variable structure

Phase 2: Core Auth Logic
- Implement password hashing (bcrypt)
- Create login/logout endpoints
- Build session management

Phase 3: Integration
- Add middleware for protected routes
- Wire authentication into existing endpoints
- Create login UI component

Phase 4: Testing and Validation
- Add unit tests for auth functions
- Test login/logout flow end-to-end
- Verify password security
```

**What you learned**: Plan Mode doesn't just generate code—it orchestrates thinking. You see the dependency chain (why Phase 2 depends on Phase 1), can approve/reject phases, and understand the sequencing logic.

### How to Recognize Plan Mode

When you ask a complex task, watch for these signals:

- **Phase breakdown**: Claude proposes numbered phases with clear boundaries
- **Dependencies identified**: Each phase explains why it depends on previous phases
- **Sequential execution**: Phases execute in order, with checkpoints between
- **Strategic thinking**: The breakdown reflects architecture, not just code order

**What you learned**: This hierarchical breakdown is Plan Mode at work—intelligent orchestration recognizing complexity and sequencing work strategically.

---

## Real-World Examples

### Example 1: Explore Agent in Action

**Scenario**: You inherit a legacy Python project. You need to understand how authentication is implemented across the codebase.

**Your query**:
```
Search for all authentication-related functions in this codebase.
Show me where they're defined, what they do, and how they connect.
```

**What happens**:
- Claude invokes Explore automatically
- Explore scans all `.py` files using pattern matching
- Returns: auth functions in `auth.py` (lines 10-50), middleware in `middleware.py` (lines 75-90), usage in three endpoints

**What you see**: Fast, targeted results. Multiple files. Pattern-based grouping.

**What you learned**: That's the Explore Agent—designed for rapid codebase orientation.

### Example 2: Plan Mode in Action

**Scenario**: You need to refactor a Flask app to use async/await for better performance.

**Your query**:
```
Plan how to refactor this Flask app to use async/await.
Break it into phases with dependencies.
```

**What happens**:
- Claude enters Plan Mode
- Proposes 4 phases: Foundation (async setup), Route conversion, Database adaptation, Testing
- Explains dependencies: Why you must set up async first, why routes depend on database refactoring

**What you see**: Hierarchical breakdown. Strategic sequencing. Explicit dependencies.

**What you learned**: That's Plan Mode—Claude orchestrating complex work by breaking it into digestible phases with clear dependencies.

---

## Orchestration Pattern: The Key Insight

Here's the core pattern underlying subagents:

1. **You specify intent clearly** — "Find error handlers" or "Refactor to async"
2. **Claude recognizes task type** — Is this search? Complex multi-step? Routine?
3. **Claude delegates to specialist** — Explore for search, Plan for complex tasks
4. **Specialist executes efficiently** — Focused context, specialized approach
5. **Results return to you** — You remain in control

**This is orchestration**: Intelligent coordination of specialized workers toward a goal. In simple projects, orchestration is automatic (Explore and Plan modes). In advanced projects (Part 5/6), you build custom orchestration with competitive agents, parallel execution, and sophisticated delegation patterns.

---

## Tier 3: Advanced Orchestration (Conceptual Preview)

As you progress to advanced work (Part 5 and beyond), you'll encounter more sophisticated orchestration patterns:

### Competitive Subagents

Multiple agents propose solutions to the same problem; you choose the best. Example: Two design patterns for authentication (Passport vs OAuth libraries), each proposed by a specialist agent.

### Parallel Orchestration

Multiple agents work simultaneously on independent tasks. Example: While one agent writes tests, another writes documentation, another optimizes performance—all working on the same feature.

### Hierarchical Orchestration

Agents coordinate at multiple levels. Example: Main agent orchestrates feature development; code-review agent validates; security agent checks for vulnerabilities; all in parallel.

**Important**: These advanced patterns are Part 5/6 content. You're learning the **concept** now so you recognize it when you encounter it later. You won't build competitive agents or hierarchical systems yet—that's for advanced chapters. For now, understand that automatic Explore and Plan modes demonstrate the orchestration principle.

---

## When to Recognize Subagent Patterns

Here's a quick reference for recognizing when Claude Code is using subagents:

| Task Type | Agent Invoked | Recognition Signal | Duration |
|-----------|---------------|-------------------|----------|
| **Search patterns** | Explore | Fast scanning, multiple files, pattern-grouped results | < 5 sec |
| **Find definitions** | Explore | Rapid location of code across files with context | < 5 sec |
| **Multi-step work** | Plan | Phase breakdown with dependencies identified | Varies by task |
| **Complex refactoring** | Plan | Sequential phases with prerequisites explained | Varies by task |
| **One-off questions** | Main Claude | Conversational response, considers all context | Variable |

---

## Hands-On: Working With Subagents

This section contains practical exercises you can run immediately in Claude Code to observe orchestration in action.

### Exercise 1: Observe the Explore Agent in Action

**Goal**: Trigger the Explore agent and watch for the signals that indicate automatic delegation.

**Setup**: Navigate to a Python project with multiple files:

```bash
cd /path/to/your/python/project
claude
```

**What to ask**:

```
Find all functions in this codebase that handle file I/O operations.
List the file path, function name, and what it does for each.
```

**What to notice**:

- **Speed**: Results come back within 2-5 seconds (not minutes)
- **Pattern matching**: Results are grouped by function type (read, write, append), not just keyword matches
- **Multiple files**: Results reference several files with specific line numbers
- **Context snippets**: Each result shows 1-2 lines of relevant code

**Reflection**: That speed and pattern-matching precision? That's the Explore Agent working. It's specialized for codebase search. If Claude Code just read through files in conversation mode, it would be much slower.

**Follow-up experiment**: Ask a different search question:

```
Where are all error handling blocks in this codebase?
Show me try/except blocks and what exceptions they catch.
```

Notice the same signals again. Explore gets faster and more accurate the more you use it because it learns your code patterns.

---

### Exercise 2: Trigger Plan Mode for a Complex Task

**Goal**: Ask Claude Code for a complex, multi-step task and observe Plan Mode breaking it into phases.

**What to ask**:

```
Plan how to add user authentication to this project.
Break it into phases with clear dependencies.
Explain why each phase depends on previous phases.
```

**What to notice**:

- **Phase breakdown**: Claude proposes 3-5 numbered phases with titles
- **Dependencies identified**: Each phase explicitly states which previous phase it depends on
- **Strategic sequencing**: Phases aren't arbitrary—they follow logical/architectural order
- **Prerequisites listed**: Claude identifies what must be ready before each phase starts

**Example phase output** (what you should see):

```
Phase 1: Foundation
- Why first: Establishes database schema and ORM models
- Create users table with hashed password field
- Set up session table for token storage

Phase 2: Core Logic
- Why here: Depends on Phase 1 (needs schema)
- Implement password hashing (bcrypt)
- Build login/logout endpoints
- Create session management

Phase 3: Integration
- Why here: Depends on Phases 1-2
- Add authentication middleware
- Protect existing endpoints
- Add login UI
```

**Reflection**: This isn't Claude Code just listing steps. This is Plan Mode—an agent specialized in breaking complex work into orchestrated phases. Notice how dependency chains make sense: Phase 2 can't happen without Phase 1's schema.

**Follow-up**: Ask for feedback on the plan:

```
What if we wanted to add API key authentication as an alternative to user/password?
Where would that fit in your phase breakdown?
Would it change the order or dependencies?
```

Watch how Claude adapts the plan based on new constraints. That's orchestration responding to requirements.

---

### Exercise 3: Distinguish Main Conversation vs. Subagent Delegation

**Goal**: See the difference between asking a question (main conversation) vs. asking for a task (subagent delegation).

**In Claude Code, try both**:

**Main Conversation (no subagent)**:

```
Explain what dependency injection is in Python.
Give me a simple example.
```

**Watch for**: A conversational response that stays in the main conversation. Claude answers based on its training knowledge. No special signals, no delegation.

**Now ask a task-oriented question (triggers Explore)**:

```
Show me how dependency injection is used in this codebase.
Find all places where it's imported or instantiated.
```

**Watch for**: Different behavior. Claude might invoke Explore. You see file references, line numbers, pattern grouping.

**The difference**:
- "Explain X" → Main conversation (general knowledge, conversational)
- "Find X in this codebase" → Explore agent (rapid pattern matching, multiple files)

This distinction is crucial: different task types delegate to different specialists.

---

## Try With AI

Use Claude Code for these exercises. If you have another AI companion tool available (ChatGPT, Gemini), you can use that instead—the concepts are the same.

### Prompt 1: Recognize the Explore Agent

In a project directory with Claude Code:

```
cd /path/to/your/project
claude "Search this codebase for all functions that handle HTTP errors.
Show me the files, line numbers, and what each error handler does."
```

**Watch for**: Fast scanning, multiple files referenced, pattern-grouped results (not just keyword matches). If you see these signals within seconds, Explore Agent is at work.

**Expected outcome**: A summary showing error handlers across multiple files with locations and brief descriptions.

### Prompt 2: Understand Plan Mode

```
claude "Plan how I would add email notifications to this project.
Break it into phases with clear dependencies between phases."
```

**Watch for**: Phase-by-phase breakdown (Phase 1, Phase 2, etc.), explicit dependency explanations ("Phase 2 depends on Phase 1 because..."), strategic sequencing.

**Expected outcome**: A multi-phase breakdown with clear rationale for why each phase must happen in order.

### Prompt 3: Evaluate the Pattern

```
claude "Explain the difference between how you handled the search query
(Prompt 1) and the planning query (Prompt 2). What agent handled each? Why?"
```

**Watch for**: Claude explaining that search uses Explore (fast pattern matching), planning uses Plan mode (phase breakdown). This metacognitive understanding confirms you recognize orchestration.

**Expected outcome**: Clear explanation of when/why orchestration happens and which agent/mode handles different task types.
