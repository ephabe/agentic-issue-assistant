# Docs Index

## Defines
- Documentation contract index.
- このディレクトリは「仕様＝契約」を置く。読み物ではなく、実装と検証の基準。
- 各ドキュメントは先頭の `## Defines` で定義対象を明確にする。
- 各ドキュメントの `## Defines` 1行目は、短い英語の1文で記載する。

## ドキュメント一覧
- **00_PRD.md**: 概要 / 目的 / MVP / 非ゴール / 前提と制約 / 未決事項
- **01_SCOPE.md**: 機能一覧と優先度（MVP / Next / Later）
- **02_UX.md**: 画面、状態（loading/ok/error）、更新ポリシー
- **03_API.md**: API契約（入出力・エラー・キャッシュ・レート制限）
- **04_DATA.md**: データモデル（テーブル/制約/プラン差/認可）
- **05_ARCH.md**: 境界（domain/infra）、依存、ドメインモデリング、再利用配置ポリシー
- **06_TESTING.md**: CI DoD / Local DoD、fixture/seed方針
- **07_SECURITY.md**: セキュリティ要件（認証/認可、保護対象、Secrets、監査、検証）
- **08_RUNBOOK.md**: 手動スモーク、リリース前チェック、環境変数、障害対応
- **09_DECISIONS.md**: 決定ログ（日付・結論・理由だけ）
- **10_IMPLEMENTATION_PLAN.md**: 実装計画（マイルストーン/成果/DoD/リスク/備考）
- **DEVFLOW.md**: 開発フロー

## 運用ルール
### 変更時にどこを更新するか
- APIレスポンス/TTL/エラー → 03_API.md
- 画面状態/更新頻度 → 02_UX.md
- DB/制約/プラン差/認可 → 04_DATA.md
- 認証/認可/Secrets/脆弱性対応 → 07_SECURITY.md
- CIで回す範囲/fixture/seed → 06_TESTING.md
- 手動スモーク → 08_RUNBOOK.md
- 判断が絡む変更 → 09_DECISIONS.md

### ISSUE-ID の命名ルール
- **必須**：`id` は一意で不変（発行後に変更しない）
- **重複防止**：Issue本文に `ISSUE-ID: <id>` を入れて照合
- **命名**：`<PREFIX>-<3桁>`（例：`MVP-001`）
- **PREFIXで分類**
    -   `MVP-###`：本筋（計画書に載る）
    -   `NEXT-###` / `V1-###` / `V2-###` ...：MVP後の計画機能
    -   `FIX-###`：バグ/機能抜け/CI補修（割り込み）
    -   `SEC-###`：セキュリティ監査/ハードニング/脆弱性対応
    -   `SPIKE-###`：調査/PoC
    -   `CHORE-###`：雑務（整備/依存更新）
    -   `OPS-###`：運用/監視/デプロイ
- **計画書との関係**
    -   計画書（10）には Issue 一覧を記述しない
    -   Issue 一覧は `backlog/INDEX.md` に記載する
