"""Script `read_hourly`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import xarray as xr
import glob
import pandas as pd
import os
import xarray as xr

logger = logging.getLogger(__name__)

class load_jja_variable:

    def __init__(self, data_path, var):
        """
        Load a merged xarray.Dataset for a given variable across years 0002–0006,
        keeping only summer months (June–August).
        
        Parameters:
         data_path (str): Path to the directory containing the netCDF files
            var (str): Variable name, e.g. "z_half"
    
        Returns:
            xarray.Dataset: Merged dataset filtered for summer months
        """
        file_pattern = f'{data_path}/atmos_level*.{var}.nc'
        file_list = sorted(glob.glob(file_pattern))
        print(file_list)
        if not file_list:
            raise FileNotFoundError(f'No files found for pattern: {file_pattern}')
        ds = xr.open_mfdataset(file_list, combine='by_coords', parallel=True)
        print('reading ds')
        ds_jja = ds.sel(time=ds['time'].dt.month.isin([6, 7, 8]))
        self.object = ds_jja

class AtmosDiagnostics:

    def __init__(self, directory, local_lon):
        self.directory = directory
        self.local_lon = local_lon
        self._load_summer_datasets()

    def _load_summer_datasets_old(self):
        for fname in os.listdir(self.directory):
            if not fname.endswith('.nc'):
                continue
            full_path = os.path.join(self.directory, fname)
            var_name = self._extract_var_name(fname)
            try:
                ds = xr.open_dataset(full_path)
                if 'time' in ds.coords:
                    summer_ds = ds.sel(time=ds['time'].dt.month.isin([6, 7, 8]))
                else:
                    print(f'No time dimension found in {fname}, skipping.')
                    continue
                hours = summer_ds['time'].dt.hour
                is_day = hours.isin(range(6, 18))
                is_night = ~is_day
                gp = [36, 37, 262, 264]
                day_ds = summer_ds.sel(time=is_day).sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3]))
                night_ds = summer_ds.sel(time=is_night).sel(lat=slice(gp[0], gp[1]), lon=slice(gp[2], gp[3]))
                setattr(self, f'{var_name}_day', day_ds)
                setattr(self, f'{var_name}_night', night_ds)
                print(f'Loaded {var_name}: {day_ds.time.size} daytime steps, {night_ds.time.size} nighttime steps')
            except Exception as e:
                print(f'Failed to process {fname}: {e}')

    def _load_summer_datasets(self):
        for fname in os.listdir(self.directory):
            if not fname.endswith('.nc'):
                continue
            full_path = os.path.join(self.directory, fname)
            var_name = self._extract_var_name(fname)
            try:
                ds = xr.open_dataset(full_path)
                if 'time' not in ds.coords:
                    print(f'No time dimension found in {fname}, skipping.')
                    continue
                summer_ds = ds.sel(time=ds['time'].dt.month.isin([6, 7, 8]))
                time_utc = summer_ds['time']
                offset_hours = self.local_lon / 15.0
                time_local = time_utc + pd.to_timedelta(offset_hours, unit='h')
                hours_local = time_local.dt.hour
                is_day = hours_local.isin(range(6, 18))
                is_night = ~is_day
                day_ds = summer_ds.sel(time=is_day)
                night_ds = summer_ds.sel(time=is_night)
                setattr(self, f'{var_name}_day', day_ds)
                setattr(self, f'{var_name}_night', night_ds)
                print(f'Loaded {var_name} using LST (lon={self.local_lon}): {day_ds.time.size} day, {night_ds.time.size} night')
            except Exception as e:
                print(f'Failed to process {fname}: {e}')

    def mean_day_night(self, var):
        """Returns (day_mean, night_mean) for the primary variable."""
        try:
            day_data = getattr(self, f'{var}_day')[var].mean(dim='time')
            night_data = getattr(self, f'{var}_night')[var].mean(dim='time')
            return (day_data, night_data)
        except AttributeError as e:
            raise ValueError(f"Variable '{var}' not found. Did you load it correctly?") from e

    def _extract_var_name(self, filename):
        parts = filename.split('.')
        if len(parts) >= 3:
            return parts[-2]
        else:
            raise ValueError(f'Cannot extract variable name from filename: {filename}')

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
