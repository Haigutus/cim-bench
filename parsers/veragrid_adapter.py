"""VeraGrid parser adapter for benchmarking.

VeraGrid is a Python library for power systems analysis and grid modeling.
Repository: https://github.com/SanPen/GridCal
"""

from parser_adapter import ParserAdapter
from datasets import DATASETS


class VeragridAdapter(ParserAdapter):
    """Adapter for VeraGrid library using low-level CGMES API."""

    def __init__(self):
        self.cgmes_circuit = None

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "VeraGrid"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#2ca02c"  # Tab10 green

    def load(self, dataset_key: str):
        """Load using VeraGrid's low-level CGMES API."""
        import VeraGridEngine as gce

        dataset = DATASETS[dataset_key]

        # Collect file paths (handles both ZIP and multiple XML files)
        files = [v for k, v in dataset.items() if k != "_metadata"]
        if "ZIP" in dataset:
            files = [dataset["ZIP"]]

        # Parse using low-level CGMES API
        logger = gce.Logger()
        data_parser = gce.CgmesDataParser()
        data_parser.load_files(files=files)

        self.cgmes_circuit = gce.CgmesCircuit(
            cgmes_version=data_parser.cgmes_version,
            cgmes_map_areas_like_raw=False,
            logger=logger
        )
        self.cgmes_circuit.parse_files(data_parser=data_parser)

        return self

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from VeraGrid CGMES circuit."""
        cgmes_circuit = loaded_obj.cgmes_circuit
        assets = cgmes_circuit.cgmes_assets

        return {
            "memory_mb": f"{memory_mb:.1f}",
            "lines": self.get_lines_count(loaded_obj),
            "generators": self.get_generators_count(loaded_obj),
            "loads": self.get_loads_count(loaded_obj),
            "substations": self.get_substations_count(loaded_obj),
            "cgmes_version": cgmes_circuit.cgmes_version,
        }

    def get_lines_count(self, loaded_obj):
        """Count ACLineSegments."""
        return len(loaded_obj.cgmes_circuit.cgmes_assets.ACLineSegment_list)

    def get_generators_count(self, loaded_obj):
        """Count SynchronousMachines."""
        return len(loaded_obj.cgmes_circuit.cgmes_assets.SynchronousMachine_list)

    def get_loads_count(self, loaded_obj):
        """Count all load types (ConformLoad + NonConformLoad + EnergyConsumer)."""
        assets = loaded_obj.cgmes_circuit.cgmes_assets
        return (
            len(assets.ConformLoad_list) +
            len(assets.NonConformLoad_list) +
            len(assets.EnergyConsumer_list)
        )

    def get_substations_count(self, loaded_obj):
        """Count Substations."""
        return len(loaded_obj.cgmes_circuit.cgmes_assets.Substation_list)
