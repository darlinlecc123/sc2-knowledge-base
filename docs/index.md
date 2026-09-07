# STORM PySC2 Raw API 变量知识库

> 一句话导航：把自然语言里的“血量、位置、冷却、动作目标、预测误差”等概念对应到 STORM 变量，请从本页进入变量目录或查询手册。

<!-- 由 knowledge/scripts/generate_step17_docs.py 自动生成。 -->

## 1. 范围和事实边界

第一版只覆盖当前 STORM 实际读取、转换、生成、校验、执行或统计的 Raw API 相关变量及其 TBox、ABox、派生状态、动作、SWM 和指标；不是完整 PySC2/SC2 百科。

- 正式变量：**135** 个
- 关系边：**1430** 条
- 已知问题：**11** 个
- 本步骤未启动 StarCraft II，未调用外部模型，也未伪造论文参考文献。

## 2. 我应该去哪查？

| 我想知道 | 首选文档 |
|---|---|
| 变量含义、接口、源码、公式 | [变量总目录](variable_catalog.md) |
| Raw 到 ABox、动作或指标的数据流 | [数据流与关系](dataflow.md) |
| 自然语言怎样定位变量 | [查询手册](query_cookbook.md) |
| ABox、TBox、RawUnit、RAG 等术语 | [术语表](glossary.md) |
| 范围、来源和已知坑 | [范围说明](01_scope.md)、[来源登记](02_source_registry.md)、[已知问题](09_known_issues.md) |

## 3. 分类总览

| 分类 | 数量 | 大白话解释 |
|---|---:|---|
| [环境与 Agent 配置](variable_catalog.md#category-environment-config) | 8 | 运行前设置，会影响接口、时间推进或 Agent 行为。 |
| [TimeStep、玩家与得分](variable_catalog.md#category-timestep-player-score) | 8 | 从 PySC2 TimeStep/observation 边界读取的信息。 |
| [RawUnit 原始单位字段](variable_catalog.md#category-raw-unit) | 10 | STORM 实际从 raw_units 读取或紧邻读取后转换的单位状态。 |
| [TBox 静态本体](variable_catalog.md#category-tbox-static) | 19 | 仓库预定义并由本体构建/加载流程提供的静态知识。 |
| [ABox 运行时实例](variable_catalog.md#category-abox-dynamic) | 28 | BattlefieldGraph 根据观测、TBox 与 fallback 构造或更新的事实。 |
| [派生战术状态](variable_catalog.md#category-derived-tactical-state) | 13 | 由观测或 ABox 按公式、聚合或阈值计算的战术量。 |
| [动作 Schema 与调度](variable_catalog.md#category-action-schema-and-scheduling) | 12 | LLM 动作输出、解析、校验和延迟执行字段。 |
| [PySC2 FunctionCall](variable_catalog.md#category-pysc2-function-call) | 9 | ActionExecutor 映射到 PySC2 Raw FunctionCall 的函数与参数。 |
| [SWM 变量](variable_catalog.md#category-swm) | 13 | 状态世界模型的输入、预测、候选和误差字段。 |
| [实验指标](variable_catalog.md#category-experiment-metric) | 15 | 实验代码实际计算、聚合或写出的指标。 |

## 4. 可信状态

| 状态 | 数量 | 含义 |
|---|---:|---|
| `code_reality` | 110 | 由当前仓库源码、配置或静态数据直接确认。 |
| `derived_runtime` | 15 | 由运行时输入按当前公式得到，不是 PySC2 原始字段。 |
| `runtime_observation` | 0 | 来自实际运行观测；静态审查不能使用此标签。 |
| `needs_verification` | 10 | 证据不足，仍需 SC2、接口或专门测试核验。 |

> `code_reality` 只证明当前代码这样做，不保证字段名称的物理语义正确；回答前仍须检查已知问题。

## 5. 高频入口

- 当前生命值：[`raw_unit.health`](variable_catalog.md#var-raw-unit-health)
- 生命比例：[`raw_unit.health_ratio`](variable_catalog.md#var-raw-unit-health-ratio)
- ABox 当前生命：[`abox.unit.hp`](variable_catalog.md#var-abox-unit-hp)
- 位置：[`raw_unit.x`](variable_catalog.md#var-raw-unit-x)、[`raw_unit.y`](variable_catalog.md#var-raw-unit-y)
- 武器冷却：[`raw_unit.weapon_cooldown`](variable_catalog.md#var-raw-unit-weapon-cooldown)
- 阵营：[`raw_unit.alliance`](variable_catalog.md#var-raw-unit-alliance)
- 动作目标：[`action.target`](variable_catalog.md#var-action-target)
- 延迟：[`action.delay_steps`](variable_catalog.md#var-action-delay-steps)

## 6. LLM Agent 最短规则

1. 先定位稳定 ID，再回答，不能只凭一般 SC2 常识。
2. 明确 Raw/TBox/ABox/派生/动作/SWM/指标层。
3. 同时返回接口、源码和公式依赖。
4. `needs_verification` 与已知问题必须保留。
5. 范围外字段应说明未收录，不能补成完整 PySC2 API。
6. 程序化问答优先 RAG，不要每题重复塞入全部变量。

## 7. 维护

- 生成日期：2026-09-07
- 生成器：`knowledge/scripts/generate_step17_docs.py`
- 验收：`knowledge/tests/validate_step17.py`
- 清单：`knowledge/manifests/step17_docs_manifest.json`
