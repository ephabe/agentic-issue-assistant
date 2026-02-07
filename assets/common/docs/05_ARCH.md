# Architecture

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Architecture boundary and dependency contract.
- モジュール境界と依存方向を定義する。
- 共通化・分離の判断基準を定義する。

## Framework baseline
- Primary framework: （主軸フレームワーク名 / バージョン）
- Inheritance policy: 主軸フレームワークの公式アーキテクチャ方針を継承する。
- Project extensions: （本プロジェクトで追加するルールのみ記載）
- Deviation rule: 標準方針から逸脱する場合は理由と影響を `docs/09_DECISIONS.md` に記録する。

## Boundaries
### `<boundary/module>`
- Responsibility: （この境界の責務）
- Owned assets: （この境界が所有するデータ/コード）
- Entry points: （公開する入口。例: service/usecase/controller）
- Allowed dependencies: （依存してよい先）
- Key invariants: （この境界で守るべき不変条件）
- Notes: （補足）

### `domain/`
- Responsibility: 純粋ロジック、制約、正規化、ユースケースの意思決定
- Owned assets: Entity / ValueObject / DomainService / Port(interface)
- Entry points: UseCase / DomainService
- Allowed dependencies: 標準ライブラリ、共通型（契約済み）
- Key invariants: 集約整合性、入力制約、状態遷移ルール

### `infra/`
- Responsibility: 外部API、DB、キャッシュ、キュー、ファイルI/Oの実装
- Owned assets: Repository実装、ServiceClient、Gateway、Adapter
- Entry points: Port実装、Repository実装
- Allowed dependencies: 外部SDK、DBドライバ、HTTPクライアント
- Key invariants: I/O失敗時の一貫したエラー変換、リトライ/タイムアウト方針

## Dependency policy
- Allowed direction: 依存逆転を使い、domain は port(interface) へ依存し、infra はその実装を提供する。
- Forbidden direction: domain から infra への直接依存は禁止する。
- External integrations rule: 外部APIは固有の ServiceClient を作成して集約する。
- Interface ownership rule: port(interface) の定義は domain 側に置き、実装は infra 側に置く。

## Domain modeling policy
- Core invariants: ValueObject は不変（immutable）を原則とする。
- Model placement rule: ビジネスルールは domain（Entity/ValueObject/DomainService）に置く。
- Consistency boundary: 集約（Aggregate）ごとに整合性境界を定義し、更新責務を明確化する。
- Reference rule: 集約間参照は ID 参照を原則とし、直接オブジェクト参照は避ける。

## Pragmatic policy
- Co-location allowance: 小規模開発ではファイル同居を許容するが、責務と依存方向は維持する。
- Split trigger: 先に分割しすぎず、変更頻度と複雑性に応じて段階的に分離する。
- Refactor trigger: 責務の混在や依存方向の崩れが検知された時点で分離・再配置する。

## Reuse policy
- Reuse candidates: component / type file / helper / library を対象とする。
- Promote-to-shared trigger: Local first, shared later を原則とし、2箇所目の利用時点で共通化案を作成し、3箇所目の利用が確定した時点で共通部品化する。
- Shared component contract rule: 共通化は入力/出力/エラー仕様が同一の処理に限定する。
- Keep-local rule: 1箇所専用で文脈依存が強い資産は共通配置に置かず、呼び出し元の近くに配置する。
- Versioning / migration rule（必要な場合）: 既存利用先への影響を抑えるため、破壊的変更時は段階移行（互換期間を設ける）を原則とする。
