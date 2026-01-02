---
slides:
  source: "https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/chapter-06-slides.pdf"
  title: "Chapter 6: Building a Complete Email Assistant"
  height: 700
---

# Chapter 6: Building a Complete Email Assistant

You've mastered individual Claude Code skills and understand how MCP servers extend your agent's capabilities. Now it's time to combine everything into a **complete AI workflow**—an Email Assistant system that demonstrates how skills, subagents, and MCP integration work together in production.

This chapter builds your first **Digital FTE component**: an Email Assistant that can triage your inbox, suggest responses, draft professional emails, and send them—all orchestrated through Claude Code. By the end, you'll understand the architecture pattern that transforms individual capabilities into a cohesive, intelligent system.

## Before You Begin

### Prerequisites Checklist

- [ ] **Chapter 5: Claude Code Features and Workflows** (REQUIRED) — You must understand skills, subagents, MCP integration, and orchestration concepts
- [ ] **Gmail account** (optional for Lesson 5) — Required only if you want to connect to actual email; lessons 1-4 work without it
- [ ] **Claude Code installed and working** — From Chapter 5, Lesson 2 or 3

### Proficiency Level

**A2 (Elementary)** — This chapter guides you through building interconnected skills with clear specifications and step-by-step collaboration patterns. Each lesson builds on the previous one.

### Estimated Time

**Total Chapter Duration**: ~3.5 hours

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Create interconnected Claude Code skills** — Build 4 skills that work together: email drafter, templates, summarizer, and orchestrator
- **Build custom subagents for specialized processing** — Design 3 subagents (inbox-triager, response-suggester, follow-up-tracker) that handle specific email workflows
- **Configure Gmail MCP server with authentication** — Connect Claude Code to real email using OAuth and the 19 Gmail MCP tools
- **Distinguish when to use skills vs subagents** — Apply the decision framework: skills for guidance (2-4 decision points), subagents for autonomous reasoning (5+ decision points)
- **Design orchestration patterns** — Combine skills + subagents + MCP into a complete Triage to Suggest to Draft to Send workflow
- **Build a "Digital FTE" component** — Create a reusable Email Assistant system that could become the foundation of a sellable product

## System Architecture

This is what you'll build:

```
Email Assistant System
├── Skills (4 Components)
│   ├── /email-drafter        → Compose emails with tone specification
│   ├── /email-templates      → Variable substitution, 3 template types
│   ├── /email-summarizer     → Thread parsing, action extraction
│   └── /email-assistant      → Orchestrator skill (combines everything)
│
├── Subagents (3 Workers)
│   ├── inbox-triager         → Categorize and prioritize incoming emails
│   ├── response-suggester    → Generate contextual reply options
│   └── follow-up-tracker     → Monitor pending responses and deadlines
│
├── MCP Integration
│   └── Gmail MCP Server      → 19 tools: read, send, search, label, archive
│
└── Orchestration Flow
    └── Triage → Suggest → Draft → Send
```

## Skills You'll Create

| Skill | Purpose | Key Learning |
|-------|---------|--------------|
| **email-drafter** | Compose professional emails with tone control | Your first skill with variable inputs |
| **email-templates** | Apply templates with placeholder substitution | Reusable content patterns |
| **email-summarizer** | Extract actions and key points from threads | Information processing skills |
| **email-assistant** | Orchestrate all components together | Meta-skill design pattern |

## Lesson Navigation

| Lesson | Title | Duration | What You'll Build |
|--------|-------|----------|-------------------|
| [01](./01-project-setup-email-drafter.md) | Project Setup & Email Drafter Skill | 30 min | First skill with tone specification |
| [02](./02-email-templates-skill.md) | Email Templates Skill | 25 min | Template system with variable substitution |
| [03](./03-email-summarizer-skill.md) | Email Summarizer Skill | 25 min | Thread parsing and action extraction |
| [04](./04-creating-custom-subagents.md) | Creating Custom Subagents | 35 min | 3 email processing subagents |
| [05](./05-gmail-mcp-integration.md) | Gmail MCP Integration | 30 min | OAuth setup and 19 Gmail tools |
| [06](./06-orchestrating-complete-system.md) | Orchestrating Complete System | 40 min | Capstone: combine everything |
| [07](./07-chapter-quiz.md) | Chapter Quiz | 15 min | 15 questions on skills, subagents, MCP |

## The Bigger Picture

This chapter teaches a fundamental pattern: **composable AI systems**.

Individual skills are useful. But real productivity comes from combining them:

- **Skills** provide expertise (how to write emails, what tone to use)
- **Subagents** provide reasoning (when to escalate, what needs follow-up, how to prioritize)
- **MCP servers** provide integration (access to actual email systems)
- **Orchestration** provides workflow (the complete inbox-to-sent pipeline)

This is the architecture pattern for Digital FTEs. Master it here with email, and you can apply it to any domain—customer support, document processing, data analysis, content creation.

### Why Email First?

Email is the ideal first system to build because:

1. **Universal relevance** — Everyone manages email, so the patterns immediately apply
2. **Clear inputs and outputs** — Email threads in, professional responses out
3. **Measurable improvement** — Time saved per email is quantifiable
4. **Composition opportunity** — Multiple skills (drafting, summarizing, templating) naturally combine
5. **Real integration target** — Gmail MCP provides actual send/receive capabilities

### Skills vs Subagents Decision Framework

You'll learn when to use each:

| Component | Use When | Decision Points | Example |
|-----------|----------|-----------------|---------|
| **Skill** | Guidance needed for consistent execution | 2-4 | Email tone guidelines |
| **Subagent** | Autonomous reasoning required | 5+ | Inbox triage prioritization |
| **MCP Tool** | External system integration | N/A | Gmail read/send |

**By the end of this chapter**, you'll have built a complete Email Assistant that demonstrates production-ready AI system design. More importantly, you'll understand the patterns that let you build similar systems for any workflow.

Let's build your first complete AI system.
