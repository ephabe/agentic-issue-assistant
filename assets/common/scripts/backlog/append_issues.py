#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Any

REQUIRED_KEYS = {"id", "title", "body"}
OPTIONAL_KEYS = {"labels"}
ALLOWED_KEYS = REQUIRED_KEYS | OPTIONAL_KEYS


def load_json(path: pathlib.Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_issue(issue: Any) -> dict:
    if not isinstance(issue, dict):
        raise ValueError("issue must be an object")

    extra = set(issue.keys()) - ALLOWED_KEYS
    if extra:
        raise ValueError(f"issue has unsupported keys: {sorted(extra)}")

    missing = REQUIRED_KEYS - set(issue.keys())
    if missing:
        raise ValueError(f"issue is missing required keys: {sorted(missing)}")

    for key in ("id", "title", "body"):
        value = issue.get(key)
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string")

    issue_id = issue["id"].strip()
    title = issue["title"].strip()
    body = issue["body"].strip()

    if not (3 <= len(issue_id) <= 64):
        raise ValueError("id length must be between 3 and 64 characters")
    if len(title) < 3:
        raise ValueError("title length must be at least 3 characters")
    if len(body) < 10:
        raise ValueError("body length must be at least 10 characters")

    labels = issue.get("labels")
    if labels is not None:
        if not isinstance(labels, list):
            raise ValueError("labels must be an array of strings")
        if any(not isinstance(label, str) for label in labels):
            raise ValueError("labels must be an array of strings")

    issue["id"] = issue_id
    issue["title"] = title
    issue["body"] = body
    return issue


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Append new issues to backlog/issues.json with validation and deduplication."
    )
    parser.add_argument(
        "--backlog",
        default="backlog/issues.json",
        help="Path to existing backlog issues JSON (default: backlog/issues.json)",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to JSON array of new issues, or '-' for stdin",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and report without writing output",
    )
    args = parser.parse_args()

    backlog_path = pathlib.Path(args.backlog)
    if not backlog_path.exists():
        print(f"ERROR: backlog file not found: {backlog_path}", file=sys.stderr)
        return 2

    try:
        existing = load_json(backlog_path)
    except Exception as exc:  # pragma: no cover - diagnostic only
        print(f"ERROR: failed to read backlog JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(existing, list):
        print("ERROR: backlog JSON must be an array", file=sys.stderr)
        return 2

    existing_ids: set[str] = set()
    for item in existing:
        try:
            validated_existing = validate_issue(dict(item))
        except ValueError as exc:
            print(f"ERROR: invalid existing backlog item: {exc}", file=sys.stderr)
            return 2

        issue_id = validated_existing["id"]
        if issue_id in existing_ids:
            print(f"ERROR: duplicate id in existing backlog: {issue_id}", file=sys.stderr)
            return 2
        existing_ids.add(issue_id)

    if args.input == "-":
        try:
            incoming = json.load(sys.stdin)
        except Exception as exc:  # pragma: no cover - diagnostic only
            print(f"ERROR: failed to read input JSON: {exc}", file=sys.stderr)
            return 2
    else:
        input_path = pathlib.Path(args.input)
        if not input_path.exists():
            print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
            return 2
        try:
            incoming = load_json(input_path)
        except Exception as exc:  # pragma: no cover - diagnostic only
            print(f"ERROR: failed to read input JSON: {exc}", file=sys.stderr)
            return 2

    if isinstance(incoming, dict):
        incoming = [incoming]

    if not isinstance(incoming, list):
        print("ERROR: input JSON must be an array (or single object)", file=sys.stderr)
        return 2

    appended: list[dict] = []
    skipped: list[str] = []
    seen_new: set[str] = set()

    for raw_issue in incoming:
        try:
            issue = validate_issue(raw_issue)
        except ValueError as exc:
            print(f"ERROR: invalid issue: {exc}", file=sys.stderr)
            return 2

        issue_id = issue["id"]
        if issue_id in existing_ids or issue_id in seen_new:
            skipped.append(issue_id)
            continue

        seen_new.add(issue_id)
        appended.append(issue)

    if not appended:
        print("No new issues to append.")
        if skipped:
            print("Skipped existing/duplicate ids:")
            for issue_id in skipped:
                print(f"- {issue_id}")
        return 0

    merged = existing + appended

    if not args.dry_run:
        with backlog_path.open("w", encoding="utf-8") as f:
            json.dump(merged, f, ensure_ascii=False, indent=2)
            f.write("\n")

    print(f"Appended {len(appended)} issue(s) to {backlog_path}.")
    if skipped:
        print("Skipped existing/duplicate ids:")
        for issue_id in skipped:
            print(f"- {issue_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
