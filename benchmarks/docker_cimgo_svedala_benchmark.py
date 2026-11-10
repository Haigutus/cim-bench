"""cimgo benchmarks on Svedala dataset (7.3 MB, CGMES 3.0)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "parsers"))

from cimgo_adapter import COLOR, DISPLAY_NAME, convert_cmd, get_cimgo_bin, inspect_validation, validate_cmd
from cli_benchmark_template import CliOperation, create_cli_benchmarks

create_cli_benchmarks(
    tool_name="cimgo",
    display_name=DISPLAY_NAME,
    color=COLOR,
    binary=get_cimgo_bin(),
    operations={
        "validate": CliOperation(validate_cmd, "load all profiles and run SHACL/SPARQL validation",
                                 accepted_returncodes=(0, 1), inspect_result=inspect_validation),
        "convert": CliOperation(convert_cmd, "load all profiles and write merged cimgo JSON",
                                output_files=("output.json",)),
    },
    dataset_key="svedala_igm_cgmes_3",
    dataset_name="svedala",
    tags=["validator", "serializer", "go"],
)
