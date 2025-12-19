---
title: "Compiling MCP to Skills"
sidebar_position: 9
chapter: 5
lesson: 9
duration_minutes: 30

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration) - using skill-creator to compile Playwright MCP into browser-automation skill"
layer_1_foundation: "Completed in Lessons 04-06 (Skills) and 08 (MCP)"
layer_2_collaboration: "Working with Claude via skill-creator to generate executable scripts that call MCP locally"
layer_3_intelligence: "N/A - Compilation creates reusable skills, but lesson focuses on Layer 2 process"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Code Execution Pattern Compilation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can identify high-token MCPs, use skill-creator to generate executable scripts, and validate 95-99% token reduction through local execution"

learning_objectives:
  - objective: "Recognize MCP token bloat and understand code execution pattern solution"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explain why scripts running locally save tokens vs direct MCP calls"
  - objective: "Use skill-creator to compile Playwright MCP into browser-automation skill"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Generate SKILL.md + scripts/ folder with executable code"
  - objective: "Understand progressive disclosure (3-stage loading)"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explain how description → SKILL.md → scripts loading saves tokens"
  - objective: "Validate token reduction through measurement"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Calculate and report 95-99% savings with concrete before/after numbers"
  - objective: "Decide when to compile MCPs vs use direct MCP"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Apply decision framework to multiple MCP servers with reasoning"

# Cognitive load tracking
cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (MCP token bloat, code execution pattern, progressive disclosure, local script execution, sandboxed environment, token savings calculation) - within B1-B2 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Compile multiple MCP servers into a unified skill library; implement caching strategies"
  remedial_for_struggling: "Focus on single MCP server; use provided templates"

# Generation metadata
generated_by: "content-implementer v1.0.0 (045-lesson-09-compiling-mcp-skills)"
source_spec: "specs/045-lesson-09-compiling-mcp-skills/spec.md"
created: "2025-12-19"
last_modified: "2025-12-19"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.0"

# Legacy compatibility
prerequisites:
  - "Lesson 05: The Concept Behind Skills"
  - "Lesson 06: Agent Skills (SKILL.md format)"
  - "Lesson 08: MCP Integration"
---

# Compiling MCP to Skills

You've learned MCP servers connect Claude Code to external systems. You've mastered skills as encoded expertise. Now: what happens when you want both, but MCP's token consumption makes it expensive?

![skills-mcp](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-2/chapter-05/skills-mcp.png)

This lesson shows you a powerful pattern: **compile high-token MCP servers into lean skills**, reducing context consumption by up to 98.7% while maintaining full functionality.

:::tip Industry Standard
Skills format is now supported by Claude Code, OpenAI Codex (beta), and Goose. 
Skills you compile here work across all three agents.
:::

---

## The Problem: MCP Token Bloat

When Claude Code loads an MCP server, it eagerly loads ALL tool definitions upfront. Here's the real impact:

**Scenario: Agent with 1,000 tools across multiple MCP servers**

- **Without optimization**: 150,000 tokens loaded before processing your first request
- **Real cost**: Model processes tool metadata before it can even read what you asked
- **Hidden waste**: Fetching a 2-hour meeting transcript from Google Drive and attaching to Salesforce means processing the full content TWICE through the model—once on retrieval, once on attachment. That's **50,000+ additional tokens for a single workflow**.

> "Tool descriptions occupy more context window space, increasing response time and costs. For agents with thousands of tools, this means processing hundreds of thousands of tokens before reading a request."
> — Anthropic, [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)

**The math**: A single Playwright MCP server loads ~8,000 tokens of definitions. Call it 3 times in one session? That's 24,000 tokens of redundant overhead—before you've accomplished anything.

#### 💬 AI Colearning Prompt
> "I have 3 MCP servers installed. Help me estimate my token overhead: For each server, how many tokens does it load at startup? What's my total context cost before I've even asked a question?"

---

## The Solution: Code Execution Pattern

Instead of calling MCP tools directly through Claude's context, compile them into **skills with executable scripts**:

### The Architecture

