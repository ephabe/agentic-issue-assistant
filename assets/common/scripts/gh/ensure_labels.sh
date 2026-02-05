#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "gh not found. Install GitHub CLI." >&2
  exit 1
fi

gh auth status >/dev/null 2>&1 || echo "Warning: gh auth status failed. Run: gh auth login"

create_label () {
  local name="$1"
  local color="$2"
  local desc="$3"
  if gh label list --json name -q '.[].name' | grep -Fxq "$name"; then
    echo "label exists: $name"
    return
  fi
  gh label create "$name" --color "$color" --description "$desc" || true
  echo "label ensured: $name"
}

create_label "codex-ready"   "0e8a16" "Ready for Codex Queue"
create_label "codex-running" "fbca04" "Being processed by Codex Queue"
create_label "codex-pr-open" "1d76db" "Codex created a PR"
create_label "codex-blocked" "b60205" "Blocked; needs human triage"
create_label "codex-done"    "5319e7" "Done / merged"
create_label "autofix-1"     "c2e0c6" "AutoFix attempted once"
create_label "from-backlog" "0366d6" "Created from backlog/issues.json"
