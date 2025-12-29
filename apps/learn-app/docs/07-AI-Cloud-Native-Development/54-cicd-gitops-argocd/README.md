---
sidebar_position: 54
title: "Chapter 54: CI/CD Pipelines & GitOps with ArgoCD"
description: "Build your GitOps skill first, then learn to understand and refine it into a production-ready asset"
---

# Chapter 54: CI/CD Pipelines & GitOps with ArgoCD

**You will build a GitOps skill BEFORE you learn GitOps.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `gitops-deployment` skill using tools from Chapter 5. Then you spend the chapter understanding what you built and making it better. By the end, you don't just "know CI/CD and ArgoCD"—you OWN a production-ready skill.

## The Skill-First Arc

```
L00: Build Your GitOps Skill (25 min)
  │   └── Clone skills-lab, fetch docs, create skill
  │
  ├── L01-04: CI/CD Fundamentals
  │   └── Concepts, GitHub Actions, Docker builds, testing
  │
  ├── L05-09: GitOps & ArgoCD Core
  │   └── Principles, ArgoCD, first app, sync strategies
  │
  ├── L10-15: Production Patterns
  │   └── ApplicationSets, RBAC, health, progressive, secrets, multi-cluster
  │
  └── L16-18: AI Collaboration & Capstone
      └── AI-assisted, end-to-end pipeline, skill finalization
```

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your GitOps Skill** | **Created from official docs** |
| 1 | CI/CD Concepts | Understand: pipeline stages |
| 2 | GitHub Actions Fundamentals | Refine: workflow YAML |
| 3 | Building Docker Images in CI | Add: CI build patterns |
| 4 | Testing & Quality Gates | Add: test automation |
| 5 | GitOps Principles | Understand: Git as truth |
| 6 | ArgoCD Architecture | Validate: ArgoCD knowledge |
| 7 | Your First ArgoCD Application | Refine: Application CRD |
| 8 | Sync Strategies & Policies | Add: sync patterns |
| 9 | Sync Waves & Hooks | Add: ordering patterns |
| 10 | ApplicationSets | Add: scaling patterns |
| 11 | ArgoCD Projects & RBAC | Add: security patterns |
| 12 | Health & Notifications | Add: observability |
| 13 | Progressive Delivery | Add: canary/blue-green |
| 14 | Secrets Management | Add: secrets patterns |
| 15 | Multi-Cluster Deployments | Add: hub-spoke patterns |
| 16 | AI-Assisted GitOps | Refine: AI collaboration |
| **17** | **Capstone: End-to-End Pipeline** | **Production-ready** |
| 18 | Finalize GitOps Skill | **Complete asset** |

## Every Lesson Has Skill Reflection

Each lesson ends with **"Reflect on Your Skill"**:

1. **Test**: Does your skill handle this lesson's concepts?
2. **Identify gaps**: What's missing?
3. **Improve**: Add or refine the capability

By Lesson 18, you've tested and improved your skill 17+ times.

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Design CI/CD pipelines**: Diagram stages (trigger → build → test → push → deploy) and explain each stage's purpose
- **Implement GitHub Actions**: Create workflows for Python projects with multi-platform builds
- **Build and push images**: Automate Docker builds with SHA-tagged releases and registry push
- **Run tests in CI**: Implement quality gates that block deployment on test failures
- **Understand GitOps principles**: Articulate why Git-as-truth enables auditability, rollback, and collaboration
- **Deploy ArgoCD**: Install ArgoCD 3.x on Minikube and access the UI/CLI
- **Create ArgoCD Applications**: Sync Helm charts from Git to cluster with health monitoring
- **Master sync strategies**: Configure auto-sync, auto-prune, self-heal, and sync waves with hooks
- **Scale with ApplicationSets**: Deploy to multiple environments with List, Cluster, and Matrix generators
- **Secure deployments**: Configure ArgoCD Projects, RBAC, and multi-tenancy patterns
- **Manage secrets**: Use Sealed Secrets or External Secrets Operator (never store secrets in Git)
- **Use AI for GitOps**: Collaborate with Claude to generate and refine ArgoCD manifests
- **Build reusable intelligence**: Create a GitOps Deployment Skill (Persona + Questions + Principles)

## Chapter Structure

