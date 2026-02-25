"""Script `ug_flux_diagnostics`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np

logger = logging.getLogger(__name__)

def plot_ug(flux_grad_xr, season, ftype):
    """
    flux_grad: product of upwp and duddz or vpwp and dvdz.
            Positive where upwp is upgradient w.r.t to dudz, and by symmetry for zonal wind
    """
    if season == 'ann':
        flux_grad = flux_grad_xr.values
    elif season == 'jja':
        flux_grad = flux_grad_xr.sel(time=flux_grad_xr['time'].dt.month.isin([6, 7, 8])).values
    positive_sign_count_time_only = np.sum(flux_grad > 0, axis=0)
    distribution = np.sum(positive_sign_count_time_only, axis=(1, 2)) / 8760
    fig = plt.figure(figsize=(15, 8))
    plt.plot(flux_grad_xr.phalf.values, distribution)
    plt.xlabel('Hybrid pressure level [hPa]', fontsize=16)
    plt.xticks(np.round(flux_grad_xr.phalf.values).astype(int)[::4], fontsize=16)
    plt.axvline(x=832, color='red')
    plt.yticks(np.arange(0, 12000, 1000), fontsize=16)
    plt.ylabel('Number of upgradient fluxes, year avg ' + ftype, fontsize=16)
    positive_sign_count_np = np.sum(flux_grad > 0, axis=1)
    positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)
    if season == 'ann':
        positive_sign_map = positive_sign_count_np_time / 8760
    elif season == 'jja':
        positive_sign_map = positive_sign_count_np_time * 3 / 8760
    else:
        pass
    fig = plt.figure(figsize=(12, 6))
    lons = flux_grad_xr.lon.values
    lats = flux_grad_xr.lat.values
    plt.figure(figsize=(12, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    levelss = np.arange(0, 10.0, 1.0)
    mesh = ax.contourf(lons, lats, positive_sign_map, levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    ax.coastlines()
    cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
    cbar.set_label('AM4-CLUBB_PM - Upgradient Flux Count over all levels - ' + season + ' average ' + ftype)
    plt.title('Positive Sign Count')
    plt.show()

def plot_ug_summer(flux_grad, ftype):
    """
    flux_grad: product of upwp and duddz or vpwp and dvdz.
            Positive where upwp is upgradient w.r.t to dudz, and by symmetry for meridional wind
    """
    flux_grad = flux_grad.sel(time=dvdz_vpwp['time'].dt.month.isin([6, 7, 8]))
    flux_grad = flux_grad.values
    positive_sign_count_time_only = np.sum(flux_grad > 0, axis=0)
    distribution = np.sum(positive_sign_count_time_only, axis=(1, 2)) / 8760
    fig = plt.figure(figsize=(15, 8))
    plt.plot(dvdz_reduced.phalf.values, distribution)
    plt.xlabel('Hybrid pressure level [hPa]', fontsize=16)
    plt.xticks(np.round(dvdz_vpwp.dvdz_vpwp.phalf.values).astype(int)[::4], fontsize=16)
    plt.axvline(x=832, color='red')
    plt.yticks(np.arange(0, 12000, 1000), fontsize=16)
    plt.ylabel('Number of upgradient fluxes, year avg ' + ftype, fontsize=16)
    positive_sign_count_np = np.sum(np_dvdz > 0, axis=1)
    positive_sign_count_np_time = np.sum(positive_sign_count_np, axis=0)
    positive_sign_map = positive_sign_count_np_time
    fig = plt.figure(figsize=(12, 6))
    lons = dvdz_vpwp.lon.values
    lats = dvdz_vpwp.lat.values
    plt.figure(figsize=(12, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    levels = np.arange(0, 10.0, 1.0)
    mesh = ax.contourf(lons, lats, positive_sign_map * 3 / 8760.0, levels=levelss, cmap='viridis', shading='auto', transform=ccrs.PlateCarree())
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    ax.coastlines()
    cbar = plt.colorbar(mesh, orientation='vertical', pad=0.02, aspect=40)
    cbar.set_label('AM4-CLUBB_PM - Upgradient Flux Count over all levels - summer average ' + ftype)
    plt.title('Positive Sign Count')
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
