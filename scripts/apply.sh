#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  python3 "${SCRIPT_DIR}/apply.py" --help
  echo "Usage: apply.sh [safe|overwrite] [repo]"
  exit 0
fi

MODE="${1:-safe}"       # safe|overwrite
REPO="${2:-.}"          # target path

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "${SCRIPT_DIR}/apply.py" --mode "$MODE" --repo "$REPO"
