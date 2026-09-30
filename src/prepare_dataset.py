"""Build a cleaned JSONL training dataset from tm-data stories."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from text_cleaner import clean_text


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_DIR = PROJECT_ROOT / "data" / "tm-data" / "stories"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "train.jsonl"


def prepare_dataset(input_dir: Path, output_path: Path) -> int:
    """Clean story pages and write one JSON object per output line."""
    json_paths = sorted(input_dir.rglob("*.json"))
    if not json_paths:
        raise FileNotFoundError(f"No JSON files found under {input_dir}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    record_count = 0

    with output_path.open("w", encoding="utf-8") as output_file:
        for json_path in json_paths:
            with json_path.open(encoding="utf-8") as input_file:
                document = json.load(input_file)

            pages = document.get("pages")
            if not isinstance(pages, list):
                raise ValueError(f"Expected a 'pages' list in {json_path}")

            source = json_path.relative_to(input_dir).as_posix()

            for page in pages:
                if not isinstance(page, dict):
                    raise ValueError(f"Expected every page in {json_path} to be an object")

                raw_text = page.get("text")
                if not isinstance(raw_text, str):
                    continue

                text = clean_text(raw_text)
                if not text:
                    continue

                record = {
                    "text": text,
                    "source": source,
                    "page": page.get("page_number"),
                }
                output_file.write(json.dumps(record, ensure_ascii=False) + "\n")
                record_count += 1

    return record_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare cleaned Turkmen story data as JSONL."
    )
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    record_count = prepare_dataset(args.input_dir, args.output)
    print(f"Wrote {record_count} records to {args.output}")


if __name__ == "__main__":
    main()
