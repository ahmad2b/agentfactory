---
title: "Lesson 7: Building Your Prompt Library"
sidebar_label: "Building Your Prompt Library"
sidebar_position: 7
description: "Create reusable prompt templates for recurring development tasks"
---

# Lesson 7: Building Your Prompt Library

You've spent six lessons learning to write effective prompts. Now you'll learn to recognize patterns in your work and create reusable templates that save time and improve consistency.

A prompt library is a collection of templates for tasks you do repeatedly. Instead of writing prompts from scratch each time, you fill in placeholders with your specific details.

Think of it like code functions. Instead of rewriting the same logic, you create a function once and call it with different parameters. Prompt templates work the same way.

## Why Build a Prompt Library?

**Efficiency**: Writing prompts from scratch every time is slow. Templates let you reuse what works.

**Consistency**: Templates ensure you don't forget important elements (context, constraints, format).

**Learning**: Creating templates forces you to identify what makes prompts effective.

**Sharing**: Templates can be shared with teammates or used across projects.

**Example**:

Without a template, you write this from scratch every time you need help with git commits:
"Write a git commit message for the feature I just added that lets users export data to CSV, following the conventional commits format with a type prefix and clear description."

With a template, you fill in placeholders:
"Write a git commit message for [FEATURE] that [ACTION], following [STYLE] format."

The template takes 10 seconds to customize. The from-scratch prompt takes 2 minutes.

## Recognizing Recurring Tasks

The first step is identifying patterns. Look at your recent prompts:

**Pattern recognition questions**:
1. Do I ask AI to do similar tasks repeatedly?
2. Do I use the same structure or constraints often?
3. Do I explain the same context multiple times?
4. Could I reuse this prompt with minor changes?

**Example recurring tasks for developers**:
- **Git commit messages**: You write commits daily
- **Bash script debugging**: You debug scripts regularly
- **Command explanations**: You ask "what does this do?" frequently
- **Markdown documentation**: You create READMEs for new projects
- **Error message help**: You search for error explanations often

If you've done something twice, it's worth templating.

## Anatomy of a Good Template

A template has three parts:

### 1. Placeholders for Variables

Use `[BRACKETS]` or `{CURLY_BRACES}` for parts that change:

**Template**:
```
Explain the [COMMAND] command, assuming I understand [PRIOR_KNOWLEDGE],
in [FORMAT] with [NUMBER] examples.
```

**Filled in**:
```
Explain the git rebase command, assuming I understand git merge,
in 3 bullet points with 2 examples.
```

---

### 2. Usage Notes (When to Use This Template)

Document when this template applies:

**Template name**: Git Commit Message

**When to use**:
- After you've staged changes with `git add`
- You need a clear, conventional commit message
- You want to follow the conventional commits style

**When NOT to use**:
- For WIP (work in progress) commits
- For merge commits (git generates those automatically)

---

### 3. Example of Filled Template

Show how the template looks when used:

**Template**:
```
Write a git commit message for [FEATURE] that [ACTION],
following [STYLE] format.
```

**Example**:
```
Write a git commit message for backup script logging that adds
detailed output about files copied, following conventional commits format.
```

**Output**:
```
feat(backup): add detailed logging for file copy operations

- Log each file copied with source and destination
- Include timestamp and total file count
- Add error logging for failed operations
```

## Template Categories

Organize templates by task type:

### Category 1: Explain

**Purpose**: Get AI to explain concepts, commands, or code

**Template structure**:
```
Explain [CONCEPT], assuming I understand [BACKGROUND],
in [FORMAT] with [LEVEL] of detail.
```

**When to use**: Understanding new commands, comparing options, learning concepts

**Example**:
```
Explain git stash, assuming I understand basic git commits and branches,
in 3 bullet points with beginner-friendly language.
```

---

### Category 2: Debug

**Purpose**: Get AI to help fix errors or diagnose problems

**Template structure**:
```
Debug this [TYPE] script that fails with [ERROR] at [LOCATION]:
[CODE]

[CONTEXT about what you expected to happen]
```

**When to use**: Scripts fail, commands produce errors, unexpected behavior

**Example**:
```
Debug this bash script that fails with "permission denied" at line 5:
#!/bin/bash
cp ~/Documents/*.txt /backup/

I expected it to copy all .txt files to the backup directory.
```

---

### Category 3: Create

**Purpose**: Get AI to generate code, scripts, or documentation

**Template structure**:
```
Create a [TYPE] to [PURPOSE], for [CONTEXT], with [REQUIREMENTS].

Constraints:
- [CONSTRAINT_1]
- [CONSTRAINT_2]
- [CONSTRAINT_3]
```

**When to use**: Starting new scripts, generating boilerplate, creating documentation

**Example**:
```
Create a bash script to backup my documents folder, for macOS,
with comments explaining each step.

Constraints:
- Use only basic commands (no rsync)
- Check if destination directory exists before copying
- Log each file copied
```

---

### Category 4: Optimize

**Purpose**: Get AI to improve existing code or solutions

**Template structure**:
```
Optimize this [CODE/SCRIPT/COMMAND] to [GOAL]:
[CURRENT_VERSION]

Focus on [OPTIMIZATION_TYPE: performance/readability/simplicity].
```

**When to use**: Code works but is slow, messy, or too complex

**Example**:
```
Optimize this bash script to improve readability:
#!/bin/bash
for f in $(ls *.txt); do cp $f /backup/$f; done

Focus on simplicity and best practices.
```

