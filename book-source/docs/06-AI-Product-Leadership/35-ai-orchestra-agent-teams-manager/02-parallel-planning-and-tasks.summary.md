### Core Concept
Running `/sp.plan` and `/sp.tasks` across 3 parallel worktrees demonstrates that clear specifications enable autonomous planning. Plan complexity becomes a decomposition quality indicator—balanced plans signal good feature boundaries; imbalanced plans reveal hidden complexity requiring redesign.

### Key Mental Models
- **Plan Quality as Decomposition Feedback**: A 12-page feature plan signals over-ambitious decomposition; balanced 2-4 page plans across features indicate healthy boundaries
- **Constitutional Alignment**: Shared constitution prevents quality drift across parallel planning sessions—without synchronous meetings, all agents make aligned decisions because they follow the same standards
- **N-Squared Dependency Management**: With 3 features, managing explicit dependencies is manual but tractable; this scales only with tight specifications (Lesson 4 proves the threshold)

### Critical Patterns
- **Dependency clarity in specifications**: Explicit dependency documentation (Feature B depends on upload format from Feature A) enables agents to plan without coordination
- **Integration point identification**: Tasks referencing specific data flow between features catch misalignments before implementation
- **Merge conflict prediction**: Unbalanced or unclear task lists that require constant cross-feature communication predict merge hell during integration

### AI Collaboration Keys
- AI produces balanced task lists automatically when specs define clear boundaries; vague specs produce divergent, conflicting task interpretations
- Completion hooks in parallel planning prevent blocking—agents report done asynchronously rather than waiting for orchestrator review
- AI can analyze plan complexity across 3 sessions to identify decomposition problems early

### Common Mistakes
- Assuming balanced effort means balanced parallelizability—a 3-hour feature taking 60 minutes vs. a 9-hour feature taking 90 minutes represents different complexity
- Not capturing explicit dependencies in tasks, leaving integration surprises for later
- Conflating task count with decomposition quality (50 small tasks ≠ good design if they have hidden dependencies)

### Connections
- **Builds on**: Worktree setup from Lesson 1, parallel specification execution, constitution alignment
- **Leads to**: Parallel implementation in Lesson 3, integration conflict analysis, scaling decisions in Lesson 4
