# ISSUE-ID
- ISSUE-ID: CHORE-001

## Docs
- docs/README.md
- docs/DEVFLOW.md
- docs/06_TESTING.md

## Goal
M0 の前提として docs/ の骨格を揃え、以後の Issue 起票と実装が迷わず進められる状態にする。

## Acceptance Criteria
- [ ] docs/ に 00_PRD〜09_IMPLEMENTATION_PLAN と DEVFLOW.md, README.md が存在する
- [ ] docs/README.md から全ドキュメントへのリンクがある（分割時は追記）
- [ ] 各ドキュメントに最小限の見出し・TBD があり、後続で追記可能

## Tests
- 通常: `docs/06_TESTING.md` の標準チェック

## DoD
- [ ] Acceptance Criteria をすべて満たす
- [ ] 標準チェックが全 Pass（CI 含む）
- [ ] 影響範囲の Docs/Notes を更新する

## Manual QA
1) docs/README.md のリンクから各ファイルを開けることを確認

## Notes
- 内容は最小で良いが「空ファイル」にはしない
