---
sidebar_position: 52
title: "Chapter 52: Event-Driven Architecture with Kafka"
description: "Build your Kafka skill first, then learn to understand and refine it into a production-ready asset"
---

# Chapter 52: Event-Driven Architecture with Kafka

You build the `kafka-events` skill first, then use each lesson to test and deepen it—from EDA fundamentals to production-grade operations. Kafka 4.0+ KRaft mode (no ZooKeeper) is the default.

---

## Goals

- Understand event-driven architecture and Kafka’s core model (topics, partitions, consumer groups)
- Deploy Kafka with Strimzi in KRaft mode
- Build reliable producers/consumers with delivery guarantees and transactions
- Integrate Kafka with FastAPI using schemas (Avro + schema registry)
- Apply advanced patterns: Connect, CDC with Debezium, agent events, saga
- Operate Kafka: production config, monitoring, debugging
- Capture everything in a reusable Kafka skill

---

## Lesson Progression

| # | Lesson | Focus |
|---|--------|-------|
| **0** | Build Your Kafka Skill | Scaffold from docs |
| 1-3 | EDA Foundations | Why events, EDA patterns, Kafka mental model |
| 4-8 | Kafka Core | Strimzi deploy, producers, consumers, groups |
| 9-13 | Production Patterns | Async FastAPI integration, schemas, delivery semantics, transactions, reliability config |
| 14-17 | Advanced Patterns | Connect, Debezium CDC, agent event design, saga orchestration |
| 18-19 | Operations | Production Strimzi, monitoring/debugging |
| 20 | AI-Assisted Development | Use AI to generate/tune configs |
| **21** | Capstone: Event-Driven Notifications | Production pipeline |
| 22 | Finalize Kafka Skill | Package prompts and patterns |

Each lesson ends with a skill reflection: test, find gaps, and improve.

---

## Outcome & Method

You finish with a production-ready Kafka deployment, reliable producer/consumer code integrated with FastAPI, and a Kafka skill for future projects. The chapter follows the 4-Layer approach: foundations → production patterns → AI-assisted authoring → spec-driven capstone.

---

## Prerequisites

- Chapters 49-51: container image and Kubernetes/Helm familiarity
- Ability to run a local Kubernetes cluster (e.g., Docker Desktop) for Strimzi
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
