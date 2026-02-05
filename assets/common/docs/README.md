# Docs Index

このディレクトリは「仕様＝契約」を置く。読み物ではなく、実装と検証の基準。

## まず読む（順番）
1) 00_PRD.md
2) 01_SCOPE.md
3) 02_UX.md
4) 03_API.md
5) 06_TESTING.md
6) 07_RUNBOOK.md

## ドキュメント一覧
- **00_PRD.md**: 目的 / MVP / 非ゴール / 成功条件 / TBD
- **01_SCOPE.md**: 機能一覧と優先度（MVP / Next / Later）
- **02_UX.md**: 画面、状態（loading/ok/error）、更新ポリシー
- **03_API.md**: API契約（入出力・エラー・キャッシュ・レート制限）
- **04_DATA.md**: データモデル（テーブル/制約/プラン差/認可）
- **05_ARCH.md**: 境界（domain/infra）、依存、キャッシュ、バックグラウンド更新
- **06_TESTING.md**: CI DoD / Local DoD、fixture/seed方針
- **07_RUNBOOK.md**: 手動スモーク、リリース前チェック、環境変数、障害対応
- **08_DECISIONS.md**: 決定ログ（日付・結論・理由だけ）
- **09_IMPLEMENTATION_PLAN.md**: 実装計画（マイルストーン/成果/Issue/DoD/リスク/備考）
- **DEVFLOW.md**: 開発フロー

## 運用ルール
### 変更時にどこを更新するか
- APIレスポンス/TTL/エラー → 03_API.md
- 画面状態/更新頻度 → 02_UX.md
- DB/制約/プラン差/認可 → 04_DATA.md
- CIで回す範囲/fixture/seed → 06_TESTING.md
- 手動スモーク → 07_RUNBOOK.md
- 判断が絡む変更 → 08_DECISIONS.md

### Issue/PRとの紐づけ
- Issue本文にISSUE-IDを記述し、backlogと関連づける
- Issue本文に該当Docsリンクを貼る（PRD/UX/API/DATA/TESTING）

### Issue-ID の命名ルール
- **必須**：`id` は一意で不変（発行後に変更しない）
- **重複防止**：GitHub Issue本文に `ISSUE-ID: <id>` を入れて照合
- **命名**：`<PREFIX>-<3桁>`（例：`MVP-001`）
- **PREFIXで分類**
    -   `MVP-###`：本筋（計画書に載る）
    -   `NEXT-###` / `V1-###` / `V2-###` ...：MVP後の計画機能
    -   `FIX-###`：バグ/機能抜け/CI補修（割り込み）
    -   `SPIKE-###`：調査/PoC
    -   `CHORE-###`：雑務（整備/依存更新）
    -   `OPS-###`：運用/監視/デプロイ
- **計画書との関係**
    -   計画書（09）は本筋（`MVP-*` や `V1-*`）のIDを列挙
    -   割り込み（`FIX-*`）は必要なら追記、基本はGitHub直で起票
