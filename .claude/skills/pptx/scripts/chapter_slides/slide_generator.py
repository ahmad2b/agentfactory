"""
Slide generation: Convert parsed lesson content to HTML slides.

Maps sections to templates and generates HTML ready for html2pptx.js.
"""

from typing import List, Dict, Any
from .markdown_parser import LessonContent, Section
from .template_manager import TemplateManager
from .adaptive_distribution import select_distribution
from .config import DEBUG

# =====================================================================
# SLIDE GENERATOR
# =====================================================================


class SlideGenerator:
    """Generates HTML slides from parsed lesson content."""

    def __init__(self, distribution: Dict[str, float], template_manager: TemplateManager):
        """
        Initialize slide generator.

        Args:
            distribution: Slide type distribution percentages
            template_manager: TemplateManager instance for rendering
        """
        self.distribution = distribution
        self.template_manager = template_manager
        self.slide_counter = 0

    def generate_slides_for_lesson(self, lesson_content: LessonContent) -> List[Dict[str, Any]]:
        """
        Generate all slides for a single lesson.

        Includes: title slide + content slides + summary slide

        Args:
            lesson_content: Parsed LessonContent object

        Returns:
            List of slide dictionaries with HTML and metadata
        """
        slides = []
        self.slide_counter = 0

        # 1. Title slide
        title_slide = self._create_title_slide(lesson_content)
        slides.append(title_slide)
        self.slide_counter += 1

        # 2. Content slides from sections
        for section in lesson_content.sections:
            slide = self._create_content_slide(section, lesson_content)
            if slide:
                slides.append(slide)
                self.slide_counter += 1

        # 3. Summary slide (optional)
        if lesson_content.sections:
            summary_slide = self._create_summary_slide(lesson_content)
            slides.append(summary_slide)
            self.slide_counter += 1

        # Add total slide info to each
        total = len(slides)
        for i, slide in enumerate(slides, 1):
            slide['slide_number'] = i
            slide['total_slides'] = total

        return slides

    def _create_title_slide(self, lesson_content: LessonContent) -> Dict[str, Any]:
        """Create title slide for lesson."""
        data = {
            'slide_title': lesson_content.title,
            'chapter_context': f"Chapter {lesson_content.metadata.chapter_number}, Lesson {lesson_content.metadata.lesson_number}",
            'subtitle': lesson_content.title,
            'duration_minutes': lesson_content.metadata.duration_minutes,
            'proficiency_level': lesson_content.metadata.proficiency_level,
            'layer': lesson_content.metadata.layer,
            'chapter_number': lesson_content.metadata.chapter_number,
            'lesson_number': lesson_content.metadata.lesson_number,
            'slide_number': 1,
            'total_slides': '?',  # Will be updated later
        }

        html = self.template_manager.render_slide(
            '01-title',
            lesson_content.metadata.layer,
            data
        )

        return {
            'id': f"L{lesson_content.metadata.lesson_number}-title",
            'slide_type': 'title',
            'layer': lesson_content.metadata.layer,
            'html': html,
            'data': data,
            'yaml_metadata': lesson_content.yaml_frontmatter,
        }

    def _create_content_slide(
        self,
        section: Section,
        lesson_content: LessonContent
    ) -> Dict[str, Any]:
        """Create content slide from section."""
        # Determine slide type
        slide_type_id = section.slide_type_hint

        # Map to template ID (e.g., "concept" → "03-concept")
        template_id = self._map_slide_type_to_template(slide_type_id)

        # Prepare slide data
        data = {
            'slide_title': section.heading,
            'section_title': section.heading,
            'slide_id': f"S-{self.slide_counter}",
            'chapter_number': lesson_content.metadata.chapter_number,
            'lesson_number': lesson_content.metadata.lesson_number,
            'proficiency_level': lesson_content.metadata.proficiency_level,
            'duration_minutes': lesson_content.metadata.duration_minutes,
        }

        # Content-type specific data extraction
        if section.content_type == "table":
            data['comparison_title'] = section.heading
            data['table_data'] = section.content
        elif section.content_type == "code":
            data['example_title'] = section.heading
            data['code_text'] = self._extract_code_block(section.content)
            data['explanation'] = self._extract_explanation(section.content)
        elif section.content_type == "try_with_ai":
            data['prompt_text'] = self._extract_prompt(section.content)
            data['learning_explanation'] = self._extract_learning_goal(section.content)
        else:
            # Default concept/text slide
            data['concept_title'] = section.heading
            data['definition_text'] = self._extract_definition(section.content)
            data['key_points'] = self._extract_key_points(section.content)
            data['additional_context'] = section.content[:200] + "..."

        try:
            html = self.template_manager.render_slide(
                template_id,
                lesson_content.metadata.layer,
                data
            )

            return {
                'id': f"L{lesson_content.metadata.lesson_number}-S{self.slide_counter}",
                'slide_type': slide_type_id,
                'template_id': template_id,
                'layer': lesson_content.metadata.layer,
                'html': html,
                'data': data,
                'yaml_metadata': lesson_content.yaml_frontmatter,
            }
        except Exception as e:
            if DEBUG:
                print(f"⚠ Warning: Failed to render slide '{section.heading}': {e}")
            return None

    def _create_summary_slide(self, lesson_content: LessonContent) -> Dict[str, Any]:
        """Create summary slide for lesson."""
        # Extract key points from learning objectives
        key_takeaways = []
        objectives = lesson_content.yaml_frontmatter.get('learning_objectives', [])

        if isinstance(objectives, list):
            for obj in objectives[:5]:  # Limit to 5 points
                if isinstance(obj, dict):
                    key_takeaways.append(obj.get('objective', ''))
                else:
                    key_takeaways.append(str(obj))

        # Fallback: extract from first few section headings
        if not key_takeaways:
            for section in lesson_content.sections[:5]:
                key_takeaways.append(section.heading)

        data = {
            'slide_title': f"{lesson_content.title} - Summary",
            'summary_title': 'Key Takeaways',
            'key_takeaways': key_takeaways,
            'chapter_number': lesson_content.metadata.chapter_number,
            'lesson_number': lesson_content.metadata.lesson_number,
            'proficiency_level': lesson_content.metadata.proficiency_level,
            'duration_minutes': lesson_content.metadata.duration_minutes,
        }

        html = self.template_manager.render_slide(
            '11-summary',
            lesson_content.metadata.layer,
            data
        )

        return {
            'id': f"L{lesson_content.metadata.lesson_number}-summary",
            'slide_type': 'summary',
            'layer': lesson_content.metadata.layer,
            'html': html,
            'data': data,
            'yaml_metadata': lesson_content.yaml_frontmatter,
        }

    # =====================================================================
    # HELPER METHODS
    # =====================================================================

    def _map_slide_type_to_template(self, slide_type: str) -> str:
        """Map slide type to template ID."""
        mapping = {
            'title': '01-title',
            'hook': '02-hook',
            'concept': '03-concept',
            'comparison': '04-comparison',
            'process': '05-process',
            'example': '06-example',
            'decision': '07-decision',
            'evidence': '08-evidence',
            'business': '09-business',
            'try_with_ai': '10-try-with-ai',
            'summary': '11-summary',
            'assessment': '12-assessment',
        }
        return mapping.get(slide_type, '03-concept')

    def _extract_code_block(self, content: str) -> str:
        """Extract code from markdown code block."""
        import re
        match = re.search(r"```[\w]*\n(.*?)\n```", content, re.DOTALL)
        if match:
            return match.group(1)
        return content[:500]

    def _extract_explanation(self, content: str) -> list:
        """Extract explanation points from section."""
        # Simple extraction: split by bullet points or sentences
        lines = content.split('\n')
        points = [line.strip() for line in lines if line.strip() and not line.startswith('```')]
        return points[:5]

    def _extract_prompt(self, content: str) -> str:
        """Extract prompt from Try With AI section."""
        # Look for quoted text
        import re
        match = re.search(r'> (.*?)(?:\n\n|$)', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        return content[:200]

    def _extract_learning_goal(self, content: str) -> str:
        """Extract learning goal from Try With AI section."""
        # Look for "What you're learning:" or similar
        import re
        match = re.search(r'(?:What you\'re learning|Learning goal)[:\s]+(.*?)(?:\n|$)', content, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "Practice using AI with this prompt"

    def _extract_definition(self, content: str) -> str:
        """Extract definition from concept section."""
        lines = content.split('\n')
        # First non-empty line (not code)
        for line in lines:
            if line.strip() and not line.startswith('```') and not line.startswith('|'):
                return line.strip()
        return content[:300]

    def _extract_key_points(self, content: str) -> list:
        """Extract key points from section content."""
        import re
        # Look for bullet points or numbered lists
        bullets = re.findall(r'[•\-\*]\s+([^\n]+)', content)
        if bullets:
            return bullets[:5]

        # Fallback: split sentences
        sentences = content.split('.')
        return [s.strip() for s in sentences[:5] if s.strip()]
