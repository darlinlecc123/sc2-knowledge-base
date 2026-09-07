"""SC2KB 可插拔模型客户端。

默认不启用任何远程模型。真实密钥只允许通过指定环境变量读取，
不会写入配置、日志或异常文本。
"""
from __future__ import annotations

import importlib
import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Protocol

import yaml


class ModelClient(Protocol):
    """问答 Agent 所需的最小模型接口。"""

    def generate(self, messages: list[dict[str, str]], **kwargs: Any) -> str:
        """根据消息生成文本；推荐返回 JSON 对象字符串。"""


class ModelClientError(RuntimeError):
    """模型配置或调用错误；metadata 只允许携带脱敏运行信息。"""

    def __init__(self, message: str, *, metadata: dict[str, Any] | None = None):
        super().__init__(message)
        self.metadata = dict(metadata or {})


class DisabledModelClient:
    """安全默认客户端，确保未显式配置时不会误调用网络。"""

    provider = "disabled"

    def generate(self, messages: list[dict[str, str]], **kwargs: Any) -> str:
        raise ModelClientError("模型客户端未启用；请使用 dry-run，或显式配置模型客户端。")


class CallableModelClient:
    """把本地 callable 适配为 ModelClient，适合测试或接入本地模型。"""

    provider = "callable"

    def __init__(self, function: Callable[..., str]):
        self.function = function

    def generate(self, messages: list[dict[str, str]], **kwargs: Any) -> str:
        return self.function(messages=messages, **kwargs)


def _usage_dict(response: Any) -> dict[str, Any] | None:
    usage = getattr(response, "usage", None)
    if usage is None:
        return None
    if hasattr(usage, "model_dump"):
        value = usage.model_dump()
        return value if isinstance(value, dict) else None
    return dict(usage) if isinstance(usage, dict) else None


def _json_object_text(text: str | None) -> bool:
    if not isinstance(text, str) or not text.strip():
        return False
    try:
        parse_json_response(text)
    except ModelClientError:
        return False
    return True


@dataclass(frozen=True)
class OpenAICompatibleClient:
    """OpenAI Python SDK 兼容客户端，并记录脱敏的最近一次调用元数据。"""

    model: str
    api_key: str
    base_url: str | None = None
    timeout_seconds: float = 60.0
    sdk_max_retries: int = 0
    temperature: float = 0.0
    max_output_tokens: int = 1500
    thinking: str | None = None
    json_mode: bool = True
    provider: str = "openai_compatible"
    last_call_metadata: dict[str, Any] = field(default_factory=dict, init=False, repr=False, compare=False)

    def generate(self, messages: list[dict[str, str]], **kwargs: Any) -> str:
        try:
            sdk = importlib.import_module("openai")
            openai_client_class = sdk.OpenAI
        except (ImportError, AttributeError) as exc:
            raise ModelClientError("缺少可用的 openai 包，无法调用 OpenAI-compatible 模型。") from exc

        client_kwargs: dict[str, Any] = {
            "api_key": self.api_key,
            "timeout": self.timeout_seconds,
            # OpenAI SDK defaults to two internal retries.  Evaluation runs need
            # transparent request counts, so retries are explicit and default off.
            "max_retries": self.sdk_max_retries,
        }
        if self.base_url:
            client_kwargs["base_url"] = self.base_url
        client = openai_client_class(**client_kwargs)
        requested_max_tokens = int(kwargs.get("max_output_tokens", self.max_output_tokens))
        request_kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "temperature": kwargs.get("temperature", self.temperature),
            "max_tokens": requested_max_tokens,
        }
        requested_json_mode = bool(kwargs.get("json_mode", self.json_mode))
        if requested_json_mode:
            request_kwargs["response_format"] = {"type": "json_object"}
        requested_thinking = kwargs.get("thinking", self.thinking)
        if requested_thinking in {"enabled", "disabled"}:
            request_kwargs["extra_body"] = {"thinking": {"type": requested_thinking}}

        # 每次调用都先清空上一次响应侧元数据。若 SDK 在获得响应对象前抛出
        # 超时/连接异常，QA Agent 只能记录请求侧信息，不能误用上次成功响应的
        # response.model、request id 等字段。
        request_metadata: dict[str, Any] = {
            "requested_model": self.model,
            "response_model": None,
            "response_id": None,
            "response_request_id": None,
            "response_created": None,
            "response_system_fingerprint": None,
            "response_service_tier": None,
            "sdk_max_retries": self.sdk_max_retries,
            "requested_max_output_tokens": requested_max_tokens,
            "requested_thinking": requested_thinking,
            "requested_json_mode": requested_json_mode,
        }
        object.__setattr__(self, "last_call_metadata", request_metadata)

        response = client.chat.completions.create(**request_kwargs)
        response_metadata: dict[str, Any] = {
            **request_metadata,
            "response_model": getattr(response, "model", None),
            "response_id": getattr(response, "id", None),
            "response_request_id": getattr(response, "_request_id", None),
            "response_created": getattr(response, "created", None),
            "response_system_fingerprint": getattr(response, "system_fingerprint", None),
            "response_service_tier": getattr(response, "service_tier", None),
        }
        if not getattr(response, "choices", None):
            metadata = {
                **response_metadata,
                "failure_reason": "missing_choice",
                "requested_max_output_tokens": requested_max_tokens,
                "usage": _usage_dict(response),
            }
            object.__setattr__(self, "last_call_metadata", metadata)
            raise ModelClientError("模型响应没有 choices。", metadata=metadata)

        choice = response.choices[0]
        message = choice.message
        content = getattr(message, "content", None)
        reasoning = getattr(message, "reasoning_content", None)
        finish_reason = getattr(choice, "finish_reason", None)
        metadata: dict[str, Any] = {
            **response_metadata,
            "finish_reason": finish_reason,
            "requested_max_output_tokens": requested_max_tokens,
            "requested_thinking": requested_thinking,
            "requested_json_mode": requested_json_mode,
            "content_length": len(content) if isinstance(content, str) else 0,
            "reasoning_content_length": len(reasoning) if isinstance(reasoning, str) else 0,
            "final_content_nonempty": bool(isinstance(content, str) and content.strip()),
            "reasoning_content_nonempty": bool(isinstance(reasoning, str) and reasoning.strip()),
            "text_source": None,
            "failure_reason": None,
            "usage": _usage_dict(response),
        }

        if isinstance(content, str) and content.strip():
            metadata["text_source"] = "content"
            object.__setattr__(self, "last_call_metadata", metadata)
            return content

        # 某些兼容接口可能仅返回 reasoning_content。只有它本身已经是合法 JSON
        # 对象时才允许作为最终回答，避免把思维链当作用户可见答案或写入结果。
        if _json_object_text(reasoning):
            metadata["text_source"] = "reasoning_content_json"
            object.__setattr__(self, "last_call_metadata", metadata)
            return str(reasoning)

        if finish_reason == "length":
            metadata["failure_reason"] = "output_truncated_before_final_content"
            message_text = "模型在输出上限处截断，未返回最终 JSON 内容。"
        elif metadata["reasoning_content_nonempty"]:
            metadata["failure_reason"] = "reasoning_present_but_final_content_empty"
            message_text = "模型只返回了非 JSON 推理字段，最终 content 为空。"
        else:
            metadata["failure_reason"] = "empty_model_content"
            message_text = "模型返回了空内容。"
        object.__setattr__(self, "last_call_metadata", metadata)
        raise ModelClientError(message_text, metadata=metadata)


