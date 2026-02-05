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
- `docs/` 一式（PRD/Scope/UX/API/Data/Arch/Testing/Runbook/Decisions/Devflow）
- `.github/ISSUE_TEMPLATE/feature.md`
- `.github/pull_request_template.md`
- `backlog/issues.json` と `backlog/issues.schema.json`
- `scripts/gh/ensure_labels.sh`
- `scripts/gh/create_issues_from_backlog.sh`
- スタック別の `AGENTS.md` と `.github/workflows`（CI / Codex Queue / Codex AutoFix）

## GitHub scripts
- `scripts/gh/ensure_labels.sh` は `gh` CLI を使い、存在しないラベルを作成する。
- `scripts/gh/create_issues_from_backlog.sh` は `gh` + `jq` を使用し、`backlog/issues.json` から issue を作成する。
- `create_issues_from_backlog.sh` の挙動: `id` 必須、`ISSUE-ID: <id>` で重複検知、タイトルに `[id]` を付与、本文先頭にマーカーを追記。

## Backlog update (agentic)
- docs と実装計画（`docs/09_IMPLEMENTATION_PLAN.md`）を読み、`backlog/issues.json` に追記する作業はエージェントが実施する。
- 既存Issueは変更せず追記のみ。ID重複はスキップし、schemaを守る。
- 追記時の補助: `scripts/backlog/append_issues.py`（検証 + 重複排除）。

## Workflows (概要)
- Codex Queue: `codex-ready` の最古 issue を `parallel` 件取得し `codex-running` に移行、Codex 実行 → DoD 実行 → 変更があればドラフト PR 作成・`codex-pr-open` 付与・issue へ PR リンクコメント、変更が無ければ `codex-blocked`。
- Codex AutoFix: CI 失敗時に `codex-pr-open` の PR に対して 1 回だけ実行し、`autofix-1` を付与。
- CI: Node は `pnpm lint/typecheck/test`、PHP は `composer lint/typecheck/test` を前提。
- スタック別ランタイム: Node は Node 20 + pnpm 9、PHP は PHP 8.3 + composer v2。

## After applying
1) `bash scripts/gh/ensure_labels.sh`
2) Add GitHub Secret: `OPENAI_API_KEY`
3) Label a couple issues with `codex-ready`
4) Run workflow: `Codex Queue (Issue -> PR)` with parallel=2


## ISSUE-ID
- `backlog/issues.json` の各項目に `id` を必ず付ける（重複発行防止）。

## Notes / Known issues
- PHP overlay の `codex-queue.yml` / `codex-autofix.yml` に `- uses: # (no node setup for php)` の空ステップが含まれている。意図が無ければ削除が必要。
