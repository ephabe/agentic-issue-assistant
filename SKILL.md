---
name: agentic-flow-installer
description: Apply agentic workflow templates into a Git repo. Combines common docs/templates with stack overlays (node/pnpm or php/composer).
---

## When to use
When the user wants to install the “Actions内で実装まで完結” workflow into a repo.

## Defaults
- stack: node
- mode: safe

## How to apply
Run:
- `python3 <skill_dir>/scripts/apply.py --stack <node|php> --mode <safe|overwrite> --repo <repo_root>`

Then remind:
- `bash scripts/gh/ensure_labels.sh`
- set GitHub Secret `OPENAI_API_KEY`
- label issues `codex-ready`
- run workflow `Codex Queue (Issue -> PR)`