def load_model_config(path: str | Path | None = None) -> dict[str, Any]:
    """读取非敏感 YAML 配置，并用 SC2KB_MODEL_* 环境变量覆盖。"""
    config: dict[str, Any] = {
        "schema_version": "1.0.0",
        "provider": "disabled",
        "model": None,
        "base_url": None,
        "api_key_env": "SC2KB_MODEL_API_KEY",
        "timeout_seconds": 60,
        "sdk_max_retries": 0,
        "temperature": 0,
        "max_output_tokens": 1500,
    }
    if path is not None:
        config_path = Path(path)
        loaded = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        if not isinstance(loaded, dict):
            raise ModelClientError("模型配置文件顶层必须是 YAML 对象。")
        config.update(loaded)

    overrides = {
        "provider": os.getenv("SC2KB_MODEL_PROVIDER"),
        "model": os.getenv("SC2KB_MODEL_NAME"),
        "base_url": os.getenv("SC2KB_MODEL_BASE_URL"),
    }
    for key, value in overrides.items():
        if value:
            config[key] = value
    return config


def build_model_client(config: dict[str, Any] | None = None) -> ModelClient:
    """按配置构建客户端；不会返回或打印密钥。"""
    config = dict(config or load_model_config())
    provider = str(config.get("provider") or "disabled").lower()
    if provider == "disabled":
        return DisabledModelClient()
    if provider not in {"openai", "openai_compatible"}:
        raise ModelClientError(f"不支持的模型 provider：{provider}")

    model = config.get("model")
    if not model:
        raise ModelClientError("已启用模型，但未配置 model。")
    api_key_env = str(config.get("api_key_env") or "SC2KB_MODEL_API_KEY")
    api_key = os.getenv(api_key_env)
    if not api_key:
        raise ModelClientError(f"已启用模型，但环境变量 {api_key_env} 未设置。")
    return OpenAICompatibleClient(
        model=str(model),
        api_key=api_key,
        base_url=config.get("base_url"),
        timeout_seconds=float(config.get("timeout_seconds", 60)),
        sdk_max_retries=int(config.get("sdk_max_retries", 0)),
        temperature=float(config.get("temperature", 0)),
        max_output_tokens=int(config.get("max_output_tokens", 1500)),
        thinking=(str(config.get("thinking")) if config.get("thinking") in {"enabled", "disabled"} else None),
        json_mode=bool(config.get("json_mode", True)),
    )


def parse_json_response(text: str) -> dict[str, Any]:
    """容忍 ```json 围栏，但拒绝非对象回答。"""
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].lstrip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    try:
        value = json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise ModelClientError("模型回答不是合法 JSON 对象。") from exc
    if not isinstance(value, dict):
        raise ModelClientError("模型回答的 JSON 顶层必须是对象。")
    return value
