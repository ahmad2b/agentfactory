---
sidebar_position: 7
title: "Permission Management"
duration: "6-8 min"
---

# Permission Management

## Why Claude Code Asks Permission

When you first use Claude Code, you'll notice something different from other AI tools: **Claude Code asks permission before taking action.**

You might see prompts like:
- "May I edit `main.py`?"
- "May I run `npm install`?"
- "May I create a new file called `config.json`?"

This isn't a limitation or annoyance—it's a **safety feature** that prevents accidents.

Think about it: Claude Code has access to your files and can run commands on your machine. Without explicit permission requests, a miscommunication could accidentally delete important files, modify code in unexpected ways, or run commands that break your system.

**The permission system exists to answer one critical question: "Do you actually want Claude Code to do this right now?"**

This is especially important when you're learning. Early on, you might test Claude Code with exploratory prompts you haven't thought through completely. Permission prompts give you a chance to pause and verify: "Yes, this change makes sense" or "Actually, let me refine this first."

#### 💬 AI Colearning Prompt
> "Explain why agentic AI systems like Claude Code ask for permissions before taking action on a user's system. What could go wrong without this safety mechanism?"

---

## Permission Modes: Three Different Approaches

Claude Code offers **three permission modes**. Each represents a different balance between safety and workflow speed.

### Mode 1: Default (Asks Every Time)

**Behavior**: Claude Code prompts you for permission before **every** file edit and bash command.

**Best for**: Beginners, unfamiliar code, high-stakes projects, or whenever you want explicit control.

**Safety level**: Highest. You review every change before it happens.

**Trade-off**: Slower workflow—you'll approve/deny frequently. But you maintain complete visibility.

**Example interaction**:
```
Claude: May I edit src/app.py to add the authentication function?
You: Yes, approve
[Change applied]
Claude: May I run npm test to validate the changes?
You: Yes, approve
[Test runs]
```

### Mode 2: AcceptEdits (Auto-Approve File Changes)

**Behavior**: Claude Code automatically applies file edits without asking. **BUT** it still asks before running bash commands that modify your system (installs, deletes, system changes).

**Best for**: Experienced users working in familiar codebases. You trust Claude Code's code generation but want safeguards on system-level operations.

**Safety level**: Medium. File changes are auto-approved, but dangerous bash commands still require permission.

**Trade-off**: Faster workflow for coding tasks, but you must review changes afterward (via git diff or file comparison).

**Example interaction**:
```
Claude: [Automatically edits src/app.py without asking]
[File changed silently]
Claude: May I run npm install to add the new dependency?
You: Yes, approve
[Command runs]
```

### Mode 3: Plan (Complex Multi-Step Tasks)

**Behavior**: Claude Code groups related operations into a "plan"—showing you all steps upfront before executing any of them.

**Best for**: Complex features requiring multiple file changes and commands. You review the entire plan, then approve the whole thing at once.

**Safety level**: High. You see the big picture before anything executes.

**Trade-off**: Requires more upfront understanding. You're committing to a multi-step workflow.

**Example interaction**:
```
Claude: Here's my plan to add authentication:
  1. Create auth.py with login function
  2. Edit app.py to import auth
  3. Run tests to verify
  4. Update documentation

Approve this plan?
You: Yes, approve
[All steps execute in sequence]
```

### Permission Modes Comparison

| Mode | Behavior | Use Case | Risk Level |
|------|----------|----------|-----------|
| **Default** | Asks before every change | Beginners; unfamiliar code; learning | Low (explicit control) |
| **AcceptEdits** | Auto-approves files; asks for bash | Experienced users; trusted workflows | Medium (files changed without review) |
| **Plan** | Shows full plan; asks once | Complex multi-step features | Medium (multiple operations approved together) |

**Key insight**: There is no "wrong" mode. Choose based on your comfort level and context. Beginners should start with **default** (safer) and graduate to **acceptEdits** as they gain confidence.

#### 🎓 Expert Insight
> In AI-native development, permission modes are about **trust and workflow speed**, not complexity. Start permissive (default mode) only after understanding what each permission means. Rushing to acceptEdits because you're tired of approvals is a classic mistake that leads to subtle bugs.

---

## Checking Your Current Permissions

To see which permission mode you're currently using, run:

```bash
claude "/permissions"
```

This command displays your current settings. You'll see output like:

```
Permission Mode: default
File edits: Ask every time
Bash commands: Ask every time
```

Or in acceptEdits mode:

```
Permission Mode: acceptEdits
File edits: Auto-approve
Bash commands: Ask every time
```

**What this tells you:**
- Your current **mode** (default, acceptEdits, or plan)
- Which operations are auto-approved
- Which operations still require permission

Run this command whenever you're unsure about your current settings. It's a quick safety check.

#### 🤝 Practice Exercise

> **Ask your AI**: "Show me how to check my Claude Code permission settings. What command do I run? Then explain what each field in the output means."

**Expected Outcome**: You'll understand how to retrieve your permission settings and interpret what they mean for your workflow.

---

## How to Respond to Permission Prompts

When Claude Code asks for permission, you have three options:

### Option 1: Approve
Type `yes` or `approve`. The change executes immediately.

**When to choose**: You've reviewed the proposed change and it looks correct.

### Option 2: Deny
Type `no` or `deny`. The change is cancelled. Claude Code will ask you to clarify or try a different approach.

**When to choose**:
- The change doesn't match what you requested
- You want to refine the specification first
- You're unsure about the impact
- The file is critical and you want extra safety

**Important**: Denying a single request **does not affect your permission mode**. You'll still be in default mode and get asked on the next request.

### Option 3: Edit
Type `edit` or `modify`. Claude Code shows you the proposed change and lets you modify it before approval.

