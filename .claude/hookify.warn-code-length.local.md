---
name: warn-code-length
enabled: true
event: file
conditions:
  - field: new_text
    operator: regex_match
    pattern: (def\s+\w+[^\n]*\n(.*\n){30,})
---

⚠️ **Long function detected**

You're writing a function that may be getting too long.

**Project values:**
- **Short and concise** > comprehensive
- **Limited lines** per function/file
- **Readability foremost** - concepts should be graspable quickly

**Guidelines:**
- Functions should ideally be < 20-30 lines
- If longer, consider:
  - Breaking into smaller functions
  - Extracting helper methods
  - Simplifying the logic

**Keep complexity minimal:**
- Introduce complexity only when needed
- Prefer simple, obvious code
- Make it easy to understand at a glance

**Remember:** This is a benchmarking tool - clarity > completeness.