| Lesson | Title | Layer | Focus |
|--------|-------|-------|-------|
| 1 | CI/CD Concepts: The Automated Pipeline | L1 | Stages, triggers, artifacts, value proposition |
| 2 | GitHub Actions Fundamentals | L1 | Workflows, jobs, steps, triggers, YAML syntax |
| 3 | Building Docker Images in CI | L1 | Multi-platform builds, registry push, caching |
| 4 | Testing and Quality Gates | L1 | Unit/integration tests, coverage, blocking failures |
| 5 | GitOps Principles: Git as Truth | L1 | Declarative, versioned, reconciled, drift detection |
| 6 | ArgoCD Architecture & Installation | L1 | Components, CRDs, Helm installation on Minikube |
| 7 | Your First ArgoCD Application | L1 | Source, destination, sync policies, UI/CLI creation |
| 8 | Sync Strategies and Policies | L1 | Manual, auto-sync, auto-prune, self-heal |
| 9 | Sync Waves and Resource Hooks | L1 | Wave ordering, PreSync, PostSync, SyncFail hooks |
| 10 | ApplicationSets: Scaling Deployments | L1 | List, Cluster, Matrix, Git generators |
| 11 | ArgoCD Projects and RBAC | L1 | Multi-tenancy, resource restrictions, roles |
| 12 | Health Status and Notifications | L1 | Health checks, degraded states, Slack/webhook alerts |
| 13 | Progressive Delivery Overview | L1 | Canary, blue-green, Argo Rollouts concepts |
| 14 | Secrets Management for GitOps | L1 | External Secrets, Sealed Secrets, Vault patterns |
| 15 | Multi-Cluster Deployments | L1 | Hub-spoke, cluster registration, ApplicationSets |
| 16 | AI-Assisted GitOps Workflows | L2 | Claude collaboration for manifests and debugging |
| 17 | Capstone: End-to-End Agent Pipeline | L4 | Spec-driven CI/CD for Part 6 agent |
| 18 | Building the GitOps Deployment Skill | L3 | Persona + Questions + Principles skill design |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lessons 1-15 (Layer 1)**: Build mental models of CI/CD and GitOps concepts manually before AI assistance. This includes pipeline architecture, GitHub Actions workflows, GitOps principles, ArgoCD fundamentals, sync strategies, ApplicationSets, RBAC, secrets, and multi-cluster patterns.

- **Lesson 16 (Layer 2)**: Collaborate with Claude to generate and refine ArgoCD manifests through iterative dialogue. By this point, you have deep GitOps knowledge to evaluate AI output critically.

- **Lesson 17 (Layer 4)**: Apply all lessons in a spec-driven capstone project. Build a complete CI/CD pipeline that deploys your Part 6 FastAPI agent from code push to running service.

- **Lesson 18 (Layer 3)**: Create reusable intelligence—a GitOps Deployment Skill that captures decision-making principles for any future deployment work.

## Prerequisites

- **Chapter 49 (Docker)**: Container image building, multi-stage builds, registry concepts
- **Chapter 50 (Kubernetes)**: Cluster operations, RBAC, resource management, Deployments, Services
- **Chapter 51 (Helm)**: Chart structure, templating, releases—ArgoCD deploys Helm charts
- **Part 6 FastAPI Agent**: A working agent in a GitHub repository (this is what you'll deploy)
- **GitHub Account**: For Actions workflows and repository hosting
- **Container Registry Access**: Docker Hub, GHCR, or similar (from Chapter 49)

## Your Part 6 Agent: The Thread Through This Chapter

Throughout this chapter, we deploy your Part 6 FastAPI agent with a complete automated pipeline:

- **Lessons 1-4**: Build the CI pipeline that tests and pushes your agent container on every commit
- **Lessons 5-9**: Deploy the agent with ArgoCD, mastering sync strategies and hooks
- **Lessons 10-15**: Prepare for production with ApplicationSets, RBAC, secrets, and multi-cluster
- **Lesson 16**: Collaborate with AI to generate sophisticated ArgoCD configurations
- **Lesson 17 (Capstone)**: Complete end-to-end automation—push code, watch it deploy, validate, and rollback
- **Lesson 18**: Capture your learning as a reusable GitOps Deployment Skill

## Looking Ahead

This chapter produces a fully automated CI/CD pipeline and a reusable GitOps skill. Chapter 56 (Observability & Cost Engineering) builds on this foundation with metrics, logging, and tracing for your deployed agents.
