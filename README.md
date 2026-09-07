# STORM PySC2 Raw API 变量知识库

面向论文写作、代码开发与 LLM Agent 的、以源码证据为基础的 STORM PySC2 Raw API 变量知识库。

> **发布状态：0.1.0 初始公开版。** 本项目采用 Apache License 2.0；内部验收仍为 `conditional_go`，已知技术限制和未通过的 RAG 门槛必须保留。

## 这个项目解决什么问题

当研究者用自然语言询问“单位当前血量对应哪个字段”“动作延迟如何表示”“某个 SWM 误差如何计算”时，LLM Agent 不应只凭预训练记忆回答。本知识库让 Agent 能够：

1. 找到当前 STORM 主路径实际使用的变量；
2. 解释物理或游戏含义、接口形式、范围和枚举；
3. 定位 STORM 中的实现文件与符号；
4. 展示上游来源、转换关系和下游用途；
5. 给出可核查证据并提示已知问题；
6. 对超出 V0.1 范围的问题明确拒答或标记待验证。

## V0.1 范围

V0.1 仅覆盖当前 STORM 代码实际读取、转换、生成、校验或使用的 PySC2 Raw API 变量，以及这些变量直接产生的 TBox、ABox、派生战术状态、动作参数、SWM 变量与实验指标。

当前发布事实规模：

- 135 个正式变量记录；
- 1430 条变量关系；
- 11 个已知问题；
- 7 类变量文件；
- minimal 与 full 两类本地候选发布包。

**不包含：**完整 PySC2 API、Feature Layer 全字段、完整 StarCraft II 百科、未经当前 STORM 代码使用的字段，以及未经运行验证的推测性语义。

## 知识状态

每项事实应区分以下状态：

| 状态 | 含义 |
|---|---|
| `design_intent` | 设计目标或文档声称的行为 |
| `code_reality` | 当前源码真实实现 |
| `runtime_observation` | 已由实际运行或测试观察到 |
| `needs_verification` | 尚需固定版本或真实 SC2 环境验证 |

当文档描述与代码实现冲突时，优先报告当前代码现实，同时保留差异说明。

## 仓库结构

| 路径 | 内容 |
|---|---|
| `variables/` | 七类正式变量记录 |
| `schemas/` | 变量数据 Schema |
| `retrieval/` | 别名、查询模式与检索数据 |
| `relations/` | 变量关系图数据 |
| `src/sc2kb/` | 本地加载、检索和问答组件 |
| `context/` | 可供 LLM 使用的上下文包 |
| `docs/` | 人类可读目录、术语表和使用说明 |
| `tests/` | 离线验证与回归测试 |
| `reports/` | 验收、评测与已知限制报告 |
| `release/` | 发布清单与候选包说明 |
| `github/` | GitHub 发布、贡献和维护材料 |

## 快速使用

### 本地自然语言检索

在知识库根目录执行：

```powershell
$env:PYTHONPATH = "src"
python -m sc2kb.cli search "单位当前血量对应哪个字段"
```

Windows 若遇到数学符号输出编码问题，临时使用：

```powershell
$env:PYTHONIOENCODING = "utf-8"
```

### 作为 LLM 上下文

- 短上下文：`context/sc2_raw_api_context_short.md`
- 标准上下文：`context/sc2_raw_api_context_standard.md`
- 推荐方式：先通过 `sc2kb` 检索相关变量和证据，再把检索结果交给 LLM，而不是默认注入全部上下文。

详细方法见 `docs/query_cookbook.md`；含本机路径或私有模型配置的历史使用说明不进入公开候选集。

## 已有评测结论

优化后的 DeepSeek v4 Flash RAG 在 challenge v0.6 回归测试中达到 90.00% 行为准确率，并比 full-context 节省 89.95% Token。但在该题集唯一一次首次盲测中，变量召回率为 84.03%（门槛 85%），原生 JSON 合规率为 98.00%（门槛 99%）。

因此准确表述是：**当前 RAG 已有明显实用价值，但尚未通过全部预先冻结的有效性门槛。** 详见 `reports/multi_model_evaluation/multi_model_test_report.md`。

## 贡献变量记录

新增或修改变量不能只提交自然语言解释。PR 必须提供：

- 稳定变量 ID 和所属层级；
- 当前 STORM 源码文件及类、函数或符号；
- 接口形式、类型、范围或枚举；
- 来源、转换和下游用途；
- 对应别名、关系与已知问题更新；
- Schema、检索和离线测试结果；
- 事实状态及仍需验证的内容。

完整要求见 `github/CONTRIBUTING.md`。

## 与 STORM、PySC2 和 StarCraft II 的关系

本知识库是围绕当前 STORM 研究代码整理的独立社区知识材料，不是 Blizzard Entertainment、DeepMind、PySC2 或任何 StarCraft II 权利人的官方产品，也不代表其认可或背书。StarCraft、StarCraft II 及相关名称和资产归各自权利人所有。本项目不分发游戏资产，也不把第三方接口定义重新授权为本项目自有内容。

## 引用

引用信息见 `CITATION.cff`。当前仓库地址已经记录；个人作者和版权主体信息仍可由项目负责人后续补充。

## 许可证

本项目采用 Apache License 2.0，完整条款见根目录 `LICENSE`。第三方名称、接口和资产仍受各自权利人的条款约束。
