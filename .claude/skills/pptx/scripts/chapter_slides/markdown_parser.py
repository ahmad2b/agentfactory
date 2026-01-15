"""
Markdown parser for extracting structured lesson content.

Parses lesson markdown files to extract:
- YAML frontmatter (metadata, learning objectives, skills, layer)
- H2 sections with classified content types
- Tables, code blocks, "Try With AI" sections
- Narrative opening paragraphs

Produces structured LessonContent objects for slide generation.
"""

import re
from pathlib import Path
from typing import List, Optional, Tuple
from dataclasses import dataclass, field
from .content_classifier import (
    extract_yaml_frontmatter,
    extract_layer_from_yaml,
    classify_section_content,
    count_conceptual_keywords
)

# =====================================================================
# DATA STRUCTURES
# =====================================================================


@dataclass
class Section:
    """Represents an H2 section in a lesson."""
    heading: str
    content: str
    content_type: str  # "text", "table", "code", "list", "try_with_ai", "hook"
    slide_type_hint: str  # "concept", "comparison", "example", etc.


@dataclass
class LessonMetadata:
    """Metadata about a lesson."""
    lesson_number: int
    chapter_number: int
    proficiency_level: str  # "A1", "A2", "B1", etc.
    duration_minutes: int
    layer: str  # "L1", "L2", "L3", "L4"
    title: str = ""
    lesson_filename: str = ""


@dataclass
class LessonContent:
    """Structured content extracted from a lesson file."""
    file_path: Path
    title: str
    yaml_frontmatter: dict
    metadata: LessonMetadata
    sections: List[Section] = field(default_factory=list)
    narrative_opening: Optional[str] = None


# =====================================================================
# PARSING FUNCTIONS
# =====================================================================


def split_by_h2_sections(content: str) -> List[Tuple[str, str]]:
    """
    Split markdown content by H2 (##) headings.

    Args:
        content: Markdown content

    Returns:
        List of (heading, content) tuples
    """
    # Pattern: ## followed by text until next ## or end
    pattern = r"^##\s+([^\n]+)\n((?:(?!^##\s).*\n?)*)"
    matches = re.findall(pattern, content, re.MULTILINE)

    return matches


def map_to_slide_type(heading: str, content_type: str) -> str:
    """
    Map section heading and content type to slide type.

    Args:
        heading: Section heading (H2 text)
        content_type: Classified content type ("text", "table", "code", etc.)

    Returns:
        Slide type ("title", "concept", "comparison", etc.)
    """
    heading_lower = heading.lower()

    # Content type-based mappings (take priority)
    if content_type == "table":
        return "comparison"
    elif content_type == "code":
        return "example"
    elif content_type == "try_with_ai":
        return "try_with_ai"

    # Heading-based mappings
    if "how to" in heading_lower or "step" in heading_lower:
        return "process"
    elif "what is" in heading_lower or "definition" in heading_lower:
        return "concept"
    elif "when to" in heading_lower or "use " in heading_lower:
        return "decision"
    elif any(word in heading_lower for word in ["roi", "business", "value", "strategy", "benefit"]):
        return "business"
    elif any(word in heading_lower for word in ["data", "research", "study", "evidence", "stat"]):
        return "evidence"
    else:
        return "concept"  # Default


def extract_lesson_number(filename: str) -> int:
    """
    Extract lesson number from filename.

    Examples: "01-origin-story.md" → 1, "04-hello-world.md" → 4

    Args:
        filename: Lesson filename

    Returns:
        Lesson number (1-indexed)
    """
    match = re.match(r"(\d+)-", filename)
    if match:
        return int(match.group(1))
    return 0


def extract_chapter_and_part(file_path: Path) -> Tuple[int, int]:
    """
    Extract chapter and part numbers from file path.

    Examples:
    - apps/learn-app/docs/02-Part/05-Chapter/01-lesson.md → (5, 2)
    - .../03-*/07-*/02-lesson.md → (7, 3)

    Args:
        file_path: Path to lesson file

    Returns:
        Tuple of (chapter_number, part_number)
    """
    parts = file_path.parts

    chapter_num = 0
    part_num = 0

    # Look for part directory (NN-* pattern in parent directories)
    for i, part in enumerate(parts):
        if re.match(r"\d{2}-", part):
            num = int(part[:2])
            # If this is the second-to-last directory, it's likely the chapter
            if i == len(parts) - 3:
                chapter_num = num
            # If it's the third-to-last, it's likely the part
            elif i == len(parts) - 4:
                part_num = num

    return chapter_num, part_num


