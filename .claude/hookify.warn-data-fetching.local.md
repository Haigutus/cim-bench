---
name: warn-data-fetching
enabled: true
event: file
conditions:
  - field: new_text
    operator: regex_match
    pattern: (import.*adapter|from.*adapter|Adapter\(\))
  - field: file_path
    operator: regex_match
    pattern: (generate_graphs|generate_report|generate_comparison)
---

⚠️ **Adapter import in report/graph tool**

You're importing adapters in report or graph generation code.

**Architecture principle:**
- **Adapters → Benchmarks** (embed data in JSON)
- **JSON Reports → Tools** (tools read from JSON)
- **NOT: Tools → Adapters** (direct fetching)

**Why this matters:**
- Keeps report tools simple and fast
- No import dependencies
- Everything needed is in JSON
- Tools just iterate over data

**The data-driven approach:**
- Store ALL needed info in benchmark JSON (display_name, color, etc.)
- Graph/report generators only read JSON files
- No fetching from adapters or other sources
- Keep logic reusable and simple

**Remember:** If graph generator needs something, add it to the JSON during benchmarking.
