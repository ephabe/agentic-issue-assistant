#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

show_help() {
  python3 "${SCRIPT_DIR}/apply.py" --help
  cat <<'EOF'
使い方:
  apply.sh [repo] [repo-integration|existing-code-analysis]
  apply.sh [repo] [integration|analysis]
  apply.sh [repo] ["Repo integration"|"Existing code analysis"]

引数を省略した場合:
  - repo: .
  - M0テンプレート: 対話で選択（非対話時は repo-integration）
EOF
}

normalize_mode() {
  local raw="${1:-}"
  local normalized="${raw,,}"
  local parts=()
  normalized="${normalized//_/ }"
  normalized="${normalized//-/ }"
  read -r -a parts <<<"${normalized}"
  normalized="${parts[*]}"

  case "${normalized}" in
    "repo integration"|"integration")
      echo "repo-integration"
      return 0
      ;;
    "existing code analysis"|"analysis")
      echo "existing-code-analysis"
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  show_help
  exit 0
fi

REPO="."
M0_MODE=""

if MODE="$(normalize_mode "${1:-}")"; then
  M0_MODE="${MODE}"
elif [[ -n "${1:-}" ]]; then
  REPO="${1}"
fi

if [[ -n "${2:-}" ]]; then
  if MODE="$(normalize_mode "${2}")"; then
    M0_MODE="${MODE}"
  else
    M0_MODE="${2}"
  fi
fi

if [[ -z "${M0_MODE}" ]]; then
  if [[ -t 0 ]]; then
    echo "M0テンプレートを選択してください。"
    select choice in "Repo integration" "Existing code analysis"; do
      case "${choice}" in
        "Repo integration")
          M0_MODE="repo-integration"
          break
          ;;
        "Existing code analysis")
          M0_MODE="existing-code-analysis"
          break
          ;;
        *)
          echo "1 または 2 を選択してください。"
          ;;
      esac
    done
  else
    M0_MODE="repo-integration"
    echo "M0テンプレート未指定のため、repo-integration（Repo integration）を使用します。"
  fi
fi

if MODE="$(normalize_mode "${M0_MODE}")"; then
  M0_MODE="${MODE}"
else
  echo "エラー: M0テンプレートは repo-integration / existing-code-analysis（または integration / analysis）を指定してください。" >&2
  exit 2
fi

python3 "${SCRIPT_DIR}/apply.py" --repo "${REPO}" --m0 "${M0_MODE}"
