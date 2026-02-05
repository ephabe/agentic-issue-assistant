# Agentic開発フロー

この文書は、Docs → 実装計画（Milestones）→ Issue起票 → 実装/検証 の一連の流れを定義する。

## 目的
- 先にDocsで合意・前提・仕様を固め、実装の迷いを減らす
- Implementation Plan を「計画の唯一の真実」にし、Issueを計画から起票する
- Issue駆動で実装・検証・マージを繰り返し、確実に前進する

## フロー概要
1. Docsを作り込む
2. `09_IMPLEMENTATION_PLAN.md` でMilestoneを定義する
3. Milestoneの内容から `backlog/issues/` に Issue を起票する
4. Issueを消化する（ブランチ → 実装 → テスト → コミット → マージ）
5. Issueがなくなるまで 3-4 を繰り返す
6. Milestoneの Exit criteria を評価し、すべて完了したら次のMilestoneへ

## Docsの作り込みルール
- まず `docs/` の章立て（00〜09）を埋める
- 章が大きくなる場合はディレクトリ化して細分化する
- 分割した場合は `docs/README.md` にリンクを追加する
- DocsはImplementation Plan / Issueの出典として必ず参照される
- この工程は Implementation Plan の M0（Repo bootstrap）に相当する

## Implementation Plan（Milestones）
- `09_IMPLEMENTATION_PLAN.md` にMilestoneを定義する
- Implementation PlanにはIssue一覧を記述しない
- Milestoneは目的・成果・DoD・リスクなど「計画の骨格」を定義する

## Issue起票（1 Issue = 1ファイル）
- Issueファイルは `backlog/issues/` に作成する
- 一覧は `backlog/INDEX.md` に記載する
- テンプレートは `backlog/ISSUE-template.md` を使う
- 形式は `backlog/issues/M{N}/<ID>_<slug>.md`
- すべてのIssueは `ISSUE-ID: <ID>` を含む
- Issue本文は関連の深いDocsを引用・参照する（最大3リンクまで）

## Issue消化（実装サイクル）
1. Issueに対応するブランチを切る
2. 実装する
3. テスト・検証する
4. 完了でコミット & マージする

## Milestone運用ルール
- Issue発行と消化のループは、基本的にMilestone単位で行う
- 現在のMilestoneで新規に発行するIssueがなくなり、DoDをすべて完了してはじめて次のMilestoneのIssue発行が可能になる

## GitHub Issue同期（任意）
- GitHub Issue管理は必須ではない
- 同期する場合は別途スクリプトを作成して運用する
