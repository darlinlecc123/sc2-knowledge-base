"""确定性的本地变量检索：精确、规范化、包含、模糊四级。"""
from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from typing import Any

from .loader import KnowledgeBase, load_knowledge_base

_GENERIC = {
    "是什么", "什么", "含义", "变量", "查询", "请问", "请", "查找", "对应", "接口", "代码",
    "where", "what", "meaning", "variable",
}


def normalize(text: str, code_sensitive: bool = False) -> str:
    """将自然语言/代码查询转换为稳定的匹配形式。"""
    value = unicodedata.normalize("NFKC", str(text)).casefold().strip()
    if not code_sensitive:
        value = re.sub(r"[_\-]+", " ", value)
    value = re.sub(r"[，。！？、；：,!?;:\"'(){}]+", " ", value)
    return " ".join(value.split())


def _compact_query(text: str) -> str:
    value = normalize(text)
    for word in sorted(_GENERIC, key=len, reverse=True):
        value = value.replace(word, " ")
    return " ".join(value.split())


def _paths(record: dict[str, Any]) -> set[str]:
    paths: set[str] = set()
    for loc in record.get("implementation", {}).get("source_locations", []):
        if loc.get("path"):
            paths.add(loc["path"])
    for item in record.get("evidence", []):
        if item.get("path"):
            paths.add(item["path"])
    for item in record.get("consumers", []):
        if item.get("path"):
            paths.add(item["path"])
    return paths


def _usable_text(value: Any) -> bool:
    """拒绝把含 Unicode replacement character 的损坏文本展示给用户。"""
    return isinstance(value, str) and bool(value.strip()) and "�" not in value


