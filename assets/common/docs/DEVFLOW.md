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
- M0 は `M0-Integration`（新規構築向け）または `M0-Analysis`（既存コード解析向け）のどちらかを選んで開始する
- 選択した M0 の初期Issue（`CHORE-001`〜`CHORE-003`）を消化し、`docs/`、`AGENTS.md`、CI の基盤を整える
- M0-Integration / M0-Analysis では Milestone Finalization Issue（`FINALIZATION-###`）を起票しない
- 選択した M0 が完了するまで、M1以降のIssueは起票/着手しない

## フロー（M1以降）
1. 対象確定: 未完了の次Milestone（M1以降）を1つだけ対象にする（複数Milestoneを同時に起票しない）
2. 初期起票: 対象Milestoneの通常Issueを起票する
3. 追加起票: `NFR影響` に追加対応が必要なら追加ISSUEを起票し、順序が必要なら `前提ISSUE` を指定する
4. Finalization起票: Milestone Finalization Issue（`FINALIZATION-###`）を1件起票する
5. 通常Issue消化: 対象Milestoneの通常Issue（`FINALIZATION-###` 以外）をすべて完了する（この間、応急対応として `FIX-###` の追加起票を許可する）
6. Finalization実施: 通常Issue完了後に Milestone Finalization Issue に着手する（この間も、応急対応として `FIX-###` の追加起票を許可する。追加した `FIX-###` は Finalization 完了前に必ず完了させる）
7. 完了確定: Milestone Finalization Issue の完了をもって当該Milestone完了とし、以後は同Milestoneへの新規Issue起票を原則禁止する
8. 反復: 次の未完了Milestone（M1以降）へ進み、1〜7を繰り返す

## Finalization完了判定（迷い防止）
- 判定対象は、`backlog/issues/M{N}/` に存在する `FINALIZATION-###` 以外の全Issue（`FIX-###` を含む全Prefix）とする。
- 判定時点は、Finalization Issue を完了にする直前の最新状態とする（着手後に追加されたIssueも対象）。
- 完了時点で、判定対象Issueが `backlog/INDEX.md` に列挙され、すべて完了状態（`[x]`）であることを確認する。
- 判定対象Issueが1件でも未完了なら、Finalization Issue を完了にしてはならない。

## 詳細参照
- Issue起票ルールと判断基準の詳細は `docs/ISSUE.md` を参照する
- 計画のテンプレートは `docs/10_IMPLEMENTATION_PLAN.md` を参照する
