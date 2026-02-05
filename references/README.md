# Agentic Flow Installer Skill

Applies a shared docs/templates skeleton plus a stack-specific overlay (node/pnpm or php/composer).

## Manual usage
```bash
bash ~/.codex/skills/agentic-flow-installer/scripts/apply.sh node safe .
bash ~/.codex/skills/agentic-flow-installer/scripts/apply.sh php safe .
```
Defaults: `stack=node`, `mode=safe`, `repo=.` (`scripts/apply.sh` internally calls `scripts/apply.py`).

Modes:
- `safe`: 既存ファイルは上書きしない（同一なら skip (same)、差分があれば skip (exists)）。
- `overwrite`: 既存ファイルも上書きする。

## What gets installed
- `docs/` 一式（`00_PRD.md`〜`09_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`README.md`）
- `backlog/` スケルトン（`INDEX.md`、`ISSUE-template.md`、`issues/`、`issues/M0/CHORE-001..003`）
- 選択したテンプレートに対応する `AGENTS.md` と `README.md`（node/pnpm または php/composer）

## Backlog update (agentic)
- docs と実装計画（`docs/09_IMPLEMENTATION_PLAN.md`）を読み、`backlog/issues/` に Issue ファイルを追加する作業はエージェントが指示を受けて実施する想定。
- 既存Issueは変更せず追記のみ。ID重複はスキップする。

## ISSUE-ID
- 各 Issue ファイルに `ISSUE-ID: <id>` を必ず付ける（重複発行防止）。