**SKILL.md + Scripts Model:**
```
.claude/skills/browser-automation/
├── SKILL.md                    # High-level procedures (~150 tokens)
└── scripts/
    ├── navigate.ts             # Browser navigation
    ├── extract-data.ts         # Data extraction with filtering
    ├── take-screenshot.ts      # Screenshot capture
    ├── fill-form.ts            # Form automation
    └── inspect-network.ts      # Network/console debugging
```

**How It Works:**
1. **SKILL.md** provides high-level procedure (loaded once at startup)
2. **Scripts** execute Playwright MCP tools locally (outside Claude's context)
3. **Data transformation** happens in sandboxed environment
4. **Only filtered results** returned to conversation

**Token Comparison:**
- Direct MCP: 8,000 tokens × 3 calls = 24,000 tokens
- Compiled skill: 150 tokens (SKILL.md) + 0 tokens (local scripts) = 150 tokens
- **Savings: 99.4%**

---

### Progressive Disclosure: 3-Stage Loading

Skills use **three-level loading** (covered in Lesson 6) to minimize token consumption:

1. **Discovery** (startup): Load only `description` field (~30 tokens)
2. **Activation** (when relevant): Load full SKILL.md (~150 tokens)
3. **Execution** (when needed): Run `scripts/` locally (0 tokens in context)

**Key for compiled skills:** Stage 3 executes MCP tools outside Claude's context, so heavy operations consume zero tokens.

**Example:**
```
User: "Extract product prices from Amazon"

→ Stage 1: Match description "browser automation"
→ Stage 2: Load SKILL.md procedures
→ Stage 3: Execute script locally (filter 1000 → 20 products)
→ Return only 20 results to Claude
```

---

### Why Scripts Save Tokens

**Without scripts (direct MCP):**
```
User request → Claude calls browser_navigate (2,000 tokens loaded)
            → Claude calls browser_evaluate (3,000 tokens loaded)
            → Returns 1,000 product objects (10,000 tokens in context)
            → Claude filters to 20 relevant (10,000 tokens wasted)
Total: 15,000 tokens
```

**With scripts (code execution):**
```
User request → Claude executes script (0 tokens - runs locally)
            → Script calls browser_navigate locally
            → Script calls browser_evaluate locally
            → Script filters 1,000 → 20 products locally
            → Returns only 20 products to Claude (200 tokens)
Total: 200 tokens
```

**Savings: 98.7%**

---

## Hands-On: Compile Playwright MCP to Browser-Automation Skill

You'll compile the Playwright MCP into a **browser-automation skill** with executable scripts following the Anthropic pattern.

### Prerequisites

Verify Playwright MCP is installed:

```bash
claude mcp list
```

You should see `playwright` in the list. If not, install it:

```bash
claude mcp add --transport stdio playwright npx @playwright/mcp@latest
```

### Step 1: Invoke Skill-Creator

Start Claude Code in any directory:

```bash
claude
```

Use this prompt to invoke skill-creator:

```
I want to compile the Playwright MCP server into a browser-automation skill
following the Anthropic code execution pattern from:
https://www.anthropic.com/engineering/code-execution-with-mcp

The workflow should be:

1. First, introspect the Playwright MCP server:
   - Call Playwright MCP tools to discover what's available
   - List all tool names and their signatures
   - Understand what each tool does

2. Then, create a browser-automation skill that:
   - Generates executable scripts in scripts/ folder
   - Scripts call the Playwright MCP tools we just discovered
   - Each script runs locally (outside Claude's context)
   - Achieves 95-99% token reduction

3. Finally, help me test it to confirm scripts execute locally.

Guide me through this entire process step by step.
```

### Step 2: Answer Skill-Creator's Questions

Skill-creator will guide you through dialogue. Example answers:

**"What browser automation tasks do you need?"**
```
Web scraping (extracting product data, prices, listings)
Testing (clicking buttons, filling forms, capturing screenshots)
Data collection (monitoring sites, tracking changes)
```

**"How often do you use Playwright MCP?"**
```
3-5 times per week across different projects.
Each use involves multiple operations (navigate, extract, sometimes screenshot).
```

**"What data transformations are common?"**
```
Filtering large result sets (1000 products → top 20)
Converting HTML to structured JSON
Removing duplicates and irrelevant data
```

**"What should trigger this skill?"**
```
When I ask to:
- Browse/scrape websites
- Extract data from pages
- Automate web interactions
- Take screenshots
- Test web applications
```

### Step 3: Review Generated Skill Structure

Skill-creator generates the complete skill structure:

```
.claude/skills/browser-automation/
├── SKILL.md                    # Procedures + descriptions
└── scripts/                    # Executable TypeScript/JavaScript
    ├── navigate.ts
    ├── extract-data.ts
    ├── take-screenshot.ts
    ├── fill-form.ts
    └── inspect-network.ts
```

**Key components to verify:**

1. **Description field** - Should trigger on browser automation requests
2. **Scripts folder** - Contains executable `.ts` or `.js` files
3. **Procedures** - Each operation explains which script to run and what parameters it needs

The skill-creator will show you the complete SKILL.md and all scripts. Review them to ensure they cover your use cases.

### Step 4: Test the Skill

Start a NEW Claude Code session (so skill loads fresh):

```bash
claude
```

Test with a real automation task:

```
Extract the top 5 product names from https://example-shop.com
```

**What to observe:**
1. Skill activates automatically (description matched your request)
2. Claude runs a script from `scripts/` folder
3. You see `node scripts/extract-data.ts` or similar execution
4. Only filtered results returned (not full page HTML)

### Step 5: Validate and Iterate

**5a. Measure Token Savings**

Ask Claude:

```
Measure the token savings for this browser-automation skill:

1. Run in Bash: Simulate calling Playwright MCP directly 3 times
   (estimate token overhead for each tool definition load)

2. Compare with the compiled skill:
   - How many tokens loaded at startup?
   - How many tokens during script execution?
   - What's the percentage reduction?

3. Show me the exact numbers and calculations.
```

Expected result: **95-99% reduction**

**5b. Test Edge Cases (Iterate if Needed)**

Test different scenarios to ensure the skill works correctly:

```
1. Test navigation: "Navigate to https://example.com and tell me the page title"
2. Test screenshot: "Take a screenshot of https://example.com"
3. Test form filling: "Fill out the contact form at [URL] with [data]"
4. Test error handling: "Extract data from an invalid URL"
```

**If any test fails:**
- Ask Claude to fix the specific script
- Retest the operation
- Iterate until all operations work

**5c. Verify Scripts Run Locally**

Ask Claude:

```
Show me evidence that scripts run outside your context:

1. Check your Bash tool usage - did you execute scripts locally?
2. How much data was filtered before returning to you?
3. What would happen if I called Playwright MCP directly instead?
```

This confirms the code execution pattern is working correctly.

#### 💬 AI Colearning Prompt
> "My browser-automation skill is working. Explain: (1) How does running scripts in Bash save tokens vs calling MCP tools? (2) What data filtering happened locally? (3) How would I debug if a script fails?"

---

## When to Compile MCP Servers

Not every MCP server benefits from compilation. Use this decision framework:

### Compile to Skill When:

✅ **High token overhead** (>5,000 tokens per query)
- Example: Playwright, Google Drive, Database MCP

✅ **Frequent use** (3+ times per session or across projects)
- Repeated calls multiply token waste

✅ **Large datasets returned** (need filtering/transformation)
- Processing 1,000 items → returning 20 relevant ones

✅ **Multi-step workflows** (chaining operations)
- Navigate → extract → transform → filter

### Use Direct MCP When:

❌ **Low token overhead** (<1,500 tokens per query)
- MCP already efficient, compilation overhead not worth it

❌ **Infrequent use** (once per month or less)
- Setup cost > token savings

❌ **Small, well-formatted results** (no transformation needed)
- Results already optimal for Claude

❌ **Rapidly changing API** (MCP tools frequently updated)
- Skill scripts would need constant maintenance

---

## Decision Framework: When to Compile vs. Use Direct MCP

Not every MCP server needs compilation. Use this matrix to decide:

| Scenario | Recommendation | Reasoning |
|----------|----------------|-----------|
| **One-off query** | Use MCP directly | Compilation overhead not worth it for single use |
| **Repeated workflow** (3+ times) | Compile to skill | Amortizes compilation cost across multiple uses |
| **High token definitions** (5,000+ tokens) | Compile to skill | Token savings justify upfront work |
| **Low token definitions** (&lt;500 tokens) | Use MCP directly | Compilation provides minimal benefit |
| **Rapidly changing API** | Use MCP directly | Compiled skill becomes stale quickly |
| **Stable tool set** | Compile to skill | Skill remains accurate over time |
| **Privacy-sensitive data** | Compile to skill | Local script execution avoids context logging |
| **Integration with other skills** | Compile to skill | Composability improves with skill format |
| **Team workflow** | Compile to skill | Shareable SKILL.md vs proprietary MCP setup |

**Decision shortcut**:
- Calling MCP 1-2 times? → Use direct MCP
- Calling MCP 3+ times in same session? → Compile to skill
- Working with high-token server? → Compile to skill
- Building production workflow? → Compile to skill

---

## What's Ahead

You've learned to compile MCP servers into lean skills—reducing token consumption by 80-98% while preserving functionality. But what happens when you need multiple skills working together on complex tasks?

**Lesson 10: Subagents and Orchestration** introduces the next level: specialized AI assistants that handle specific types of work with isolated context. Where compilation gives you *efficiency*, subagents give you *coordination*—a team of focused specialists instead of one overloaded generalist.

Skills you compile now become building blocks for subagent workflows later.

---

## Sources

Research and tools supporting this lesson:

- [Anthropic: Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Architecture for local execution + context reduction
- [Armin Ronacher: Skills vs Dynamic MCP Loadouts](https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/) — Token efficiency analysis and pattern recommendations
- [SmartScope: MCP Code Execution Deep Dive](https://smartscope.blog/en/blog/mcp-code-execution-agent-design/) — Detailed compilation workflow examples
- [Claude Code Documentation: MCP Integration](https://docs.anthropic.com/claude-code/mcp) — Official MCP protocol reference

---

## Try With AI

**Compile Playwright MCP to Browser-Automation Skill:**

> "I have the Playwright MCP installed. Use skill-creator to compile it into a browser-automation skill following the Anthropic code execution pattern. The skill should: (1) Generate executable scripts in scripts/ folder, (2) Call Playwright MCP tools locally (outside context), (3) Achieve 95-99% token reduction. Guide me through the compilation process with script generation."

**Measure Real Token Savings:**

> "I've compiled Playwright MCP to a skill with scripts. Calculate the actual token savings: (1) Estimate tokens for 3 direct MCP operations (navigate, extract data, screenshot), (2) Estimate tokens with the compiled skill, (3) Show percentage reduction, (4) Explain where each savings comes from (tool definitions, local execution, data filtering)."

**Validate Script Execution:**

> "Test my browser-automation skill: Extract product names from https://example-shop.com. Show me: (1) Which script executed, (2) What happened locally vs in context, (3) How much data was filtered before returning to you, (4) Token count comparison if this was direct MCP."

**Decide Which MCPs to Compile:**

> "I have these MCP servers: [list your servers]. For each, analyze: (1) Token overhead per query, (2) How often I use it, (3) Whether it returns large datasets, (4) If data transformation is needed. Recommend which ones to compile to skills with reasoning."

**Debug Skill Execution:**

> "My browser-automation skill isn't activating when I ask to scrape data. Debug: (1) Check the description field - is it specific enough? (2) Suggest better trigger phrases, (3) Test if the skill loads at all, (4) Verify scripts are executable and in correct location."

**Compare Compilation Strategies:**

> "I compiled Playwright MCP. Now I want to understand: (1) What if I had created an instruction wrapper instead of code execution? (2) How much would token savings differ? (3) When would instruction wrapper be better? (4) Show me the trade-offs between the two approaches."
