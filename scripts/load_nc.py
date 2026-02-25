"""Script `load_nc`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import xarray as xr
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

class loader_am4:

    def __init__(self, ftype, filename):
        """
        
        Parameters
        ----------
        ftype: string
            describes field type to analyse
        filename : string
            describes name of am4 run
        coords : list
            describes lat/long bounds

        Returns
        -------
        None.

        """
        self.path = '../clim_am4_clubb_data/'
        self.ftype = ftype
        self.filename = filename
        self.xr_object = xr.open_dataset(self.path + self.filename)

    def load_var(self):
        if self.ftype == 'u_ref':
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'v_ref':
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'wind_ref':
            self.u10 = self.xr_object['u_ref']
            self.v10 = self.xr_object['v_ref']
            self.u10.data = self.u10.data ** 2
            self.v10.data = self.v10.data ** 2
            self.object = self.u10.copy()
            self.object.data = self.u10.data ** 2 + self.v10.data ** 2
        elif self.ftype == 'z_Ri_025':
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'ucomp':
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'vcomp':
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'z_full':
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'zsurf':
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'ps':
            self.object = self.xr_object['slp_dyn']
        elif self.ftype == 'stress':
            self.tau_x = self.xr_object['tau_x']
            self.tau_y = self.xr_object['tau_y']
            self.object = self.tau_x.copy()
            self.object.data = np.sqrt(self.tau_x.data ** 2 + self.tau_y.data ** 2 / float(1.2))
        elif self.ftype == 'wind_925':
            self.ucomp = self.xr_object['ucomp']
            self.vcomp = self.xr_object['vcomp']
            self.wind = self.ucomp[:, 1, :, :] ** 2 + self.vcomp[:, 1, :, :] ** 2
        else:
            raise ValueError('the ftype requested is not available')

    def zoom(self):
        print('##################################')
        print('I am zooming with specified coords')
        self.coords = [20.0, 50.0, -130.0, -70.0]
        self.load_var()
        self.xr_object.coords['lon'] = (self.xr_object.coords['lon'] + 180) % 360 - 180
        self.xr_object = self.xr_object.sortby(self.xr_object.lon)
        self.field = self.object.sel(lat=slice(self.coords[0], self.coords[1]), lon=slice(self.coords[2], self.coords[3]))

class loader_era5:

    def __init__(self, ftype, filename):
        """
        
        Parameters
        ----------
        ftype: string
            describes field type to analyse
        filename : string
            describes name of am4 run
        coords : list
            describes lat/long bounds

        Returns
        -------
        None.

        """
        self.path = '../../../../../scratch/gpfs/eg3736/clim_am4_clubb_data/'
        self.ftype = ftype

    def load_var(self):
        if self.ftype == 'u10':
            self.filename = 'ucomp_10.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'v10':
            self.filename = 'vcomp_10.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'wind_ref':
            self.filename = 'ucomp_10.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.u10 = self.xr_object['u10']
            self.filename = 'vcomp_10.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.v10 = self.xr_object['v10']
            self.object = self.u10.copy()
            self.object.data = self.u10.data ** 2 + self.v10.data ** 2
        elif self.ftype == 'u':
            self.filename = 'ucomp.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'v':
            self.filename = 'vcomp.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'blh':
            self.filename = 'bl_height.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'mslp':
            self.filename = 'mslp.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object['msl']
        elif self.ftype == 'ustar':
            self.filename = 'u_star.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object['zust']
        elif self.ftype == 'z':
            self.filename = 'geopotential.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'zsurf':
            self.ftype = 'z'
            self.filename = 'geopotential_surf.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object[self.ftype]
        elif self.ftype == 'stress':
            self.tau_x = self.xr_object['tau_x']
            self.tau_y = self.xr_object['tau_y']
            self.object = self.tau_x.copy()
            self.object.data = np.sqrt(self.tau_x.data ** 2 + self.tau_y.data ** 2 / float(1.2))
        elif self.ftype == 'wind_925':
            self.filename = 'ucomp.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.ucomp = self.xr_object['u']
            self.filename = 'vcomp.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.vcomp = self.xr_object['v']
            self.wind = self.ucomp[:, -4, :, :] ** 2 + self.vcomp[:, -4, :, :] ** 2
        else:
            raise ValueError('the ftype requested is not available')

    def zoom(self):
        self.coords = [20.0, 50.0, -130.0, -70.0]
        self.load_var()
        self.xr_object.coords['longitude'] = (self.xr_object.coords['longitude'] + 180) % 360 - 180
        self.xr_object = self.xr_object.sortby(self.xr_object.longitude)
        self.field = self.xr_object[self.ftype].sel(latitude=slice(self.coords[1], self.coords[0]), longitude=slice(self.coords[2], self.coords[3]))

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
