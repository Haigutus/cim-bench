"""PowerIO parser adapter for benchmarking."""

from importlib.metadata import version
from pathlib import Path
import shutil
import tempfile
from collections import Counter
from types import SimpleNamespace

import powerio

from datasets import DATASETS
from parser_adapter import IncompleteLoadError, ParserAdapter


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

    @classmethod
    def get_measurement_notes(cls):
        return {
            "query_family": "native_component_count",
            "count_semantics": {
                "lines": "native lines; transformers are separate",
                "generators": "native generators",
                "loads": "native loads, including equivalent injections",
                "substations": "retained source substations, including boundary records",
            },
            "export_method": "source_retention_removal_then_canonical_CGMES_3_filesystem_write",
            "source_replay": False,
            "native_versions": powerio.versions(),
        }

    def load(self, dataset_key):
        dataset = DATASETS[dataset_key]
        inputs = [(key, Path(path)) for key, path in dataset.items() if not key.startswith("_")]
        missing = [key for key, path in inputs if not path.is_file()]
        if missing or not inputs:
            raise IncompleteLoadError(f"missing registered inputs: {', '.join(missing) or 'all'}")
        source = dataset.get("ZIP")
        temp_dir = None
        try:
            if source is None:
                if len({path.name for _, path in inputs}) != len(inputs):
                    raise IncompleteLoadError("registered inputs have colliding filenames")
                temp_dir = tempfile.TemporaryDirectory()
                source = Path(temp_dir.name)
                for _, path in inputs:
                    shutil.copyfile(path, source / path.name)
            elif len(inputs) != 1:
                raise IncompleteLoadError("ZIP inputs with external companions need an explicit merged dataset")
            module = powerio.parse(source, format="cgmes")
            # The returned value owns its native handles. The reusable adapter
            # does not retain an earlier load during the next timed parse.
            return SimpleNamespace(module=module, network=module.value)
        finally:
            if temp_dir:
                temp_dir.cleanup()

    def get_load_metrics(self, loaded_obj, memory_mb):
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "lines": self.get_lines_count(loaded_obj),
            "generators": self.get_generators_count(loaded_obj),
            "loads": self.get_loads_count(loaded_obj),
            "substations": self.get_substations_count(loaded_obj),
            "read_diagnostic_counts": dict(sorted(Counter(d.code for d in loaded_obj.module.diagnostics).items())),
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
        """Time source removal, fresh CGMES emission and the native file writer."""
        output_dir = Path(output_path).parent / "profiles"
        emitted = powerio.emit(loaded_obj.module.sever_source(), "cgmes", output_dir)
        loaded_obj.export_diagnostics = emitted.diagnostics
        return output_dir

    def get_export_metrics(self, loaded_obj, output_path):
        """Untimed self-consistency check; this is not independent validation."""
        output_dir = Path(output_path).parent / "profiles"
        reread = powerio.parse(output_dir, format="cgmes").value
        before = {name: getattr(loaded_obj.network, f"n_{name}")
                  for name in ("lines", "generators", "loads", "substations")}
        after = {name: getattr(reread, f"n_{name}") for name in before}
        assert before == after, {"before": before, "after": after}
        return {
            "fresh_export_reparse_counts": after,
            "export_diagnostic_counts": dict(sorted(Counter(d.code for d in loaded_obj.export_diagnostics).items())),
            "independent_consumer": "not_run_by_this_benchmark",
        }
