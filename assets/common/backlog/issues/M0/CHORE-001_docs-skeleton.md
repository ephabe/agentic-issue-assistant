# ISSUE-ID
- ISSUE-ID: CHORE-001

## Docs
- docs/README.md
- docs/DEVFLOW.md
- docs/ISSUE.md

## Goal
M0 の前提として docs/ の骨格を揃え、以後の Issue 起票と実装が迷わず進められる状態にする。

## Scope
- `docs/` の骨格整備のみを対象とする（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`ISSUE.md`、`README.md`）。
- `docs/README.md` の目次と運用ルールを、実ファイル構成と整合させる。
- 非対象: アプリ実装、CI設定変更、テストコード追加、依存更新。

## 前提ISSUE（任意）
- none

## Acceptance Criteria
- [ ] docs/ に 00_PRD〜10_IMPLEMENTATION_PLAN と DEVFLOW.md, ISSUE.md, README.md が存在する
- [ ] docs/README.md に全ドキュメントが列挙されている（分割時は追記）
- [ ] 各ドキュメント先頭に `## Defines` があり、後続で追記可能

## Tests
- なし（ドキュメントのみ）

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) docs/README.md に全ドキュメントが列挙されていることを確認

## Notes
- 内容は最小で良いが「空ファイル」にはしない
- Docs作り込みでは、`docs/` の章立て（`00_PRD.md`〜`10_IMPLEMENTATION_PLAN.md`、`DEVFLOW.md`、`ISSUE.md`、`README.md`）を揃える
- 章が大きくなる場合はディレクトリ化して細分化し、分割時は `docs/README.md` に追記する
- Docsは Implementation Plan / Issue 起票の出典として参照できる状態を維持する
- このIssueは M0（Repo bootstrap）で先行して完了させる
