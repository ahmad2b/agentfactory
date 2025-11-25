### Core Concept
Integration contracts define exactly what each feature provides, what it depends on, and measurable acceptance criteria. Clear contracts enable autonomous agent execution without constant orchestrator supervision—vague contracts require continuous clarification, defeating parallelization gains.

### Key Mental Models
- **Explicitness Reduces Coordination**: Vague contracts generate clarifying questions and rework; precise contracts enable agents to implement independently and validation to be automated
- **Acceptance Criteria as Operational Definition**: Measurable criteria (API latency &lt;100ms, 80% test coverage) enable autonomous verification; vague criteria (good performance, robust error handling) require human judgment
- **Hook-Based Async Notification**: Completion hooks enable orchestrators to track progress without constant monitoring; agents fire hooks when done, orchestrator polls asynchronously

### Critical Patterns
- **Provides/Depends/Integration Points Structure**: Contracts explicitly list what features export, import, and how they integrate, eliminating interpretation ambiguity
- **Testable Acceptance Criteria**: Each criterion must be verifiable without human judgment (e.g., "Load test shows &lt;100ms response time" vs. "API should be fast")
- **Hook Orchestration at Scale**: At 5-7 agents, hooks replace manual status checking—orchestrator polls once instead of monitoring 5 terminals

### AI Collaboration Keys
- AI writes integration contracts that are unambiguous enough for other agents to implement without asking clarifying questions
- AI can evaluate contracts for ambiguity and suggest specificity improvements (e.g., replacing "handle errors robustly" with specific error codes and retry logic)
- Hooks enable AI agents to report completion autonomously, reducing orchestrator context-switching

### Common Mistakes
- Writing vague acceptance criteria that sound good but require judgment to verify (violates autonomy)
- Incomplete dependency documentation, leaving agents to discover integration requirements during implementation
- Not configuring hooks, forcing orchestrator to manually track progress across parallel sessions

### Connections
- **Builds on**: Scaling analysis from Lesson 4, understanding what breaks at 5+ features
- **Leads to**: Orchestration patterns in Lesson 6, creative independence through autonomous execution
