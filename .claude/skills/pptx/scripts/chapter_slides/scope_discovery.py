"""
Scope discovery for chapter-based presentation generation.

Discovers lesson files based on user input:
- "Chapter 5" → auto-discover all lessons in Chapter 5
- "Part 2" → auto-discover all chapters in Part 2
- "Chapter 5 from Part 2" → specific chapter
- File path → single lesson

Follows the assessment-architect pattern for scope discovery.
"""

import re
from pathlib import Path
from typing import List, Optional, Tuple
from dataclasses import dataclass, field

# =====================================================================
# DATA STRUCTURES
# =====================================================================


@dataclass
class ScopeMetadata:
    """Metadata describing the scope of lesson discovery."""
    scope_type: str  # "chapter", "part", "lesson", "custom"
    part_number: Optional[int] = None
    chapter_number: Optional[int] = None
    chapter_name: Optional[str] = None
    lesson_files: List[Path] = field(default_factory=list)
    estimated_slides: int = 0
    total_word_count: int = 0

    def summary(self) -> str:
        """Generate user-friendly summary of scope."""
        if self.scope_type == "chapter":
            return f"Chapter {self.chapter_number}"
        elif self.scope_type == "part":
            return f"Part {self.part_number}"
        elif self.scope_type == "lesson":
            return self.lesson_files[0].stem if self.lesson_files else "Single lesson"
        return "Custom scope"


# =====================================================================
# SCOPE PARSING
# =====================================================================


def parse_scope_input(user_input: str) -> ScopeMetadata:
    """
    Parse user input to determine scope.

    Examples:
    - "Chapter 5" → chapter_number=5
    - "Part 2" → part_number=2
    - "Chapter 5 from Part 2" → part_number=2, chapter_number=5
    - "Lesson 04-hello-world-basics" → specific lesson
    - File path → single lesson file

    Args:
        user_input: User's scope specification

    Returns:
        ScopeMetadata with parsed scope information
    """
    user_input = user_input.strip()

    # Try to parse "Chapter N from Part M" pattern
    match = re.match(r"Chapter\s+(\d+)\s+from\s+Part\s+(\d+)", user_input, re.IGNORECASE)
    if match:
        chapter_num = int(match.group(1))
        part_num = int(match.group(2))
        return ScopeMetadata(
            scope_type="chapter",
            part_number=part_num,
            chapter_number=chapter_num
        )

    # Try to parse "Part N" pattern
    match = re.match(r"Part\s+(\d+)$", user_input, re.IGNORECASE)
    if match:
        part_num = int(match.group(1))
        return ScopeMetadata(
            scope_type="part",
            part_number=part_num
        )

    # Try to parse "Chapter N" pattern
    match = re.match(r"Chapter\s+(\d+)$", user_input, re.IGNORECASE)
    if match:
        chapter_num = int(match.group(1))
        return ScopeMetadata(
            scope_type="chapter",
            chapter_number=chapter_num
        )

    # Try to parse file path
    if "/" in user_input or "\\" in user_input or user_input.endswith(".md"):
        file_path = Path(user_input)
        if file_path.exists():
            return ScopeMetadata(
                scope_type="lesson",
                lesson_files=[file_path]
            )

    # Fallback: treat as chapter number if it's just a number
    try:
        chapter_num = int(user_input)
        return ScopeMetadata(
            scope_type="chapter",
            chapter_number=chapter_num
        )
    except ValueError:
        pass

    # Unknown format - return as-is with custom scope type
    return ScopeMetadata(scope_type="custom")


def discover_lesson_files(
    scope: ScopeMetadata,
    base_path: Optional[Path] = None
) -> List[Path]:
    """
    Auto-discover lesson files based on scope.

    Lesson file patterns:
    - NN-lesson-name.md (e.g., 01-origin-story.md, 02-installation.md)
    - 00-build-skill-name.md (L00 skill-first lessons)

    Exclusions:
    - README.md
    - *.summary.md
    - *quiz.md

    Args:
        scope: ScopeMetadata describing what to discover
        base_path: Root path for lesson discovery (defaults to book docs directory)

    Returns:
        Sorted list of Path objects for discovered lessons
    """
    if base_path is None:
        # Default to book docs directory
        base_path = Path(__file__).parent.parent.parent.parent.parent / \
                   "apps/learn-app/docs"

    discovered_files = []

    if scope.scope_type == "chapter":
        # Discover lessons in specific chapter
        # Pattern: docs/NN-*/0N-*/NN-lesson-name.md

        if scope.part_number and scope.chapter_number:
            # Chapter from specific part
            part_dir = f"{scope.part_number:02d}-*"
            chapter_dir = f"{scope.chapter_number:02d}-*"
        elif scope.chapter_number:
            # Any chapter with this number (may be ambiguous)
            part_dir = "*"
            chapter_dir = f"{scope.chapter_number:02d}-*"
        else:
            return []

        # Search for matching directories
        for part_match in base_path.glob(part_dir):
            for chapter_match in part_match.glob(chapter_dir):
                # Find lesson files in this chapter
                for lesson_file in sorted(chapter_match.glob("[0-9][0-9]-*.md")):
                    # Exclude certain files
                    if lesson_file.name.startswith("README"):
                        continue
                    if lesson_file.name.endswith(".summary.md"):
                        continue
                    if "quiz" in lesson_file.name.lower():
                        continue

                    discovered_files.append(lesson_file)

    elif scope.scope_type == "part":
        # Discover all chapters/lessons in part
        part_dir = f"{scope.part_number:02d}-*"

        for part_match in base_path.glob(part_dir):
            # Find all chapter directories
            for chapter_match in part_match.glob("[0-9][0-9]-*"):
                # Find lesson files
                for lesson_file in sorted(chapter_match.glob("[0-9][0-9]-*.md")):
                    if lesson_file.name.startswith("README"):
                        continue
                    if lesson_file.name.endswith(".summary.md"):
                        continue
                    if "quiz" in lesson_file.name.lower():
                        continue

                    discovered_files.append(lesson_file)

    elif scope.scope_type == "lesson":
        discovered_files = scope.lesson_files

    return sorted(discovered_files)


