"""GridLab GMSS CIM (.NET) parser adapter for benchmarking.

Hosts CoreCLR in-process via pythonnet and drives the real GMSS ingestion
pipeline: each file is loaded through the ABP-registered CimGraphContext
(GMSS's validated document ingestion). The FullModelReader header step is
deliberately not run: it adds nothing the benchmark consumes and its
model-URI validator rejects RealGrid's legacy IDs regardless of
CimUriValidatorOptions.SupportLegacyIds (see PR #16 discussion).

The published GMSS packages ship the document/graph layer (typed equipment
classes are what applications generate with the GMSS code generator), so
queries run SPARQL on the underlying dotNetRDF (VDS.RDF) graphs via the
Leviathan engine - the same query family as the other triplestore tools,
including PowSyBl's acLineSegments reference query for lines.

Repository: https://gitlab.com/gms-squared/modules/gridlab.gmss.cim
Requires: GMSS_DLL_DIR pointing at the published DLLs, .NET runtime,
PYTHONNET_RUNTIME=coreclr (set by docker/tools/gmss.dockerfile).
"""

import os
import tempfile
import zipfile
from pathlib import Path

from parser_adapter import ParserAdapter, QueryUnsupported
from datasets import DATASETS

CIM_NAMESPACES = [
    "http://iec.ch/TC57/CIM100#",  # CGMES 3.0
    "http://iec.ch/TC57/2013/CIM-schema-cim16#",  # CGMES 2.4.15
]

# GMSS has no SPARQL engine of its own, so queries run through dotNetRDF's
# in-memory Leviathan engine. It cannot finish the PowSyBl join queries on a
# million-triple graph in reasonable time (rdflib needed ~447 s for the same
# acLineSegments query; Leviathan is slower). Above this triple count the
# query benchmarks are skipped - load is still measured.
QUERY_TRIPLE_LIMIT = 500_000

_clr_initialized = False


def init_clr():
    """Load CoreCLR and the GMSS assemblies (once per process)."""
    global _clr_initialized
    if _clr_initialized:
        return
    from pythonnet import load
    load("coreclr")
    import clr  # noqa: F401
    import System

    # Publish folders mix managed and native DLLs - LoadFrom the managed ones
    dll_dir = Path(os.environ["GMSS_DLL_DIR"])
    for dll in sorted(dll_dir.glob("*.dll")):
        try:
            System.Reflection.Assembly.LoadFrom(str(dll))
        except System.BadImageFormatException:
            pass  # native library, not a CLR assembly

    _clr_initialized = True


