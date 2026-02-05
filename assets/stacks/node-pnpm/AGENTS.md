# AGENTS.md (Node/pnpm)

## Definition of Done (CI)
- pnpm lint
- pnpm typecheck
- pnpm test

## External dependencies policy
- 外部APIはテストで直接叩かない（fixtures/mock）
- 決済/Webhook/実外部疎通は docs/07_RUNBOOK.md で手動確認

## 開発フロー
- 詳細は `docs/DEVFLOW.md` を参照
- Docs → `09_IMPLEMENTATION_PLAN.md` → `backlog/issues/`（1 Issue = 1ファイル）→ 実装/検証
- Issue発行/消化はMilestone単位で回す（Exit criteria 完了で次へ）

## Issue指定時の挙動
- 指定されたISSUE-IDの `backlog/issues/` を確認し、本文と参照Docsを読む
- 受け入れ条件/DoDが曖昧なら着手前に確認する
- 実装はIssueの範囲に限定し、CI DoDを満たす
- 仕様変更や追加対応が必要なら別Issueを提案する

## Commands
- Install: pnpm i --frozen-lockfile
- Dev: pnpm dev
