"""
Content classification for chapter-based presentations.

Analyzes lessons to determine content type (conceptual/procedural/coding)
using 8 indicators:

1. Code blocks (```) → coding indicator
2. Try With AI sections → procedural indicator
3. Markdown tables (|---|---|) → conceptual indicator
4. Numbered lists → procedural indicator
5. "How to..." sections → procedural indicator
6. Layer metadata (L1 vs L4) → conceptual vs technical
7. Inline code density (`code`) → coding indicator
8. Conceptual keywords (strategy, framework, paradigm) → conceptual

Follows the assessment-architect pattern for content classification.
"""

import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from .config import (
    CLASSIFICATION_THRESHOLDS,
    INDICATOR_WEIGHTS,
    DEBUG
)

# =====================================================================
# DATA STRUCTURES
# =====================================================================


@dataclass
class ContentClassification:
    """Results of content classification analysis."""
    content_type: str  # "conceptual", "procedural", "coding", "mixed"
    scores: Dict[str, float]  # {conceptual: 65, procedural: 25, coding: 10}
    indicators: Dict[str, int]  # Raw indicator counts
    confidence: float  # 0-100, highest score
    lesson_count: int = 0


# =====================================================================
# INDICATOR EXTRACTION
# =====================================================================


def extract_yaml_frontmatter(content: str) -> Dict[str, any]:
    """
    Extract YAML frontmatter from markdown without external library.

    Handles:
    - Simple key: value pairs
    - Lists: [item1, item2]
    - Nested dictionaries (basic support)

    Args:
        content: Markdown file content

    Returns:
        Dictionary of frontmatter key-value pairs
    """
    if not content.startswith("---"):
        return {}

    lines = content.split("\n")

    # Find end delimiter
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].startswith("---"):
            end_idx = i
            break

    if end_idx is None:
        return {}

    frontmatter = {}

    for line in lines[1:end_idx]:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if ":" not in line:
            continue

        # Split on first colon
        parts = line.split(":", 1)
        key = parts[0].strip()
        value = parts[1].strip() if len(parts) > 1 else ""

        # Try to parse value
        if value.startswith("[") and value.endswith("]"):
            # List: [item1, item2]
            items = value[1:-1].split(",")
            value = [item.strip() for item in items]
        elif value.lower() in ("true", "false"):
            value = value.lower() == "true"
        elif value.isdigit():
            value = int(value)

        frontmatter[key.lower()] = value

    return frontmatter


def extract_layer_from_yaml(frontmatter: Dict) -> str:
    """
    Extract pedagogical layer from YAML metadata.

    Looks for: primary_layer, layer_1_foundation, etc.

    Args:
        frontmatter: Parsed YAML dictionary

    Returns:
        Layer designation ("L1", "L2", "L3", "L4") or default "L1"
    """
    # Try primary_layer field
    primary_layer = frontmatter.get("primary_layer", "").lower()
    if "layer 1" in primary_layer:
        return "L1"
    elif "layer 2" in primary_layer:
        return "L2"
    elif "layer 3" in primary_layer:
        return "L3"
    elif "layer 4" in primary_layer:
        return "L4"

    # Try individual layer fields
    for layer_num in [1, 2, 3, 4]:
        key = f"layer_{layer_num}_" + ("foundation" if layer_num == 1 else "collaboration" if layer_num == 2 else "intelligence" if layer_num == 3 else "capstone")
        if key in frontmatter and frontmatter[key]:
            return f"L{layer_num}"

    return "L1"  # Default


def count_code_blocks(content: str) -> int:
    """Count markdown code blocks (```)."""
    return len(re.findall(r"```[\s\S]*?```", content))


def count_try_with_ai_sections(content: str) -> int:
    """Count 'Try With AI' sections."""
    return len(re.findall(r"##\s*Try\s+With\s+AI", content, re.IGNORECASE))


def count_markdown_tables(content: str) -> int:
    """Count markdown tables (|---|---|)."""
    # Simple pattern: line with pipes and dashes
    return len(re.findall(r"^\|[\s\-\w]+\|", content, re.MULTILINE))


