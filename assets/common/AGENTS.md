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
- 決済/Webhook/実外部疎通は `docs/08_RUNBOOK.md` で手動確認
- セキュリティ要件は `docs/07_SECURITY.md` を参照して実装判断する

## Local DoD（手動）
- 結合テスト（開発環境前提）
- 実外部API疎通 / 決済 / Webhook / メール等は `docs/08_RUNBOOK.md` に従う

## 開発フロー
- 詳細は `docs/DEVFLOW.md` を参照
- `docs/10_IMPLEMENTATION_PLAN.md` → `backlog/issues/`（1 Issue = 1ファイル）→ 実装/検証
- Issue発行/消化はMilestone単位で回す（Exit criteria 完了で次へ）

## Issue指定時の挙動
- 指定されたISSUE-IDの `backlog/issues/` を確認し、本文と参照Docsを読む
- Issueの `前提ISSUE` があれば、すべて完了していることを確認する（未完了なら前提Issueを先に提案）
- `FINALIZATION-###`（Milestone Finalization Issue）は M1以降でのみ扱う（M0は対象外）
- `FINALIZATION-###`（Milestone Finalization Issue）の場合は、当該Milestoneの他Issueすべてが完了していることを確認する（個別列挙不要）
- 受け入れ条件/DoDが曖昧なら着手前に確認する
- 実装はIssueの範囲に限定し、CI DoDを満たす
- Issueの `NFR影響` に追加対応の必要性が記載されている場合は、追加ISSUEの起票と `前提ISSUE` 指定の要否を確認する
- `FINALIZATION-###` 完了後は、同Milestoneへの新規Issue起票を原則禁止とする
- 例外で同Milestoneに新規Issueを起票する場合は、理由を `docs/09_DECISIONS.md` に記録する前提で提案する
- テスト失敗時は修復して再実行し、全 Pass まで繰り返す
- 仕様変更や追加対応が必要なら別Issueを提案する

## Commands（環境に合わせて編集）
- Install: `<install-command>`
- Dev: `<dev-command>`（任意）
