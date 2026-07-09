"""CIM-Graph parser adapter for benchmarking.

CIM-Graph (CIMantic Graphs) is a Python library for creating in-memory
knowledge graphs for CIM power system models with typed CIM objects.
Repository: https://github.com/PNNL-CIM-Tools/CIM-Graph
Documentation: https://github.com/PNNL-CIM-Tools/CIM-Documentation
"""
import os
import importlib
import tempfile
import zipfile
from pathlib import Path
from dataclasses import fields

from cimgraph.databases import XMLFile
from cimgraph.models import NodeBreakerModel
from parser_adapter import ParserAdapter
from datasets import DATASETS


class CIMGraphAdapter(ParserAdapter):
    """Adapter for CIM-Graph library using RDFlibConnection."""

    def __init__(self):
        self.models = {}
        self.network = None
        self.cim = None
        self.cim_profile = None

    @classmethod
    def get_version(cls) -> str:
        from importlib.metadata import version
        return version("cim-graph")

    @classmethod
    def get_dependencies(cls) -> dict:
        return cls._get_package_dependencies("cim-graph")

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "CIM-Graph"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#9467bd"  # Purple

    @classmethod
    def get_tags(cls):
        return ["parser", "query", "typed-model", "triplestore", "python"]

    def load(self, dataset_key: str):
        """Load using CIM-Graph's NodeBreakerModel.

        CIMGraph loads each profile separately. We load all files to measure
        real-world performance, but use only the EQ profile for queries.
        """
        dataset = DATASETS[dataset_key]

        # Detect CIM profile and parameters for this dataset
        self.cim_profile = self._get_cim_profile(dataset_key)
        os.environ['CIMG_CIM_PROFILE'] = self.cim_profile
        os.environ['CIMG_NAMESPACE'] = str(self._get_namespace(dataset_key))
        os.environ['CIMG_IEC61970_301'] = str(self._get_iec_version(dataset_key))

        # Determine files to load (keep profile names for EQ selection)
        files = [(k, Path(v)) for k, v in dataset.items() if k != "_metadata"]

        # Extract ZIP if needed
        temp_dir = None
        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            tmp = temp_dir.name
            zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
            files = [(f.stem, f) for f in Path(tmp).rglob("*.xml")]

        # Load CIM profile module for typed access
        self.cim = importlib.import_module(f'cimgraph.data_profile.{self.cim_profile}')

        # Sort files to load EQ first (required for cross-references)
        eq_files = [(name, path) for name, path in files if "EQ" in name.upper()]
        other_files = [(name, path) for name, path in files if "EQ" not in name.upper()]
        sorted_files = eq_files + other_files

        # Load all files, accumulating into a shared graph
        temp_graph = {}
        for profile_name, filename in sorted_files:
            try:
                xml_file = XMLFile(filename)
                model = NodeBreakerModel(connection=xml_file, container=None, graph=temp_graph)
                self.models[profile_name] = model
                temp_graph = model.graph  # Accumulate for next file
            except Exception as e:
                # Some profiles may fail if they reference missing equipment
                # This is expected for datasets with incomplete profiles
                pass

        # Use the accumulated network (EQ profile with merged data)
        if self.models:
            # Prefer EQ model if available
            eq_key = next((k for k in self.models.keys() if "EQ" in k.upper()), None)
            self.network = self.models[eq_key] if eq_key else list(self.models.values())[0]
        else:
            raise ValueError("No models could be loaded")

        # Cleanup if ZIP was used
        if temp_dir:
            temp_dir.cleanup()

        return self

    def _get_cim_profile(self, dataset_key: str) -> str:
        """Map dataset to CIM profile."""
        metadata = DATASETS[dataset_key]["_metadata"]
        cgmes_version = metadata.get("cgmes_version", "3.0")

        if cgmes_version == "3.0":
            return "cim17v40"  # CGMES 3.0 → cim17v40 profile
        elif cgmes_version.startswith("2.4"):
            return "cim16v33"  # CGMES 2.4 → cim16v33 profile
        else:
            return "rc4_2021"  # Default

    def _get_namespace(self, dataset_key: str) -> str:
        """Get CIM namespace for dataset."""
        metadata = DATASETS[dataset_key]["_metadata"]
        cgmes_version = metadata.get("cgmes_version", "3.0")

        if cgmes_version == "3.0":
            return "http://iec.ch/TC57/CIM100#"
        elif cgmes_version.startswith("2.4"):
            return "http://iec.ch/TC57/2013/CIM-schema-cim16#"
        else:
            return "http://iec.ch/TC57/CIM100#"

    def _get_iec_version(self, dataset_key: str) -> int:
        """Get IEC 61970-301 version."""
        metadata = DATASETS[dataset_key]["_metadata"]
        cgmes_version = metadata.get("cgmes_version", "3.0")

        return 8 if cgmes_version == "3.0" else 6

    def _count_instances(self, class_name: str) -> int:
        """Count instances using CIM-Graph's RDFlibConnection."""
        count = 0
        for cim_class in self.network.graph:
            count += len(self.network.graph[cim_class])
        return count

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from CIM-Graph connection."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triples": loaded_obj.count_triples(),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        return len(loaded_obj.network.graph.get(loaded_obj.cim.ACLineSegment, {}))

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        return len(loaded_obj.network.graph.get(loaded_obj.cim.SynchronousMachine, {}))

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        conform = len(loaded_obj.network.graph.get(loaded_obj.cim.ConformLoad, {}))
        nonconform = len(loaded_obj.network.graph.get(loaded_obj.cim.NonConformLoad, {}))
        energy_consumer = len(loaded_obj.network.graph.get(loaded_obj.cim.EnergyConsumer, {}))
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        return len(loaded_obj.network.graph.get(loaded_obj.cim.Substation, {}))
    

    def export(self, loaded_obj, output_path):
        """Export CIM-Graph network to XML."""
        from cimgraph.utils import write_xml

        # write_xml defaults to CIM100 namespaces; override 'cim' with the
        # namespace the loaded profile actually uses (e.g. cim16 for CGMES 2.4)
        cim_ns = next(f.metadata["namespace"]
                      for f in fields(loaded_obj.cim.IdentifiedObject)
                      if f.metadata.get("namespace"))

        output_path = Path(output_path)
        write_xml(loaded_obj.network, str(output_path), namespaces={"cim": cim_ns})
        return output_path

    def count_triples(self):
        """Count triples across all loaded models."""
        thing_count = 0
        for model in self.models.values():
            for cim_class in model.graph:
                attrs = fields(cim_class)
                for obj in model.graph[cim_class].values():
                    for field in attrs:
                        value = getattr(obj, field.name)
                        if value or value == 0:
                            thing_count += 1
        return thing_count