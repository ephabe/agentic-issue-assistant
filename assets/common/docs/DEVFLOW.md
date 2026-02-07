# Agentic開発フロー

## Defines
- End-to-end development flow.
- Milestone運用の最短手順
- SKILL操作とIssueサイクルの入口

## 目的
- 先にDocsで合意・前提・仕様を固め、実装の迷いを減らす
- TODO -> Issue -> 実装 -> Finalization の流れを標準化する
- SKILLによる操作補助で運用手順を統一する
- Issue駆動で実装・検証・マージを繰り返し、確実に前進する

## 運用原則
- 1時点で扱うMilestoneは、起票ルールにより1つに限定される。
- 通常Issueの起票ルートは「Milestone根拠 / TODO根拠 / インスタント」の3つを想定する。
- 起票先Milestoneの制約・補正ルールは `docs/ISSUE.md` の `Issue所属Milestoneルール` を正とする。
- TODOとIssueの切り分け・移動ルールは `backlog/TODO.md` と `docs/ISSUE.md` を正とする。

## SKILLによる操作補助
- この開発フローでは、`SKILL.md` で定義された次のアクションを利用できる。
- `todo-add`: 対話で必要情報を揃えて `backlog/TODO.md` の `未起票` に追加する。
- `issue-create-from-milestone`: Milestone根拠で通常Issueを起票する。
- `issue-create-from-todo`: TODO根拠で通常Issueを起票する。
- `issue-create-instant`: その場の指示から通常Issueを起票する。
- `issue-implement`: 指定Issueを実装し、`実装 -> テスト -> 修復` を反復する。
- `finalization-create`: M1以降のMilestone Finalization Issueを起票する。
- `finalization-execute`: Milestone Finalizationの最終判定を実行する。

## 初期配置後の最初のアクション
- M0 はインストール時に選択したテンプレート（`M0-Integration` または `M0-Analysis`）を起点に開始する。
- 選択した M0 の初期Issue（`CHORE-001`〜`CHORE-003`）を完了し、`docs/`、`AGENTS.md`、CI 基盤を整える。
- M0 では Milestone Finalization Issue（`FINALIZATION-###`）を起票しない。
- M0 完了までは M1以降のIssueを起票/着手しない。

## フロー（M1以降）
1. 対象Milestoneを1つ確定する。
2. 通常Issueを起票する（Milestone根拠 / TODO根拠 / インスタント）。
3. 必要なら追加Issueを起票する（`NFR影響` / 依存関係）。
4. 進行中Milestone内の `FINALIZATION-###` 以外のIssueを完了する。
5. `FINALIZATION-###` を1件起票する。
6. `FINALIZATION-###` を実行し、不足があれば修復する。
7. Finalization完了で当該Milestone完了とする。
8. 次のMilestoneへ進み、同じ手順を繰り返す。

## Issue起票の起点（通常Issue）
- Milestone根拠: `docs/10_IMPLEMENTATION_PLAN.md` の対象Milestone記述を分解して起票する。
- TODO根拠: `backlog/TODO.md` の `未起票` から選んでIssue化し、`ISSUE起票済み` へ移動する。
- インスタント: その場の指示を直接Issue化して起票する。
- 起票先Milestoneの決定・補正ルールは `docs/ISSUE.md` の `Issue所属Milestoneルール` を正とする。

## Finalization完了判定（迷い防止）
- 判定対象は同Milestoneの `FINALIZATION-###` 以外の全Issue（`FIX-###` を含む）。
- 判定時点は Finalization を完了にする直前の最新状態とする。
- 判定対象Issueは `backlog/INDEX.md` で全件完了（`[x]`）でなければならない。
- 1件でも未完了があれば Finalization は完了にしない。

## 詳細参照
- SKILLの操作定義は `SKILL.md` を参照する
- Issue起票ルールと判断基準の詳細は `docs/ISSUE.md` を参照する
- TODOの管理ルールは `backlog/TODO.md` を参照する
- 計画のテンプレートは `docs/10_IMPLEMENTATION_PLAN.md` を参照する
