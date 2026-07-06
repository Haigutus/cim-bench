"""Peak-RSS measurement for subprocess-based benchmarks.

Spawns the command via psutil.Popen and polls RSS until the process
exits, returning the peak value in MB.
"""

import subprocess

import psutil


def measure_peak_rss_mb(args):
    """Run *args* as a subprocess and return its peak RSS in MB."""
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
