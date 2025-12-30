---
sidebar_position: 5
title: "Building Retrieval Chains"
description: "Transform vector similarity into intelligent answers using LangChain retrieval chains and LCEL composition"
keywords: [retrieval chain, RAG, LangChain, LCEL, QA chain, retriever pattern, document formatting]
chapter: 43
lesson: 5
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Retriever Pattern Implementation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student converts vector store to retriever and configures search parameters"

  - name: "LCEL Chain Composition"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student composes retrieval chains using pipe operators and lambda functions"

  - name: "Context Formatting for LLMs"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student implements document formatting functions that structure context for prompts"

  - name: "QA Chain Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student analyzes chain flow and debugs retrieval issues"

learning_objectives:
  - objective: "Implement the retriever pattern using vector_store.as_retriever() with search configuration"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Code produces working retriever that returns relevant documents"

  - objective: "Build a complete QA chain that retrieves context and generates answers"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Chain returns coherent answers grounded in retrieved documents"

  - objective: "Compose chains using LCEL with proper document formatting"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates custom chains with format_docs function and pipe operators"

  - objective: "Analyze the flow of data through retrieval chains for debugging"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can trace query through retriever, formatter, prompt, and LLM"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (retriever pattern, format_docs, LCEL pipes, QA chain, chain invocation) within B1 limit of 7-10"

differentiation:
  extension_for_advanced: "Implement MMR retrieval for diversity, add source citations to responses"
  remedial_for_struggling: "Focus on the basic QA chain pattern before exploring LCEL composition details"
---

# Building Retrieval Chains

You have a vector store. You can find similar documents. But similarity isn't understanding.

When a user asks "How do I mark a task as complete?", they don't want a list of documents. They want an answer. This is where retrieval chains transform raw vector similarity into intelligent responses.

The pattern is straightforward: retrieve relevant documents, format them as context, and let an LLM generate a grounded answer. LangChain's Expression Language (LCEL) makes this composition elegant and powerful.

---

## The Retrieval Chain Flow

Every retrieval chain follows this data flow:

```
┌─────────────────────────────────────────────────────────────────┐
│                    RETRIEVAL CHAIN FLOW                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   USER QUERY                                                    │
│       │                                                         │
│       ▼                                                         │
│   ┌──────────┐    Top-k docs    ┌──────────────┐               │
│   │ Retriever │ ──────────────► │ Format Docs  │               │
│   └──────────┘                  └──────────────┘               │
│       │                              │                          │
│       │ (vector search)              │ (concatenate)            │
│       ▼                              ▼                          │
│   ┌──────────┐                 ┌──────────────┐                │
│   │  Qdrant  │                 │    Context   │                │
│   └──────────┘                 │    String    │                │
│                                └──────────────┘                │
│                                      │                          │
│                                      ▼                          │
│                              ┌──────────────┐                  │
│                              │    Prompt    │                  │
│                              │   Template   │                  │
│                              └──────────────┘                  │
│                                      │                          │
│                                      ▼                          │
│                              ┌──────────────┐                  │
│                              │     LLM      │                  │
│                              └──────────────┘                  │
│                                      │                          │
│                                      ▼                          │
│                              ┌──────────────┐                  │
│                              │   Answer     │                  │
│                              └──────────────┘                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Each component has a single responsibility. The retriever finds relevant documents. The formatter structures them for the LLM. The prompt frames the question. The LLM synthesizes an answer. This modularity means you can swap any component without rewriting the chain.

---

## The Retriever Pattern

A retriever abstracts document search into a simple interface. Instead of calling `similarity_search` directly, you get an object that works seamlessly in chains.

```python
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

# Assume vector_store exists from previous lesson
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="task_docs",
    url="http://localhost:6333",
)

# Convert to retriever with search configuration
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}  # Return top 4 documents
)

# Use directly
docs = retriever.invoke("How do I create a task?")
print(f"Retrieved {len(docs)} documents")
for doc in docs:
    print(f"- {doc.page_content[:100]}...")
