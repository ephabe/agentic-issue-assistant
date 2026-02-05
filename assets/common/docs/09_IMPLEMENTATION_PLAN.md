# Implementation Plan

この文書は「Milestones（開発単位の束）」を定義する。Issue本文の詳細は backlog/ に置く。
Implementation Plan には Issue 一覧を記述しない。

## Global rules
- Issueファイルは `backlog/issues/M{N}/<ID>_<slug>.md`
- すべてのIssueは `ISSUE-ID: <ID>` を含む
- Issue本文は docs を参照する（最大3リンクまで）

## DoD tiers
- CI DoD: lint / typecheck / unit（CIで強制）
- Local DoD: 結合・実外部API・決済/Webhook（RUNBOOK参照）

---

# M0: Repo bootstrap
## Purpose
- 契約（docs/、AGENTS、テンプレ）を揃えて以後の実装を流せる状態にする

## Exit criteria（Milestones完了条件）
- [ ] docs/ の骨格が揃っている
- [ ] AGENTS.md がある（DoD定義）
- [ ] CIが最低限回る開発環境構築

## Risks
- Docs/DoD の合意が曖昧で以後のIssueがブレる
- CI の最低限構成が整わず、実装フェーズの品質ゲートが機能しない
- テンプレ/運用ルールの未整備で backlog が形骸化する

### Notes
- このMilestonesは「最初に整えるべき契約」を固めるフェーズ。docs/ の骨格（00_PRD〜09_IMPLEMENTATION_PLAN、DEVFLOW、README）とバックログ運用（ISSUE-template 等）を揃える。
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

## Risks
- {技術/スケジュール/依存関係の不確実性}
- none

### Notes
- {前提条件 / 依存タスク / 外部調整}

---
