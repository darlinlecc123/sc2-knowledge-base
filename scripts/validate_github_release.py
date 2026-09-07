"""Validate the local GitHub publication boundary without network access."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "github" / "PUBLISH_ALLOWLIST.txt"
REQUIRED = [
    "github/README_GITHUB.md",
    "github/CONTRIBUTING.md",
    "github/ROADMAP.md",
    "github/ISSUE_TEMPLATE/variable_request.md",
    "github/ISSUE_TEMPLATE/bug_report.md",
    "github/PULL_REQUEST_TEMPLATE.md",
    "docs/wechat_article_draft.md",
    "reports/20_release_readiness.md",
]
DENIED_PARTS = {".git", "__pycache__", "results", "configs"}
DENIED_SUFFIXES = {".pyc", ".log", ".env"}
SECRET_PATTERNS = {
    "openai_style_key": re.compile(r"(?i)(?:sk|ds)-[A-Za-z0-9_-]{20,}"),
    "bearer_token": re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+/-]{20,}"),
    "assigned_secret": re.compile(r"(?i)(?:api[_-]?key|token|secret)\s*[:=]\s*['\"][^'\"]{12,}"),
    "private_windows_path": re.compile(r"(?i)[A-Z]:\\Users\\[^\\s]+"),
}
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".jsonl", ".py", ".cff"}


def load_entries() -> list[str]:
    return [
        line.strip().replace("\\", "/")
        for line in ALLOWLIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def expand(entries: list[str]) -> list[Path]:
    found: set[Path] = set()
    for entry in entries:
        candidate = (ROOT / entry).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError as exc:
            raise SystemExit(f"OUTSIDE_ROOT: {entry}") from exc
        if not candidate.exists():
            raise SystemExit(f"MISSING_ALLOWLIST_ENTRY: {entry}")
        if candidate.is_dir():
            found.update(
                p for p in candidate.rglob("*")
                if p.is_file()
                and not ({part.lower() for part in p.relative_to(ROOT).parts} & DENIED_PARTS)
                and p.suffix.lower() not in DENIED_SUFFIXES
                and p.name.lower() != ".env"
            )
        else:
            found.add(candidate)
    return sorted(found)


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    files = expand(load_entries())
    for file in files:
        rel = file.relative_to(ROOT)
        lowered_parts = {part.lower() for part in rel.parts}
        if lowered_parts & DENIED_PARTS:
            errors.append(f"denied path component: {rel.as_posix()}")
        if file.suffix.lower() in DENIED_SUFFIXES or file.name.lower() == ".env":
            errors.append(f"denied file type: {rel.as_posix()}")
        if file.suffix.lower() in TEXT_SUFFIXES:
            try:
                text = file.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                errors.append(f"not UTF-8: {rel.as_posix()}")
                continue
            for name, pattern in SECRET_PATTERNS.items():
                if pattern.search(text):
                    errors.append(f"{name}: {rel.as_posix()}")

    if errors:
        print("GITHUB_RELEASE_VALIDATION_FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("GITHUB_RELEASE_VALIDATION_OK")
    print(f"knowledge_root={ROOT}")
    print(f"allowlisted_files={len(files)}")
    print("outside_knowledge_files=0")
    print("network_accessed=false")
    print("uploaded=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