class SearchEngine:
    """对步骤05/07/08/09产物建立内存索引并返回结构化结果。"""

    def __init__(self, kb: KnowledgeBase | None = None):
        self.kb = kb or load_knowledge_base()
        self.exact: dict[str, set[str]] = defaultdict(set)
        self.normalized: dict[str, set[str]] = defaultdict(set)
        self.terms: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self._build_index()

    def _put(self, variable_id: str, term: Any, kind: str) -> None:
        if variable_id not in self.kb.records or term is None or not str(term).strip():
            return
        surface = unicodedata.normalize("NFKC", str(term)).strip()
        self.exact[normalize(surface, code_sensitive=True)].add(variable_id)
        norm = normalize(surface)
        if norm:
            self.normalized[norm].add(variable_id)
            self.terms[variable_id][norm].add(kind)

    def _build_index(self) -> None:
        for variable_id, record in self.kb.records.items():
            self._put(variable_id, variable_id, "variable_id")
            self._put(variable_id, record.get("canonical_name"), "canonical_name")
            for key, value in record.get("names", {}).items():
                self._put(variable_id, value, "name_" + key)
            for value in record.get("aliases", []):
                self._put(variable_id, value, "record_alias")
            self._put(variable_id, record.get("category"), "category")
            for source_path in _paths(record):
                self._put(variable_id, source_path, "source_path")
            alias_record = self.kb.alias_records.get(variable_id, {})
            for group, values in alias_record.get("alias_groups", {}).items():
                for value in values:
                    self._put(variable_id, value, "alias_" + group)
            for value in alias_record.get("searchable_terms", []):
                self._put(variable_id, value, "searchable_term")

        # 步骤07显式歧义组是检索规则的一部分：同一表述必须召回全部候选。
        for group in self.kb.ambiguity_groups.values():
            for surface in group.get("surface_forms", []):
                for variable_id in group.get("candidate_variable_ids", []):
                    self._put(variable_id, surface, "ambiguity_group")

    def _relation_filter(
        self, upstream_of: str | None, downstream_of: str | None
    ) -> set[str] | None:
        allowed: set[str] | None = None
        if upstream_of:
            ids = {
                relation.get("source", {}).get("id")
                for relation in self.kb.upstream(upstream_of)
            } & self.kb.records.keys()
            allowed = ids
        if downstream_of:
            ids = {
                relation.get("target", {}).get("id")
                for relation in self.kb.downstream(downstream_of)
            } & self.kb.records.keys()
            allowed = ids if allowed is None else allowed & ids
        return allowed

    def _apply_filters(
        self,
        ids: set[str],
        category: str | None,
        source_path: str | None,
        upstream_of: str | None,
        downstream_of: str | None,
    ) -> set[str]:
        result = set(ids)
        if category:
            cat = normalize(category)
            result = {
                variable_id
                for variable_id in result
                if normalize(self.kb.records[variable_id].get("category", "")) == cat
            }
        if source_path:
            wanted = source_path.replace("\\", "/").casefold()
            result = {
                variable_id
                for variable_id in result
                if any(
                    wanted in path.replace("\\", "/").casefold()
                    for path in _paths(self.kb.records[variable_id])
                )
            }
        allowed = self._relation_filter(upstream_of, downstream_of)
        if allowed is not None:
            result &= allowed
        return result

    def _clarification(self, query_norm: str, candidate_ids: list[str]) -> str:
        alias_entry = self.kb.alias_index.get(query_norm)
        if alias_entry:
            question = alias_entry.get("resolution", {}).get("clarification_question")
            if _usable_text(question):
                return question
        wanted = set(candidate_ids)
        for group in self.kb.ambiguity_groups.values():
            if len(wanted & set(group.get("candidate_variable_ids", []))) >= 2:
                question = group.get("clarification_question")
                if _usable_text(question):
                    return question
        return "查询存在多个候选，请指定变量层级或规范 ID：" + "、".join(candidate_ids)

    def search(
        self,
        query: str = "",
        *,
        category: str | None = None,
        source_path: str | None = None,
        upstream_of: str | None = None,
        downstream_of: str | None = None,
        limit: int = 10,
        fuzzy_threshold: float = 0.56,
    ) -> dict[str, Any]:
        raw = str(query or "").strip()
        norm = normalize(raw)
        compact = _compact_query(raw) or norm
        limit = max(1, int(limit))
        universe = self._apply_filters(
            set(self.kb.records), category, source_path, upstream_of, downstream_of
        )
        if not raw:
            ids = sorted(universe)[:limit]
            return self._response(
                raw,
                norm,
                "filter_only",
                ids,
                {variable_id: (100.0, ["filter"]) for variable_id in ids},
                False,
                None,
            )

        scores: dict[str, tuple[float, set[str]]] = {}

        def award(variable_id: str, score: float, reason: str) -> None:
            if variable_id not in universe:
                return
            old_score, reasons = scores.get(variable_id, (0.0, set()))
            if score > old_score:
                scores[variable_id] = (score, {reason})
            elif score == old_score:
                reasons.add(reason)
                scores[variable_id] = (old_score, reasons)

        exact_query = normalize(raw, code_sensitive=True)
        for variable_id in self.exact.get(exact_query, ()):
            award(variable_id, 100.0, "exact")
        stage = "exact"

        if not scores:
            for variable_id in self.normalized.get(norm, ()):
                award(variable_id, 95.0, "normalized")
            stage = "normalized"

        if not scores:
            for variable_id, terms in self.terms.items():
                matched: list[tuple[str, set[str]]] = []
                for term, kinds in terms.items():
                    pattern = r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])"
                    if len(term) >= 2 and re.search(pattern, compact):
                        matched.append((term, kinds))
                if matched:
                    # 同一变量若同时命中多个独立线索，应高于只命中一个泛词的候选。
                    # 例如“生命值 + RMSE”应优先于只共享“RMSE”的位置误差。
                    unique_terms = sorted({term for term, _ in matched}, key=lambda x: (-len(x), x))
                    non_redundant: list[str] = []
                    for term in unique_terms:
                        if not any(term in kept or kept in term for kept in non_redundant):
                            non_redundant.append(term)
                    coverage = sum(len(term) for term in non_redundant) / max(len(compact), 1)
                    evidence_bonus = min(8.0, max(0, len(non_redundant) - 1) * 2.5)
                    score = 84.0 + min(6.0, coverage * 6) + evidence_bonus
                    reasons = sorted({kind for _, kinds in matched for kind in kinds})
                    award(variable_id, score, "contained:" + ",".join(reasons))
            stage = "contained"

        if not scores:
            for variable_id, terms in self.terms.items():
                best, best_kinds = 0.0, set()
                for term, kinds in terms.items():
                    ratio = SequenceMatcher(None, compact, term).ratio()
                    q_tokens, t_tokens = set(compact.split()), set(term.split())
                    overlap = len(q_tokens & t_tokens) / max(len(q_tokens | t_tokens), 1)
                    value = max(ratio, overlap)
                    if value > best:
                        best, best_kinds = value, kinds
                if best >= fuzzy_threshold:
                    award(
                        variable_id,
                        round(40 + best * 50, 3),
                        "fuzzy:" + ",".join(sorted(best_kinds)),
                    )
            stage = "fuzzy"

        if not scores:
            return {
                "status": "not_found",
                "query": raw,
                "normalized_query": norm,
                "match_stage": "none",
                "clarification_question": None,
                "result_count": 0,
                "results": [],
                "message": "未找到符合条件的正式变量；没有自动创建新变量。",
            }

        ordered = sorted(scores, key=lambda variable_id: (-scores[variable_id][0], variable_id))
        top_score = scores[ordered[0]][0]
        tolerance = 0.001 if stage in {"exact", "normalized"} else 2.0
        top = [variable_id for variable_id in ordered if top_score - scores[variable_id][0] < tolerance]
        ambiguous = len(top) > 1
        selected = ordered[:limit]
        cooked = {
            variable_id: (scores[variable_id][0], sorted(scores[variable_id][1]))
            for variable_id in selected
        }
        return self._response(
            raw,
            norm,
            stage,
            selected,
            cooked,
            ambiguous,
            self._clarification(norm, top) if ambiguous else None,
        )

    def _relation_view(self, relation: dict[str, Any], direction: str) -> dict[str, Any]:
        other = relation["source" if direction == "upstream" else "target"]
        return {
            "relation_id": relation.get("id"),
            "relation_type": relation.get("relation_type"),
            "variable_id": other.get("id"),
            "label": other.get("label"),
            "truth_status": relation.get("truth_status"),
            "formulas": relation.get("formulas", []),
            "evidence": relation.get("evidence", []),
        }

    def _result(self, variable_id: str, score: float, matched_by: list[str]) -> dict[str, Any]:
        record = self.kb.records[variable_id]
        incoming = [
            relation
            for relation in self.kb.upstream(variable_id)
            if relation.get("source", {}).get("id") in self.kb.records
        ]
        outgoing = [
            relation
            for relation in self.kb.downstream(variable_id)
            if relation.get("target", {}).get("id") in self.kb.records
        ]
        return {
            "variable_id": variable_id,
            "canonical_name": record.get("canonical_name"),
            "names": record.get("names", {}),
            "category": record.get("category"),
            "score": score,
            "matched_by": matched_by,
            "meaning": {
                "definition": record.get("definition"),
                "intuitive_explanation": record.get("intuitive_explanation"),
            },
            "interface": record.get("interface", {}),
            "implementation": {
                "source_locations": record.get("implementation", {}).get("source_locations", []),
                "extraction_code": record.get("implementation", {}).get("extraction_code", []),
                "transformation_formula": record.get("implementation", {}).get("transformation_formula", []),
            },
            "source_evidence": record.get("evidence", []),
            "formula_or_transformation": {
                "derivation_kind": record.get("provenance", {}).get("derivation_kind"),
                "upstream_variable_ids": record.get("provenance", {}).get("upstream_variable_ids", []),
                "formulas": record.get("implementation", {}).get("transformation_formula", []),
            },
            "relationships": {
                "upstream": [self._relation_view(relation, "upstream") for relation in incoming],
                "downstream": [self._relation_view(relation, "downstream") for relation in outgoing],
            },
            "limitations": record.get("limitations", []),
            "known_issues": {
                "record_level": record.get("known_issues", []),
                "step09": self.kb.known_issues_for(variable_id),
            },
            "verification": record.get("verification", {}),
        }

    def _response(
        self,
        query: str,
        norm: str,
        stage: str,
        ids: list[str],
        scores: dict[str, tuple[float, list[str]]],
        ambiguous: bool,
        clarification: str | None,
    ) -> dict[str, Any]:
        results = [
            self._result(variable_id, scores[variable_id][0], scores[variable_id][1])
            for variable_id in ids
        ]
        response = {
            "status": "ambiguous" if ambiguous else ("found" if results else "not_found"),
            "query": query,
            "normalized_query": norm,
            "match_stage": stage,
            "clarification_question": clarification,
            "result_count": len(results),
            "results": results,
        }
        if not results:
            response["message"] = "未找到符合条件的正式变量；没有自动创建新变量。"
        return response


def search(query: str = "", **kwargs: Any) -> dict[str, Any]:
    """一次性便利函数。批量查询时建议复用 SearchEngine。"""
    return SearchEngine().search(query, **kwargs)
