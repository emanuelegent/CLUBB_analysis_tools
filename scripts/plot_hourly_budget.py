"""Script `plot_hourly_budget`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import read_hourly as rh
import upwp_vert_profile as upvp
import upwp_vert_profile as upvp
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import read_hourly as rh
import upwp_vert_profile as upvp
import upwp_vert_profile as upvp
import upwp_vert_profile as upvp
import upwp_vert_profile as upvp

logger = logging.getLogger(__name__)

def run(cfg: dict) -> None:
    local_lon = 262.5

    diurnal_pm = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_pm_tau = rh.AtmosDiagnostics('your/file/path', local_lon)

    gp = [36, 37, 262, 264]

    budgets_vpwp_pm_day = [diurnal_pm.vpwp_bt_day.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).vpwp_bt.mean(dim='time'), diurnal_pm.vpwp_ma_day.vpwp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_ta_day.vpwp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_tp_day.vpwp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_ac_day.vpwp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_bp_day.vpwp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr1_day.vpwp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr2_day.vpwp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr3_day.vpwp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr4_day.vpwp_pr4.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('budget 1')

    budgets_vpwp_pm_tau_day = [diurnal_pm_tau.vpwp_bt_day.vpwp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_ma_day.vpwp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_ta_day.vpwp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_tp_day.vpwp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_ac_day.vpwp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_bp_day.vpwp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr1_day.vpwp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr2_day.vpwp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr3_day.vpwp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr4_day.vpwp_pr4.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('budget 2')

    z_half_pm_day = diurnal_pm.z_half_day.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_pm_tau_day = diurnal_pm_tau.z_half_day.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm_day, z_half_pm_day, 'AM4-CLUBB_PM', 'day')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pmtau_day, z_half_pm_tau, 'AM4-CLUBB_PM_X', 'day')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm_day, z_half_pm_day, 'AM4-CLUBB_PM', 'day')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm_tau_day, z_half_pm_tau_day, 'AM4-CLUBB_PM_X', 'day')

    gp = [36, 37, 262, 264]

    budgets_vpwp_pm_night = [diurnal_pm.vpwp_bt_night.vpwp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_ma_night.vpwp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_ta_night.vpwp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_tp_night.vpwp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_ac_night.vpwp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_bp_night.vpwp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr1_night.vpwp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr2_night.vpwp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr3_night.vpwp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.vpwp_pr4_night.vpwp_pr4.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb1')

    budgets_vpwp_pm_tau_night = [diurnal_pm_tau.vpwp_bt_night.vpwp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_ma_night.vpwp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_ta_night.vpwp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_tp_night.vpwp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_ac_night.vpwp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_bp_night.vpwp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr1_night.vpwp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr2_night.vpwp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr3_night.vpwp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.vpwp_pr4_night.vpwp_pr4.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb2')

    z_half_pm_night = diurnal_pm.z_half_night.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_pm_tau_night = diurnal_pm_tau.z_half_night.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm_night, z_half_pm_night, 'AM4-CLUBB_PM_X', 'night')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm_tau_night, z_half_pm_tau_night, 'AM4-CLUBB_PM_X', 'night')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm_night, z_half_pm_night, 'AM4-CLUBB_PM', 'night')

    upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm_tau_day, z_half_pm_tau_night, 'AM4-CLUBB_PM_X', 'night')

    lonmin = 262

    lonmax = 264

    latmin = 36

    latmax = 37

    zsurf = xr.open_dataset('your/file/path')

    zsurf_val = zsurf.zsurf.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).mean().values

    field = diurnal_pm.ug_vpwp_count_day.ug_vpwp_count.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))[:, :, :]

    profile = field.mean(dim=['lon', 'lat', 'time'])

    vertical_coord = profile['phalf']

    fiel2d = diurnal_pm_tau.ug_vpwp_count_day.ug_vpwp_count.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))[:, :, :]

    profile2 = fiel2d.mean(dim=['lon', 'lat', 'time'])

    vertical_coord2 = profile2['phalf']

    fig, ax = plt.subplots(figsize=(6, 8))

    z_half_pm_day = diurnal_pm.z_half_day.z_half.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).mean(dim='time')[:, 0, 0]

    z_half_pm_tau_day = diurnal_pm_tau.z_half_day.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).z_half.mean(dim='time')[:, 0, 0]

    ax.plot(profile * 90 * 24, z_half_pm_day.values - zsurf_val, marker='o', linestyle='-', color='magenta', label='AM4-CLUBB_PM')

    ax.plot(profile2 * 90 * 12, z_half_pm_tau_day - zsurf_val, marker='o', linestyle='-', color='darkblue', label='AM4-CLUBB_PM_X')

    ax.invert_yaxis()

    ax.set_xlabel("Daytime upgradient $\\overline{v'w'}$ flux count [month$^{-1}$]", fontsize=14)

    ax.set_ylabel('Height from surface [m]', fontsize=14)

    plt.legend(loc='upper left', fontsize=14)

    tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]

    for tick in tickss:
        plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    ax.set_ylim(0, 1500)

    plt.yticks(ticks=tickss, fontsize=12)

    plt.xticks(ticks=[0, 20, 40, 60, 80, 100, 120, 140, 160], fontsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    lonmin = 262

    lonmax = 264

    latmin = 36

    latmax = 37

    zsurf = xr.open_dataset('your/file/path')

    zsurf_val = zsurf.zsurf.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).mean().values

    field = diurnal_pm.ug_vpwp_count_night.ug_vpwp_count.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))[:, :, :]

    profile = field.mean(dim=['lon', 'lat', 'time'])

    vertical_coord = profile['phalf']

    fiel2d = diurnal_pm_tau.ug_vpwp_count_night.ug_vpwp_count.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))[:, :, :]

    profile2 = fiel2d.mean(dim=['lon', 'lat', 'time'])

    vertical_coord2 = profile2['phalf']

    fig, ax = plt.subplots(figsize=(6, 8))

    z_half_pm_night = diurnal_pm.z_half_night.z_half.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).mean(dim='time')[:, 0, 0]

    z_half_pm_tau_night = diurnal_pm_tau.z_half_night.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).z_half.mean(dim='time')[:, 0, 0]

    ax.plot(profile * 90 * 24, z_half_pm_night.values - zsurf_val, marker='o', linestyle='-', color='magenta', label='AM4-CLUBB_PM')

    ax.plot(profile2 * 90 * 12, z_half_pm_tau_day - zsurf_val, marker='o', linestyle='-', color='darkblue', label='AM4-CLUBB_PM_X')

    ax.invert_yaxis()

    ax.set_xlabel("Nighttime upgradient $\\overline{v'w'}$ flux count [month$^{-1}$]", fontsize=14)

    ax.set_ylabel('Height from surface [m]', fontsize=14)

    plt.legend(loc='upper left', fontsize=14)

    tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]

    for tick in tickss:
        plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    ax.set_ylim(0, 1900)

    plt.yticks(ticks=tickss, fontsize=12)

    plt.xticks(ticks=[0, 20, 40, 60, 80, 100, 120], fontsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    diurnal_pm.vpwp_bt_night.vpwp_bt

    local_lon = 262.5

    diurnal_dm = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_dm_tau = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_pm = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_pm_tau = rh.AtmosDiagnostics('your/file/path', local_lon)

    gp = [36, 37, 262, 264]

    budgets_wprtp_dm_night = [diurnal_dm.wprtp_bt_night.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_ma_night.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_ta_night.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_tp_night.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_ac_night.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_bp_night.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_pr1_night.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_pr2_night.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_pr3_night.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb_dm')

    budgets_wprtp_dm_tau_night = [diurnal_dm_tau.wprtp_bt_night.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_ma_night.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_ta_night.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_tp_night.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_ac_night.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_bp_night.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_pr1_night.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_pr2_night.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_pr3_night.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb_dm')

    budgets_wprtp_pm_night = [diurnal_pm.wprtp_bt_night.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_ma_night.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_ta_night.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_tp_night.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_ac_night.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_bp_night.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_pr1_night.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_pr2_night.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_pr3_night.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb1')

    budgets_wprtp_pm_tau_night = [diurnal_pm_tau.wprtp_bt_night.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_ma_night.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_ta_night.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_tp_night.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_ac_night.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_bp_night.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_pr1_night.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_pr2_night.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_pr3_night.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb2')

    z_half_dm_night = diurnal_dm.z_half_night.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_dm_tau_night = diurnal_dm_tau.z_half_night.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_pm_night = diurnal_pm.z_half_night.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_pm_tau_night = diurnal_pm_tau.z_half_night.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_dm_night, z_half_dm_night, 'night', 'AM4-CLUBB_DM')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_dm_tau_night, z_half_dm_tau_night, 'night', 'AM4-CLUBB_DM_X')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_pm_night, z_half_pm_night, 'night', 'AM4-CLUBB_PM')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_pm_tau_night, z_half_pm_tau_night, 'night', 'AM4-CLUBB_PM_X')

    gp = [36, 37, 262, 264]

    budgets_wprtp_dm_day = [diurnal_dm.wprtp_bt_day.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_ma_day.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_ta_day.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_tp_day.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_ac_day.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_bp_day.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_pr1_day.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_pr2_day.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm.wprtp_pr3_day.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb_dm')

    budgets_wprtp_dm_tau_day = [diurnal_dm_tau.wprtp_bt_night.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_ma_day.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_ta_day.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_tp_day.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_ac_day.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_bp_day.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_pr1_day.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_pr2_day.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_dm_tau.wprtp_pr3_day.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb_dm')

    budgets_wprtp_pm_day = [diurnal_pm.wprtp_bt_day.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_ma_day.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_ta_day.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_tp_day.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_ac_day.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_bp_day.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_pr1_day.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_pr2_day.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm.wprtp_pr3_day.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb1')

    budgets_wprtp_pm_tau_day = [diurnal_pm_tau.wprtp_bt_day.wprtp_bt.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_ma_day.wprtp_ma.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_ta_day.wprtp_ta.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_tp_day.wprtp_tp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_ac_day.wprtp_ac.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_bp_day.wprtp_bp.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_pr1_day.wprtp_pr1.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_pr2_day.wprtp_pr2.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time'), diurnal_pm_tau.wprtp_pr3_day.wprtp_pr3.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')]

    print('clubb2')

    z_half_dm_day = diurnal_dm.z_half_day.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_dm_tau_day = diurnal_dm_tau.z_half_day.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_pm_day = diurnal_pm.z_half_day.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    z_half_pm_tau_day = diurnal_pm_tau.z_half_day.z_half.sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3])).mean(dim='time')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_dm_day, z_half_dm_day, 'day', 'AM4-CLUBB_DM')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_dm_tau_day, z_half_dm_tau_day, 'day', 'AM4-CLUBB_DM_X')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_pm_day, z_half_pm_day, 'day', 'AM4-CLUBB_PM')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_pm_tau_day, z_half_pm_tau_day, 'day', 'AM4-CLUBB_PM_X')

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
