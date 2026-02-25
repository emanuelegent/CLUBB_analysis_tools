"""Script `read_diurnal`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import xarray as xr

logger = logging.getLogger(__name__)

def read_diurnal_cycle(filename):
    ucomp = xr.open_dataset(filename + 'atmos_level.0002010100-0002123123.ucomp.nc')
    vcomp = xr.open_dataset(filename + 'atmos_level.0002010100-0002123123.vcomp.nc')
    upwp = xr.open_dataset(filename + 'atmos_level.0002010100-0002123123.upwp_CLUBB.nc')
    vpwp = xr.open_dataset(filename + 'atmos_level.0002010100-0002123123.vpwp_CLUBB.nc')
    return (ucomp, vcomp, upwp, vpwp)

def run(cfg: dict) -> None:
    logger.info('Nothing to run (no top-level executable statements).')

def main() -> None:
    import argparse
    from llj.config import load_config
    from llj.logging_config import setup_logging

    parser = argparse.ArgumentParser(description="Run LLJ analysis script.")
    parser.add_argument("-c", "--config", default="config/config.yaml", help="Path to YAML configuration file.")
    parser.add_argument("--log-level", default=None, help="Override log level (e.g., INFO, DEBUG).")
    args = parser.parse_args()

    cfg = load_config(args.config)
    setup_logging(cfg.get("logging", {}), override_level=args.log_level)

    logger.info("Loaded config from %s", args.config)
    run(cfg)

if __name__ == "__main__":
    main()
