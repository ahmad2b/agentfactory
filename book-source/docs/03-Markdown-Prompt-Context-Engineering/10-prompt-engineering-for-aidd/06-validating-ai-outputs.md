---
title: "Lesson 6: Validating AI Outputs"
sidebar_label: "Validating AI Outputs"
sidebar_position: 6
description: "Learn to systematically validate AI-generated code and solutions before using them"
---

# Lesson 6: Validating AI Outputs

AI is powerful, but it's not perfect. It makes mistakes. It hallucinates commands that don't exist. It generates code with security issues. It confidently gives you wrong answers.

The solution isn't to stop using AI—it's to validate everything AI produces before you use it. This lesson teaches you a systematic validation checklist and how to spot common red flags in AI-generated code.

**Core principle**: Never trust AI blindly. Always validate.

## Why Validation Matters

Here's what can go wrong if you don't validate:

**Example 1: Security Issues**
AI generates a bash script with hardcoded passwords:
```bash
#!/bin/bash
curl -u admin:password123 https://api.example.com/backup
```

If you run this without review, you've just embedded credentials in your script—a major security risk.

---

**Example 2: Wrong Commands**
AI suggests a command that doesn't exist:
```bash
git undo-commit  # This is not a real git command
```

If you copy-paste without checking, you'll get an error and waste time debugging.

---

**Example 3: Dangerous Operations**
AI generates a script without safety checks:
```bash
#!/bin/bash
rm -rf $BACKUP_DIR/*  # If $BACKUP_DIR is empty, this becomes rm -rf /*
```

If you run this without validation, you could delete critical files.

These aren't hypothetical—they're real examples of AI mistakes. Validation catches them before they cause problems.

## The Validation Checklist

For every AI-generated solution, follow this four-step process:

### 1. Read — Understand What AI Gave You

Don't skip to copy-paste. Read the entire output.

**Ask yourself**:
- What does this code DO?
- What are the inputs and outputs?
- Are there any side effects (file operations, network calls, deletions)?

**Red flag**: If you can't explain what the code does, don't run it.

---

### 2. Understand — Check for Red Flags

Look for common problem patterns:

**Red Flag 1: Hardcoded Values**
```bash
# RED FLAG: Hardcoded path
cp ~/Documents/report.txt /backup/report.txt

# BETTER: Use variables
SOURCE=~/Documents/report.txt
DEST=/backup/report.txt
cp "$SOURCE" "$DEST"
```

**Red Flag 2: Missing Error Handling**
```bash
# RED FLAG: No error checking
mkdir /backup
cp important-file.txt /backup/

# BETTER: Check if commands succeed
if mkdir /backup; then
    cp important-file.txt /backup/
else
    echo "Error: Could not create backup directory"
    exit 1
fi
```

**Red Flag 3: Overly Complex Solutions**
If AI generates 50 lines of code for something that should take 5, it's probably overengineering.

**Red Flag 4: Unexplained "Magic"**
AI uses commands or flags you don't recognize without explaining them.
```bash
# RED FLAG: What does -aq do?
git stash -aq
```

**Red Flag 5: Security Issues**
- Hardcoded passwords or API keys
- Scripts that run with sudo unnecessarily
- Commands that delete or modify files without confirmation

---

### 3. Test — Try It in a Safe Environment

Never run AI-generated code on production data or systems first.

**Safe testing approaches**:

**Option 1: Test with sample data**
```bash
# Create test files first
mkdir ~/test-backup
touch ~/test-backup/test-file.txt

# Test the script on test directory
./backup-script.sh ~/test-backup
```

**Option 2: Use dry-run mode**
Many commands have a dry-run option that shows what would happen without actually doing it:
```bash
# Test what would be deleted without deleting
find . -name "*.log" -print  # Just shows files
# find . -name "*.log" -delete  # Actually deletes (do this after testing)
```

**Option 3: Test in a separate directory**
```bash
# Create test environment
mkdir ~/ai-test
cd ~/ai-test
# Test script here, not in your actual projects
```

---

### 4. Question — Ask AI to Explain Anything Unfamiliar

If you see something you don't understand, ask AI to explain it.

**Example**: AI generates this script:
```bash
#!/bin/bash
find ~ -type f -mtime +30 -name "*.log" -exec rm {} \;
```

**You don't recognize**: `-exec rm {} \;`

**Your question to AI**:
"Explain what `-exec rm {} \;` does in this find command, and why the backslash-semicolon is needed."

**AI explains**:
"`-exec rm {} \;` executes the `rm` command on each file found. The `{}` is a placeholder for the filename, and `\;` marks the end of the exec command (the backslash escapes the semicolon for the shell)."

**Now you understand**: The command finds .log files older than 30 days and deletes each one.

