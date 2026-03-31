"""PyPowSyBl parser adapter for benchmarking.

pypowsybl is a Python binding for PowSyBl (Power System Blocks),
an open-source framework for power system modeling and analysis.
Repository: https://github.com/powsybl/pypowsybl
Documentation: https://pypowsybl.readthedocs.io/
"""

import tempfile
import zipfile
from pathlib import Path

from parser_adapter import ParserAdapter
from datasets import DATASETS, get_size_mb
import pypowsybl.network as pn


class PypowsyblAdapter(ParserAdapter):
    """Adapter for pypowsybl library."""

    def __init__(self):
        self.network = None

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "PyPowSyBl"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#ff7f0e"  # Tab10 orange

    def load(self, dataset_key: str):
        """Load using pypowsybl."""
        dataset = DATASETS[dataset_key]

        # Determine files and prepare ZIP if needed
        files = [v for k, v in dataset.items() if k != "_metadata"]
        zip_to_load = dataset.get("ZIP")
        temp_dir = None

        if not zip_to_load:
            # Create temp ZIP for multiple files
            temp_dir = tempfile.TemporaryDirectory()
            tmpzip = Path(temp_dir.name) / "dataset.zip"
            zf = zipfile.ZipFile(tmpzip, 'w')
            for f in files:
                zf.write(f, arcname=Path(f).name)
            zf.close()
            zip_to_load = tmpzip

        # Load ZIP
        self.network = pn.load(zip_to_load)

        # Cleanup if temp ZIP was created
        if temp_dir:
            temp_dir.cleanup()

        return self

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from pypowsybl network."""
        network = loaded_obj.network
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "buses": len(network.get_buses()),
            "lines": len(network.get_lines()) + len(network.get_dangling_lines()),
            "ac_lines": len(network.get_lines()),
            "dangling_lines": len(network.get_dangling_lines()),
            "generators": len(network.get_generators()),
            "loads": len(network.get_loads()),
            "substations": len(network.get_substations()),
        }

    def get_lines_count(self, loaded_obj):
        return len(loaded_obj.network.get_lines())

    def get_generators_count(self, loaded_obj):
        return len(loaded_obj.network.get_generators())

    def get_loads_count(self, loaded_obj):
        return len(loaded_obj.network.get_loads())

    def get_substations_count(self, loaded_obj):
        return len(loaded_obj.network.get_substations())

    def export(self, loaded_obj, output_path):
        """Export pypowsybl network to CGMES ZIP format."""
        from pathlib import Path

        if loaded_obj.network is None:
            raise ValueError("No network loaded")

        # Ensure output path is a Path object
        output_path = Path(output_path)

        # Export to CGMES format as ZIP
        # PyPowSyBl exports CGMES as a ZIP file containing multiple XML files
        loaded_obj.network.dump(output_path, format="CGMES")

        return output_path
