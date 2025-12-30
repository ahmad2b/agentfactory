---
sidebar_position: 5
title: "Progressive Loading and Memory Files"
description: "Design three-tier context loading strategies and persistent memory files for multi-session AI collaboration"
sidebar_label: "Progressive Loading & Memory Files"
keywords: [progressive loading, memory files, CLAUDE.md, context strategy, architecture.md, decisions.md, persistent intelligence]
chapter: 12
lesson: 5
duration_minutes: 40
proficiency: "B1"
concepts: 6

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Progressive Loading Strategy"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student applies Foundation/Current/On-Demand loading strategy to real projects"

  - name: "Memory File Architecture"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student creates CLAUDE.md, architecture.md, and decisions.md for projects"

  - name: "Context Persistence Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student evaluates when to use memory files versus session context"

learning_objectives:
  - objective: "Apply three-phase loading strategy (Foundation, Current, On-Demand) to manage context efficiently"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Loading strategy document with tier allocation and token budget"

  - objective: "Design CLAUDE.md memory files for project convention persistence"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "CLAUDE.md file with conventions, patterns, and anti-patterns"

  - objective: "Create architecture.md and decisions.md for multi-session continuity"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Memory file set demonstrating cross-session intelligence"

  - objective: "Evaluate when to use memory files versus session-only context"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Decision analysis comparing persistence strategies for different scenarios"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (three loading tiers, CLAUDE.md structure, architecture.md design, decisions.md ADR format, persistence strategy, memory vs session tradeoffs) within B1 limit of 7-10"

differentiation:
  extension_for_advanced: "Research context caching strategies; design automated memory file updates triggered by git commits; compare memory files to ADRs in enterprise architecture"
  remedial_for_struggling: "Focus on binary categorization (Always load vs Sometimes load) before three-tier framework; create single CLAUDE.md with 3 conventions before full memory architecture"
---

# Progressive Loading and Memory Files

You've been working on a FastAPI project for three weeks. Across a dozen sessions, you've made decisions: SQLAlchemy query API instead of ORM, Argon2 for password hashing, structured JSON logging. You've established patterns and identified anti-patterns to avoid.

Then you start a fresh session Monday morning.

Claude has no memory of those decisions. You find yourself re-explaining: "We use SQLAlchemy query API, not ORM." "Password hashing is Argon2, not bcrypt." "Never log sensitive data." Every session, the same context re-establishment.

This isn't just inefficient---it's risky. Without your project's accumulated knowledge, AI might suggest patterns you've already rejected, contradicting architectural decisions you made for good reasons.

This lesson solves two connected problems: **how to load context efficiently within a session** (progressive loading) and **how to preserve intelligence across sessions** (memory files). Together, they transform AI collaboration from repetitive setup to continuous, context-aware partnership.

## Part 1: Progressive Loading Strategy

### The Context Allocation Problem

Imagine starting a documentation project with 50 markdown files. Your instinct might be: "Load everything so AI has full context."

But loading all 50 files immediately creates problems:

| Problem | Impact |
|---------|--------|
| **Context saturation** | 60% of context used before work begins |
| **Wasted capacity** | Only 10 files relevant to today's task |
| **On-demand handicap** | No room to load reference files mid-session |
| **Degradation risk** | AI loses focus in context overload |

The alternative---load selectively---requires strategy. Which files when? That's where progressive loading becomes essential.

### The Three-Tier Loading Model

Progressive loading divides context into three tiers, each serving a distinct purpose:

**Tier 1: Foundation (Always Loaded)**

Purpose: Core patterns that apply to ALL tasks in this project.

What belongs here:
- Project conventions (CLAUDE.md)
- System architecture (architecture.md)
- Key decisions (decisions.md)
- Critical reference files that guide every task

Size target: 10-15% of context window (~20-30K tokens for Claude Sonnet)

Foundation provides consistent context across sessions. Without it, AI starts every session from zero, requiring you to re-establish patterns repeatedly.

**Tier 2: Current (Task-Specific)**

Purpose: Files relevant to TODAY'S specific task.

What belongs here:
- Files you're actively editing
- Related documentation that informs this work
- Dependencies that this task touches

Size target: 20-30% of context window (~40-60K tokens)

Current tier provides focused context without overwhelming the session with everything that *might* be relevant.

**Tier 3: On-Demand (Fetch As Needed)**

Purpose: Reference files loaded only when explicitly needed.

What belongs here:
- Examples from other sections (fetch if AI asks "Can I see example X?")
- Technical specifications (load when needed for validation)
- Archive files (older decisions, legacy patterns)

