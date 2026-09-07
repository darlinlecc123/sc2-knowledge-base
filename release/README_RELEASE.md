# STORM PySC2 Raw API 变量知识库 V0.1 发布说明

- 版本：`0.1.0`
- 生成日期：`2026-09-07`
- 发布仓库：`https://github.com/darlinlecc123/sc2-knowledge-base`
- 许可证：`Apache-2.0`

## 1. 这是什么

本知识库把当前 STORM 主路径实际读取、转换、生成、校验或使用的 PySC2 Raw API 变量，以及直接产生的 TBox、ABox、派生战术状态、动作参数、SWM 变量和实验指标，整理为可检索、可回溯证据的结构化上下文。

它不是完整 PySC2 字段表，也不是 StarCraft II 百科。正式变量中的事实状态明确区分：

- `design_intent`：设计意图；
- `code_reality`：当前代码实际行为；
- `runtime_observation`：需要运行时观察的值；
- `needs_verification`：尚需进一步验证。

## 2. 两种发布包

### minimal

`storm-sc2kb-0.1.0-minimal.zip` 面向只需要离线查询的用户，包含：

- 135 个正式变量、别名、关系和已知问题；
- 本地检索器和 CLI；
- 核心文档、schema、引用与 Apache License 2.0；
- 不包含外部模型配置、模型结果或 API Key。

### full

`storm-sc2kb-0.1.0-full.zip` 面向维护者和研究复现，包含 minimal 的全部内容，以及安全审计通过的上下文、血缘、taxonomy、模板、生成脚本、离线测试、公开题集和冻结凭据。

为避免泄露或体积失控，full 明确排除：

- `evals/results/`、`evals/analysis/`；
- `evals/configs/` 和环境设置脚本；
- `.env`、日志、缓存、`__pycache__`、`*.pyc`；
- 含个人绝对路径的旧文档/提示词；
- 本次外层发布目录和归档自身。

精确包含/排除记录见 `release/MANIFEST.json`。

## 3. 安装与离线快速开始

要求：Python 3.11 或更高版本。

解压 minimal 包并进入包根目录后：

```powershell
python -m pip install -r requirements-minimal.txt
python src/sc2kb/cli.py "单位当前血量对应哪个字段" --limit 8 --json
```

预期首个核心结果包含：

```text
raw_unit.health
```

关系查询示例：

```powershell
python src/sc2kb/cli.py "" --upstream-of abox.unit.health --json
python src/sc2kb/cli.py "" --downstream-of raw_unit.health --json
```

Python 调用示例：

```python
import sys
sys.path.insert(0, "src")
from sc2kb import SearchEngine

result = SearchEngine().search("单位当前血量对应哪个字段", limit=8)
print(result["status"])
print(result["results"][0]["variable_id"])
```

## 4. 可选 LLM Agent

full 包中包含 QA Agent 和评测工具，可连接 OpenAI-compatible 接口。该能力是可选的：

- 本发布包不携带 API Key；
- 默认离线检索不会调用模型；
- 使用者必须自行提供环境变量和兼容接口；
- 正式测试前应设置费用/调用次数上限；
- 不应把模型输出当作高于源码证据的事实。

## 5. 完整性验证

在原始 `knowledge/` 工作区可执行：

```powershell
python knowledge/tests/validate_step18_release.py
Get-FileHash knowledge/dist/storm-sc2kb-0.1.0-minimal.zip -Algorithm SHA256
Get-FileHash knowledge/dist/storm-sc2kb-0.1.0-full.zip -Algorithm SHA256
```

归档外层 SHA-256 见 `dist/SHA256SUMS`，包内每个文件的哈希见各 ZIP 内的 `PACKAGE_MANIFEST.json`。

## 6. 引用

机器可读引用信息见 `CITATION.cff`。当前未编造 DOI、个人作者或邮箱；永久仓库地址记录在 `CITATION.cff`。

## 7. 许可证与使用边界

本项目采用 Apache License 2.0，完整条款见根目录 `LICENSE`。第三方名称、接口和资产不因本许可证而变成本项目自有内容。

## 8. 已知限制

1. V0.1 范围仅限当前 STORM Raw API 主路径。
2. 某些结论仍需要真实 SC2 运行确认。
3. 旧实验材料可能包含特定模型/接口环境信息，因此没有直接打入发布包。
4. 发布包使用文件 SHA-256 和 manifest 保证内容完整性；GitHub 仓库另提供版本历史。
