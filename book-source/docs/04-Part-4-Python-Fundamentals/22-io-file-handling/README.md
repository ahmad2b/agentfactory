# Chapter 22: IO and File Handling

## Overview

Welcome to Chapter 22, where you'll master input/output operations—the foundation of every useful program. You'll learn how programs interact with users through the console, persist data to files for long-term storage, organize file systems using cross-platform paths, and work with structured data formats like CSV and JSON. By the end, you'll build a complete Note-Taking CLI application that integrates all these concepts.

This chapter applies the **AI-Native Learning methodology** you've practiced since Chapter 1: you describe what you want your code to do, explore concepts with your AI companion, validate your understanding through interactive programs, and learn from errors by asking "why?" This is the same pattern you'll use throughout your professional career.

## What You'll Learn

By the end of this chapter, you will be able to:

1. **Gather and validate console input** with proper error handling and formatted output (Lesson 1)
2. **Read and write files safely** using context managers and exception handling (Lesson 2)
3. **Work with file paths** across Windows, Mac, and Linux using pathlib (Lesson 3)
4. **Load and save structured data** in CSV and JSON formats with correct encoding (Lesson 4)
5. **Build a complete CLI application** integrating all I/O concepts (Lesson 5 - Capstone)

## Estimated Time

Total estimated time for this chapter: **5-6 hours** (including capstone project)

- **Lesson 1**: Console I/O and User Input Validation — 75 minutes
- **Lesson 2**: File I/O Fundamentals with Context Managers — 90 minutes
- **Lesson 3**: Cross-Platform Path Handling with pathlib — 75 minutes
- **Lesson 4**: Structured Data Formats (CSV and JSON) — 90 minutes
- **Lesson 5**: Capstone - Note-Taking App — 90-120 minutes

## Prerequisites

You should have already completed:

- **Chapters 1-12**: AI-Driven Development foundations, Python setup, basic terminal
- **Chapter 13**: Python basics (variables, print, basic I/O)
- **Chapter 14**: Data types (strings, lists, dicts)
- **Chapter 15**: Operators and type conversion
- **Chapter 16**: Strings and type casting (f-strings)
- **Chapter 17**: Control flow and loops (for menu loops, iterating files)
- **Chapter 18**: Lists, tuples, dictionaries (in-memory data structures)
- **Chapter 19**: Sets and collections (understanding container types)
- **Chapter 20**: Modules and functions (importing csv, json, pathlib; function organization)
- **Chapter 21**: Exception handling (try/except for FileNotFoundError, JSONDecodeError, IOError)

No prior file handling experience required—we start from zero.

## Tools You'll Need

- **Python 3.14+** (installed in Chapter 12)
- **Text editor or IDE** (VS Code, Cursor, or similar)
- **Terminal/command line** (Windows PowerShell, Mac Terminal, or Linux Terminal)
- **Your AI tool** (Claude Code or Gemini CLI for exploring and validating)

## Key Themes Throughout This Chapter

### Theme 1: "Persistence Matters"

Console programs are temporary—data disappears when the program ends. Files provide **persistence**: data survives between program runs. This is what makes software useful in the real world.

### Theme 2: "Safety First"

File operations can fail (missing files, permission errors, disk full). We teach **defensive programming**: always use context managers (`with` statements), always handle exceptions, always validate paths before operations.

### Theme 3: "Cross-Platform by Default"

Your code must work on Windows, Mac, AND Linux without changes. We use **pathlib** exclusively (not `os.path`) because it handles platform differences automatically. This is the modern Python standard.

### Theme 4: "Structured Data = Real-World Integration"

CSV and JSON aren't just file formats—they're **integration points** with the rest of the software world. CSV connects to Excel and databases; JSON connects to web APIs and configuration systems.

### Theme 5: "Build Real Applications"

Every concept builds toward the **Capstone Project** (Lesson 5): a complete Note-Taking App with Create/Read/Update/Delete/Search operations. This isn't a toy—it's a real CLI application you could extend and use professionally.

## Lesson Structure

Each lesson follows the same pattern:

1. **Core Content**: Clear explanations with real-world context
2. **Code Examples**: Tested, commented, production-quality Python 3.14+
3. **CoLearning Elements** (💬🎓🚀✨): Prompts and activities with AI distributed throughout
4. **Practice Exercises**: Hands-on coding with acceptance criteria
5. **"Try With AI"**: 4 progressive prompts (Remember → Understand → Apply → Analyze)

**Important**: Every lesson ends with "Try With AI"—no additional summary or checklist. That section is your cognitive closure for the lesson.

## The Capstone Project (Lesson 5)

