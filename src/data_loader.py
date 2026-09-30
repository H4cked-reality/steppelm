"""Utilities for reading page-level story data from tm-data."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STORY_PATH = (
    PROJECT_ROOT
    / "data"
    / "tm-data"
    / "stories"
    / "nejep-oglan"
    / "nejep_oglan_-_dessan.json"
)


def iter_story_texts(path: Path = DEFAULT_STORY_PATH) -> Iterator[str]:
    """Yield non-empty page texts from a tm-data story JSON file."""
    with path.open(encoding="utf-8") as file:
        document = json.load(file)

    pages = document.get("pages")
    if not isinstance(pages, list):
        raise ValueError(f"Expected a 'pages' list in {path}")

    for page in pages:
        if not isinstance(page, dict):
            raise ValueError(f"Expected every page in {path} to be an object")

        text = page.get("text")
        if isinstance(text, str) and text.strip():
            yield text.strip()


if __name__ == "__main__":
    texts = list(iter_story_texts())
    character_count = sum(len(text) for text in texts)
    print(f"Loaded {len(texts)} non-empty pages ({character_count} characters).")
