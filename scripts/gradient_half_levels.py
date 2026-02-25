"""Script `gradient_half_levels`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import numpy as np

logger = logging.getLogger(__name__)

def compute_dx_dz_phalf(um, zfull, zhalf):
    """
    Compute dx/dz at phalf levels given um at pfull levels and zfull at pfull levels.
    
    Parameters:
        um (numpy array): Wind speed at pfull levels (size = kdim, e.g., 33).
        zfull (numpy array): Heights or pressures at pfull levels (size = kdim, e.g., 33).

    Returns:
        numpy array: Vertical gradient du/dz at phalf levels (size = kdim + 1, e.g., 34).
    """
    kdim = len(um)
    du_dz = np.zeros(kdim + 1)
    du_dz[0] = 0
    for k in range(1, kdim - 1):
        du_dz[k] = (um[k] - um[k - 1]) / (zfull[k] - zfull[k - 1])
    du_dz[kdim] = (0 - um[kdim - 1]) / (zhalf[kdim] - zfull[kdim - 1])
    return du_dz

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
