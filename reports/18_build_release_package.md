# 步骤 18 完成报告：构建可分发知识库包

- 执行日期：2026-09-07
- 状态：**完成（已采用 Apache License 2.0）**
- 版本：`0.1.0`
- 范围：`storm-sc2kb-v1-raw`
- 外部模型 API：**未调用**
- StarCraft II：**未启动**
- 外部账号：**未访问**
- GitHub/远端仓库：**未上传**
- STORM 业务源码：**未修改**

## 1. 简明结论

步骤 18 已生成两个可重复构建的本地 ZIP：

| 包 | 用途 | 包内文件数 | 大小 | SHA-256 |
|---|---|---:|---:|---|
| `storm-sc2kb-0.1.0-minimal.zip` | 无外部 API 的核心变量离线查询 | 27 | 243,000 bytes | `02a4920e6154660f88992f6780242827b6fd98c6f77688f593fd8e3347af3f2a` |
| `storm-sc2kb-0.1.0-full.zip` | 维护、上下文生成、离线评测和复现 | 195 | 999,724 bytes | `6215fb25b127bfe0897c4f8230e1ff7105a3ff2634e3f445571844e5dc508626` |

minimal 包已经实际解压，并用包内 CLI 查询“单位当前血量对应哪个字段”；返回 `status=found`，首项为 `raw_unit.health`。

## 2. 读取的关键证据

- `knowledge/prompts/00_master_prompt.md`
- `knowledge/prompts/18_build_release_package.md`
- 步骤 10–17 的检索器、上下文、QA Agent、评测、离线测试与文档产物
- `knowledge/src/sc2kb/{__init__,loader,search,cli}.py`
- `knowledge/variables/*.yaml`：7 个正式变量文件，共 135 条记录
- `knowledge/retrieval/aliases.yaml`
- `knowledge/relations/variable_relations.jsonl`：1430 条关系
- `knowledge/known_issues.yaml`：11 个已知问题
- `knowledge/manifests/step17_docs_manifest.json`
- `knowledge/reports/17_generate_docs.md`

发布事实以当前机器可读记录、实现和已完成验证为依据，没有把步骤提示词当作变量事实来源。

## 3. 新建或修改的文件

### 步骤 18 指定产物

- `knowledge/VERSION`
- `knowledge/CHANGELOG.md`
- `knowledge/CITATION.cff`
- `knowledge/release/MANIFEST.json`
- `knowledge/release/README_RELEASE.md`
- `knowledge/dist/storm-sc2kb-0.1.0-minimal.zip`
- `knowledge/dist/storm-sc2kb-0.1.0-full.zip`

### 必要辅助产物

- `knowledge/LICENSE`：Apache License 2.0 官方完整文本
- `knowledge/LICENSE_CANDIDATE.md`：保留许可证选择的历史决策记录
- `knowledge/requirements-minimal.txt`：minimal 包的最小 Python 依赖
- `knowledge/dist/SHA256SUMS`：两个归档的外层校验和
- `knowledge/scripts/build_step18_release.py`：确定性打包脚本
- `knowledge/tests/validate_step18_release.py`：纯离线发布验收程序
- `knowledge/reports/18_build_release_package.md`：本报告

没有覆盖已经过时但仍可能有历史价值的 `knowledge/README.md`；发布入口单独使用 `release/README_RELEASE.md`。

## 4. 包内容设计

### 4.1 minimal

包含版本、变更日志、引用、许可证候选说明、5 份步骤 17 核心文档、7 类正式变量、schema、别名、1430 条关系、11 个已知问题，以及可直接运行的 `sc2kb` loader/search/CLI。

最小运行要求：

- Python >= 3.11
- PyYAML >= 6.0

### 4.2 full

在 minimal 基础上，加入安全审计通过的：

- LLM 上下文；
- 血缘、taxonomy、模板和 manifests；
- 生成脚本与离线测试；
- QA Agent、三条件评测代码；
- 公开开发集、challenge 题集、冻结 manifest/receipt/lock；
- 不含敏感配置的研究文档和报告。

