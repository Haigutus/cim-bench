"""Parser adapter interface for benchmarking."""

from abc import ABC, abstractmethod
from typing import Any, Dict
from pathlib import Path


class ParserAdapter(ABC):
    """
    Adapter interface that each parser must implement for benchmarking.

    This standardizes how benchmarks interact with different parsers,
    eliminating the need for parser-specific benchmark code.
    """

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