```

**Output:**
```
Retrieved 4 documents
- Task creation requires a title and optional description. Use POST /tasks with a JSON body contain...
- The Task model accepts title (required), description (optional), and priority (default: medium)...
- Creating tasks programmatically: Call the create_task function with TaskCreate schema validatio...
- Example task creation: {"title": "Deploy API", "description": "Deploy to production server"}...
```

The `search_kwargs` parameter controls how many documents to retrieve. Start with 4 and adjust based on your context window and answer quality.

### Search Types

LangChain retrievers support different search strategies:

| Search Type | When to Use | Trade-off |
|-------------|-------------|-----------|
| `similarity` | Default choice, most similar docs | May return redundant content |
| `mmr` | Need diverse perspectives | Slower, balances relevance/diversity |
| `similarity_score_threshold` | Want only highly relevant docs | May return fewer than k docs |

```python
# MMR retriever for diverse results
retriever_mmr = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,           # Final number of docs
        "fetch_k": 20,    # Fetch more, then select diverse subset
        "lambda_mult": 0.5,  # Balance relevance (1) vs diversity (0)
    }
)
```

---

## Formatting Documents for Context

Raw documents need structure before feeding into an LLM. The `format_docs` function concatenates retrieved documents into a single context string.

```python
def format_docs(docs):
    """Convert retrieved documents to a context string."""
    return "\n\n".join(doc.page_content for doc in docs)

# Test the formatter
docs = retriever.invoke("task completion")
context = format_docs(docs)
print(context[:500])
```

**Output:**
```
Task completion requires updating the status field to 'completed'. Use PATCH /tasks/{task_id} with {"status": "completed"} in the request body.

The complete_task function handles completion logic: validates task exists, updates status, records completion timestamp, and triggers any configured webhooks.

Tasks can only be marked complete if they exist and have status 'pending' or 'in_progress'. Attempting to complete an already-completed task returns 400 Bad Request.

