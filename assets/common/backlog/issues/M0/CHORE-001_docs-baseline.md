# ISSUE-ID
- ISSUE-ID: CHORE-001

## Docs
- docs/README.md
- docs/DEVFLOW.md
- docs/ISSUE.md
- docs/10_IMPLEMENTATION_PLAN.md
- docs/07_SECURITY.md

## Goal
M0 の前提として docs/ の初版契約（章立て + 初版内容）を整え、以後の Issue 起票と実装判断の基準を確定する。

## Scope
- `docs/` の章立て整備に加えて、各ドキュメントに初版内容を記載する（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`ISSUE.md`、`README.md`）。
- `docs/10_IMPLEMENTATION_PLAN.md` に M1以降のMilestoneを定義する（各Milestoneに Purpose / Exit criteria / Risks / Notes を記載）。
- `docs/07_SECURITY.md` に初版のセキュリティ要件を記載する（Security scope / Authentication / Data protection / Secrets / Security verification）。
- `docs/README.md` の目次と運用ルールを、実ファイル構成と整合させる。
- 非対象: アプリ実装、CI設定変更、テストコード追加、依存更新。

## 前提ISSUE（任意）
- none

## Acceptance Criteria
- [ ] docs/ に 00_PRD〜10_IMPLEMENTATION_PLAN と DEVFLOW.md, ISSUE.md, README.md が存在する
- [ ] docs/README.md に全ドキュメントが列挙されている（分割時は追記）
- [ ] 各ドキュメント先頭に `## Defines` があり、後続で追記可能
- [ ] `docs/10_IMPLEMENTATION_PLAN.md` に M1以降のMilestoneが定義され、各Milestoneに Purpose / Exit criteria / Risks / Notes が記載されている
- [ ] `docs/07_SECURITY.md` の初版要件（Security scope / Authentication / Data protection / Secrets / Security verification）が記載されている

## Tests
- なし（ドキュメントのみ）

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) docs/README.md に全ドキュメントが列挙されていることを確認

## Notes
- 章立てだけで完了にせず、Issue起票と実装判断に使える初版内容まで記載する
- 章が大きくなる場合はディレクトリ化して細分化し、分割時は `docs/README.md` に追記する
- Docsは Implementation Plan / Issue 起票の出典として参照できる状態を維持する
- このIssueは M0（Repo bootstrap）で先行して完了させる
