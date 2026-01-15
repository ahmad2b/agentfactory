---
name: chapter-linter
description: GATE 1. Fast, deterministic checker for chapter structure, safety, and metadata (Chapter Contract). RUN THIS FIRST. returns PASS/FAIL only.
---

# Chapter Linter (The Bouncer)

## Purpose
**GATE 1 of the Production Pipeline.**
A binary PASS/FAIL gate for structural integrity and safety. Does not evaluate quality, only compliance.

## Usage
**Trigger:** "Lint chapter X", "Check structure of [file]"
**Output:** `[PASS]` or `[FAIL]` with line numbers.

## LINTING RULES (Hard Gates)

### 1. Safety Sanity Check (CRITICAL)
- **Regex:** `rm -rf`, `sudo .* >`, `chmod 777`, `eval\(`
- **Rule:** If present, MUST be inside a warning block or flagged as dangerous.
- **Fail:** Unwarned dangerous commands.

### 2. The Spec-First Structure
- **Requirement:** For any lesson with >20 lines of code.
- **Pattern:**
  1. `## Problem` (or Scenario)
  2. `## Strategy` (or Solution)
  3. `## Spec` (or Blueprint/Design)
  4. `## Implementation` (or Code)
- **Fail:** `## Implementation` appearing before `## Spec`.

### 3. Forbidden Sections
- **List:** `## Summary`, `## Conclusion`, `## Key Takeaways`, `## Wrap Up`.
- **Allowed Exception:** `## Operational Takeaways` (for rigorous synthesis).
- **Fail:** Presence of forbidden headers.

### 4. The Chapter Contract (Metadata)
**Rule:** Frontmatter must explicitly define the editorial contract.
**Required Fields:**
```yaml
proficiency_level: [A1|A2|B1|B2|C1]
layer: [1|2|3|4]
estimated_time: "XX mins"
chapter_type: [Concept|Hands-On|Hybrid]
running_example_id: [string]  # e.g., "booking-agent", "support-bot"
```
- **Fail:** Missing any of these fields.

## Output Format

```text
[FAIL] Chapter Structure
- Line 45: Found '## Implementation' before '## Spec'.
- Line 120: Found forbidden section '## Summary'. (Use '## Operational Takeaways' if synthesis is needed).
- Line 12: Missing 'running_example_id' in frontmatter (Contract Violation).
```
OR
```text
[PASS] Structure Verified. Proceed to Terminology Check.
```
