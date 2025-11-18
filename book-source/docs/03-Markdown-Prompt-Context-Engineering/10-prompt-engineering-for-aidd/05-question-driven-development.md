---
title: "Lesson 5: Question-Driven Development"
sidebar_label: "Question-Driven Development"
sidebar_position: 5
description: "Prompt AI to ask clarifying questions before providing solutions"
---

# Lesson 5: Question-Driven Development

In Lesson 4, you learned to refine prompts through iteration. But what if AI could help you write better prompts BEFORE giving you an answer? That's Question-Driven Development (QDD).

Instead of asking AI to solve your problem immediately, you ask AI to ask YOU questions first. AI's questions reveal gaps in your request and help you provide the context needed for a tailored solution.

Think of it like visiting a technical consultant. A good consultant doesn't immediately give you a solution—they ask about your specific situation, constraints, and goals first. AI can do the same thing, if you prompt it to.

## The Problem: One-Size-Fits-All Answers

When you ask AI a complex question without enough context, you get generic advice:

**Your prompt**:
"Explain git workflows"

**AI's response**:
"Git workflows are collaboration patterns. The most common are:
- **Centralized Workflow**: Single main branch, all commits go there
- **Feature Branch Workflow**: Each feature gets its own branch
- **Gitflow**: Structured workflow with main, develop, feature, release, and hotfix branches
- **Forking Workflow**: Each developer has their own remote repository

Choose based on team size, project type, and release cadence."

**What's wrong?**
- You work alone, not on a team (irrelevant advice)
- You don't need release management yet (too complex)
- You wanted something simpler for personal projects

AI gave you accurate information, but it wasn't TAILORED to your needs. If AI had asked about your situation first, it would have given you a different answer.

## Question-Driven Development: Let AI Ask First

Here's the same scenario using QDD:

**Your QDD prompt**:
"Before explaining git workflows, ask me 5 questions about my experience level and project needs. Use my answers to give me a tailored recommendation."

**AI's questions**:
1. Are you working solo or with a team?
2. What type of project are you working on (personal, open-source, production)?
3. How often do you plan to release updates?
4. Have you used git branching before, or is this your first time?
5. What's your main goal: learning git, collaborating with others, or managing releases?

**Your answers**:
1. Solo developer
2. Personal scripts and small automation projects
3. No formal releases—I just commit when features work
4. I've used branching once or twice but kept it simple
5. I want to keep my code organized without overcomplicating things

**AI's tailored response**:
"Based on your answers, I recommend a **simple feature branch workflow**:

- **Main branch**: Stable code that works
- **Feature branches**: Create a branch when trying something new
- **No release branches needed**: Merge to main when ready

Example workflow:
```bash
# Start new feature
git checkout -b add-backup-logging

# Work on feature, commit changes
git add .
git commit -m "Add logging to backup script"

# Merge when feature works
git checkout main
git merge add-backup-logging
```

This keeps main clean without the overhead of Gitflow or team collaboration patterns."

**What's different?**
- AI asked about your situation (solo vs. team)
- AI tailored complexity to your needs (simple, not Gitflow)
- AI gave you concrete steps for YOUR use case
- AI didn't waste time on irrelevant patterns

## When to Use Question-Driven Development

QDD works best for:

**1. Complex tasks with multiple valid approaches**
- "How should I structure my git repository?"
- "What's the best way to automate backups?"
- "How do I organize documentation for my scripts?"

**2. Tasks where your context changes the answer significantly**
- Solo vs. team workflows
- Beginner vs. advanced techniques
- Personal projects vs. production systems

**3. Tasks where you don't know what information AI needs**
- You know you need help, but you're not sure what details matter
- You haven't done this task before

**When NOT to use QDD:**
- Simple, factual questions ("What does `chmod 755` do?")
- Tasks with one obvious answer ("How do I create a markdown heading?")
- When you already know exactly what you need

## How to Prompt for Questions

The basic pattern:

**"Before [doing the task], ask me [number] questions about [what you need to know]. Use my answers to [desired outcome]."**

### Example 1: Bash Script Design

**QDD prompt**:
"Before writing a backup script for me, ask me 5 questions about what I need to back up, where it should go, and how often I'll run it. Use my answers to create a script that fits my specific needs."

**Why it works**:
- Specifies the number of questions (5)
- Identifies what areas AI should ask about (what, where, frequency)
- States the desired outcome (tailored script)

---

### Example 2: Git Branch Strategy

**QDD prompt**:
"Before recommending a git workflow, ask me 4 questions about my team size, project type, and release process. Use my answers to recommend the simplest workflow that meets my needs."

**Why it works**:
- Number of questions (4)
- Areas to explore (team, project, releases)
- Desired outcome (simplest that works)

---

