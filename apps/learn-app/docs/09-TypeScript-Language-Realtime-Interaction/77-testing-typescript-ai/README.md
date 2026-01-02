---
sidebar_position: 77
title: "Chapter 77: Testing TypeScript for AI Applications"
---

# Chapter 77: Testing TypeScript for AI Applications

AI applications present unique testing challenges. You can't run thousands of tests against OpenAI's API—it's too slow and too expensive. Streaming responses need careful mocking. And how do you test that your SDK stays in sync with your backend when the API evolves?

This chapter teaches testing patterns specifically for AI applications. You'll learn to mock LLM responses, test streaming behavior, implement contract testing with Zod, and use TypeScript's compiler as a testing tool.

## Before You Begin

**Prerequisites**: Chapter 76 (you'll test the SDK you built). Understanding of testing concepts from Part 5.

**What you'll need**: Vitest installed (`npm install -D vitest`), your Chapter 76 SDK.

---

## What You'll Learn

### Testing Fundamentals (Lessons 1-2)
- **Vitest Fundamentals**: Modern test runner that's faster than Jest and TypeScript-native
- **Mocking AI APIs**: vi.mock, vi.fn, mockResolvedValue for async functions, vi.mocked for type safety

### AI-Specific Testing (Lessons 3-4)
- **Testing Streaming Responses**: Mock SSE and Streamable HTTP, test async generators, verify cancellation
- **Contract Testing**: Zod schemas as contracts, frontend-backend compatibility, schema evolution

### Advanced Patterns (Lessons 5-6)
- **Integration Testing**: When to use real APIs, recorded fixtures, deterministic testing with seeds
- **Type-Driven Development**: TypeScript compiler as test tool, @ts-expect-error, type narrowing verification

---

## The AI Testing Problem

Traditional testing advice doesn't account for AI:

| Traditional Testing | AI Testing Challenge |
|--------------------|--------------------|
| "Test against real APIs" | OpenAI costs $0.03/request, tests run 10,000x |
| "Use fixtures" | LLM responses are non-deterministic |
| "Mock everything" | Streaming mocks are complex |
| "Test edge cases" | AI edge cases are unpredictable |

**The solution**: Strategic mocking for unit tests, recorded fixtures for integration tests, and contract testing to catch API drift.

---

## Vitest for AI Applications

Vitest is the modern choice for TypeScript testing:

```typescript
import { describe, it, expect, vi, beforeEach } from "vitest";
import { AgentSDK } from "./agent-sdk";

describe("AgentSDK", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("streams chat responses", async () => {
    // Mock the streaming response
    const mockStream = async function* () {
      yield { type: "content", delta: "Hello" };
      yield { type: "content", delta: " world" };
      yield { type: "done", usage: { total: 10 } };
    };

    vi.spyOn(sdk, "streamChat").mockReturnValue(mockStream());

    const chunks: string[] = [];
    for await (const chunk of sdk.chat.stream({ messages: [] })) {
      if (chunk.type === "content") {
        chunks.push(chunk.delta);
      }
    }

    expect(chunks.join("")).toBe("Hello world");
  });

  it("handles cancellation", async () => {
    const controller = new AbortController();
    const stream = sdk.chat.stream({
      messages: [],
      signal: controller.signal,
    });

    // Cancel after first chunk
    setTimeout(() => controller.abort(), 10);

    await expect(async () => {
      for await (const chunk of stream) {
        // Process chunks
      }
    }).rejects.toThrow("aborted");
  });
});
```

---

## Contract Testing with Zod

Zod schemas serve as contracts between frontend and backend:

```typescript
import { z } from "zod";
import { describe, it, expect } from "vitest";

// This schema IS the contract
const ChatResponseSchema = z.object({
  choices: z.array(z.object({
    message: z.object({
      role: z.string(),
      content: z.string(),
    }),
  })),
});

describe("API Contract", () => {
  it("validates against real API response", async () => {
    // Recorded fixture from actual API
    const fixture = await import("./fixtures/chat-response.json");

    const result = ChatResponseSchema.safeParse(fixture);

    if (!result.success) {
      console.error("Contract violation:", result.error.format());
    }
    expect(result.success).toBe(true);
  });

  it("rejects malformed responses", () => {
    const malformed = { choices: [{ message: { role: 123 } }] };

    expect(ChatResponseSchema.safeParse(malformed).success).toBe(false);
  });
});
```

---

## Chapter Structure

| Lesson | Topic | Duration |
|--------|-------|----------|
| 1 | Vitest Fundamentals | 20 min |
| 2 | Mocking AI APIs | 25 min |
| 3 | Testing Streaming Responses | 25 min |
| 4 | Contract Testing | 20 min |
| 5 | Integration Testing Patterns | 20 min |
| 6 | Type-Driven Development | 15 min |

**Total**: ~2 hours

---

## What You'll Build

**Capstone: SDK Test Suite**

By the end of this chapter, you'll have comprehensive tests for your Chapter 76 SDK:

```typescript
// test/agent-sdk.test.ts
import { describe, it, expect, vi } from "vitest";
import { createAgentSDK } from "../src/agent-sdk";

describe("AgentSDK", () => {
  describe("chat.create", () => {
    it("validates response against schema", async () => { /* ... */ });
    it("throws on invalid response", async () => { /* ... */ });
  });

  describe("chat.stream", () => {
    it("yields chunks in order", async () => { /* ... */ });
    it("handles tool calls", async () => { /* ... */ });
    it("respects abort signal", async () => { /* ... */ });
    it("retries on transient errors", async () => { /* ... */ });
  });

  describe("contracts", () => {
    it("matches backend schema", async () => { /* ... */ });
    it("handles schema evolution gracefully", async () => { /* ... */ });
  });
});
```

Test metrics you'll achieve:
- 90%+ code coverage on SDK
- Under 5 second test runtime (all mocked)
- 0 real API calls in unit tests
- Contract tests that catch API drift

---

## What's Next

After testing your SDK, **Chapter 78: CLI Tools and Developer Experience** teaches you to build a publishable CLI that uses your SDK. You'll implement streaming terminal output, conversation history, and package for npm distribution.

---

## Pedagogical Approach

This chapter uses **Layer 1 (Manual Foundation)** for testing concepts:

- You write tests manually to understand mocking patterns
- Real failures teach debugging strategies
- Contract tests are conceptually explained before implementation

The Three Roles apply:
- **AI as Teacher**: Explains Vitest APIs and mocking patterns
- **AI as Student**: You describe edge cases, AI generates test scenarios
- **AI as Co-Worker**: Collaborate on complex streaming test implementations
