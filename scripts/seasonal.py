"""Script `seasonal`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import numpy as np

logger = logging.getLogger(__name__)

class seasonal:

    def __init__(self, var):
        self.var = var

    def seasonal(self, season):
        """
        Parameters
        ----------
        var: xr object
            atmospheric variable to be analysed
        season : string
            string describing season to analyse

        Returns
        -------
        seasonal average

        """
        if season == 'DJF':
            m = 0
            n = 3
        if season == 'MAM':
            m = 3
            n = 6
        if season == 'JJA':
            m = 6
            n = 9
        if season == 'SON':
            m = 9
            n = 12
        seasonal = self.var.data[m:n].mean(axis=0)
        return seasonal

    def get_seasonal_var(self):
        self.djf = self.seasonal('DJF')
        self.mam = self.seasonal('MAM')
        self.jja = self.seasonal('JJA')
        self.son = self.seasonal('SON')
        self.annual = np.median(self.var.data, axis=0)

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
