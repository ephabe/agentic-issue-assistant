#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, shutil, sys, pathlib

def find_conflicts(src: pathlib.Path, dst: pathlib.Path) -> list[pathlib.Path]:
    conflicts: list[pathlib.Path] = []
    for root, _, files in os.walk(src):
        for f in files:
            s = pathlib.Path(root) / f
            rel = s.relative_to(src)
            t = dst / rel
            if t.exists():
                conflicts.append(rel)
    return conflicts

def copy_tree(src: pathlib.Path, dst: pathlib.Path) -> list[str]:
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
            shutil.copy2(s, t)
            logs.append(f"write: {rel}")
    return logs

def main() -> int:
    p = argparse.ArgumentParser(description="Apply agentic-flow templates into a target repo.")
    p.add_argument("--repo", default=".", help="Target repository root")
    args = p.parse_args()

    skill_dir = pathlib.Path(__file__).resolve().parent.parent
    common = skill_dir / "assets" / "common"

    if not common.exists():
        print(f"ERROR: common assets not found: {common}", file=sys.stderr)
        return 2

    repo = pathlib.Path(args.repo).resolve()
    if not repo.exists():
        print(f"ERROR: repo not found: {repo}", file=sys.stderr)
        return 2

    conflicts = find_conflicts(common, repo)
    if conflicts:
        print("ERROR: destination already has existing template files. Aborting.", file=sys.stderr)
        for rel in conflicts[:2000]:
            print(f"exists: {rel}", file=sys.stderr)
        if len(conflicts) > 2000:
            print(f"... ({len(conflicts)-2000} more lines omitted)", file=sys.stderr)
        return 3

    logs = []
    logs += copy_tree(common, repo)

    print(f"Applied to {repo}")
    for line in logs[:2000]:
        print(line)
    if len(logs) > 2000:
        print(f"... ({len(logs)-2000} more lines omitted)")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
