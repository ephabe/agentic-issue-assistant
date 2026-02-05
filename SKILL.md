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
  - label: `append backlog from docs`
    description: `docs/ と 09_IMPLEMENTATION_PLAN を読み、backlog/issues.json に追記する。`

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

### append backlog from docs (agentic)
Run only (repo root):
- Read `docs/README.md` and `docs/09_IMPLEMENTATION_PLAN.md`. Load the referenced docs needed to author each issue body.
- Collect issue IDs and short descriptions from each milestone's `Issues:` list (`- [ISSUE-ID] summary`). Ignore the `Sample` section if it still exists.
- Load `backlog/issues.json` and append only missing IDs. Do not modify existing items. Preserve order by the plan.
- For each new issue, generate:
  - `id`: from the plan.
  - `title`: short summary (>= 3 chars).
  - `body`: based on docs + plan (>= 10 chars), including context, scope/acceptance, and doc references.
  - `labels` (optional): only if you know the labels exist.
- Enforce schema: only `id`, `title`, `body`, `labels` keys. Keep ISSUE-ID unique.
- Optionally validate/append via `python3 scripts/backlog/append_issues.py --input <draft.json>` after drafting the new items.

Then remind:
- 既存Issueは修正せず追記のみ（変更が必要なら新規Issueを起票）。
- 重複IDはスキップした旨を伝える。
