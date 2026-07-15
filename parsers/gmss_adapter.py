"""GridLab GMSS CIM (.NET) parser adapter for benchmarking.

Hosts CoreCLR in-process via pythonnet and drives the real GMSS ingestion
pipeline: each file is loaded through the ABP-registered CimGraphContext and
parsed into a typed CimFullModel by FullModelReader (the same flow as
CimDocumentManager.ProcessAsync, minus repository persistence).

Class counts are queried on the underlying dotNetRDF (VDS.RDF) graphs, the
same rdf:type counting the RDFlib and Jena adapters use.

Repository: https://gitlab.com/gms-squared/modules/gridlab.gmss.cim
Requires: GMSS_DLL_DIR pointing at the published DLLs, .NET runtime,
PYTHONNET_RUNTIME=coreclr (set by docker/tools/gmss.dockerfile).
"""

import os
import tempfile
import zipfile
from pathlib import Path

from parser_adapter import ParserAdapter
from datasets import DATASETS

RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
CIM_NAMESPACES = [
    "http://iec.ch/TC57/CIM100#",  # CGMES 3.0
    "http://iec.ch/TC57/2013/CIM-schema-cim16#",  # CGMES 2.4.15
]

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
        self.models = None  # list of typed CimFullModel
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
        return ["parser", "query", "typed-model", "c#"]

    def _init_services(self):
        """Bootstrap the ABP module and resolve the GMSS services."""
        self.cleanup()  # dispose previous app (load() runs once per benchmark round)
        init_clr()
        from System import Action
        from Volo.Abp import AbpApplicationFactory, AbpApplicationCreationOptions
        from GridLab.Gmss.Cim import CimDomainModule
        from GridLab.Abp.Rdf.GraphContext import IRdfGraphContext
        from GridLab.Gmss.Cim.Parsing.Readers.FullModels import IFullModelReader
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
        self._model_reader = ServiceProviderServiceExtensions.GetRequiredService[IFullModelReader](provider)

    def load(self, dataset_key: str):
        """Load all dataset files through the GMSS graph context + full model reader."""
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
        self.models = []
        for f in files:
            self._graph_context.LoadFromFileAsync(
                str(f), RdfFormat.RdfXml, f.stem, token
            ).GetAwaiter().GetResult()

            graph = self._graph_context.GetGraphAsync(f.stem, token).GetAwaiter().GetResult()
            self.graphs.append((f.stem, graph))
            self.models.append(self._model_reader.GetModelAsync(graph).GetAwaiter().GetResult())

        if temp_dir:
            temp_dir.cleanup()

        self._detect_namespace()
        return self

    def _detect_namespace(self):
        """Detect the CIM namespace used in the loaded graphs."""
        for ns in CIM_NAMESPACES:
            if self._count_instances_ns("ACLineSegment", ns) > 0:
                self.cim_namespace = ns
                return
        self.cim_namespace = CIM_NAMESPACES[0]

    def _count_instances_ns(self, class_name, namespace):
        """Count rdf:type triples of a CIM class across all loaded graphs."""
        from VDS.RDF import UriFactory

        total = 0
        for _, graph in self.graphs:
            rdf_type = graph.CreateUriNode(UriFactory.Create(RDF_TYPE))
            cim_class = graph.CreateUriNode(UriFactory.Create(namespace + class_name))
            total += sum(1 for _ in graph.GetTriplesWithPredicateObject(rdf_type, cim_class))
        return total

    def _count_instances(self, class_name):
        return self._count_instances_ns(class_name, self.cim_namespace)

    def get_load_metrics(self, loaded_obj, memory_mb):
        return {
            "memory_mb": f"{memory_mb:.1f}",
            "triples": sum(g.Triples.Count for _, g in loaded_obj.graphs),
            "lines": loaded_obj.get_lines_count(loaded_obj),
            "generators": loaded_obj.get_generators_count(loaded_obj),
            "loads": loaded_obj.get_loads_count(loaded_obj),
            "substations": loaded_obj.get_substations_count(loaded_obj),
        }

    def get_lines_count(self, loaded_obj):
        return loaded_obj._count_instances("ACLineSegment")

    def get_generators_count(self, loaded_obj):
        return loaded_obj._count_instances("SynchronousMachine")

    def get_loads_count(self, loaded_obj):
        return (
            loaded_obj._count_instances("ConformLoad")
            + loaded_obj._count_instances("NonConformLoad")
            + loaded_obj._count_instances("EnergyConsumer")
        )

    def get_substations_count(self, loaded_obj):
        return loaded_obj._count_instances("Substation")

    def cleanup(self):
        """Dispose the ABP application between benchmark rounds."""
        if self._app is not None:
            self._app.Dispose()
            self._app = None
