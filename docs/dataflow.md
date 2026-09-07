# 数据流与变量关系

> 大白话：这里回答“一个量从哪里来、经过什么转换、最后被谁使用”。Raw 值、TBox 静态知识、ABox 动态实例和派生指标不能混为一谈。

<!-- 由 knowledge/scripts/generate_step17_docs.py 自动生成。 -->

## 1. 总体数据流

```text
SC2Env 配置
  ↓
PySC2 TimeStep / observation / raw_units
  ↓ RawAgent 读取与紧邻归一化
RawUnit / player / score
  ↓ BattlefieldGraph + 静态 TBox
运行时 ABox 节点、边和图级缓存
  ↓ 聚合、阈值和公式
派生战术状态 → Prompt → LLM 动作
  ↓ ResponseParser 校验和延迟调度
验证后动作 → ActionExecutor → PySC2 Raw FunctionCall
  ↓
下一次 TimeStep / observation

可选：ABox + 候选动作 → SWM 预测 → 再评估 → 最终动作 → 轨迹/预测误差
实验：episode 与动作日志 → 聚合指标 → CSV/JSON
```

## 2. 来源层

| 来源层 | 数量 | 定义 |
|---|---:|---|
| `abox_runtime` | 29 | 运行时 ABox 实例 |
| `derived_runtime` | 15 | 运行时公式、聚合或阈值派生 |
| `environment_config` | 9 | 运行前配置输入 |
| `executor_mapping` | 9 | PySC2 FunctionCall 执行映射 |
| `experiment_aggregate` | 15 | 实验级统计与落盘 |
| `llm_output` | 3 | LLM 原始动作输出 |
| `pysc2_raw_observation` | 8 | PySC2 Raw observation/RawUnit 直接读取 |
| `pysc2_timestep` | 6 | PySC2 TimeStep/observation 直接读取 |
| `raw_unit_transformed` | 2 | 紧邻 RawUnit 读取后的归一化或转换 |
| `swm_prediction` | 9 | SWM 输入、输出或预测 |
| `tbox_static` | 19 | 静态本体声明 |
| `validated_action` | 11 | 解析与校验后的动作 |

## 3. TBox、ABox 与 Raw 的边界

- **Raw observation**：当前 PySC2 观测直接提供或紧邻读取后计算的值。
- **TBox**：单位类型的静态声明，不是当前战场实时值。
- **ABox**：当前单位实例事实，可能混合 Raw 值、TBox 副本和 fallback。
- **派生状态**：从运行时单位集合进一步聚合或计算。
- **模型预测**：SWM 预测不是已经发生的游戏事实。

## 4. 典型链路

### 当前生命值

```text
observation.raw_units[*].health
 → raw_unit.health
 → raw_unit.health_ratio
 → abox.unit.hp / abox.unit.hp_ratio
 → derived.tactical.*_avg_hp / critical_units
```

### 位置与动作目标

```text
raw_unit.x + raw_unit.y → ABox position → 空间/距离关系
自然语言目标 → action.target → ResponseParser → pysc2.function.target → FunctionCall
```

> 已知问题：Parser 计算了坐标裁剪值但没有写回 `action.target`，不能声称越界值已经修正后传入执行器。

### shield 与 ABox armor 名称错配

```text
raw_unit.shield / shield_ratio → abox.unit.armor / armor_ratio  # 当前代码现实
```

这是实现事实，不是推荐命名；回答必须附带 `issue.abox_armor_stores_shield`。

### 延迟动作

```text
LLM action.delay_steps → Parser → 延迟队列/到期重验证 → ActionExecutor
```

`delay_steps` 是环境/Agent 步语义，没有证据时不能换算成现实秒数。

### SWM

```text
当前 ABox + candidate_action/index → SWM.predict → predicted_state/confidence
 → LLM 再评估 → 实际下一状态 → prediction_error
```

SWM 输出属于预测，在下一状态实际到来前不能标成 `runtime_observation`。

## 5. 关系图统计

当前共有 **1430** 条关系，其中 **125** 条带公式或转换摘记。

| 关系类型 | 数量 |
|---|---:|
| `aggregated_into` | 26 |
| `aliases` | 1146 |
| `evaluated_by` | 3 |
| `mapped_to` | 12 |
| `normalized_as` | 1 |
| `predicts` | 3 |
| `read_from` | 42 |
| `stored_as` | 109 |
| `transformed_to` | 7 |
| `used_by` | 79 |
| `validated_by` | 2 |