Size reserved: 30% of context window (~60K tokens)

On-demand reserve prevents preloading waste. You've protected capacity for mid-session needs without committing it upfront.

### Example Loading Strategy

For a documentation project where today's task is writing a specific chapter:

```markdown
## Context Budget

Foundation (Always): 18K tokens (9%)
- CLAUDE.md: ~8K tokens (core conventions)
- chapter-index.md: ~10K tokens (cross-reference structure)

Current (Today's Task): 18K tokens (9%)
- style-guide.md: ~7K tokens (fresh version each session)
- current-chapter/outline.md: ~5K tokens
- previous-chapter/final-lesson.md: ~6K tokens (consistency check)

Conversation Space: ~80K tokens (40%)

On-Demand Reserve: ~60K tokens (30%)
- Other chapter files (available if needed)
- Historical examples

Safety Buffer: ~24K tokens (12%)

TOTAL: 200K tokens
```

Total preload (Foundation + Current) is under 20%---well within the 35% recommendation.

### Tier Classification Decision Framework

When deciding which tier a file belongs in, ask:

| Question | If YES | If NO |
|----------|--------|-------|
| Does this apply to EVERY task? | Foundation | Current or On-Demand |
| Does this file change frequently? | Current (fresh each session) | Foundation (stable) |
| Am I actively editing this today? | Current | On-Demand |
| Is this "might need" vs "definitely need"? | On-Demand | Foundation or Current |
| Can I work without it initially? | On-Demand | Foundation or Current |

## Part 2: Memory Files for Persistent Intelligence

Progressive loading tells you HOW to load context within a session. But what about ACROSS sessions? That's where memory files become essential.

### The Cross-Session Problem

Each Claude Code session starts fresh. Decisions made Tuesday are forgotten by Thursday. The architectural choices, patterns discovered, and anti-patterns identified---all lost.

Memory files solve this by **documenting project intelligence in files AI reads at session start**.

Instead of re-explaining the same decisions, you document them once. Every new session, AI reads these files first, restores context, and continues work with full understanding.

### Three Memory Files

Your project needs three memory files, each serving a specific purpose:

**1. CLAUDE.md (Project Conventions)**

Purpose: Operational guidelines AI should follow.

Contains:
- Naming conventions
- File organization rules
- Technology choices
- Anti-patterns to avoid

Example structure:

```markdown
# CLAUDE.md - Project Conventions

## Overview
FastAPI backend with PostgreSQL, Redis cache, React frontend.

## Database
- ORM: SQLAlchemy query API (not ORM pattern)
- Migrations: Alembic in migrations/ folder
- Connection: async pool via asyncpg

## Authentication
- Password hashing: Argon2 (never bcrypt)
- Token expiry: 24 hours
- Session blacklist: Redis

## Logging
- Format: Structured JSON
- Never log: passwords, tokens, PII
- Log level: INFO for production

## Anti-Patterns (What NOT to Do)
- Never use ORM lazy loading (causes N+1)
- Never store secrets in code (use env vars)
- Never skip input validation
```

**2. architecture.md (System Design)**

Purpose: How components relate, which files matter, design patterns.

Contains:
- Component relationships
- Key files and their purposes
- Design patterns in use
- System properties

Example structure:

```markdown
# System Architecture

## Components

### API Layer
- Framework: FastAPI
- Entry point: app/main.py
- Routes: app/routes/

### Database Layer
- Models: app/models/ (SQLAlchemy)
- Migrations: migrations/ (Alembic)
- Connection: app/database.py

### Services
- auth_service: Token management, login
- payment_service: Stripe integration
- email_service: Async email sending

## Key Files Map
- app/main.py: Application entry
- app/models/user.py: User entity
- app/services/auth.py: Authentication logic
- app/routes/auth.py: Auth endpoints

## Design Patterns
- Repository pattern for database access
- Dependency injection via FastAPI
- Event-driven for background tasks
```

**3. decisions.md (Architectural Decision Records)**

Purpose: WHY decisions were made, what alternatives were rejected.

Contains:
- Decision statements
- Context and rationale
- Alternatives considered
- Consequences accepted

Example structure:

