# Runbook

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Release and incident operations.
- デプロイ時チェック項目（Secrets/Webhook/監視）
- 障害時の一次切り分けと復旧手順

## Manual smoke (before release)
- （手動確認手順）

## Deployment checklist
- Secrets / env vars
- Webhook (if any)
- Monitoring (if any)

## Incident triage
- Logs
- Rollback
