"""Triplets parser adapter for benchmarking.

Triplets is a Python library for parsing CIM RDF/XML data to pandas DataFrames.
Repository: https://github.com/Haigutus/triplets
Documentation: https://haigutus.github.io/triplets/
"""

import pandas
import triplets  # noqa: F401 - Extends pandas with read_RDF
from parser_adapter import ParserAdapter
from datasets import DATASETS, get_size_mb


class TripletsAdapter(ParserAdapter):
    """Adapter for triplets library."""

    def __init__(self):
        self.df = None

    @classmethod
    def get_version(cls) -> str:
        from importlib.metadata import version
        return version("triplets")

    @classmethod
    def get_dependencies(cls) -> dict:
        return cls._get_package_dependencies("triplets")

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "triplets"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#1f77b4"  # Tab10 blue

    @classmethod
    def get_tags(cls):
        return ["parser", "serializer", "query", "python"]

    def load(self, dataset_key: str):
        """Load using triplets library directly."""
        dataset = DATASETS[dataset_key]

        # Determine files to load
        files_to_load = [v for k, v in dataset.items() if k != "_metadata"]
        if "ZIP" in dataset:
            files_to_load = dataset["ZIP"]

        # Load all files (single call regardless of format)
        self.df = pandas.read_RDF(files_to_load)

        return self

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from triplets dataframe."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triplets_count": len(loaded_obj.df),
            "unique_objects": loaded_obj.df['ID'].nunique(),
            "instances": loaded_obj.df['INSTANCE_ID'].nunique(),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")
        table = loaded_obj.df.type_tableview("ACLineSegment", string_to_number=False)
        return len(table) if table is not None else 0

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")
        table = loaded_obj.df.type_tableview("SynchronousMachine", string_to_number=False)
        return len(table) if table is not None else 0

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")

        conform_table = loaded_obj.df.type_tableview("ConformLoad", string_to_number=False)
        nonconform_table = loaded_obj.df.type_tableview("NonConformLoad", string_to_number=False)
        energy_consumer_table = loaded_obj.df.type_tableview("EnergyConsumer", string_to_number=False)

        conform = len(conform_table) if conform_table is not None else 0
        nonconform = len(nonconform_table) if nonconform_table is not None else 0
        energy_consumer = len(energy_consumer_table) if energy_consumer_table is not None else 0

        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        if loaded_obj.df is None:
            raise ValueError("No data loaded")
        table = loaded_obj.df.type_tableview("Substation", string_to_number=False)
        return len(table) if table is not None else 0

    def export(self, loaded_obj, output_path):
        """Export triplets dataframe to RDF/XML."""
        from pathlib import Path
        from triplets.export_schema import schemas
        from triplets.rdf_parser import ExportType

        if loaded_obj.df is None:
            raise ValueError("No data loaded")

        output_path = Path(output_path)
        output_dir = output_path.parent

        # Export per instance (creates separate ZIP files in output_dir)
        loaded_obj.df.export_to_cimxml(
            rdf_map=schemas.ENTSOE_CGMES_3_0_0_552_ED1,
            export_type=ExportType.XML_PER_INSTANCE_ZIP_PER_XML,
            export_base_path=str(output_dir),
            max_workers=4
        )

        return output_dir
