---
sidebar_position: 0
title: "Build Your Kafka Skill"
description: "Create your Kafka event schema skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 52
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a Kafka skill"

learning_objectives:
  - objective: "Build a Kafka event schema skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working kafka-events skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to Kafka domain"
---

# Build Your Kafka Skill

You're about to learn Kafka—building event-driven architectures for your AI agents. But you won't start with "what is a topic?"

You'll start by **building a skill that knows Kafka**.

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
I'm learning Apache Kafka to build event-driven AI agent architectures.

Before I learn the details, help me BUILD a skill that can:
1. Design Kafka topic structures for AI agent events
2. Generate producer code with proper serialization
3. Create consumer code with consumer groups
4. Define Avro/JSON schemas for events
5. Implement error handling and retry patterns

Let's do this in two steps:
1. First, use /fetching-library-docs to get official Kafka documentation
2. Then, use /skill-creator to build a skill called "kafka-events"
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs kafka
```

---

## Step 4: Create the Skill

```
/skill-creator
```

You'll see `.claude/skills/kafka-events/SKILL.md` created:

```markdown
---
name: kafka-events
description: Design Kafka event architectures with proper topics, schemas, producers, and consumers for AI agents
allowed-tools: Read, Write, Bash, Glob, Grep
---

## Persona
You are an event-driven architecture expert specializing in Kafka...

## Principles
1. Design events as immutable facts, not commands
2. Use schema registry for event versioning
3. Partition by entity ID for ordering guarantees
4. Handle poison pills with dead letter topics
...
```

---

## Step 5: Test Your Skill

```
Using my kafka-events skill, design an event architecture for:
- Task created, updated, completed events
- Notification triggers based on task state changes
- Consumer group for processing reminders

Just design it—I want to see what my skill produces.
```

---

## What Happens Next

| Lesson | You Learn | Your Skill Improves |
|--------|-----------|---------------------|
| L00 (this) | Build skill first | Initial version from docs |
| L01-03 | Event concepts, Kafka basics | Understand event patterns |
| L04-08 | Producers, consumers | Refine: better code generation |
| L09-15 | Schemas, reliability | Add: production patterns |
| L16-22 | Agent patterns + Capstone | **Production-ready skill** |

---

## Your Growing Skills Library

```
.claude/skills/
├── skill-creator/
├── fetching-library-docs/
├── fastapi-agent-api/       # Chapter 40
├── docker-deployment/       # Chapter 49
├── kubernetes-deployment/   # Chapter 50
├── helm-chart/              # Chapter 51
└── kafka-events/            # NEW - this chapter
```

---

**Next: Lesson 1 — From Request-Response to Events**
