"""Thin wrapper around the cimgo CLI for subprocess-based benchmarking.

cimgo is a Go binary with no Python bindings, so we call it via subprocess
(see benchmarks/cli_benchmark_template.py). This module provides the binary
resolution and command builders shared by both benchmark files.
"""

import os
import shutil

DISPLAY_NAME = "cimgo"
COLOR = "#2ecc71"
BINARY_NAME = "cimcli-linux-amd64"


def get_cimgo_bin():
    """Find the cimgo binary via env var or PATH."""
    return os.environ.get("CIMGO_BIN") or shutil.which(BINARY_NAME)


def validate_cmd(binary, files, tmp_dir):
    """Build `cimgo validate -json` command (exits 1 on violations - expected)."""
    return [binary, "validate", "-json"] + [str(f) for f in files]


def convert_cmd(binary, files, tmp_dir):
    """Build `cimgo convert -to json` command."""
    return [binary, "convert", "-to", "json", "-out", str(tmp_dir / "output.json")] + [
        str(f) for f in files
    ]