Important: Task completion is i...
```

For richer context, include metadata:

```python
def format_docs_with_source(docs):
    """Include source information in context."""
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        formatted.append(f"[Source {i}: {source}]\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)
```

**Output:**
```
[Source 1: api_endpoints.md]
Task completion requires updating the status field to 'completed'. Use PATCH /tasks/{task_id}...

---

[Source 2: functions.md]
The complete_task function handles completion logic: validates task exists, updates status...
```

---

## Building a Simple QA Chain

Now combine retriever, formatter, prompt, and LLM into a complete chain:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# LLM for answer generation
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Prompt that frames the question with context
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context:

{context}

Question: {question}

Provide a concise, accurate answer. If the context doesn't contain enough information, say so.
""")

# The complete chain using LCEL
chain = (
    {"context": retriever | format_docs, "question": lambda x: x}
    | prompt
    | llm
)

# Invoke the chain
response = chain.invoke("How do I mark a task as complete?")
print(response.content)
```

**Output:**
```
To mark a task as complete, use PATCH /tasks/{task_id} with the request body {"status": "completed"}.

The task must exist and have a status of 'pending' or 'in_progress'. Attempting to complete an already-completed task returns a 400 Bad Request error.

The completion operation validates the task, updates the status, records a completion timestamp, and triggers any configured webhooks.
```

The answer synthesizes information from multiple documents into a coherent response grounded in the retrieved context.

### Understanding the LCEL Pipe Syntax

The chain uses LangChain Expression Language (LCEL). Let's break it down:

```python
# This creates a RunnableParallel that processes inputs
{
    "context": retriever | format_docs,  # Pipe retriever output through formatter
    "question": lambda x: x               # Pass question through unchanged
}
# Output: {"context": "formatted docs...", "question": "user question"}

| prompt   # Template fills {context} and {question}
# Output: ChatPromptValue with formatted message

| llm      # LLM generates response
# Output: AIMessage with answer
```

The `|` operator chains components together. Data flows left to right. The dictionary creates parallel branches that merge before the next step.

---

## Chain Variations

### Adding Output Parsing

Parse the LLM response into a structured format:

```python
from langchain_core.output_parsers import StrOutputParser

chain_with_parser = (
    {"context": retriever | format_docs, "question": lambda x: x}
    | prompt
    | llm
    | StrOutputParser()  # Extract just the text content
)

answer = chain_with_parser.invoke("What fields does a task have?")
print(answer)  # String, not AIMessage
```

**Output:**
```
A task has the following fields:
- title (required): The name of the task
- description (optional): Additional details about the task
- priority (default: medium): Can be low, medium, or high
- status: pending, in_progress, or completed
- created_at: Timestamp when task was created
- completed_at: Timestamp when task was completed (if applicable)
```

### Streaming Responses

For long answers, stream tokens as they generate:

```python
async def stream_answer(question: str):
    """Stream the answer token by token."""
    async for chunk in chain_with_parser.astream(question):
        print(chunk, end="", flush=True)
    print()  # Newline at end

# Usage
import asyncio
asyncio.run(stream_answer("Explain the task lifecycle"))
```

**Output (tokens appear progressively):**
```
A task moves through this lifecycle:
1. Created (pending) - Task exists but work hasn't started
2. In Progress - Work has begun
3. Completed - Task finished successfully
...
```

### Debugging: Inspect Chain Components

When answers seem wrong, inspect each step:

```python
# Step 1: Check what documents are retrieved
question = "How do I delete a task?"
docs = retriever.invoke(question)
print("=== RETRIEVED DOCUMENTS ===")
for i, doc in enumerate(docs):
    print(f"\n--- Doc {i+1} ---")
    print(doc.page_content[:200])
    print(f"Metadata: {doc.metadata}")

# Step 2: Check formatted context
context = format_docs(docs)
print("\n=== FORMATTED CONTEXT ===")
print(context[:500])

# Step 3: Check the prompt
filled_prompt = prompt.invoke({"context": context, "question": question})
print("\n=== FILLED PROMPT ===")
print(filled_prompt.to_string()[:500])
```

**Output:**
```
=== RETRIEVED DOCUMENTS ===

--- Doc 1 ---
DELETE /tasks/{task_id} removes a task permanently. Returns 204 No Content on success. Returns 404 Not Found if task doesn't exist.
Metadata: {'source': 'api_endpoints.md', 'section': 'DELETE'}

--- Doc 2 ---
The delete_task function validates the task exists, removes it from the database, and returns...
Metadata: {'source': 'functions.md', 'section': 'deletion'}

=== FORMATTED CONTEXT ===
DELETE /tasks/{task_id} removes a task permanently. Returns 204 No Content on success...

=== FILLED PROMPT ===
Answer the question based only on the following context:

DELETE /tasks/{task_id} removes a task permanently...

Question: How do I delete a task?
...
```

This trace reveals issues: Are the right documents retrieved? Is context properly formatted? Does the prompt make sense?

---

## Common Mistakes to Avoid

### Mistake 1: Forgetting to Format Documents

```python
# WRONG: Documents aren't strings
chain_broken = (
    {"context": retriever, "question": lambda x: x}  # retriever returns List[Document]
    | prompt  # Prompt expects string for {context}
    | llm
)
# Error: Prompt template can't format list of documents
```

**Fix:** Always pipe retriever through a formatter:

```python
# CORRECT: Format documents to string
chain_working = (
    {"context": retriever | format_docs, "question": lambda x: x}
    | prompt
    | llm
)
```

### Mistake 2: Too Few or Too Many Documents

```python
# Too few: May miss relevant information
retriever_minimal = vector_store.as_retriever(search_kwargs={"k": 1})

# Too many: Overwhelms context, confuses LLM, wastes tokens
retriever_excessive = vector_store.as_retriever(search_kwargs={"k": 50})
```

**Guideline:** Start with k=4, adjust based on:
- Answer quality (missing info? increase k)
- Token costs (too expensive? decrease k)
- Response coherence (confused answers? decrease k)

### Mistake 3: Ignoring the Question in Context

```python
# WRONG: Question lost
bad_chain = (
    {"context": retriever | format_docs}  # Where's the question?
    | prompt  # Prompt needs {question}!
    | llm
)
```

**Fix:** Always pass the question through:

```python
# CORRECT: Question flows to prompt
good_chain = (
    {"context": retriever | format_docs, "question": lambda x: x}
    | prompt
    | llm
)
```

---

## Putting It Together: Task API QA Chain

Here's a complete implementation for your Task API documentation:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# Initialize components
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="task_api_docs",
    url="http://localhost:6333",
)

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4, "fetch_k": 10}
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant for the Task API. Answer questions based only on the provided documentation.

Documentation:
{context}

Question: {question}

