# Implementation Plan

## Defines
- Milestone delivery plan.
- Milestoneごとの目的、完了条件、リスク
- 全体で適用するDoD tiers（CI / Local）
- Implementation Plan には Issue 一覧を記述しない

## Global rules
- Issueファイルは `backlog/issues/M{N}/<ID>_<slug>.md`
- すべてのIssueは `ISSUE-ID: <ID>` を含む
- Issue本文は docs を参照する（最大3リンクまで）
- 各Milestoneで統合ハードニングIssueを1件作成し、NFR影響ありの項目を集約する
- セキュリティ監査の統合ハードニングIssueは `SEC-###` を使用する

## DoD tiers
- CI DoD: lint / typecheck / unit（CIで強制）
- Local DoD: 結合・実外部API・決済/Webhook（RUNBOOK参照）

## Milestone品質ゲート（横断品質ゲート）
- Security gate: `docs/07_SECURITY.md` の該当要件を満たす
- Observability gate: 主要シナリオの観測項目/閾値を定義し、`docs/08_RUNBOOK.md` に反映する
- Operability gate: デプロイ/ロールバック/Secrets変更手順を `docs/08_RUNBOOK.md` に反映する
- `NFR影響` が `none` 以外のIssueは、同Milestoneの統合ハードニングIssueで完了判定する

---

# M0: Repo bootstrap
## Purpose
- 契約（docs/、AGENTS、テンプレ）を揃えて以後の実装を流せる状態にする

## Exit criteria（Milestones完了条件）
- [ ] docs/ の骨格が揃っている（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、README）
- [ ] AGENTS.md がある（DoD定義）
- [ ] CIが最低限回る開発環境構築
- [ ] `docs/07_SECURITY.md` に初版のセキュリティ要件が定義されている

## Risks
- Docs/DoD の合意が曖昧で以後のIssueがブレる
- CI の最低限構成が整わず、実装フェーズの品質ゲートが機能しない
- テンプレ/運用ルールの未整備で backlog が形骸化する

### Notes
- このMilestonesは「最初に整えるべき契約」を固めるフェーズ。docs/ の骨格（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、README）とバックログ運用（ISSUE-template 等）を揃える。
- CIは lint / typecheck / unit が必ず走る最低限構成を想定し、以後のMilestoneで強化する。
- 以後の実装は M0 の成果を前提とするため、テンプレ/AGENTS/DoD と CI はここで固定化する。

---

# M{N}: {短いタイトル} ({任意: フェーズ/領域})
## Purpose
- {このマイルストーンで達成する成果物/ユーザー価値}
- {成果物/価値が複数ある場合は追加}

## Exit criteria（Milestones完了条件）
- [ ] {完了条件 / 受け入れ条件}
- [ ] {完了条件が複数なら追加}
- [ ] 統合ハードニングIssue（NFR影響あり項目を集約）が完了している
- [ ] Security gate: `docs/07_SECURITY.md` の該当要件を満たす
- [ ] Observability gate: 主要シナリオの観測項目/閾値を定義し、`docs/08_RUNBOOK.md` に反映する
- [ ] Operability gate: デプロイ/ロールバック/Secrets変更手順を `docs/08_RUNBOOK.md` に反映する

## Risks
- {技術/スケジュール/依存関係の不確実性}
- none

### Notes
- {前提条件 / 依存タスク / 外部調整}

---
