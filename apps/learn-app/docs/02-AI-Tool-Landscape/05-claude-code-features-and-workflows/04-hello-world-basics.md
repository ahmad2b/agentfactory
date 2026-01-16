---
title: "Hello Claude: Your First Conversation"
sidebar_position: 4
chapter: 5
lesson: 4
duration_minutes: 7

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Opening Claude Code, natural language conversation, basic file creation, understanding Claude as a collaborator"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Claude Code First Contact"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Digital Engagement"
    measurable_at_this_level: "Student can open Claude Code, have a natural conversation, and create a simple file through natural language"

learning_objectives:
  - objective: "Start Claude Code and engage in natural conversation"
    proficiency_level: "A1"
    bloom_level: "Remember"
    assessment_method: "Successfully typing 'claude' and receiving a response"
  - objective: "Ask Claude exploratory questions about its capabilities"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Asking 'Where am I?' and 'What can you do?' and understanding responses"
  - objective: "Create a simple file by describing what you want"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Creating a markdown file with content using natural language"
  - objective: "Observe Claude's offer-and-approval workflow"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Noticing when Claude proposes actions and asks for approval"

# Cognitive load tracking
cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (Claude Code terminal, natural conversation, approval pattern) - well within A1 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Try asking Claude to search the web for information and save it to a file"
  remedial_for_struggling: "Just focus on opening Claude and asking 'What can you do?' - that's success"

# Generation metadata
generated_by: "content-rewriter (04-hello-world-basics-beginner-focused)"
source_spec: "specs/04-hello-world-basics/spec.md"
created: "2026-01-16"
version: "2.0.0"

# Legacy compatibility
prerequisites:
  - "Lesson 02 or 03: Claude Code installed and authenticated"
---

# Hello Claude: Your First Conversation

You've installed Claude Code. Now it's time to actually use it.

This lesson isn't about learning complex features. It's about having your first real conversation with Claude and realizing it's not intimidating—it's actually natural.

---

## The Setup: One Command

Open your terminal and type:

```bash
claude
```

That's it. You're now in Claude Code.

You'll see a prompt. It looks something like:

```
> _
```

This is where you talk to Claude. In plain English. No special syntax. No commands you need to memorize.

---

## Your First Questions: Orient Yourself

Let's start with the basics. Ask Claude where you are:

```
> Where am I in the filesystem?
```

Claude will tell you. Your current directory. Simple context.

Now ask what Claude can do:

```
> What can you do? What are my main options?
```

Claude will explain it naturally. Not a manual. Not technical jargon. Just what's possible.

**What you're learning:** Claude responds to natural language. You're not "commanding"—you're asking questions and conversing.

---

## Real-World Example: Search for News and Save It

Here's something useful. Let's find recent AI news and save it to a file.

Ask Claude:

```
> Search for the latest news about AI agents in 2026 and create a file called 'ai-news-2026.md' with what you find
```

Watch what happens:

1. **Claude reads the web** for recent news
2. **Claude proposes a file** with formatted content
3. **You'll see a prompt asking:** `> Create file ai-news-2026.md?`
4. **You press Enter** to approve

Done. You now have a file with actual, current information.

**What just happened:**
- You described what you wanted in plain English
- Claude figured out the steps (search, format, create file)
- Claude showed you what it was about to do
- You approved with one keypress

No clicking. No menu hunting. Just conversation.

---

## The Approval Pattern: You're Always in Control

Notice that Claude didn't just do things. **It asked first.**

This is the permission model. Every time Claude wants to:
- **Read** a file
- **Write** or create a file
- **Run** a command

It shows you exactly what it's about to do and waits for your approval.

Press `[Enter]` to approve. Press `[Esc]` to reject.

If you reject, you can ask Claude to try differently. That's steering.

**Why this matters:** You're never surprised. Claude can't accidentally delete your project or run something dangerous without your knowledge.

---

## Try With AI

**Explore naturally:**
> "Ask Claude: 'What's in this directory?' Then ask: 'Tell me about my project structure.' Watch how Claude learns about your environment through conversation."

**Create something real:**
> "Ask Claude to search for recent breakthroughs in your field of interest and save them to a file. Use natural language—describe what you want, not how to do it."

**Test the approval workflow:**
> "Ask Claude to create a file, and when it asks for approval, press Esc to reject. Then ask it to do something different. Notice how Claude adapts without frustration."

---

## What You Just Did

You opened Claude Code and had a conversation. No installation wizards. No configuration files. No learning curve.

You asked questions. Claude answered. You created a file with current information from the web.

This is agentic development at its simplest: **describing your intent in natural language and letting Claude handle the mechanics.**

In the next lessons, you'll learn how to:
- Save Claude's instructions about *your* project (Lesson 5)
- Build reusable Skills (Lesson 7)
- Connect Claude to external systems (Lesson 9)

But here's the truth: Everything you just did—the conversation, the approval, the file creation—that's the foundation for all of it.

---

**Next Up:** Now that you're comfortable conversing with Claude, let's teach Claude about YOUR project. Proceed to **Lesson 5: Teaching Claude Your Project with CLAUDE.md**.
