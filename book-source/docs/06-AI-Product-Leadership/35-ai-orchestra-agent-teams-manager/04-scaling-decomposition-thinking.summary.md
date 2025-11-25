### Core Concept
Scaling from 3 to 5+ features requires understanding N-squared communication complexity (3 features = 3 integration points; 5 features = 10 points; 10 features = 45 points). Manual coordination works at 3, becomes tedious at 5, becomes impossible at 10—specifications must become exponentially more precise to compensate.

### Key Mental Models
- **Communication Complexity (N²)**: Coordination overhead grows quadratically with feature count; this is why specifications matter exponentially more at scale
- **Decomposition Quality Indicators**: Tight specs, independent concerns, clear APIs, and modular architecture scale; implicit dependencies, shared code modifications, and circular dependencies break at larger scale
- **Bottleneck Analysis**: Cross-cutting concerns (logging, auth, monitoring) create unavoidable bottlenecks at 5+ features; must be designed as shared services upfront, not discovered during integration

### Critical Patterns
- **Red Flag Detection**: Unbalanced feature sizes (one feature 2x larger), heavy merge conflicts, circular dependencies, and cross-feature code changes are early warnings that decomposition won't scale
- **API-First Design**: Features communicate only through APIs, never through shared databases or shared code, eliminating hidden coupling that emerges at scale
- **Dependency Analysis**: Mapping all inter-feature dependencies and checking for cycles prevents integration chaos when scaling to 5-7 features

### AI Collaboration Keys
- AI can analyze retrospective data from 3-feature project to predict scaling breakpoints and identify which patterns (tight specs, clear APIs) transfer to larger systems
- AI calculates N-squared complexity to help orchestrators understand why 10-agent coordination requires fundamentally different tooling than 3-agent coordination
- AI evaluates decomposition retrospectives to extract reusable patterns for future projects

### Common Mistakes
- Assuming patterns that work at 3 features automatically scale to 5-7; they don't without explicit re-design
- Treating merge conflicts as implementation problems rather than decomposition feedback
- Not establishing shared services for cross-cutting concerns until integration chaos forces the redesign

### Connections
- **Builds on**: Integration experience from Lesson 3, metrics from all previous lessons
- **Leads to**: Contract-based coordination in Lesson 5, orchestration patterns in Lesson 6, capstone project reflection