## Creating Your First Three Templates

Let's build three templates based on tasks you've practiced in previous lessons.

### Template 1: Git Commit Message

**Template name**: `git-commit-message.md`

**When to use**: Writing conventional commit messages for features, fixes, or docs

**Template**:
```
Write a git commit message for [FEATURE/FIX/DOCS] that [WHAT_CHANGED],
following conventional commits format with type prefix.

Changes made:
- [CHANGE_1]
- [CHANGE_2]
- [CHANGE_3]
```

**Example filled**:
```
Write a git commit message for a new feature that adds backup logging,
following conventional commits format with type prefix.

Changes made:
- Added timestamp logging for each backup operation
- Included file count in summary
- Created log file in ~/backup-logs/
```

---

### Template 2: Bash Script Debugging

**Template name**: `bash-debug.md`

**When to use**: Script produces errors or unexpected behavior

**Template**:
```
Debug this bash script that fails with "[ERROR_MESSAGE]" at [LINE/LOCATION]:

```bash
[SCRIPT_CODE]
```

Expected behavior: [WHAT_YOU_EXPECTED]
Actual behavior: [WHAT_HAPPENED]
Environment: [macOS/Linux, bash version if known]
```

**Example filled**:
```
Debug this bash script that fails with "No such file or directory" at the cp command:

```bash
#!/bin/bash
cp ~/Documents/*.txt /backup/
echo "Backup complete"
```

Expected behavior: Copy all .txt files from Documents to /backup/
Actual behavior: Script fails immediately with error
Environment: macOS, bash 5.0
```

---

### Template 3: Markdown Documentation

**Template name**: `markdown-readme.md`

**When to use**: Creating README files for scripts or small projects

**Template**:
```
Create a markdown README for [PROJECT_NAME] that [PROJECT_PURPOSE].

Include these sections:
- [SECTION_1]
- [SECTION_2]
- [SECTION_3]

Constraints:
- Maximum [WORD_COUNT] words
- [TONE: beginner-friendly/technical/concise]
- Include [ADDITIONAL_REQUIREMENTS]
```

**Example filled**:
```
Create a markdown README for my backup scripts collection that helps users
automate file backups.

Include these sections:
- Installation (how to download and set up)
- Usage (basic commands to run backups)
- Configuration (how to customize backup destinations)

Constraints:
- Maximum 300 words
- Beginner-friendly tone
- Include examples for each script
```

## Practice: Create Your Own Templates

Build three templates for tasks YOU do regularly. Do this manually, WITHOUT AI.

### Your Template 1

**Template name**:

**When to use**:

**Template structure** (with [PLACEHOLDERS]):

**Example filled**:

---

### Your Template 2

**Template name**:

**When to use**:

**Template structure** (with [PLACEHOLDERS]):

**Example filled**:

---

### Your Template 3

**Template name**:

**When to use**:

**Template structure** (with [PLACEHOLDERS]):

**Example filled**:

---

**After you've created your templates**, review them:
- Do the placeholders clearly indicate what to fill in?
- Do the usage notes explain WHEN to use this template?
- Could someone else use your template without asking you questions?

## Version Control for Templates

Templates aren't static—they improve over time.

**Track what works**:
- Did this template produce good results?
- Did you have to refine the output anyway?
- Did you forget to include important context?

**Iterate and improve**:
- Add placeholders you wish you'd included
- Refine constraints based on AI's responses
- Update examples with better use cases

**Example evolution**:

**Version 1** (initial template):
```
Create a bash script to [TASK].
```

**Version 2** (added context and constraints):
```
Create a bash script to [TASK], for [ENVIRONMENT], with [REQUIREMENTS].
```

**Version 3** (added error handling reminder):
```
Create a bash script to [TASK], for [ENVIRONMENT], with [REQUIREMENTS].

Include:
- Error handling for [COMMON_FAILURE]
- Comments explaining [COMPLEX_PARTS]
```

Each version learned from previous usage.

## Try With AI

Now test your templates with real tasks. Use Claude Code or Gemini CLI:

### Exercise 1: Test Template 1 (Git Commit Message)

**Fill in your template**:
Think of a recent code change you made. Fill in the git commit template you created.

**Use with AI**:
Paste your filled template and see what commit message AI generates.

**Evaluate**:
- Did the template provide enough context?
- Was the output immediately usable?
- What would you change about the template?

---

### Exercise 2: Test Template 2 (Bash Debugging)

**Fill in your template**:
Find a bash script that has an error (or create one with an intentional bug).

**Use with AI**:
Paste your filled debugging template.

**Evaluate**:
- Did AI identify the issue?
- Did the template structure help AI give a focused answer?
- What information was missing?

---

### Exercise 3: Test Template 3 (Your Custom Template)

**Fill in one of your custom templates**

**Use with AI**:
Paste your filled template.

**Evaluate**:
- Did AI understand the placeholders?
- Did you get the output you expected?
- How would you refine this template for next time?

---

### Exercise 4: Template Evolution

**Pick one template that didn't work perfectly**

**Refine it**:
Based on AI's response, update the template:
- Add missing placeholders
- Clarify constraints
- Update the example

**Test the refined version**:
Use it on a similar task and compare results.

---

**Reflection questions**:
- Which templates saved you the most time?
- Which templates needed the most refinement?
- When did you realize a template was too generic or too specific?
- How would you organize templates as your library grows (folders, naming conventions)?
- What tasks do you do that you haven't templated yet?
