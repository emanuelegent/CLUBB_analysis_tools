#!/usr/bin/env python
# coding: utf-8

#load AM4 simulations
import manage_nc as mn

filename_am4_lock = "your/file/path"
filename_am4_clubb_dm = "your/file/path"
filename_am4_clubb_dm_tau = "your/file/path"

filename_am4_clubb_pm = "your/file/path"
filename_am4_clubb_pm_tau = "your/file/path"

#filename_am4_clubb_pm_nsconv = "your/file/path"

am4_lock = mn.manage_am4(filename_am4_lock, "lock", 3, True, False, True)
am4_clubb_dm = mn.manage_am4(filename_am4_clubb_dm, "dm", 3, True, False, True)
am4_clubb_dm_tau = mn.manage_am4(filename_am4_clubb_dm_tau, "tau", 3, True, False, True)
am4_clubb_pm = mn.manage_am4(filename_am4_clubb_pm, "pm", 3, True, False, True)
am4_clubb_pm_tau = mn.manage_am4(filename_am4_clubb_pm_tau, "tau", 3, True, False, True)

filename_am4_clubb_pm = "your/file/path"
am4_clubb_pm = mn.manage_am4(filename_am4_clubb_pm, "pm", 3, True, False, True, "ug")
am4_clubb_pm_tau = mn.manage_am4(filename_am4_clubb_pm_tau, "tau", 3, True, False, True, "ug")

#plot profiles vertical diffusion 
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cmocean
min_lat = 30
max_lat = 40
min_lon = 260
max_lon = 265
fig = plt.figure(dpi=130, figsize=(4,6))

clubb_dm_diff = am4_lock.vdt_vdif.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', color="blue", yincrease=False, label="AM4 diff")

clubb_dm_dyn = am4_lock.vdt_dyn.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', color="blue", linestyle="--", yincrease=False, label="AM4 dyn")

clubb_dm_topo = am4_lock.vdt_topo.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="blue", linestyle="-.", label="AM4 topo")

clubb_dm_diff = am4_clubb_dm.vdt_vdif_CLUBB.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="orange", linestyle="-", label="AM4-CLUBB_DM diff")

clubb_dm_dyn = am4_clubb_dm.vdt_dyn.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False,  color="orange", linestyle="--",  label="AM4-CLUBB_DM dyn")

clubb_dm_topo = am4_clubb_dm.vdt_topo.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="orange", linestyle="-.",  label="AM4-CLUBB_DM topo")

udt_vdif = am4_clubb_pm.vdt_vdif_CLUBB.object.copy()
udt_vdif.data = (am4_clubb_pm.vdt_vdif_CLUBB.object.data)# + am4_clubb_pm_2.udt_vdif_CLUBB.object.data + am4_clubb_pm_3.udt_vdif_CLUBB.object.data)/3

udt_dyn = am4_clubb_pm.vdt_dyn.object.copy()
udt_dyn.data = (am4_clubb_pm.vdt_dyn.object.data)# + am4_clubb_pm_2.udt_dyn.object.data + am4_clubb_pm_3.udt_dyn.object.data)/3

udt_topo = am4_clubb_pm.vdt_topo.object.copy()
udt_topo.data = (am4_clubb_pm.vdt_topo.object.data)# + am4_clubb_pm_2.udt_topo.object.data + am4_clubb_pm_3.udt_topo.object.data)/3

clubb_dm_diff = udt_vdif.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="-",   label="AM4-CLUBB_PM diff")

clubb_dm_dyn = udt_dyn.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="--", label="AM4-CLUBB_PM dyn")

clubb_dm_topo = udt_topo.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="-.", label="AM4-CLUBB_PM topo")

plt.legend(loc="upper right", fontsize=8)
#plt.yticks(np.arange(1000,0,100))
plt.title("")
plt.ylabel(r"Reference pressure levels [hPa]")
plt.tight_layout()
plt.xlabel(r"Meridional wind tendency $\frac{\partial{v}}{\partial{t}}$ [$\times{10^{-5}}$ ms$^{-2}$]")
fig.savefig('your/file/path')

import momentum_diagnostics as md 

lock_dm_mom = md.momentum_diagnostics(am4_lock.udt_vdif.object, am4_lock.vdt_vdif.object, 
                        am4_lock.zfull.object, am4_lock.zhalf.object, am4_lock.ucomp.object, 
                        am4_lock.vcomp.object)
lock_dm_mom.manage_diagnostics()

clubb_dm_mom = md.momentum_diagnostics(am4_clubb_dm.udt_vdif_CLUBB.object, am4_clubb_dm.vdt_vdif_CLUBB.object, 
                        am4_clubb_dm.zfull.object, am4_clubb_dm.zhalf.object, am4_clubb_dm.ucomp.object, 
                        am4_clubb_dm.vcomp.object)
clubb_dm_mom.manage_diagnostics()

clubb_dm_mom_tau = md.momentum_diagnostics(am4_clubb_dm_tau.udt_vdif_CLUBB.object, am4_clubb_dm_tau.vdt_vdif_CLUBB.object, 
                        am4_clubb_dm_tau.zfull.object, am4_clubb_dm_tau.zhalf.object, am4_clubb_dm_tau.ucomp.object, 
                        am4_clubb_dm_tau.vcomp.object)
clubb_dm_mom_tau.manage_diagnostics()

clubb_pm_mom = md.momentum_diagnostics(am4_clubb_pm.udt_vdif_CLUBB.object, am4_clubb_pm.vdt_vdif_CLUBB.object, 
                        am4_clubb_pm.zfull.object, am4_clubb_pm.zhalf.object, am4_clubb_pm.ucomp.object, 
                        am4_clubb_pm.vcomp.object)
clubb_pm_mom.manage_diagnostics()

clubb_tau_mom = md.momentum_diagnostics(am4_clubb_pm_tau.udt_vdif_CLUBB.object, am4_clubb_pm_tau.vdt_vdif_CLUBB.object, 
                        am4_clubb_pm_tau.zfull.object, am4_clubb_pm_tau.zhalf.object, am4_clubb_pm_tau.ucomp.object, 
                        am4_clubb_pm_tau.vcomp.object)
clubb_tau_mom.manage_diagnostics()

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,40,260,265]
coords_gp = [36,37,262,264]
#coords_gp = [36,37,261,262]
#coords_gp = [30,40,260,265]

coords = coords_gp

save_fig = "vcomp"
p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.v_comp, clubb_dm_mom.v_comp,  clubb_dm_mom_tau.v_comp, clubb_pm_mom.v_comp, clubb_tau_mom.v_comp],
                                          [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull],
                                          [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf],
                                          [am4_lock.zpbl.object, am4_clubb_dm.zpbl.object, am4_clubb_dm_tau.zpbl.object, am4_clubb_pm.zpbl.object, am4_clubb_pm_tau.zpbl.object], "v_comp", coords)
p_mom_diag.plot_diagnostics(save_fig)

save_fig = "ucomp"

p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.u_comp, clubb_dm_mom.u_comp,  clubb_dm_mom_tau.u_comp, clubb_pm_mom.u_comp, clubb_tau_mom.u_comp],
                                          [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull],
                                          [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf],
                                          [am4_lock.zpbl.object, am4_clubb_dm.zpbl.object, am4_clubb_dm_tau.zpbl.object, am4_clubb_pm.zpbl.object, am4_clubb_pm_tau.zpbl.object], "u_comp", coords)
p_mom_diag.plot_diagnostics(save_fig)

save_fig = "ucomp"

p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.dir, clubb_dm_mom.dir,  clubb_dm_mom_tau.dir, clubb_pm_mom.dir, clubb_tau_mom.dir],
                                          [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull],
                                          [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf],
                                          [am4_lock.zpbl.object, am4_clubb_dm.zpbl.object, am4_clubb_dm_tau.zpbl.object, am4_clubb_pm.zpbl.object, am4_clubb_pm_tau.zpbl.object], "dir", coords)
p_mom_diag.plot_diagnostics(save_fig)

save_fig = "ucomp"

p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.k_m, clubb_dm_mom.k_m,  clubb_dm_mom_tau.k_m, clubb_pm_mom.k_m, clubb_tau_mom.k_m],
                                          [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_dm_mom_tau.zfull, clubb_pm_mom.zfull, clubb_tau_mom.zfull],
                                          [lock_dm_mom.zhalf, clubb_dm_mom.zhalf, clubb_dm_mom_tau.zhalf, clubb_pm_mom.zhalf, clubb_tau_mom.zhalf],
                                          [am4_lock.zpbl.object, am4_clubb_dm.zpbl.object, am4_clubb_dm_tau.zpbl.object, am4_clubb_pm.zpbl.object, am4_clubb_pm_tau.zpbl.object], "k_m", coords)
p_mom_diag.plot_diagnostics(save_fig)

import xarray as xr
check = xr.open_dataset(data)

