from __future__ import annotations

from pathlib import Path
import yaml

def load_config(path: str | Path) -> dict:
    """Load YAML configuration file.

    Parameters
    ----------
    path
        Path to a YAML config.

    Returns
    -------
    dict
        Configuration dictionary.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    return cfg
