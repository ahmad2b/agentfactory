---
sidebar_position: 0
title: "Build Your Docker Skill"
description: "Create your Docker deployment skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 49
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a Docker skill"

learning_objectives:
  - objective: "Build a Docker deployment skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working docker-deployment skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to Docker domain"

differentiation:
  extension_for_advanced: "Add multi-stage build patterns to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes later"
---

# Build Your Docker Skill

You're about to learn Docker—containerizing your Task API for production deployment. But you won't start with "what is a container?"

You'll start by **building a skill that knows Docker**.

In Chapter 5, you learned `skill-creator` and `fetching-library-docs`. Now you'll apply them to create a `docker-deployment` skill. The official Docker documentation will teach your skill. Then THIS chapter teaches YOU.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git
cd claude-code-skills-lab
```

Or pull latest:

```bash
cd claude-code-skills-lab
git pull
```

Open Claude Code:

```bash
claude
```

---

## Step 2: Write Your Learning Spec

```
I'm learning Docker to containerize Python/FastAPI applications for production.

Before I learn the details, help me BUILD a skill that can:
1. Generate Dockerfiles for Python applications using UV package manager
2. Create multi-stage builds for smaller production images
3. Add proper .dockerignore files
4. Configure health checks and environment variables
5. Follow security best practices (non-root users, minimal images)

Let's do this in two steps:
1. First, use /fetching-library-docs to get official Docker documentation
2. Then, use /skill-creator to build a skill called "docker-deployment"
```

---

## Step 3: Fetch Official Documentation

Claude runs:

```
/fetching-library-docs docker
```

This fetches Docker best practices via Context7—official, accurate knowledge.

---

## Step 4: Create the Skill

Claude runs:

```
/skill-creator
```

You'll see `.claude/skills/docker-deployment/SKILL.md` created:

```markdown
---
name: docker-deployment
description: Generate production Dockerfiles for Python/FastAPI apps with UV, multi-stage builds, and security best practices
allowed-tools: Read, Write, Bash, Glob, Grep
---

## Persona
You are a DevOps engineer specializing in container optimization...

## Principles
1. Always use multi-stage builds to minimize image size
2. Install dependencies before copying application code (layer caching)
3. Run as non-root user in production
4. Use specific image tags, never :latest in production
...
```

**You own a Docker skill—before learning Docker.**

---

## Step 5: Test Your Skill

```
Using my docker-deployment skill, generate a Dockerfile for:
- A FastAPI application using UV package manager
- Python 3.12 base image
- Production-ready with multi-stage build

Just generate it—I want to see what my skill produces.
```

---

## What Happens Next

| Lesson | You Learn | Your Skill Improves |
|--------|-----------|---------------------|
| L00 (this) | Build skill first | Initial version from docs |
| L01 Installation | Docker Desktop basics | Validate: works on your system |
| L02 Fundamentals | Container concepts | Understand what skill generates |
| L03 Dockerfile | Writing Dockerfiles | Refine: better structure |
| L04 Lifecycle | Container management | Add: debugging patterns |
| L05 Multi-stage | Optimization | Refine: smaller images |
| L06 Production | Hardening | Add: security patterns |
| L07 Skill Building | Finalize skill | **Production-ready** |
| L08 Capstone | Deploy Task API | Test skill end-to-end |

---

## Your Growing Skills Library

```
.claude/skills/
├── skill-creator/           # From Chapter 5
├── fetching-library-docs/   # From Chapter 5
├── fastapi-agent-api/       # From Chapter 40
└── docker-deployment/       # NEW - this chapter
```

---

## Verify Before Proceeding

```
Show me my docker-deployment skill.
What can it do? What might be missing?
```

**Next: Lesson 1 — Docker Installation and Setup**
