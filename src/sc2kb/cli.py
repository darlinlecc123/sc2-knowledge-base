"""sc2kb 命令行入口。"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

if __package__:
    from .search import SearchEngine
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from sc2kb.search import SearchEngine


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sc2kb",
        description="离线检索当前 STORM 使用的 PySC2 Raw API 及其直接衍生变量。",
    )
    parser.add_argument("query", nargs="?", default="", help="变量名、自然语言描述或别名")
    parser.add_argument("--category", help="仅保留指定 category")
    parser.add_argument("--source-path", help="仅保留证据/实现路径包含此文本的变量")
    parser.add_argument("--upstream-of", help="仅返回指定变量的直接上游正式变量")
    parser.add_argument("--downstream-of", help="仅返回指定变量的直接下游正式变量")
    parser.add_argument("--limit", type=int, default=10, help="最多返回多少条，默认 10")
    parser.add_argument("--fuzzy-threshold", type=float, default=0.56, help="模糊匹配阈值，默认 0.56")
    parser.add_argument("--json", action="store_true", help="输出完整 UTF-8 JSON")
    return parser


def _one_line(value: Any) -> str:
    if value is None:
        return "未记录"
    if isinstance(value, str):
        return " ".join(value.split()) or "未记录"
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def print_human(result: dict[str, Any]) -> None:
    status_labels = {"found": "找到", "ambiguous": "存在歧义", "not_found": "未找到"}
    print(f"状态：{status_labels.get(result['status'], result['status'])}")
    print(f"匹配阶段：{result['match_stage']}；结果数：{result['result_count']}")
    if result.get("message"):
        print(result["message"])
    if result.get("clarification_question"):
        print("需要澄清：" + result["clarification_question"])
    for number, item in enumerate(result["results"], 1):
        names = item.get("names", {})
        print(f"\n[{number}] {item['variable_id']}  ({item.get('category')})")
        print(f"  中文名：{_one_line(names.get('zh'))}")
        print(f"  英文名：{_one_line(names.get('en'))}")
        print(f"  含义：{_one_line(item.get('meaning', {}).get('definition'))}")
        print(f"  接口：{_one_line(item.get('interface'))}")
        evidence = item.get("source_evidence", [])
        print(f"  源码证据：{_one_line(evidence[:2])}")
        formulas = item.get("formula_or_transformation", {}).get("formulas", [])
        print(f"  公式/转换：{_one_line(formulas)}")
        print(f"  限制：{_one_line(item.get('limitations'))}")
        issues = item.get("known_issues", {})
        issue_ids = [entry.get("id") for entry in issues.get("step09", [])]
        print(f"  已知问题：{_one_line(issue_ids or issues.get('record_level'))}")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = SearchEngine().search(
        args.query,
        category=args.category,
        source_path=args.source_path,
        upstream_of=args.upstream_of,
        downstream_of=args.downstream_of,
        limit=args.limit,
        fuzzy_threshold=args.fuzzy_threshold,
    )
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_human(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
