"""
Centralized configuration for chapter-based slide generation.

All thresholds, colors, templates, and settings are defined here for easy tuning.
Follows the assessment-architect config.py pattern.
"""

from typing import Dict, Any

# =====================================================================
# LAYER COLOR SCHEMES (Pedagogical Layers)
# =====================================================================

LAYER_COLORS = {
    'L1': {
        'primary': '#4472C4',
        'dark': '#2E5C9A',
        'light': '#8FAADC',
        'name': 'Blue',
        'description': 'Manual Foundation - First exposure, no AI'
    },
    'L2': {
        'primary': '#70AD47',
        'dark': '#548235',
        'light': '#A9D18E',
        'name': 'Green',
        'description': 'Collaboration - AI as Teacher/Student/Co-Worker'
    },
    'L3': {
        'primary': '#9B59B6',
        'dark': '#7D3C98',
        'light': '#D2B4DE',
        'name': 'Purple',
        'description': 'Intelligence - Skills, MCP, automation'
    },
    'L4': {
        'primary': '#ED7D31',
        'dark': '#C65911',
        'light': '#F4B084',
        'name': 'Orange',
        'description': 'Technical/Capstone - Code-heavy, production'
    }
}

# =====================================================================
# SLIDE TYPE DISTRIBUTION BY CONTENT TYPE
# =====================================================================

DEFAULT_DISTRIBUTIONS = {
    'conceptual': {
        'title': 1,           # Fixed: 1 slide
        'hook': 0.10,         # 10% - narrative openings
        'concept': 0.40,      # 40% - definitions, frameworks (DOMINANT)
        'comparison': 0.15,   # 15% - tables, contrasts
        'process': 0.05,      # 5% - procedures (REDUCED)
        'example': 0.10,      # 10% - conceptual examples
        'decision': 0.05,     # 5% - when to use
        'evidence': 0.05,     # 5% - research, data
        'business': 0.05,     # 5% - ROI, strategy
        'try_with_ai': 0.03,  # 3% - limited hands-on (REDUCED)
        'summary': 1,         # Fixed: 1 slide
        'assessment': 0.01    # 1% - quiz preview
    },
    'procedural': {
        'title': 1,
        'hook': 0.05,
        'concept': 0.20,      # Reduced theory
        'comparison': 0.10,
        'process': 0.25,      # 25% - step-by-step procedures (DOMINANT)
        'example': 0.20,      # 20% - practical examples
        'decision': 0.05,
        'evidence': 0.02,
        'business': 0.02,
        'try_with_ai': 0.10,  # 10% - hands-on exercises
        'summary': 1,
        'assessment': 0.01
    },
    'coding': {
        'title': 1,
        'hook': 0.02,
        'concept': 0.15,      # Minimal theory
        'comparison': 0.10,
        'process': 0.20,
        'example': 0.30,      # 30% - code examples (DOMINANT)
        'decision': 0.05,
        'evidence': 0.01,
        'business': 0.01,
        'try_with_ai': 0.15,  # 15% - extensive hands-on
        'summary': 1,
        'assessment': 0.01
    },
    'mixed': {
        'title': 1,           # Balanced distribution
        'hook': 0.08,
        'concept': 0.30,
        'comparison': 0.12,
        'process': 0.15,
        'example': 0.18,
        'decision': 0.05,
        'evidence': 0.03,
        'business': 0.03,
        'try_with_ai': 0.05,
        'summary': 1,
        'assessment': 0.01
    }
}

# =====================================================================
# CONTENT CLASSIFICATION CONFIGURATION
# =====================================================================

CLASSIFICATION_THRESHOLDS = {
    'conceptual': 0.60,     # >60% conceptual indicators → conceptual
    'coding': 0.40,         # >40% coding indicators → coding
    'procedural': 0.50,     # >50% procedural indicators → procedural
    # Otherwise → mixed
}

# Indicator weights (used in classification scoring)
INDICATOR_WEIGHTS = {
    'code_blocks': 0.15,
    'try_with_ai': 0.10,
    'tables': 0.15,
    'numbered_lists': 0.08,
    'how_to_sections': 0.10,
    'layer_1_lessons': 0.15,
    'inline_code_density': 0.15,
    'conceptual_keywords': 0.12
}

# =====================================================================
# SLIDE GENERATION SETTINGS
# =====================================================================

SLIDE_SETTINGS = {
    'default_layout': '16:9',      # Layout type
    'layout_dimensions': {
        '16:9': {'width': 720, 'height': 405},
        '4:3': {'width': 720, 'height': 540},
        '16:10': {'width': 720, 'height': 450}
    },
    'words_per_slide': 125,        # Average target words per slide
    'max_slides_per_lesson': 8,    # Prevent slide explosion
    'min_slides_per_lesson': 2,    # At least title + content
    'default_font_family': 'Arial, Helvetica, sans-serif',
    'default_body_font_size': 28,  # Points
    'default_heading_font_size': 36,  # Points
}

# =====================================================================
# ACCESSIBILITY THRESHOLDS (WCAG 2.1 AA)
# =====================================================================

ACCESSIBILITY = {
    'min_contrast_ratio': 4.5,     # Text:background minimum
    'min_body_font_size': 28,      # Points (presentation context)
    'min_heading_font_size': 36,   # Points
    'max_words_per_slide': 100,    # Readability threshold
    'alt_text_required': True,     # All images need alt text
    'line_height_min': 1.4,        # Minimum line spacing
}

# =====================================================================
# VALIDATION SETTINGS
# =====================================================================

