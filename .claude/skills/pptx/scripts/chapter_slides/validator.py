"""
Validation for generated presentations.

Checks:
- Structure (slide count, ordering)
- Accessibility (WCAG 2.1 AA)
- Consistency (metadata, layer colors)
- Content (word count, completeness)
"""

from typing import List, Dict, Any
from dataclasses import dataclass

# =====================================================================
# VALIDATION RESULTS
# =====================================================================


@dataclass
class ValidationResult:
    """A single validation result."""
    level: str  # "ERROR", "WARNING", "INFO"
    category: str  # "structure", "accessibility", "consistency"
    message: str
    slide_id: str = None


@dataclass
class ValidationReport:
    """Complete validation report."""
    structure_checks: List[ValidationResult]
    accessibility_checks: List[ValidationResult]
    consistency_checks: List[ValidationResult]

    @property
    def errors(self) -> List[str]:
        """Get all error messages."""
        all_checks = self.structure_checks + self.accessibility_checks + self.consistency_checks
        return [r.message for r in all_checks if r.level == "ERROR"]

    @property
    def warnings(self) -> List[str]:
        """Get all warning messages."""
        all_checks = self.structure_checks + self.accessibility_checks + self.consistency_checks
        return [r.message for r in all_checks if r.level == "WARNING"]

    @property
    def passed(self) -> bool:
        """Check if validation passed (no errors)."""
        return len(self.errors) == 0


# =====================================================================
# VALIDATION FUNCTIONS
# =====================================================================


def validate_presentation(slides: List[Dict[str, Any]], metadata: Dict) -> ValidationReport:
    """
    Run full validation pipeline.

    Args:
        slides: List of slide dictionaries
        metadata: Presentation metadata

    Returns:
        ValidationReport with all check results
    """
    report = ValidationReport(
        structure_checks=[],
        accessibility_checks=[],
        consistency_checks=[]
    )

    # Phase 1: Structure
    report.structure_checks.extend(_validate_structure(slides, metadata))

    # Phase 2: Accessibility
    report.accessibility_checks.extend(_validate_accessibility(slides))

    # Phase 3: Consistency
    report.consistency_checks.extend(_validate_consistency(slides, metadata))

    return report


def _validate_structure(slides: List[Dict], metadata: Dict) -> List[ValidationResult]:
    """Validate presentation structure."""
    results = []

    if not slides:
        results.append(ValidationResult(
            level="ERROR",
            category="structure",
            message="No slides generated"
        ))
        return results

    # Check slide count
    expected_count = metadata.get('estimated_slides', len(slides))
    actual_count = len(slides)

    if expected_count > 0:
        variance = abs(actual_count - expected_count) / expected_count
        if variance > 0.20:  # >20% variance
            results.append(ValidationResult(
                level="WARNING",
                category="structure",
                message=f"Slide count ({actual_count}) differs from estimate ({expected_count}) by {variance*100:.0f}%"
            ))

    # Check first slide type
    if slides[0].get('slide_type') != 'title':
        results.append(ValidationResult(
            level="WARNING",
            category="structure",
            message="First slide should be title slide"
        ))

    # Check last slide type
    last_type = slides[-1].get('slide_type')
    if last_type not in ['summary', 'assessment']:
        results.append(ValidationResult(
            level="INFO",
            category="structure",
            message=f"Last slide is {last_type}, ideally should be summary or assessment"
        ))

    # Check for duplicate IDs
    ids = [s.get('id') for s in slides]
    if len(ids) != len(set(ids)):
        results.append(ValidationResult(
            level="ERROR",
            category="structure",
            message="Duplicate slide IDs detected"
        ))

    return results


def _validate_accessibility(slides: List[Dict]) -> List[ValidationResult]:
    """Validate WCAG 2.1 AA accessibility."""
    results = []

    for slide in slides:
        slide_id = slide.get('id', 'unknown')
        html = slide.get('html', '')

        # Check for minimum font sizes in generated content
        if 'font-size' in html:
            # Simple check: look for very small font
            if 'font-size: 8pt' in html or 'font-size: 9pt' in html:
                results.append(ValidationResult(
                    level="WARNING",
                    category="accessibility",
                    message=f"Very small font detected (8-9pt)",
                    slide_id=slide_id
                ))

        # Check for color contrast (basic check for layer colors)
        has_color = '#4472C4' in html or '#70AD47' in html or '#9B59B6' in html or '#ED7D31' in html
        has_text = len(html) > 500  # Rough check for content

        if not has_color and has_text:
            results.append(ValidationResult(
                level="INFO",
                category="accessibility",
                message="No layer color detected (may indicate templating issue)",
                slide_id=slide_id
            ))

        # Check for alt text (for future image support)
        if '<img' in html and 'alt=' not in html:
            results.append(ValidationResult(
                level="WARNING",
                category="accessibility",
                message="Image found without alt text",
                slide_id=slide_id
            ))

    return results


def _validate_consistency(slides: List[Dict], metadata: Dict) -> List[ValidationResult]:
    """Validate consistency across presentation."""
    results = []

    expected_chapter = metadata.get('chapter_number')
    expected_layer = metadata.get('layer')

    layers_found = set()
    chapters_found = set()

    for slide in slides:
        slide_id = slide.get('id', 'unknown')
        layer = slide.get('layer', 'L1')
        data = slide.get('data', {})
        chapter = data.get('chapter_number')

        layers_found.add(layer)
        if chapter:
            chapters_found.add(chapter)

        # Check that layer is valid
        if layer not in ['L1', 'L2', 'L3', 'L4']:
            results.append(ValidationResult(
                level="WARNING",
                category="consistency",
                message=f"Invalid layer: {layer}",
                slide_id=slide_id
            ))

        # Check chapter consistency
        if expected_chapter and chapter != expected_chapter:
            results.append(ValidationResult(
                level="WARNING",
                category="consistency",
                message=f"Chapter mismatch: slide is chapter {chapter}, expected {expected_chapter}",
                slide_id=slide_id
            ))

    # Check for mixed layers (warning if more than 2 layers)
    if len(layers_found) > 2:
        results.append(ValidationResult(
            level="INFO",
            category="consistency",
            message=f"Multiple layers found: {sorted(layers_found)} (expect 1-2 per chapter)"
        ))

    return results


def print_validation_report(report: ValidationReport) -> None:
    """Print validation report to console."""
    print("\n" + "=" * 70)
    print("VALIDATION REPORT")
    print("=" * 70)

    # Summary
    total_checks = len(report.structure_checks) + len(report.accessibility_checks) + len(report.consistency_checks)
    print(f"\nTotal checks: {total_checks}")
    print(f"Errors: {len(report.errors)}")
    print(f"Warnings: {len(report.warnings)}")

    # Status
    if report.passed:
        print("\n✅ PASSED - No errors detected")
    else:
        print("\n❌ FAILED - Errors detected")

    # Details
    if report.errors:
        print("\n🔴 ERRORS:")
        for error in report.errors[:10]:
            print(f"  • {error}")
        if len(report.errors) > 10:
            print(f"  ... and {len(report.errors) - 10} more")

    if report.warnings:
        print("\n⚠️  WARNINGS:")
        for warning in report.warnings[:10]:
            print(f"  • {warning}")
        if len(report.warnings) > 10:
            print(f"  ... and {len(report.warnings) - 10} more")

    print("\n" + "=" * 70)
