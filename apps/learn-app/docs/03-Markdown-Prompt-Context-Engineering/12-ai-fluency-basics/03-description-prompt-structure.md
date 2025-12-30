---
sidebar_position: 3
title: "Description: Prompt Structure & Clarity"
description: "Master Anthropic's 6 prompting techniques and the Product-Process-Performance framework to communicate effectively with AI systems"
keywords: [prompt engineering, AI fluency, Anthropic prompting, context engineering, action verbs, prompt structure]
chapter: 12
lesson: 3
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "Prompt Structure Design"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can structure prompts using the 6 prompting techniques and Product-Process-Performance framework to produce targeted AI outputs"

  - name: "Action Verb Selection"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can select appropriate action verbs (CREATE, DEBUG, REFACTOR, ANALYZE, etc.) to communicate intent precisely to AI systems"

  - name: "Constraint Specification"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can articulate MUST/MUST NOT rules that bound AI output to requirements"

  - name: "Prompt Quality Evaluation"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can identify what makes descriptions effective versus vague, and explain why clarity matters for AI output quality"

learning_objectives:
  - objective: "Apply Anthropic's 6 prompting techniques to structure effective prompts"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student rewrites vague prompts using all 6 techniques"

  - objective: "Structure prompts using the Product-Process-Performance framework"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student decomposes requirements into Product, Process, and Performance components"

  - objective: "Use action verbs to communicate clear intent"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student selects appropriate verbs from the action verb taxonomy for different task types"

  - objective: "Identify what makes descriptions effective versus vague"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student analyzes prompt pairs and explains why one produces better results"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (6 prompting techniques, PPP framework, action verbs, constraints, step decomposition, role/tone) within A2 limit (5-7 concepts)"

differentiation:
  extension_for_advanced: "Practice combining all 6 techniques in complex, multi-step prompts for production scenarios"
  remedial_for_struggling: "Focus on the two most impactful techniques (context and constraints) before adding others"
---

# Description: Prompt Structure & Clarity

You have decided *what* to delegate to AI. Now comes the harder question: *how* do you communicate your intent so clearly that AI delivers exactly what you need?

This is where most people fail. They write vague requests like "help me with this code" and wonder why AI produces generic, unhelpful responses. The problem is not AI capability. The problem is description quality. AI systems are remarkably capable when given clear direction, but they cannot read your mind. They respond to what you actually write, not what you meant to write.

Anthropic, the company behind Claude, has documented specific techniques that dramatically improve AI output quality. These are not vague suggestions. They are research-backed patterns that work consistently across different tasks and contexts. Master these six techniques, and you will communicate with AI as effectively as you communicate with your best colleagues.

## Claude 4.x: Explicit Instructions Matter More

Claude 4.x models (Sonnet 4.5, Haiku 4.5, Opus 4.5) are trained for **precise instruction following**. This is powerful but requires adjustment: behaviors that previous models would infer now need explicit requests.

### "Suggest" vs. "Make"

Claude 4.x takes your words literally:

