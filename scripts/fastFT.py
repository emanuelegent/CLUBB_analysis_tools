"""Script `fastFT`.

Auto-cleaned for publication: configuration-driven paths and structured logging.
"""

from __future__ import annotations
import logging


logger = logging.getLogger(__name__)

def fastAllGridFT(x, t):
    """
    This version of fastFT (see above) does all gridpoints at once.

    Use a Numerical Python function to compute a FAST Fourier transform -- which should give the same result as a simple
    SLOW Fourier integration via the trapezoidal rule.

    Return mean + amplitudes and times-of-maximum of the first three Fourier harmonic components of a time series x(t).
    Do NOT detrend the time series first, in order to retain the "sawtooth" frequency implied by the input length of the
    time series (e.g. the 24-hour period from a composite-diurnal cycle).

    On input: x[k,i,j] = values      at each gridpoint (i,j) for N times (k), e.g. N = 8 for a 3-hr composite-diurnal cycle
          t[k,i,j] = timepoints  at each gridpoint (i,j) for N times (k), e.g. Local Standard Times

    On output: c[i,j] = mean value at each gridpoint (i,j) in the time series ("zeroth" term in Fourier series)
           maxvalue[n,i,j] = amplitude       at each gridpoint (i,j) for each Fourier harmonic (n)
           tmax    [n,i,j] =\xa0time of maximum at each gridpoint (i,j) for each Fourier harmonic (n)

                Curt Covey, PCMDI/LLNL                                      December 2016
    """
    import numpy
    print('Creating output arrays ...')
    nx = x.shape[1]
    ny = x.shape[2]
    tmax = numpy.zeros((3, nx, ny))
    maxvalue = numpy.zeros((3, nx, ny))
    print('Calling numpy FFT function ...')
    X = numpy.fft.ifft(x, axis=0)
    print(X.shape)
    print('Converting from complex-valued FFT to real-valued amplitude and phase ...')
    a = X.real
    b = X.imag
    S = numpy.sqrt(a ** 2 + b ** 2)
    c = S[0]
    for n in range(3):
        maxvalue[n] = S[n + 1] + S[-n - 1]
        tmax[n] = numpy.arctan2(b[n + 1], a[n + 1])
        tmax[n] = tmax[n] * 12.0 / (numpy.pi * (n + 1))
        tmax[n] = tmax[n] + t[0]
        tmax[n] = tmax[n] % (24 / (n + 1))
    return (c, maxvalue, tmax)

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
