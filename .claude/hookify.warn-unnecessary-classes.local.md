---
name: warn-unnecessary-classes
enabled: true
event: file
conditions:
  - field: new_text
    operator: regex_match
    pattern: ^class\s+\w+
  - field: file_path
    operator: regex_match
    pattern: ^(?!.*adapter\.py$).*\.py$
---

⚠️ **Class definition in non-adapter file**

You're adding a class outside of the adapter pattern.

**When to use classes:**
- Parser adapters (implementing ParserAdapter interface)
- Performance-critical libraries that require state
- Clear object-oriented abstractions

**When NOT to use classes:**
- Simple data transformations → use functions
- Utility operations → use functions
- Report generation → use functions
- Graph generation → use functions

**Philosophy:**
- **Functional > Object-Oriented** for simple tools
- Keep things short and concise
- Classes add complexity - use only when needed
- Prefer data structures (dict, list) over custom objects

**Ask yourself:**
- Does this really need state?
- Would a function with parameters work?
- Is inheritance/polymorphism actually needed?

If unsure, **start with functions** - refactor to classes only if complexity demands it.