**Follow-up validation**: Ask AI for a safer alternative:
"Is there a safer way to do this, like showing me the files before deleting them?"

**AI provides**:
```bash
# Show files first
find ~ -type f -mtime +30 -name "*.log"

# Review the list, then delete if it looks right
find ~ -type f -mtime +30 -name "*.log" -delete
```

## Common AI Mistakes and How to Catch Them

### Mistake 1: Platform-Specific Code

**AI's output**:
```bash
#!/bin/bash
apt-get install git  # Linux package manager
```

**Problem**: You're on macOS, which doesn't have `apt-get`.

**How to catch**: Read the code. If you see unfamiliar commands, ask AI: "Is this command available on macOS?"

**Validation prompt**: "Rewrite this for macOS using Homebrew."

---

### Mistake 2: Assuming Directory Structures

**AI's output**:
```bash
#!/bin/bash
cp ~/Documents/report.txt /var/backups/
```

**Problem**: AI assumes `/var/backups/` exists and you have write access.

**How to catch**: Look for absolute paths. Ask yourself: "Does this directory exist on MY system?"

**Validation prompt**: "Add error handling to check if the destination directory exists before copying."

---

### Mistake 3: Missing Edge Cases

**AI's output**:
```bash
#!/bin/bash
filename="$1"
cat "$filename"
```

**Problem**: What if the user doesn't provide an argument? The script will fail.

**How to catch**: Think about edge cases. What if the input is empty, invalid, or unexpected?

**Validation prompt**: "Add a check to ensure the user provides a filename argument."

---

### Mistake 4: Inefficient Solutions

**AI's output**: A script that loops through files one at a time when a single command would work.

**How to catch**: If the solution feels overly complicated, ask AI: "Is there a simpler way to do this?"

## Practice: Validate AI-Generated Code

Here are three AI-generated scripts. Identify the red flags in each one WITHOUT using AI.

### Script 1: Backup Script

```bash
#!/bin/bash
cp -r ~/Documents /backup/
echo "Backup complete"
```

**Red flags you found**:
1.
2.
3.

**What questions would you ask AI to improve this?**

---

### Script 2: Log Cleanup

```bash
#!/bin/bash
rm -rf /var/log/*.log
echo "Logs cleaned"
```

**Red flags you found**:
1.
2.
3.

**What questions would you ask AI to improve this?**

---

### Script 3: Git Commit Helper

```bash
#!/bin/bash
git add .
git commit -m "updates"
git push origin main
```

**Red flags you found**:
1.
2.
3.

**What questions would you ask AI to improve this?**

---

**After you've identified red flags**, review your answers:
- Did you check for hardcoded values?
- Did you check for missing error handling?
- Did you check for security issues?
- Did you think about what could go wrong?

## Try With AI

Now test your validation skills with real AI-generated code. Use Claude Code or Gemini CLI:

### Exercise 1: Generate and Validate a Backup Script

**Step 1: Get AI to generate code**
"Create a bash script to backup my Downloads folder to an external drive at /Volumes/Backup."

**Step 2: Validate the output**
Apply the 4-step checklist:
1. **Read**: What does this script do step-by-step?
2. **Understand**: What red flags do you see?
3. **Test**: How would you test this safely?
4. **Question**: What parts don't you understand?

**Step 3: Ask AI to fix issues**
"I see these problems in your script: [list the red flags]. Fix them and add error handling."

**Step 4: Validate the improved version**
Run through the checklist again. Is it better?

---

### Exercise 2: Validate a Find Command

**Step 1: Get AI to generate a command**
"Create a find command to delete all .tmp files in my home directory older than 7 days."

**Step 2: Before running it, ask AI to explain**
"Explain exactly what this command will do, step by step."

**Step 3: Ask for a safer version**
"Show me how to test this command without actually deleting files first."

**Step 4: Test the safe version, then run the real command**
Compare what the test shows vs. what you expected.

---

### Exercise 3: Challenge AI's Solution

**Step 1: Ask AI for help with a complex task**
"Create a bash script to organize my Downloads folder by file type, moving .pdf files to a Documents/PDFs folder, .jpg files to Pictures/Downloads, and everything else to a Misc folder."

**Step 2: Deliberately look for problems**
- Are there hardcoded paths?
- What if the destination folders don't exist?
- What if files with the same name already exist?
- What if you run this on an empty folder?

**Step 3: Ask AI to address each issue**
"What happens if the Documents/PDFs folder doesn't exist? Add error handling for that."

**Step 4: Iterate until you trust the script**
Keep asking questions until all edge cases are handled.

---

**Reflection questions**:
- How many red flags did you find in AI's first output?
- Did AI explain unfamiliar parts clearly when you asked?
- What would have happened if you'd run the code without validation?
- When did you realize AI made an assumption about your environment?
- How many iterations did it take before you trusted the code?
