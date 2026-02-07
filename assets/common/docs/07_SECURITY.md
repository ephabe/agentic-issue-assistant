# Security Requirements

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Security requirements baseline.
- 認証/認可とデータ保護の要件を定義する。
- 検証・監査・リスク処理の基準を定義する。

## Out of scope
- 詳細な脅威分析や監査証跡設計の詳細はここに書かない。
- インシデント運用の詳細手順は `docs/08_RUNBOOK.md` に記載する。

## Security scope
- Protected assets: （保護対象資産）
- Access model: （認証/認可方式と適用範囲）
- Data sensitivity: （機微データの有無・分類）

## Required controls（must）
- Input/output handling: （入力検証・出力エスケープ）
- Secret handling: （シークレット保管場所・取り扱い）
- Dependency policy: （依存脆弱性の検知と更新方針）
- Transport/storage protection: （通信時・保存時の保護方針）

## Security verification
- CI checks: （最低限の自動検証）
- Pre-release manual checks: （手動確認項目）
- Release gate: （重大リスク時のリリース可否）

## Incident handling（必要な場合）
- First response: （初動対応）
- Communication rule: （影響共有ルール）
- Record location: （記録先。`docs/08_RUNBOOK.md`）
