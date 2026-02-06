# Implementation Plan

## Defines
- Milestone delivery plan.
- Milestoneごとの目的、完了条件、リスク、備考
- Milestone計画をIssue起票の起点として扱う

---

# M0-Integration: Repo integration
## Purpose
- 契約（docs/、AGENTS、テンプレ）を揃えて以後の実装を流せる状態にする

## Exit criteria（Milestones完了条件）
- [ ] docs/ の初版契約が定義されている（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、ISSUE、README）
- [ ] AGENTS.md がある（DoD定義）
- [ ] CIが最低限回る開発環境構築
- [ ] `docs/07_SECURITY.md` に初版のセキュリティ要件が定義されている

## Risks
- Docs/DoD の合意が曖昧で以後のIssueがブレる
- M0-Integration でCIの最低限構成が整わない場合、実装フェーズの品質要件をIssueとして運用できない
- テンプレ/運用ルールの未整備で backlog が形骸化する

### Notes
- docs/ の初版契約（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、ISSUE、README）とバックログ運用（ISSUE-template 等）を揃える。
- CIは lint / typecheck / unit が必ず走る最低限構成を前提にする。

---

# M0-Analysis: Existing code analysis
## Purpose
- 既存ソースコードの実装事実を解析し、契約（docs/、AGENTS、テンプレ）へ反映して以後の改善を流せる状態にする

## Exit criteria（Milestones完了条件）
- [ ] docs/ の初版契約が既存実装の根拠に基づいて定義されている（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、ISSUE、README）
- [ ] AGENTS.md がある（DoD定義）
- [ ] 既存CIと品質ゲート（lint/typecheck/unit）の現状が定義され、必要な補完方針が明確になっている
- [ ] `docs/07_SECURITY.md` に現状のセキュリティ要件とギャップが定義されている

## Risks
- 既存実装の読み違いで docs が実態と乖離する
- CIや運用ルールの現状把握が不足すると、M1以降のIssueが不正確になる
- 既知ギャップが未整理のまま進み、後続の品質担保コストが増える

### Notes
- 既存コード解析の結果は、判断根拠を docs に残して追跡可能にする。
- 既知ギャップや未確定事項は `docs/09_DECISIONS.md` と backlog に記録する。

---

# M{N>=1}: {短いタイトル} ({任意: フェーズ/領域})
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
- このテンプレートブロックは M1以降のMilestoneで利用する。
- {前提条件 / 依存タスク / 外部調整}
- Milestone Finalization Issue（`FINALIZATION-###`）は当該Milestoneの他Issueすべてを前提とし、Milestone終了時に取りかかる。

---
