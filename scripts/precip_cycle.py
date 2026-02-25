"""Script `precip_cycle`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from datetime import datetime, timedelta
import glob
import xarray as xr
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import xarray as xr
import cartopy.crs as ccrs
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import xarray as xr
import cartopy.crs as ccrs
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import xarray as xr
import cartopy.crs as ccrs
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import xarray as xr
import cartopy.crs as ccrs
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import h5py
import numpy as np
import xarray as xr
import os
import glob
import pandas as pd

logger = logging.getLogger(__name__)

def load_all_data(file_path):
    """Loads all NetCDF files matching the pattern and concatenates them along the time dimension."""
    ds = xr.open_dataset(file_path, engine='netcdf4')
    precip = ds['precip']
    time = ds['time']
    lat = ds['lat']
    lon = ds['lon']
    return (ds, precip, time, lat, lon)

def plot_map(data, lat, lon, title, cmap, units):
    """Plots a map of data over the CONUS region."""
    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent([-125, -75, 25, 50], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.STATES, linestyle=':')
    plt.pcolormesh(lon, lat, data, cmap=cmap, shading='auto')
    plt.colorbar(label=units)
    plt.title(title)
    plt.show()

def main():
    file_pattern = 'your/file/path'
    ds, precip, time, lat, lon = load_all_data(file_pattern)
    return (ds, precip, time, lat, lon)

def convert_time_to_lst(time_values, lon_values):
    """Convert CFTime in UTC to local standard time (LST) for each longitude."""
    timestamps = np.array([pd.Timestamp(t.strftime('%Y-%m-%d %H:%M:%S')) for t in time_values.values])
    lst_offsets = np.interp(lon_values, [-125, -75], [-8, -5])
    lst_hours = np.array([(t.hour - offset) % 24 for t, offset in zip(timestamps, lst_offsets)])
    return (lst_hours, timestamps)

def find_peak_precip(precip, time_lst):
    """Finds peak precipitation value and corresponding time for each grid cell over all files."""
    peak_time_index = precip.argmax(dim='time')
    peak_precip_values = np.max(precip, axis=0)
    peak_times = time_lst[peak_time_index]
    return (peak_precip_values, peak_times)

def run(cfg: dict) -> None:
    if __name__ == '__main__':
        ds, precip, time, lat, lon = main()

    time_lst, timestamps = convert_time_to_lst(time, lon)

    peak_precip, peak_times = find_peak_precip(precip, time_lst)

    time_lst

    plot_map(peak_precip, lat, lon, 'Peak Precipitation (kg/m²/s)', cmap='Blues', units='kg/m²/s')

    plot_map(peak_times, lat, lon, 'Time of Peak Precipitation (Local Standard Time)', cmap='viridis', units='Hour')

    precip

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    lat = ds['lat']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(24, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(10, 70), lon=slice(235, 294))

    precip_daily = precip_conus.resample(time='1D').mean()

    precip_conus['hour'] = precip_conus.time.dt.hour

    precip_diurnal = precip_conus.groupby('hour').mean(dim='time')

    precip_diurnal.shape

    peak_hour_utc = precip_diurnal.argmax(dim='hour') + 1

    lon = precip.lon

    peak_hour_lst = (peak_hour_utc + lon / 15) % 24

    peak_hour_lst = np.where((peak_hour_lst < 0.5) & (peak_hour_lst >= 0), 24, peak_hour_lst)

    peak_hour_lst = np.where((peak_hour_lst >= 0.5) & (peak_hour_lst < 1), 1, peak_hour_lst)

    plt.figure(figsize=(6, 10), dpi=150)

    ax = plt.axes(projection=ccrs.PlateCarree())

    im = plt.contourf(precip_conus.lon, precip_conus.lat, peak_hour_lst, cmap='twilight_shifted', levels=np.arange(1, 25, 1), transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, label='Peak Precipitation Hour (LST)', orientation='horizontal', pad=0.02)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    plt.title('Peak Precipitation Time of the Diurnal Cycle (LST) - CONUS')

    plt.tight_layout()

    plt.show()

    fft_coeffs = np.fft.fft(precip_diurnal, axis=0)

    first_harmonic = fft_coeffs[1]

    phase_radians = np.angle(first_harmonic)

    phase_hours_utc = phase_radians / (2 * np.pi) * 24

    lon_1d = precip_diurnal.lon

    lon_2d = np.broadcast_to(lon_1d, phase_hours_utc.shape)

    print(phase_hours_utc.shape)

    print(lon.shape)

    phase_hours_lst = (phase_hours_utc + lon_2d / 15) % 24

    peak_hour_lst = np.where((peak_hour_lst < 0.5) & (peak_hour_lst >= 0), 24, peak_hour_lst)

    peak_hour_lst = np.where((peak_hour_lst >= 0.5) & (peak_hour_lst < 1), 1, peak_hour_lst)

    colors = [(0.0, 'cyan'), (0.125, 'blue'), (0.25, 'darkblue'), (0.375, 'purple'), (0.5, 'red'), (0.625, 'orange'), (0.75, 'yellow'), (0.875, 'green'), (1.0, 'cyan')]

    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)

    norm = mcolors.Normalize(vmin=0, vmax=24)

    plt.figure(figsize=(10, 6))

    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})

    im = plt.contourf(precip_diurnal.lon, precip_diurnal.lat, peak_hour_lst, levels=np.arange(1, 25, 1), cmap=custom_cmap, transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, label='Phase of 1st Harmonic (Peak Precip Time in LST)', norm=norm)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    plt.title('Phase of First Harmonic of the Diurnal Cycle (LST) - CONUS')

    plt.show()

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    lat = ds['lat']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(24, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(10, 70), lon=slice(235, 294))

    precip_daily = precip_conus.resample(time='1D').mean()

    precip_conus['hour'] = precip_conus.time.dt.hour

    precip_diurnal = precip_conus.groupby('hour').mean(dim='time')

    fft_coeffs = np.fft.fft(precip_diurnal, axis=0)

    first_harmonic = fft_coeffs[1]

    phase_radians = np.angle(first_harmonic)

    phase_hours_utc = phase_radians / (2 * np.pi) * 24

    lon_1d = precip_diurnal.lon

    lon_2d = np.broadcast_to(lon_1d, phase_hours_utc.shape)

    print(phase_hours_utc.shape)

    phase_hours_lst = (phase_hours_utc + lon_2d / 15) % 24

    peak_hour_lst = np.where((phase_hours_lst < 0.5) & (phase_hours_lst >= 0), 24, phase_hours_lst)

    peak_hour_lst = np.where((phase_hours_lst >= 0.5) & (phase_hours_lst < 1), 1, phase_hours_lst)

    colors = [(0.0, 'cyan'), (0.125, 'blue'), (0.25, 'darkblue'), (0.375, 'purple'), (0.5, 'red'), (0.625, 'orange'), (0.75, 'yellow'), (0.875, 'green'), (1.0, 'cyan')]

    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)

    norm = mcolors.Normalize(vmin=0, vmax=24)

    plt.figure(figsize=(10, 6))

    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})

    im = plt.contourf(precip_diurnal.lon, precip_diurnal.lat, peak_hour_lst, levels=np.arange(1, 25, 1), cmap=custom_cmap, transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, label='Phase of 1st Harmonic (Peak Precip Time in LST)', norm=norm)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    plt.title('Phase of First Harmonic of the Diurnal Cycle (LST) - CONUS')

    plt.show()

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    lat = ds['lat']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(24, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(10, 70), lon=slice(235, 294))

    precip_daily = precip_conus.resample(time='1D').mean()

    precip_conus['hour'] = precip_conus.time.dt.hour

    precip_diurnal = precip_conus.groupby('hour').mean(dim='time')

    fft_coeffs = np.fft.fft(precip_diurnal, axis=0)

    first_harmonic = fft_coeffs[1]

    phase_radians = np.angle(first_harmonic)

    phase_hours_utc = phase_radians / (2 * np.pi) * 24

    lon_1d = precip_diurnal.lon

    lon_2d = np.broadcast_to(lon_1d, phase_hours_utc.shape)

    print(phase_hours_utc.shape)

    phase_hours_lst = (phase_hours_utc + lon_2d / 15) % 24

    peak_hour_lst = np.where((phase_hours_lst < 0.5) & (phase_hours_lst >= 0), 24, phase_hours_lst)

    peak_hour_lst = np.where((phase_hours_lst >= 0.5) & (phase_hours_lst < 1), 1, phase_hours_lst)

    colors = [(0.0, 'cyan'), (0.125, 'blue'), (0.25, 'darkblue'), (0.375, 'purple'), (0.5, 'red'), (0.625, 'orange'), (0.75, 'yellow'), (0.875, 'green'), (1.0, 'cyan')]

    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)

    norm = mcolors.Normalize(vmin=0, vmax=24)

    plt.figure(figsize=(10, 6))

    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})

    im = plt.contourf(precip_diurnal.lon, precip_diurnal.lat, peak_hour_lst, levels=np.arange(1, 25, 1), cmap=custom_cmap, transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, label='Phase of 1st Harmonic (Peak Precip Time in LST)', norm=norm)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    plt.title('Phase of First Harmonic of the Diurnal Cycle (LST) - CONUS')

    plt.show()

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(24, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(10, 70), lon=slice(235, 294))

    lon_conus = precip_conus.lon

    precip_conus['hour'] = precip_conus.time.dt.hour

    precip_diurnal = precip_conus.groupby('hour').mean(dim='time')

    lon = precip_diurnal.lon.values

    N = 24

    gmt_hours = np.linspace(0, 24, N, endpoint=False)

    t = np.zeros((N, len(lon)))

    for i in range(len(lon)):
        t[:, i] = (gmt_hours + lon[i] / 15.0) % 24

    c, maxvalue, tmax = ff.fastAllGridFT(precip_diurnal.values, t)

    tmax.shape

    tmax = np.where((tmax < 0.5) & (tmax >= 0), 24, tmax)

    tmax = np.where((tmax >= 0.5) & (tmax < 1), 1, tmax)

    colors = [(0.0, 'cyan'), (0.125, 'blue'), (0.25, 'darkblue'), (0.375, 'purple'), (0.5, 'red'), (0.625, 'orange'), (0.75, 'yellow'), (0.875, 'green'), (1.0, 'cyan')]

    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)

    norm = mcolors.Normalize(vmin=0, vmax=24)

    plt.figure(figsize=(10, 6))

    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})

    im = plt.contourf(precip_diurnal.lon, precip_diurnal.lat, tmax[0], levels=np.arange(1, 25, 1), cmap=custom_cmap, transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, label='Phase of 1st Harmonic (Peak Precip Time in LST)', norm=norm)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linestyle='--')

    gl.top_labels = False

    gl.right_labels = False

    plt.title('Phase of First Harmonic of the Diurnal Cycle (LST) - CONUS')

    plt.show()

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(24, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(10, 70), lon=slice(235, 294))

    precip_conus = precip_conus.sel(time=precip.time.dt.month.isin([6, 7, 8]))

    lon_conus = precip_conus.lon

    precip_conus['hour'] = precip_conus.time.dt.hour

    precip_diurnal = precip_conus.groupby('hour').mean(dim='time')

    lon = precip_diurnal.lon.values

    N = 24

    gmt_hours = np.linspace(0, 24, N, endpoint=False)

    t = np.zeros((N, len(lon)))

    for i in range(len(lon)):
        t[:, i] = (gmt_hours + lon[i] / 15.0) % 24

    c, maxvalue, tmax = ff.fastAllGridFT(precip_diurnal.values, t)

    tmax = np.where((tmax < 0.5) & (tmax >= 0), 24, tmax)

    tmax = np.where((tmax >= 0.5) & (tmax < 1), 1, tmax)

    colors = ['cyan', 'violet', 'blue', 'red', 'yellow', 'green', 'cyan']

    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)

    norm = mcolors.Normalize(vmin=0, vmax=24)

    plt.figure(figsize=(10, 6))

    projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=39, standard_parallels=(33, 45))

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})

    im = plt.contourf(precip_diurnal.lon, precip_diurnal.lat, tmax[0], levels=np.arange(1, 25, 1), cmap=custom_cmap, transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, label='Phase of 1st Harmonic (Peak Precip Time in LST)', norm=norm)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linestyle='--')

    gl.top_labels = False

    gl.right_labels = False

    plt.title('Phase of First Harmonic of the Diurnal Cycle (LST) - CONUS')

    plt.show()

    plt.savefig('your/file/path')

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})

    im = plt.contourf(precip_diurnal.lon, precip_diurnal.lat, tmax[0], levels=np.arange(1, 25, 1), cmap=custom_cmap, transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, label='Phase of 1st Harmonic (Peak Precip Time in LST)', norm=norm)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linestyle='--')

    gl.top_labels = False

    gl.right_labels = False

    plt.title('Phase of First Harmonic of the Diurnal Cycle (LST) - CONUS')

    plt.savefig('your/file/path')

    precip

    c.shape

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': projection})

    im = plt.contourf(precip_diurnal.lon, precip_diurnal.lat, c * 86400, levels=np.arange(0.5, 13), cmap=custom_cmap, transform=ccrs.PlateCarree(), extend='both')

    cbar = plt.colorbar(im, label='Precip max value (Peak Precip Time in LST)', norm=norm)

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    ax.coastlines()

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linestyle='--')

    gl.top_labels = False

    gl.right_labels = False

    plt.title('Precip max value (LST) - CONUS')

    plt.show()

    plt.savefig('your/file/path')

    peak_time_utc = precip.time[peak_time_idx]

    precip_daily

    peak_utc_hours = peak_time_utc.dt.hour + peak_time_utc.dt.minute / 60

    lon = precip.lon

    peak_lst = (peak_utc_hours + lon / 15) % 24

    colors = [(0.0, (0, 1, 1)), (0.125, 'blue'), (0.25, 'darkblue'), (0.375, 'purple'), (0.5, 'red'), (0.625, 'orange'), (0.75, 'yellow'), (0.875, 'green'), (1.0, (0, 1, 1))]

    custom_cmap = mcolors.LinearSegmentedColormap.from_list('custom_LST', colors)

    norm = mcolors.Normalize(vmin=0, vmax=24)

    plt.figure(figsize=(12, 6))

    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.set_extent([-125, -66, 24, 50], crs=ccrs.PlateCarree())

    im = plt.contourf(precip_conus.lon, precip_conus.lat, peak_lst, levels=np.arange(0, 25, 1), cmap=custom_cmap, norm=norm, transform=ccrs.PlateCarree())

    cbar = plt.colorbar(im, ticks=np.arange(0, 25, 1), label='Peak Precipitation Time (LST) [hours]')

    ax.coastlines()

    plt.title('Local Solar Time of Peak Precipitation')

    plt.show()

    base_dir = 'your/file/path'

    years = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])

    all_years_ds = []

    for year in years:
        year_path = os.path.join(base_dir, year)
        print(f'Processing year: {year}')
        file_list = sorted(glob.glob(os.path.join(year_path, '*.HDF5')))
        ds_list = []
        for file in file_list:
            with h5py.File(file, 'r') as f:
                precip = f['Grid']['precipitation'][:]
                time = f['Grid']['time'][:]
                lat = f['Grid']['lat'][:]
                lon = f['Grid']['lon'][:]
                time_reference = np.datetime64('1980-01-06')
                time = time_reference + np.timedelta64(int(time[0]), 's')
                ds = xr.Dataset({'precipitation': (['lat', 'lon'], precip.squeeze())}, coords={'lat': lat, 'lon': lon, 'time': time})
                ds_list.append(ds)
        if ds_list:
            year_ds = xr.concat(ds_list, dim='time')
            all_years_ds.append(year_ds)

    final_ds = xr.concat(all_years_ds, dim='time')

    final_ds.to_netcdf('your/file/path')

    print(final_ds)

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
