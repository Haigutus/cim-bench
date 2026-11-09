"""
Simple benchmark template generator.

Usage in benchmark file:
    from triplets_adapter import TripletsAdapter
    from benchmark_template import create_benchmarks

    create_benchmarks(
        adapter=TripletsAdapter(),
        dataset_key="svedala_igm_cgmes_3",
        parser_name="triplets",
        dataset_name="svedala"
    )
"""

import psutil
import pytest
import sys
import shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from datasets import DATASETS, get_size_mb
from parser_adapter import IncompleteLoadError, QueryUnsupported


def export_files(output_path):
    """Require fresh nonempty output, including adapters that write a directory."""
    files = sorted(path for path in output_path.parent.rglob("*") if path.is_file())
    assert files and any(path.stat().st_size for path in files), "export produced no nonempty files"
    return files


def prepare_export_output(output_path):
    """Remove only this test's output outside the measured export operation."""
    if output_path.parent.exists():
        shutil.rmtree(output_path.parent)
    output_path.parent.mkdir()


def get_memory_mb():
    """Get current memory usage in MB."""
    return psutil.Process().memory_info().rss / 1024 / 1024


def create_benchmarks(adapter, dataset_key, parser_name, dataset_name):
    """
    Create all benchmark fixtures and tests for a parser+dataset.

    Call this from your benchmark file and it will inject all tests
    into the module's namespace.

    Args:
        adapter: ParserAdapter instance
        dataset_key: Key in DATASETS dict
        parser_name: Short name for parser (e.g., "triplets")
        dataset_name: Short name for dataset (e.g., "svedala")
    """

    # Get caller's globals to inject tests
    import inspect
    caller_globals = inspect.currentframe().f_back.f_globals

    def annotate(benchmark):
        benchmark.extra_info.update({
            "library": parser_name,
            "library_version": adapter.__class__.get_version(),
            "dataset": dataset_name,
            "dataset_key": dataset_key,
            "display_name": adapter.__class__.get_display_name(),
            "color": adapter.__class__.get_color(),
            "tags": adapter.__class__.get_tags(),
            **adapter.__class__.get_measurement_notes(),
        })

    # Memory baseline fixture
    @pytest.fixture(scope="module")
    def memory_baseline():
        return get_memory_mb()

    # Loaded object fixture
    @pytest.fixture(scope="module")
    def loaded_object():
        try:
            obj = adapter.load(dataset_key)
        except IncompleteLoadError as e:
            pytest.skip(f"tool cannot load all profiles: {e}")
        yield obj
        # Cleanup if adapter has cleanup method
        if hasattr(adapter, 'cleanup'):
            adapter.cleanup()

    # Load test
    def test_load(benchmark, memory_baseline):
        """Benchmark loading dataset."""
        try:
            loaded_obj = benchmark(adapter.load, dataset_key)
        except IncompleteLoadError as e:
            pytest.skip(f"tool cannot load all profiles: {e}")

        memory_delta = get_memory_mb() - memory_baseline
        metrics = adapter.get_load_metrics(loaded_obj, memory_delta)
        metrics["memory_method"] = "retained_RSS_delta_after_calibrated_repeated_loads"
        metrics["memory_is_peak"] = False

        # Add dataset metadata
        dataset = DATASETS[dataset_key]
        metadata = dataset["_metadata"]
        metrics["dataset_size_mb"] = metadata["size_mb"]
        metrics["cgmes_version"] = metadata["cgmes_version"]

        # Add library and dataset metadata
        metrics["library_dependencies"] = adapter.__class__.get_dependencies()

        # Add Java version if available (separate top-level key)
        deps = adapter.__class__.get_dependencies()
        if "java" in deps:
            metrics["java_version"] = deps["java"]

        for key, value in metrics.items():
            benchmark.extra_info[key] = value
        annotate(benchmark)

        # Cleanup if needed
        if hasattr(adapter, 'cleanup'):
            adapter.cleanup()

        assert loaded_obj is not None

    # Query tests
    def test_get_lines(benchmark, loaded_object):
        """Benchmark querying lines."""
        try:
            count = benchmark(adapter.get_lines_count, loaded_object)
        except QueryUnsupported as e:
            pytest.skip(f"query not feasible for this tool/dataset: {e}")
        benchmark.extra_info["line_count"] = count
        benchmark.extra_info["query_type"] = "get_lines"
        annotate(benchmark)
        assert count > 0

    def test_get_generators(benchmark, loaded_object):
        """Benchmark querying generators."""
        try:
            count = benchmark(adapter.get_generators_count, loaded_object)
        except QueryUnsupported as e:
            pytest.skip(f"query not feasible for this tool/dataset: {e}")
        benchmark.extra_info["generator_count"] = count
        benchmark.extra_info["query_type"] = "get_generators"
        annotate(benchmark)
        assert count > 0

    def test_get_loads(benchmark, loaded_object):
        """Benchmark querying loads."""
        try:
            count = benchmark(adapter.get_loads_count, loaded_object)
        except QueryUnsupported as e:
            pytest.skip(f"query not feasible for this tool/dataset: {e}")
        benchmark.extra_info["load_count"] = count
        benchmark.extra_info["query_type"] = "get_loads"
        annotate(benchmark)
        # RealGrid has 0 loads, so allow >= 0
        assert count >= 0

    def test_get_substations(benchmark, loaded_object):
        """Benchmark querying substations."""
        try:
            count = benchmark(adapter.get_substations_count, loaded_object)
        except QueryUnsupported as e:
            pytest.skip(f"query not feasible for this tool/dataset: {e}")
        benchmark.extra_info["substation_count"] = count
        benchmark.extra_info["query_type"] = "get_substations"
        annotate(benchmark)
        assert count > 0

    # Export test (only if adapter supports it)
    def _has_export():
        try:
            adapter.export(None, None)
        except NotImplementedError:
            return False
        except Exception:
            return True
        return True

    has_export = _has_export()

    if has_export:
        @pytest.fixture
        def export_output(tmp_path):
            """Each test starts empty; prior tools/datasets cannot satisfy it."""
            return tmp_path / "output" / "export_output.xml"

        def test_export(benchmark, loaded_object, export_output, pytestconfig):
            """Benchmark exporting dataset."""
            # Check a first write into an empty directory outside the timing.
            # Repeated benchmark rounds may overwrite files, but a stale file
            # from another test cannot make a no-op exporter pass.
            prepare_export_output(export_output)
            adapter.export(loaded_object, export_output)
            export_files(export_output)
            benchmark.pedantic(
                adapter.export,
                args=(loaded_object, export_output),
                setup=lambda: prepare_export_output(export_output),
                rounds=pytestconfig.getoption("benchmark_min_rounds"),
                iterations=1,
            )

            benchmark.extra_info["operation"] = "export"
            benchmark.extra_info["export_timing_method"] = "one_call_per_round_with_fresh_destination"
            benchmark.extra_info["export_cleanup_timed"] = False

            # Verify export produced output
            exported_files = export_files(export_output)
            benchmark.extra_info["export_file_count"] = len(exported_files)
            benchmark.extra_info["export_bytes"] = sum(path.stat().st_size for path in exported_files)
            benchmark.extra_info.update(adapter.get_export_metrics(loaded_object, export_output))
            annotate(benchmark)

    # Set proper test names for pytest discovery
    test_load.__name__ = f"test_{parser_name}_load_{dataset_name}"
    test_get_lines.__name__ = f"test_{parser_name}_get_lines"
    test_get_generators.__name__ = f"test_{parser_name}_get_generators"
    test_get_loads.__name__ = f"test_{parser_name}_get_loads"
    test_get_substations.__name__ = f"test_{parser_name}_get_substations"

    # Inject into caller's module namespace
    caller_globals['memory_baseline'] = memory_baseline
    caller_globals['loaded_object'] = loaded_object
    caller_globals[test_load.__name__] = test_load
    caller_globals[test_get_lines.__name__] = test_get_lines
    caller_globals[test_get_generators.__name__] = test_get_generators
    caller_globals[test_get_loads.__name__] = test_get_loads
    caller_globals[test_get_substations.__name__] = test_get_substations

    if has_export:
        test_export.__name__ = f"test_{parser_name}_export_{dataset_name}"
        caller_globals['export_output'] = export_output
        caller_globals[test_export.__name__] = test_export
