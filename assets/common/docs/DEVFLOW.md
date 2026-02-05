# Agentic開発フロー（Actions内で実装まで完結）

目的：Issueをキューとして、Actionsで **N件だけ** 自動実装→PR作成→（必要なら自動修正）まで回す。人間は **開始ボタン** と **PRマージ** に集中する。

## 役割分担
### 人間
- docs/ と AGENTS.md を更新
- Issueを分解し、Goal/AC/Manual QA を整える（ローカル）
- `codex-ready` を付けて実行対象にする
- PRをレビューしてマージ
- 定期的にローカルで結合テスト→軌道修正

### 自動（Actions）
- `codex-ready` から最大N件を取り出し、実装してPRを作る
- CIが落ちたPRは自動で最大1回だけ修正を試す（無限ループ防止）
- ラベルで状態遷移を管理（running / pr-open / blocked / done）

## 初回セットアップ（ラベル作成）
Issue/PRラベルが未作成だとQueue/AutoFixが失敗する。最初に1回だけ実行：
- `bash scripts/gh/ensure_labels.sh`
