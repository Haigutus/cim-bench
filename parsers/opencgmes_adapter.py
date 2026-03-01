"""OpenCGMES parser adapter for benchmarking CGMES files.

OpenCGMES is a Java-based CGMES parser optimized for large files.
Repository: https://github.com/SOPTIM/OpenCGMES

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


class OpenCGMESAdapter(ParserAdapter):
    """Adapter for OpenCGMES library using JPype bridge."""

    _jvm_started = False

    def __init__(self):
        self.dataset = None
        self.cim_namespace = None
        self.all_profiles = {}  # Dict to store all loaded profile datasets

        # Start JVM if not already started
        if not OpenCGMESAdapter._jvm_started:
            classpath = "/app/lib/*"
            jpype.startJVM(classpath=[classpath], convertStrings=False)
            OpenCGMESAdapter._jvm_started = True

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "OpenCGMES"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#e91e63"  # Pink

    def load(self, dataset_key: str):
        """Load using OpenCGMES Java library via JPype."""
        dataset = DATASETS[dataset_key]

        # Import Java classes (after JVM started)
        from de.soptim.opencgmes.cimxml.parser import CimXmlParser
        from java.nio.file import Paths

        parser = CimXmlParser()

        # OpenCGMES parseCimModel() only loads individual XML files
        # Load ALL files to demonstrate loading capability
        if "ZIP" in dataset:
            # Single ZIP file (RealGrid) - extract and load each file individually
            with tempfile.TemporaryDirectory() as tmpdir:
                with zipfile.ZipFile(dataset["ZIP"], 'r') as zf:
                    zf.extractall(tmpdir)
                    xml_files = list(Path(tmpdir).rglob("*.xml"))

                    for xml_file in xml_files:
                        profile_name = xml_file.stem  # Use filename as profile name
                        java_path = Paths.get(str(xml_file))
                        self.all_profiles[profile_name] = parser.parseCimModel(java_path)

                    # Use first EQ file for queries
                    eq_profiles = [k for k in self.all_profiles.keys() if "_EQ" in k]
                    if eq_profiles:
                        self.dataset = self.all_profiles[eq_profiles[0]]
        else:
            # Multiple files (Svedala) - load each file individually
            for profile_name, file_path in dataset.items():
                if profile_name == "_metadata":
                    continue
                java_path = Paths.get(str(file_path))
                self.all_profiles[profile_name] = parser.parseCimModel(java_path)

            # Use EQ dataset for queries (main equipment data)
            if "EQ" in self.all_profiles:
                self.dataset = self.all_profiles["EQ"]

        # Detect CIM namespace from loaded data
        self._detect_namespace()

        return self

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded RDF dataset."""
        namespaces = [
            "http://iec.ch/TC57/CIM100#",  # CGMES 3.0
            "http://iec.ch/TC57/2013/CIM-schema-cim16#",  # CGMES 2.4.15
        ]

        # Import Jena query classes
        from org.apache.jena.query import QueryFactory, QueryExecutionFactory

        for ns in namespaces:
            test_query = f'''
            ASK {{
                ?s a <{ns}ACLineSegment> .
            }}
            '''
            query = QueryFactory.create(test_query)
            with QueryExecutionFactory.create(query, self.dataset) as qexec:
                if qexec.execAsk():
                    self.cim_namespace = ns
                    return

        # Default to CIM100 if nothing found
        self.cim_namespace = "http://iec.ch/TC57/CIM100#"

    def _count_instances(self, class_name: str) -> int:
        """Count instances of a CIM class using SPARQL."""
        if not self.dataset:
            raise ValueError("No data loaded")

        if not self.cim_namespace:
            self._detect_namespace()

        # Import Jena query classes
        from org.apache.jena.query import QueryFactory, QueryExecutionFactory

        query_string = f'''
        SELECT (COUNT(DISTINCT ?s) as ?count)
        WHERE {{
            ?s a <{self.cim_namespace}{class_name}> .
        }}
        '''

        query = QueryFactory.create(query_string)
        with QueryExecutionFactory.create(query, self.dataset) as qexec:
            results = qexec.execSelect()
            if results.hasNext():
                soln = results.next()
                count_literal = soln.get("count")
                return count_literal.getInt()

        return 0

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from loaded dataset."""
        # Count triples in dataset
        triples = 0
        if loaded_obj.dataset:
            # Get the default graph and count triples
            # OpenCGMES uses getDefaultGraph() which returns a Graph object
            graph = loaded_obj.dataset.getDefaultGraph()
            triples = graph.size()

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
        if loaded_obj.dataset is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        """Get all generators (SynchronousMachines) in the network."""
        if loaded_obj.dataset is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        """Get all loads (ConformLoad + NonConformLoad + EnergyConsumer) in the network."""
        if loaded_obj.dataset is None:
            raise ValueError("No data loaded")
        conform = loaded_obj._count_instances("ConformLoad")
        nonconform = loaded_obj._count_instances("NonConformLoad")
        energy_consumer = loaded_obj._count_instances("EnergyConsumer")
        return conform + nonconform + energy_consumer

    def get_substations_count(self, loaded_obj):
        """Get all substations in the network."""
        if loaded_obj.dataset is None:
            raise ValueError("No data loaded")
        return loaded_obj._count_instances("Substation")

    def cleanup(self):
        """Cleanup resources (shutdown JVM if needed)."""
        # Note: JVM shutdown is optional and typically not done
        # as it cannot be restarted in the same process
        # Let the process exit naturally to clean up JVM
        pass
