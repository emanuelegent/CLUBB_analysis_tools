"""Script `plot_hourly`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import xarray as xr
import read_hourly as rh
import momentum_diagnostics as md
import momentum_diagnostics as md
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import manage_nc as mn
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import plot_summer_wind as psw
import upwp_vert_profile as upvp
import upwp_vert_profile as upvp
import upwp_vert_profile as upvp
import upwp_vert_profile as upvp
import xarray as xr

logger = logging.getLogger(__name__)

def generate_input_day(sim):
    input_list = [sim.udt_vdif_day.udt_vdif.mean(dim='time'), sim.vdt_vdif_day.vdt_vdif.mean(dim='time'), sim.z_full_day.z_full.mean(dim='time'), sim.z_half_day.z_half.mean(dim='time'), sim.ucomp_day.ucomp.mean(dim='time'), sim.vcomp_day.vcomp.mean(dim='time')]
    return input_list

def generate_input_day_clubb(sim):
    input_list = [sim.udt_CLUBB_day.udt_CLUBB.mean(dim='time'), sim.vdt_CLUBB_day.vdt_CLUBB.mean(dim='time'), sim.z_full_day.z_full.mean(dim='time'), sim.z_half_day.z_half.mean(dim='time'), sim.ucomp_day.ucomp.mean(dim='time'), sim.vcomp_day.vcomp.mean(dim='time')]
    return input_list

def generate_input_night(sim):
    input_list = [sim.udt_vdif_night.udt_vdif.mean(dim='time'), sim.vdt_vdif_night.vdt_vdif.mean(dim='time'), sim.z_full_night.z_full.mean(dim='time'), sim.z_half_night.z_half.mean(dim='time'), sim.ucomp_night.ucomp.mean(dim='time'), sim.vcomp_night.vcomp.mean(dim='time')]
    return input_list

def generate_input_night_clubb(sim):
    input_list = [sim.udt_CLUBB_night.udt_CLUBB.mean(dim='time'), sim.vdt_CLUBB_night.vdt_CLUBB.mean(dim='time'), sim.z_full_night.z_full.mean(dim='time'), sim.z_half_night.z_half.mean(dim='time'), sim.ucomp_night.ucomp.mean(dim='time'), sim.vcomp_night.vcomp.mean(dim='time')]
    return input_list

def run(cfg: dict) -> None:
    years = range(2013, 2026)

    files = [f'your/file/path' for year in years if year != 2021]

    datasets = [xr.open_dataset(f) for f in files]

    arm_stacked = xr.concat(datasets, dim='time')

    arm_summer = arm_stacked.sel(time=arm_stacked['time'].dt.month.isin([6, 7, 8]))

    arm_summer_diurnal = arm_summer.sel(time=arm_summer['time'].dt.hour.isin(range(6, 18)))

    arm_summer_diurnal_mean = arm_summer_diurnal.mean(dim='time')

    arm_summer_diurnal_mean.to_netcdf('your/file/path')

    arm_summer_nocturnal = arm_summer.sel(time=~arm_summer['time'].dt.hour.isin(range(6, 18)))

    arm_summer_nocturnal_mean = arm_summer_nocturnal.mean(dim='time')

    arm_summer_nocturnal_mean.to_netcdf('your/file/path')

    diurnal_pm = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_pm_tau = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_dm = rh.AtmosDiagnostics('your/file/path', local_lon)

    local_lon = 262.5

    diurnal_am4 = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_dm = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_dm_tau = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_pm = rh.AtmosDiagnostics('your/file/path', local_lon)

    diurnal_pm_tau = rh.AtmosDiagnostics('your/file/path', local_lon)

    am4_input = generate_input_day(diurnal_am4)

    lock_dm_mom = md.momentum_diagnostics_diurnal(am4_input[0], am4_input[1], am4_input[2], am4_input[3], am4_input[4], am4_input[5])

    lock_dm_mom.manage_diagnostics()

    print('dm')

    dm_input = generate_input_day_clubb(diurnal_dm)

    clubb_dm_mom = md.momentum_diagnostics_diurnal(dm_input[0], dm_input[1], dm_input[2], dm_input[3], dm_input[4], dm_input[5])

    clubb_dm_mom.manage_diagnostics()

    print('pm')

    dm_tau_input = generate_input_day_clubb(diurnal_dm_tau)

    clubb_dm_mom_tau = md.momentum_diagnostics_diurnal(dm_tau_input[0], dm_tau_input[1], dm_tau_input[2], dm_tau_input[3], dm_tau_input[4], dm_tau_input[5])

    clubb_dm_mom_tau.manage_diagnostics()

    print('pm')

    pm_input = generate_input_day_clubb(diurnal_pm)

    clubb_pm_mom = md.momentum_diagnostics_diurnal(pm_input[0], pm_input[1], pm_input[2], pm_input[3], pm_input[4], pm_input[5])

    clubb_pm_mom.manage_diagnostics()

    print('pm_tau')

    pm_tau_input = generate_input_day_clubb(diurnal_pm_tau)

    clubb_tau_mom = md.momentum_diagnostics_diurnal(pm_tau_input[0], pm_tau_input[1], pm_tau_input[2], pm_tau_input[3], pm_tau_input[4], pm_tau_input[5])

    clubb_tau_mom.manage_diagnostics()

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'vcomp'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom.v_comp, clubb_dm_mom.v_comp, clubb_dm_mom_tau.v_comp, clubb_pm_mom.v_comp, clubb_tau_mom.v_comp], [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull], [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf], [diurnal_am4.z_Ri_025_day.z_Ri_025, diurnal_dm.z_Ri_025_day.z_Ri_025, diurnal_dm_tau.z_Ri_025_day.z_Ri_025, diurnal_pm.z_Ri_025_day.z_Ri_025, diurnal_pm_tau.z_Ri_025_day.z_Ri_025], 'v_comp', coords, 'day')

    p_mom_diag.plot_diagnostics(save_fig)

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'ucomp'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom.u_comp, clubb_dm_mom.u_comp, clubb_dm_mom_tau.u_comp, clubb_pm_mom.u_comp, clubb_tau_mom.u_comp], [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull], [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf], [diurnal_am4.z_Ri_025_day.z_Ri_025, diurnal_dm.z_Ri_025_day.z_Ri_025, diurnal_dm_tau.z_Ri_025_day.z_Ri_025, diurnal_pm.z_Ri_025_day.z_Ri_025, diurnal_pm_tau.z_Ri_025_day.z_Ri_025], 'u_comp', coords, 'day')

    p_mom_diag.plot_diagnostics(save_fig)

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'k_m'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom.k_m, clubb_dm_mom.k_m, clubb_dm_mom_tau.k_m, clubb_pm_mom.k_m, clubb_tau_mom.k_m], [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull], [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf], [diurnal_am4.z_Ri_025_day.z_Ri_025, diurnal_dm.z_Ri_025_day.z_Ri_025, diurnal_dm_tau.z_Ri_025_day.z_Ri_025, diurnal_pm.z_Ri_025_day.z_Ri_025, diurnal_pm_tau.z_Ri_025_day.z_Ri_025], 'k_m', coords, 'day')

    p_mom_diag.plot_diagnostics(save_fig)

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'dir'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom.dir, clubb_dm_mom.dir, clubb_dm_mom_tau.dir, clubb_pm_mom.dir, clubb_tau_mom.dir], [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull], [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf], [diurnal_am4.z_Ri_025_day.z_Ri_025, diurnal_dm.z_Ri_025_day.z_Ri_025, diurnal_dm_tau.z_Ri_025_day.z_Ri_025, diurnal_pm.z_Ri_025_day.z_Ri_025, diurnal_pm_tau.z_Ri_025_day.z_Ri_025], 'dir', coords, 'day')

    p_mom_diag.plot_diagnostics(save_fig)

    am4_input = generate_input_night(diurnal_am4)

    lock_dm_mom_night = md.momentum_diagnostics_diurnal(am4_input[0], am4_input[1], am4_input[2], am4_input[3], am4_input[4], am4_input[5])

    lock_dm_mom_night.manage_diagnostics()

    print('dm')

    dm_input = generate_input_night_clubb(diurnal_dm)

    clubb_dm_mom_night = md.momentum_diagnostics_diurnal(dm_input[0], dm_input[1], dm_input[2], dm_input[3], dm_input[4], dm_input[5])

    clubb_dm_mom_night.manage_diagnostics()

    print('dm_tau')

    dm_tau_input = generate_input_night_clubb(diurnal_dm_tau)

    clubb_dm_mom_tau_night = md.momentum_diagnostics_diurnal(dm_tau_input[0], dm_tau_input[1], dm_tau_input[2], dm_tau_input[3], dm_tau_input[4], dm_tau_input[5])

    clubb_dm_mom_tau_night.manage_diagnostics()

    print('pm')

    pm_input = generate_input_night_clubb(diurnal_pm)

    clubb_pm_mom_night = md.momentum_diagnostics_diurnal(pm_input[0], pm_input[1], pm_input[2], pm_input[3], pm_input[4], pm_input[5])

    clubb_pm_mom_night.manage_diagnostics()

    print('pm_tau')

    pm_tau_input = generate_input_night_clubb(diurnal_pm_tau)

    clubb_tau_mom_night = md.momentum_diagnostics_diurnal(pm_tau_input[0], pm_tau_input[1], pm_tau_input[2], pm_tau_input[3], pm_tau_input[4], pm_tau_input[5])

    clubb_tau_mom_night.manage_diagnostics()

    print('dm_tau')

    dm_tau_input = generate_input_night_clubb(diurnal_dm_tau)

    clubb_dm_mom_tau_night = md.momentum_diagnostics_diurnal(dm_tau_input[0], dm_tau_input[1], dm_tau_input[2], dm_tau_input[3], dm_tau_input[4], dm_tau_input[5])

    clubb_dm_mom_tau_night.manage_diagnostics()

    print('pm')

    pm_input = generate_input_night_clubb(diurnal_pm)

    clubb_pm_mom_night = md.momentum_diagnostics_diurnal(pm_input[0], pm_input[1], pm_input[2], pm_input[3], pm_input[4], pm_input[5])

    clubb_pm_mom_night.manage_diagnostics()

    print('pm_tau')

    pm_tau_input = generate_input_night_clubb(diurnal_pm_tau)

    clubb_tau_mom_night = md.momentum_diagnostics_diurnal(pm_tau_input[0], pm_tau_input[1], pm_tau_input[2], pm_tau_input[3], pm_tau_input[4], pm_tau_input[5])

    clubb_tau_mom_night.manage_diagnostics()

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'ucomp'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom_night.u_comp, clubb_dm_mom.u_comp, clubb_dm_mom_tau_night.u_comp, clubb_pm_mom_night.u_comp, clubb_tau_mom_night.u_comp], [lock_dm_mom_night.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau_night.zfull, clubb_pm_mom_night.zfull, clubb_tau_mom_night.zfull], [lock_dm_mom_night.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau_night.zhalf, clubb_pm_mom_night.zhalf, clubb_tau_mom_night.zhalf], [diurnal_am4.z_Ri_025_night.z_Ri_025, diurnal_dm.z_Ri_025_night.z_Ri_025, diurnal_dm_tau.z_Ri_025_night.z_Ri_025, diurnal_pm.z_Ri_025_night.z_Ri_025, diurnal_pm_tau.z_Ri_025_night.z_Ri_025], 'u_comp', coords, 'night')

    p_mom_diag.plot_diagnostics(save_fig)

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'vcomp'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom_night.v_comp, clubb_dm_mom.v_comp, clubb_dm_mom_tau_night.v_comp, clubb_pm_mom_night.v_comp, clubb_tau_mom_night.v_comp], [lock_dm_mom_night.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau_night.zfull, clubb_pm_mom_night.zfull, clubb_tau_mom_night.zfull], [lock_dm_mom_night.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau_night.zhalf, clubb_pm_mom_night.zhalf, clubb_tau_mom_night.zhalf], [diurnal_am4.z_Ri_025_night.z_Ri_025, diurnal_dm.z_Ri_025_night.z_Ri_025, diurnal_dm_tau.z_Ri_025_night.z_Ri_025, diurnal_pm.z_Ri_025_night.z_Ri_025, diurnal_pm_tau.z_Ri_025_night.z_Ri_025], 'v_comp', coords, 'night')

    p_mom_diag.plot_diagnostics(save_fig)

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'dir'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom_night.dir, clubb_dm_mom.dir, clubb_dm_mom_tau_night.dir, clubb_pm_mom_night.dir, clubb_tau_mom_night.dir], [lock_dm_mom_night.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom_night.zfull, clubb_tau_mom_night.zfull], [lock_dm_mom_night.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom_night.zhalf, clubb_tau_mom_night.zhalf], [diurnal_am4.z_Ri_025_night.z_Ri_025, diurnal_dm.z_Ri_025_night.z_Ri_025, diurnal_dm_tau.z_Ri_025_night.z_Ri_025, diurnal_pm.z_Ri_025_night.z_Ri_025, diurnal_pm_tau.z_Ri_025_night.z_Ri_025], 'dir', coords, 'night')

    p_mom_diag.plot_diagnostics(save_fig)

    coords_gp = [36, 37, 262, 264]

    coords = coords_gp

    save_fig = 'k_m'

    p_mom_diag = md.plot_momentum_diagnostics_diurnal([lock_dm_mom_night.k_m, clubb_dm_mom.k_m, clubb_dm_mom_tau_night.k_m, clubb_pm_mom_night.k_m, clubb_tau_mom_night.k_m], [lock_dm_mom_night.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau_night.zfull, clubb_pm_mom_night.zfull, clubb_tau_mom_night.zfull], [lock_dm_mom_night.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau_night.zhalf, clubb_pm_mom_night.zhalf, clubb_tau_mom_night.zhalf], [diurnal_am4.z_Ri_025_night.z_Ri_025, diurnal_dm.z_Ri_025_night.z_Ri_025, diurnal_dm_tau.z_Ri_025_night.z_Ri_025, diurnal_pm.z_Ri_025_night.z_Ri_025, diurnal_pm_tau.z_Ri_025_night.z_Ri_025], 'k_m', coords, 'night')

    p_mom_diag.plot_diagnostics(save_fig)

    lonmin = 262

    lonmax = 264

    latmin = 36

    latmax = 37

    zsurf = xr.open_dataset('your/file/path')

    zsurf_val = zsurf.zsurf.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).mean().values

    field = diurnal_pm.ug_vpwp_count_night.ug_vpwp_count[0, :, :, :]

    subset = field.sel(lon=slice(261, 262), lat=slice(30, 31))

    profile = subset.mean(dim=['lon', 'lat'])

    vertical_coord = profile['phalf']

    zhalf_slice = am4_clubb_pm.zhalf.object.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))

    vpwp_slice = am4_clubb_pm.vpwp_CLUBB.object.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))

    vpwp_slice_mean = vpwp_slice.mean(dim=['lat', 'lon']).values

    max_vpwp = np.max(abs(vpwp_slice_mean))

    field2 = am4_clubb_pm_tau.ug_vpwp_count.object[0, :, :, :]

    subset2 = field2.sel(lon=slice(261, 262), lat=slice(30, 31))

    profile2 = subset2.mean(dim=['lon', 'lat'])

    vertical_coord2 = profile2['phalf']

    zhalf_slice2 = am4_clubb_pm_tau.zhalf.object.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))

    vpwp_slice2 = am4_clubb_pm_tau.vpwp_CLUBB.object.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax))

    vpwp_slice_mean2 = vpwp_slice2.mean(dim=['lat', 'lon']).values

    max_vpwp2 = np.max(abs(vpwp_slice_mean2))

    fig, ax = plt.subplots(figsize=(6, 8))

    ax.plot(profile * 90 * 24, zhalf_slice.mean(dim=['lat', 'lon']).values[0, :] - zsurf_val, marker='o', linestyle='-', color='magenta', label='AM4-CLUBB_PM')

    ax.plot(profile2 * 90 * 24, zhalf_slice2.mean(dim=['lat', 'lon']).values[0, :] - zsurf_val, marker='o', linestyle='-', color='darkblue', label='AM4-CLUBB_PM_X')

    ax.invert_yaxis()

    ax.set_xlabel("Upgradient $\\overline{v'w'}$ flux count [month$^{-1}$]", fontsize=14)

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

    a = xr.open_dataset(path)

    filename_am4_lock = 'your/file/path'

    filename_am4_clubb_dm = 'your/file/path'

    filename_am4_clubb_dm_tau = 'your/file/path'

    filename_am4_clubb_pm = 'your/file/path'

    filename_am4_clubb_pm_tau = 'your/file/path'

    am4_lock = mn.manage_am4(filename_am4_lock, 'lock', 3, True, False, True)

    am4_clubb_dm = mn.manage_am4(filename_am4_clubb_dm, 'dm', 3, True, False, True)

    am4_clubb_dm_tau = mn.manage_am4(filename_am4_clubb_dm_tau, 'tau', 3, True, False, True)

    am4_clubb_pm = mn.manage_am4(filename_am4_clubb_pm, 'pm', 3, True, False, True)

    am4_clubb_pm_tau = mn.manage_am4(filename_am4_clubb_pm_tau, 'tau', 3, True, False, True)

    am4_lock.cape.object[0, :, :]

    psw.plot_cape_conus(am4_lock.cape.object[0, :, :], 'AM4')

    psw.plot_cape_conus(am4_clubb_dm.cape.object[0, :, :], 'AM4-CLUBB_DM')

    psw.plot_cape_conus(am4_clubb_pm.cape.object[0, :, :], 'AM4-CLUBB_PM')

    psw.plot_cape_conus(am4_clubb_dm_tau.cape.object[0, :, :], 'AM4-CLUBB_DM_X')

    psw.plot_cape_conus(am4_clubb_pm_tau.cape.object[0, :, :], 'AM4-CLUBB_PM_X', 'plasma')

    psw.plot_tot_cld_amt(am4_lock.tot_cld_amt.object[0, :, :], 'AM4')

    psw.plot_tot_cld_amt(am4_clubb_dm.tot_cld_amt.object[0, :, :], 'AM4-CLUBB_DM')

    psw.plot_tot_cld_amt(am4_clubb_dm_tau.tot_cld_amt.object[0, :, :], 'AM4-CLUBB_DM_X')

    psw.plot_tot_cld_amt(am4_clubb_pm.tot_cld_amt.object[0, :, :], 'AM4-CLUBB_PM')

    psw.plot_tot_cld_amt(am4_clubb_pm_tau.tot_cld_amt.object[0, :, :], 'AM4-CLUBB_PM_X')

    psw.plot_low_cld_amt(am4_lock.low_cld_amt.object[0, :, :], 'AM4')

    psw.plot_low_cld_amt(am4_clubb_dm.low_cld_amt.object[0, :, :], 'AM4-CLUBB_DM')

    psw.plot_low_cld_amt(am4_clubb_dm_tau.low_cld_amt.object[0, :, :], 'AM4-CLUBB_DM_X')

    psw.plot_low_cld_amt(am4_clubb_pm.low_cld_amt.object[0, :, :], 'AM4-CLUBB_PM')

    psw.plot_low_cld_amt(am4_clubb_pm_tau.low_cld_amt.object[0, :, :], 'AM4-CLUBB_PM_X')

    psw.plot_mid_cld_amt(am4_lock.mid_cld_amt.object[0, :, :], 'AM4')

    psw.plot_mid_cld_amt(am4_clubb_dm.mid_cld_amt.object[0, :, :], 'AM4-CLUBB_DM')

    psw.plot_mid_cld_amt(am4_clubb_dm_tau.mid_cld_amt.object[0, :, :], 'AM4-CLUBB_DM_X')

    psw.plot_mid_cld_amt(am4_aclubb_pm.mid_cld_amt.object[0, :, :], 'AM4-CLUBB_PM')

    psw.plot_mid_cld_amt(am4_clubb_pm_tau.mid_cld_amt.object[0, :, :], 'AM4-CLUBB_PM_X')

    psw.plot_high_cld_amt(am4_lock.high_cld_amt.object[0, :, :], 'AM4')

    psw.plot_high_cld_amt(am4_clubb_dm.high_cld_amt.object[0, :, :], 'AM4-CLUBB_DM')

    psw.plot_high_cld_amt(am4_clubb_dm_tau.high_cld_amt.object[0, :, :], 'AM4-CLUBB_DM_X')

    psw.plot_high_cld_amt(am4_clubb_pm.high_cld_amt.object[0, :, :], 'AM4-CLUBB_PM')

    psw.plot_high_cld_amt(am4_clubb_pm_tau.high_cld_amt.object[0, :, :], 'AM4-CLUBB_PM_X')

    budgets_wprtp_dm = [am4_clubb_dm.wrtp_bt.object, am4_clubb_dm.wrtp_ma.object, am4_clubb_dm.wrtp_ta.object, am4_clubb_dm.wrtp_tp.object, am4_clubb_dm.wrtp_ac.object, am4_clubb_dm.wrtp_bp.object, am4_clubb_dm.wrtp_pr1.object, am4_clubb_dm.wrtp_pr2.object, am4_clubb_dm.wrtp_pr3.object]

    budgets_wprtp_dm_tau = [am4_clubb_dm_tau.wrtp_bt.object, am4_clubb_dm_tau.wrtp_ma.object, am4_clubb_dm_tau.wrtp_ta.object, am4_clubb_dm_tau.wrtp_tp.object, am4_clubb_dm_tau.wrtp_ac.object, am4_clubb_dm_tau.wrtp_bp.object, am4_clubb_dm_tau.wrtp_pr1.object, am4_clubb_dm_tau.wrtp_pr2.object, am4_clubb_dm_tau.wrtp_pr3.object]

    budgets_wprtp_pm = [am4_clubb_pm.wrtp_bt.object, am4_clubb_pm.wrtp_ma.object, am4_clubb_pm.wrtp_ta.object, am4_clubb_pm.wrtp_tp.object, am4_clubb_pm.wrtp_ac.object, am4_clubb_pm.wrtp_bp.object, am4_clubb_pm.wrtp_pr1.object, am4_clubb_pm.wrtp_pr2.object, am4_clubb_pm.wrtp_pr3.object]

    budgets_wprtp_pm_tau = [am4_clubb_pm_tau.wrtp_bt.object, am4_clubb_pm_tau.wrtp_ma.object, am4_clubb_pm_tau.wrtp_ta.object, am4_clubb_pm_tau.wrtp_tp.object, am4_clubb_pm_tau.wrtp_ac.object, am4_clubb_pm_tau.wrtp_bp.object, am4_clubb_pm_tau.wrtp_pr1.object, am4_clubb_pm_tau.wrtp_pr2.object, am4_clubb_pm_tau.wrtp_pr3.object]

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_dm, am4_clubb_dm.zhalf.object, 'AM4-CLUBB_DM')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_dm_tau, am4_clubb_dm_tau.zhalf.object, 'AM4-CLUBB_DM_X')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_pm, am4_clubb_pm.zhalf.object, 'AM4-CLUBB_PM')

    upvp.plot_rtpwp_vertical_profile_all(budgets_wprtp_pm_tau, am4_clubb_pm_tau.zhalf.object, 'AM4-CLUBB_PM_tau')

    file = 'your/file/path'

    a = xr.open_dataset(file)

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
