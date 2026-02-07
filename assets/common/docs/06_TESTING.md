# Testing

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Testing and DoD contract.
- Local DoDに回す検証範囲（結合/E2E/実外部疎通）
- fixture/mock/seed の運用方針

## CI DoD (must)
- lint
- typecheck
- unit tests
（※コマンド名はAGENTS.md / CI workflowに合わせる）

## CI rules
- 外部APIへ直接接続しない（fixtures/mock）
- DBが必要なら「捨てDB + 最小seed」
- E2E/結合はLocal DoDへ

## Local DoD
- 結合テスト（開発環境前提）
- 実外部API疎通
- 決済/Webhook/メール等の疎通
