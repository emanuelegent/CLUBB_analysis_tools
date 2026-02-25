from __future__ import annotations

import argparse
import runpy
from pathlib import Path

from llj.config import load_config
from llj.logging_config import setup_logging

def main() -> None:
    parser = argparse.ArgumentParser(description="Run a script from the LLJ package with a config.")
    parser.add_argument("script", help="Path to a script inside ./scripts (e.g., analyse_llj.py)")
    parser.add_argument("-c", "--config", default="config/config.yaml", help="Path to YAML configuration file.")
    parser.add_argument("--log-level", default=None, help="Override log level (INFO, DEBUG, ...).")
    args = parser.parse_args()

    cfg = load_config(args.config)
    setup_logging(cfg.get("logging", {}), override_level=args.log_level)

    script_path = Path(args.script)
    if not script_path.exists():
        # allow shorthand: name only
        candidate = Path("scripts") / args.script
        if candidate.exists():
            script_path = candidate
        else:
            raise FileNotFoundError(f"Script not found: {args.script}")

    # Provide cfg into script global namespace if needed
    runpy.run_path(str(script_path), init_globals={"CFG": cfg}, run_name="__main__")
