---
sidebar_position: 60
title: "Chapter 60: Real Cloud Deployment"
description: "Deploy AI agent services to production Kubernetes clusters on real cloud providers. Master the universal pattern: provision, connect, deploy."
---

# Chapter 60: Real Cloud Deployment

**You will build a cloud deployment skill BEFORE you deploy to the cloud.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `multi-cloud-deployer` skill using tools from Chapter 5. Then you deploy your Task API to real cloud infrastructure. By the end, you don't just "know cloud deployment"—you OWN a production-ready skill that works across providers.

## The Key Insight

**Only cluster provisioning differs between clouds. Everything else is identical.**

```
Cloud Provider A              Cloud Provider B
      │                             │
      ▼                             ▼
┌─────────────────┐         ┌─────────────────┐
│ doctl/az/gcloud │         │ hetzner-k3s     │
│ (provision)     │         │ (provision)     │
└────────┬────────┘         └────────┬────────┘
         │                           │
         └───────────┬───────────────┘
                     │
                     ▼
           ┌─────────────────┐
           │ kubectl/Helm    │  ← 90% identical
           │ Dapr/Traefik    │
           │ cert-manager    │
           └─────────────────┘
```

kubectl commands, Helm deployments, Ingress configuration, Dapr installation, secrets management—all universal.

## Two Learning Paths

| Path | Provider | Monthly Cost | Best For |
|------|----------|--------------|----------|
| **Production** | DigitalOcean DOKS | ~$24+/mo | Teams, real traffic, managed SLA |
| **Learning Sandbox** | Hetzner + K3s | ~$5/mo | Personal practice, budget-conscious |

Choose based on your goals—the Kubernetes skills transfer directly between both.

## The Skill-First Arc

```
L00: Build Your Cloud Deployment Skill (15 min)
  │   └── Clone skills-lab, fetch docs, create multi-cloud-deployer skill
  │
  ├── L01-L04: Cloud & DOKS Fundamentals (L1 - Manual)
  │   └── Why cloud, doctl setup, cluster provisioning, Load Balancer/DNS
  │
  ├── L05-L06: Deploying to DOKS (L2 - AI Collaboration)
  │   └── Full stack deployment, secrets & configuration
  │
  ├── L07: Hetzner Alternative Path (L1 - Manual)
  │   └── Budget cloud lab with K3s
  │
  ├── L08-L09: Production & Multi-Cloud (L2 - AI Collaboration)
  │   └── Production checklist, same patterns different clouds
  │
  └── L10: Capstone - Full Production Deployment (L4 - Spec-Driven)
      └── End-to-end deployment, skill finalization
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Provision Kubernetes clusters** on DigitalOcean (DOKS) and Hetzner (K3s)
- **Deploy full production stacks**: Dapr, Traefik Ingress, cert-manager, Let's Encrypt
- **Configure cloud-native secrets**: API tokens, image pull secrets, environment configs
- **Set up real Load Balancers and DNS** with HTTPS endpoints
- **Run production verification checklists** with kubectl commands
- **Understand the universal pattern**: provision → connect → deploy
- **Apply skills across providers**: AKS, GKE, EKS, Civo (quick-starts)
- **Manage costs**: Budget alerts, teardown procedures, cost optimization

## Chapter Structure

| # | Lesson | Teaching Layer | Your Skill Improves |
|---|--------|----------------|---------------------|
| **0** | **Build Your Cloud Deployment Skill** | L3 (Skill-First) | **Created from official docs** |
| 1 | Beyond Docker Desktop | L1 (Manual) | Understand: why real cloud |
| 2 | DigitalOcean Account & doctl Setup | L1 (Manual) | Add: DO authentication |
| 3 | Provisioning DOKS Cluster | L1 (Manual) | Add: cluster creation |
| 4 | Cloud Load Balancer & DNS | L1 (Manual) | Add: networking patterns |
| 5 | Deploying Task API to DOKS | L2 (Collaboration) | Refine: deployment sequence |
| 6 | Production Secrets & Configuration | L2 (Collaboration) | Add: secrets management |
| 7 | Personal Cloud Lab - Hetzner + K3s | L1 (Manual) | Add: budget alternative |
| 8 | Production Checklist & Verification | L2 (Collaboration) | Add: verification patterns |
| 9 | Same Patterns, Different Clouds | L2 (Collaboration) | Add: multi-cloud quick-starts |
| **10** | **Capstone - Full Production Deployment** | L4 (Spec-Driven) | **Production-ready asset** |

## Every Lesson Has Skill Reflection

Each lesson ends with **"Reflect on Your Skill"**:

1. **Test**: Does your skill handle this lesson's concepts?
2. **Identify gaps**: What's missing for multi-cloud support?
3. **Improve**: Add provider-specific or universal patterns

By Lesson 10, you've tested and improved your skill 10+ times.

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (Layer 3)**: Create the `multi-cloud-deployer` skill FIRST—grounded in official documentation, not AI memory.

- **Lessons 1-4, 7 (Layer 1)**: Build mental models of cloud infrastructure manually. Understand what your skill will automate.

- **Lessons 5-6, 8-9 (Layer 2)**: Collaborate with AI using Three Roles (invisible framework) to deploy and verify production stacks.

- **Lesson 10 (Layer 4)**: Apply all lessons in a spec-driven capstone. Deploy your Task API with full production stack, verify with HTTPS, finalize your skill.

## Prerequisites

- **Chapter 49-59 completion**: Containerized Task API, Kubernetes basics, Helm, observability
- **Cloud account ready**: DigitalOcean ($200 free credit) or Hetzner account
- **Domain name** (optional): For real HTTPS, or use nip.io/sslip.io for testing
- **Terminal comfort**: You should be comfortable running CLI commands

## Your Task API: The Thread Through This Chapter

Throughout this chapter, you deploy your Task API to real cloud infrastructure:

- **Lessons 1-4**: Learn cloud fundamentals using Task API as the deployment target
- **Lessons 5-6**: Deploy complete stack (Dapr + Ingress + TLS) with AI assistance
- **Lesson 7**: Alternative path with Hetzner for budget-conscious learners
- **Lessons 8-9**: Validate production readiness, understand multi-cloud portability
- **Lesson 10 (Capstone)**: Full production deployment with spec-driven approach

By the end, your Task API runs on real cloud infrastructure with HTTPS, monitoring, and production-grade configuration.

## Looking Ahead

This chapter produces a deployed Task API and a reusable `multi-cloud-deployer` skill. This is the culmination of Part 7: AI Cloud Native Development—you now have skills to deploy AI agent services to any major cloud provider.
