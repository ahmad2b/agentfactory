---
sidebar_position: 51
title: "Chapter 51: Helm Charts for AI Services"
description: "Build your Helm skill first, then learn to understand and refine it into a production-ready asset"
---

# Chapter 51: Helm Charts for AI Services

You build the `helm-chart` skill first, then refine it through templating, testing, and distribution patterns so you can ship production-ready charts for your agents.

---

## Goals

- Master Helm templating (Go templates, helpers, values)
- Design multi-environment charts with schema validation
- Compose dependencies and hooks for lifecycle control
- Test and lint charts before release
- Publish and consume charts from OCI registries
- Capture the patterns in a reusable Helm skill

---

## Lesson Progression

| # | Lesson | Focus |
|---|--------|-------|
| **0** | Build Your Helm Skill | Scaffold from official docs |
| 1 | Helm Introduction | Chart basics and what the skill generates |
| 2-4 | Templating Foundation | Templates, helpers, values hierarchy |
| 5-6 | Advanced Patterns | Dependencies, hooks, lifecycle |
| 7 | Testing Charts | Linting and template debugging |
| 8 | OCI Registries | Push/pull/install from OCI |
| 9 | Library Charts | Standardized building blocks |
| 10 | AI-Assisted Development | Use AI to author/refine charts |
| **11** | Capstone: Production Chart | Ship a production-ready chart |
| 12 | Finalize Helm Skill | Package prompts and patterns |

Each lesson ends with a skill reflection: test, find gaps, and improve the skill.

---

## Outcome & Method

You finish with a production Helm chart for your Kubernetes-deployed agent plus a refined Helm skill. The chapter follows the 4-Layer method: foundational templating → advanced composition → AI-assisted authoring → spec-driven capstone.

---

## Prerequisites

- Chapter 50 Kubernetes fundamentals (Pods, Deployments, Services, ConfigMaps, Secrets, RBAC, HPA)
- Working Docker Desktop Kubernetes cluster and kubectl access
- **Create Library Charts**: Organizational standards that enforce consistency
- **Build Reusable Intelligence**: A Helm Chart Architect skill for AI-native development

## Chapter Structure

### Introduction Phase (Lesson 1): Helm Fundamentals

| Lesson | Title | Focus |
|--------|-------|-------|
| 1 | Introduction to Helm | Installation, chart structure, public charts, release management |

### Foundation Phase (Lessons 2-4): Templating Vocabulary

| Lesson | Title | Focus |
|--------|-------|-------|
| 2 | Advanced Go Templating | Variables, pipelines, conditionals, ranges |
| 3 | Named Templates and Helpers | `_helpers.tpl`, `include` vs `template`, scope rules |
| 4 | Values Deep Dive | Hierarchy, schema validation, multi-environment configs |

### Application Phase (Lessons 5-7): Real-World Patterns

| Lesson | Title | Focus |
|--------|-------|-------|
| 5 | Chart Dependencies | Subcharts, conditions, tags, import-values |
| 6 | Helm Hooks and Lifecycle | 9 hook types, weights, delete policies |
| 7 | Testing Your Charts | `helm lint`, `helm test`, template debugging |

### Distribution Phase (Lessons 8-9): Enterprise Scaling

| Lesson | Title | Focus |
|--------|-------|-------|
| 8 | OCI Registries and Distribution | `helm push`, `helm pull`, OCI URLs |
| 9 | Library Charts and Standardization | `type: library`, organizational patterns |

### Synthesis Phase (Lessons 10-12): Intelligence and Mastery

| Lesson | Title | Layer |
|--------|-------|-------|
| 10 | AI-Assisted Chart Development | Layer 2: AI Collaboration |
| 11 | Capstone: Production AI Agent Chart | Layer 4: Spec-Driven |
| 12 | Building a Helm Chart Skill | Layer 3: Intelligence Design |

## What Lesson 1 Covers

Lesson 1 (Introduction to Helm) teaches:
- Why Helm exists (repetitive YAML problem)
- Basic chart structure (Chart.yaml, values.yaml, templates/)
- Installing public charts (Bitnami Redis example)
- Creating simple custom charts (`helm create` scaffold)
- Basic release management (install, upgrade, rollback, uninstall)
- Environment-specific values files (dev vs prod)

**Lessons 2-12 build on this foundation** with:
- Advanced Go templating (variables, `with`, `range`, named templates)
- Chart dependencies and subchart composition
- Helm hooks and lifecycle management
- Chart testing strategies
- OCI registry distribution
- Library charts for organizational standards
- Production patterns (umbrella charts, GitOps integration points)
- AI-assisted chart development (Layer 2)
- Reusable Helm skill creation (Layer 3)

## Looking Ahead

After mastering Helm, you'll use your charts in:
- **Chapter 52 (Kafka)**: Event-driven architecture with Helm-deployed message brokers
- **Chapter 55 (CI/CD)**: GitOps pipelines that automatically deploy your Helm charts
- **Chapter 56 (Observability)**: Monitoring charts with Prometheus and Grafana dependencies