def count_numbered_lists(content: str) -> int:
    """Count numbered list items (1. 2. 3.)."""
    return len(re.findall(r"^\d+\.\s+", content, re.MULTILINE))


def count_how_to_sections(content: str) -> int:
    """Count 'How to...' H2 sections."""
    return len(re.findall(r"^##\s+How\s+to", content, re.MULTILINE | re.IGNORECASE))


def count_inline_code(content: str) -> int:
    """Count inline code (`code`)."""
    return len(re.findall(r"`[^`]+`", content))


def count_conceptual_keywords(content: str) -> int:
    """Count conceptual/framework keywords."""
    keywords = [
        'strategy', 'framework', 'model', 'paradigm', 'concept',
        'theory', 'principle', 'pattern', 'architecture', 'design',
        'methodology', 'approach', 'foundation', 'thesis'
    ]

    count = 0
    for keyword in keywords:
        # Case-insensitive word boundary match
        pattern = rf"\b{keyword}s?\b"  # Match singular and plural
        count += len(re.findall(pattern, content, re.IGNORECASE))

    return count


# =====================================================================
# CLASSIFICATION
# =====================================================================


def classify_single_lesson(lesson_file: Path) -> ContentClassification:
    """
    Classify a single lesson using 8 indicators.

    Args:
        lesson_file: Path to markdown lesson file

    Returns:
        ContentClassification for this lesson
    """
    try:
        content = lesson_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"⚠ Warning: Could not read {lesson_file.name}: {e}")
        return ContentClassification(
            content_type="mixed",
            scores={"conceptual": 33.3, "procedural": 33.3, "coding": 33.4},
            indicators={},
            confidence=0
        )

    # Extract indicators
    indicators = {
        'code_blocks': count_code_blocks(content),
        'try_with_ai': count_try_with_ai_sections(content),
        'tables': count_markdown_tables(content),
        'numbered_lists': count_numbered_lists(content),
        'how_to_sections': count_how_to_sections(content),
        'inline_code': count_inline_code(content),
        'conceptual_keywords': count_conceptual_keywords(content),
    }

    # Add layer indicator
    frontmatter = extract_yaml_frontmatter(content)
    layer = extract_layer_from_yaml(frontmatter)
    indicators['layer'] = 1 if layer == 'L1' else 4 if layer == 'L4' else 2

    # Calculate word count for density
    word_count = len(content.split())
    indicators['word_count'] = word_count
    indicators['inline_code_density'] = indicators['inline_code'] / max(word_count, 1)

    # Score each dimension
    scores = {
        'conceptual': 0.0,
        'procedural': 0.0,
        'coding': 0.0
    }

    # Coding score
    scores['coding'] += indicators['code_blocks'] * 2.0  # 2 points per code block
    scores['coding'] += indicators['inline_code_density'] * 50.0  # Up to 50 points
    scores['coding'] += indicators['inline_code'] * 0.5

    # Procedural score
    scores['procedural'] += indicators['try_with_ai'] * 5.0  # 5 per Try With AI
    scores['procedural'] += indicators['how_to_sections'] * 3.0  # 3 per How To
    scores['procedural'] += indicators['numbered_lists'] * 2.0  # 2 per numbered list

    # Conceptual score
    scores['conceptual'] += indicators['tables'] * 3.0  # 3 per table
    scores['conceptual'] += (1 if indicators['layer'] == 1 else 0) * 20.0  # L1 boost
    scores['conceptual'] += indicators['conceptual_keywords'] * 0.5

    # Normalize to percentages
    total = sum(scores.values())
    if total > 0:
        for key in scores:
            scores[key] = (scores[key] / total) * 100
    else:
        scores = {"conceptual": 33.3, "procedural": 33.3, "coding": 33.4}

    # Determine content type by highest score
    content_type = max(scores.items(), key=lambda x: x[1])[0]
    confidence = max(scores.values())

    return ContentClassification(
        content_type=content_type,
        scores={k: round(v, 1) for k, v in scores.items()},
        indicators=indicators,
        confidence=round(confidence, 1),
        lesson_count=1
    )


