#!/usr/bin/env python
"""
Generate the static results site (GitHub Pages) from benchmark JSONs.

Usage:
    python tools/generate_site.py [results-dir] [output-dir]   # defaults: results-docker docs

Self-contained: inline CSS/JS, graphs copied next to index.html.
Tables are sortable (click headers) and filterable by tool tags.
"""

import html
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from benchmark_data import load_benchmarks, dataset_label, format_time

REPO_URL = "https://github.com/Haigutus/cim-bench"

CSS = """
:root { --bg:#ffffff; --card:#f6f8fa; --ink:#1f2328; --ink2:#59636e; --line:#d1d9e0;
        --chip:#eaeef2; --chip-on:#0969da; --chip-on-ink:#ffffff; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#0d1117; --card:#161b22; --ink:#e6edf3; --ink2:#9198a1; --line:#3d444d;
          --chip:#21262d; --chip-on:#4493f8; --chip-on-ink:#0d1117; }
}
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--ink);
       font:15px/1.5 -apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
main { max-width:1100px; margin:0 auto; padding:24px 20px 60px; }
header { display:flex; flex-wrap:wrap; align-items:baseline; gap:12px; }
h1 { font-size:26px; margin:0; }
h2 { font-size:20px; margin:36px 0 4px; border-bottom:1px solid var(--line); padding-bottom:6px; }
h3 { font-size:16px; margin:20px 0 8px; }
a { color:var(--chip-on); text-decoration:none; }
a:hover { text-decoration:underline; }
.meta { color:var(--ink2); font-size:13px; }
.note { color:var(--ink2); font-size:13px; margin:4px 0 10px; }
.filters { display:flex; flex-wrap:wrap; gap:6px; margin:16px 0; align-items:center; }
.tag { display:inline-block; padding:1px 9px; border-radius:12px; background:var(--chip);
       color:var(--ink2); font-size:12px; white-space:nowrap; }
.filters .tag { cursor:pointer; user-select:none; font-size:13px; padding:3px 12px; }
.filters .tag.on { background:var(--chip-on); color:var(--chip-on-ink); }
.tablewrap { overflow-x:auto; }
table { border-collapse:collapse; width:100%; font-size:14px; font-variant-numeric:tabular-nums; }
th, td { text-align:left; padding:6px 12px 6px 0; border-bottom:1px solid var(--line); }
th { color:var(--ink2); font-weight:600; cursor:pointer; white-space:nowrap; user-select:none; }
th:hover { color:var(--ink); }
th .dir { font-size:10px; }
td.num, th.num { text-align:right; }
tr.hidden { display:none; }
.dot { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:7px; }
.tool { white-space:nowrap; font-weight:600; }
figure { margin:14px 0; background:#ffffff; border:1px solid var(--line); border-radius:8px; padding:10px; }
figure img { max-width:100%; height:auto; display:block; margin:0 auto; }
"""

JS = """
// Tag filtering: a row stays visible if it has ALL active tags
const chips = document.querySelectorAll('.filters .tag');
function applyFilter() {
  const active = [...chips].filter(c => c.classList.contains('on')).map(c => c.dataset.tag);
  document.querySelectorAll('tr[data-tags]').forEach(tr => {
    const tags = tr.dataset.tags.split(',');
    tr.classList.toggle('hidden', !active.every(t => tags.includes(t)));
  });
}
chips.forEach(c => c.addEventListener('click', () => { c.classList.toggle('on'); applyFilter(); }));

// Column sorting: click a header to sort by that column (data-v holds sort value)
document.querySelectorAll('th').forEach(th => th.addEventListener('click', () => {
  const table = th.closest('table');
  const idx = [...th.parentNode.children].indexOf(th);
  const asc = th.dataset.dir !== 'asc';
  table.querySelectorAll('th').forEach(h => { delete h.dataset.dir; h.querySelector('.dir')?.remove(); });
  th.dataset.dir = asc ? 'asc' : 'desc';
  th.insertAdjacentHTML('beforeend', `<span class="dir"> ${asc ? '▲' : '▼'}</span>`);
  const rows = [...table.tBodies[0].rows];
  rows.sort((a, b) => {
    const av = a.cells[idx].dataset.v ?? a.cells[idx].textContent.trim();
    const bv = b.cells[idx].dataset.v ?? b.cells[idx].textContent.trim();
    const an = parseFloat(av), bn = parseFloat(bv);
    const cmp = (!isNaN(an) && !isNaN(bn)) ? an - bn : String(av).localeCompare(String(bv));
    return asc ? cmp : -cmp;
  });
  rows.forEach(r => table.tBodies[0].appendChild(r));
}));
"""


