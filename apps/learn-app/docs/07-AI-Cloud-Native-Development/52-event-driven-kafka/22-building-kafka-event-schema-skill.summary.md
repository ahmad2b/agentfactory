### Core Concept
Extract recurring event schema patterns from this chapter into a reusable SKILL.md file that captures decision frameworks (not just rules), enabling faster and more reliable event schema design in future projects.

### Key Mental Models
- **Three-test framework**: Pattern worth extracting if it recurs across projects (frequency), involves enough decisions (complexity), and benefits multiple teams (organizational value)
- **Skill anatomy**: Persona (thinking stance) + Questions (force context analysis) + Principles (decision frameworks with reasoning)
- **Layer 3 Intelligence**: Not just using AI to solve problems, but encoding accumulated expertise into format that makes future projects faster
- **Validation through novel application**: Test skill on different domain (e-commerce orders, not Task API) to verify reusability

### Critical Patterns
- Strong persona activates specific reasoning: "Think like a data architect designing event contracts for system where producers and consumers evolve independently"
- Strong questions force context analysis: "What would you need to debug an event that caused failure 3 hours ago?"
- Strong principles explain reasoning: "Events are forensic records - if you can't debug using only event data, your metadata is insufficient"
- SKILL.md structure: Frontmatter (triggering conditions), Persona, Decision Points with questions, Principles with decision tests, Common Patterns

### AI Collaboration Keys
- Use AI to review skill and identify gaps - external validation reveals blind spots from being too close to material
- Ask AI to apply skill to novel domain (IoT sensors) to test if patterns are truly reusable or just Task API specific
- Leverage AI to identify production gaps your skill might miss (compression, partition keys, dead letter handling)

### Common Mistakes
- Writing prescriptive rules ("always include X") instead of decision frameworks with reasoning
- Creating skill from single project without testing on different domain to verify generality
- Treating skill as static document instead of iterating based on use across projects

### Connections
- **Builds on**: Lessons 10-21 (all event schema patterns, naming conventions, evolution strategies)
- **Leads to**: Future event-driven projects where skill guides design decisions
