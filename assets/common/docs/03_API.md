# API Contract

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- API interface contract.
- 入出力、ステータス、エラー契約を定義する。
- キャッシュ/再試行/レート制限の運用ルールを定義する。

## Out of scope
- 画面UXやコンポーネント設計の詳細はここに書かない。
- モジュール内部実装の詳細は、契約に影響しない限りここに書かない。

## Conventions
- Base URL / versioning: （ベースURL、バージョン付与方針）
- Authentication: （認証方式、トークン形式、必須ヘッダー）
- Content type: （受信/送信のMIMEタイプ）
- Timestamp / timezone format: （日時の形式とタイムゾーン）
- Pagination / sorting / filtering: （ページング、並び替え、絞り込みの仕様）
- Error response format: （エラーレスポンスの共通形式）
- Idempotency key policy（必要な場合）: （冪等キーの付与条件、有効範囲、有効期限）

## Endpoints
### `<METHOD> <path>`
- Purpose: （このAPIの目的）
- Caller: （どの画面/機能から呼ばれるか）
- Auth: （認証/認可要件）
- Request path params: （パラメータ名、型、必須/任意、制約）
- Request query params: （クエリ名、型、必須/任意、既定値）
- Request headers: （必須ヘッダー、任意ヘッダー、形式）
- Request body: （リクエスト構造、必須/任意、バリデーション）
- Response success status: （成功時HTTPステータス）
- Response success body: （成功時レスポンス構造）
- Errors（status + code + 条件）: （想定エラー一覧と発生条件）
- Side effects: （更新対象、発火イベントなど）
- Idempotency / concurrency control: （冪等性と同時更新制御の方法）
- Caching policy: （キャッシュ可否、TTL、無効化条件）
- Rate limit: （制限値、単位時間、超過時挙動）
- Timeout / retry policy: （タイムアウト値、再試行回数、バックオフ）
- Observability: （ログ/メトリクス/トレース）
- Notes: （補足、互換性の注意点）

## Error catalog
### `<ERROR_CODE>`
- HTTP status: （対応するHTTPステータス）
- Meaning: （エラーの意味と発生条件）
- Client action: （再試行/入力修正/再ログインなど）
- Server action: （アラート/調査要否）
