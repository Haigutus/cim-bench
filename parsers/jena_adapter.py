"""Apache Jena parser adapter for benchmarking CGMES files.

This adapter uses Apache Jena (Java RDF library) via JPype to parse CGMES/CIMXML files.
Jena provides robust RDF parsing and SPARQL query capabilities.

Apache Jena: https://jena.apache.org/

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
from parser_adapter import IncompleteLoadError, ParserAdapter
from datasets import DATASETS


class JenaAdapter(ParserAdapter):
    """Adapter for Apache Jena library using JPype bridge."""

    _jvm_started = False

    def __init__(self):
        self.models = {}  # Dict of profile -> model
        self.model = None  # Active model for queries (will be EQ)
        self.cim_namespace = None

        # Start JVM if not already started
        if not JenaAdapter._jvm_started:
            classpath = "/app/lib/*"
            jpype.startJVM(classpath=[classpath], convertStrings=False)
            JenaAdapter._jvm_started = True

    @classmethod
    def get_version(cls) -> str:
        if not jpype.isJVMStarted():
            return "unknown"
        from org.apache.jena.rdf.model import ModelFactory
        v = ModelFactory.class_.getPackage().getImplementationVersion()
        return str(v) if v else "unknown"

    @classmethod
    def get_dependencies(cls) -> dict:
        from importlib.metadata import version
        deps = {"jpype1": version("jpype1")}
        if jpype.isJVMStarted():
            deps["java"] = str(jpype.java.lang.System.getProperty("java.version"))
        return deps

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "Apache Jena"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#d62728"  # Red

    @classmethod
    def get_tags(cls):
        return ["parser", "serializer", "query", "sparql", "triplestore", "java"]

    def load(self, dataset_key: str):
        """Load using Apache Jena via JPype."""
        dataset = DATASETS[dataset_key]

        # Import Jena classes (after JVM started)
        from org.apache.jena.rdf.model import ModelFactory
        from java.io import FileInputStream

        # Determine files to load
        files = [Path(v) for k, v in dataset.items() if k != "_metadata"]

        # Extract ZIP if needed
        temp_dir = None
        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            tmp = temp_dir.name
            zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
            files = Path(tmp).rglob("*.xml")

        # Load all files into separate models (lax mode tolerates the datasets'
        # invalid UUIDs); benchmarks require ALL profiles to load
        failed = {}
        for xml_file in files:
            try:
                model = ModelFactory.createDefaultModel()
                reader = model.getReader("RDF/XML")
                reader.setProperty("error-mode", "lax")

                file_input = FileInputStream(str(xml_file))
                file_url = f"file://{str(xml_file)}"
                reader.read(model, file_input, file_url)
                file_input.close()

                self.models[xml_file.stem] = model
            except Exception as e:
                failed[xml_file.stem] = f"{type(e).__name__}: {e}"

        # Cleanup if ZIP was used
        if temp_dir:
            temp_dir.cleanup()

        if failed:
            raise IncompleteLoadError(
                f"Jena loaded {len(self.models)} profiles; failed: {failed}")

        # Select EQ model for queries
        eq_key = next((k for k in self.models.keys() if "EQ" in k), None)
        if eq_key:
            self.model = self.models[eq_key]
        else:
            raise ValueError(f"No EQ profile found in {list(self.models.keys())}")

        # Detect CIM namespace from loaded data
        self._detect_namespace()

        return self

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded RDF model."""
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
            with QueryExecutionFactory.create(query, self.model) as qexec:
                if qexec.execAsk():
                    self.cim_namespace = ns
                    return

        # Default to CIM100 if nothing found
        self.cim_namespace = "http://iec.ch/TC57/CIM100#"

    def _count_instances(self, class_name: str) -> int:
        """Count instances of a CIM class using SPARQL."""
        if not self.model:
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
        with QueryExecutionFactory.create(query, self.model) as qexec:
            results = qexec.execSelect()
            if results.hasNext():
                soln = results.next()
                count_literal = soln.get("count")
                return count_literal.getInt()

        return 0

    def get_load_metrics(self, loaded_obj, memory_mb):
        """Extract metrics from loaded model."""
        # Count triples in model
        triples = 0
        if loaded_obj.model:
            triples = loaded_obj.model.size()

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
        """Export all loaded RDF models to per-profile RDF/XML files."""
        from java.io import FileOutputStream

        if not loaded_obj.models:
            raise ValueError("No data loaded")

        output_path = Path(output_path)
        output_dir = output_path.parent

        # Write each profile to a separate XML file
        for profile_name, model in loaded_obj.models.items():
            profile_path = output_dir / f"{profile_name}.xml"
            fos = FileOutputStream(str(profile_path))
            model.write(fos, "RDF/XML")
            fos.close()

        return output_path

    def cleanup(self):
        """Cleanup resources (shutdown JVM if needed)."""
        # Note: JVM shutdown is optional and typically not done
        # as it cannot be restarted in the same process
        # Let the process exit naturally to clean up JVM
        pass
