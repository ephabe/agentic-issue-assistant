# Agentic Issue Assistant Skill

Applies a shared docs/templates skeleton plus an `AGENTS.md` template.

## Manual usage
```bash
bash ~/.codex/skills/agentic-issue-assistant/scripts/apply.sh . repo-integration
# or
bash ~/.codex/skills/agentic-issue-assistant/scripts/apply.sh . existing-code-analysis
```
Defaults: `repo=.` / `m0=repo-integration` (`scripts/apply.sh` internally calls `scripts/apply.py`).
(`integration` / `analysis` は互換エイリアスとして利用可能)

Behavior:
- 配置対象と同名のファイルが1つでも既に存在する場合、インストールは中止される（何も書き込まない）。

## What gets installed
- `docs/` 一式（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`ISSUE.md`、`README.md`）
- `backlog/` スケルトン（`INDEX.md`、`ISSUE-template.md`、`FINALIZATION-template.md`、`issues/`）
- `backlog/issues/M0/CHORE-001..003`（`--m0` で選択: `repo-integration` = `M0-Integration` / `existing-code-analysis` = `M0-Analysis`）
- `docs/10_IMPLEMENTATION_PLAN.md`（`--m0` で選択した M0 のみを含む内容）
- `AGENTS.md`（CIコマンドは環境に応じて編集）

## Backlog update (agentic)
- docs と実装計画（`docs/10_IMPLEMENTATION_PLAN.md`）を読み、`backlog/issues/` に Issue ファイルを追加する作業はエージェントが指示を受けて実施する。
- 既存Issueは変更せず追記のみ。ID重複はスキップする。

## Wrap usage (agent instructions replacement)
- `ISSUEの起票`: Milestone（`docs/10_IMPLEMENTATION_PLAN.md`）から内容を推測し、通常Issueを `backlog/issues/M{N}/` に作成して `backlog/INDEX.md` を更新する。
- `ISSUEのインスタント起票`: Milestone推測を行わず、その場の指示を優先して通常Issueを起票する。
- `ISSUEの着手と実装`: 指定ISSUE-IDの `Scope` に沿って実装し、`実装 -> テスト -> 修復` を全Passまで反復する。
- `FINALIZATIONの起票`: `backlog/FINALIZATION-template.md` から `FINALIZATION-###` を作成し、`docs/ISSUE.md` / `docs/DEVFLOW.md` を満たす。
- `FINALIZATIONの実行`: 当該Milestoneの `FINALIZATION-###` 以外の全Issue完了を確認し、`docs/06_TESTING.md` / `docs/07_SECURITY.md` / `docs/08_RUNBOOK.md` 準拠で最終判定する。

Notes:
- M0（`M0-Integration` / `M0-Analysis`）では `FINALIZATION-###` を起票しない。
- Finalization完了後は同Milestoneへの新規Issue起票を原則禁止し、例外は `docs/09_DECISIONS.md` に理由を記録する。

## ISSUE-ID
- 各 Issue ファイルに `ISSUE-ID: <id>` を必ず付ける（重複発行防止）。
