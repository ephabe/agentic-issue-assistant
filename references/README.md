# Agentic Flow Installer Skill

Applies a shared docs/templates skeleton plus an `AGENTS.md` template.

## Manual usage
```bash
bash ~/.codex/skills/agentic-flow-installer/scripts/apply.sh safe .
bash ~/.codex/skills/agentic-flow-installer/scripts/apply.sh overwrite .
```
Defaults: `mode=safe`, `repo=.` (`scripts/apply.sh` internally calls `scripts/apply.py`).

Modes:
- `safe`: 既存ファイルは上書きしない（同一なら skip (same)、差分があれば skip (exists)）。
- `overwrite`: 既存ファイルも上書きする。

## What gets installed
- `docs/` 一式（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`README.md`）
- `backlog/` スケルトン（`INDEX.md`、`ISSUE-template.md`、`issues/`、`issues/M0/CHORE-001..003`）
- `AGENTS.md`（CIコマンドは環境に応じて編集）

## Backlog update (agentic)
- docs と実装計画（`docs/10_IMPLEMENTATION_PLAN.md`）を読み、`backlog/issues/` に Issue ファイルを追加する作業はエージェントが指示を受けて実施する。
- 既存Issueは変更せず追記のみ。ID重複はスキップする。

## ISSUE-ID
- 各 Issue ファイルに `ISSUE-ID: <id>` を必ず付ける（重複発行防止）。
