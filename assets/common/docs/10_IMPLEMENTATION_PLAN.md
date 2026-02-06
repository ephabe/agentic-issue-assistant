# Implementation Plan

## Defines
- Milestone delivery plan.
- Milestoneごとの目的、完了条件、リスク、備考
- Milestone計画をIssue起票の起点として扱う

---

# M0: Repo bootstrap
## Purpose
- 契約（docs/、AGENTS、テンプレ）を揃えて以後の実装を流せる状態にする

## Exit criteria（Milestones完了条件）
- [ ] docs/ の骨格が揃っている（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、ISSUE、README）
- [ ] AGENTS.md がある（DoD定義）
- [ ] CIが最低限回る開発環境構築
- [ ] `docs/07_SECURITY.md` に初版のセキュリティ要件が定義されている

## Risks
- Docs/DoD の合意が曖昧で以後のIssueがブレる
- M0でCIの最低限構成が整わない場合、実装フェーズの品質要件をIssueとして運用できない
- テンプレ/運用ルールの未整備で backlog が形骸化する

### Notes
- docs/ の骨格（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、ISSUE、README）とバックログ運用（ISSUE-template 等）を揃える。
- CIは lint / typecheck / unit が必ず走る最低限構成を前提にする。

---

# M{N}: {短いタイトル} ({任意: フェーズ/領域})
## Purpose
- {このマイルストーンで達成する成果物/ユーザー価値}
- {成果物/価値が複数ある場合は追加}

## Exit criteria（Milestones完了条件）
- [ ] 当該Milestoneの Milestone Finalization Issue（`FINALIZATION-###`）が完了している
- [ ] {完了条件 / 受け入れ条件を追加する場合のみ記載}

## Risks
- {技術/スケジュール/依存関係の不確実性}
- none

### Notes
- {前提条件 / 依存タスク / 外部調整}
- Milestone Finalization Issue（`FINALIZATION-###`）は当該Milestoneの他Issueすべてを前提とし、Milestone終了時に取りかかる。

---