At the end of Chapter 22, you'll build a **Note-Taking App (CLI)**—an interactive application that:

- Displays a menu with 7 options (Create/Read/Update/Delete/Search/List/Exit)
- Accepts user input with validation and error recovery
- Saves notes as JSON files in organized directory structure (notes/[category]/[id].json)
- Supports search by keyword across all notes
- Handles 10-50 notes comfortably (dozens, proof-of-concept scale)
- Demonstrates path security (prevents `../../../etc/passwd` attacks)
- Integrates ALL concepts from Lessons 1-4

This is a **specification-first project**: you design before you code, then implement incrementally with your AI companion.

## How to Use This Chapter

**Read in order**: Lessons 1-5 build on each other. Don't skip ahead.

**Do every "Try With AI" prompt**: These aren't optional extras—they're where the real learning happens. Take time with each prompt, think through your answers, and engage authentically with your AI partner.

**Test all code examples**: Run every code example yourself. Don't just read it. See it work (or fail) on your computer. That hands-on experience matters.

**Build the capstone thoughtfully**: The capstone is your chance to apply everything. Don't rush. Design first, code second. Validate that your program does what you intended.

## Connection to Your Learning Journey

### From Chapter 21 → Chapter 22

Chapter 21 taught exception handling fundamentals (try/except/finally, raising exceptions, custom exceptions). Chapter 22 applies those patterns to file operations, where errors are common and must be handled gracefully.

### From Chapter 22 → Chapter 23

Chapter 22 completes Python's core I/O capabilities (console, file operations, structured formats). Chapter 23 (Math, DateTime, Calendar) builds on file-based workflows—you'll timestamp files, store configuration with dates, and work with time-sensitive data.

### Preparing for Part 5 (Spec-Driven Development)

Part 5 introduces **Specification-Driven Development (SDD)**—the professional practice of writing detailed specifications before coding. In this chapter, we preview that with **structured data formats** and **application architecture**. When you reach Part 5, SDD will feel natural because you've been practicing specification-first thinking with the capstone project.

## A Note on AI Collaboration

This chapter assumes you have access to Claude Code or Gemini CLI (or a similar AI tool). Every "Try With AI" section references your AI companion. If you don't have access yet, revisit Chapters 5-6 to set up your tool before proceeding.

Your AI tool isn't a crutch—it's a partner in learning. Use it to:
- Clarify concepts
- Validate your code
- Understand error messages
- Review your work
- Explore extensions
- Reflect on your learning

Professional developers use AI daily. Learning to use it effectively is a core skill this chapter teaches.

---

## Lessons

1. **[Lesson 1: Console I/O and User Input Validation](./01-lesson-1.md)** (75 min)
   - Using input() for user interaction
   - Type conversion and validation
   - F-string formatting for professional output
   - Error recovery loops

2. **[Lesson 2: File I/O Fundamentals with Context Managers](./02-lesson-2.md)** (90 min)
   - Safe file reading with context managers
   - File modes (r/w/a/r+)
   - Reading methods (read/readline/readlines)
   - Writing files with proper formatting
   - Exception handling (FileNotFoundError, PermissionError)

3. **[Lesson 3: Cross-Platform Path Handling with pathlib](./03-lesson-3.md)** (75 min)
   - Creating Path objects
   - Checking file and directory existence
   - Creating nested directories
   - Listing and globbing files
   - Path security (preventing traversal attacks)

4. **[Lesson 4: Structured Data Formats (CSV and JSON)](./04-lesson-4.md)** (90 min)
   - Reading and writing CSV files
   - Loading and saving JSON data
   - Character encoding (UTF-8)
   - Format-specific error handling
   - Choosing between CSV and JSON

5. **[Lesson 5: Capstone - Note-Taking App](./05-lesson-5.md)** (90-120 min)
   - Integrating all I/O concepts
   - Implementing CRUD operations
   - Menu-driven interactive loops
   - Search and filter operations
   - Application-level error handling
   - Data validation at scale
   - Code organization for maintainability

---

## Ready to Begin?

Start with **[Lesson 1: Console I/O and User Input Validation](./01-lesson-1.md)**. Take your time, engage with your AI partner, and enjoy building your foundation in file handling and I/O operations.

Let's build something real! 🚀

---

**Chapter Information**:
- **Part**: 4 (Python Fundamentals)
- **Number**: 22
- **Complexity Tier**: Intermediate (A2-B1, with B1 capstone)
- **Learning Pattern**: AI-Native Learning
- **Key Skill Focus**: File I/O safety, cross-platform paths, structured data, application integration
- **Capstone Project**: Note-Taking App (CLI) with CRUD operations and JSON persistence