Provide a clear, accurate answer. Include relevant code examples when helpful.
If the documentation doesn't cover this topic, say so.
""")

# Build the chain
qa_chain = (
    {"context": retriever | format_docs, "question": lambda x: x}
    | prompt
    | llm
    | StrOutputParser()
)

# Test it
questions = [
    "How do I create a task?",
    "What's the difference between pending and in_progress?",
    "How do I filter tasks by priority?",
]

for q in questions:
    print(f"\n**Q: {q}**")
    print(qa_chain.invoke(q))
    print("-" * 50)
```

**Output:**
```
**Q: How do I create a task?**
To create a task, send a POST request to /tasks with a JSON body:

```json
{
    "title": "Your task title",
    "description": "Optional description",
    "priority": "medium"
}
```

The title field is required. Description is optional. Priority defaults to "medium" if not specified (can be "low", "medium", or "high").

The API returns the created task with its assigned ID and timestamps.
--------------------------------------------------

**Q: What's the difference between pending and in_progress?**
The difference is:

- **pending**: Task has been created but work hasn't started yet. This is the initial status for all new tasks.
- **in_progress**: Work has begun on the task but isn't complete yet.

You can update a task's status using PATCH /tasks/{task_id} with {"status": "in_progress"}.
--------------------------------------------------

**Q: How do I filter tasks by priority?**
Use the priority query parameter on the GET /tasks endpoint:

```
GET /tasks?priority=high
```

This returns only tasks with the specified priority level. You can combine with other filters:

```
GET /tasks?priority=high&status=pending
```

Valid priority values are: low, medium, high.
--------------------------------------------------
```

You now have an intelligent Q&A system over your Task API documentation. Users ask natural language questions; the chain retrieves relevant context and synthesizes accurate answers.

---

## Reflect on Your Skill

You built a `rag-deployment` skill in Lesson 0. Now test whether it handles retrieval chains.

### Test Your Skill

Ask your skill:

```
I have a Qdrant vector store with Task API documentation. Help me build a
retrieval chain that answers user questions about the API. I want to use
MMR for diversity and include source citations in responses.
```

### Identify Gaps

After reviewing the response:
- Does it show the `as_retriever()` pattern with search configuration?
- Does it include a document formatting function?
- Does it demonstrate LCEL chain composition?
- Does it explain how to debug chain issues?

### Improve Your Skill

If any gaps exist, update your skill:

```
Update my rag-deployment skill with retrieval chain patterns:
1. Retriever creation with search_type and search_kwargs
2. format_docs and format_docs_with_source functions
3. LCEL chain composition with parallel branches
4. Debugging techniques for tracing data through chains
5. Common mistakes (forgetting formatter, wrong k values)
```

Your skill should now help you build retrieval chains that transform similarity search into intelligent, grounded answers.

---

## Try With AI

### Prompt 1: Customize Your Prompt Template

```
Help me improve this RAG prompt template for the Task API. I want the
assistant to:
1. Suggest related tasks when answering
2. Include code examples in Python and curl
3. Warn about common mistakes

Current template:
"""
Answer based on the context: {context}
Question: {question}
"""

Show me an improved template and explain why each section helps.
```

**What you're learning:** Prompt engineering for RAG systems. The quality of answers depends heavily on how you frame the question and structure the context.

### Prompt 2: Build a Conversational Chain

```
I want my QA chain to remember previous questions in the conversation.
For example:
- User: "How do I create a task?"
- Assistant: [answers]
- User: "What about with high priority?"
- Assistant: [should understand this relates to task creation]

Help me extend my chain with conversation memory. Use LangChain patterns.
```

**What you're learning:** Stateful chains maintain context across multiple questions, enabling natural multi-turn conversations.

### Prompt 3: Handle No-Answer Cases

```
Sometimes my retrieval chain makes up answers when the documentation
doesn't cover a topic. For example, asking about "task archiving" returns
plausible but fabricated information.

Help me:
1. Detect when retrieved documents aren't relevant
2. Return "I don't have information about that" gracefully
3. Suggest what topics the documentation DOES cover

Show code for implementing this guardrail.
```

**What you're learning:** Grounding and hallucination prevention. Production RAG systems need safeguards when context doesn't support an answer.

**Safety Note:** Retrieval chains can expose sensitive information from indexed documents. Before deploying, audit what's in your vector store and consider access controls for who can query it.
---
sidebar_position: 5
title: "RAG with OpenAI Agents SDK"
description: "Transform vector similarity into intelligent answers by combining LangChain retrieval with OpenAI Agents SDK"
keywords: [RAG, retrieval, OpenAI Agents SDK, LangChain, Qdrant, function tool, agent]
chapter: 43
lesson: 5
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "RAG Tool Implementation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student creates a retrieval tool using LangChain and integrates it with an OpenAI agent"

  - name: "Agent-Based RAG Pattern"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student builds an agent that uses retrieval tools to answer questions"

  - name: "Context Formatting for Agents"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student implements document formatting that provides useful context to the agent"

  - name: "RAG Agent Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student analyzes retrieval results and debugs agent behavior"

learning_objectives:
  - objective: "Create a retrieval function tool that wraps LangChain similarity search"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Tool returns formatted context from vector store queries"

  - objective: "Build an OpenAI agent that uses retrieval tools for grounded answers"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Agent answers questions using retrieved context"

  - objective: "Format retrieved documents as useful context for agents"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates format functions that preserve metadata and structure"

  - objective: "Debug RAG agent behavior by inspecting retrieval and responses"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student traces query through retrieval tool to agent response"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (function_tool, Agent with tools, retrieval tool pattern, context formatting) within B1 limit of 7-10"

differentiation:
  extension_for_advanced: "Add multiple retrieval tools for different document collections, implement source citations"
  remedial_for_struggling: "Focus on single retrieval tool pattern before adding complexity"
---

# RAG with OpenAI Agents SDK

You have a vector store. You can find similar documents. But similarity isn't understanding.

When a user asks "How do I mark a task as complete?", they don't want a list of documents. They want an answer. This is where we combine LangChain's retrieval capabilities with the OpenAI Agents SDK to build intelligent RAG systems.

The architecture is clean:
- **LangChain**: Document loading, embeddings, vector store, similarity search
- **OpenAI Agents SDK**: Agent orchestration, LLM calls, tool use

You learned the Agents SDK in Chapter 34. Now you'll give your agents the power of retrieval.

---

## The RAG Agent Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    RAG AGENT ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   USER QUERY                                                    │
│       │                                                         │
│       ▼                                                         │
│   ┌──────────────────────────────────────────┐                 │
│   │           OPENAI AGENTS SDK              │                 │
│   │  ┌──────────────────────────────────┐   │                 │
│   │  │            Agent                  │   │                 │
│   │  │  - instructions                   │   │                 │
│   │  │  - tools: [search_docs]           │   │                 │
│   │  └──────────────────────────────────┘   │                 │
│   │              │                           │                 │
│   │              │ calls tool                │                 │
│   │              ▼                           │                 │
│   │  ┌──────────────────────────────────┐   │                 │
│   │  │     @function_tool                │   │                 │
│   │  │     search_docs(query)            │   │                 │
│   │  └──────────────────────────────────┘   │                 │
│   └──────────────────────────────────────────┘                 │
│                  │                                              │
│                  │ calls LangChain                              │
│                  ▼                                              │
│   ┌──────────────────────────────────────────┐                 │
│   │             LANGCHAIN                     │                 │
│   │  ┌────────────┐    ┌────────────────┐   │                 │
│   │  │ Embeddings │───►│ QdrantVectorStore│   │                 │
│   │  └────────────┘    └────────────────┘   │                 │
│   │                           │              │                 │
│   │                           │ similarity   │                 │
│   │                           │ search       │                 │
│   │                           ▼              │                 │
│   │                    ┌────────────┐        │                 │
│   │                    │   Qdrant   │        │                 │
│   │                    └────────────┘        │                 │
│   └──────────────────────────────────────────┘                 │
│                  │                                              │
│                  │ returns formatted docs                       │
│                  ▼                                              │
│   ┌──────────────────────────────────────────┐                 │
│   │  Agent generates answer with context     │                 │
│   └──────────────────────────────────────────┘                 │
│                  │                                              │
│                  ▼                                              │
│              ANSWER                                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Each layer does what it's best at. LangChain handles the complex embedding and vector search operations. The Agents SDK orchestrates the conversation and decides when to retrieve information.

---

## Creating a Retrieval Tool

The first step is wrapping your LangChain retrieval in a function tool that the agent can call.

```python
from agents import function_tool
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

# Initialize LangChain components (from Lesson 4)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="task_docs",
    url="http://localhost:6333",
)


def format_docs(docs) -> str:
    """Convert retrieved documents to a context string."""
    if not docs:
        return "No relevant documents found."

    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        formatted.append(f"[Source {i}: {source}]\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)


@function_tool
def search_docs(query: str) -> str:
    """Search the documentation for information relevant to the query.

    Args:
        query: The search query to find relevant documentation.
    """
    docs = vector_store.similarity_search(query, k=4)
    return format_docs(docs)
```

**Output (testing the tool directly):**
```python
>>> result = search_docs("How do I complete a task?")
>>> print(result)
[Source 1: api_endpoints.md]
Task completion requires updating the status field to 'completed'.
Use PATCH /tasks/{task_id} with {"status": "completed"} in the request body.

---

[Source 2: functions.md]
The complete_task function handles completion logic: validates task exists,
updates status, records completion timestamp, and triggers any configured webhooks.
```

The `@function_tool` decorator from the Agents SDK makes this function callable by your agent. The docstring becomes the tool description that helps the agent understand when to use it.

---

## Building the RAG Agent

Now create an agent that uses the retrieval tool:

```python
from agents import Agent, Runner

# Create the RAG agent
rag_agent = Agent(
    name="TaskAPIAssistant",
    instructions="""You are a helpful assistant for the Task API.

