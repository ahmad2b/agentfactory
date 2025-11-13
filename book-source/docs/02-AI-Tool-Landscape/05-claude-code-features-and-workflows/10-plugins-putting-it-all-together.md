---
sidebar_position: 10
title: "Plugins: Putting It All Together"
duration: "10-12 min"
---

# Plugins: Putting It All Together

Throughout this chapter, you've learned five key Claude Code features individually:

1. **Subagents** (Lesson 5): Specialized AI assistants for complex tasks
2. **Skills** (Lesson 6): Autonomous capabilities discovered automatically
3. **MCP Servers** (Lesson 4): External integrations (web, APIs, databases)
4. **Hooks** (Lesson 8): Event-driven automation
5. **Permission Management** (Lesson 7): Safe collaboration boundaries

But these aren't separate features—they're **components inside a larger architectural whole called plugins**.

A **plugin** bundles all of these together into a shareable, reusable package. This lesson shows you how they integrate and when to use them.

---

## What Is a Plugin?

**Definition**: A plugin is a directory (`.claude-plugin/` in your project) that bundles:

- **Skills** (autonomous capabilities discovered by Claude)
- **Commands** (slash commands like `/code-review`)
- **Agents** (specialized subagents with focused context)
- **Hooks** (automation triggered by events like file saves)
- **MCP Configuration** (external integrations)

**A plugin is NOT a single feature—it's an integrated collection of extensions.**

### Why Plugins Matter

**Before Plugins** (scattered):
- Skills in `.claude/skills/`
- Subagents in `.claude/agents/`
- MCP config in `~/.config/claude/`
- Hooks scattered across your project

**With Plugins** (unified):
- Everything related to a feature bundled together
- Share entire plugin with team or community
- One installation installs entire integrated system
- Version control and updates become simple

---

## Plugin Architecture: The Manifest

Every plugin starts with a manifest file: `.claude-plugin/plugin.json`

```json
{
  "name": "feature-dev",
  "version": "1.0.0",
  "description": "Feature development plugin with code review, testing, and deployment hooks",

  "components": {
    "skills": [
      { "path": "skills/code-quality-checker" },
      { "path": "skills/test-coverage-analyzer" }
    ],
    "commands": [
      { "name": "feature-dev", "path": "commands/feature-dev.md" },
      { "name": "code-review", "path": "commands/code-review.md" }
    ],
    "agents": [
      { "name": "test-orchestrator", "path": "agents/test-orchestrator.md" }
    ],
    "hooks": [
      { "trigger": "PreToolUse", "path": "hooks/pre-tool-validation.md" }
    ],
    "mcp_config": "mcp-servers.json"
  }
}
```

**What this says**: *"This plugin includes 2 skills, 2 commands, 1 agent, 1 hook, and MCP configuration."*

### Inside a Plugin Directory Structure

```
.claude-plugin/
├── plugin.json                    # Manifest
├── commands/
│   ├── feature-dev.md             # Slash command: /feature-dev
│   └── code-review.md             # Slash command: /code-review
├── agents/
│   └── test-orchestrator.md       # Specialized subagent for testing
├── skills/
│   ├── code-quality-checker/
│   │   ├── SKILL.md               # Skill definition
│   │   └── scripts/
│   │       └── analyzer.py        # Implementation script
│   └── test-coverage-analyzer/
│       ├── SKILL.md
│       └── scripts/
│           └── coverage.py
├── hooks/
│   └── pre-tool-validation.md     # Runs before tool execution
└── mcp-servers.json               # External integrations
```

**Key insight**: A **single plugin** can deliver capabilities at multiple levels. The `feature-dev` plugin gives you:

- ✅ Autonomous skills (code quality checking, coverage analysis)
- ✅ Explicit commands (`/code-review`, `/feature-dev`)
- ✅ Specialized agents (test orchestration)
- ✅ Automation hooks (pre-execution validation)
- ✅ External integrations (GitHub MCP for issue tracking)

---

## The Relationship Hierarchy: Plugins Contain Everything

Here's how all the pieces fit together:

