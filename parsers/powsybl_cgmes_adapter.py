"""PowSyBL CGMES Model adapter for benchmarking CGMES files.

PowSyBL is a Java framework for power system analysis with a dedicated
CGMES model component that loads CIM/XML into an RDF4J in-memory triplestore.
Repository: https://github.com/powsybl/powsybl-core

This adapter uses JPype to bridge Python and Java (JNI), allowing direct
Java method calls from Python while maintaining single-process execution
for accurate memory measurement via psutil.
"""

import tempfile
import zipfile
from pathlib import Path
import jpype
import jpype.imports
from jpype.types import *
from parser_adapter import ParserAdapter
from datasets import DATASETS


class PowsyblCgmesAdapter(ParserAdapter):
    """Adapter for PowSyBL CGMES Model library using JPype bridge."""

    _jvm_started = False

    def __init__(self):
        self.model = None
        self.triplestore = None
        self.cim_namespace = None

        # Start JVM if not already started
        if not PowsyblCgmesAdapter._jvm_started:
            classpath = "/app/lib/*"
            jpype.startJVM(classpath=[classpath], convertStrings=False)
            PowsyblCgmesAdapter._jvm_started = True

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "PowSyBL CGMES"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#8c564b"  # Brown

    def load(self, dataset_key: str):
        """Load using PowSyBL CGMES Model library via JPype."""
        dataset = DATASETS[dataset_key]

        # Import Java classes (after JVM started)
        from com.powsybl.cgmes.model import CgmesModelFactory
        from com.powsybl.commons.datasource import ZipArchiveDataSource
        from java.nio.file import Paths

        if "ZIP" in dataset:
            # Single ZIP file (RealGrid)
            java_path = Paths.get(str(dataset["ZIP"]))
            datasource = ZipArchiveDataSource(java_path)
            self.model = CgmesModelFactory.create(datasource)
        else:
            # Multiple files (Svedala) - create temp ZIP with ALL files like PyPowSyBL
            with tempfile.TemporaryDirectory() as tmpdir:
                tmpzip = Path(tmpdir) / "svedala_all.zip"
                files = [v for k, v in dataset.items() if k != "_metadata"]
                with zipfile.ZipFile(tmpzip, 'w', zipfile.ZIP_DEFLATED) as zf:
                    for file_path in files:
                        zf.write(file_path, Path(file_path).name)

                java_path = Paths.get(str(tmpzip))
                datasource = ZipArchiveDataSource(java_path)
                self.model = CgmesModelFactory.create(datasource)
                # Keep triplestore reference before tmpdir is deleted
                self.triplestore = self.model.tripleStore()
                return self

        # Get underlying triplestore for SPARQL queries
        self.triplestore = self.model.tripleStore()

        # Detect CIM namespace from loaded data
        self._detect_namespace()

        return self

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded RDF dataset."""
        namespaces = [
            "http://iec.ch/TC57/CIM100#",  # CGMES 3.0
            "http://iec.ch/TC57/2013/CIM-schema-cim16#",  # CGMES 2.4.15
        ]

        for ns in namespaces:
            test_query = f'''
            SELECT ?s
            WHERE {{
                ?s a <{ns}ACLineSegment> .
            }}
            LIMIT 1
            '''
            result = self.triplestore.query(test_query)
            # PropertyBags returns results - check if any found
            if result and len(result) > 0:
                self.cim_namespace = ns
                return

        # Default to CIM100 if nothing found
        self.cim_namespace = "http://iec.ch/TC57/CIM100#"

    def _count_instances(self, class_name: str) -> int:
        """Count instances of a CIM class using SPARQL."""
        if not self.triplestore:
            raise ValueError("No data loaded")

        if not self.cim_namespace:
            self._detect_namespace()

        query_string = f'''
        SELECT (COUNT(DISTINCT ?s) as ?count)
        WHERE {{
            ?s a <{self.cim_namespace}{class_name}> .
        }}
        '''

        result = self.triplestore.query(query_string)
        if result and len(result) > 0:
            # PropertyBags returns results as a list of PropertyBag objects
            # Each PropertyBag has a get(String) method
            count_value = result.get(0).get("count")
            return int(str(count_value))

        return 0

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from loaded dataset."""
        # Count triples in triplestore - use SPARQL COUNT query
        triples = 0
        if loaded_obj.triplestore:
            query_string = '''
            SELECT (COUNT(*) as ?count)
            WHERE {
                ?s ?p ?o .
            }
            '''
            result = loaded_obj.triplestore.query(query_string)
            if result and len(result) > 0:
                count_value = result.get(0).get("count")
                triples = int(str(count_value))

        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triples": triples,
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines (ACLineSegments) in the network."""
        if loaded_obj.triplestore is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        if loaded_obj.triplestore is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        if loaded_obj.triplestore is None:
            raise ValueError("No data loaded")
        conform = loaded_obj._count_instances("ConformLoad")
        nonconform = loaded_obj._count_instances("NonConformLoad")
        energy_consumer = loaded_obj._count_instances("EnergyConsumer")
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        if loaded_obj.triplestore is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("Substation")

    def cleanup(self):
        """Cleanup resources (shutdown JVM if needed)."""
        # Note: JVM shutdown is optional and typically not done
        # as it cannot be restarted in the same process
        # Let the process exit naturally to clean up JVM
        pass
