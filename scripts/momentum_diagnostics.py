"""Script `momentum_diagnostics`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

logger = logging.getLogger(__name__)

class momentum_diagnostics:

    def __init__(self, dudt_diff, dvdt_diff, zfull, zhalf, u_comp, v_comp):
        """
        Initialise class to compute momentum diagnostics 
        dudt_diff: xarray
            tendency of zonal wind component due to vertical diffusion (lock or CLUBB) [ms-2]
        dvdt_diff: xarray
            tendency of zonal wind component due to vertical diffusion (lock or CLUBB) ms-2
        zfull: xarray
            geopotential height full levels 
        zhalf: xarray
            geopotential height half levels 
        u_comp: xarray
            zonal wind speed on full levels
        v_comp: xarray
            meridional wind speed on full levels 
        """
        self.dudt_diff = dudt_diff
        self.dvdt_diff = dvdt_diff
        self.zfull = zfull.copy()
        self.zhalf = zhalf.copy()
        self.u_comp = u_comp.copy()
        self.v_comp = v_comp.copy()
        self.axis_idx = 1
        self.dir = (180 + np.degrees(np.arctan2(self.u_comp, self.v_comp))) % 360

    def diff_zhalf(self):
        """
        Compute differences between half-height levels 
        Note that zhalf[bottom] = zsurf
        """
        print(self.zhalf.data.shape)
        print(np.diff(self.zhalf.data, axis=self.axis_idx).shape)
        diff_zhalf_array = np.diff(self.zhalf.data, axis=self.axis_idx)
        self.diff_zhalf = self.zfull.copy()
        self.diff_zhalf.data = diff_zhalf_array

    def upwp_vpwp(self):
        """
        Compute \\overline{upwp} and \\overline{vpwp} from vertical diffusion tendency .
        """
        self.diff_zhalf()
        self.upwp = self.zhalf.copy()
        self.upwp.data[:, 0, :, :] = 0
        self.upwp.data[:, 1:, :] = -self.dudt_diff.data * self.diff_zhalf.data
        self.upwp.data = np.cumsum(self.upwp.data, axis=self.axis_idx)
        self.vpwp = self.zhalf.copy()
        self.vpwp.data[:, 0, :, :] = 0
        self.vpwp.data[:, 1:, :] = -self.dvdt_diff.data * self.diff_zhalf.data
        self.vpwp.data = np.cumsum(self.vpwp.data, axis=self.axis_idx)

    def du_dz(self):
        """
        Compute gradient of zonal wind w.r.t full height levels 
        """
        self.dudz = self.u_comp.copy()
        self.dudz.data[:, 1:, :, :] = np.diff(self.u_comp.data, axis=self.axis_idx) / np.diff(self.zfull.data, axis=self.axis_idx)

    def dv_dz(self):
        """
        Compute gradient of meridional wind w.r.t full height levels 
        """
        self.dvdz = self.v_comp.copy()
        self.dvdz.data[:, 1:, :, :] = np.diff(self.v_comp.data, axis=self.axis_idx) / np.diff(self.zfull.data, axis=self.axis_idx)

    def compute_k_m(self):
        """
        Compute eddy diffusivity coefficient, defined
        """
        self.du_dz()
        self.dv_dz()
        self.k_m = self.zhalf.copy()
        self.k_m[:, 0, :, :] = 0
        self.k_m.data[:, 1:, :, :] = np.sqrt(self.upwp.data[:, 1:, :, :] ** 2 + self.vpwp.data[:, 1:, :, :] ** 2) / np.sqrt(self.dudz.data ** 2 + self.dvdz.data ** 2)

    def manage_diagnostics(self):
        """
        Manage computation of momentum diagnostics 
        """
        self.upwp_vpwp()
        self.compute_k_m()

class momentum_diagnostics_diurnal:

    def __init__(self, dudt_diff, dvdt_diff, zfull, zhalf, u_comp, v_comp):
        """
        Initialise class to compute momentum diagnostics 
        dudt_diff: xarray
            tendency of zonal wind component due to vertical diffusion (lock or CLUBB) [ms-2]
        dvdt_diff: xarray
            tendency of zonal wind component due to vertical diffusion (lock or CLUBB) ms-2
        zfull: xarray
            geopotential height full levels 
        zhalf: xarray
            geopotential height half levels 
        u_comp: xarray
            zonal wind speed on full levels
        v_comp: xarray
            meridional wind speed on full levels 
        """
        self.dudt_diff = dudt_diff
        self.dvdt_diff = dvdt_diff
        self.zfull = zfull.copy()
        self.zhalf = zhalf.copy()
        self.u_comp = u_comp.copy()
        self.v_comp = v_comp.copy()
        self.axis_idx = 0
        self.dir = (180 + np.degrees(np.arctan2(self.u_comp, self.v_comp))) % 360

    def diff_zhalf(self):
        """
        Compute differences between half-height levels 
        Note that zhalf[bottom] = zsurf
        """
        print(self.zhalf.data.shape)
        print(np.diff(self.zhalf.data, axis=self.axis_idx).shape)
        diff_zhalf_array = np.diff(self.zhalf.data, axis=self.axis_idx)
        self.diff_zhalf = self.zfull.copy()
        self.diff_zhalf.data = diff_zhalf_array

    def upwp_vpwp(self):
        """
        Compute \\overline{upwp} and \\overline{vpwp} from vertical diffusion tendency .
        """
        self.diff_zhalf()
        self.upwp = self.zhalf.copy()
        self.upwp.data[0, :, :] = 0
        self.upwp.data[1:, :, :] = -self.dudt_diff.data * self.diff_zhalf.data
        self.upwp.data = np.cumsum(self.upwp.data, axis=self.axis_idx)
        self.vpwp = self.zhalf.copy()
        self.vpwp.data[0, :, :] = 0
        self.vpwp.data[1:, :, :] = -self.dvdt_diff.data * self.diff_zhalf.data
        self.vpwp.data = np.cumsum(self.vpwp.data, axis=self.axis_idx)

    def du_dz(self):
        """
        Compute gradient of zonal wind w.r.t full height levels 
        """
        self.dudz = self.u_comp.copy()
        self.dudz.data[1:, :, :] = np.diff(self.u_comp.data, axis=self.axis_idx) / np.diff(self.zfull.data, axis=self.axis_idx)

    def dv_dz(self):
        """
        Compute gradient of meridional wind w.r.t full height levels 
        """
        self.dvdz = self.v_comp.copy()
        self.dvdz.data[1:, :, :] = np.diff(self.v_comp.data, axis=self.axis_idx) / np.diff(self.zfull.data, axis=self.axis_idx)

    def compute_k_m(self):
        """
        Compute eddy diffusivity coefficient, defined
        """
        self.du_dz()
        self.dv_dz()
        self.k_m = self.zhalf.copy()
        self.k_m[0, :, :] = 0
        self.k_m.data[1:, :, :] = np.sqrt(self.upwp.data[1:, :, :] ** 2 + self.vpwp.data[1:, :, :] ** 2) / np.sqrt(self.dudz.data ** 2 + self.dvdz.data ** 2)

    def manage_diagnostics(self):
        """
        Manage computation of momentum diagnostics 
        """
        self.upwp_vpwp()
        self.compute_k_m()

class plot_momentum_diagnostics:

    def __init__(self, diagnostics, zfulls, zhalfs, bl_heights, diag_type, coords):
        """
        diagnostic: list of xarrays 
           diagnostic to plot
        coords: list of integers
            lat/lon box to zoom in for plotting 
        """
        self.diagnostics = diagnostics
        self.zfulls = zfulls
        self.zhalfs = zhalfs
        self.bl_heights = bl_heights
        self.diag_type = diag_type
        self.coords = coords

    def plot_diagnostics(self, save_fig):
        """
        Plot diagnostics 
        """
        self.min_lat = self.coords[0]
        self.max_lat = self.coords[1]
        self.min_lon = self.coords[2]
        self.max_lon = self.coords[3]
        colors = ['blue', 'orange', 'green', 'magenta', 'darkblue', 'gray']
        labels = ['AM4 ', 'AM4-CLUBB_DM ', 'AM4-CLUBB_DM_X ', 'AM4-CLUBB_PM ', 'AM4-CLUBB_PM_X ', 'ERA5']
        if self.diag_type in ['dudt', 'dvdt']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(500, 1000)) * 10 ** 5
                y_axis = 'pfull'
                plot_config = config_slice.mean(dim=['lat', 'lon']).plot(y=y_axis, color=colors[i], yincrease=False, label=labels[i])
            plt.legend(loc='upper right', fontsize=8)
            plt.title('')
            plt.ylabel('Reference pressure levels [hPa]')
            plt.xlabel('$\\frac{\\partial{u}}{\\partial{t}} [\\times{10^{-5}}ms^{-2}$]')
            plt.tight_layout()
            plt.show()
            fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
        elif self.diag_type in ['upwp', 'vpwp']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), phalf=slice(750, 1000))
                zfull_slice = self.zfulls[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                y_axis = 'zfull'
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values[0, :], zfull_slice.mean(dim=['lat', 'lon']).values[0, :] - zfull_slice.mean(dim=['lat', 'lon']).values[0, -1], color=colors[i], label=labels[i])
                plt.xlim([-0.2, 0.05])
                plt.ylim([0, 1500])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            if self.diag_type == 'upwp':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel("$\\overline{u'w'} [m^2s^{-2}]$")
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            elif self.diag_type == 'vpwp':
                plt.legend(loc='upper left', fontsize=8)
                plt.title('')
                plt.xlabel("$\\overline{v'w'} [m^2s^{-2}]$")
                plt.ylabel('Height from surface [m]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            elif self.diag_type == 'k_m':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel('$K_m$ [m$^2$s$^{-1}$]')
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            else:
                raise ValueError('Diag type does not exist')
        elif self.diag_type in ['u_comp', 'v_comp']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            print(self.diag_type)
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                zfull_slice = self.zfulls[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                bl_height_slice = self.bl_heights[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon))
                import xarray as xr
                zsurf = xr.open_dataset('your/file/path')
                zsurf_val = zsurf.zsurf.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon)).mean().values
                print('True surface height is:', zsurf_val)
                y_axis = 'zfull'
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values[0, :], zfull_slice.mean(dim=['lat', 'lon']).values[0, :] - zsurf_val, color=colors[i], label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=1)
                plt.axhline(bl_height_slice.mean(dim=['lat', 'lon']).values, color=colors[i], linestyle='--', linewidth=1)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            if self.diag_type == 'v_comp':
                import xarray as xr
                ds = xr.open_dataset('your/file/path')
                ds_box = ds.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), pressure_level=slice(1000, 500))
                ds_mean_spatial = ds_box.mean(dim=['latitude', 'longitude', 'date'])
                print(ds_mean_spatial)
                arm_summer_mean = xr.open_dataset('your/file/path')
                gp_era5 = xr.open_dataset('your/file/path').z.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), level=slice(500, 1000)).mean(dim=['latitude', 'longitude', 'time']).values * 9.81 ** (-1)
                bl_height_era5 = xr.open_dataset('your/file/path').blh.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon)).mean(dim=['latitude', 'longitude', 'time'])
                Re = 6371000
                gp_era5_true = Re * gp_era5 / (Re - gp_era5)
                print('ERA5 level heights', gp_era5)
                print(ds_mean_spatial['v'])
                plt.plot(ds_mean_spatial['v'].values, gp_era5_true[::-1], color='purple', label='ERA5')
                plt.axhline(bl_height_era5, color='purple', linewidth=1.0)
                plt.plot(arm_summer_mean.v.values, arm_summer_mean.height.values, linestyle='--', color='black', label='ARM obs')
                print('arm lowest', arm_summer_mean.height.values[0])
                plt.legend(loc='upper left', fontsize=8)
                plt.title('')
                plt.xlabel('$\\overline{v }$ [ms$^{-1}$]', fontsize=14)
                plt.ylabel('Height from surface [m]', fontsize=14)
                plt.tight_layout()
                plt.xlim([0, 8])
                plt.ylim([0, 1500])
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png', bbox_inches='tight')
            elif self.diag_type == 'u_comp':
                import xarray as xr
                print('we are in u_comp')
                ds = xr.open_dataset('your/file/path')
                ds_box = ds.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), pressure_level=slice(1000, 500))
                ds_mean_spatial = ds_box.mean(dim=['latitude', 'longitude', 'date'])
                print(ds_mean_spatial)
                arm_summer_mean = xr.open_dataset('your/file/path')
                gp_era5 = xr.open_dataset('your/file/path').z.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), level=slice(500, 1000)).mean(dim=['latitude', 'longitude', 'time']).values * 9.81 ** (-1)
                bl_height_era5 = xr.open_dataset('your/file/path').blh.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon)).mean(dim=['latitude', 'longitude', 'time'])
                Re = 6371000
                gp_era5_true = Re * gp_era5 / (Re - gp_era5)
                print('ERA5 level heights', gp_era5)
                print(ds_mean_spatial['u'])
                plt.plot(ds_mean_spatial['u'].values, gp_era5_true[::-1], color='purple', label='ERA5')
                plt.axhline(bl_height_era5, color='purple', linewidth=1.0)
                print('The summer array is:')
                print(arm_summer_mean)
                plt.plot(arm_summer_mean.u.values, arm_summer_mean.height.values, linestyle='--', color='black', label='ARM obs')
                print('arm lowest', arm_summer_mean.height.values[0])
                plt.legend(loc='upper left', fontsize=8)
                plt.title('')
                plt.xlabel('$\\overline{u }$ [m s$^{-1}$]', fontsize=14)
                plt.ylabel('Height from surface [m]', fontsize=14)
                plt.tight_layout()
                plt.xlim([-4, 4])
                plt.ylim([0, 1500])
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png', bbox_inches='tight')
        elif self.diag_type in ['dir']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            print(self.diag_type)
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                zfull_slice = self.zfulls[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                import xarray as xr
                zsurf = xr.open_dataset('your/file/path')
                zsurf_val = zsurf.zsurf.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon)).mean().values
                print('True surface height is:', zsurf_val)
                y_axis = 'zfull'
                print(config_slice.mean(dim=['lat', 'lon']).values[0, :])
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values[0, :], zfull_slice.mean(dim=['lat', 'lon']).values[0, :] - zsurf_val, color=colors[i], label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=1)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            import xarray as xr
            ds = xr.open_dataset('your/file/path')
            ds_box = ds.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), pressure_level=slice(1000, 500))
            ds_mean_spatial = ds_box.mean(dim=['latitude', 'longitude', 'date'])
            print(ds_mean_spatial)
            arm_summer_mean = xr.open_dataset('your/file/path')
            gp_era5 = xr.open_dataset('your/file/path').z.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), level=slice(500, 1000)).mean(dim=['latitude', 'longitude', 'time']).values * 9.81 ** (-1)
            Re = 6371000
            gp_era5_true = Re * gp_era5 / (Re - gp_era5)
            print('ERA5 level heights', gp_era5)
            print(ds_mean_spatial['v'])
            wind_dir_era5 = (180 + np.degrees(np.arctan2(ds_mean_spatial['u'].values, ds_mean_spatial['v']).values)) % 360
            plt.plot(wind_dir_era5, gp_era5_true[::-1], color='purple', label='ERA5')
            wind_dir_arm = (180 + np.degrees(np.arctan2(arm_summer_mean.u.values, arm_summer_mean.v.values))) % 360
            plt.plot(wind_dir_arm, arm_summer_mean.height.values, linestyle='--', color='black', label='ARM obs')
            print('arm lowest', arm_summer_mean.height.values[0])
            plt.legend(loc='upper left', fontsize=8)
            plt.title('')
            plt.xlabel('Wind direction [$^{\\circ}$]', fontsize=14)
            plt.ylabel('Height from surface [m]', fontsize=14)
            plt.tight_layout()
            plt.xlim([150, 250])
            plt.ylim([0, 1500])
            plt.show()
            fig.savefig('your/file/path' + self.diag_type + save_fig + '.png', bbox_inches='tight')
        elif self.diag_type in ['k_m']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            print(self.diag_type)
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), phalf=slice(750, 1000))
                zfull_slice = self.zhalfs[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), phalf=slice(750, 1000))
                import xarray as xr
                zsurf = xr.open_dataset('your/file/path')
                zsurf_val = zsurf.zsurf.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon)).mean().values
                print('True surface height is:', zsurf_val)
                print('Zhalf surface height is:', zsurf_val)
                y_axis = 'zfull'
                print(config_slice.mean(dim=['lat', 'lon']).values[0, :])
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values[0, :], zfull_slice.mean(dim=['lat', 'lon']).values[0, :] - zsurf_val, color=colors[i], label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=1)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            plt.legend(loc='upper left', fontsize=8)
            plt.title('')
            plt.xlabel('$K_m$ [m$^{2}$ s$^{-1}$]', fontsize=14)
            plt.ylabel('Height from surface [m]', fontsize=14)
            plt.tight_layout()
            plt.xlim([0, 62])
            plt.ylim([0, 1500])
            plt.show()
            fig.savefig('your/file/path' + self.diag_type + save_fig + '.png', bbox_inches='tight')
        else:
            raise ValueError('Diag type does not exist')

    def plot_diagnostics_level(self, save_fig):
        """
            Plot diagnostics 
            """
        self.min_lat = self.coords[0]
        self.max_lat = self.coords[1]
        self.min_lon = self.coords[2]
        self.max_lon = self.coords[3]
        colors = ['blue', 'orange', 'green', 'red', 'grey', 'magenta']
        labels = ['AM4_CLUBB_DM ', 'AM4_CLUBB_PM ']
        labels = ['AM4_lock ', 'AM4_CLUBB_DM ', 'AM4_CLUBB_DM_tau ', 'AM4_CLUBB_DM_mom5 ', 'AM4_CLUBB_PM ', 'AM4_CLUBB_PM_colin']
        labels = ['AM4 ', 'AM4-CLUBB_DM ', 'AM4-CLUBB_DM ', 'AM4-CLUBB_PM_no_sconv ', 'ERA5']
        if self.diag_type in ['dudt', 'dvdt']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), level=slice(500, 1000)) * 10 ** 5
                y_axis = 'level'
                plot_config = config_slice.mean(dim=['lat', 'lon']).plot(y=y_axis, color=colors[i], yincrease=False, label=labels[i])
            plt.legend(loc='upper right', fontsize=8)
            plt.title('')
            plt.ylabel('Reference pressure levels [hPa]')
            plt.xlabel('$\\frac{\\partial{u}}{\\partial{t}} [\\times{10^{-5}}ms^{-2}$]')
            plt.tight_layout()
            plt.show()
            fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
        elif self.diag_type in ['upwp', 'vpwp', 'k_m']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), level=slice(1000, 500))[0, :, :, :]
                y_axis = 'level'
                plot_config = config_slice.mean(dim=['lat', 'lon']).plot(y=y_axis, color=colors[i], yincrease=False, label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            if self.diag_type == 'upwp':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel("$\\overline{u'w'} [m^2s^{-2}]$")
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            elif self.diag_type == 'vpwp':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel("$\\overline{v'w'} [m^2s^{-2}]$")
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            elif self.diag_type == 'k_m':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel('$K_m$ [m$^2$s$^{-1}$]')
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            else:
                raise ValueError('Diag type does not exist')
        elif self.diag_type in ['u_comp', 'v_comp']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), level=slice(1000, 500))[0, :, :, :]
                y_axis = 'level'
                plot_config = config_slice.mean(dim=['lat', 'lon']).plot(y=y_axis, color=colors[i], yincrease=False, label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)
                tickss = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500]
                plt.yticks(ticks=tickss)
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            if self.diag_type == 'u_comp':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel('$\\overline{u} [ms^{-1}]$')
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            elif self.diag_type == 'v_comp':
                import xarray as xr
                ds = xr.open_dataset('your/file/path')
                ds_box = ds.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), pressure_level=slice(1000, 500))
                ds_mean_spatial = ds_box.mean(dim=['latitude', 'longitude', 'date'])
                print(ds_mean_spatial)
                ds_mean_spatial['v'].plot(y='pressure_level', color=colors[4], yincrease=False, label=labels[4])
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel('$\\overline{v} [ms^{-1}]$')
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
        else:
            raise ValueError('Diag type does not exist')

class plot_momentum_diagnostics_diurnal:

    def __init__(self, diagnostics, zfulls, zhalfs, bl_heights, diag_type, coords, day):
        """
        diagnostic: list of xarrays 
           diagnostic to plot
        coords: list of integers
            lat/lon box to zoom in for plotting 
        """
        self.diagnostics = diagnostics
        self.zfulls = zfulls
        self.zhalfs = zhalfs
        self.bl_heights = bl_heights
        self.diag_type = diag_type
        self.coords = coords
        self.day = day

    def plot_diagnostics(self, save_fig):
        """
        Plot diagnostics 
        """
        self.min_lat = self.coords[0]
        self.max_lat = self.coords[1]
        self.min_lon = self.coords[2]
        self.max_lon = self.coords[3]
        colors = ['blue', 'orange', 'green', 'magenta', 'darkblue', 'gray']
        labels = ['AM4 ', 'AM4-CLUBB_DM ', 'AM4-CLUBB_DM_X ', 'AM4-CLUBB_PM ', 'AM4-CLUBB_PM_X ', 'ERA5']
        if self.diag_type in ['dudt', 'dvdt']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(500, 1000)) * 10 ** 5
                y_axis = 'pfull'
                plot_config = config_slice.mean(dim=['lat', 'lon']).plot(y=y_axis, color=colors[i], yincrease=False, label=labels[i])
            plt.legend(loc='upper right', fontsize=8)
            plt.title('')
            plt.ylabel('Reference pressure levels [hPa]')
            plt.xlabel('$\\frac{\\partial{u}}{\\partial{t}} [\\times{10^{-5}}ms^{-2}$]')
            plt.tight_layout()
            plt.show()
            fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
        elif self.diag_type in ['upwp', 'vpwp']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), phalf=slice(750, 1000))
                zfull_slice = self.zfulls[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                y_axis = 'zfull'
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values[0, :], zfull_slice.mean(dim=['lat', 'lon']).values[0, :] - zfull_slice.mean(dim=['lat', 'lon']).values[0, -1], color=colors[i], label=labels[i])
                plt.xlim([-0.2, 0.05])
                plt.ylim([0, 1500])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            if self.diag_type == 'upwp':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel("$\\overline{u'w'} [m^2s^{-2}]$")
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            elif self.diag_type == 'vpwp':
                plt.legend(loc='upper left', fontsize=8)
                plt.title('')
                plt.xlabel("$\\overline{v'w'} [m^2s^{-2}]$")
                plt.ylabel('Height from surface [m]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            elif self.diag_type == 'k_m':
                plt.legend(loc='upper right', fontsize=8)
                plt.title('')
                plt.xlabel('$K_m$ [m$^2$s$^{-1}$]')
                plt.ylabel('Reference pressure levels [hPa]')
                plt.tight_layout()
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + '.png')
            else:
                raise ValueError('Diag type does not exist')
        elif self.diag_type in ['u_comp', 'v_comp']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            print(self.diag_type)
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                zfull_slice = self.zfulls[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                bl_height_slice = self.bl_heights[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon))
                import xarray as xr
                zsurf = xr.open_dataset('your/file/path')
                zsurf_val = zsurf.zsurf.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon)).mean().values
                print('True surface height is:', zsurf_val)
                y_axis = 'zfull'
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values, zfull_slice.mean(dim=['lat', 'lon']).values - zsurf_val, color=colors[i], label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=1)
                bl_values = bl_height_slice.mean(dim=['lat', 'lon', 'time']).values
                print('bl_values are', bl_values)
                plt.axhline(bl_values, color=colors[i], linestyle='--', linewidth=1)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            if self.diag_type == 'v_comp':
                import xarray as xr
                ds = xr.open_dataset('your/file/path')
                ds_box = ds.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), pressure_level=slice(1000, 500))
                ds_mean_spatial = ds_box.mean(dim=['latitude', 'longitude', 'date'])
                print(ds_mean_spatial)
                if self.day == 'day':
                    arm_summer_mean = xr.open_dataset('your/file/path')
                else:
                    arm_summer_mean = xr.open_dataset('your/file/path')
                plt.plot(arm_summer_mean.v.values, arm_summer_mean.height.values, linestyle='--', color='black', label='ARM obs')
                print('arm lowest', arm_summer_mean.height.values[0])
                plt.legend(loc='upper left', fontsize=8)
                plt.title('')
                plt.xlabel('$\\overline{v }$ [ms$^{-1}$]', fontsize=14)
                plt.ylabel('Height from surface [m]', fontsize=14)
                plt.tight_layout()
                if self.day == 'day':
                    plt.xlim([0, 8])
                else:
                    plt.xlim([0, 14])
                plt.ylim([0, 1800])
                plt.show()
                fig.savefig('your/file/path' + self.diag_type + save_fig + self.day + '.png', bbox_inches='tight')
            elif self.diag_type == 'u_comp':
                import xarray as xr
                print('we are in u_comp')
                ds = xr.open_dataset('your/file/path')
                ds_box = ds.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), pressure_level=slice(1000, 500))
                ds_mean_spatial = ds_box.mean(dim=['latitude', 'longitude', 'date'])
                print(ds_mean_spatial)
                if self.day == 'day':
                    arm_summer_mean = xr.open_dataset('your/file/path')
                else:
                    arm_summer_mean = xr.open_dataset('your/file/path')
                print('The summer array is:')
                print(arm_summer_mean)
                plt.plot(arm_summer_mean.u.values, arm_summer_mean.height.values, linestyle='--', color='black', label='ARM obs')
                print('arm lowest', arm_summer_mean.height.values[0])
                plt.legend(loc='upper left', fontsize=8)
                plt.title('')
                plt.xlabel('$\\overline{u }$ [m s$^{-1}$]', fontsize=14)
                plt.ylabel('Height from surface [m]', fontsize=14)
                plt.tight_layout()
                plt.xlim([-5, 5])
                plt.ylim([0, 1900])
                plt.show()
                fig.savefig('your/file/path' + '_' + self.diag_type + save_fig + self.day + '.png', bbox_inches='tight')
        elif self.diag_type in ['dir']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            print(self.diag_type)
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                zfull_slice = self.zfulls[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), pfull=slice(750, 1000))
                import xarray as xr
                zsurf = xr.open_dataset('your/file/path')
                zsurf_val = zsurf.zsurf.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon)).mean().values
                print('True surface height is:', zsurf_val)
                y_axis = 'zfull'
                print(config_slice.mean(dim=['lat', 'lon']).values)
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values, zfull_slice.mean(dim=['lat', 'lon']).values - zsurf_val, color=colors[i], label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=1)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            import xarray as xr
            ds = xr.open_dataset('your/file/path')
            ds_box = ds.sel(latitude=slice(self.max_lat, self.min_lat), longitude=slice(self.min_lon, self.max_lon), pressure_level=slice(1000, 500))
            ds_mean_spatial = ds_box.mean(dim=['latitude', 'longitude', 'date'])
            print(ds_mean_spatial)
            arm_summer_mean = xr.open_dataset('your/file/path')
            wind_dir_arm = (180 + np.degrees(np.arctan2(arm_summer_mean.u.values, arm_summer_mean.v.values))) % 360
            plt.plot(wind_dir_arm, arm_summer_mean.height.values, linestyle='--', color='black', label='ARM obs')
            print('arm lowest', arm_summer_mean.height.values[0])
            plt.legend(loc='upper left', fontsize=8)
            plt.title('')
            plt.xlabel('Wind direction [$^{\\circ}$]', fontsize=14)
            plt.ylabel('Height from surface [m]', fontsize=14)
            plt.tight_layout()
            plt.xlim([150, 250])
            plt.ylim([0, 1900])
            plt.show()
            fig.savefig('your/file/path' + self.diag_type + save_fig + self.day + '.png', bbox_inches='tight')
        elif self.diag_type in ['k_m']:
            fig = plt.figure(dpi=130, figsize=(4, 6))
            print(self.diag_type)
            for i, config in enumerate(self.diagnostics):
                config_slice = config.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), phalf=slice(750, 1000))
                zfull_slice = self.zhalfs[i].sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon), phalf=slice(750, 1000))
                import xarray as xr
                zsurf = xr.open_dataset('your/file/path')
                zsurf_val = zsurf.zsurf.sel(lat=slice(self.min_lat, self.max_lat), lon=slice(self.min_lon, self.max_lon)).mean().values
                print('True surface height is:', zsurf_val)
                print('Zhalf surface height is:', zsurf_val)
                y_axis = 'zfull'
                print(config_slice.mean(dim=['lat', 'lon']).values)
                plot_config = plt.plot(config_slice.mean(dim=['lat', 'lon']).values, zfull_slice.mean(dim=['lat', 'lon']).values - zsurf_val, color=colors[i], label=labels[i])
                plt.axvline(x=0, color='gray', linestyle='--', linewidth=1)
                tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
                for tick in tickss:
                    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
            plt.legend(loc='upper left', fontsize=8)
            plt.title('')
            plt.xlabel('$K_m$ [m$^{2}$ s$^{-1}$]', fontsize=14)
            plt.ylabel('Height from surface [m]', fontsize=14)
            plt.tight_layout()
            if self.day == 'day':
                plt.xlim([0, 100])
            else:
                plt.xlim([0, 32])
            plt.ylim([0, 1900])
            plt.show()
            fig.savefig('your/file/path' + self.diag_type + save_fig + self.day + '.png', bbox_inches='tight')
        else:
            raise ValueError('Diag type does not exist')

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
