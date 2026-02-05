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
- **DEVFLOW.md**: 開発フロー（Actions内で実装まで完結）

## 運用ルール
### 変更時にどこを更新するか
- APIレスポンス/TTL/エラー → 03_API.md
- 画面状態/更新頻度 → 02_UX.md
- DB/制約/プラン差/認可 → 04_DATA.md
- CIで回す範囲/fixture/seed → 06_TESTING.md
- 手動スモーク → 07_RUNBOOK.md
- 判断が絡む変更 → 08_DECISIONS.md

### Issue/PRのリンク
- Issue本文の先頭に該当Docsリンクを貼る（PRD/UX/API/DATA/TESTING）
