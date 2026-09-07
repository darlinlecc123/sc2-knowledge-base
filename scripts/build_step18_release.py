#!/usr/bin/env python3
"""步骤18：生成确定性的 minimal/full 本地发布包。不会调用外部 API。"""
from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
RELEASE_DATE = "2026-09-07"
PREFIX_MIN = f"storm-sc2kb-{VERSION}-minimal"
PREFIX_FULL = f"storm-sc2kb-{VERSION}-full"
ZIP_TIME = (2026, 9, 7, 0, 0, 0)

MINIMAL = (
    "VERSION", "CHANGELOG.md", "CITATION.cff", "LICENSE",
    "requirements-minimal.txt", "release/README_RELEASE.md",
    "docs/index.md", "docs/variable_catalog.md", "docs/dataflow.md",
    "docs/query_cookbook.md", "docs/glossary.md",
    "variables/raw_api.yaml", "variables/tbox.yaml", "variables/abox.yaml",
    "variables/derived.yaml", "variables/actions.yaml", "variables/swm.yaml",
    "variables/metrics.yaml", "schemas/variable.schema.json",
    "retrieval/aliases.yaml", "relations/variable_relations.jsonl",
    "known_issues.yaml", "src/sc2kb/__init__.py", "src/sc2kb/loader.py",
    "src/sc2kb/search.py", "src/sc2kb/cli.py",
)

FULL_TOP_LEVEL = {
    "config", "context", "docs", "evals", "lineage", "manifests", "prompts",
    "reports", "retrieval", "schemas", "scripts", "src", "taxonomy",
    "templates", "tests", "variables",
}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".jsonl", ".py", ".cff", ".txt"}
PRIVATE_PATTERNS = (
    (re.compile(r"C:\\Users\\18753", re.I), "private_windows_user_path"),
    (re.compile(r"D:\\anaconda3", re.I), "private_python_path"),
    (re.compile(r"sk-[A-Za-z0-9_-]{12,}"), "possible_api_key"),
    (re.compile(r"Bearer\s+[A-Za-z0-9._-]{12,}", re.I), "possible_bearer_token"),
    (re.compile(r"api[_-]?key\s*[:=]\s*[\"'][^$%{<][^\"']{7,}[\"']", re.I), "possible_literal_api_key"),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def remap(rel: str) -> str:
    return "README_RELEASE.md" if rel == "release/README_RELEASE.md" else rel


def sensitive_reason(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"VERSION"}:
        return "unsupported_or_binary_file"
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return "non_utf8_file"
    for pattern, reason in PRIVATE_PATTERNS:
        if pattern.search(text):
            return reason
    return None


def full_candidates() -> tuple[list[str], list[dict[str, str]]]:
    include = set(MINIMAL)
    excluded: list[dict[str, str]] = []
    fixed_exclusions = {
        "README.md": "outdated_workspace_readme",
        "reports/18_build_release_package.md": "outer_release_report_avoids_hash_cycle",
        "tests/validate_step16.py": "stale_planned_state_validator",
    }
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        parts = rel.split("/")
        if ".git" in parts:
            continue
        reason = None
        if rel in fixed_exclusions:
            reason = fixed_exclusions[rel]
        elif parts[0] in {"dist", "release"}:
            reason = "outer_release_artifact"
        elif "__pycache__" in parts or path.suffix.lower() == ".pyc":
            reason = "python_cache"
        elif parts[0] not in FULL_TOP_LEVEL and rel not in {
            "VERSION", "CHANGELOG.md", "CITATION.cff", "LICENSE",
            "requirements-minimal.txt", "known_issues.yaml",
        }:
            reason = "not_in_full_whitelist"
        elif parts[0] == "evals" and len(parts) > 1 and parts[1] in {"results", "analysis", "configs"}:
            reason = f"excluded_evaluation_{parts[1]}"
        elif path.name.lower().endswith(".log") or path.name.lower().startswith(".env"):
            reason = "secret_or_log_file"
        else:
            reason = sensitive_reason(path)
        if reason:
            if rel not in include:
                excluded.append({"path": rel, "reason": reason})
        else:
            include.add(rel)
    missing = [rel for rel in sorted(include) if not (ROOT / rel).is_file()]
    if missing:
        raise FileNotFoundError("缺少发布输入: " + ", ".join(missing))
    return sorted(include, key=remap), sorted(excluded, key=lambda x: x["path"])


def package_manifest(kind: str, entries: list[tuple[str, bytes]]) -> bytes:
    manifest = {
        "schema_version": "1.0.0",
        "package": f"storm-sc2kb-{VERSION}-{kind}",
        "version": VERSION,
        "release_date": RELEASE_DATE,
        "scope": "current STORM PySC2 Raw API variables and direct derivatives",
        "license_status": "Apache-2.0",
        "external_api_called": False,
        "uploaded": False,
        "files": [
            {"path": arc, "bytes": len(data), "sha256": sha256_bytes(data)}
            for arc, data in sorted(entries)
        ],
    }
    return (json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def write_zip(kind: str, rels: Iterable[str]) -> dict[str, object]:
    prefix = PREFIX_MIN if kind == "minimal" else PREFIX_FULL
    dest = ROOT / "dist" / f"{prefix}.zip"
    entries: list[tuple[str, bytes]] = []
    for rel in rels:
        arc = remap(rel)
        entries.append((arc, (ROOT / rel).read_bytes()))
    entries.sort()
    entries.append(("PACKAGE_MANIFEST.json", package_manifest(kind, entries)))
    entries.sort()
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for arc, data in entries:
            info = zipfile.ZipInfo(f"{prefix}/{arc}", ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            zf.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return {
        "kind": kind,
        "filename": dest.name,
        "bytes": dest.stat().st_size,
        "sha256": sha256_file(dest),
        "file_count": len(entries),
        "root_directory": prefix,
    }


def main() -> int:
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "release").mkdir(exist_ok=True)
    full, excluded = full_candidates()
    packages = [write_zip("minimal", MINIMAL), write_zip("full", full)]
    manifest = {
        "schema_version": "1.0.0",
        "release": {
            "name": "STORM PySC2 Raw API Variable Knowledge Base",
            "version": VERSION,
            "release_date": RELEASE_DATE,
            "knowledge_base": "storm-sc2kb-v1-raw",
            "formal_variable_count": 135,
            "relation_count": 1430,
            "known_issue_count": 11,
        },
        "scope": {
            "description": "Only variables used by the current STORM PySC2 Raw API path and direct derivatives.",
            "fact_statuses": ["design_intent", "code_reality", "runtime_observation", "needs_verification"],
        },
        "license_status": "Apache-2.0",
        "publication": {"repository": "https://github.com/darlinlecc123/sc2-knowledge-base", "uploaded": False, "external_account_accessed": False},
        "execution": {"external_api_called": False, "sc2_executed": False},
        "packages": packages,
        "minimal_source_files": list(MINIMAL),
        "full_source_file_count": len(full),
        "excluded_files": excluded,
        "security_policy": {
            "excluded": [".env", "API keys", "logs", "Python caches", "private absolute paths", "evals/results", "evals/analysis", "evals/configs"],
            "note": "The literal not-a-real-key in an offline test fixture is treated as a placeholder, but that test is excluded by the generic literal-key filter.",
        },
        "git_metadata_available": (ROOT / ".git").exists(),
    }
    manifest_path = ROOT / "release" / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sums = "".join(f"{p['sha256']}  {p['filename']}\n" for p in packages)
    (ROOT / "dist" / "SHA256SUMS").write_text(sums, encoding="utf-8", newline="\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
