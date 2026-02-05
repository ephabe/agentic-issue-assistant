# Implementation Plan (Template)

このファイルは実装計画のテンプレート。具体的な内容は下記の記述例の形式に置き換えて記入する。

## Milestones

### M{N}: {短いタイトル} ({任意: フェーズ/領域})
Outcome:
- {このマイルストーンで達成する成果物/ユーザー価値}
- {成果物/価値が複数ある場合は追加}

Issues:
- [{ISSUE-ID}] {短い説明}
- [{ISSUE-ID}] {短い説明}

DoD impact (optional):
- CI: {追加/変更されるCI項目やテスト方針}
- Local: {手動検証やRunbook記載が必要な内容}

Risks (optional):
- {技術/スケジュール/依存関係の不確実性}
- none

Notes (optional):
- {前提条件 / 依存タスク / 外部調整}

---

## Sample (remove before real use)
以下は記述例。実運用時は必ず削除すること。

### M1: 認証導入 (Auth)
Outcome:
- ユーザーがログインできる
- 認証状態で基本画面が表示される

Issues:
- [MVP-010] auth: ログインAPI
- [MVP-011] ui: ログイン画面

DoD impact (optional):
- CI: auth関連のユニットテスト追加
- Local: RUNBOOK に手動ログイン確認を追記

Risks (optional):
- OAuth プロバイダの仕様変更リスク
