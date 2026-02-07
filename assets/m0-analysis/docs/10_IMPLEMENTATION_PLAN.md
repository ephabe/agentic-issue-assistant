# Implementation Plan

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Milestone delivery plan.
- 開発フェーズ単位である Milestone ごとの目的、完了条件、リスク、備考
- Milestone をIssue起票の起点として扱う

## Out of scope
- API/DB/実装コードの詳細設計はここに書かない。
- 未解決メモや調査ノートはここに書かず、`backlog/TODO.md` に記録する。

---

# M0-Analysis: Existing code analysis
## Purpose
- 既存ソースコードの実装事実を解析し、契約（docs/、AGENTS、テンプレ）へ反映して以後の改善を流せる状態にする

## Deliverables
- 既存実装の根拠に基づく docs/ 初版契約一式（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`ISSUE.md`、`README.md`）
- `AGENTS.md`（現状DoD・運用ルール反映）
- 既存CI/品質ゲートの現状整理と不足補完方針
- AGENTICな開発環境一式（既存実装に合わせた backlog 運用と Issue 実行導線）

## Exit criteria（Milestones完了条件）
- [ ] docs/ が既存実装の根拠に基づいて定義されている（00_PRD〜10_IMPLEMENTATION_PLAN、DEVFLOW、ISSUE、README）
- [ ] AGENTS.md がある（DoD定義）
- [ ] CIがエラーなく回る

## Risks
- 既存実装の読み違いで docs が実態と乖離する
- CIや運用ルールの現状把握が不足すると、M1以降のIssueが不正確になる

### Notes
- 既存コード解析の結果は、判断根拠を docs に残して追跡可能にする。
- 既知ギャップや未確定事項（TODO）は `backlog/TODO.md` に記録する。
- TODO は一次置き場として流動運用し、優先度と内容は随時更新する。
- 実装着手すると決めた TODO のみ Issue 化し、`backlog/INDEX.md` と `backlog/issues/` に反映する。
- 方針の選択や例外許容などの意思決定事項のみ `docs/09_DECISIONS.md` に記録する。

---

# M{N>=1}: {短いタイトル} ({任意: フェーズ/領域})
## Purpose
- {このマイルストーンで達成する成果物/ユーザー価値}
- {成果物/価値が複数ある場合は追加}

## Deliverables
- {成果物1}
- {成果物2}

## Requirements
- [ ] REQ-01: {要件}
- [ ] REQ-02: {要件}
- [ ] REQ-03: {要件}

## Exit criteria（Milestones完了条件）
- [ ] `Requirements` の全項目が、当該MilestoneのIssue群で網羅され起票済み
- [ ] 当該MilestoneのIssueがすべて完了している
- [ ] 当該Milestoneの Milestone Finalization Issue（`FINALIZATION-###`）が完了している
- [ ] {完了条件 / 受け入れ条件を追加する場合のみ記載}

### Notes
- このテンプレートブロックは M1以降のMilestoneで利用する。
- {前提条件 / 依存タスク / 外部調整}
- Milestone Finalization Issue（`FINALIZATION-###`）は当該Milestoneの他Issueすべてを前提とし、Milestone終了時に取りかかる。

---
