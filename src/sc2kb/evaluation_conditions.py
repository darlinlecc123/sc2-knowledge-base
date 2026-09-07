"""步骤 16 三知识条件中的无知识库与完整上下文 Agent。"""
from __future__ import annotations

import hashlib
import json
import re

import yaml
from pathlib import Path
from typing import Any

from .model_clients import ModelClient, ModelClientError, parse_json_response

_REQUIRED_FIELDS = (
    "corresponding_variables",
    "plain_language_meaning",
    "physical_or_business_meaning",
    "interface_form",
    "storm_code_locations",
    "transformations_or_formulas",
    "limitations_and_evidence",
)

_SYSTEM_PROMPT = """你正在参加 STORM PySC2 Raw API 变量知识库的标准化评测。
请只输出一个 JSON 对象，不要输出 Markdown 围栏或 JSON 之外的说明。
JSON 必须包含：response_status, corresponding_variables,
plain_language_meaning, physical_or_business_meaning, interface_form,
storm_code_locations, transformations_or_formulas, limitations_and_evidence。
response_status 只能是 answered、ambiguous、not_found。
corresponding_variables 必须是规范变量 ID 字符串数组。
若问题存在多个层级且无法确定，使用 ambiguous，并给 clarification_question。
若没有可验证依据，使用 not_found，并给 refusal；禁止编造源码路径、接口或运行事实。
不要输出思考过程，优先尽快给出简短、合法、完整的 JSON。
"""


def parse_direct_condition_response(text: str) -> tuple[dict[str, Any], str]:
    """优先严格 JSON；仅恢复 DeepSeek smoke 中出现的确定性 YAML 映射格式。"""
    try:
        return parse_json_response(text), "json"
    except ModelClientError as original:
        candidate = text.strip()
        # 不接受思维链混入的多段输出；只处理单段、键名明确的映射。
        if "<｜end▁of▁thinking｜>" in candidate:
            raise original
        lines = candidate.splitlines()
        if not lines:
            raise original
        first = lines[0].strip()
        if first.endswith(","):
            first = first[:-1].rstrip()
        # 已观察到接口会漏掉 {response_status, corresponding_variables: 前缀，
        # 但保留 corresponding_variables 的数组值和后续键名。
        if first.startswith("[") and first.endswith("]"):
            lines[0] = "corresponding_variables: " + first
        normalized_lines: list[str] = []
        for line in lines:
            # 去掉缺失外层花括号后遗留的顶层 JSON 逗号；数组内部保持不变。
            if line and not line[0].isspace() and line.rstrip().endswith(","):
                line = line.rstrip()[:-1]
            normalized_lines.append(line)
        repaired_text = "\n".join(normalized_lines)
        try:
            value = yaml.safe_load(repaired_text)
        except yaml.YAMLError:
            raise original
        if not isinstance(value, dict):
            raise original
        # DeepSeek v4-flash 在关闭 JSON mode 时观察到把 response_status 缩写为 _status。
        # 仅在目标键缺失且值属于固定枚举时做一对一字段名恢复。
        if "response_status" not in value and value.get("_status") in {"answered", "ambiguous", "not_found"}:
            value["response_status"] = value.pop("_status")
        known = set(_REQUIRED_FIELDS) | {"response_status", "clarification_question", "refusal", "needs_verification"}
        if not set(value).issubset(known) or "corresponding_variables" not in value:
            raise original
        return value, "yaml_mapping_repair"


