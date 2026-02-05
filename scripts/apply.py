#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, shutil, sys, filecmp, pathlib

def copy_tree(src: pathlib.Path, dst: pathlib.Path, mode: str) -> list[str]:
    logs = []
    for root, dirs, files in os.walk(src):
        rel_root = pathlib.Path(root).relative_to(src)
        for d in dirs:
            (dst / rel_root / d).mkdir(parents=True, exist_ok=True)
        for f in files:
            s = pathlib.Path(root) / f
            rel = s.relative_to(src)
            t = dst / rel
            t.parent.mkdir(parents=True, exist_ok=True)

            if mode == "safe" and t.exists():
                try:
                    if filecmp.cmp(s, t, shallow=False):
                        logs.append(f"skip (same): {rel}")
                    else:
                        logs.append(f"skip (exists): {rel}")
                except Exception:
                    logs.append(f"skip (exists): {rel}")
                continue

            shutil.copy2(s, t)
            logs.append(f"write: {rel}")
    return logs

def main() -> int:
    p = argparse.ArgumentParser(description="Apply agentic-flow templates into a target repo.")
    p.add_argument("--stack", choices=["node", "php"], default="node")
    p.add_argument("--mode", choices=["safe", "overwrite"], default="safe")
    p.add_argument("--repo", default=".", help="Target repository root")
    args = p.parse_args()

    skill_dir = pathlib.Path(__file__).resolve().parent.parent
    common = skill_dir / "assets" / "common"
    overlay = skill_dir / "assets" / "stacks" / ("node-pnpm" if args.stack == "node" else "php")

    if not common.exists():
        print(f"ERROR: common assets not found: {common}", file=sys.stderr)
        return 2
    if not overlay.exists():
        print(f"ERROR: overlay assets not found: {overlay}", file=sys.stderr)
        return 2

    repo = pathlib.Path(args.repo).resolve()
    if not repo.exists():
        print(f"ERROR: repo not found: {repo}", file=sys.stderr)
        return 2

    if not (repo / ".git").exists():
        print(f"WARNING: {repo} has no .git directory. If this is not the repo root, pass --repo <git-root>.")

    logs = []
    logs += copy_tree(common, repo, args.mode)
    logs += copy_tree(overlay, repo, args.mode)

    print(f"Applied stack={args.stack} mode={args.mode} to {repo}")
    for line in logs[:2000]:
        print(line)
    if len(logs) > 2000:
        print(f"... ({len(logs)-2000} more lines omitted)")

    print("\nNext:")
    print("- Create labels once: bash scripts/gh/ensure_labels.sh")
    print("- Add GitHub Secret OPENAI_API_KEY")
    print("- Add codex-ready to a few issues, then run Actions: Codex Queue")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
