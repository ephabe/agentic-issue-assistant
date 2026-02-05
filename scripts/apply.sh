#!/usr/bin/env bash
set -euo pipefail

STACK="${1:-node}"      # node|php
MODE="${2:-safe}"       # safe|overwrite
REPO="${3:-.}"          # target path

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "${SCRIPT_DIR}/apply.py" --stack "$STACK" --mode "$MODE" --repo "$REPO"
