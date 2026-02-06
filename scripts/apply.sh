#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

show_help() {
  python3 "${SCRIPT_DIR}/apply.py" --help
  cat <<'EOF'
使い方:
  apply.sh [repo] [integration|analysis]
  apply.sh [integration|analysis]

引数を省略した場合:
  - repo: .
  - M0テンプレート: 対話で選択（非対話時は integration）
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  show_help
  exit 0
fi

REPO="."
M0_MODE=""

if [[ "${1:-}" == "integration" || "${1:-}" == "analysis" ]]; then
  M0_MODE="${1}"
elif [[ -n "${1:-}" ]]; then
  REPO="${1}"
fi

if [[ -n "${2:-}" ]]; then
  M0_MODE="${2}"
fi

if [[ -z "${M0_MODE}" ]]; then
  if [[ -t 0 ]]; then
    echo "M0テンプレートを選択してください。"
    select choice in "integration" "analysis"; do
      case "${choice}" in
        integration|analysis)
          M0_MODE="${choice}"
          break
          ;;
        *)
          echo "1 または 2 を選択してください。"
          ;;
      esac
    done
  else
    M0_MODE="integration"
    echo "M0テンプレート未指定のため、integration を使用します。"
  fi
fi

if [[ "${M0_MODE}" != "integration" && "${M0_MODE}" != "analysis" ]]; then
  echo "エラー: M0テンプレートは integration または analysis を指定してください。" >&2
  exit 2
fi

python3 "${SCRIPT_DIR}/apply.py" --repo "${REPO}" --m0 "${M0_MODE}"
