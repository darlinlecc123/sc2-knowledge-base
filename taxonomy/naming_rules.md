# STORM 变量知识库分类与命名规范

- 规范版本：`1.0.0`
- 适用范围：`storm-sc2kb-v1-raw`
- 分类清单：`knowledge/taxonomy/categories.yaml`
- 来源层清单：`knowledge/taxonomy/source_layers.yaml`
- 变量 Schema：`knowledge/schemas/variable.schema.json`
- 核对日期：2026-09-03
- 验证状态：**静态设计；未运行 StarCraft II，未调用外部 LLM**

## 1. 一句话规则

每个变量只有一个稳定 ID、一个一级分类和一个来源层；如果同一个表面名称在 TBox、ABox、原始观测或派生层含义不同，就建立不同记录并用关系连接，绝不能为了“看起来简单”而合并。

## 2. 一级分类

步骤四要求的十个一级分类全部保存在 `categories.yaml`：

| 规范分类 ID | 展示名 | 步骤三 Schema 兼容值 | 推荐 ID 前缀 |
|---|---|---|---|
| `environment` | environment | `environment_config` | `environment.` |
| `timestep_player` | timestep/player | `timestep_player_score` | `timestep.`、`player.` |
| `raw_unit` | raw_unit | `raw_unit` | `raw_unit.` |
| `tbox_static` | tbox_static | `tbox_static` | `tbox.` |
| `abox_dynamic` | abox_dynamic | `abox_dynamic` | `abox.` |
| `derived_tactical` | derived_tactical | `derived_tactical_state` | `derived.` |
| `action_schema` | action_schema | `action_schema_and_scheduling` | `action.` |
| `pysc2_function_call` | pysc2_function_call | `pysc2_function_call` | `pysc2.` |
| `swm` | swm | `swm` | `swm.` |
| `experiment_metric` | experiment_metric | `experiment_metric` | `metric.` |

步骤四短分类名与步骤三 Schema 的部分枚举不同。本步骤不静默修改上游 Schema，而在 `categories.yaml` 显式保存映射。当前创建变量卡片时，检索治理使用 `categories[].id`，写入变量记录的 `category` 使用 `schema_category`。后续统一时必须升级 Schema 版本并提供迁移脚本。

## 3. 分类互斥性与交叉关系

每条变量记录必须有且只有一个一级分类。分类依据是“这条记录描述的变量在当前阶段是什么”，而不是“它最早来自哪个文件”。

例如：

- `raw_unit.health` 是 RawUnit 解析字段；
- `abox.unit.hp` 是 ABox 实例字段；
- `derived.tactical.health_status` 是聚合后的战术摘要量。

三者可以存在数据流关系，但不能合并成一条记录，也不能让一条记录同时属于三个一级分类。

跨分类只通过以下关系表达：`derived_from`、`transformed_to`、`consumed_by`、`constrains`、`distinct_from`、`related_to`。

```text
raw_unit.health
  --transformed_to--> abox.unit.hp
  --derived_from----> derived.tactical.health_status
```

## 4. 来源层级

步骤四要求的九个来源层全部定义在 `source_layers.yaml`：

1. `raw_observation`
2. `static_ontology`
3. `runtime_abox`
4. `derived_runtime`
5. `llm_output`
6. `parser_validated`
7. `executor_mapped`
8. `model_predicted`
9. `experiment_aggregated`

另增加一个有明确理由的边界层 `environment_config`，表示调用 SC2Env 或 Agent 前传入的配置。若强行归入 `raw_observation`，会把“输入配置”和“环境返回观测”混为一谈。

三种概念不能混写：

- category 回答“它是哪一类变量”；
- source layer 回答“它在数据流哪一层产生”；
- fact status 回答“当前断言是什么证据状态”。

事实状态必须使用步骤三 Schema 中的固定英文标签，并保留以下边界：

- `design_intent`：设计目标、注释或文档声明，不能自动视为代码已经实现；
- `code_reality`：当前源码或静态数据直接体现的实现事实；
- `runtime_observation`：必须来自实际运行观测，本步骤未运行 SC2 时不得填写为已验证；
- `derived_runtime`：由运行时输入按当前代码计算得到的派生值，不能冒充原始观测；
- `needs_verification`：证据不足、依赖外部接口语义或尚未运行验证时使用，禁止凭常识补全。

