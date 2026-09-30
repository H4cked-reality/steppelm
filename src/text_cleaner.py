import re


def clean_text(text: str) -> str:
    """Clean whitespace while preserving paragraphs and Turkmen characters."""
    cleaned_lines = []

    for line in text.splitlines():
        line = re.sub(r"[ \t]+", " ", line).strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)