**When to choose**: The change is mostly right but needs small tweaks before you approve.

**Example**:
```
Claude: May I add error handling to login.py?
[Shows proposed code]
You: edit
[You make small changes to the error message]
You: approve
[Modified version applies]
```

#### 💬 AI Colearning Prompt
> "Explain the difference between denying a permission request and changing your permission mode to reject future edits. If I deny one request, will Claude Code still ask me next time?"

---

## Common Permission Scenarios and Best Practices

### Scenario 1: Permission Denied Blocks Your Workflow

**What happens**: You deny a permission request, but now Claude Code can't proceed with your feature.

**Why this is intentional**: You've told Claude Code "not this way." It's asking you to clarify.

**What to do**:
- **If you changed your mind**: Re-ask Claude to make the change
- **If you want a different approach**: Specify what you prefer: "Instead of editing login.py directly, create a new file auth_helpers.py with the same logic"
- **If you want to override**: You can manually approve changes later, or ask Claude to try a simpler approach

**Example**:
```
You: Build user authentication
Claude: May I edit models.py?
You: no
Claude: I can't proceed without editing models.py. Would you like me to:
  A) Create a separate auth_models.py instead?
  B) Explain why the edit is necessary?
You: A - create separate file
[Claude continues with alternative approach]
```

### Scenario 2: Permission Denied vs. Error Message

**Easy confusion**: "Permission denied" prompt vs. runtime error.

**How to distinguish**:
- **Permission prompt**: "May I edit X?" - Claude is **asking** if it's OK
- **Error message**: "TypeError: X is undefined" - Claude tried to do something and it **failed**

**Action**:
- **Permission prompt**: You decide yes/no/edit
- **Error message**: Claude will troubleshoot and ask questions, or propose a fix

### Scenario 3: Worried About Permission Mode Memory

**Question**: "If I approve an edit in default mode, will Claude Code 'remember' that I'm permissive?"

**Answer**: No. **Each permission request is independent.** Your **mode setting** persists (that's deliberate), but individual approvals/denials are forgotten.

**Example**:
- You approve 10 edits today in default mode
- Tomorrow, Claude Code asks permission again on the 11th edit
- Your mode is still default (memory of the setting)
- But it doesn't assume the 11th edit is approved (no memory of past decisions)

This is the right balance: your preference (mode) is remembered, but each change requires fresh evaluation.

#### 🤝 Practice Exercise

> **Ask your AI**: "Walk me through a scenario where I deny a permission request. What happens next? Then show me an example where I approve. How do those two interactions differ?"

**Expected Outcome**: You'll understand that denying slows progress (requires clarification) while approving keeps workflow moving—helping you decide when each is appropriate.

---

## Best Practices: Building Safe Habits

### Start Permissive Only After Understanding

**Temptation**: "Default mode is slowing me down. Let me switch to acceptEdits."

**Better approach**: Switch modes intentionally, not by frustration.
- Understand what each mode means
- Recognize your current confidence level
- Start with default until you're comfortable
- Graduate to acceptEdits when you trust your specifications

### Use Default Mode When Learning

When you're **learning** Claude Code or working in **unfamiliar code**, stay in default mode. Every "May I?" prompt is a learning opportunity:
- You see what Claude Code plans to do
- You catch mistakes early
- You build intuition about what good code changes look like

### AcceptEdits is for Experienced Workflows

Use acceptEdits when:
- You've worked in this codebase before
- Your specifications are crystal clear
- You review git changes frequently (so you catch surprises)
- You understand the consequences of auto-approved edits

### Review Changes After Auto-Approval

If you use acceptEdits, **establish a habit**:
```bash
git diff
```

After Claude Code runs, check what actually changed. This prevents surprises and helps you catch edge cases.

#### 🎓 Expert Insight
> Permission modes are like **car safety features**. Default mode is like cruise control with lane-keeping assist—safety features actively protect you. AcceptEdits is like driving without those features—faster, but you need to be skilled and attentive. Don't switch until you're ready.

---

## Try With AI

Now let's practice understanding your permission system.

**Setup**: Open Claude Code in your terminal and work through these prompts to understand permissions deeply.

### Prompt 1: Check Your Current Permissions

```bash
claude "/permissions"
```

Read the output and answer: What mode are you in? What does that mean for file edits and bash commands?

**Expected Outcome**: You see your current permission mode and understand what gets auto-approved vs. what still requires permission.

### Prompt 2: Understand Permission Trade-offs

```
In Claude Code, I'm in 'default' mode (asks every time).
Explain what happens if I switch to 'acceptEdits'. What changes?
What operations would still ask for permission?
```

**Expected Outcome**: AI explains that files auto-approve but dangerous bash commands still require permission. You understand the specific trade-offs.

### Prompt 3: Scenario-Based Response

```
Scenario: I ask Claude Code to "Add user login to my app."
Claude proposes editing three files: models.py, routes.py, and templates.py.
I'm in default mode.

What happens next? What do I see? What choices do I have?
Then explain: If I deny the first file edit, what should I do?
```

**Expected Outcome**: AI walks you through the interaction—you see prompts for each file, understand you approve/deny individually, and know how to course-correct if you deny.

### Prompt 4 (Stretch Challenge): Plan Mode Workflow

```
Explain what permission 'plan' mode does with a concrete example.
Show me what a plan looks like when I ask Claude Code to:
"Create a complete REST API with user authentication, database setup, and tests."
```

**Expected Outcome**: AI shows you how plan mode groups operations, shows the full plan upfront, and lets you approve the entire workflow at once.

**Safety Note**: Permissions exist to keep your system safe. Don't rush to auto-approve modes before understanding what you're approving. Test prompts in default mode first, then graduate to acceptEdits once you have a clear workflow. Remember: faster isn't better if it leads to mistakes.