```markdown
# Architectural Decisions

## ADR-001: SQLAlchemy Query API Over ORM

**Decision**: Use query API for all database operations.

**Context**: Early project had N+1 query issues with ORM lazy loading.

**Rationale**:
- Explicit control over SQL generation
- Easier to optimize complex queries
- Still maintains schema safety

**Alternatives Rejected**:
- Raw SQL: Lost type safety
- Full ORM: Performance issues

**Consequences**: Team must understand SQL optimization.

---

## ADR-002: Argon2 for Password Hashing

**Decision**: Use Argon2 with recommended parameters.

**Context**: Security audit recommended modern algorithm.

**Rationale**:
- Resistant to GPU/ASIC attacks
- Configurable memory/time cost
- OWASP recommended

**Alternatives Rejected**:
- bcrypt: Older, less resistant to hardware attacks
```

### When to Use Memory Files vs Session Context

| Scenario | Use Memory Files | Use Session Context |
|----------|-----------------|-------------------|
| Project conventions that rarely change | Yes | No |
| Today's specific task files | No | Yes (Current tier) |
| Architectural decisions | Yes | Reference as needed |
| Files you're actively editing | No | Yes (Current tier) |
| Cross-session continuity needed | Yes | No |
| One-time exploration | No | Yes (temporary) |
| Team collaboration (shared knowledge) | Yes | No |

Memory files are for **persistent project intelligence**. Session context is for **immediate task focus**.

### Memory File Maintenance

**When to update each file:**

| Trigger | File to Update |
|---------|---------------|
| Discovered new pattern | CLAUDE.md |
| Changed technology choice | CLAUDE.md + architecture.md |
| Made architectural decision | decisions.md |
| Added new component | architecture.md |
| Found anti-pattern to avoid | CLAUDE.md |
| Reversed previous decision | decisions.md (add new ADR, mark old as superseded) |

**Update protocol:**

For non-breaking changes (clarifications):
- Update file directly
- No special marking needed

For breaking changes (reversing decisions):
- Add new ADR explaining the change
- Mark old ADR as "SUPERSEDED by ADR-XXX"
- Keep old ADR for historical context

### Connecting Loading Strategy to Memory Files

Memory files are part of your **Foundation tier**. They're loaded at the start of every session:

```markdown
Foundation (Always Loaded):
- CLAUDE.md: ~5K tokens (project conventions)
- architecture.md: ~4K tokens (system design)
- decisions.md: ~6K tokens (key ADRs)

Total Foundation from Memory Files: ~15K tokens (7.5%)
```

This foundation ensures every session starts with your project's accumulated intelligence---decisions, patterns, and constraints---without re-explanation.

## Practice Exercise: Design Your Loading and Memory Strategy

For a project you're working on (or use this example):

**Project**: E-commerce API with authentication, products, and orders
**Files**: 30+ source files, 10+ test files, 5+ docs

**Your assignment:**

1. **Classify into tiers**: List 5 files for Foundation, 5 for Current (today: adding payment webhook), 5 for On-Demand

2. **Calculate token budget**: Estimate tokens per tier, verify total preload under 35%

3. **Create CLAUDE.md skeleton**: Write 3 conventions, 2 anti-patterns for this project

4. **Write one ADR**: Document a decision (e.g., "Why we chose Stripe over PayPal")

5. **Design update triggers**: When would you update each memory file?

## Try With AI

**Prompt 1 - Design Loading Strategy:**

```
I'm working on a [project type] with [N] files. Here's my structure:
[List key files and estimated sizes]

Today's task: [specific work]

Help me design a Foundation/Current/On-Demand loading strategy.
Calculate my token budget and verify I'm under 35% preload.
```

**What you're learning:** How to apply the three-tier model to real projects and calculate context budgets that prevent degradation.

**Prompt 2 - Create Memory Files:**

```
Help me create memory files for my [describe project: tech stack,
domain, size]. I need:

1. CLAUDE.md with our conventions
2. architecture.md with component relationships
3. decisions.md with key ADRs

Ask me clarifying questions about patterns, decisions, and
anti-patterns to populate these files accurately.
```

**What you're learning:** How to extract implicit project knowledge into explicit, persistent documentation that AI can reference across sessions.

**Prompt 3 - Evaluate Persistence Strategy:**

```
For this scenario, should I use memory files or session context?

Scenario 1: I'm trying a new library to see if it fits our needs
Scenario 2: We decided to switch from REST to GraphQL
Scenario 3: I'm debugging a specific test failure today
Scenario 4: Our team agreed on new naming conventions

Explain your reasoning for each.
```

**What you're learning:** How to evaluate the persistence tradeoff---when to invest in memory files versus when session-only context is sufficient.

**Safety Note**: Memory files become your project's source of truth for AI collaboration. Keep them accurate---outdated memory files can cause AI to suggest patterns you've already rejected. Update them as your project evolves.