因此 `model_predicted` 不能当作 `runtime_observation`，历史 CSV 中的 `experiment_aggregated` 也不能自动代表当前代码结果。

## 5. 稳定 ID 规范

### 5.1 字符规则

稳定 ID 必须：

- 全部使用小写 ASCII；
- 单词之间使用 `snake_case`；
- 层级之间使用点号 `.`；
- 匹配正则 `^[a-z0-9]+(?:[._-][a-z0-9]+)*$`；
- 不包含空格、中文、斜杠、Python 行号、绝对路径或当前数值；
- 创建后原则上不可修改。

推荐结构：

```text
<prefix>.<object-or-namespace>.<property>[.<qualifier>]
```

段数由语义决定，但第一段必须来自前缀注册表。

### 5.2 前缀注册表

| 前缀 | 分类 | 示例 |
|---|---|---|
| `environment` | environment | `environment.step_mul` |
| `timestep` | timestep/player | `timestep.is_last` |
| `player` | timestep/player | `player.minerals` |
| `raw_unit` | raw_unit | `raw_unit.health_ratio` |
| `tbox` | tbox_static | `tbox.unit.marine.attack_range` |
| `abox` | abox_dynamic | `abox.unit.hp` |
| `derived` | derived_tactical | `derived.tactical.engagement_type` |
| `action` | action_schema | `action.delay_steps` |
| `pysc2` | pysc2_function_call | `pysc2.move.function_id` |
| `swm` | swm | `swm.prediction.error` |
| `metric` | experiment_metric | `metric.action.failure_rate` |

前缀与分类的映射必须确定。禁止创建含义不明的顶层前缀，如 `state.`、`value.` 或 `misc.`。

## 6. 规范名规则

`canonical_name` 是面向人和检索系统的规范术语，不等同于稳定 ID。优先级如下：

1. 当前代码真实字段名，例如 `health_ratio`、`delay_steps`；
2. 当前代码输出的精确标签，例如 `Engagement_Type`；
3. 静态容器中的完整访问名，例如 `Marine.attack_range`；
4. 没有现成代码名时使用简洁英文 `snake_case` 概念名，并标记命名依据。

不得为了表面统一改变代码大小写。`names.code` 保留实现形式；同一个代码字段在不同容器中含义不同，必须通过稳定 ID 和上下文区分。

| 稳定 ID | canonical_name | names.code |
|---|---|---|
| `raw_unit.health_ratio` | `health_ratio` | `health_ratio` |
| `tbox.unit.marine.attack_range` | `Marine.attack_range` | `UNITS["Marine"]["attack_range"]` |
| `derived.tactical.engagement_type` | `Engagement_Type` | `Engagement_Type` |
| `action.delay_steps` | `delay_steps` | `delay_steps` |

## 7. 中文名规则

中文名采用“对象 + 属性 + 必要限定”：

```text
[对象/主体] + [物理量或业务属性] + [静态/当前/预测等必要限定]
```

要求：

- 区分绝对值和比例，例如“当前生命值”与“生命值比例”；
- 区分类型知识和实例状态，例如“Marine 静态攻击射程”与“当前单位实例攻击射程”；
- 区分观测、派生和预测；
- 第一次出现缩写时写出含义；
- 不写未经证据确认的单位。

不要让“血量”同时指 `health`、`health_ratio` 和平均血量，也不要让“距离”同时指坐标差、质心距离和攻击射程。

## 8. 同名异义冲突处理

### 8.1 armor

- `tbox.unit.marine.armor`：Marine 类型的静态本体属性；
- `abox.unit.armor`：当前 ABox 实例字段。

即使两者某次取值相同，也不能使用同一 ID。当前 bridge 中 ABox `armor/armor_ratio` 的赋值还有已登记语义问题，更不能用 TBox 静态 armor 解释它。

### 8.2 health / hp

至少区分：

- `raw_unit.health`：RawUnit 当前绝对生命值；
- `raw_unit.health_ratio`：RawUnit 归一化生命比例；
- `abox.unit.hp`：ABox 当前实例生命值；
- `abox.unit.hp_ratio`：ABox 当前实例生命比例；
- `tbox.unit.marine.hp`：Marine 类型静态属性；
- `derived.tactical.health_status`：多个单位聚合后的摘要。

### 8.3 attack_range

- `tbox.unit.marine.attack_range`：类型级静态声明；
- `abox.unit.attack_range`：实例节点携带的字段。

