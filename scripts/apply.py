#!/usr/bin/env python3
from __future__ import annotations
import argparse
import os
import pathlib
import shutil
import sys


MODE_REPO_INTEGRATION = "repo-integration"
MODE_EXISTING_CODE_ANALYSIS = "existing-code-analysis"

MODE_LABELS = {
    MODE_REPO_INTEGRATION: "Repo integration",
    MODE_EXISTING_CODE_ANALYSIS: "Existing code analysis",
}

MODE_ALIASES = {
    "repo-integration": MODE_REPO_INTEGRATION,
    "repo integration": MODE_REPO_INTEGRATION,
    "integration": MODE_REPO_INTEGRATION,
    "existing-code-analysis": MODE_EXISTING_CODE_ANALYSIS,
    "existing code analysis": MODE_EXISTING_CODE_ANALYSIS,
    "analysis": MODE_EXISTING_CODE_ANALYSIS,
}


class JaArgumentParser(argparse.ArgumentParser):
    def format_usage(self) -> str:
        return super().format_usage().replace("usage: ", "使い方: ")

    def format_help(self) -> str:
        text = super().format_help()
        text = text.replace("usage: ", "使い方: ")
        text = text.replace("\noptions:\n", "\nオプション:\n")
        return text

    def error(self, _message: str) -> None:
        self.print_usage(sys.stderr)
        print("エラー: 引数が不正です。`--help` を参照してください。", file=sys.stderr)
        self.exit(2)

def build_file_map(sources: list[pathlib.Path]) -> dict[pathlib.Path, pathlib.Path]:
    file_map: dict[pathlib.Path, pathlib.Path] = {}
    for src in sources:
        for root, _, files in os.walk(src):
            for name in files:
                src_file = pathlib.Path(root) / name
                rel = src_file.relative_to(src)
                file_map[rel] = src_file
    return file_map

def find_conflicts(file_map: dict[pathlib.Path, pathlib.Path], dst: pathlib.Path) -> list[pathlib.Path]:
    conflicts: list[pathlib.Path] = []
    for rel in sorted(file_map.keys(), key=str):
        t = dst / rel
        if t.exists():
            conflicts.append(rel)
    return conflicts

def copy_files(file_map: dict[pathlib.Path, pathlib.Path], dst: pathlib.Path) -> list[str]:
    logs = []
    for rel in sorted(file_map.keys(), key=str):
        src_file = file_map[rel]
        t = dst / rel
        t.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, t)
        logs.append(f"書き込み: {rel}")
    return logs


def normalize_m0_mode(value: str) -> str | None:
    normalized = value.strip().lower().replace("_", " ").replace("-", " ")
    normalized = " ".join(normalized.split())
    if normalized in MODE_ALIASES:
        return MODE_ALIASES[normalized]
    normalized = normalized.replace(" ", "-")
    return MODE_ALIASES.get(normalized)

def main() -> int:
    p = JaArgumentParser(
        description="agentic-flow テンプレートを対象リポジトリへ適用します。",
        add_help=False,
    )
    p.add_argument("-h", "--help", action="help", help="このヘルプを表示して終了")
    p.add_argument("--repo", default=".", help="対象リポジトリのルートパス")
    p.add_argument(
        "--m0",
        default=MODE_REPO_INTEGRATION,
        help=(
            "M0テンプレート種別 "
            "（Repo integration / Existing code analysis。"
            "互換エイリアス: integration / analysis）"
        ),
    )
    args = p.parse_args()
    m0_mode = normalize_m0_mode(args.m0)
    if m0_mode is None:
        print(
            "エラー: --m0 は `repo-integration` / `existing-code-analysis` "
            "（または互換エイリアス `integration` / `analysis`）を指定してください。",
            file=sys.stderr,
        )
        return 2

    skill_dir = pathlib.Path(__file__).resolve().parent.parent
    common = skill_dir / "assets" / "common"
    analysis_overlay = skill_dir / "assets" / "m0-analysis"

    if not common.exists():
        print(f"エラー: 共通アセットが見つかりません: {common}", file=sys.stderr)
        return 2
    if m0_mode == MODE_EXISTING_CODE_ANALYSIS and not analysis_overlay.exists():
        print(f"エラー: Analysis用アセットが見つかりません: {analysis_overlay}", file=sys.stderr)
        return 2

    repo = pathlib.Path(args.repo).resolve()
    if not repo.exists():
        print(f"エラー: リポジトリが見つかりません: {repo}", file=sys.stderr)
        return 2

    sources = [common]
    if m0_mode == MODE_EXISTING_CODE_ANALYSIS:
        sources.append(analysis_overlay)
    file_map = build_file_map(sources)

    conflicts = find_conflicts(file_map, repo)
    if conflicts:
        print("エラー: 適用先に同名テンプレートファイルが既に存在するため中止しました。", file=sys.stderr)
        for rel in conflicts[:2000]:
            print(f"既存ファイル: {rel}", file=sys.stderr)
        if len(conflicts) > 2000:
            print(f"...（残り {len(conflicts)-2000} 行は省略）", file=sys.stderr)
        print("", file=sys.stderr)
        print("ファイルは一切変更していません。", file=sys.stderr)
        print("続行するには、上記の競合ファイルを削除または退避してから再実行してください。", file=sys.stderr)
        print("推奨手順（手動のみ）:", file=sys.stderr)
        print("  - 競合ファイルを削除: rm <repo>/<path>", file=sys.stderr)
        print("  - 競合ファイルを退避:", file=sys.stderr)
        print("      mkdir -p <repo>/.agentic-flow-backup", file=sys.stderr)
        print("      mv <repo>/<path> <repo>/.agentic-flow-backup/<path>", file=sys.stderr)
        print(f"対象リポジトリ: {repo}", file=sys.stderr)
        return 3

    logs = copy_files(file_map, repo)

    print(f"適用先: {repo}")
    print(f"M0テンプレート: {MODE_LABELS[m0_mode]} ({m0_mode})")
    for line in logs[:2000]:
        print(line)
    if len(logs) > 2000:
        print(f"...（残り {len(logs)-2000} 行は省略）")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