def esc(value):
    return html.escape(str(value))


def tool_cell(name, color):
    return f'<td class="tool"><span class="dot" style="background:{esc(color)}"></span>{esc(name)}</td>'


def tag_chips(tags):
    return " ".join(f'<span class="tag">{esc(t)}</span>' for t in tags)


def time_cell(seconds):
    return f'<td class="num" data-v="{seconds}">{format_time(seconds)}</td>'


def table_html(headers, rows):
    """headers: list of (label, is_numeric); rows: list of (tags, cells_html)."""
    ths = "".join(f'<th{" class=num" if num else ""}>{esc(label)}</th>' for label, num in headers)
    trs = "".join(f'<tr data-tags="{esc(",".join(tags))}">{cells}</tr>' for tags, cells in rows)
    return f'<div class="tablewrap"><table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>'


def figures(graphs_dir, names):
    return "".join(
        f'<figure><img src="graphs/{name}" alt="{esc(name)}" loading="lazy"></figure>'
        for name in names if (graphs_dir / name).exists()
    )


def load_table(tools):
    headers = [("Tool", False), ("Tags", False), ("Version", False), ("Load time", True),
               ("Memory (MB)", True), ("Lines", True), ("Generators", True),
               ("Loads", True), ("Substations", True)]
    rows = []
    for name in sorted(tools, key=lambda t: tools[t].get("load", {}).get("time", 1e9)):
        t = tools[name]
        if "load" not in t:
            continue
        load = t["load"]
        deps = ", ".join(f"{k} {v}" for k, v in t.get("dependencies", {}).items())
        version = esc(t.get("version") or "?") + (f' <span class="meta">({esc(deps)})</span>' if deps else "")
        cells = (
            tool_cell(name, t["color"])
            + f"<td>{tag_chips(t['tags'])}</td><td>{version}</td>"
            + time_cell(load["time"])
            + f'<td class="num" data-v="{load["memory"]}">{load["memory"]:.1f}</td>'
            + "".join(f'<td class="num">{load[k]:,}</td>' for k in ("lines", "generators", "loads", "substations"))
        )
        rows.append((t["tags"], cells))
    return table_html(headers, rows)


def query_table(tools):
    query_types = sorted({q for t in tools.values() for q in t.get("queries", {})})
    if not query_types:
        return ""
    headers = [("Tool", False)] + [(q.replace("get_", ""), True) for q in query_types]
    rows = []
    for name in sorted(tools):
        t = tools[name]
        if not t.get("queries"):
            continue
        cells = tool_cell(name, t["color"]) + "".join(
            f'<td class="num" data-v="{t["queries"][q]}">{format_time(t["queries"][q] / 1000)}</td>'
            if q in t["queries"] else '<td class="num">–</td>'
            for q in query_types
        )
        rows.append((t["tags"], cells))
    return "<h3>Query performance</h3>" + table_html(headers, rows)


def export_table(data):
    rows = []
    for dataset in sorted(data):
        for name, t in sorted(data[dataset].items()):
            if "export" not in t:
                continue
            export_time = t["export"]["time"]
            load_time = t.get("load", {}).get("time")
            ratio = f'<td class="num" data-v="{export_time / load_time:.2f}">{export_time / load_time:.2f}x</td>' \
                if load_time else '<td class="num">–</td>'
            cells = (tool_cell(name, t["color"]) + f"<td>{esc(dataset)}</td>"
                     + time_cell(export_time) + ratio)
            rows.append((t["tags"], cells))
    if not rows:
        return ""
    headers = [("Tool", False), ("Dataset", False), ("Export time", True), ("Export/Import ratio", True)]
    return ("<h2>Export performance</h2>"
            '<p class="note">Serialization of loaded data back to RDF/XML. Ratio is export time over import time.</p>'
            + table_html(headers, rows))