When users ask questions about the API:
1. Use the search_docs tool to find relevant documentation
2. Answer based ONLY on the retrieved information
3. If the documentation doesn't cover the topic, say so clearly
4. Include code examples when helpful

Never make up information that isn't in the retrieved documents.""",
    tools=[search_docs],
)

# Run the agent
result = Runner.run_sync(rag_agent, "How do I mark a task as complete?")
print(result.final_output)
```

**Output:**
```
To mark a task as complete, send a PATCH request to `/tasks/{task_id}` with the
following request body:

```json
{"status": "completed"}
```

The task must exist and have a status of 'pending' or 'in_progress'. The API will:
- Validate the task exists
- Update the status to 'completed'
- Record a completion timestamp
- Trigger any configured webhooks

Attempting to complete an already-completed task returns a 400 Bad Request error.
```

The agent automatically called `search_docs`, retrieved relevant documentation, and synthesized a clear answer.

---

## Search Configuration

Control how many documents to retrieve and how to rank them:

```python
@function_tool
def search_docs_configured(query: str, num_results: int = 4) -> str:
    """Search documentation with configurable result count.

    Args:
        query: The search query.
        num_results: Number of documents to retrieve (1-10).
    """
    k = min(max(num_results, 1), 10)  # Clamp between 1 and 10
    docs = vector_store.similarity_search(query, k=k)
    return format_docs(docs)
