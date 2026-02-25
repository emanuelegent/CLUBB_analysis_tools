"""Script `paper_clubb_pressure_levs`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import manage_nc as mn
import plot_summer_wind as psw
import xarray as xr
import plot_summer_wind as psw
import xarray as xr
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import numpy as np
import xarray as xr
import read_summer_wind as rsw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import xarray as xr
import plot_summer_wind as psw

logger = logging.getLogger(__name__)

def run(cfg: dict) -> None:
    filename_am4_lock = 'your/file/path'

    filename_am4_clubb_dm = 'your/file/path'

    filename_am4_clubb_pm = 'your/file/path'

    filename_am4_clubb_pm_nsconv = 'your/file/path'

    am4_lock = mn.manage_am4(filename_am4_lock, 'lock', None, True, False, True)

    am4_clubb_dm = mn.manage_am4(filename_am4_clubb_dm, 'dm', None, True, False, True)

    am4_clubb_pm = mn.manage_am4(filename_am4_clubb_pm, 'pm', None, True, False, True)

    am4_clubb_pm_nosconv = mn.manage_am4(filename_am4_clubb_pm_nsconv, 'pm_nosconv', 31, True, False, True)

    era5_925_summer = xr.open_dataset('your/file/path')

    era5_925_summer_mean = era5_925_summer.mean(dim='date')

    psw.plot_wind_vector_meridional_era5(era5_925_summer_mean.u[0, :, :], era5_925_summer_mean.v[0, :, :], label='ERA5 925hPa Meridional Wind')

    psw.plot_wind_vector_meridional_era5(era5_925_summer_mean.u[0, :, :], era5_925_summer_mean.v[0, :, :], label='ERA5 925hPa Meridional Wind')

    psw.plot_wind_vector_meridional(am4_lock.ucomp.object, am4_lock.vcomp.object, label='AM4 Meridional Wind at 925 hPa')

    psw.plot_wind_vector_meridional(am4_clubb_dm.ucomp.object, am4_clubb_dm.vcomp.object, label='AM4-CLUBB_DM Meridional Wind at 925 hPa')

    psw.plot_wind_vector_meridional(am4_clubb_pm.ucomp.object, am4_clubb_pm.vcomp.object, label='AM4-CLUBB_PM Meridional Wind at 925 hPa')

    psw.plot_wind_vector_meridional(am4_clubb_pm_nosconv.ucomp.object, am4_clubb_pm_nosconv.vcomp.object, label='AM4-CLUBB_PM_nosconv Meridional Wind at 925 hPa')

    era5_925_summer = xr.open_dataset('your/file/path')

    era5_925_summer_mean = era5_925_summer.mean(dim='date')

    target_grid = am4_clubb_pm_nosconv.ucomp.object

    new_lats = target_grid['lat']

    new_lons = target_grid['lon']

    era5_925_summer_mean_rg = era5_925_summer_mean.interp(latitude=new_lats, longitude=new_lons, method='linear')

    masked_data = era5_925_summer_mean_rg.where(~np.isnan(am4_clubb_pm_nosconv.ucomp.object[:, 1, :, :]), np.nan)

    psw.plot_wind_vector_meridional_era5(masked_data.u[0, :, :, 0], masked_data.v[0, :, :, 0], label='ERA5 925hPa Meridional Wind')

    path_ctrl = cfg.get('paths', {}).get('ctrl', 'your/file/path')

    ctrl_u10m_summer, ctrl_v10m_summer, ctrl_u925_summer, ctrl_v925_summer, ctrl_u_summer, ctrl_v_summer = rsw.read_wind(path_ctrl)

    path_dm = cfg.get('paths', {}).get('dm', 'your/file/path')

    dm_u10m_summer, dm_v10m_summer, dm_u925_summer, dm_v925_summer, dm_u_summer, dm_v_summer = rsw.read_wind(path_dm)

    path_pm_only = cfg.get('paths', {}).get('pm_only', 'your/file/path')

    pm_u10m_summer, pm_v10m_summer, pm_u925_summer, pm_v925_summer, pm_u_summer, pm_v_summer = rsw.read_wind(path_pm_only)

    path_pm_nsconv = cfg.get('paths', {}).get('pm_nsconv', 'your/file/path')

    pm_nsconv_u10m_summer, pm_nsconv_v10m_summer, pm_nsconv_u925_summer, pm_nsconv_v925_summer, pm_nsconv_u_summer, pm_nsconv_v_summer = rsw.read_wind(path_pm_nsconv)

    psw.plot_meridional_structure(ctrl_v_summer, 'AM4')

    psw.plot_meridional_structure(dm_v_summer, 'AM4-CLUBB_DM')

    psw.plot_meridional_structure(pm_v_summer, 'AM4-CLUBB_PM')

    psw.plot_meridional_structure(pm_nsconv_v_summer, 'AM4-CLUBB_PM_nosconv')

    masked_data = xr.open_dataset('your/file/path')

    psw.plot_meridional_structure(masked_data.v, 'ERA5', True)

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
