# ISSUE-ID
- ISSUE-ID: CHORE-003

## Docs
- docs/DEVFLOW.md
- docs/06_TESTING.md
- docs/05_ARCH.md

## Goal
CI に最小限の品質ゲート（lint/typecheck/unit）を導入し、以後の Milestone で品質基準を担保できる状態にする。

## Scope
- CIで `lint / typecheck / unit` を実行し、失敗時にジョブを失敗させる最小構成を整備する。
- 実行コマンドと運用前提を `AGENTS.md` / CI設定に反映し、`docs/06_TESTING.md` と整合させる。
- 非対象: E2E導入、結合テスト基盤の構築、実外部APIへの接続を伴うテスト。

## 前提ISSUE（任意）
- CHORE-002

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
- このIssueは M0-Integration の初期Issueとして運用する
