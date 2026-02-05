# Agentic Flow Installer Skill

Applies a shared docs/templates skeleton plus a stack-specific overlay (node/pnpm or php/composer).

## Manual usage
```bash
bash ~/.codex/skills/agentic-flow-installer/scripts/apply.sh node safe .
bash ~/.codex/skills/agentic-flow-installer/scripts/apply.sh php safe .
```

## After applying
1) `bash scripts/gh/ensure_labels.sh`
2) Add GitHub Secret: `OPENAI_API_KEY`
3) Label a couple issues with `codex-ready`
4) Run workflow: `Codex Queue (Issue -> PR)` with parallel=2


## Backlog ID
- `backlog/issues.json` の各項目に `id` を必ず付ける（重複発行防止）。
