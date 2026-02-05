# Agentic開発フロー

## Defines
- End-to-end development flow.
- Milestone単位での運用ルール
- Issue起票と消化サイクルの原則

## 目的
- 先にDocsで合意・前提・仕様を固め、実装の迷いを減らす
- Implementation Plan を「計画の唯一の真実」にし、Issueを計画から起票する
- Issue駆動で実装・検証・マージを繰り返し、確実に前進する

## フロー概要
1. Docsを作り込む
2. `10_IMPLEMENTATION_PLAN.md` でMilestoneを定義する
3. Milestoneの内容から `backlog/issues/` に Issue を起票する
4. Milestoneごとに「統合ハードニングIssue」を1件起票する
5. Issueを消化する（ブランチ → 実装 → テスト → コミット → マージ）
6. Issueがなくなるまで 3-5 を繰り返す
7. Milestoneの Exit criteria と品質ゲートを評価し、すべて完了したら次のMilestoneへ

## Docsの作り込みルール
- まず `docs/` の章立て（00〜10）を埋める
- 章が大きくなる場合はディレクトリ化して細分化する
- ファイルを分割した場合は `docs/README.md` に追加する
- DocsはImplementation Plan / Issueの出典として必ず参照される
- この工程は Implementation Plan の M0（Repo bootstrap）に相当する

## Implementation Plan（Milestones）
- `10_IMPLEMENTATION_PLAN.md` にMilestoneを定義する
- Implementation PlanにはIssue一覧を記述しない
- Milestoneは目的・成果・DoD・リスクなど「計画の骨格」を定義する

## Issue起票（1 Issue = 1ファイル）
- Issueファイルは `backlog/issues/` に作成する
- 一覧は `backlog/INDEX.md` に記載する
- テンプレートは `backlog/ISSUE-template.md` を使う
- 形式は `backlog/issues/M{N}/<ID>_<slug>.md`
- すべてのIssueは `ISSUE-ID: <ID>` を含む
- Issue本文は関連の深いDocsを引用・参照する（最大3リンクまで）
- すべてのIssueに `NFR影響` を記載する（`none` / `security` / `observability` / `operability` / `multiple`）
- `NFR影響` が `none` 以外なら、同Milestoneの統合ハードニングIssueへ集約する

## 統合ハードニングIssue（Milestone単位）
- 各Milestoneで1件作成し、NFR影響ありの対応を集約する
- 代表例: セキュリティ要件の反映、監視/アラート整備、Runbook更新
- セキュリティ監査Issueは `SEC-###` プレフィックスを使用する
- Milestone完了条件として、このIssueの完了を必須にする

## Issue消化（実装サイクル）
1. Issueに対応するブランチを切る
2. 実装する
3. テスト・検証する
4. 完了でコミット & マージする

## Milestone運用ルール
- Issue発行と消化のループは、基本的にMilestone単位で行う
- 現在のMilestoneで新規に発行するIssueがなくなり、DoDと品質ゲートをすべて完了してはじめて次のMilestoneのIssue発行が可能になる

## GitHub Issue同期（任意）
- GitHub Issue の使用は必須ではない
- 付加要素として同期する場合は別途スクリプトを作成して運用する
