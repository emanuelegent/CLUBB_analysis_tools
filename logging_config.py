from __future__ import annotations

import logging
import logging.config

def setup_logging(cfg: dict | None = None, override_level: str | None = None) -> None:
    """Configure logging from a dict-like config.

    The YAML config should contain a `logging` section following Python's
    `logging.config.dictConfig` schema.

    If not provided, a sensible default is used.
    """
    cfg = cfg or {}
    if "version" not in cfg:
        # Default: human-readable console logs
        cfg = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {"format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"}
            },
            "handlers": {
                "console": {"class": "logging.StreamHandler", "formatter": "standard", "level": "INFO"}
            },
            "root": {"handlers": ["console"], "level": "INFO"},
        }

    if override_level:
        # Override root + all handler levels
        cfg = dict(cfg)  # shallow copy
        if "root" in cfg and isinstance(cfg["root"], dict):
            cfg["root"] = dict(cfg["root"])
            cfg["root"]["level"] = override_level
        for h in (cfg.get("handlers") or {}).values():
            if isinstance(h, dict):
                h["level"] = override_level

    logging.config.dictConfig(cfg)
