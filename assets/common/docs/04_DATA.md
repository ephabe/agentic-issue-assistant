# Data Model

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Data model contract.
- エンティティ関係と制約を定義する。
- 認可、整合性、ライフサイクルを定義する。

## Out of scope
- 画面表示やUI文言の仕様はここに書かない。
- リリース手順や障害対応手順はここに書かない。

## Tables / Collections
### `<name>`
- Purpose: （このテーブル/コレクションの責務）
- Primary key: （主キー項目と採番方式）
- Ownership / tenant boundary: （データ所有者とテナント分離境界）
- Fields: （型 / nullable / default）
- Indexes: （検索・整列・一意性のためのインデックス）
- Constraints: （unique/check/fk）
- Relations: （1:1 / 1:N / N:N）
- Write rules: （誰がいつ更新できるか）
- Lifecycle: （作成条件、削除方針、保持期間）
- Sensitive data handling: （暗号化/マスキング）
- Notes: （補足事項、移行時の注意点）

## Derived / Computed data（必要な場合）
- Definition: （どのデータから算出するか）
- Refresh trigger: （いつ再計算するか）
- Consistency expectation: （整合性の期待値、反映遅延の許容範囲）

## Rules
- Authorization rules: （ロール/プランごとの参照・更新可否）
- Integrity rules: （不変条件、重複禁止、参照整合）
- Transaction boundary: （同時更新時の整合性保証）
- Plan differences: （Free/Pro/Enterprise など）
- Deletion / retention policy: （削除条件、保持期間、復元可否）
- Audit requirements: （変更履歴の記録対象）
