"""CIMpy parser adapter for benchmarking.

CIMpy is a Python library for importing/exporting CGMES XML/RDF files.
Repository: https://github.com/sogno-platform/cimpy

KNOWN ISSUES (as of cimpy v1.1.0):
----------------------------------
1. CGMES 3.0 NOT SUPPORTED:
   - Only cgmes_v2_4_15 module is included
   - Svedala dataset (CGMES 3.0) fails: all classes show "Module ... not implemented"
   - Results in empty topology with 0 element counts

2. CGMES 2.4.15 PARSING BUG:
   - RealGrid dataset fails with: ValueError: invalid literal for int() with base 10: '60.000000'
   - Parser tries to convert float values to integers
   - Fails during _set_attributes() phase in cimimport.py:271

3. STATUS:
   - This adapter is in dev-cimpy branch for future investigation
   - Needs cimpy library fixes or different test datasets
   - May work with other CGMES 2.4.15 files that don't trigger the parsing bug

TESTING PERFORMED:
-----------------
- Tested on Svedala IGM (CGMES 3.0, 7.3MB): Classes not implemented
- Tested on RealGrid (CGMES 2.4.15, 86.5MB): Parsing error
- Both datasets work with other parsers (triplets, pypowsybl, etc.)

For details, see test output in git history when this was tested.
"""

import cimpy
import tempfile
import zipfile
from pathlib import Path
from parser_adapter import ParserAdapter
from datasets import DATASETS


class CimpyAdapter(ParserAdapter):
    """Adapter for cimpy library."""

    def __init__(self):
        self.topology = None
        self.meta_info = None

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "cimpy"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#e377c2"  # Pink/magenta

    def load(self, dataset_key: str):
        """Load CGMES files using cimpy."""
        dataset = DATASETS[dataset_key]
        cgmes_version = self._get_cgmes_version(dataset_key)

        if "ZIP" in dataset:
            # Extract ZIP and import within same context
            with tempfile.TemporaryDirectory() as tmpdir:
                with zipfile.ZipFile(dataset["ZIP"], 'r') as zf:
                    zf.extractall(tmpdir)
                xml_files = [str(f) for f in Path(tmpdir).rglob("*.xml")]
                result = cimpy.cim_import(xml_files, cgmes_version)
        else:
            # Multiple files dataset
            files = [str(v) for k, v in dataset.items() if k != "_metadata"]
            result = cimpy.cim_import(files, cgmes_version)

        self.topology = result['topology']
        self.meta_info = result['meta_info']

        return self

    def _get_cgmes_version(self, dataset_key: str) -> str:
        """Map dataset to cimpy version string."""
        metadata = DATASETS[dataset_key]["_metadata"]
        cgmes_version = metadata.get("cgmes_version", "3.0")

        if cgmes_version == "3.0":
            return "cgmes_v3_0_0"
        elif cgmes_version.startswith("2.4"):
            return "cgmes_v2_4_15"
        else:
            return "cgmes_v3_0_0"  # Default

    def _count_by_classname(self, classname: str) -> int:
        """Count objects by class name."""
        if self.topology is None:
            raise ValueError("No data loaded")
        return sum(1 for obj in self.topology.values()
                   if obj.__class__.__name__ == classname)

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from cimpy result."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "objects": len(loaded_obj.topology),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments)."""
        return loaded_obj._count_by_classname("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines)."""
        return loaded_obj._count_by_classname("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer)."""
        conform = loaded_obj._count_by_classname("ConformLoad")
        nonconform = loaded_obj._count_by_classname("NonConformLoad")
        energy_consumer = loaded_obj._count_by_classname("EnergyConsumer")
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        return loaded_obj._count_by_classname("Substation")
