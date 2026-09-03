"""cimoxide parser adapter for benchmarking.

cimoxide is a Rust CGMES parser with typed structs generated from ENTSO-E
RDF/SHACL schemas, plus SHACL/SPARQL validation. Benchmarked in-process via
its PyO3 bindings (the `cimoxide` package).

Counts run through cimoxide's SPARQL engine (oxigraph), so cimoxide sits in
the same query family as the other triplestore-backed tools. The graph is
materialised lazily on the first query and cached, so the first query pays the
build and the rest are index lookups.

Lines are the exception: they use cimoxide's native `count_type` index rather
than PowSyBl's acLineSegments join, which oxigraph's planner needs ~4 minutes
to answer on RealGrid. Both return the same count, but the timing is not
comparable with the tools that run the join - it measures an O(1) lookup, not
a query. It is the same for VeraGrid, which also has a native index.

Repository: https://github.com/m-mirz/cimoxide
"""
import re
import tempfile
import zipfile
from pathlib import Path

from cimoxide import CimDataset
from parser_adapter import ParserAdapter
from datasets import DATASETS

# CGMES profiles cimoxide can encode, longest name first so EQBD beats EQ.
PROFILES = ("EQBD", "SSH", "EQ", "SV", "TP", "SC", "OP", "DY")


def _profiles_in(files):
    """Profile short names appearing as a token in the loaded file names."""
    found = []
    for path in files:
        tokens = set(re.split(r"[^A-Za-z0-9]+", Path(path).stem.upper()))
        for profile in PROFILES:
            if profile in tokens and profile not in found:
                found.append(profile)
    return found


class CimoxideAdapter(ParserAdapter):
    """Adapter for cimoxide via its PyO3 Python bindings."""

    def __init__(self):
        self.dataset = None
        self.profiles = []

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
        return ["parser", "serializer", "validator", "query", "typed-model",
                "python", "rust"]

    def load(self, dataset_key: str):
        """Load all dataset files into a single merged CimDataset."""
        dataset = DATASETS[dataset_key]

        files = [v for k, v in dataset.items() if "_metadata" not in k.lower()]

        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            tmp = temp_dir.name
            zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
            files = list(Path(tmp).rglob("*.xml"))

        self.profiles = _profiles_in(files)
        self.dataset = CimDataset.decode_files([str(f) for f in files])

        if "ZIP" in dataset:
            temp_dir.cleanup()

        return self

    def _count_instances(self, class_name: str) -> int:
        """SPARQL COUNT of one CIM class (cim: is pre-bound to CIM100)."""
        rows = self.dataset.query(
            f"SELECT (COUNT(DISTINCT ?s) AS ?count) WHERE {{ ?s a cim:{class_name} }}")
        return int(rows[0]["count"]) if rows else 0

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
        """Lines via cimoxide's native type index (see module docstring)."""
        return loaded_obj.dataset.count_type("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        return (loaded_obj._count_instances("ConformLoad")
                + loaded_obj._count_instances("NonConformLoad")
                + loaded_obj._count_instances("EnergyConsumer"))

    def get_substations_count(self, loaded_obj):
        return loaded_obj._count_instances("Substation")

    def export(self, loaded_obj, output_path):
        """Write one RDF/XML file per loaded CGMES profile."""
        output_dir = Path(output_path).parent
        loaded_obj.dataset.write_xml_files(str(output_dir), loaded_obj.profiles)
        return output_path
