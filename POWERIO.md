# PowerIO measurements

The default tool image installs **PowerIO 0.11.10**. It loads every registered
CGMES profile and queries the native typed model. Its load count includes
equivalent injections; substations include retained boundary/source records.
These are native component counts, not SPARQL result materialization. Compare
query timings only after checking these semantics and the returned counts.
The query assertions are API sanity checks; they do not certify the dataset's
semantic component counts against an independent oracle.
PowerIO's Python wrapper caches immutable scalar count attributes after their
first access. Repeated calibrated getter timings therefore measure steady-state
access, not first-query traversal or index-construction cost.

Each load returns an independently owned module/network. The reusable adapter
does not retain a previous module during the next timed parse. Temporary input
staging is included in load time and is cleaned up even if parsing fails.

## Fresh export and fidelity

The timed export includes copying the module without retained source bytes,
canonical CGMES 3.0 emission and native filesystem writing. It cannot use the
same-format byte replay path. All adapters use one export call per measured
round into a fresh destination; removing the preceding output happens outside
the timer. `--benchmark-min-rounds` controls the number of export rounds.

An untimed first export must produce nonempty files in an empty directory.
PowerIO reparses its final output and requires native component counts to
survive. Export bytes, file count, and diagnostic-code counts accompany the
timing. A successful reparse is **self-consistency evidence**, not independent
consumer acceptance or a claim that every source field was preserved. Reported
field losses remain visible even when the benchmark passes.

Old results used different export/count preparation and repeated overwrite
semantics. Keep them as historical evidence; rerun all comparison tools with
the current harness before comparing their timings.

## Versioned runs

Keep each version and environment in a separate results directory. For example,
create a separate RC image from an exact Linux wheel. PowerIO RCs are distributed
through GitHub prereleases and workflow artifacts; they are not published to
PyPI, crates.io or the Julia registry. Download a wheel for the container's Linux
architecture from the selected release workflow, or build one from an immutable
source revision in a matching Linux environment:

```sh
# Run in the selected clean PowerIO checkout, inside Linux with Rust, Python
# >= 3.11 and maturin installed. Record this commit with the resulting wheel.
git rev-parse HEAD
maturin build --release --locked --features gridfm -i python3 -o /out
```

Install that single wheel into a separate image, preserving its wheel filename.
A macOS wheel cannot be installed in the Linux benchmark container.

```sh
image_context=$(mktemp -d)
# Replace this path with the one exact, compatible wheel being evaluated.
cp /path/to/powerio-0.12.0rc1-cp311-abi3-manylinux_2_35_aarch64.whl "$image_context/"
cat > "$image_context/Dockerfile" <<'EOF'
FROM localhost/cim-bench/powerio:latest
COPY *.whl /tmp/
RUN uv pip install --python /app/.venv/bin/python --no-deps --reinstall /tmp/*.whl
EOF
podman build -t cim-bench/powerio:rc-evaluation "$image_context"
```

Retain the wheel SHA-256, exact source commit, build features and resulting image
ID with the run. The root environment's seven-day package-age policy can delay a
newly published stable release; the isolated tool image uses its explicit version
pin. Do not silently replace a requested version.

The benchmark JSON's `cim_bench_evidence` records input SHA-256 hashes and byte
counts, the observed harness commit/dirty state, run exit status, test outcomes
(including skips, collection errors and teardown failures), and optional
runner declarations:

- `CIM_BENCH_RUN_ID`: a shared identifier for one comparison run.
- `CIM_BENCH_COMMIT`: harness commit when the container has no `.git` checkout.
- `CIM_BENCH_IMAGE_ID`: the image digest/ID returned by the container runtime.
- `CIM_BENCH_TOOL_COMMIT` (or `POWERIO_SOURCE_COMMIT`): the implementation commit
  used to build a source package.

Declarations are labelled separately from an observed checkout. Installed
package and native release versions are recorded for every timed operation.
The ordinary `machine_info` and timing statistics remain in pytest-benchmark's
JSON. Avoid `--benchmark-save-data` for long getter runs unless individual raw
samples are needed; summary statistics and round counts are recorded either way.

RSS in the standard load test is a **retained process-RSS delta after repeated
loads**. It is not isolated peak memory, allocation volume or model size. A
sampled process-tree peak from an independent fresh process is a separate metric
and must state its sampling interval and whether interpreter startup is included.

Run the synthetic contract tests without downloading datasets:

```sh
python -m pytest tests -q
```

These tests cover missing profiles, independent ownership, fresh export setup,
native reparsing, and evidence hashes. Performance scores still require the
full datasets and comparable fresh runs. The standard benchmark does not itself
validate sparse matrices, solver results, SHACL compliance or cross-tool fidelity.
