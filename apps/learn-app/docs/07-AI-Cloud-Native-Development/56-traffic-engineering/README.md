---
sidebar_position: 56
title: "Chapter 56: Traffic Engineering"
description: "Gateway API, Envoy Gateway, KEDA autoscaling, and Envoy AI Gateway for production traffic management"
---

# Chapter 56: Traffic Engineering

Your AI agent is running inside Kubernetes, but external users can't reach it yet. Traffic engineering sits at the edge, handling ingress traffic, rate limiting, TLS, and autoscaling. This chapter teaches the **Gateway API**—the new Kubernetes standard replacing Ingress—with **Envoy Gateway** as the production implementation.

You'll build a `traffic-engineer` skill that encapsulates Gateway API patterns, rate limiting, TLS configuration, and KEDA autoscaling. By chapter's end, your Task API will have production-ready traffic management that protects against abuse and scales with demand.

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Build a traffic-engineer skill** from official documentation using Skill-First learning
- **Understand Gateway API** as the Kubernetes standard replacing Ingress
- **Deploy Envoy Gateway** as a production-grade Gateway API implementation
- **Configure HTTPRoute** with path, header, and query parameter matching
- **Implement rate limiting** with BackendTrafficPolicy to protect services and control costs
- **Configure TLS** with CertManager for automated certificate management
- **Deploy canary and blue-green** patterns with traffic splitting
- **Autoscale with KEDA** on Prometheus metrics and Kafka consumer lag
- **Apply resilience patterns** including retries, timeouts, and circuit breaking
- **Manage LLM traffic** with Envoy AI Gateway for token-based rate limiting

## Chapter Structure

| Lesson | Title | Duration | Focus |
|--------|-------|----------|-------|
| L00 | Build Your Traffic Engineering Skill | 25 min | Skill-First Discovery |
| L01 | Ingress Fundamentals | 30 min | Service types, Ingress limitations |
| L02 | Traefik Ingress Controller | 35 min | Simpler alternative before Gateway API |
| L03 | Gateway API - The New Standard | 40 min | GatewayClass, Gateway, HTTPRoute |
| L04 | Envoy Gateway Setup | 35 min | Helm installation, architecture |
| L05 | Traffic Routing with HTTPRoute | 40 min | Path, header, query matching |
| L06 | Rate Limiting & Circuit Breaking | 45 min | BackendTrafficPolicy patterns |
| L07 | TLS Termination with CertManager | 40 min | HTTPS, automated certificates |
| L08 | Traffic Splitting Patterns | 35 min | Canary, blue-green, A/B testing |
| L09 | Autoscaling with HPA, VPA & KEDA | 45 min | Event-driven scaling |
| L10 | Resilience Patterns | 40 min | Retries, timeouts, PDB |
| L11 | Envoy AI Gateway for LLM Traffic | 45 min | Token limiting, provider fallback |
| L12 | Capstone - Production Traffic for Task API | 60 min | Full integration |

**Total Duration**: ~8 hours

## Prerequisites

- **Chapter 49**: Docker (Task API containerized)
- **Chapter 50**: Kubernetes fundamentals (Pods, Services, Deployments)
- **Chapter 51**: Helm charts (installation method)
- **Chapter 55**: Observability (Prometheus metrics for KEDA)
- **Docker Desktop Kubernetes** enabled

## Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Gateway API | v1.2+ | Kubernetes standard for ingress |
| Envoy Gateway | v1.6+ | CNCF Gateway API implementation |
| Traefik | v3.x | Simpler ingress (comparison) |
| KEDA | v2.18+ | Event-driven autoscaling |
| CertManager | v1.16+ | TLS automation |
| Envoy AI Gateway | v0.4+ | LLM traffic management |

## Your Deliverable

By completing this chapter, you'll own a production-tested `traffic-engineer` skill that generates:

- Gateway + HTTPRoute configurations
- Rate limiting policies (per-user and global)
- TLS with automated certificate renewal
- KEDA ScaledObjects for autoscaling
- Canary deployment patterns

This skill becomes a **Digital FTE component**—reusable traffic management automation for any AI agent deployment.

## Looking Ahead

With traffic engineered and protected, Chapter 57 introduces **Dapr Actors and Workflows** for stateful, long-running agent patterns that require durable execution guarantees.
