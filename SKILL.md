---
name: agentic-flow-installer
description: Install common docs/backlog skeleton plus stack-specific AGENTS (node/pnpm or php/composer) into a target directory.
---

## When to use
When the user wants to install the agentic workflow templates into a directory.

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

## Actions
### install (default, node)
Run:
- `python3 <skill_dir>/scripts/apply.py --stack node --mode safe --repo <repo_root>`

Then remind (install後のみ):
- (no additional reminders)

### install (php)
Run:
- `python3 <skill_dir>/scripts/apply.py --stack php --mode safe --repo <repo_root>`

Then remind (install後のみ):
- (no additional reminders)
