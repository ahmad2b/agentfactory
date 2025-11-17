---
sidebar_position: 9
title: "Discovering and Using Claude Code Plugins"
duration: "10-12 min"
stage: "L4"
prerequisites:
  - "Lessons 1-8: Complete understanding of all Claude Code features"
  - "Understanding of composition and orchestration"
learning_objectives:
  - "Understand plugins as bundled capabilities (skills + agents + hooks + MCP)"
  - "Discover available plugins through marketplaces"
  - "Install and use pre-built plugins from Anthropic's skills repository"
  - "Recognize when a plugin solves your workflow needs"
skills:
  - name: "Leveraging Claude Code Ecosystem and Plugins"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
concept_count: 8
---

# Discovering and Using Claude Code Plugins

## The Problem: Reinventing the Wheel

You've learned to create skills, use subagents, and connect MCP servers. But what if someone has already built exactly what you need?

**Scenario**: You want Claude to help with:
- Creating visual designs (canvas art, diagrams)
- Building web apps with React components
- Testing web applications automatically
- Following your company's brand guidelines

**Question**: Should you build these capabilities from scratch, or use what already exists?

**Answer**: Use existing plugins from marketplaces.

---

## What Are Plugins?

**Definition**: A plugin is a **bundled package** that can include:

1. **Skills** (autonomous capabilities Claude discovers)
2. **Subagents** (specialized AI assistants)
3. **Hooks** (event-driven automation)
4. **Commands** (slash commands like `/design`)
5. **MCP configuration** (external integrations)

**Think of plugins as**: Pre-built toolkits that extend Claude's capabilities in specific domains (design, testing, development, enterprise workflows).

**Key insight**: You don't need to build everything yourself. Marketplaces provide ready-to-use plugins created by Anthropic and the community.

---

## Discovering Plugins: Anthropic's Skills Marketplace

The easiest way to extend Claude Code is using **Anthropic's official skills repository**—a curated collection of pre-built capabilities.

### What's Available in the Skills Repository?

The Anthropic skills marketplace provides **two main plugin bundles**:

**1. example-skills** - Creative and development capabilities (canvas design, web testing, communications, and more)

**2. document-skills** - Document processing suite (Word, PDF, PowerPoint, Excel)

### How to Add the Skills Marketplace

In Claude Code, run:

```bash
/plugin marketplace add anthropics/skills
```

**What happens**:
1. Claude Code connects to https://github.com/anthropics/skills
2. Downloads the marketplace configuration
3. Marketplace appears as **"anthropic-agent-skills"** in your plugin list

### Browse and Install Plugins

After adding the marketplace, run `/plugin` to see an interactive menu that guides you through browsing and installing available plugins.

### Install a Plugin Bundle

Use the `/plugin` UI to browse and install, or run directly:

```bash
/plugin install example-skills@anthropic-agent-skills
```

Claude Code downloads the skills bundle and installs it to `.claude/skills/`, making all skills immediately available.

### Test Your Installed Skills

After installing `example-skills`, try asking Claude to create a visual diagram. The canvas-design skill will activate automatically when it detects visual/design requests.

---

## Plugin Marketplaces: Beyond Anthropic

### Adding Custom Marketplaces

You can add marketplaces from:

**GitHub repositories**:
```bash
/plugin marketplace add owner/repo
```

**GitLab or other git services**:
```bash
/plugin marketplace add https://gitlab.com/company/plugins.git
```

**Local paths** (for development):
```bash
/plugin marketplace add ./my-marketplace
```

**Direct URLs**:
```bash
/plugin marketplace add https://url.of/marketplace.json
```

### List Installed Marketplaces

```bash
/plugin marketplace list
```

**What you'll see**:
- All marketplaces you've added
- Source URLs
- Number of plugins available from each

---

## When to Use Existing Plugins vs. Create Custom

**Use existing plugins** when standard capabilities exist (design, testing, document processing). **Create custom** when your workflow is team-specific or no existing plugin matches your needs. Check marketplaces first.

---

## Hands-On: Set Up the Anthropic Skills Marketplace

### Step 1: Add the Marketplace

```bash
claude
/plugin marketplace add anthropics/skills
```

### Step 2: Install a Plugin Bundle

```bash
/plugin install example-skills@anthropic-agent-skills
```

### Step 3: Test the Installation

Ask Claude: "What skills do you have available?" You should see the installed skills listed.

