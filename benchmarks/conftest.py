"""Attach reproducible input/build evidence without adding work to timed calls."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import uuid

import pytest

ROOT = Path(__file__).resolve().parents[1]
OUTCOMES = []
COLLECTED_DATASETS = set()


def pytest_collection_modifyitems(items):
    # Preserve input provenance even when a CLI fails before timing begins.
    for item in items:
        if key := getattr(getattr(item, "obj", None), "_cim_bench_dataset_key", None):
            COLLECTED_DATASETS.add(key)


def git_evidence():
    def git(*args):
        try:
            result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
        except FileNotFoundError:
            return None
        return result.stdout.strip() if result.returncode == 0 else None

    if not (commit := git("rev-parse", "HEAD")):
        return {"commit": None, "dirty": None}
    status = git("status", "--porcelain", "--untracked-files=normal")
    return {"commit": commit, "dirty": None if status is None else bool(status)}


def input_evidence(dataset):
    inputs = []
    for role, path in sorted(dataset.items()):
        if role.startswith("_"):
            continue
        path = Path(path)
        record = {"role": role, "name": path.name, "present": path.is_file()}
        if record["present"]:
            with path.open("rb") as stream:
                record.update(sha256=hashlib.file_digest(stream, "sha256").hexdigest(),
                              bytes=path.stat().st_size)
        inputs.append(record)
    return {"cgmes_version": dataset["_metadata"]["cgmes_version"], "inputs": inputs}


def pytest_runtest_logreport(report):
    if report.when == "call" or report.outcome != "passed":
        outcome = {"test": report.nodeid, "phase": report.when, "outcome": report.outcome}
        if cli := dict(report.user_properties).get("cim_bench_cli"):
            outcome["cli"] = cli
        OUTCOMES.append(outcome)


def pytest_collectreport(report):
    if report.outcome != "passed":
        OUTCOMES.append({"test": report.nodeid, "phase": "collection", "outcome": report.outcome})


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    # Run before pytest-benchmark writes JSON during its sessionfinish hook.
    session.config._cim_bench_run = {"exit_status": int(exitstatus),
                                    "tests_collected": session.testscollected}
    yield
    destination = session.config.getoption("benchmark_json", default=None)
    if destination and not getattr(session.config, "_cim_bench_json_written", False):
        # pytest-benchmark omits JSON when every operation fails before timing.
        # Overwrite any stale requested report with explicit failure/skip evidence.
        report = {"benchmarks": [], "incomplete_run": True}
        pytest_benchmark_update_json(session.config, [], report)
        Path(destination).write_text(json.dumps(report, indent=2) + "\n")


@pytest.hookimpl(optionalhook=True)
def pytest_benchmark_update_json(config, benchmarks, output_json):
    # The container runner supplies build identity when source .git is absent.
    # Such values are declared evidence, distinct from an observed checkout.
    from datasets import DATASETS

    config._cim_bench_json_written = True

    keys = {b.get("extra_info", {}).get("dataset_key") for b in output_json["benchmarks"]}
    keys.update(COLLECTED_DATASETS)
    output_json["cim_bench_evidence"] = {
        "schema": "cim-bench-evidence",
        "schema_version": 1,
        "run_id": os.environ.get("CIM_BENCH_RUN_ID", str(uuid.uuid4())),
        "run": config._cim_bench_run,
        "benchmark": git_evidence(),
        "declared_build": {
            "benchmark_commit": os.environ.get("CIM_BENCH_COMMIT"),
            "image_id": os.environ.get("CIM_BENCH_IMAGE_ID"),
            "tool_source_commit": os.environ.get("CIM_BENCH_TOOL_COMMIT") or os.environ.get("POWERIO_SOURCE_COMMIT"),
        },
        "datasets": {key: input_evidence(DATASETS[key]) for key in sorted(keys - {None})},
        "tests": list(OUTCOMES),
        "limitations": [
            "Retained RSS after repeated loads is not isolated peak memory or model size.",
            "Compare query timings only when operation and count semantics match.",
            "Same-tool export reparsing does not establish independent consumer acceptance.",
        ],
    }
