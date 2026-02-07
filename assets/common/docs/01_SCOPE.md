# Scope

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Feature scope contract.
- 実装対象となる機能範囲を定義する。
- スコープは検証可能な機能単位で定義する。

## Implementation Scopes
- `<scope title>`
  - Scope: （当該スコープで実装する内容）
  - References（optional）: （関連仕様）
- `ADMIN-USER-CRUD` 管理画面でユーザーをCRUDできる
  - Scope: 一覧表示、詳細表示、作成、編集、削除、入力バリデーション
  - References（optional）: `docs/02_UX.md`, `docs/03_API.md`, `docs/04_DATA.md`
- `FRONT-FLOWS` 主要導線でユーザー操作が完結できる
  - Scope: 一覧表示、詳細表示、検索/絞り込み、エラー表示、再試行導線を本番想定データ契約で確認可能
  - References（optional）: `docs/02_UX.md`, `docs/06_TESTING.md`
