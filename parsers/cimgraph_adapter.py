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
        self.connection = None
        self.cim = None
        self.cim_profile = None

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "CIM-Graph"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#9467bd"  # Purple

    def load(self, dataset_key: str):
        """Load using CIM-Graph's RDFlibConnection."""
        dataset = DATASETS[dataset_key]

        # Detect CIM profile and parameters for this dataset
        self.cim_profile = self._get_cim_profile(dataset_key)
        # os.environ['CIMG_VALIDATION_LOG_LEVEL'] = 'DEBUG'
        os.environ['CIMG_CIM_PROFILE'] = self.cim_profile
        os.environ['CIMG_NAMESPACE'] = str(self._get_namespace(dataset_key))
        os.environ['CIMG_IEC61970_301'] = str(self._get_iec_version(dataset_key))
        
        print('DATASET NAME:', dataset)

        if "ZIP" in dataset:
            # Single ZIP file (RealGrid) - extract and load EQ files
            # with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = './tmpdir'
            with zipfile.ZipFile(dataset["ZIP"], 'r') as zf:
                zf.extractall(tmpdir)
                # Parse EQ (Equipment) files only for canonical counts
                eq_files = list(Path(tmpdir).rglob("*_EQ_*.xml"))
                eq_files.extend(Path(tmpdir).rglob("*_EQ.xml"))
                eq_files.extend(Path(tmpdir).rglob("*EQ.xml"))
                
                xml_file_set = eq_files
        else:
            # Multiple files (Svedala) - load EQ file only
            if "EQ" in dataset:
                xml_file_set = [dataset["EQ"]]
            else:
                # Fallback: load all files if no EQ file specified
                files = [v for k, v in dataset.items() if k != "_metadata"]
                xml_file_set = files

        # Load CIM profile module for typed access
        self.cim = importlib.import_module(f'cimgraph.data_profile.{self.cim_profile}')
        
        temp_graph = {} # temp var to merge graphs from multiple XML file
        for filename in xml_file_set: # loop through all files in set
            file = XMLFile(filename) # open xml file
            self.network = NodeBreakerModel(connection=file, container=None, graph = temp_graph)
            temp_graph = self.network.graph # copy graph out of XML file to load into next one

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
            "triples": self.count_triples(),
            "lines": len(self.network.graph[self.cim.ACLineSegment]),
            "generators": len(self.network.graph[self.cim.SynchronousMachine]),
            "loads": len(self.network.graph[self.cim.EnergyConsumer]),
            "substations": len(self.network.graph[self.cim.Substation]),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        return len(self.network.graph[self.cim.ACLineSegment])

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        return len(self.network.graph[self.cim.SynchronousMachine])

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        conform = len(self.network.graph[self.cim.ConformLoad])
        nonconform = len(self.network.graph[self.cim.NonConformLoad])
        energy_consumer = len(self.network.graph[self.cim.EnergyConsumer])
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        return len(self.network.graph[self.cim.Substation])
    

    def count_triples(self):
        thing_count = 0
        for cim_class in self.network.graph:
            attrs = fields(cim_class)
            for obj in self.network.graph[cim_class].values():
                for field in attrs:
                    value = getattr(obj, field.name)
                    if value or value == 0:
                        thing_count +=1
        return thing_count