```

For diverse results, use MMR (Maximal Marginal Relevance):

```python
@function_tool
def search_docs_diverse(query: str) -> str:
    """Search for diverse documentation covering different aspects.

    Args:
        query: The search query.
    """
    # MMR balances relevance with diversity
    docs = vector_store.max_marginal_relevance_search(
        query,
        k=4,           # Return 4 documents
        fetch_k=20,    # Consider top 20 candidates
        lambda_mult=0.5,  # Balance relevance (1) vs diversity (0)
    )
    return format_docs(docs)
```

**When to use each:**

| Method | Use Case | Trade-off |
|--------|----------|-----------|
| `similarity_search` | General queries, focused answers | May return redundant content |
| `max_marginal_relevance_search` | Need breadth, multiple perspectives | Slower, may include less relevant docs |

---

## Adding Relevance Scores

Sometimes you want to know how confident the retrieval is:

```python
@function_tool
def search_docs_with_scores(query: str) -> str:
    """Search documentation and include relevance scores.

    Args:
        query: The search query.
    """
    results = vector_store.similarity_search_with_score(query, k=4)

    if not results:
        return "No relevant documents found."

    formatted = []
    for i, (doc, score) in enumerate(results, 1):
        source = doc.metadata.get("source", "unknown")
        # Lower score = more similar for cosine distance
        relevance = f"(relevance: {1 - score:.2f})"
        formatted.append(f"[Source {i}: {source}] {relevance}\n{doc.page_content}")

    return "\n\n---\n\n".join(formatted)
```

**Output:**
```python
>>> print(search_docs_with_scores("task priority"))
[Source 1: task_model.md] (relevance: 0.89)
Tasks have a priority field that accepts 'low', 'medium', or 'high'.
Default value is 'medium' if not specified during creation.

---

[Source 2: api_endpoints.md] (relevance: 0.76)
Filter tasks by priority using GET /tasks?priority=high...
```

The agent can use these scores to assess confidence and potentially search again if relevance is low.

---

## Multiple Retrieval Tools

Real applications often have multiple document collections. Give your agent specialized tools:

```python
# Assume we have multiple vector stores
api_docs_store = QdrantVectorStore.from_existing_collection(...)
tutorials_store = QdrantVectorStore.from_existing_collection(...)
faq_store = QdrantVectorStore.from_existing_collection(...)


@function_tool
def search_api_docs(query: str) -> str:
    """Search the API reference documentation.

    Args:
        query: Technical query about API endpoints, schemas, or parameters.
    """
    docs = api_docs_store.similarity_search(query, k=4)
    return format_docs(docs)


@function_tool
def search_tutorials(query: str) -> str:
    """Search tutorials and how-to guides.

    Args:
        query: Query about how to accomplish a task or workflow.
    """
    docs = tutorials_store.similarity_search(query, k=3)
    return format_docs(docs)


@function_tool
def search_faq(query: str) -> str:
    """Search frequently asked questions.

    Args:
        query: Common question or troubleshooting query.
    """
    docs = faq_store.similarity_search(query, k=3)
    return format_docs(docs)


