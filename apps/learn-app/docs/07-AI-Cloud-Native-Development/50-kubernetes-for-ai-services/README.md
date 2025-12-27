---
sidebar_position: 50
title: "Chapter 50: Kubernetes for AI Services"
description: "Deploy and orchestrate AI agents on Kubernetes clusters"
---

# Chapter 50: Kubernetes for AI Services

Docker gives you portable containers. Kubernetes orchestrates them—handling deployment, scaling, networking, and self-healing automatically. When your agent container crashes, Kubernetes restarts it. When traffic spikes, Kubernetes scales it. When you push a new version, Kubernetes rolls it out safely.

This chapter teaches Kubernetes from core primitives to production-ready patterns for AI services. You'll learn the declarative model that makes Kubernetes powerful, understand how the control plane manages desired state, and master the kubectl commands that make operations automated and repeatable.

By the end, your containerized FastAPI agent from Chapter 49 will be running on a Kubernetes cluster with proper health checks, resource management, security policies, and automated scaling—all without manual intervention.

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

| Lesson | Title | Layer | Focus |
|--------|-------|-------|-------|
| 1 | Kubernetes Architecture & the Declarative Model | L1 | Control plane, workers, desired vs observed state |
| 2 | Enabling Kubernetes (Docker Desktop) | L1 | Enable K8s, verify, kubectl context |
| 3 | Pods: The Atomic Unit | L1 | Pod anatomy, YAML, lifecycle |
| 4 | Deployments: Self-Healing at Scale | L1 | ReplicaSets, rolling updates, rollbacks |
| 5 | Services & Networking | L1 | ClusterIP, NodePort, LoadBalancer, DNS |
| 6 | Namespaces: Virtual Clusters | L1 | Isolation, ResourceQuotas, LimitRanges |
| 7 | ConfigMaps & Secrets | L1 | Configuration injection, security notes |
| 8 | Resource Management & Debugging | L1 | Requests/limits, QoS, kubectl debug |
| 9 | Horizontal Pod Autoscaler | L1 | Metrics-server, CPU/memory scaling |
| 10 | RBAC: Securing Agent Deployments | L1 | ServiceAccount, Role, RoleBinding |
| 11 | Health Checks & Probes | L1 | Liveness, readiness, startup probes |
| 12 | Jobs & CronJobs: Batch Workloads | L1 | One-time tasks, scheduled jobs |
| 13 | AI-Assisted K8s with kubectl-ai | L2 | Natural language to manifests |
| 14 | Capstone: Deploy Your Agent to Kubernetes | L4 | Spec-driven deployment, full validation |
| 15 | Building the Kubernetes Deployment Skill | L3 | Persona + Questions + Principles |

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