coords_gp = [36,37,262,264]
check.zsurf.sel

import xarray as xr
arm_2013 = 'your/file/path'
arm_2014 = 'your/file/path'
arm_2015 = 'your/file/path'
arm_2016 = 'your/file/path'
arm_2017 = 'your/file/path'
arm_2018 = 'your/file/path'
arm_2019 = 'your/file/path'
arm_2020 = 'your/file/path'
arm_2022 = 'your/file/path'
arm_2023 = 'your/file/path'
arm_2024 = 'your/file/path'
arm_2025 = 'your/file/path'

arm_13 = xr.open_dataset(arm_2013)
arm_14 = xr.open_dataset(arm_2014)
arm_15 = xr.open_dataset(arm_2015)
arm_16 = xr.open_dataset(arm_2016)
arm_17 = xr.open_dataset(arm_2017)
arm_18 = xr.open_dataset(arm_2018)
arm_19 = xr.open_dataset(arm_2019)
arm_20 = xr.open_dataset(arm_2020)
arm_22 = xr.open_dataset(arm_2022)
arm_23 = xr.open_dataset(arm_2023)
arm_24 = xr.open_dataset(arm_2024)
arm_25 = xr.open_dataset(arm_2025)

arm_list = [arm_13, arm_14, arm_15, arm_16, arm_17, arm_18, arm_19, arm_20, arm_22, arm_23, arm_24]
# Concatenate along time
arm_stacked = xr.concat(arm_list, dim="time")

# Select only summer months (JJA: June, July, August)
arm_summer = arm_stacked.sel(time=arm_stacked["time"].dt.month.isin([6, 7, 8]))

# Compute the mean along time for summer months only
arm_summer_mean = arm_summer.mean(dim="time")
arm_summer_mean.to_netcdf('your/file/path')

import momentum_diagnostics as md 

save_fig = "vpwp"
coords_gp = [36,37,262,264]
p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.vpwp, clubb_dm_mom.vpwp, clubb_pm_mom.vpwp],
                                          [lock_dm_mom.zfull, clubb_dm_mom.zfull, clubb_pm_mom.zfull],
                                          [am4_lock.zpbl.object, am4_clubb_dm.zpbl.object, am4_clubb_pm.zpbl.object], 
                                          "vpwp", coords)
p_mom_diag.plot_diagnostics(save_fig)

budgets_vpwp_pm = [am4_clubb_pm.vpwp_bt.object,
           am4_clubb_pm.vpwp_ma.object, 
           am4_clubb_pm.vpwp_ta.object, 
           am4_clubb_pm.vpwp_tp.object, 
           am4_clubb_pm.vpwp_ac.object, 
           am4_clubb_pm.vpwp_bp.object, 
           am4_clubb_pm.vpwp_pr1.object, 
           am4_clubb_pm.vpwp_pr2.object, 
           am4_clubb_pm.vpwp_pr3.object, 
           am4_clubb_pm.vpwp_pr4.object]#, am4_stats.upwp_dp1.object]

budgets_vpwp_pmtau = [am4_clubb_pm_tau.vpwp_bt.object,
           am4_clubb_pm_tau.vpwp_ma.object, 
           am4_clubb_pm_tau.vpwp_ta.object, 
           am4_clubb_pm_tau.vpwp_tp.object, 
           am4_clubb_pm_tau.vpwp_ac.object, 
           am4_clubb_pm_tau.vpwp_bp.object, 
           am4_clubb_pm_tau.vpwp_pr1.object, 
           am4_clubb_pm_tau.vpwp_pr2.object, 
           am4_clubb_pm_tau.vpwp_pr3.object, 
           am4_clubb_pm_tau.vpwp_pr4.object]#, am4_stats.upwp_dp1.object]

import upwp_vert_profile as upvp

upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pm, am4_clubb_pm.zhalf.object, "AM4-CLUBB_PM")

import upwp_vert_profile as upvp

upvp.plot_vpwp_vertical_profile_all(budgets_vpwp_pmtau, am4_clubb_pm.zhalf.object, "AM4-CLUBB_PM_X")

budgets_upwp_pm = [am4_clubb_pm.upwp_bt.object,
           am4_clubb_pm.upwp_ma.object, 
           am4_clubb_pm.upwp_ta.object, 
           am4_clubb_pm.upwp_tp.object, 
           am4_clubb_pm.upwp_ac.object, 
           am4_clubb_pm.upwp_bp.object, 
           am4_clubb_pm.upwp_pr1.object, 
           am4_clubb_pm.upwp_pr2.object, 
           am4_clubb_pm.upwp_pr3.object, 
           am4_clubb_pm.upwp_pr4.object]#, am4_stats.upwp_dp1.object]
budgets_upwp_pm_tau = [am4_clubb_pm_tau.upwp_bt.object,
           am4_clubb_pm_tau.upwp_ma.object, 
           am4_clubb_pm_tau.upwp_ta.object, 
           am4_clubb_pm_tau.upwp_tp.object, 
           am4_clubb_pm_tau.upwp_ac.object, 
           am4_clubb_pm_tau.upwp_bp.object, 
           am4_clubb_pm_tau.upwp_pr1.object, 
           am4_clubb_pm_tau.upwp_pr2.object, 
           am4_clubb_pm_tau.upwp_pr3.object, 
           am4_clubb_pm_tau.upwp_pr4.object]#, am4_stats.upwp_dp1.object]

import upwp_vert_profile as upvp

upvp.plot_upwp_vertical_profile_all(budgets_upwp_pm_tau, am4_clubb_pm_tau.zhalf.object, "AM4-CLUBB_PM_X")

import upwp_vert_profile as upvp

upvp.plot_upwp_vertical_profile_all(budgets_upwp_pm, am4_clubb_pm.zhalf.object, "AM4-CLUBB_PM")

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

lonmin = 262
lonmax= 264
latmin = 36
latmax=37
zsurf = xr.open_dataset("your/file/path")
zsurf_val = zsurf.zsurf.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).mean().values

# Extract the field
field = am4_clubb_pm.ug_vpwp_count.object[0,:,:,:]  # Adjust if needed
# Select the region: Longitude (260°W to 265°W) and Latitude (30°N to 40°N)
subset = field.sel(lon=slice(261, 262), lat=slice(30, 31))
profile = subset.mean(dim=["lon", "lat"])
# Extract vertical coordinate (assuming pressure or height)
vertical_coord = profile["phalf"]  # Replace with the actual vertical coordinate name
# Plot the vertical profile
zhalf_slice = am4_clubb_pm.zhalf.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice = am4_clubb_pm.vpwp_CLUBB.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice_mean = vpwp_slice.mean(dim=["lat","lon"]).values
#print(np.max(abs(vpwp_slice_mean)))
max_vpwp = np.max(abs(vpwp_slice_mean))

# Extract the field
field2 = am4_clubb_pm_tau.ug_vpwp_count.object[0,:,:,:]  # Adjust if needed
# Select the region: Longitude (260°W to 265°W) and Latitude (30°N to 40°N)
subset2 = field2.sel(lon=slice(261, 262), lat=slice(30, 31))
profile2 = subset2.mean(dim=["lon", "lat"])
# Extract vertical coordinate (assuming pressure or height)
vertical_coord2 = profile2["phalf"]  # Replace with the actual vertical coordinate name
# Plot the vertical profile
zhalf_slice2 = am4_clubb_pm_tau.zhalf.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice2 = am4_clubb_pm_tau.vpwp_CLUBB.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice_mean2 = vpwp_slice2.mean(dim=["lat","lon"]).values
#print(np.max(abs(vpwp_slice_mean)))
max_vpwp2 = np.max(abs(vpwp_slice_mean2))

#print('vpwp')
#print((vpwp_slice_mean/max_vpwp)[0])
fig, ax = plt.subplots(figsize=(6, 8))
#ax.plot((profile*abs(vpwp_slice_mean/max_vpwp)[0])*90, zhalf_slice.mean(dim=["lat","lon"]).values[0,:]-zhalf_slice.mean(dim=["lat","lon"]).values[0,-1],
#        marker="o", linestyle="-", color="magenta")
#ax.plot((profile2*abs(vpwp_slice_mean2/max_vpwp2)[0])*90, zhalf_slice2.mean(dim=["lat","lon"]).values[0,:]-zhalf_slice.mean(dim=["lat","lon"]).values[0,-1],
#        marker="o", linestyle="-", color="darkblue")

ax.plot((profile)*90*24, zhalf_slice.mean(dim=["lat","lon"]).values[0,:]-zsurf_val,
        marker="o", linestyle="-", color="magenta", label="AM4-CLUBB_PM")
ax.plot((profile2)*90*24, zhalf_slice2.mean(dim=["lat","lon"]).values[0,:]-zsurf_val,
        marker="o", linestyle="-", color="darkblue", label="AM4-CLUBB_PM_X")
#print(vpwp_slice_mean)

