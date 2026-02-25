"""Script `get_bl`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import numpy as np

logger = logging.getLogger(__name__)

def bl_height(bl_height, zfull, field):
    """
    Parameters
    ----------
    bl_height : xarray object 3D
        ri number calculated BL height
    zfull : xarray object 4D
        true altitude
    field : xarr object 4D 
        field to slice at bl height 4D
        
    Returns
    -------
    field : 3D array
        field of wind speed at the top of the BL 

    """
    field_bl_top = bl_height.copy()
    p_mask = bl_height.copy()
    for t in range(len(bl_height[:, 0, 0].data)):
        print('Month:', t)
        for i in range(len(bl_height[0, 0, :].data)):
            for j in range(len(bl_height[0, :, 0].data)):
                diff = np.abs(zfull[t, :, j, i].data - bl_height[t, j, i].data)
                idx = np.argmin(diff)
                field_bl_top[t, j, i] = field[t, idx, j, i]
                p_mask[t, j, i] = float(field[t, idx, j, i].pfull.data)
    return (field_bl_top, p_mask)

def bl_height_era5(bl_height, zfull, field):
    """
    Parameters
    ----------
    bl_height : xarray object 3D
        ri number calculated BL height
    zfull : xarray object 4D
        true altitude
    field : xarr object 4D 
        field to slice at bl height 4D
        
    Returns
    -------
    field : 3D array
        field of wind speed at the top of the BL 

    """
    field_bl_top = bl_height.copy()
    p_mask = bl_height.copy()
    for t in range(len(bl_height[:, 0, 0].data)):
        print('Month:', t)
        for i in range(len(bl_height[0, 0, :].data)):
            for j in range(len(bl_height[0, :, 0].data)):
                diff = np.abs(zfull[t, :, j, i].data - bl_height[t, j, i].data)
                idx = np.argmin(diff)
                print(idx, zfull[t, idx, j, i].data, bl_height[t, j, i].data)
                field_bl_top[t, j, i] = field[t, idx, j, i]
                p_mask[t, j, i] = float(field[t, idx, j, i].level.data)
    return (field_bl_top, p_mask)

def bl_height_vectorized(bl_height, zfull, field, zsurf, config):
    """
    Parameters
    ----------
    bl_height : xarray object 3D
        ri number calculated BL height
    zfull : xarray object 4D
        true altitude
    zsurf : xarray object 4D
        surface height
    field : xarr object 4D 
        field to slice at bl height 4D
        
    Returns
    -------
    bl_height: 3D array
        field sliced at the top of the BL 
    p_mask: 3D array 
        pressure mask at the top of the BL
    """
    field_tmp = field.copy()
    field_new = bl_height.copy()
    z_top = bl_height.copy()
    pmask_new = bl_height.copy()
    l, m, n = bl_height.data.shape
    print(l, m, n)
    print(zsurf.shape)
    zsurf = np.resize(zsurf, (l, m, n))
    print('Shape of zsurf is:', zsurf.shape)
    diffs = np.abs(zfull.data - (bl_height.data[:, None, :, :] + zsurf[:, None, :, :]))
    idxs = np.argmin(diffs, axis=1)
    l, m, n = idxs.shape
    I, J, K = np.ogrid[:l, :m, :n]
    field_bl_top = field_tmp.data[I, idxs, J, K]
    ztop = zfull.data[I, idxs, J, K]
    print('The idx mean is:', np.mean(idxs.flatten()))
    z_top.data = ztop
    if config == 'ERA5':
        p_mask = zfull.level.data
    elif config == 'AM4':
        p_mask = zfull.pfull.data
    else:
        raise ValueError('Config is either ERA5 or AM4')
    p_mask = np.broadcast_to(p_mask[:, np.newaxis, np.newaxis], (l, p_mask.size, m, n))
    p_mask = p_mask[I, idxs, J, K]
    print('pmask', p_mask.shape, np.mean(p_mask))
    field_new.data = field_bl_top
    pmask_new.data = p_mask
    print('The mean is:', np.mean(z_top))
    print('The mean is:', np.mean(p_mask))
    return (field_new, pmask_new, z_top)

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
