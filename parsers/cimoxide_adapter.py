"""cimoxide parser adapter for benchmarking.

cimoxide is a Rust CGMES parser with typed structs generated from ENTSO-E
RDF/SHACL schemas, plus SHACL/SPARQL validation. Benchmarked in-process via
its published PyO3 bindings (the `cimoxide` package on PyPI).
Repository: https://github.com/m-mirz/cimoxide
"""
import tempfile
import zipfile
from pathlib import Path

from cimoxide import CimDataset
from parser_adapter import ParserAdapter
from datasets import DATASETS


class CimoxideAdapter(ParserAdapter):
    """Adapter for cimoxide via its PyO3 Python bindings."""

    def __init__(self):
        self.dataset = None

    @classmethod
    def get_version(cls) -> str:
        from importlib.metadata import version
        return version("cimoxide")

    @classmethod
    def get_dependencies(cls) -> dict:
        return cls._get_package_dependencies("cimoxide")

    @classmethod
    def get_display_name(cls) -> str:
        return "cimoxide"

    @classmethod
    def get_color(cls) -> str:
        return "#ce422b"  # Rust orange

    @classmethod
    def get_tags(cls):
        return ["parser", "validator", "typed-model", "python", "rust"]

    def load(self, dataset_key: str):
        """Load all dataset files into a single merged CimDataset."""
        dataset = DATASETS[dataset_key]

        files = (v for k, v in dataset.items() if "_metadata" not in k.lower())

        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            tmp = temp_dir.name
            zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
            files = Path(tmp).rglob("*.xml")

        self.dataset = CimDataset.decode_files([str(f) for f in files])

        if "ZIP" in dataset:
            temp_dir.cleanup()

        return self

    def _count_type(self, type_name: str) -> int:
        return len(self.dataset.by_type().get(type_name, []))

    def get_load_metrics(self, loaded_obj, memory_mb):
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "objects": len(loaded_obj.dataset),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        return loaded_obj._count_type("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        return loaded_obj._count_type("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        return (loaded_obj._count_type("ConformLoad")
                + loaded_obj._count_type("NonConformLoad")
                + loaded_obj._count_type("EnergyConsumer"))

    def get_substations_count(self, loaded_obj):
        return loaded_obj._count_type("Substation")
