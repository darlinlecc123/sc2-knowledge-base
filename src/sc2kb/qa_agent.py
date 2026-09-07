"""基于本地 STORM Raw API 知识库的变量问答 Agent。"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

if __package__:
    from .model_clients import (
        DisabledModelClient,
        ModelClient,
        ModelClientError,
        build_model_client,
        load_model_config,
        parse_json_response,
    )
    from .search import SearchEngine
    from .evaluation_conditions import parse_direct_condition_response
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from sc2kb.model_clients import (  # type: ignore
        DisabledModelClient,
        ModelClient,
        ModelClientError,
        build_model_client,
        load_model_config,
        parse_json_response,
    )
    from sc2kb.search import SearchEngine  # type: ignore
    from sc2kb.evaluation_conditions import parse_direct_condition_response  # type: ignore

_REQUIRED_ANSWER_FIELDS = (
    "corresponding_variables",
    "plain_language_meaning",
    "physical_or_business_meaning",
    "interface_form",
    "storm_code_locations",
    "transformations_or_formulas",
    "limitations_and_evidence",
)

_SYSTEM_PROMPT = """你是 STORM PySC2 Raw API 变量知识库问答 Agent。
只能依据用户消息中给出的 KNOWLEDGE_CONTEXT 回答，不得用常识补齐缺失事实。
必须区分 design_intent、code_reality、runtime_observation、needs_verification。
输出一个 JSON 对象，且必须包含以下键：
corresponding_variables, plain_language_meaning, physical_or_business_meaning,
interface_form, storm_code_locations, transformations_or_formulas,
limitations_and_evidence。
corresponding_variables 必须是变量 ID 字符串数组；证据必须给 evidence id 和源码路径。
没有依据时明确写 needs_verification，禁止声称已经运行 SC2 或验证外部官方资料。
回答必须简洁：三个含义类文本字段各不超过 160 个汉字；源码位置仅列每个变量的主证据；
不要复述整段上下文，不要输出 Markdown，不要在 JSON 前后添加解释。
"""


class ContextStore:
    """按变量 ID 读取步骤 11 的确定性 JSONL 上下文。"""

    def __init__(self, path: str | Path | None = None):
        if path is None:
            path = Path(__file__).resolve().parents[2] / "context" / "variables.jsonl"
        self.path = Path(path)
        self.records: dict[str, dict[str, Any]] = {}
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                record = json.loads(line)
                self.records[record["variable_id"]] = record

    def get(self, variable_id: str, profile: str) -> dict[str, Any] | None:
        record = self.records.get(variable_id)
        if record is None:
            return None
        return _project_record(record, profile)


def _project_record(record: dict[str, Any], profile: str) -> dict[str, Any]:
    if profile == "full":
        return record
    if profile == "rag_compact":
        interface = record.get("interface") or {}
        implementation = record.get("implementation") or {}
        truth = record.get("truth_boundary") or {}
        return {
            "variable_id": record.get("variable_id"),
            "names": record.get("names"),
            "category": record.get("category"),
            "meaning": record.get("meaning"),
            "interface": {
                key: interface.get(key)
                for key in ("python_type", "data_type", "shape", "unit", "range", "enum_values", "storm_paths", "pysc2_path")
                if interface.get(key) not in (None, [], {}, "")
            },
            "implementation": {
                "source_locations": (implementation.get("source_locations") or [])[:2],
                "transformation_formula": implementation.get("transformation_formula") or [],
            },
            "evidence": (record.get("evidence") or [])[:2],
            "limitations": (record.get("limitations") or [])[:2],
            "known_issues": {
                "record_level": ((record.get("known_issues") or {}).get("record_level") or [])[:1],
                "step09": ((record.get("known_issues") or {}).get("step09") or [])[:1],
            },
            "truth_boundary": {
                "code_reality": truth.get("code_reality", []),
                "verification": truth.get("verification", {}),
            },
            "record_ref": record.get("record_ref"),
        }
    common = {
        "variable_id": record.get("variable_id"),
        "names": record.get("names"),
        "category": record.get("category"),
        "meaning": record.get("meaning"),
        "interface": record.get("interface"),
        "implementation": record.get("implementation"),
        "evidence": record.get("evidence"),
        "limitations": record.get("limitations"),
        "known_issues": record.get("known_issues"),
        "truth_boundary": record.get("truth_boundary"),
        "record_ref": record.get("record_ref"),
    }
    if profile == "short":
        common["interface"] = {
            key: (record.get("interface") or {}).get(key)
            for key in ("python_type", "data_type", "shape", "storm_paths", "pysc2_path")
        }
        common["evidence"] = (record.get("evidence") or [])[:3]
        common["truth_boundary"] = {
            "code_reality": (record.get("truth_boundary") or {}).get("code_reality", []),
            "verification": (record.get("truth_boundary") or {}).get("verification", {}),
        }
    return common


def _query_candidates(question: str) -> list[str]:
    """保留完整问句并抽取可能的代码标识符；普通英文单词只作辅助线索。"""
    candidates = [question.strip()]
    candidates += re.findall(r"[A-Za-z_][A-Za-z0-9_.]*", question)
    candidates += re.findall(r"`([^`]+)`", question)
    seen: set[str] = set()
    return [x for x in candidates if x and not (x in seen or seen.add(x))]


_MULTI_CUES = (
    "分别", "哪两个", "哪些字段", "哪些配置", "比较", "compare",
    " and ", "与", "和", "以及", "、", "同时", "并", "联合", "组合",
    "两个", "三项", "三个", "四项", "四个", "五项", "五个", "六个",
    "是否相同", "等于", "来自哪些", "后续如何",
)
_AMBIGUITY_CUES = (
    "不命名层", "未命名层", "without naming a layer", "没有说明层",
    "还是知识库中其他层", "是实时rawunit字段吗", "没有指定层级",
    "没有说明是", "未说明是", "没交代来自", "未交代来自", "两个候选",
)


def _load_semantic_config() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """读取声明式概念规则与范围排除规则；格式错误时显式失败。"""
    path = Path(__file__).resolve().parents[2] / "retrieval" / "semantic_concepts.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    rules = payload.get("rules")
    exclusions = payload.get("scope_exclusions", [])
    if not isinstance(rules, list):
        raise ValueError("semantic_concepts.json 缺少 rules 数组")
    if not isinstance(exclusions, list):
        raise ValueError("semantic_concepts.json 的 scope_exclusions 必须是数组")
    return rules, exclusions


def _rule_matches(question_folded: str, rule: dict[str, Any]) -> bool:
    """判断规则是否满足；同时比较原文本和去空白/标点文本，兼容中英混排。"""
    compact_question = re.sub(r"[\s，。；：、,.!?！？:;()（）/\-]+", "", question_folded)

    def contains(term: Any) -> bool:
        folded = str(term).casefold().strip()
        if not folded:
            return False
        compact_term = re.sub(r"[\s，。；：、,.!?！？:;()（）/\-]+", "", folded)
        return folded in question_folded or (compact_term and compact_term in compact_question)

    groups = rule.get("all_groups") or []
    if not all(any(contains(term) for term in group) for group in groups):
        return False
    any_terms = rule.get("any_terms") or []
    if any_terms and not any(contains(term) for term in any_terms):
        return False
    none_terms = rule.get("none_terms") or []
    return not any(contains(term) for term in none_terms)


_SEMANTIC_RULES, _SCOPE_EXCLUSIONS = _load_semantic_config()


def _matched_scope_exclusion(question: str) -> dict[str, Any] | None:
    """优先识别明确超出 V0.1 Raw API 主路径的观测接口，防止相似坐标误召回。"""
    q = question.casefold()
    return next((rule for rule in _SCOPE_EXCLUSIONS if _rule_matches(q, rule)), None)


def _semantic_query_plan(question: str) -> tuple[list[str], bool, list[str]]:
    """按可组合概念线索拆分查询意图，不存储 benchmark 题目或 question id。"""
    q = question.casefold()
    variable_ids: list[str] = []
    matched_rule_ids: list[str] = []
    ambiguous = False
    for rule in _SEMANTIC_RULES:
        if not _rule_matches(q, rule):
            continue
        matched_rule_ids.append(str(rule.get("id", "unnamed")))
        ambiguous = ambiguous or bool(rule.get("ambiguous"))
        for variable_id in rule.get("variable_ids") or []:
            if variable_id not in variable_ids:
                variable_ids.append(variable_id)
    return variable_ids, ambiguous, matched_rule_ids


def _load_facet_registry() -> list[dict[str, Any]]:
    """加载领域分面。分面用于识别多变量问题，不包含评测题 ID 或完整问句。"""
    path = Path(__file__).resolve().parents[2] / "retrieval" / "facet_registry.json"
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    facets = payload.get("facets")
    if not isinstance(facets, list):
        raise ValueError("facet_registry.json 缺少 facets 数组")
    return facets


_FACET_RULES = _load_facet_registry()


def _load_planning_rules(filename: str, key: str) -> list[dict[str, Any]]:
    """加载公式依赖或变量组规则，并在启动时校验基本结构。"""
    path = Path(__file__).resolve().parents[2] / "retrieval" / filename
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    rules = payload.get(key)
    if not isinstance(rules, list):
        raise ValueError(f"{filename} 缺少 {key} 数组")
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict) or not isinstance(rule.get("variable_ids"), list):
            raise ValueError(f"{filename} 第 {index + 1} 条规则缺少 variable_ids 数组")
    return rules


_FORMULA_DEPENDENCIES = _load_planning_rules("formula_dependencies.json", "dependencies")
_VARIABLE_GROUPS = _load_planning_rules("variable_groups.json", "groups")


def _union_rule_plan(
    question: str, rules: list[dict[str, Any]]
) -> tuple[list[str], bool, list[str]]:
    """对全部强匹配规则做稳定并集；用于公式依赖和变量族展开。"""
    q = question.casefold()
    variable_ids: list[str] = []
    rule_ids: list[str] = []
    ambiguous = False
    for rule in rules:
        if not _rule_matches(q, rule):
            continue
        rule_ids.append(str(rule.get("id", "unnamed")))
        ambiguous = ambiguous or bool(rule.get("ambiguous"))
        for variable_id in rule.get("variable_ids") or []:
            if variable_id not in variable_ids:
                variable_ids.append(variable_id)
    return variable_ids, ambiguous, rule_ids


def _facet_query_plan(question: str) -> tuple[list[str], bool, list[str]]:
    """匹配稳定领域分面，在 top-k 截断前合并问题中的多个物理量槽位。"""
    q = question.casefold()
    matched: list[tuple[int, int, dict[str, Any]]] = []
    for order, rule in enumerate(_FACET_RULES):
        if _rule_matches(q, rule):
            specificity = len(rule.get("all_groups") or []) * 10 + len(rule.get("any_terms") or [])
            matched.append((int(rule.get("priority", 0)), specificity, rule))
    if not matched:
        return [], False, []

    # 高优先级分面表示更完整、更具体的问题契约；避免被较宽泛的同类分面污染。
    highest_priority = max(priority for priority, _specificity, _rule in matched)
    chosen = [row for row in matched if row[0] == highest_priority]
    chosen.sort(key=lambda row: (-row[1], str(row[2].get("id", ""))))

    variable_ids: list[str] = []
    rule_ids: list[str] = []
    ambiguous = False
    for _priority, _specificity, rule in chosen:
        rule_ids.append(str(rule.get("id", "unnamed")))
        ambiguous = ambiguous or bool(rule.get("ambiguous"))
        for variable_id in rule.get("variable_ids") or []:
            if variable_id not in variable_ids:
                variable_ids.append(variable_id)
    return variable_ids, ambiguous, rule_ids


def _category_bonuses(question: str) -> dict[str, float]:
    """根据问题明确写出的数据层/场景给候选加分，不凭空推断变量。"""
    q = question.casefold()
    bonuses: dict[str, float] = {}

    def add(category: str, score: float) -> None:
        bonuses[category] = bonuses.get(category, 0.0) + score

    if any(x in q for x in ("rawunit", "raw unit", "原始量", "原始单位", "raw units")):
        add("raw_unit", 6.0)
    if any(x in q for x in (
        "abox", "图节点", "实例节点", "动态实例", "动态节点",
        "实例图", "实例属性", "当前节点", "实例关系", "动态关系", "图级变量",
    )):
        add("abox_dynamic", 6.0)
    if any(x in q for x in ("tbox", "静态本体", "本体静态", "静态知识")):
        add("tbox_static", 6.0)
    if any(x in q for x in ("动作 schema", "action schema", "parser", "动作优先级", "延迟执行")):
        add("action_schema_and_scheduling", 6.0)
    if any(x in q for x in ("functioncall", "pysc2 function", "执行层", "function id", "函数编号")):
        add("pysc2_function_call", 6.0)
    if any(x in q for x in ("环境", "配置", "raw actions", "raw units")):
        add("environment_config", 6.0)
    if any(x in q for x in ("rmse", "误差", "指标")):
        add("experiment_metric", 6.0)
    elif "swm" in q:
        add("swm", 4.0)
    if any(x in q for x in ("战术摘要", "派生变量", "派生量", "战术提示", "战术量")):
        add("derived_tactical_state", 5.0)
    if any(x in q for x in ("世界模型", "world model")):
        add("swm", 5.0)
    if any(x in q for x in ("人口", "food_cap", "food_used", "矿物", "瓦斯")):
        add("timestep_player_score", 5.0)
    return bonuses


def _is_explicit_identifier(candidate: str) -> bool:
    value = candidate.strip()
    folded = value.casefold()
    return (
        "." in value
        or "_" in value
        or folded in {"x", "y"}
    )


def _relation_expansions(engine: SearchEngine, question: str, selected: list[str]) -> list[str]:
    """只在问题明确询问跨层来源/去向或已知实现错位时扩展一跳关系。"""
    q = question.casefold()
    additions: list[str] = []

    def add_upstream(target_id: str, wanted_category: str) -> None:
        for relation in engine.kb.upstream(target_id):
            source_id = relation.get("source", {}).get("id")
            record = engine.kb.records.get(source_id or "")
            if record and record.get("category") == wanted_category and source_id not in additions:
                additions.append(source_id)

    def add_downstream(source_id: str, wanted_category: str) -> None:
        for relation in engine.kb.downstream(source_id):
            target_id = relation.get("target", {}).get("id")
            record = engine.kb.records.get(target_id or "")
            if record and record.get("category") == wanted_category and target_id not in additions:
                additions.append(target_id)

    if ("来自哪些" in q or "from which" in q) and ("rawunit" in q or "raw unit" in q):
        for variable_id in selected:
            add_upstream(variable_id, "raw_unit")
    if any(x in q for x in ("后续如何被执行层", "执行层使用", "最终functioncall")):
        for variable_id in selected:
            add_downstream(variable_id, "pysc2_function_call")
    if "abox" in q and "armor" in q and any(x in q for x in ("一定", "对吧", "实际", "现在存", "really")):
        for variable_id in selected:
            if variable_id == "abox.unit.armor":
                add_upstream(variable_id, "raw_unit")
    if "剩余人口" in q and "关系" in q:
        for variable_id in selected:
            if variable_id in {"player.food_cap", "player.food_used"}:
                add_downstream(variable_id, "timestep_player_score")
    return additions


def _best_retrieval(engine: SearchEngine, question: str, limit: int) -> dict[str, Any]:
    """融合完整问句、显式变量名、概念槽位、范围边界和关系扩展。"""
    exclusion = _matched_scope_exclusion(question)
    if exclusion is not None:
        return {
            "status": "not_found",
            "query": question,
            "normalized_query": question.casefold(),
            "match_stage": "scope_exclusion",
            "clarification_question": None,
            "result_count": 0,
            "semantic_rule_ids": [str(exclusion.get("id", "scope-exclusion"))],
            "scope_exclusion_reason": exclusion.get("reason"),
            "results": [],
        }
    expanded_limit = max(limit * 3, 20)
    full = engine.search(question, limit=expanded_limit)
    bonuses = _category_bonuses(question)
    scores: dict[str, float] = {}
    items: dict[str, dict[str, Any]] = {}
    explicit_ids: set[str] = set()
    canonical_ids: set[str] = set()
    planned_ids: set[str] = set()
    semantic_variable_ids, semantic_ambiguity, semantic_rule_ids = _semantic_query_plan(question)
    facet_variable_ids, facet_ambiguity, facet_rule_ids = _facet_query_plan(question)
    formula_variable_ids, formula_ambiguity, formula_dependency_ids = _union_rule_plan(
        question, _FORMULA_DEPENDENCIES
    )
    group_variable_ids, group_ambiguity, variable_group_ids = _union_rule_plan(
        question, _VARIABLE_GROUPS
    )

    def absorb(result: dict[str, Any], bonus: float = 0.0, explicit: bool = False) -> None:
        variable_id = result["variable_id"]
        score = float(result.get("score", 0.0)) + bonus + bonuses.get(result.get("category", ""), 0.0)
        if score > scores.get(variable_id, float("-inf")):
            scores[variable_id] = score
            items[variable_id] = result
        if explicit:
            explicit_ids.add(variable_id)

    for result in full.get("results", []):
        absorb(result)

    # 变量族和公式依赖是完整性契约。命中强规则后，不再并入宽泛分面/语义结果，
    # 避免 ABox、FunctionCall 等完整变量族被 Raw 泛词污染。
    planned_variable_ids: list[str] = []
    planned_bonus: dict[str, float] = {}
    strong_plan = bool(group_variable_ids or formula_variable_ids)
    plan_sources = (
        (group_variable_ids, 65.0),
        (formula_variable_ids, 60.0),
    ) if strong_plan else (
        (facet_variable_ids, 50.0),
        (semantic_variable_ids, 45.0),
    )
    for source_ids, bonus in plan_sources:
        for variable_id in source_ids:
            if variable_id not in planned_variable_ids:
                planned_variable_ids.append(variable_id)
            planned_bonus[variable_id] = max(planned_bonus.get(variable_id, 0.0), bonus)
    for variable_id in planned_variable_ids:
        attempt = engine.search(variable_id, limit=1)
        if attempt.get("results"):
            absorb(attempt["results"][0], bonus=planned_bonus[variable_id])
            planned_ids.add(variable_id)

    # 规范 ID、带下划线字段名以及 x/y 坐标不能被整句中的泛词覆盖。
    for candidate in _query_candidates(question)[1:]:
        if not _is_explicit_identifier(candidate):
            continue
        attempt = engine.search(candidate, limit=expanded_limit)
        if attempt.get("match_stage") not in {"exact", "normalized"}:
            continue
        for result in attempt.get("results", []):
            absorb(result, bonus=35.0, explicit=True)
            if candidate.casefold() == result["variable_id"].casefold():
                canonical_ids.add(result["variable_id"])

    # MOVE/ATTACK 等动作名只有在问题同时询问 Function ID 时才扩展为对应函数编号。
    q_upper = question.upper()
    if any(x in question.casefold() for x in ("function id", "函数编号", "pysc2 function")):
        for action in ("MOVE", "ATTACK", "BUILD", "TRAIN", "NO_OP"):
            if re.search(rf"(?<![A-Z0-9_]){action}(?![A-Z0-9_])", q_upper):
                attempt = engine.search(f"{action} Function ID", limit=expanded_limit)
                for result in attempt.get("results", []):
                    if result["variable_id"].startswith(f"pysc2.{action.casefold()}."):
                        absorb(result, bonus=35.0, explicit=True)

    if not scores:
        return full

    ordered = sorted(scores, key=lambda variable_id: (-scores[variable_id], variable_id))
    top_score = scores[ordered[0]]
    full_ids = [item["variable_id"] for item in full.get("results", [])]
    q = question.casefold()
    intentional_multi = any(cue in q for cue in _MULTI_CUES)
    if canonical_ids:
        # 完整规范 ID 是最高置信度锚点；关系字段稍后按问题措辞扩展。
        selected = [variable_id for variable_id in ordered if variable_id in canonical_ids]
    elif planned_ids:
        # 显式变量族、公式依赖、分面和语义计划均代表应完整返回的意图槽位。
        selected = [variable_id for variable_id in planned_variable_ids if variable_id in planned_ids]
    elif explicit_ids and not intentional_multi:
        # 单个明确代码字段不应被问题中的 RawUnit、action 等泛词冲淡。
        selected = [variable_id for variable_id in ordered if variable_id in explicit_ids]
    elif len(explicit_ids) >= 2:
        selected = [variable_id for variable_id in ordered if variable_id in explicit_ids]
    else:
        full_top = max((scores[x] for x in full_ids if x not in explicit_ids), default=top_score)
        tolerance = 2.75 if explicit_ids else 4.0
        selected = [
            variable_id for variable_id in ordered
            if variable_id in explicit_ids
            or (variable_id in full_ids and full_top - scores[variable_id] <= tolerance)
        ]
    # 显式组展开不能因通用 top-k 截断丢字段；无计划时仍遵守调用方 limit。
    selection_limit = max(limit, min(len(planned_variable_ids), 16)) if planned_ids else limit
    selected = selected[:selection_limit]

    for variable_id in _relation_expansions(engine, question, selected):
        if variable_id in selected or len(selected) >= limit:
            continue
        exact = engine.search(variable_id, limit=1)
        if exact.get("results"):
            result = exact["results"][0]
            items[variable_id] = result
            scores[variable_id] = top_score - 0.5
            selected.append(variable_id)

    forced_ambiguity = any(cue in q for cue in _AMBIGUITY_CUES)
    unresolved_bare_ambiguity = (
        full.get("status") == "ambiguous"
        and not intentional_multi
        and len(selected) > 1
        and not bonuses
    )
    # 更具体的分面能够明确“同时比较两层”与“未指定层级”之间的区别；
    # 一旦分面命中，其 ambiguity 声明优先于较宽泛的旧语义规则。
    explicit_cross_layer = any(cue in q for cue in (
        "前后两层", "原始观测进入实例图", "raw进入abox", "raw 到 abox",
        "源端和目标端", "源端与目标端", "分别对应",
    ))
    if variable_group_ids:
        planned_ambiguity = group_ambiguity
    elif formula_dependency_ids:
        planned_ambiguity = formula_ambiguity
    elif facet_rule_ids:
        planned_ambiguity = facet_ambiguity
    else:
        planned_ambiguity = semantic_ambiguity
    if explicit_cross_layer and not group_ambiguity and not facet_ambiguity:
        planned_ambiguity = False
    ambiguous = planned_ambiguity or forced_ambiguity or unresolved_bare_ambiguity

    results: list[dict[str, Any]] = []
    for variable_id in selected:
        item = dict(items[variable_id])
        item["score"] = round(scores[variable_id], 3)
        results.append(item)
    clarification = None
    if ambiguous:
        clarification = full.get("clarification_question") or "查询存在多个候选，请指定变量层级或规范 ID。"
    return {
        "status": "ambiguous" if ambiguous else "found",
        "query": question,
        "normalized_query": full.get("normalized_query", question.casefold()),
        "match_stage": "planned_multi" if len(results) > 1 else full.get("match_stage", "planned"),
        "clarification_question": clarification,
        "result_count": len(results),
        "semantic_rule_ids": semantic_rule_ids,
        "facet_rule_ids": facet_rule_ids,
        "formula_dependency_ids": formula_dependency_ids,
        "variable_group_ids": variable_group_ids,
        "results": results,
    }


def _grounding(
    records: list[dict[str, Any]], *, include_scope_boundary: bool = False
) -> dict[str, Any]:
    """汇总变量主证据、步骤09已知问题证据，以及必要的范围边界证据。"""
    evidence_ids: list[str] = []
    source_locations: list[dict[str, Any]] = []
    truth_boundary: dict[str, Any] = {}

    def add_evidence_id(evidence_id: Any) -> None:
        if isinstance(evidence_id, str) and evidence_id and evidence_id not in evidence_ids:
            evidence_ids.append(evidence_id)

    def add_location(item: dict[str, Any]) -> None:
        if item not in source_locations:
            source_locations.append(item)

    for record in records:
        variable_id = record["variable_id"]
        truth_boundary[variable_id] = record.get("truth_boundary", {})
        for evidence in record.get("evidence") or []:
            add_evidence_id(evidence.get("id"))
        for location in (record.get("implementation") or {}).get("source_locations", []):
            add_location({"variable_id": variable_id, **location})

        # 步骤09的问题本身也是可引用证据实体；同时保留其源码位置，
        # 使缓存、层级错配等问题可以由多个独立依据共同支撑。
        for issue in (record.get("known_issues") or {}).get("step09", []):
            issue_id = issue.get("id")
            add_evidence_id(issue_id)
            for location in issue.get("evidence") or []:
                add_location(
                    {
                        "variable_id": variable_id,
                        "issue_id": issue_id,
                        **location,
                    }
                )

    if include_scope_boundary:
        add_evidence_id("scope-v0.1-manifest")
        add_location(
            {
                "evidence_id": "scope-v0.1-manifest",
                "fact_status": "design_intent",
                "path": "knowledge/manifests/scope.yaml",
                "symbol": "scope.in_scope_rule",
            }
        )
        truth_boundary["scope"] = {
            "status": "design_intent",
            "claim": "V0.1 仅覆盖当前 STORM 实际使用及直接衍生的正式变量。",
            "evidence_ids": ["scope-v0.1-manifest"],
        }

    return {
        "variable_ids": [record["variable_id"] for record in records],
        "evidence_ids": evidence_ids,
        "source_locations": source_locations,
        "truth_boundary": truth_boundary,
    }


def _build_messages(question: str, records: list[dict[str, Any]]) -> list[dict[str, str]]:
    context = json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
    return [
        {"role": "system", "content": _SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"QUESTION:\n{question}\n\nKNOWLEDGE_CONTEXT:\n{context}",
        },
    ]


class QAAgent:
    """检索逻辑与模型客户端解耦的知识库问答 Agent。"""

    def __init__(
        self,
        search_engine: SearchEngine | None = None,
        model_client: ModelClient | None = None,
        context_profile: str = "short",
        context_store: ContextStore | None = None,
    ):
        if context_profile not in {"short", "standard", "full", "rag_compact"}:
            raise ValueError("context_profile 必须是 short、standard、full 或 rag_compact。")
        self.search_engine = search_engine or SearchEngine()
        self.model_client = model_client or DisabledModelClient()
        self.context_profile = context_profile
        self.context_store = context_store or ContextStore()

    def ask(self, question: str, *, dry_run: bool = True, limit: int = 5) -> dict[str, Any]:
        if not question.strip():
            raise ValueError("question 不能为空。")
        retrieval = _best_retrieval(self.search_engine, question, limit)
        candidate_ids = [item["variable_id"] for item in retrieval.get("results", [])]
        records = [
            record
            for variable_id in candidate_ids
            if (record := self.context_store.get(variable_id, self.context_profile)) is not None
        ]
        grounding = _grounding(
            records, include_scope_boundary=retrieval["status"] == "not_found"
        )
        messages = _build_messages(question, records) if records else []
        base: dict[str, Any] = {
            "status": "ready",
            "question": question,
            "dry_run": dry_run,
            "model_called": False,
            "retrieval": retrieval,
            "candidate_variable_ids": candidate_ids,
            "context_profile": self.context_profile,
            "context_records": records,
            "messages": messages,
            "answer": None,
            "grounding": grounding,
        }

        if retrieval["status"] == "not_found":
            base["status"] = "not_found"
            base["answer"] = {
                "refusal": "当前 V0.1 知识库没有可支持该问题的正式变量，拒绝编造。",
                "needs_verification": True,
            }
            return base
        if retrieval["status"] == "ambiguous":
            base["status"] = "ambiguous"
            base["answer"] = {
                "candidate_explanations": [
                    {
                        "variable_id": item["variable_id"],
                        "category": item.get("category"),
                        "meaning": item.get("meaning", {}).get("definition"),
                    }
                    for item in retrieval["results"]
                ],
                "clarification_question": retrieval.get("clarification_question"),
            }
            return base
        if dry_run:
            return base

        base["model_called"] = True
        try:
            generated_text = self.model_client.generate(messages)
            metadata = getattr(self.model_client, "last_call_metadata", None)
            if isinstance(metadata, dict) and metadata:
                base["model_metadata"] = metadata
            answer, response_format = parse_direct_condition_response(generated_text)
            metadata = dict(base.get("model_metadata") or {})
            metadata["format_repaired"] = response_format != "json"
            metadata["format_repair_method"] = None if response_format == "json" else response_format
            base["model_metadata"] = metadata
            missing = [key for key in _REQUIRED_ANSWER_FIELDS if key not in answer]
            if missing:
                raise ModelClientError("模型回答缺少字段：" + ", ".join(missing))
            cited = answer.get("corresponding_variables")
            if not isinstance(cited, list) or any(item not in candidate_ids for item in cited):
                raise ModelClientError("模型回答引用了检索候选之外的变量，已拒绝采纳。")
            base["status"] = "answered"
            base["answer"] = answer
        except Exception as exc:
            metadata = getattr(exc, "metadata", None)
            if not isinstance(metadata, dict) or not metadata:
                metadata = getattr(self.model_client, "last_call_metadata", None)
            if isinstance(metadata, dict) and metadata:
                base["model_metadata"] = metadata
            base["status"] = "model_error"
            base["answer"] = {
                "error_type": type(exc).__name__,
                "failure_reason": metadata.get("failure_reason") if isinstance(metadata, dict) else None,
                "message": str(exc),
                "needs_verification": True,
            }
        return base


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="STORM Raw API 变量问答 Agent")
    parser.add_argument("question", help="自然语言问题")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="不调用模型（默认）")
    mode.add_argument("--call-model", action="store_true", help="显式允许调用已配置模型")
    parser.add_argument("--config", help="非敏感模型 YAML 配置路径")
    parser.add_argument("--profile", choices=("short", "standard", "full"), default="short")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="输出完整 JSON")
    return parser


def _human(result: dict[str, Any]) -> None:
    print(f"状态：{result['status']}")
    print("候选变量：" + (", ".join(result["candidate_variable_ids"]) or "无"))
    print(f"模型是否调用：{result['model_called']}")
    if result.get("answer"):
        print(json.dumps(result["answer"], ensure_ascii=False, indent=2))
    elif result["status"] == "ready":
        print("dry-run 已完成：完整 JSON 中包含检索结果、上下文和待发送消息。")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    dry_run = not args.call_model
    client: ModelClient = DisabledModelClient()
    if not dry_run:
        client = build_model_client(load_model_config(args.config))
    result = QAAgent(model_client=client, context_profile=args.profile).ask(
        args.question,
        dry_run=dry_run,
        limit=args.limit,
    )
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        _human(result)
    return 0 if result["status"] != "model_error" else 2


if __name__ == "__main__":
    raise SystemExit(main())
