# Designing Reusable Intelligence

This lesson teaches students to create reusable skills through conversation with AI. After good sessions, students identify patterns worth encoding (frequency + complexity + value), then have a conversation where they explain their approach and AI structures it into a skill file. Students learn to test skills on real tasks, iterate until they work, and distinguish when to create a skill (2-6 decision points, human-guided) vs subagent (7+ decisions, AI autonomous). The key insight: skills transform good sessions into reusable playbooks that compound capability across projects.

### Mental Models

- **Skills from Good Sessions**: After a session that went well, ask: Will I do this again? Did it involve multiple decisions? Would I want the same quality next time? If 2+ YES → create a skill.

- **Conversation-Based Creation**: You describe your process naturally, AI asks clarifying questions, AI structures it into a skill file. No need to write files manually—AI handles formatting.

- **Test and Iterate Loop**: Skills need iteration. Save skill → test on real task → evaluate results → update skill → repeat until it works consistently.

- **Intelligence Compounds**: Project 1 takes 8-10 hours (from scratch). Project 2 with skill takes 4 hours (50% faster). Project 3 with multiple skills takes 3.5 hours. Each skill accelerates future work.

### Key Patterns

- **Start skill conversation**: After good session, say "I want to create a skill for [workflow]. During my work, I noticed my best [outputs] had [specific qualities]. Help me turn this into a reusable skill."

- **Answer AI's questions**: AI asks about what makes output "good", your process, quality checks. Provide enough detail that someone capable but unfamiliar could follow.

- **AI builds skill file**: AI creates skill with Description, When to Use, Process (steps), Quality Criteria. Save to `.claude/skills/`.

- **Test the skill**: Use skill on real task. Evaluate: Did AI follow process? Did output meet criteria? What's missing?

- **Iterate**: "The skill worked but [specific issue]. Update skill to [fix]. Test again."

- **Skill vs Subagent**: Skills (2-6 decisions, human guides). Subagents (7+ decisions, AI autonomous). Section-writer = skill. Research-validator = subagent.

### Common Mistakes

- **Creating skills for trivial patterns**: "How to format headings" (1-2 decisions) doesn't justify a skill. Save skills for 5+ decision workflows.

- **Skipping testing**: Saving skill and assuming it works. Skills need iteration—first version misses edge cases.

- **Over-specific skills**: "AI-Education-Literature-Review-Writer" only works for one topic. Generalize to "Section-Writer" (any paper).

- **No quality criteria**: Skill describes process but not what "good" looks like. Every skill needs explicit success criteria.

### Progression Context

- **Builds on**: Lessons 04-08 (complete SDD workflow). Students have executed one full project cycle and understand where patterns recur.

- **Leads to**: Lesson 11 (Capstone) where students invoke created skills to accelerate new work, demonstrating intelligence compounding.
