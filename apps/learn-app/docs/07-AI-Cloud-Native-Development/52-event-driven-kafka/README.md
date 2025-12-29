---
sidebar_position: 52
title: "Chapter 52: Event-Driven Architecture with Kafka"
description: "Build your Kafka skill first, then learn to understand and refine it into a production-ready asset"
---

# Chapter 52: Event-Driven Architecture with Kafka

**You will build a Kafka skill BEFORE you learn Kafka.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `kafka-events` skill using tools from Chapter 5. Then you spend the chapter understanding what you built and making it better. By the end, you don't just "know Kafka"—you OWN a production-ready skill.

## The Skill-First Arc

```
L00: Build Your Kafka Skill (25 min)
  │   └── Clone skills-lab, fetch docs, create skill
  │
  ├── L01-03: EDA Foundations
  │   └── Events vs requests, EDA concepts, Kafka mental model
  │
  ├── L04-08: Kafka Core
  │   └── Strimzi deployment, producers, consumers
  │
  ├── L09-13: Production Patterns
  │   └── FastAPI integration, schemas, delivery, transactions
  │
  ├── L14-17: Advanced Patterns
  │   └── Connect, CDC, agent patterns, saga
  │
  └── L18-22: Operations & Capstone
      └── Production Strimzi, monitoring, AI-assisted, capstone, skill
```

**Key Update (2025):** Kafka 4.0 removed ZooKeeper entirely. This chapter teaches KRaft-only deployment—the modern, simplified architecture.

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Kafka Skill** | **Created from official docs** |
| 1 | From Request-Response to Events | Understand: why events |
| 2 | EDA Concepts | Understand: event patterns |
| 3 | Kafka Mental Model | Understand: topics, partitions |
| 4 | Deploying Kafka with Strimzi | Validate: skill knows Strimzi |
| 5 | Your First Producer | Refine: producer code |
| 6 | Producer Reliability | Add: acks, retries |
| 7 | Your First Consumer | Refine: consumer code |
| 8 | Consumer Groups & Rebalancing | Add: group patterns |
| 9 | Async FastAPI Integration | Add: async patterns |
| 10 | Avro & Schema Registry | Add: schema patterns |
| 11 | Delivery Semantics | Add: guarantees |
| 12 | Transactions | Add: transaction patterns |
| 13 | Reliability Configuration | Add: production config |
| 14 | Kafka Connect | Add: connector patterns |
| 15 | CDC with Debezium | Add: CDC patterns |
| 16 | Agent Event Patterns | Add: agent events |
| 17 | Saga Pattern | Add: saga patterns |
| 18 | Production Strimzi | Refine: production config |
| 19 | Monitoring & Debugging | Add: observability |
| 20 | AI-Assisted Development | Refine: AI collaboration |
| **21** | **Capstone: Event-Driven Notifications** | **Production-ready** |
| 22 | Finalize Kafka Skill | **Complete asset** |

## Every Lesson Has Skill Reflection

Each lesson ends with **"Reflect on Your Skill"**:

1. **Test**: Does your skill handle this lesson's concepts?
2. **Identify gaps**: What's missing?
3. **Improve**: Add or refine the capability

By Lesson 22, you've tested and improved your skill 21+ times.

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Explain why events beat direct calls**: Coupling problems, async benefits, when to use EDA
- **Understand Kafka architecture**: Brokers, topics, partitions, consumer groups, offsets (KRaft mode)
- **Implement reliable producers**: acks semantics, retries, idempotent producer, error handling
- **Implement robust consumers**: Consumer groups, rebalancing, offset management, lag monitoring
- **Integrate with FastAPI**: Async producers/consumers, lifespan events, background tasks
- **Design event schemas**: Avro with Schema Registry, schema evolution, breaking change prevention
- **Apply delivery guarantees**: At-least-once, at-most-once, exactly-once semantics and trade-offs
- **Use transactions**: Consume-process-produce pattern, zombie fencing, read_committed isolation
- **Build data pipelines**: Kafka Connect, Debezium CDC, outbox pattern for microservices
- **Implement agent patterns**: Task events, notification fanout, audit logs, saga pattern
- **Run Kafka on Kubernetes**: Strimzi operator, Kafka CRDs, KRaft mode, production configuration
- **Debug production issues**: Consumer lag, under-replicated partitions, rebalancing storms

## Chapter Structure

### Part A: EDA Foundations (Lessons 1-3)

| # | Lesson | Focus |
|---|--------|-------|
| 1 | From Request-Response to Events | Why direct API calls fail at scale, coupling problems, async benefits |
| 2 | Event-Driven Architecture Concepts | Events vs commands, event sourcing intro, CQRS overview, when to use EDA |
| 3 | How Kafka Fits: The Mental Model | Topics, partitions, producers, consumers, brokers, offsets — visual + analogies |

