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
    def get_version(cls) -> str:
        if not jpype.isJVMStarted():
            return "unknown"
        from de.soptim.opencgmes.cimxml.parser import CimXmlParser
        v = CimXmlParser.class_.getPackage().getImplementationVersion()
        if v:
            return str(v)
        # Fallback: parse version from JAR filename (SNAPSHOT builds lack manifest version)
        import re
        from java.lang import Thread
        url = str(Thread.currentThread().getContextClassLoader()
                  .getResource("de/soptim/opencgmes/cimxml/parser/CimXmlParser.class"))
        if (m := re.search(r"cimxml-([\d.]+[^/]*?)\.jar", url)):
            return m.group(1)
        return "unknown"

    @classmethod
    def get_dependencies(cls) -> dict:
        from importlib.metadata import version
        deps = {"jpype1": version("jpype1")}
        if jpype.isJVMStarted():
            deps["java"] = str(jpype.java.lang.System.getProperty("java.version"))
            from org.apache.jena.rdf.model import ModelFactory
            v = ModelFactory.class_.getPackage().getImplementationVersion()
            if v:
                deps["jena"] = str(v)
        return deps

    @classmethod
    def get_display_name(cls) -> str:
        """Get the display name for this parser."""
        return "OpenCGMES"

    @classmethod
    def get_color(cls) -> str:
        """Get the color hex code for graph visualization."""
        return "#e91e63"  # Pink

    @classmethod
    def get_tags(cls):
        return ["parser", "serializer", "query", "sparql", "triplestore", "java"]

    def load(self, dataset_key: str):
        """Load using OpenCGMES Java library via JPype."""
        dataset = DATASETS[dataset_key]

        # Import Java classes (after JVM started)
        from de.soptim.opencgmes.cimxml.parser import CimXmlParser
        from java.nio.file import Paths

        parser = CimXmlParser()

        # Determine files to load
        files = [(k, Path(v)) for k, v in dataset.items() if k != "_metadata"]

        # Extract ZIP if needed
        temp_dir = None
        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            tmp = temp_dir.name
            zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
            files = [(f.stem, f) for f in Path(tmp).rglob("*.xml")]

        # Load all files into separate profile datasets
        for profile_name, file_path in files:
            java_path = Paths.get(str(file_path))
            self.all_profiles[profile_name] = parser.parseCimModel(java_path)

        # Cleanup if ZIP was used
        if temp_dir:
            temp_dir.cleanup()

        # Select EQ dataset for queries
        eq_key = next((k for k in self.all_profiles.keys() if "EQ" in k), None)
        if eq_key:
            self.dataset = self.all_profiles[eq_key]
        else:
            raise ValueError(f"No EQ profile found in {list(self.all_profiles.keys())}")

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

    def export(self, loaded_obj, output_path):
        """Export all loaded RDF datasets to per-profile RDF/XML files."""
        from java.io import FileOutputStream
        from org.apache.jena.rdf.model import ModelFactory

        if not loaded_obj.all_profiles:
            raise ValueError("No data loaded")

        output_path = Path(output_path)
        output_dir = output_path.parent

        # Write each profile to a separate XML file
        for profile_name, dataset in loaded_obj.all_profiles.items():
            profile_path = output_dir / f"{profile_name}.xml"
            graph = dataset.getDefaultGraph()
            model = ModelFactory.createModelForGraph(graph)
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