**What you just did**: Added Anthropic's marketplace and installed production-quality skills that are now available across all Claude Code sessions.

---

## What You Just Learned

- ✅ Plugins bundle multiple capabilities (skills + agents + hooks + commands + MCP)
- ✅ Marketplaces provide pre-built plugins you can install
- ✅ Anthropic's skills repository has curated, production-quality skills
- ✅ `/plugin marketplace add` connects to plugin sources
- ✅ `/plugin install` adds capabilities to your Claude Code
- ✅ Check marketplaces FIRST before building custom capabilities

---

## Official Resources

**Anthropic Skills Repository**:
- https://github.com/anthropics/skills
- Browse all available skills
- View skill source code and documentation
- Learn from professional skill examples

**Plugin Marketplaces Documentation**:
- https://code.claude.com/docs/en/plugin-marketplaces
- How to create custom marketplaces
- Team distribution strategies
- Advanced marketplace configuration

**When You're Ready to Build**:
After using existing plugins, you can learn to create custom ones in advanced content (Part 5+).

---

## Why This Matters: Composition as Organizational Practice

**Workflow Impact**: Plugins bundle everything you've learned (CLAUDE.md, MCP, Subagents, Skills, Hooks) into shareable, reusable packages.

**Paradigm Connection**: This is L4—spec-driven composition. You define WHAT you need (design tools, testing automation, document processing), install the plugin, and orchestrate the capabilities.

**Real-World Context**: Teams can distribute organizational intelligence as plugins. Your company's code review process, brand guidelines, deployment workflows—all packaged as plugins that work the same way for every team member.

**From scattered to unified**: Before plugins, skills lived in `.claude/skills/`, agents in `.claude/agents/`, MCP configs elsewhere. Plugins bundle everything into one installable package.

---

## Plugin Architecture: The Manifest

Every plugin has a `.claude-plugin/plugin.json` manifest listing its components:

```json
{
  "name": "feature-dev",
  "version": "1.0.0",
  "description": "Feature development workflow",
  "components": {
    "skills": [{ "path": "skills/code-quality-checker" }],
    "commands": [{ "name": "code-review", "path": "commands/code-review.md" }],
    "agents": [{ "name": "test-orchestrator", "path": "agents/test-orchestrator.md" }],
    "hooks": [{ "trigger": "PreToolUse", "path": "hooks/pre-tool-validation.md" }],
    "mcp_config": "mcp-servers.json"
  }
}
```

**A single plugin can bundle skills, commands, agents, hooks, and MCP—everything you've learned in Lessons 1-8.**

---

## How Components Work Together

**Skills**: Claude discovers and uses autonomously
**Commands**: You invoke explicitly with `/command-name`
**Agents**: Specialized assistants for focused tasks
**Hooks**: Event-triggered automation
**MCP**: External integrations

**All bundled in one plugin** for easy sharing.

---

## Skill Best Practices Reference

**When you're ready to create custom skills** (covered in Lesson 6, advanced implementation in Part 5+), follow these patterns:

### 1. Write Clear Descriptions
Include activation triggers and examples in your SKILL.md:
```markdown
# Description
This skill [what it does] by [how it does it].

Use this skill when:
- [Specific trigger scenario]
- [Another trigger scenario]

Examples:
- "Help me [example request]"
```

### 2. Keep Skills Focused
One skill, one workflow. Don't create "mega-skills"—Claude can compose multiple focused skills together.

### 3. Start Simple, Iterate
V1: Basic description + happy path
V2: Add error handling from real usage
V3: Production-grade with validation

### 4. Avoid Common Pitfalls
- ❌ Vague descriptions ("helps with tasks")
- ❌ Technology lock-in (hardcoded frameworks)
- ❌ No examples (abstract triggers)

### 5. Learn from Anthropic's Repository
Study production examples at https://github.com/anthropics/skills (canvas-design, web-app-testing, skill-creator)

---

## Try With AI

### Exercise 1: Install and Use a Plugin

```
Install example-skills from anthropics/skills, then help me create
a visual diagram showing the Claude Code plugin architecture
```

**Expected outcome**: Claude uses the canvas-design skill to create visual output.

### Exercise 2: Decision Framework

```
I need Claude to help with [describe your specific task].
Should I use an existing plugin, create a custom skill, or just ask directly?
Walk me through the decision.
```

**Expected outcome**: Understanding when to use existing vs. custom capabilities.