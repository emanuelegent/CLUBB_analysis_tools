# LLJ reproducible analysis package (publication-ready)

This repository contains publication-ready Python scripts for low-level jet (LLJ) diagnostics and related precipitation/wind analyses.

## Quickstart

```bash
# from repo root
python -m pip install -e .
llj-run analyse_llj.py -c config/config.yaml
```

## Configuration

All user-specific paths have been removed. Set your local paths in:

- `config/config.yaml`

Paths are referenced in scripts via:

- `cfg["paths"]["<key>"]`, with fallback to `"your/file/path"`.

## Reproducibility notes

- Deterministic numerical operations may still vary across platforms (BLAS/MKL, etc.).
- For archival, pin dependency versions (see `requirements.txt`) and include your data provenance.

## Contents

- `scripts/`: runnable analysis scripts (auto-cleaned from notebooks)
- `src/llj/`: lightweight utilities for config + logging
- `config/`: YAML configuration templates

## Citation

See `CITATION.cff`.