# Agent with multiple retrieval tools
multi_rag_agent = Agent(
    name="TaskAPIAssistant",
    instructions="""You help users with the Task API.

Available search tools:
- search_api_docs: Technical reference (endpoints, schemas, parameters)
- search_tutorials: Step-by-step guides and workflows
- search_faq: Common questions and troubleshooting

Choose the most appropriate tool based on the question type.
You can use multiple tools if needed for comprehensive answers.""",
    tools=[search_api_docs, search_tutorials, search_faq],
)
```

The agent learns to route queries to the appropriate knowledge base based on the tool descriptions.

---

## Conversation Memory with RAG

The Agents SDK handles conversation memory automatically with sessions:

```python
from agents import Agent, Runner, SQLiteSession

rag_agent = Agent(
    name="TaskAPIAssistant",
    instructions="""You help with the Task API.
Use search_docs to find information. Remember the conversation context.""",
    tools=[search_docs],
)

# Create a persistent session
session = SQLiteSession("user_123", "conversations.db")

# First question
result1 = Runner.run_sync(
    rag_agent,
    "How do I create a task?",
    session=session
)
print("Q1:", result1.final_output)

# Follow-up question (agent remembers context)
result2 = Runner.run_sync(
    rag_agent,
    "What about with high priority?",
    session=session
)
print("Q2:", result2.final_output)
```

**Output:**
```
Q1: To create a task, send a POST request to /tasks with:
```json
{
    "title": "Your task title",
    "description": "Optional description"
}
```
The title field is required. Description is optional.

Q2: To create a task with high priority, include the priority field:
```json
{
    "title": "Urgent task",
    "priority": "high"
}
```
Valid priority values are: low, medium, high. Default is medium.
```

The agent understood "What about with high priority?" relates to task creation from the previous turn.

---

## Debugging RAG Agents

When answers seem wrong, trace the retrieval:

```python
@function_tool
def search_docs_debug(query: str) -> str:
    """Search documentation with debug output.

    Args:
        query: The search query.
    """
    print(f"🔍 Searching for: {query}")

    docs = vector_store.similarity_search_with_score(query, k=4)

    print(f"📚 Found {len(docs)} documents:")
    for i, (doc, score) in enumerate(docs, 1):
        print(f"  {i}. Score: {score:.3f} | Source: {doc.metadata.get('source', 'unknown')}")
        print(f"     Preview: {doc.page_content[:100]}...")

    return format_docs([doc for doc, _ in docs])


# Test with debug tool
debug_agent = Agent(
    name="DebugAssistant",
    instructions="Search docs to answer questions.",
    tools=[search_docs_debug],
)

result = Runner.run_sync(debug_agent, "How do I delete a task?")
```

**Output:**
```
🔍 Searching for: How do I delete a task?
📚 Found 4 documents:
  1. Score: 0.234 | Source: api_endpoints.md
     Preview: DELETE /tasks/{task_id} removes a task permanently. Returns 204 No Content on success...
  2. Score: 0.412 | Source: functions.md
     Preview: The delete_task function validates the task exists, removes it from the database...
  3. Score: 0.523 | Source: api_endpoints.md
     Preview: Task lifecycle includes creation, updates, and optional deletion...
  4. Score: 0.678 | Source: best_practices.md
     Preview: Consider soft deletes instead of permanent removal for audit trails...
```

This reveals what documents are being retrieved and their relevance scores, helping diagnose issues.

---

## Common Patterns

### Pattern 1: Guardrail for Low Relevance

```python
@function_tool
def search_docs_safe(query: str) -> str:
    """Search documentation, warn if results may be unreliable.

    Args:
        query: The search query.
    """
    results = vector_store.similarity_search_with_score(query, k=4)

    if not results:
        return "⚠️ NO DOCUMENTS FOUND. Cannot answer this question from documentation."

    # Check if best result is too dissimilar (high score = low similarity)
    best_score = results[0][1]
    if best_score > 0.5:  # Threshold depends on your data
        warning = "⚠️ LOW CONFIDENCE: Retrieved documents may not be relevant.\n\n"
    else:
        warning = ""

    return warning + format_docs([doc for doc, _ in results])
```

### Pattern 2: Structured Output

```python
from pydantic import BaseModel
from typing import List


class SourcedAnswer(BaseModel):
    answer: str
    sources: List[str]
    confidence: str  # "high", "medium", "low"


sourced_agent = Agent(
    name="TaskAPIAssistant",
    instructions="""Answer questions about the Task API.
Always cite your sources and indicate confidence level.""",
    tools=[search_docs],
    output_type=SourcedAnswer,
)