VALIDATION = {
    'require_speaker_notes': True,
    'require_footer_metadata': True,
    'check_accessibility': True,
    'check_consistency': True,
    'slide_count_tolerance': 0.20,  # ±20% from estimate
}

# =====================================================================
# PERFORMANCE TARGETS
# =====================================================================

PERFORMANCE = {
    'scope_discovery_ms': 200,
    'content_classification_ms': 5000,
    'slide_generation_ms_per_slide': 500,
    'total_generation_ms_target': 60000,  # 60 seconds for 15 lessons
}

# =====================================================================
# SLIDE TYPE DEFINITIONS
# =====================================================================

SLIDE_TYPES = {
    '01-title': {
        'name': 'Title',
        'description': 'Chapter/lesson introduction with metadata',
        'typical_content': 'YAML frontmatter (title, objectives, skills)'
    },
    '02-hook': {
        'name': 'Hook',
        'description': 'Narrative opening to engage learners',
        'typical_content': 'Real-world scenario, problem statement'
    },
    '03-concept': {
        'name': 'Concept',
        'description': 'Definition or framework explanation',
        'typical_content': '"What is..." sections, key points'
    },
    '04-comparison': {
        'name': 'Comparison',
        'description': 'Side-by-side comparison using tables',
        'typical_content': 'Markdown tables, feature matrices'
    },
    '05-process': {
        'name': 'Process',
        'description': 'Step-by-step procedures',
        'typical_content': '"How to..." sections, numbered lists'
    },
    '06-example': {
        'name': 'Example',
        'description': 'Code examples with explanations',
        'typical_content': 'Code blocks with annotations'
    },
    '07-decision': {
        'name': 'Decision',
        'description': 'Decision trees and trade-offs',
        'typical_content': '"When to use..." sections'
    },
    '08-evidence': {
        'name': 'Evidence',
        'description': 'Data, research, statistics',
        'typical_content': 'Research findings, case studies'
    },
    '09-business': {
        'name': 'Business',
        'description': 'Business value and strategy',
        'typical_content': 'ROI, business impact, value proposition'
    },
    '10-try-with-ai': {
        'name': 'Try With AI',
        'description': 'Interactive prompts with learning goals',
        'typical_content': '3-4 prompts with "What you\'re learning" explanations'
    },
    '11-summary': {
        'name': 'Summary',
        'description': 'Chapter recap with key takeaways',
        'typical_content': 'Final section, key points summary'
    },
    '12-assessment': {
        'name': 'Assessment',
        'description': 'Quiz preview or practice questions',
        'typical_content': 'Link to quiz, sample questions'
    }
}

# Content pattern mappings for automatic slide type detection
CONTENT_PATTERN_MAPPINGS = {
    'table': 'comparison',      # Markdown tables → comparison slides
    'code': 'example',          # Code blocks → example slides
    'try_with_ai': 'try_with_ai',  # Try With AI sections
    'how_to': 'process',        # "How to..." → process slides
    'what_is': 'concept',       # "What is..." → concept slides
    'when_to': 'decision',      # "When to use..." → decision slides
    'roi': 'business',          # Business/ROI content
    'data': 'evidence',         # Data/research/statistics
    'numbered_list': 'process',  # Numbered steps → process slides
}

# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def get_distribution(content_type: str) -> Dict[str, float]:
    """Get slide type distribution for content type."""
    return DEFAULT_DISTRIBUTIONS.get(content_type, DEFAULT_DISTRIBUTIONS['mixed']).copy()


def get_layer_colors(layer: str) -> Dict[str, str]:
    """Get color scheme for pedagogical layer."""
    return LAYER_COLORS.get(layer, LAYER_COLORS['L1']).copy()


def get_layout_dimensions(layout: str = '16:9') -> Dict[str, int]:
    """Get slide dimensions for layout."""
    return SLIDE_SETTINGS['layout_dimensions'].get(layout, {'width': 720, 'height': 405})


def get_slide_type_info(slide_id: str) -> Dict[str, str]:
    """Get metadata for a slide type."""
    return SLIDE_TYPES.get(slide_id, {})


def get_contrast_threshold(level: str = 'normal') -> float:
    """Get contrast ratio threshold for WCAG compliance."""
    if level == 'large':
        return 3.0  # Large text (18pt+ or 14pt+ bold)
    return 4.5  # Normal text


# =====================================================================
# VALIDATION HELPERS
# =====================================================================

def should_validate_accessibility() -> bool:
    """Check if accessibility validation is enabled."""
    return VALIDATION.get('check_accessibility', True)


def should_require_speaker_notes() -> bool:
    """Check if speaker notes are required."""
    return VALIDATION.get('require_speaker_notes', True)


# =====================================================================
# DEBUG/TESTING MODE
# =====================================================================

DEBUG = False  # Set to True for verbose logging


if __name__ == "__main__":
    # Quick validation of config
    print("Layer Colors:")
    for layer, colors in LAYER_COLORS.items():
        print(f"  {layer} ({colors['name']}): {colors['primary']}")

    print("\nSlide Types:")
    for slide_id, info in SLIDE_TYPES.items():
        print(f"  {slide_id}: {info['name']}")

    print("\nContent Distributions:")
    for content_type, dist in DEFAULT_DISTRIBUTIONS.items():
        print(f"  {content_type}:")
        top_types = sorted(dist.items(), key=lambda x: x[1], reverse=True)[:3]
        for slide_type, percentage in top_types:
            print(f"    {slide_type}: {percentage*100:.0f}%")

    print("\nAccessibility Thresholds:")
    for key, value in ACCESSIBILITY.items():
        print(f"  {key}: {value}")
