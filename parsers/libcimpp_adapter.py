from parser_adapter import ParserAdapter
from datasets import DATASETS
from pathlib import Path
import tempfile
import zipfile

# Import C++ module
import _libcimpp_benchmark


class LibCIMppAdapter(ParserAdapter):
    def __init__(self):
        self.benchmark = None

    @classmethod
    def get_display_name(cls):
        return "libcimpp"

    @classmethod
    def get_color(cls):
        return "#000000"  # Black

    def load(self, dataset_key: str):
        """Load CIM dataset."""
        dataset = DATASETS[dataset_key]

        # Collect file paths
        files = [Path(v) for k, v in dataset.items() if "_metadata" not in k.lower()]

        # Handle ZIP extraction
        temp_dir = None
        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            zipfile.ZipFile(dataset["ZIP"]).extractall(temp_dir.name)
            files = list(Path(temp_dir.name).rglob("*.xml"))

        # Load via C++ wrapper
        self.benchmark = _libcimpp_benchmark.LibCIMppBenchmark()
        file_paths = [str(f) for f in files]
        success = self.benchmark.load(file_paths)

        if not success:
            raise RuntimeError("Failed to load CIM files")

        # Cleanup
        if temp_dir:
            temp_dir.cleanup()

        return self

    def get_load_metrics(self, loaded_obj, memory_mb):
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "lines": self.get_lines_count(loaded_obj),
            "generators": self.get_generators_count(loaded_obj),
            "loads": self.get_loads_count(loaded_obj),
            "substations": self.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        return loaded_obj.benchmark.count_acline_segments()

    def get_generators_count(self, loaded_obj):
        return loaded_obj.benchmark.count_synchronous_machines()

    def get_loads_count(self, loaded_obj):
        return loaded_obj.benchmark.count_loads()

    def get_substations_count(self, loaded_obj):
        return loaded_obj.benchmark.count_substations()
