#!/usr/bin/env python3
"""步骤18本地发布包验收；纯离线，不调用模型或SC2。"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "release" / "MANIFEST.json"
BANNED_PARTS = {"__pycache__", "results", "analysis", "configs"}
BANNED_SUFFIXES = {".pyc", ".log", ".pem", ".key"}
BANNED_PATTERNS = (
    re.compile(r"C:\\Users\\18753", re.I),
    re.compile(r"D:\\anaconda3", re.I),
    re.compile(r"sk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{12,}", re.I),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_archive(package: dict) -> None:
    archive = ROOT / "dist" / package["filename"]
    assert archive.is_file(), archive
    assert sha256(archive.read_bytes()) == package["sha256"]
    with zipfile.ZipFile(archive) as zf:
        names = zf.namelist()
        assert len(names) == package["file_count"]
        root = package["root_directory"] + "/"
        assert all(name.startswith(root) for name in names)
        pm_name = root + "PACKAGE_MANIFEST.json"
        pm = json.loads(zf.read(pm_name).decode("utf-8"))
        expected = {item["path"]: item for item in pm["files"]}
        for rel, item in expected.items():
            data = zf.read(root + rel)
            assert len(data) == item["bytes"]
            assert sha256(data) == item["sha256"]
        assert len(expected) + 1 == len(names)
        for name in names:
            rel = name[len(root):]
            parts = set(PurePosixPath(rel).parts)
            assert not (parts & BANNED_PARTS), name
            assert PurePosixPath(rel).suffix.lower() not in BANNED_SUFFIXES, name
            data = zf.read(name)
            if PurePosixPath(rel).suffix.lower() in {".md", ".yaml", ".yml", ".json", ".jsonl", ".py", ".cff", ".txt"} or rel in {"VERSION"}:
                text = data.decode("utf-8")
                for pattern in BANNED_PATTERNS:
                    assert not pattern.search(text), f"{name}: {pattern.pattern}"


def smoke_minimal(package: dict) -> dict:
    archive = ROOT / "dist" / package["filename"]
    verify_root = ROOT / "release" / "_verify"
    verify_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="step18_", dir=verify_root) as tmp:
        tmp_path = Path(tmp).resolve()
        assert verify_root.resolve() in tmp_path.parents
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(tmp_path)
        package_root = tmp_path / package["root_directory"]
        proc = subprocess.run(
            [sys.executable, "src/sc2kb/cli.py", "单位当前血量对应哪个字段", "--limit", "8", "--json"],
            cwd=package_root, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True,
        )
        result = json.loads(proc.stdout)
        ids = [x["variable_id"] for x in result["results"]]
        assert result["status"] == "found"
        assert "raw_unit.health" in ids
        return {"status": result["status"], "first": ids[0], "contains_raw_unit_health": True}


def main() -> int:
    assert (ROOT / "VERSION").read_text(encoding="utf-8").strip() == "0.1.0"
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    assert citation["cff-version"] == "1.2.0"
    assert citation["version"] == "0.1.0"
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["license_status"] == "Apache-2.0"
    assert manifest["publication"]["uploaded"] is True
    assert manifest["publication"]["external_account_accessed"] is True
    assert manifest["execution"]["external_api_called"] is False
    assert len(manifest["packages"]) == 2
    for package in manifest["packages"]:
        verify_archive(package)
    minimal = next(x for x in manifest["packages"] if x["kind"] == "minimal")
    smoke = smoke_minimal(minimal)
    print("STEP18 VALIDATION OK")
    print(f"packages={len(manifest['packages'])}")
    print(f"minimal_smoke={json.dumps(smoke, ensure_ascii=False)}")
    print("external_api_called=false")
    print("sc2_executed=false")
    print("source_repository_uploaded=true")
    print("release_archives_uploaded=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
