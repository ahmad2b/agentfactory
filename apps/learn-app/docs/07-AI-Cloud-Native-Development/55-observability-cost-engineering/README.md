---
sidebar_position: 55
title: "Chapter 55: Observability & Cost Engineering"
description: "Master the three pillars of observability (metrics, tracing, logging), SRE foundations, and FinOps practices for cloud-native AI applications"
---

# Chapter 55: Observability & Cost Engineering

You build the `observability-cost-engineer` skill first, then implement the three pillars (metrics, traces, logs), SRE practices, and FinOps for your deployed agents.

---

## Goals

- Instrument metrics, traces, and logs with Prometheus, OpenTelemetry, Jaeger, and Loki
- Visualize and alert with Grafana; define SLIs/SLOs and error budgets
- Apply FinOps and OpenCost to control spend
- Integrate Dapr observability where applicable
- Capture the patterns in a reusable observability skill

---

## Lesson Progression

- **L00**: Build Your Observability Skill (skill-first)
- **L01**: Three Pillars overview (metrics, traces, logs)
- **L02-L05**: Instrumentation and collection with Prometheus, Grafana, OTel, Jaeger, Loki
- **L06-L07**: SRE foundations—SLIs, SLOs, error budgets, alerting
- **L08-L09**: Cost engineering and Dapr observability (OpenCost, FinOps practices)
- **L10**: Capstone—full observability stack for the Task API; finalize the skill

Each lesson ends with a reflection: test, find gaps, and improve the skill.

---

## Outcome & Method

You finish with a production observability stack (metrics, traces, logs, alerts, cost tracking) for the Task API plus a reusable observability/cost-engineering skill. The chapter combines foundational concepts, hands-on instrumentation, and a spec-driven capstone.

---

## Prerequisites

- Chapters 49-54 (Docker → GitOps pipeline)
- Part 6 Task API deployed via Kubernetes/ArgoCD

1. **Implement metrics collection** with Prometheus and visualize with Grafana dashboards using PromQL queries
2. **Instrument applications** with OpenTelemetry and trace requests through distributed systems with Jaeger
3. **Configure centralized logging** with Loki and query logs efficiently with LogQL
4. **Define and measure** SLIs, SLOs, and error budgets for your services using SRE best practices
5. **Set up cost monitoring** with OpenCost and implement FinOps practices for Kubernetes cost optimization
6. **Integrate Dapr observability** features for metrics and tracing across actors and workflows
7. **Build a complete observability stack** for production AI applications with multi-burn-rate alerting

## Chapter Structure

| # | Lesson | Duration | Your Skill Improves |
|---|--------|----------|---------------------|
| **0** | **Build Your Observability Skill** | 25 min | **Created from official docs** |
| 1 | Three Pillars of Observability | 20 min | Understand: metrics, traces, logs |
| 2 | Metrics with Prometheus | 30 min | Add: PromQL queries, ServiceMonitor |
| 3 | Visualization with Grafana | 25 min | Add: dashboard JSON, alerting |
| 4 | Distributed Tracing with OpenTelemetry & Jaeger | 30 min | Add: span creation, trace analysis |
| 5 | Centralized Logging with Loki | 25 min | Add: LogQL, structured logging |
| 6 | SRE Foundations: SLIs, SLOs, and Error Budgets | 30 min | Add: SLO recording rules |
| 7 | Alerting and Incident Response | 25 min | Add: multi-burn-rate alerting |
| 8 | Cost Engineering and FinOps | 30 min | Add: OpenCost queries, cost allocation |
| 9 | Dapr Observability Integration | 25 min | Add: Dapr metrics and tracing |
| **10** | **Capstone: Full Observability Stack for Task API** | 40 min | **Production-ready asset** |

## Every Lesson Has Skill Reflection

Each lesson ends with **"Reflect on Your Skill"**:

1. **Test**: Does your skill handle this lesson's concepts?
2. **Identify gaps**: What's missing from your current skill?
3. **Improve**: Add or refine the capability

By Lesson 10, you've tested and improved your skill through hands-on practice with each observability pillar.

## The Three Pillars

| Pillar | Tool | Query Language | What It Answers |
|--------|------|----------------|-----------------|
| **Metrics** | Prometheus | PromQL | "What's the request rate? Error rate? P95 latency?" |
| **Traces** | Jaeger | - | "Why is this request slow? Which service is the bottleneck?" |
| **Logs** | Loki | LogQL | "What happened at 3am? What error did user X see?" |

**Choosing the right signal:**
- **Metrics** for aggregated data over time (dashboards, alerting, capacity planning)
- **Traces** for debugging distributed request flows (latency analysis, bottleneck identification)
- **Logs** for event-level detail (error messages, audit trails, debugging)

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (Layer 3)**: Build your `observability-cost-engineer` skill from official documentation using `/fetching-library-docs` and `/skill-creator`.

- **Lesson 1 (Layer 1)**: Conceptual foundation—understand the three pillars before touching tools. Build mental models for when to use metrics vs traces vs logs.

- **Lessons 2-9 (Layer 2)**: AI-assisted hands-on practice. Install tools, write queries, build dashboards, define SLOs, and configure alerting—all while collaborating with your skill.

- **Lesson 10 (Layer 4)**: Spec-driven capstone. Build a complete observability stack for Task API with metrics, traces, logs, SLO dashboards, and cost monitoring—orchestrating everything you've learned.

## Prerequisites

- **Chapter 49 (Docker)**: Container resource limits, image building
- **Chapter 50 (Kubernetes)**: Pods, Deployments, Services, ConfigMaps—where observability tools deploy
- **Chapter 51 (Helm)**: Chart installation for kube-prometheus-stack, Loki, Jaeger
- **Chapter 52 (Kafka)**: Event-driven patterns (observability applies to message flows)
- **Chapter 53 (Dapr Core)**: Dapr sidecar pattern—L09 observes Dapr metrics and traces
- **Chapter 54 (GitOps)**: CI/CD pipelines—observability stack deploys via ArgoCD
- **Chapter 57 (Dapr Actors & Workflows)**: Actor patterns—L09 observes actor-based systems

## Running Example: Task API

Throughout this chapter, you instrument the **Task API** from earlier chapters:

- **L02**: Add Prometheus metrics (request count, latency histogram) to Task API
- **L03**: Build Grafana dashboard showing 4 golden signals for Task API
- **L04**: Instrument with OpenTelemetry, trace requests through Dapr sidecar to database
- **L05**: Configure structured JSON logging, correlate logs with trace IDs
- **L06**: Define 99.9% availability SLO for Task API, calculate error budget
- **L07**: Set up multi-burn-rate alerts that page when burning budget too fast
- **L08**: Configure cost allocation labels, identify Task API resource costs
- **L09**: Enable Dapr observability for actor-based task workflows
- **L10**: Complete observability stack with SLO dashboard and incident runbook

## Looking Ahead

This chapter gives you visibility into your deployed systems. Chapter 56 (API Gateway & Traffic Management) builds on this observability foundation to implement traffic routing, rate limiting, and canary deployments—using metrics to make intelligent traffic decisions.
