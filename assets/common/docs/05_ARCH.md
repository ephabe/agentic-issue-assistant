# Architecture

## Defines
- Architecture boundary and dependency contract.
- 機能仕様ではなく「どこに置くか・どう依存するか」を定義する。
- モジュール配置と責務境界（domain/infra）
- 依存方向の制約と外部接続の集約方針
- Clean Architecture/DDD の採用方針と例外運用
- 再利用資産（component/type/helper/library）の共通化判断基準

## Boundaries
- domain/: （純粋ロジック、正規化、制約）
- infra/: （外部API、DB、キャッシュ、IO）

## Dependency policy
- domain -> infra 依存はなるべく持たない
- 外部APIは固有のServiceClientを作成して集約
- 依存逆転を使い、port(interface) は domain 側、実装は infra 側

## Domain modeling policy
- ビジネスルールは domain（Entity/ValueObject/DomainService）に置く
- ValueObject は不変（immutable）を原則とする
- 集約（Aggregate）ごとに整合性境界を定義し、更新責務を明確化する
- 集約間参照は ID 参照を原則とし、直接オブジェクト参照は避ける

## Pragmatic policy
- 小規模開発ではファイル同居を許容するが、責務と依存方向は維持する
- 先に分割しすぎず、変更頻度と複雑性に応じて段階的に分離する

## Reuse policy
- 対象は component / type file / helper / library とする
- Local first, shared later（共通配置は再利用が確認できてから）
- 2箇所目で共通化を検討し、3箇所目で共通化を原則とする
- 大部分が類似し、共通化で保守性や実装効率に優位が出る場合は共通部品化する
- 単一利用でも、可読性や実装効率に有意な効果があるならモジュール化を推奨する
- 1箇所専用で文脈依存が強い資産は共通配置に置かず、呼び出し元の近くに配置する