full 共纳入 194 个源文件，加 1 个包内 `PACKAGE_MANIFEST.json`，因此 ZIP 内共 195 个文件。

## 5. 安全审计与排除

构建器采用安全白名单，并对文本内容检查私人绝对路径、疑似 API Key 和 Bearer token。总计记录 590 个排除项，主要包括：

- `evals/results/`：447 个结果文件；
- `evals/analysis/`：21 个分析文件；
- `evals/configs/`：9 个模型/中转站配置文件；
- Python 缓存：43 个；
- 含私人 Python 或用户绝对路径的旧文档/提示词：8 个；
- 旧 `knowledge/README.md`：内容状态已过时；
- `tests/test_model_runtime_metadata.py`：虽然只有 `not-a-real-key` 离线桩，仍按通用明文 key 规则保守排除；
- `tests/validate_step16.py`：仍断言步骤 16 为 planned，与后来已执行的模型评测状态不兼容。

两个 ZIP 均未包含 `.env`、日志、`*.pyc`、`__pycache__`、模型结果目录、模型配置目录或私人绝对路径。

## 6. 执行的验证

### 6.1 语法检查

```powershell
python -m py_compile knowledge\scripts\build_step18_release.py knowledge\tests\validate_step18_release.py
```

结果：通过。

### 6.2 发布构建

```powershell
python knowledge\scripts\build_step18_release.py
```

结果：生成 minimal/full ZIP、外层 manifest 和 `SHA256SUMS`。

### 6.3 包内完整性与安全验证

```powershell
python knowledge\tests\validate_step18_release.py
```

结果：

```text
STEP18 VALIDATION OK
packages=2
minimal_smoke={"status": "found", "first": "raw_unit.health", "contains_raw_unit_health": true}
external_api_called=false
sc2_executed=false
uploaded=false
```

验收程序验证了：

1. 外层 ZIP SHA-256 与 `release/MANIFEST.json` 一致；
2. ZIP 内 `PACKAGE_MANIFEST.json` 的全部文件大小和 SHA-256 一致；
3. ZIP 文件名没有缓存、日志、结果/分析/配置目录；
4. UTF-8 文本没有命中私人路径或真实密钥形态；
5. minimal 包可独立解压和查询核心变量。

### 6.4 确定性重建

连续两次构建的两个 ZIP SHA-256 完全一致：

```text
storm-sc2kb-0.1.0-minimal.zip  stable=true
storm-sc2kb-0.1.0-full.zip     stable=true
DETERMINISM_OK
```

## 7. 主要发现

1. 现有 `knowledge/README.md` 仍声称制作步骤和外部模型测试尚未执行，不能作为当前发布首页。
2. 项目负责人已选择 Apache License 2.0，正式完整文本已写入根目录 `LICENSE`。
3. 工作区当前无法提供 Git repository 元数据，因此本版以文件 SHA-256、包内 manifest 和冻结题集凭据保证可追溯性。
4. 发布包的核心事实规模为 135 个正式变量、1430 条关系和 11 个已知问题。

## 8. 未解决问题

- 正式许可证已确认为 Apache License 2.0；个人作者和版权主体展示信息仍可在后续版本补充。
- 如未来改为代码与知识数据双许可证，需要另行完成兼容性审查和版本说明。
- 需要真实 SC2 运行确认的记录仍保持 `needs_verification`，本步骤没有把它们提升为已验证事实。
- 本步骤只准备本地候选包，没有创建 Git tag、GitHub Release、DOI 或永久下载链接。

## 9. 建议下一步

进入步骤 19 内部验收：由另一名维护者在干净目录中只使用发布 ZIP，复核安装、查询、引用、许可证状态、安全清单和 challenge 冻结凭据。许可证已经确认；公开发布仍需执行步骤 20 的路径白名单、安全扫描和 GitHub 暂存审计。
