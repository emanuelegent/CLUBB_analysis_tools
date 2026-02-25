"""Script `plot_diurnal_cycle`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)

def plot_diurnal_cycle(summer_vcomp, labell, sim):
    ds_summer = summer_vcomp.copy()
    lat_bounds = slice(30, 40)
    lon_bounds = slice(260, 265)
    vcomp_gp = ds_summer[labell].sel(lat=lat_bounds, lon=lon_bounds, phalf=slice(300, 1000))
    vcomp_gp = vcomp_gp.sel(time=vcomp_gp['time.month'].isin([6, 7, 8]))
    vcomp_gp = vcomp_gp.mean(dim=['lon', 'lat'])
    diurnal_cycle_gp = vcomp_gp.groupby(vcomp_gp['time.hour']).mean(dim=['time'])
    hour = diurnal_cycle_gp['hour']
    vcomp = diurnal_cycle_gp.values
    utc_offset_central = 5
    hour_local = (diurnal_cycle_gp['hour'] - utc_offset_central) % 24
    print(hour_local.values)
    plt.figure(figsize=(12, 6))
    if labell == 'vcomp':
        levs_diurnal = np.arange(-12, 13, 1)
        pfull = diurnal_cycle_gp['pfull']
        print(pfull)
        contour = plt.contourf(hour, pfull, vcomp[:, :].T, levels=levs_diurnal, cmap='coolwarm', extend='both')
    elif labell == 'vpwp_CLUBB':
        levs_diurnal = np.arange(-0.1, 0.11, 0.01)
        phalf = diurnal_cycle_gp['phalf']
        print(phalf)
        contour = plt.contourf(hour, phalf, vcomp[:, :].T, levels=levs_diurnal, cmap='bwr', extend='both')
        print('ciao')
    elif labell == 'ucomp':
        levs_diurnal = np.arange(-5, 5, 1)
    elif labell == 'upwp_CLUBB':
        levs_diurnal = np.arange(-0.5, 0.51, 0.05)
    else:
        pass
    print(vcomp.T[:, :].shape)
    if labell == 'vcomp':
        plt.colorbar(contour, label=sim + ' vcomp (m/s)')
        levs_diurnal = np.arange(-10, 11, 1)
    elif labell == 'vpwp_CLUBB':
        plt.colorbar(contour, label=sim + ' vpwp (m2/s-2)')
        levs_diurnal = np.arange(-0.1, 0.11, 0.01)
    elif labell == 'ucomp':
        plt.colorbar(contour, label=sim + ' ucomp (m/s)')
        levs_diurnal = np.arange(-5, 5, 1)
    elif labell == 'upwp_CLUBB':
        plt.colorbar(contour, label=sim + ' upwp (m2/s-2)')
        levs_diurnal = np.arange(-0.2, 0.21, 0.02)
    else:
        pass
    plt.title('Diurnal Cycle of vcomp (Great Plains)')
    plt.xlabel('Hour of Day')
    plt.ylabel('Pressure Levels (hPa)')
    plt.gca().invert_yaxis()
    plt.xticks(ticks=hour.values[::3], labels=[19, 22, 1, 4, 7, 10, 13, 16])
    plt.title('Diurnal cycle vpwp at point ' + 'lat 34.5, lon 263.', fontsize=15)
    plt.savefig('your/file/path' + sim + '_' + labell + '.png')
    plt.show()

def plot_diurnal_cycle_prognostic(summer_vcomp, summer_vpwp, labell, labell2, sim):
    ds_summer = summer_vcomp.copy()
    lat_bounds = slice(34, 35)
    lon_bounds = slice(262, 264)
    press_bounds = slice(300, 1000)
    vcomp_gp = ds_summer[labell].sel(lat=lat_bounds, lon=lon_bounds, pfull=press_bounds)
    vcomp_gp = vcomp_gp.sel(time=vcomp_gp['time.month'].isin([6, 7, 8]))
    vcomp_gp = vcomp_gp.mean(dim=['lon', 'lat'])
    diurnal_cycle_gp = vcomp_gp.groupby(vcomp_gp['time.hour']).mean(dim=['time'])
    levs_diurnal = np.arange(-10, 11, 1)
    pfull = diurnal_cycle_gp['pfull']
    max_indices = np.argmax(np.abs(diurnal_cycle_gp.values[:, :]), axis=1)
    max_values = diurnal_cycle_gp.values[:, max_indices]
    above_indices = max_indices - 1
    above_pressure = pfull[above_indices]
    ds_summer_2 = summer_vpwp.copy()
    lat_bounds = slice(34, 35)
    lon_bounds = slice(262, 264)
    vpwp_gp = ds_summer_2[labell2].sel(lat=lat_bounds, lon=lon_bounds, phalf=press_bounds)
    vpwp_gp = vpwp_gp.sel(time=vpwp_gp['time.month'].isin([6, 7, 8]))
    vpwp_gp = vpwp_gp.mean(dim=['lon', 'lat'])
    diurnal_cycle_vpwp_gp = vpwp_gp.groupby(vpwp_gp['time.hour']).mean(dim=['time'])
    phalf = diurnal_cycle_vpwp_gp['phalf']
    sign_changes = np.diff(np.sign(diurnal_cycle_vpwp_gp.values), axis=1) != 0
    sign_change_levels = [phalf[:-1][changes] for changes in sign_changes]
    hour = diurnal_cycle_gp['hour']
    vcomp = diurnal_cycle_gp.values
    utc_offset_central = 5
    hour_local = (diurnal_cycle_gp['hour'] - utc_offset_central) % 24
    plt.figure(figsize=(12, 6))
    contour = plt.contourf(hour, pfull, vcomp[:, :].T, levels=levs_diurnal, cmap='coolwarm', extend='both')
    plt.plot(hour, pfull[max_indices], 'k--', linewidth=1, label='Max Tropo Wind Pressure Level')
    plt.plot(hour, above_pressure, 'b-.', linewidth=1, label='Level Above Max Tropo Wind')
    plt.legend(loc='upper left')
    for i, levels in enumerate(sign_change_levels):
        plt.scatter([hour[i]] * len(levels), levels, color='green', s=10, label='Sign Change' if i == 0 else '')
    print(vcomp.T[:, :].shape)
    if labell == 'vcomp':
        plt.colorbar(contour, label=sim + ' vcomp (m/s)')
    elif labell == 'vpwp_CLUBB':
        plt.colorbar(contour, label=sim + 'vpwp (m2/s-2)')
    elif labell == 'ucomp':
        plt.colorbar(contour, label=sim + 'ucomp (m/s)')
    elif labell == 'upwp_CLUBB':
        plt.colorbar(contour, label=sim + 'upwp (m2/s-2)')
    else:
        pass
    plt.title('Diurnal Cycle of vcomp (Great Plains)')
    plt.xlabel('Hour of Day', fontsize=15)
    plt.ylabel('Pressure Levels (hPa)', fontsize=15)
    plt.title('Diurnal cycle vcomp at point ' + 'lat 34.5, lon 263. Green scatter points where vpwp change sign', fontsize=15)
    plt.gca().invert_yaxis()
    plt.xticks(ticks=hour.values[::3], labels=[19, 22, 1, 4, 7, 10, 13, 16])
    plt.savefig('your/file/path' + sim + '_prog_diag.png')
    plt.show()

def plot_diurnal_cycle_prognostic_inst(summer_vcomp, summer_vpwp, labell, labell2, sim):
    ds_summer = summer_vcomp.copy()
    lat_bounds = slice(34, 35)
    lon_bounds = slice(262, 264)
    press_bounds = slice(300, 1000)
    vcomp_gp = ds_summer[labell].sel(lat=lat_bounds, lon=lon_bounds, pfull=press_bounds)
    vcomp_gp = vcomp_gp.sel(time=vcomp_gp['time.month'].isin([6, 7, 8]))
    diurnal_cycle_gp = vcomp_gp.mean(dim=['lon', 'lat'])
    step = 24 * 45
    diurnal_cycle_gp = diurnal_cycle_gp[step:step + 24, :]
    levs_diurnal = np.arange(-10, 11, 1)
    pfull = diurnal_cycle_gp['pfull']
    max_indices = np.argmax(np.abs(diurnal_cycle_gp.values[:, :]), axis=1)
    max_values = diurnal_cycle_gp.values[:, max_indices]
    above_indices = max_indices - 1
    above_pressure = pfull[above_indices]
    ds_summer_2 = summer_vpwp.copy()
    lat_bounds = slice(34, 35)
    lon_bounds = slice(262, 264)
    vpwp_gp = ds_summer_2[labell2].sel(lat=lat_bounds, lon=lon_bounds, phalf=press_bounds)
    vpwp_gp = vpwp_gp.sel(time=vpwp_gp['time.month'].isin([6, 7, 8]))
    vpwp_gp = vpwp_gp.mean(dim=['lon', 'lat'])
    diurnal_cycle_vpwp_gp = vpwp_gp[step:step + 24, :]
    phalf = diurnal_cycle_vpwp_gp['phalf']
    sign_changes = np.diff(np.sign(diurnal_cycle_vpwp_gp.values), axis=1) != 0
    sign_change_levels = [phalf[:-1][changes] for changes in sign_changes]
    hour = np.arange(24)
    vcomp = diurnal_cycle_gp.values
    plt.figure(figsize=(12, 6))
    contour = plt.contourf(hour, pfull, vcomp[:, :].T, levels=levs_diurnal, cmap='coolwarm', extend='both')
    plt.plot(hour, pfull[max_indices], 'k--', linewidth=1, label='Max Tropo Wind Pressure Level')
    plt.plot(hour, above_pressure, 'b-.', linewidth=1, label='Level Above Max Tropo Wind')
    plt.legend(loc='upper left')
    for i, levels in enumerate(sign_change_levels):
        plt.scatter([hour[i]] * len(levels), levels, color='green', s=10, label='Sign Change' if i == 0 else '')
    print(vcomp.T[:, :].shape)
    if labell == 'vcomp':
        plt.colorbar(contour, label=sim + ' vcomp (m/s)')
    elif labell == 'vpwp_CLUBB':
        plt.colorbar(contour, label=sim + 'vpwp (m2/s-2)')
    elif labell == 'ucomp':
        plt.colorbar(contour, label=sim + 'ucomp (m/s)')
    elif labell == 'upwp_CLUBB':
        plt.colorbar(contour, label=sim + 'upwp (m2/s-2)')
    else:
        pass
    plt.title('Diurnal Cycle of vcomp (Great Plains)')
    plt.xlabel('Hour of Day', fontsize=15)
    plt.ylabel('Pressure Levels (hPa)', fontsize=15)
    plt.title('Diurnal cycle vcomp at point ' + 'lat 34.5, lon 263. Green scatter points where vpwp change sign', fontsize=15)
    plt.gca().invert_yaxis()
    plt.xticks(ticks=hour[::3], labels=[19, 22, 1, 4, 7, 10, 13, 16])
    plt.savefig('your/file/path' + sim + '_prog_diag.png')
    plt.show()

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
