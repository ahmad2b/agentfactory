"""
Chapter-based presentation generation for the pptx skill.

This module provides intelligent slide generation from educational content:
- Scope discovery (auto-discover lessons from chapter/part references)
- Content classification (detect conceptual/procedural/coding mix)
- Adaptive distribution (adjust slide types based on content)
- Markdown parsing (extract YAML, sections, tables, code)
- Slide generation (map content to templates with layer colors)
- Speaker notes (auto-generate from metadata)
- Validation (WCAG 2.1 AA accessibility + structure)

Main entry point: workflow_orchestrator.ChapterSlideWorkflow
"""

__version__ = "1.0.0"
__all__ = [
    'config',
    'scope_discovery',
    'content_classifier',
    'adaptive_distribution',
    'markdown_parser',
    'template_manager',
    'slide_generator',
    'speaker_notes',
    'validator',
    'workflow_orchestrator',
]
