"""Thin wrapper around the cimgo CLI for subprocess-based benchmarking.

cimgo is a Go binary with no Python bindings, so we call it via subprocess
(see benchmarks/cli_benchmark_template.py). This module provides the binary
resolution and command builders shared by both benchmark files.
"""

import json
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


def inspect_validation(result):
    """Exit 1 is meaningful only with a structured validation report.

    cimgo v0.0.5 also exits 1 for read/parse errors, without a JSON report:
    https://github.com/m-mirz/cimgo/blob/v0.0.5/cmd/cimcli/main.go
    """
    report = json.loads(result.stdout)
    assert report is None or isinstance(report, list), "expected cimgo JSON validation report"
    report = report or []
    assert all(isinstance(item, dict) and isinstance(item.get("Severity"), str) for item in report), (
        "expected cimgo validation entries with Severity"
    )
    violations = sum(item["Severity"] == "sh:Violation" for item in report)
    assert result.returncode == (1 if violations else 0), "validation status disagrees with reported violations"
    return {"validation_report_entries": len(report or []),
            "validation_violation_count": violations,
            "validation_outcome": "violations_reported" if result.returncode else "no_violation_exit"}


def convert_cmd(binary, files, tmp_dir):
    """Build `cimgo convert -to json` command."""
    return [binary, "convert", "-to", "json", "-out", str(tmp_dir / "output.json")] + [
        str(f) for f in files
    ]