def cli_section(cli_data, dataset_sizes, graphs_dir):
    if not cli_data:
        return ""
    parts = ["<h2>CLI tools</h2>",
             '<p class="note">Benchmarked as subprocesses (full process lifecycle per run) - '
             '<strong>not comparable</strong> with the in-process library numbers above.</p>']
    headers = [("Tool", False), ("Tags", False), ("Version", False), ("Dataset", False),
               ("Operation", False), ("Time", True), ("Peak RSS (MB)", True)]
    rows = []
    for dataset in sorted(cli_data, key=lambda ds: dataset_sizes.get(ds, 0), reverse=True):
        for name, t in sorted(cli_data[dataset].items()):
            for operation, values in sorted(t["operations"].items()):
                cells = (tool_cell(name, t["color"])
                         + f"<td>{tag_chips(t['tags'])}</td><td>{esc(t.get('version') or '?')}</td>"
                         + f"<td>{esc(dataset)}</td><td>{esc(operation)}</td>"
                         + time_cell(values["time"])
                         + f'<td class="num" data-v="{values["memory"]}">{values["memory"]:.1f}</td>')
                rows.append((t["tags"], cells))
    parts.append(table_html(headers, rows))
    parts.append(figures(graphs_dir, ["cli_time_comparison.svg", "cli_memory_comparison.svg"]))
    return "".join(parts)


def main(results_dir="results-docker", output_dir="docs"):
    results_dir, output_dir = Path(results_dir), Path(output_dir)
    data, cli_data, dataset_sizes, meta = load_benchmarks(results_dir)

    # Copy graphs next to the page
    graphs_dir = output_dir / "graphs"
    graphs_dir.mkdir(parents=True, exist_ok=True)
    for svg in (results_dir / "graphs").glob("*.svg"):
        shutil.copy(svg, graphs_dir / svg.name)

    all_tags = sorted({t for ds in list(data.values()) + list(cli_data.values())
                       for tool in ds.values() for t in tool["tags"]})
    machine = meta.get("machine_info", {})
    env = (f"{machine.get('cpu', {}).get('brand_raw', 'unknown CPU')} · "
           f"{machine.get('cpu', {}).get('count', '?')} cores · "
           f"{machine.get('system', '')} {machine.get('release', '')}")
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    sections = []
    for dataset in sorted(data, key=lambda ds: dataset_sizes.get(ds, 0), reverse=True):
        sections.append(f"<h2>{esc(dataset_label(dataset, dataset_sizes))}</h2>")
        sections.append(load_table(data[dataset]))
        sections.append(query_table(data[dataset]))
        sections.append(figures(graphs_dir, [f"{dataset}_comparison.svg", f"{dataset}_detailed.svg"]))

    sections.append("<h2>Cross-dataset comparisons</h2>")
    sections.append(figures(graphs_dir, ["import_comparison.svg", "memory_comparison.svg",
                                         "query_comparison.svg", "export_comparison.svg"]))
    sections.append(export_table(data))
    sections.append(cli_section(cli_data, dataset_sizes, graphs_dir))

    chips = "".join(f'<span class="tag" data-tag="{esc(t)}">{esc(t)}</span>' for t in all_tags)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>cim-bench results</title>
<style>{CSS}</style>
</head>
<body>
<main>
<header>
  <h1>cim-bench</h1>
  <span class="meta">CIM/CGMES parser &amp; serializer benchmarks ·
    <a href="{REPO_URL}">GitHub repository</a></span>
</header>
<p class="meta">Environment: {esc(env)} · Latest benchmark: {esc(meta.get('datetime', '?')[:10])} ·
Page generated: {generated}</p>
<div class="filters"><span class="meta">Filter by tag:</span>{chips}</div>
{"".join(sections)}
<p class="meta">Generated by <a href="{REPO_URL}/blob/master/tools/generate_site.py">tools/generate_site.py</a>
from pytest-benchmark JSON results. Sort any table by clicking a column header.</p>
</main>
<script>{JS}</script>
</body>
</html>
"""
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(page)
    print(f"✅ Site generated: {output_dir / 'index.html'}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
