# Architecture

## このドキュメントで定義すること
- domain / infra の責務境界
- 依存方向の制約と外部接続の集約方針
- キャッシュ戦略（key/TTL）

## Boundaries
- domain/: （純粋ロジック、正規化、制約）
- infra/: （外部API、DB、キャッシュ、IO）

## Dependency policy
- domain -> infra 依存を持たない
- 外部APIはclient 1箇所に集約

## Caching
- key設計
- TTL方針