| What You Say | What Claude Does |
|--------------|------------------|
| "Can you suggest some changes?" | Suggests changes (doesn't implement) |
| "Make these changes" | Implements the changes |
| "Help me improve this" | Provides advice (doesn't modify) |
| "Improve this code" | Modifies the code directly |

**The fix**: Use action verbs that match your intent. If you want implementation, say "implement," "create," or "change"---not "suggest," "help," or "consider."

### Requesting "Above and Beyond" Behavior

Previous Claude models would sometimes add helpful extras unprompted. Claude 4.x is more conservative. If you want thorough, creative, or expansive output, request it explicitly:

```
Less effective:
"Create an analytics dashboard"

More effective:
"Create an analytics dashboard. Include as many relevant features
and interactions as possible. Go beyond the basics to create a
fully-featured implementation."
```

### Scope Discipline

When you want focused, minimal output, add explicit constraints:

```
Implement EXACTLY and ONLY what is requested. No extra features,
no added components, no UX embellishments. Keep solutions simple
and focused on the specific requirement.
```

This prevents over-engineering---a common issue when AI tries to be helpful.

## The Cost of Vague Descriptions

Consider this common prompt:

```
Review my code
```

What does AI do with this? It has no idea what you want. Should it check for bugs? Suggest optimizations? Evaluate readability? Follow your team's style guide? Without direction, AI makes assumptions. Sometimes those assumptions align with your needs. Usually they do not.

Now consider:

```
Review this Python function for security vulnerabilities.
Focus specifically on input validation, SQL injection risks,
and authentication bypass opportunities. Flag any issues
with severity (critical/high/medium/low) and suggest
specific fixes with code examples.
```

This prompt will produce dramatically better results. Not because AI suddenly became smarter, but because you told it exactly what you needed.

**The principle**: AI output quality is bounded by description quality. Vague input produces vague output. Precise input produces precise output.

## Anthropic's 6 Prompting Techniques

Anthropic's research has identified six techniques that consistently improve AI performance. Each technique addresses a specific failure mode in AI communication.

### Technique 1: Give Context

**What it does**: Provides background information, situation, and constraints that AI needs to understand your task.

**Why it matters**: Without context, AI fills gaps with assumptions from its training data. Those assumptions may not match your specific situation.

**How to apply it**:

```
Context example:

I'm building a customer support chatbot for a healthcare company.
We handle sensitive patient data (HIPAA regulated). Our users
are primarily elderly patients who may not be tech-savvy.
The chatbot must never provide medical advice—only help with
appointment scheduling and general inquiries.

[Then state your actual request]
```

**What changes**: AI now understands the regulatory environment (HIPAA), the user demographic (elderly, not tech-savvy), and the hard constraints (no medical advice). Every response it generates will respect these boundaries.

### Technique 2: Show Examples

**What it does**: Provides sample inputs and expected outputs so AI understands exactly what format and style you want.

**Why it matters**: Describing output format in words is ambiguous. Showing examples is concrete.

**How to apply it**:

```
Example format:

INPUT: "What are the side effects of aspirin?"
OUTPUT: "I'm not able to provide medical advice. For questions
about medications, please consult your healthcare provider or
call our nurse hotline at 1-800-XXX-XXXX. I can help you
schedule an appointment if you'd like."

INPUT: "I need to reschedule my appointment"
OUTPUT: "I'd be happy to help you reschedule. What's your
patient ID or the phone number associated with your account?"
```

**What changes**: AI now has concrete patterns to follow. It knows the exact tone, format, and content structure you expect.

### Technique 3: Specify Constraints

**What it does**: Establishes explicit MUST and MUST NOT rules that bound AI output.

**Why it matters**: AI will explore the full space of possible responses unless you define boundaries. Constraints prevent unwanted behavior.

**How to apply it**:

```
MUST:
- Always verify patient identity before accessing records
- Use simple language (6th grade reading level)
- Provide phone numbers for human escalation

MUST NOT:
- Provide medical advice or medication information
- Access or display full patient records
- Promise specific appointment times before confirmation
```

**What changes**: AI treats these as hard rules, not suggestions. MUST constraints are always followed. MUST NOT constraints are never violated.

### Technique 4: Break Into Steps

**What it does**: Decomposes complex tasks into sequential steps that AI can execute one at a time.

**Why it matters**: Complex tasks with many requirements overwhelm AI attention. Breaking tasks into steps ensures each requirement gets addressed.

**How to apply it**:

```
Step 1: Parse the user's request to identify the appointment type
Step 2: Check the patient's eligibility for that appointment type
Step 3: Query available time slots within the next 2 weeks
Step 4: Present top 3 options with specific dates and times
Step 5: Confirm the patient's selection and send confirmation
```

**What changes**: AI executes each step methodically rather than trying to handle everything at once. Complex logic becomes manageable sequences.

### Technique 5: Ask AI to Think First

**What it does**: Requests that AI reason through the problem before producing output. This is called chain-of-thought reasoning.

**Why it matters**: For complex tasks, immediate answers are often wrong. Thinking through the problem first produces better results.

**How to apply it**:

```
Before suggesting a solution, analyze:
1. What is the user actually asking for?
2. What constraints apply to this situation?
3. What are the possible approaches?
4. What are the tradeoffs of each approach?
5. Which approach best fits the constraints?

Then provide your recommendation with reasoning.
```

**What changes**: AI produces reasoned responses rather than pattern-matched guesses. You can see its reasoning and catch errors before they become problems.

### Technique 6: Define Role and Tone

**What it does**: Establishes the perspective, expertise, and communication style AI should adopt.

**Why it matters**: The same information can be communicated many ways. Role and tone ensure the communication style matches your audience.

**How to apply it**:

```
Role: You are a patient care coordinator with 10 years of
experience helping elderly patients navigate healthcare systems.

Tone: Warm, patient, reassuring. Use simple language. Never
make patients feel rushed or stupid for asking questions.
Repeat important information. Always confirm understanding
before moving forward.
```

**What changes**: AI adopts the specified persona consistently. A "patient care coordinator" sounds different from a "technical support agent" even when providing similar information.

## The Product-Process-Performance Framework

While the 6 techniques tell you *what* to include, the Product-Process-Performance framework helps you organize your description around three key questions.

### Product: What Should the Output Be?

Define the deliverable. What exactly should AI produce?

| Component | Questions to Answer |
|-----------|-------------------|
| **Format** | Text? Code? JSON? Markdown? Table? |
| **Length** | One paragraph? Full document? Bullet points? |
| **Structure** | What sections? What order? What headings? |
| **Content** | What must be included? What should be excluded? |

**Example**:

```
Product:
A Python function that validates email addresses.
Return type: bool
No external dependencies allowed.
Include docstring with usage examples.
```

### Process: How Should AI Approach the Task?

Define the methodology. How should AI work through the problem?

| Component | Questions to Answer |
|-----------|-------------------|
| **Methodology** | What approach should be used? |
| **Order** | What should be done first, second, third? |
| **Reasoning** | Should AI explain its thinking? |
| **Iteration** | Should AI refine its output? |

**Example**:

```
Process:
1. First, list the RFC 5321 email format requirements
2. Then, implement validation for each requirement
3. Test against edge cases (international domains, plus addressing)
4. Refactor for readability
```

### Performance: What Quality Standards Apply?

Define success criteria. How will you evaluate the output?

| Component | Questions to Answer |
|-----------|-------------------|
| **Correctness** | What must be true for output to be correct? |
| **Completeness** | What coverage is required? |
| **Quality** | What standards apply (readability, performance, security)? |
| **Constraints** | What limits must be respected? |

**Example**:

```
Performance:
- Must pass all RFC 5321 compliance tests
- Must handle edge cases without crashing
- Must reject malformed input gracefully (no exceptions)
- Should complete validation in under 1ms for typical emails
```

## Action Verb Taxonomy

The verb you choose communicates your intent. Different verbs activate different AI behaviors.

| Verb | When to Use | Example |
|------|-------------|---------|
| **CREATE** | Generating new content from scratch | "Create a user authentication flow" |
| **DEBUG** | Finding and fixing errors | "Debug this failing API endpoint" |
| **REFACTOR** | Improving code structure without changing behavior | "Refactor for better readability" |
| **ANALYZE** | Examining patterns, causes, or implications | "Analyze this error log for root cause" |
| **OPTIMIZE** | Improving performance or efficiency | "Optimize this database query" |
| **EXPLAIN** | Teaching or clarifying concepts | "Explain how decorators work" |
| **VALIDATE** | Checking correctness against criteria | "Validate this config against our schema" |
| **COMPARE** | Examining similarities and differences | "Compare these two approaches" |

**Precision matters**: "Help me with this function" is vague. "Debug this function" tells AI exactly what you need.

## Putting It Together: Vague vs. Precise

Here is a real transformation from vague to precise:

**Vague prompt**:

```
Help me write a function for user registration
```

**Precise prompt using all 6 techniques**:

```
Context:
I'm building a SaaS application for small business owners.
Registration must be simple (< 30 seconds) but secure.
We store data in PostgreSQL and use bcrypt for passwords.

Product:
Create a Python function that handles user registration.

Process:
Step 1: Validate email format and check for existing account
Step 2: Validate password strength (min 8 chars, 1 uppercase, 1 number)
Step 3: Hash password with bcrypt (cost factor 12)
Step 4: Create user record with created_at timestamp
Step 5: Return success response with user ID (no password in response)

Performance:
MUST: Return clear error messages for validation failures
MUST: Handle database errors gracefully
MUST NOT: Expose password hash in any response
MUST NOT: Allow registration with disposable email domains

Examples:
- Valid registration: {"success": true, "user_id": "uuid"}
- Duplicate email: {"success": false, "error": "email_exists"}
- Weak password: {"success": false, "error": "password_too_weak"}

Role/Tone:
Write production-quality code with comprehensive docstrings.
Follow PEP 8 style guide. Include type hints.

Before implementing, verify: What validation edge cases exist
for email addresses and passwords in this context?
```

The second prompt will produce dramatically better code. Not because it is longer, but because it eliminates ambiguity. AI knows exactly what you need.

## Common Mistakes and Fixes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| No context | AI assumes generic situation | Add 2-3 sentences of background |
| Vague verbs | "Help me" could mean anything | Use specific action verbs |
| Missing constraints | AI explores unwanted possibilities | Add MUST/MUST NOT rules |
| Format not specified | AI guesses output structure | Show example output |
| Too many things at once | Attention diluted across requirements | Break into sequential steps |
| Implicit assumptions | AI cannot read your mind | Make all assumptions explicit |

## Verbosity Control

Claude 4.x models tend toward efficiency and may skip verbal summaries after tool calls. Control output length explicitly:

### Quantitative Guidelines

| Output Type | Target Length |
|-------------|---------------|
| Concise summary | 45-70 words |
| Explanation | 3-6 sentences |
| Complex analysis | ≤5 tagged bullets + 1 overview paragraph |
| Code review | Focus on critical issues first |

### Requesting Updates

If you want Claude to provide progress updates as it works:

```
After completing a task that involves tool use, provide a quick
summary of the work you've done.
```

### Structured Output for Complex Tasks

For multi-step tasks, request structured responses:

```
For complex responses, use this format:
- What changed: [specific files/components]
- Where: [locations affected]
- Risks: [potential issues]
- Next steps: [immediate actions]
- Open questions: [decisions needed]
```

This ensures you get actionable information without verbosity.

## Try With AI

Use your AI assistant (Claude, ChatGPT, or similar) to practice these techniques.

### Prompt 1: Transform a Vague Request

```
I have this vague prompt: "Fix my Python code that's not working"

Help me transform this into a precise prompt using all 6 of
Anthropic's prompting techniques:
1. Give context
2. Show examples
3. Specify constraints
4. Break into steps
5. Ask AI to think first
6. Define role/tone

Ask me clarifying questions first to understand what I'm
actually trying to accomplish. Then show me the transformed
prompt with each technique labeled.
```

**What you are practicing**: The full prompt transformation workflow. By having AI ask you questions, you will discover what information you typically omit.

### Prompt 2: Build a Product-Process-Performance Specification

```
I need to write a prompt for this task: [describe your real task]

Walk me through the Product-Process-Performance framework:
1. First, help me define the Product (what should be delivered)
2. Then, define the Process (how to approach the task)
3. Finally, define Performance (quality standards)

For each section, ask me questions until we have enough detail.
Then assemble the complete prompt specification.
```

**What you are practicing**: Systematic decomposition of requirements. This framework prevents you from leaving out critical information.

### Prompt 3: Action Verb Precision

```
I want to work with this code: [paste code or describe it]

But instead of me telling you what to do, help me choose
the right action verb. Present these options:

- CREATE: If I need something new built from scratch
- DEBUG: If something is broken and needs fixing
- REFACTOR: If it works but needs restructuring
- ANALYZE: If I need to understand what's happening
- OPTIMIZE: If it's slow and needs performance improvement
- VALIDATE: If I need to check correctness

Ask me: What problem am I actually trying to solve?
Based on my answer, recommend the right verb and explain why.
```

**What you are practicing**: Precise intent communication. The right verb fundamentally changes how AI approaches your task.

### Safety Note

When practicing prompt engineering, start with non-critical tasks where mistakes have low consequences. As you build skill with these techniques, gradually apply them to more important work. Always review AI output carefully, especially for code that handles security, data, or money.
