"""maplib parser adapter for benchmarking.

maplib is a high-performance RDF knowledge graph library with Rust backend.
Provides SPARQL querying and returns results as Polars DataFrames.
Repository: https://github.com/DataTreehouse/maplib
Documentation: https://datatreehouse.github.io/documentation/
"""

import tempfile
import zipfile
from pathlib import Path
from parser_adapter import ParserAdapter
from datasets import DATASETS

try:
    from maplib import Model
except ImportError:
    raise ImportError("maplib is not installed. Install with: pip install maplib")


class MaplibAdapter(ParserAdapter):
    """Adapter for maplib library with Rust backend."""

    def __init__(self):
        self.model = None
        self.cim_namespace = None  # Will be detected from loaded data

    @classmethod
    def get_version(cls) -> str:
        from importlib.metadata import version
        return version("maplib")

    @classmethod
    def get_dependencies(cls) -> dict:
        return cls._get_package_dependencies("maplib")

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "maplib"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#8b4513"  # Saddle brown (Rust color)

    @classmethod
    def get_tags(cls):
        return ["parser", "serializer", "query", "triplestore", "python", "rust"]

    def load(self, dataset_key: str):
        """Load CIM dataset into maplib Model."""
        dataset = DATASETS[dataset_key]

        # Create model instance
        self.model = Model()

        # Determine files to load
        files = (v for k, v in dataset.items() if k != "_metadata")

        # Extract ZIP if needed
        temp_dir = None
        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            tmp = temp_dir.name
            zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
            files = Path(tmp).rglob("*.xml")

        # Load all files (same logic for ZIP and non-ZIP)
        # Note: base_iri required for relative IRIs in CGMES files
        for f in files:
            self.model.read(str(f), base_iri="http://example.org/")

        # Cleanup if ZIP was used
        if temp_dir:
            temp_dir.cleanup()

        # Detect CIM namespace from loaded data
        self._detect_namespace()

        return self

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded RDF graph."""
        # Try common CIM namespaces
        namespaces = [
            "http://iec.ch/TC57/CIM100#",  # CGMES 3.0
            "http://iec.ch/TC57/2013/CIM-schema-cim16#",  # CGMES 2.4.15
        ]

        # Query to find which namespace is used
        for ns in namespaces:
            test_query = f'''
            SELECT (COUNT(*) as ?count)
            WHERE {{
                ?s a <{ns}ACLineSegment> .
            }}
            '''
            result = self.model.query(test_query)
            # maplib returns a Polars DataFrame
            if result is not None and len(result) > 0 and result['count'][0] > 0:
                self.cim_namespace = ns
                return

        # Default to CIM100 if nothing found
        self.cim_namespace = "http://iec.ch/TC57/CIM100#"

    def _count_instances(self, class_name: str) -> int:
        """Count instances of a CIM class using SPARQL."""
        if not self.cim_namespace:
            self._detect_namespace()

        query = f'''
        SELECT (COUNT(DISTINCT ?s) as ?count)
        WHERE {{
            ?s a <{self.cim_namespace}{class_name}> .
        }}
        '''
        result = self.model.query(query)
        # maplib returns Polars DataFrame
        if result is not None and len(result) > 0:
            return int(result['count'][0])
        return 0

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from maplib mapping."""
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        if loaded_obj.model is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        if loaded_obj.model is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        if loaded_obj.model is None:
            raise ValueError("No data loaded")
        conform = loaded_obj._count_instances("ConformLoad")
        nonconform = loaded_obj._count_instances("NonConformLoad")
        energy_consumer = loaded_obj._count_instances("EnergyConsumer")
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        if loaded_obj.model is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("Substation")

    def export(self, loaded_obj, output_path):
        """Export maplib model to RDF/XML format."""
        from pathlib import Path

        if loaded_obj.model is None:
            raise ValueError("No data loaded")

        # Ensure output path is a Path object
        output_path = Path(output_path)

        # Export to RDF/XML format (default is nquads without format param)
        loaded_obj.model.write(str(output_path), format="rdf/xml")

        return output_path