result = Runner.run_sync(sourced_agent, "How do I filter tasks?")
answer: SourcedAnswer = result.final_output
print(f"Answer: {answer.answer}")
print(f"Sources: {answer.sources}")
print(f"Confidence: {answer.confidence}")
```

**Output:**
```
Answer: Use query parameters on GET /tasks: ?status=pending, ?priority=high
Sources: ['api_endpoints.md', 'query_parameters.md']
Confidence: high
```

---

## Putting It Together

Here's a complete RAG agent implementation:

```python
from agents import Agent, Runner, function_tool, SQLiteSession
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

# === LangChain: Retrieval Layer ===
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="task_api_docs",
    url="http://localhost:6333",
)


def format_docs(docs) -> str:
    if not docs:
        return "No relevant documents found."
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        formatted.append(f"[{source}]\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)


@function_tool
def search_docs(query: str) -> str:
    """Search Task API documentation for relevant information.

    Args:
        query: What to search for in the documentation.
    """
    docs = vector_store.similarity_search(query, k=4)
    return format_docs(docs)


# === OpenAI Agents SDK: Intelligence Layer ===
task_api_agent = Agent(
    name="TaskAPIAssistant",
    instructions="""You are a helpful assistant for the Task API.

When answering questions:
1. ALWAYS use search_docs to find relevant information first
2. Base your answers ONLY on retrieved documentation
3. Include code examples when helpful (JSON for requests, curl commands)
4. If documentation doesn't cover the topic, clearly say so
5. Never fabricate information

Be concise but thorough. Cite sources when helpful.""",
    tools=[search_docs],
)


# === Usage ===
def ask_task_api(question: str, user_id: str = "default") -> str:
    """Ask a question about the Task API."""
    session = SQLiteSession(user_id, "task_api_conversations.db")
    result = Runner.run_sync(task_api_agent, question, session=session)
    return result.final_output


# Test it
questions = [
    "How do I create a task with high priority?",
    "What happens if I try to complete an already-completed task?",
    "How do I filter tasks by status?",
]

for q in questions:
    print(f"\n**Q: {q}**")
    print(ask_task_api(q))
    print("-" * 50)
```

This combines LangChain's retrieval with the Agents SDK's orchestration for a clean, powerful RAG system.

---

## Reflect on Your Skill

You built a `rag-deployment` skill in Lesson 0. Test whether it handles agent-based RAG.

### Test Your Skill

Ask your skill:

```
I have a Qdrant vector store with Task API documentation indexed via LangChain.
Help me build a RAG agent using the OpenAI Agents SDK that:
1. Has a search_docs tool wrapping similarity_search
2. Uses conversation memory with SQLiteSession
3. Returns structured responses with sources cited

Show the complete implementation.
```

### Identify Gaps

After reviewing the response:
- Does it show the `@function_tool` decorator pattern?
- Does it create an Agent with tools and instructions?
- Does it demonstrate session-based memory?
- Does it format documents with source metadata?

### Improve Your Skill

If gaps exist, update your skill:

```
Update my rag-deployment skill with OpenAI Agents SDK patterns:
1. @function_tool wrapping LangChain similarity_search
2. Agent creation with retrieval tools
3. SQLiteSession for conversation memory
4. Debug patterns for tracing retrieval
5. Structured output with SourcedAnswer
```

Your skill should now help you build RAG agents that combine LangChain retrieval with Agents SDK orchestration.

---

## Try With AI

### Prompt 1: Add Retrieval Filtering

```
My RAG agent uses search_docs to find Task API documentation.
I want to add filters so users can search specific sections:
- Only API endpoints
- Only tutorials
- Only a specific chapter

Help me modify my @function_tool to support optional filters
using LangChain's filter parameter with Qdrant.
```

**What you're learning:** Combining semantic search with metadata filters gives users more control over what knowledge the agent accesses.

### Prompt 2: Multi-Turn Refinement

```
Sometimes my RAG agent's first answer isn't quite right.
I want the agent to:
1. Search for initial information
2. If the user says "not quite" or asks for clarification
3. Automatically search again with a refined query

How do I structure my agent's instructions and tools to
support this iterative refinement pattern?
```

**What you're learning:** Agentic RAG patterns where the agent decides when to retrieve more information based on conversation flow.

### Prompt 3: Source Citations

```
I need my RAG agent to cite sources in its answers like:
"To create a task, use POST /tasks [1]. The title field is required [1][2]."

Where [1] and [2] reference the retrieved documents.

Help me:
1. Track which document each piece of information came from
2. Format citations in the agent's output
3. Add a "Sources" section at the end

Show the implementation.
```

**What you're learning:** Production RAG systems need citations for trust and verification. This pattern enables users to check the original sources.

**Safety Note:** RAG agents can expose sensitive information from indexed documents. Before deploying, audit what's in your vector store and implement access controls for who can query it.
