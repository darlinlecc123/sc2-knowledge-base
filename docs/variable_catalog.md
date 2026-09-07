# 变量总目录

> 这里是 135 个正式变量的人工可读视图。每个条目先用大白话解释，再给定义、接口、源码、公式、例子、关系、限制和可信状态。

<!-- 由 knowledge/scripts/generate_step17_docs.py 自动生成。 -->

## 阅读规则

- 稳定 ID 是检索和跨文档引用的主键；代码字段保留英文。
- 行号可能漂移，定位时以“路径 + 类/函数/符号”为主。
- Raw、TBox、ABox、派生量和预测不能混为一谈。
- 已知问题优先于字段字面名称。

## 分类索引

| 分类 | 数量 |
|---|---:|
| [环境与 Agent 配置](#category-environment-config) | 8 |
| [TimeStep、玩家与得分](#category-timestep-player-score) | 8 |
| [RawUnit 原始单位字段](#category-raw-unit) | 10 |
| [TBox 静态本体](#category-tbox-static) | 19 |
| [ABox 运行时实例](#category-abox-dynamic) | 28 |
| [派生战术状态](#category-derived-tactical-state) | 13 |
| [动作 Schema 与调度](#category-action-schema-and-scheduling) | 12 |
| [PySC2 FunctionCall](#category-pysc2-function-call) | 9 |
| [SWM 变量](#category-swm) | 13 |
| [实验指标](#category-experiment-metric) | 15 |

<a id="category-environment-config"></a>
## 环境与 Agent 配置

运行前设置，会影响接口、时间推进或 Agent 行为。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`environment.decision_interval`](#var-environment-decision-interval) | 决策间隔 | `environment_config` | `code_reality` |
| [`environment.map_name`](#var-environment-map-name) | 地图名 | `environment_config` | `code_reality` |
| [`environment.raw_resolution`](#var-environment-raw-resolution) | Raw 坐标分辨率 | `environment_config` | `code_reality` |
| [`environment.realtime`](#var-environment-realtime) | 实时模式 | `environment_config` | `code_reality` |
| [`environment.step_mul`](#var-environment-step-mul) | 环境步长倍数 | `environment_config` | `code_reality` |
| [`environment.use_raw_actions`](#var-environment-use-raw-actions) | 启用 Raw Actions | `environment_config` | `code_reality` |
| [`environment.use_raw_units`](#var-environment-use-raw-units) | 启用 Raw Units | `environment_config` | `code_reality` |
| [`environment.visualize`](#var-environment-visualize) | 可视化开关 | `environment_config` | `code_reality` |

<a id="var-environment-decision-interval"></a>
### `environment.decision_interval` — 决策间隔

**一句大白话：** 当前代码将 decision_interval 配置为 10。

**正式定义：** 当前代码将 decision_interval 配置为 10。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`决策间隔`, `Decision Interval`, `decision_interval`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：`environment step`（`known`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.decision_interval`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.__init__（记录行 50–50；行号可能漂移）`

代码摘记：

- `decision_interval: int = 10`

公式或转换：

- `decision_interval=10`

**示例**

- 当前实现的最小语义示例：当前代码将 decision_interval 配置为 10。 输入=`{"decision_interval": 10}`；输出=`{"decision_interval": 10}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-environment-map-name"></a>
### `environment.map_name` — 地图名

**一句大白话：** 当前代码将 map_name 配置为 'DefeatRoaches'。

**正式定义：** 当前代码将 map_name 配置为 'DefeatRoaches'。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`地图名`, `Map Name`, `map_name`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.map_name`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 77–77；行号可能漂移）`

代码摘记：

- `map_name="DefeatRoaches"`

公式或转换：

- `map_name='DefeatRoaches'`

**示例**

- 当前实现的最小语义示例：当前代码将 map_name 配置为 'DefeatRoaches'。 输入=`{"map_name": "DefeatRoaches"}`；输出=`{"map_name": "DefeatRoaches"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-environment-raw-resolution"></a>
### `environment.raw_resolution` — Raw 坐标分辨率

**一句大白话：** 当前代码将 raw_resolution 配置为 64。

**正式定义：** 当前代码将 raw_resolution 配置为 64。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`Raw 坐标分辨率`, `Raw Resolution`, `raw_resolution`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.raw_resolution`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 86–86；行号可能漂移）`

代码摘记：

- `raw_resolution=64`

公式或转换：

- `raw_resolution=64`

**示例**

- 当前实现的最小语义示例：当前代码将 raw_resolution 配置为 64。 输入=`{"raw_resolution": 64}`；输出=`{"raw_resolution": 64}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-environment-realtime"></a>
### `environment.realtime` — 实时模式

**一句大白话：** 当前代码将 realtime 配置为 False。

**正式定义：** 当前代码将 realtime 配置为 False。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`实时模式`, `Realtime Mode`, `realtime`

**接口形式**

- 数据类型：`boolean`；Python 类型：`bool`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.realtime`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 90–90；行号可能漂移）`

代码摘记：

- `realtime=False`

公式或转换：

- `realtime=False`

**示例**

- 当前实现的最小语义示例：当前代码将 realtime 配置为 False。 输入=`{"realtime": false}`；输出=`{"realtime": false}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-environment-step-mul"></a>
### `environment.step_mul` — 环境步长倍数

**一句大白话：** 当前代码将 step_mul 配置为 8。

**正式定义：** 当前代码将 step_mul 配置为 8。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`环境步长倍数`, `Environment Step Multiplier`, `step_mul`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.step_mul`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 89–89；行号可能漂移）`

代码摘记：

- `step_mul=8`

公式或转换：

- `step_mul=8`

**示例**

- 当前实现的最小语义示例：当前代码将 step_mul 配置为 8。 输入=`{"step_mul": 8}`；输出=`{"step_mul": 8}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-environment-use-raw-actions"></a>
### `environment.use_raw_actions` — 启用 Raw Actions

**一句大白话：** 当前代码将 use_raw_actions 配置为 True。

**正式定义：** 当前代码将 use_raw_actions 配置为 True。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`启用 Raw Actions`, `Use Raw Actions`, `use_raw_actions`

**接口形式**

- 数据类型：`boolean`；Python 类型：`bool`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.use_raw_actions`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 85–85；行号可能漂移）`

代码摘记：

- `use_raw_actions=True`

公式或转换：

- `use_raw_actions=True`

**示例**

- 当前实现的最小语义示例：当前代码将 use_raw_actions 配置为 True。 输入=`{"use_raw_actions": true}`；输出=`{"use_raw_actions": true}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`pysc2.function.raw_flag`](#var-pysc2-function-raw-flag)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-environment-use-raw-units"></a>
### `environment.use_raw_units` — 启用 Raw Units

**一句大白话：** 当前代码将 use_raw_units 配置为 True。

**正式定义：** 当前代码将 use_raw_units 配置为 True。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`启用 Raw Units`, `Use Raw Units`, `use_raw_units`

**接口形式**

- 数据类型：`boolean`；Python 类型：`bool`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.use_raw_units`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 84–84；行号可能漂移）`

代码摘记：

- `use_raw_units=True`

公式或转换：

- `use_raw_units=True`

**示例**

- 当前实现的最小语义示例：当前代码将 use_raw_units 配置为 True。 输入=`{"use_raw_units": true}`；输出=`{"use_raw_units": true}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-environment-visualize"></a>
### `environment.visualize` — 可视化开关

**一句大白话：** 当前代码将 visualize 配置为 False。

**正式定义：** 当前代码将 visualize 配置为 False。

**身份与来源**

- 分类：`environment_config`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`可视化开关`, `Visualization Flag`, `visualize`

**接口形式**

- 数据类型：`boolean`；Python 类型：`bool`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`SC2Env.visualize`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 91–91；行号可能漂移）`

代码摘记：

- `visualize=False`

公式或转换：

- `visualize=False`

**示例**

- 当前实现的最小语义示例：当前代码将 visualize 配置为 False。 输入=`{"visualize": false}`；输出=`{"visualize": false}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-timestep-player-score"></a>
## TimeStep、玩家与得分

从 PySC2 TimeStep/observation 边界读取的信息。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`player.food_cap`](#var-player-food-cap) | 人口上限 | `pysc2_timestep` | `code_reality` |
| [`player.food_used`](#var-player-food-used) | 已用人口 | `pysc2_timestep` | `code_reality` |
| [`player.minerals`](#var-player-minerals) | 矿物资源 | `pysc2_timestep` | `code_reality` |
| [`player.supply_remaining`](#var-player-supply-remaining) | 剩余人口 | `derived_runtime` | `derived_runtime` |
| [`player.vespene`](#var-player-vespene) | 高能瓦斯资源 | `pysc2_timestep` | `code_reality` |
| [`timestep.is_last`](#var-timestep-is-last) | 回合结束标志 | `pysc2_timestep` | `code_reality` |
| [`timestep.reward_delta`](#var-timestep-reward-delta) | 决策间得分增量 | `derived_runtime` | `derived_runtime` |
| [`timestep.score_cumulative_0`](#var-timestep-score-cumulative-0) | 累计得分首元素 | `pysc2_timestep` | `code_reality` |

<a id="var-player-food-cap"></a>
### `player.food_cap` — 人口上限

**一句大白话：** 从 player_info 索引 4 读取人口上限。

**正式定义：** 从 player_info 索引 4 读取人口上限。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`pysc2_timestep`（PySC2 TimeStep/observation 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`人口上限`, `Food Cap`, `player[4]`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.player[4]`（`needs_verification`）
- STORM 接口：`BattlefieldGraph.player_info[4]`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 933–933；行号可能漂移）`

代码摘记：

- `player_info[4]`

公式或转换：

- `food_cap=player_info[4]`

**示例**

- 当前实现的最小语义示例：从 player_info 索引 4 读取人口上限。 输入=`{"source": "current code"}`；输出=`{"player[4]": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`player.supply_remaining`](#var-player-supply-remaining)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-player-food-used"></a>
### `player.food_used` — 已用人口

**一句大白话：** 从 player_info 索引 3 读取已用人口。

**正式定义：** 从 player_info 索引 3 读取已用人口。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`pysc2_timestep`（PySC2 TimeStep/observation 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`已用人口`, `Food Used`, `player[3]`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.player[3]`（`needs_verification`）
- STORM 接口：`BattlefieldGraph.player_info[3]`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 933–933；行号可能漂移）`

代码摘记：

- `player_info[3]`

公式或转换：

- `food_used=player_info[3]`

**示例**

- 当前实现的最小语义示例：从 player_info 索引 3 读取已用人口。 输入=`{"source": "current code"}`；输出=`{"player[3]": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`player.supply_remaining`](#var-player-supply-remaining)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-player-minerals"></a>
### `player.minerals` — 矿物资源

**一句大白话：** 从 player_info 索引 1 读取矿物资源。

**正式定义：** 从 player_info 索引 1 读取矿物资源。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`pysc2_timestep`（PySC2 TimeStep/observation 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`矿物资源`, `Minerals`, `player[1]`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.player[1]`（`needs_verification`）
- STORM 接口：`BattlefieldGraph.player_info[1]`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 933–933；行号可能漂移）`

代码摘记：

- `player_info[1]`

公式或转换：

- `minerals=player_info[1]`

**示例**

- 当前实现的最小语义示例：从 player_info 索引 1 读取矿物资源。 输入=`{"source": "current code"}`；输出=`{"player[1]": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-player-supply-remaining"></a>
### `player.supply_remaining` — 剩余人口

**一句大白话：** 人口上限减去已用人口。

**正式定义：** 人口上限减去已用人口。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`剩余人口`, `Remaining Supply`, `supply_remaining`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.Resources.Supply remaining`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 933–933；行号可能漂移）`

代码摘记：

- `player_info[4] - player_info[3]`

公式或转换：

- `supply_remaining=food_cap-food_used`

**示例**

- 当前实现的最小语义示例：人口上限减去已用人口。 输入=`{"source": "current code"}`；输出=`{"supply_remaining": "按公式得到"}`

**上下游关系**

- 上游：[`player.food_cap`](#var-player-food-cap)、[`player.food_used`](#var-player-food-used)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-player-vespene"></a>
### `player.vespene` — 高能瓦斯资源

**一句大白话：** 从 player_info 索引 2 读取高能瓦斯资源。

**正式定义：** 从 player_info 索引 2 读取高能瓦斯资源。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`pysc2_timestep`（PySC2 TimeStep/observation 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`高能瓦斯资源`, `Vespene Gas`, `player[2]`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.player[2]`（`needs_verification`）
- STORM 接口：`BattlefieldGraph.player_info[2]`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 933–933；行号可能漂移）`

代码摘记：

- `player_info[2]`

公式或转换：

- `vespene=player_info[2]`

**示例**

- 当前实现的最小语义示例：从 player_info 索引 2 读取高能瓦斯资源。 输入=`{"source": "current code"}`；输出=`{"player[2]": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-timestep-is-last"></a>
### `timestep.is_last` — 回合结束标志

**一句大白话：** 通过 TimeStep.last() 判断当前步是否结束回合。

**正式定义：** 通过 TimeStep.last() 判断当前步是否结束回合。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`pysc2_timestep`（PySC2 TimeStep/observation 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`回合结束标志`, `Terminal TimeStep Flag`, `last()`

**接口形式**

- 数据类型：`boolean`；Python 类型：`bool`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.last()`（`needs_verification`）
- STORM 接口：`RawAgent.step terminal branch`

**STORM 实现与依据**

- `examples/llm_agent_example.py::main（记录行 114–114；行号可能漂移）`

代码摘记：

- `if timesteps[0].last():`

公式或转换：

- `is_last=obs.last()`

**示例**

- 当前实现的最小语义示例：通过 TimeStep.last() 判断当前步是否结束回合。 输入=`{"source": "current code"}`；输出=`{"last()": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-timestep-reward-delta"></a>
### `timestep.reward_delta` — 决策间得分增量

**一句大白话：** 相邻两次触发决策时累计分数之差；不是直接读取 TimeStep.reward。

**正式定义：** 相邻两次触发决策时累计分数之差；不是直接读取 TimeStep.reward。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`决策间得分增量`, `Decision Score Delta`, `reward`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`score point`（`known`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`RawAgent.reward`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.step（记录行 314–314；行号可能漂移）`

代码摘记：

- `self.reward = new_score - self.score`

公式或转换：

- `reward=new_score-previous_score`

**示例**

- 当前实现的最小语义示例：相邻两次触发决策时累计分数之差；不是直接读取 TimeStep.reward。 输入=`{"source": "current code"}`；输出=`{"reward": "按公式得到"}`

**上下游关系**

- 上游：[`timestep.score_cumulative_0`](#var-timestep-score-cumulative-0)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-timestep-score-cumulative-0"></a>
### `timestep.score_cumulative_0` — 累计得分首元素

**一句大白话：** 读取 score_cumulative 第 0 个元素作为累计分数。

**正式定义：** 读取 score_cumulative 第 0 个元素作为累计分数。

**身份与来源**

- 分类：`timestep_player_score`
- 来源层：`pysc2_timestep`（PySC2 TimeStep/observation 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`累计得分首元素`, `Cumulative Score Element 0`, `score_cumulative[0]`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`score point`（`known`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.score_cumulative[0]`（`needs_verification`）
- STORM 接口：`RawAgent.score`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.step（记录行 313–313；行号可能漂移）`

代码摘记：

- `obs.observation.get("score_cumulative", [0])[0]`

公式或转换：

- `score=score_cumulative[0]`

**示例**

- 当前实现的最小语义示例：读取 score_cumulative 第 0 个元素作为累计分数。 输入=`{"source": "current code"}`；输出=`{"score_cumulative[0]": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`metric.episode.final_score`](#var-metric-episode-final-score)、[`timestep.reward_delta`](#var-timestep-reward-delta)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-raw-unit"></a>
## RawUnit 原始单位字段

STORM 实际从 raw_units 读取或紧邻读取后转换的单位状态。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`raw_unit.alliance`](#var-raw-unit-alliance) | 阵营关系编码 | `pysc2_raw_observation` | `code_reality` |
| [`raw_unit.health`](#var-raw-unit-health) | 当前生命值 | `pysc2_raw_observation` | `code_reality` |
| [`raw_unit.health_ratio`](#var-raw-unit-health-ratio) | 生命值比例 | `raw_unit_transformed` | `code_reality` |
| [`raw_unit.shield`](#var-raw-unit-shield) | 当前护盾值 | `pysc2_raw_observation` | `code_reality` |
| [`raw_unit.shield_ratio`](#var-raw-unit-shield-ratio) | 护盾比例 | `raw_unit_transformed` | `code_reality` |
| [`raw_unit.tag`](#var-raw-unit-tag) | 单位标签 | `pysc2_raw_observation` | `code_reality` |
| [`raw_unit.unit_type`](#var-raw-unit-unit-type) | 单位类型编号 | `pysc2_raw_observation` | `code_reality` |
| [`raw_unit.weapon_cooldown`](#var-raw-unit-weapon-cooldown) | 武器冷却 | `pysc2_raw_observation` | `code_reality` |
| [`raw_unit.x`](#var-raw-unit-x) | 横坐标 | `pysc2_raw_observation` | `code_reality` |
| [`raw_unit.y`](#var-raw-unit-y) | 纵坐标 | `pysc2_raw_observation` | `code_reality` |

<a id="var-raw-unit-alliance"></a>
### `raw_unit.alliance` — 阵营关系编码

**一句大白话：** 相对当前代理的阵营编码；代码按 0/1/2/3/4 分组。

**正式定义：** 相对当前代理的阵营编码；代码按 0/1/2/3/4 分组。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`阵营关系编码`, `Alliance Code`, `alliance`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：`0`, `1`, `2`, `3`, `4`
- PySC2 路径：`obs.observation.raw_units[*][1]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.alliance`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 351–351；行号可能漂移）`

代码摘记：

- `"alliance": unit[1]`

公式或转换：

- `alliance=unit[1]`

**示例**

- 当前实现的最小语义示例：相对当前代理的阵营编码；代码按 0/1/2/3/4 分组。 输入=`{"source": "current code"}`；输出=`{"alliance": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.alliance`](#var-abox-unit-alliance)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-health"></a>
### `raw_unit.health` — 当前生命值

**一句大白话：** 当前绝对生命值。

**正式定义：** 当前绝对生命值。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`当前生命值`, `Current Health`, `health`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][2]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.health`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 354–354；行号可能漂移）`

代码摘记：

- `"health": unit[2]`

公式或转换：

- `health=unit[2]`

**示例**

- 当前实现的最小语义示例：当前绝对生命值。 输入=`{"source": "current code"}`；输出=`{"health": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.hp`](#var-abox-unit-hp)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- **`issue.unknown_unit_hp_default_is_static_only` / low：** 100 是未知类型静态占位，不是动态生命值覆盖。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-health-ratio"></a>
### `raw_unit.health_ratio` — 生命值比例

**一句大白话：** 索引 7 的编码值除以 255。

**正式定义：** 索引 7 的编码值除以 255。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`raw_unit_transformed`（紧邻 RawUnit 读取后的归一化或转换）
- 派生方式：`normalized`
- 可信状态：`code_reality`
- 别名：`生命值比例`, `Health Ratio`, `health_ratio`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][7]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.health_ratio`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 355–355；行号可能漂移）`

代码摘记：

- `"health_ratio": unit[7]`

公式或转换：

- `health_ratio=unit[7]/255`

**示例**

- 当前实现的最小语义示例：索引 7 的编码值除以 255。 输入=`{"source": "current code"}`；输出=`{"health_ratio": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.hp_ratio`](#var-abox-unit-hp-ratio)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 比例不是绝对值。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-shield"></a>
### `raw_unit.shield` — 当前护盾值

**一句大白话：** 当前绝对护盾值。

**正式定义：** 当前绝对护盾值。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`当前护盾值`, `Current Shield`, `shield`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][3]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.shield`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 356–356；行号可能漂移）`

代码摘记：

- `"shield": unit[3]`

公式或转换：

- `shield=unit[3]`

**示例**

- 当前实现的最小语义示例：当前绝对护盾值。 输入=`{"source": "current code"}`；输出=`{"shield": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.armor`](#var-abox-unit-armor)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- **`issue.abox_armor_stores_shield` / high：** 字段名称表达护甲，但当前数值语义是护盾。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-shield-ratio"></a>
### `raw_unit.shield_ratio` — 护盾比例

**一句大白话：** 索引 8 的编码值除以 255。

**正式定义：** 索引 8 的编码值除以 255。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`raw_unit_transformed`（紧邻 RawUnit 读取后的归一化或转换）
- 派生方式：`normalized`
- 可信状态：`code_reality`
- 别名：`护盾比例`, `Shield Ratio`, `shield_ratio`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][8]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.shield_ratio`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 357–357；行号可能漂移）`

代码摘记：

- `"shield_ratio": unit[8]`

公式或转换：

- `shield_ratio=unit[8]/255`

**示例**

- 当前实现的最小语义示例：索引 8 的编码值除以 255。 输入=`{"source": "current code"}`；输出=`{"shield_ratio": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.armor_ratio`](#var-abox-unit-armor-ratio)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 比例不是绝对值。
- **`issue.abox_armor_stores_shield` / high：** 字段名称表达护甲，但当前数值语义是护盾。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-tag"></a>
### `raw_unit.tag` — 单位标签

**一句大白话：** 单位实例的运行时标签，用于追踪和动作寻址。

**正式定义：** 单位实例的运行时标签，用于追踪和动作寻址。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`单位标签`, `Unit Tag`, `tag`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][29]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.tag`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 349–349；行号可能漂移）`

代码摘记：

- `"tag": unit[29]`

公式或转换：

- `tag=unit[29]`

**示例**

- 当前实现的最小语义示例：单位实例的运行时标签，用于追踪和动作寻址。 输入=`{"source": "current code"}`；输出=`{"tag": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.tag`](#var-abox-unit-tag)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-unit-type"></a>
### `raw_unit.unit_type` — 单位类型编号

**一句大白话：** 单位类型数字编号，用于查询 TBox。

**正式定义：** 单位类型数字编号，用于查询 TBox。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`单位类型编号`, `Unit Type ID`, `unit_type`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][0]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.unit_type`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 350–350；行号可能漂移）`

代码摘记：

- `"unit_type": unit[0]`

公式或转换：

- `unit_type=unit[0]`

**示例**

- 当前实现的最小语义示例：单位类型数字编号，用于查询 TBox。 输入=`{"source": "current code"}`；输出=`{"unit_type": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.is_unknown`](#var-abox-unit-is-unknown)、[`abox.unit.unit_type_id`](#var-abox-unit-unit-type-id)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-weapon-cooldown"></a>
### `raw_unit.weapon_cooldown` — 武器冷却

**一句大白话：** 当前武器冷却；等于 0 被近似视为可开火。

**正式定义：** 当前武器冷却；等于 0 被近似视为可开火。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`武器冷却`, `Weapon Cooldown`, `weapon_cooldown`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][25]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.weapon_cooldown`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 358–358；行号可能漂移）`

代码摘记：

- `"weapon_cooldown": unit[25]`

公式或转换：

- `weapon_cooldown=unit[25]`

**示例**

- 当前实现的最小语义示例：当前武器冷却；等于 0 被近似视为可开火。 输入=`{"source": "current code"}`；输出=`{"weapon_cooldown": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.weapon_cooldown`](#var-abox-unit-weapon-cooldown)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-x"></a>
### `raw_unit.x` — 横坐标

**一句大白话：** Raw 坐标 x 分量。

**正式定义：** Raw 坐标 x 分量。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`横坐标`, `X Coordinate`, `x`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][12]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.x`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 352–352；行号可能漂移）`

代码摘记：

- `"x": unit[12]`

公式或转换：

- `x=unit[12]`

**示例**

- 当前实现的最小语义示例：Raw 坐标 x 分量。 输入=`{"source": "current code"}`；输出=`{"x": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.position`](#var-abox-unit-position)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-raw-unit-y"></a>
### `raw_unit.y` — 纵坐标

**一句大白话：** Raw 坐标 y 分量。

**正式定义：** Raw 坐标 y 分量。

**身份与来源**

- 分类：`raw_unit`
- 来源层：`pysc2_raw_observation`（PySC2 Raw observation/RawUnit 直接读取）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`纵坐标`, `Y Coordinate`, `y`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：`obs.observation.raw_units[*][13]`（`needs_verification`）
- STORM 接口：`parsed_raw_unit.y`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.parse_raw_units（记录行 353–353；行号可能漂移）`

代码摘记：

- `"y": unit[13]`

公式或转换：

- `y=unit[13]`

**示例**

- 当前实现的最小语义示例：Raw 坐标 y 分量。 输入=`{"source": "current code"}`；输出=`{"y": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.position`](#var-abox-unit-position)

**限制与已知问题**

- 采用位置索引；需与实际 PySC2 版本核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-tbox-static"></a>
## TBox 静态本体

仓库预定义并由本体构建/加载流程提供的静态知识。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`tbox.entity.armor`](#var-tbox-entity-armor) | 类型护甲 | `tbox_static` | `code_reality` |
| [`tbox.entity.attack_damage`](#var-tbox-entity-attack-damage) | 攻击伤害 | `tbox_static` | `code_reality` |
| [`tbox.entity.attack_range`](#var-tbox-entity-attack-range) | 攻击射程 | `tbox_static` | `code_reality` |
| [`tbox.entity.attack_speed`](#var-tbox-entity-attack-speed) | 攻击速度字段 | `tbox_static` | `code_reality` |
| [`tbox.entity.build_time`](#var-tbox-entity-build-time) | 建造时间 | `tbox_static` | `code_reality` |
| [`tbox.entity.category`](#var-tbox-entity-category) | 实体类别 | `tbox_static` | `code_reality` |
| [`tbox.entity.description`](#var-tbox-entity-description) | 实体说明 | `tbox_static` | `code_reality` |
| [`tbox.entity.dps`](#var-tbox-entity-dps) | 每秒伤害 | `tbox_static` | `code_reality` |
| [`tbox.entity.gas_cost`](#var-tbox-entity-gas-cost) | 瓦斯成本 | `tbox_static` | `code_reality` |
| [`tbox.entity.hp`](#var-tbox-entity-hp) | 类型生命值 | `tbox_static` | `code_reality` |
| [`tbox.entity.mineral_cost`](#var-tbox-entity-mineral-cost) | 矿物成本 | `tbox_static` | `code_reality` |
| [`tbox.entity.movement_speed`](#var-tbox-entity-movement-speed) | 移动速度 | `tbox_static` | `code_reality` |
| [`tbox.entity.node_type`](#var-tbox-entity-node-type) | 节点类型 | `tbox_static` | `code_reality` |
| [`tbox.entity.race`](#var-tbox-entity-race) | 种族 | `tbox_static` | `code_reality` |
| [`tbox.entity.resource_type`](#var-tbox-entity-resource-type) | 资源类型 | `tbox_static` | `code_reality` |
| [`tbox.entity.sight`](#var-tbox-entity-sight) | 视野 | `tbox_static` | `code_reality` |
| [`tbox.entity.supply_cost`](#var-tbox-entity-supply-cost) | 人口成本 | `tbox_static` | `code_reality` |
| [`tbox.entity.unit_type_id`](#var-tbox-entity-unit-type-id) | 单位类型编号 | `tbox_static` | `code_reality` |
| [`tbox.relation.edge`](#var-tbox-relation-edge) | 本体关系边 | `tbox_static` | `code_reality` |

<a id="var-tbox-entity-armor"></a>
### `tbox.entity.armor` — 类型护甲

**一句大白话：** 本体数据中已收录实体的类型级静态 armor 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 armor 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`类型护甲`, `Type Armor`, `armor`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.armor`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 27–27；行号可能漂移）`

代码摘记：

- `"armor":`

公式或转换：

- `armor=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 armor 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 0, "Banshee": 0, "Barracks": 1, "CommandCenter": 1, "Drone": 0, "Hellion": 0, "Hydralisk": 0, "Marauder": 1, "Marine": 0, "Medivac": 1, "Mutalisk": 0, "Overlord": 0, "Reaper": 0, "Roach": 1, "SCV": 0, "SiegeTank": 1, "SupplyDepot": 1, "Zergling": 0}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- **`issue.ontology_pickle_may_be_stale` / medium：** 修改本体定义后若未重建缓存，运行时可能继续使用旧 TBox。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-attack-damage"></a>
### `tbox.entity.attack_damage` — 攻击伤害

**一句大白话：** 本体数据中已收录实体的类型级静态 attack_damage 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 attack_damage 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`攻击伤害`, `Attack Damage`, `attack_damage`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.attack_damage`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 28–28；行号可能漂移）`

代码摘记：

- `"attack_damage":`

公式或转换：

- `attack_damage=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 attack_damage 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 20, "Banshee": 12, "Drone": 5, "Hellion": 8, "Hydralisk": 12, "Marauder": 10, "Marine": 6, "Medivac": 0, "Mutalisk": 9, "Overlord": 0, "Reaper": 4, "Roach": 16, "SCV": 5, "SiegeTank": 15, "Zergling": 5}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.attack_damage`](#var-abox-unit-attack-damage)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-attack-range"></a>
### `tbox.entity.attack_range` — 攻击射程

**一句大白话：** 本体数据中已收录实体的类型级静态 attack_range 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 attack_range 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`攻击射程`, `Attack Range`, `attack_range`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.attack_range`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 29–29；行号可能漂移）`

代码摘记：

- `"attack_range":`

公式或转换：

- `attack_range=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 attack_range 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 0.25, "Banshee": 6.0, "Drone": 0.1, "Hellion": 5.0, "Hydralisk": 5.0, "Marauder": 6.0, "Marine": 5.0, "Medivac": 0.0, "Mutalisk": 3.0, "Overlord": 0.0, "Reaper": 5.0, "Roach": 4.0, "SCV": 0.2, "SiegeTank": 7.0, "Zergling": 0.1}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.attack_range`](#var-abox-unit-attack-range)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-attack-speed"></a>
### `tbox.entity.attack_speed` — 攻击速度字段

**一句大白话：** 本体数据中已收录实体的类型级静态 attack_speed 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 attack_speed 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`攻击速度字段`, `Attack Speed`, `attack_speed`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.attack_speed`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 66–66；行号可能漂移）`

代码摘记：

- `"attack_speed":`

公式或转换：

- `attack_speed=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 attack_speed 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 0.0, "Banshee": 0.89, "Drone": 1.07, "Hellion": 1.79, "Hydralisk": 0.59, "Marauder": 1.5, "Medivac": 0.0, "Mutalisk": 1.09, "Overlord": 0.0, "Reaper": 1.1, "Roach": 2.0, "SiegeTank": 0.74, "Zergling": 0.497}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.attack_speed`](#var-abox-unit-attack-speed)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-build-time"></a>
### `tbox.entity.build_time` — 建造时间

**一句大白话：** 本体数据中已收录实体的类型级静态 build_time 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 build_time 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`建造时间`, `Build Time`, `build_time`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.build_time`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 36–36；行号可能漂移）`

代码摘记：

- `"build_time":`

公式或转换：

- `build_time=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 build_time 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 14, "Banshee": 43, "Barracks": 46, "CommandCenter": 71, "Drone": 12, "Hellion": 21, "Hydralisk": 24, "Marauder": 21, "Marine": 25, "Medivac": 30, "Mutalisk": 24, "Overlord": 18, "Reaper": 32, "Roach": 27, "SCV": 17, "SiegeTank": 32, "SupplyDepot": 21, "Zergling": 17}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-category"></a>
### `tbox.entity.category` — 实体类别

**一句大白话：** 本体数据中已收录实体的类型级静态 category 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 category 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`实体类别`, `Entity Category`, `category`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.category`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 25–25；行号可能漂移）`

代码摘记：

- `"category":`

公式或转换：

- `category=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 category 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": "Combat", "Banshee": "Combat", "Barracks": "Production", "CommandCenter": "Main", "Drone": "Worker", "Hellion": "Combat", "Hydralisk": "Combat", "Marauder": "Combat", "Marine": "Combat", "Medivac": "Support", "Mutalisk": "Combat", "Overlord": "Support", "Reaper": "Combat", "Roach": "Combat", "SCV": "Worker", "SiegeTank": "Combat", "SupplyDepot": "Resource", "Zergling": "Combat"}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.category`](#var-abox-unit-category)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-description"></a>
### `tbox.entity.description` — 实体说明

**一句大白话：** 本体数据中已收录实体的类型级静态 description 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 description 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`实体说明`, `Description`, `description`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.description`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 37–37；行号可能漂移）`

代码摘记：

- `"description":`

公式或转换：

- `description=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 description 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": "Zerg suicide AOE unit (morphed from Zergling). Single-shot 20 splash damage (+15 vs Light) devastates clumped Marines/Zerglings. Dies on use.", "Banshee": "Terran cloakable air-to-ground gunship. High burst DPS against ground; cannot attack air. Cloaking enables harassment.", "Barracks": "Terran barracks for infantry production. Requires SupplyDepot prerequisite. Produces Marine, Reaper, Marauder and other infantry units.", "Beacon": "Score resource used for tracking minigame performance. Accumulated based on actions taken and objectives achieved during the episode.", "CommandCenter": "Terran main base building. Produces SCV workers and provides 11 population capacity. Upgradable to Planetary_Fortress or Orbital_Command.", "Drone": "Zerg worker. Gathers minerals/gas and morphs into structures (consumed). Essential for economy.", "Hellion": "Fast Terran light vehicle. Linear flame attack (+5 vs Light) excels against workers and light infantry. Fragile vs heavy fire.", "Hydralisk": "Zerg ranged unit firing both ground and air. High DPS but fragile (90 HP, 0 armor). Backbone vs Marines and air harass.", "Marauder": "Terran heavy infantry with concussive shells (slows armored). Excellent vs Roach/Stalker/Immortal. Vulnerable to massed light units.", "Marine": "Basic Terran infantry. High fire rate with low per-shot damage. Vulnerable with only 45 HP, easily eliminated by area damage. Low cost enables rapid production and numerical superiority. Effective against melee units (Zergling) due to range advantage, but struggles against high-armor units (Roach).", "Medivac": "Terran flying medic / dropship. Heals biological units (12.6 HP/s) and transports infantry (8 cargo). Cannot attack.", "Mineral": "Mineral crystals, primary resource for constructing all buildings and units. Harvested by SCV workers.", "Mutalisk": "Zerg mobile flying unit with bouncing glaive attack (3 targets). Excels at harass / map control. Weak vs Marine massed AA.", "Overlord": "Zerg supply provider and basic detector (after upgrade). Slow flying unit, vital for population cap. Cannot attack.", "Reaper": "Highly mobile Terran scout/skirmisher. Cliff-jumping ability and KD8 charge enable hit-and-run tactics. Effective against light units, weak against heavy armor.", "Roach": "Zerg medium ground unit with high HP (145) and armor, effectively resists low-damage weapons. Strong attack power with slow fire rate, excels against high-HP units.", "SCV": "Terran worker unit. Can gather minerals and gas, construct buildings, and repair mechanical units. Vulnerable with only 45 HP and no armor. Low cost allows for rapid production, but should be protected from enemy attacks. Essential for economy and infrastructure development.", "SiegeTank": "Terran heavy mech. Siege Mode unlocks splash damage at 13 range, devastating massed armies. Vulnerable to flanks while sieged.", "Supply": "Population supply limiting maximum unit count. Provided by Supply_Depot and Command_Center structures.", "SupplyDepot": "Terran supply structure providing 8 population capacity. Can raise/lower to block ground unit passage when lowered.", "VespeneGas": "Vespene gas, advanced resource for tech upgrades and advanced units. Requires Refinery construction for SCV harvesting.", "Zergling": "Cheapest Zerg melee unit with high mobility for flanking and harassment. Low HP without armor makes it vulnerable to ranged fire suppression."}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.description`](#var-abox-unit-description)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-dps"></a>
### `tbox.entity.dps` — 每秒伤害

**一句大白话：** 本体数据中已收录实体的类型级静态 dps 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 dps 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`每秒伤害`, `Damage Per Second`, `dps`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.dps`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 31–31；行号可能漂移）`

代码摘记：

- `"dps":`

公式或转换：

- `dps=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 dps 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 20.0, "Banshee": 27.0, "Drone": 4.67, "Hellion": 4.5, "Hydralisk": 20.4, "Marauder": 9.3, "Marine": 9.8, "Medivac": 0.0, "Mutalisk": 8.3, "Overlord": 0.0, "Reaper": 10.1, "SCV": 4.67, "SiegeTank": 20.3}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-gas-cost"></a>
### `tbox.entity.gas_cost` — 瓦斯成本

**一句大白话：** 本体数据中已收录实体的类型级静态 gas_cost 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 gas_cost 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`瓦斯成本`, `Gas Cost`, `gas_cost`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.gas_cost`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 34–34；行号可能漂移）`

代码摘记：

- `"gas_cost":`

公式或转换：

- `gas_cost=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 gas_cost 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 25, "Banshee": 100, "Barracks": 0, "CommandCenter": 0, "Drone": 0, "Hellion": 0, "Hydralisk": 50, "Marauder": 25, "Marine": 0, "Medivac": 100, "Mutalisk": 100, "Overlord": 0, "Reaper": 50, "Roach": 25, "SCV": 0, "SiegeTank": 125, "SupplyDepot": 0, "Zergling": 0}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-hp"></a>
### `tbox.entity.hp` — 类型生命值

**一句大白话：** 本体数据中已收录实体的类型级静态 hp 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 hp 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`类型生命值`, `Type HP`, `hp`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.hp`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 26–26；行号可能漂移）`

代码摘记：

- `"hp":`

公式或转换：

- `hp=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 hp 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 30, "Banshee": 140, "Barracks": 1000, "CommandCenter": 1500, "Drone": 40, "Hellion": 90, "Hydralisk": 90, "Marauder": 125, "Marine": 45, "Medivac": 150, "Mutalisk": 120, "Overlord": 200, "Reaper": 60, "Roach": 145, "SCV": 45, "SiegeTank": 175, "SupplyDepot": 400, "Zergling": 35}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- **`issue.ontology_pickle_may_be_stale` / medium：** 修改本体定义后若未重建缓存，运行时可能继续使用旧 TBox。
- **`issue.unknown_unit_hp_default_is_static_only` / low：** 100 是未知类型静态占位，不是动态生命值覆盖。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-mineral-cost"></a>
### `tbox.entity.mineral_cost` — 矿物成本

**一句大白话：** 本体数据中已收录实体的类型级静态 mineral_cost 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 mineral_cost 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`矿物成本`, `Mineral Cost`, `mineral_cost`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.mineral_cost`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 33–33；行号可能漂移）`

代码摘记：

- `"mineral_cost":`

公式或转换：

- `mineral_cost=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 mineral_cost 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 25, "Banshee": 150, "Barracks": 150, "CommandCenter": 400, "Drone": 50, "Hellion": 100, "Hydralisk": 100, "Marauder": 100, "Marine": 50, "Medivac": 100, "Mutalisk": 100, "Overlord": 100, "Reaper": 50, "Roach": 75, "SCV": 50, "SiegeTank": 150, "SupplyDepot": 100, "Zergling": 25}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-movement-speed"></a>
### `tbox.entity.movement_speed` — 移动速度

**一句大白话：** 本体数据中已收录实体的类型级静态 movement_speed 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 movement_speed 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`移动速度`, `Movement Speed`, `movement_speed`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.movement_speed`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 32–32；行号可能漂移）`

代码摘记：

- `"movement_speed":`

公式或转换：

- `movement_speed=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 movement_speed 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 3.5, "Banshee": 3.85, "Drone": 3.94, "Hellion": 5.95, "Hydralisk": 3.15, "Marauder": 3.15, "Marine": 3.15, "Medivac": 3.5, "Mutalisk": 5.6, "Overlord": 0.902, "Reaper": 5.25, "Roach": 3.15, "SCV": 3.94, "SiegeTank": 2.25, "Zergling": 3.85}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.movement_speed`](#var-abox-unit-movement-speed)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-node-type"></a>
### `tbox.entity.node_type` — 节点类型

**一句大白话：** 本体数据中已收录实体的类型级静态 node_type 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 node_type 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`节点类型`, `Node Type`, `node_type`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.node_type`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 22–22；行号可能漂移）`

代码摘记：

- `"node_type":`

公式或转换：

- `node_type=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 node_type 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": "Unit", "Banshee": "Unit", "Barracks": "Building", "Beacon": "Resource", "CommandCenter": "Building", "Drone": "Unit", "Hellion": "Unit", "Hydralisk": "Unit", "Marauder": "Unit", "Marine": "Unit", "Medivac": "Unit", "Mineral": "Resource", "Mutalisk": "Unit", "Overlord": "Unit", "Reaper": "Unit", "Roach": "Unit", "SCV": "Unit", "SiegeTank": "Unit", "Supply": "Resource", "SupplyDepot": "Building", "VespeneGas": "Resource", "Zergling": "Unit"}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.node_type`](#var-abox-unit-node-type)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-race"></a>
### `tbox.entity.race` — 种族

**一句大白话：** 本体数据中已收录实体的类型级静态 race 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 race 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`种族`, `Race`, `race`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.race`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 24–24；行号可能漂移）`

代码摘记：

- `"race":`

公式或转换：

- `race=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 race 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": "Zerg", "Banshee": "Terran", "Barracks": "Terran", "CommandCenter": "Terran", "Drone": "Zerg", "Hellion": "Terran", "Hydralisk": "Zerg", "Marauder": "Terran", "Marine": "Terran", "Medivac": "Terran", "Mutalisk": "Zerg", "Overlord": "Zerg", "Reaper": "Terran", "Roach": "Zerg", "SCV": "Terran", "SiegeTank": "Terran", "SupplyDepot": "Terran", "Zergling": "Zerg"}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.race`](#var-abox-unit-race)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-resource-type"></a>
### `tbox.entity.resource_type` — 资源类型

**一句大白话：** 本体数据中已收录实体的类型级静态 resource_type 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 resource_type 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`资源类型`, `Resource Type`, `resource_type`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.resource_type`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 349–349；行号可能漂移）`

代码摘记：

- `"resource_type":`

公式或转换：

- `resource_type=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 resource_type 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Beacon": "Score", "Mineral": "Mineral", "Supply": "Supply", "VespeneGas": "Gas"}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-sight"></a>
### `tbox.entity.sight` — 视野

**一句大白话：** 本体数据中已收录实体的类型级静态 sight 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 sight 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`视野`, `Sight`, `sight`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.sight`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 30–30；行号可能漂移）`

代码摘记：

- `"sight":`

公式或转换：

- `sight=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 sight 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 8, "Banshee": 10, "Drone": 8, "Hellion": 10, "Hydralisk": 9, "Marauder": 10, "Marine": 9, "Medivac": 11, "Mutalisk": 11, "Overlord": 11, "Reaper": 9, "SCV": 8, "SiegeTank": 11}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-supply-cost"></a>
### `tbox.entity.supply_cost` — 人口成本

**一句大白话：** 本体数据中已收录实体的类型级静态 supply_cost 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 supply_cost 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`人口成本`, `Supply Cost`, `supply_cost`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.supply_cost`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 35–35；行号可能漂移）`

代码摘记：

- `"supply_cost":`

公式或转换：

- `supply_cost=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 supply_cost 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 0.5, "Banshee": 3, "Drone": 1, "Hellion": 2, "Hydralisk": 2, "Marauder": 2, "Marine": 1, "Medivac": 2, "Mutalisk": 2, "Overlord": 0, "Reaper": 1, "Roach": 2, "SCV": 1, "SiegeTank": 3, "Zergling": 0.5}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-entity-unit-type-id"></a>
### `tbox.entity.unit_type_id` — 单位类型编号

**一句大白话：** 本体数据中已收录实体的类型级静态 unit_type_id 属性。

**正式定义：** 本体数据中已收录实体的类型级静态 unit_type_id 属性。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`单位类型编号`, `Unit Type ID`, `unit_type_id`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`TBox node.unit_type_id`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::UNITS / BUILDINGS / RESOURCES（记录行 23–23；行号可能漂移）`

代码摘记：

- `"unit_type_id":`

公式或转换：

- `unit_type_id=ontology node attribute`

**示例**

- 当前实现的最小语义示例：本体数据中已收录实体的类型级静态 unit_type_id 属性。 输入=`{"entity": "Marine"}`；输出=`{"known_values": {"Baneling": 9, "Banshee": 55, "Barracks": 21, "Beacon": 317, "CommandCenter": 18, "Drone": 104, "Hellion": 53, "Hydralisk": 107, "Marauder": 51, "Marine": 48, "Medivac": 54, "Mineral": 341, "Mutalisk": 108, "Overlord": 106, "Reaper": 49, "Roach": 110, "SCV": 45, "SiegeTank": 33, "SupplyDepot": 19, "VespeneGas": 342, "Zergling": 105}}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.unit.unit_class`](#var-abox-unit-unit-class)

**限制与已知问题**

- 当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。
- 未逐项用 SC2 运行时或官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-tbox-relation-edge"></a>
### `tbox.relation.edge` — 本体关系边

**一句大白话：** 类型级生产、依赖、消耗和克制等关系的边元组列表。

**正式定义：** 类型级生产、依赖、消耗和克制等关系的边元组列表。

**身份与来源**

- 分类：`tbox_static`
- 来源层：`tbox_static`（静态本体声明）
- 派生方式：`static_declaration`
- 可信状态：`code_reality`
- 别名：`本体关系边`, `Ontology Relation Edge`, `EDGES`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`ontology.data.marine_ontology.EDGES`

**STORM 实现与依据**

- `ontology/data/marine_ontology.py::EDGES（记录行 394–394；行号可能漂移）`

代码摘记：

- `EDGES =`

公式或转换：

- `edge=(source,target,attributes)`

**示例**

- 当前实现的最小语义示例：类型级生产、依赖、消耗和克制等关系的边元组列表。 输入=`{"container": "EDGES"}`；输出=`{"edge_count": 6, "relation_types": ["Consumes", "Countered_By", "Counters", "Produces", "Requires", "Upgrades"]}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.relation.effectiveness`](#var-abox-relation-effectiveness)、[`abox.relation.reason`](#var-abox-relation-reason)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-abox-dynamic"></a>
## ABox 运行时实例

BattlefieldGraph 根据观测、TBox 与 fallback 构造或更新的事实。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`abox.graph.enemy_count`](#var-abox-graph-enemy-count) | ABox 敌军节点计数 | `abox_runtime` | `code_reality` |
| [`abox.graph.step_count`](#var-abox-graph-step-count) | ABox 更新步数 | `abox_runtime` | `code_reality` |
| [`abox.relation.edge_class`](#var-abox-relation-edge-class) | 关系类别 | `abox_runtime` | `code_reality` |
| [`abox.relation.edge_type`](#var-abox-relation-edge-type) | 关系类型 | `abox_runtime` | `code_reality` |
| [`abox.relation.effectiveness`](#var-abox-relation-effectiveness) | 关系有效性 | `abox_runtime` | `code_reality` |
| [`abox.relation.reason`](#var-abox-relation-reason) | 关系原因 | `abox_runtime` | `code_reality` |
| [`abox.relation.source_node`](#var-abox-relation-source-node) | 关系源节点 | `abox_runtime` | `code_reality` |
| [`abox.relation.target_node`](#var-abox-relation-target-node) | 关系目标节点 | `abox_runtime` | `code_reality` |
| [`abox.relation.timestamp`](#var-abox-relation-timestamp) | 动态关系时间戳 | `abox_runtime` | `code_reality` |
| [`abox.unit.alliance`](#var-abox-unit-alliance) | 阵营编码 | `abox_runtime` | `code_reality` |
| [`abox.unit.armor`](#var-abox-unit-armor) | ABox armor 字段 | `abox_runtime` | `code_reality` |
| [`abox.unit.armor_ratio`](#var-abox-unit-armor-ratio) | ABox armor_ratio 字段 | `abox_runtime` | `code_reality` |
| [`abox.unit.attack_damage`](#var-abox-unit-attack-damage) | 攻击伤害 | `abox_runtime` | `code_reality` |
| [`abox.unit.attack_range`](#var-abox-unit-attack-range) | 攻击射程 | `abox_runtime` | `code_reality` |
| [`abox.unit.attack_speed`](#var-abox-unit-attack-speed) | 攻击速度字段 | `abox_runtime` | `code_reality` |
| [`abox.unit.category`](#var-abox-unit-category) | 实体类别 | `abox_runtime` | `code_reality` |
| [`abox.unit.description`](#var-abox-unit-description) | 实体说明 | `abox_runtime` | `code_reality` |
| [`abox.unit.hp`](#var-abox-unit-hp) | 实例生命值 | `abox_runtime` | `code_reality` |
| [`abox.unit.hp_ratio`](#var-abox-unit-hp-ratio) | 实例生命比例 | `abox_runtime` | `code_reality` |
| [`abox.unit.is_unknown`](#var-abox-unit-is-unknown) | 未知实体标志 | `abox_runtime` | `code_reality` |
| [`abox.unit.movement_speed`](#var-abox-unit-movement-speed) | 移动速度 | `abox_runtime` | `code_reality` |
| [`abox.unit.node_type`](#var-abox-unit-node-type) | 节点类型 | `abox_runtime` | `code_reality` |
| [`abox.unit.position`](#var-abox-unit-position) | 二维位置对象 | `abox_runtime` | `code_reality` |
| [`abox.unit.race`](#var-abox-unit-race) | 种族 | `abox_runtime` | `code_reality` |
| [`abox.unit.tag`](#var-abox-unit-tag) | 实例标签 | `abox_runtime` | `code_reality` |
| [`abox.unit.unit_class`](#var-abox-unit-unit-class) | 单位类别名 | `abox_runtime` | `code_reality` |
| [`abox.unit.unit_type_id`](#var-abox-unit-unit-type-id) | 单位类型编号 | `abox_runtime` | `code_reality` |
| [`abox.unit.weapon_cooldown`](#var-abox-unit-weapon-cooldown) | 武器冷却 | `abox_runtime` | `code_reality` |

<a id="var-abox-graph-enemy-count"></a>
### `abox.graph.enemy_count` — ABox 敌军节点计数

**一句大白话：** 当前 ABox 中 alliance 等于 4 的敌军单位节点数缓存。

**正式定义：** 当前 ABox 中 alliance 等于 4 的敌军单位节点数缓存。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`computed`
- 可信状态：`code_reality`
- 别名：`ABox 敌军节点计数`, `ABox Enemy Node Count`, `enemy_count`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.enemy_count`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 941–941；行号可能漂移）`

代码摘记：

- `self.enemy_count = enemy_count`

公式或转换：

- `enemy_count = len(enemy_units)`

**示例**

- 当前实现的最小语义示例：当前 ABox 中 alliance 等于 4 的敌军单位节点数缓存。 输入=`{"source": "current code"}`；输出=`{"enemy_count": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.alliance`](#var-abox-unit-alliance)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该缓存会在创建、删除节点或生成战术摘要时更新；不要与 derived.tactical.enemy_count 合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-graph-step-count"></a>
### `abox.graph.step_count` — ABox 更新步数

**一句大白话：** BattlefieldGraph 每次接收一批 raw_units 时递增的图更新序号。

**正式定义：** BattlefieldGraph 每次接收一批 raw_units 时递增的图更新序号。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`computed`
- 可信状态：`code_reality`
- 别名：`ABox 更新步数`, `ABox Update Step Count`, `step_count`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.step_count`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.update_from_observation（记录行 113–113；行号可能漂移）`

代码摘记：

- `self.step_count += 1`

公式或转换：

- `step_count = previous_step_count + 1`

**示例**

- 当前实现的最小语义示例：BattlefieldGraph 每次接收一批 raw_units 时递增的图更新序号。 输入=`{"source": "current code"}`；输出=`{"step_count": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`abox.relation.timestamp`](#var-abox-relation-timestamp)

**限制与已知问题**

- 这是 BattlefieldGraph 更新次数，不等同于 SC2 game loop，也不等同于 PySC2 TimeStep 数。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-relation-edge-class"></a>
### `abox.relation.edge_class` — 关系类别

**一句大白话：** ABox 边是静态关系副本还是动态动作关系。

**正式定义：** ABox 边是静态关系副本还是动态动作关系。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`关系类别`, `Relation Edge Class`, `edge_class`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：`static`, `dynamic`
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.edges[*].edge_class`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._replicate_static_relations / add_dynamic_relation（记录行 417–417；行号可能漂移）`

代码摘记：

- `edge_class="dynamic"`

公式或转换：

- `edge_class 按当前 add_edge 调用参数写入`

**示例**

- 当前实现的最小语义示例：ABox 边是静态关系副本还是动态动作关系。 输入=`{"source": "current code"}`；输出=`{"edge_class": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-relation-edge-type"></a>
### `abox.relation.edge_type` — 关系类型

**一句大白话：** ABox 边的关系类型；动态关系由 relation_type 参数写入。

**正式定义：** ABox 边的关系类型；动态关系由 relation_type 参数写入。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`关系类型`, `Relation Edge Type`, `edge_type`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.edges[*].edge_type`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._replicate_static_relations / add_dynamic_relation（记录行 416–416；行号可能漂移）`

代码摘记：

- `edge_type=relation_type`

公式或转换：

- `edge_type 按当前 add_edge 调用参数写入`

**示例**

- 当前实现的最小语义示例：ABox 边的关系类型；动态关系由 relation_type 参数写入。 输入=`{"source": "current code"}`；输出=`{"edge_type": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-relation-effectiveness"></a>
### `abox.relation.effectiveness` — 关系有效性

**一句大白话：** 从 TBox 克制关系复制到 ABox 静态边的有效性描述。

**正式定义：** 从 TBox 克制关系复制到 ABox 静态边的有效性描述。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`computed`
- 可信状态：`code_reality`
- 别名：`关系有效性`, `Relation Effectiveness`, `effectiveness`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.edges[*].effectiveness`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._replicate_static_relations / add_dynamic_relation（记录行 343–343；行号可能漂移）`

代码摘记：

- `effectiveness=relation["effectiveness"]`

公式或转换：

- `effectiveness 按当前 add_edge 调用参数写入`

**示例**

- 当前实现的最小语义示例：从 TBox 克制关系复制到 ABox 静态边的有效性描述。 输入=`{"source": "current code"}`；输出=`{"effectiveness": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.relation.edge`](#var-tbox-relation-edge)
- 下游：未记录正式变量下游。

**限制与已知问题**

- NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-relation-reason"></a>
### `abox.relation.reason` — 关系原因

**一句大白话：** 从 TBox 克制关系复制到 ABox 静态边的原因说明。

**正式定义：** 从 TBox 克制关系复制到 ABox 静态边的原因说明。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`computed`
- 可信状态：`code_reality`
- 别名：`关系原因`, `Relation Reason`, `reason`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.edges[*].reason`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._replicate_static_relations / add_dynamic_relation（记录行 342–342；行号可能漂移）`

代码摘记：

- `reason=relation["reason"]`

公式或转换：

- `reason 按当前 add_edge 调用参数写入`

**示例**

- 当前实现的最小语义示例：从 TBox 克制关系复制到 ABox 静态边的原因说明。 输入=`{"source": "current code"}`；输出=`{"reason": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.relation.edge`](#var-tbox-relation-edge)
- 下游：未记录正式变量下游。

**限制与已知问题**

- NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-relation-source-node"></a>
### `abox.relation.source_node` — 关系源节点

**一句大白话：** ABox 有向关系边的起点实例节点 ID。

**正式定义：** ABox 有向关系边的起点实例节点 ID。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`关系源节点`, `Relation Source Node`, `source_node`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.edges[*].source_node`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._replicate_static_relations / add_dynamic_relation（记录行 337–337；行号可能漂移）`

代码摘记：

- `self.abox.add_edge(`

公式或转换：

- `source_node 按当前 add_edge 调用参数写入`

**示例**

- 当前实现的最小语义示例：ABox 有向关系边的起点实例节点 ID。 输入=`{"source": "current code"}`；输出=`{"source_node": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-relation-target-node"></a>
### `abox.relation.target_node` — 关系目标节点

**一句大白话：** ABox 有向关系边的终点实例节点 ID。

**正式定义：** ABox 有向关系边的终点实例节点 ID。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`关系目标节点`, `Relation Target Node`, `target_node`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.edges[*].target_node`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._replicate_static_relations / add_dynamic_relation（记录行 337–337；行号可能漂移）`

代码摘记：

- `self.abox.add_edge(`

公式或转换：

- `target_node 按当前 add_edge 调用参数写入`

**示例**

- 当前实现的最小语义示例：ABox 有向关系边的终点实例节点 ID。 输入=`{"source": "current code"}`；输出=`{"target_node": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-relation-timestamp"></a>
### `abox.relation.timestamp` — 动态关系时间戳

**一句大白话：** 动态 ABox 关系创建时记录的 BattlefieldGraph.step_count。

**正式定义：** 动态 ABox 关系创建时记录的 BattlefieldGraph.step_count。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`computed`
- 可信状态：`code_reality`
- 别名：`动态关系时间戳`, `Dynamic Relation Timestamp`, `timestamp`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：`ABox update step`（`known`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.edges[*].timestamp`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._replicate_static_relations / add_dynamic_relation（记录行 418–418；行号可能漂移）`

代码摘记：

- `timestamp=self.step_count`

公式或转换：

- `timestamp 按当前 add_edge 调用参数写入`

**示例**

- 当前实现的最小语义示例：动态 ABox 关系创建时记录的 BattlefieldGraph.step_count。 输入=`{"source": "current code"}`；输出=`{"timestamp": "按公式得到"}`

**上下游关系**

- 上游：[`abox.graph.step_count`](#var-abox-graph-step-count)
- 下游：未记录正式变量下游。

**限制与已知问题**

- NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-alliance"></a>
### `abox.unit.alliance` — 阵营编码

**一句大白话：** 创建 ABox 单位实例时写入的 alliance 属性。

**正式定义：** 创建 ABox 单位实例时写入的 alliance 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`阵营编码`, `Alliance Code`, `alliance`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].alliance`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 189–189；行号可能漂移）`

代码摘记：

- `"alliance": raw_unit["alliance"]`

公式或转换：

- `abox.alliance=raw_unit["alliance"]`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 alliance 属性。 输入=`{"source": "current code"}`；输出=`{"alliance": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.alliance`](#var-raw-unit-alliance)
- 下游：[`abox.graph.enemy_count`](#var-abox-graph-enemy-count)、[`derived.tactical.critical_units`](#var-derived-tactical-critical-units)、[`derived.tactical.enemy_avg_hp`](#var-derived-tactical-enemy-avg-hp)、[`derived.tactical.enemy_count`](#var-derived-tactical-enemy-count)、[`derived.tactical.friendly_avg_hp`](#var-derived-tactical-friendly-avg-hp)、[`derived.tactical.friendly_count`](#var-derived-tactical-friendly-count)、[`derived.tactical.ready_to_fire_count`](#var-derived-tactical-ready-to-fire-count)

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-armor"></a>
### `abox.unit.armor` — ABox armor 字段

**一句大白话：** 创建 ABox 单位实例时写入的 armor 属性。

**正式定义：** 创建 ABox 单位实例时写入的 armor 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`ABox armor 字段`, `ABox Armor Field`, `armor`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].armor`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 201–201；行号可能漂移）`

代码摘记：

- `"armor": raw_unit.get("shield", 0)`

公式或转换：

- `abox.armor=raw_unit.get("shield", 0)`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 armor 属性。 输入=`{"source": "current code"}`；输出=`{"armor": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.shield`](#var-raw-unit-shield)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 该字段实际承载护盾值或护盾比例，不能按静态护甲解释。
- **`issue.abox_armor_stores_shield` / high：** 字段名称表达护甲，但当前数值语义是护盾。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-armor-ratio"></a>
### `abox.unit.armor_ratio` — ABox armor_ratio 字段

**一句大白话：** 创建 ABox 单位实例时写入的 armor_ratio 属性。

**正式定义：** 创建 ABox 单位实例时写入的 armor_ratio 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`ABox armor_ratio 字段`, `ABox Armor Ratio Field`, `armor_ratio`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ 1（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].armor_ratio`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 202–202；行号可能漂移）`

代码摘记：

- `"armor_ratio": raw_unit.get("shield_ratio", 0)`

公式或转换：

- `abox.armor_ratio=raw_unit.get("shield_ratio", 0)`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 armor_ratio 属性。 输入=`{"source": "current code"}`；输出=`{"armor_ratio": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.shield_ratio`](#var-raw-unit-shield-ratio)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 该字段实际承载护盾值或护盾比例，不能按静态护甲解释。
- **`issue.abox_armor_stores_shield` / high：** 字段名称表达护甲，但当前数值语义是护盾。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-attack-damage"></a>
### `abox.unit.attack_damage` — 攻击伤害

**一句大白话：** 创建 ABox 单位实例时写入的 attack_damage 属性。

**正式定义：** 创建 ABox 单位实例时写入的 attack_damage 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`攻击伤害`, `Attack Damage`, `attack_damage`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].attack_damage`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 194–194；行号可能漂移）`

代码摘记：

- `"attack_damage": static_info.get("attack_damage")`

公式或转换：

- `abox.attack_damage=static_info.get("attack_damage")`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 attack_damage 属性。 输入=`{"source": "current code"}`；输出=`{"attack_damage": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.attack_damage`](#var-tbox-entity-attack-damage)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-attack-range"></a>
### `abox.unit.attack_range` — 攻击射程

**一句大白话：** 创建 ABox 单位实例时写入的 attack_range 属性。

**正式定义：** 创建 ABox 单位实例时写入的 attack_range 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`攻击射程`, `Attack Range`, `attack_range`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].attack_range`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 195–195；行号可能漂移）`

代码摘记：

- `"attack_range": static_info.get("attack_range")`

公式或转换：

- `abox.attack_range=static_info.get("attack_range")`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 attack_range 属性。 输入=`{"source": "current code"}`；输出=`{"attack_range": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.attack_range`](#var-tbox-entity-attack-range)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-attack-speed"></a>
### `abox.unit.attack_speed` — 攻击速度字段

**一句大白话：** 创建 ABox 单位实例时写入的 attack_speed 属性。

**正式定义：** 创建 ABox 单位实例时写入的 attack_speed 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`攻击速度字段`, `Attack Speed`, `attack_speed`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].attack_speed`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 196–196；行号可能漂移）`

代码摘记：

- `"attack_speed": static_info.get("attack_speed")`

公式或转换：

- `abox.attack_speed=static_info.get("attack_speed")`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 attack_speed 属性。 输入=`{"source": "current code"}`；输出=`{"attack_speed": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.attack_speed`](#var-tbox-entity-attack-speed)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-category"></a>
### `abox.unit.category` — 实体类别

**一句大白话：** 创建 ABox 单位实例时写入的 category 属性。

**正式定义：** 创建 ABox 单位实例时写入的 category 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`实体类别`, `Entity Category`, `category`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].category`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 193–193；行号可能漂移）`

代码摘记：

- `"category": static_info.get("category")`

公式或转换：

- `abox.category=static_info.get("category")`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 category 属性。 输入=`{"source": "current code"}`；输出=`{"category": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.category`](#var-tbox-entity-category)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-description"></a>
### `abox.unit.description` — 实体说明

**一句大白话：** 创建 ABox 单位实例时写入的 description 属性。

**正式定义：** 创建 ABox 单位实例时写入的 description 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`实体说明`, `Description`, `description`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].description`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 206–206；行号可能漂移）`

代码摘记：

- `"description": static_info.get("description")`

公式或转换：

- `abox.description=static_info.get("description")`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 description 属性。 输入=`{"source": "current code"}`；输出=`{"description": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.description`](#var-tbox-entity-description)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-hp"></a>
### `abox.unit.hp` — 实例生命值

**一句大白话：** 创建 ABox 单位实例时写入的 hp 属性。

**正式定义：** 创建 ABox 单位实例时写入的 hp 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`实例生命值`, `Instance HP`, `hp`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].hp`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 199–199；行号可能漂移）`

代码摘记：

- `"hp": raw_unit["health"]`

公式或转换：

- `abox.hp=raw_unit["health"]`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 hp 属性。 输入=`{"source": "current code"}`；输出=`{"hp": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.health`](#var-raw-unit-health)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- **`issue.unknown_unit_hp_default_is_static_only` / low：** 100 是未知类型静态占位，不是动态生命值覆盖。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-hp-ratio"></a>
### `abox.unit.hp_ratio` — 实例生命比例

**一句大白话：** 创建 ABox 单位实例时写入的 hp_ratio 属性。

**正式定义：** 创建 ABox 单位实例时写入的 hp_ratio 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`实例生命比例`, `Instance HP Ratio`, `hp_ratio`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ 1（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].hp_ratio`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 200–200；行号可能漂移）`

代码摘记：

- `"hp_ratio": raw_unit["health_ratio"]`

公式或转换：

- `abox.hp_ratio=raw_unit["health_ratio"]`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 hp_ratio 属性。 输入=`{"source": "current code"}`；输出=`{"hp_ratio": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.health_ratio`](#var-raw-unit-health-ratio)
- 下游：[`derived.tactical.critical_units`](#var-derived-tactical-critical-units)、[`derived.tactical.enemy_avg_hp`](#var-derived-tactical-enemy-avg-hp)、[`derived.tactical.friendly_avg_hp`](#var-derived-tactical-friendly-avg-hp)

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-is-unknown"></a>
### `abox.unit.is_unknown` — 未知实体标志

**一句大白话：** 创建 ABox 单位实例时写入的 is_unknown 属性。

**正式定义：** 创建 ABox 单位实例时写入的 is_unknown 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`未知实体标志`, `Unknown Entity Flag`, `is_unknown`

**接口形式**

- 数据类型：`boolean`；Python 类型：`bool`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].is_unknown`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 190–190；行号可能漂移）`

代码摘记：

- `"is_unknown": is_unknown`

公式或转换：

- `abox.is_unknown=is_unknown`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 is_unknown 属性。 输入=`{"source": "current code"}`；输出=`{"is_unknown": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.unit_type`](#var-raw-unit-unit-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-movement-speed"></a>
### `abox.unit.movement_speed` — 移动速度

**一句大白话：** 创建 ABox 单位实例时写入的 movement_speed 属性。

**正式定义：** 创建 ABox 单位实例时写入的 movement_speed 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`移动速度`, `Movement Speed`, `movement_speed`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].movement_speed`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 197–197；行号可能漂移）`

代码摘记：

- `"movement_speed": static_info.get("movement_speed")`

公式或转换：

- `abox.movement_speed=static_info.get("movement_speed")`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 movement_speed 属性。 输入=`{"source": "current code"}`；输出=`{"movement_speed": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.movement_speed`](#var-tbox-entity-movement-speed)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-node-type"></a>
### `abox.unit.node_type` — 节点类型

**一句大白话：** 创建 ABox 单位实例时写入的 node_type 属性。

**正式定义：** 创建 ABox 单位实例时写入的 node_type 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`节点类型`, `Node Type`, `node_type`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].node_type`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 185–185；行号可能漂移）`

代码摘记：

- `"node_type": static_info["node_type"]`

公式或转换：

- `abox.node_type=static_info["node_type"]`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 node_type 属性。 输入=`{"source": "current code"}`；输出=`{"node_type": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.node_type`](#var-tbox-entity-node-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-position"></a>
### `abox.unit.position` — 二维位置对象

**一句大白话：** 创建 ABox 单位实例时写入的 position 属性。

**正式定义：** 创建 ABox 单位实例时写入的 position 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`二维位置对象`, `2D Position`, `position`

**接口形式**

- 数据类型：`object`；Python 类型：`dict`
- 形状：`object`；键值对象。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].position`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 203–203；行号可能漂移）`

代码摘记：

- `"position": {"x": raw_unit["x"], "y": raw_unit["y"]}`

公式或转换：

- `abox.position={"x": raw_unit["x"], "y": raw_unit["y"]}`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 position 属性。 输入=`{"source": "current code"}`；输出=`{"position": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.x`](#var-raw-unit-x)、[`raw_unit.y`](#var-raw-unit-y)
- 下游：[`derived.tactical.enemy_centroid`](#var-derived-tactical-enemy-centroid)、[`derived.tactical.friendly_centroid`](#var-derived-tactical-friendly-centroid)

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-race"></a>
### `abox.unit.race` — 种族

**一句大白话：** 创建 ABox 单位实例时写入的 race 属性。

**正式定义：** 创建 ABox 单位实例时写入的 race 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`种族`, `Race`, `race`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].race`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 192–192；行号可能漂移）`

代码摘记：

- `"race": static_info.get("race")`

公式或转换：

- `abox.race=static_info.get("race")`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 race 属性。 输入=`{"source": "current code"}`；输出=`{"race": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.race`](#var-tbox-entity-race)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-tag"></a>
### `abox.unit.tag` — 实例标签

**一句大白话：** 创建 ABox 单位实例时写入的 tag 属性。

**正式定义：** 创建 ABox 单位实例时写入的 tag 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`实例标签`, `Instance Tag`, `tag`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].tag`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 186–186；行号可能漂移）`

代码摘记：

- `"tag": tag`

公式或转换：

- `abox.tag=tag`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 tag 属性。 输入=`{"source": "current code"}`；输出=`{"tag": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.tag`](#var-raw-unit-tag)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-unit-class"></a>
### `abox.unit.unit_class` — 单位类别名

**一句大白话：** 创建 ABox 单位实例时写入的 unit_class 属性。

**正式定义：** 创建 ABox 单位实例时写入的 unit_class 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`单位类别名`, `Unit Class`, `unit_class`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].unit_class`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 188–188；行号可能漂移）`

代码摘记：

- `"unit_class": unit_name`

公式或转换：

- `abox.unit_class=unit_name`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 unit_class 属性。 输入=`{"source": "current code"}`；输出=`{"unit_class": "按公式得到"}`

**上下游关系**

- 上游：[`tbox.entity.unit_type_id`](#var-tbox-entity-unit-type-id)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-unit-type-id"></a>
### `abox.unit.unit_type_id` — 单位类型编号

**一句大白话：** 创建 ABox 单位实例时写入的 unit_type_id 属性。

**正式定义：** 创建 ABox 单位实例时写入的 unit_type_id 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`单位类型编号`, `Unit Type ID`, `unit_type_id`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].unit_type_id`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 187–187；行号可能漂移）`

代码摘记：

- `"unit_type_id": unit_type_id`

公式或转换：

- `abox.unit_type_id=unit_type_id`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 unit_type_id 属性。 输入=`{"source": "current code"}`；输出=`{"unit_type_id": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.unit_type`](#var-raw-unit-unit-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-abox-unit-weapon-cooldown"></a>
### `abox.unit.weapon_cooldown` — 武器冷却

**一句大白话：** 创建 ABox 单位实例时写入的 weapon_cooldown 属性。

**正式定义：** 创建 ABox 单位实例时写入的 weapon_cooldown 属性。

**身份与来源**

- 分类：`abox_dynamic`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`renamed`
- 可信状态：`code_reality`
- 别名：`武器冷却`, `Weapon Cooldown`, `weapon_cooldown`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`BattlefieldGraph.abox.nodes[*].weapon_cooldown`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph._create_instance（记录行 204–204；行号可能漂移）`

代码摘记：

- `"weapon_cooldown": raw_unit.get("weapon_cooldown", 0)`

公式或转换：

- `abox.weapon_cooldown=raw_unit.get("weapon_cooldown", 0)`

**示例**

- 当前实现的最小语义示例：创建 ABox 单位实例时写入的 weapon_cooldown 属性。 输入=`{"source": "current code"}`；输出=`{"weapon_cooldown": "按公式得到"}`

**上下游关系**

- 上游：[`raw_unit.weapon_cooldown`](#var-raw-unit-weapon-cooldown)
- 下游：[`derived.tactical.ready_to_fire_count`](#var-derived-tactical-ready-to-fire-count)

**限制与已知问题**

- ABox 实例字段不能与同名 TBox 静态属性合并。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-derived-tactical-state"></a>
## 派生战术状态

由观测或 ABox 按公式、聚合或阈值计算的战术量。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`derived.tactical.critical_units`](#var-derived-tactical-critical-units) | 危急单位列表 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.enemy_avg_hp`](#var-derived-tactical-enemy-avg-hp) | 敌军平均生命比例 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.enemy_centroid`](#var-derived-tactical-enemy-centroid) | 敌军质心 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.enemy_count`](#var-derived-tactical-enemy-count) | 敌军单位数 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.engagement_type`](#var-derived-tactical-engagement-type) | 接战距离类型 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.fire_readiness`](#var-derived-tactical-fire-readiness) | 火力就绪比例 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.force_ratio`](#var-derived-tactical-force-ratio) | 兵力对比 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.formation_distance`](#var-derived-tactical-formation-distance) | 阵型中心距离 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.friendly_avg_hp`](#var-derived-tactical-friendly-avg-hp) | 友军平均生命比例 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.friendly_centroid`](#var-derived-tactical-friendly-centroid) | 友军质心 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.friendly_count`](#var-derived-tactical-friendly-count) | 友军单位数 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.health_status`](#var-derived-tactical-health-status) | 血量态势 | `derived_runtime` | `derived_runtime` |
| [`derived.tactical.ready_to_fire_count`](#var-derived-tactical-ready-to-fire-count) | 可开火友军数 | `derived_runtime` | `derived_runtime` |

<a id="var-derived-tactical-critical-units"></a>
### `derived.tactical.critical_units` — 危急单位列表

**一句大白话：** hp_ratio 小于 0.3 的友军，输出最多三个实例名。

**正式定义：** hp_ratio 小于 0.3 的友军，输出最多三个实例名。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`危急单位列表`, `Critical Units`, `critical_units`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.Critical_Units`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 952–952；行号可能漂移）`

代码摘记：

- `d.get("hp_ratio", 1.0) < 0.3`

公式或转换：

- `d.get("hp_ratio", 1.0) < 0.3`

**示例**

- 当前实现的最小语义示例：hp_ratio 小于 0.3 的友军，输出最多三个实例名。 输入=`{"source": "current code"}`；输出=`{"critical_units": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.alliance`](#var-abox-unit-alliance)、[`abox.unit.hp_ratio`](#var-abox-unit-hp-ratio)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-enemy-avg-hp"></a>
### `derived.tactical.enemy_avg_hp` — 敌军平均生命比例

**一句大白话：** 敌军 hp_ratio 算术平均。

**正式定义：** 敌军 hp_ratio 算术平均。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`敌军平均生命比例`, `Enemy Average HP Ratio`, `enemy_avg_hp`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.enemy_avg_hp`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 945–945；行号可能漂移）`

代码摘记：

- `enemy_avg_hp = sum`

公式或转换：

- `enemy_avg_hp = sum`

**示例**

- 当前实现的最小语义示例：敌军 hp_ratio 算术平均。 输入=`{"source": "current code"}`；输出=`{"enemy_avg_hp": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.alliance`](#var-abox-unit-alliance)、[`abox.unit.hp_ratio`](#var-abox-unit-hp-ratio)
- 下游：[`derived.tactical.health_status`](#var-derived-tactical-health-status)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-enemy-centroid"></a>
### `derived.tactical.enemy_centroid` — 敌军质心

**一句大白话：** 敌军二维位置的算术平均点。

**正式定义：** 敌军二维位置的算术平均点。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`敌军质心`, `Enemy Centroid`, `enemy_centroid`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`vector`；二维 [x, y] 向量。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`derived.enemy_centroid`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 965–965；行号可能漂移）`

代码摘记：

- `enemy_center_x =`

公式或转换：

- `enemy_center_x =`

**示例**

- 当前实现的最小语义示例：敌军二维位置的算术平均点。 输入=`{"source": "current code"}`；输出=`{"enemy_centroid": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.position`](#var-abox-unit-position)
- 下游：[`derived.tactical.formation_distance`](#var-derived-tactical-formation-distance)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-enemy-count"></a>
### `derived.tactical.enemy_count` — 敌军单位数

**一句大白话：** 敌军 ABox 节点数量。

**正式定义：** 敌军 ABox 节点数量。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`敌军单位数`, `Enemy Unit Count`, `enemy_count`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.enemy_count`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 940–940；行号可能漂移）`

代码摘记：

- `enemy_count = len(enemy_units)`

公式或转换：

- `enemy_count = len(enemy_units)`

**示例**

- 当前实现的最小语义示例：敌军 ABox 节点数量。 输入=`{"source": "current code"}`；输出=`{"enemy_count": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.alliance`](#var-abox-unit-alliance)
- 下游：[`derived.tactical.force_ratio`](#var-derived-tactical-force-ratio)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-engagement-type"></a>
### `derived.tactical.engagement_type` — 接战距离类型

**一句大白话：** 质心距离小于 10 为 Close-Combat，小于 20 为 Medium-Range，否则 Long-Range。

**正式定义：** 质心距离小于 10 为 Close-Combat，小于 20 为 Medium-Range，否则 Long-Range。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`接战距离类型`, `Engagement Type`, `engagement_type`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：`Close-Combat`, `Medium-Range`, `Long-Range`
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.Engagement_Type`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 976–976；行号可能漂移）`

代码摘记：

- `situation = "Close-Combat"`

公式或转换：

- `d<10: Close-Combat; 10<=d<20: Medium-Range; d>=20: Long-Range`

**示例**

- 当前实现的最小语义示例：质心距离小于 10 为 Close-Combat，小于 20 为 Medium-Range，否则 Long-Range。 输入=`{"source": "current code"}`；输出=`{"engagement_type": "按公式得到"}`

**上下游关系**

- 上游：[`derived.tactical.formation_distance`](#var-derived-tactical-formation-distance)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-fire-readiness"></a>
### `derived.tactical.fire_readiness` — 火力就绪比例

**一句大白话：** 可开火友军数除以友军总数。

**正式定义：** 可开火友军数除以友军总数。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`火力就绪比例`, `Fire Readiness`, `fire_readiness`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.fire_readiness`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 987–987；行号可能漂移）`

代码摘记：

- `ready_ratio = ready_to_fire / friendly_count`

公式或转换：

- `ready_ratio = ready_to_fire / friendly_count`

**示例**

- 当前实现的最小语义示例：可开火友军数除以友军总数。 输入=`{"source": "current code"}`；输出=`{"fire_readiness": "按公式得到"}`

**上下游关系**

- 上游：[`derived.tactical.friendly_count`](#var-derived-tactical-friendly-count)、[`derived.tactical.ready_to_fire_count`](#var-derived-tactical-ready-to-fire-count)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-force-ratio"></a>
### `derived.tactical.force_ratio` — 兵力对比

**一句大白话：** “友军数 vs 敌军数”的摘要文本。

**正式定义：** “友军数 vs 敌军数”的摘要文本。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`兵力对比`, `Force Ratio`, `force_ratio`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.force_ratio`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 948–948；行号可能漂移）`

代码摘记：

- `Force_Ratio: {friendly_count} vs {enemy_count}`

公式或转换：

- `Force_Ratio: {friendly_count} vs {enemy_count}`

**示例**

- 当前实现的最小语义示例：“友军数 vs 敌军数”的摘要文本。 输入=`{"source": "current code"}`；输出=`{"force_ratio": "按公式得到"}`

**上下游关系**

- 上游：[`derived.tactical.enemy_count`](#var-derived-tactical-enemy-count)、[`derived.tactical.friendly_count`](#var-derived-tactical-friendly-count)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-formation-distance"></a>
### `derived.tactical.formation_distance` — 阵型中心距离

**一句大白话：** 敌我质心之间的欧氏距离。

**正式定义：** 敌我质心之间的欧氏距离。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`阵型中心距离`, `Formation Distance`, `formation_distance`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.formation_distance`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 969–969；行号可能漂移）`

代码摘记：

- `center_distance = math.dist`

公式或转换：

- `center_distance = math.dist`

**示例**

- 当前实现的最小语义示例：敌我质心之间的欧氏距离。 输入=`{"source": "current code"}`；输出=`{"formation_distance": "按公式得到"}`

**上下游关系**

- 上游：[`derived.tactical.enemy_centroid`](#var-derived-tactical-enemy-centroid)、[`derived.tactical.friendly_centroid`](#var-derived-tactical-friendly-centroid)
- 下游：[`derived.tactical.engagement_type`](#var-derived-tactical-engagement-type)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-friendly-avg-hp"></a>
### `derived.tactical.friendly_avg_hp` — 友军平均生命比例

**一句大白话：** 友军 hp_ratio 算术平均。

**正式定义：** 友军 hp_ratio 算术平均。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`友军平均生命比例`, `Friendly Average HP Ratio`, `friendly_avg_hp`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.friendly_avg_hp`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 944–944；行号可能漂移）`

代码摘记：

- `friendly_avg_hp = sum`

公式或转换：

- `friendly_avg_hp = sum`

**示例**

- 当前实现的最小语义示例：友军 hp_ratio 算术平均。 输入=`{"source": "current code"}`；输出=`{"friendly_avg_hp": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.alliance`](#var-abox-unit-alliance)、[`abox.unit.hp_ratio`](#var-abox-unit-hp-ratio)
- 下游：[`derived.tactical.health_status`](#var-derived-tactical-health-status)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-friendly-centroid"></a>
### `derived.tactical.friendly_centroid` — 友军质心

**一句大白话：** 友军二维位置的算术平均点。

**正式定义：** 友军二维位置的算术平均点。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`友军质心`, `Friendly Centroid`, `friendly_centroid`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`vector`；二维 [x, y] 向量。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`derived.friendly_centroid`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 960–960；行号可能漂移）`

代码摘记：

- `friendly_center_x =`

公式或转换：

- `friendly_center_x =`

**示例**

- 当前实现的最小语义示例：友军二维位置的算术平均点。 输入=`{"source": "current code"}`；输出=`{"friendly_centroid": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.position`](#var-abox-unit-position)
- 下游：[`derived.tactical.formation_distance`](#var-derived-tactical-formation-distance)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-friendly-count"></a>
### `derived.tactical.friendly_count` — 友军单位数

**一句大白话：** 友军 ABox 节点数量。

**正式定义：** 友军 ABox 节点数量。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`友军单位数`, `Friendly Unit Count`, `friendly_count`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.friendly_count`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 939–939；行号可能漂移）`

代码摘记：

- `friendly_count = len(friendly_units)`

公式或转换：

- `friendly_count = len(friendly_units)`

**示例**

- 当前实现的最小语义示例：友军 ABox 节点数量。 输入=`{"source": "current code"}`；输出=`{"friendly_count": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.alliance`](#var-abox-unit-alliance)
- 下游：[`derived.tactical.fire_readiness`](#var-derived-tactical-fire-readiness)、[`derived.tactical.force_ratio`](#var-derived-tactical-force-ratio)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-health-status"></a>
### `derived.tactical.health_status` — 血量态势

**一句大白话：** 敌我平均生命比例的百分比摘要。

**正式定义：** 敌我平均生命比例的百分比摘要。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`血量态势`, `Health Status`, `health_status`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.health_status`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 949–949；行号可能漂移）`

代码摘记：

- `Health_Status: Friendly`

公式或转换：

- `Health_Status: Friendly`

**示例**

- 当前实现的最小语义示例：敌我平均生命比例的百分比摘要。 输入=`{"source": "current code"}`；输出=`{"health_status": "按公式得到"}`

**上下游关系**

- 上游：[`derived.tactical.enemy_avg_hp`](#var-derived-tactical-enemy-avg-hp)、[`derived.tactical.friendly_avg_hp`](#var-derived-tactical-friendly-avg-hp)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-derived-tactical-ready-to-fire-count"></a>
### `derived.tactical.ready_to_fire_count` — 可开火友军数

**一句大白话：** weapon_cooldown 等于 0 的友军数量。

**正式定义：** weapon_cooldown 等于 0 的友军数量。

**身份与来源**

- 分类：`derived_tactical_state`
- 来源层：`derived_runtime`（运行时公式、聚合或阈值派生）
- 派生方式：`computed`
- 可信状态：`derived_runtime`
- 别名：`可开火友军数`, `Ready-to-fire Unit Count`, `ready_to_fire_count`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`tactical_summary.ready_to_fire_count`

**STORM 实现与依据**

- `ontology/bridge.py::BattlefieldGraph.generate_tactical_summary（记录行 985–985；行号可能漂移）`

代码摘记：

- `ready_to_fire = sum`

公式或转换：

- `ready_to_fire = sum`

**示例**

- 当前实现的最小语义示例：weapon_cooldown 等于 0 的友军数量。 输入=`{"source": "current code"}`；输出=`{"ready_to_fire_count": "按公式得到"}`

**上下游关系**

- 上游：[`abox.unit.alliance`](#var-abox-unit-alliance)、[`abox.unit.weapon_cooldown`](#var-abox-unit-weapon-cooldown)
- 下游：[`derived.tactical.fire_readiness`](#var-derived-tactical-fire-readiness)

**限制与已知问题**

- 只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-action-schema-and-scheduling"></a>
## 动作 Schema 与调度

LLM 动作输出、解析、校验和延迟执行字段。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`action.delay_steps`](#var-action-delay-steps) | 延迟步数 | `validated_action` | `code_reality` |
| [`action.invalid_actions`](#var-action-invalid-actions) | 无效动作数 | `validated_action` | `code_reality` |
| [`action.invalid_reason_counts`](#var-action-invalid-reason-counts) | 无效原因计数 | `validated_action` | `code_reality` |
| [`action.plan`](#var-action-plan) | 计划文本 | `llm_output` | `code_reality` |
| [`action.planned_actions`](#var-action-planned-actions) | 计划动作数 | `validated_action` | `code_reality` |
| [`action.priority`](#var-action-priority) | 优先级 | `validated_action` | `code_reality` |
| [`action.reasoning`](#var-action-reasoning) | 战术推理文本 | `llm_output` | `code_reality` |
| [`action.subtype`](#var-action-subtype) | 动作子类型 | `validated_action` | `code_reality` |
| [`action.target`](#var-action-target) | 动作目标 | `validated_action` | `code_reality` |
| [`action.target_type`](#var-action-target-type) | 目标类型 | `validated_action` | `code_reality` |
| [`action.type`](#var-action-type) | 动作类型 | `validated_action` | `code_reality` |
| [`action.units`](#var-action-units) | 执行单位列表 | `validated_action` | `code_reality` |

<a id="var-action-delay-steps"></a>
### `action.delay_steps` — 延迟步数

**一句大白话：** 延迟的 STORM environment step 数；缺失为 0，并限制到 0..9。

**正式定义：** 延迟的 STORM environment step 数；缺失为 0，并限制到 0..9。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`延迟步数`, `Delay Steps`, `delay_steps`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：`environment step`（`known`）
- 范围：0 ～ 9（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.delay_steps`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 246–246；行号可能漂移）`

代码摘记：

- `if "delay_steps" not in action`

公式或转换：

- `delay_steps=min(9,max(0,int(value or 0)))`

**示例**

- 当前实现的最小语义示例：延迟的 STORM environment step 数；缺失为 0，并限制到 0..9。 输入=`{"source": "current code"}`；输出=`{"delay_steps": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 单位是 environment step，不是秒或 SC2 game loop。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-invalid-actions"></a>
### `action.invalid_actions` — 无效动作数

**一句大白话：** 语义校验判为无效的动作数。

**正式定义：** 语义校验判为无效的动作数。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`无效动作数`, `Invalid Action Count`, `invalid_actions`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`not_applicable`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.invalid_actions`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 113–113；行号可能漂移）`

代码摘记：

- `invalid_actions = 0`

公式或转换：

- `invalid_actions=parser output/validation result`

**示例**

- 当前实现的最小语义示例：语义校验判为无效的动作数。 输入=`{"source": "current code"}`；输出=`{"invalid_actions": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-invalid-reason-counts"></a>
### `action.invalid_reason_counts` — 无效原因计数

**一句大白话：** 按原因代码聚合的无效动作数。

**正式定义：** 按原因代码聚合的无效动作数。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`无效原因计数`, `Invalid Reason Counts`, `invalid_reason_counts`

**接口形式**

- 数据类型：`object`；Python 类型：`dict`
- 形状：`object`；键值对象。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.invalid_reason_counts`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 114–114；行号可能漂移）`

代码摘记：

- `invalid_reason_counts = {}`

公式或转换：

- `invalid_reason_counts=parser output/validation result`

**示例**

- 当前实现的最小语义示例：按原因代码聚合的无效动作数。 输入=`{"source": "current code"}`；输出=`{"invalid_reason_counts": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-plan"></a>
### `action.plan` — 计划文本

**一句大白话：** LLM 返回并由解析器透传的计划文本。

**正式定义：** LLM 返回并由解析器透传的计划文本。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`llm_output`（LLM 原始动作输出）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`计划文本`, `Plan Text`, `plan`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.plan`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 120–120；行号可能漂移）`

代码摘记：

- `json_data.get("plan", "")`

公式或转换：

- `plan=parser output/validation result`

**示例**

- 当前实现的最小语义示例：LLM 返回并由解析器透传的计划文本。 输入=`{"source": "current code"}`；输出=`{"plan": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-planned-actions"></a>
### `action.planned_actions` — 计划动作数

**一句大白话：** 语义过滤前的动作数量。

**正式定义：** 语义过滤前的动作数量。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`计划动作数`, `Planned Action Count`, `planned_actions`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`not_applicable`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.planned_actions`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 103–103；行号可能漂移）`

代码摘记：

- `planned_actions = len`

公式或转换：

- `planned_actions=parser output/validation result`

**示例**

- 当前实现的最小语义示例：语义过滤前的动作数量。 输入=`{"source": "current code"}`；输出=`{"planned_actions": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-priority"></a>
### `action.priority` — 优先级

**一句大白话：** 只允许 high、medium、low。

**正式定义：** 只允许 high、medium、low。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`优先级`, `Priority`, `priority`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：`high`, `medium`, `low`
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.priority`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 37–37；行号可能漂移）`

代码摘记：

- `VALID_PRIORITIES =`

公式或转换：

- `priority=parser output/validation result`

**示例**

- 当前实现的最小语义示例：只允许 high、medium、low。 输入=`{"source": "current code"}`；输出=`{"priority": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- **`issue.action_priority_not_validated_or_consumed` / medium：** priority 更接近设计字段，而不是已生效的调度量。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-reasoning"></a>
### `action.reasoning` — 战术推理文本

**一句大白话：** LLM 返回并由解析器透传的推理文本。

**正式定义：** LLM 返回并由解析器透传的推理文本。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`llm_output`（LLM 原始动作输出）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`战术推理文本`, `Tactical Reasoning`, `reasoning`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.reasoning`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 119–119；行号可能漂移）`

代码摘记：

- `json_data.get("reasoning", "")`

公式或转换：

- `reasoning=parser output/validation result`

**示例**

- 当前实现的最小语义示例：LLM 返回并由解析器透传的推理文本。 输入=`{"source": "current code"}`；输出=`{"reasoning": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-subtype"></a>
### `action.subtype` — 动作子类型

**一句大白话：** BUILD 的建筑类型或 TRAIN 的单位类型。

**正式定义：** BUILD 的建筑类型或 TRAIN 的单位类型。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`动作子类型`, `Action Subtype`, `subtype`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.subtype`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 545–545；行号可能漂移）`

代码摘记：

- `sub_type = action.get("subtype", "")`

公式或转换：

- `subtype=parser output/validation result`

**示例**

- 当前实现的最小语义示例：BUILD 的建筑类型或 TRAIN 的单位类型。 输入=`{"source": "current code"}`；输出=`{"subtype": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`pysc2.build.function_id`](#var-pysc2-build-function-id)、[`pysc2.train.function_id`](#var-pysc2-train-function-id)

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- **`issue.build_train_dual_representation` / high：** 纯 BUILD/TRAIN 若不另给 subtype，不能满足当前执行链。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-target"></a>
### `action.target` — 动作目标

**一句大白话：** 单位 ID、二维坐标或空目标，取决于 target_type。

**正式定义：** 单位 ID、二维坐标或空目标，取决于 target_type。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`动作目标`, `Action Target`, `target`

**接口形式**

- 数据类型：`object`；Python 类型：`dict`
- 形状：`object`；键值对象。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.target`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 298–298；行号可能漂移）`

代码摘记：

- `if "target" not in action`

公式或转换：

- `target=parser output/validation result`

**示例**

- 当前实现的最小语义示例：单位 ID、二维坐标或空目标，取决于 target_type。 输入=`{"source": "current code"}`；输出=`{"target": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`pysc2.function.target`](#var-pysc2-function-target)

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- **`issue.action_coordinate_clip_not_written_back` / high：** 越界坐标看似被裁剪，后续仍可能收到原始 target。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-target-type"></a>
### `action.target_type` — 目标类型

**一句大白话：** 只允许 unit、pos、none。

**正式定义：** 只允许 unit、pos、none。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`目标类型`, `Target Type`, `target_type`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：`unit`, `pos`, `none`
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.target_type`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 34–34；行号可能漂移）`

代码摘记：

- `VALID_TARGET_TYPES =`

公式或转换：

- `target_type=parser output/validation result`

**示例**

- 当前实现的最小语义示例：只允许 unit、pos、none。 输入=`{"source": "current code"}`；输出=`{"target_type": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`pysc2.function.target`](#var-pysc2-function-target)

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-type"></a>
### `action.type` — 动作类型

**一句大白话：** 只允许 MOVE、ATTACK、BUILD、TRAIN。

**正式定义：** 只允许 MOVE、ATTACK、BUILD、TRAIN。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`动作类型`, `Action Type`, `action`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：`MOVE`, `ATTACK`, `BUILD`, `TRAIN`
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.action`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 26–26；行号可能漂移）`

代码摘记：

- `VALID_ACTIONS = {`

公式或转换：

- `action=parser output/validation result`

**示例**

- 当前实现的最小语义示例：只允许 MOVE、ATTACK、BUILD、TRAIN。 输入=`{"source": "current code"}`；输出=`{"action": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`pysc2.attack.function_id`](#var-pysc2-attack-function-id)、[`pysc2.build.function_id`](#var-pysc2-build-function-id)、[`pysc2.move.function_id`](#var-pysc2-move-function-id)、[`pysc2.train.function_id`](#var-pysc2-train-function-id)

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- **`issue.build_train_dual_representation` / high：** 纯 BUILD/TRAIN 若不另给 subtype，不能满足当前执行链。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-action-units"></a>
### `action.units` — 执行单位列表

**一句大白话：** 动作涉及的 ABox 实例 ID 列表。

**正式定义：** 动作涉及的 ABox 实例 ID 列表。

**身份与来源**

- 分类：`action_schema_and_scheduling`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`执行单位列表`, `Acting Units`, `units`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`validated_action.units`

**STORM 实现与依据**

- `agents/response_parser.py::ResponseParser.parse / validation（记录行 227–227；行号可能漂移）`

代码摘记：

- `if "units" not in action`

公式或转换：

- `units=parser output/validation result`

**示例**

- 当前实现的最小语义示例：动作涉及的 ABox 实例 ID 列表。 输入=`{"source": "current code"}`；输出=`{"units": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`pysc2.function.unit_tags`](#var-pysc2-function-unit-tags)

**限制与已知问题**

- 这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-pysc2-function-call"></a>
## PySC2 FunctionCall

ActionExecutor 映射到 PySC2 Raw FunctionCall 的函数与参数。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`pysc2.attack.function_id`](#var-pysc2-attack-function-id) | ATTACK 函数编号 | `executor_mapping` | `code_reality` |
| [`pysc2.build.function_id`](#var-pysc2-build-function-id) | BUILD 函数编号 | `executor_mapping` | `code_reality` |
| [`pysc2.function.queued`](#var-pysc2-function-queued) | 排队标志 | `executor_mapping` | `code_reality` |
| [`pysc2.function.raw_flag`](#var-pysc2-function-raw-flag) | Raw FunctionCall 标志 | `executor_mapping` | `code_reality` |
| [`pysc2.function.target`](#var-pysc2-function-target) | 目标参数 | `executor_mapping` | `code_reality` |
| [`pysc2.function.unit_tags`](#var-pysc2-function-unit-tags) | 单位标签参数 | `executor_mapping` | `code_reality` |
| [`pysc2.move.function_id`](#var-pysc2-move-function-id) | MOVE 函数编号 | `executor_mapping` | `code_reality` |
| [`pysc2.no_op.function_id`](#var-pysc2-no-op-function-id) | No-op 函数编号 | `executor_mapping` | `code_reality` |
| [`pysc2.train.function_id`](#var-pysc2-train-function-id) | TRAIN 函数编号 | `executor_mapping` | `code_reality` |

<a id="var-pysc2-attack-function-id"></a>
### `pysc2.attack.function_id` — ATTACK 函数编号

**一句大白话：** ATTACK 使用编号 3。

**正式定义：** ATTACK 使用编号 3。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`ATTACK 函数编号`, `ATTACK Function ID`, `function_id`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.function`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 162–162；行号可能漂移）`

代码摘记：

- `3, arguments=args, raw=True`

公式或转换：

- `ATTACK 使用编号 3。`

**示例**

- 当前实现的最小语义示例：ATTACK 使用编号 3。 输入=`{"source": "current code"}`；输出=`{"function_id": "按公式得到"}`

**上下游关系**

- 上游：[`action.type`](#var-action-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- **`issue.function_ids_require_runtime_actionspec_check` / high：** 静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-build-function-id"></a>
### `pysc2.build.function_id` — BUILD 函数编号

**一句大白话：** BUILD 按 subtype 查询 BUILD_CALLS。

**正式定义：** BUILD 按 subtype 查询 BUILD_CALLS。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`BUILD 函数编号`, `BUILD Function ID`, `function_id`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.function`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 210–210；行号可能漂移）`

代码摘记：

- `BUILD_CALLS[subtype]`

公式或转换：

- `BUILD 按 subtype 查询 BUILD_CALLS。`

**示例**

- 当前实现的最小语义示例：BUILD 按 subtype 查询 BUILD_CALLS。 输入=`{"source": "current code"}`；输出=`{"function_id": "按公式得到"}`

**上下游关系**

- 上游：[`action.subtype`](#var-action-subtype)、[`action.type`](#var-action-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- **`issue.function_ids_require_runtime_actionspec_check` / high：** 静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-function-queued"></a>
### `pysc2.function.queued` — 排队标志

**一句大白话：** MOVE/ATTACK/BUILD 当前均传 [0]。

**正式定义：** MOVE/ATTACK/BUILD 当前均传 [0]。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`排队标志`, `Queued Flag`, `queued`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.function`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 160–160；行号可能漂移）`

代码摘记：

- `args = [[0], action["units"], action["target"]]`

公式或转换：

- `MOVE/ATTACK/BUILD 当前均传 [0]。`

**示例**

- 当前实现的最小语义示例：MOVE/ATTACK/BUILD 当前均传 [0]。 输入=`{"source": "current code"}`；输出=`{"queued": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-function-raw-flag"></a>
### `pysc2.function.raw_flag` — Raw FunctionCall 标志

**一句大白话：** FunctionCall 使用 Raw 参数。

**正式定义：** FunctionCall 使用 Raw 参数。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`Raw FunctionCall 标志`, `Raw FunctionCall Flag`, `raw`

**接口形式**

- 数据类型：`boolean`；Python 类型：`bool`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.raw`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 139–139；行号可能漂移）`

代码摘记：

- `raw=True`

公式或转换：

- `FunctionCall 使用 Raw 参数。`

**示例**

- 当前实现的最小语义示例：FunctionCall 使用 Raw 参数。 输入=`{"source": "current code"}`；输出=`{"raw": "按公式得到"}`

**上下游关系**

- 上游：[`environment.use_raw_actions`](#var-environment-use-raw-actions)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-function-target"></a>
### `pysc2.function.target` — 目标参数

**一句大白话：** MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。

**正式定义：** MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`目标参数`, `Target Argument`, `target`

**接口形式**

- 数据类型：`object`；Python 类型：`dict`
- 形状：`object`；键值对象。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.arguments.target`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 160–160；行号可能漂移）`

代码摘记：

- `action["target"]`

公式或转换：

- `MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。`

**示例**

- 当前实现的最小语义示例：MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。 输入=`{"source": "current code"}`；输出=`{"target": "按公式得到"}`

**上下游关系**

- 上游：[`action.target`](#var-action-target)、[`action.target_type`](#var-action-target-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- **`issue.action_coordinate_clip_not_written_back` / high：** 越界坐标看似被裁剪，后续仍可能收到原始 target。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-function-unit-tags"></a>
### `pysc2.function.unit_tags` — 单位标签参数

**一句大白话：** 经验证和映射的 tag 列表。

**正式定义：** 经验证和映射的 tag 列表。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`单位标签参数`, `Unit Tags Argument`, `unit_tags`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.arguments.unit_tags`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 160–160；行号可能漂移）`

代码摘记：

- `action["units"]`

公式或转换：

- `经验证和映射的 tag 列表。`

**示例**

- 当前实现的最小语义示例：经验证和映射的 tag 列表。 输入=`{"source": "current code"}`；输出=`{"unit_tags": "按公式得到"}`

**上下游关系**

- 上游：[`action.units`](#var-action-units)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-move-function-id"></a>
### `pysc2.move.function_id` — MOVE 函数编号

**一句大白话：** MOVE 使用编号 13。

**正式定义：** MOVE 使用编号 13。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`MOVE 函数编号`, `MOVE Function ID`, `function_id`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.function`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 162–162；行号可能漂移）`

代码摘记：

- `13, arguments=args, raw=True`

公式或转换：

- `MOVE 使用编号 13。`

**示例**

- 当前实现的最小语义示例：MOVE 使用编号 13。 输入=`{"source": "current code"}`；输出=`{"function_id": "按公式得到"}`

**上下游关系**

- 上游：[`action.type`](#var-action-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- **`issue.function_ids_require_runtime_actionspec_check` / high：** 静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-no-op-function-id"></a>
### `pysc2.no_op.function_id` — No-op 函数编号

**一句大白话：** 空动作返回编号 0。

**正式定义：** 空动作返回编号 0。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`No-op 函数编号`, `No-op Function ID`, `function_id`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.function`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 139–139；行号可能漂移）`

代码摘记：

- `init_with_validation(0, arguments=[], raw=True)`

公式或转换：

- `空动作返回编号 0。`

**示例**

- 当前实现的最小语义示例：空动作返回编号 0。 输入=`{"source": "current code"}`；输出=`{"function_id": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- **`issue.function_ids_require_runtime_actionspec_check` / high：** 静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-pysc2-train-function-id"></a>
### `pysc2.train.function_id` — TRAIN 函数编号

**一句大白话：** TRAIN 按 subtype 查询 TRAIN_CALLS。

**正式定义：** TRAIN 按 subtype 查询 TRAIN_CALLS。

**身份与来源**

- 分类：`pysc2_function_call`
- 来源层：`executor_mapping`（PySC2 FunctionCall 执行映射）
- 派生方式：`validated`
- 可信状态：`code_reality`
- 别名：`TRAIN 函数编号`, `TRAIN Function ID`, `function_id`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`FunctionCall.function`

**STORM 实现与依据**

- `agents/action_executor.py::ActionExecutor.execute（记录行 236–236；行号可能漂移）`

代码摘记：

- `TRAIN_CALLS[subtype]`

公式或转换：

- `TRAIN 按 subtype 查询 TRAIN_CALLS。`

**示例**

- 当前实现的最小语义示例：TRAIN 按 subtype 查询 TRAIN_CALLS。 输入=`{"source": "current code"}`；输出=`{"function_id": "按公式得到"}`

**上下游关系**

- 上游：[`action.subtype`](#var-action-subtype)、[`action.type`](#var-action-type)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。
- **`issue.function_ids_require_runtime_actionspec_check` / high：** 静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="category-swm"></a>
## SWM 变量

状态世界模型的输入、预测、候选和误差字段。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`swm.candidate_index`](#var-swm-candidate-index) | 候选动作编号 | `swm_prediction` | `needs_verification` |
| [`swm.confidence`](#var-swm-confidence) | 预测置信度 | `swm_prediction` | `needs_verification` |
| [`swm.input.abox_state`](#var-swm-input-abox-state) | ABox 状态文本 | `abox_runtime` | `code_reality` |
| [`swm.input.planned_actions`](#var-swm-input-planned-actions) | 候选动作 | `validated_action` | `code_reality` |
| [`swm.predicted_relations`](#var-swm-predicted-relations) | 预测关系 | `swm_prediction` | `needs_verification` |
| [`swm.predicted_unit_states`](#var-swm-predicted-unit-states) | 预测单位状态 | `swm_prediction` | `needs_verification` |
| [`swm.prediction.step`](#var-swm-prediction-step) | 预测相对步 | `swm_prediction` | `needs_verification` |
| [`swm.prediction_steps`](#var-swm-prediction-steps) | 预测步数 | `environment_config` | `code_reality` |
| [`swm.predictions`](#var-swm-predictions) | 逐步预测列表 | `swm_prediction` | `needs_verification` |
| [`swm.raw_response`](#var-swm-raw-response) | 预测原始响应 | `llm_output` | `needs_verification` |
| [`swm.token_usage`](#var-swm-token-usage) | 预测 Token 用量 | `swm_prediction` | `needs_verification` |
| [`swm.unit.health_delta`](#var-swm-unit-health-delta) | 预测生命变化 | `swm_prediction` | `needs_verification` |
| [`swm.unit.position_delta`](#var-swm-unit-position-delta) | 预测位置变化 | `swm_prediction` | `needs_verification` |

<a id="var-swm-candidate-index"></a>
### `swm.candidate_index` — 候选动作编号

**一句大白话：** 多候选预测的零基编号。

**正式定义：** 多候选预测的零基编号。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`候选动作编号`, `Candidate Index`, `candidate_index`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.candidate_index`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 189–189；行号可能漂移）`

代码摘记：

- `result["candidate_index"] = i`

公式或转换：

- `candidate_index=SWM input/output field`

**示例**

- 当前实现的最小语义示例：多候选预测的零基编号。 输入=`{"source": "current code"}`；输出=`{"candidate_index": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predictions`](#var-swm-predictions)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-confidence"></a>
### `swm.confidence` — 预测置信度

**一句大白话：** SWM 返回的置信度。

**正式定义：** SWM 返回的置信度。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测置信度`, `Prediction Confidence`, `confidence`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ 1（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.confidence`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 119–119；行号可能漂移）`

代码摘记：

- `"confidence": 0.75`

公式或转换：

- `confidence=SWM input/output field`

**示例**

- 当前实现的最小语义示例：SWM 返回的置信度。 输入=`{"source": "current code"}`；输出=`{"confidence": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- **`issue.swm_confidence_not_a_gate` / medium：** 该值当前是预测元数据，不是自动决定采用预测的开关。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-input-abox-state"></a>
### `swm.input.abox_state` — ABox 状态文本

**一句大白话：** 当前 ABox 序列化文本输入。

**正式定义：** 当前 ABox 序列化文本输入。

**身份与来源**

- 分类：`swm`
- 来源层：`abox_runtime`（运行时 ABox 实例）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`ABox 状态文本`, `ABox State Text`, `abox_state`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.input.abox_state`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 95–95；行号可能漂移）`

代码摘记：

- `abox_state: str`

公式或转换：

- `abox_state=SWM input/output field`

**示例**

- 当前实现的最小语义示例：当前 ABox 序列化文本输入。 输入=`{"source": "current code"}`；输出=`{"abox_state": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`swm.raw_response`](#var-swm-raw-response)

**限制与已知问题**

- 输入格式由当前 STORM 约定；来源层表示输入在进入 SWM 前的事实边界。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-swm-input-planned-actions"></a>
### `swm.input.planned_actions` — 候选动作

**一句大白话：** 待预测的候选动作列表。

**正式定义：** 待预测的候选动作列表。

**身份与来源**

- 分类：`swm`
- 来源层：`validated_action`（解析与校验后的动作）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`候选动作`, `Planned Actions`, `planned_actions`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.input.planned_actions`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 96–96；行号可能漂移）`

代码摘记：

- `planned_actions: List`

公式或转换：

- `planned_actions=SWM input/output field`

**示例**

- 当前实现的最小语义示例：待预测的候选动作列表。 输入=`{"source": "current code"}`；输出=`{"planned_actions": "按公式得到"}`

**上下游关系**

- 上游：[`action.planned_actions`](#var-action-planned-actions)
- 下游：[`swm.raw_response`](#var-swm-raw-response)

**限制与已知问题**

- 输入格式由当前 STORM 约定；来源层表示输入在进入 SWM 前的事实边界。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-swm-predicted-relations"></a>
### `swm.predicted_relations` — 预测关系

**一句大白话：** 预测步内的关系列表。

**正式定义：** 预测步内的关系列表。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测关系`, `Predicted Relations`, `predicted_relations`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.predicted_relations`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 116–116；行号可能漂移）`

代码摘记：

- `"predicted_relations":`

公式或转换：

- `predicted_relations=SWM input/output field`

**示例**

- 当前实现的最小语义示例：预测步内的关系列表。 输入=`{"source": "current code"}`；输出=`{"predicted_relations": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predictions`](#var-swm-predictions)
- 下游：[`metric.swm.relation_accuracy`](#var-metric-swm-relation-accuracy)

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-predicted-unit-states"></a>
### `swm.predicted_unit_states` — 预测单位状态

**一句大白话：** 预测步内的单位状态变化列表。

**正式定义：** 预测步内的单位状态变化列表。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测单位状态`, `Predicted Unit States`, `predicted_unit_states`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.predicted_unit_states`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 115–115；行号可能漂移）`

代码摘记：

- `"predicted_unit_states":`

公式或转换：

- `predicted_unit_states=SWM input/output field`

**示例**

- 当前实现的最小语义示例：预测步内的单位状态变化列表。 输入=`{"source": "current code"}`；输出=`{"predicted_unit_states": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predictions`](#var-swm-predictions)
- 下游：[`metric.swm.health_rmse`](#var-metric-swm-health-rmse)、[`metric.swm.position_rmse`](#var-metric-swm-position-rmse)、[`swm.unit.health_delta`](#var-swm-unit-health-delta)、[`swm.unit.position_delta`](#var-swm-unit-position-delta)

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-prediction-step"></a>
### `swm.prediction.step` — 预测相对步

**一句大白话：** 预测项相对当前状态的步号。

**正式定义：** 预测项相对当前状态的步号。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测相对步`, `Prediction Step`, `step`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.prediction.step`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 114–114；行号可能漂移）`

代码摘记：

- `"step": 1`

公式或转换：

- `step=SWM input/output field`

**示例**

- 当前实现的最小语义示例：预测项相对当前状态的步号。 输入=`{"source": "current code"}`；输出=`{"step": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predictions`](#var-swm-predictions)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-prediction-steps"></a>
### `swm.prediction_steps` — 预测步数

**一句大白话：** 预测未来多少个 STORM 步。

**正式定义：** 预测未来多少个 STORM 步。

**身份与来源**

- 分类：`swm`
- 来源层：`environment_config`（运行前配置输入）
- 派生方式：`direct_read`
- 可信状态：`code_reality`
- 别名：`预测步数`, `Prediction Steps`, `prediction_steps`

**接口形式**

- 数据类型：`integer`；Python 类型：`int`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.prediction_steps`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 129–129；行号可能漂移）`

代码摘记：

- `n_steps = prediction_steps or self.prediction_steps`

公式或转换：

- `prediction_steps=SWM input/output field`

**示例**

- 当前实现的最小语义示例：预测未来多少个 STORM 步。 输入=`{"source": "current code"}`；输出=`{"prediction_steps": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`swm.raw_response`](#var-swm-raw-response)

**限制与已知问题**

- 输入格式由当前 STORM 约定；来源层表示输入在进入 SWM 前的事实边界。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-swm-predictions"></a>
### `swm.predictions` — 逐步预测列表

**一句大白话：** 未来各步预测对象列表。

**正式定义：** 未来各步预测对象列表。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`逐步预测列表`, `Step Predictions`, `predictions`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`sequence`；可变长度序列。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.predictions`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 112–112；行号可能漂移）`

代码摘记：

- `"predictions": [`

公式或转换：

- `predictions=SWM input/output field`

**示例**

- 当前实现的最小语义示例：未来各步预测对象列表。 输入=`{"source": "current code"}`；输出=`{"predictions": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`swm.candidate_index`](#var-swm-candidate-index)、[`swm.predicted_relations`](#var-swm-predicted-relations)、[`swm.predicted_unit_states`](#var-swm-predicted-unit-states)、[`swm.prediction.step`](#var-swm-prediction-step)

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-raw-response"></a>
### `swm.raw_response` — 预测原始响应

**一句大白话：** 预测模型原始返回文本。

**正式定义：** 预测模型原始返回文本。

**身份与来源**

- 分类：`swm`
- 来源层：`llm_output`（LLM 原始动作输出）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测原始响应`, `Prediction Raw Response`, `raw_response`

**接口形式**

- 数据类型：`string`；Python 类型：`str`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.raw_response`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 147–147；行号可能漂移）`

代码摘记：

- `parsed["raw_response"] = raw_response`

公式或转换：

- `raw_response=SWM input/output field`

**示例**

- 当前实现的最小语义示例：预测模型原始返回文本。 输入=`{"source": "current code"}`；输出=`{"raw_response": "按公式得到"}`

**上下游关系**

- 上游：[`swm.input.abox_state`](#var-swm-input-abox-state)、[`swm.input.planned_actions`](#var-swm-input-planned-actions)、[`swm.prediction_steps`](#var-swm-prediction-steps)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-token-usage"></a>
### `swm.token_usage` — 预测 Token 用量

**一句大白话：** SWM LLM 调用 token 用量对象。

**正式定义：** SWM LLM 调用 token 用量对象。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测 Token 用量`, `Prediction Token Usage`, `token_usage`

**接口形式**

- 数据类型：`object`；Python 类型：`dict`
- 形状：`object`；键值对象。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.token_usage`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 146–146；行号可能漂移）`

代码摘记：

- `parsed["token_usage"] = self.client.last_usage`

公式或转换：

- `token_usage=SWM input/output field`

**示例**

- 当前实现的最小语义示例：SWM LLM 调用 token 用量对象。 输入=`{"source": "current code"}`；输出=`{"token_usage": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-unit-health-delta"></a>
### `swm.unit.health_delta` — 预测生命变化

**一句大白话：** 预测单位生命变化量。

**正式定义：** 预测单位生命变化量。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测生命变化`, `Predicted Health Delta`, `health_delta`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.unit.health_delta`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 272–272；行号可能漂移）`

代码摘记：

- `pred_unit.get("health_delta", 0)`

公式或转换：

- `health_delta=SWM input/output field`

**示例**

- 当前实现的最小语义示例：预测单位生命变化量。 输入=`{"source": "current code"}`；输出=`{"health_delta": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predicted_unit_states`](#var-swm-predicted-unit-states)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="var-swm-unit-position-delta"></a>
### `swm.unit.position_delta` — 预测位置变化

**一句大白话：** 预测单位二维位置变化。

**正式定义：** 预测单位二维位置变化。

**身份与来源**

- 分类：`swm`
- 来源层：`swm_prediction`（SWM 输入、输出或预测）
- 派生方式：`predicted`
- 可信状态：`needs_verification`
- 别名：`预测位置变化`, `Predicted Position Delta`, `position_delta`

**接口形式**

- 数据类型：`array`；Python 类型：`list`
- 形状：`vector`；二维 [x, y] 向量。
- 单位：未知（`unknown`）
- 范围：当前代码能证明的范围；其余范围待核验。（`unknown`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`swm.unit.position_delta`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.predict / compute_prediction_error（记录行 276–276；行号可能漂移）`

代码摘记：

- `pred_unit.get("position_delta", [0, 0])`

公式或转换：

- `position_delta=SWM input/output field`

**示例**

- 当前实现的最小语义示例：预测单位二维位置变化。 输入=`{"source": "current code"}`；输出=`{"position_delta": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predicted_unit_states`](#var-swm-predicted-unit-states)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`needs_verification`
- 方法：未记录

---

<a id="category-experiment-metric"></a>
## 实验指标

实验代码实际计算、聚合或写出的指标。

| 稳定 ID | 中文名 | 来源层 | 状态 |
|---|---|---|---|
| [`metric.action.decision_failure_rate`](#var-metric-action-decision-failure-rate) | 决策动作失败率 | `experiment_aggregate` | `code_reality` |
| [`metric.action.delayed_failure_rate`](#var-metric-action-delayed-failure-rate) | 延迟动作失败率 | `experiment_aggregate` | `code_reality` |
| [`metric.action.failure_rate`](#var-metric-action-failure-rate) | 动作失败率 | `experiment_aggregate` | `code_reality` |
| [`metric.episode.final_score`](#var-metric-episode-final-score) | 回合最终得分 | `experiment_aggregate` | `code_reality` |
| [`metric.experiment.avg_score`](#var-metric-experiment-avg-score) | 平均回合得分 | `experiment_aggregate` | `code_reality` |
| [`metric.llm.avg_decision_time`](#var-metric-llm-avg-decision-time) | 平均决策耗时 | `experiment_aggregate` | `code_reality` |
| [`metric.llm.avg_tokens_per_decision`](#var-metric-llm-avg-tokens-per-decision) | 每决策平均 Token | `experiment_aggregate` | `code_reality` |
| [`metric.llm.completion_tokens`](#var-metric-llm-completion-tokens) | 补全 Token 数 | `experiment_aggregate` | `code_reality` |
| [`metric.llm.decision_calls`](#var-metric-llm-decision-calls) | 决策调用次数 | `experiment_aggregate` | `code_reality` |
| [`metric.llm.prompt_tokens`](#var-metric-llm-prompt-tokens) | 提示 Token 数 | `experiment_aggregate` | `code_reality` |
| [`metric.llm.total_tokens`](#var-metric-llm-total-tokens) | 总 Token 数 | `experiment_aggregate` | `code_reality` |
| [`metric.swm.health_rmse`](#var-metric-swm-health-rmse) | 生命预测均方根误差 | `experiment_aggregate` | `code_reality` |
| [`metric.swm.overall_error`](#var-metric-swm-overall-error) | SWM 综合误差 | `experiment_aggregate` | `code_reality` |
| [`metric.swm.position_rmse`](#var-metric-swm-position-rmse) | 位置预测均方根误差 | `experiment_aggregate` | `code_reality` |
| [`metric.swm.relation_accuracy`](#var-metric-swm-relation-accuracy) | 关系预测准确率 | `experiment_aggregate` | `code_reality` |

<a id="var-metric-action-decision-failure-rate"></a>
### `metric.action.decision_failure_rate` — 决策动作失败率

**一句大白话：** 当前代码计算或聚合的决策动作失败率。

**正式定义：** 当前代码计算或聚合的决策动作失败率。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`决策动作失败率`, `Decision Action Failure Rate`, `decision_failure_rate`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.action.decision_failure_rate`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 146–146；行号可能漂移）`

代码摘记：

- `decision_failure_rate = float`

公式或转换：

- `failure_stats.action_failure_rate`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的决策动作失败率。 输入=`{"source": "current code"}`；输出=`{"decision_failure_rate": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`metric.action.failure_rate`](#var-metric-action-failure-rate)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-action-delayed-failure-rate"></a>
### `metric.action.delayed_failure_rate` — 延迟动作失败率

**一句大白话：** 当前代码计算或聚合的延迟动作失败率。

**正式定义：** 当前代码计算或聚合的延迟动作失败率。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`延迟动作失败率`, `Delayed Action Failure Rate`, `delayed_failure_rate`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.action.delayed_failure_rate`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 147–147；行号可能漂移）`

代码摘记：

- `delayed_failure_rate = float`

公式或转换：

- `failure_stats.delayed_failure_rate`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的延迟动作失败率。 输入=`{"source": "current code"}`；输出=`{"delayed_failure_rate": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`metric.action.failure_rate`](#var-metric-action-failure-rate)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-action-failure-rate"></a>
### `metric.action.failure_rate` — 动作失败率

**一句大白话：** 当前代码计算或聚合的动作失败率。

**正式定义：** 当前代码计算或聚合的动作失败率。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`动作失败率`, `Action Failure Rate`, `action_failure_rate`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.action.failure_rate`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 150–150；行号可能漂移）`

代码摘记：

- `action_failure_rate_list.append`

公式或转换：

- `min(1,decision_failure_rate+delayed_failure_rate)`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的动作失败率。 输入=`{"source": "current code"}`；输出=`{"action_failure_rate": "按公式得到"}`

**上下游关系**

- 上游：[`metric.action.decision_failure_rate`](#var-metric-action-decision-failure-rate)、[`metric.action.delayed_failure_rate`](#var-metric-action-delayed-failure-rate)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-episode-final-score"></a>
### `metric.episode.final_score` — 回合最终得分

**一句大白话：** 当前代码计算或聚合的回合最终得分。

**正式定义：** 当前代码计算或聚合的回合最终得分。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`回合最终得分`, `Episode Final Score`, `final_score`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.episode.final_score`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 133–133；行号可能漂移）`

代码摘记：

- `final_score = float(score_cumulative[0])`

公式或转换：

- `终止步 score_cumulative[0]`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的回合最终得分。 输入=`{"source": "current code"}`；输出=`{"final_score": "按公式得到"}`

**上下游关系**

- 上游：[`timestep.score_cumulative_0`](#var-timestep-score-cumulative-0)
- 下游：[`metric.experiment.avg_score`](#var-metric-experiment-avg-score)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-experiment-avg-score"></a>
### `metric.experiment.avg_score` — 平均回合得分

**一句大白话：** 当前代码计算或聚合的平均回合得分。

**正式定义：** 当前代码计算或聚合的平均回合得分。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`平均回合得分`, `Average Episode Score`, `avg_score`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.experiment.avg_score`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 178–178；行号可能漂移）`

代码摘记：

- `avg_score = sum(score_list)`

公式或转换：

- `sum(score_list)/len(score_list)`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的平均回合得分。 输入=`{"source": "current code"}`；输出=`{"avg_score": "按公式得到"}`

**上下游关系**

- 上游：[`metric.episode.final_score`](#var-metric-episode-final-score)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-llm-avg-decision-time"></a>
### `metric.llm.avg_decision_time` — 平均决策耗时

**一句大白话：** 当前代码计算或聚合的平均决策耗时。

**正式定义：** 当前代码计算或聚合的平均决策耗时。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`平均决策耗时`, `Average Decision Time`, `avg_decision_time`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`second`（`known`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.llm.avg_decision_time`

**STORM 实现与依据**

- `agents/raw_agent.py::RawAgent.step（记录行 321–321；行号可能漂移）`

代码摘记：

- `self.avg_decision_time = self.total_decision_time / self.decision_calls`

公式或转换：

- `total_decision_time/decision_calls`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的平均决策耗时。 输入=`{"source": "current code"}`；输出=`{"avg_decision_time": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-llm-avg-tokens-per-decision"></a>
### `metric.llm.avg_tokens_per_decision` — 每决策平均 Token

**一句大白话：** 当前代码计算或聚合的每决策平均 Token。

**正式定义：** 当前代码计算或聚合的每决策平均 Token。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`每决策平均 Token`, `Average Tokens per Decision`, `avg_total_tokens_per_decision`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.llm.avg_tokens_per_decision`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 172–172；行号可能漂移）`

代码摘记：

- `avg_total_tokens_per_decision = total_tokens / total_decision_calls`

公式或转换：

- `total_tokens/decision_calls；零调用为 0`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的每决策平均 Token。 输入=`{"source": "current code"}`；输出=`{"avg_total_tokens_per_decision": "按公式得到"}`

**上下游关系**

- 上游：[`metric.llm.decision_calls`](#var-metric-llm-decision-calls)、[`metric.llm.total_tokens`](#var-metric-llm-total-tokens)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-llm-completion-tokens"></a>
### `metric.llm.completion_tokens` — 补全 Token 数

**一句大白话：** 当前代码计算或聚合的补全 Token 数。

**正式定义：** 当前代码计算或聚合的补全 Token 数。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`补全 Token 数`, `Completion Tokens`, `completion_tokens`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.llm.completion_tokens`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 154–154；行号可能漂移）`

代码摘记：

- `total_completion_tokens +=`

公式或转换：

- `各决策 completion_tokens 求和`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的补全 Token 数。 输入=`{"source": "current code"}`；输出=`{"completion_tokens": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-llm-decision-calls"></a>
### `metric.llm.decision_calls` — 决策调用次数

**一句大白话：** 当前代码计算或聚合的决策调用次数。

**正式定义：** 当前代码计算或聚合的决策调用次数。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`决策调用次数`, `Decision Calls`, `decision_calls`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.llm.decision_calls`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 156–156；行号可能漂移）`

代码摘记：

- `total_decision_calls +=`

公式或转换：

- `决策调用次数求和`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的决策调用次数。 输入=`{"source": "current code"}`；输出=`{"decision_calls": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`metric.llm.avg_tokens_per_decision`](#var-metric-llm-avg-tokens-per-decision)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-llm-prompt-tokens"></a>
### `metric.llm.prompt_tokens` — 提示 Token 数

**一句大白话：** 当前代码计算或聚合的提示 Token 数。

**正式定义：** 当前代码计算或聚合的提示 Token 数。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`提示 Token 数`, `Prompt Tokens`, `prompt_tokens`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.llm.prompt_tokens`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 153–153；行号可能漂移）`

代码摘记：

- `total_prompt_tokens +=`

公式或转换：

- `各决策 prompt_tokens 求和`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的提示 Token 数。 输入=`{"source": "current code"}`；输出=`{"prompt_tokens": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：未记录正式变量下游。

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-llm-total-tokens"></a>
### `metric.llm.total_tokens` — 总 Token 数

**一句大白话：** 当前代码计算或聚合的总 Token 数。

**正式定义：** 当前代码计算或聚合的总 Token 数。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`总 Token 数`, `Total Tokens`, `total_tokens`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.llm.total_tokens`

**STORM 实现与依据**

- `examples/ablation_experiment.py::run_variant（记录行 155–155；行号可能漂移）`

代码摘记：

- `total_tokens +=`

公式或转换：

- `各决策 total_tokens 求和`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的总 Token 数。 输入=`{"source": "current code"}`；输出=`{"total_tokens": "按公式得到"}`

**上下游关系**

- 上游：未记录正式变量上游。
- 下游：[`metric.llm.avg_tokens_per_decision`](#var-metric-llm-avg-tokens-per-decision)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- 当前没有关联到登记中的已知问题。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-swm-health-rmse"></a>
### `metric.swm.health_rmse` — 生命预测均方根误差

**一句大白话：** 当前代码计算或聚合的生命预测均方根误差。

**正式定义：** 当前代码计算或聚合的生命预测均方根误差。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`生命预测均方根误差`, `Health RMSE`, `health_rmse`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.swm.health_rmse`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.compute_prediction_error（记录行 288–288；行号可能漂移）`

代码摘记：

- `health_rmse = float`

公式或转换：

- `sqrt(mean((pred_hp-actual_hp)^2))`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的生命预测均方根误差。 输入=`{"source": "current code"}`；输出=`{"health_rmse": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predicted_unit_states`](#var-swm-predicted-unit-states)
- 下游：[`metric.swm.overall_error`](#var-metric-swm-overall-error)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- **`issue.swm_error_uses_future_state_as_baseline` / critical：** health 误差退化为 delta²，position 误差退化为预测位移模长。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-swm-overall-error"></a>
### `metric.swm.overall_error` — SWM 综合误差

**一句大白话：** 当前代码计算或聚合的SWM 综合误差。

**正式定义：** 当前代码计算或聚合的SWM 综合误差。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`SWM 综合误差`, `SWM Overall Error`, `overall_error`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.swm.overall_error`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.compute_prediction_error（记录行 311–311；行号可能漂移）`

代码摘记：

- `overall = 0.4 * health_rmse`

公式或转换：

- `0.4*health_rmse+0.3*position_rmse+0.3*(1-relation_accuracy)`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的SWM 综合误差。 输入=`{"source": "current code"}`；输出=`{"overall_error": "按公式得到"}`

**上下游关系**

- 上游：[`metric.swm.health_rmse`](#var-metric-swm-health-rmse)、[`metric.swm.position_rmse`](#var-metric-swm-position-rmse)、[`metric.swm.relation_accuracy`](#var-metric-swm-relation-accuracy)
- 下游：未记录正式变量下游。

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- **`issue.swm_error_uses_future_state_as_baseline` / critical：** health 误差退化为 delta²，position 误差退化为预测位移模长。
- **`issue.swm_relation_accuracy_is_prediction_precision` / high：** 它不等同于覆盖假阴性的完整关系准确率。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-swm-position-rmse"></a>
### `metric.swm.position_rmse` — 位置预测均方根误差

**一句大白话：** 当前代码计算或聚合的位置预测均方根误差。

**正式定义：** 当前代码计算或聚合的位置预测均方根误差。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`位置预测均方根误差`, `Position RMSE`, `position_rmse`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：未知（`unknown`）
- 范围：0 ～ +∞（`needs_verification`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.swm.position_rmse`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.compute_prediction_error（记录行 289–289；行号可能漂移）`

代码摘记：

- `position_rmse = float`

公式或转换：

- `sqrt(mean(dx^2+dy^2))`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的位置预测均方根误差。 输入=`{"source": "current code"}`；输出=`{"position_rmse": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predicted_unit_states`](#var-swm-predicted-unit-states)
- 下游：[`metric.swm.overall_error`](#var-metric-swm-overall-error)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- **`issue.swm_error_uses_future_state_as_baseline` / critical：** health 误差退化为 delta²，position 误差退化为预测位移模长。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---

<a id="var-metric-swm-relation-accuracy"></a>
### `metric.swm.relation_accuracy` — 关系预测准确率

**一句大白话：** 当前代码计算或聚合的关系预测准确率。

**正式定义：** 当前代码计算或聚合的关系预测准确率。

**身份与来源**

- 分类：`experiment_metric`
- 来源层：`experiment_aggregate`（实验级统计与落盘）
- 派生方式：`aggregated`
- 可信状态：`code_reality`
- 别名：`关系预测准确率`, `Relation Accuracy`, `relation_accuracy`

**接口形式**

- 数据类型：`number`；Python 类型：`float`
- 形状：`scalar`；单个标量值。
- 单位：`1`（`known`）
- 范围：0 ～ 1（`known`）
- 枚举：不适用或未声明
- PySC2 路径：不适用或未确认（`not_applicable`）
- STORM 接口：`metric.swm.relation_accuracy`

**STORM 实现与依据**

- `ontology/swm_predictor.py::SWMPredictor.compute_prediction_error（记录行 309–309；行号可能漂移）`

代码摘记：

- `relation_accuracy = relation_correct / relation_total`

公式或转换：

- `correct/total；total=0 时为 1`

**示例**

- 当前实现的最小语义示例：当前代码计算或聚合的关系预测准确率。 输入=`{"source": "current code"}`；输出=`{"relation_accuracy": "按公式得到"}`

**上下游关系**

- 上游：[`swm.predicted_relations`](#var-swm-predicted-relations)
- 下游：[`metric.swm.overall_error`](#var-metric-swm-overall-error)

**限制与已知问题**

- 本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。
- **`issue.swm_relation_accuracy_is_prediction_precision` / high：** 它不等同于覆盖假阴性的完整关系准确率。

**核验状态**

- verification.status：`static_verified`
- 方法：未记录

---
