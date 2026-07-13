"""Ontotext GraphDB parser adapter for benchmarking CGMES files.

GraphDB is an enterprise RDF database. This adapter embeds it in-process via
the graphdb-runtime library and the RDF4J API (no server). GraphDB 10.8.x is
the last series whose runtime jar bundles a free GRAPHDB_LITE license
(licensed for 1 CPU core); 11.x refuses all operations without a purchased
license, even in the official server image. Ruleset "empty" disables
inference so load times measure parsing+indexing only.
Documentation: https://graphdb.ontotext.com/documentation/

This adapter uses JPype to bridge Python and Java (JNI), allowing direct
Java method calls from Python while maintaining single-process execution
for accurate memory measurement via psutil.

Note: unlike the in-memory competitors, GraphDB is a persistent store -
load times include writing its storage folder to disk.
"""

import glob
import re
import tempfile
import zipfile
from pathlib import Path
import jpype
import jpype.imports
from jpype.types import *
from parser_adapter import ParserAdapter
from datasets import DATASETS

REPO_ID = "cim-bench"

REPO_CONFIG_TTL = """
@prefix rep: <http://www.openrdf.org/config/repository#> .
@prefix sr: <http://www.openrdf.org/config/repository/sail#> .
@prefix sail: <http://www.openrdf.org/config/sail#> .
@prefix graphdb: <http://www.ontotext.com/config/graphdb#> .

[] a rep:Repository ;
    rep:repositoryID "cim-bench" ;
    rep:repositoryImpl [
        rep:repositoryType "graphdb:SailRepository" ;
        sr:sailImpl [
            sail:sailType "graphdb:Sail" ;
            graphdb:ruleset "empty"
        ]
    ] .
"""


