---
title: "Lesson 2: Basic Prompt Structure"
sidebar_label: "Basic Prompt Structure"
sidebar_position: 2
description: "Learn the three-element pattern for clear prompts: Task + Context + Format"
---

# Lesson 2: Basic Prompt Structure

In Lesson 1, you learned that specific prompts work better than vague ones. But what makes a prompt "specific"? This lesson teaches you a simple three-element pattern that works for most AI prompts: **Task + Context + Format**.

Think of it like giving directions. You wouldn't just say "go somewhere" (vague). You'd say:
- **Task**: "Drive to the grocery store"
- **Context**: "the one on Main Street, not the downtown location"
- **Format**: "take Highway 1 and turn left at the second light"

AI prompts work the same way. When you structure your prompts clearly, AI understands exactly what you need.

## The Three Elements

Every effective prompt has three parts:

### 1. Task — WHAT You Want

This is your action verb. It tells AI what to DO with the information.

**Common action verbs for development tasks**:
- **Explain**: Break down a concept or command
- **Create**: Generate code, docs, or configurations
- **Debug**: Find and fix errors
- **Optimize**: Improve performance or clarity
- **Compare**: Show differences between approaches
- **Validate**: Check if something is correct

**Example tasks**:
- "Explain the difference between git merge and git rebase"
- "Create a bash script to backup my documents folder"
- "Debug this script that's failing with permission denied"

**Why task matters**: Without a clear action verb, AI doesn't know if you want an explanation, example code, or a complete implementation.

---

### 2. Context — Background AI Needs

This is what AI needs to know ABOUT YOU to give a useful answer.

**Common context elements**:
- **Your experience level**: "I'm new to bash" or "I understand basic git"
- **Your project type**: "for a personal backup script" or "for documentation"
- **What you've tried**: "I used ls but got unexpected output"
- **Your environment**: "on macOS" or "in a GitHub repository"

**Example contexts**:
- "assuming I understand basic bash commands"
- "for a personal project, not production"
- "I'm familiar with markdown headings but not tables"

**Why context matters**: AI adjusts its response based on what you know. If you say "I'm new to git," AI will explain from the basics. If you say "I understand merge," AI skips that and focuses on new concepts.

---

### 3. Format — HOW You Want the Answer

This tells AI what structure you want in the response.

**Common formats**:
- **Bullet points**: "in 3 bullet points"
- **Code block**: "as a bash script with comments"
- **Step-by-step**: "with numbered steps I can follow"
- **Table**: "in a markdown table comparing options"
- **Examples**: "with 2 examples showing before and after"

**Example formats**:
- "in 3 bullet points with examples"
- "as a bash script with comments explaining each line"
- "with step-by-step instructions I can copy and paste"

**Why format matters**: AI can explain the same concept in dozens of ways. Specifying the format ensures you get information in the form you'll actually use.

## Putting It Together: Task + Context + Format

Let's see how the three elements combine:

### Example 1: Git Command Explanation

**Without structure** (vague):
"git rebase"

**With structure**:
- **Task**: "Explain git rebase"
- **Context**: "assuming I understand git merge"
- **Format**: "in 3 bullet points with examples"

**Full prompt**:
"Explain git rebase, assuming I understand git merge, in 3 bullet points with examples."

---

### Example 2: Bash Script Creation

**Without structure** (vague):
"backup script"

**With structure**:
- **Task**: "Create a bash script to backup my documents folder"
- **Context**: "for macOS, saving to an external drive"
- **Format**: "with comments explaining each command"

**Full prompt**:
"Create a bash script to backup my documents folder for macOS, saving to an external drive, with comments explaining each command."

---

### Example 3: Markdown Documentation

**Without structure** (vague):
"markdown table"

**With structure**:
- **Task**: "Show me how to create a markdown table"
- **Context**: "for documenting bash command options"
- **Format**: "with example syntax and rendered output"

**Full prompt**:
"Show me how to create a markdown table for documenting bash command options, with example syntax and rendered output."

## Practice: Write Structured Prompts

Write three prompts using the Task + Context + Format structure. Do this WITHOUT AI—practice thinking through each element before you start prompting.

### Scenario 1: Bash Command Help

You need to understand what the `chmod` command does.

**Your prompt** (fill in each element):
- **Task** (what you want AI to do):
- **Context** (what AI needs to know about your situation):
- **Format** (how you want the answer):

**Full prompt** (combine all three):

---

### Scenario 2: Git Workflow Question

You want to know when to use `git fetch` vs `git pull`.

**Your prompt** (fill in each element):
- **Task**:
- **Context**:
- **Format**:

**Full prompt**:

---

### Scenario 3: Markdown Formatting

You need to create a markdown document for a project README.

**Your prompt** (fill in each element):
- **Task**:
- **Context**:
- **Format**:

**Full prompt**:

---

**After you've written your three prompts**, review them:

- Does each have a clear action verb? (Task)
- Does each explain your situation? (Context)
- Does each specify how you want the answer? (Format)

## Try With AI

Now test your structured prompts from the practice exercise above. Use Claude Code or Gemini CLI and:

1. **Test your Scenario 1 prompt** (chmod command)
   - Type your full structured prompt
   - Evaluate the response:
     - Did AI understand your task?
     - Did the context shape the answer?
     - Did you get the format you requested?

2. **Test your Scenario 2 prompt** (git fetch vs pull)
   - Type your full structured prompt
   - Evaluate the response:
     - Was the explanation at the right level for your experience?
     - Did the format make it easy to understand?

3. **Test your Scenario 3 prompt** (markdown README)
   - Type your full structured prompt
   - Evaluate the response:
     - Did AI provide what you asked for?
     - Could you use the response immediately?

**Experiment**:
- Try removing one element (Task, Context, OR Format) from one prompt
- Compare the response to the full structured version
- What changed when you removed that element?

**Reflection questions**:
- Which element (Task, Context, Format) made the biggest difference in response quality?
- When you removed an element, how did AI compensate (or fail to)?
- What would you add to your prompts that's NOT in the three elements?
