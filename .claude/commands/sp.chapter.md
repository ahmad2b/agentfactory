---
description: Execute research-first chapter creation. Builds expertise skill BEFORE writing content. Use for new technical chapters requiring deep understanding of frameworks/libraries.
handoffs:
  - label: Skip to Content
    agent: sp.autonomous
    prompt: Skip skill creation, proceed with content
    send: true
---

# /sp.chapter: Research-First Chapter Creation (v1.0)

**Purpose**: Build deep expertise BEFORE writing content. Creates a programmatic skill for the technical domain, tests it on real projects, then uses that expertise to write high-quality chapter content.

**When to Use**: Creating new technical chapters (Part 6-7) that teach frameworks, SDKs, or tools.

---

## User Input

```text
$ARGUMENTS
```

---

## The Two-Phase Approach

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE A: SKILL RESEARCH & CREATION               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Fetch official docs (Context7, DeepWiki)                       │
│  2. Research community patterns (WebSearch)                         │
│  3. Build programmatic skill with:                                  │
│     ├── Persona (who is this skill?)                               │
│     ├── Logic (decision trees, workflows)                          │
│     ├── Context (what it needs to know)                            │
│     ├── MCP (tool integrations)                                    │
│     ├── Data/Knowledge (embedded expertise)                        │
│     └── Safety & Guardrails                                        │
│  4. Test skill on real projects                                     │
│  5. Validate skill works                                            │
│                                                                     │
│  OUTPUT: .claude/skills/[framework-name]/SKILL.md                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE B: CHAPTER CREATION                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  With deep expertise encoded in skill:                              │
│  /sp.specify → /sp.clarify → /sp.plan → /sp.tasks →                │
│  /sp.analyze → /sp.taskstoissues → /sp.implement →                 │
│  validators → update tasks.md (close issues) →                      │
│  /sp.git.commit_pr                                                  │
│                                                                     │
│  The skill IS the research - no hallucination risk                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## PHASE A: SKILL RESEARCH & CREATION

### Step A.1: Identify the Technical Domain

From user input, extract:
- **Framework/SDK**: e.g., "OpenAI Agents SDK", "Google ADK", "Anthropic Agents Kit"
- **Chapter Number**: e.g., "Ch 34", "Ch 37"
- **Running Example**: TaskManager Agent (from Part 6 framing)

### Step A.2: Research Official Documentation

**Invoke skills in sequence:**

```
1. Skill: researching-with-deepwiki
   Args: "[framework] architecture patterns examples"

2. Skill: fetching-library-docs
   Args: "[framework] official documentation via Context7"
```

**Capture from official docs:**
- Core concepts and terminology
- API patterns and signatures
- Best practices from maintainers
- Common pitfalls documented

### Step A.3: Research Community Patterns

**Use WebSearch for:**
- "[framework] real world examples"
- "[framework] production patterns"
- "[framework] vs alternatives comparison"
- "[framework] common mistakes"

**Capture from community:**
- How practitioners actually use it
- Patterns that emerged from production
- Edge cases and gotchas
- Integration patterns with other tools

### Step A.4: Design the Skill Architecture

**The skill must include these components:**

```yaml
# Skill Architecture Template
skill-name/
├── SKILL.md
│   ├── Frontmatter
│   │   ├── name: building-with-[framework]
│   │   └── description: "Use when building [type] with [framework]..."
│   └── Body
│       ├── ## Persona
│       │   └── Who is this skill? Expert role definition
│       ├── ## Core Concepts
│       │   └── Essential understanding (from official docs)
│       ├── ## Decision Logic
│       │   └── When to use what pattern (decision trees)
│       ├── ## Workflow
│       │   └── Step-by-step procedures
│       ├── ## MCP Integration
│       │   └── How to connect with MCP servers
│       ├── ## Safety & Guardrails
│       │   └── What to avoid, error handling
│       └── ## TaskManager Example
│           └── How to build TaskManager with this framework
│
├── references/
│   ├── api-patterns.md      # API signatures and usage
│   ├── examples.md          # Code examples from research
│   └── community-wisdom.md  # Patterns from practitioners
│
├── scripts/
│   └── verify-[framework].py  # Test the skill works
│
└── assets/
    └── templates/            # Starter templates if needed
```

### Step A.5: Build the Skill

**Use skill-creator to build:**

```
Skill: creating-skills
Args: "Create skill for [framework] with research from Phase A"
```

**Skill MUST include:**

1. **Persona** - Expert identity
   ```markdown
   ## Persona
   You are a [Framework] expert who has built production systems.
   You understand both the official patterns and community wisdom.
   ```

2. **Logic** - Decision trees
   ```markdown
   ## When to Use What

   | Situation | Pattern | Why |
   |-----------|---------|-----|
   | Simple agent | Single-agent | Less overhead |
   | Complex workflow | Multi-agent | Separation of concerns |
   | Tool-heavy | MCP integration | Standard connectivity |
   ```

3. **Context** - What it needs to know
   ```markdown
   ## Essential Context

   Before building, always check:
   - [ ] Python version compatibility
   - [ ] Required dependencies
   - [ ] API key configuration
   ```

4. **MCP Integration** - Tool connections
   ```markdown
   ## MCP Integration

   This framework connects to MCP via:
   - Tool registration pattern
   - Resource exposure pattern
   - Prompt template pattern
   ```

