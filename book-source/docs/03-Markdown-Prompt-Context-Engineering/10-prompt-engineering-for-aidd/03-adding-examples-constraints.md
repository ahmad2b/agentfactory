---
title: "Lesson 3: Adding Examples and Constraints"
sidebar_label: "Adding Examples and Constraints"
sidebar_position: 3
description: "Enhance prompts with examples showing desired output style and constraints limiting scope"
---

# Lesson 3: Adding Examples and Constraints

You've learned the basic three-element structure (Task + Context + Format). Now you'll refine your prompts further by adding **examples** and **constraints**. These two additions help AI understand exactly what you want—and what you DON'T want.

Think of examples as showing AI your preferred style. Think of constraints as setting boundaries. Together, they make your prompts more precise.

## Why Examples Matter

Telling AI "write in a clear style" is vague. Showing AI an example of what you consider "clear" is specific.

### The Difference Examples Make

**Without example**:
"Create a markdown README for my backup script"

AI might give you:
- A 500-word document with sections you don't need
- Technical jargon that's too advanced
- A structure that doesn't match your project

**With example**:
"Create a markdown README for my backup script, similar to this structure:
```
# Script Name
Brief description

## Usage
Command to run the script

## Options
List of flags with explanations
```

AI will match your example structure and tone.

### When to Provide Examples

Use examples when you need AI to:
- Match a specific writing style or tone
- Follow a particular structure or format
- Replicate a pattern you've used before
- Generate output similar to something you like

### Example Types

**1. Structure examples** (show the format):
```
"Create a git commit message following this pattern:
type(scope): brief description

Extended explanation of what changed and why.
"
```

**2. Style examples** (show the tone):
```
"Explain git branches using simple analogies like this:
'A branch is like a copy of your project where you can experiment
without affecting the original.'"
```

**3. Output examples** (show desired result):
```
"Generate bash comments like these:
# Check if directory exists before creating it
# Loop through all .txt files in current directory"
```

## Why Constraints Matter

Constraints tell AI what to avoid or limit. Without constraints, AI might:
- Give you more than you need
- Use complexity you can't follow
- Include features you don't want

### The Difference Constraints Make

**Without constraints**:
"Explain how to use git branches"

AI might give you:
- A 2000-word essay covering advanced scenarios
- Explanations of remote branches, rebasing, and merge strategies
- Technical details about HEAD pointers and ref logs

**With constraints**:
"Explain how to use git branches in 200 words maximum, focusing only on creating and switching between local branches, using beginner-friendly language"

AI will stay focused and brief.

### Common Constraint Types

**1. Length constraints**:
- "in 100 words or less"
- "with 3 bullet points maximum"
- "one paragraph only"

**2. Complexity constraints**:
- "using beginner-friendly language"
- "without technical jargon"
- "assuming I've never used [tool] before"

**3. Scope constraints**:
- "focusing only on [specific feature]"
- "excluding advanced topics like [X, Y, Z]"
- "for personal projects, not production systems"

**4. Style constraints**:
- "without using analogies"
- "in a professional tone"
- "with practical examples, not theory"

**5. Format constraints**:
- "as a bash script, not pseudocode"
- "with inline comments, not a separate explanation"
- "in a markdown table, not prose"

## Combining Examples and Constraints

The most effective prompts use both. Examples show what you want. Constraints prevent what you don't want.

### Example 1: Bash Script Help

**Basic prompt** (from Lesson 2):
"Create a bash script to backup my documents folder for macOS, with comments"

**Enhanced with examples and constraints**:
"Create a bash script to backup my documents folder for macOS, with comments explaining each line.

**Example style I want**:
```bash
# Create backup directory if it doesn't exist
mkdir -p /path/to/backup
```

**Constraints**:
- Maximum 20 lines of code
- Use simple commands only (cp, mkdir, no rsync)
- Assume source is ~/Documents and destination is /Volumes/Backup"

---

### Example 2: Git Command Explanation

**Basic prompt** (from Lesson 2):
"Explain git rebase, assuming I understand git merge, in 3 bullet points"

**Enhanced with examples and constraints**:
"Explain git rebase, assuming I understand git merge, in 3 bullet points with examples.

**Example of explanation style I prefer**:
'Git merge combines branches by creating a new commit that has both branches as parents.'

**Constraints**:
- Each bullet point: 1-2 sentences maximum
- Use simple analogies, avoid technical terms like 'DAG' or 'ref'
- Focus only on basic rebase, not interactive rebase"

---

### Example 3: Markdown Documentation

**Basic prompt** (from Lesson 2):
"Create a markdown table for documenting bash command options, with example syntax"

**Enhanced with examples and constraints**:
"Create a markdown table for documenting bash command options.

**Example format I want**:
| Option | Description | Example |
|--------|-------------|---------|
| `-a`   | Show all   | `ls -a` |

**Constraints**:
- Maximum 5 rows
- Keep descriptions under 10 words each
- Use only common options (-a, -l, -h, -r)"

## Practice: Enhance Your Prompts

Take these three basic prompts and add examples and constraints. Do this manually, WITHOUT AI.

### Prompt 1: Bash Script

**Basic**:
"Create a bash script to list all files modified in the last 7 days"

**Your enhanced version** (add examples and constraints):

**Example you'd provide**:

**Constraints you'd add**:
1.
2.
3.

**Full enhanced prompt**:

---

### Prompt 2: Git Help

**Basic**:
"Explain the difference between git fetch and git pull"

**Your enhanced version** (add examples and constraints):

**Example you'd provide**:

**Constraints you'd add**:
1.
2.
3.

**Full enhanced prompt**:

---

### Prompt 3: Markdown Formatting

**Basic**:
"Create a markdown README for a personal script repository"

**Your enhanced version** (add examples and constraints):

**Example structure you'd provide**:

**Constraints you'd add**:
1.
2.
3.

**Full enhanced prompt**:

---

**After you've enhanced all three prompts**, review them:

- Do your examples show the specific style or structure you want?
- Do your constraints limit scope, complexity, or length?
- Would AI have enough guidance to match your needs?

## Try With AI

Now test your enhanced prompts from the practice exercise. Use Claude Code or Gemini CLI and:

1. **Test Prompt 1** (basic version first)
   - Type the basic prompt: "Create a bash script to list all files modified in the last 7 days"
   - Note what AI generates

2. **Test Prompt 1** (enhanced version)
   - Type your enhanced prompt with examples and constraints
   - Compare the output to the basic version
   - Did the example guide AI's style?
   - Did the constraints limit scope effectively?

3. **Test Prompt 2 and 3** (enhanced versions only)
   - Type your enhanced prompts
   - Evaluate if AI followed your examples
   - Evaluate if AI respected your constraints

**Experiment**:
- Try adding a constraint AI can't follow (e.g., "in exactly 47 words")
- See how AI handles impossible or conflicting constraints
- Adjust your constraints based on the response

**Reflection questions**:
- When did examples help most? When did they not matter?
- Which constraint types (length, complexity, scope, style) had the biggest impact?
- How many constraints are too many? Did you overwhelm AI with too much guidance?
