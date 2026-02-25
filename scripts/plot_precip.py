"""Script `plot_precip`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import xarray as xr
import cartopy.crs as ccrs

logger = logging.getLogger(__name__)

def plot_precip_phase(precip_diurnal, tmax, data_type):
    lon = precip_diurnal.lon
    precip_cycle_shifted = np.ma.masked_invalid(tmax.copy())
    print(precip_cycle_shifted.shape)
    colors = ['cyan', 'violet', 'blue', 'red', 'yellow', 'green', 'cyan']
    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors, N=24)
    levels = np.arange(0, 24, 1)
    norm = mcolors.BoundaryNorm(levels, custom_cmap.N)
    print(custom_cmap.N)
    plt.figure(figsize=(10, 6))
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})
    im = plt.pcolormesh(lon, precip_diurnal.lat, precip_cycle_shifted[0], cmap=custom_cmap, transform=ccrs.PlateCarree())
    ax.set_extent([-125, -66, 20, 50], crs=ccrs.PlateCarree())
    ax.gridlines(draw_labels=False, dms=True, x_inline=False, y_inline=False)
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [-0.1, 3.5, 8.4, 11.0]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-122 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    cbar = plt.colorbar(im, norm=norm, ticks=levels, pad=0.04, orientation='horizontal')
    cbar.set_label(label=data_type + ' Phase of 1st Harmonic (Peak Precip Time in LST)', fontsize=14)
    cbar.ax.tick_params(labelsize=12)
    ax.coastlines()
    plt.savefig('your/file/path' + data_type + 'precip_cycle_phase.png', bbox_inches='tight')
    plt.show()

def plot_precip_peak(precip_diurnal, maxvalue, data_type):
    colors = ['white', 'violet', 'purple', 'darkorange', 'orange', 'yellow', 'green', 'cyan', 'blue']
    lon = precip_diurnal.lon
    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)
    norm = mcolors.Normalize(vmin=0, vmax=24)
    tick_values = [0.25, 0.5, 0.75, 1.5, 2.25, 3.0, 5.0, 8.0]
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_cmap', colors, N=24)
    print(len(tick_values))
    print(len(colors))
    norm = mcolors.BoundaryNorm(boundaries=tick_values, ncolors=len(colors), extend='both')
    plt.figure(figsize=(10, 6))
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})
    im = plt.contourf(lon, precip_diurnal.lat, maxvalue[0] * 86400, levels=tick_values, cmap=custom_cmap, transform=ccrs.PlateCarree(), extend='both')
    cbar = plt.colorbar(im, norm=norm, values=tick_values, pad=0.04, orientation='horizontal')
    cbar.set_label(label=data_type + ' Diurnal amplitude of precipitation [mm day$^{-1}$]', fontsize=14)
    cbar.ax.tick_params(labelsize=12)
    ax.coastlines()
    ax.set_extent([-125, -66, 20, 50], crs=ccrs.PlateCarree())
    ax.gridlines(draw_labels=False, dms=True, x_inline=False, y_inline=False)
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [-0.1, 3.5, 8.4, 11.0]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-122 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    plt.tight_layout()
    plt.savefig('your/file/path' + data_type + '_precip_cycle_peak.png', bbox_inches='tight')
    plt.show()

def plot_precip_mean_rate(precip_diurnal, maxvalue, data_type):
    colors = ['white', 'violet', 'purple', 'darkorange', 'orange', 'yellow', 'green', 'cyan', 'blue']
    lon = precip_diurnal.lon
    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)
    norm = mcolors.Normalize(vmin=0, vmax=24)
    tick_values = [0.25, 0.5, 0.75, 1.5, 2.25, 3.0, 5.0, 8.0]
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_cmap', colors, N=24)
    print(len(tick_values))
    print(len(colors))
    norm = mcolors.BoundaryNorm(boundaries=tick_values, ncolors=len(colors), extend='both')
    plt.figure(figsize=(10, 6))
    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})
    im = plt.contourf(lon, precip_diurnal.lat, maxvalue * 86400, levels=tick_values, cmap=custom_cmap, transform=ccrs.PlateCarree(), extend='both')
    cbar = plt.colorbar(im, norm=norm, values=tick_values, pad=0.04, orientation='horizontal')
    cbar.set_label(label=data_type + ' Mean precipitation rate [mm day$^{-1}$]', fontsize=14)
    cbar.ax.tick_params(labelsize=12)
    ax.coastlines()
    ax.set_extent([-125, -66, 20, 50], crs=ccrs.PlateCarree())
    ax.gridlines(draw_labels=False, dms=True, x_inline=False, y_inline=False)
    lon_ticks = [-120, -100, -80]
    lat_ticks = [20, 30, 40]
    shifts = [-0.1, 3.5, 8.4, 11.0]
    for i, lat in enumerate(lat_ticks):
        x, y = ax.projection.transform_point(-122 - shifts[i], lat, ccrs.PlateCarree())
        ax.text(x, y, f'{lat}°', ha='right', va='center', fontsize=10, fontweight='bold', rotation=0)
    for lon in lon_ticks:
        ax.text(lon, 50, f'{lon}°', transform=ccrs.PlateCarree(), ha='center', va='bottom', fontsize=10, fontweight='bold', rotation=0)
    plt.tight_layout()
    plt.savefig('your/file/path' + data_type + '_precip_cycle_rate.png', bbox_inches='tight')
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
