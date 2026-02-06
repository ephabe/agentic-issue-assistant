# Issue Rules

## Defines
- Issue authoring and lifecycle rules.
- Issue起票、依存関係、完了判定の運用ルール
- ISSUE-ID 命名規約

## 起票ルール（1 Issue = 1ファイル）
- Issueファイルは `backlog/issues/M{N}/<ID>_<slug>.md` 形式で作成する。
- 一覧は `backlog/INDEX.md` に記載する。
- 通常Issueのテンプレートは `backlog/ISSUE-template.md` を使う。
- Milestone Finalization Issueのテンプレートは `backlog/FINALIZATION-template.md` を使う。
- すべてのIssueは `ISSUE-ID: <ID>` を含む。
- Issue本文は関連の深いDocsのみを引用・参照する。

## 依存関係と順序
- 通常Issueで前提がある場合は `前提ISSUE` セクションに `ISSUE-ID` を列挙する（複数可）。
- 着手前に `前提ISSUE` の完了を確認し、未完了なら先に前提Issueを消化する。

## NFR影響の扱い
- M1以降のIssueは `NFR影響` を補足情報として自然言語で記載する。
- M0（Repo bootstrap）のIssue（docs/AGENTS/CI整備）は `NFR影響` を省略できる。
- `NFR影響` に追加対応が必要と記載した場合は、内容に応じて追加ISSUEを起票する（`MVP-` に限らない）。
- 追加ISSUEの処理順が重要な場合は、`前提ISSUE` を指定したうえで起票する。
- Milestone締め時の品質最終判定は、Milestone Finalization Issue（`FINALIZATION-###`）で行う。

## Milestone Finalization Issue（特殊）
- M1以降の各Milestoneで、Milestone Finalization Issueを1件運用する。
- `ISSUE-ID` は `FINALIZATION-###` を使う。
- このIssueは Milestone を終了するときに取りかかる。
- 通常Issue消化中および Milestone Finalization Issue 実施中は、応急対応として `FIX-###` を追加起票できる。
- 前提ISSUEは「当該Milestoneの他Issueすべて」を固定とし、個別列挙しない。
- このIssueの完了をもって、当該Milestoneの完了とセキュリティ/品質担保とする。
- このIssueの完了後は、同Milestoneへの新規Issue起票を原則禁止とする。

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
