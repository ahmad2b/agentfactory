"""
Adaptive slide distribution based on content classification.

Selects slide type distribution percentages based on classified content type:
- Conceptual chapters: 40% concept, 15% comparison, 10% example
- Procedural chapters: 25% process, 20% example, 15% concept
- Coding chapters: 30% example, 20% process, 15% try-with-ai
- Mixed: Balanced distribution

Ensures educational content matches pedagogical needs.
"""

from typing import Dict
from .config import DEFAULT_DISTRIBUTIONS, DEBUG

# =====================================================================
# DISTRIBUTION SELECTION
# =====================================================================


def select_distribution(content_type: str) -> Dict[str, float]:
    """
    Select slide type distribution for a content type.

    Args:
        content_type: One of "conceptual", "procedural", "coding", "mixed"

    Returns:
        Dictionary mapping slide type IDs to percentages (0-1)

    Example:
        dist = select_distribution("conceptual")
        dist['concept']  # 0.40 (40% of slides)
        dist['comparison']  # 0.15 (15% of slides)
    """
    # Get distribution from config
    dist = DEFAULT_DISTRIBUTIONS.get(content_type.lower())

    if dist is None:
        if DEBUG:
            print(f"⚠ Warning: Unknown content type '{content_type}', using 'mixed'")
        dist = DEFAULT_DISTRIBUTIONS['mixed']

    # Return a copy to avoid modifying config
    return dist.copy()


def calculate_slide_counts(
    total_sections: int,
    distribution: Dict[str, float],
    total_slides_target: int
) -> Dict[str, int]:
    """
    Calculate how many slides of each type to generate.

    Args:
        total_sections: Total number of H2 sections in lessons
        distribution: Slide type distribution percentages
        total_slides_target: Target total slide count

    Returns:
        Dictionary mapping slide types to target slide counts

    Example:
        sections = 87
        dist = select_distribution("conceptual")
        counts = calculate_slide_counts(87, dist, 90)
        counts['concept']  # Expected number of concept slides
    """
    slide_counts = {}
    remaining_slides = total_slides_target

    # Process each slide type
    slide_types = list(distribution.keys())

    for i, slide_type in enumerate(slide_types):
        percentage = distribution[slide_type]

        # Fixed slides (title, summary) have count of 1 or more
        if percentage == 1:
            slide_counts[slide_type] = 1
            remaining_slides -= 1
        else:
            # Calculate proportional count
            count = int(remaining_slides * percentage)
            slide_counts[slide_type] = max(0, count)
            remaining_slides -= count

    # Distribute any remaining slides to the largest percentage type
    if remaining_slides > 0:
        # Find non-fixed slide type with highest percentage
        largest_type = max(
            (k for k, v in slide_types if v != 1 and v > 0),
            key=lambda k: distribution[k],
            default=None
        )

        if largest_type:
            slide_counts[largest_type] = slide_counts.get(largest_type, 0) + remaining_slides

    return slide_counts


def validate_distribution(distribution: Dict[str, float]) -> bool:
    """
    Validate that a distribution is valid.

    Rules:
    - All percentages should be 0-1
    - Non-fixed types should sum to ~1 (allow ±0.05 tolerance)
    - Fixed types (value 1) should be limited (title, summary)

    Args:
        distribution: Distribution to validate

    Returns:
        True if valid, False otherwise
    """
    # Check all values are valid
    for slide_type, percentage in distribution.items():
        if percentage < 0 or percentage > 1:
            print(f"⚠ Invalid percentage for {slide_type}: {percentage}")
            return False

    # Check sum of non-fixed percentages
    non_fixed_sum = sum(v for v in distribution.values() if v != 1)
    if non_fixed_sum < 0.95 or non_fixed_sum > 1.05:
        if DEBUG:
            print(f"⚠ Warning: Non-fixed percentages sum to {non_fixed_sum}, expected ~1.0")
        # Don't fail - allow some tolerance

    # Check fixed type count
    fixed_count = sum(1 for v in distribution.values() if v == 1)
    if fixed_count > 5:
        print(f"⚠ Warning: Too many fixed slides ({fixed_count}), should be <5")
        return False

    return True


# =====================================================================
# DISTRIBUTION UTILITIES
# =====================================================================


def describe_distribution(content_type: str) -> str:
    """
    Describe a distribution in human-readable format.

    Args:
        content_type: Content type (conceptual/procedural/coding/mixed)

    Returns:
        Formatted description of the distribution

    Example:
        print(describe_distribution("conceptual"))
        # Output:
        # Conceptual Content Distribution
        # - Concept: 40.0%
        # - Comparison: 15.0%
        # - Hook: 10.0%
        # ...
    """
    dist = select_distribution(content_type)
    lines = [f"\n{content_type.title()} Content Distribution"]
    lines.append("-" * 40)

    # Sort by percentage (descending)
    sorted_items = sorted(dist.items(), key=lambda x: x[1], reverse=True)

    for slide_type, percentage in sorted_items:
        if percentage == 1:
            lines.append(f"  {slide_type:20s} (fixed)")
        else:
            lines.append(f"  {slide_type:20s} {percentage*100:5.1f}%")

    return "\n".join(lines)


def compare_distributions() -> str:
    """
    Compare all available distributions.

    Returns:
        Formatted comparison of all distributions

    Example:
        print(compare_distributions())
        # Shows side-by-side comparison of conceptual vs procedural vs coding vs mixed
    """
    lines = ["Slide Distribution Comparison"]
    lines.append("=" * 80)

    content_types = ['conceptual', 'procedural', 'coding', 'mixed']
    distributions = {ct: select_distribution(ct) for ct in content_types}

    # Get all slide types
    all_types = set()
    for dist in distributions.values():
        all_types.update(dist.keys())

    all_types = sorted(all_types)

    # Header
    header = f"{'Slide Type':20s}"
    for ct in content_types:
        header += f" {ct:12s}"
    lines.append(header)
    lines.append("-" * 80)

    # Rows
    for slide_type in all_types:
        row = f"{slide_type:20s}"
        for ct in content_types:
            dist = distributions[ct]
            if slide_type in dist:
                percentage = dist[slide_type]
                if percentage == 1:
                    row += f" {'fixed':12s}"
                else:
                    row += f" {percentage*100:6.1f}%     "
            else:
                row += f" {'-':12s}"
        lines.append(row)

    return "\n".join(lines)


# =====================================================================
# TESTING
# =====================================================================


if __name__ == "__main__":
    print("Testing adaptive distribution:\n")

    # Test distribution selection
    print("1. Testing distribution selection:")
    for content_type in ['conceptual', 'procedural', 'coding', 'mixed']:
        dist = select_distribution(content_type)
        print(f"   {content_type}: {len(dist)} slide types")

    # Test calculation
    print("\n2. Testing slide count calculation:")
    dist = select_distribution("conceptual")
    counts = calculate_slide_counts(87, dist, 90)
    total = sum(v for k, v in counts.items() if dist.get(k, 0) != 1)
    print(f"   Total calculated slides: {sum(counts.values())}")
    print(f"   Target: 90, Actual: {sum(counts.values())}")

    # Test validation
    print("\n3. Testing distribution validation:")
    is_valid = validate_distribution(dist)
    print(f"   Conceptual distribution valid: {is_valid}")

    # Show descriptions
    print("\n" + describe_distribution("conceptual"))
    print("\n" + describe_distribution("coding"))

    # Show comparison
    print("\n" + compare_distributions())
