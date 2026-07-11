"""Thin wrapper around the pocket-rdf CLI for subprocess-based benchmarking.

pocket-rdf is a Typer-based RDF toolkit (rdflib + pySHACL) with no documented
importable API, so we call it via subprocess (see
benchmarks/cli_benchmark_template.py). This module provides the binary
resolution and command builders shared by both benchmark files.
"""

import os
import shutil

DISPLAY_NAME = "pocket-rdf"
COLOR = "#16a085"

# Version-agnostic SPARQL (CGMES 2.4 and 3.0 use different cim namespaces)
COUNT_QUERY = "SELECT (COUNT(*) AS ?n) WHERE { ?s ?p ?o }"


def get_pocket_rdf_bin():
    """Find the pocket-rdf entry point via env var or PATH."""
    return os.environ.get("POCKET_RDF_BIN") or shutil.which("pocket-rdf")


def serialize_cmd(binary, files, tmp_dir):
    """Build `pocket-rdf serialize` command (load all files, write RDF/XML)."""
    return [binary, "serialize"] + [str(f) for f in files] + [
        "--out", str(tmp_dir / "output.xml")
    ]


def query_cmd(binary, files, tmp_dir):
    """Build `pocket-rdf query` command (load all files, run a COUNT query)."""
    query_file = tmp_dir / "count.sparql"
    query_file.write_text(COUNT_QUERY)
    return [binary, "query"] + [str(f) for f in files] + [
        "--query", str(query_file), "--out", str(tmp_dir / "results.json")
    ]
