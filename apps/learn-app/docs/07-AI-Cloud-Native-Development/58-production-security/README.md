---
sidebar_position: 58
title: "Chapter 58: Production Security & Compliance"
description: "Build your cloud security skill first, then learn to secure Kubernetes deployments with RBAC, NetworkPolicies, Pod Security Standards, and compliance controls"
---

# Chapter 58: Production Security & Compliance

**You will build a cloud-security skill BEFORE you learn security concepts.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `cloud-security` skill using tools from Chapter 5. Then you spend the chapter understanding what you built and making it better. By the end, you don't just "know Kubernetes security"—you OWN a production-ready security skill.

## The Skill-First Arc

```
L00: Build Your Cloud Security Skill (15 min)
  │   └── Clone skills-lab, fetch docs, create skill
  │
  ├── L01: Cloud Native Security Model (25 min)
  │   └── 4C's: Cloud → Cluster → Container → Code
  │
  ├── L02-L03: Cluster Security (60 min)
  │   └── RBAC, NetworkPolicies
  │
  ├── L04-L06: Container Security (75 min)
  │   └── Secrets, PSS, Image Scanning
  │
  ├── L07: Dapr Security with AI Collaboration (25 min)
  │   └── mTLS, component scopes, Three Roles
  │
  ├── L08: Compliance Fundamentals (20 min)
  │   └── SOC2, HIPAA awareness
  │
  └── L09: Capstone - Secure Task API (40 min)
      └── Apply all patterns, 10-point audit
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Apply the 4C security model**: Understand defense in depth across Cloud, Cluster, Container, and Code layers
- **Implement RBAC**: ServiceAccounts, Roles, ClusterRoles, RoleBindings with least privilege
- **Configure NetworkPolicies**: Default-deny with explicit allow rules, DNS considerations
- **Manage secrets securely**: K8s Secrets via volume mounts, External Secrets Operator awareness
- **Enforce Pod Security Standards**: Namespace labels, Restricted profile compliance
- **Scan container images**: Trivy for vulnerability detection, SBOM generation
- **Secure Dapr deployments**: mTLS verification, component scopes, API tokens
- **Map compliance requirements**: SOC2 and HIPAA controls to Kubernetes primitives
- **Conduct security audits**: 10-point checklist for production deployments

## Chapter Structure

| # | Lesson | Your Skill Improves | Layer |
|---|--------|---------------------|-------|
| **0** | **Build Your Cloud Security Skill** | **Created from official docs** | L3 |
| 1 | Cloud Native Security Model | Understand: 4C framework | L1 |
| 2 | RBAC Deep Dive | Add: ServiceAccount patterns | L1 |
| 3 | NetworkPolicies | Add: default-deny patterns | L1 |
| 4 | Secrets Management | Add: volume mount patterns | L1 |
| 5 | Pod Security Standards | Add: PSS compliance | L1 |
| 6 | Image Scanning & Supply Chain | Add: Trivy integration | L1 |
| 7 | Dapr Security | Refine: mTLS, scopes (Three Roles) | L2 |
| 8 | Compliance Fundamentals | Add: compliance mapping | L1 |
| **9** | **Capstone: Secure Task API** | **Production-ready audit** | L4 |

## Every Lesson Has Skill Reflection

Each lesson ends with **"Reflect on Your Skill"**:

1. **Test**: Does your skill handle this lesson's concepts?
2. **Identify gaps**: What's missing?
3. **Improve**: Add or refine the capability

By Lesson 9, you've tested and improved your skill 8+ times.

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (Layer 3)**: Create your `cloud-security` skill from official Kubernetes security documentation
- **Lessons 1-6, 8 (Layer 1)**: Build mental models of security concepts manually before AI assistance
- **Lesson 7 (Layer 2)**: Collaborate with AI using Three Roles to configure Dapr security
- **Lesson 9 (Layer 4)**: Apply all security patterns in a spec-driven capstone with 10-point audit

## Prerequisites

- **Chapter 50 completion**: Kubernetes fundamentals (Pods, Deployments, Services, Namespaces)
- **Chapter 53 completion**: Dapr building blocks (state, pub/sub, service invocation)
- **Chapter 55 completion**: Observability basics (metrics, logging, tracing)
- **Chapter 56 completion**: Traffic engineering (Gateway API)
- **Docker Desktop with Kubernetes enabled**: Local development environment
- **Task API from Ch40**: The running example you'll secure throughout this chapter

## Technology Versions

| Technology | Version | Purpose |
|------------|---------|---------|
| Kubernetes | 1.28+ | Container orchestration |
| Calico | 3.26+ | CNI with NetworkPolicy support |
| Trivy | latest | Image vulnerability scanning |
| Dapr | 1.12+ | Distributed application runtime |
| External Secrets Operator | 0.9+ | External secrets management |
| Cosign | latest | Image signing |

## Your Task API: The Thread Through This Chapter

Throughout this chapter, we secure the Task API from Chapter 40:

- **Lesson 1**: Classify Task API security requirements across 4C layers
- **Lessons 2-3**: Implement RBAC and NetworkPolicy for Task API
- **Lessons 4-6**: Add secrets, PSS compliance, and vulnerability scanning
- **Lesson 7**: Configure Dapr security for Task API sidecars
- **Lesson 8**: Map Task API to compliance requirements
- **Lesson 9**: Complete 10-point security audit

By the end, your Task API is production-ready with comprehensive security controls.

## NOT Covered in This Chapter

The following are covered in Chapter 56 (Traffic Engineering):
- TLS termination at ingress (Gateway API TLS)
- JWT/OIDC authentication (SecurityPolicy)
- Rate limiting (EnvoyPatchPolicy)

## Looking Ahead

This chapter produces a secured Task API and a reusable `cloud-security` skill. Chapter 59 builds on these foundations for enterprise deployment patterns.