## 6. 公式依赖示例

以下从关系图确定性展示前 30 条“上下游均为正式变量”的公式边；完整内容见 JSONL。

| 上游 | 关系 | 下游 | 公式/转换 | 状态 |
|---|---|---|---|---|
| [`abox.graph.step_count`](variable_catalog.md#var-abox-graph-step-count) | `stored_as` | [`abox.relation.timestamp`](variable_catalog.md#var-abox-relation-timestamp) | timestamp 按当前 add_edge 调用参数写入 | `code_reality` |
| [`abox.unit.alliance`](variable_catalog.md#var-abox-unit-alliance) | `stored_as` | [`abox.graph.enemy_count`](variable_catalog.md#var-abox-graph-enemy-count) | enemy_count = len(enemy_units) | `code_reality` |
| [`abox.unit.alliance`](variable_catalog.md#var-abox-unit-alliance) | `aggregated_into` | [`derived.tactical.critical_units`](variable_catalog.md#var-derived-tactical-critical-units) | d.get("hp_ratio", 1.0) < 0.3 | `code_reality` |
| [`abox.unit.alliance`](variable_catalog.md#var-abox-unit-alliance) | `aggregated_into` | [`derived.tactical.enemy_avg_hp`](variable_catalog.md#var-derived-tactical-enemy-avg-hp) | enemy_avg_hp = sum | `code_reality` |
| [`abox.unit.alliance`](variable_catalog.md#var-abox-unit-alliance) | `aggregated_into` | [`derived.tactical.enemy_count`](variable_catalog.md#var-derived-tactical-enemy-count) | enemy_count = len(enemy_units) | `code_reality` |
| [`abox.unit.alliance`](variable_catalog.md#var-abox-unit-alliance) | `aggregated_into` | [`derived.tactical.friendly_avg_hp`](variable_catalog.md#var-derived-tactical-friendly-avg-hp) | friendly_avg_hp = sum | `code_reality` |
| [`abox.unit.alliance`](variable_catalog.md#var-abox-unit-alliance) | `aggregated_into` | [`derived.tactical.friendly_count`](variable_catalog.md#var-derived-tactical-friendly-count) | friendly_count = len(friendly_units) | `code_reality` |
| [`abox.unit.alliance`](variable_catalog.md#var-abox-unit-alliance) | `aggregated_into` | [`derived.tactical.ready_to_fire_count`](variable_catalog.md#var-derived-tactical-ready-to-fire-count) | ready_to_fire = sum | `code_reality` |
| [`abox.unit.hp_ratio`](variable_catalog.md#var-abox-unit-hp-ratio) | `aggregated_into` | [`derived.tactical.critical_units`](variable_catalog.md#var-derived-tactical-critical-units) | d.get("hp_ratio", 1.0) < 0.3 | `code_reality` |
| [`abox.unit.hp_ratio`](variable_catalog.md#var-abox-unit-hp-ratio) | `aggregated_into` | [`derived.tactical.enemy_avg_hp`](variable_catalog.md#var-derived-tactical-enemy-avg-hp) | enemy_avg_hp = sum | `code_reality` |
| [`abox.unit.hp_ratio`](variable_catalog.md#var-abox-unit-hp-ratio) | `aggregated_into` | [`derived.tactical.friendly_avg_hp`](variable_catalog.md#var-derived-tactical-friendly-avg-hp) | friendly_avg_hp = sum | `code_reality` |
| [`abox.unit.position`](variable_catalog.md#var-abox-unit-position) | `aggregated_into` | [`derived.tactical.enemy_centroid`](variable_catalog.md#var-derived-tactical-enemy-centroid) | enemy_center_x = | `code_reality` |
| [`abox.unit.position`](variable_catalog.md#var-abox-unit-position) | `aggregated_into` | [`derived.tactical.friendly_centroid`](variable_catalog.md#var-derived-tactical-friendly-centroid) | friendly_center_x = | `code_reality` |
| [`abox.unit.weapon_cooldown`](variable_catalog.md#var-abox-unit-weapon-cooldown) | `aggregated_into` | [`derived.tactical.ready_to_fire_count`](variable_catalog.md#var-derived-tactical-ready-to-fire-count) | ready_to_fire = sum | `code_reality` |
| [`action.subtype`](variable_catalog.md#var-action-subtype) | `mapped_to` | [`pysc2.build.function_id`](variable_catalog.md#var-pysc2-build-function-id) | BUILD 按 subtype 查询 BUILD_CALLS。 | `code_reality` |
| [`action.subtype`](variable_catalog.md#var-action-subtype) | `mapped_to` | [`pysc2.train.function_id`](variable_catalog.md#var-pysc2-train-function-id) | TRAIN 按 subtype 查询 TRAIN_CALLS。 | `code_reality` |
| [`action.target`](variable_catalog.md#var-action-target) | `mapped_to` | [`pysc2.function.target`](variable_catalog.md#var-pysc2-function-target) | MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。 | `code_reality` |
| [`action.target_type`](variable_catalog.md#var-action-target-type) | `mapped_to` | [`pysc2.function.target`](variable_catalog.md#var-pysc2-function-target) | MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。 | `code_reality` |
| [`action.type`](variable_catalog.md#var-action-type) | `mapped_to` | [`pysc2.attack.function_id`](variable_catalog.md#var-pysc2-attack-function-id) | ATTACK 使用编号 3。 | `code_reality` |
| [`action.type`](variable_catalog.md#var-action-type) | `mapped_to` | [`pysc2.build.function_id`](variable_catalog.md#var-pysc2-build-function-id) | BUILD 按 subtype 查询 BUILD_CALLS。 | `code_reality` |
| [`action.type`](variable_catalog.md#var-action-type) | `mapped_to` | [`pysc2.move.function_id`](variable_catalog.md#var-pysc2-move-function-id) | MOVE 使用编号 13。 | `code_reality` |
| [`action.type`](variable_catalog.md#var-action-type) | `mapped_to` | [`pysc2.train.function_id`](variable_catalog.md#var-pysc2-train-function-id) | TRAIN 按 subtype 查询 TRAIN_CALLS。 | `code_reality` |
| [`action.units`](variable_catalog.md#var-action-units) | `mapped_to` | [`pysc2.function.unit_tags`](variable_catalog.md#var-pysc2-function-unit-tags) | 经验证和映射的 tag 列表。 | `code_reality` |
| [`derived.tactical.enemy_avg_hp`](variable_catalog.md#var-derived-tactical-enemy-avg-hp) | `transformed_to` | [`derived.tactical.health_status`](variable_catalog.md#var-derived-tactical-health-status) | Health_Status: Friendly | `code_reality` |
| [`derived.tactical.enemy_centroid`](variable_catalog.md#var-derived-tactical-enemy-centroid) | `aggregated_into` | [`derived.tactical.formation_distance`](variable_catalog.md#var-derived-tactical-formation-distance) | center_distance = math.dist | `code_reality` |
| [`derived.tactical.enemy_count`](variable_catalog.md#var-derived-tactical-enemy-count) | `aggregated_into` | [`derived.tactical.force_ratio`](variable_catalog.md#var-derived-tactical-force-ratio) | Force_Ratio: {friendly_count} vs {enemy_count} | `code_reality` |
| [`derived.tactical.formation_distance`](variable_catalog.md#var-derived-tactical-formation-distance) | `transformed_to` | [`derived.tactical.engagement_type`](variable_catalog.md#var-derived-tactical-engagement-type) | d<10: Close-Combat; 10<=d<20: Medium-Range; d>=20: Long-Range | `code_reality` |
| [`derived.tactical.friendly_avg_hp`](variable_catalog.md#var-derived-tactical-friendly-avg-hp) | `transformed_to` | [`derived.tactical.health_status`](variable_catalog.md#var-derived-tactical-health-status) | Health_Status: Friendly | `code_reality` |
| [`derived.tactical.friendly_centroid`](variable_catalog.md#var-derived-tactical-friendly-centroid) | `aggregated_into` | [`derived.tactical.formation_distance`](variable_catalog.md#var-derived-tactical-formation-distance) | center_distance = math.dist | `code_reality` |
| [`derived.tactical.friendly_count`](variable_catalog.md#var-derived-tactical-friendly-count) | `aggregated_into` | [`derived.tactical.fire_readiness`](variable_catalog.md#var-derived-tactical-fire-readiness) | ready_ratio = ready_to_fire / friendly_count | `code_reality` |

## 7. 追溯步骤

1. 在变量总目录找到稳定 ID。
2. 查看 `source_layer`、`derivation_kind` 和源码符号。
3. 查看上下游链接；全量关系读取 `knowledge/relations/variable_relations.jsonl`。
4. 查看关联已知问题。
5. `needs_verification` 必须运行相应测试后才能升级结论。
