"""Script `analyse_llj`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import xarray as xr
import read_summer_wind as rsw
import read_summer_wind as rsw
import read_summer_wind as rsw
import read_summer_wind as rsw
import plot_summer_wind as psw
import xarray as xr
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
import matplotlib.pyplot as plt
import numpy as np
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
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import xarray as xr
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import xarray as xr
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cmocean
import matplotlib.pyplot as plt
import numpy as np
import cmocean
import matplotlib.pyplot as plt
import numpy as np
import cmocean
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)

def run(cfg: dict) -> None:
    path_ctrl = cfg.get('paths', {}).get('ctrl', 'your/file/path')

    ctrl_u10m_summer, ctrl_v10m_summer, ctrl_u925_summer, ctrl_v925_summer, ctrl_u_summer, ctrl_v_summer, ctrl_sphum = rsw.read_wind(path_ctrl)

    path_dm = cfg.get('paths', {}).get('dm', 'your/file/path')

    dm_u10m_summer, dm_v10m_summer, dm_u925_summer, dm_v925_summer, dm_u_summer, dm_v_summer, dm_sphum = rsw.read_wind_nsconv(path_dm)

    path_dm_tau = cfg.get('paths', {}).get('dm_tau', 'your/file/path')

    dmtau_u10m_summer, dmtau_v10m_summer, dmtau_u925_summer, dmtau_v925_summer, dmtau_u_summer, dmtau_v_summer, dmtau_sphum = rsw.read_wind_nsconv_temp(path_dm_tau)

    path_pm_only = cfg.get('paths', {}).get('pm_only', 'your/file/path')

    pm_u10m_summer, pm_v10m_summer, pm_u925_summer, pm_v925_summer, pm_u_summer, pm_v_summer, pm_sphum = rsw.read_wind_nsconv(path_pm_only)

    path_pm_tau = cfg.get('paths', {}).get('pm_tau', 'your/file/path')

    pmtau_u10m_summer, pmtau_v10m_summer, pmtau_u925_summer, pmtau_v925_summer, pmtau_u_summer, pmtau_v_summer, pmtau_sphum = rsw.read_wind_nsconv_temp(path_pm_tau)

    era5_925_summer = xr.open_dataset('your/file/path')

    era5_925_summer_mean = era5_925_summer.mean(dim='date')

    psw.plot_wind_vector_meridional_era5(era5_925_summer_mean.u[0, :, :], era5_925_summer_mean.v[0, :, :], label='ERA5 925hPa $v$')

    psw.plot_wind_vector_meridional(ctrl_u925_summer, ctrl_v925_summer, label='AM4 $v$ at 925 hPa')

    psw.plot_wind_vector_meridional(dm_u925_summer, dm_v925_summer, label='AM4-CLUBB_DM $v$ at 925 hPa')

    psw.plot_wind_vector_meridional(pm_u925_summer, pm_v925_summer, label='AM4-CLUBB_PM $v$ at 925 hPa')

    psw.plot_wind_vector_meridional(dmtau_u925_summer, dmtau_v925_summer, label='AM4-CLUBB_DM_X $v$ at 925 hPa')

    psw.plot_wind_vector_meridional(pmtau_u925_summer, pmtau_v925_summer, label='AM4-CLUBB_PM_X $v$ at 925 hPa')

    psw.plot_wind_vector_meridional(pm_u925_summer, pm_v925_summer, label='AM4-CLUBB_PM $v$ at 925 hPa')

    psw.plot_wind_vector_meridional_diff(ctrl_v925_summer, dm_v925_summer, 'AM4', 'AM4-CLUBB_DM', 'diff')

    psw.plot_wind_vector_meridional_diff(dm_v925_summer, pm_v925_summer, 'AM4-CLUBB_DM', 'AM4-CLUBB_PM', 'diff')

    psw.plot_wind_vector_meridional_diff(dm_v925_summer, dmtau_v925_summer, 'AM4-CLUBB_DM', 'AM4-CLUBB_DM_X', 'diff')

    psw.plot_wind_vector_meridional_diff(pm_v925_summer, pmtau_v925_summer, 'AM4-CLUBB_PM', 'AM4-CLUBB_PM_X', 'diff')

    psw.plot_structure_wind(ctrl_v_summer, 'AM4')

    psw.plot_structure_wind(dm_v_summer, 'AM4-CLUBB_DM')

    psw.plot_structure_wind_diff(ctrl_v_summer, dm_v_summer, 'AM4', 'AM4-CLUBB_DM')

    psw.plot_structure_wind(pm_v_summer, 'AM4-CLUBB_PM')

    psw.plot_structure_wind_diff(dm_v_summer, pm_v_summer, 'AM4-CLUBB_DM', 'AM4-CLUBB_PM')

    psw.plot_structure_wind(dmtau_v_summer, 'AM4-CLUBB_DM_X')

    psw.plot_structure_sphum(ctrl_sphum, 'AM4')

    psw.plot_structure_wind_diff(dm_v_summer, dmtau_v_summer, 'AM4-CLUBB_DM', 'AM4-CLUBB_DM_X')

    psw.plot_structure_wind_diff(pm_v_summer, pmtau_v_summer, 'AM4-CLUBB_PM', 'AM4-CLUBB_PM_X')

    vcomp = pm_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg_pm = lat_range.mean(dim='lat')

    diff = vcomp_avg_pm - vcomp_avg_dm

    plt.figure(figsize=(10, 7), dpi=150)

    levels = np.arange(-1.0, 1.1, 0.25)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level, diff, levels=levels, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    cbar = plt.colorbar()

    cbar.ax.tick_params(labelsize=12)

    cbar.set_label('AM4-CLUBB_PM - AM4-CLUBB_DM Meridional wind $v$ [m s$^{-1}]$', fontsize=12)

    plt.xlabel('Longitude (degrees)', fontsize=12)

    plt.ylabel('Pressure (hPa)', fontsize=12)

    plt.tick_params(axis='x', labelsize=12)

    plt.tick_params(axis='y', labelsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    psw.plot_structure_wind(dmtau_v_summer, 'AM4-CLUBB_DM_X')

    psw.plot_structure_wind(pmtau_v_summer, 'AM4-CLUBB_PM_X')

    psw.plot_structure_sphum(ctrl_sphum, 'AM4')

    psw.plot_structure_sphum(dm_sphum, 'AM4-CLUBB_DM')

    psw.plot_structure_sphum(pm_sphum, 'AM4-CLUBB_PM')

    psw.plot_structure_sphum(pmtau_sphum, 'AM4-CLUBB_PM_X')

    psw.plot_structure_sphum(dmtau_sphum, 'AM4-CLUBB_DM_X')

    psw.plot_structure_sphum_diff(ctrl_sphum, dm_sphum, 'AM4', 'AM4-CLUBB_DM')

    psw.plot_structure_sphum_diff(dm_sphum, pm_sphum, 'AM4-CLUBB_DM', 'AM4-CLUBB_PM')

    psw.plot_structure_sphum_diff(dm_sphum, dmtau_sphum, 'AM4-CLUBB_DM', 'AM4-CLUBB_DM_X')

    psw.plot_structure_sphum_diff(pm_sphum, pmtau_sphum, 'AM4-CLUBB_PM', 'AM4-CLUBB_PM_X')

    psw.plot_structure_sphum_lat(ctrl_sphum, 'AM4')

    psw.plot_structure_sphum_lat(dm_sphum, 'AM4-CLUBB_DM')

    psw.plot_structure_sphum_lat(pm_sphum, 'AM4-CLUBB_PM')

    psw.plot_structure_sphum_lat(pmtau_sphum, 'AM4-CLUBB_PM_X')

    psw.plot_structure_sphum_lat(dmtau_sphum, 'AM4-CLUBB_DM_X')

    psw.plot_structure_sphum_diff_lat(ctrl_sphum, dm_sphum, 'AM4', 'AM4-CLUBB_DM')

    psw.plot_structure_sphum_diff_lat(dm_sphum, pm_sphum, 'AM4-CLUBB_DM', 'AM4-CLUBB_PM')

    psw.plot_structure_sphum_diff_lat(dm_sphum, dmtau_sphum, 'AM4-CLUBB_DM', 'AM4-CLUBB_DM_X')

    psw.plot_structure_sphum_diff_lat(pm_sphum, pmtau_sphum, 'AM4-CLUBB_PM', 'AM4-CLUBB_PM_X')

    psw.plot_specific_humidity_conus(ctrl_sphum, 925, 'AM4')

    psw.plot_specific_humidity_conus(dm_sphum, 925, 'AM4-CLUBB_DM')

    psw.plot_specific_humidity_conus(pm_sphum, 925, 'AM4-CLUBB_PM')

    psw.plot_specific_humidity_conus(pmtau_sphum, 925, 'AM4-CLUBB_PM_X')

    psw.plot_specific_humidity_conus(dmtau_sphum, 925, 'AM4-CLUBB_DM_X')

    psw.plot_q_diff(ctrl_sphum.sel(level=925), dm_sphum.sel(level=925), 'AM4', 'AM4-CLUBB_DM', 'qdiff')

    psw.plot_q_diff(dm_sphum.sel(level=925), pm_sphum.sel(level=925), 'AM4-CLUBB_DM', 'AM4-CLUBB_PM', 'qdiff')

    psw.plot_q_diff(dm_sphum.sel(level=925), dmtau_sphum.sel(level=925), 'AM4-CLUBB_DM', 'AM4-CLUBB_DM_X', 'qdiff')

    psw.plot_q_diff(pm_sphum.sel(level=925), pmtau_sphum.sel(level=925), 'AM4-CLUBB_PM', 'AM4-CLUBB_PM_X', 'qdiff')

    vcomp = pmtau_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg = lat_range.mean(dim='lat')

    plt.figure(figsize=(10, 6))

    levels = np.arange(-7.5, 7.5, 2.5)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level, vcomp_avg, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    vcomp = pm_nsconv_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg = lat_range.mean(dim='lat')

    plt.figure(figsize=(10, 6))

    levels = np.arange(-7.5, 7.5, 2.5)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level, vcomp_avg, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    vcomp = dm_nsconv_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg = lat_range.mean(dim='lat')

    plt.figure(figsize=(10, 6))

    levels = np.arange(-7.5, 7.5, 2.5)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level, vcomp_avg, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    precip_am4 = xr.open_dataset('your/file/path')

    precip.coords['time']

    precip

    precip_am4 = xr.open_dataset('your/file/path')

    ds = precip_am4

    lat_min, lat_max = (30, 50)

    lon_min, lon_max = (260, 280)

    precip_gp = ds['precip'].sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

    time_in_hours = np.array([t.hour for t in ds['time'].values])

    precip_gp.coords['hour_of_day'] = ('time', time_in_hours)

    summer_months = [6, 7, 8]

    summer_precip_gp = precip_gp.sel(time=precip_gp['time'].dt.month.isin(summer_months))

    diurnal_cycle = summer_precip_gp.groupby('hour_of_day').mean(dim=['time', 'lat', 'lon'])

    plt.figure(figsize=(10, 6))

    plt.plot(np.arange(1.5, 24, 3), diurnal_cycle, marker='o', linestyle='-', color='b')

    plt.title('Diurnal Cycle of Precipitation over US Great Plains (Summer Months Only)')

    plt.xlabel('Hour of the Day (UTC)')

    plt.ylabel('Precipitation (mm/hr)')

    plt.grid(True)

    plt.xticks(np.arange(1.5, 24, 3))

    plt.tight_layout()

    plt.show()

    precip_clubb = xr.open_dataset('your/file/path')

    precip_am4_dm = xr.open_dataset('your/file/path')

    ds = precip_am4_dm

    lat_min, lat_max = (30, 50)

    lon_min, lon_max = (260, 280)

    precip_gp = ds['precip'].sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

    time_in_hours = np.array([t.hour for t in ds['time'].values])

    precip_gp.coords['hour_of_day'] = ('time', time_in_hours)

    summer_months = [6, 7, 8]

    summer_precip_gp = precip_gp.sel(time=precip_gp['time'].dt.month.isin(summer_months))

    diurnal_cycle = summer_precip_gp.groupby('hour_of_day').mean(dim=['time', 'lat', 'lon'])

    plt.figure(figsize=(10, 6))

    plt.plot(np.arange(1.5, 24, 3), diurnal_cycle, marker='o', linestyle='-', color='b')

    plt.title('Diurnal Cycle of Precipitation over US Great Plains (Summer Months Only)')

    plt.xlabel('Hour of the Day (UTC)')

    plt.ylabel('Precipitation (mm/hr)')

    plt.grid(True)

    plt.xticks(np.arange(1.5, 24, 3))

    plt.tight_layout()

    plt.show()

    precip_am4_pm = xr.open_dataset('your/file/path')

    ds = precip_am4_pm

    lat_min, lat_max = (30, 50)

    lon_min, lon_max = (260, 280)

    precip_gp = ds['precip'].sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

    time_in_hours = np.array([t.hour for t in ds['time'].values])

    precip_gp.coords['hour_of_day'] = ('time', time_in_hours)

    summer_months = [6, 7, 8]

    summer_precip_gp = precip_gp.sel(time=precip_gp['time'].dt.month.isin(summer_months))

    diurnal_cycle = summer_precip_gp.groupby('hour_of_day').mean(dim=['time', 'lat', 'lon'])

    plt.figure(figsize=(10, 6))

    plt.plot(np.arange(1.5, 24, 3), diurnal_cycle, marker='o', linestyle='-', color='b')

    plt.title('Diurnal Cycle of Precipitation over US Great Plains (Summer Months Only)')

    plt.xlabel('Hour of the Day (UTC)')

    plt.ylabel('Precipitation (mm/hr)')

    plt.grid(True)

    plt.xticks(np.arange(1.5, 24, 3))

    plt.tight_layout()

    plt.show()

    precip_am4_dm_nsconv = xr.open_dataset('your/file/path')

    ds = precip_am4_dm_nsconv

    lat_min, lat_max = (30, 50)

    lon_min, lon_max = (260, 280)

    precip_gp = ds['precip'].sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

    time_in_hours = np.array([t.hour for t in ds['time'].values])

    precip_gp.coords['hour_of_day'] = ('time', time_in_hours)

    summer_months = [6, 7, 8]

    summer_precip_gp = precip_gp.sel(time=precip_gp['time'].dt.month.isin(summer_months))

    diurnal_cycle = summer_precip_gp.groupby('hour_of_day').mean(dim=['time', 'lat', 'lon'])

    plt.figure(figsize=(10, 6))

    plt.plot(np.arange(1.5, 24, 3), diurnal_cycle, marker='o', linestyle='-', color='b')

    plt.title('Diurnal Cycle of Precipitation over US Great Plains (Summer Months Only)')

    plt.xlabel('Hour of the Day (UTC)')

    plt.ylabel('Precipitation (mm/hr)')

    plt.grid(True)

    plt.xticks(np.arange(1.5, 24, 3))

    plt.tight_layout()

    plt.show()

    precip_am4_pm_nsconv = xr.open_dataset('your/file/path')

    ds = precip_am4_pm_nsconv

    lat_min, lat_max = (40, 50)

    lon_min, lon_max = (260, 270)

    precip_gp = ds['precip'].sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))

    time_in_hours = np.array([t.hour for t in ds['time'].values])

    precip_gp.coords['hour_of_day'] = ('time', time_in_hours)

    summer_months = [6, 7, 8]

    summer_precip_gp = precip_gp.sel(time=precip_gp['time'].dt.month.isin(summer_months))

    diurnal_cycle = summer_precip_gp.groupby('hour_of_day').mean(dim=['time', 'lat', 'lon'])

    plt.figure(figsize=(10, 6))

    plt.plot(np.arange(1.5, 24, 3), diurnal_cycle, marker='o', linestyle='-', color='b')

    plt.title('Diurnal Cycle of Precipitation over US Great Plains (Summer Months Only)')

    plt.xlabel('Hour of the Day (UTC)')

    plt.ylabel('Precipitation (mm/hr)')

    plt.grid(True)

    plt.xticks(np.arange(1.5, 24, 3))

    plt.tight_layout()

    plt.show()

    vcomp = xr.open_dataset('your/file/path')

    vcomp = xr.open_dataset('your/file/path')

    ds = vcomp.v

    jja = ds.sel(time=ds['time.month'].isin([6, 7, 8]))

    jja_mean = jja.mean(dim='time')

    target_grid = ctrl_v_summer

    new_lats = target_grid['lat']

    new_lons = target_grid['lon']

    new_level = target_grid['level']

    jja_mean_regridded = jja_mean.interp(latitude=new_lats, longitude=new_lons, level=new_level, method='linear')

    masked_data = jja_mean_regridded.where(~np.isnan(ctrl_v_summer), np.nan)

    vcomp_avg.level[::-1]

    lat_range = masked_data[:, :, :].sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg = lat_range.mean(dim='lat')

    plt.figure(figsize=(10, 6))

    levels = np.arange(-7.5, 7.6, 2.5)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level[::-1], vcomp_avg[::-1, :], levels=levels, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    vcomp_avg_era5 = masked_data.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200)).mean(dim='lat')

    vcomp = ctrl_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg = lat_range.mean(dim='lat')

    diff_ctrl = -vcomp_avg_era5.data + vcomp_avg.data

    print(np.sqrt(np.nanmean(vcomp_avg_era5.data - vcomp_avg.data) ** 2))

    vcomp = dm_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg = lat_range.mean(dim='lat')

    diff_dm = -vcomp_avg_era5.data + vcomp_avg.data

    print(np.sqrt(np.nanmean(vcomp_avg_era5.data - vcomp_avg.data) ** 2))

    vcomp = pm_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg = lat_range.mean(dim='lat')

    diff_pm = -vcomp_avg_era5.data + vcomp_avg.data

    print(np.sqrt(np.nanmean(vcomp_avg_era5.data - vcomp_avg.data) ** 2))

    vcomp = pmtau_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg = lat_range.mean(dim='lat')

    diff_pm_tau = -vcomp_avg_era5.data + vcomp_avg.data

    print(np.sqrt(np.nanmean(vcomp_avg_era5.data - vcomp_avg.data) ** 2))

    vcomp = pm_nsconv_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg = lat_range.mean(dim='lat')

    diff_pm_nsconv = -vcomp_avg_era5.data + vcomp_avg.data

    print(np.sqrt(np.nanmean(vcomp_avg_era5.data - vcomp_avg.data) ** 2))

    vcomp = pm_nsconv_v_summer

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg = lat_range.mean(dim='lat')

    vcomp_ctrl = ctrl_v_summer

    lat_range_ctrl = vcomp_ctrl.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg_ctrl = lat_range_ctrl.mean(dim='lat')

    vcomp_dm = dm_v_summer

    lat_range_dm = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg_dm = lat_range_dm.mean(dim='lat')

    diff_ctrl_dm = -vcomp_avg_ctrl + vcomp_avg_dm.data

    vcomp_pm = pm_v_summer

    lat_range_pm = vcomp_pm.sel(lat=slice(30, 40), lon=slice(230, 290), level=slice(1000, 200))

    vcomp_avg_pm = lat_range_pm.mean(dim='lat')

    diff_ctrl_pm = -vcomp_avg_dm + vcomp_avg_pm.data

    v = diff_ctrl

    plt.figure(figsize=(10, 6))

    levels = np.arange(-2.0, 2.1, 0.25)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level[::-1], v[::-1, :], levels=levels, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    v = diff_ctrl_dm

    plt.figure(figsize=(10, 6))

    levels = np.arange(-2.0, 2.1, 0.25)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level[::-1], v[::-1, :], levels=levels, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    v = diff_ctrl_pm

    plt.figure(figsize=(10, 6))

    levels = np.arange(-2.0, 2.1, 0.25)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level[::-1], v[::-1, :], levels=levels, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    v = diff_pm_tau

    plt.figure(figsize=(10, 6))

    levels = np.arange(-2.0, 2.1, 0.25)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level[::-1], v[::-1, :], levels=levels, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    v = diff_pm_nsconv

    plt.figure(figsize=(10, 6))

    levels = np.arange(-2.0, 2.1, 0.25)

    plt.contourf(vcomp_avg.lon, vcomp_avg.level[::-1], v[::-1, :], levels=levels, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    plt.colorbar(label='Meridional wind (m/s)')

    plt.xlabel('Longitude (degrees)')

    plt.ylabel('Pressure (hPa)')

    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')

    plt.show()

    path = 'your/file/path'

    atmos_month_1 = xr.open_dataset(path)

    (atmos_month_1.ug_vpwp_count[0, -4, :, :] * 30).plot()

    atmos_month_1.ug_upwp_count.phalf

    vcomp = ctrl_sphum

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg_ctrl = lat_range.mean(dim='lat')

    levels = np.arange(1, 13, 1)

    plt.figure(figsize=(10, 6), dpi=150)

    plt.contourf(vcomp_avg_ctrl.lon, vcomp_avg_ctrl.level, vcomp_avg_ctrl * 1000, levels=levels, cmap=cmocean.cm.haline, extend='both')

    plt.gca().invert_yaxis()

    cbar = plt.colorbar()

    cbar.ax.tick_params(labelsize=12)

    cbar.set_label('AM4 $q$ [g kg$^{-1}$]', fontsize=12)

    plt.xlabel('Longitude (degrees)', fontsize=12)

    plt.ylabel('Pressure (hPa)', fontsize=12)

    plt.tick_params(axis='x', labelsize=12)

    plt.tick_params(axis='y', labelsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    vcomp = dm_sphum

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg_dm = lat_range.mean(dim='lat')

    levels = np.arange(1, 13, 1)

    plt.figure(figsize=(10, 6), dpi=150)

    plt.contourf(vcomp_avg_dm.lon, vcomp_avg_dm.level, vcomp_avg_dm * 1000, levels=levels, cmap=cmocean.cm.haline, extend='both')

    plt.gca().invert_yaxis()

    cbar = plt.colorbar()

    cbar.ax.tick_params(labelsize=12)

    cbar.set_label('AM4-CLUBB_DM $q$ [g kg$^{-1}$]', fontsize=12)

    plt.xlabel('Longitude (degrees)', fontsize=12)

    plt.ylabel('Pressure (hPa)', fontsize=12)

    plt.tick_params(axis='x', labelsize=12)

    plt.tick_params(axis='y', labelsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    vcomp = pm_sphum

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg_pm = lat_range.mean(dim='lat')

    levels = np.arange(1, 13, 1)

    plt.figure(figsize=(10, 6), dpi=150)

    plt.contourf(vcomp_avg_pm.lon, vcomp_avg_pm.level, vcomp_avg_pm * 1000, levels=levels, cmap=cmocean.cm.haline, extend='both')

    plt.gca().invert_yaxis()

    cbar = plt.colorbar()

    cbar.ax.tick_params(labelsize=12)

    cbar.set_label('AM4-CLUBB_PM $q$ [g kg$^{-1}$]', fontsize=12)

    plt.xlabel('Longitude (degrees)', fontsize=12)

    plt.ylabel('Pressure (hPa)', fontsize=12)

    plt.tick_params(axis='x', labelsize=12)

    plt.tick_params(axis='y', labelsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    vcomp = pm_sphum

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg_pm = lat_range.mean(dim='lat')

    diff = (vcomp_avg_pm - vcomp_avg_dm) * 1000

    plt.figure(figsize=(10, 7), dpi=150)

    levelss = np.arange(-0.5, 0.6, 0.1)

    plt.contourf(vcomp_avg_pm.lon, vcomp_avg_pm.level, diff, levels=levelss, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    cbar = plt.colorbar()

    cbar.ax.tick_params(labelsize=12)

    cbar.set_label('AM4-CLUBB_PM - AM4-CLUBB_DM $q$ [g kg$^{-1}]$', fontsize=12)

    plt.xlabel('Longitude (degrees)', fontsize=12)

    plt.ylabel('Pressure (hPa)', fontsize=12)

    plt.tick_params(axis='x', labelsize=12)

    plt.tick_params(axis='y', labelsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    vcomp = pm_sphum

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg_pm = lat_range.mean(dim='lat')

    diff = (vcomp_avg_dm - vcomp_avg_ctrl) * 1000

    plt.figure(figsize=(10, 7), dpi=150)

    levelss = np.arange(-1.5, 1.6, 0.25)

    plt.contourf(vcomp_avg_pm.lon, vcomp_avg_pm.level, diff, levels=levelss, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    cbar = plt.colorbar()

    cbar.ax.tick_params(labelsize=12)

    cbar.set_label('AM4-CLUBB_DM - AM4 $q$ [g kg$^{-1}]$', fontsize=12)

    plt.xlabel('Longitude (degrees)', fontsize=12)

    plt.ylabel('Pressure (hPa)', fontsize=12)

    plt.tick_params(axis='x', labelsize=12)

    plt.tick_params(axis='y', labelsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

    vcomp = pm_sphum

    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))

    vcomp_avg_pm = lat_range.mean(dim='lat')

    diff = (vcomp_avg_pm - vcomp_avg_ctrl) * 1000

    plt.figure(figsize=(10, 7), dpi=150)

    levelss = np.arange(-1.5, 1.6, 0.25)

    plt.contourf(vcomp_avg_pm.lon, vcomp_avg_pm.level, diff, levels=levelss, cmap='coolwarm', extend='both')

    plt.gca().invert_yaxis()

    cbar = plt.colorbar()

    cbar.ax.tick_params(labelsize=12)

    cbar.set_label('AM4-CLUBB_PM - AM4 $q$ [g kg$^{-1}]$', fontsize=12)

    plt.xlabel('Longitude (degrees)', fontsize=12)

    plt.ylabel('Pressure (hPa)', fontsize=12)

    plt.tick_params(axis='x', labelsize=12)

    plt.tick_params(axis='y', labelsize=12)

    plt.savefig('your/file/path', bbox_inches='tight')

    plt.show()

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