def classify_lessons(lesson_files: List[Path]) -> ContentClassification:
    """
    Classify multiple lessons and aggregate results.

    Args:
        lesson_files: List of lesson file paths

    Returns:
        Aggregated ContentClassification for all lessons
    """
    if not lesson_files:
        return ContentClassification(
            content_type="mixed",
            scores={"conceptual": 33.3, "procedural": 33.3, "coding": 33.4},
            indicators={},
            confidence=0,
            lesson_count=0
        )

    # Classify each lesson
    classifications = []
    aggregated_indicators = {
        'code_blocks': 0,
        'try_with_ai': 0,
        'tables': 0,
        'numbered_lists': 0,
        'how_to_sections': 0,
        'inline_code': 0,
        'conceptual_keywords': 0,
        'layer_1_count': 0,
        'word_count': 0,
    }

    for lesson_file in lesson_files:
        classification = classify_single_lesson(lesson_file)
        classifications.append(classification)

        # Aggregate indicators
        for key, value in classification.indicators.items():
            if key in aggregated_indicators:
                aggregated_indicators[key] += value

        if classification.indicators.get('layer') == 1:
            aggregated_indicators['layer_1_count'] += 1

    # Calculate aggregate scores
    lesson_count = len(lesson_files)
    averages = {}
    for score_type in ['conceptual', 'procedural', 'coding']:
        averages[score_type] = sum(
            c.scores.get(score_type, 0) for c in classifications
        ) / lesson_count

    # Determine overall content type
    content_type = max(averages.items(), key=lambda x: x[1])[0]
    confidence = max(averages.values())

    # Round percentages
    scores = {k: round(v, 1) for k, v in averages.items()}

    if DEBUG:
        print(f"\nClassification Debug Info:")
        print(f"  Lessons analyzed: {lesson_count}")
        print(f"  Code blocks: {aggregated_indicators['code_blocks']}")
        print(f"  Try With AI: {aggregated_indicators['try_with_ai']}")
        print(f"  Tables: {aggregated_indicators['tables']}")
        print(f"  Layer 1 lessons: {aggregated_indicators['layer_1_count']}/{lesson_count}")

    return ContentClassification(
        content_type=content_type,
        scores=scores,
        indicators=aggregated_indicators,
        confidence=confidence,
        lesson_count=lesson_count
    )


# =====================================================================
# TESTING
# =====================================================================


if __name__ == "__main__":
    # Test indicator extraction
    test_content = """---
title: Test Lesson
primary_layer: Layer 1
---

# Heading

This is a lesson about frameworks and patterns.

## What is an Agent?

An agent is a pattern in code.

## Try With AI

> Test prompt

## How to Build an Agent

1. Step one
2. Step two

```python
print("code block")
```

| Feature | Value |
|---------|-------|
| Test | Data |
"""

    print("Testing content classifier:\n")

    # Test YAML extraction
    yaml = extract_yaml_frontmatter(test_content)
    print(f"YAML: {yaml}")
    print(f"Layer: {extract_layer_from_yaml(yaml)}")

    # Count indicators
    print(f"\nIndicators:")
    print(f"  Code blocks: {count_code_blocks(test_content)}")
    print(f"  Try With AI: {count_try_with_ai_sections(test_content)}")
    print(f"  Tables: {count_markdown_tables(test_content)}")
    print(f"  How to sections: {count_how_to_sections(test_content)}")
    print(f"  Conceptual keywords: {count_conceptual_keywords(test_content)}")
    print(f"  Inline code: {count_inline_code(test_content)}")


def classify_section_content(content: str) -> str:
    """
    Determine section content type by analyzing content.

    Priority order (check in sequence):
    1. Contains table (|---|---|) → "table"
    2. Contains code block (```) → "code"
    3. Contains numbered list (1. 2. 3.) → "list"
    4. Heading contains "Try With AI" → "try_with_ai"
    5. Otherwise → "text"
    """
    if re.search(r"\|.*\|.*\|", content):
        return "table"
    elif re.search(r"```", content):
        return "code"
    elif re.search(r"^\d+\.\s+", content, re.M):
        return "list"
    elif re.search(r"try\s+with\s+ai", content, re.IGNORECASE):
        return "try_with_ai"
    else:
        return "text"
