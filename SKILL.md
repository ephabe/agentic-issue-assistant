---
name: agentic-flow-installer
description: Apply agentic workflow templates into a Git repo. Combines common docs/templates with stack overlays (node/pnpm or php/composer).
---

## When to use
When the user wants to install the “End-to-end implementation within Actions” workflow into a repo.

## Defaults
- stack: node
- mode: safe

## Interactive flow (応答式)
If the user did not explicitly choose an action, call `request_user_input` with the UI below.

request_user_input:
- header: `Action`
- id: `action`
- question: `実行したい操作を選択してください。`
- options:
  - label: `install (node)` (Recommended)
    description: `node/pnpm のテンプレを repo に適用する。`
  - label: `install (php)`
    description: `php/composer のテンプレを repo に適用する。`
  - label: `ensure github labels`
    description: `GitHub ラベル作成スクリプトのみ実行する。`
  - label: `create github issues`
    description: `backlog から GitHub Issue を作成する。`

## Actions
### install (default, node)
Run:
- `python3 <skill_dir>/scripts/apply.py --stack node --mode safe --repo <repo_root>`

Then remind (install後のみ):
- `bash scripts/gh/ensure_labels.sh`
- set GitHub Secret `OPENAI_API_KEY`
- label only ready issues `codex-ready` (対象Issueが用意できたタイミングで。backlog から作る場合は labels に `codex-ready` を入れてもよい)
- run workflow `Codex Queue (Issue -> PR)`

### install (php)
Run:
- `python3 <skill_dir>/scripts/apply.py --stack php --mode safe --repo <repo_root>`

Then remind (install後のみ):
- `bash scripts/gh/ensure_labels.sh`
- set GitHub Secret `OPENAI_API_KEY`
- label only ready issues `codex-ready` (対象Issueが用意できたタイミングで。backlog から作る場合は labels に `codex-ready` を入れてもよい)
- run workflow `Codex Queue (Issue -> PR)`

### ensure github labels
Run only (repo root):
- `bash scripts/gh/ensure_labels.sh`

Then remind:
- (no additional reminders)

### create github issues
Run only (repo root):
- `bash scripts/gh/create_issues_from_backlog.sh`

Then remind:
- (no additional reminders)