#print(zhalf_slice.mean(dim=["lat","lon"]).values[0,:])
# Reverse y-axis if lev is pressure (typical in atmospheric data)
#if vertical_coord.attrs.get("units", "").lower() in ["hpa", "pa"]:
ax.invert_yaxis()

# Labels and title
ax.set_xlabel(r"Upgradient $\overline{v'w'}$ flux count [month$^{-1}$]", fontsize=14)
ax.set_ylabel("Height from surface [m]", fontsize=14)
plt.legend(loc="upper left", fontsize=14)
tickss = [0,200, 400, 600, 800, 1000, 1200, 1400]#, 2500, 3000, 3500, 4000, 4500]
for tick in tickss: 
    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_ylim(0,1500)
plt.yticks(ticks=tickss, fontsize=12)
plt.xticks(ticks=[0,20,40,60,80,100,120,140, 160], fontsize=12)
#ax.set_title("Vertical Profile of AM4 CLUBB Prognostic Momentum\n(Averaged over 260°W-265°W, 30°N-40°N)")
plt.savefig('your/file/path', bbox_inches='tight')
plt.show()

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

lonmin = 262
lonmax= 264
latmin = 36
latmax=37
zsurf = xr.open_dataset("your/file/path")
zsurf_val = zsurf.zsurf.sel(lat=slice(latmin, latmax), lon=slice(lonmin, lonmax)).mean().values

# Extract the field
field = am4_clubb_pm.ug_vpwp_count.object[0,:,:,:]  # Adjust if needed
# Select the region: Longitude (260°W to 265°W) and Latitude (30°N to 40°N)
subset = field.sel(lon=slice(261, 262), lat=slice(30, 31))
profile = subset.mean(dim=["lon", "lat"])
# Extract vertical coordinate (assuming pressure or height)
vertical_coord = profile["phalf"]  # Replace with the actual vertical coordinate name
# Plot the vertical profile
zhalf_slice = am4_clubb_pm.zhalf.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice = am4_clubb_pm.upwp_CLUBB.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice_mean = vpwp_slice.mean(dim=["lat","lon"]).values
#print(np.max(abs(vpwp_slice_mean)))
max_vpwp = np.max(abs(vpwp_slice_mean))

# Extract the field
field2 = am4_clubb_pm_tau.ug_upwp_count.object[0,:,:,:]  # Adjust if needed
# Select the region: Longitude (260°W to 265°W) and Latitude (30°N to 40°N)
subset2 = field2.sel(lon=slice(261, 262), lat=slice(30, 31))
profile2 = subset2.mean(dim=["lon", "lat"])
# Extract vertical coordinate (assuming pressure or height)
vertical_coord2 = profile2["phalf"]  # Replace with the actual vertical coordinate name
# Plot the vertical profile
zhalf_slice2 = am4_clubb_pm_tau.zhalf.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice2 = am4_clubb_pm_tau.vpwp_CLUBB.object.sel(lat= slice(latmin, latmax), 
                                lon=slice(lonmin, lonmax))
vpwp_slice_mean2 = vpwp_slice2.mean(dim=["lat","lon"]).values
#print(np.max(abs(vpwp_slice_mean)))
max_vpwp2 = np.max(abs(vpwp_slice_mean2))

#print('vpwp')
#print((vpwp_slice_mean/max_vpwp)[0])
fig, ax = plt.subplots(figsize=(6, 8))
#ax.plot((profile*abs(vpwp_slice_mean/max_vpwp)[0])*90, zhalf_slice.mean(dim=["lat","lon"]).values[0,:]-zhalf_slice.mean(dim=["lat","lon"]).values[0,-1],
        #marker="o", linestyle="-", color="magenta")
#ax.plot((profile2*abs(vpwp_slice_mean2/max_vpwp2)[0])*90, zhalf_slice2.mean(dim=["lat","lon"]).values[0,:]-zhalf_slice.mean(dim=["lat","lon"]).values[0,-1],
        #marker="o", linestyle="-", color="darkblue")

ax.plot((profile)*90*24, zhalf_slice.mean(dim=["lat","lon"]).values[0,:]-zsurf_val,
        marker="o", linestyle="-", color="magenta", label="AM4-CLUBB_PM")
ax.plot((profile2)*90*24, zhalf_slice2.mean(dim=["lat","lon"]).values[0,:]-zsurf_val,
        marker="o", linestyle="-", color="darkblue", label="AM4-CLUBB_PM_X")
#print(vpwp_slice_mean)
plt.legend(loc="upper left", fontsize=14)
#print(zhalf_slice.mean(dim=["lat","lon"]).values[0,:])
# Reverse y-axis if lev is pressure (typical in atmospheric data)
#if vertical_coord.attrs.get("units", "").lower() in ["hpa", "pa"]:
ax.invert_yaxis()

# Labels and title
ax.set_xlabel(r"Upgradient $\overline{u'w'}$ flux count [month$^{-1}$]", fontsize=14)
ax.set_ylabel("Height from surface [m]", fontsize=14)

tickss = [0,200, 400, 600, 800, 1000, 1200, 1400]#, 2500, 3000, 3500, 4000, 4500]
for tick in tickss: 
    plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_ylim(0,1500)
plt.yticks(ticks=tickss, fontsize=12)
plt.xticks(ticks=[0,20,40,60,80,100,120,140, 160], fontsize=12)
#ax.set_title("Vertical Profile of AM4 CLUBB Prognostic Momentum\n(Averaged over 260°W-265°W, 30°N-40°N)")
plt.savefig('your/file/path', bbox_inches='tight')
plt.show()

filename_am4_clubb_pm_ug = "your/file/path"
am4_clubb_pm_ug_new = mn.manage_am4(filename_am4_clubb_pm_ug, "ug", 3, True, False, True)

# In[ ]:


import xarray as xr 
import pandas as pd
import numpy as np
uvcomp = xr.open_dataset("your/file/path")
ds = uvcomp.v
ds = ds.assign_coords(date=pd.to_datetime(ds['date'].values, format='%Y%m%d'))

# Step 2: Select only summer months (June, July, August)
jja = ds.sel(date=ds['date'].dt.month.isin([6, 7, 8]))

# Compute the mean along the time dimension for these months
jja_mean = jja.mean(dim="date")
jja_mean.to_netcdf("your/file/path")

target_grid = ctrl_v_summer  # Replace with your target grid path

# Extract the target latitude and longitude coordinates
new_lats = target_grid['lat']
new_lons = target_grid['lon']
new_level = target_grid['level']

# Perform interpolation using xarray's interp
jja_mean_regridded = jja_mean.interp(latitude=new_lats, longitude=new_lons, pressure_level= new_level, method='linear')
masked_data = jja_mean_regridded.where(~np.isnan(ctrl_v_summer), np.nan)
masked_data.to_netcdf("your/file/path")

import xarray as xr
masked_data = xr.open_dataset("your/file/path")

import plot_summer_wind as psw

psw.plot_meridional_structure(masked_data.v, "ERA5", True)

#get summer field 
import read_summer_wind as rsw

path_dm = cfg.get("paths", {}).get("dm", "your/file/path")
dm_u10m_summer, dm_v10m_summer, dm_u925_summer, dm_v925_summer, dm_u_summer, dm_v_summer = rsw.read_wind(path_dm)

#get summer field 
import read_summer_wind as rsw

path_pm_only = cfg.get("paths", {}).get("pm_only", "your/file/path")
pm_u10m_summer, pm_v10m_summer, pm_u925_summer, pm_v925_summer, pm_u_summer, pm_v_summer = rsw.read_wind(path_pm_only)

psw.plot_meridional_structure(dm_u_summer, "AM4-CLUBB_DM")

import plot_summer_wind as psw

psw.plot_meridional_structure(pm_v_summer, "AM4-CLUBB_PM")

#get summer field 
import read_summer_wind as rsw

path_pm_nsconv = cfg.get("paths", {}).get("pm_nsconv", "your/file/path")
pm_nsconv_u10m_summer, pm_nsconv_v10m_summer, pm_nsconv_u925_summer, pm_nsconv_v925_summer, pm_nsconv_u_summer, pm_nsconv_v_summer = rsw.read_wind_nsconv(path_pm_nsconv)

psw.plot_meridional_structure(pm_nsconv_v_summer, "AM4-CLUBB_PM_nosconv")

import plot_summer_wind as psw

psw.plot_meridional_structure(masked_data.v, "ERA5", True)

psw.plot_meridional_structure(am4_lock.vcomp.object, "AM4")

psw.plot_meridional_structure(am4_clubb_pm_nosconv.vcomp.object, "AM4-CLUBB_PM_nosconv")

#load AM4 simulations
import manage_nc as mn

filename_am4_lock = "your/file/path"
filename_am4_clubb_dm = "your/file/path"
filename_am4_clubb_pm = "your/file/path"
filename_am4_clubb_pm_nsconv = "your/file/path"

