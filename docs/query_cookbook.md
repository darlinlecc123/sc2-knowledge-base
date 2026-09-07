# 查询手册：从自然语言找到变量

> 大白话：先判断用户问的是哪一层、哪种量，再找稳定 ID；不要看到“血量”“护甲”“目标”就只按字面猜。

<!-- 由 knowledge/scripts/generate_step17_docs.py 自动生成。 -->

## 1. 标准流程

1. 识别对象：环境、单位、图节点、动作、SWM 或实验。
2. 识别时间语义：静态知识、当前观测、派生值、预测或实验聚合。
3. 识别形式：原始值、比例、计数、坐标、枚举、公式、代码位置或接口参数。
4. 用中文别名、英文名、代码名召回候选并归一到稳定 ID。
5. Raw/TBox/ABox 同名时根据上下文消歧，必要时要求澄清。
6. 公式、多变量和跨层 lineage 问题要展开上下游。
7. 绑定路径 + 类/函数/符号证据。
8. 范围外问题拒答；已知问题与待核验状态必须说明。

## 2. 常见映射

| 问题 | 首选变量 | 说明 |
|---|---|---|
| 单位当前还剩多少血？ | [`raw_unit.health`](variable_catalog.md#var-raw-unit-health) | 当前原始观测；若明确问图节点则查 abox.unit.hp。 |
| 血量百分比是什么？ | [`raw_unit.health_ratio`](variable_catalog.md#var-raw-unit-health-ratio) | 比例不能和原始 health 混用。 |
| 敌我阵营怎么看？ | [`raw_unit.alliance`](variable_catalog.md#var-raw-unit-alliance) | 若明确问 ABox，再查 abox.unit.alliance。 |
| ABox armor 真是护甲吗？ | [`abox.unit.armor`](variable_catalog.md#var-abox-unit-armor) | 必须说明当前实际映射到 shield。 |
| 延迟几步在哪里控制？ | [`action.delay_steps`](variable_catalog.md#var-action-delay-steps) | 继续追踪 Parser 和延迟队列。 |
| 坐标最后传给 PySC2 哪个参数？ | [`pysc2.function.target`](variable_catalog.md#var-pysc2-function-target) | 沿 executor mapping 追踪。 |
| 友军平均生命比例怎么算？ | [`derived.tactical.friendly_avg_hp`](variable_catalog.md#var-derived-tactical-friendly-avg-hp) | 公式题必须展开依赖。 |
| SWM 预测是真实观测吗？ | [`swm.predicted_unit_states`](variable_catalog.md#var-swm-predicted-unit-states) | 预测不是实际观测。 |

## 3. 按意图导航

| 意图 | 优先分类 | 同时检查 |
|---|---|---|
| 当前单位状态 | `raw_unit` | ABox 映射和派生比例 |
| 单位类型静态知识 | `tbox_static` | 不能写成当前实时值 |
| 图实例节点或边 | `abox_dynamic` | Raw 来源、TBox 副本、fallback、已知问题 |
| 战术统计/公式 | `derived_tactical_state` | 全部上游、聚合范围、除零/空集合 |
| LLM 动作字段 | `action_schema_and_scheduling` | 是否真正校验和消费 |
| 最终 PySC2 调用 | `pysc2_function_call` | 函数 ID、参数形状、executor 映射 |
| 世界模型预测 | `swm` | 输入、预测、实际下一状态与误差 |
| 论文实验指标 | `experiment_metric` | 聚合公式、写出位置与运行批次 |

## 4. 歧义处理

别名登记共有 **12** 个显式歧义组。完整内容见 `knowledge/retrieval/aliases.yaml`。

| 歧义组 | 候选变量 | 处理建议 |
|---|---|---|
| `ambiguity.alliance` | `abox.unit.alliance`, `raw_unit.alliance` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.armor` | `abox.unit.armor`, `tbox.entity.armor` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.enemy_count` | `abox.graph.enemy_count`, `derived.tactical.enemy_count` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.function_id` | `pysc2.attack.function_id`, `pysc2.build.function_id`, `pysc2.move.function_id`, `pysc2.no_op.function_id`, `pysc2.train.function_id` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.health_absolute` | `abox.unit.hp`, `raw_unit.health`, `tbox.entity.hp` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.health_ratio` | `abox.unit.hp_ratio`, `derived.tactical.enemy_avg_hp`, `derived.tactical.friendly_avg_hp`, `raw_unit.health_ratio` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.planned_actions` | `action.planned_actions`, `swm.input.planned_actions` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.score` | `metric.episode.final_score`, `metric.experiment.avg_score`, `timestep.reward_delta`, `timestep.score_cumulative_0` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.step` | `abox.graph.step_count`, `action.delay_steps`, `environment.step_mul`, `swm.prediction.step`, `swm.prediction_steps` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.tag` | `abox.unit.tag`, `pysc2.function.unit_tags`, `raw_unit.tag` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.target` | `abox.relation.target_node`, `action.target`, `pysc2.function.target` | 根据层级、时间语义和对象澄清。 |
| `ambiguity.unit_type` | `abox.unit.unit_type_id`, `raw_unit.unit_type`, `tbox.entity.unit_type_id` | 根据层级、时间语义和对象澄清。 |

## 5. 负向范围识别

以下情况应先判为范围外，而不是因为出现 Raw 关键词就强行命中：

- STORM 当前未读取的完整 PySC2 字段；
- feature layer、RGB、完整单位或科技百科；
- 没有仓库证据的游戏机制常识；
- 要求实时战局数值但没有传入 observation/ABox；
- 要求官方单位或版本语义，而记录标记为未知或待核验。

## 6. 本地检索

目的：先缩小到相关记录，再让 LLM 组织回答，避免每次提供全部 135 个变量。

```powershell
$env:PYTHONIOENCODING = "utf-8"
python knowledge/src/sc2kb/cli.py "单位当前血量对应哪个字段" --limit 8
```

以 [检索用法](10_retrieval_usage.md) 中当前验证过的入口为准，不要自行猜参数。

## 7. 回答契约

```text
对应变量：稳定 ID、规范名、层级
一句话解释与正式含义
接口：路径、类型、形状、范围/枚举、单位
实现：路径、类/函数、提取/转换
关系和公式：上下游与聚合
限制、已知问题、证据、可信状态
```

## 8. 论文和代码

- 论文可引用“当前 STORM 实现做了什么”并给仓库路径/符号，但源码位置不是学术文献。
- 代码修改前先确认接口、范围和消费者；修改本体后注意 ontology pickle 缓存。
- 历史 CSV 只代表特定运行，不自动证明当前 checkout 的效果。
