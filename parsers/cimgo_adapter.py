"""Thin wrapper around the cimgo CLI for subprocess-based benchmarking.

cimgo is a Go binary with no Python bindings, so we call it via subprocess.
This module provides helpers shared by both benchmark files.
"""

import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from datasets import DATASETS

DISPLAY_NAME = "cimgo"
COLOR = "#2ecc71"
BINARY_NAME = "cimcli-linux-amd64"


def get_cimgo_bin():
    """Find the cimgo binary via env var or PATH."""
    return os.environ.get("CIMGO_BIN") or shutil.which(BINARY_NAME)


def resolve_dataset_files(dataset_key):
    """Return (list[Path], temp_dir_or_None) for a dataset.

    Extracts ZIP if needed. Caller must call temp_dir.cleanup() when done.
    """
    dataset = DATASETS[dataset_key]

    if "ZIP" in dataset:
        temp_dir = tempfile.TemporaryDirectory()
        zipfile.ZipFile(dataset["ZIP"]).extractall(temp_dir.name)
        files = list(Path(temp_dir.name).rglob("*.xml"))
        return files, temp_dir

    files = [Path(v) for k, v in dataset.items() if "_metadata" not in k.lower()]
    return files, None


def validate_files(bin_path, files):
    """Run `cimgo validate -json` on the given files."""
    result = subprocess.run(
        [bin_path, "validate", "-json"] + [str(f) for f in files],
        capture_output=True,
        text=True,
    )
    # validate returns exit code 1 when violations are found — that's expected
    return result.stdout


def convert_files(bin_path, files, output_path):
    """Run `cimgo convert -to json` on the given files."""
    result = subprocess.run(
        [bin_path, "convert", "-to", "json", "-out", str(output_path)]
        + [str(f) for f in files],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"cimgo convert failed: {result.stderr}")
    return result.stdout