filename_am4_lock = "your/file/path"
filename_am4_clubb_dm = "your/file/path"
filename_am4_clubb_pm = "your/file/path"
filename_am4_clubb_pm_nsconv = "your/file/path"

am4_lock = mn.manage_am4(filename_am4_lock, "lock", None, True, False, True)
am4_clubb_dm = mn.manage_am4(filename_am4_clubb_dm, "dm", None, True, False, True)
am4_clubb_pm = mn.manage_am4(filename_am4_clubb_pm, "pm", None, True, False, True)
am4_clubb_pm_nosconv = mn.manage_am4(filename_am4_clubb_pm_nsconv, "pm_nosconv", 6, True, False, True)

import manage_nc as mn

am4_clubb_pm_nosconv = mn.manage_am4(filename_am4_clubb_pm_nsconv, "pm_nosconv", 6, True, False, True)

filename_am4_clubb_pm_nsconv_C8 = "your/file/path"
am4_clubb_pm_nosconv_C8 = mn.manage_am4(filename_am4_clubb_pm_nsconv_C8, "pm_nosconv", 6, True, False, True)

#plot profiles vertical diffusion 
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cmocean
min_lat = 30
max_lat = 40
min_lon = 260
max_lon = 265
fig = plt.figure(dpi=130, figsize=(4,6))

clubb_dm_diff = am4_lock.udt_vdif.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', color="blue", yincrease=False, label="AM4 diff")

clubb_dm_dyn = am4_lock.udt_dyn.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', color="blue", linestyle="--", yincrease=False, label="AM4 dyn")

clubb_dm_topo = am4_lock.udt_topo.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="blue", linestyle="-.", label="AM4 topo")

clubb_dm_diff = am4_clubb_dm.udt_vdif_CLUBB.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="orange", linestyle="-", label="AM4-CLUBB_1 diff")

clubb_dm_dyn = am4_clubb_dm.udt_dyn.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False,  color="orange", linestyle="--",  label="AM4-CLUBB_1 dyn")

clubb_dm_topo = am4_clubb_dm.udt_topo.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="orange", linestyle="-.",  label="AM4-CLUBB_1 topo")

udt_vdif = am4_clubb_pm.udt_vdif_CLUBB.object.copy()
udt_vdif.data = (am4_clubb_pm.udt_vdif_CLUBB.object.data)# + am4_clubb_pm_2.udt_vdif_CLUBB.object.data + am4_clubb_pm_3.udt_vdif_CLUBB.object.data)/3

udt_dyn = am4_clubb_pm.udt_dyn.object.copy()
udt_dyn.data = (am4_clubb_pm.udt_dyn.object.data)# + am4_clubb_pm_2.udt_dyn.object.data + am4_clubb_pm_3.udt_dyn.object.data)/3

udt_topo = am4_clubb_pm.udt_topo.object.copy()
udt_topo.data = (am4_clubb_pm.udt_topo.object.data)# + am4_clubb_pm_2.udt_topo.object.data + am4_clubb_pm_3.udt_topo.object.data)/3

clubb_dm_diff = udt_vdif.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="-",   label="AM4-CLUBB_PM diff")

clubb_dm_dyn = udt_dyn.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="--", label="AM4-CLUBB_PM dyn")

clubb_dm_topo = udt_topo.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="-.", label="AM4-CLUBB_PM topo")

udt_vdif = am4_clubb_pm_nosconv.udt_vdif_CLUBB.object.copy()
udt_vdif.data = (am4_clubb_pm_nosconv.udt_vdif_CLUBB.object.data)# + am4_clubb_pm_2.udt_vdif_CLUBB.object.data + am4_clubb_pm_3.udt_vdif_CLUBB.object.data)/3

udt_dyn = am4_clubb_pm_nosconv.udt_dyn.object.copy()
udt_dyn.data = (am4_clubb_pm_nosconv.udt_dyn.object.data)# + am4_clubb_pm_2.udt_dyn.object.data + am4_clubb_pm_3.udt_dyn.object.data)/3

udt_topo = am4_clubb_pm_nosconv.udt_topo.object.copy()
udt_topo.data = (am4_clubb_pm_nosconv.udt_topo.object.data)# + am4_clubb_pm_2.udt_topo.object.data + am4_clubb_pm_3.udt_topo.object.data)/3

clubb_dm_diff = udt_vdif.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="purple", linestyle="-",   label="AM4-CLUBB_PM_nsconv diff")

clubb_dm_dyn = udt_dyn.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="purple", linestyle="--", label="AM4-CLUBB_PM_nsconv dyn")

clubb_dm_topo = udt_topo.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="purple", linestyle="-.", label="AM4-CLUBB_PM_nsconv topo")


plt.legend(loc="upper right", fontsize=8)
#plt.yticks(np.arange(1000,0,100))
plt.title("")
plt.ylabel(r"Reference pressure levels [hPa]")
plt.tight_layout()
plt.xlabel(r"Zonal wind tendency $\frac{\partial{u}}{\partial{t}}$ [$\times{10^{-5}}$ ms$^{-2}$]")
fig.savefig('your/file/path')

#plot profiles vertical diffusion 
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import cmocean
min_lat = 30
max_lat = 40
min_lon = 260
max_lon = 265
fig = plt.figure(dpi=130, figsize=(4,6))

clubb_dm_diff = am4_lock.vdt_vdif.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', color="blue", yincrease=False, label="AM4 diff")

clubb_dm_dyn = am4_lock.vdt_dyn.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', color="blue", linestyle="--", yincrease=False, label="AM4 dyn")

clubb_dm_topo = am4_lock.vdt_topo.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="blue", linestyle="-.", label="AM4 topo")

clubb_dm_diff = am4_clubb_dm.vdt_vdif_CLUBB.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="orange", linestyle="-", label="AM4-CLUBB_1 diff")

clubb_dm_dyn = am4_clubb_dm.vdt_dyn.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False,  color="orange", linestyle="--",  label="AM4-CLUBB_1 dyn")

clubb_dm_topo = am4_clubb_dm.vdt_topo.object.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="orange", linestyle="-.",  label="AM4-CLUBB_1 topo")

udt_vdif = am4_clubb_pm.vdt_vdif_CLUBB.object.copy()
udt_vdif.data = (am4_clubb_pm.vdt_vdif_CLUBB.object.data)# + am4_clubb_pm_2.udt_vdif_CLUBB.object.data + am4_clubb_pm_3.udt_vdif_CLUBB.object.data)/3

udt_dyn = am4_clubb_pm.vdt_dyn.object.copy()
udt_dyn.data = (am4_clubb_pm.vdt_dyn.object.data)# + am4_clubb_pm_2.udt_dyn.object.data + am4_clubb_pm_3.udt_dyn.object.data)/3

udt_topo = am4_clubb_pm.vdt_topo.object.copy()
udt_topo.data = (am4_clubb_pm.vdt_topo.object.data)# + am4_clubb_pm_2.udt_topo.object.data + am4_clubb_pm_3.udt_topo.object.data)/3

clubb_dm_diff = udt_vdif.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="-",   label="AM4-CLUBB_PM diff")

clubb_dm_dyn = udt_dyn.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="--", label="AM4-CLUBB_PM dyn")

clubb_dm_topo = udt_topo.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="green", linestyle="-.", label="AM4-CLUBB_PM topo")

udt_vdif = am4_clubb_pm_nosconv.vdt_vdif_CLUBB.object.copy()
udt_vdif.data = (am4_clubb_pm_nosconv.vdt_vdif_CLUBB.object.data)# + am4_clubb_pm_2.udt_vdif_CLUBB.object.data + am4_clubb_pm_3.udt_vdif_CLUBB.object.data)/3

udt_dyn = am4_clubb_pm_nosconv.vdt_dyn.object.copy()
udt_dyn.data = (am4_clubb_pm_nosconv.vdt_dyn.object.data)# + am4_clubb_pm_2.udt_dyn.object.data + am4_clubb_pm_3.udt_dyn.object.data)/3

udt_topo = am4_clubb_pm_nosconv.vdt_topo.object.copy()
udt_topo.data = (am4_clubb_pm_nosconv.vdt_topo.object.data)# + am4_clubb_pm_2.udt_topo.object.data + am4_clubb_pm_3.udt_topo.object.data)/3

clubb_dm_diff = udt_vdif.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm = clubb_dm_diff.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="purple", linestyle="-",   label="AM4-CLUBB_PM_nsconv diff")

clubb_dm_dyn = udt_dyn.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_dyn = clubb_dm_dyn.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="purple", linestyle="--", label="AM4-CLUBB_PM_nsconv dyn")

clubb_dm_topo = udt_topo.sel(lat=slice(min_lat, max_lat),lon=slice(min_lon, max_lon), pfull=slice(700, 1000))*10**5
clubb_dm_topo = clubb_dm_topo.mean(dim=["lat","lon"]).plot(y='pfull', yincrease=False, color="purple", linestyle="-.", label="AM4-CLUBB_PM_nsconv topo")