```
┌─────────────────────────────────────────────────────┐
│                    PLUGIN (Container)               │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │         SKILLS (Autonomous Discovery)        │  │
│  │  • Code quality checker (autonomous)         │  │
│  │  • Test coverage analyzer (autonomous)       │  │
│  │  • Compliance checker (autonomous)           │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │        COMMANDS (Explicit Slash Cmds)        │  │
│  │  • /code-review                              │  │
│  │  • /feature-dev                              │  │
│  │  • /deploy                                   │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │      AGENTS (Specialized Subagents)          │  │
│  │  • test-orchestrator (runs tests)            │  │
│  │  • security-auditor (checks vulnerabilities)│  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │     HOOKS (Event-Triggered Automation)       │  │
│  │  • PreToolUse: Validate before execution    │  │
│  │  • PostToolUse: Log execution results        │  │
│  │  • SessionStart: Initialize context          │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  MCP CONFIGURATION (External Integrations)  │  │
│  │  • GitHub MCP (@github activation)          │  │
│  │  • Filesystem MCP (@filesystem activation)  │  │
│  │  • Jira MCP (@jira for issue tracking)      │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Interpretation**:
- **Skills** = Claude discovers and uses autonomously based on context
- **Commands** = You explicitly invoke with `/command-name`
- **Agents** = Specialized AI assistants you delegate to for focused tasks
- **Hooks** = Automation triggered by events (before/after operations)
- **MCP** = External tools and data (web, GitHub, databases, APIs)

**All of these live INSIDE the plugin**—bundled as a cohesive unit.

---

## Installation and Activation: The Plugin Workflow

The real power of plugins is **sharing and discovering them from a marketplace**.

**Important**: Plugin management uses CLI commands (from your terminal), not session slash commands. Use `claude plugin [subcommand]` outside of a Claude Code session.

### Step 1: Browse the Marketplace

**From your terminal** (outside any Claude Code session):

```bash
# First, check what marketplaces you have configured
claude plugin marketplace list

# Add the official Anthropic marketplace if not already added
claude plugin marketplace add anthropics/claude-code
```

This gives you access to plugins from three main sources:

**Anthropic Official Plugins** (anthropics/claude-code):
- `feature-dev` — Feature development with testing integration
- `code-review` — Autonomous code quality auditing
- `security-guidance` — Security vulnerability detection

**Community Plugins by Dan Ávila**:
- `devops-automation` — Docker, K8s, deployment workflows
- `documentation-generator` — Auto-generate README, API docs
- `testing-frameworks` — Test setup and execution

**Community Plugins by Seth Hobson & Others** (specialized domain-specific):
- Framework-specific plugins (React, FastAPI, Django, Next.js)
- Team standards enforcement (code style, documentation patterns)
- Industry-specific (healthcare HIPAA compliance, fintech validation)

### Step 2: Install a Plugin

**From your terminal:**

```bash
# Install a plugin from the configured marketplace
claude plugin install feature-dev

# Verify it's installed
claude plugin list
# Should show "feature-dev" with enabled status
```

### Step 3: Activate and Verify

**If you have an active Claude Code session, restart it** to load the new plugin:

```bash
# Press Ctrl+C to exit your current session (if running)
# Then start a new session
claude
```

**Inside your Claude Code session**, check what the plugin added:

```
> /help
# Look for new commands added by the plugin
# Different plugins add different capabilities:
# - Slash commands (like /code-review)
# - Autonomous skills (discovered automatically)
# - Specialized agents
```

**Verify from terminal:**

```bash
claude plugin list
# Should show "feature-dev" as enabled
```

**Why restart?** Plugins are loaded when Claude Code starts. A restart loads the new components into memory.

---

## Plugins vs. Standalone Components: When to Use What

You now have multiple ways to extend Claude Code:

### Single-Purpose Components

**When to use**: One specific capability, one tool.

**Examples**:
- A standalone MCP server for GitHub access
- A single slash command for deployment
- One subagent for code review

**Install**: Via CLI command (e.g., `claude mcp add`)

### Cohesive Multi-Component Plugin

**When to use**: A feature requires multiple integrated components working together.

**Examples**:
- **feature-dev plugin**: Skills (quality check) + Commands (/feature-dev) + Agents (test orchestrator) + Hooks (pre-validation) + MCP (GitHub integration)
- **documentation-generator plugin**: Skills (auto-doc) + Commands (/generate-docs) + Hooks (on-save generation)

**Install**: Via marketplace (e.g., `claude plugin install feature-dev`)

### Complete Decision Framework

Ask yourself:

```
What are you solving?

┌─ One capability (code review, GitHub access)?
│  └─ Install standalone component (MCP, command, or skill)
│
└─ Multiple integrated capabilities (feature development)?
   ├─ Do they work together (quality check → test → deploy)?
   │  └─ Build/install as a Plugin
   │
   └─ Do they work separately?
      └─ Install individually