### Example 3: Markdown Documentation Structure

**QDD prompt**:
"Before creating a markdown template for my project documentation, ask me 3 questions about what I'm documenting, who will read it, and what sections I need. Use my answers to create a template I can reuse."

**Why it works**:
- Number of questions (3)
- Areas to ask about (content, audience, structure)
- Desired outcome (reusable template)

## Answering AI's Questions Effectively

When AI asks you questions, your answers shape the final solution. Good answers:

**1. Are specific, not vague**
- ❌ "Normal team size"
- ✅ "Solo developer, occasionally one collaborator"

**2. Include your constraints**
- ❌ "Daily backups"
- ✅ "Daily backups, but they need to run without manual intervention"

**3. Acknowledge what you don't know**
- ❌ Guessing at technical details
- ✅ "I don't know yet—recommend best practices"

**4. Explain your goals**
- ❌ "Make it work"
- ✅ "I want to learn the concept, not just copy code"

## Comparing Direct vs. Question-Driven Approaches

Let's see both approaches side-by-side:

### Direct Approach

**Prompt**: "Create a bash script to organize my downloads folder"

**AI's output**: A generic script that:
- Moves files by extension (.pdf, .jpg, .txt)
- Creates folders if they don't exist
- Logs the actions

**Problem**: You wanted to organize by date, not file type.

---

### Question-Driven Approach

**Prompt**: "Before creating a bash script to organize my downloads folder, ask me 4 questions about how I want files organized. Use my answers to create a script that matches my workflow."

**AI asks**:
1. How do you want to organize files—by type, by date, by project, or something else?
2. Should the script move or copy files?
3. Should the script run automatically or manually?
4. What should happen if a file already exists in the destination?

**Your answers**:
1. By month (YYYY-MM folders)
2. Move files
3. Manually for now
4. Skip duplicates, don't overwrite

**AI's tailored output**: A script that:
- Creates YYYY-MM folders based on file modification dates
- Moves (not copies) files
- Skips files that already exist in destination
- Includes a dry-run option for testing

**Result**: You got exactly what you needed without multiple iterations.

## Practice: Write Question-Driven Prompts

For each scenario below, write a QDD prompt. Do this WITHOUT AI first.

### Scenario 1: Git Commit Message Style

You want AI to help you write better commit messages, but you're not sure what style to follow.

**Your QDD prompt** (write it):

**What questions should AI ask you?** (predict 3-4):
1.
2.
3.
4.

---

### Scenario 2: Bash Error Handling

You want to add error handling to your scripts, but you don't know where to start.

**Your QDD prompt** (write it):

**What questions should AI ask you?** (predict 3-4):
1.
2.
3.
4.

---

### Scenario 3: Markdown Documentation Template

You need a documentation template for your collection of scripts.

**Your QDD prompt** (write it):

**What questions should AI ask you?** (predict 3-4):
1.
2.
3.
4.

---

**After you've written your prompts**, review them:
- Did you specify how many questions AI should ask?
- Did you identify what areas AI should explore?
- Did you state what you want as the final outcome?

## Try With AI

Now test Question-Driven Development with real prompts. Use Claude Code or Gemini CLI:

### Exercise 1: Git Workflow Recommendation

**Use this QDD prompt**:
"Before recommending a git workflow for me, ask me 5 questions about my experience, team size, project type, and goals. Use my answers to recommend the simplest workflow that meets my needs."

**Answer AI's questions honestly**

**Evaluate the tailored response**:
- Did AI's questions reveal assumptions you didn't state?
- Did the final answer match your actual needs?
- Compare this to what you'd get from "Explain git workflows"—which was more useful?

---

### Exercise 2: Bash Script Design (Your Choice)

Think of a bash script you actually need. Use QDD:

**Your QDD prompt**:
"Before writing a bash script to [your task], ask me 5 questions about [relevant areas]. Use my answers to create a script that [desired outcome]."

**Answer AI's questions**

**Evaluate the result**:
- Did AI ask about things you hadn't considered?
- Did answering the questions clarify your own requirements?
- Was the final script closer to what you needed than a direct "create script" prompt?

---

### Exercise 3: Compare Approaches

Pick one task and try BOTH approaches:

**Direct prompt**: "Explain [topic]"
- Note the response

**QDD prompt**: "Before explaining [topic], ask me 3 questions about my experience and what I need to know. Use my answers to tailor the explanation."
- Answer AI's questions
- Note the response

**Compare**:
- Which approach gave you more useful information?
- Which approach required less iteration?
- Which approach taught you something unexpected?

---

**Reflection questions**:
- When did AI's questions surprise you (ask about something you hadn't thought of)?
- When did answering questions help you clarify your own needs?
- When would you use QDD instead of direct prompting?
- When would direct prompting be faster and better?
