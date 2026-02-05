# AGENTS.md

## このファイルについて
- この `AGENTS.md` はテンプレート
- CIコマンド（lint / typecheck / unit）はプロジェクト環境に合わせて必ず編集する

## Definition of Done (CI)
- `<lint-command>`
- `<typecheck-command>`
- `<unit-test-command>`

例:
- Node/pnpm: `pnpm lint` / `pnpm typecheck` / `pnpm test`
- PHP/composer: `composer lint` / `composer typecheck` / `composer test`

## External dependencies policy
- 外部APIはテストで直接叩かない（fixtures/mock）
- 決済/Webhook/実外部疎通は `docs/07_RUNBOOK.md` で手動確認
- セキュリティ要件は `docs/10_SECURITY.md` を参照して実装判断する

## Local DoD（手動）
- 結合テスト（開発環境前提）
- 実外部API疎通 / 決済 / Webhook / メール等は `docs/07_RUNBOOK.md` に従う

## 開発フロー
- 詳細は `docs/DEVFLOW.md` を参照
- `docs/09_IMPLEMENTATION_PLAN.md` → `backlog/issues/`（1 Issue = 1ファイル）→ 実装/検証
- Issue発行/消化はMilestone単位で回す（Exit criteria 完了で次へ）

## Issue指定時の挙動
- 指定されたISSUE-IDの `backlog/issues/` を確認し、本文と参照Docsを読む
- 受け入れ条件/DoDが曖昧なら着手前に確認する
- 実装はIssueの範囲に限定し、CI DoDを満たす
- Issueの `NFR影響` が `none` 以外なら、統合ハードニングIssueとの整合を確認する
- テスト失敗時は修復して再実行し、全 Pass まで繰り返す
- 仕様変更や追加対応が必要なら別Issueを提案する

## Commands（環境に合わせて編集）
- Install: `<install-command>`
- Dev: `<dev-command>`（任意）
