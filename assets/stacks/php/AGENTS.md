# AGENTS.md (PHP)

## Definition of Done (CI)
- composer lint
- composer typecheck
- composer test

## External dependencies policy
- 外部APIはテストで直接叩かない（fixtures/mock）
- 決済/Webhook/実外部疎通は docs/07_RUNBOOK.md で手動確認

## PR rules
- 1 PR = 1目的、差分は小さく
- 依存追加は理由と影響を書く
- 秘密情報をコミット/ログ出力しない

## Commands
- Install: composer install --no-interaction --prefer-dist