plt.legend(loc="upper right", fontsize=8)
#plt.yticks(np.arange(1000,0,100))
plt.title("")
plt.ylabel(r"Reference pressure levels [hPa]")
plt.tight_layout()
plt.xlabel(r"Meridional wind tendency $\frac{\partial{v}}{\partial{t}}$ [$\times{10^{-5}}$ ms$^{-2}$]")
fig.savefig('your/file/path')

import momentum_diagnostics as md 

coords_so = [-58.5, -58, -180, 180]
coords_so = [-30.5, -30, -180, 180]
coords_so = [30,35, 260, 265]
#coords_na = [55, 55.5, -90, 90]
save_fig = "so"
coords = coords_so

lock_dm_mom = md.momentum_diagnostics(am4_lock.udt_vdif.object, am4_lock.vdt_vdif.object, 
                        am4_lock.zfull.object, am4_lock.zhalf.object, am4_lock.ucomp.object, 
                        am4_lock.vcomp.object)
lock_dm_mom.manage_diagnostics()

clubb_dm_mom = md.momentum_diagnostics(am4_clubb_dm.udt_vdif_CLUBB.object, am4_clubb_dm.vdt_vdif_CLUBB.object, 
                        am4_clubb_dm.zfull.object, am4_clubb_dm.zhalf.object, am4_clubb_dm.ucomp.object, 
                        am4_clubb_dm.vcomp.object)
clubb_dm_mom.manage_diagnostics()

clubb_pm_mom = md.momentum_diagnostics(am4_clubb_pm.udt_vdif_CLUBB.object, am4_clubb_pm.vdt_vdif_CLUBB.object, 
                        am4_clubb_pm.zfull.object, am4_clubb_pm.zhalf.object, am4_clubb_pm.ucomp.object, 
                        am4_clubb_pm.vcomp.object)
clubb_pm_mom.manage_diagnostics()

clubb_pm_nsconv_mom = md.momentum_diagnostics(am4_clubb_pm_nosconv.udt_vdif_CLUBB.object, am4_clubb_pm_nosconv.vdt_vdif_CLUBB.object, 
                        am4_clubb_pm_nosconv.zfull.object, am4_clubb_pm_nosconv.zhalf.object, am4_clubb_pm_nosconv.ucomp.object, 
                        am4_clubb_pm_nosconv.vcomp.object)
clubb_pm_nsconv_mom.manage_diagnostics()
"""
clubb_pm_nsconv_mom_C8 = md.momentum_diagnostics(am4_clubb_pm_nosconv_C8.udt_vdif_CLUBB.object, am4_clubb_pm_nosconv_C8.vdt_vdif_CLUBB.object, 
                        am4_clubb_pm_nosconv_C8.zfull.object, am4_clubb_pm_nosconv_C8.zhalf.object, am4_clubb_pm_nosconv_C8.ucomp.object, 
                        am4_clubb_pm_nosconv_C8.vcomp.object)
clubb_pm_nsconv_mom_C8.manage_diagnostics()
"""

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,40,260,265]
coords = coords_gp

save_fig = "k_m_gp"
p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.k_m, clubb_dm_mom.k_m, clubb_pm_mom.k_m, clubb_pm_nsconv_mom.k_m],"k_m", coords)
p_mom_diag.plot_diagnostics(save_fig)

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,40,260,265]
coords = coords_gp

save_fig = "ucomp_gp"
p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.u_comp, clubb_dm_mom.u_comp, clubb_pm_mom.u_comp, clubb_pm_nsconv_mom.u_comp],"u_comp", coords)
p_mom_diag.plot_diagnostics(save_fig)

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,35,260,265]
coords = coords_gp

save_fig = "k_m_gp"
p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.upwp, clubb_dm_mom.upwp, clubb_pm_mom.upwp, clubb_pm_nsconv_mom.upwp],"upwp", coords)
p_mom_diag.plot_diagnostics(save_fig)

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,40,260,265]
coords = coords_gp

save_fig = "vcomp"
p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.v_comp, clubb_dm_mom.v_comp, clubb_pm_mom.v_comp, clubb_pm_nsconv_mom.v_comp],"v_comp", coords)
p_mom_diag.plot_diagnostics(save_fig)

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,35,260,265]
coords = coords_gp

save_fig = "vpwp"
p_mom_diag = md.plot_momentum_diagnostics([lock_dm_mom.vpwp, clubb_dm_mom.vpwp, clubb_pm_mom.vpwp, clubb_pm_nsconv_mom.vpwp],"vpwp", coords)
p_mom_diag.plot_diagnostics(save_fig)

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,40,262,265]
coords = coords_gp

save_fig = "k_m_gp"
p_mom_diag = md.plot_momentum_diagnostics([am4_lock.vcomp.object, am4_clubb_dm.vcomp.object, am4_clubb_pm.vcomp.object, am4_clubb_pm_nosconv.vcomp.object],"v_comp", coords)
p_mom_diag.plot_diagnostics_level(save_fig)

import momentum_diagnostics as md 

coords_trop = [28, 29, 310, 315]
coords_so = [-60.5, -60, 120, 121]
coords_gp = [30,35,260,265]
coords = coords_gp

save_fig = "k_m_gp"
p_mom_diag = md.plot_momentum_diagnostics([am4_clubb_dm.vpwp_CLUBB.object, am4_clubb_dm.vpwp_CLUBB.object, am4_clubb_pm.vpwp_CLUBB.object],"vpwp", coords)
p_mom_diag.plot_diagnostics_level(save_fig)

print(masked_data.sel(lat=slice(30, 40), lon=slice(260,265), level=slice(1000,500)).v.)

print(lock_dm_mom.v_comp.sel(lat=slice(30, 40), lon=slice(260,265), pfull=slice(500,1000)).data.shape)

uvcomp = xr.open_dataset("your/file/path")


# In[ ]:


import pandas as pd
uvcomp = xr.open_dataset("your/file/path")
ds = uvcomp.v
ds = ds.assign_coords(date=pd.to_datetime(ds['date'].values, format='%Y%m%d'))

# Step 2: Select only summer months (June, July, August)
jja = ds.sel(date=ds['date'].dt.month.isin([6, 7, 8]))

# Compute the mean along the time dimension for these months
jja_mean = jja.mean(dim="date")
jja_mean.to_netcdf("your/file/path")


# In[ ]:

filename_am4_lock = "your/file/path"
filename_am4_clubb_dm = "your/file/path"
filename_am4_clubb_pm = "your/file/path"
filename_am4_c4lubb_pm_nsconv = "your/file/path"

import read_diurnal as rd 

dm_ucomp, dm_vcomp, dm_upwp, dm_vpwp = rd.read_diurnal_cycle(filename_am4_clubb_dm)

pm_ucomp, pm_vcomp, pm_upwp, pm_vpwp = rd.read_diurnal_cycle(filename_am4_clubb_pm)

pm_nsconv_ucomp, pm_nsconv_vcomp, pm_nsconv_upwp, pm_nsconv_vpwp = rd.read_diurnal_cycle(filename_am4_c4lubb_pm_nsconv)

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle_prognostic(dm_vcomp, dm_vpwp, "vcomp", "vpwp_CLUBB","AM4-CLUBB_DM")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle_prognostic(pm_vcomp, pm_vpwp, "vcomp", "vpwp_CLUBB","AM4-CLUBB_PM")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle_prognostic(pm_nsconv_vcomp, pm_nsconv_vpwp, "vcomp", "vpwp_CLUBB","AM4-CLUBB_PM_nosconv")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle_prognostic_inst(pm_vcomp, pm_vpwp, "vcomp", "vpwp_CLUBB","AM4-CLUBB_PM")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle_prognostic_inst(pm_nsconv_vcomp, pm_nsconv_vpwp, "vcomp", "vpwp_CLUBB","AM4-CLUBB_PM_nosconv")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(dm_vcomp, "vcomp", "AM4-CLUBB_DM")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(dm_vpwp, "vpwp_CLUBB", "AM4-CLUBB_DM ")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_vpwp, "vpwp_CLUBB", "AM4-CLUBB_PM ")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_nsconv_vpwp, "vpwp_CLUBB", "AM4-CLUBB_PM_nosconv ")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_vcomp, "vcomp", "AM4-CLUBB_PM ")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_vpwp, "vpwp_CLUBB", "AM4-CLUBB_PM ")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_nsconv_vcomp, "vcomp", "AM4-CLUBB_PM_nosconv ")

import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_nsconv_vpwp, "vpwp_CLUBB", "AM4-CLUBB_PM_nosconv ")


# In[ ]:


#plot single day
#plot maximum of every hour
#plot layer above 
#plot layer below
#plot place where flux changes sign or overlay the contour 
#then check for every day


# In[ ]:


import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_vcomp, "vcomp", "AM4-CLUBB_PM ")


# In[ ]:


import plot_diurnal_cycle as pd 

pd.plot_diurnal_cycle(pm_vcomp, "vcomp", "AM4-CLUBB_PM")

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

ds_summer = summer_vcomp
# Define the bounding box for the Great Plains region
lat_bounds = slice(35, 40)  # Latitude range (degrees North)
lon_bounds = slice(262, 264)  # Longitude range (degrees East, 360° format)

# Subset the data for the Great Plains region
vcomp_gp = ds_summer['vcomp'].sel(lat=lat_bounds, lon=lon_bounds)

# Group by hour of the day and compute the mean over space and pressure levels
diurnal_cycle_gp = vcomp_gp.groupby(vcomp_gp['time.hour']).mean(dim=['lat', 'lon', 'time'])
"""
# Plot the diurnal cycle for the Great Plains
plt.figure(figsize=(10, 6))
diurnal_cycle_gp.plot(marker='o', linestyle='-')
plt.title("Diurnal Cycle of vcomp over the Great Plains")
plt.xlabel("Hour of Day")
plt.ylabel("Mean vcomp (m/s)")  # Adjust units if necessary
plt.grid()
plt.show()
"""

# Extract data for plotting
hour = diurnal_cycle_gp['hour']
pfull = diurnal_cycle_gp['pfull']
vcomp = diurnal_cycle_gp.values  # Extract the data array

utc_offset_central = 5
hour_local = (diurnal_cycle_gp['hour'] - utc_offset_central) % 24
print(hour_local.values)
# Create a contour/heatmap
plt.figure(figsize=(12, 6))
levs_diurnal = np.arange(-7,7,1)
contour = plt.contourf(hour, pfull, vcomp.T[:,:], levels=levs_diurnal, cmap='coolwarm', extend="both")  # Transpose vcomp for correct alignment
plt.colorbar(contour, label="vcomp (m/s)")
plt.title("Diurnal Cycle of vcomp (Great Plains)")
plt.xlabel("Hour of Day")
plt.ylabel("Pressure Levels (hPa)")
print(np.round(hour_local).astype(int)[::3].values)
plt.gca().invert_yaxis()
plt.xticks(ticks=hour.values[::3], labels=[19, 22,  1,  4,  7, 10, 13, 16])#np.round(hour_local).astype(int)[::3].values)
#plt.gca().invert_yaxis()  # Invert y-axis to match atmospheric convention
#lt.grid()
plt.show()

vcomp.shape

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
# Extract time and pressure levels
time = diurnal_cycle_gp['time']
pfull = diurnal_cycle_gp['pfull']

time_in_hours = np.array([(t - diurnal_cycle_gp['time'][0]).total_seconds() / 3600
                          for t in diurnal_cycle_gp['time'].values])
# Create a contour plot
plt.figure(figsize=(12, 6))
contour = plt.contourf(time_in_hours, pfull, diurnal_cycle_gp.T, levels=20, cmap='viridis')
plt.colorbar(contour, label="vcomp (m/s)")
plt.title("Diurnal Cycle of vcomp over the Great Plains")
plt.xlabel("Hour of Day")
plt.ylabel("Pressure Levels (hPa)")
plt.gca().invert_yaxis()  # Invert y-axis to have higher pressure at the bottom
plt.grid()
plt.show()

time

pfull

diurnal_cycle_gp.mean(dim="time")


# In[ ]:


"your/file/path"

path ="your/file/path"


# In[ ]:

file = "your/file/path"
import xarray as xr
a = xr.open_dataset(path+file)

a.dudz_clubb.values.shape

a.dudz_clubb.values[0,:,1,1]

import numpy as np 
dudz = np.gradient(a.ucomp.values[0,:,1,1], a.z_full[0,:,1,1].values)

import numpy as np 
dudz = np.gradient(a.ucomp.values[0,:,100,100], a.z_full[0,:,100,100].values)

idx=100
import matplotlib.pyplot as plt
plt.plot(-a.dudz_clubb.values[0,:,idx,idx], a.z_full[0,:,idx,idx].values, label="diagnosed dudz")
plt.plot(dudz, a.z_full[0,:,idx,idx].values, label="dudz postproc from monthly output")
plt.ylabel("zfull")
plt.xlabel("dudz")
plt.legend()
#plt.plot(a.ucomp.values[0,:,1,1], a.z_full[0,:,1,1].values)

import numpy as np 
dvdz = np.gradient(a.vcomp.values[0,:,100,100], a.z_full[0,:,100,100].values)

idx=100
import matplotlib.pyplot as plt
plt.plot(-a.dvdz_clubb.values[0,:,idx,idx], a.z_full[0,:,idx,idx].values, label="diagnosed dudz")
plt.plot(dvdz, a.z_full[0,:,idx,idx].values, label="dudz postproc from monthly output")
plt.ylabel("zfull")
plt.xlabel("dudz")
plt.legend()
#plt.plot(a.ucomp.values[0,:,1,1], a.z_full[0,:,1,1].values)

a.dudz_clubb

a.udt_CLUBB

path_dudz = cfg.get("paths", {}).get("dudz", "your/file/path")
path_ucomp = cfg.get("paths", {}).get("ucomp", "your/file/path")
path_zfull = cfg.get("paths", {}).get("zfull", "your/file/path")
import xarray as xr
dudz = xr.open_dataset(path_dudz)
ucomp = xr.open_dataset(path_ucomp)
zfull = xr.open_dataset(path_zfull)

import numpy as np 
dudz_comp = np.gradient(ucomp.ucomp[0,:,100,100].values, zfull.z_full[0,:,100,100].values)
idx=100
import matplotlib.pyplot as plt
plt.plot(-dudz.dudz_clubb[0,:,idx,idx].values, zfull.z_full[0,:,idx,idx].values, label="diagnosed dudz")
plt.plot(dudz_comp, zfull.z_full[0,:,idx,idx].values, label="dudz postproc from hourly output")
plt.ylabel("zfull")
plt.xlabel("dudz")
plt.legend()

path_dvdz = cfg.get("paths", {}).get("dvdz", "your/file/path")
path_vcomp = cfg.get("paths", {}).get("vcomp", "your/file/path")
path_zfull = cfg.get("paths", {}).get("zfull", "your/file/path")
import xarray as xr
dvdz = xr.open_dataset(path_dvdz)
vcomp = xr.open_dataset(path_vcomp)
zfull = xr.open_dataset(path_zfull)

import numpy as np 
dvdz_comp = np.gradient(vcomp.vcomp[0,:,100,100].values, zfull.z_full[0,:,100,100].values)
idx=100
import matplotlib.pyplot as plt
plt.plot(-dvdz.dvdz_clubb[0,:,idx,idx].values, zfull.z_full[0,:,idx,idx].values, label="diagnosed dvdz")
plt.plot(dvdz_comp, zfull.z_full[0,:,idx,idx].values, label="dvdz postproc from hourly output")
plt.ylabel("zfull")
plt.xlabel("dvdz")
plt.legend()

ucomp.ucomp[0,:,100,100].values

import xarray as xr 
a =xr.open_dataset("your/file/path")

import gradient_half_levels as ghl

import numpy as np 
idx=100
iz=-20
dudz_diag = ghl.compute_dx_dz_phalf(a.ucomp[0,:,idx,idx].values, a.z_full[0,:,idx,idx].values, a.z_half[0,:,idx,idx].values)
dudz_clubb = a.dudz_clubb[0,iz:,idx,idx].values
dudz_clubb[:-1] *=-1
plt.plot(dudz_clubb[:-1], a.z_half[0,iz:-1,idx,idx].values, linestyle="--", linewidth=4.0, label="diagnosed dvdz - monthly average")
plt.plot(dudz_diag[iz:-1], a.z_half[0,iz:-1,idx,idx].values,  linewidth=2.0, label="dvdz postproc from monthly output")
#plt.axvline(x=0.0)
#plt.axhline(y=1000)
plt.ylabel("zfull")
plt.xlabel("dvdz")
plt.legend()

import gradient_half_levels as ghl

import numpy as np 
idx=100
iz=-15
dvdz_diag = ghl.compute_dx_dz_phalf(a.vcomp[0,:,idx,idx].values, a.z_full[0,:,idx,idx].values, a.z_half[0,:,idx,idx].values)
plt.plot(a.dvdz_clubb[0,iz:,idx,idx].values, a.z_half[0,iz:,idx,idx].values, linestyle="--",label="diagnosed dvdz")
plt.plot(dvdz_diag[iz:], a.z_half[0,iz:,idx,idx].values, label="dvdz postproc from hourly output")
plt.axvline(x=0.0)
plt.axhline(y=1000)
plt.ylabel("zfull")
plt.xlabel("dvdz")
plt.legend()

plt.plot(a.vcomp[0,iz:,idx,idx].values, a.z_full[0,iz:,idx,idx].values, label="vcomp")

