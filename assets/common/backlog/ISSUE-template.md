# ISSUE-ID
- ISSUE-ID: 

## テンプレート用途
- 通常Issue用テンプレート
- Milestone Finalization Issueは `backlog/FINALIZATION-template.md` を使用

## Docs
- `Goal` / `Scope` / `Acceptance Criteria` の判定に直接使うDocに加えて、設計判断や依存関係の理解に必要な関連Docも記載する

## Goal
（何を実現するか。1文）

## Scope
（この機能を成立させるために必ず必要な変更）

## 前提ISSUE（任意）
- 前提がある場合は `ISSUE-ID` を1行ずつ列挙（複数可）
- 記法例: `- CHORE-010` / `- MVP-023`
- 前提がない場合は `none`

## NFR影響（任意）
- 列挙値（enum）で管理せず、補足情報として自然言語で記載する
- どのようなリスク・変更・追加対応の必要性があるかを簡潔に説明する
- 不要な場合は省略できる
- 複数Issueにまたがる追加対応が必要な場合は、内容に応じて追加ISSUEを起票する（`MVP-` に限らない）
- 追加ISSUEの処理順が重要な場合は、`前提ISSUE` を指定する
- 追加ISSUE: `<ISSUE-ID>`（必要な場合のみ）

## Acceptance Criteria（達成する機能要件）
- [ ] （CIで判定できる条件）
- [ ] （UI/API/型/エラーなど）

## Tests
- 通常: `docs/06_TESTING.md` の標準チェックを実施（失敗→修復→再実行を全 Pass まで繰り返す）
- 特殊: 必要な場合のみ追記（コマンド/前提/期待）

## DoD（完了判定）
- [ ] Acceptance Criteria をすべて満たす
- [ ] Testsを全 Pass（CI 含む）
- [ ] 前提ISSUEがある場合は、対象がすべて完了している
- [ ] `NFR影響` に追加対応が必要と記載した場合は、追加ISSUEを起票済みで、順序が必要なものは `前提ISSUE` で依存関係を定義している
- [ ] 影響範囲の Docs, backlog/INDEX を更新する

## Manual QA
1) （ローカル確認）

## Notes
（依存、制約、参考リンク）
