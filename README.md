# steppelm

## Current files and folders

- `README.md` — project overview and learning notes
- `requirements.txt` — Python dependencies
- `data/` — source and prepared datasets
- `src/` — Python source code
- `tests/` — tests for the code you write
- `checkpoints/` — saved model weights (later)

## First task

Choose one Turkmen text file from the dataset. Note its filename, format, and the field containing the text. No code is needed for this step.

## Prepare the training dataset

The initial pipeline reads page-level JSON files from `tm-data`, removes empty
lines, normalizes repeated spaces, and preserves Turkmen characters. It writes
one cleaned page per line in JSONL format, together with its source and page
number.

Initialize the dataset submodule after cloning the repository:

```bash
git submodule update --init --recursive
```

Prepare the dataset:

```bash
python3 src/prepare_dataset.py
```

The generated file is written to `data/processed/train.jsonl`. Generated data
is ignored by Git and can be rebuilt from the source data at any time.

Run the cleaning tests:

```bash
python3 -m unittest discover -s tests
```