# =====================================================================
# LESSON PARSING
# =====================================================================


def parse_lesson(lesson_file: Path) -> Optional[LessonContent]:
    """
    Parse a markdown lesson file into structured content.

    Args:
        lesson_file: Path to markdown lesson file

    Returns:
        LessonContent object with structured sections, or None if parsing fails
    """
    try:
        content = lesson_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"⚠ Error: Could not read {lesson_file.name}: {e}")
        return None

    # Extract YAML frontmatter
    yaml_frontmatter = extract_yaml_frontmatter(content)

    # Extract metadata
    lesson_number = extract_lesson_number(lesson_file.name)
    chapter_number, part_number = extract_chapter_and_part(lesson_file)
    layer = extract_layer_from_yaml(yaml_frontmatter)

    title = yaml_frontmatter.get("title", lesson_file.stem)
    proficiency_level = yaml_frontmatter.get("proficiency_level", "A2")

    # Try to extract from skills
    if "proficiency_level" not in yaml_frontmatter:
        skills = yaml_frontmatter.get("skills", [])
        if isinstance(skills, list) and len(skills) > 0:
            if isinstance(skills[0], dict):
                proficiency_level = skills[0].get("proficiency_level", "A2")

    duration_minutes = yaml_frontmatter.get("duration_minutes", 15)
    if isinstance(duration_minutes, str):
        try:
            duration_minutes = int(duration_minutes)
        except ValueError:
            duration_minutes = 15

    metadata = LessonMetadata(
        lesson_number=lesson_number,
        chapter_number=chapter_number,
        proficiency_level=str(proficiency_level),
        duration_minutes=int(duration_minutes),
        layer=layer,
        title=str(title),
        lesson_filename=lesson_file.name
    )

    # Extract narrative opening (first 2-3 paragraphs before first H2)
    opening_match = re.match(r"^---.*?---\n((?:[^#].*\n?)*)", content, re.DOTALL)
    narrative_opening = None
    if opening_match:
        opening_text = opening_match.group(1).strip()
        # Take first 1-2 paragraphs
        paragraphs = opening_text.split("\n\n")
        if paragraphs:
            narrative_opening = paragraphs[0]

    # Split by H2 sections
    h2_sections = split_by_h2_sections(content)

    sections = []
    for heading, section_content in h2_sections:
        if not heading or not section_content.strip():
            continue

        # Classify section content
        content_type = classify_section_content(heading + "\n" + section_content)

        # Map to slide type
        slide_type = map_to_slide_type(heading, content_type)

        section = Section(
            heading=heading,
            content=section_content.strip(),
            content_type=content_type,
            slide_type_hint=slide_type
        )
        sections.append(section)

    return LessonContent(
        file_path=lesson_file,
        title=title,
        yaml_frontmatter=yaml_frontmatter,
        metadata=metadata,
        sections=sections,
        narrative_opening=narrative_opening
    )


def parse_lessons_batch(lesson_files: List[Path]) -> List[LessonContent]:
    """
    Parse multiple lessons.

    Args:
        lesson_files: List of lesson file paths

    Returns:
        List of successfully parsed LessonContent objects
    """
    parsed_lessons = []

    for lesson_file in lesson_files:
        try:
            lesson_content = parse_lesson(lesson_file)
            if lesson_content is not None:
                parsed_lessons.append(lesson_content)
        except Exception as e:
            print(f"⚠ Warning: Failed to parse {lesson_file.name}: {e}")

    return parsed_lessons


# =====================================================================
# TESTING
# =====================================================================


if __name__ == "__main__":
    print("Testing markdown parser:\n")

    # Test section classification
    test_content = """## What is an Agent?

An agent is a concept in computer science.

## How to Build an Agent

1. Step one
2. Step two

## Try With AI

> Test prompt
"""

    sections = split_by_h2_sections(test_content)
    print(f"Found {len(sections)} H2 sections:")
    for heading, content in sections:
        content_type = classify_section_content(heading + "\n" + content)
        slide_type = map_to_slide_type(heading, content_type)
        print(f"  {heading} → {content_type} → {slide_type}")

    # Test lesson number extraction
    print("\nTesting lesson number extraction:")
    test_names = [
        "01-origin-story.md",
        "04-hello-world-basics.md",
        "15-ralph-wiggum-loop.md"
    ]
    for name in test_names:
        num = extract_lesson_number(name)
        print(f"  {name} → {num}")
