# ISSUE-ID
- ISSUE-ID: CHORE-002

## Docs
- docs/DEVFLOW.md
- docs/06_TESTING.md
- docs/08_RUNBOOK.md
- docs/07_SECURITY.md
- docs/09_DECISIONS.md

## Goal
AGENTS.md に DoD とエージェント運用ルールを明記し、既存コード解析を含む実装・検証の基準を固定する。

## Scope
- リポジトリ直下 `AGENTS.md` のテンプレート内容を、当該プロジェクトの運用ルールに合わせて整備する。
- CI DoD / Local DoD / Security 参照先を `docs/06_TESTING.md`、`docs/08_RUNBOOK.md`、`docs/07_SECURITY.md` と整合させる。
- 既存コード解析時の運用ルール（根拠明記、未確定事項の記録先）を明記する。
- 非対象: 本体機能の実装、CIワークフロー自体の実装、外部サービス疎通の実施。

## 前提ISSUE（任意）
- CHORE-001

## Acceptance Criteria
- [ ] リポジトリ直下に AGENTS.md が存在する
- [ ] CI DoD（lint/typecheck/unit）が明記され、`docs/06_TESTING.md` と整合する
- [ ] Local DoD（結合/外部API/決済等）の参照先が `docs/08_RUNBOOK.md` と整合する
- [ ] セキュリティ要件の参照先が `docs/07_SECURITY.md` と整合する
- [ ] 既存コード解析時のルール（根拠明記、未確定事項の記録）が明記されている

## Tests
- なし（ドキュメントのみ）

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) AGENTS.md を読み、DoD と運用ルールが矛盾していないことを確認

## Notes
- 具体的なコマンド名は CI/ツール構成に合わせて記載する
