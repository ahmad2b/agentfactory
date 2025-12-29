---
sidebar_position: 0
title: "Build Your Apps SDK Skill"
description: "Create your OpenAI Apps SDK skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 42
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build an Apps SDK skill"

learning_objectives:
  - objective: "Build an Apps SDK skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working openai-apps-sdk skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to Apps SDK domain"

differentiation:
  extension_for_advanced: "Add React Apps SDK UI patterns to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes later"
---

# Build Your Apps SDK Skill

You've built agents with the Agents SDK (Chapter 34) and MCP servers (Chapter 38). Now you'll create the visual layer—ChatGPT Apps with interactive widgets. But you won't start with widget concepts.

You'll start by **building a skill that knows the Apps SDK**.

In Chapter 5, you learned `skill-creator` and `fetching-library-docs`. Now you'll apply them to create an `openai-apps-sdk` skill. The official OpenAI documentation will teach your skill. Then THIS chapter teaches YOU.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git ch42-apps-sdk-skill
cd ch42-apps-sdk-skill
claude
```

---

## Step 2: Write Your Learning Specification

Create `LEARNING-SPEC.md`:

```markdown
# Learning Specification: OpenAI Apps SDK

## What I'm Learning
OpenAI's Apps SDK—building interactive ChatGPT Apps with widgets.

## Why I'm Learning It
To build ChatGPT Apps that:
- Render rich UI inside ChatGPT conversations
- Expose my agents to 800M+ weekly active users
- Use interactive widgets with buttons, forms, and real-time updates
- Combine MCP servers with visual frontends

## My Current Level
- I've built agents with OpenAI Agents SDK (Chapter 34)
- I've created MCP servers with FastMCP (Chapter 38)
- I want to add visual interfaces to my agents

## What I Want My Skill to Do
Help me create ChatGPT Apps with:
- Widget resources using `text/html+skybridge` MIME type
- Interactivity via `window.openai` API
- Action buttons (`sendFollowUpMessage`, `callTool`)
- Response payload design (`structuredContent` vs `_meta`)
- State management with `widgetState`
- Display modes (inline, pip, fullscreen)
- React Apps SDK UI components

## Success Criteria
By the end of Chapter 42, my skill can:
1. Generate a working ChatGPT App with widgets
2. Implement widget interactivity patterns
3. Design efficient response payloads
4. Manage state across tool invocations
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs openai-apps-sdk
```

This pulls official Apps SDK documentation via Context7.

---

## Step 4: Build Your Initial Skill

```
/skill-creator

Create an Apps SDK skill based on the documentation I just fetched.

Name: openai-apps-sdk
Purpose: Generate ChatGPT Apps with interactive widgets

The skill should help with:
1. MCP server setup with FastMCP for ChatGPT Apps
2. Widget resources using text/html+skybridge MIME type
3. window.openai API (sendFollowUpMessage, callTool)
4. Response payload design (structuredContent, _meta)
5. State management (widgetState)
6. Display modes (inline, pip, fullscreen)
7. React Apps SDK UI integration
8. Developer Mode configuration

Base everything on the official documentation patterns.
```

---

## Step 5: Verify Your Skill Works

```
Using my openai-apps-sdk skill, generate a minimal ChatGPT App that:
1. Uses FastMCP to create an MCP server
2. Has one tool that returns a widget resource
3. Shows a simple greeting with a "Refresh" button
```

---

## Step 6: Understand What's Next

Your skill now contains official Apps SDK patterns. Each lesson tests your skill, identifies gaps, and improves it.

| Lesson | Your Skill Learns |
|--------|-------------------|
| 1 | Three-layer architecture validated |
| 2 | Basic widget patterns refined |
| 3 | Interactivity (sendFollowUpMessage) |
| 4 | Response payload design |
| 5 | Tool chaining (callTool) |
| 6 | State and display modes |
| 7 | React Apps SDK UI patterns |
| 8 | Production deployment |

---

:::note Your Growing Toolkit
```
.claude/skills/
├── skill-creator/           # From Chapter 5
├── fetching-library-docs/   # From Chapter 5
├── openai-agents/           # From Chapter 34
├── google-adk/              # From Chapter 35
├── claude-agent-sdk/        # From Chapter 36
├── mcp-server-builder/      # From Chapter 38
├── fastapi-agent-api/       # From Chapter 40
├── chatkit-server/          # From Chapter 41
└── openai-apps-sdk/         # NEW - this chapter
```

Each chapter adds to your Digital FTE toolkit.
:::

---

Start **Lesson 1** with your skill ready to test and improve.