a.z_full[0,-5:,100,100].values

a.vcomp[0,:,idx,idx].pfull.values

dvdz_comp

a.z_full[0,:,idx,idx].values

a.z_half[0,:,idx,idx].values

import xarray as xr
filepath = "your/file/path"
dvdz = "atmos_level.0002010100-0002123123.dvdz_clubb.nc"
vpwp = "atmos_level.0002010100-0002123123.vpwp_CLUBB.nc"
file_dvdz = filepath+dvdz
file_vpwp = filepath+vpwp
dvdz = xr.open_dataset(file_dvdz)
vpwp = xr.open_dataset(file_vpwp)

vpwp = "atmos_level.0002010100-0002123123.vpwp_CLUBB.nc"
file_vpwp = filepath+vpwp
vpwp = xr.open_dataset(file_vpwp)

# Assuming `product_da` is an xarray DataArray with dimensions [time, phalf, lats, lons]
# Remove the last two phalf levels
dvdz_reduced = dvdz.dvdz_clubb.isel(phalf=slice(21, -2))
vpwp_reduced = vpwp.vpwp_CLUBB.isel(phalf=slice(21, -2))
# Count how many phalf levels at each time, lat, lon have a positive sign
#positive_sign_count = (product_reduced > 0).sum(dim='phalf')

np_dvdz = dvdz_reduced.values
np_vpwp = vpwp_reduced.values
np_reduced = np_dvdz*np_vpwp

positive_sign_count_np = np.sum(np_reduced < 0, axis=1)

positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)

positive_sign_count_np.shape

positive_sign_map = positive_sign_count_np_time