class GmssAdapter(ParserAdapter):
    """Adapter for GridLab GMSS CIM via pythonnet."""

    def __init__(self):
        self.graphs = None  # list of (name, VDS.RDF IGraph)
        self.cim_namespace = None
        self._app = None

    @classmethod
    def get_version(cls) -> str:
        init_clr()
        import System
        asm = System.Reflection.Assembly.Load("GridLab.Gmss.Cim.Domain")
        return str(asm.GetName().Version)

    @classmethod
    def get_dependencies(cls) -> dict:
        init_clr()
        import System
        deps = {"dotnet": str(System.Environment.Version)}
        for name in ("GridLab.Abp.Rdf", "Volo.Abp.Core"):
            asm = System.Reflection.Assembly.Load(name)
            deps[name] = str(asm.GetName().Version)
        return deps

    @classmethod
    def get_display_name(cls) -> str:
        return "GMSS CIM"

    @classmethod
    def get_color(cls) -> str:
        return "#512bd4"  # .NET purple

    @classmethod
    def get_tags(cls):
        return ["parser", "query", "sparql", "c#"]

    def _init_services(self):
        """Bootstrap the ABP module and resolve the GMSS services."""
        self.cleanup()  # dispose previous app (load() runs once per benchmark round)
        init_clr()
        from System import Action
        from Volo.Abp import AbpApplicationFactory, AbpApplicationCreationOptions
        from GridLab.Gmss.Cim import CimDomainModule
        from GridLab.Abp.Rdf.GraphContext import IRdfGraphContext
        from GridLab.Abp.Cim.Configuration import CimUriValidatorOptions
        from Microsoft.Extensions.DependencyInjection import (
            LoggingServiceCollectionExtensions,
            OptionsServiceCollectionExtensions,
            ServiceProviderServiceExtensions,
        )

        # ABP property injection (Logger etc.) requires the Autofac provider;
        # AddLogging supplies the ILoggerFactory it injects
        from Volo.Abp import AbpAutofacAbpApplicationCreationOptionsExtensions

        def set_legacy_ids(o):
            # RealGrid uses legacy "urn:uuid:_..." rdf:IDs that the default
            # strict IEC 61970-552 validator rejects (per the GMSS author)
            o.SupportLegacyIds = True

        def configure(options):
            LoggingServiceCollectionExtensions.AddLogging(options.Services)
            AbpAutofacAbpApplicationCreationOptionsExtensions.UseAutofac(options)
            OptionsServiceCollectionExtensions.Configure[CimUriValidatorOptions](
                options.Services, Action[CimUriValidatorOptions](set_legacy_ids))

        self._app = AbpApplicationFactory.Create[CimDomainModule](
            Action[AbpApplicationCreationOptions](configure)
        )
        self._app.Initialize()
        provider = self._app.ServiceProvider
        self._graph_context = ServiceProviderServiceExtensions.GetRequiredService[IRdfGraphContext](provider)

    def load(self, dataset_key: str):
        """Load all dataset files through the GMSS graph context."""
        self._init_services()
        from GridLab.Abp.Rdf import RdfFormat
        from System.Threading import CancellationToken

        token = getattr(CancellationToken, "None")  # "None" is a Python keyword
        dataset = DATASETS[dataset_key]

        # Determine files to load
        files = [Path(v) for k, v in dataset.items() if "_metadata" not in k.lower()]

        # Extract ZIP if needed
        temp_dir = None
        if "ZIP" in dataset:
            temp_dir = tempfile.TemporaryDirectory()
            zipfile.ZipFile(dataset["ZIP"]).extractall(temp_dir.name)
            files = list(Path(temp_dir.name).rglob("*.xml"))

        # Load all files (same logic for ZIP and non-ZIP)
        self.graphs = []
        for f in files:
            self._graph_context.LoadFromFileAsync(
                str(f), RdfFormat.RdfXml, f.stem, token
            ).GetAwaiter().GetResult()

            graph = self._graph_context.GetGraphAsync(f.stem, token).GetAwaiter().GetResult()
            self.graphs.append((f.stem, graph))

        if temp_dir:
            temp_dir.cleanup()

        # SPARQL (Leviathan) over each loaded graph - the published GMSS
        # packages have no typed equipment model, so queries are SPARQL like
        # the other triplestore tools
        from VDS.RDF.Parsing import SparqlQueryParser
        from VDS.RDF.Query import LeviathanQueryProcessor
        from VDS.RDF.Query.Datasets import InMemoryDataset

        self._sparql_parser = SparqlQueryParser()
        self._processors = [LeviathanQueryProcessor(InMemoryDataset(g)) for _, g in self.graphs]

        self._n_triples = sum(g.Triples.Count for _, g in self.graphs)
        self._skip_queries = self._n_triples > QUERY_TRIPLE_LIMIT

        self._detect_namespace()
        return self

    def _require_queries(self):
        """Raise QueryUnsupported when Leviathan can't run queries at this scale."""
        if self._skip_queries:
            raise QueryUnsupported(
                f"{self._n_triples} triples exceed the Leviathan query limit "
                f"({QUERY_TRIPLE_LIMIT}); load measured, queries skipped")

    def _query_rows(self, query_text):
        """Run a SPARQL query on every loaded graph, return total result rows."""
        query = self._sparql_parser.ParseFromString(query_text)
        return sum(p.ProcessQuery(query).Results.Count for p in self._processors)

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded graphs."""
        for ns in CIM_NAMESPACES:
            if self._query_rows(f"SELECT ?s WHERE {{ ?s a <{ns}ACLineSegment> }} LIMIT 1"):
                self.cim_namespace = ns
                return
        self.cim_namespace = CIM_NAMESPACES[0]

    def _count_instances(self, class_name):
        """SPARQL COUNT of a CIM class, summed across the per-profile graphs."""
        query = self._sparql_parser.ParseFromString(f'''
        SELECT (COUNT(DISTINCT ?s) as ?count)
        WHERE {{ ?s a <{self.cim_namespace}{class_name}> . }}
        ''')
        total = 0
        for p in self._processors:
            results = p.ProcessQuery(query).Results
            # pythonnet exposes the result as INode; str() gives "39^^xsd:integer".
            # Graphs without a match return an unbound ?count (None) instead of 0.
            node = results[0].Value("count") if results.Count else None
            if node is not None:
                total += int(str(node).split("^^")[0])
        return total

    def get_load_metrics(self, loaded_obj, memory_mb):
        metrics = {
            "memory_mb": f"{memory_mb:.1f}",
            "triples": loaded_obj._n_triples,
        }
        # Element counts come from SPARQL; omit them where queries are skipped
        if not loaded_obj._skip_queries:
            metrics.update({
                "lines": loaded_obj.get_lines_count(loaded_obj),
                "generators": loaded_obj.get_generators_count(loaded_obj),
                "loads": loaded_obj.get_loads_count(loaded_obj),
                "substations": loaded_obj.get_substations_count(loaded_obj),
            })
        return metrics

    def get_lines_count(self, loaded_obj):
        """Get all lines via PowSyBl's acLineSegments query (full row retrieval)."""
        from powsybl_queries import acline_segments_query
        loaded_obj._require_queries()
        return loaded_obj._query_rows(acline_segments_query(loaded_obj.cim_namespace))

    def get_generators_count(self, loaded_obj):
        loaded_obj._require_queries()
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        loaded_obj._require_queries()
        return (
            loaded_obj._count_instances("ConformLoad")
            + loaded_obj._count_instances("NonConformLoad")
            + loaded_obj._count_instances("EnergyConsumer")
        )

    def get_substations_count(self, loaded_obj):
        loaded_obj._require_queries()
        return loaded_obj._count_instances("Substation")

    def cleanup(self):
        """Dispose the ABP application between benchmark rounds."""
        if self._app is not None:
            self._app.Dispose()
            self._app = None
