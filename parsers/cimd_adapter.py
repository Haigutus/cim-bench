"""Thin wrapper around the cimd CLI for subprocess-based benchmarking.

cimd is a Zig binary with no Python bindings, so we call it via subprocess
(see benchmarks/cli_benchmark_template.py). This module provides the binary
resolution and command builders shared by both benchmark files.

cimd takes a single primary CGMES file per invocation (XML or ZIP), with
optional profile flags, so the builders select profile files by name.
Originally proposed by the cimd author in PR #3.
"""

import os
import shutil

DISPLAY_NAME = "cimd"
COLOR = "#f39c12"


def get_cimd_bin():
    """Find the cimd binary via env var or PATH."""
    return os.environ.get("CIMD_BIN") or shutil.which("cimd")


def _find_profile(files, token):
    """Return the file whose name contains _{token} (e.g. _EQ), or None."""
    return next((f for f in files if f"_{token}" in f.stem.upper()), None)


def types_cmd(binary, files, tmp_dir):
    """Build `cimd types --json` on the EQ profile (parse + per-type counts)."""
    return [binary, "types", "--json", str(_find_profile(files, "EQ"))]


def convert_cmd(binary, files, tmp_dir):
    """Build `cimd convert` EQ (+TP/SSH) to JIIDM JSON."""
    cmd = [binary, "convert", str(_find_profile(files, "EQ"))]
    if tp := _find_profile(files, "TP"):
        cmd += ["--tp", str(tp)]
    if ssh := _find_profile(files, "SSH"):
        cmd += ["--ssh", str(ssh)]
    return cmd + ["--output", str(tmp_dir / "output.json")]
