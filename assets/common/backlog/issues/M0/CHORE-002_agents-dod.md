# ISSUE-ID
- ISSUE-ID: CHORE-002

## Docs
- docs/06_TESTING.md
- docs/07_RUNBOOK.md
- docs/DEVFLOW.md

## Goal
AGENTS.md に DoD とエージェント運用ルールを明記し、実装・検証の基準を固定する。

## Acceptance Criteria
- [ ] リポジトリ直下に AGENTS.md が存在する
- [ ] CI DoD（lint/typecheck/unit）が明記され、`docs/06_TESTING.md` と整合する
- [ ] Local DoD（結合/外部API/決済等）の参照先が `docs/07_RUNBOOK.md` と整合する
- [ ] Issue 実装時のテスト実行と修復の基本方針が明記されている

## Tests
- 通常: `docs/06_TESTING.md` の標準チェック

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 標準チェックが全 Pass（CI 含む）
- [ ] 影響範囲の Docs/Notes を更新する

## Manual QA
1) AGENTS.md を読み、DoD と運用ルールが矛盾していないことを確認

## Notes
- 具体的なコマンド名は CI/ツール構成に合わせて記載する
