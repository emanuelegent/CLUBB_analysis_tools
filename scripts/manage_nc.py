"""Script `manage_nc`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import load_nc as ln
import numpy as np
import xarray as xr
import pandas as pd
import seasonal as seasonal
import get_bl
import get_angle

logger = logging.getLogger(__name__)

class load_am4:

    def __init__(self, simulation_path, ftype, sim_type, yr, season):
        self.simulation_path = simulation_path
        if sim_type in ['lock', 'sim_new']:
            self.simulation_path = self.simulation_path + 'atmos_level.0001.'
        elif sim_type == 'dm':
            self.simulation_path = self.simulation_path + 'atmos_level.0001.'
        elif sim_type == 'dmnew':
            self.simulation_path = self.simulation_path + 'atmos_level.0001.'
        elif sim_type == 'pm':
            self.simulation_path = self.simulation_path + 'atmos_level.0001.'
        elif sim_type == 'tau':
            self.simulation_path = self.simulation_path + 'atmos_level.0001.'
        elif sim_type == 'ug':
            self.simulation_path = self.simulation_path + 'atmos_level.0001.'
        elif sim_type == 'pm_nosconv':
            self.simulation_path = self.simulation_path + 'atmos.0001' + '.'
        else:
            pass
        if season == True:
            self.months = ['06', '07', '08']
        else:
            self.months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.ftype = ftype
        self.fields = []
        for month in self.months:
            path = self.simulation_path + month + '.nc'
            clim_monthly = xr.open_dataset(path)
            if self.ftype == 'wind_ref':
                u = clim_monthly['u_ref']
                v = clim_monthly['v_ref']
                wind = (u ** 2 + v ** 2) ** (1.0 / 2.0)
                field = wind
            elif self.ftype == 'stress':
                tau_x = clim_monthly['tau_x']
                tau_y = clim_monthly['tau_y']
                tau = (tau_x ** 2 + tau_y ** 2) ** (1.0 / 2.0)
                field = tau
            elif self.ftype == 'c_d':
                tau_x = clim_monthly['tau_x']
                tau_y = clim_monthly['tau_y']
                tau = (tau_x ** 2 + tau_y ** 2) ** (1.0 / 2.0)
                u = clim_monthly['u_ref']
                v = clim_monthly['v_ref']
                wind = (u ** 2 + v ** 2) ** (1.0 / 2.0)
                c_d = tau / (1.3 * wind ** 2)
                field = c_d
            else:
                field = clim_monthly[ftype]
            self.fields.append(field)
        self.field_data = [ff.data for ff in self.fields]

    def mean(self):
        self.means = np.mean(self.field_data, axis=0)
        self.object = self.fields[0].copy()
        self.object.data = self.means

class load_am4_hybrid:

    def __init__(self, simulation_path, ftype, sim_type, yr, season):
        self.simulation_path = simulation_path
        if sim_type in ['lock', 'sim_new']:
            self.simulation_path = self.simulation_path + 'atmos_level.0002-0031.'
        elif sim_type == 'dm':
            self.simulation_path = self.simulation_path + 'atmos_level.0002-0031.'
        elif sim_type == 'dmnew':
            self.simulation_path = self.simulation_path + 'atmos_level.0002-0011.'
        elif sim_type == 'pm':
            self.simulation_path = self.simulation_path + 'atmos_level.0002-0031.'
        elif sim_type == 'pm_nosconv':
            self.simulation_path = self.simulation_path + 'atmos_level.0002' + '-00' + str(yr) + '.'
        else:
            pass
        if season == True:
            self.months = ['06', '07', '08']
        else:
            self.months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        self.ftype = ftype
        self.fields = []
        for month in self.months:
            path = self.simulation_path + month + '.nc'
            clim_monthly = xr.open_dataset(path)
            if self.ftype == 'wind_ref':
                u = clim_monthly['u_ref']
                v = clim_monthly['v_ref']
                wind = (u ** 2 + v ** 2) ** (1.0 / 2.0)
                field = wind
            elif self.ftype == 'stress':
                tau_x = clim_monthly['tau_x']
                tau_y = clim_monthly['tau_y']
                tau = (tau_x ** 2 + tau_y ** 2) ** (1.0 / 2.0)
                field = tau
            elif self.ftype == 'c_d':
                tau_x = clim_monthly['tau_x']
                tau_y = clim_monthly['tau_y']
                tau = (tau_x ** 2 + tau_y ** 2) ** (1.0 / 2.0)
                u = clim_monthly['u_ref']
                v = clim_monthly['v_ref']
                wind = (u ** 2 + v ** 2) ** (1.0 / 2.0)
                c_d = tau / (1.3 * wind ** 2)
                field = c_d
            else:
                field = clim_monthly[ftype]
            self.fields.append(field)
        self.field_data = [ff.data for ff in self.fields]

    def mean(self):
        print(len(self.field_data))
        self.means = np.mean(self.field_data, axis=0)
        self.object = self.fields[0].copy()
        self.object.data = self.means

class manage_am4:

    def __init__(self, simulation_path, sim_type, yr, clubb_flux, k_m_comp, season, ug=None):
        self.simulation_path = simulation_path
        self.sim_type = sim_type
        self.ug = ug
        print('start')
        ftype = 'u_ref'
        self.u_ref = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.u_ref.mean()
        ftype = 'wind_ref'
        self.wind = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.wind.mean()
        ftype = 'cape_uwc'
        self.cape = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.cape.mean()
        ftype = 'ucomp'
        self.ucomp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.ucomp.mean()
        ftype = 'vcomp'
        self.vcomp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        print(self.vcomp)
        self.vcomp.mean()
        ftype = 'zsurf'
        self.zsurf = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.zsurf.mean()
        ftype = 'z_pbl'
        self.zpbl = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.zpbl.mean()
        ftype = 'z_full'
        self.zfull = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.zfull.mean()
        ftype = 'z_half'
        self.zhalf = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.zhalf.mean()
        ftype = 'low_cld_amt'
        self.low_cld_amt = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.low_cld_amt.mean()
        ftype = 'mid_cld_amt'
        self.mid_cld_amt = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.mid_cld_amt.mean()
        ftype = 'high_cld_amt'
        self.high_cld_amt = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.high_cld_amt.mean()
        ftype = 'tot_cld_amt'
        self.tot_cld_amt = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.tot_cld_amt.mean()
        ftype = 'stress'
        self.stress = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.stress.mean()
        print('Halfway')
        ftype = 'z_Ri_025'
        self.bl_height = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.bl_height.mean()
        ftype = 'drag_mom'
        self.c_d = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.c_d.mean()
        ftype = 'tau_x'
        self.stress_x = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.stress_x.mean()
        ftype = 'tau_y'
        self.stress_y = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.stress_y.mean()
        ftype = 'temp'
        self.temp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.temp.mean()
        if clubb_flux:
            ftype = 'xw_upwp_sfc'
            print(self.simulation_path)
            self.clubb_stress_x = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            print(self.clubb_stress_x.ftype)
            self.clubb_stress_x.mean()
            ftype = 'xw_vpwp_sfc'
            self.clubb_stress_y = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.clubb_stress_y.mean()
            self.clubb_stress = (self.clubb_stress_x.object ** 2 + self.clubb_stress_y.object ** 2) ** 0.5
        if k_m_comp:
            ftype = 'khzm_3d'
            self.diff_m_clubb = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.diff_m_clubb.mean()
        ftype = 'slp_dyn'
        self.slp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.slp.mean()
        ftype = 'diff_t'
        self.diff_t = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.diff_t.mean()
        ftype = 'diff_m'
        self.diff_m = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.diff_m.mean()
        ftype = 'udt_vdif'
        self.udt_vdif = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.udt_vdif.mean()
        ftype = 'udt_dyn'
        self.udt_dyn = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.udt_dyn.mean()
        ftype = 'udt_topo'
        self.udt_topo = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.udt_topo.mean()
        ftype = 'vdt_vdif'
        self.vdt_vdif = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.vdt_vdif.mean()
        ftype = 'vdt_dyn'
        self.vdt_dyn = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.vdt_dyn.mean()
        ftype = 'vdt_topo'
        self.vdt_topo = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.vdt_topo.mean()
        ftype = 'qdt_vdif'
        self.qdt_vdif = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.qdt_vdif.mean()
        ftype = 'udt_CLUBB'
        self.udt_vdif_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.udt_vdif_CLUBB.mean()
        ftype = 'vdt_CLUBB'
        self.vdt_vdif_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.vdt_vdif_CLUBB.mean()
        ftype = 'qdt_CLUBB'
        self.qdt_vdif_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.qdt_vdif_CLUBB.mean()
        ftype = 'qldt_CLUBB'
        self.qldt_vdif_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.qldt_vdif_CLUBB.mean()
        ftype = 'qidt_CLUBB'
        self.qidt_vdif_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.qidt_vdif_CLUBB.mean()
        ftype = 'upwp_CLUBB'
        self.upwp_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.upwp_CLUBB.mean()
        ftype = 'vpwp_CLUBB'
        self.vpwp_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.vpwp_CLUBB.mean()
        ftype = 'vpwp_CLUBB'
        self.vpwp_CLUBB = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
        self.vpwp_CLUBB.mean()
        if self.ug == 'ug':
            self.ug_upwp_count = load_am4(self.simulation_path, 'ug_upwp_count', self.sim_type, yr, season)
            self.ug_upwp_count.mean()
            self.ug_vpwp_count = load_am4(self.simulation_path, 'ug_vpwp_count', self.sim_type, yr, season)
            self.ug_vpwp_count.mean()
        if self.sim_type != 'lock':
            ftype = 'upwp_bt'
            self.upwp_bt = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_bt.mean()
            ftype = 'upwp_ma'
            self.upwp_ma = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_ma.mean()
            ftype = 'upwp_ta'
            self.upwp_ta = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_ta.mean()
            ftype = 'upwp_tp'
            self.upwp_tp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_tp.mean()
            ftype = 'upwp_ac'
            self.upwp_ac = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_ac.mean()
            ftype = 'upwp_bp'
            self.upwp_bp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_bp.mean()
            ftype = 'upwp_pr1'
            self.upwp_pr1 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_pr1.mean()
            ftype = 'upwp_pr2'
            self.upwp_pr2 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_pr2.mean()
            ftype = 'upwp_pr3'
            self.upwp_pr3 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_pr3.mean()
            ftype = 'upwp_pr4'
            self.upwp_pr4 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.upwp_pr4.mean()
            ftype = 'up2_tp'
            self.up2_tp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.up2_tp.mean()
            ftype = 'vpwp_bt'
            self.vpwp_bt = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_bt.mean()
            ftype = 'vpwp_ma'
            self.vpwp_ma = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_ma.mean()
            ftype = 'vpwp_ta'
            self.vpwp_ta = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_ta.mean()
            ftype = 'vpwp_tp'
            self.vpwp_tp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_tp.mean()
            ftype = 'vpwp_ac'
            self.vpwp_ac = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_ac.mean()
            ftype = 'vpwp_bp'
            self.vpwp_bp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_bp.mean()
            ftype = 'vpwp_pr1'
            self.vpwp_pr1 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_pr1.mean()
            ftype = 'vpwp_pr2'
            self.vpwp_pr2 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_pr2.mean()
            ftype = 'vpwp_pr3'
            self.vpwp_pr3 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_pr3.mean()
            ftype = 'vpwp_pr4'
            self.vpwp_pr4 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vpwp_pr4.mean()
            ftype = 'vp2_tp'
            self.vp2_tp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.vp2_tp.mean()
            ftype = 'wprtp_bt'
            self.wrtp_bt = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_bt.mean()
            ftype = 'wprtp_ma'
            self.wrtp_ma = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_ma.mean()
            ftype = 'wprtp_ta'
            self.wrtp_ta = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_ta.mean()
            ftype = 'wprtp_tp'
            self.wrtp_tp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_tp.mean()
            ftype = 'wprtp_ac'
            self.wrtp_ac = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_ac.mean()
            ftype = 'wprtp_bp'
            self.wrtp_bp = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_bp.mean()
            ftype = 'wprtp_pr1'
            self.wrtp_pr1 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_pr1.mean()
            ftype = 'wprtp_pr2'
            self.wrtp_pr2 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_pr2.mean()
            ftype = 'wprtp_pr3'
            self.wrtp_pr3 = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)
            self.wrtp_pr3.mean()
        '\n        ftype = "bk"\n        self.bk = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)\n        self.bk.mean()\n        #print(self.bk.object.shape)\n        \n        ftype = "ps"\n        self.ps = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)\n        self.ps.mean()\n        \n        ftype = "pk"\n        self.pk = load_am4(self.simulation_path, ftype, self.sim_type, yr, season)\n        self.pk.mean()\n        \n        self.pressure = self.upwp_CLUBB.object.copy()\n        #tmp = self.bk.object.data[:, np.newaxis, np.newaxis]*self.ps.object.data\n        #print(tmp.shape)\n        #print(self.pk.object.data.shape)\n        self.pressure = self.pressure.mean(dim="time")\n        self.pressure.data = self.bk.object.data[:, np.newaxis, np.newaxis]*self.ps.object.data + self.pk.object.data[:, np.newaxis, np.newaxis]\n        #print(self.pressure.data)\n        tmp_press = (self.pressure.data[1:, :,:]+self.pressure.data[:-1, :,:])/2\n        print(tmp_press.shape)\n        print(tmp_press.max())\n        print(self.pressure.data.max())\n        print(self.temp.object.data.max())\n        self.pot_temp = self.temp.object.copy()\n        self.pot_temp = self.pot_temp.mean(dim = "time")\n        self.temp = self.temp.object.mean(dim = "time")\n        self.pot_temp.data = self.temp.data*((100000./tmp_press)**0.286)\n        '

class load_era5:

    def __init__(self, ftype):
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
        self.path = 'your/file/path'
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
            self.filename = 'u_10.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.u10 = self.xr_object['u10']
            self.filename = 'v_10.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.v10 = self.xr_object['v10']
            self.object = self.u10.copy()
            self.object.data = (self.u10.data ** 2 + self.v10.data ** 2) ** (1.0 / 2.0)
        elif self.ftype == 'wind_ref_new':
            path = 'your/file/path'
            self.filename = 'ERA5_monthly_averaged_10m_u_component_of_wind_'
            xa_list = []
            for year in range(1980, 2014):
                year = str(year)
                xa_list.append(xr.open_dataset(path + self.filename + year + '.nc')['u10'])
            merged = xr.merge(xa_list)
            print(merged)
            self.object_u = merged
            path = 'your/file/path'
            self.filename = 'ERA5_monthly_averaged_10m_v_component_of_wind_'
            xa_list = []
            for year in range(1980, 2014):
                year = str(year)
                xa_list.append(xr.open_dataset(path + self.filename + year + '.nc')['v10'])
            merged = xr.merge(xa_list)
            print(merged)
            self.object_v = merged
            self.object = self.object_u.u10.copy()
            self.object.data = (self.object_u.u10.data ** 2 + self.object_v.v10.data ** 2) ** 0.5
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
        elif self.ftype == 'stress':
            self.filename = 'ustar.nc'
            self.xr_object = xr.open_dataset(self.path + self.filename)
            self.object = self.xr_object['zust']
            self.object.data = 1.2 * self.object.data ** 2
        elif self.ftype == 'tau_x':
            path = 'your/file/path'
            self.filename = 'your/file/path'
            xa_list = []
            for year in range(2010, 2020):
                year = str(year)
                xa_list.append(xr.open_dataset(path + self.filename + year + '.nc')['iews'])
            merged = xr.merge(xa_list)
            print(merged)
            self.object = merged
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
            self.object = self.ucomp[:, -4, :, :] ** 2 + self.vcomp[:, -4, :, :] ** 2
        else:
            raise ValueError('the ftype requested is not available')

    def mean(self):
        self.load_var()
        self.mean = self.object.mean(dim='time')

class manage_era5:

    def __init__(self, ftype):
        self.ftype = ftype
        self.wind = load_era5(self.ftype)
        self.wind.mean()

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
