# Security Requirements

## このドキュメントで定義すること
- 保護対象（ユーザーデータ、機密情報、決済情報など）
- 認証/認可の境界と権限制御
- データ保護、秘密情報管理、監査ログ要件
- セキュリティ検証とリリース判定条件

## Security scope
- 保護対象資産:
- 想定脅威:
- 守るべき要件（法令/規約/社内基準）:

## Authentication / Authorization
- 認証方式（例: session/JWT/OAuth）:
- 権限モデル（role/permission）:
- 認可チェックの実施箇所（API/DB/UI）:

## Data protection
- 機微データ分類（PII/決済/認証情報）:
- 保存時保護（暗号化、マスキング、保持期間）:
- 通信時保護（TLS、署名、検証）:

## Secrets / Key management
- Secretsの保管場所:
- ローテーション方針:
- ローカル/CI/本番での取り扱い差分:

## Application security controls
- 入力検証/出力エスケープ方針:
- 依存パッケージ脆弱性対応（SCA/更新ルール）:
- Abuse対策（rate limit、bot対策）:

## Audit / Monitoring
- 監査ログ対象（認証、権限変更、重要操作）:
- セキュリティアラート条件:
- 検知時の一次対応（Runbook参照）:

## Security verification
- CIで実施する検証（例: lint, test, dependency scan）:
- 手動確認項目（例: 権限境界、Secrets設定、監査ログ）:
- リリース判定基準（満たすべき最低条件）:
