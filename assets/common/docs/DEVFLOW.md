# Agentic開発フロー

## Defines
- End-to-end development flow.
- Milestone単位での運用ルール
- Issue起票と消化サイクルの原則

## 目的
- 先にDocsで合意・前提・仕様を固め、実装の迷いを減らす
- Implementation Plan を「計画の唯一の参照元」とし、Issueを計画から起票する
- Issue駆動で実装・検証・マージを繰り返し、確実に前進する

## 初期配置後の最初のアクション
- `backlog/issues/M0/` の初期Issue（`CHORE-001`〜`CHORE-003`）を消化し、`docs/`、`AGENTS.md`、CI の基盤を整える
- M0の作業として `docs/10_IMPLEMENTATION_PLAN.md` に M1以降のMilestoneを定義する
- M0（Repo bootstrap）が完了するまで、M1以降のIssueは起票/着手しない

## フロー
1. 対象確定: 未完了の次Milestoneを1つだけ対象にする（複数Milestoneを同時に起票しない）
2. 初期起票: 対象Milestoneの通常Issueを起票する
3. 追加起票: `NFR影響` に追加対応が必要なら追加ISSUEを起票し、順序が必要なら `前提ISSUE` を指定する
4. Finalization起票: Milestone Finalization Issue（`FINALIZATION-###`）を1件起票する
5. 通常Issue消化: 対象Milestoneの通常Issueをすべて完了する（この間、応急対応として `FIX-###` の追加起票を許可する）
6. Finalization実施: 通常Issue完了後に Milestone Finalization Issue に着手する（この間も、応急対応として `FIX-###` の追加起票を許可する）
7. 完了確定: Milestone Finalization Issue の完了をもって当該Milestone完了とし、以後は同Milestoneへの新規Issue起票を原則禁止する
8. 反復: 次の未完了Milestoneへ進み、1〜7を繰り返す

## 詳細参照
- Issue起票ルールと判断基準の詳細は `docs/ISSUE.md` を参照する
- 計画のテンプレートは `docs/10_IMPLEMENTATION_PLAN.md` を参照する
