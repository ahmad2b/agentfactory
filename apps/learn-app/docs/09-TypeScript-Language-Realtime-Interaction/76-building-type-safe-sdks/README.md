---
sidebar_position: 76
title: "Chapter 76: Building Type-Safe AI SDKs"
---

# Chapter 76: Building Type-Safe AI SDKs

Every AI platform needs an SDK. OpenAI, Anthropic, Vercel, and MCP all provide TypeScript SDKs that make their APIs pleasant to use. In this chapter, you'll learn the patterns behind these SDKs and build your own type-safe wrapper for the FastAPI AI backend you created in Part 7.

The key insight: SDKs aren't just HTTP wrappers. They provide **runtime validation** (catching API changes before they break your app), **streaming abstractions** (making async iteration feel natural), and **developer experience** (autocomplete, inline docs, type checking).

## Before You Begin

**Prerequisites**: Chapter 74 (async patterns for streaming), Chapter 75 (HTTP client patterns). Your Part 7 FastAPI AI backend should be running.

**What you'll need**: Zod installed (`npm install zod`), your FastAPI backend URL.

---

## What You'll Learn

### SDK Architecture (Lessons 1-2)
- **SDK Design Patterns**: Centralized HTTP, abstraction layers, avoiding `any`, cross-runtime compatibility
- **Zod for Schema Validation**: Runtime validation that generates TypeScript types, safeParse for error handling

### AI SDK Patterns (Lessons 3-4)
- **OpenAI/Anthropic SDK Patterns**: How official SDKs handle streaming, tool calls, message accumulation
- **Vercel AI SDK 5**: streamText, generateObject, useChat hook, Agent class for agentic patterns

### Advanced Integration (Lessons 5-6)
- **MCP TypeScript SDK**: Server implementation, Streamable HTTP transport, session management
- **tRPC for Internal APIs**: End-to-end type safety without code generation, React/Next.js integration

---

## Why Type-Safe SDKs Matter

Consider the difference:

**Without SDK (raw fetch)**:
```typescript
const response = await fetch("/api/chat", {
  method: "POST",
  body: JSON.stringify({ messages, model: "gpt-4" }),
});
const data = await response.json(); // What shape is this?
console.log(data.choices[0].message.content); // Hope it exists!
```

**With type-safe SDK**:
```typescript
const response = await sdk.chat.create({
  messages,
  model: "gpt-4",
});
// TypeScript knows: response.choices[0].message.content is string
// Zod validated at runtime: guaranteed to match schema
console.log(response.choices[0].message.content);
```

The SDK provides compile-time type checking AND runtime validation—catching both developer mistakes and API changes.

---

## The Zod Advantage

Zod is the standard for TypeScript schema validation because it provides:

1. **Runtime validation**: Catch malformed API responses
2. **Type inference**: `z.infer<typeof schema>` generates TypeScript types
3. **Error messages**: Detailed validation failures for debugging
4. **Transforms**: Parse and transform data in one step

```typescript
import { z } from "zod";

// Define schema once
const ChatResponseSchema = z.object({
  id: z.string(),
  choices: z.array(z.object({
    message: z.object({
      role: z.enum(["assistant", "user", "system"]),
      content: z.string(),
    }),
    finish_reason: z.enum(["stop", "length", "tool_calls"]),
  })),
});

// Get TypeScript type automatically
type ChatResponse = z.infer<typeof ChatResponseSchema>;

// Validate at runtime
const result = ChatResponseSchema.safeParse(apiResponse);
if (!result.success) {
  console.error("API response changed:", result.error);
}
```

---

## Chapter Structure

| Lesson | Topic | Duration |
|--------|-------|----------|
| 1 | SDK Architecture Patterns | 25 min |
| 2 | Zod for Schema Validation | 25 min |
| 3 | OpenAI/Anthropic SDK Patterns | 25 min |
| 4 | Vercel AI SDK 5 Integration | 25 min |
| 5 | MCP TypeScript SDK | 25 min |
| 6 | tRPC for Internal APIs | 25 min |

**Total**: ~2.5 hours

---

## What You'll Build

**Capstone: FastAPI Agent SDK**

By the end of this chapter, you'll create a type-safe SDK for your Part 7 FastAPI AI backend:

```typescript
import { createAgentSDK } from "./agent-sdk";

const sdk = createAgentSDK({
  baseUrl: process.env.FASTAPI_URL,
  apiKey: process.env.AGENT_API_KEY,
});

// Streaming chat with type safety
const stream = await sdk.chat.stream({
  messages: [{ role: "user", content: "Analyze this data" }],
  tools: ["data_analyzer", "chart_generator"],
});

for await (const event of stream) {
  switch (event.type) {
    case "content":
      process.stdout.write(event.delta);
      break;
    case "tool_call":
      console.log(`Calling ${event.name}...`);
      break;
    case "tool_result":
      console.log(`Result: ${JSON.stringify(event.result)}`);
      break;
    case "done":
      console.log(`\nTokens: ${event.usage.total}`);
      break;
  }
}
```

Features you'll implement:
- Zod schemas for all API responses
- Streaming with async iterators
- Tool call handling
- Retry logic with exponential backoff
- Cross-runtime compatibility (Node, Deno, Bun, browser)

---

## What's Next

After building your SDK, **Chapter 77: Testing TypeScript for AI Applications** teaches you to write comprehensive tests with Vitest. You'll mock AI API responses, test streaming behavior, and implement contract testing to ensure your SDK stays in sync with your backend.

---

## Pedagogical Approach

This chapter uses **Layer 2 (AI Collaboration)** heavily:

- You understand HTTP from Chapter 75—AI helps you design SDK abstractions
- Real SDKs (OpenAI, Anthropic, Vercel) provide patterns to learn from
- AI helps translate patterns to your specific FastAPI backend

The Three Roles apply:
- **AI as Teacher**: Explains SDK design patterns from production codebases
- **AI as Student**: You describe your API structure, AI generates Zod schemas
- **AI as Co-Worker**: Collaborate on streaming implementation and error handling
