---
title: "Lesson 1: Why Prompting Matters"
sidebar_label: "Why Prompting Matters"
sidebar_position: 1
description: "Learn why clear prompts get better AI responses through comparison of vague vs. specific examples"
---

# Lesson 1: Why Prompting Matters

You're stuck on a Bash command. You open Claude Code and type: "help with ls". The AI responds with a general overview of the `ls` command—history, basic usage, and a list of common flags. It's accurate, but it doesn't answer your specific question about the output you're seeing.

You try again: "explain the ls -la output showing file permissions and sizes". This time, AI gives you exactly what you need: a breakdown of the permission columns, file size units, and how to interpret the output format.

**What changed?** The second prompt was specific. It told AI exactly what you needed help with. This lesson teaches you why clarity matters when working with AI.

## The Problem with Vague Prompts

When you ask AI for "help" without context, you're forcing it to guess what you need. AI has no way of knowing:

- What you already understand
- What specific problem you're trying to solve
- What format of answer would be most useful

Let's look at five common scenarios where vague prompts fail:

### Example 1: Bash Commands

**Vague**: "help with ls"

**Why it fails**: AI doesn't know if you want command options, output interpretation, or usage examples.

**Specific**: "explain ls -la output showing file permissions and sizes"

**Why it works**: Clear task (explain), specific command (ls -la), exact focus (permissions and sizes).

---

### Example 2: Git Operations

**Vague**: "git problems"

**Why it fails**: Thousands of potential issues. AI can't prioritize without more information.

**Specific**: "why does git status show 'detached HEAD' after checkout?"

**Why it works**: Specific symptom (detached HEAD), specific command (git status), clear context (after checkout).

---

### Example 3: Markdown Formatting

**Vague**: "markdown help"

**Why it fails**: Markdown has dozens of features. AI has no way to narrow the scope.

**Specific**: "how do I create a markdown table with headers and 3 rows of data?"

**Why it works**: Specific feature (table), specific requirements (headers, 3 rows), clear deliverable.

---

### Example 4: File Operations

**Vague**: "find files"

**Why it fails**: What files? Where? Based on what criteria?

**Specific**: "find all .txt files in my home directory modified in the last 7 days"

**Why it works**: File type (.txt), location (home directory), criteria (modified last 7 days).

---

### Example 5: Script Debugging

**Vague**: "script not working"

**Why it fails**: No error message, no code context, no clue what "not working" means.

**Specific**: "my bash backup script fails with 'permission denied' when copying to /backup/"

**Why it works**: Script type (bash backup), error message (permission denied), operation (copying), location (/backup/).

---

## Why Specific Prompts Work Better

AI is a collaborator, not a mind reader. It works best when you provide:

1. **Context**: What are you working on?
2. **Task**: What do you need AI to do?
3. **Details**: What specific aspects matter?

Think of AI like a technical consultant you've hired. If you walked into their office and said "computer problems," they'd ask clarifying questions. When you're specific upfront, you skip the back-and-forth and get useful answers immediately.

**Key insight**: AI doesn't "understand" like humans do. It pattern-matches your prompt against millions of examples. Specific prompts give AI more patterns to match, leading to more targeted responses.

## Practice: Improve Vague Prompts

Take these three vague prompts and rewrite them to be specific. Do this exercise WITHOUT using AI—the goal is to practice thinking about clarity before you start prompting.

### Prompt 1 (Vague)
"bash syntax"

**Your improved version** (write your answer):
- What specific bash syntax feature do you need?
- What's your use case?
- What format do you want the answer in?

---

### Prompt 2 (Vague)
"explain git"

**Your improved version** (write your answer):
- Which git concept or command?
- What's your experience level?
- What problem are you trying to solve?

---

### Prompt 3 (Vague)
"markdown formatting"

**Your improved version** (write your answer):
- Which markdown feature?
- What are you trying to format?
- Do you need examples?

---

**After you've written your improved prompts**, compare them to the originals. Ask yourself:

- Did I specify what I want AI to do? (Task)
- Did I provide enough context? (Background)
- Did I clarify what kind of answer I need? (Format)

## Try With AI

Now test your improved prompts from the practice exercise above. Use Claude Code or Gemini CLI and:

1. **Test the vague prompt first**
   - Type the original vague prompt (e.g., "bash syntax")
   - Note the response quality
   - Was it generic or specific?

2. **Test your improved prompt**
   - Type your rewritten, specific prompt
   - Note the response quality
   - How much more useful is it?

3. **Compare the results**
   - Which prompt gave you actionable information?
   - Which prompt required follow-up questions?
   - What made the difference?

**Reflection questions**:
- What patterns do you notice in prompts that work well?
- When you added specificity, what kinds of details helped most?
- How would you explain "specific prompts" to someone learning AI collaboration?