class DirectKnowledgeConditionAgent:
    """不经过检索，直接运行 no-KB 或完整静态上下文条件。"""

    def __init__(
        self,
        model_client: ModelClient,
        condition: str,
        full_context_path: str | Path | None = None,
    ):
        if condition not in {"no_knowledge_base", "full_context"}:
            raise ValueError(f"不支持的直接知识条件：{condition}")
        self.model_client = model_client
        self.condition = condition
        self.full_context_path = Path(full_context_path) if full_context_path else None
        self._full_context: str | None = None
        self.context_metadata: dict[str, Any] = {"condition": condition}
        if condition == "full_context":
            if self.full_context_path is None or not self.full_context_path.exists():
                raise FileNotFoundError(f"完整上下文不存在：{self.full_context_path}")
            raw = self.full_context_path.read_bytes()
            self._full_context = raw.decode("utf-8")
            self.context_metadata.update({
                "path": str(self.full_context_path),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "characters": len(self._full_context),
                "truncated": False,
            })

    def _messages(self, question: str) -> list[dict[str, str]]:
        if self.condition == "no_knowledge_base":
            user = (
                "KNOWLEDGE_CONDITION: no_knowledge_base\n"
                "本条件不提供知识库正文或检索结果。不得假装看过当前仓库。\n\n"
                f"QUESTION:\n{question}"
            )
        else:
            user = (
                "KNOWLEDGE_CONDITION: full_context\n"
                "下面提供未经检索和截断的完整静态知识库上下文。只能依据该上下文回答。\n\n"
                f"FULL_KNOWLEDGE_CONTEXT_BEGIN\n{self._full_context}\n"
                "FULL_KNOWLEDGE_CONTEXT_END\n\n"
                f"QUESTION:\n{question}"
            )
        user += """

FINAL_OUTPUT_REQUIREMENT:
现在立即停止分析，只输出一个可被 json.loads 解析的完整 JSON 对象。
必须从 { 开始并以 } 结束，不要使用 YAML、Markdown 或代码围栏。
最小结构示例：
{"response_status":"answered","corresponding_variables":[],"plain_language_meaning":"","physical_or_business_meaning":"","interface_form":{},"storm_code_locations":[],"transformations_or_formulas":[],"limitations_and_evidence":[]}
"""
        return [{"role": "system", "content": _SYSTEM_PROMPT}, {"role": "user", "content": user}]

    @staticmethod
    def _status(answer: dict[str, Any]) -> str:
        value = answer.get("response_status")
        if value in {"answered", "ambiguous", "not_found"}:
            return str(value)
        ids = answer.get("corresponding_variables")
        ids = ids if isinstance(ids, list) else []
        if not ids and answer.get("clarification_question"):
            return "ambiguous"
        if not ids and (answer.get("refusal") or answer.get("needs_verification")):
            return "not_found"
        return "answered"

    def ask(self, question: str, *, dry_run: bool = True, limit: int = 8) -> dict[str, Any]:
        del limit
        messages = self._messages(question)
        base: dict[str, Any] = {
            "status": "ready",
            "question": question,
            "dry_run": dry_run,
            "model_called": False,
            "knowledge_condition": self.condition,
            "candidate_variable_ids": [],
            "context_metadata": self.context_metadata,
            "answer": None,
            "grounding": {"variable_ids": [], "evidence_ids": [], "source_locations": []},
        }
        if dry_run:
            base["prompt_metadata"] = {
                "message_count": len(messages),
                "full_context_included": self.condition == "full_context",
            }
            return base

        base["model_called"] = True
        try:
            generated = self.model_client.generate(messages)
            # 只保存最终可见正文，便于审计格式错误；不保存 reasoning_content 或密钥。
            base["raw_model_response"] = generated
            metadata = getattr(self.model_client, "last_call_metadata", None)
            if isinstance(metadata, dict) and metadata:
                base["model_metadata"] = metadata
            answer, response_format = parse_direct_condition_response(generated)
            if response_format != "json":
                metadata = dict(base.get("model_metadata") or {})
                metadata["format_repaired"] = True
                metadata["format_repair_method"] = response_format
                base["model_metadata"] = metadata
            else:
                metadata = dict(base.get("model_metadata") or {})
                metadata["format_repaired"] = False
                metadata["format_repair_method"] = None
                base["model_metadata"] = metadata
            missing = [key for key in _REQUIRED_FIELDS if key not in answer]
            if missing:
                raise ModelClientError("模型回答缺少字段：" + ", ".join(missing))
            ids = answer.get("corresponding_variables")
            if not isinstance(ids, list) or any(not isinstance(item, str) for item in ids):
                raise ModelClientError("corresponding_variables 必须是字符串数组。")
            base["candidate_variable_ids"] = list(dict.fromkeys(ids))
            base["grounding"]["variable_ids"] = list(dict.fromkeys(ids))
            base["status"] = self._status(answer)
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
