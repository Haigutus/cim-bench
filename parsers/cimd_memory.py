"""Peak-RSS measurement helper for subprocess-based benchmarks (cimd).

The other adapters measure memory via psutil in-process around their load
call. cimd runs in a subprocess, so we spawn it via psutil.Popen and poll
RSS tightly until the process exits, then return the peak in MB.
"""

import subprocess

import psutil


def measure_peak_rss_mb(args):
    """Run `args` as a subprocess and return its peak resident-set size in MB."""
    proc = psutil.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    peak = 0
    while True:
        try:
            rss = proc.memory_info().rss
            if rss > peak:
                peak = rss
        except psutil.NoSuchProcess:
            break
        if proc.poll() is not None:
            try:
                rss = proc.memory_info().rss
                if rss > peak:
                    peak = rss
            except psutil.NoSuchProcess:
                pass
            break
    proc.wait()
    return peak / (1024 * 1024)
