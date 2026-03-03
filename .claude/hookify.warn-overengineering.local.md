---
name: warn-overengineering
enabled: true
event: file
conditions:
  - field: new_text
    operator: regex_match
    pattern: (try:|except\s+\w+|\.get\([^)]+,\s*[^)]+\)|if\s+\w+\s+is\s+not\s+None)
---

⚠️ **Potential over-engineering detected**

You're adding exception handling or defensive checks that may not be needed.

**Project philosophy:**
- This is a benchmarking tool, not production-critical software
- **Let things fail with clear errors** - easier to debug
- Simple `.get()` without complex fallbacks is sufficient
- Avoid try-except unless truly necessary
- Keep code short and readable

**Guidelines:**
- Use simple dict access: `data["key"]` - let KeyError happen
- Use `.get()` only for optional values: `data.get("key")`
- No complex fallback chains: `data.get("a", {}).get("b", default)`
- Exception handling only for expected, recoverable errors

**Remember:** Readability and brevity > robustness. Make failures obvious.