```

---

## Community Plugin Ecosystem: Your Options

### Option 1: Official Anthropic Plugins (Most Stable)

**Use when**: You want battle-tested, production-ready capabilities.

**Examples**:
- `feature-dev` (feature development with testing integration)
- `code-review` (autonomous code quality auditing)
- `security-guidance` (vulnerability detection)

**Advantage**: Maintained by Anthropic, automatic updates, high reliability.

### Option 2: Community Plugins by Specialized Developers

**Dan Ávila** (DevOps, Documentation, Testing Focus):
- `devops-automation` — Orchestrate Docker, Kubernetes, CI/CD
- `documentation-generator` — Auto-generate README, API docs
- `testing-frameworks` — Set up tests for your stack

**Seth Hobson & Community** (domain-specific plugins):
- Framework-specific: React, FastAPI, Django, Next.js plugins
- Team standards: Code style enforcement, documentation patterns
- Industry-specific: Healthcare (HIPAA), fintech (compliance), e-commerce

**Advantage**: Specialized expertise, evolving with community needs, often free.

### Option 3: Team Plugins (Your Organization)

Store plugins in your team's `.claude-plugin/` directory and commit to version control.

```bash
# Team plugin in your repo
.claude-plugin/
├── plugin.json              # Team-specific configuration
├── skills/
│   └── compliance-checker/  # Your company's rules
├── commands/
│   └── deploy.md            # Your deployment process
└── mcp-servers.json         # Your internal systems
```

**Advantage**: Encodes your team's expertise, persists across projects, shared standards.

---

## Putting It All Together: Real-World Example

Let's see how all components work together in a single workflow.

### Scenario: Feature Development Workflow

**You want to**: Build a new feature with confidence.

**What the feature-dev plugin includes**:

1. **Skills** (autonomous):
   - Code quality checker: Automatically reviews code for style, type hints, docstrings
   - Test coverage analyzer: Automatically measures test coverage

2. **Commands** (explicit):
   - `/feature-dev`: Start feature development (scaffolds files)
   - `/code-review`: Manually request deep code review

3. **Agents** (specialized):
   - Test orchestrator: Runs entire test suite, reports failures

4. **Hooks** (automated):
   - PreToolUse: Validates code before execution
   - PostToolUse: Logs test results

5. **MCP** (external):
   - GitHub: Creates/updates PRs automatically
   - Filesystem: Access to project files

### Workflow in Action

```
1. You: "Start a new feature for user authentication"
   Plugin: /feature-dev scaffolds auth module

2. You: Write code in your editor
   Plugin Skills: Autonomously check code quality and type hints

3. You: "Run tests"
   Plugin Hooks: PreToolUse validates code
   Plugin Agents: test-orchestrator runs full test suite
   Plugin Skills: Measure coverage automatically

4. You: "Create a PR"
   Plugin MCP (GitHub): Creates PR with test results
   Plugin Commands: /code-review invoked implicitly

5. You see: Complete feature with automated quality checks, tests, coverage report, and PR
```

---

## Try With AI

Use Claude Code for this activity (preferred). If you have another AI companion tool, you can use that instead.

### Prompt 1: Plugin Marketplace Exploration

```
I want to find a plugin that helps with [your domain: Python/JavaScript/DevOps].
(a) What Anthropic or community plugins exist for my area?
(b) What components does each plugin include (skills, commands, agents)?
(c) How would I install and test each one?
(d) Which would be most useful for my work?
```

**Expected outcome**: Concrete plugin recommendations with installation steps for your specific domain.

### Prompt 2: Building a Team Plugin

```
My team repeatedly does [describe a workflow: code review, deployment, testing].
Design a custom plugin that would automate this:
(a) What's the plugin name and purpose?
(b) What skills would it include?
(c) What commands would make it easy to use?
(d) What hooks would automate repetitive steps?
(e) What MCP servers (if any) would improve it?
(f) How would your team install and use it?
```

**Expected outcome**: Complete team plugin design blueprint you could implement.

### Prompt 3: Plugin vs. Standalone Decisions

```
You have three capabilities you want to implement:
1. Automatic code review on file save
2. GitHub PR creation with test results
3. Weekly report generation

Should each be:
(a) A standalone MCP server?
(b) A standalone skill?
(c) A single unified plugin?
(d) Multiple plugins?

Explain your reasoning for each decision.
What's the user experience difference between your choices?
```

**Expected outcome**: Clear decision framework for plugin architecture design.

### Prompt 4: Community Plugin Integration

```
I installed 3 plugins: feature-dev, security-guidance, and documentation-generator.
They all have hooks and MCP servers that might conflict.
(a) How do I check if they're compatible?
(b) What could go wrong if plugins conflict?
(c) How do I debug plugin interactions?
(d) Create a 'plugin health checklist' for teams installing multiple plugins.
```

**Expected outcome**: Safety procedures and debugging guide for working with multiple plugins.
