# Decisions

## GUIDE（作業用 / 最終稿では削除）
- この文書は作業中ガイドです。最終稿では削除します。
- 現在の本文は仮置きです。要件に合わせて変更・削除してください。
- 不要なレイヤーは削除せず `適用なし（N/A）` とし、`適用しない理由` と `再適用条件` を記載してください。
- 共通ルールは `docs/README.md` の「共通ガイド」を参照してください。

## Defines
- Key decision log.
- 変更後に確定した意思決定を記録する。
- 最低限「日付・結論・理由」を残す。

## Out of scope
- 未解決課題・保留アイデア・調査メモはここに書かない。
- 未解決事項は `backlog/TODO.md`（文脈依存の補足は各ドキュメントの `Open questions`）に記録する。

## Record template
### `YYYY-MM-DD <title>`
- Decision: （最終的に採用した方針・ルール）
- Reason: （採用理由と判断根拠）
- Impacted docs/code（必要な場合）: （影響を受けるドキュメントやコード）
- Supersedes（必要な場合）: `<old-title>`

## Supersession rule
- 以前の決定を置き換える場合は、旧決定に `superseded by <new-title>` を追記する。
