---
name: agentic-flow-installer
description: Install common docs/backlog skeleton plus an AGENTS template into a target directory.
---

## When to use
When the user wants to install the agentic workflow templates into a directory.

## Defaults
- repo: `.`

## Actions
### install (default)
Run:
- `python3 <skill_dir>/scripts/apply.py --repo <repo_root>`

Then remind (install後のみ):
- `backlog/issues/M0/` の初期Issue（`CHORE-001`〜`CHORE-003`）に従って、`docs/`、`AGENTS.md`、CI の整備を進める。
