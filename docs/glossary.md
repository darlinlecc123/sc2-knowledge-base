# 术语表

> 本页解释术语在当前 STORM Raw API 知识库中的严格含义，不是完整 SC2 百科。

<!-- 由 knowledge/scripts/generate_step17_docs.py 自动生成。 -->

## 1. 核心术语

| 术语 | 当前项目中的含义 |
|---|---|
| **Raw API** | 当前项目使用的 PySC2 原始单位/动作接口边界；第一版不含 feature layer/RGB。 |
| **TimeStep** | 环境一次 step 返回的对象；只收录 STORM 当前实际读取部分。 |
| **RawUnit** | observation.raw_units 中的单位对象；只收录当前代码读取字段。 |
| **TBox** | 类型层静态本体知识，不等于当前战局实例值。 |
| **ABox** | BattlefieldGraph 根据观测建立的实例事实，可能混合 Raw、TBox 和 fallback。 |
| **BattlefieldGraph** | 使用 networkx.DiGraph 组织 TBox/ABox 并生成战术摘要的图结构。 |
| **派生变量** | 经公式、归一化、聚合、阈值或映射得到，不是原始字段。 |
| **lineage / 数据血缘** | 变量的上游来源、转换以及下游消费者链。 |
| **稳定 ID** | 跨文件和评测使用的主键，例如 raw_unit.health。 |
| **alias / 别名** | 用户可能使用的中文、英文或代码表达，可能需要跨层消歧。 |
| **source layer** | 值或断言来自数据流的哪一层，与 category 是不同维度。 |
| **design intent** | 设计或文档希望实现的行为，可能与代码现实不同。 |
| **code reality** | 当前源码、配置或静态数据直接确认的行为。 |
| **runtime observation** | 实际运行记录；静态审查不能冒充运行结果。 |
| **needs verification** | 证据不足，需要运行或接口核验。 |
| **ResponseParser** | 解析 LLM 动作并进行当前实现中的语义校验。 |
| **ActionExecutor** | 把验证后动作映射为 PySC2 Raw FunctionCall。 |
| **FunctionCall** | PySC2 动作调用对象，具体函数和参数以 executor 映射为准。 |
| **delay_steps** | 动作延迟的环境/Agent 步数，不能无依据换算成现实秒。 |
| **SWM** | 状态世界模型分支；预测不是实际观测。 |
| **RAG** | 先检索相关知识，再把有限证据交给 LLM 生成回答。 |
| **full-context** | 每题提供全部静态知识，不做查询专属检索。 |
| **no-KB** | 不向模型提供本知识库的对照条件。 |
| **grounding / 证据绑定** | 回答能回指变量记录、关系与源码证据。 |

## 2. 变量分类

| 分类 ID | 中文名 | 定义 |
|---|---|---|
| `environment_config` | 环境与 Agent 配置 | 运行前设置，会影响接口、时间推进或 Agent 行为。 当前 8 个。 |
| `timestep_player_score` | TimeStep、玩家与得分 | 从 PySC2 TimeStep/observation 边界读取的信息。 当前 8 个。 |
| `raw_unit` | RawUnit 原始单位字段 | STORM 实际从 raw_units 读取或紧邻读取后转换的单位状态。 当前 10 个。 |
| `tbox_static` | TBox 静态本体 | 仓库预定义并由本体构建/加载流程提供的静态知识。 当前 19 个。 |
| `abox_dynamic` | ABox 运行时实例 | BattlefieldGraph 根据观测、TBox 与 fallback 构造或更新的事实。 当前 28 个。 |
| `derived_tactical_state` | 派生战术状态 | 由观测或 ABox 按公式、聚合或阈值计算的战术量。 当前 13 个。 |
| `action_schema_and_scheduling` | 动作 Schema 与调度 | LLM 动作输出、解析、校验和延迟执行字段。 当前 12 个。 |
| `pysc2_function_call` | PySC2 FunctionCall | ActionExecutor 映射到 PySC2 Raw FunctionCall 的函数与参数。 当前 9 个。 |
| `swm` | SWM 变量 | 状态世界模型的输入、预测、候选和误差字段。 当前 13 个。 |
| `experiment_metric` | 实验指标 | 实验代码实际计算、聚合或写出的指标。 当前 15 个。 |

## 3. 来源层

| 来源层 | 含义 |
|---|---|
| `environment_config` | 运行前配置输入 |
| `pysc2_timestep` | PySC2 TimeStep/observation 直接读取 |
| `pysc2_raw_observation` | PySC2 Raw observation/RawUnit 直接读取 |
| `raw_unit_transformed` | 紧邻 RawUnit 读取后的归一化或转换 |
| `tbox_static` | 静态本体声明 |
| `abox_runtime` | 运行时 ABox 实例 |
| `derived_runtime` | 运行时公式、聚合或阈值派生 |
| `llm_output` | LLM 原始动作输出 |
| `validated_action` | 解析与校验后的动作 |
| `executor_mapping` | PySC2 FunctionCall 执行映射 |
| `swm_prediction` | SWM 输入、输出或预测 |
| `experiment_aggregate` | 实验级统计与落盘 |

## 4. 事实状态

| 状态 | 含义 |
|---|---|
| `design_intent` | 设计目标、注释或文档承诺，不能自动视为已经实现。 |
| `code_reality` | 由当前仓库源码、配置或静态数据直接确认。 |
| `runtime_observation` | 来自实际运行观测；静态审查不能使用此标签。 |
| `derived_runtime` | 由运行时输入按当前公式得到，不是 PySC2 原始字段。 |
| `needs_verification` | 证据不足，仍需 SC2、接口或专门测试核验。 |

## 5. 关系类型

这些关系表示当前代码和知识记录中的血缘或映射，不自动证明外部游戏机制。

| 关系 | 阅读方式 |
|---|---|
| `aggregated_into` | 计数、求和、平均或列表化。 |
| `aliases` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `evaluated_by` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `mapped_to` | 字段或参数映射。 |
| `normalized_as` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `predicts` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `read_from` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `stored_as` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `transformed_to` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `used_by` | 具体含义以关系边的 summary 与 evidence 为准。 |
| `validated_by` | 由解析或验证规则检查。 |

## 6. 易混淆术语

- **health vs hp**：Raw 常用 health，ABox 映射常用 hp，必须看完整 ID。
- **armor vs shield**：当前 ABox armor 实际来自 Raw shield，是已登记错配。
- **静态最大值 vs 当前值**：TBox 属性、Raw 当前值、比例不能互换。
- **动作 confidence vs SWM confidence**：生产者和消费者不同。
- **prediction vs observation**：预测不是事实；实际下一状态到来后才能计算误差。
