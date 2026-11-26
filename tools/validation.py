
import re


REQUIRED_SECTIONS = [
    "Topic",
    "Simple Explanation",
    "Key Concepts",
    "Example",
    "Practice Exercise",
    "Common Mistakes",
    "Review Comments",
    "Final Summary",
]


def validate_required_sections(markdown: str) -> dict:
    """Check whether Markdown contains all required headings."""

    headings = re.findall(
        r"^#{1,6}\s+(.+?)\s*#*\s*$",
        markdown,
        flags=re.MULTILINE
    )

    normalized_headings = [
        heading.strip().lower()
        for heading in headings
    ]

    missing = []

    for section in REQUIRED_SECTIONS:
        section_found = any(
            heading == section.lower()
            or (
                section == "Topic"
                and heading.startswith("topic:")
            )
            for heading in normalized_headings
        )

        if not section_found:
            missing.append(section)

    return {
        "is_valid": len(missing) == 0,
        "missing_sections": missing
    }

