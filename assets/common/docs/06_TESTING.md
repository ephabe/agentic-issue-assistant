# Testing

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Testing and DoD contract.
- CI/Localで実施する検証範囲を定義する。
- テストデータと責務分担の方針を定義する。

## CI DoD (must)
- Required checks:
  - lint: （実行コマンドと対象範囲）
  - typecheck: （実行コマンドと対象範囲）
  - unit tests: （実行コマンド、対象モジュール、成功条件）
- Gate rule: （失敗時のマージ可否）
- Command source: （AGENTS.md / CI workflow に合わせる）

## CI rules
- External dependency policy: （外部API直接接続可否）
- Test data policy: （fixture/mock/seed）
- Ephemeral DB policy: （一時DB利用有無、初期化方法、破棄タイミング）
- Flaky test policy: （不安定テストの判定条件と対応手順）
- Retry policy（必要な場合）: （再実行回数、対象条件、記録方法）

## Local DoD
- Integration tests: （ローカルで実施する統合テストの範囲と手順）
- Real external connectivity checks: （実外部接続確認の対象と実施条件）
- Critical flows: （決済/Webhook/メール等）
- Manual verification checklist link: （`docs/08_RUNBOOK.md`）

## Test matrix
### `<scope>`
- Objective: （このテスト群で保証する目的）
- Test type: （unit/integration/e2e/manual）
- Environment: （実行環境。local/ci/staging など）
- Required data: （必要なfixture/mock/seedデータ）
- Pass criteria: （合格条件。件数、結果、失敗許容の有無）
