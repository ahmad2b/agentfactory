---
sidebar_position: 50
title: "Chapter 50: Kubernetes for AI Services"
description: "Build your Kubernetes skill first, then learn to understand and refine it into a production-ready asset"
---

# Chapter 50: Kubernetes for AI Services

**You will build a Kubernetes skill BEFORE you learn Kubernetes.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `kubernetes-deployment` skill using tools from Chapter 5. Then you spend the chapter understanding what you built and making it better. By the end, you don't just "know Kubernetes"—you OWN a production-ready skill.

## The Skill-First Arc

```
L00: Build Your Kubernetes Skill (25 min)
  │   └── Clone skills-lab, fetch docs, create skill
  │
  ├── L01-05: K8s Fundamentals
  │   └── Architecture, Pods, Deployments, Services
  │
  ├── L06-12: Production Essentials
  │   └── Config, Resources, Security, Health, Scaling
  │
  ├── L13-15: AI Collaboration & Capstone
  │   └── kubectl-ai, deployment, skill finalization
  │
  └── L16-22 (Optional): Advanced Patterns
      └── Init, Sidecar, Ingress, StatefulSets
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Understand Kubernetes architecture**: Control plane, worker nodes, and the declarative model
- **Deploy containers on Kubernetes**: Pods, Deployments, ReplicaSets, Jobs, CronJobs
- **Organize workloads**: Namespaces for isolation, resource quotas
- **Configure applications**: ConfigMaps for configuration, Secrets for sensitive data
- **Manage resources**: CPU/memory requests and limits, Horizontal Pod Autoscaler
- **Secure deployments**: RBAC, ServiceAccounts, Role, RoleBinding
- **Monitor health**: Liveness, readiness, and startup probes
- **Use kubectl-ai**: AI-assisted manifest generation and cluster operations
- **Deploy agents at scale**: Rolling updates, horizontal scaling, self-healing patterns

## Chapter Structure

### Core Lessons (Required for Agent Deployment)

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Kubernetes Skill** | **Created from official docs** |
| 1 | Kubernetes Architecture | Understand: what skill generates |
| 2 | Enabling K8s (Docker Desktop) | Validate: skill works locally |
| 3 | Pods: The Atomic Unit | Refine: Pod YAML patterns |
| 4 | Deployments: Self-Healing | Refine: Deployment patterns |
| 5 | Services & Networking | Add: Service types |
| 6 | Namespaces: Virtual Clusters | Add: namespace isolation |
| 7 | ConfigMaps & Secrets | Add: config injection |
| 8 | Resource Management | Add: requests/limits |
| 9 | Horizontal Pod Autoscaler | Add: HPA patterns |
| 10 | RBAC Security | Add: RBAC scaffolding |
| 11 | Health Checks & Probes | Add: probe patterns |
| 12 | Jobs & CronJobs | Add: batch workloads |
| 13 | AI-Assisted with kubectl-ai | Refine: AI collaboration |
| **14** | **Capstone: Deploy Agent** | **Production-ready** |
| 15 | Finalize Kubernetes Skill | **Complete asset** |

## Every Lesson Has Skill Reflection

Each lesson ends with **"Reflect on Your Skill"**:

1. **Test**: Does your skill handle this lesson's concepts?
2. **Identify gaps**: What's missing?
3. **Improve**: Add or refine the capability

By Lesson 15, you've tested and improved your skill 14+ times.

### Optional Lessons (Advanced Patterns)

| Lesson | Title | Layer | Focus |
|--------|-------|-------|-------|
| 16 | Init Containers (Optional) | L1 | Initialization patterns, dependency setup |
| 17 | Sidecar Containers (Optional) | L1 | Native sidecars (K8s 1.28+), logging |
| 18 | Ingress: External Access (Optional) | L1 | Path/host routing, TLS, annotations |
| 19 | Service Discovery Deep Dive (Optional) | L1 | CoreDNS, FQDN, headless services |
| 20 | StatefulSets (Optional) | L1 | Stable identity, volumeClaimTemplates |
| 21 | Persistent Storage (Optional) | L1 | PV, PVC, StorageClass |
| 22 | Kubernetes Security Deep Dive (Optional) | L1 | SecurityContext, NetworkPolicy, Pod Security |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lessons 1-12, 16-22 (Layer 1)**: Build mental models of Kubernetes concepts manually before AI assistance. Core lessons cover essential primitives; optional lessons add advanced patterns.

- **Lesson 13 (Layer 2)**: Collaborate with kubectl-ai using Three Roles to translate natural language into cluster operations. By this point, you have deep Kubernetes knowledge to evaluate AI-generated manifests critically.

- **Lesson 14 (Layer 4)**: Apply all lessons in a spec-driven capstone project. Deploy your Part 6 FastAPI agent with proper configuration, security, health checks, and resource management.

- **Lesson 15 (Layer 3)**: Create reusable intelligence—a Kubernetes deployment skill that compounds across cloud-native projects.

## Core vs Optional Path

**Core Path (Lessons 1-15)**: Everything you need to deploy a stateless AI agent to Kubernetes with production-ready configuration. Most AI agents are stateless services that need Deployments, Services, ConfigMaps, health checks, and RBAC.

**Optional Path (Lessons 16-22)**: Advanced patterns for specialized use cases:
- Init containers for complex initialization sequences
- Sidecars for logging, monitoring, or proxying
- Ingress for external HTTP access
- Service discovery for microservice communication
- StatefulSets for agents that need persistent identity
- Persistent storage for agents that store data
- Deep security for compliance requirements

## Prerequisites

- **Chapter 49 completion**: A containerized FastAPI agent pushed to a registry—this is the container you'll deploy to Kubernetes
- **Docker Desktop installed and running**: Kubernetes is built into Docker Desktop—you enable it with a checkbox
- **Basic command-line comfort**: You should be comfortable running commands in a terminal
- **No Kubernetes experience required**: Lesson 1 explains cluster architecture from scratch

## Your Part 6 Agent: The Thread Through This Chapter

Throughout this chapter, we deploy your Part 6 FastAPI agent to Kubernetes:

- **Lessons 1-12**: Learn Kubernetes concepts using your agent as the running example—from basic Pod deployment to production-ready configurations with security, autoscaling, and health checks
- **Lesson 13**: Use kubectl-ai to generate deployment manifests and troubleshoot cluster issues collaboratively
- **Lesson 14 (Capstone)**: Deploy your containerized Part 6 agent to a Kubernetes cluster with all production patterns applied
- **Lesson 15**: Create a reusable skill for future Kubernetes deployment work
- **Lessons 16-22 (Optional)**: Add advanced patterns as needed for your specific use case

By the end, your agent runs on an orchestrated cluster with automatic scaling, self-healing, proper security, and rolling updates.

## Looking Ahead

This chapter produces a deployed agent and a reusable Kubernetes deployment skill. Chapter 51 (Helm Charts) packages your deployments for repeatable, environment-specific installations.
