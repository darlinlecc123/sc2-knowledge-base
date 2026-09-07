# 步骤 17 完成报告：生成面向人和 LLM 的知识文档

- 执行日期：2026-09-07
- 状态：**完成（带 1 项上游历史验证器兼容说明）**
- 范围：`storm-sc2kb-v1-raw`
- 外部模型 API：**未调用**
- StarCraft II 运行时：**未启动**
- STORM 业务源码：**未修改**

## 1. 读取的关键证据

- `knowledge/prompts/00_master_prompt.md`
- `knowledge/prompts/17_generate_docs.md`
- `knowledge/variables/*.yaml`：7 个正式变量文件，共 135 条正式变量记录
- `knowledge/retrieval/aliases.yaml`
- `knowledge/relations/variable_relations.jsonl`：1430 条关系
- `knowledge/known_issues.yaml`：11 个已知问题
- `knowledge/taxonomy/categories.yaml`
- `knowledge/taxonomy/source_layers.yaml`
- `knowledge/schemas/variable.schema.json`
- `knowledge/src/sc2kb/loader.py`
- `knowledge/src/sc2kb/cli.py`
- 步骤 1–16 已有文档、上下文、评测与离线验证产物

文档内容以机器可读变量记录、关系、已知问题和当前源码位置为依据；没有把任务提示词本身当作变量事实证据。

## 2. 新建或修改的文件

### 步骤 17 指定文档

- `knowledge/docs/index.md`：知识库总入口和“应该去哪查”导航
- `knowledge/docs/variable_catalog.md`：135 个变量的分类索引和完整详情
- `knowledge/docs/dataflow.md`：Raw → TBox/ABox → 派生状态 → 动作/SWM/指标的数据流
- `knowledge/docs/query_cookbook.md`：自然语言检索、消歧、范围识别和回答模板
- `knowledge/docs/glossary.md`：核心术语、分类、来源层、事实状态和关系类型

### 为保证可重复生成增加的辅助文件

- `knowledge/scripts/generate_step17_docs.py`：确定性生成上述 5 份文档
- `knowledge/tests/validate_step17.py`：离线检查覆盖率、源码引用、链接、状态标签和哈希
- `knowledge/manifests/step17_docs_manifest.json`：记录输入/输出 SHA-256、变量数和边界状态
- `knowledge/reports/17_generate_docs.md`：本完成报告

以上文件全部位于 `knowledge/`。

## 3. 主要生成结果

- 正式变量：135/135 全部写入变量目录
- 变量详情锚点：135/135
- 可定位源码引用：135/135
- 变量关系：1430 条，与上游关系文件一致
- 已知问题：11 个，与上游登记一致
- 文档事实状态明确区分：
  - `design_intent`
  - `code_reality`
  - `runtime_observation`
  - `derived_runtime`
  - `needs_verification`
- 每个变量条目包含：
  - 一句大白话
  - 正式定义
  - 分类与来源层
  - 接口类型、形状、单位、范围、枚举与路径
  - STORM 源码路径和符号
  - 公式或转换
  - 示例
  - 上下游关系
  - 限制和已知问题
  - 核验状态

## 4. 执行的验证

### 4.1 步骤 17 专项验证

```powershell
python knowledge\scripts\generate_step17_docs.py
python knowledge\tests\validate_step17.py
```

结果：

```text
STEP17 VALIDATION OK
documents=5
formal_variables=135
relations=1430
known_issues=11
source_references=135
external_model_called=false
sc2_executed=false
```

### 4.2 确定性生成

连续重新生成后比较 5 份目标文档 SHA-256：

```text
DETERMINISM OK: 5/5 hashes unchanged
```

### 4.3 当前 CLI 示例冒烟

```powershell
python knowledge\src\sc2kb\cli.py "单位当前血量对应哪个字段" --limit 8 --json
```

结果：

```text
CLI_SMOKE_OK status=found results=3 first=raw_unit.health
```

### 4.4 上游离线验证

以下验证通过：

- `knowledge/tests/validate_step10.py`
- `knowledge/tests/validate_step11.py`
- `knowledge/tests/validate_step12.py`
- `knowledge/tests/validate_step13.py`
- `knowledge/tests/validate_step14.py`

生成器和验收脚本也通过 `python -m py_compile`。

## 5. 主要发现

1. 当前正式知识记录可以完整生成面向研究者的 135 变量目录，无需凭记忆补全 PySC2 字段。
2. Raw、TBox、ABox、派生状态、动作、SWM 和实验指标已在导航、变量详情和数据流中分层呈现。
3. `abox.unit.armor` 实际接收 Raw `shield`、动作坐标裁剪未写回、`priority` 声明与消费不一致等问题已通过已知问题绑定进入变量详情。
4. 查询手册使用当前真实 CLI 参数；已实际冒烟验证，避免写入不存在的 `search` 子命令或 `--top-k` 参数。
5. 文档是机器可读记录的派生产物，后续应先更新 YAML/JSONL，再重新运行生成器，不建议直接手工修改自动生成文档。

## 6. 未解决问题

### 步骤 16 旧验证器状态断言过期

运行 `knowledge/tests/validate_step16.py` 时失败在：

```text
assert data["status"] == "planned"
```

原因是该验证器仍按步骤 16 最初的“仅计划”状态编写，而步骤 16 后续已经执行了模型评测，`model_matrix.yaml` 的状态已发生合理变化。该失败不表示步骤 17 文档错误。

本步骤没有擅自修改步骤 16 的历史验证器。建议后续单独将其改为版本化验证：分别校验 planned 快照和 executed/current 状态，避免把历史固定断言用于当前矩阵。

### 运行时边界

本步骤未启动 SC2，因此所有需要真实 observation、地图或游戏版本确认的内容继续保持 `needs_verification`，没有升级成 `runtime_observation`。

## 7. 建议下一步

1. 执行步骤 18（若已有对应提示词），对文档链接、打包结构、许可证、版本号和发布边界进行最终整理。
2. 在发布前增加一个“文档漂移检查”：若变量 YAML 或关系 JSONL 哈希改变而文档未重新生成，则 CI 失败。
3. 单独修复/版本化 `validate_step16.py`，不要影响已经保存的历史实验结果。
4. 下一轮真正无偏的 RAG 泛化评估应使用新的冻结题集版本，不能继续把已暴露的 challenge v0.6 当首次盲测。
