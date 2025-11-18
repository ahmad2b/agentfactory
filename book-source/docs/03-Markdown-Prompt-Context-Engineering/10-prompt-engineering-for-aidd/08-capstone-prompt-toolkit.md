---
title: "Lesson 8: Capstone - Your First Prompt Toolkit"
sidebar_label: "Capstone: Your First Prompt Toolkit"
sidebar_position: 8
description: "Build a comprehensive, reusable prompt toolkit for your development work"
---

# Lesson 8: Capstone - Your First Prompt Toolkit

You've learned to write clear prompts, iterate through collaboration, validate AI outputs, and create reusable templates. Now you'll put it all together by building your personal prompt toolkit—a collection of 5-7 templates with usage guidance that you'll actually use in your daily work.

This isn't a theoretical exercise. By the end of this lesson, you'll have a working toolkit you can reference every time you use AI for development tasks.

## What Is a Prompt Toolkit?

A prompt toolkit is:
- **5-7 templates** for tasks you do regularly
- **Clear usage criteria** for each template (when to use it)
- **A decision guide** that maps tasks to templates
- **Tested and validated** templates that produce good results

Think of it as your personal reference library. Instead of wondering "how should I prompt AI for this?" you'll have a tested template ready to go.

## Toolkit Requirements

Your toolkit must:

**1. Cover YOUR recurring tasks** (not generic examples)
- Audit what you actually do with AI
- Focus on tasks you've done 2+ times
- Templates should solve real problems you face

**2. Be immediately usable** (no clarification needed)
- Clear placeholders with descriptions
- Usage notes explain WHEN to use each template
- Examples show filled versions

**3. Include a decision guide** (task → template mapping)
- Map common tasks to specific templates
- Explain when to use Template A vs. Template B
- Cover edge cases ("What if none of these fit?")

**4. Be validated** (test each template)
- Test each template on a real task
- Verify it produces good results
- Refine based on testing

## Step 1: Audit Your Recurring Tasks

Before building templates, identify what you actually do with AI.

### Task Audit Questions

**Bash/Command-Line Tasks**:
- Do you debug bash scripts regularly?
- Do you ask AI to explain commands you don't recognize?
- Do you create automation scripts?
- Do you need help with file operations (find, grep, etc.)?

**Git Tasks**:
- Do you write commit messages?
- Do you need help with branching strategies?
- Do you ask how to undo or fix mistakes?
- Do you need explanations of git commands?

**Markdown/Documentation Tasks**:
- Do you create README files for projects?
- Do you document scripts or tools?
- Do you write notes or tutorials?
- Do you need formatting help?

**General Development Tasks**:
- Do you ask AI to optimize code?
- Do you need error explanations?
- Do you compare different approaches?
- Do you ask for best practices?

### Your Task List

Write down 5-7 tasks you've used AI for in the past month:

1.
2.
3.
4.
5.
6.
7.

**Prioritize**: Which tasks do you do most often? Which take the most time? Start with those.

## Step 2: Create 5-7 Templates

For each recurring task, create a template using this structure:

### Template Structure

```markdown
## Template [NUMBER]: [NAME]

**When to use**:
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]

**Template**:
```
[Your prompt template with [PLACEHOLDERS]]
```

**Example** (filled in):
```
[Show what the template looks like when used]
```

**Expected output**:
[Brief description of what AI should generate]
```

### Example Template: Git Commit Messages

```markdown
## Template 1: Git Commit Message

**When to use**:
- You've staged changes and need a commit message
- You want to follow conventional commits format
- Changes are significant enough to warrant detailed description

**Template**:
```
Write a git commit message for [FEATURE/FIX/DOCS/REFACTOR] that [BRIEF_DESCRIPTION].

Changes made:
- [CHANGE_1]
- [CHANGE_2]
- [CHANGE_3]

Follow conventional commits format with type prefix.
```

**Example** (filled in):
```
Write a git commit message for a feature that adds logging to the backup script.

Changes made:
- Added timestamp logging for each backup operation
- Created log file in ~/backup-logs/
- Included file count in completion message

Follow conventional commits format with type prefix.
```

**Expected output**:
Commit message with type prefix (feat/fix/docs), brief description, and detailed body explaining what changed and why.
```

Now create your templates. Aim for 5-7 that cover your most common tasks.

## Step 3: Create Your Decision Guide

A decision guide helps you choose the right template quickly. It's a mapping from tasks to templates.

### Decision Guide Structure

```markdown
# Decision Guide

## For Git Tasks
- **Writing commit messages** → Use Template 1: Git Commit Message
- **Undoing changes** → Use Template 2: Git Undo Help
- **Understanding git commands** → Use Template 3: Git Command Explainer

## For Bash Tasks
- **Debugging script errors** → Use Template 4: Bash Script Debugger
- **Creating new scripts** → Use Template 5: Bash Script Creator
- **Explaining commands** → Use Template 6: Command Explainer

## For Documentation Tasks
- **Creating README files** → Use Template 7: Markdown README Generator

## When No Template Fits
- Start with basic Task + Context + Format structure
- If you use it 2+ times, create a new template
- Use Question-Driven Development for complex, one-off tasks
```

### Your Decision Guide

Create a decision guide for YOUR templates:

