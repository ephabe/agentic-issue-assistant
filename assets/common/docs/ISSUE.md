# Issue Rules

## Defines
- Issue authoring and lifecycle rules.
- Issue起票、依存関係、完了判定の運用ルール
- ISSUE-ID 命名規約

## 起票ルール（1 Issue = 1ファイル）
- Issueファイルは `backlog/issues/M{N}/<ID>_<slug>.md` 形式で作成する。
- 一覧は `backlog/INDEX.md` に記載する。
- 通常Issueのテンプレートは `backlog/ISSUE-template.md` を使う。
- Milestone Finalization Issue（M1以降）のテンプレートは `backlog/FINALIZATION-template.md` を使う。
- すべてのIssueは `ISSUE-ID: <ID>` を含む。
- Issue本文の `Docs` には、`Goal` / `Scope` / `Acceptance Criteria` の判定に直接使うDocsに加えて、設計判断や依存関係の理解に必要な関連Docsも記載する。

## 通常Issue起票の起点（3種類）
- Milestone根拠: `docs/10_IMPLEMENTATION_PLAN.md` の進行中Milestone記述を根拠に分解して起票する。
- TODO根拠: `backlog/TODO.md` で「今やる」と決めた項目をIssue化して起票する。
- インスタント: その場の指示を直接Issue化して起票する。

## Issue所属Milestoneルール
- 通常Issueは、起票時点で進行中のMilestoneに必ず所属させる。
- 進行中Milestoneは `backlog/INDEX.md` の未完了（`[ ]`）Issueを持つ最小の `M{N}` とする。
- 未完了Issueが1件もない場合は、`docs/10_IMPLEMENTATION_PLAN.md` の定義順で次に着手するMilestoneを進行中とする。
- ユーザー指定が別Milestoneでも、起票先は進行中Milestoneに補正する。

## TODO と Issue の切り分け
- TODO（未着手候補・保留タスク）は `backlog/TODO.md` に記録する。
- TODO は一次置き場として流動運用し、追加・統合・分割・撤回を許容する。
- TODO は「今やる」と決まるまで Issue 化しない。
- 実装着手すると決めた時点で Issue 化し、`backlog/INDEX.md` と `backlog/issues/` に反映する。
- Issue 化した項目は `backlog/TODO.md` の `未起票` から `ISSUE起票済み` へ移動する（削除しない）。

## 依存関係と順序
- 通常Issueで前提がある場合は `前提ISSUE` セクションに `ISSUE-ID` を列挙する（複数可）。
- 着手前に `前提ISSUE` の完了を確認し、未完了なら先に前提Issueを消化する。

## NFR影響の扱い
- `NFR影響` は任意項目とし、必要な場合のみ補足情報として自然言語で記載する。
- `NFR影響` が不要な場合は省略できる。
- `NFR影響` に追加対応が必要と記載した場合は、内容に応じて追加ISSUEを起票する（`MVP-` に限らない）。
- 追加ISSUEの処理順が重要な場合は、`前提ISSUE` を指定したうえで起票する。
- M1以降のMilestone締め時の品質最終判定は、Milestone Finalization Issue（`FINALIZATION-###`）で行う。

## Milestone Finalization Issue（特殊）
- M1以降の各Milestoneで、Milestone Finalization Issueを1件運用する。
- M0-Integration / M0-Analysis では Milestone Finalization Issueを起票しない。
- `ISSUE-ID` は `FINALIZATION-###` を使う。
- このIssueは Milestone を終了するときに取りかかる。
- 通常Issue消化中および Milestone Finalization Issue 実施中は、応急対応として `FIX-###` を追加起票できる。
- 前提ISSUEは「当該Milestoneの `FINALIZATION-###` 以外の全Issue（`FIX-###` を含む）」を固定とし、個別列挙しない。
- 判定時点は、Finalization Issue を完了にする直前の最新状態とする（着手後に追加されたIssueも対象）。
- 判定対象Issueは `backlog/INDEX.md` に列挙し、完了時点で全件を完了状態（`[x]`）にする。
- 判定対象Issueが1件でも未完了なら、Finalization Issue を完了にしてはならない。
- このIssueの完了をもって、当該Milestoneの完了とセキュリティ/品質担保とする。
- このIssueの完了後は、同Milestoneへの新規Issue起票を原則禁止とする。
- 例外で同Milestoneに新規Issueを起票する場合は、理由を `docs/09_DECISIONS.md` に記録する。

## 完了判定
- 完了判定は各Issueの `Acceptance Criteria` と `DoD` を正とする。
- CI/Localのテスト方針と手順は `docs/06_TESTING.md` と `docs/08_RUNBOOK.md` を参照する。

## ISSUE-ID 命名ルール
- **必須**：`id` は一意で不変（発行後に変更しない）
- **重複防止**：Issue本文に `ISSUE-ID: <id>` を入れて照合
- **命名**：`<PREFIX>-<3桁>`（例：`MVP-001`）

分類:
- `MVP-###`：本筋（計画書に載る）
- `NEXT-###` / `V1-###` / `V2-###` ...：MVP後の計画機能
- `FIX-###`：バグ/機能抜け/CI補修（割り込み）
- `SEC-###`：セキュリティ監査/脆弱性対応
- `SPIKE-###`：調査/PoC
- `CHORE-###`：雑務（整備/依存更新）
- `OPS-###`：運用/監視/デプロイ
- `FINALIZATION-###`：Milestone Finalization（締め用）
