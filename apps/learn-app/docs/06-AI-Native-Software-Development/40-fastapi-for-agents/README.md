---
sidebar_position: 40
title: "Chapter 40: FastAPI for Agents"
description: "Expose the TaskManager Agent as a production-ready REST API with FastAPI"
---

# Chapter 40: FastAPI for Agents

You've built the **TaskManager Agent** with the OpenAI Agents SDK (Chapter 34), connected it via MCP (Chapters 37-38), and added reusable skills (Chapter 39). Now you'll expose it as an HTTP service. FastAPI is the natural choice: Python-native, async-first, automatic OpenAPI documentation, and battle-tested in production.

This chapter has three phases:
- **Lessons 1-5**: Learn FastAPI fundamentals with a simple Task API
- **Lessons 6-9**: Add production essentials—database, auth, security
- **Lessons 10-13**: Integrate agents with streaming and multi-agent patterns

By the end, the TaskManager Agent you built locally is callable via REST—tool execution, streaming responses, and authentication—all accessible to any HTTP client.

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Create FastAPI applications**: Build HTTP APIs with automatic documentation and validation
- **Write tests**: Use pytest and TestClient to test endpoints (Layer 1: Manual First)
- **Implement CRUD operations**: Design RESTful endpoints for Create, Read, Update, Delete
- **Handle errors properly**: Return appropriate HTTP status codes (200, 201, 400, 404, 422)
- **Manage configuration**: Use environment variables and pydantic-settings securely
- **Persist data**: Connect to PostgreSQL via SQLModel and Neon
- **Authenticate users**: Implement JWT tokens, password hashing, and rate limiting
- **Use dependency injection**: Organize code with FastAPI's Depends() pattern
- **Stream responses**: Implement Server-Sent Events (SSE) for real-time updates
- **Expose agents**: Wrap agents in REST endpoints where APIs become tools

## Chapter Structure

| # | Lesson | Focus |
|---|--------|-------|
| 1 | Hello FastAPI | First app, uvicorn, Swagger UI |
| 2 | Pytest Fundamentals | Testing endpoints (L1: Manual First) |
| 3 | POST and Pydantic Models | Request validation, models |
| 4 | Full CRUD Operations | GET, PUT, DELETE patterns |
| 5 | Error Handling | HTTPException, status codes |
| 6 | Environment Variables | pydantic-settings, secrets management |
| 7 | SQLModel + Neon Setup | Real database persistence |
| 8 | JWT Authentication | Tokens, protected endpoints |
| 9 | Password Hashing + Rate Limiting | Argon2, abuse protection |
| 10 | Dependency Injection | Depends(), repository pattern |
| 11 | Streaming with SSE | Server-Sent Events foundation |
| 12 | Agent Integration | APIs become tools, streaming agents |
| 13 | Capstone: TaskManager Agent Service | Complete multi-agent API |

## Prerequisites

- **Chapter 34**: OpenAI Agents SDK (Agent, Runner, function_tool, handoffs)
- **Chapters 37-38**: MCP experience (HTTP/SSE patterns familiar)
- **Part 5**: Python Fundamentals (async/await, type hints, Pydantic)

## The Running Example

Lessons 1-9 build a **Task API**—a production-ready CRUD service with testing, database persistence, and authentication. This teaches FastAPI patterns without agent complexity.

Lessons 10-13 transition to the **TaskManager Agent**—where you'll see the key insight: **APIs are just functions, functions become tools, agents use tools**.

## Looking Ahead

This chapter gives you a REST API exposing full TaskManager capabilities. Chapter 41 (ChatKit Server) builds on this foundation to add conversational infrastructure—the session management, turn-taking, and chat-specific patterns that conversational interfaces require.
