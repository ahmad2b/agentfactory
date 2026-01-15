---
title: "Hello World: Mastering the Interface"
sidebar_position: 4
chapter: 5
lesson: 4
duration_minutes: 10

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Command line interface navigation, permission model, basic interaction patterns"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Claude Code CLI Navigation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute basic commands (/help, /clear, /compact), understand the permission approval workflow (Read/Write/Run), and interpret cost transparency indicators"

learning_objectives:
  - objective: "Navigate the Claude Code TUI (Terminal User Interface) efficiently"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful execution of slash commands"
  - objective: "Understand and control the Permission Loop (Read vs Write vs Execute)"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Correctly identifying when to approve vs reject a proposed action"
  - objective: "Monitor token usage and cost transparency"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Identification of the 'Cost Pill' and what it measures"
  - objective: "Execute a 'Hello World' workflow from start to finish"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Creation and modification of a simple file using natural language prompts"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (TUI, Slash Commands, Permission Loop, Cost Pill, Natural Language coding) - within A2 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Explore /compact mode vs /verbose mode differences; experiment with `claude doctor`"
  remedial_for_struggling: "Focus solely on the 'Hello World' file creation task; skip advanced slash commands initially"

# Generation metadata
generated_by: "content-implementer v1.0.0 (04-hello-world-basics)"
source_spec: "specs/04-hello-world-basics/spec.md"
created: "2026-01-16"
version: "1.0.0"

# Legacy compatibility
prerequisites:
  - "Lesson 02 or 03: Claude Code installed and authenticated"
---

# Hello World: Being the Boss

You've installed Claude Code. Now you're staring at a terminal cursor.

Before you learn advanced features, you need to master the **one skill that matters most**: being the boss.

---

## The Problem: You Just Gave a Bad Order

Imagine this:

You ask Claude Code: "Clean up my temporary files. Delete everything in the `/tmp` and `~/.cache` directories."

Claude reads this and proposes:

```
> I'm about to run:
  rm -rf /tmp/* ~/.cache/*

  [Enter] Approve  [Esc] Reject
```

You pause. That command *seems* right, but what if there's something important in those directories? What if a running process needs `/tmp`?

**This is the Permission Loop. And it's your safety mechanism.**

Claude Code doesn't just do things. It proposes actions and **waits for your approval**. You review before execution. You stay in control.

This is why Claude Code is safe: not because Claude is careful, but because **you get to be careful**.

---

## Why Permissions Matter: The Three Levels

When Claude proposes something, every action has a risk level:

| Action | Risk | Your Job |
|--------|------|----------|
| **Read**: "I'll read `src/config.py`" | Low | Usually safe, unless file has secrets |
| **Write**: "I'll edit `README.md`" | Medium | File gets changed; you might want different changes |
| **Execute**: "I'll run `npm install`" | High | Code runs on your machine right now |

You're not approving blindly. **You're reviewing the exact command before it runs.**

---

## The TUI: Your Command Center

When you run `claude`, you enter the **TUI** (Terminal User Interface). It's simple, but designed for control.

![claude-code-tui-anatomy](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-2/chapter-05/tui-anatomy-annotated.png)

**Key elements:**
- **Input field**: Type natural language instructions
- **History**: Scroll to see previous exchanges
- **Cost Pill**: Dollar amount for current session (top right)
- **Activity Indicator**: Shows when Claude is "Thinking" vs "Executing"

**Slash commands** (like Discord/Slack):
- `/help` → Show available commands
- `/clear` → Clear screen (keeps session context)
- `/compact` → Minimal view (hide detailed outputs)
- `/cost` → Detailed token usage

---

## The Permission Loop Anatomy

### How It Works

1. **You give an instruction** (natural language)
2. **Claude proposes an action** (exact command or file edit)
3. **You see the proposal** and make a choice:
   - `[Enter]` = Approve
   - `[Esc]` or 'n' = Reject
4. **If approved**: Claude executes
5. **If rejected**: You can give new instructions

**Example:**

```
You:    "Write a Python script to sum numbers"
Claude: "I'll create sum.py with this content: [shows code]
        > Write file sum.py?
        [Enter] Approve  [Esc] Reject"
You:    [Press Esc]
You:    "Actually, make it sum integers only, and handle errors"
Claude: "Better approach: [new code shown]
        > Write file sum.py?
        [Enter] Approve"
You:    [Press Enter]
```

---

## Steering: The Real Skill

Here's what makes you "the boss": **You don't just approve or reject. You steer.**

When Claude proposes something wrong, don't say "No." Give a better instruction:

```
Claude: "I'm about to delete /tmp/*"
You:    "Stop. Don't delete. Instead, list what's in /tmp
         and only delete .*.tmp files older than 1 week"
Claude: *proposes safer command*
You:    "Approve"
```

**This feedback loop—propose, reject with correction, iterate—is how you teach Claude your standards.** You're not the rubber stamp. You're the editor, the reviewer, the decision-maker.

---

## Hands-On: Make a Mistake and Recover

Let's build the muscle memory.

### Setup
```bash
mkdir hello-claude
cd hello-claude
claude
```

### Step 1: Ask for Something Risky

Type this:
> "Delete all Python cache files in this directory and subdirectories"

**Watch Claude propose:**
```
> I'm about to run: find . -name "__pycache__" -type d -exec rm -rf {} +
```

### Step 2: Reject It (Even If It Looks Right)

Press `Esc`. This is practice.

### Step 3: Steer with a Better Request

Type:
> "Don't delete yet. First, let me see what we have. List all Python cache directories."

Claude runs the safer `find` command (list-only).

### Step 4: Approve the Real Action

Once you see what exists:
> "OK, now delete just the __pycache__ directories, not .pyc files"

Claude proposes again. You review. You approve.

**What you just did:** You experienced the Read-Write-Execute loop and steered the outcome. This is agentic development in one action.

---

## Cost Pill: Understanding Token Usage

Top right, you'll see a number like `$0.04`. This is **session cost**.

- **Input tokens** (cheaper): What you type + files Claude reads
- **Output tokens** (expensive): What Claude writes

**Cost management rule:**
```
Bad:  "Fix the bug in my app" → Reads everything
Good: "Fix the bug in auth.py" → Reads one file
```

Type `/cost` to see detailed breakdown.

---

## Try With AI

**Practice steering:**
> "Ask Claude to create a file. When it asks for permission, REJECT it. Then guide it: 'Actually, make it a markdown file with a different name.' Watch how Claude adapts to your feedback."

**Understand cost:**
> "Run `/cost`. Ask Claude to read a large file. Run `/cost` again. How much did that file cost?"

**Master approval workflow:**
> "Give Claude a task with 3 steps (Read → Write → Execute). Watch for all three permission requests. Approve them one at a time and see the workflow complete."

---

## You've Just Learned the Most Important Skill

You now know something most AI users miss: **Control happens through feedback, not just approval.**

You're not a passive user saying "yes" or "no." You're an active editor, steering Claude toward your goals.

In Lesson 6, you'll teach Claude about your project (CLAUDE.md). In Lesson 8, you'll build Skills. But none of that matters if you can't be the boss here.

You've learned it. You can now build anything.

---

**Next Up:** Now that you know how to be the boss, let's teach Claude about your project. Proceed to **Lesson 6: CLAUDE.md Context Files**.
