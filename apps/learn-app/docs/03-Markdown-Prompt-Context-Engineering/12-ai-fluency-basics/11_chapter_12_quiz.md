---
sidebar_position: 11
title: "Chapter 12 Quiz: AI Fluency Basics"
sidebar_label: "Chapter Quiz"
---

# Chapter 12 Quiz: AI Fluency Basics

Test your understanding of the 4D Framework and AI Fluency concepts.

<Quiz
  title="Chapter 12: AI Fluency Basics Assessment"
  questions={[
    {
      question: "What are the four components of the AI Fluency Framework?",
      options: [
        "Design, Develop, Deploy, Debug",
        "Delegation, Description, Discernment, Diligence",
        "Define, Document, Demonstrate, Deliver",
        "Draft, Discuss, Decide, Deliver"
      ],
      correctOption: 1,
      explanation: "The 4D Framework represents the complete workflow for AI Fluency: deciding what AI should do (Delegation), communicating intent (Description), evaluating outputs (Discernment), and ensuring responsible use (Diligence).",
      source: "Lesson 1: What is AI Fluency?"
    },
    {
      question: "Which 'D' addresses the question 'Should AI handle this task?'",
      options: [
        "Description",
        "Discernment",
        "Delegation",
        "Diligence"
      ],
      correctOption: 2,
      explanation: "Delegation is about deciding what AI should do—and what it shouldn't. It involves assessing whether a task is appropriate for AI collaboration.",
      source: "Lesson 1: What is AI Fluency?"
    },
    {
      question: "What distinguishes AI Fluency from basic 'prompt engineering'?",
      options: [
        "AI Fluency focuses only on writing better prompts",
        "AI Fluency is a complete workflow including evaluation and responsibility",
        "Prompt engineering is more comprehensive than AI Fluency",
        "There is no difference"
      ],
      correctOption: 1,
      explanation: "Prompt engineering is just one part of AI Fluency (Description). AI Fluency encompasses the entire collaboration: deciding what to delegate, how to describe it, how to evaluate outputs, and how to be responsible about results.",
      source: "Lesson 1: What is AI Fluency?"
    },
    {
      question: "Which of these tasks is LEAST appropriate to delegate to AI?",
      options: [
        "Writing a first draft of documentation",
        "Making a final hiring decision for a candidate",
        "Summarizing meeting notes",
        "Generating test cases for a function"
      ],
      correctOption: 1,
      explanation: "High-stakes decisions involving people's lives and careers require human judgment, accountability, and ethical reasoning. AI can assist with research, but final decisions in sensitive areas should remain human.",
      source: "Lesson 2: Delegation"
    },
    {
      question: "What are the three modes of AI interaction?",
      options: [
        "Input, Processing, Output",
        "Automation, Augmentation, Agency",
        "Simple, Medium, Complex",
        "Text, Code, Image"
      ],
      correctOption: 1,
      explanation: "The three modes are: Automation (AI acts independently on routine tasks), Augmentation (AI assists humans who make final decisions), and Agency (AI takes initiative within defined boundaries).",
      source: "Lesson 2: Delegation"
    },
    {
      question: "Which of these is NOT one of the 6 prompting techniques?",
      options: [
        "Give context",
        "Show examples",
        "Use complex vocabulary",
        "Define role/tone"
      ],
      correctOption: 2,
      explanation: "The 6 techniques are: Give context, Show examples, Specify constraints, Break into steps, Ask AI to think first, and Define role/tone. Clear, simple language is preferred over complex vocabulary.",
      source: "Lesson 3: Description"
    },
    {
      question: "What does the 'Intent → Constraints → Success Criteria' structure accomplish?",
      options: [
        "Makes prompts longer",
        "Eliminates ambiguity in AI requests",
        "Speeds up AI response time",
        "Reduces token usage"
      ],
      correctOption: 1,
      explanation: "This structure ensures prompts are specifications, not vague requests. Intent defines WHAT, Constraints define MUST/MUST NOT rules, and Success Criteria define HOW you'll validate the output.",
      source: "Lesson 3: Description"
    },
    {
      question: "Which action verb is most appropriate for 'find out why my script crashes with error code 127'?",
      options: [
        "CREATE",
        "GENERATE",
        "DEBUG",
        "REFACTOR"
      ],
      correctOption: 2,
      explanation: "DEBUG is used when code crashes, throws errors, or produces wrong output. It signals you need to identify and fix a specific problem.",
      source: "Lesson 3: Description"
    },
    {
      question: "What is a typical context window size for modern AI coding assistants (like GPT-4o or Claude)?",
      options: [
        "8K tokens",
        "32K tokens",
        "128K-200K tokens",
        "10M tokens"
      ],
      correctOption: 2,
      explanation: "Most modern AI coding assistants have context windows between 128K and 200K tokens, with some models offering extended context up to 1-2M tokens.",
      source: "Lesson 4: Context Windows"
    },
    {
      question: "What is the approximate token-to-word ratio for estimating context usage?",
      options: [
        "1 word = 0.5 tokens",
        "1 word = 1-1.2 tokens",
        "1 word = 2 tokens",
        "1 word = 5 tokens"
      ],
      correctOption: 1,
      explanation: "For quick estimates: simple text ≈ 1 token per word, technical content with symbols ≈ 1.2 tokens per word.",
      source: "Lesson 4: Context Windows"
    },
    {
      question: "At what utilization percentage should you consider creating a checkpoint?",
      options: [
        "30-40%",
        "50-60%",
        "70-85%",
        "95-100%"
      ],
      correctOption: 2,
      explanation: "The Yellow Zone (70-85%) indicates you're approaching limits. Plan to create a checkpoint soon. Above 85% (Red Zone), you should create a checkpoint immediately.",
      source: "Lesson 4: Context Windows"
    },
    {
      question: "What triggers moving from Description to Discernment in the loop?",
      options: [
        "Running out of ideas",
        "AI generates output that needs evaluation",
        "The user gets tired",
        "Token limit is reached"
      ],
      correctOption: 1,
      explanation: "After you Describe (communicate intent) and AI generates output, you enter Discernment to evaluate whether the output meets your criteria. The loop continues until convergence.",
      source: "Lesson 6: The Description-Discernment Loop"
    },
    {
      question: "When should you stop iterating through the Description-Discernment loop?",
      options: [
        "After exactly 5 iterations",
        "When success criteria are met or returns diminish below 5%",
        "Only when the AI says it's done",
        "After 1 hour of work"
      ],
      correctOption: 1,
      explanation: "Termination criteria include: success criteria met, diminishing returns (< 5% improvement per iteration), or time budget exceeded.",
      source: "Lesson 6: The Description-Discernment Loop"
    },
    {
      question: "Which symptom indicates context degradation in the Red Zone?",
      options: [
        "AI suggests improvements you hadn't considered",
        "AI repeats the same suggestion multiple times",
        "AI asks clarifying questions",
        "AI provides detailed explanations"
      ],
      correctOption: 1,
      explanation: "Red Zone symptoms include: AI forgetting earlier patterns, repeating suggestions, generic responses, and asking you to re-explain information already provided.",
      source: "Lesson 7: Discernment"
    },
    {
      question: "According to Jake Heller, what accuracy does a typical first prompt achieve?",
      options: [
        "20%",
        "40%",
        "60%",
        "90%"
      ],
      correctOption: 2,
      explanation: "Jake Heller found that first prompts typically achieve 60% accuracy. Professional results (97%+) require iterative refinement over weeks. 'Most people quit too early.'",
      source: "Lesson 7: Discernment"
    },
    {
      question: "What are the three areas of Diligence in AI collaboration?",
      options: [
        "Speed, Quality, Cost",
        "Creation, Transparency, Deployment",
        "Input, Process, Output",
        "Planning, Execution, Review"
      ],
      correctOption: 1,
      explanation: "The three areas are: Creation (fact-checking, source verification, quality gates), Transparency (attribution, disclosure, documentation), and Deployment (impact assessment, monitoring, feedback loops).",
      source: "Lesson 9: Diligence"
    },
    {
      question: "When should you NOT use AI for a task?",
      options: [
        "When you're in a hurry",
        "When the task is repetitive",
        "When high-stakes decisions require human judgment",
        "When you're learning something new"
      ],
      correctOption: 2,
      explanation: "Avoid using AI for: high-stakes decisions requiring human judgment, situations with ethical ambiguity, tasks requiring emotional intelligence, and legal/medical advice without professional oversight.",
      source: "Lesson 9: Diligence"
    },
    {
      question: "What is the purpose of a project memory file (like CLAUDE.md)?",
      options: [
        "Store temporary session data",
        "Persist project rules and context across sessions",
        "Log errors and debugging information",
        "Track token usage"
      ],
      correctOption: 1,
      explanation: "Project memory files store project-specific rules, patterns, and decisions that should persist across multiple AI sessions, ensuring context carries over between conversations.",
      source: "Lesson 5: Progressive Loading & Memory Files"
    },
    {
      question: "What is the primary purpose of context isolation?",
      options: [
        "To save money on API calls",
        "To prevent pattern cross-contamination between unrelated tasks",
        "To make AI responses faster",
        "To increase context window size"
      ],
      correctOption: 1,
      explanation: "Context isolation (using separate sessions for unrelated work) prevents one task's patterns from interfering with another, maintaining quality across parallel workstreams.",
      source: "Lesson 8: Compression & Multi-Session"
    },
    {
      question: "Which loading phase includes files that AI always needs?",
      options: [
        "On-Demand",
        "Current Focus",
        "Foundation",
        "Extended"
      ],
      correctOption: 2,
      explanation: "The three-phase loading strategy includes: Foundation (what AI always needs—project rules, core patterns), Current Focus (active working files), and On-Demand (load when referenced).",
      source: "Lesson 5: Progressive Loading & Memory Files"
    }
  ]}
  questionsPerBatch={20}
/>
