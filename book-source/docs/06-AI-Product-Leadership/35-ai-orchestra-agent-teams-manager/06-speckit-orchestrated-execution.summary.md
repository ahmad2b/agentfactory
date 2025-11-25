### Core Concept
SpecKit Plus itself becomes the orchestrator through `/sp.specify`, `/sp.plan`, `/sp.tasks` generating coordination contracts, not bash scripts. Agents read specifications autonomously, execute independently, and notify via hooks—enabling 5-10 agent coordination without complex orchestration infrastructure.

### Key Mental Models
- **Specifications as Orchestration**: SpecKit commands generate the contracts that coordinate agent behavior; no separate orchestration layer needed
- **Phase-Based Execution**: Human designs (30 min), SpecKit plans (10 min), human spawns sessions (5 min), agents execute (2-3 hrs), human reviews (30 min)—total pipeline enables multi-agent creativity within defined boundaries
- **Strategic Oversight vs. Execution Management**: Shift from constant monitoring (3-agent scale) to validation checkpoints (5+ agent scale); human reviews results against contracts, not progress against timeline

### Critical Patterns
- **Contract Generation via /sp.specify**: Specifications explicitly define API contracts, data schemas, dependencies—agents read contract.md and implement to specification
- **Dependency Graph Extraction**: `/sp.plan` generates explicit dependency ordering showing which features can run in parallel, which must wait for prerequisites
- **Completion Hooks for Status**: Simple hooks notify orchestrator asynchronously when agents finish; orchestrator polls one status file instead of monitoring 5 terminals

### AI Collaboration Keys
- AI reads contract.md and executes autonomously; no supervision needed during 2-3 hour implementation windows
- Hooks enable AI agents to report completion without blocking on human review
- Strategic review becomes human's checkpoint: Did agents deliver on contracts? Are integration issues acceptable? What's next?

### Common Mistakes
- Adding complexity with bash orchestration scripts when specifications provide sufficient coordination
- Monitoring constantly instead of using hooks for async notification
- Not establishing clear contracts upfront, resulting in agents asking questions during execution

### Connections
- **Builds on**: Contract patterns from Lesson 5, scaling lessons from Lesson 4
- **Leads to**: Capstone project proving orchestration patterns work, portfolio narrative demonstrating team coordination capability
