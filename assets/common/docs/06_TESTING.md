# Testing

## このドキュメントで定義すること
- CIで必須とする検証項目（lint/typecheck/unit）
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
