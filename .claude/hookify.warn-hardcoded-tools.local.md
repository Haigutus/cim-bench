---
name: warn-hardcoded-tools
enabled: true
event: file
conditions:
  - field: new_text
    operator: regex_match
    pattern: (["'])(triplets|pypowsybl|cimpy)\1
---

⚠️ **Hardcoded tool/library name detected**

You're adding a hardcoded tool name to the code. This violates the principle of keeping the code dynamic and tool-agnostic.

**Why this matters:**
- Makes adding new parsers harder
- Creates maintenance burden
- Goes against the adapter pattern design

**Instead:**
- Use data from adapters (display_name, etc.)
- Store in configuration/datasets
- Let the code discover tools dynamically

**Remember:** The goal is zero-configuration extensibility - adding a parser shouldn't require code changes.
