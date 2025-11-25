### Core Concept
Git worktrees enable parallel feature specification by creating isolated workspaces sharing the same git history. This eliminates sequential bottlenecks, allowing 3+ agents to write specifications simultaneously while maintaining clean decomposition boundaries.

### Key Mental Models
- **Worktree Isolation**: Each worktree occupies its own branch with independent file systems but shared git repository, enabling true parallelization without merge conflicts during development
- **Decomposition Mindset**: Breaking a system into independent features upfront determines whether parallel work is feasible; poor decomposition creates hidden dependencies that emerge during integration
- **Feature Numbering Pattern**: Using consistent naming (feature-001-upload) across worktrees and specifications creates automatic context for AI agents and enables PHR auto-routing

### Critical Patterns
- **Branch detection optimization**: Modifying `/sp.specify` to detect existing feature branches prevents workflow friction when using worktrees with SpecKit Plus
- **Parallel PHR routing**: When 3 agents run `/sp.specify` simultaneously, PHR creation automatically routes to feature-specific directories based on branch context
- **Time tracking validation**: Measuring sequential vs. parallel execution (90 min → 30 min = 3x speedup) proves the methodology works before scaling to 5+ features

### AI Collaboration Keys
- AI can set up complex worktree structures through clear decomposition prompts without manual git command knowledge
- Agents executing `/sp.specify` in parallel need zero synchronization; isolation guarantees clean, independent specs
- AI validates worktree isolation through concrete verification commands that prove file independence

### Common Mistakes
- Skipping feature branch pre-creation and forcing `/sp.specify` to manage branches, adding complexity
- Unclear feature boundaries leading to hidden dependencies discovered late in integration
- Not tracking execution time, missing the concrete proof that parallelization works

### Connections
- **Builds on**: Understanding git fundamentals, `/sp.specify` workflow, decomposition principles from earlier chapters
- **Leads to**: Parallel planning in Lesson 2, integration strategy in Lesson 3, scaling analysis in Lesson 4