```markdown
# My Prompt Toolkit Decision Guide

## For [Task Category 1]
- [Specific task] → Use Template [Number]: [Name]
- [Specific task] → Use Template [Number]: [Name]

## For [Task Category 2]
- [Specific task] → Use Template [Number]: [Name]
- [Specific task] → Use Template [Number]: [Name]

## When No Template Fits
- [Your strategy]
```

## Step 4: Test and Validate Each Template

Don't assume your templates work—test them.

### Testing Checklist

For each template:

**1. Fill it in with a real task**
- Use actual details from recent work
- Don't use made-up examples

**2. Use it with AI**
- Paste the filled template into Claude Code or Gemini CLI
- Evaluate the output quality

**3. Check validation criteria**
- Did AI understand the placeholders?
- Did you get the output format you expected?
- Would you use this output without changes?

**4. Refine if needed**
- Add missing placeholders
- Clarify constraints
- Update the example

**5. Document learnings**
- What worked well?
- What needed refinement?
- Would you change the template for next time?

### Validation Log

For each template, record your test results:

**Template**: [Name]

**Test task**: [What you tested it on]

**Result**: [What AI generated]

**Quality** (1-5 stars):

**Refinements needed**:
- [Change 1]
- [Change 2]

**Final version ready?**: Yes / No

## Your Complete Toolkit

Combine everything into a single markdown file.

### Toolkit File Structure

```markdown
# My Prompt Toolkit

Version: 1.0
Created: [Date]
Last Updated: [Date]

## Templates

### Template 1: [Name]
[Full template with usage notes and example]

### Template 2: [Name]
[Full template with usage notes and example]

### Template 3: [Name]
[Full template with usage notes and example]

[Continue for all 5-7 templates]

## Decision Guide

[Your decision guide mapping tasks to templates]

## Validation Log

[Optional: Track which templates you've tested and refined]

## Future Templates

[Tasks you do occasionally but haven't templated yet]
```

## Toolkit Quality Checklist

Before you consider your toolkit complete, verify:

**Completeness**:
- [ ] 5-7 templates included
- [ ] Each template has usage criteria
- [ ] Each template has example (filled version)
- [ ] Decision guide maps common tasks to templates

**Usability**:
- [ ] Placeholders clearly indicate what to fill in
- [ ] Someone else could use your templates without asking questions
- [ ] Templates solve actual problems you face

**Validation**:
- [ ] Each template tested on real task
- [ ] Quality verified (good AI outputs)
- [ ] Refinements applied based on testing

**Organization**:
- [ ] Templates grouped by category (Git, Bash, Markdown, etc.)
- [ ] Decision guide is easy to scan
- [ ] File structure is clear

## Try With AI

Now build your complete toolkit using AI as a collaborator.

### Part 1: Create Your Templates

**For each template you designed**:

1. **Test it with AI**
   - Fill in a real example
   - Paste into Claude Code or Gemini CLI
   - Evaluate the output

2. **Refine based on results**
   - What worked well?
   - What was missing?
   - Update the template

3. **Document the final version**
   - Include usage notes
   - Add the tested example
   - Note what output to expect

---

### Part 2: Validate Your Decision Guide

**Test your decision guide**:

1. **Pick a task you need to do**
   - Consult your decision guide
   - Which template does it recommend?

2. **Use the recommended template**
   - Fill it in
   - Test with AI
   - Evaluate if the recommendation was correct

3. **Refine the guide if needed**
   - Did the guide point you to the right template?
   - Are there tasks missing from the guide?
   - Are the criteria clear enough?

---

### Part 3: Peer Review (Optional but Recommended)

**Share your toolkit with a peer**:

1. **Give them a task**
   - Ask them to use your toolkit for a real task
   - Don't explain anything—let the toolkit speak for itself

2. **Observe**
   - Did they find the right template?
   - Did they understand the placeholders?
   - Did they get good results?

3. **Incorporate feedback**
   - What confused them?
   - What worked well?
   - Refine based on their experience

---

### Part 4: Real-World Usage

**Use your toolkit for one week**:

1. **Track usage**
   - Which templates did you use most?
   - Which templates did you never use?
   - What tasks came up that you didn't have templates for?

2. **Version 1.1 Updates**
   - Remove templates you don't use
   - Add templates for recurring tasks you discovered
   - Refine templates based on real usage

3. **Iteration**
   - Update your toolkit monthly
   - Add new templates as patterns emerge
   - Remove templates that don't provide value

---

**Final Reflection**:
- How much time did your templates save compared to writing prompts from scratch?
- Which template surprised you by being more useful than expected?
- Which template needed the most refinement before it worked well?
- What would you tell someone starting to build their own toolkit?
- How will you maintain and evolve this toolkit over time?

---

## Next Steps: Beyond This Chapter

You've built foundational skills in prompt engineering—how to communicate clearly with AI, iterate through collaboration, and create reusable patterns.

**Chapter 11** will teach **context engineering**—how to give AI the background knowledge it needs for complex tasks. You'll learn about context windows, memory files, and session management.

**Part 4** will introduce Python programming, where you'll apply these prompting skills to learning a new language with AI as your teacher.

Your toolkit will grow as you tackle new domains, but the patterns you've learned here—clear structure, iteration, validation, and reusability—apply universally.

**Congratulations on completing Chapter 10!** You now have a personal prompt toolkit and the skills to continue refining it as your work evolves.
