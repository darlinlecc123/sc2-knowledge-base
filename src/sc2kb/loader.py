"""加载步骤03/05/07/08/09生成的本地知识库产物。"""
from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

KNOWLEDGE_ROOT = Path(__file__).resolve().parents[2]
VARIABLE_FILES = ("raw_api", "tbox", "abox", "derived", "actions", "swm", "metrics")


@dataclass(frozen=True)
class KnowledgeBase:
    root: Path
    records: dict[str, dict[str, Any]]
    alias_records: dict[str, dict[str, Any]]
    alias_index: dict[str, dict[str, Any]]
    ambiguity_groups: dict[str, dict[str, Any]]
    relations: tuple[dict[str, Any], ...]
    outgoing: dict[str, tuple[dict[str, Any], ...]]
    incoming: dict[str, tuple[dict[str, Any], ...]]
    issues: dict[str, dict[str, Any]]
    variable_issue_index: dict[str, tuple[str, ...]]

    def record(self, variable_id: str) -> dict[str, Any] | None:
        return self.records.get(variable_id)

    def known_issues_for(self, variable_id: str) -> list[dict[str, Any]]:
        return [self.issues[i] for i in self.variable_issue_index.get(variable_id, ()) if i in self.issues]

    def upstream(self, variable_id: str) -> tuple[dict[str, Any], ...]:
        return self.incoming.get(variable_id, ())

    def downstream(self, variable_id: str) -> tuple[dict[str, Any], ...]:
        return self.outgoing.get(variable_id, ())


def _read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"缺少知识库上游文件: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"YAML 顶层必须是对象: {path}")
    return data


def load_knowledge_base(root: str | Path | None = None) -> KnowledgeBase:
    kb_root = Path(root).resolve() if root else KNOWLEDGE_ROOT
    records: dict[str, dict[str, Any]] = {}
    for name in VARIABLE_FILES:
        data = _read_yaml(kb_root / "variables" / f"{name}.yaml")
        for item in data.get("records", []):
            variable_id = item["id"]
            if variable_id in records:
                raise ValueError(f"重复变量 ID: {variable_id}")
            records[variable_id] = item

    aliases = _read_yaml(kb_root / "retrieval" / "aliases.yaml")
    alias_records = {x["variable_id"]: x for x in aliases.get("records", [])}
    alias_index = {x["normalized_term"]: x for x in aliases.get("alias_index", [])}
    ambiguity_groups = {x["id"]: x for x in aliases.get("ambiguity_groups", [])}

    relation_rows: list[dict[str, Any]] = []
    outgoing: dict[str, list[dict[str, Any]]] = defaultdict(list)
    incoming: dict[str, list[dict[str, Any]]] = defaultdict(list)
    relation_path = kb_root / "relations" / "variable_relations.jsonl"
    if not relation_path.exists():
        raise FileNotFoundError(f"缺少知识库上游文件: {relation_path}")
    with relation_path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                relation = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"关系 JSONL 第 {number} 行无效: {exc}") from exc
            relation_rows.append(relation)
            source_id = relation.get("source", {}).get("id")
            target_id = relation.get("target", {}).get("id")
            if source_id:
                outgoing[source_id].append(relation)
            if target_id:
                incoming[target_id].append(relation)

    known = _read_yaml(kb_root / "known_issues.yaml")
    issues = {x["id"]: x for x in known.get("issues", [])}
    issue_index = {x["variable_id"]: tuple(x.get("issue_ids", []))
                   for x in known.get("variable_issue_index", [])}

    sort_rel = lambda rows: tuple(sorted(rows, key=lambda x: x.get("id", "")))
    return KnowledgeBase(
        root=kb_root,
        records=dict(sorted(records.items())),
        alias_records=dict(sorted(alias_records.items())),
        alias_index=dict(sorted(alias_index.items())),
        ambiguity_groups=dict(sorted(ambiguity_groups.items())),
        relations=tuple(sorted(relation_rows, key=lambda x: x.get("id", ""))),
        outgoing={k: sort_rel(v) for k, v in sorted(outgoing.items())},
        incoming={k: sort_rel(v) for k, v in sorted(incoming.items())},
        issues=dict(sorted(issues.items())),
        variable_issue_index=dict(sorted(issue_index.items())),
    )
