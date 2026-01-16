"""
Template management for chapter slide generation.

Handles:
- Loading master templates (L1-L4 with layer colors)
- Loading slide type templates (01-title through 12-assessment)
- Rendering templates with variable substitution
- Applying layer colors dynamically

Uses simple mustache-style {{variable}} rendering (no external dependencies).
"""

import re
from pathlib import Path
from typing import Dict, Any, Optional
from .config import LAYER_COLORS, DEBUG

# =====================================================================
# TEMPLATE MANAGER
# =====================================================================


class TemplateManager:
    """Manages loading and rendering presentation templates."""

    def __init__(self, template_dir: Optional[Path] = None):
        """
        Initialize template manager.

        Args:
            template_dir: Root directory containing templates/
                         (defaults to ./templates relative to this module)
        """
        if template_dir is None:
            # Path: .claude/skills/pptx/scripts/chapter_slides/template_manager.py
            # Go to: .claude/skills/pptx/templates
            template_dir = Path(__file__).parent.parent.parent / "templates"

        self.template_dir = template_dir
        self.master_templates: Dict[str, str] = {}
        self.slide_type_templates: Dict[str, str] = {}

        self._load_all_templates()

    def _load_all_templates(self) -> None:
        """Load all master and slide type templates."""
        self._load_master_templates()
        self._load_slide_type_templates()

        if DEBUG:
            print(f"✓ Loaded {len(self.master_templates)} master templates")
            print(f"✓ Loaded {len(self.slide_type_templates)} slide type templates")

    def _load_master_templates(self) -> None:
        """Load all 4 master templates (L1-L4)."""
        master_dir = self.template_dir / "master"

        if not master_dir.exists():
            print(f"⚠ Warning: Master template directory not found: {master_dir}")
            return

        layer_files = {
            'L1': 'L1-blue-master.html',
            'L2': 'L2-green-master.html',
            'L3': 'L3-purple-master.html',
            'L4': 'L4-orange-master.html'
        }

        for layer, filename in layer_files.items():
            template_file = master_dir / filename
            if template_file.exists():
                try:
                    self.master_templates[layer] = template_file.read_text(encoding='utf-8')
                except Exception as e:
                    print(f"⚠ Warning: Failed to load {filename}: {e}")
            else:
                print(f"⚠ Warning: Master template not found: {filename}")

    def _load_slide_type_templates(self) -> None:
        """Load all 12 slide type templates."""
        types_dir = self.template_dir / "slide_types"

        if not types_dir.exists():
            print(f"⚠ Warning: Slide types template directory not found: {types_dir}")
            return

        # List of expected slide type templates
        slide_types = [
            '01-title', '02-hook', '03-concept', '04-comparison',
            '05-process', '06-example', '07-decision', '08-evidence',
            '09-business', '10-try-with-ai', '11-summary', '12-assessment'
        ]

        for slide_type in slide_types:
            template_file = types_dir / f"{slide_type}.html"
            if template_file.exists():
                try:
                    self.slide_type_templates[slide_type] = template_file.read_text(encoding='utf-8')
                except Exception as e:
                    print(f"⚠ Warning: Failed to load {slide_type}.html: {e}")
            else:
                if DEBUG:
                    print(f"⚠ Debug: Slide type template not found: {slide_type}.html")

    # =====================================================================
    # TEMPLATE RENDERING
    # =====================================================================

    def render_slide(
        self,
        slide_type: str,
        layer: str,
        data: Dict[str, Any]
    ) -> str:
        """
        Render a complete HTML slide from templates.

        Process:
        1. Get master template for pedagogical layer
        2. Get slide type template
        3. Apply layer colors to data
        4. Render slide type template with data
        5. Insert rendered content into master template
        6. Replace all {{variable}} placeholders

        Args:
            slide_type: Slide type ID (e.g., "01-title", "03-concept")
            layer: Pedagogical layer ("L1", "L2", "L3", "L4")
            data: Dictionary of template variables

        Returns:
            Complete HTML string ready for html2pptx.js
        """
        # Get master template for layer
        if layer not in self.master_templates:
            if DEBUG:
                print(f"⚠ Warning: No master template for layer {layer}, using L1")
            layer = 'L1'

        master_html = self.master_templates.get(layer, self.master_templates.get('L1', ''))
        if not master_html:
            raise ValueError(f"No master template available for layer {layer}")

        # Get slide type template
        if slide_type not in self.slide_type_templates:
            if DEBUG:
                print(f"⚠ Warning: Slide type {slide_type} not found, using 03-concept")
            slide_type = '03-concept'

        slide_template = self.slide_type_templates.get(slide_type, '')
        if not slide_template:
            raise ValueError(f"No slide type template available for {slide_type}")

        # Apply layer colors to data
        colors = self._get_layer_colors(layer)
        data['accent_color'] = colors['primary']
        data['accent_bg'] = colors['primary']
        data['accent_border'] = colors['primary']

        # Render slide type template
        slide_content = self._render_template(slide_template, data)

        # Insert slide content into master template
        html = master_html.replace('{{SLIDE_CONTENT}}', slide_content)

        # Replace remaining variables in master
        html = self._replace_variables(html, data)

        return html

    def _render_template(self, template: str, data: Dict[str, Any]) -> str:
        """
        Render a template with variable substitution.

        Supports:
        - {{variable}} → simple replacement
        - {{#list}}...{{/list}} → iteration over list items
        - {{.}} → current list item when inside {{#list}}

        Args:
            template: Template HTML string
            data: Variables dictionary

        Returns:
            Rendered template string
        """
        result = template

        # First, replace simple {{variable}} (non-list)
        for key, value in data.items():
            if isinstance(value, list):
                # Skip lists for now, handle separately
                continue
            result = result.replace(f"{{{{{key}}}}}", str(value) if value is not None else "")

        # Handle {{#list}}...{{/list}} patterns
        for key, value in data.items():
            if not isinstance(value, list):
                continue

            # Find {{#key}}...{{/key}} blocks
            pattern = re.compile(
                rf"{{{{{#{re.escape(key)}}}}(.*?){{{{{/{re.escape(key)}}}}}",
                re.DOTALL
            )

            matches = pattern.findall(result)
            if matches:
                item_template = matches[0]
                rendered_items = []

                for item in value:
                    if isinstance(item, dict):
                        # Item is dictionary - render with item variables
                        rendered = self._render_template(item_template, item)
                    else:
                        # Item is scalar - replace {{.}} with item value
                        rendered = item_template.replace('{{.}}', str(item))

                    rendered_items.append(rendered)

                # Replace the entire {{#key}}...{{/key}} block with rendered items
                result = pattern.sub(''.join(rendered_items), result)

        return result

    def _replace_variables(self, html: str, data: Dict[str, Any]) -> str:
        """
        Replace all {{variable}} placeholders in HTML.

        Args:
            html: HTML string with placeholders
            data: Variables dictionary

        Returns:
            HTML with placeholders replaced
        """
        result = html

        for key, value in data.items():
            if isinstance(value, list):
                # Already handled in _render_template
                continue

            placeholder = f"{{{{{key}}}}}"
            replacement = str(value) if value is not None else ""
            result = result.replace(placeholder, replacement)

        return result

    # =====================================================================
    # HELPER METHODS
    # =====================================================================

    def _get_layer_colors(self, layer: str) -> Dict[str, str]:
        """
        Get color scheme for pedagogical layer.

        Args:
            layer: Layer designation ("L1", "L2", "L3", "L4")

        Returns:
            Dictionary with 'primary', 'dark', 'light' colors
        """
        return LAYER_COLORS.get(layer, LAYER_COLORS['L1']).copy()

    def has_slide_type(self, slide_type: str) -> bool:
        """Check if a slide type template is available."""
        return slide_type in self.slide_type_templates

    def has_layer(self, layer: str) -> bool:
        """Check if a layer master template is available."""
        return layer in self.master_templates

    def get_available_slide_types(self) -> list:
        """Get list of available slide type templates."""
        return sorted(self.slide_type_templates.keys())

    def get_available_layers(self) -> list:
        """Get list of available layer templates."""
        return sorted(self.master_templates.keys())


# =====================================================================
# TESTING
# =====================================================================


if __name__ == "__main__":
    print("Testing TemplateManager:\n")

    # Initialize
    tm = TemplateManager()

    print(f"✓ Available layers: {tm.get_available_layers()}")
    print(f"✓ Available slide types: {tm.get_available_slide_types()}\n")

    # Test rendering
    test_data = {
        'slide_title': 'Test Concept',
        'concept_title': 'What is an Agent?',
        'definition_text': 'An agent is a system that can perceive its environment and take actions.',
        'key_points': [
            'Point 1: Agents have sensors',
            'Point 2: Agents have actuators',
            'Point 3: Agents have intelligence'
        ],
        'additional_context': 'This is additional context about agents.',
        'chapter_number': 5,
        'lesson_number': 2,
        'proficiency_level': 'A2',
        'duration_minutes': 15,
        'slide_number': 3,
        'total_slides': 90,
    }

    try:
        html = tm.render_slide('03-concept', 'L1', test_data)
        print(f"✓ Rendered slide (length: {len(html)} chars)")
        print(f"✓ Contains layer color: {'#4472C4' in html}")
        print(f"✓ Contains slide title: {'Test Concept' in html}")
    except Exception as e:
        print(f"✗ Error rendering slide: {e}")
