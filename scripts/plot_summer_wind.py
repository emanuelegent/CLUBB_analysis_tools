"""Script `plot_summer_wind`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from cartopy.mpl.gridliner import LongitudeFormatter, LatitudeFormatter
import cmocean

logger = logging.getLogger(__name__)

def plot_wind_vector_meridional(u_data, v_data, label, vmin=-6, vmax=7, cmap='RdBu_r'):
    """
    Plots wind vectors overlaid on the meridional wind component (v).
    
    Parameters:
    - u_data: xarray DataArray, the zonal wind component (e.g., u10m or u925)
    - v_data: xarray DataArray, the meridional wind component (e.g., v10m or v925)
    - label: str, label for the colorbar representing the meridional wind
    - vmin: int/float, minimum value for contour color range (default: -10)
    - vmax: int/float, maximum value for contour color range (default: 10)
    - cmap: str, colormap to use for meridional wind (default: 'RdBu_r')
    """
    projection = ccrs.PlateCarree()
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    u_data_region = u_data.sel(lat=slice(20, 50), lon=slice(360 - 130, 360 - 70))[:, :]
    v_data_region = v_data.sel(lat=slice(20, 50), lon=slice(360 - 130, 360 - 70))[:, :]
    meridional_wind = v_data_region
    levels = np.arange(vmin, vmax, 1)
    contf = ax.contourf(u_data_region.lon, u_data_region.lat, meridional_wind, levels=levels, cmap=cmap, alpha=0.8, extend='both', transform=ccrs.PlateCarree())
    cbar = fig.colorbar(contf, ax=ax, orientation='horizontal', pad=0.05, label=label)
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(label, fontsize=14)
    ax.quiver(u_data_region.lon[::2].values, u_data_region.lat[::2].values, u_data_region[::2, ::2].values, v_data_region[::2, ::2].values, transform=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    for ll in ax.xaxis.get_ticklabels():
        ll.set_rotation(90)
        ll.set_fontweight('bold')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    fig.savefig('your/file/path' + label + '.png', bbox_inches='tight')
    plt.show()

def plot_wind_vector_meridional_diff(v_data_1, v_data_2, ftype1, ftype2, label, vmin=-2.5, vmax=2.75, cmap='RdBu_r'):
    """
    Plots wind vectors overlaid on the meridional wind component (v).
    
    Parameters:
    - u_data: xarray DataArray, the zonal wind component (e.g., u10m or u925)
    - v_data: xarray DataArray, the meridional wind component (e.g., v10m or v925)
    - label: str, label for the colorbar representing the meridional wind
    - vmin: int/float, minimum value for contour color range (default: -10)
    - vmax: int/float, maximum value for contour color range (default: 10)
    - cmap: str, colormap to use for meridional wind (default: 'RdBu_r')
    """
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    v_data_region_1 = v_data_1.sel(lat=slice(20, 50), lon=slice(360 - 130, 360 - 70))[:, :]
    v_data_region_2 = v_data_2.sel(lat=slice(20, 50), lon=slice(360 - 130, 360 - 70))[:, :]
    meridional_wind = v_data_region_2 - v_data_region_1
    levels = np.arange(vmin, vmax, 0.25)
    contf = ax.contourf(v_data_region_1.lon, v_data_region_1.lat, meridional_wind, levels=levels, cmap=cmap, alpha=0.8, extend='both', transform=ccrs.PlateCarree())
    cbar = fig.colorbar(contf, ax=ax, orientation='horizontal', pad=0.05)
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(label=ftype2 + ' - ' + ftype1 + ' 925hPa $v$', fontsize=14)
    ax.add_feature(cfeature.COASTLINE)
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    ax.gridlines(draw_labels=False, dms=True, x_inline=False, y_inline=False)
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    for ll in ax.xaxis.get_ticklabels():
        ll.set_rotation(90)
        ll.set_fontweight('bold')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    fig.savefig('your/file/path' + ftype2 + '_' + 'ftype1' + label + '.png', bbox_inches='tight')
    plt.show()

def plot_wind_vector_meridional_era5(u_data, v_data, label, vmin=-6, vmax=7, cmap='RdBu_r'):
    """
    Plots wind vectors overlaid on the meridional wind component (v) for ERA5
    
    Parameters:
    - u_data: xarray DataArray, the zonal wind component (e.g., u10m or u925)
    - v_data: xarray DataArray, the meridional wind component (e.g., v10m or v925)
    - label: str, label for the colorbar representing the meridional wind
    - vmin: int/float, minimum value for contour color range (default: -10)
    - vmax: int/float, maximum value for contour color range (default: 10)
    - cmap: str, colormap to use for meridional wind (default: 'RdBu_r')
    """
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    u_data_region = u_data.sel(latitude=slice(50, 20), longitude=slice(360 - 130, 360 - 70))
    v_data_region = v_data.sel(latitude=slice(50, 20), longitude=slice(360 - 130, 360 - 70))
    meridional_wind = v_data_region
    levels = np.arange(vmin, vmax, 1)
    contf = ax.contourf(u_data_region.longitude, u_data_region.latitude, meridional_wind, levels=levels, cmap=cmap, alpha=0.8, extend='both', transform=ccrs.PlateCarree())
    cbar = fig.colorbar(contf, ax=ax, orientation='horizontal', pad=0.05, label=label)
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(label, fontsize=14)
    step = 8
    ax.quiver(u_data_region.longitude[::step].values, u_data_region.latitude[::step].values, u_data_region[::step, ::step].values, v_data_region[::step, ::step].values, transform=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    ax.gridlines(draw_labels=False, dms=True, x_inline=False, y_inline=False)
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    plt.tight_layout()
    fig.savefig('your/file/path' + label + '.png', bbox_inches='tight')
    plt.show()
    plt.close()

def plot_meridional_structure(vcomp, label, era5=False):
    print(vcomp)
    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))
    vcomp_avg = lat_range.mean(dim='lat')
    plt.figure(figsize=(10, 6), dpi=180)
    levels = np.arange(-2.0, 2.1, 0.25)
    plt.contourf(vcomp_avg.lon, vcomp_avg.pfull, vcomp_avg[0, :, :], levels=levels, cmap='coolwarm', extend='both')
    plt.gca().invert_yaxis()
    cbar = plt.colorbar(label=label + ' Meridional wind [m s$^{-1}$]')
    cbar.set_label(label=label + ' Meridional wind [m s$^{-1}$]', fontsize=14)
    plt.xlabel('Longitude (degrees)', fontsize=14)
    lon_ticks = np.round(vcomp_avg.lon.values)
    plt.xticks(np.arange(230, 300, 10), [f'{abs(tick - 360)}°W' for tick in np.arange(230, 300, 10)])
    plt.grid(axis='x', linestyle='--', linewidth=0.7)
    plt.ylabel('Pressure (hPa)', fontsize=14)
    plt.title('Pressure-Longitude Slice of Meridional Wind (Averaged between 30N and 40N, 130W-70W)')
    plt.savefig('your/file/path' + label + '.png', bbox_inches='tight')
    plt.show()

def plot_structure_wind(v_summer, ftype):
    vcomp = v_summer
    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))
    vcomp_avg = lat_range.mean(dim='lat')
    plt.figure(figsize=(10, 6), dpi=150)
    levels = np.arange(-7.5, 7.5, 2.5)
    plt.contourf(vcomp_avg.lon, vcomp_avg.level, vcomp_avg, cmap='coolwarm', extend='both')
    plt.gca().invert_yaxis()
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(ftype + ' $v$ [m s$^{-1}$]', fontsize=14)
    cbar.ax.tick_params(labelsize=12)
    plt.xlabel('Longitude (degrees)', fontsize=14)
    plt.ylabel('Pressure (hPa)', fontsize=14)
    plt.tick_params(axis='x', labelsize=12)
    plt.tick_params(axis='y', labelsize=12)
    plt.savefig('your/file/path' + ftype + 'wind_profile.png', bbox_inches='tight')
    plt.show()

def plot_structure_wind_diff(field1, field2, ftype1, ftype2):
    vcomp = field1
    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))
    vcomp_avg = lat_range.mean(dim='lat')
    vcomp2 = field2
    lat_range2 = vcomp2.sel(lat=slice(30, 40), lon=slice(230, 290))
    vcomp_avg2 = lat_range2.mean(dim='lat')
    plt.figure(figsize=(10, 6))
    levels = np.arange(-1.0, 1.1, 0.25)
    diff = vcomp_avg2 - vcomp_avg
    plt.contourf(vcomp_avg.lon, vcomp_avg.level, diff, levels=levels, cmap='coolwarm', extend='both')
    plt.gca().invert_yaxis()
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(ftype2 + ' - ' + ftype1 + ' $v$ [m s$^{-1}$]', fontsize=14)
    plt.xlabel('Longitude [degrees]', fontsize=14)
    plt.ylabel('Pressure [hPa]', fontsize=14)
    plt.tick_params(axis='x', labelsize=12)
    plt.tick_params(axis='y', labelsize=12)
    plt.savefig('your/file/path' + ftype1 + ftype2 + '_wind_profile_diff.png', bbox_inches='tight')
    plt.show()

def plot_structure_sphum(sphum, ftype):
    vcomp = sphum
    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))
    vcomp_avg_ctrl = lat_range.mean(dim='lat')
    levels = np.arange(1, 17, 2)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.contourf(vcomp_avg_ctrl.lon, vcomp_avg_ctrl.level, vcomp_avg_ctrl * 1000, levels=levels, cmap=cmocean.cm.haline, extend='both')
    plt.gca().invert_yaxis()
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(ftype + ' $q$ [g kg$^{-1}$]', fontsize=14)
    plt.xlabel('Longitude [degrees]', fontsize=14)
    plt.ylabel('Pressure [hPa]', fontsize=14)
    plt.tick_params(axis='x', labelsize=12)
    plt.tick_params(axis='y', labelsize=12)
    plt.savefig('your/file/path' + ftype + '_sphum_profile.png', bbox_inches='tight')
    plt.show()

def plot_structure_sphum_lat(sphum, ftype):
    vcomp = sphum
    lat_range = vcomp.sel(lat=slice(20, 50), lon=slice(265, 266))
    vcomp_avg_ctrl = lat_range.mean(dim='lon')
    levels = np.arange(1, 17, 2)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.contourf(vcomp_avg_ctrl.lat, vcomp_avg_ctrl.level, vcomp_avg_ctrl * 1000, levels=levels, cmap=cmocean.cm.haline, extend='both')
    plt.gca().invert_yaxis()
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(ftype + ' $q$ [g kg$^{-1}$]', fontsize=14)
    plt.xlabel('Latitude [degrees]', fontsize=14)
    plt.ylabel('Pressure [hPa]', fontsize=14)
    plt.tick_params(axis='x', labelsize=12)
    plt.tick_params(axis='y', labelsize=12)
    plt.savefig('your/file/path' + ftype + '_sphum_profile_lat.png', bbox_inches='tight')
    plt.show()

def plot_structure_sphum_diff(field1, field2, ftype1, ftype2):
    vcomp = field1
    lat_range = vcomp.sel(lat=slice(30, 40), lon=slice(230, 290))
    vcomp_avg = lat_range.mean(dim='lat')
    vcomp2 = field2
    lat_range2 = vcomp2.sel(lat=slice(30, 40), lon=slice(230, 290))
    vcomp_avg2 = lat_range2.mean(dim='lat')
    plt.figure(figsize=(10, 6))
    levels = np.arange(-1.5, 1.6, 0.25)
    diff = vcomp_avg2 - vcomp_avg
    plt.contourf(vcomp_avg.lon, vcomp_avg.level, diff * 1000, levels=levels, cmap='coolwarm', extend='both')
    plt.gca().invert_yaxis()
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(ftype2 + ' - ' + ftype1 + ' $q$ [g kg$^{-1}$]', fontsize=14)
    plt.xlabel('Longitude [degrees]', fontsize=14)
    plt.ylabel('Pressure [hPa]', fontsize=14)
    plt.tick_params(axis='x', labelsize=12)
    plt.tick_params(axis='y', labelsize=12)
    plt.savefig('your/file/path' + ftype1 + ftype2 + '_sphum_profile_diff.png', bbox_inches='tight')
    plt.show()

def plot_structure_sphum_diff_lat(field1, field2, ftype1, ftype2):
    vcomp = field1
    lat_range = vcomp.sel(lat=slice(20, 50), lon=slice(265, 266))
    vcomp_avg = lat_range.mean(dim='lon')
    vcomp2 = field2
    lat_range2 = vcomp2.sel(lat=slice(20, 50), lon=slice(264, 265))
    vcomp_avg2 = lat_range2.mean(dim='lon')
    plt.figure(figsize=(10, 6))
    levels = np.arange(-1.5, 1.6, 0.25)
    diff = vcomp_avg2 - vcomp_avg
    plt.contourf(vcomp_avg.lat, vcomp_avg.level, diff * 1000, levels=levels, cmap='coolwarm', extend='both')
    plt.gca().invert_yaxis()
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(ftype2 + ' - ' + ftype1 + ' $q$ [g kg$^{-1}$]', fontsize=14)
    plt.xlabel('Latitude [degrees]', fontsize=14)
    plt.ylabel('Pressure [hPa]', fontsize=14)
    plt.tick_params(axis='x', labelsize=12)
    plt.tick_params(axis='y', labelsize=12)
    plt.savefig('your/file/path' + ftype1 + ftype2 + '_sphum_profile_diff_lat.png', bbox_inches='tight')
    plt.show()

def plot_specific_humidity_conus(data, level, ftype, time_index=0, vmin=None, vmax=None, cmap='viridis'):
    """
    Plot specific humidity over the CONUS using contourf.

    Parameters:
    - data: xarray.DataArray
        Specific humidity field with dimensions including 'lat', 'lon', and optionally 'time', 'level'.
    - level: int or float
        Pressure level in hPa to select from the 'level' dimension (if present).
    - time_index: int
        Time index to use if 'time' is a dimension.
    - vmin, vmax: float or None
        Min and max color limits.
    - cmap: str
        Matplotlib colormap.
    """
    if data.lon.max() > 180:
        data = data.assign_coords(lon=(data.lon + 180) % 360 - 180).sortby('lon')
    data = data.sel(level=level, method='nearest')
    data = data.sel(lat=slice(20, 50), lon=slice(-130, -65))
    lons, lats = (data.lon.values, data.lat.values)
    field = data.values
    lon2d, lat2d = np.meshgrid(lons, lats)
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    levels = np.arange(0, 18, 1)
    contour = ax.contourf(lon2d, lat2d, field * 1000, transform=ccrs.PlateCarree(), levels=levels, cmap=cmocean.cm.matter, extend='max')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    ax.coastlines()
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    cbar = plt.colorbar(contour, ax=ax, pad=0.05, orientation='horizontal')
    cbar.set_label(ftype + ' $q$ at 925hPa [g kg$^{-1}$]')
    cbar.ax.tick_params(labelsize=12)
    ax.set_title(f'Specific Humidity at {level} hPa')
    plt.tight_layout()
    plt.savefig('your/file/path' + ftype + '_sphum_1000.png', bbox_inches='tight')
    plt.show()

def plot_q_diff(v_data_1, v_data_2, ftype1, ftype2, label, vmin=-3.0, vmax=3.1, cmap='RdBu_r'):
    """
    Plots wind vectors overlaid on the meridional wind component (v).
    
    Parameters:
    - u_data: xarray DataArray, the zonal wind component (e.g., u10m or u925)
    - v_data: xarray DataArray, the meridional wind component (e.g., v10m or v925)
    - label: str, label for the colorbar representing the meridional wind
    - vmin: int/float, minimum value for contour color range (default: -10)
    - vmax: int/float, maximum value for contour color range (default: 10)
    - cmap: str, colormap to use for meridional wind (default: 'RdBu_r')
    """
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    v_data_region_1 = v_data_1.sel(lat=slice(20, 50), lon=slice(360 - 130, 360 - 70))[:, :]
    v_data_region_2 = v_data_2.sel(lat=slice(20, 50), lon=slice(360 - 130, 360 - 70))[:, :]
    meridional_wind = v_data_region_2 - v_data_region_1
    vmin = -3.0
    vmax = 3.25
    levels = np.arange(vmin, vmax, 0.5)
    contf = ax.contourf(v_data_region_1.lon, v_data_region_1.lat, meridional_wind * 1000, levels=levels, cmap=cmap, alpha=0.8, extend='both', transform=ccrs.PlateCarree())
    cbar = fig.colorbar(contf, ax=ax, orientation='horizontal', pad=0.05)
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(label=ftype2 + ' - ' + ftype1 + ' 925hPa $q$', fontsize=14)
    ax.add_feature(cfeature.COASTLINE)
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    ax.gridlines(draw_labels=False, dms=True, x_inline=False, y_inline=False)
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    for ll in ax.xaxis.get_ticklabels():
        ll.set_rotation(90)
        ll.set_fontweight('bold')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    fig.savefig('your/file/path' + ftype2 + '_' + 'ftype1' + label + '.png', bbox_inches='tight')
    plt.show()

def plot_cape_conus(data, ftype, time_index=0, vmin=None, vmax=None, cmap='viridis'):
    """
    Plot specific humidity over the CONUS using contourf.

    Parameters:
    - data: xarray.DataArray
        Specific humidity field with dimensions including 'lat', 'lon', and optionally 'time', 'level'.
    - level: int or float
        Pressure level in hPa to select from the 'level' dimension (if present).
    - time_index: int
        Time index to use if 'time' is a dimension.
    - vmin, vmax: float or None
        Min and max color limits.
    - cmap: str
        Matplotlib colormap.
    """
    if data.lon.max() > 180:
        data = data.assign_coords(lon=(data.lon + 180) % 360 - 180).sortby('lon')
    data = data.sel(lat=slice(20, 50), lon=slice(-130, -65))
    lons, lats = (data.lon.values, data.lat.values)
    field = data.values
    lon2d, lat2d = np.meshgrid(lons, lats)
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    from matplotlib import cm
    from matplotlib.colors import LinearSegmentedColormap

    def truncate_colormap(cmap, minval=0.2, maxval=1.0, n=256):
        new_cmap = LinearSegmentedColormap.from_list(f'trunc({cmap.name},{minval:.2f},{maxval:.2f})', cmap(np.linspace(minval, maxval, n)))
        return new_cmap
    trunc_inferno = truncate_colormap(cm.inferno, 0.2, 1.0)
    levels = np.arange(0, 2500, 400)
    contour = ax.contourf(lon2d, lat2d, field, transform=ccrs.PlateCarree(), levels=levels, cmap=trunc_inferno, extend='max')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    ax.coastlines()
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    cbar = plt.colorbar(contour, ax=ax, pad=0.05, orientation='horizontal')
    cbar.set_label(ftype + ' CAPE [J kg$^{-1}$]')
    cbar.ax.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('your/file/path' + ftype + '_cape.png', bbox_inches='tight')
    plt.show()

def plot_tot_cld_amt(data, ftype, time_index=0, vmin=None, vmax=None, cmap='viridis'):
    """
    Plot specific humidity over the CONUS using contourf.

    Parameters:
    - data: xarray.DataArray
        Specific humidity field with dimensions including 'lat', 'lon', and optionally 'time', 'level'.
    - level: int or float
        Pressure level in hPa to select from the 'level' dimension (if present).
    - time_index: int
        Time index to use if 'time' is a dimension.
    - vmin, vmax: float or None
        Min and max color limits.
    - cmap: str
        Matplotlib colormap.
    """
    if data.lon.max() > 180:
        data = data.assign_coords(lon=(data.lon + 180) % 360 - 180).sortby('lon')
    data = data.sel(lat=slice(20, 50), lon=slice(-130, -65))
    lons, lats = (data.lon.values, data.lat.values)
    field = data.values
    lon2d, lat2d = np.meshgrid(lons, lats)
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    from matplotlib import cm
    from matplotlib.colors import LinearSegmentedColormap

    def truncate_colormap(cmap, minval=0.2, maxval=1.0, n=256):
        new_cmap = LinearSegmentedColormap.from_list(f'trunc({cmap.name},{minval:.2f},{maxval:.2f})', cmap(np.linspace(minval, maxval, n)))
        return new_cmap
    trunc_inferno = truncate_colormap(cm.inferno, 0.2, 1.0)
    levels = np.arange(0, 81, 10)
    contour = ax.contourf(lon2d, lat2d, field, transform=ccrs.PlateCarree(), levels=levels, cmap='Greys', extend='max')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    ax.coastlines()
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    cbar = plt.colorbar(contour, ax=ax, pad=0.05, orientation='horizontal')
    cbar.set_label(ftype + ' TOTAL CLOUD AMOUNT [%]')
    cbar.ax.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('your/file/path' + ftype + '_tot_cld_amt.png', bbox_inches='tight')
    plt.show()

def plot_low_cld_amt(data, ftype, time_index=0, vmin=None, vmax=None, cmap='viridis'):
    """
    Plot specific humidity over the CONUS using contourf.

    Parameters:
    - data: xarray.DataArray
        Specific humidity field with dimensions including 'lat', 'lon', and optionally 'time', 'level'.
    - level: int or float
        Pressure level in hPa to select from the 'level' dimension (if present).
    - time_index: int
        Time index to use if 'time' is a dimension.
    - vmin, vmax: float or None
        Min and max color limits.
    - cmap: str
        Matplotlib colormap.
    """
    if data.lon.max() > 180:
        data = data.assign_coords(lon=(data.lon + 180) % 360 - 180).sortby('lon')
    data = data.sel(lat=slice(20, 50), lon=slice(-130, -65))
    lons, lats = (data.lon.values, data.lat.values)
    field = data.values
    lon2d, lat2d = np.meshgrid(lons, lats)
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    from matplotlib import cm
    from matplotlib.colors import LinearSegmentedColormap

    def truncate_colormap(cmap, minval=0.2, maxval=1.0, n=256):
        new_cmap = LinearSegmentedColormap.from_list(f'trunc({cmap.name},{minval:.2f},{maxval:.2f})', cmap(np.linspace(minval, maxval, n)))
        return new_cmap
    trunc_inferno = truncate_colormap(cm.inferno, 0.2, 1.0)
    levels = np.arange(0, 51, 5)
    contour = ax.contourf(lon2d, lat2d, field, transform=ccrs.PlateCarree(), levels=levels, cmap='Greys', extend='max')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    ax.coastlines()
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    cbar = plt.colorbar(contour, ax=ax, pad=0.05, orientation='horizontal')
    cbar.set_label(ftype + ' LOW CLOUD AMOUNT [%]')
    cbar.ax.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('your/file/path' + ftype + '_low_cld_amt.png', bbox_inches='tight')
    plt.show()

def plot_mid_cld_amt(data, ftype, time_index=0, vmin=None, vmax=None, cmap='viridis'):
    """
    Plot specific humidity over the CONUS using contourf.

    Parameters:
    - data: xarray.DataArray
        Specific humidity field with dimensions including 'lat', 'lon', and optionally 'time', 'level'.
    - level: int or float
        Pressure level in hPa to select from the 'level' dimension (if present).
    - time_index: int
        Time index to use if 'time' is a dimension.
    - vmin, vmax: float or None
        Min and max color limits.
    - cmap: str
        Matplotlib colormap.
    """
    if data.lon.max() > 180:
        data = data.assign_coords(lon=(data.lon + 180) % 360 - 180).sortby('lon')
    data = data.sel(lat=slice(20, 50), lon=slice(-130, -65))
    lons, lats = (data.lon.values, data.lat.values)
    field = data.values
    lon2d, lat2d = np.meshgrid(lons, lats)
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    from matplotlib import cm
    from matplotlib.colors import LinearSegmentedColormap

    def truncate_colormap(cmap, minval=0.2, maxval=1.0, n=256):
        new_cmap = LinearSegmentedColormap.from_list(f'trunc({cmap.name},{minval:.2f},{maxval:.2f})', cmap(np.linspace(minval, maxval, n)))
        return new_cmap
    trunc_inferno = truncate_colormap(cm.inferno, 0.2, 1.0)
    levels = np.arange(0, 51, 5)
    contour = ax.contourf(lon2d, lat2d, field, transform=ccrs.PlateCarree(), levels=levels, cmap='Greys', extend='max')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    ax.coastlines()
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    cbar = plt.colorbar(contour, ax=ax, pad=0.05, orientation='horizontal')
    cbar.set_label(ftype + ' MID-LEVEL CLOUD AMOUNT [%]')
    cbar.ax.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('your/file/path' + ftype + '_mid_cld_amt.png', bbox_inches='tight')
    plt.show()

def plot_high_cld_amt(data, ftype, time_index=0, vmin=None, vmax=None, cmap='viridis'):
    """
    Plot specific humidity over the CONUS using contourf.

    Parameters:
    - data: xarray.DataArray
        Specific humidity field with dimensions including 'lat', 'lon', and optionally 'time', 'level'.
    - level: int or float
        Pressure level in hPa to select from the 'level' dimension (if present).
    - time_index: int
        Time index to use if 'time' is a dimension.
    - vmin, vmax: float or None
        Min and max color limits.
    - cmap: str
        Matplotlib colormap.
    """
    if data.lon.max() > 180:
        data = data.assign_coords(lon=(data.lon + 180) % 360 - 180).sortby('lon')
    data = data.sel(lat=slice(20, 50), lon=slice(-130, -65))
    lons, lats = (data.lon.values, data.lat.values)
    field = data.values
    lon2d, lat2d = np.meshgrid(lons, lats)
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(subplot_kw={'projection': projection}, dpi=180)
    from matplotlib import cm
    from matplotlib.colors import LinearSegmentedColormap

    def truncate_colormap(cmap, minval=0.2, maxval=1.0, n=256):
        new_cmap = LinearSegmentedColormap.from_list(f'trunc({cmap.name},{minval:.2f},{maxval:.2f})', cmap(np.linspace(minval, maxval, n)))
        return new_cmap
    trunc_inferno = truncate_colormap(cm.inferno, 0.2, 1.0)
    levels = np.arange(0, 101, 10)
    contour = ax.contourf(lon2d, lat2d, field, transform=ccrs.PlateCarree(), levels=levels, cmap='Greys', extend='max')
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [0, 3.5, 8.5, 11.3]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-125 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    ax.coastlines()
    ax.set_extent([360 - 130, 360 - 70, 20, 50], crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color='gray', linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(number_format='.0f')
    gl.yformatter = LatitudeFormatter(number_format='.0f')
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    cbar = plt.colorbar(contour, ax=ax, pad=0.05, orientation='horizontal')
    cbar.set_label(ftype + ' HIGH CLOUD AMOUNT [%]')
    cbar.ax.tick_params(labelsize=12)
    plt.tight_layout()
    plt.savefig('your/file/path' + ftype + '_high_cld_amt.png', bbox_inches='tight')
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
