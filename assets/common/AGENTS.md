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

## Wrap指示（ショートカット）
- `ISSUEの起票`: 対象Milestoneを特定し、Milestone内容から通常Issueを推測して起票する
- `ISSUEのインスタント起票`: Milestone推測を使わず、その場の指示に従って通常Issueを起票する
- `ISSUEの着手と実装`: 指定ISSUE-IDを起点に、Issue内容に従って実装を進める
- `FINALIZATIONの起票`: `FINALIZATION-###` を作成し、Milestone最終判定Issueを準備する
- `FINALIZATIONの実行`: `FINALIZATION-###` を実行し、Milestone完了判定を行う
- 上記ショートカットは、以下「Issue指定時の挙動」と `docs/ISSUE.md` / `docs/DEVFLOW.md` を必ず遵守して処理する

## Issue指定時の挙動
- 指定されたISSUE-IDの `backlog/issues/` を確認し、本文と参照Docsを読む
- Issueの `前提ISSUE` があれば、すべて完了していることを確認する（未完了なら前提Issueを先に提案）
- `FINALIZATION-###`（Milestone Finalization Issue）は M1以降でのみ扱う（M0-Integration / M0-Analysis は対象外）
- `FINALIZATION-###`（Milestone Finalization Issue）の判定対象は、当該Milestoneの `FINALIZATION-###` 以外の全Issue（`FIX-###` を含む）とする
- 判定時点は Finalization を完了にする直前の最新状態とし、着手後に追加されたIssueも対象に含める
- 判定対象Issueが `backlog/INDEX.md` に列挙され、`FINALIZATION-###` 以外がすべて完了状態（`[x]`）であることを確認する
- 判定対象Issueが1件でも未完了なら、Finalization を完了にしない
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