### Part B: Kafka Core (Lessons 4-8)

| # | Lesson | Focus |
|---|--------|-------|
| 4 | Deploying Kafka with Strimzi | Strimzi operator Helm install, Kafka CRD, KRaft mode, Kafka UI |
| 5 | Your First Producer (Python) | confluent-kafka-python, sync send, fire-and-forget vs sync vs async |
| 6 | Producer Deep Dive: Reliability | acks (0, 1, all), retries, delivery.timeout.ms, idempotent producer |
| 7 | Your First Consumer (Python) | Consumer groups, poll loop, auto-commit vs manual, offset management |
| 8 | Consumer Deep Dive: Groups & Rebalancing | Partition assignment, rebalance listeners, static membership, consumer lag |

### Part C: Production Patterns (Lessons 9-13)

| # | Lesson | Focus |
|---|--------|-------|
| 9 | Async Producers & Consumers in FastAPI | AIOProducer, async consumer patterns, lifespan events, background tasks |
| 10 | Message Schemas: Avro & Schema Registry | Why schemas, Avro basics, Schema Registry, evolution strategies |
| 11 | Delivery Semantics Deep Dive | At-most-once, at-least-once, exactly-once trade-offs, idempotent producer limits |
| 12 | Transactions for Stream Processing | Consume-process-produce, transactional.id, zombie fencing, read_committed |
| 13 | Reliability Configuration | Replication factor, min.insync.replicas, unclean leader election, ISR |

### Part D: Data Pipelines (Lessons 14-15)

| # | Lesson | Focus |
|---|--------|-------|
| 14 | Kafka Connect: Building Data Pipelines | Source vs sink connectors, REST API, when to use Connect vs client |
| 15 | Change Data Capture with Debezium | CDC vs polling, Debezium for Postgres, outbox pattern for atomicity |

### Part E: Agent Communication Patterns (Lessons 16-17)

| # | Lesson | Focus |
|---|--------|-------|
| 16 | Agent Event Patterns | Task lifecycle events, notification fanout, immutable audit log, naming conventions |
| 17 | Saga Pattern for Multi-Step Workflows | Choreography vs orchestration, compensation events, implementing saga |

### Part F: Deployment & Operations (Lessons 18-19)

| # | Lesson | Focus |
|---|--------|-------|
| 18 | Production Kafka with Strimzi | Multi-broker Kafka CRD, resource limits, persistence, Strimzi Entity Operator |
| 19 | Monitoring & Debugging Kafka | Consumer lag, under-replicated partitions, key metrics, tooling |

### Part G: AI Collaboration & Capstone (Lessons 20-22)

| # | Lesson | Focus |
|---|--------|-------|
| 20 | AI-Assisted Kafka Development | Use Claude to debug consumer lag, generate Avro schemas, optimize configs |
| 21 | Capstone: Event-Driven Agent Notifications | Spec-driven: add Kafka events to Part 6 agent (task.created, audit log) |
| 22 | Building the Kafka Event Schema Skill | Reusable skill for designing event schemas and topic structures |

## Prerequisites

- **Chapter 49**: Docker fundamentals (containers, images, volumes)
- **Chapter 50**: Kubernetes basics (Pods, Deployments, Services)
- **Chapter 51**: Helm Charts (for Kafka deployment)
- **Part 6**: Your FastAPI agent service (Task API)
- **Python**: Async patterns (async/await, asyncio)

## Technology Choices

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Kafka Operator** | Strimzi | CNCF project, industry standard for Kafka on K8s |
| **Kafka Mode** | KRaft (no ZooKeeper) | Kafka 4.0+ default, simpler architecture |
| **Python Client** | confluent-kafka-python | Best performance, native async, Schema Registry support |
| **Schemas** | Avro + Confluent Schema Registry | Industry standard, evolution support |
| **Platform** | Docker Desktop Kubernetes | Consistent with Chapters 49-51 |
| **CDC** | Debezium | Best-in-class change data capture |

## What's NOT Covered

This chapter focuses on **developer skills**, not SRE operations:

- Docker Compose — we use Kubernetes throughout Part 7
- Multi-datacenter replication (MirrorMaker 2)
- Security deep dive (SASL, SSL, ACLs) — covered at overview level only
- Kafka Streams framework — separate advanced topic
- Broker hardware sizing and tuning
- ZooKeeper — removed in Kafka 4.0

## Looking Ahead

This chapter teaches Kafka directly. Chapter 53 (Dapr) shows how to abstract pub/sub behind Dapr's API, making your code portable across message brokers while retaining the concepts you learned here.
