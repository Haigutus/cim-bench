"""Parser adapter interface for benchmarking."""

from abc import ABC, abstractmethod
from typing import Any, Dict
from pathlib import Path


class IncompleteLoadError(Exception):
    """Raised when a tool cannot load every profile file of a dataset.

    Benchmarks require all available CGMES profiles to be loaded (merged or
    as separate models). The benchmark template turns this into a pytest
    skip so partial loads never produce misleading numbers.
    """


class QueryUnsupported(Exception):
    """Raised by a query method the tool cannot run on this dataset.

    Load (and export) may still be benchmarked; only the affected query test
    is skipped. Use when a query is infeasible rather than unimplemented -
    e.g. a slow in-memory SPARQL engine that cannot finish a join query on a
    million-triple graph in reasonable time.
    """


class ParserAdapter(ABC):
    """
    Adapter interface that each parser must implement for benchmarking.

    This standardizes how benchmarks interact with different parsers,
    eliminating the need for parser-specific benchmark code.
    """

    @classmethod
    def get_version(cls) -> str:
        """Get the library version string."""
        return "unknown"

    @classmethod
    def get_dependencies(cls) -> dict:
        """Get versions of library dependencies (excluding benchmark framework).

        Returns:
            Dict of dependency name → version string.
        """
        return {}

    @staticmethod
    def _get_package_dependencies(package_name: str) -> dict:
        """Get installed versions of a package's dependencies."""
        from importlib.metadata import requires, version
        EXCLUDE = {"pytest", "pytest-benchmark", "psutil"}
        reqs = requires(package_name) or []
        deps = {}
        for req in reqs:
            # Skip extras/conditional deps
            if "; extra ==" in req:
                continue
            name = req.split(";")[0].split("[")[0].split(">")[0].split("<")[0].split("=")[0].split("!")[0].split("~")[0].strip()
            if name in EXCLUDE:
                continue
            try:
                deps[name] = version(name)
            except Exception:
                pass
        return deps

    @classmethod
    def get_tags(cls) -> list:
        """Get capability/language tags for this tool (drives site filtering).

        Vocabulary: parser, serializer, validator, query, powerflow-tool,
        triplestore, typed-model, cli + language (python, java, c++, rust, go, c#).
        """
        return ["parser"]

    @classmethod
    @abstractmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser (e.g., 'PyPowSyBl', 'Triplets')."""
        pass

    @classmethod
    @abstractmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization (e.g., '#3498db')."""
        pass

    @abstractmethod
    def load(self, dataset_key: str) -> Any:
        """
        Load dataset and return the loaded object.

        Args:
            dataset_key: Key in DATASETS dict (e.g., "svedala_igm_cgmes_3")

        Returns:
            Loaded parser object (loader, network, etc.)
        """
        pass

    @abstractmethod
    def get_load_metrics(self, loaded_obj: Any, memory_mb: float) -> Dict[str, Any]:
        """
        Extract metrics from loaded object for benchmark.extra_info.

        Args:
            loaded_obj: Object returned by load()
            memory_mb: Memory delta in MB

        Returns:
            Dict of metrics for benchmark.extra_info
        """
        pass

    @abstractmethod
    def get_lines_count(self, loaded_obj: Any) -> int:
        """Get count of lines in loaded dataset."""
        pass

    @abstractmethod
    def get_generators_count(self, loaded_obj: Any) -> int:
        """Get count of generators in loaded dataset."""
        pass

    @abstractmethod
    def get_loads_count(self, loaded_obj: Any) -> int:
        """Get count of loads in loaded dataset."""
        pass

    @abstractmethod
    def get_substations_count(self, loaded_obj: Any) -> int:
        """Get count of substations in loaded dataset."""
        pass

    def export(self, loaded_obj: Any, output_path: Path) -> None:
        """
        Export loaded data to file(s).

        Args:
            loaded_obj: Object returned by load()
            output_path: Path to export file (or directory for multiple files)

        Returns:
            None

        Note:
            This method is optional. Parsers that don't support export
            should raise NotImplementedError with a descriptive message.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not support export functionality"
        )
