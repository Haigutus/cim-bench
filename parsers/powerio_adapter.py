"""PowerIO parser adapter for benchmarking."""

from importlib.metadata import version
from pathlib import Path
import shutil
import tempfile

import powerio

from datasets import DATASETS
from parser_adapter import ParserAdapter


class PowerIOAdapter(ParserAdapter):
    @classmethod
    def get_version(cls):
        return version("powerio")

    @classmethod
    def get_dependencies(cls):
        return cls._get_package_dependencies("powerio")

    @classmethod
    def get_display_name(cls):
        return "PowerIO"

    @classmethod
    def get_color(cls):
        return "#176b87"

    @classmethod
    def get_tags(cls):
        return ["parser", "serializer", "query", "typed-model", "python", "rust"]

    def load(self, dataset_key):
        dataset = DATASETS[dataset_key]
        source = dataset.get("ZIP")
        temp_dir = None
        if source is None:
            temp_dir = tempfile.TemporaryDirectory()
            source = Path(temp_dir.name)
            for key, path in dataset.items():
                if key != "_metadata":
                    shutil.copyfile(path, source / path.name)

        self.module = powerio.parse(source, format="cgmes")
        self.network = self.module.value
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
        return loaded_obj.network.n_lines

    def get_generators_count(self, loaded_obj):
        return loaded_obj.network.n_generators

    def get_loads_count(self, loaded_obj):
        return loaded_obj.network.n_loads

    def get_substations_count(self, loaded_obj):
        return loaded_obj.network.n_substations

    def export(self, loaded_obj, output_path):
        """Write fresh CGMES profiles alongside the requested output path."""
        output_dir = Path(output_path).parent
        emitted = powerio.emit(loaded_obj.module.sever_source(), "cgmes")
        for artifact in emitted.artifacts:
            (output_dir / Path(artifact.name).name).write_bytes(artifact.data)
        return output_dir
