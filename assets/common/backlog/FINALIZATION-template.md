# ISSUE-ID
- ISSUE-ID: FINALIZATION-

## Docs
- docs/ISSUE.md
- docs/07_SECURITY.md
- docs/06_TESTING.md
- docs/08_RUNBOOK.md
- docs/10_IMPLEMENTATION_PLAN.md

## Milestone
- M{N}

## Goal
当該Milestoneを締めるために、セキュリティ/品質の最終確認を完了する。

## Scope
- 当該Milestone成果物の品質ゲート確認（Security / Observability / Operability）
- 既存Issueの未充足点があれば、Milestone内で解消して再確認する
- 非対象: 新規機能追加、大規模な仕様変更

## 前提ISSUE（固定）
- 当該Milestoneの他ISSUEすべて（個別列挙しない）

## Acceptance Criteria（Milestone Finalization条件）
- [ ] 当該Milestoneの他ISSUEがすべて完了している
- [ ] `docs/07_SECURITY.md` の該当要件が満たされている
- [ ] `docs/06_TESTING.md` のCI DoDが満たされている
- [ ] `docs/08_RUNBOOK.md` に必要な運用手順が反映されている
- [ ] 本Issueの完了をもって当該Milestone完了とする

## Tests
- `docs/06_TESTING.md` と `docs/08_RUNBOOK.md` に従って確認する

## DoD（完了判定）
- [ ] Acceptance Criteria をすべて満たす
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) セキュリティ/品質ゲートの確認結果を記録

## Notes
- 例外で同Milestoneに新規Issueを起票する場合は、理由を `docs/09_DECISIONS.md` に記録する
