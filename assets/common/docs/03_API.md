# API Contract

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- API interface contract.
- 対象APIの範囲（公開/内部、同期/非同期）
- 入出力スキーマとステータスコード
- エラー、再試行、キャッシュ、レート制限の運用ルール

## Conventions
- Base URL / versioning:
- Authentication:
- Content type:
- Timestamp / timezone format:
- Pagination / sorting / filtering:
- Error response format:
- Idempotency key policy（必要な場合）:

## Endpoints
### `<METHOD> <path>`
- Purpose: （このAPIの目的）
- Caller: （どの画面/機能から呼ばれるか）
- Auth: （認証/認可要件）
- Request path params:
- Request query params:
- Request headers:
- Request body:
- Response success status:
- Response success body:
- Errors（status + code + 条件）:
- Side effects: （更新対象、発火イベントなど）
- Idempotency / concurrency control:
- Caching policy:
- Rate limit:
- Timeout / retry policy:
- Observability: （ログ/メトリクス/トレース）
- Notes:

## Error catalog
### `<ERROR_CODE>`
- HTTP status:
- Meaning:
- Client action: （再試行/入力修正/再ログインなど）
- Server action: （アラート/調査要否）
