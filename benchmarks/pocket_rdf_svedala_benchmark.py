"""pocket-rdf benchmarks on Svedala dataset (7.3 MB, CGMES 3.0)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from pocket_rdf_adapter import COLOR, DISPLAY_NAME, get_pocket_rdf_bin, query_cmd, serialize_cmd
from cli_benchmark_template import CliOperation, create_cli_benchmarks

create_cli_benchmarks(
    tool_name="pocket_rdf",
    display_name=DISPLAY_NAME,
    color=COLOR,
    binary=get_pocket_rdf_bin(),
    operations={
        "serialize": CliOperation(serialize_cmd, "load all profiles and serialize merged RDF/XML",
                                  output_files=("output.xml",)),
        "query": CliOperation(query_cmd, "load all profiles and materialize SPARQL triple COUNT",
                              output_files=("results.json",)),
    },
    dataset_key="svedala_igm_cgmes_3",
    dataset_name="svedala",
    tags=["serializer", "query", "sparql", "python"],
)
