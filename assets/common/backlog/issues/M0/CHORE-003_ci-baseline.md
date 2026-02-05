# ISSUE-ID
- ISSUE-ID: CHORE-003

## Docs
- docs/DEVFLOW.md
- docs/06_TESTING.md
- docs/05_ARCH.md

## Goal
CI に最小限の品質ゲート（lint/typecheck/unit）を導入し、以後の Milestone で品質基準を担保できる状態にする。

## Acceptance Criteria
- [ ] lint / typecheck / unit が CI で実行され、失敗時に落ちる
- [ ] lint / typecheck / unit が CI で全て Pass する
- [ ] 実行コマンドが AGENTS.md / CI 設定に明記されている

## Tests
- 通常: `docs/06_TESTING.md` の標準チェック

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) CI ワークフローが実行され、lint/typecheck/unit が走ることを確認

## Notes
- 外部 API への直接アクセスは禁止（fixtures/mock を使用）
