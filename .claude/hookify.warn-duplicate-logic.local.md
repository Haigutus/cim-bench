---
name: warn-duplicate-logic
enabled: true
event: file
conditions:
  - field: new_text
    operator: regex_match
    pattern: (for\s+\w+\s+in.{20,}|def\s+\w+\(.{10,})
---

⚠️ **Check for duplicate logic**

You're adding new logic. Before proceeding, verify:

**Reuse checklist:**
- [ ] Is similar logic already implemented elsewhere?
- [ ] Can existing functions/methods handle this?
- [ ] Should this be extracted to a shared utility?

**Key principles:**
- **DRY (Don't Repeat Yourself)** - same logic should exist once
- Look for similar patterns in existing code
- Extract common operations to shared functions
- Keep things short and concise

**If duplicating:**
- Consider refactoring both instances
- Extract to common location
- Ensure consistency across codebase

**Data-driven approach:**
- Store needed data in JSON reports
- Let graph/report tools read from reports
- Don't fetch from adapters or other sources in multiple places