用户问“Marine 的射程是多少”时，应判断是在问静态类型知识、当前实例字段还是游戏官方值。证据不足时必须说明，不能任选一个回答。

## 9. 别名与歧义规则

`aliases` 可包含中文称呼、英文全称、缩写、代码字段名、历史规范名和常见说法。

1. 别名用于召回，不改变规范含义；
2. 精确别名可以唯一指向一个稳定 ID；
3. “血量”“armor”“距离”等歧义别名允许召回多个候选，但不得自动声称唯一匹配；
4. 结合 category、source layer、对象和上下文消歧；
5. 拼写错误可以作为兼容别名，但不能成为 canonical_name；
6. 步骤七建立别名字典时必须保存歧义候选集合。

## 10. 新增变量流程

1. **范围检查**：确认当前 STORM 实际读取、转换、生成、校验或使用该量。
2. **证据检查**：核心变量至少有当前代码或静态数据证据。
3. **粒度检查**：原始、转换、容器、实例、派生或指标等不同语义拆分记录。
4. **分类**：从 `categories.yaml` 选择唯一一级分类。
5. **来源层**：从 `source_layers.yaml` 选择来源层并使用 Schema 兼容映射。
6. **生成 ID**：按前缀和语义生成候选 ID。
7. **冲突检查**：检查 ID 唯一、规范名冲突和别名歧义。
8. **填写变量卡片**：按 `variable.schema.json` 填完必填字段。
9. **关系连接**：补充 derived_from、transformed_to、distinct_from 等关系。
10. **验证**：运行解析、Schema、证据路径和状态检查。

## 11. 重命名流程

### 语义不变

- 稳定 ID 不变；
- 更新 `canonical_name` 和显示名称；
- 旧规范名加入 `aliases`；
- 记录原因和日期；
- 重新执行别名冲突测试。

### 语义改变

语义改变不是普通重命名，而是新增变量：创建新 ID，保留旧记录，建立替代关系，并在旧记录中说明迁移。禁止覆盖旧 ID 的原有含义。

## 12. 废弃流程

当前 `variable.schema.json` 1.0.0 尚未定义 `record_status`、`deprecated_at` 和 `replaced_by`，因此不能提前向变量记录写入这些未被 Schema 接受的字段。

升级 Schema 前采用兼容流程：

1. 不删除旧记录和旧 ID；
2. 添加稳定问题 ID，如 `deprecated.<old_id>`；
3. `known_issues.status` 使用 `open`；
4. 在 `limitations` 写明“已废弃，不用于新代码”；
5. 使用关系指向新 ID；
6. 旧名称保留为兼容别名；
7. 检索器降低废弃记录排序，但查询旧名时仍返回迁移说明。

后续 Schema 建议正式增加：

```yaml
record_status: active | deprecated | removed
introduced_at: <date or version>
deprecated_at: <date or null>
replaced_by: <stable-id or null>
```

以上只是后续建议，当前变量记录不得提前写入。

## 13. 兼容别名流程

1. 旧名称加入 `aliases`；
2. 记录别名来源；
3. 对大小写和下划线差异标准化匹配，但保留原始展示；
4. 旧名称若指向多个概念，返回候选列表并要求上下文消歧；
5. 不允许别名覆盖另一个活跃变量的稳定 ID；
6. 删除别名前检查基准问题集和历史查询日志。

## 14. 维护检查

- 一级分类存在且唯一；
- 稳定 ID 合法且全库唯一；
- ID 第一段已在前缀注册表登记；
- category 与前缀映射一致；
- source layer 与 category 的组合允许；
- 三种名称非空；
- 同名异义记录没有被合并；
- 歧义别名没有造成错误唯一匹配；
- 证据路径存在，行号没有越界；
- `design_intent` 与 `code_reality` 分开；
- 未运行的 SC2、LLM、SWM 或实验没有标成成功；
- 所有生成文件位于 `knowledge/`。

## 15. 当前未解决问题

1. 步骤三 Schema 枚举与步骤四短名称尚未进行版本级统一，目前依赖显式映射。
2. Schema 1.0.0 尚无正式记录生命周期字段，废弃流程只能兼容表达。
3. 歧义别名的机器可读倒排索引将在步骤七建立。
4. 本步骤只定义规则；步骤五应按本规范批量提取变量。
5. PySC2 官方字段语义和版本信息仍需后续证据核验。
