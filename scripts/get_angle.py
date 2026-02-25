"""Script `get_angle`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import numpy as np
import numpy.linalg as la

logger = logging.getLogger(__name__)

def turning(surf, bl_top):
    """
    Parameters
    ----------
    surf : surface wind vector
        1x2 array
    bl_top : wind vector at bl top
        1x2 array

    Returns
    -------
    Th : wind turning angle
        scalar, float

    """
    cosTh = np.dot(surf, bl_top) / (np.linalg.norm(surf) * np.linalg.norm(bl_top))
    sinTh = np.cross(surf, bl_top) / (np.linalg.norm(surf) * np.linalg.norm(bl_top))
    Th = np.rad2deg(np.arctan2(sinTh, cosTh))
    return Th

def turning_domain(ucomp_10, vcomp_10, ucomp_bl, vcomp_bl):
    """
    Parameters
    ----------
    ucomp_10 : 
        DESCRIPTION.
    vcomp_10 : TYPE
        DESCRIPTION.
    ucomp_bl : TYPE
        DESCRIPTION.
    vcomp_bl : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    angle = ucomp_10.copy()
    for t in range(12):
        print(t)
        for i in range(len(ucomp_10[0, 0, :])):
            for j in range(len(vcomp_10[0, :, 0])):
                wind_10 = np.array([ucomp_10[t, j, i], vcomp_10[t, j, i]])
                wind_bl = np.array([ucomp_bl[t, j, i], vcomp_bl[t, j, i]])
                angle[t, j, i] = turning(wind_10, wind_bl)
    return angle

def turning_vectorized(ucomp_10, vcomp_10, ucomp_bl, vcomp_bl):
    """
    Parameters
    ----------
    ucomp_10 : 
        DESCRIPTION.
    vcomp_10 : TYPE
        DESCRIPTION.
    ucomp_bl : TYPE
        DESCRIPTION.
    vcomp_bl : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    angle = ucomp_10.copy()
    wind_10 = np.vstack(([ucomp_10.data.T], [vcomp_10.data.T])).T
    wind_bl = np.vstack(([ucomp_bl.data.T], [vcomp_bl.data.T])).T
    cosTh = np.sum(wind_10 * wind_bl, axis=3)
    sinTh = np.cross(wind_10, wind_bl)
    Th = np.rad2deg(np.arctan2(sinTh, cosTh))
    angle.data = -Th
    return angle

def turning_vectorized_new(ucomp_10, vcomp_10, ucomp_bl, vcomp_bl):
    """
    Parameters
    ----------
    ucomp_10 : 
        DESCRIPTION.
    vcomp_10 : TYPE
        DESCRIPTION.
    ucomp_bl : TYPE
        DESCRIPTION.
    vcomp_bl : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    angle = ucomp_10.copy()
    wind_10 = np.vstack(([ucomp_10.data.T], [vcomp_10.data.T])).T
    wind_bl = np.vstack(([ucomp_bl.data.T], [vcomp_bl.data.T])).T
    cosTh = np.sum(wind_10 * wind_bl, axis=3)
    sinTh = np.cross(wind_10, wind_bl)
    Th = np.rad2deg(np.arctan2(sinTh, cosTh))
    angle.data = -Th
    return angle

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
