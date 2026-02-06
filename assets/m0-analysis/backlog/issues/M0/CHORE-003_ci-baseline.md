# ISSUE-ID
- ISSUE-ID: CHORE-003

## Docs
- docs/DEVFLOW.md
- docs/06_TESTING.md
- docs/05_ARCH.md
- docs/09_DECISIONS.md

## Goal
既存CIと品質ゲートの現状を可視化し、M1以降で運用可能な最小限の品質ゲート（lint/typecheck/unit）を確定する。

## Scope
- 既存CIにおける `lint / typecheck / unit` の実行可否を棚卸しし、`docs/06_TESTING.md` と整合させる。
- 実行コマンドと運用前提を `AGENTS.md` / CI設定に反映する。
- 不足している品質ゲートがある場合は追加ISSUEを起票し、依存関係を定義する。
- 非対象: E2E導入、結合テスト基盤の全面刷新、実外部APIへの接続を伴うテスト。

## 前提ISSUE（任意）
- CHORE-002

## Acceptance Criteria
- [ ] `lint / typecheck / unit` の現状（実行有無、実行経路、責務）が `docs/06_TESTING.md` に記載されている
- [ ] `lint / typecheck / unit` が CI で実行される、または不足項目について追加ISSUEが起票されている
- [ ] 実行コマンドが AGENTS.md / CI 設定に明記されている

## Tests
- 通常: `docs/06_TESTING.md` の標準チェック

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) CI ワークフローの現状と不足項目の扱いが docs/backlog と整合していることを確認

## Notes
- 外部 API への直接アクセスは禁止（fixtures/mock を使用）