import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz.lon.values
lats =dvdz.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
levelss = np.arange(0,6.5, 0.8)
mesh = ax.contourf(lons, lats, positive_sign_map/8760., levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz.lon.values
lats =dvdz.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree())  
mesh = ax.contourf(lons, lats, positive_sign_map/8760., cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import matplotlib.pyplot as plt
positive_sign_map = positive_sign_count_np_time_ns
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz.lon.values
lats =dvdz.lat.values
plt.figure(figsize=(12, 6))
levelss = np.arange(0,6.5,.8)
ax = plt.axes(projection=ccrs.PlateCarree())  
mesh = ax.contourf(lons, lats, positive_sign_map/8760., levels = levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import xarray as xr
filepath = "your/file/path"
dvdz = "atmos_level.0002010100-0002123123.dvdz_clubb.nc"
vpwp = "atmos_level.0002010100-0002123123.vpwp_CLUBB.nc"
file_dvdz = filepath+dvdz
file_vpwp = filepath+vpwp
dvdz = xr.open_dataset(file_dvdz)
vpwp = xr.open_dataset(file_vpwp)

import numpy as np 
positive_sign_count_np_ns = np.sum(np_reduced_ns < 0, axis=1)
positive_sign_count_np_time_ns = np.sum(positive_sign_count_np_ns, axis=0)

# Assuming `product_da` is an xarray DataArray with dimensions [time, phalf, lats, lons]
# Remove the last two phalf levels
dvdz_reduced = dvdz.dvdz_clubb.isel(phalf=slice(None, -2))
vpwp_reduced = vpwp.vpwp_CLUBB.isel(phalf=slice(None, -2))

np_dvdz_ns = dvdz_reduced.values
np_vpwp_ns = vpwp_reduced.values
np_reduced_ns = np_dvdz_ns*np_vpwp_ns

import matplotlib.pyplot as plt
positive_sign_map = positive_sign_count_np_time_ns
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz.lon.values
lats =dvdz.lat.values
plt.figure(figsize=(12, 6))
levelss = np.arange(0,6.5,.8)
ax = plt.axes(projection=ccrs.PlateCarree())  
mesh = ax.contourf(lons, lats, positive_sign_map/8760., levels = levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import numpy as np
product_reduced_np = product
positive_sign_count_np = np.sum(product_reduced_np > 0, axis=1)
print(f"NumPy result shape: {positive_sign_count_np.shape}")  # Shape: (8100, 240, 140)

import xarray as xr
filepath = "your/file/path"
dvdz = "atmos_level.0002010100-0002123123.dvdz_clubb.nc"
vpwp = "atmos_level.0002010100-0002123123.vpwp_CLUBB.nc"
file_dvdz = filepath+dvdz
file_vpwp = filepath+vpwp
dvdz = xr.open_dataset(file_dvdz)
vpwp = xr.open_dataset(file_vpwp)

# Assuming `product_da` is an xarray DataArray with dimensions [time, phalf, lats, lons]
# Remove the last two phalf levels
dvdz_reduced = dvdz.dvdz_clubb.isel(phalf=slice(None, -2))
vpwp_reduced = vpwp.vpwp_CLUBB.isel(phalf=slice(None, -2))
# Count how many phalf levels at each time, lat, lon have a positive sign
#positive_sign_count = (product_reduced > 0).sum(dim='phalf')

# Assuming `product_da` is an xarray DataArray with dimensions [time, phalf, lats, lons]
# Remove the last two phalf levels
dvdz_reduced = dvdz.sel(time=dvdz['time'].dt.month.isin([6, 7, 8])).dvdz_clubb.isel(phalf=slice(None, -2))
vpwp_reduced = vpwp.sel(time=vpwp['time'].dt.month.isin([6, 7, 8])).vpwp_CLUBB.isel(phalf=slice(None, -2))
# Count how many phalf levels at each time, lat, lon have a positive sign
#positive_sign_count = (product_reduced > 0).sum(dim='phalf')

np_dvdz = dvdz_reduced.values
np_vpwp = vpwp_reduced.values
np_reduced = np_dvdz*np_vpwp

import numpy as np
positive_sign_count_np = np.sum(np_reduced < 0, axis=1)
positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)

positive_sign_map = positive_sign_count_np_time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz.lon.values
lats =dvdz.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
levelss = np.arange(0,6.5, 0.8)
mesh = ax.contourf(lons, lats, positive_sign_map/2190., levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import matplotlib.pyplot as plt
positive_sign_map = positive_sign_count_np_time
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz.lon.values
lats =dvdz.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
levelss = np.arange(0,6.5, 0.8)
mesh = ax.contourf(lons, lats, positive_sign_map/8760., levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import xarray as xr
filepath = "your/file/path"
dvdz = "atmos_level.0001010100-0001123123.dvdz_clubb.nc"
vpwp = "atmos_level.0001010100-0001123123.vpwp_CLUBB.nc"
file_dvdz = filepath+dvdz
file_vpwp = filepath+vpwp
dvdz = xr.open_dataset(file_dvdz)
vpwp = xr.open_dataset(file_vpwp)

# Assuming `product_da` is an xarray DataArray with dimensions [time, phalf, lats, lons]
# Remove the last two phalf levels
dvdz_reduced = dvdz.dvdz_clubb.isel(phalf=slice(None, -2))
vpwp_reduced = vpwp.vpwp_CLUBB.isel(phalf=slice(None, -2))
# Count how many phalf levels at each time, lat, lon have a positive sign
#positive_sign_count = (product_reduced > 0).sum(dim='phalf')

np_dvdz = dvdz_reduced.values
np_vpwp = vpwp_reduced.values
np_reduced = np_dvdz*np_vpwp

import numpy as np
positive_sign_count_np = np.sum(np_reduced > 0, axis=1)
positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)

positive_sign_map = positive_sign_count_np_time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz.lon.values
lats =dvdz.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
levelss = np.arange(0,6.5, 0.8)
mesh = ax.contourf(lons, lats, positive_sign_map/8760., levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import xarray as xr
filepath = "your/file/path"
dvdz_vpwp = "atmos_level.0001010100-0001123123.dvdz_vpwp.nc"
file_dvdz_vpwp = filepath+dvdz_vpwp
dvdz_vpwp = xr.open_dataset(file_dvdz_vpwp)

dvdz_reduced = dvdz_vpwp.dvdz_vpwp.isel(phalf=slice(None, -2))
np_dvdz = dvdz_reduced.values

import numpy as np
positive_sign_count_np = np.sum(np_dvdz > 0, axis=1)
positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)

positive_sign_count_np_time 

positive_sign_map = positive_sign_count_np_time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz_vpwp.lon.values
lats =dvdz_vpwp.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
levelss = np.arange(0,6.5, 0.8)
mesh = ax.contourf(lons, lats, positive_sign_map/8760., levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

dvdz_vpwp

import xarray as xr
filepath = "your/file/path"
dudz_upwp = "atmos_level.0001010100-0001123123.dudz_upwp.nc"
file_dudz_upwp = filepath+dudz_upwp
dudz_upwp = xr.open_dataset(file_dudz_upwp)

dudz_reduced = dudz_upwp.dudz_upwp.isel(phalf=slice(None, -2))
np_dudz = dudz_reduced.values

np_dudz[500,0:,150,200]

import numpy as np
positive_sign_count_np = np.sum(np_dudz > 1e-9, axis=1)
positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)

positive_sign_map = positive_sign_count_np_time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dudz_upwp.lon.values
lats =dudz_upwp.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
#levelss = np.arange(0,6.5, 0.8)
mesh = ax.contourf(lons, lats, positive_sign_map/8760., cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

positive_sign_map = positive_sign_count_np_time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dudz_upwp.lon.values
lats =dudz_upwp.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
#levelss = np.arange(0,6.5, 0.8)
mesh = ax.contourf(lons, lats, positive_sign_map/8760., cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('Positive Sign Count - yearly average')
plt.title('Positive Sign Count')
plt.show()

import xarray as xr
filepath = "your/file/path"
dvdz_vpwp = "your/file/path"
file_dvdz_vpwp = filepath+dvdz_vpwp
dvdz_vpwp = xr.open_dataset(file_dvdz_vpwp)

dvdz_reduced = dvdz_vpwp.dvdz_vpwp.sel(time=dvdz_vpwp['time'].dt.month.isin([6, 7, 8]))#.isel(phalf=slice(None, -2))
np_dvdz = dvdz_reduced.values

positive_sign_count_time_only = np.sum(np_dvdz > 0, axis=0)
distribution = np.sum(positive_sign_count_time_only, axis=(1,2))/8760

fig = plt.figure(figsize=(15,8))
plt.plot(dvdz_reduced.phalf.values, distribution)
plt.xlabel("Hybrid pressure level [hPa]", fontsize=16)
plt.xticks(np.round(dvdz_vpwp.dvdz_vpwp.phalf.values).astype(int)[::4], fontsize=16)
plt.axvline(x=832, color="red")
plt.yticks(np.arange(0,12000,1000), fontsize=16)
plt.ylabel("NUmber of upgradient fluxes, year avg", fontsize=16)

import numpy as np
positive_sign_count_np = np.sum(np_dvdz > 0, axis=1)
positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)

import matplotlib.pyplot as plt
positive_sign_count_np_time_only = np.sum(np_dvdz > 0, axis=0)

positive_sign_map = positive_sign_count_np_time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(figsize=(12, 6))
lons = dvdz_vpwp.lon.values
lats =dvdz_vpwp.lat.values
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) 
levelss = np.arange(0,10.0, 1.0)
mesh = ax.contourf(lons, lats, positive_sign_map*3/8760., levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add coastlines for context
ax.coastlines()
# Add a colorbar
cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
cbar.set_label('AM4-CLUBB_PM - Upgradient Flux Count over all levels - yearly average')
plt.title('Positive Sign Count')
plt.show()

import xarray as xr 
file = "your/file/path"
tile = "00010101.atmos_24xdaily.tile3.nc"
ds = xr.open_dataset(file+tile)

dudz_upwp = ds.dudz_upwp[:168,:,:,:].values

import numpy as np
a = np.sum( dudz_upwp > 0, axis=1)

a.shape

b = np.sum(a>0, axis=0)

import matplotlib.pyplot as plt
plt.pcolormesh(b)

path = "your/file/path"

import xarray as xr
ds = xr.open_dataset(path+"your/file/path")

dudz_upwp = ds.dvdz_upwp.values

import numpy as np
a = np.sum( dudz_upwp > 0, axis=1)

b = np.sum(a>0, axis=0)

b.max()

import matplotlib.pyplot as plt
plt.pcolormesh(b)

dvdz_vpwp = ds.dvdz_vpwp.values

import numpy as np
a = np.sum( dvdz_vpwp > 0, axis=1)

b = np.sum(a>0, axis=0)

import matplotlib.pyplot as plt
plt.pcolormesh(b)

path = "your/file/path"
import xarray as xr
ds = xr.open_dataset(path+"your/file/path")

import numpy as np
dudz_upwp = ds.dudz_upwp.values
a = np.sum( dudz_upwp > 0, axis=1)
b = np.sum(a>0, axis=0)
import matplotlib.pyplot as plt
cmesh = plt.pcolormesh(b/168)
plt.colorbar(cmesh)

b.max()

import xarray as xr
filepath = "your/file/path"
dvdz_vpwp = "your/file/path"
file_dvdz_vpwp = filepath+dvdz_vpwp
dvdz_vpwp = xr.open_dataset(file_dvdz_vpwp)

import ug_flux_diagnostics as ufd

ufd.plot_ug(dvdz_vpwp.dvdz_vpwp, "ann", "vpwp")

import xarray as xr
filepath = "your/file/path"
dudz_upwp = "your/file/path"
file_dudz_upwp = filepath+dudz_upwp
dudz_vpwp = xr.open_dataset(file_dudz_upwp)

import ug_flux_diagnostics as ufd

ufd.plot_ug(dudz_vpwp.dudz_upwp, "ann", "upwp")

import ug_flux_diagnostics as ufd

ufd.plot_ug(dudz_vpwp.dudz_upwp, "jja", "upwp")

import xarray as xr
filepath = "your/file/path"
dudz_upwp = "your/file/path"
file_dudz_upwp = filepath+dudz_upwp
dudz_vpwp = xr.open_dataset(file_dudz_upwp)

import ug_flux_diagnostics as ufd

ufd.plot_ug(dudz_vpwp.dudz_upwp, "jja", "upwp")

import ug_flux_diagnostics as ufd

ufd.plot_ug(dudz_vpwp.dudz_upwp, "ann", "upwp")

import manage_nc as mn

filename_am4_stats = "your/file/path"
am4_stats = mn.manage_am4(filename_am4_stats, "pm", 3, True, False, True)

budgets = [am4_stats.upwp_bt.object,
           am4_stats.upwp_ma.object, 
           am4_stats.upwp_ta.object, 
           am4_stats.upwp_tp.object, 
           am4_stats.upwp_ac.object, 
           am4_stats.upwp_bp.object, 
           am4_stats.upwp_pr1.object, 
           am4_stats.upwp_pr2.object, 
           am4_stats.upwp_pr3.object, 
           am4_stats.upwp_pr4.object]#, am4_stats.upwp_dp1.object]

budgets_vpwp = [am4_stats.vpwp_bt.object,
           am4_stats.vpwp_ma.object, 
           am4_stats.vpwp_ta.object, 
           am4_stats.vpwp_tp.object, 
           am4_stats.vpwp_ac.object, 
           am4_stats.vpwp_bp.object, 
           am4_stats.vpwp_pr1.object, 
           am4_stats.vpwp_pr2.object, 
           am4_stats.vpwp_pr3.object, 
           am4_stats.vpwp_pr4.object]#, am4_stats.upwp_dp1.object]

import upwp_vert_profile as upvp

upvp.plot_upwp_vertical_profile_all(budgets)

import upwp_vert_profile as upvp

upvp.plot_vpwp_vertical_profile_all(budgets_vpwp)

budgets_xp2_tp=[am4_stats.up2_tp.object,am4_stats.vp2_tp.object]
import upwp_vert_profile as upvp

upvp.plot_vertical_profile_gp(budgets_xp2_tp)

budgets = [am4_stats.vpwp_ta.object, am4_stats.vpwp_tp.object, am4_stats.vpwp_ac.object, am4_stats.vpwp_bp.object, 
           am4_stats.vpwp_pr1.object, am4_stats.vpwp_pr2.object, am4_stats.vpwp_pr3.object, am4_stats.vpwp_pr4.object]#, am4_stats.upwp_dp1.object]

import upwp_vert_profile as upvp

upvp.plot_vpwp_vertical_profile(budgets)

filename_am4_stats = "your/file/path"
import xarray as xr
a = xr.open_dataset(filename_am4_stats)


# In[ ]:

am4_stats.vpwp_pr2.object.values.mean()

# In[ ]:

import xarray as xr 
sgpd = xr.open_dataset("your/file/path")

sgpd.v.plot()

#load AM4 simulations
import manage_nc as mn

filename_am4_lock = "your/file/path"
filename_am4_clubb_dm = "your/file/path"
filename_am4_clubb_dm_tau = "your/file/path"

filename_am4_clubb_pm = "your/file/path"
filename_am4_clubb_pm_tau = "your/file/path"

#filename_am4_clubb_pm_nsconv = "your/file/path"

am4_lock = mn.manage_am4(filename_am4_lock, "lock", 3, True, False, True)
#am4_clubb_dm = mn.manage_am4(filename_am4_clubb_dm, "dm", 3, True, False, True)
#am4_clubb_dm_tau = mn.manage_am4(filename_am4_clubb_dm_tau, "tau", 3, True, False, True)
#am4_clubb_pm = mn.manage_am4(filename_am4_clubb_pm, "pm", 3, True, False, True)
am4_clubb_pm_tau = mn.manage_am4(filename_am4_clubb_pm_tau, "tau", 3, True, False, True)


# In[ ]:




