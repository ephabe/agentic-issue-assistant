#!/usr/bin/env bash
set -euo pipefail

FILE="${1:-backlog/issues.json}"

if ! command -v gh >/dev/null 2>&1; then
  echo "gh not found. Install GitHub CLI." >&2
  exit 1
fi
if ! command -v jq >/dev/null 2>&1; then
  echo "jq not found. Install jq." >&2
  exit 1
fi

gh auth status >/dev/null 2>&1 || echo "Warning: gh auth status failed. Run: gh auth login"

# Behavior:
# - Requires each item to have a stable `id`.
# - Prevents duplicates by searching existing issues for "BACKLOG_ID: <id>".
# - Prefixes title with "[<id>]" (unless already present).
# - Prepends marker line to body (unless already present).

jq -c '.[]' "$FILE" | while read -r it; do
  id=$(echo "$it" | jq -r '.id // empty')
  title=$(echo "$it" | jq -r '.title')
  body=$(echo "$it" | jq -r '.body')
  labels=$(echo "$it" | jq -r '.labels // [] | join(",")')

  if [ -z "$id" ] || [ "$id" = "null" ]; then
    echo "ERROR: missing required field: id (title=$title)" >&2
    exit 1
  fi

  marker="BACKLOG_ID: $id"

  # Skip duplicates by marker
  if gh issue list --state all --search ""$marker"" --json number -q '.[].number' | grep -Eq '^[0-9]+$'; then
    echo "skip (exists): $id $title"
    continue
  fi

  # Title prefix
  final_title="$title"
  if [[ "$final_title" != "[${id}]"* ]]; then
    final_title="[$id] $final_title"
  fi

  # Body marker
  final_body="$body"
  if ! printf "%s" "$final_body" | grep -Fq "$marker"; then
    final_body="$marker

$final_body"
  fi

  if [ -n "$labels" ]; then
    gh issue create --title "$final_title" --body "$final_body" --label "$labels"
  else
    gh issue create --title "$final_title" --body "$final_body"
  fi

  echo "created: $id $title"
done