def estimate_slide_count(lesson_files: List[Path]) -> int:
    """
    Estimate total slide count from lesson files.

    Formula:
    - Count words in each lesson
    - Divide by target words per slide (125)
    - Add 20% margin for tables/code blocks/diagrams

    Args:
        lesson_files: List of lesson file paths

    Returns:
        Estimated slide count
    """
    total_words = 0

    for lesson_file in lesson_files:
        try:
            content = lesson_file.read_text(encoding='utf-8')
            # Count words (simple: split by whitespace)
            word_count = len(content.split())
            total_words += word_count
        except Exception as e:
            print(f"⚠ Warning: Could not read {lesson_file.name}: {e}")

    # Target: 125 words per slide
    base_slides = total_words / 125

    # Add margin for visual elements (tables, code, diagrams)
    # Typically add 20% for these
    estimated_slides = int(base_slides * 1.2)

    return estimated_slides


def estimate_word_count(lesson_files: List[Path]) -> int:
    """
    Calculate total word count across lesson files.

    Args:
        lesson_files: List of lesson file paths

    Returns:
        Total word count
    """
    total_words = 0

    for lesson_file in lesson_files:
        try:
            content = lesson_file.read_text(encoding='utf-8')
            word_count = len(content.split())
            total_words += word_count
        except Exception:
            pass

    return total_words


# =====================================================================
# CONFIRMATION AND VALIDATION
# =====================================================================


def format_discovery_confirmation(
    scope: ScopeMetadata,
    lesson_files: List[Path],
    estimated_slides: int
) -> str:
    """
    Format discovery results for user confirmation.

    Args:
        scope: Parsed scope metadata
        lesson_files: Discovered lesson files
        estimated_slides: Estimated slide count

    Returns:
        Formatted confirmation message
    """
    lines = []

    # Header
    lines.append("=" * 70)
    lines.append("CHAPTER SLIDE GENERATION: SCOPE DISCOVERY")
    lines.append("=" * 70)

    # Summary
    lines.append(f"\nFound {len(lesson_files)} lessons in {scope.summary()}:")
    lines.append("")

    # Lesson list
    for i, lesson_file in enumerate(lesson_files, 1):
        # Extract lesson number from filename
        match = re.match(r"(\d+)-(.*?)(.md)?$", lesson_file.name)
        if match:
            lesson_num = match.group(1)
            lesson_title = match.group(2).replace("-", " ").title()
            lines.append(f"  {i:2d}. L{lesson_num}: {lesson_title}")
        else:
            lines.append(f"  {i:2d}. {lesson_file.name}")

    # Statistics
    total_words = estimate_word_count(lesson_files)
    lines.append("")
    lines.append("Summary:")
    lines.append(f"  Lessons: {len(lesson_files)}")
    lines.append(f"  Total words: {total_words:,}")
    lines.append(f"  Estimated slides: {estimated_slides} (at 125 words/slide)")
    lines.append(f"  Generation time: ~{estimated_slides * 0.5:.0f} seconds")

    lines.append("")
    return "\n".join(lines)


def handle_ambiguous_scope(chapter_num: int, found_locations: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
    """
    Handle case where chapter number exists in multiple parts.

    Args:
        chapter_num: Chapter number (ambiguous)
        found_locations: List of (part_num, chapter_num) tuples where chapter was found

    Returns:
        Selected (part_num, chapter_num) or None if user cancelled
    """
    if not found_locations:
        print(f"❌ Chapter {chapter_num} not found in any part.")
        return None

    if len(found_locations) == 1:
        return found_locations[0]

    # Multiple locations - ask user to clarify
    print(f"\n⚠ Chapter {chapter_num} found in multiple parts:")
    for i, (part_num, _) in enumerate(found_locations, 1):
        print(f"  {i}. Part {part_num}, Chapter {chapter_num}")

    try:
        choice = input("Enter choice (1-" + str(len(found_locations)) + ") or 'cancel': ")
        if choice.lower() == 'cancel':
            return None
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(found_locations):
            return found_locations[choice_idx]
    except ValueError:
        pass

    return None


# =====================================================================
# TESTING
# =====================================================================


if __name__ == "__main__":
    # Test scope parsing
    print("Testing scope parsing:\n")

    test_cases = [
        "Chapter 5",
        "Part 2",
        "Chapter 5 from Part 2",
        "5",
    ]

    for test_input in test_cases:
        scope = parse_scope_input(test_input)
        print(f"Input: '{test_input}'")
        print(f"  Type: {scope.scope_type}")
        print(f"  Part: {scope.part_number}, Chapter: {scope.chapter_number}")
        print()
