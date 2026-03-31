"""RDFlib export benchmark for Svedala dataset."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from rdflib_adapter import RDFlibAdapter
from datasets import DATASETS
import pytest
import psutil

REPO_ROOT = Path(__file__).parent.parent


def get_memory_mb():
    """Get current memory usage in MB."""
    return psutil.Process().memory_info().rss / 1024 / 1024


@pytest.fixture(scope="module")
def adapter():
    """Create adapter instance."""
    return RDFlibAdapter()


@pytest.fixture(scope="module")
def loaded_object(adapter):
    """Load dataset once for all tests."""
    obj = adapter.load("svedala_igm_cgmes_3")
    yield obj


@pytest.fixture
def temp_output():
    """Create output directory for rdflib exports."""
    output_dir = REPO_ROOT / "temp" / "export" / "rdflib"
    output_dir.mkdir(parents=True, exist_ok=True)
    yield output_dir / "export_output.xml"


def test_rdflib_export_svedala(benchmark, adapter, loaded_object, temp_output):
    """Benchmark exporting Svedala dataset with RDFlib."""
    # Benchmark the export operation
    result_path = benchmark(adapter.export, loaded_object, temp_output)

    # Add metrics
    benchmark.extra_info["library"] = "rdflib"
    benchmark.extra_info["dataset"] = "svedala"
    benchmark.extra_info["operation"] = "export"
    benchmark.extra_info["display_name"] = adapter.get_display_name()
    benchmark.extra_info["color"] = adapter.get_color()
    benchmark.extra_info["output_file"] = str(result_path.name)

    # Check that output exists and has content
    assert result_path.exists()
    assert result_path.stat().st_size > 0
