---
sidebar_position: 0
title: "Build Your Kubernetes Skill"
description: "Create your Kubernetes deployment skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 50
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a Kubernetes skill"

learning_objectives:
  - objective: "Build a Kubernetes deployment skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working kubernetes-deployment skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to Kubernetes domain"
---

# Build Your Kubernetes Skill

You're about to learn Kubernetes—orchestrating your containerized Task API at scale. But you won't start with "what is a Pod?"

You'll start by **building a skill that knows Kubernetes**.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git
cd claude-code-skills-lab
claude
```

---

## Step 2: Write Your Learning Spec

```
I'm learning Kubernetes to deploy and scale containerized AI agents.

Before I learn the details, help me BUILD a skill that can:
1. Generate Kubernetes Deployments with proper resource limits
2. Create Services for internal and external access
3. Configure ConfigMaps and Secrets for configuration
4. Set up health checks (liveness/readiness probes)
5. Implement Horizontal Pod Autoscaler for auto-scaling

Let's do this in two steps:
1. First, use /fetching-library-docs to get official Kubernetes documentation
2. Then, use /skill-creator to build a skill called "kubernetes-deployment"
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs kubernetes
```

---

## Step 4: Create the Skill

```
/skill-creator
```

You'll see `.claude/skills/kubernetes-deployment/SKILL.md` created:

```markdown
---
name: kubernetes-deployment
description: Generate Kubernetes manifests for deploying AI agents with proper resources, health checks, and scaling
allowed-tools: Read, Write, Bash, Glob, Grep
---

## Persona
You are a Kubernetes platform engineer...

## Principles
1. Always set resource requests AND limits
2. Include liveness and readiness probes
3. Use ConfigMaps for config, Secrets for sensitive data
4. Label everything consistently for selection
...
```

---

## Step 5: Test Your Skill

```
Using my kubernetes-deployment skill, generate manifests for:
- A Deployment for task-api with 2 replicas
- A Service exposing port 8000
- A ConfigMap for environment settings

Just generate them—I want to see what my skill produces.
```

---

## What Happens Next

| Lesson | You Learn | Your Skill Improves |
|--------|-----------|---------------------|
| L00 (this) | Build skill first | Initial version from docs |
| L01 Architecture | K8s concepts | Understand what skill generates |
| L02 Docker Desktop | Local cluster | Validate: skill works locally |
| L03-05 | Core objects | Refine: better manifests |
| L06-09 | Production patterns | Add: scaling, RBAC, health |
| L10-14 | Advanced + Capstone | **Production-ready skill** |

---

## Your Growing Skills Library

```
.claude/skills/
├── skill-creator/
├── fetching-library-docs/
├── fastapi-agent-api/       # Chapter 40
├── docker-deployment/       # Chapter 49
└── kubernetes-deployment/   # NEW - this chapter
```

---

**Next: Lesson 1 — Kubernetes Architecture**
