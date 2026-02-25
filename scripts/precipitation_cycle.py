"""Script `precipitation_cycle`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import os
import h5py
import numpy as np
import xarray as xr
import time
from multiprocessing import Pool, cpu_count
import xarray as sr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import os
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import plot_precip as pp
import plot_precip as pp
import plot_precip as pp
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import plot_precip as pp
import plot_precip as pp
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import plot_precip as pp
import plot_precip as pp
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import plot_precip as pp
import plot_precip as pp
import xarray as xr
import glob
import os
import xarray as xr
import glob
import os
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import plot_precip as pp
import plot_precip as pp
import fastFT as ff
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import xarray as xr
import plot_precip as pp
import plot_precip as pp

logger = logging.getLogger(__name__)

def process_file(file_path):
    """Reads a single HDF5 IMERG file and extracts precipitation, time, lat, lon."""
    start_time = time.time()
    with h5py.File(file_path, 'r') as f:
        precip = f['Grid/precipitation'][:]
        time_data = f['Grid/time'][:]
        lat = f['Grid/lat'][:]
        lon = f['Grid/lon'][:]
    duration = time.time() - start_time
    return (precip, time_data, lat, lon, duration)

def process_year(year):
    data_dir = os.path.join(input_root, year)
    output_file = os.path.join(output_root, f'IMERG_{year}_conus.nc')
    file_list = sorted([os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.HDF5') and (str(year) + '06' in f or str(year) + '07' in f or str(year) + '08' in f)])
    if not file_list:
        print(f'No summer files found for {year}, skipping...')
        return
    print(f'\nProcessing {len(file_list)} files for year {year}')
    start_time_total = time.time()
    with Pool(processes=NUM_WORKERS) as pool:
        results = pool.map(process_file, file_list)
    precip_list, time_list, lat_list, lon_list, time_durations = zip(*results)
    precip_stack = np.concatenate(precip_list, axis=0)
    time_stack = np.concatenate(time_list, axis=0)
    lat_grid = lat_list[0]
    lon_grid = lon_list[0]
    lat_indices = np.where((lat_grid >= lat_min) & (lat_grid <= lat_max))[0]
    lon_indices = np.where((lon_grid >= lon_min) & (lon_grid <= lon_max))[0]
    lat_subset = lat_grid[lat_indices]
    lon_subset = lon_grid[lon_indices]
    precip_subset = precip_stack[:, lon_indices, :][:, :, lat_indices]
    print(f'Subset precipitation shape: {precip_subset.shape}')
    print(f'Lat subset shape: {lat_subset.shape}, range: {lat_subset[0]} to {lat_subset[-1]}')
    print(f'Lon subset shape: {lon_subset.shape}, range: {lon_subset[0]} to {lon_subset[-1]}')
    ds_conus = xr.Dataset({'precipitation': (['time', 'lon', 'lat'], precip_subset)}, coords={'time': time_stack, 'lon': lon_subset, 'lat': lat_subset})
    ds_conus.to_netcdf(output_file, encoding={'precipitation': {'zlib': True, 'complevel': 4}})
    total_duration = time.time() - start_time_total
    print(f'Saved {year} CONUS data to {output_file} in {total_duration:.2f} seconds')

def run(cfg: dict) -> None:
    input_root = 'your/file/path'

    output_root = 'your/file/path'

    years = sorted([d for d in os.listdir(input_root) if d.isdigit()])

    print(f'Found {len(years)} years: {years}')

    NUM_WORKERS = min(8, cpu_count())

    lat_min, lat_max = (24, 50)

    lon_min, lon_max = (-125, -65)

    for year in years:
        process_year(year)

    print('\n All years processed successfully!')

    year_2006 = xr.open_dataset('your/file/path')

    mean_precip = year_2006['precipitation'].mean(dim='time')

    print(mean_precip.values.shape)

    print(year_2006['lon'].values.shape)

    print(year_2006['lat'].values.shape)

    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})

    ax.set_extent([-125, -65, 24, 50], crs=ccrs.PlateCarree())

    ax.add_feature(cfeature.COASTLINE)

    p = ax.contourf(year_2006['lon'].values, year_2006['lat'].values, mean_precip.values.T, cmap='Blues', transform=ccrs.PlateCarree())

    plt.colorbar(p, ax=ax, orientation='vertical', label='Mean Precipitation (mm/hr)')

    plt.show()

    data_dir = 'your/file/path'

    file_list = sorted([os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.startswith('IMERG_') and f.endswith('_conus.nc')])

    print(f'📂 Found {len(file_list)} yearly files: {file_list}')

    ds = xr.open_mfdataset(file_list, combine='by_coords', chunks=None)

    ds.load()

    print(ds)

    ds['time'] = ds['time'].astype('datetime64[s]')

    ds['hour'] = ds['time'].dt.hour

    print(ds['hour'])

    ds = ds.set_coords('hour')

    hourly_precip = ds['precipitation'].groupby('hour').mean(dim='time')

    hourly_precip = hourly_precip.transpose('hour', 'lat', 'lon')

    lon = hourly_precip.lon.values

    N = 24

    gmt_hours = np.linspace(0, 24, N, endpoint=False)

    precip_diurnal = hourly_precip

    t = np.zeros((N, len(lon)))

    for i in range(len(lon)):
        t[:, i] = (gmt_hours + lon[i] / 15.0) % 24

    c, maxvalue, tmax = ff.fastAllGridFT(precip_diurnal.values, t)

    pp.plot_precip_phase(precip_diurnal, tmax, 'IMERG')

    pp.plot_precip_peak(precip_diurnal, maxvalue, 'IMERG')

    pp.plot_precip_mean_rate(precip_diurnal, c, 'IMERG')

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(24, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(25, 50), lon=slice(235, 294))

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

    tmax = np.round(tmax)

    pp.plot_precip_phase(precip_diurnal, tmax, 'AM4')

    pp.plot_precip_peak(precip_diurnal, maxvalue, 'AM4')

    pp.plot_precip_mean_rate(precip_diurnal, c, 'AM4')

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(20, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(25, 50), lon=slice(235, 294))

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

    tmax = np.round(tmax)

    pp.plot_precip_phase(precip_diurnal, tmax, 'AM4-CLUBB_DM')

    pp.plot_precip_peak(precip_diurnal, maxvalue, 'AM4-CLUBB_DM')

    pp.plot_precip_mean_rate(precip_diurnal, c, 'AM4-CLUBB_DM')

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

    tmax = np.round(tmax)

    pp.plot_precip_phase(precip_diurnal, tmax, 'AM4-CLUBB_PM')

    pp.plot_precip_peak(precip_diurnal, maxvalue, 'AM4-CLUBB_PM')

    pp.plot_precip_mean_rate(precip_diurnal, c, 'AM4-CLUBB_PM')

    file_pattern = 'atmos_level.*.precip.nc'

    input_folder = 'your/file/path'

    output_folder = 'your/file/path'

    output_file = os.path.join(output_folder, 'merged_summer_precip.nc')

    file_list = sorted(glob.glob(os.path.join(input_folder, file_pattern)))

    summer_datasets = []

    for file in file_list:
        print(f'Processing {file}...')
        ds = xr.open_dataset(file)
        summer_ds = ds.sel(time=ds.time.dt.month.isin([6, 7, 8]))
        summer_datasets.append(summer_ds)

    merged_summer = xr.concat(summer_datasets, dim='time')

    print(f'Saving merged summer dataset to {output_file}...')

    merged_summer.to_netcdf(output_file, format='NETCDF4')

    print('Done!')

    file_pattern = 'atmos_level.*.precip.nc'

    input_folder = 'your/file/path'

    output_folder = 'your/file/path'

    output_file = os.path.join(output_folder, 'merged_summer_precip.nc')

    file_list = sorted(glob.glob(os.path.join(input_folder, file_pattern)))

    summer_datasets = []

    for file in file_list:
        print(f'Processing {file}...')
        ds = xr.open_dataset(file)
        summer_ds = ds.sel(time=ds.time.dt.month.isin([6, 7, 8]))
        summer_datasets.append(summer_ds)

    merged_summer = xr.concat(summer_datasets, dim='time')

    print(f'Saving merged summer dataset to {output_file}...')

    merged_summer.to_netcdf(output_file, format='NETCDF4')

    print('Done!')

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(24, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(25, 50), lon=slice(235, 294))

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

    tmax = np.round(tmax)

    pp.plot_precip_phase(precip_diurnal, tmax, 'AM4-CLUBB_DM_X')

    pp.plot_precip_peak(precip_diurnal, maxvalue, 'AM4-CLUBB_DM_X')

    pp.plot_precip_mean_rate(precip_diurnal, c, 'AM4-CLUBB_DM_X')

    file_path = 'your/file/path'

    ds = xr.open_dataset(file_path, engine='netcdf4')

    precip = ds['precip']

    time = ds['time']

    if precip.lon.min() < 0:
        precip_conus = precip.sel(lat=slice(25, 50), lon=slice(-125, -66))
    else:
        precip_conus = precip.sel(lat=slice(25, 50), lon=slice(235, 294))

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

    tmax = np.round(tmax)

    pp.plot_precip_phase(precip_diurnal, tmax, 'AM4-CLUBB_PM_X')

    pp.plot_precip_peak(precip_diurnal, maxvalue, 'AM4-CLUBB_PM_X')

    pp.plot_precip_mean_rate(precip_diurnal, c, 'AM4-CLUBB_PM_X')

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
