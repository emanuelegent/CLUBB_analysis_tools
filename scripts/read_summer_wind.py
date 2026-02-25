"""Script `read_summer_wind`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import xarray as xr

logger = logging.getLogger(__name__)

def read_wind(path):
    """
    path: simulation path where archive data are stored
    """
    june = xr.open_dataset(path + 'your/file/path')
    july = xr.open_dataset(path + 'your/file/path')
    august = xr.open_dataset(path + 'your/file/path')
    u10m_summer = june.u_ref.copy()[0, :, :]
    u10m_summer.data = (june.u_ref[0, :, :].data + july.u_ref[0, :, :].data + august.u_ref[0, :, :].data) / 3.0
    v10m_summer = june.v_ref.copy()[0, :, :]
    v10m_summer.data = (june.v_ref[0, :, :].data + july.v_ref[0, :, :].data + august.v_ref[0, :, :].data) / 3.0
    u925_summer = june.ucomp.copy()[0, 1, :, :]
    u925_summer.data = (june.ucomp[0, 1, :, :].data + july.ucomp[0, 1, :, :].data + august.ucomp[0, 1, :, :].data) / 3.0
    import numpy as np
    v925_summer = june.vcomp.copy()[0, 1, :, :]
    v925_summer.data = np.mean([june.vcomp[0, 1, :, :].data, july.vcomp[0, 1, :, :].data, august.vcomp[0, 1, :, :].data], axis=0)
    u_summer = june.ucomp.copy()[0, :, :, :]
    u_summer.data = (june.ucomp[0, :, :, :].data + july.ucomp[0, :, :, :].data + august.ucomp[0, :, :, :].data) / 3.0
    v_summer = june.vcomp.copy()[0, :, :, :]
    v_summer.data = (june.vcomp[0, :, :, :].data + july.vcomp[0, :, :, :].data + august.vcomp[0, :, :, :].data) / 3.0
    sphum = june.sphum.copy()[0, :, :, :]
    sphum.data = (june.sphum[0, :, :, :].data + july.sphum[0, :, :, :].data + august.sphum[0, :, :, :].data) / 3.0
    return (u10m_summer, v10m_summer, u925_summer, v925_summer, u_summer, v_summer, sphum)

def read_wind_nsconv(path):
    """
    path: simulation path where archive data are stored
    """
    june = xr.open_dataset(path + 'your/file/path')
    july = xr.open_dataset(path + 'your/file/path')
    august = xr.open_dataset(path + 'your/file/path')
    u10m_summer = june.u_ref.copy()[0, :, :]
    u10m_summer.data = (june.u_ref[0, :, :].data + july.u_ref[0, :, :].data + august.u_ref[0, :, :].data) / 3.0
    v10m_summer = june.v_ref.copy()[0, :, :]
    v10m_summer.data = (june.v_ref[0, :, :].data + july.v_ref[0, :, :].data + august.v_ref[0, :, :].data) / 3.0
    u925_summer = june.ucomp.copy()[0, 1, :, :]
    u925_summer.data = (june.ucomp[0, 1, :, :].data + july.ucomp[0, 1, :, :].data + august.ucomp[0, 1, :, :].data) / 3.0
    v925_summer = june.vcomp.copy()[0, 1, :, :]
    v925_summer.data = (june.vcomp[0, 1, :, :].data + july.vcomp[0, 1, :, :].data + august.vcomp[0, 1, :, :].data) / 3.0
    u_summer = june.ucomp.copy()[0, :, :, :]
    u_summer.data = (june.ucomp[0, :, :, :].data + july.ucomp[0, :, :, :].data + august.ucomp[0, :, :, :].data) / 3.0
    v_summer = june.vcomp.copy()[0, :, :, :]
    v_summer.data = (june.vcomp[0, :, :, :].data + july.vcomp[0, :, :, :].data + august.vcomp[0, :, :, :].data) / 3.0
    sphum = june.sphum.copy()[0, :, :, :]
    sphum.data = (june.sphum[0, :, :, :].data + july.sphum[0, :, :, :].data + august.sphum[0, :, :, :].data) / 3.0
    return (u10m_summer, v10m_summer, u925_summer, v925_summer, u_summer, v_summer, sphum)

def read_wind_nsconv_temp(path):
    """
    path: simulation path where archive data are stored
    """
    june = xr.open_dataset(path + 'your/file/path')
    july = xr.open_dataset(path + 'your/file/path')
    august = xr.open_dataset(path + 'your/file/path')
    u10m_summer = june.u_ref.copy()[0, :, :]
    u10m_summer.data = (june.u_ref[0, :, :].data + july.u_ref[0, :, :].data + august.u_ref[0, :, :].data) / 3.0
    v10m_summer = june.v_ref.copy()[0, :, :]
    v10m_summer.data = (june.v_ref[0, :, :].data + july.v_ref[0, :, :].data + august.v_ref[0, :, :].data) / 3.0
    u925_summer = june.ucomp.copy()[0, 1, :, :]
    u925_summer.data = (june.ucomp[0, 1, :, :].data + july.ucomp[0, 1, :, :].data + august.ucomp[0, 1, :, :].data) / 3.0
    v925_summer = june.vcomp.copy()[0, 1, :, :]
    v925_summer.data = (june.vcomp[0, 1, :, :].data + july.vcomp[0, 1, :, :].data + august.vcomp[0, 1, :, :].data) / 3.0
    u_summer = june.ucomp.copy()[0, :, :, :]
    u_summer.data = (june.ucomp[0, :, :, :].data + july.ucomp[0, :, :, :].data + august.ucomp[0, :, :, :].data) / 3.0
    v_summer = june.vcomp.copy()[0, :, :, :]
    v_summer.data = (june.vcomp[0, :, :, :].data + july.vcomp[0, :, :, :].data + august.vcomp[0, :, :, :].data) / 3.0
    sphum = june.sphum.copy()[0, :, :, :]
    sphum.data = (june.sphum[0, :, :, :].data + july.sphum[0, :, :, :].data + august.sphum[0, :, :, :].data) / 3.0
    return (u10m_summer, v10m_summer, u925_summer, v925_summer, u_summer, v_summer, sphum)

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
