# ISSUE-ID
- ISSUE-ID: 

## Docs
（深い関連があるDocのみをLink）

## Goal
（何を実現するか。1文）

## Scope
（この機能を成立させるために必ず必要な変更）

## NFR影響（M1以降は必須）
- `none` | `security` | `observability` | `operability` | `multiple`
- M0（Repo bootstrap: docs/AGENTS/CI整備）のIssueでは省略可
- `none` 以外の場合: 同Milestoneの統合ハードニングIssueを記載（M1以降）
- `NFR影響 = security` の監査/ハードニングIssueは `SEC-###` を使用
- Hardening Issue: `<ISSUE-ID>`

## Acceptance Criteria（達成する機能要件）
- [ ] （CIで判定できる条件）
- [ ] （UI/API/型/エラーなど）

## Tests
- 通常: `docs/06_TESTING.md` の標準チェックを実施（失敗→修復→再実行を全 Pass まで繰り返す）
- 特殊: 必要な場合のみ追記（コマンド/前提/期待）

## DoD（完了判定）
- [ ] Acceptance Criteria をすべて満たす
- [ ] Testsを全 Pass（CI 含む）
- [ ] `NFR影響` を記載したIssueで、`none` 以外なら統合ハードニングIssueへ反映済み
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) （ローカル確認）

## Notes
（依存、制約、参考リンク）