5. **Data/Knowledge** - Embedded expertise
   ```markdown
   ## References

   See references/api-patterns.md for:
   - All API signatures
   - Common usage patterns
   - Error handling patterns
   ```

6. **Safety & Guardrails**
   ```markdown
   ## Safety

   NEVER:
   - Expose API keys in code
   - Skip error handling for API calls
   - Ignore rate limits

   ALWAYS:
   - Validate inputs before API calls
   - Handle timeout gracefully
   - Log errors for debugging
   ```

### Step A.6: Test the Skill

**Create a test project:**

```bash
# Create test directory
mkdir -p /tmp/test-[framework]
cd /tmp/test-[framework]

# Use the skill to build TaskManager
# This validates the skill works
```

**Test criteria:**
- [ ] Skill triggers on relevant prompts
- [ ] Skill provides accurate guidance
- [ ] TaskManager example works
- [ ] No hallucinated APIs or patterns

### Step A.7: Validate and Commit Skill

```bash
# Validate skill structure
python3 .claude/skills/creating-skills/scripts/verify.py .claude/skills/[framework-name]

# If valid, commit
git add .claude/skills/[framework-name]
git commit -m "feat(skill): add [framework] expertise skill"
```

---

## PHASE B: CHAPTER CREATION

**Now with deep expertise encoded in the skill, proceed with standard workflow:**

### Step B.1: Specification

```
Skill: sp.specify
Args: "Chapter [N]: [Title] - Use .claude/skills/[framework] as knowledge source"
```

**The spec should reference:**
- The skill created in Phase A
- TaskManager as running example
- Auxiliary domain examples (legal, finance, healthcare)

### Step B.2: Clarification

```
Skill: sp.clarify
Args: [feature-name]
```

### Step B.3: Planning

```
Skill: sp.plan
Args: [feature-name]
```

**Plan should leverage:**
- Skill's decision logic for lesson structure
- Skill's examples for "Try With AI" sections
- Skill's safety notes for guardrails

### Step B.4: Task Generation

```
Skill: sp.tasks
Args: [feature-name]
```

### Step B.5: Cross-Artifact Analysis

```
Skill: sp.analyze
Args: [feature-name]
```

### Step B.6: GitHub Issues (Optional)

```
Skill: sp.taskstoissues
Args: [feature-name]
```

### Step B.7: Implementation

```
Skill: sp.implement
Args: [feature-name]
```

**During implementation:**
- Each lesson subagent has access to the skill
- Skill provides accurate technical details
- No hallucination because skill is verified

### Step B.8: Validation

Run validators in parallel:
- `validation-auditor`
- `educational-validator`
- `factual-verifier` (facts already verified in skill)

### Step B.9: Update Tasks & Close Issues

After each task completes:
1. Mark task complete in tasks.md
2. Close corresponding GitHub issue (if created)

```bash
# Close issue
gh issue close [issue-number] --comment "Completed in [commit-hash]"
```

### Step B.10: Commit and PR

```
Skill: sp.git.commit_pr
Args: [feature-name]
```

---

## Skill Components Reference

| Component | Purpose | Source |
|-----------|---------|--------|
| **Persona** | Expert identity and voice | Define based on domain |
| **Logic** | Decision trees, when-to-use | Official docs + community |
| **Context** | Prerequisites, setup | Official docs |
| **MCP** | Tool integrations | MCP specification |
| **Data** | API patterns, examples | Official docs + research |
| **Safety** | Guardrails, what to avoid | Community wisdom + docs |

---

## Example: Creating Chapter 34 (OpenAI Agents SDK)

**User Input**: "Create Chapter 34: OpenAI Agents SDK"

**Phase A Output**:
```
.claude/skills/building-with-openai-agents/
├── SKILL.md (persona, logic, workflow, safety)
├── references/
│   ├── api-patterns.md (Runner, Agent, Tool signatures)
│   ├── examples.md (TaskManager implementation)
│   └── community-wisdom.md (production patterns)
└── scripts/
    └── verify-openai-agents.py
```

**Phase B Output**:
```
apps/learn-app/docs/06-AI-Native-Software-Development/34-openai-agents-sdk/
├── 01-what-is-openai-agents-sdk.md
├── 02-creating-your-first-agent.md
├── 03-tools-and-function-calling.md
├── 04-multi-agent-patterns.md
├── 05-taskmanager-implementation.md
├── 06-error-handling-and-safety.md
├── 07-capstone-complete-agent.md
└── README.md
```

---

## Quality Gate

Before proceeding from Phase A to Phase B:

| Check | Requirement |
|-------|-------------|
| Skill validates | `verify.py` passes |
| Skill triggers correctly | Test prompts activate it |
| TaskManager example works | Build produces working code |
| No hallucinated patterns | All APIs verified against docs |

**If any check fails**: Fix the skill before proceeding to content.

---

## Integration with CLAUDE.md

Add to CLAUDE.md:

```markdown
## Chapter Creation Protocol

For new technical chapters (Part 6-7):
1. **Research first**: Use /sp.chapter to build expertise skill
2. **Skill = Source of Truth**: Content draws from verified skill
3. **No hallucination**: All technical details skill-verified
```

---

**Version**: 1.0 (December 2025)
**Requires**: skill-creator, researching-with-deepwiki, fetching-library-docs
**Best For**: Technical chapters teaching frameworks/SDKs
