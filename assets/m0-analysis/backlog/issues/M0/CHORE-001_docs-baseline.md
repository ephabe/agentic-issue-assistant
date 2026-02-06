# ISSUE-ID
- ISSUE-ID: CHORE-001

## Docs
- docs/README.md
- docs/DEVFLOW.md
- docs/ISSUE.md
- docs/10_IMPLEMENTATION_PLAN.md
- docs/07_SECURITY.md
- docs/09_DECISIONS.md

## Goal
M0-Analysis の前提として、既存ソースコードの実装事実を根拠に docs の初版契約（章立て + 初版内容）を整え、以後の Issue 起票と実装判断の基準を確定する。

## Scope
- `docs/` の章立て整備に加えて、各ドキュメントに初版内容を記載する（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`ISSUE.md`、`README.md`）。
- 既存実装の As-Is を docs に反映し、仕様との差分・未確定事項を明記する。
- `docs/10_IMPLEMENTATION_PLAN.md` に M1 以降のMilestoneを定義する（各Milestoneに Purpose / Exit criteria / Risks / Notes を記載）。
- `docs/07_SECURITY.md` に現状のセキュリティ要件と既知ギャップを記載する（Security scope / Authentication / Data protection / Secrets / Security verification）。
- `docs/README.md` の目次と運用ルールを、実ファイル構成と整合させる。
- 非対象: 大規模な実装改修、CI設定の全面刷新、依存更新の一括実施。

## 前提ISSUE（任意）
- none

## Acceptance Criteria
- [ ] docs/ に 00_PRD〜10_IMPLEMENTATION_PLAN と DEVFLOW.md, ISSUE.md, README.md が存在する
- [ ] docs/README.md に全ドキュメントが列挙されている（分割時は追記）
- [ ] 各ドキュメント先頭に `## Defines` があり、後続で追記可能
- [ ] `docs/10_IMPLEMENTATION_PLAN.md` に M1以降のMilestoneが定義され、各Milestoneに Purpose / Exit criteria / Risks / Notes が記載されている
- [ ] `docs/07_SECURITY.md` に現状要件（Security scope / Authentication / Data protection / Secrets / Security verification）と既知ギャップが記載されている
- [ ] 既存実装の重要仕様について、docs から追跡可能な根拠が示されている

## Tests
- なし（ドキュメントのみ）

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) docs/README.md に全ドキュメントが列挙されていることを確認
2) docs の主要記述が既存実装の挙動と矛盾しないことを確認

## Notes
- 推測で仕様を記述せず、根拠が曖昧な点は未確定事項として明示する
- 既知ギャップや例外判断は `docs/09_DECISIONS.md` に記録する
- このIssueは M0-Analysis で先行して完了させる
