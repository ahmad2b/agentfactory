---
name: content-refiner
description: POST-GATE TOOL. Refine verbose content by eliminating redundancy, trimming word count, and strengthening lesson connections. Use ONLY to fix Gate 4 failures.
---

# Content Refiner (The Fixer)

## Purpose
**POST-GATE TOOL.**
Transforms content that **FAILED Gate 4** into passing content.
Focuses on trimming verbosity and fixing continuity.

## When to Use
- **Trigger**: Gate 4 returned `[FAIL]`.
- **Goal**: Reduce word count or fix "generic opening" issues.

## The Refinement Procedure

### 1. The Fluff Cutter (Word Count Fix)
**Target**: Reduce words by 15-20%.
**Actions:**
- **Delete "Why This Matters"** unless it reveals non-obvious insight.
- **Delete "Reflection"** sections.
- **Reduce "Try With AI"** to exactly 2 prompts.
- **One Analogy Rule:** Keep the best analogy, delete the rest.
- **Merge Tables/Text:** Use Table OR Text, never both.

### 2. The Connection Builder (Continuity Fix)
**Target**: Fix generic openings.
**Formula:**
```markdown
In [Previous Lesson], you [specific outcome].
Now, we will [connect outcome to new goal] by [strategy].
```
**Running Example Check:** Ensure the code uses the chapter's persistent domain.

## Output Format

```markdown
## Refinement Report: [Lesson Name]

### Metrics
| Before | After | Target |
|--------|-------|--------|
| 1650   | 1450  | <1500  |

### Fixes Applied
1. **Cut**: Removed redundant "Why This Matters" (Line 40).
2. **Cut**: Deleted 2 extra "Try With AI" prompts.
3. **Continuity**: Rewrote opening to reference "booking-agent" from Lesson 2.

### Refined Content
[Full refined lesson content]
```