class GraphDBAdapter(ParserAdapter):
    """Adapter for embedded Ontotext GraphDB using JPype bridge."""

    _jvm_started = False

    def __init__(self):
        self.manager = None
        self.connection = None
        self.work_dir = None
        self.cim_namespace = None

        # Start JVM if not already started
        if not GraphDBAdapter._jvm_started:
            classpath = "/app/lib/*"
            # Quiet logback's DEBUG default (it dumps the license on every load)
            jvm_args = (["-Dlogback.configurationFile=/app/logback.xml"]
                        if Path("/app/logback.xml").exists() else [])
            jpype.startJVM(*jvm_args, classpath=[classpath], convertStrings=False)
            GraphDBAdapter._jvm_started = True

    @classmethod
    def get_version(cls) -> str:
        jars = glob.glob("/app/lib/graphdb-runtime-*.jar")
        if jars and (m := re.search(r"graphdb-runtime-(.+)\.jar", jars[0])):
            return m.group(1)
        return "unknown"

    @classmethod
    def get_dependencies(cls) -> dict:
        from importlib.metadata import version
        deps = {"jpype1": version("jpype1")}
        if jpype.isJVMStarted():
            deps["java"] = str(jpype.java.lang.System.getProperty("java.version"))
        return deps

    @classmethod
    def get_display_name(cls) -> str:
        return "GraphDB"

    @classmethod
    def get_color(cls) -> str:
        return "#2c3e50"  # Navy

    @classmethod
    def get_tags(cls):
        return ["parser", "serializer", "query", "sparql", "triplestore", "java"]

    def _create_repository(self):
        """Create a fresh embedded GraphDB repository in a temp directory."""
        from org.eclipse.rdf4j.repository.manager import LocalRepositoryManager
        from org.eclipse.rdf4j.repository.config import RepositoryConfig, RepositoryConfigSchema
        from org.eclipse.rdf4j.rio import Rio, RDFFormat
        from org.eclipse.rdf4j.model.util import Models
        from java.io import File, StringReader

        self._teardown()
        self.work_dir = tempfile.TemporaryDirectory()

        self.manager = LocalRepositoryManager(File(self.work_dir.name))
        self.manager.init()

        model = Rio.parse(StringReader(REPO_CONFIG_TTL), "", RDFFormat.TURTLE)
        repo_node = Models.subject(
            model.filter(None, RepositoryConfigSchema.REPOSITORYID, None)).get()
        self.manager.addRepositoryConfig(RepositoryConfig.create(model, repo_node))

        self.connection = self.manager.getRepository(REPO_ID).getConnection()

    def _teardown(self):
        """Close connection/manager and remove the storage directory."""
        if self.connection:
            self.connection.close()
            self.connection = None
        if self.manager:
            self.manager.shutDown()
            self.manager = None
        if self.work_dir:
            self.work_dir.cleanup()
            self.work_dir = None

    def cleanup(self):
        """Called automatically by the benchmark template after tests."""
        self._teardown()

    def load(self, dataset_key: str):
        """Load all dataset files into a fresh embedded GraphDB repository."""
        from org.eclipse.rdf4j.rio import RDFFormat
        from java.io import File

        dataset = DATASETS[dataset_key]
        self._create_repository()

        files = (v for k, v in dataset.items() if "_metadata" not in k.lower())

        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            tmp = temp_dir.name
            zipfile.ZipFile(dataset["ZIP"]).extractall(tmp)
            files = Path(tmp).rglob("*.xml")

        for f in files:
            self.connection.add(File(str(f)), "urn:cim", RDFFormat.RDFXML)

        if "ZIP" in dataset:
            temp_dir.cleanup()

        self._detect_namespace()

        return self

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded RDF dataset."""
        namespaces = [
            "http://iec.ch/TC57/CIM100#",  # CGMES 3.0
            "http://iec.ch/TC57/2013/CIM-schema-cim16#",  # CGMES 2.4.15
        ]

        for ns in namespaces:
            query = self.connection.prepareBooleanQuery(
                f"ASK {{ ?s a <{ns}ACLineSegment> }}")
            if query.evaluate():
                self.cim_namespace = ns
                return

        self.cim_namespace = "http://iec.ch/TC57/CIM100#"

    def _query_count(self, query_string: str) -> int:
        """Run a SPARQL COUNT query and return the integer result."""
        result = self.connection.prepareTupleQuery(query_string).evaluate()
        count = int(str(result.next().getValue("count").stringValue()))
        result.close()
        return count

    def _count_instances(self, class_name: str) -> int:
        return self._query_count(f'''
        SELECT (COUNT(DISTINCT ?s) as ?count)
        WHERE {{ ?s a <{self.cim_namespace}{class_name}> . }}
        ''')

    def get_load_metrics(self, loaded_obj, memory_mb):
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triples": loaded_obj._query_count(
                "SELECT (COUNT(*) as ?count) WHERE { ?s ?p ?o . }"),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        """Get all lines via PowSyBl's acLineSegments query (full row retrieval)."""
        from powsybl_queries import acline_segments_query
        query = acline_segments_query(loaded_obj.cim_namespace)
        result = loaded_obj.connection.prepareTupleQuery(query).evaluate()
        count = 0
        while result.hasNext():
            result.next()
            count += 1
        result.close()
        return count

    def get_generators_count(self, loaded_obj):
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        return (loaded_obj._count_instances("ConformLoad")
                + loaded_obj._count_instances("NonConformLoad")
                + loaded_obj._count_instances("EnergyConsumer"))

    def get_substations_count(self, loaded_obj):
        return loaded_obj._count_instances("Substation")

    def export(self, loaded_obj, output_path):
        """Export the repository to RDF/XML via RDF4J RIO."""
        from org.eclipse.rdf4j.rio import Rio, RDFFormat
        from java.io import FileOutputStream

        out = FileOutputStream(str(output_path))
        loaded_obj.connection.export(Rio.createWriter(RDFFormat.RDFXML, out))
        out.close()
        return Path(output_path)
