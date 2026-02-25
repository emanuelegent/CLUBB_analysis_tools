"""Script `upwp_vert_profile`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging

import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def plot_upwp_vertical_profile(budgets, coords_gp=[30, 35, 235, 240]):
    """
    Plots the vertical profile of a list of upwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of upwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    """
    plt.figure(figsize=(4, 6))
    linestyles = ('-', ':', '-', ':', '-', ':', '-', '--', '--', '--')
    colors = ('red', 'red', 'brown', 'brown', 'blue', 'purple', 'black', 'black', 'black', 'black', 'black')
    for i, budget in enumerate(budgets):
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon', 'time'])
        if i < 5:
            values = budget_mean.values
            phalf = budget.phalf.values
            plt.plot(values, phalf, color=colors[i], linestyle=linestyles[i], label=budget.name)
        elif i == 5:
            values = budget_mean.values + budgets[7].sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3])).mean(dim=['lat', 'lon', 'time']).values + budgets[8].sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3])).mean(dim=['lat', 'lon', 'time']).values + budgets[9].sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3])).mean(dim=['lat', 'lon', 'time']).values
            phalf = budget.phalf.values
            plt.plot(values, phalf, color=colors[i], linestyle=linestyles[i], label='Return to isotropy')
        elif i == 9:
            values = 10 * budget_mean.values
            phalf = budget.phalf.values
            plt.plot(values, phalf, linestyle=linestyles[i], color=colors[i], label=budget.name)
        else:
            continue
    plt.gca().invert_yaxis()
    plt.gca().set_ylim(1000, 300)
    plt.gca().set_xlim(-0.00025, 0.00025)
    plt.xlabel('Upwp Budget [10^$^{-5}$ m^2/s^3]')
    plt.ylabel('Pressure (hPa)')
    plt.title('Vertical Profile of Upwp Budgets [10^$^{-5}$]')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def plot_upwp_vertical_profile_all(budgets, zfull, coords_gp=[26, 15, 300, 315]):
    """
    Plots the vertical profile of a list of upwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of upwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    """
    plt.figure(figsize=(4, 6))
    linestyles = ('-', ':', '-', ':', '-', ':', '-', '--', ':', '-')
    linestyles = ('-', '-', '-', '-', '-', '-', '-', '-', '-', '-')
    colors = ('red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'red', 'blue', 'green')
    for i, budget in enumerate(budgets):
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon', 'time'])
        zfull_sel = zfull.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        zfull_sel_mean = zfull_sel.mean(dim=['lat', 'lon', 'time'])
        values = zell_full_mean.values
        plt.plot(10 ** 4 * values, values, color=colors[i], linestyle=linestyles[i], label=budget.name)
    plt.gca().invert_yaxis()
    plt.gca().set_ylim(0, 2000)
    plt.gca().set_xlim(-7, 7)
    plt.xlabel('BOMEX Upwp Budget [10^$^{-4}$ m^2/s^3]')
    plt.ylabel('Pressure (hPa)')
    plt.legend(loc='upper left')
    plt.savefig('your/file/path')
    plt.grid()
    plt.show()

def plot_vpwp_vertical_profile_all(budgets, zfull, ftype, coords_gp=[36, 37, 262, 264]):
    """
    Plots the vertical profile of a list of upwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of upwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    """
    plt.figure(figsize=(6, 8))
    linestyles = ('-', '-', '-', '-', '-', '-', '-', '--', '--', '--')
    colors = ('red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'red', 'blue', 'green')
    for i, budget in enumerate(budgets):
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon', 'time'])
        values = budget_mean.values
        phalf = budget.phalf.values
        zfull_sel = zfull.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        zfull_sel_mean = zfull_sel.mean(dim=['lat', 'lon', 'time'])
        zvalues = zfull_sel_mean.values - zfull_sel_mean.values[-1]
        plt.plot(10 ** 4 * values[::-1], zvalues[::-1], color=colors[i], linestyle=linestyles[i], label=budget.name)
    plt.gca().set_ylim(0, 1500)
    plt.gca().set_xlim(-20, 20)
    plt.xlabel(ftype + " $\\overline{v'w'}$ Budget [10$^{-4}$ m$^2$s$^{-3}$]", fontsize=14)
    plt.ylabel('Height from surface [m]', fontsize=14)
    plt.legend(loc='upper left')
    tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
    plt.yticks(ticks=tickss, fontsize=12)
    plt.xticks(ticks=[-20, -15, -10, -5, 0, 5, 10, 15, 20], fontsize=12)
    for tick in tickss:
        plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.savefig('your/file/path' + ftype + 'gp_llj_vpwp.png')
    plt.show()

def plot_vpwp_vertical_profile_all(budgets, zfull, ftype, day, coords_gp=[36, 37, 262, 264]):
    """
    Plots the vertical profile of a list of upwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of upwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    """
    plt.figure(figsize=(6, 8))
    linestyles = ('-', '-', '-', '-', '-', '-', '-', '--', '--', '--')
    colors = ('red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'red', 'blue', 'green')
    for i, budget in enumerate(budgets):
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon'])
        values = budget_mean.values
        phalf = budget.phalf.values
        zfull_sel = zfull.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        zfull_sel_mean = zfull_sel.mean(dim=['lat', 'lon'])
        zvalues = zfull_sel_mean.values - zfull_sel_mean.values[-1]
        plt.plot(10 ** 4 * values[::-1], zvalues[::-1], color=colors[i], linestyle=linestyles[i], label=budget.name)
    plt.gca().set_ylim(0, 1500)
    plt.gca().set_xlim(-20, 20)
    plt.xlabel(ftype + " $\\overline{v'w'}$ Budget [10$^{-4}$ m$^2$s$^{-3}$]", fontsize=14)
    plt.ylabel('Height from surface [m]', fontsize=14)
    plt.legend(loc='upper left')
    tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
    plt.yticks(ticks=tickss, fontsize=12)
    plt.xticks(ticks=[-20, -15, -10, -5, 0, 5, 10, 15, 20], fontsize=12)
    for tick in tickss:
        plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.savefig('your/file/path' + ftype + day + 'gp_llj_vpwp.png', bbox_inches='tight')
    plt.show()

def plot_upwp_vertical_profile_all(budgets, zfull, ftype, day, coords_gp=[36, 37, 262, 264]):
    """
    Plots the vertical profile of a list of upwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of upwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    """
    plt.figure(figsize=(6, 8))
    linestyles = ('-', '-', '-', '-', '-', '-', '-', '--', '--', '--')
    colors = ('red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'red', 'blue', 'green')
    for i, budget in enumerate(budgets):
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon', 'time'])
        values = budget_mean.values
        phalf = budget.phalf.values
        zfull_sel = zfull.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        zfull_sel_mean = zfull_sel.mean(dim=['lat', 'lon', 'time'])
        zvalues = zfull_sel_mean.values - zfull_sel_mean.values[-1]
        plt.plot(10 ** 4 * values[::-1], zvalues[::-1], color=colors[i], linestyle=linestyles[i], label=budget.name)
    plt.gca().set_ylim(0, 1500)
    plt.gca().set_xlim(-15, 15)
    plt.xlabel(ftype + " $\\overline{u'w'}$ Budget [10$^{-4}$ m$^2$s$^{-3}$]", fontsize=14)
    plt.ylabel('Height from surface [m]', fontsize=14)
    plt.legend(loc='upper left')
    tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400]
    plt.yticks(ticks=tickss, fontsize=12)
    plt.xticks(ticks=[-15, -10, -5, 0, 5, 10, 15], fontsize=12)
    for tick in tickss:
        plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.savefig('your/file/path' + ftype + day + 'gp_llj_upwp.png', bbox_inches='tight')
    plt.show()

def plot_rtpwp_vertical_profile_all(budgets, zfull, day, ftype, coords_gp=[36, 37, 262, 264]):
    """
    Plots the vertical profile of a list of upwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of upwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    """
    plt.figure(figsize=(6, 8))
    linestyles = ('-', '-', '-', '-', '-', '-', '-', '--', '--', '--')
    colors = ('red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'red', 'blue', 'green')
    for i, budget in enumerate(budgets):
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon'])
        values = budget_mean.values
        phalf = budget.phalf.values
        zfull_sel = zfull.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        zfull_sel_mean = zfull_sel.mean(dim=['lat', 'lon'])
        zvalues = zfull_sel_mean.values - zfull_sel_mean.values[-1]
        plt.plot(10 ** 7 * values[::-1], zvalues[::-1], color=colors[i], linestyle=linestyles[i], label=budget.name)
    plt.gca().set_ylim(0, 1900)
    plt.gca().set_xlim(-15, 15)
    plt.xlabel(ftype + " $\\overline{r'_tw'}$ Budget [10$^{-7}$ m kg s$^{-2}$]", fontsize=14)
    plt.ylabel('Height from surface [m]', fontsize=14)
    plt.legend(loc='upper left')
    tickss = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800]
    plt.yticks(ticks=tickss, fontsize=12)
    plt.xticks(ticks=[-15, -10, -5, 0, 5, 10, 15], fontsize=12)
    for tick in tickss:
        plt.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.savefig('your/file/path' + ftype + day + 'gp_llj_rtpwp.png', bbox_inches='tight')
    plt.show()

def plot_vpwp_vertical_profile(budgets, coords_gp=[10, 15, 300, 315]):
    """
    Plots the vertical profile of a list of vpwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of vpwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    """
    plt.figure(figsize=(4, 6))
    for budget in budgets[:-4]:
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon', 'time'])
        values = budget_mean.values * 10 ** 4
        phalf = budget.phalf.values
        plt.plot(values, phalf, linestyle=linestyles[i], label=budget.name)
    plt.gca().invert_yaxis()
    plt.xlabel('Vpwp Budget [10^$^{-4}$ m^2/s$^3$]', fontsize=14)
    plt.ylabel('Pressure (hPa)', fontsize=14)
    plt.gca().set_ylim(1000, 200)
    plt.legend()
    plt.grid()
    plt.show()

def plot_vertical_profile_gp(budgets, coords_gp=[10, 15, 300, 315]):
    """
    Plots the vertical profile of a list of upwp budgets averaged over specified lat/lon coordinates.
    
    Parameters:
    budgets (list of xarray.DataArray): List of upwp budget terms.
    coords_gp (list): Coordinates for averaging [lat_min, lat_max, lon_min, lon_max].
    coords_gp=[30, 40, 260, 265]
    coords_gp=[10, 15, 300, 315]
    """
    plt.figure(figsize=(4, 6))
    linestyles = ('-', ':', '-', ':', '-', ':', '-', '--', ':', '-')
    linestyles = ('-', '-', '-', '-', '-', '-', '-', '-', '-', '-')
    colors = ('red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'red', 'blue', 'green')
    for i, budget in enumerate(budgets):
        budget_sel = budget.sel(lat=slice(coords_gp[0], coords_gp[1]), lon=slice(coords_gp[2], coords_gp[3]))
        budget_mean = budget_sel.mean(dim=['lat', 'lon', 'time'])
        values = budget_mean.values
        phalf = budget.phalf.values
        plt.plot(10 ** 4 * values, phalf, color=colors[i], linestyle=linestyles[i], label=budget.name)
    plt.gca().invert_yaxis()
    plt.gca().set_ylim(1000, 300)
    plt.gca().set_xlim(-5, 5)
    plt.xlabel('xp2_tp great plains [10^$^{-4}$ m^2/s^3]')
    plt.ylabel('Pressure (hPa)')
    plt.legend(loc='upper left')
    plt.savefig('your/file/path')
    plt.grid()
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
