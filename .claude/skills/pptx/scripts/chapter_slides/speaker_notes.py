"""
Auto-generate speaker notes from lesson metadata and content.

Extracts from YAML:
- learning_objectives → key points
- cognitive_load → timing guidance
- differentiation → extension/remedial guidance
"""

from typing import Dict, Any, Optional
from dataclasses import dataclass

# =====================================================================
# SPEAKER NOTES
# =====================================================================


@dataclass
class SpeakerNotes:
    """Speaker notes for a slide."""
    slide_id: str
    timing: str
    key_points: list
    anticipated_qa: list = None
    differentiation: dict = None

    def format_for_pptx(self) -> str:
        """Format speaker notes for PptxGenJS."""
        lines = []
        lines.append(f"⏱ TIMING: {self.timing}")
        lines.append("")
        lines.append("KEY POINTS:")
        for point in self.key_points:
            lines.append(f"  • {point}")

        if self.anticipated_qa:
            lines.append("")
            lines.append("ANTICIPATED Q&A:")
            for qa in self.anticipated_qa:
                lines.append(f"  Q: {qa['question']}")
                lines.append(f"  A: {qa['answer']}")

        if self.differentiation:
            lines.append("")
            lines.append("DIFFERENTIATION:")
            if self.differentiation.get('extension_for_advanced'):
                lines.append(f"  Extension: {self.differentiation['extension_for_advanced']}")
            if self.differentiation.get('remedial_for_struggling'):
                lines.append(f"  Remedial: {self.differentiation['remedial_for_struggling']}")

        return "\n".join(lines)


def generate_speaker_notes(slide_data: Dict[str, Any], yaml_metadata: Dict) -> SpeakerNotes:
    """
    Auto-generate speaker notes from slide data and YAML metadata.

    Args:
        slide_data: Slide data dictionary
        yaml_metadata: YAML frontmatter dictionary

    Returns:
        SpeakerNotes object
    """
    slide_id = slide_data.get('id', 'unknown')

    # 1. Calculate timing
    cognitive_load = yaml_metadata.get('cognitive_load', {})
    if isinstance(cognitive_load, dict):
        new_concepts = cognitive_load.get('new_concepts', 3)
    else:
        new_concepts = 3

    timing_minutes = int(new_concepts * 0.5)  # ~30 sec per concept
    timing = f"{timing_minutes} minute{'s' if timing_minutes != 1 else ''}"

    # 2. Extract key points from learning objectives
    key_points = []
    objectives = yaml_metadata.get('learning_objectives', [])

    if isinstance(objectives, list):
        for obj in objectives[:5]:
            if isinstance(obj, dict):
                objective_text = obj.get('objective', '')
                if objective_text:
                    key_points.append(objective_text)
            else:
                key_points.append(str(obj))

    # Fallback
    if not key_points:
        slide_title = slide_data.get('slide_title', 'This concept')
        key_points = [f"Understand: {slide_title}", "Answer student questions", "Connect to prior knowledge"]

    # 3. Generate Q&A from content
    anticipated_qa = _generate_qa(slide_data)

    # 4. Extract differentiation guidance
    differentiation = yaml_metadata.get('differentiation', {})

    return SpeakerNotes(
        slide_id=slide_id,
        timing=timing,
        key_points=key_points,
        anticipated_qa=anticipated_qa,
        differentiation=differentiation if isinstance(differentiation, dict) else {}
    )


def _generate_qa(slide_data: Dict[str, Any]) -> list:
    """Generate anticipated Q&A from slide content."""
    slide_type = slide_data.get('slide_type', 'concept')
    qa = []

    if slide_type == 'concept':
        qa.append({
            'question': "What's a real-world example of this?",
            'answer': "See the example slides or Try With AI sections for practical applications."
        })
    elif slide_type == 'process':
        qa.append({
            'question': "What happens if I skip a step?",
            'answer': "Each step builds on the previous ones. Skipping may cause errors or incomplete results."
        })
    elif slide_type == 'example':
        qa.append({
            'question': "Can I modify this code for my use case?",
            'answer': "Yes - identify the key parameters and adjust them to your specific needs."
        })
    elif slide_type == 'try_with_ai':
        qa.append({
            'question': "What should I look for in the response?",
            'answer': "Check for: (1) Correct structure, (2) Relevant details, (3) Clear explanation"
        })
    elif slide_type == 'comparison':
        qa.append({
            'question': "When should I use Option A vs Option B?",
            'answer': "It depends on your requirements. Consider factors shown in the table."
        })

    return qa
