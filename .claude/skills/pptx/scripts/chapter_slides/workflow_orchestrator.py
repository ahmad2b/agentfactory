"""
Workflow orchestrator for chapter-based presentation generation.

7-Step Pipeline:
1. Scope Discovery - Parse input, discover lessons
2. Content Classification - Analyze content type
3. Adaptive Distribution - Select slide type mix
4. Markdown Parsing - Extract structured content
5. Slide Generation - Create HTML slides
6. Speaker Notes - Generate notes from metadata
7. Validation - Check quality and accessibility
"""

import json
from pathlib import Path
from typing import List, Optional

from .scope_discovery import (
    parse_scope_input,
    discover_lesson_files,
    estimate_slide_count,
    format_discovery_confirmation
)
from .content_classifier import classify_lessons
from .adaptive_distribution import select_distribution, describe_distribution
from .markdown_parser import parse_lessons_batch
from .template_manager import TemplateManager
from .slide_generator import SlideGenerator
from .speaker_notes import generate_speaker_notes
from .validator import validate_presentation, print_validation_report

# =====================================================================
# WORKFLOW ORCHESTRATOR
# =====================================================================


class ChapterSlideWorkflow:
    """Orchestrate complete chapter slide generation workflow."""

    def __init__(self, user_input: str, output_dir: Optional[Path] = None):
        """
        Initialize workflow.

        Args:
            user_input: User's scope specification (e.g., "Chapter 5")
            output_dir: Output directory (defaults to current directory)
        """
        self.user_input = user_input
        self.output_dir = output_dir or Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.scope = None
        self.lesson_files = None
        self.classification = None
        self.distribution = None
        self.parsed_lessons = None
        self.all_slides = []

    def execute(self) -> Optional[Path]:
        """
        Execute complete workflow.

        Returns:
            Path to generated PPTX file, or None if cancelled
        """
        print("\n" + "=" * 70)
        print("CHAPTER SLIDE GENERATION WORKFLOW")
        print("=" * 70)

        # STEP 1: Scope Discovery
        print("\n[1/7] Discovering scope...")
        if not self._step_discover_scope():
            print("❌ Scope discovery failed")
            return None

        # STEP 2: Content Classification
        print("\n[2/7] Classifying content...")
        if not self._step_classify_content():
            print("❌ Content classification failed")
            return None

        # STEP 3: Adaptive Distribution
        print("\n[3/7] Selecting slide distribution...")
        if not self._step_select_distribution():
            print("❌ Distribution selection failed")
            return None

        # STEP 4: Markdown Parsing
        print("\n[4/7] Parsing lesson content...")
        if not self._step_parse_lessons():
            print("❌ Lesson parsing failed")
            return None

        # STEP 5: Slide Generation
        print("\n[5/7] Generating slides...")
        if not self._step_generate_slides():
            print("❌ Slide generation failed")
            return None

        # STEP 6: Speaker Notes
        print("\n[6/7] Generating speaker notes...")
        if not self._step_generate_notes():
            print("❌ Speaker notes generation failed")
            return None

        # STEP 7: Validation
        print("\n[7/7] Validating presentation...")
        self._step_validate()

        # Save metadata
        self._save_metadata()

        print("\n" + "=" * 70)
        print("✅ WORKFLOW COMPLETE")
        print("=" * 70)
        print(f"\n📊 Summary:")
        print(f"  Total slides: {len(self.all_slides)}")
        print(f"  Lessons: {len(self.parsed_lessons) if self.parsed_lessons else 0}")
        print(f"  Content type: {self.classification.content_type if self.classification else 'unknown'}")
        print(f"\n💾 Output files:")
        print(f"  Slides JSON: {self.output_dir / 'slides.json'}")
        print(f"  Metadata: {self.output_dir / 'metadata.json'}")

        return self.output_dir / "slides.json"

    # =====================================================================
    # WORKFLOW STEPS
    # =====================================================================

    def _step_discover_scope(self) -> bool:
        """Step 1: Parse input and discover lessons."""
        try:
            self.scope = parse_scope_input(self.user_input)

            # Discover lesson files
            base_path = Path(__file__).parent.parent.parent.parent.parent / "apps/learn-app/docs"
            self.lesson_files = discover_lesson_files(self.scope, base_path)

            if not self.lesson_files:
                print(f"❌ No lessons found for {self.user_input}")
                return False

            # Show confirmation
            estimated_slides = estimate_slide_count(self.lesson_files)
            print(format_discovery_confirmation(self.scope, self.lesson_files, estimated_slides))

            return True
        except Exception as e:
            print(f"❌ Error in scope discovery: {e}")
            return False

    def _step_classify_content(self) -> bool:
        """Step 2: Classify content type."""
        try:
            self.classification = classify_lessons(self.lesson_files)

            print(f"✅ Content type: {self.classification.content_type.upper()}")
            print(f"   Scores: Conceptual {self.classification.scores.get('conceptual', 0):.0f}%, "
                  f"Procedural {self.classification.scores.get('procedural', 0):.0f}%, "
                  f"Coding {self.classification.scores.get('coding', 0):.0f}%")
            print(f"   Confidence: {self.classification.confidence:.0f}%")

            return True
        except Exception as e:
            print(f"❌ Error in content classification: {e}")
            return False

    def _step_select_distribution(self) -> bool:
        """Step 3: Select adaptive slide distribution."""
        try:
            self.distribution = select_distribution(self.classification.content_type)

            print(f"✅ Using '{self.classification.content_type}' distribution")
            print(describe_distribution(self.classification.content_type))

            return True
        except Exception as e:
            print(f"❌ Error in distribution selection: {e}")
            return False

    def _step_parse_lessons(self) -> bool:
        """Step 4: Parse markdown lessons."""
        try:
            self.parsed_lessons = parse_lessons_batch(self.lesson_files)

            if not self.parsed_lessons:
                print("❌ No lessons successfully parsed")
                return False

            total_sections = sum(len(l.sections) for l in self.parsed_lessons)
            total_words = sum(
                len(l.file_path.read_text().split())
                for l in self.parsed_lessons
            )

            print(f"✅ Parsed {len(self.parsed_lessons)} lessons")
            print(f"   Sections: {total_sections}")
            print(f"   Total words: {total_words:,}")

            return True
        except Exception as e:
            print(f"❌ Error in lesson parsing: {e}")
            return False

    def _step_generate_slides(self) -> bool:
        """Step 5: Generate HTML slides."""
        try:
            template_manager = TemplateManager()
            slide_generator = SlideGenerator(self.distribution, template_manager)

            self.all_slides = []
            for lesson in self.parsed_lessons:
                slides = slide_generator.generate_slides_for_lesson(lesson)
                self.all_slides.extend(slides)

            print(f"✅ Generated {len(self.all_slides)} slides")

            # Layer distribution
            layer_counts = {}
            for slide in self.all_slides:
                layer = slide.get('layer', 'L1')
                layer_counts[layer] = layer_counts.get(layer, 0) + 1

            for layer, count in sorted(layer_counts.items()):
                print(f"   {layer}: {count} slides")

            return True
        except Exception as e:
            print(f"❌ Error in slide generation: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _step_generate_notes(self) -> bool:
        """Step 6: Generate speaker notes."""
        try:
            for slide in self.all_slides:
                yaml_metadata = slide.get('yaml_metadata', {})
                notes = generate_speaker_notes(slide, yaml_metadata)
                slide['speaker_notes'] = notes.format_for_pptx()

            print(f"✅ Generated speaker notes for {len(self.all_slides)} slides")
            return True
        except Exception as e:
            print(f"❌ Error in speaker notes generation: {e}")
            return False

    def _step_validate(self) -> bool:
        """Step 7: Validate presentation."""
        try:
            metadata = {
                'chapter_number': self.scope.chapter_number,
                'estimated_slides': estimate_slide_count(self.lesson_files),
                'content_type': self.classification.content_type,
            }

            report = validate_presentation(self.all_slides, metadata)
            print_validation_report(report)

            return report.passed
        except Exception as e:
            print(f"❌ Error in validation: {e}")
            return False

    def _save_metadata(self) -> None:
        """Save presentation metadata and slides."""
        # Save slides as JSON (for further processing)
        slides_data = []
        for slide in self.all_slides:
            slides_data.append({
                'id': slide.get('id'),
                'type': slide.get('slide_type'),
                'layer': slide.get('layer'),
                'html': slide.get('html', '')[:500],  # Truncate for readability
                'speaker_notes': slide.get('speaker_notes', ''),
            })

        slides_file = self.output_dir / "slides.json"
        with open(slides_file, 'w') as f:
            json.dump(slides_data, f, indent=2)
        print(f"   Saved: {slides_file}")

        # Save metadata
        metadata = {
            'scope': str(self.scope.summary()),
            'lesson_count': len(self.parsed_lessons) if self.parsed_lessons else 0,
            'slide_count': len(self.all_slides),
            'content_type': self.classification.content_type if self.classification else 'unknown',
            'classification_scores': self.classification.scores if self.classification else {},
            'output_dir': str(self.output_dir),
        }

        metadata_file = self.output_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        print(f"   Saved: {metadata_file}")


# =====================================================================
# COMMAND-LINE INTERFACE
# =====================================================================


def main():
    """Command-line interface for workflow."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m chapter_slides.workflow_orchestrator '<scope>'")
        print("Examples:")
        print("  'Chapter 5'")
        print("  'Part 2'")
        print("  'Chapter 5 from Part 2'")
        sys.exit(1)

    user_input = sys.argv[1]
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd() / "output"

    workflow = ChapterSlideWorkflow(user_input, output_dir)
    result = workflow.execute()

    if result:
        print(f"\n✅ Success: {result}")
        sys.exit(0)
    else:
        print("\n❌ Workflow failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
