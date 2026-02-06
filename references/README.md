# Agentic Issue Assistant Skill

Applies a shared docs/templates skeleton plus an `AGENTS.md` template.

## Manual usage
```bash
bash ~/.codex/skills/agentic-issue-assistant/scripts/apply.sh . integration
# or
bash ~/.codex/skills/agentic-issue-assistant/scripts/apply.sh . analysis
```
Defaults: `repo=.` / `m0=integration` (`scripts/apply.sh` internally calls `scripts/apply.py`).

Behavior:
- 配置対象と同名のファイルが1つでも既に存在する場合、インストールは中止される（何も書き込まない）。

## What gets installed
- `docs/` 一式（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`ISSUE.md`、`README.md`）
- `backlog/` スケルトン（`INDEX.md`、`ISSUE-template.md`、`FINALIZATION-template.md`、`issues/`）
- `backlog/issues/M0/CHORE-001..003`（`--m0` で選択: `integration` = `M0-Integration` / `analysis` = `M0-Analysis`）
- `AGENTS.md`（CIコマンドは環境に応じて編集）

## Backlog update (agentic)
- docs と実装計画（`docs/10_IMPLEMENTATION_PLAN.md`）を読み、`backlog/issues/` に Issue ファイルを追加する作業はエージェントが指示を受けて実施する。
- 既存Issueは変更せず追記のみ。ID重複はスキップする。

## ISSUE-ID
- 各 Issue ファイルに `ISSUE-ID: <id>` を必ず付ける（重複発行防止）。
