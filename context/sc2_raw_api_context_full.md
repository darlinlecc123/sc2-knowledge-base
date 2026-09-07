# STORM PySC2 Raw API 知识上下文（full）

> 版本：V0.1；正式变量：135；本文件注入变量卡：135。
> 证据边界：静态仓库证据；本步骤未启动 SC2、未调用外部 LLM/SWM、未核验外部官方资料。
> 若任何上游字段含明确的 Unicode U+FFFD 损坏标记，该字段将不注入；必须依据其余接口、公式和源码证据回答，不得猜测。

## 回答规则（必须遵守）

1. **先识别层级**：先说明变量属于 Raw observation、TimeStep/player、TBox、ABox、派生战术状态、动作、PySC2 FunctionCall、SWM、实验指标或环境配置中的哪一层。
2. **歧义不强选**：同名词对应多个变量时，列出候选 `variable_id` 并询问层级或使用场景。
3. **固定回答顺序**：给出 `variable_id` → 简明含义 → 接口形式 → 公式/转换 → 源码依据 → 限制与已知问题。
4. **证据优先**：以记录中的仓库相对路径、符号、代码片段和 evidence ID 为依据，不用外部常识替代当前代码事实。
5. **保留事实边界**：区分 `design_intent`、`code_reality`、`runtime_observation` 和 `needs_verification`；静态校验不等于 SC2 运行时验证。
6. **证据不足就说不知道**：字段缺失、编码损坏、范围未验证或当前 V0.1 未收录时，明确回答“不知道/当前知识库未验证”，不得补造 PySC2 字段。
7. **范围边界**：这里只覆盖当前 STORM 主路径实际使用及直接产生的 135 个正式变量，不是完整 PySC2 或 StarCraft II 百科。


## 使用说明

本文件包含 135 个正式变量的完整上下文卡。机器检索优先使用 `variables.jsonl` 与 `index.yaml`，避免每次注入全文。

## raw_unit：PySC2 RawUnit 观测与直接转换

### `raw_unit.alliance`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`alliance`；zh=阵营关系编码；en=Alliance Code
- **别名**：阵营关系编码、Alliance Code、alliance
- **简明含义**：相对当前代理的阵营编码；代码按 0/1/2/3/4 分组。
- **直观解释**：相对当前代理的阵营编码；代码按 0/1/2/3/4 分组。
- **接口**：`{"data_type":"integer","enum_values":{"description":"当前代码显式分组使用。","status":"known","values":[0,1,2,3,4]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][1]"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.alliance"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["alliance=unit[1]"]`
- **实现**：`{"extraction_code":["\"alliance\": unit[1]"],"source_locations":[{"line_end":351,"line_start":351,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["alliance=unit[1]"]}`
- **源码证据**：raw-unit-alliance-code @ agents/raw_agent.py:351-351 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.a16247ab6df92793","relation_type":"stored_as","variable_id":"abox.unit.alliance"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 1 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-alliance-code"],"id":"raw_alliance_index_semantics","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"相对当前代理的阵营编码；代码按 0/1/2/3/4 分组。","evidence_ids":["raw-unit-alliance-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.alliance`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.health`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`health`；zh=当前生命值；en=Current Health
- **别名**：当前生命值、Current Health、health
- **简明含义**：当前绝对生命值。
- **直观解释**：当前绝对生命值。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][2]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.health"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["health=unit[2]"]`
- **实现**：`{"extraction_code":["\"health\": unit[2]"],"source_locations":[{"line_end":354,"line_start":354,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["health=unit[2]"]}`
- **源码证据**：raw-unit-health-code @ agents/raw_agent.py:354-354 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.45c05ce1b1bc3c3f","relation_type":"stored_as","variable_id":"abox.unit.hp"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 2 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-health-code"],"id":"raw_health_index_semantics","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["abox.unit.hp","raw_unit.health","tbox.entity.hp"],"concise_explanation":"100 是未知类型静态占位，不是动态生命值覆盖。","current_implementation":"合并 static_info 后，instance_attrs.hp 单独使用实时 health。","evidence":[{"claim":"未知类型静态默认 hp 为 100。","line_end":37,"line_start":37,"path":"ontology/bridge.py","symbol":"UNKNOWN_UNIT_DEFAULTS"},{"claim":"ABox 动态 hp 读取实时 health。","line_end":199,"line_start":166,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._add_unit_instance"}],"expected_or_documented_behavior":"静态默认与动态观测应明确分层。","id":"issue.unknown_unit_hp_default_is_static_only","impact":{"code_or_experiment_risk":"混淆两层会错误判断未知单位状态。","knowledge_answer_constraint":"不能说未知单位生命值总被设为100；要解释静态占位和动态 hp 的层次。"},"issue_type":"implementation_quirk","limitations":["结论来自静态赋值路径。"],"phenomenon":"UNKNOWN_UNIT_DEFAULTS 定义 hp=100，但 ABox hp 仍读取 raw_unit['health']。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造未知类型且 health=37。","断言 ABox hp=37。"],"success_criteria":"动态 hp 保持实时值，静态占位仍可保留。"},"severity":"low","status":"open","title_zh":"未知单位 hp=100 不覆盖实时 health","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"当前绝对生命值。","evidence_ids":["raw-unit-health-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.health`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.health_ratio`
- **层级**：category=`raw_unit`；source_layer=`raw_unit_transformed`；derivation=`normalized`
- **名称**：canonical=`health_ratio`；zh=生命值比例；en=Health Ratio
- **别名**：生命值比例、Health Ratio、health_ratio
- **简明含义**：索引 7 的编码值除以 255。
- **直观解释**：索引 7 的编码值除以 255。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][7]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.health_ratio"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["health_ratio=unit[7]/255"]`
- **实现**：`{"extraction_code":["\"health_ratio\": unit[7]"],"source_locations":[{"line_end":355,"line_start":355,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["health_ratio=unit[7]/255"]}`
- **源码证据**：raw-unit-health-ratio-code @ agents/raw_agent.py:355-355 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.04580d13d79fa4a4","relation_type":"stored_as","variable_id":"abox.unit.hp_ratio"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。", "比例不是绝对值。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 7 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-health-ratio-code"],"id":"raw_health_ratio_index_semantics","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"索引 7 的编码值除以 255。","evidence_ids":["raw-unit-health-ratio-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'counts_and_aggregation']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.health_ratio`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.shield`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`shield`；zh=当前护盾值；en=Current Shield
- **别名**：当前护盾值、Current Shield、shield
- **简明含义**：当前绝对护盾值。
- **直观解释**：当前绝对护盾值。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][3]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.shield"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["shield=unit[3]"]`
- **实现**：`{"extraction_code":["\"shield\": unit[3]"],"source_locations":[{"line_end":356,"line_start":356,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["shield=unit[3]"]}`
- **源码证据**：raw-unit-shield-code @ agents/raw_agent.py:356-356 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.55fe9df54a3b743e","relation_type":"stored_as","variable_id":"abox.unit.armor"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 3 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-shield-code"],"id":"raw_shield_index_semantics","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["abox.unit.armor","abox.unit.armor_ratio","raw_unit.shield","raw_unit.shield_ratio"],"concise_explanation":"字段名称表达护甲，但当前数值语义是护盾。","current_implementation":"创建和更新 ABox 时均使用 shield 映射。","evidence":[{"claim":"创建路径把 shield 写入 armor。","line_end":202,"line_start":201,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._add_unit_instance"},{"claim":"更新路径沿用同一映射。","line_end":269,"line_start":264,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._update_unit_instance"}],"expected_or_documented_behavior":"armor 应保存护甲；若保存护盾应采用 shield 语义。","id":"issue.abox_armor_stores_shield","impact":{"code_or_experiment_risk":"论文或代码可能错误解释物理量。","knowledge_answer_constraint":"必须说明当前 ABox armor 实际是 shield，不能解释为 SC2 护甲。"},"issue_type":"implementation_quirk","limitations":["未启动 SC2。"],"phenomenon":"ABox 的 armor/armor_ratio 由 shield/shield_ratio 赋值。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造 shield 非零的 raw_unit。","检查 ABox 创建和更新结果。"],"success_criteria":"字段命名、文档语义和数据源一致。"},"severity":"high","status":"open","title_zh":"ABox armor 字段实际保存 shield","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"当前绝对护盾值。","evidence_ids":["raw-unit-shield-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.shield`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.shield_ratio`
- **层级**：category=`raw_unit`；source_layer=`raw_unit_transformed`；derivation=`normalized`
- **名称**：canonical=`shield_ratio`；zh=护盾比例；en=Shield Ratio
- **别名**：护盾比例、Shield Ratio、shield_ratio
- **简明含义**：索引 8 的编码值除以 255。
- **直观解释**：索引 8 的编码值除以 255。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][8]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.shield_ratio"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["shield_ratio=unit[8]/255"]`
- **实现**：`{"extraction_code":["\"shield_ratio\": unit[8]"],"source_locations":[{"line_end":357,"line_start":357,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["shield_ratio=unit[8]/255"]}`
- **源码证据**：raw-unit-shield-ratio-code @ agents/raw_agent.py:357-357 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.e0bc35595cab2815","relation_type":"stored_as","variable_id":"abox.unit.armor_ratio"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。", "比例不是绝对值。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 8 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-shield-ratio-code"],"id":"raw_shield_ratio_index_semantics","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["abox.unit.armor","abox.unit.armor_ratio","raw_unit.shield","raw_unit.shield_ratio"],"concise_explanation":"字段名称表达护甲，但当前数值语义是护盾。","current_implementation":"创建和更新 ABox 时均使用 shield 映射。","evidence":[{"claim":"创建路径把 shield 写入 armor。","line_end":202,"line_start":201,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._add_unit_instance"},{"claim":"更新路径沿用同一映射。","line_end":269,"line_start":264,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._update_unit_instance"}],"expected_or_documented_behavior":"armor 应保存护甲；若保存护盾应采用 shield 语义。","id":"issue.abox_armor_stores_shield","impact":{"code_or_experiment_risk":"论文或代码可能错误解释物理量。","knowledge_answer_constraint":"必须说明当前 ABox armor 实际是 shield，不能解释为 SC2 护甲。"},"issue_type":"implementation_quirk","limitations":["未启动 SC2。"],"phenomenon":"ABox 的 armor/armor_ratio 由 shield/shield_ratio 赋值。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造 shield 非零的 raw_unit。","检查 ABox 创建和更新结果。"],"success_criteria":"字段命名、文档语义和数据源一致。"},"severity":"high","status":"open","title_zh":"ABox armor 字段实际保存 shield","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"索引 8 的编码值除以 255。","evidence_ids":["raw-unit-shield-ratio-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'counts_and_aggregation']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.shield_ratio`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.tag`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`tag`；zh=单位标签；en=Unit Tag
- **别名**：单位标签、Unit Tag、tag
- **简明含义**：单位实例的运行时标签，用于追踪和动作寻址。
- **直观解释**：单位实例的运行时标签，用于追踪和动作寻址。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][29]"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.tag"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["tag=unit[29]"]`
- **实现**：`{"extraction_code":["\"tag\": unit[29]"],"source_locations":[{"line_end":349,"line_start":349,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["tag=unit[29]"]}`
- **源码证据**：raw-unit-tag-code @ agents/raw_agent.py:349-349 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.1abaa695443a64bd","relation_type":"stored_as","variable_id":"abox.unit.tag"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 29 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-tag-code"],"id":"raw_tag_index_semantics","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"单位实例的运行时标签，用于追踪和动作寻址。","evidence_ids":["raw-unit-tag-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.tag`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.unit_type`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`unit_type`；zh=单位类型编号；en=Unit Type ID
- **别名**：单位类型编号、Unit Type ID、unit_type
- **简明含义**：单位类型数字编号，用于查询 TBox。
- **直观解释**：单位类型数字编号，用于查询 TBox。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][0]"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.unit_type"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["unit_type=unit[0]"]`
- **实现**：`{"extraction_code":["\"unit_type\": unit[0]"],"source_locations":[{"line_end":350,"line_start":350,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["unit_type=unit[0]"]}`
- **源码证据**：raw-unit-unit-type-code @ agents/raw_agent.py:350-350 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.097320d17c031644","relation_type":"stored_as","variable_id":"abox.unit.is_unknown"},{"relation_id":"rel.stored_as.c913d241ad3a2c4f","relation_type":"stored_as","variable_id":"abox.unit.unit_type_id"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 0 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-unit-type-code"],"id":"raw_unit_type_index_semantics","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"单位类型数字编号，用于查询 TBox。","evidence_ids":["raw-unit-unit-type-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.unit_type`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.weapon_cooldown`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`weapon_cooldown`；zh=武器冷却；en=Weapon Cooldown
- **别名**：武器冷却、Weapon Cooldown、weapon_cooldown
- **简明含义**：当前武器冷却；等于 0 被近似视为可开火。
- **直观解释**：当前武器冷却；等于 0 被近似视为可开火。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][25]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.weapon_cooldown"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["weapon_cooldown=unit[25]"]`
- **实现**：`{"extraction_code":["\"weapon_cooldown\": unit[25]"],"source_locations":[{"line_end":358,"line_start":358,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["weapon_cooldown=unit[25]"]}`
- **源码证据**：raw-unit-weapon-cooldown-code @ agents/raw_agent.py:358-358 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.1074bb46d3ae1b13","relation_type":"stored_as","variable_id":"abox.unit.weapon_cooldown"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 25 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-weapon-cooldown-code"],"id":"raw_weapon_cooldown_index_semantics","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前武器冷却；等于 0 被近似视为可开火。","evidence_ids":["raw-unit-weapon-cooldown-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.weapon_cooldown`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.x`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`x`；zh=横坐标；en=X Coordinate
- **别名**：横坐标、X Coordinate、x
- **简明含义**：Raw 坐标 x 分量。
- **直观解释**：Raw 坐标 x 分量。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][12]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.x"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["x=unit[12]"]`
- **实现**：`{"extraction_code":["\"x\": unit[12]"],"source_locations":[{"line_end":352,"line_start":352,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["x=unit[12]"]}`
- **源码证据**：raw-unit-x-code @ agents/raw_agent.py:352-352 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.fd2a30bb49188146","relation_type":"stored_as","variable_id":"abox.unit.position"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 12 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-x-code"],"id":"raw_x_index_semantics","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"Raw 坐标 x 分量。","evidence_ids":["raw-unit-x-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.x`
- **因编码损坏未注入字段**：`[]`

### `raw_unit.y`
- **层级**：category=`raw_unit`；source_layer=`pysc2_raw_observation`；derivation=`direct_read`
- **名称**：canonical=`y`；zh=纵坐标；en=Y Coordinate
- **别名**：纵坐标、Y Coordinate、y
- **简明含义**：Raw 坐标 y 分量。
- **直观解释**：Raw 坐标 y 分量。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.raw_units[*][13]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["parsed_raw_unit.y"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["y=unit[13]"]`
- **实现**：`{"extraction_code":["\"y\": unit[13]"],"source_locations":[{"line_end":353,"line_start":353,"path":"agents/raw_agent.py","symbol":"RawAgent.parse_raw_units"}],"transformation_formula":["y=unit[13]"]}`
- **源码证据**：raw-unit-y-code @ agents/raw_agent.py:353-353 (RawAgent.parse_raw_units; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.9008c9352582ecbb","relation_type":"stored_as","variable_id":"abox.unit.position"}]`
- **限制**：`["采用位置索引；需与实际 PySC2 版本核验。"]`
- **已知问题**：`{"record_level":[{"description":"RawUnit 索引 13 的官方字段名、dtype 和版本语义尚未核验。","evidence_ids":["raw-unit-y-code"],"id":"raw_y_index_semantics","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"Raw 坐标 y 分量。","evidence_ids":["raw-unit-y-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry']；data_chains=['observation_to_abox']
- **原始记录引用**：`knowledge/variables/raw_unit.yaml#id=raw_unit.y`
- **因编码损坏未注入字段**：`[]`

## timestep_player_score：TimeStep、玩家资源与得分

### `player.food_cap`
- **层级**：category=`timestep_player_score`；source_layer=`pysc2_timestep`；derivation=`direct_read`
- **名称**：canonical=`player[4]`；zh=人口上限；en=Food Cap
- **别名**：人口上限、Food Cap、player[4]
- **简明含义**：从 player_info 索引 4 读取人口上限。
- **直观解释**：从 player_info 索引 4 读取人口上限。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.player[4]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.player_info[4]"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["food_cap=player_info[4]"]`
- **实现**：`{"extraction_code":["player_info[4]"],"source_locations":[{"line_end":933,"line_start":933,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["food_cap=player_info[4]"]}`
- **源码证据**：player-food-cap-code @ ontology/bridge.py:933-933 (BattlefieldGraph.generate_tactical_summary; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.transformed_to.770fe534a8462f32","relation_type":"transformed_to","variable_id":"player.supply_remaining"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"从 player_info 索引 4 读取人口上限。","evidence_ids":["player-food-cap-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'counts_and_aggregation', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=player.food_cap`
- **因编码损坏未注入字段**：`[]`

### `player.food_used`
- **层级**：category=`timestep_player_score`；source_layer=`pysc2_timestep`；derivation=`direct_read`
- **名称**：canonical=`player[3]`；zh=已用人口；en=Food Used
- **别名**：已用人口、Food Used、player[3]
- **简明含义**：从 player_info 索引 3 读取已用人口。
- **直观解释**：从 player_info 索引 3 读取已用人口。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.player[3]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.player_info[3]"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["food_used=player_info[3]"]`
- **实现**：`{"extraction_code":["player_info[3]"],"source_locations":[{"line_end":933,"line_start":933,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["food_used=player_info[3]"]}`
- **源码证据**：player-food-used-code @ ontology/bridge.py:933-933 (BattlefieldGraph.generate_tactical_summary; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.transformed_to.0d08d2b8d8b44bd5","relation_type":"transformed_to","variable_id":"player.supply_remaining"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"从 player_info 索引 3 读取已用人口。","evidence_ids":["player-food-used-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'counts_and_aggregation', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=player.food_used`
- **因编码损坏未注入字段**：`[]`

### `player.minerals`
- **层级**：category=`timestep_player_score`；source_layer=`pysc2_timestep`；derivation=`direct_read`
- **名称**：canonical=`player[1]`；zh=矿物资源；en=Minerals
- **别名**：矿物资源、Minerals、player[1]
- **简明含义**：从 player_info 索引 1 读取矿物资源。
- **直观解释**：从 player_info 索引 1 读取矿物资源。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.player[1]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.player_info[1]"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["minerals=player_info[1]"]`
- **实现**：`{"extraction_code":["player_info[1]"],"source_locations":[{"line_end":933,"line_start":933,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["minerals=player_info[1]"]}`
- **源码证据**：player-minerals-code @ ontology/bridge.py:933-933 (BattlefieldGraph.generate_tactical_summary; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"从 player_info 索引 1 读取矿物资源。","evidence_ids":["player-minerals-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'counts_and_aggregation', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=player.minerals`
- **因编码损坏未注入字段**：`[]`

### `player.supply_remaining`
- **层级**：category=`timestep_player_score`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`supply_remaining`；zh=剩余人口；en=Remaining Supply
- **别名**：剩余人口、Remaining Supply、supply_remaining
- **简明含义**：人口上限减去已用人口。
- **直观解释**：人口上限减去已用人口。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.Resources.Supply remaining"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["supply_remaining=food_cap-food_used"]`
- **实现**：`{"extraction_code":["player_info[4] - player_info[3]"],"source_locations":[{"line_end":933,"line_start":933,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["supply_remaining=food_cap-food_used"]}`
- **源码证据**：player-supply-remaining-code @ ontology/bridge.py:933-933 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.transformed_to.0d08d2b8d8b44bd5","relation_type":"transformed_to","variable_id":"player.food_used"},{"relation_id":"rel.transformed_to.770fe534a8462f32","relation_type":"transformed_to","variable_id":"player.food_cap"}]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"人口上限减去已用人口。","evidence_ids":["player-supply-remaining-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'counts_and_aggregation', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=player.supply_remaining`
- **因编码损坏未注入字段**：`[]`

### `player.vespene`
- **层级**：category=`timestep_player_score`；source_layer=`pysc2_timestep`；derivation=`direct_read`
- **名称**：canonical=`player[2]`；zh=高能瓦斯资源；en=Vespene Gas
- **别名**：高能瓦斯资源、Vespene Gas、player[2]
- **简明含义**：从 player_info 索引 2 读取高能瓦斯资源。
- **直观解释**：从 player_info 索引 2 读取高能瓦斯资源。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.player[2]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.player_info[2]"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["vespene=player_info[2]"]`
- **实现**：`{"extraction_code":["player_info[2]"],"source_locations":[{"line_end":933,"line_start":933,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["vespene=player_info[2]"]}`
- **源码证据**：player-vespene-code @ ontology/bridge.py:933-933 (BattlefieldGraph.generate_tactical_summary; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"从 player_info 索引 2 读取高能瓦斯资源。","evidence_ids":["player-vespene-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'counts_and_aggregation', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=player.vespene`
- **因编码损坏未注入字段**：`[]`

### `timestep.is_last`
- **层级**：category=`timestep_player_score`；source_layer=`pysc2_timestep`；derivation=`direct_read`
- **名称**：canonical=`last()`；zh=回合结束标志；en=Terminal TimeStep Flag
- **别名**：回合结束标志、Terminal TimeStep Flag、last()
- **简明含义**：通过 TimeStep.last() 判断当前步是否结束回合。
- **直观解释**：通过 TimeStep.last() 判断当前步是否结束回合。
- **接口**：`{"data_type":"boolean","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.last()"},"python_type":"bool","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["RawAgent.step terminal branch"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["is_last=obs.last()"]`
- **实现**：`{"extraction_code":["if timesteps[0].last():"],"source_locations":[{"line_end":114,"line_start":114,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["is_last=obs.last()"]}`
- **源码证据**：timestep-is-last-code @ examples/llm_agent_example.py:114-114 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"通过 TimeStep.last() 判断当前步是否结束回合。","evidence_ids":["timestep-is-last-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=timestep.is_last`
- **因编码损坏未注入字段**：`[]`

### `timestep.reward_delta`
- **层级**：category=`timestep_player_score`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`reward`；zh=决策间得分增量；en=Decision Score Delta
- **别名**：决策间得分增量、Decision Score Delta、reward
- **简明含义**：相邻两次触发决策时累计分数之差；不是直接读取 TimeStep.reward。
- **直观解释**：相邻两次触发决策时累计分数之差；不是直接读取 TimeStep.reward。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["RawAgent.reward"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"score point"}}`
- **公式/转换**：`["reward=new_score-previous_score"]`
- **实现**：`{"extraction_code":["self.reward = new_score - self.score"],"source_locations":[{"line_end":314,"line_start":314,"path":"agents/raw_agent.py","symbol":"RawAgent.step"}],"transformation_formula":["reward=new_score-previous_score"]}`
- **源码证据**：timestep-reward-delta-code @ agents/raw_agent.py:314-314 (RawAgent.step; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.transformed_to.23de9ad906cebe9c","relation_type":"transformed_to","variable_id":"timestep.score_cumulative_0"}]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"相邻两次触发决策时累计分数之差；不是直接读取 TimeStep.reward。","evidence_ids":["timestep-reward-delta-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'swm_prediction', 'evaluation_and_tokens', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=timestep.reward_delta`
- **因编码损坏未注入字段**：`[]`

### `timestep.score_cumulative_0`
- **层级**：category=`timestep_player_score`；source_layer=`pysc2_timestep`；derivation=`direct_read`
- **名称**：canonical=`score_cumulative[0]`；zh=累计得分首元素；en=Cumulative Score Element 0
- **别名**：累计得分首元素、Cumulative Score Element 0、score_cumulative[0]
- **简明含义**：读取 score_cumulative 第 0 个元素作为累计分数。
- **直观解释**：读取 score_cumulative 第 0 个元素作为累计分数。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"needs_verification","value":"obs.observation.score_cumulative[0]"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["RawAgent.score"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"score point"}}`
- **公式/转换**：`["score=score_cumulative[0]"]`
- **实现**：`{"extraction_code":["obs.observation.get(\"score_cumulative\", [0])[0]"],"source_locations":[{"line_end":313,"line_start":313,"path":"agents/raw_agent.py","symbol":"RawAgent.step"}],"transformation_formula":["score=score_cumulative[0]"]}`
- **源码证据**：timestep-score-cumulative-0-code @ agents/raw_agent.py:313-313 (RawAgent.step; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.93de4079427da478","relation_type":"stored_as","variable_id":"metric.episode.final_score"},{"relation_id":"rel.transformed_to.23de9ad906cebe9c","relation_type":"transformed_to","variable_id":"timestep.reward_delta"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"读取 score_cumulative 第 0 个元素作为累计分数。","evidence_ids":["timestep-score-cumulative-0-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'environment_and_timing']；data_chains=['observation_to_abox', 'environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=timestep.score_cumulative_0`
- **因编码损坏未注入字段**：`[]`

## tbox_static：TBox 静态类型知识

### `tbox.entity.armor`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`armor`；zh=类型护甲；en=Type Armor
- **别名**：类型护甲、Type Armor、armor
- **简明含义**：本体数据中已收录实体的类型级静态 armor 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 armor 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.armor"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["armor=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"armor\":"],"source_locations":[{"line_end":27,"line_start":27,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["armor=ontology node attribute"]}`
- **源码证据**：tbox-entity-armor-code @ ontology/data/marine_ontology.py:27-27 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-armor-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["tbox.entity.armor","tbox.entity.hp"],"concise_explanation":"修改本体定义后若未重建缓存，运行时可能继续使用旧 TBox。","current_implementation":"reload(use_pickle=True) 只在 pickle 不存在时重建。","evidence":[{"claim":"存在 pickle 时优先加载。","line_end":61,"line_start":57,"path":"ontology/loader.py","symbol":"OntologyLoader.reload"}],"expected_or_documented_behavior":"缓存应有一致性检查或版本标记。","id":"issue.ontology_pickle_may_be_stale","impact":{"code_or_experiment_risk":"静态属性和 BUILD/TRAIN 校验可能使用陈旧值。","knowledge_answer_constraint":"回答 TBox 数值时应披露缓存来源；未比对前不能断言与 Python 定义同步。"},"issue_type":"needs_runtime_test","limitations":["离线检查未执行。"],"phenomenon":"OntologyLoader 默认在 pickle 存在时优先加载，未自动比对源码定义。","recommended_verification":{"execution_status":"not_executed","method":"cache_consistency_check","steps":["分别加载 pickle 与源码重建图。","规范化后输出节点、边和属性差异。"],"success_criteria":"两图一致，或缓存可追溯且变更时自动重建。"},"severity":"medium","status":"open","title_zh":"TBox pickle 可能与 Python 定义不同步","truth_status":"needs_verification"}]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 armor 属性。","evidence_ids":["tbox-entity-armor-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.armor`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.attack_damage`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`attack_damage`；zh=攻击伤害；en=Attack Damage
- **别名**：攻击伤害、Attack Damage、attack_damage
- **简明含义**：本体数据中已收录实体的类型级静态 attack_damage 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 attack_damage 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.attack_damage"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["attack_damage=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"attack_damage\":"],"source_locations":[{"line_end":28,"line_start":28,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["attack_damage=ontology node attribute"]}`
- **源码证据**：tbox-entity-attack-damage-code @ ontology/data/marine_ontology.py:28-28 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.c78809703ef78063","relation_type":"stored_as","variable_id":"abox.unit.attack_damage"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-attack-damage-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 attack_damage 属性。","evidence_ids":["tbox-entity-attack-damage-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.attack_damage`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.attack_range`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`attack_range`；zh=攻击射程；en=Attack Range
- **别名**：攻击射程、Attack Range、attack_range
- **简明含义**：本体数据中已收录实体的类型级静态 attack_range 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 attack_range 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.attack_range"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["attack_range=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"attack_range\":"],"source_locations":[{"line_end":29,"line_start":29,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["attack_range=ontology node attribute"]}`
- **源码证据**：tbox-entity-attack-range-code @ ontology/data/marine_ontology.py:29-29 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.c15bfb455dc4d4b7","relation_type":"stored_as","variable_id":"abox.unit.attack_range"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-attack-range-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 attack_range 属性。","evidence_ids":["tbox-entity-attack-range-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry', 'combat_and_weapons', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.attack_range`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.attack_speed`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`attack_speed`；zh=攻击速度字段；en=Attack Speed
- **别名**：攻击速度字段、Attack Speed、attack_speed
- **简明含义**：本体数据中已收录实体的类型级静态 attack_speed 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 attack_speed 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.attack_speed"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["attack_speed=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"attack_speed\":"],"source_locations":[{"line_end":66,"line_start":66,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["attack_speed=ontology node attribute"]}`
- **源码证据**：tbox-entity-attack-speed-code @ ontology/data/marine_ontology.py:66-66 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.c8cfb2d4c2c5698f","relation_type":"stored_as","variable_id":"abox.unit.attack_speed"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-attack-speed-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 attack_speed 属性。","evidence_ids":["tbox-entity-attack-speed-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.attack_speed`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.build_time`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`build_time`；zh=建造时间；en=Build Time
- **别名**：建造时间、Build Time、build_time
- **简明含义**：本体数据中已收录实体的类型级静态 build_time 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 build_time 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.build_time"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["build_time=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"build_time\":"],"source_locations":[{"line_end":36,"line_start":36,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["build_time=ontology node attribute"]}`
- **源码证据**：tbox-entity-build-time-code @ ontology/data/marine_ontology.py:36-36 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-build-time-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 build_time 属性。","evidence_ids":["tbox-entity-build-time-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'actions_and_execution', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.build_time`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.category`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`category`；zh=实体类别；en=Entity Category
- **别名**：实体类别、Entity Category、category
- **简明含义**：本体数据中已收录实体的类型级静态 category 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 category 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.category"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["category=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"category\":"],"source_locations":[{"line_end":25,"line_start":25,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["category=ontology node attribute"]}`
- **源码证据**：tbox-entity-category-code @ ontology/data/marine_ontology.py:25-25 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.07231e6647a62c52","relation_type":"stored_as","variable_id":"abox.unit.category"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-category-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 category 属性。","evidence_ids":["tbox-entity-category-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.category`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.description`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`description`；zh=实体说明；en=Description
- **别名**：实体说明、Description、description
- **简明含义**：本体数据中已收录实体的类型级静态 description 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 description 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.description"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["description=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"description\":"],"source_locations":[{"line_end":37,"line_start":37,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["description=ontology node attribute"]}`
- **源码证据**：tbox-entity-description-code @ ontology/data/marine_ontology.py:37-37 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.5a79f0b5e0263ed1","relation_type":"stored_as","variable_id":"abox.unit.description"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-description-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 description 属性。","evidence_ids":["tbox-entity-description-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.description`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.dps`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`dps`；zh=每秒伤害；en=Damage Per Second
- **别名**：每秒伤害、Damage Per Second、dps
- **简明含义**：本体数据中已收录实体的类型级静态 dps 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 dps 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.dps"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["dps=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"dps\":"],"source_locations":[{"line_end":31,"line_start":31,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["dps=ontology node attribute"]}`
- **源码证据**：tbox-entity-dps-code @ ontology/data/marine_ontology.py:31-31 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-dps-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 dps 属性。","evidence_ids":["tbox-entity-dps-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.dps`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.gas_cost`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`gas_cost`；zh=瓦斯成本；en=Gas Cost
- **别名**：瓦斯成本、Gas Cost、gas_cost
- **简明含义**：本体数据中已收录实体的类型级静态 gas_cost 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 gas_cost 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.gas_cost"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["gas_cost=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"gas_cost\":"],"source_locations":[{"line_end":34,"line_start":34,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["gas_cost=ontology node attribute"]}`
- **源码证据**：tbox-entity-gas-cost-code @ ontology/data/marine_ontology.py:34-34 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-gas-cost-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 gas_cost 属性。","evidence_ids":["tbox-entity-gas-cost-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.gas_cost`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.hp`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`hp`；zh=类型生命值；en=Type HP
- **别名**：类型生命值、Type HP、hp
- **简明含义**：本体数据中已收录实体的类型级静态 hp 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 hp 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.hp"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["hp=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"hp\":"],"source_locations":[{"line_end":26,"line_start":26,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["hp=ontology node attribute"]}`
- **源码证据**：tbox-entity-hp-code @ ontology/data/marine_ontology.py:26-26 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-hp-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["tbox.entity.armor","tbox.entity.hp"],"concise_explanation":"修改本体定义后若未重建缓存，运行时可能继续使用旧 TBox。","current_implementation":"reload(use_pickle=True) 只在 pickle 不存在时重建。","evidence":[{"claim":"存在 pickle 时优先加载。","line_end":61,"line_start":57,"path":"ontology/loader.py","symbol":"OntologyLoader.reload"}],"expected_or_documented_behavior":"缓存应有一致性检查或版本标记。","id":"issue.ontology_pickle_may_be_stale","impact":{"code_or_experiment_risk":"静态属性和 BUILD/TRAIN 校验可能使用陈旧值。","knowledge_answer_constraint":"回答 TBox 数值时应披露缓存来源；未比对前不能断言与 Python 定义同步。"},"issue_type":"needs_runtime_test","limitations":["离线检查未执行。"],"phenomenon":"OntologyLoader 默认在 pickle 存在时优先加载，未自动比对源码定义。","recommended_verification":{"execution_status":"not_executed","method":"cache_consistency_check","steps":["分别加载 pickle 与源码重建图。","规范化后输出节点、边和属性差异。"],"success_criteria":"两图一致，或缓存可追溯且变更时自动重建。"},"severity":"medium","status":"open","title_zh":"TBox pickle 可能与 Python 定义不同步","truth_status":"needs_verification"},{"affected_noncanonical_fields":[],"affected_variable_ids":["abox.unit.hp","raw_unit.health","tbox.entity.hp"],"concise_explanation":"100 是未知类型静态占位，不是动态生命值覆盖。","current_implementation":"合并 static_info 后，instance_attrs.hp 单独使用实时 health。","evidence":[{"claim":"未知类型静态默认 hp 为 100。","line_end":37,"line_start":37,"path":"ontology/bridge.py","symbol":"UNKNOWN_UNIT_DEFAULTS"},{"claim":"ABox 动态 hp 读取实时 health。","line_end":199,"line_start":166,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._add_unit_instance"}],"expected_or_documented_behavior":"静态默认与动态观测应明确分层。","id":"issue.unknown_unit_hp_default_is_static_only","impact":{"code_or_experiment_risk":"混淆两层会错误判断未知单位状态。","knowledge_answer_constraint":"不能说未知单位生命值总被设为100；要解释静态占位和动态 hp 的层次。"},"issue_type":"implementation_quirk","limitations":["结论来自静态赋值路径。"],"phenomenon":"UNKNOWN_UNIT_DEFAULTS 定义 hp=100，但 ABox hp 仍读取 raw_unit['health']。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造未知类型且 health=37。","断言 ABox hp=37。"],"success_criteria":"动态 hp 保持实时值，静态占位仍可保留。"},"severity":"low","status":"open","title_zh":"未知单位 hp=100 不覆盖实时 health","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 hp 属性。","evidence_ids":["tbox-entity-hp-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.hp`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.mineral_cost`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`mineral_cost`；zh=矿物成本；en=Mineral Cost
- **别名**：矿物成本、Mineral Cost、mineral_cost
- **简明含义**：本体数据中已收录实体的类型级静态 mineral_cost 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 mineral_cost 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.mineral_cost"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["mineral_cost=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"mineral_cost\":"],"source_locations":[{"line_end":33,"line_start":33,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["mineral_cost=ontology node attribute"]}`
- **源码证据**：tbox-entity-mineral-cost-code @ ontology/data/marine_ontology.py:33-33 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-mineral-cost-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 mineral_cost 属性。","evidence_ids":["tbox-entity-mineral-cost-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.mineral_cost`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.movement_speed`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`movement_speed`；zh=移动速度；en=Movement Speed
- **别名**：移动速度、Movement Speed、movement_speed
- **简明含义**：本体数据中已收录实体的类型级静态 movement_speed 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 movement_speed 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.movement_speed"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["movement_speed=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"movement_speed\":"],"source_locations":[{"line_end":32,"line_start":32,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["movement_speed=ontology node attribute"]}`
- **源码证据**：tbox-entity-movement-speed-code @ ontology/data/marine_ontology.py:32-32 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.2adb6429a831593f","relation_type":"stored_as","variable_id":"abox.unit.movement_speed"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-movement-speed-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 movement_speed 属性。","evidence_ids":["tbox-entity-movement-speed-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.movement_speed`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.node_type`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`node_type`；zh=节点类型；en=Node Type
- **别名**：节点类型、Node Type、node_type
- **简明含义**：本体数据中已收录实体的类型级静态 node_type 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 node_type 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.node_type"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["node_type=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"node_type\":"],"source_locations":[{"line_end":22,"line_start":22,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["node_type=ontology node attribute"]}`
- **源码证据**：tbox-entity-node-type-code @ ontology/data/marine_ontology.py:22-22 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.db979ad77a0eeb92","relation_type":"stored_as","variable_id":"abox.unit.node_type"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-node-type-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 node_type 属性。","evidence_ids":["tbox-entity-node-type-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.node_type`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.race`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`race`；zh=种族；en=Race
- **别名**：种族、Race、race
- **简明含义**：本体数据中已收录实体的类型级静态 race 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 race 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.race"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["race=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"race\":"],"source_locations":[{"line_end":24,"line_start":24,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["race=ontology node attribute"]}`
- **源码证据**：tbox-entity-race-code @ ontology/data/marine_ontology.py:24-24 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.07bc9c4da25058e5","relation_type":"stored_as","variable_id":"abox.unit.race"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-race-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 race 属性。","evidence_ids":["tbox-entity-race-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.race`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.resource_type`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`resource_type`；zh=资源类型；en=Resource Type
- **别名**：资源类型、Resource Type、resource_type
- **简明含义**：本体数据中已收录实体的类型级静态 resource_type 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 resource_type 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.resource_type"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["resource_type=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"resource_type\":"],"source_locations":[{"line_end":349,"line_start":349,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["resource_type=ontology node attribute"]}`
- **源码证据**：tbox-entity-resource-type-code @ ontology/data/marine_ontology.py:349-349 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-resource-type-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 resource_type 属性。","evidence_ids":["tbox-entity-resource-type-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.resource_type`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.sight`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`sight`；zh=视野；en=Sight
- **别名**：视野、Sight、sight
- **简明含义**：本体数据中已收录实体的类型级静态 sight 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 sight 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.sight"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["sight=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"sight\":"],"source_locations":[{"line_end":30,"line_start":30,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["sight=ontology node attribute"]}`
- **源码证据**：tbox-entity-sight-code @ ontology/data/marine_ontology.py:30-30 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-sight-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 sight 属性。","evidence_ids":["tbox-entity-sight-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.sight`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.supply_cost`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`supply_cost`；zh=人口成本；en=Supply Cost
- **别名**：人口成本、Supply Cost、supply_cost
- **简明含义**：本体数据中已收录实体的类型级静态 supply_cost 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 supply_cost 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.supply_cost"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["supply_cost=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"supply_cost\":"],"source_locations":[{"line_end":35,"line_start":35,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["supply_cost=ontology node attribute"]}`
- **源码证据**：tbox-entity-supply-cost-code @ ontology/data/marine_ontology.py:35-35 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-supply-cost-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 supply_cost 属性。","evidence_ids":["tbox-entity-supply-cost-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['resources_and_supply', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.supply_cost`
- **因编码损坏未注入字段**：`[]`

### `tbox.entity.unit_type_id`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`unit_type_id`；zh=单位类型编号；en=Unit Type ID
- **别名**：单位类型编号、Unit Type ID、unit_type_id
- **简明含义**：本体数据中已收录实体的类型级静态 unit_type_id 属性。
- **直观解释**：本体数据中已收录实体的类型级静态 unit_type_id 属性。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["TBox node.unit_type_id"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["unit_type_id=ontology node attribute"]`
- **实现**：`{"extraction_code":["\"unit_type_id\":"],"source_locations":[{"line_end":23,"line_start":23,"path":"ontology/data/marine_ontology.py","symbol":"UNITS / BUILDINGS / RESOURCES"}],"transformation_formula":["unit_type_id=ontology node attribute"]}`
- **源码证据**：tbox-entity-unit-type-id-code @ ontology/data/marine_ontology.py:23-23 (UNITS / BUILDINGS / RESOURCES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.7930bc19a2671f0d","relation_type":"stored_as","variable_id":"abox.unit.unit_class"}]`
- **限制**：`["当前值来自 marine_ontology.py；OntologyLoader 可能优先读取 pickle 缓存，二者可能不同步。", "未逐项用 SC2 运行时或官方资料核验。"]`
- **已知问题**：`{"record_level":[{"description":"OntologyLoader 优先使用 data/ontology/ontology_graph.pkl，Python 定义修改后需重建缓存。","evidence_ids":["tbox-entity-unit-type-id-code"],"id":"tbox_cache_sync","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"本体数据中已收录实体的类型级静态 unit_type_id 属性。","evidence_ids":["tbox-entity-unit-type-id-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.entity.unit_type_id`
- **因编码损坏未注入字段**：`[]`

### `tbox.relation.edge`
- **层级**：category=`tbox_static`；source_layer=`tbox_static`；derivation=`static_declaration`
- **名称**：canonical=`EDGES`；zh=本体关系边；en=Ontology Relation Edge
- **别名**：本体关系边、Ontology Relation Edge、EDGES
- **简明含义**：类型级生产、依赖、消耗和克制等关系的边元组列表。
- **直观解释**：类型级生产、依赖、消耗和克制等关系的边元组列表。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["ontology.data.marine_ontology.EDGES"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["edge=(source,target,attributes)"]`
- **实现**：`{"extraction_code":["EDGES ="],"source_locations":[{"line_end":394,"line_start":394,"path":"ontology/data/marine_ontology.py","symbol":"EDGES"}],"transformation_formula":["edge=(source,target,attributes)"]}`
- **源码证据**：tbox-relation-edge-code @ ontology/data/marine_ontology.py:394-394 (EDGES; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.27f435e7ee8e875c","relation_type":"stored_as","variable_id":"abox.relation.effectiveness"},{"relation_id":"rel.stored_as.8df65ce4e738b832","relation_type":"stored_as","variable_id":"abox.relation.reason"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"类型级生产、依赖、消耗和克制等关系的边元组列表。","evidence_ids":["tbox-relation-edge-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['ontology_tbox_abox']
- **原始记录引用**：`knowledge/variables/tbox.yaml#id=tbox.relation.edge`
- **因编码损坏未注入字段**：`[]`

## abox_dynamic：ABox 运行时实例与关系

### `abox.graph.enemy_count`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`computed`
- **名称**：canonical=`enemy_count`；zh=ABox 敌军节点计数；en=ABox Enemy Node Count
- **别名**：ABox 敌军节点计数、ABox Enemy Node Count、enemy_count
- **简明含义**：当前 ABox 中 alliance 等于 4 的敌军单位节点数缓存。
- **直观解释**：当前 ABox 中 alliance 等于 4 的敌军单位节点数缓存。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.enemy_count"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["enemy_count = len(enemy_units)"]`
- **实现**：`{"extraction_code":["self.enemy_count = enemy_count"],"source_locations":[{"line_end":941,"line_start":941,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["enemy_count = len(enemy_units)"]}`
- **源码证据**：abox-graph-enemy-count-code @ ontology/bridge.py:941-941 (BattlefieldGraph.generate_tactical_summary; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.a7375d7e89087537","relation_type":"stored_as","variable_id":"abox.unit.alliance"}]`
- **直接下游**：`[]`
- **限制**：`["该缓存会在创建、删除节点或生成战术摘要时更新；不要与 derived.tactical.enemy_count 合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前 ABox 中 alliance 等于 4 的敌军单位节点数缓存。","evidence_ids":["abox-graph-enemy-count-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.graph.enemy_count`
- **因编码损坏未注入字段**：`[]`

### `abox.graph.step_count`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`computed`
- **名称**：canonical=`step_count`；zh=ABox 更新步数；en=ABox Update Step Count
- **别名**：ABox 更新步数、ABox Update Step Count、step_count
- **简明含义**：BattlefieldGraph 每次接收一批 raw_units 时递增的图更新序号。
- **直观解释**：BattlefieldGraph 每次接收一批 raw_units 时递增的图更新序号。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.step_count"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["step_count = previous_step_count + 1"]`
- **实现**：`{"extraction_code":["self.step_count += 1"],"source_locations":[{"line_end":113,"line_start":113,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.update_from_observation"}],"transformation_formula":["step_count = previous_step_count + 1"]}`
- **源码证据**：abox-graph-step-count-code @ ontology/bridge.py:113-113 (BattlefieldGraph.update_from_observation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.0e6b69c3eecd08ba","relation_type":"stored_as","variable_id":"abox.relation.timestamp"}]`
- **限制**：`["这是 BattlefieldGraph 更新次数，不等同于 SC2 game loop，也不等同于 PySC2 TimeStep 数。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"BattlefieldGraph 每次接收一批 raw_units 时递增的图更新序号。","evidence_ids":["abox-graph-step-count-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'ontology_and_graph', 'environment_and_timing']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.graph.step_count`
- **因编码损坏未注入字段**：`[]`

### `abox.relation.edge_class`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`direct_read`
- **名称**：canonical=`edge_class`；zh=关系类别；en=Relation Edge Class
- **别名**：关系类别、Relation Edge Class、edge_class
- **简明含义**：ABox 边是静态关系副本还是动态动作关系。
- **直观解释**：ABox 边是静态关系副本还是动态动作关系。
- **接口**：`{"data_type":"string","enum_values":{"description":"当前代码显式使用的枚举值。","status":"known","values":["static","dynamic"]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.edges[*].edge_class"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["edge_class 按当前 add_edge 调用参数写入"]`
- **实现**：`{"extraction_code":["edge_class=\"dynamic\""],"source_locations":[{"line_end":417,"line_start":417,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._replicate_static_relations / add_dynamic_relation"}],"transformation_formula":["edge_class 按当前 add_edge 调用参数写入"]}`
- **源码证据**：abox-relation-edge-class-code @ ontology/bridge.py:417-417 (BattlefieldGraph._replicate_static_relations / add_dynamic_relation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"ABox 边是静态关系副本还是动态动作关系。","evidence_ids":["abox-relation-edge-class-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.relation.edge_class`
- **因编码损坏未注入字段**：`[]`

### `abox.relation.edge_type`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`direct_read`
- **名称**：canonical=`edge_type`；zh=关系类型；en=Relation Edge Type
- **别名**：关系类型、Relation Edge Type、edge_type
- **简明含义**：ABox 边的关系类型；动态关系由 relation_type 参数写入。
- **直观解释**：ABox 边的关系类型；动态关系由 relation_type 参数写入。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.edges[*].edge_type"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["edge_type 按当前 add_edge 调用参数写入"]`
- **实现**：`{"extraction_code":["edge_type=relation_type"],"source_locations":[{"line_end":416,"line_start":416,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._replicate_static_relations / add_dynamic_relation"}],"transformation_formula":["edge_type 按当前 add_edge 调用参数写入"]}`
- **源码证据**：abox-relation-edge-type-code @ ontology/bridge.py:416-416 (BattlefieldGraph._replicate_static_relations / add_dynamic_relation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"ABox 边的关系类型；动态关系由 relation_type 参数写入。","evidence_ids":["abox-relation-edge-type-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.relation.edge_type`
- **因编码损坏未注入字段**：`[]`

### `abox.relation.effectiveness`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`computed`
- **名称**：canonical=`effectiveness`；zh=关系有效性；en=Relation Effectiveness
- **别名**：关系有效性、Relation Effectiveness、effectiveness
- **简明含义**：从 TBox 克制关系复制到 ABox 静态边的有效性描述。
- **直观解释**：从 TBox 克制关系复制到 ABox 静态边的有效性描述。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.edges[*].effectiveness"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["effectiveness 按当前 add_edge 调用参数写入"]`
- **实现**：`{"extraction_code":["effectiveness=relation[\"effectiveness\"]"],"source_locations":[{"line_end":343,"line_start":343,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._replicate_static_relations / add_dynamic_relation"}],"transformation_formula":["effectiveness 按当前 add_edge 调用参数写入"]}`
- **源码证据**：abox-relation-effectiveness-code @ ontology/bridge.py:343-343 (BattlefieldGraph._replicate_static_relations / add_dynamic_relation; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.27f435e7ee8e875c","relation_type":"stored_as","variable_id":"tbox.relation.edge"}]`
- **直接下游**：`[]`
- **限制**：`["NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"从 TBox 克制关系复制到 ABox 静态边的有效性描述。","evidence_ids":["abox-relation-effectiveness-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.relation.effectiveness`
- **因编码损坏未注入字段**：`[]`

### `abox.relation.reason`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`computed`
- **名称**：canonical=`reason`；zh=关系原因；en=Relation Reason
- **别名**：关系原因、Relation Reason、reason
- **简明含义**：从 TBox 克制关系复制到 ABox 静态边的原因说明。
- **直观解释**：从 TBox 克制关系复制到 ABox 静态边的原因说明。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.edges[*].reason"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["reason 按当前 add_edge 调用参数写入"]`
- **实现**：`{"extraction_code":["reason=relation[\"reason\"]"],"source_locations":[{"line_end":342,"line_start":342,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._replicate_static_relations / add_dynamic_relation"}],"transformation_formula":["reason 按当前 add_edge 调用参数写入"]}`
- **源码证据**：abox-relation-reason-code @ ontology/bridge.py:342-342 (BattlefieldGraph._replicate_static_relations / add_dynamic_relation; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.8df65ce4e738b832","relation_type":"stored_as","variable_id":"tbox.relation.edge"}]`
- **直接下游**：`[]`
- **限制**：`["NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"从 TBox 克制关系复制到 ABox 静态边的原因说明。","evidence_ids":["abox-relation-reason-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.relation.reason`
- **因编码损坏未注入字段**：`[]`

### `abox.relation.source_node`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`direct_read`
- **名称**：canonical=`source_node`；zh=关系源节点；en=Relation Source Node
- **别名**：关系源节点、Relation Source Node、source_node
- **简明含义**：ABox 有向关系边的起点实例节点 ID。
- **直观解释**：ABox 有向关系边的起点实例节点 ID。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.edges[*].source_node"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["source_node 按当前 add_edge 调用参数写入"]`
- **实现**：`{"extraction_code":["self.abox.add_edge("],"source_locations":[{"line_end":337,"line_start":337,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._replicate_static_relations / add_dynamic_relation"}],"transformation_formula":["source_node 按当前 add_edge 调用参数写入"]}`
- **源码证据**：abox-relation-source-node-code @ ontology/bridge.py:337-337 (BattlefieldGraph._replicate_static_relations / add_dynamic_relation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"ABox 有向关系边的起点实例节点 ID。","evidence_ids":["abox-relation-source-node-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.relation.source_node`
- **因编码损坏未注入字段**：`[]`

### `abox.relation.target_node`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`direct_read`
- **名称**：canonical=`target_node`；zh=关系目标节点；en=Relation Target Node
- **别名**：关系目标节点、Relation Target Node、target_node
- **简明含义**：ABox 有向关系边的终点实例节点 ID。
- **直观解释**：ABox 有向关系边的终点实例节点 ID。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.edges[*].target_node"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["target_node 按当前 add_edge 调用参数写入"]`
- **实现**：`{"extraction_code":["self.abox.add_edge("],"source_locations":[{"line_end":337,"line_start":337,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._replicate_static_relations / add_dynamic_relation"}],"transformation_formula":["target_node 按当前 add_edge 调用参数写入"]}`
- **源码证据**：abox-relation-target-node-code @ ontology/bridge.py:337-337 (BattlefieldGraph._replicate_static_relations / add_dynamic_relation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"ABox 有向关系边的终点实例节点 ID。","evidence_ids":["abox-relation-target-node-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.relation.target_node`
- **因编码损坏未注入字段**：`[]`

### `abox.relation.timestamp`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`computed`
- **名称**：canonical=`timestamp`；zh=动态关系时间戳；en=Dynamic Relation Timestamp
- **别名**：动态关系时间戳、Dynamic Relation Timestamp、timestamp
- **简明含义**：动态 ABox 关系创建时记录的 BattlefieldGraph.step_count。
- **直观解释**：动态 ABox 关系创建时记录的 BattlefieldGraph.step_count。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.edges[*].timestamp"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"ABox update step"}}`
- **公式/转换**：`["timestamp 按当前 add_edge 调用参数写入"]`
- **实现**：`{"extraction_code":["timestamp=self.step_count"],"source_locations":[{"line_end":418,"line_start":418,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._replicate_static_relations / add_dynamic_relation"}],"transformation_formula":["timestamp 按当前 add_edge 调用参数写入"]}`
- **源码证据**：abox-relation-timestamp-code @ ontology/bridge.py:418-418 (BattlefieldGraph._replicate_static_relations / add_dynamic_relation; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.0e6b69c3eecd08ba","relation_type":"stored_as","variable_id":"abox.graph.step_count"}]`
- **直接下游**：`[]`
- **限制**：`["NetworkX DiGraph 对同一 source-target 节点对只保留一组边属性；后写入关系可能更新既有边。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"动态 ABox 关系创建时记录的 BattlefieldGraph.step_count。","evidence_ids":["abox-relation-timestamp-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.relation.timestamp`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.alliance`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`alliance`；zh=阵营编码；en=Alliance Code
- **别名**：阵营编码、Alliance Code、alliance
- **简明含义**：创建 ABox 单位实例时写入的 alliance 属性。
- **直观解释**：创建 ABox 单位实例时写入的 alliance 属性。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].alliance"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.alliance=raw_unit[\"alliance\"]"]`
- **实现**：`{"extraction_code":["\"alliance\": raw_unit[\"alliance\"]"],"source_locations":[{"line_end":189,"line_start":189,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.alliance=raw_unit[\"alliance\"]"]}`
- **源码证据**：abox-unit-alliance-code @ ontology/bridge.py:189-189 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.a16247ab6df92793","relation_type":"stored_as","variable_id":"raw_unit.alliance"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.0bfbdaf9d8f3314a","relation_type":"aggregated_into","variable_id":"derived.tactical.friendly_avg_hp"},{"relation_id":"rel.aggregated_into.5fb62146af8e752d","relation_type":"aggregated_into","variable_id":"derived.tactical.enemy_avg_hp"},{"relation_id":"rel.aggregated_into.6591b82dd5011942","relation_type":"aggregated_into","variable_id":"derived.tactical.critical_units"},{"relation_id":"rel.aggregated_into.7a69a277212cbb19","relation_type":"aggregated_into","variable_id":"derived.tactical.enemy_count"},{"relation_id":"rel.aggregated_into.ac2e061e279a3b4a","relation_type":"aggregated_into","variable_id":"derived.tactical.friendly_count"},{"relation_id":"rel.aggregated_into.d8cec40154e8c4ae","relation_type":"aggregated_into","variable_id":"derived.tactical.ready_to_fire_count"},{"relation_id":"rel.stored_as.a7375d7e89087537","relation_type":"stored_as","variable_id":"abox.graph.enemy_count"}]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 alliance 属性。","evidence_ids":["abox-unit-alliance-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.alliance`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.armor`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`armor`；zh=ABox armor 字段；en=ABox Armor Field
- **别名**：ABox armor 字段、ABox Armor Field、armor
- **简明含义**：创建 ABox 单位实例时写入的 armor 属性。
- **直观解释**：创建 ABox 单位实例时写入的 armor 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].armor"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.armor=raw_unit.get(\"shield\", 0)"]`
- **实现**：`{"extraction_code":["\"armor\": raw_unit.get(\"shield\", 0)"],"source_locations":[{"line_end":201,"line_start":201,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.armor=raw_unit.get(\"shield\", 0)"]}`
- **源码证据**：abox-unit-armor-code @ ontology/bridge.py:201-201 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.55fe9df54a3b743e","relation_type":"stored_as","variable_id":"raw_unit.shield"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。", "该字段实际承载护盾值或护盾比例，不能按静态护甲解释。"]`
- **已知问题**：`{"record_level":[{"description":"当前代码把 raw_unit.shield 写入 armor，字段名与来源语义不一致。","evidence_ids":["abox-unit-armor-code"],"id":"abox_armor_is_shield","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["abox.unit.armor","abox.unit.armor_ratio","raw_unit.shield","raw_unit.shield_ratio"],"concise_explanation":"字段名称表达护甲，但当前数值语义是护盾。","current_implementation":"创建和更新 ABox 时均使用 shield 映射。","evidence":[{"claim":"创建路径把 shield 写入 armor。","line_end":202,"line_start":201,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._add_unit_instance"},{"claim":"更新路径沿用同一映射。","line_end":269,"line_start":264,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._update_unit_instance"}],"expected_or_documented_behavior":"armor 应保存护甲；若保存护盾应采用 shield 语义。","id":"issue.abox_armor_stores_shield","impact":{"code_or_experiment_risk":"论文或代码可能错误解释物理量。","knowledge_answer_constraint":"必须说明当前 ABox armor 实际是 shield，不能解释为 SC2 护甲。"},"issue_type":"implementation_quirk","limitations":["未启动 SC2。"],"phenomenon":"ABox 的 armor/armor_ratio 由 shield/shield_ratio 赋值。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造 shield 非零的 raw_unit。","检查 ABox 创建和更新结果。"],"success_criteria":"字段命名、文档语义和数据源一致。"},"severity":"high","status":"open","title_zh":"ABox armor 字段实际保存 shield","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 armor 属性。","evidence_ids":["abox-unit-armor-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.armor`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.armor_ratio`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`armor_ratio`；zh=ABox armor_ratio 字段；en=ABox Armor Ratio Field
- **别名**：ABox armor_ratio 字段、ABox Armor Ratio Field、armor_ratio
- **简明含义**：创建 ABox 单位实例时写入的 armor_ratio 属性。
- **直观解释**：创建 ABox 单位实例时写入的 armor_ratio 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].armor_ratio"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.armor_ratio=raw_unit.get(\"shield_ratio\", 0)"]`
- **实现**：`{"extraction_code":["\"armor_ratio\": raw_unit.get(\"shield_ratio\", 0)"],"source_locations":[{"line_end":202,"line_start":202,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.armor_ratio=raw_unit.get(\"shield_ratio\", 0)"]}`
- **源码证据**：abox-unit-armor-ratio-code @ ontology/bridge.py:202-202 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.e0bc35595cab2815","relation_type":"stored_as","variable_id":"raw_unit.shield_ratio"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。", "该字段实际承载护盾值或护盾比例，不能按静态护甲解释。"]`
- **已知问题**：`{"record_level":[{"description":"当前代码把 raw_unit.shield_ratio 写入 armor_ratio，字段名与来源语义不一致。","evidence_ids":["abox-unit-armor-ratio-code"],"id":"abox_armor_is_shield","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["abox.unit.armor","abox.unit.armor_ratio","raw_unit.shield","raw_unit.shield_ratio"],"concise_explanation":"字段名称表达护甲，但当前数值语义是护盾。","current_implementation":"创建和更新 ABox 时均使用 shield 映射。","evidence":[{"claim":"创建路径把 shield 写入 armor。","line_end":202,"line_start":201,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._add_unit_instance"},{"claim":"更新路径沿用同一映射。","line_end":269,"line_start":264,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._update_unit_instance"}],"expected_or_documented_behavior":"armor 应保存护甲；若保存护盾应采用 shield 语义。","id":"issue.abox_armor_stores_shield","impact":{"code_or_experiment_risk":"论文或代码可能错误解释物理量。","knowledge_answer_constraint":"必须说明当前 ABox armor 实际是 shield，不能解释为 SC2 护甲。"},"issue_type":"implementation_quirk","limitations":["未启动 SC2。"],"phenomenon":"ABox 的 armor/armor_ratio 由 shield/shield_ratio 赋值。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造 shield 非零的 raw_unit。","检查 ABox 创建和更新结果。"],"success_criteria":"字段命名、文档语义和数据源一致。"},"severity":"high","status":"open","title_zh":"ABox armor 字段实际保存 shield","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 armor_ratio 属性。","evidence_ids":["abox-unit-armor-ratio-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'counts_and_aggregation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.armor_ratio`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.attack_damage`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`attack_damage`；zh=攻击伤害；en=Attack Damage
- **别名**：攻击伤害、Attack Damage、attack_damage
- **简明含义**：创建 ABox 单位实例时写入的 attack_damage 属性。
- **直观解释**：创建 ABox 单位实例时写入的 attack_damage 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].attack_damage"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.attack_damage=static_info.get(\"attack_damage\")"]`
- **实现**：`{"extraction_code":["\"attack_damage\": static_info.get(\"attack_damage\")"],"source_locations":[{"line_end":194,"line_start":194,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.attack_damage=static_info.get(\"attack_damage\")"]}`
- **源码证据**：abox-unit-attack-damage-code @ ontology/bridge.py:194-194 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.c78809703ef78063","relation_type":"stored_as","variable_id":"tbox.entity.attack_damage"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 attack_damage 属性。","evidence_ids":["abox-unit-attack-damage-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.attack_damage`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.attack_range`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`attack_range`；zh=攻击射程；en=Attack Range
- **别名**：攻击射程、Attack Range、attack_range
- **简明含义**：创建 ABox 单位实例时写入的 attack_range 属性。
- **直观解释**：创建 ABox 单位实例时写入的 attack_range 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].attack_range"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.attack_range=static_info.get(\"attack_range\")"]`
- **实现**：`{"extraction_code":["\"attack_range\": static_info.get(\"attack_range\")"],"source_locations":[{"line_end":195,"line_start":195,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.attack_range=static_info.get(\"attack_range\")"]}`
- **源码证据**：abox-unit-attack-range-code @ ontology/bridge.py:195-195 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.c15bfb455dc4d4b7","relation_type":"stored_as","variable_id":"tbox.entity.attack_range"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 attack_range 属性。","evidence_ids":["abox-unit-attack-range-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry', 'combat_and_weapons', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.attack_range`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.attack_speed`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`attack_speed`；zh=攻击速度字段；en=Attack Speed
- **别名**：攻击速度字段、Attack Speed、attack_speed
- **简明含义**：创建 ABox 单位实例时写入的 attack_speed 属性。
- **直观解释**：创建 ABox 单位实例时写入的 attack_speed 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].attack_speed"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.attack_speed=static_info.get(\"attack_speed\")"]`
- **实现**：`{"extraction_code":["\"attack_speed\": static_info.get(\"attack_speed\")"],"source_locations":[{"line_end":196,"line_start":196,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.attack_speed=static_info.get(\"attack_speed\")"]}`
- **源码证据**：abox-unit-attack-speed-code @ ontology/bridge.py:196-196 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.c8cfb2d4c2c5698f","relation_type":"stored_as","variable_id":"tbox.entity.attack_speed"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 attack_speed 属性。","evidence_ids":["abox-unit-attack-speed-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.attack_speed`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.category`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`category`；zh=实体类别；en=Entity Category
- **别名**：实体类别、Entity Category、category
- **简明含义**：创建 ABox 单位实例时写入的 category 属性。
- **直观解释**：创建 ABox 单位实例时写入的 category 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":true,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].category"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.category=static_info.get(\"category\")"]`
- **实现**：`{"extraction_code":["\"category\": static_info.get(\"category\")"],"source_locations":[{"line_end":193,"line_start":193,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.category=static_info.get(\"category\")"]}`
- **源码证据**：abox-unit-category-code @ ontology/bridge.py:193-193 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.07231e6647a62c52","relation_type":"stored_as","variable_id":"tbox.entity.category"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 category 属性。","evidence_ids":["abox-unit-category-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.category`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.description`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`description`；zh=实体说明；en=Description
- **别名**：实体说明、Description、description
- **简明含义**：创建 ABox 单位实例时写入的 description 属性。
- **直观解释**：创建 ABox 单位实例时写入的 description 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":true,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].description"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.description=static_info.get(\"description\")"]`
- **实现**：`{"extraction_code":["\"description\": static_info.get(\"description\")"],"source_locations":[{"line_end":206,"line_start":206,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.description=static_info.get(\"description\")"]}`
- **源码证据**：abox-unit-description-code @ ontology/bridge.py:206-206 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.5a79f0b5e0263ed1","relation_type":"stored_as","variable_id":"tbox.entity.description"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 description 属性。","evidence_ids":["abox-unit-description-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.description`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.hp`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`hp`；zh=实例生命值；en=Instance HP
- **别名**：实例生命值、Instance HP、hp
- **简明含义**：创建 ABox 单位实例时写入的 hp 属性。
- **直观解释**：创建 ABox 单位实例时写入的 hp 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].hp"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.hp=raw_unit[\"health\"]"]`
- **实现**：`{"extraction_code":["\"hp\": raw_unit[\"health\"]"],"source_locations":[{"line_end":199,"line_start":199,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.hp=raw_unit[\"health\"]"]}`
- **源码证据**：abox-unit-hp-code @ ontology/bridge.py:199-199 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.45c05ce1b1bc3c3f","relation_type":"stored_as","variable_id":"raw_unit.health"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["abox.unit.hp","raw_unit.health","tbox.entity.hp"],"concise_explanation":"100 是未知类型静态占位，不是动态生命值覆盖。","current_implementation":"合并 static_info 后，instance_attrs.hp 单独使用实时 health。","evidence":[{"claim":"未知类型静态默认 hp 为 100。","line_end":37,"line_start":37,"path":"ontology/bridge.py","symbol":"UNKNOWN_UNIT_DEFAULTS"},{"claim":"ABox 动态 hp 读取实时 health。","line_end":199,"line_start":166,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._add_unit_instance"}],"expected_or_documented_behavior":"静态默认与动态观测应明确分层。","id":"issue.unknown_unit_hp_default_is_static_only","impact":{"code_or_experiment_risk":"混淆两层会错误判断未知单位状态。","knowledge_answer_constraint":"不能说未知单位生命值总被设为100；要解释静态占位和动态 hp 的层次。"},"issue_type":"implementation_quirk","limitations":["结论来自静态赋值路径。"],"phenomenon":"UNKNOWN_UNIT_DEFAULTS 定义 hp=100，但 ABox hp 仍读取 raw_unit['health']。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造未知类型且 health=37。","断言 ABox hp=37。"],"success_criteria":"动态 hp 保持实时值，静态占位仍可保留。"},"severity":"low","status":"open","title_zh":"未知单位 hp=100 不覆盖实时 health","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 hp 属性。","evidence_ids":["abox-unit-hp-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.hp`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.hp_ratio`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`hp_ratio`；zh=实例生命比例；en=Instance HP Ratio
- **别名**：实例生命比例、Instance HP Ratio、hp_ratio
- **简明含义**：创建 ABox 单位实例时写入的 hp_ratio 属性。
- **直观解释**：创建 ABox 单位实例时写入的 hp_ratio 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].hp_ratio"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.hp_ratio=raw_unit[\"health_ratio\"]"]`
- **实现**：`{"extraction_code":["\"hp_ratio\": raw_unit[\"health_ratio\"]"],"source_locations":[{"line_end":200,"line_start":200,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.hp_ratio=raw_unit[\"health_ratio\"]"]}`
- **源码证据**：abox-unit-hp-ratio-code @ ontology/bridge.py:200-200 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.04580d13d79fa4a4","relation_type":"stored_as","variable_id":"raw_unit.health_ratio"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.6e4553ea2413826f","relation_type":"aggregated_into","variable_id":"derived.tactical.friendly_avg_hp"},{"relation_id":"rel.aggregated_into.891dcca5411d0229","relation_type":"aggregated_into","variable_id":"derived.tactical.critical_units"},{"relation_id":"rel.aggregated_into.b9f197a1f3e93ad0","relation_type":"aggregated_into","variable_id":"derived.tactical.enemy_avg_hp"}]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 hp_ratio 属性。","evidence_ids":["abox-unit-hp-ratio-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'counts_and_aggregation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.hp_ratio`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.is_unknown`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`is_unknown`；zh=未知实体标志；en=Unknown Entity Flag
- **别名**：未知实体标志、Unknown Entity Flag、is_unknown
- **简明含义**：创建 ABox 单位实例时写入的 is_unknown 属性。
- **直观解释**：创建 ABox 单位实例时写入的 is_unknown 属性。
- **接口**：`{"data_type":"boolean","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"bool","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].is_unknown"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.is_unknown=is_unknown"]`
- **实现**：`{"extraction_code":["\"is_unknown\": is_unknown"],"source_locations":[{"line_end":190,"line_start":190,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.is_unknown=is_unknown"]}`
- **源码证据**：abox-unit-is-unknown-code @ ontology/bridge.py:190-190 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.097320d17c031644","relation_type":"stored_as","variable_id":"raw_unit.unit_type"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 is_unknown 属性。","evidence_ids":["abox-unit-is-unknown-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.is_unknown`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.movement_speed`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`movement_speed`；zh=移动速度；en=Movement Speed
- **别名**：移动速度、Movement Speed、movement_speed
- **简明含义**：创建 ABox 单位实例时写入的 movement_speed 属性。
- **直观解释**：创建 ABox 单位实例时写入的 movement_speed 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].movement_speed"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.movement_speed=static_info.get(\"movement_speed\")"]`
- **实现**：`{"extraction_code":["\"movement_speed\": static_info.get(\"movement_speed\")"],"source_locations":[{"line_end":197,"line_start":197,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.movement_speed=static_info.get(\"movement_speed\")"]}`
- **源码证据**：abox-unit-movement-speed-code @ ontology/bridge.py:197-197 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.2adb6429a831593f","relation_type":"stored_as","variable_id":"tbox.entity.movement_speed"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 movement_speed 属性。","evidence_ids":["abox-unit-movement-speed-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.movement_speed`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.node_type`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`node_type`；zh=节点类型；en=Node Type
- **别名**：节点类型、Node Type、node_type
- **简明含义**：创建 ABox 单位实例时写入的 node_type 属性。
- **直观解释**：创建 ABox 单位实例时写入的 node_type 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":true,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].node_type"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.node_type=static_info[\"node_type\"]"]`
- **实现**：`{"extraction_code":["\"node_type\": static_info[\"node_type\"]"],"source_locations":[{"line_end":185,"line_start":185,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.node_type=static_info[\"node_type\"]"]}`
- **源码证据**：abox-unit-node-type-code @ ontology/bridge.py:185-185 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.db979ad77a0eeb92","relation_type":"stored_as","variable_id":"tbox.entity.node_type"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 node_type 属性。","evidence_ids":["abox-unit-node-type-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.node_type`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.position`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`position`；zh=二维位置对象；en=2D Position
- **别名**：二维位置对象、2D Position、position
- **简明含义**：创建 ABox 单位实例时写入的 position 属性。
- **直观解释**：创建 ABox 单位实例时写入的 position 属性。
- **接口**：`{"data_type":"object","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"dict","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"键值对象。","dimensions":[],"kind":"object"},"storm_paths":["BattlefieldGraph.abox.nodes[*].position"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.position={\"x\": raw_unit[\"x\"], \"y\": raw_unit[\"y\"]}"]`
- **实现**：`{"extraction_code":["\"position\": {\"x\": raw_unit[\"x\"], \"y\": raw_unit[\"y\"]}"],"source_locations":[{"line_end":203,"line_start":203,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.position={\"x\": raw_unit[\"x\"], \"y\": raw_unit[\"y\"]}"]}`
- **源码证据**：abox-unit-position-code @ ontology/bridge.py:203-203 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.9008c9352582ecbb","relation_type":"stored_as","variable_id":"raw_unit.y"},{"relation_id":"rel.stored_as.fd2a30bb49188146","relation_type":"stored_as","variable_id":"raw_unit.x"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.432869a2c9739ef0","relation_type":"aggregated_into","variable_id":"derived.tactical.friendly_centroid"},{"relation_id":"rel.aggregated_into.9a9e282a831dd378","relation_type":"aggregated_into","variable_id":"derived.tactical.enemy_centroid"}]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 position 属性。","evidence_ids":["abox-unit-position-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.position`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.race`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`race`；zh=种族；en=Race
- **别名**：种族、Race、race
- **简明含义**：创建 ABox 单位实例时写入的 race 属性。
- **直观解释**：创建 ABox 单位实例时写入的 race 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":true,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].race"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.race=static_info.get(\"race\")"]`
- **实现**：`{"extraction_code":["\"race\": static_info.get(\"race\")"],"source_locations":[{"line_end":192,"line_start":192,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.race=static_info.get(\"race\")"]}`
- **源码证据**：abox-unit-race-code @ ontology/bridge.py:192-192 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.07bc9c4da25058e5","relation_type":"stored_as","variable_id":"tbox.entity.race"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 race 属性。","evidence_ids":["abox-unit-race-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.race`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.tag`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`tag`；zh=实例标签；en=Instance Tag
- **别名**：实例标签、Instance Tag、tag
- **简明含义**：创建 ABox 单位实例时写入的 tag 属性。
- **直观解释**：创建 ABox 单位实例时写入的 tag 属性。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].tag"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.tag=tag"]`
- **实现**：`{"extraction_code":["\"tag\": tag"],"source_locations":[{"line_end":186,"line_start":186,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.tag=tag"]}`
- **源码证据**：abox-unit-tag-code @ ontology/bridge.py:186-186 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.1abaa695443a64bd","relation_type":"stored_as","variable_id":"raw_unit.tag"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 tag 属性。","evidence_ids":["abox-unit-tag-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.tag`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.unit_class`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`unit_class`；zh=单位类别名；en=Unit Class
- **别名**：单位类别名、Unit Class、unit_class
- **简明含义**：创建 ABox 单位实例时写入的 unit_class 属性。
- **直观解释**：创建 ABox 单位实例时写入的 unit_class 属性。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":true,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].unit_class"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.unit_class=unit_name"]`
- **实现**：`{"extraction_code":["\"unit_class\": unit_name"],"source_locations":[{"line_end":188,"line_start":188,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.unit_class=unit_name"]}`
- **源码证据**：abox-unit-unit-class-code @ ontology/bridge.py:188-188 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.7930bc19a2671f0d","relation_type":"stored_as","variable_id":"tbox.entity.unit_type_id"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 unit_class 属性。","evidence_ids":["abox-unit-unit-class-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.unit_class`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.unit_type_id`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`unit_type_id`；zh=单位类型编号；en=Unit Type ID
- **别名**：单位类型编号、Unit Type ID、unit_type_id
- **简明含义**：创建 ABox 单位实例时写入的 unit_type_id 属性。
- **直观解释**：创建 ABox 单位实例时写入的 unit_type_id 属性。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].unit_type_id"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.unit_type_id=unit_type_id"]`
- **实现**：`{"extraction_code":["\"unit_type_id\": unit_type_id"],"source_locations":[{"line_end":187,"line_start":187,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.unit_type_id=unit_type_id"]}`
- **源码证据**：abox-unit-unit-type-id-code @ ontology/bridge.py:187-187 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.c913d241ad3a2c4f","relation_type":"stored_as","variable_id":"raw_unit.unit_type"}]`
- **直接下游**：`[]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 unit_type_id 属性。","evidence_ids":["abox-unit-unit-type-id-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.unit_type_id`
- **因编码损坏未注入字段**：`[]`

### `abox.unit.weapon_cooldown`
- **层级**：category=`abox_dynamic`；source_layer=`abox_runtime`；derivation=`renamed`
- **名称**：canonical=`weapon_cooldown`；zh=武器冷却；en=Weapon Cooldown
- **别名**：武器冷却、Weapon Cooldown、weapon_cooldown
- **简明含义**：创建 ABox 单位实例时写入的 weapon_cooldown 属性。
- **直观解释**：创建 ABox 单位实例时写入的 weapon_cooldown 属性。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["BattlefieldGraph.abox.nodes[*].weapon_cooldown"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox.weapon_cooldown=raw_unit.get(\"weapon_cooldown\", 0)"]`
- **实现**：`{"extraction_code":["\"weapon_cooldown\": raw_unit.get(\"weapon_cooldown\", 0)"],"source_locations":[{"line_end":204,"line_start":204,"path":"ontology/bridge.py","symbol":"BattlefieldGraph._create_instance"}],"transformation_formula":["abox.weapon_cooldown=raw_unit.get(\"weapon_cooldown\", 0)"]}`
- **源码证据**：abox-unit-weapon-cooldown-code @ ontology/bridge.py:204-204 (BattlefieldGraph._create_instance; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.1074bb46d3ae1b13","relation_type":"stored_as","variable_id":"raw_unit.weapon_cooldown"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.0b6ab10389150863","relation_type":"aggregated_into","variable_id":"derived.tactical.ready_to_fire_count"}]`
- **限制**：`["ABox 实例字段不能与同名 TBox 静态属性合并。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"创建 ABox 单位实例时写入的 weapon_cooldown 属性。","evidence_ids":["abox-unit-weapon-cooldown-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'ontology_and_graph']；data_chains=['observation_to_abox', 'ontology_tbox_abox', 'abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/abox.yaml#id=abox.unit.weapon_cooldown`
- **因编码损坏未注入字段**：`[]`

## derived_tactical_state：派生战术状态

### `derived.tactical.critical_units`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`critical_units`；zh=危急单位列表；en=Critical Units
- **别名**：危急单位列表、Critical Units、critical_units
- **简明含义**：hp_ratio 小于 0.3 的友军，输出最多三个实例名。
- **直观解释**：hp_ratio 小于 0.3 的友军，输出最多三个实例名。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["tactical_summary.Critical_Units"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["d.get(\"hp_ratio\", 1.0) < 0.3"]`
- **实现**：`{"extraction_code":["d.get(\"hp_ratio\", 1.0) < 0.3"],"source_locations":[{"line_end":952,"line_start":952,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["d.get(\"hp_ratio\", 1.0) < 0.3"]}`
- **源码证据**：derived-tactical-critical-units-code @ ontology/bridge.py:952-952 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.6591b82dd5011942","relation_type":"aggregated_into","variable_id":"abox.unit.alliance"},{"relation_id":"rel.aggregated_into.891dcca5411d0229","relation_type":"aggregated_into","variable_id":"abox.unit.hp_ratio"}]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"hp_ratio 小于 0.3 的友军，输出最多三个实例名。","evidence_ids":["derived-tactical-critical-units-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.critical_units`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.enemy_avg_hp`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`enemy_avg_hp`；zh=敌军平均生命比例；en=Enemy Average HP Ratio
- **别名**：敌军平均生命比例、Enemy Average HP Ratio、enemy_avg_hp
- **简明含义**：敌军 hp_ratio 算术平均。
- **直观解释**：敌军 hp_ratio 算术平均。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.enemy_avg_hp"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["enemy_avg_hp = sum"]`
- **实现**：`{"extraction_code":["enemy_avg_hp = sum"],"source_locations":[{"line_end":945,"line_start":945,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["enemy_avg_hp = sum"]}`
- **源码证据**：derived-tactical-enemy-avg-hp-code @ ontology/bridge.py:945-945 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.5fb62146af8e752d","relation_type":"aggregated_into","variable_id":"abox.unit.alliance"},{"relation_id":"rel.aggregated_into.b9f197a1f3e93ad0","relation_type":"aggregated_into","variable_id":"abox.unit.hp_ratio"}]`
- **直接下游**：`[{"relation_id":"rel.transformed_to.26de7cfddbed7434","relation_type":"transformed_to","variable_id":"derived.tactical.health_status"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"敌军 hp_ratio 算术平均。","evidence_ids":["derived-tactical-enemy-avg-hp-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.enemy_avg_hp`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.enemy_centroid`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`enemy_centroid`；zh=敌军质心；en=Enemy Centroid
- **别名**：敌军质心、Enemy Centroid、enemy_centroid
- **简明含义**：敌军二维位置的算术平均点。
- **直观解释**：敌军二维位置的算术平均点。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"二维 [x, y] 向量。","dimensions":[2],"kind":"vector"},"storm_paths":["derived.enemy_centroid"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["enemy_center_x ="]`
- **实现**：`{"extraction_code":["enemy_center_x ="],"source_locations":[{"line_end":965,"line_start":965,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["enemy_center_x ="]}`
- **源码证据**：derived-tactical-enemy-centroid-code @ ontology/bridge.py:965-965 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.9a9e282a831dd378","relation_type":"aggregated_into","variable_id":"abox.unit.position"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.6b8c24ea3425532e","relation_type":"aggregated_into","variable_id":"derived.tactical.formation_distance"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"敌军二维位置的算术平均点。","evidence_ids":["derived-tactical-enemy-centroid-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.enemy_centroid`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.enemy_count`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`enemy_count`；zh=敌军单位数；en=Enemy Unit Count
- **别名**：敌军单位数、Enemy Unit Count、enemy_count
- **简明含义**：敌军 ABox 节点数量。
- **直观解释**：敌军 ABox 节点数量。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.enemy_count"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["enemy_count = len(enemy_units)"]`
- **实现**：`{"extraction_code":["enemy_count = len(enemy_units)"],"source_locations":[{"line_end":940,"line_start":940,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["enemy_count = len(enemy_units)"]}`
- **源码证据**：derived-tactical-enemy-count-code @ ontology/bridge.py:940-940 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.7a69a277212cbb19","relation_type":"aggregated_into","variable_id":"abox.unit.alliance"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.cb789af2658e03e1","relation_type":"aggregated_into","variable_id":"derived.tactical.force_ratio"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"敌军 ABox 节点数量。","evidence_ids":["derived-tactical-enemy-count-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.enemy_count`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.engagement_type`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`engagement_type`；zh=接战距离类型；en=Engagement Type
- **别名**：接战距离类型、Engagement Type、engagement_type
- **简明含义**：质心距离小于 10 为 Close-Combat，小于 20 为 Medium-Range，否则 Long-Range。
- **直观解释**：质心距离小于 10 为 Close-Combat，小于 20 为 Medium-Range，否则 Long-Range。
- **接口**：`{"data_type":"string","enum_values":{"description":"当前代码显式使用的枚举值。","status":"known","values":["Close-Combat","Medium-Range","Long-Range"]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.Engagement_Type"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["d<10: Close-Combat; 10<=d<20: Medium-Range; d>=20: Long-Range"]`
- **实现**：`{"extraction_code":["situation = \"Close-Combat\""],"source_locations":[{"line_end":976,"line_start":976,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["d<10: Close-Combat; 10<=d<20: Medium-Range; d>=20: Long-Range"]}`
- **源码证据**：derived-tactical-engagement-type-code @ ontology/bridge.py:976-976 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.transformed_to.99f6b4d07c767d4e","relation_type":"transformed_to","variable_id":"derived.tactical.formation_distance"}]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"质心距离小于 10 为 Close-Combat，小于 20 为 Medium-Range，否则 Long-Range。","evidence_ids":["derived-tactical-engagement-type-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['other_project_variable']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.engagement_type`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.fire_readiness`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`fire_readiness`；zh=火力就绪比例；en=Fire Readiness
- **别名**：火力就绪比例、Fire Readiness、fire_readiness
- **简明含义**：可开火友军数除以友军总数。
- **直观解释**：可开火友军数除以友军总数。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.fire_readiness"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["ready_ratio = ready_to_fire / friendly_count"]`
- **实现**：`{"extraction_code":["ready_ratio = ready_to_fire / friendly_count"],"source_locations":[{"line_end":987,"line_start":987,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["ready_ratio = ready_to_fire / friendly_count"]}`
- **源码证据**：derived-tactical-fire-readiness-code @ ontology/bridge.py:987-987 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.05e2d525dda918a6","relation_type":"aggregated_into","variable_id":"derived.tactical.friendly_count"},{"relation_id":"rel.aggregated_into.7498cd35b96dc33e","relation_type":"aggregated_into","variable_id":"derived.tactical.ready_to_fire_count"}]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"可开火友军数除以友军总数。","evidence_ids":["derived-tactical-fire-readiness-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.fire_readiness`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.force_ratio`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`force_ratio`；zh=兵力对比；en=Force Ratio
- **别名**：兵力对比、Force Ratio、force_ratio
- **简明含义**：“友军数 vs 敌军数”的摘要文本。
- **直观解释**：“友军数 vs 敌军数”的摘要文本。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.force_ratio"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["Force_Ratio: {friendly_count} vs {enemy_count}"]`
- **实现**：`{"extraction_code":["Force_Ratio: {friendly_count} vs {enemy_count}"],"source_locations":[{"line_end":948,"line_start":948,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["Force_Ratio: {friendly_count} vs {enemy_count}"]}`
- **源码证据**：derived-tactical-force-ratio-code @ ontology/bridge.py:948-948 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.550884e5eb3782f4","relation_type":"aggregated_into","variable_id":"derived.tactical.friendly_count"},{"relation_id":"rel.aggregated_into.cb789af2658e03e1","relation_type":"aggregated_into","variable_id":"derived.tactical.enemy_count"}]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"“友军数 vs 敌军数”的摘要文本。","evidence_ids":["derived-tactical-force-ratio-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.force_ratio`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.formation_distance`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`formation_distance`；zh=阵型中心距离；en=Formation Distance
- **别名**：阵型中心距离、Formation Distance、formation_distance
- **简明含义**：敌我质心之间的欧氏距离。
- **直观解释**：敌我质心之间的欧氏距离。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.formation_distance"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["center_distance = math.dist"]`
- **实现**：`{"extraction_code":["center_distance = math.dist"],"source_locations":[{"line_end":969,"line_start":969,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["center_distance = math.dist"]}`
- **源码证据**：derived-tactical-formation-distance-code @ ontology/bridge.py:969-969 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.6b8c24ea3425532e","relation_type":"aggregated_into","variable_id":"derived.tactical.enemy_centroid"},{"relation_id":"rel.aggregated_into.f6620df914bda5ea","relation_type":"aggregated_into","variable_id":"derived.tactical.friendly_centroid"}]`
- **直接下游**：`[{"relation_id":"rel.transformed_to.99f6b4d07c767d4e","relation_type":"transformed_to","variable_id":"derived.tactical.engagement_type"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"敌我质心之间的欧氏距离。","evidence_ids":["derived-tactical-formation-distance-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.formation_distance`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.friendly_avg_hp`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`friendly_avg_hp`；zh=友军平均生命比例；en=Friendly Average HP Ratio
- **别名**：友军平均生命比例、Friendly Average HP Ratio、friendly_avg_hp
- **简明含义**：友军 hp_ratio 算术平均。
- **直观解释**：友军 hp_ratio 算术平均。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.friendly_avg_hp"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["friendly_avg_hp = sum"]`
- **实现**：`{"extraction_code":["friendly_avg_hp = sum"],"source_locations":[{"line_end":944,"line_start":944,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["friendly_avg_hp = sum"]}`
- **源码证据**：derived-tactical-friendly-avg-hp-code @ ontology/bridge.py:944-944 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.0bfbdaf9d8f3314a","relation_type":"aggregated_into","variable_id":"abox.unit.alliance"},{"relation_id":"rel.aggregated_into.6e4553ea2413826f","relation_type":"aggregated_into","variable_id":"abox.unit.hp_ratio"}]`
- **直接下游**：`[{"relation_id":"rel.transformed_to.daa7dbae7461cec4","relation_type":"transformed_to","variable_id":"derived.tactical.health_status"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"友军 hp_ratio 算术平均。","evidence_ids":["derived-tactical-friendly-avg-hp-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.friendly_avg_hp`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.friendly_centroid`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`friendly_centroid`；zh=友军质心；en=Friendly Centroid
- **别名**：友军质心、Friendly Centroid、friendly_centroid
- **简明含义**：友军二维位置的算术平均点。
- **直观解释**：友军二维位置的算术平均点。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"二维 [x, y] 向量。","dimensions":[2],"kind":"vector"},"storm_paths":["derived.friendly_centroid"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["friendly_center_x ="]`
- **实现**：`{"extraction_code":["friendly_center_x ="],"source_locations":[{"line_end":960,"line_start":960,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["friendly_center_x ="]}`
- **源码证据**：derived-tactical-friendly-centroid-code @ ontology/bridge.py:960-960 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.432869a2c9739ef0","relation_type":"aggregated_into","variable_id":"abox.unit.position"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.f6620df914bda5ea","relation_type":"aggregated_into","variable_id":"derived.tactical.formation_distance"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"友军二维位置的算术平均点。","evidence_ids":["derived-tactical-friendly-centroid-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.friendly_centroid`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.friendly_count`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`friendly_count`；zh=友军单位数；en=Friendly Unit Count
- **别名**：友军单位数、Friendly Unit Count、friendly_count
- **简明含义**：友军 ABox 节点数量。
- **直观解释**：友军 ABox 节点数量。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.friendly_count"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["friendly_count = len(friendly_units)"]`
- **实现**：`{"extraction_code":["friendly_count = len(friendly_units)"],"source_locations":[{"line_end":939,"line_start":939,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["friendly_count = len(friendly_units)"]}`
- **源码证据**：derived-tactical-friendly-count-code @ ontology/bridge.py:939-939 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.ac2e061e279a3b4a","relation_type":"aggregated_into","variable_id":"abox.unit.alliance"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.05e2d525dda918a6","relation_type":"aggregated_into","variable_id":"derived.tactical.fire_readiness"},{"relation_id":"rel.aggregated_into.550884e5eb3782f4","relation_type":"aggregated_into","variable_id":"derived.tactical.force_ratio"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"友军 ABox 节点数量。","evidence_ids":["derived-tactical-friendly-count-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.friendly_count`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.health_status`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`health_status`；zh=血量态势；en=Health Status
- **别名**：血量态势、Health Status、health_status
- **简明含义**：敌我平均生命比例的百分比摘要。
- **直观解释**：敌我平均生命比例的百分比摘要。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.health_status"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["Health_Status: Friendly"]`
- **实现**：`{"extraction_code":["Health_Status: Friendly"],"source_locations":[{"line_end":949,"line_start":949,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["Health_Status: Friendly"]}`
- **源码证据**：derived-tactical-health-status-code @ ontology/bridge.py:949-949 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.transformed_to.26de7cfddbed7434","relation_type":"transformed_to","variable_id":"derived.tactical.enemy_avg_hp"},{"relation_id":"rel.transformed_to.daa7dbae7461cec4","relation_type":"transformed_to","variable_id":"derived.tactical.friendly_avg_hp"}]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"敌我平均生命比例的百分比摘要。","evidence_ids":["derived-tactical-health-status-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.health_status`
- **因编码损坏未注入字段**：`[]`

### `derived.tactical.ready_to_fire_count`
- **层级**：category=`derived_tactical_state`；source_layer=`derived_runtime`；derivation=`computed`
- **名称**：canonical=`ready_to_fire_count`；zh=可开火友军数；en=Ready-to-fire Unit Count
- **别名**：可开火友军数、Ready-to-fire Unit Count、ready_to_fire_count
- **简明含义**：weapon_cooldown 等于 0 的友军数量。
- **直观解释**：weapon_cooldown 等于 0 的友军数量。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["tactical_summary.ready_to_fire_count"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["ready_to_fire = sum"]`
- **实现**：`{"extraction_code":["ready_to_fire = sum"],"source_locations":[{"line_end":985,"line_start":985,"path":"ontology/bridge.py","symbol":"BattlefieldGraph.generate_tactical_summary"}],"transformation_formula":["ready_to_fire = sum"]}`
- **源码证据**：derived-tactical-ready-to-fire-count-code @ ontology/bridge.py:985-985 (BattlefieldGraph.generate_tactical_summary; derived_runtime)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.0b6ab10389150863","relation_type":"aggregated_into","variable_id":"abox.unit.weapon_cooldown"},{"relation_id":"rel.aggregated_into.d8cec40154e8c4ae","relation_type":"aggregated_into","variable_id":"abox.unit.alliance"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.7498cd35b96dc33e","relation_type":"aggregated_into","variable_id":"derived.tactical.fire_readiness"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"weapon_cooldown 等于 0 的友军数量。","evidence_ids":["derived-tactical-ready-to-fire-count-code"],"status":"derived_runtime"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'counts_and_aggregation']；data_chains=['abox_to_tactical_state']
- **原始记录引用**：`knowledge/variables/derived.yaml#id=derived.tactical.ready_to_fire_count`
- **因编码损坏未注入字段**：`[]`

## action_schema_and_scheduling：动作计划、校验与调度

### `action.delay_steps`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`delay_steps`；zh=延迟步数；en=Delay Steps
- **别名**：延迟步数、Delay Steps、delay_steps
- **简明含义**：延迟的 STORM environment step 数；缺失为 0，并限制到 0..9。
- **直观解释**：延迟的 STORM environment step 数；缺失为 0，并限制到 0..9。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":9,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.delay_steps"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"environment step"}}`
- **公式/转换**：`["delay_steps=min(9,max(0,int(value or 0)))"]`
- **实现**：`{"extraction_code":["if \"delay_steps\" not in action"],"source_locations":[{"line_end":246,"line_start":246,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["delay_steps=min(9,max(0,int(value or 0)))"]}`
- **源码证据**：action-delay-steps-code @ agents/response_parser.py:246-246 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。", "单位是 environment step，不是秒或 SC2 game loop。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"延迟的 STORM environment step 数；缺失为 0，并限制到 0..9。","evidence_ids":["action-delay-steps-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution', 'environment_and_timing']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.delay_steps`
- **因编码损坏未注入字段**：`[]`

### `action.invalid_actions`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`invalid_actions`；zh=无效动作数；en=Invalid Action Count
- **别名**：无效动作数、Invalid Action Count、invalid_actions
- **简明含义**：语义校验判为无效的动作数。
- **直观解释**：语义校验判为无效的动作数。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.invalid_actions"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"not_applicable"}}`
- **公式/转换**：`["invalid_actions=parser output/validation result"]`
- **实现**：`{"extraction_code":["invalid_actions = 0"],"source_locations":[{"line_end":113,"line_start":113,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["invalid_actions=parser output/validation result"]}`
- **源码证据**：action-invalid-actions-code @ agents/response_parser.py:113-113 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"语义校验判为无效的动作数。","evidence_ids":["action-invalid-actions-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.invalid_actions`
- **因编码损坏未注入字段**：`[]`

### `action.invalid_reason_counts`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`invalid_reason_counts`；zh=无效原因计数；en=Invalid Reason Counts
- **别名**：无效原因计数、Invalid Reason Counts、invalid_reason_counts
- **简明含义**：按原因代码聚合的无效动作数。
- **直观解释**：按原因代码聚合的无效动作数。
- **接口**：`{"data_type":"object","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"dict","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"键值对象。","dimensions":[],"kind":"object"},"storm_paths":["validated_action.invalid_reason_counts"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["invalid_reason_counts=parser output/validation result"]`
- **实现**：`{"extraction_code":["invalid_reason_counts = {}"],"source_locations":[{"line_end":114,"line_start":114,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["invalid_reason_counts=parser output/validation result"]}`
- **源码证据**：action-invalid-reason-counts-code @ agents/response_parser.py:114-114 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"按原因代码聚合的无效动作数。","evidence_ids":["action-invalid-reason-counts-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.invalid_reason_counts`
- **因编码损坏未注入字段**：`[]`

### `action.plan`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`llm_output`；derivation=`validated`
- **名称**：canonical=`plan`；zh=计划文本；en=Plan Text
- **别名**：计划文本、Plan Text、plan
- **简明含义**：LLM 返回并由解析器透传的计划文本。
- **直观解释**：LLM 返回并由解析器透传的计划文本。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.plan"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["plan=parser output/validation result"]`
- **实现**：`{"extraction_code":["json_data.get(\"plan\", \"\")"],"source_locations":[{"line_end":120,"line_start":120,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["plan=parser output/validation result"]}`
- **源码证据**：action-plan-code @ agents/response_parser.py:120-120 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"LLM 返回并由解析器透传的计划文本。","evidence_ids":["action-plan-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.plan`
- **因编码损坏未注入字段**：`[]`

### `action.planned_actions`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`planned_actions`；zh=计划动作数；en=Planned Action Count
- **别名**：计划动作数、Planned Action Count、planned_actions
- **简明含义**：语义过滤前的动作数量。
- **直观解释**：语义过滤前的动作数量。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.planned_actions"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"not_applicable"}}`
- **公式/转换**：`["planned_actions=parser output/validation result"]`
- **实现**：`{"extraction_code":["planned_actions = len"],"source_locations":[{"line_end":103,"line_start":103,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["planned_actions=parser output/validation result"]}`
- **源码证据**：action-planned-actions-code @ agents/response_parser.py:103-103 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"语义过滤前的动作数量。","evidence_ids":["action-planned-actions-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.planned_actions`
- **因编码损坏未注入字段**：`[]`

### `action.priority`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`priority`；zh=优先级；en=Priority
- **别名**：优先级、Priority、priority
- **简明含义**：只允许 high、medium、low。
- **直观解释**：只允许 high、medium、low。
- **接口**：`{"data_type":"string","enum_values":{"description":"当前代码显式使用的枚举值。","status":"known","values":["high","medium","low"]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.priority"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["priority=parser output/validation result"]`
- **实现**：`{"extraction_code":["VALID_PRIORITIES ="],"source_locations":[{"line_end":37,"line_start":37,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["priority=parser output/validation result"]}`
- **源码证据**：action-priority-code @ agents/response_parser.py:37-37 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["action.priority"],"concise_explanation":"priority 更接近设计字段，而不是已生效的调度量。","current_implementation":"常量和文档承诺存在，主路径未见强制校验或排序。","evidence":[{"claim":"允许值常量已声明。","line_end":37,"line_start":37,"path":"agents/response_parser.py","symbol":"VALID_PRIORITIES"},{"claim":"README 声称会校验。","line_end":254,"line_start":254,"path":"agents/README.md","symbol":"ResponseParser semantic validation"}],"expected_or_documented_behavior":"priority 应限制为 high/medium/low 并有明确消费点。","id":"issue.action_priority_not_validated_or_consumed","impact":{"code_or_experiment_risk":"错误值不会被拒绝，调度语义可能被误读。","knowledge_answer_constraint":"不得说 priority 当前会被强制校验或决定执行顺序。"},"issue_type":"documentation_mismatch","limitations":["结论来自静态搜索。"],"phenomenon":"VALID_PRIORITIES 已定义，README 称会校验，但当前验证和执行链未读取 priority。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["输入 priority='urgent'。","跟踪解析结果和执行顺序。"],"success_criteria":"非法值被拒绝且有消费逻辑，或文档明确未使用。"},"severity":"medium","status":"open","title_zh":"priority 声明存在但未校验或调度","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"只允许 high、medium、low。","evidence_ids":["action-priority-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.priority`
- **因编码损坏未注入字段**：`[]`

### `action.reasoning`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`llm_output`；derivation=`validated`
- **名称**：canonical=`reasoning`；zh=战术推理文本；en=Tactical Reasoning
- **别名**：战术推理文本、Tactical Reasoning、reasoning
- **简明含义**：LLM 返回并由解析器透传的推理文本。
- **直观解释**：LLM 返回并由解析器透传的推理文本。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.reasoning"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["reasoning=parser output/validation result"]`
- **实现**：`{"extraction_code":["json_data.get(\"reasoning\", \"\")"],"source_locations":[{"line_end":119,"line_start":119,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["reasoning=parser output/validation result"]}`
- **源码证据**：action-reasoning-code @ agents/response_parser.py:119-119 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"LLM 返回并由解析器透传的推理文本。","evidence_ids":["action-reasoning-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.reasoning`
- **因编码损坏未注入字段**：`[]`

### `action.subtype`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`subtype`；zh=动作子类型；en=Action Subtype
- **别名**：动作子类型、Action Subtype、subtype
- **简明含义**：BUILD 的建筑类型或 TRAIN 的单位类型。
- **直观解释**：BUILD 的建筑类型或 TRAIN 的单位类型。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.subtype"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["subtype=parser output/validation result"]`
- **实现**：`{"extraction_code":["sub_type = action.get(\"subtype\", \"\")"],"source_locations":[{"line_end":545,"line_start":545,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["subtype=parser output/validation result"]}`
- **源码证据**：action-subtype-code @ agents/response_parser.py:545-545 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.mapped_to.7c53c2e292d2c13e","relation_type":"mapped_to","variable_id":"pysc2.build.function_id"},{"relation_id":"rel.mapped_to.bd8599d690aa888a","relation_type":"mapped_to","variable_id":"pysc2.train.function_id"}]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["action.subtype","action.type"],"concise_explanation":"纯 BUILD/TRAIN 若不另给 subtype，不能满足当前执行链。","current_implementation":"Parser 拆分连字符形式；ActionExecutor 读取并要求 subtype。","evidence":[{"claim":"动作说明使用连字符形式。","line_end":38,"line_start":32,"path":"ontology/prompt_template.py","symbol":"ACTION_TYPES"},{"claim":"Parser 将连字符动作拆为 action 与 subtype。","line_end":277,"line_start":269,"path":"agents/response_parser.py","symbol":"ResponseParser._validate_schema"},{"claim":"执行器读取并要求 subtype。","line_end":177,"line_start":176,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute_actions"}],"expected_or_documented_behavior":"提示、Schema、Parser、Executor 应统一一种规范。","id":"issue.build_train_dual_representation","impact":{"code_or_experiment_risk":"模型照 Schema 生成纯动作名时可能失败。","knowledge_answer_constraint":"推荐写 BUILD-Barracks/TRAIN-Marine，或显式提供 subtype；不能说纯动作名一定足够。"},"issue_type":"documentation_mismatch","limitations":["未启动 SC2。"],"phenomenon":"提示示例使用 BUILD-Barracks/TRAIN-Marine，Schema 又列 BUILD/TRAIN；执行器依赖 subtype。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["比较 BUILD、BUILD-Barracks、BUILD+subtype。","对 TRAIN 重复测试。"],"success_criteria":"四处接口使用同一规范并有回归测试。"},"severity":"high","status":"open","title_zh":"BUILD/TRAIN 动作表示形式不一致","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"BUILD 的建筑类型或 TRAIN 的单位类型。","evidence_ids":["action-subtype-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.subtype`
- **因编码损坏未注入字段**：`[]`

### `action.target`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`target`；zh=动作目标；en=Action Target
- **别名**：动作目标、Action Target、target
- **简明含义**：单位 ID、二维坐标或空目标，取决于 target_type。
- **直观解释**：单位 ID、二维坐标或空目标，取决于 target_type。
- **接口**：`{"data_type":"object","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"dict","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"键值对象。","dimensions":[],"kind":"object"},"storm_paths":["validated_action.target"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["target=parser output/validation result"]`
- **实现**：`{"extraction_code":["if \"target\" not in action"],"source_locations":[{"line_end":298,"line_start":298,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["target=parser output/validation result"]}`
- **源码证据**：action-target-code @ agents/response_parser.py:298-298 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.mapped_to.0fab77b818b3a885","relation_type":"mapped_to","variable_id":"pysc2.function.target"}]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["action.target","pysc2.function.target"],"concise_explanation":"越界坐标看似被裁剪，后续仍可能收到原始 target。","current_implementation":"代码计算 x/y 后直接返回 True。","evidence":[{"claim":"局部裁剪值未写回 action['target']。","line_end":525,"line_start":524,"path":"agents/response_parser.py","symbol":"ResponseParser._validate_semantics"}],"expected_or_documented_behavior":"裁剪值应写回 action['target']，或明确拒绝越界动作。","id":"issue.action_coordinate_clip_not_written_back","impact":{"code_or_experiment_risk":"越界参数可能进入转换或执行阶段。","knowledge_answer_constraint":"不得声称 Parser 已把越界坐标修正后传给执行器。"},"issue_type":"confirmed_bug","limitations":["测试未执行。"],"phenomenon":"np.clip 只修改局部 x/y，没有更新动作对象。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["提交 target=[-1,80]。","检查校验后动作对象中的 target。"],"success_criteria":"通过校验的动作实际携带 [0,63]，或被明确拒绝。"},"severity":"high","status":"open","title_zh":"坐标裁剪结果未写回 action.target","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"单位 ID、二维坐标或空目标，取决于 target_type。","evidence_ids":["action-target-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.target`
- **因编码损坏未注入字段**：`[]`

### `action.target_type`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`target_type`；zh=目标类型；en=Target Type
- **别名**：目标类型、Target Type、target_type
- **简明含义**：只允许 unit、pos、none。
- **直观解释**：只允许 unit、pos、none。
- **接口**：`{"data_type":"string","enum_values":{"description":"当前代码显式使用的枚举值。","status":"known","values":["unit","pos","none"]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.target_type"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["target_type=parser output/validation result"]`
- **实现**：`{"extraction_code":["VALID_TARGET_TYPES ="],"source_locations":[{"line_end":34,"line_start":34,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["target_type=parser output/validation result"]}`
- **源码证据**：action-target-type-code @ agents/response_parser.py:34-34 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.mapped_to.fb03e8189ac3bcad","relation_type":"mapped_to","variable_id":"pysc2.function.target"}]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"只允许 unit、pos、none。","evidence_ids":["action-target-type-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.target_type`
- **因编码损坏未注入字段**：`[]`

### `action.type`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`action`；zh=动作类型；en=Action Type
- **别名**：动作类型、Action Type、action
- **简明含义**：只允许 MOVE、ATTACK、BUILD、TRAIN。
- **直观解释**：只允许 MOVE、ATTACK、BUILD、TRAIN。
- **接口**：`{"data_type":"string","enum_values":{"description":"当前代码显式使用的枚举值。","status":"known","values":["MOVE","ATTACK","BUILD","TRAIN"]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["validated_action.action"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["action=parser output/validation result"]`
- **实现**：`{"extraction_code":["VALID_ACTIONS = {"],"source_locations":[{"line_end":26,"line_start":26,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["action=parser output/validation result"]}`
- **源码证据**：action-type-code @ agents/response_parser.py:26-26 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.mapped_to.5e6688ba4a1f0835","relation_type":"mapped_to","variable_id":"pysc2.train.function_id"},{"relation_id":"rel.mapped_to.7331879112b7e344","relation_type":"mapped_to","variable_id":"pysc2.move.function_id"},{"relation_id":"rel.mapped_to.a77000534c9b4760","relation_type":"mapped_to","variable_id":"pysc2.attack.function_id"},{"relation_id":"rel.mapped_to.cd3b05035cbc73d2","relation_type":"mapped_to","variable_id":"pysc2.build.function_id"}]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["action.subtype","action.type"],"concise_explanation":"纯 BUILD/TRAIN 若不另给 subtype，不能满足当前执行链。","current_implementation":"Parser 拆分连字符形式；ActionExecutor 读取并要求 subtype。","evidence":[{"claim":"动作说明使用连字符形式。","line_end":38,"line_start":32,"path":"ontology/prompt_template.py","symbol":"ACTION_TYPES"},{"claim":"Parser 将连字符动作拆为 action 与 subtype。","line_end":277,"line_start":269,"path":"agents/response_parser.py","symbol":"ResponseParser._validate_schema"},{"claim":"执行器读取并要求 subtype。","line_end":177,"line_start":176,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute_actions"}],"expected_or_documented_behavior":"提示、Schema、Parser、Executor 应统一一种规范。","id":"issue.build_train_dual_representation","impact":{"code_or_experiment_risk":"模型照 Schema 生成纯动作名时可能失败。","knowledge_answer_constraint":"推荐写 BUILD-Barracks/TRAIN-Marine，或显式提供 subtype；不能说纯动作名一定足够。"},"issue_type":"documentation_mismatch","limitations":["未启动 SC2。"],"phenomenon":"提示示例使用 BUILD-Barracks/TRAIN-Marine，Schema 又列 BUILD/TRAIN；执行器依赖 subtype。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["比较 BUILD、BUILD-Barracks、BUILD+subtype。","对 TRAIN 重复测试。"],"success_criteria":"四处接口使用同一规范并有回归测试。"},"severity":"high","status":"open","title_zh":"BUILD/TRAIN 动作表示形式不一致","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"只允许 MOVE、ATTACK、BUILD、TRAIN。","evidence_ids":["action-type-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.type`
- **因编码损坏未注入字段**：`[]`

### `action.units`
- **层级**：category=`action_schema_and_scheduling`；source_layer=`validated_action`；derivation=`validated`
- **名称**：canonical=`units`；zh=执行单位列表；en=Acting Units
- **别名**：执行单位列表、Acting Units、units
- **简明含义**：动作涉及的 ABox 实例 ID 列表。
- **直观解释**：动作涉及的 ABox 实例 ID 列表。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["validated_action.units"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["units=parser output/validation result"]`
- **实现**：`{"extraction_code":["if \"units\" not in action"],"source_locations":[{"line_end":227,"line_start":227,"path":"agents/response_parser.py","symbol":"ResponseParser.parse / validation"}],"transformation_formula":["units=parser output/validation result"]}`
- **源码证据**：action-units-code @ agents/response_parser.py:227-227 (ResponseParser.parse / validation; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.mapped_to.2a0107d045b91be1","relation_type":"mapped_to","variable_id":"pysc2.function.unit_tags"}]`
- **限制**：`["这是 STORM 动作约定，不是 PySC2 完整 ActionSpec。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"动作涉及的 ABox 实例 ID 列表。","evidence_ids":["action-units-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call', 'swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=action.units`
- **因编码损坏未注入字段**：`[]`

## pysc2_function_call：PySC2 FunctionCall 参数

### `pysc2.attack.function_id`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`function_id`；zh=ATTACK 函数编号；en=ATTACK Function ID
- **别名**：ATTACK 函数编号、ATTACK Function ID、function_id
- **简明含义**：ATTACK 使用编号 3。
- **直观解释**：ATTACK 使用编号 3。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["FunctionCall.function"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["ATTACK 使用编号 3。"]`
- **实现**：`{"extraction_code":["3, arguments=args, raw=True"],"source_locations":[{"line_end":162,"line_start":162,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["ATTACK 使用编号 3。"]}`
- **源码证据**：pysc2-attack-function-id-code @ agents/action_executor.py:162-162 (ActionExecutor.execute; code_reality)
- **直接上游**：`[{"relation_id":"rel.mapped_to.a77000534c9b4760","relation_type":"mapped_to","variable_id":"action.type"}]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-attack-function-id-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["pysc2.attack.function_id","pysc2.build.function_id","pysc2.move.function_id","pysc2.no_op.function_id","pysc2.train.function_id"],"concise_explanation":"静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。","current_implementation":"执行器直接用常量构造 FunctionCall。","evidence":[{"claim":"BUILD/TRAIN 函数编号以常量形式硬编码。","line_end":15,"line_start":7,"path":"agents/action_executor.py","symbol":"BUILD_CALLS/TRAIN_CALLS"},{"claim":"NO_OP、MOVE、ATTACK 调用使用数值 ID 0、13、3。","line_end":162,"line_start":139,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute_actions"}],"expected_or_documented_behavior":"应从当前 PySC2/SC2 ActionSpec 核对 ID、名称和参数签名。","id":"issue.function_ids_require_runtime_actionspec_check","impact":{"code_or_experiment_risk":"版本或动作可用性差异可能导致无效调用。","knowledge_answer_constraint":"回答 ID 时须标注为当前源码硬编码值、尚未运行核验。"},"issue_type":"needs_runtime_test","limitations":["本步骤未启动 SC2。"],"phenomenon":"ActionExecutor 硬编码 NO_OP/MOVE/ATTACK/BUILD/TRAIN 函数编号。","recommended_verification":{"execution_status":"not_executed","method":"runtime_sc2_test","steps":["启动 Raw API 环境。","读取 ActionSpec。","逐项比对并做最小冒烟测试。"],"success_criteria":"所有 ID 与参数签名匹配且调用可被环境接受。"},"severity":"high","status":"open","title_zh":"硬编码 FunctionCall ID 尚未核验","truth_status":"needs_verification"}]}`
- **事实边界**：`{"code_reality":[{"claim":"ATTACK 使用编号 3。","evidence_ids":["pysc2-attack-function-id-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['combat_and_weapons', 'actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.attack.function_id`
- **因编码损坏未注入字段**：`[]`

### `pysc2.build.function_id`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`function_id`；zh=BUILD 函数编号；en=BUILD Function ID
- **别名**：BUILD 函数编号、BUILD Function ID、function_id
- **简明含义**：BUILD 按 subtype 查询 BUILD_CALLS。
- **直观解释**：BUILD 按 subtype 查询 BUILD_CALLS。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["FunctionCall.function"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["BUILD 按 subtype 查询 BUILD_CALLS。"]`
- **实现**：`{"extraction_code":["BUILD_CALLS[subtype]"],"source_locations":[{"line_end":210,"line_start":210,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["BUILD 按 subtype 查询 BUILD_CALLS。"]}`
- **源码证据**：pysc2-build-function-id-code @ agents/action_executor.py:210-210 (ActionExecutor.execute; code_reality)
- **直接上游**：`[{"relation_id":"rel.mapped_to.7c53c2e292d2c13e","relation_type":"mapped_to","variable_id":"action.subtype"},{"relation_id":"rel.mapped_to.cd3b05035cbc73d2","relation_type":"mapped_to","variable_id":"action.type"}]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-build-function-id-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["pysc2.attack.function_id","pysc2.build.function_id","pysc2.move.function_id","pysc2.no_op.function_id","pysc2.train.function_id"],"concise_explanation":"静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。","current_implementation":"执行器直接用常量构造 FunctionCall。","evidence":[{"claim":"BUILD/TRAIN 函数编号以常量形式硬编码。","line_end":15,"line_start":7,"path":"agents/action_executor.py","symbol":"BUILD_CALLS/TRAIN_CALLS"},{"claim":"NO_OP、MOVE、ATTACK 调用使用数值 ID 0、13、3。","line_end":162,"line_start":139,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute_actions"}],"expected_or_documented_behavior":"应从当前 PySC2/SC2 ActionSpec 核对 ID、名称和参数签名。","id":"issue.function_ids_require_runtime_actionspec_check","impact":{"code_or_experiment_risk":"版本或动作可用性差异可能导致无效调用。","knowledge_answer_constraint":"回答 ID 时须标注为当前源码硬编码值、尚未运行核验。"},"issue_type":"needs_runtime_test","limitations":["本步骤未启动 SC2。"],"phenomenon":"ActionExecutor 硬编码 NO_OP/MOVE/ATTACK/BUILD/TRAIN 函数编号。","recommended_verification":{"execution_status":"not_executed","method":"runtime_sc2_test","steps":["启动 Raw API 环境。","读取 ActionSpec。","逐项比对并做最小冒烟测试。"],"success_criteria":"所有 ID 与参数签名匹配且调用可被环境接受。"},"severity":"high","status":"open","title_zh":"硬编码 FunctionCall ID 尚未核验","truth_status":"needs_verification"}]}`
- **事实边界**：`{"code_reality":[{"claim":"BUILD 按 subtype 查询 BUILD_CALLS。","evidence_ids":["pysc2-build-function-id-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.build.function_id`
- **因编码损坏未注入字段**：`[]`

### `pysc2.function.queued`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`queued`；zh=排队标志；en=Queued Flag
- **别名**：排队标志、Queued Flag、queued
- **简明含义**：MOVE/ATTACK/BUILD 当前均传 [0]。
- **直观解释**：MOVE/ATTACK/BUILD 当前均传 [0]。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["FunctionCall.function"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["MOVE/ATTACK/BUILD 当前均传 [0]。"]`
- **实现**：`{"extraction_code":["args = [[0], action[\"units\"], action[\"target\"]]"],"source_locations":[{"line_end":160,"line_start":160,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["MOVE/ATTACK/BUILD 当前均传 [0]。"]}`
- **源码证据**：pysc2-function-queued-code @ agents/action_executor.py:160-160 (ActionExecutor.execute; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-function-queued-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"MOVE/ATTACK/BUILD 当前均传 [0]。","evidence_ids":["pysc2-function-queued-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.function.queued`
- **因编码损坏未注入字段**：`[]`

### `pysc2.function.raw_flag`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`raw`；zh=Raw FunctionCall 标志；en=Raw FunctionCall Flag
- **别名**：Raw FunctionCall 标志、Raw FunctionCall Flag、raw
- **简明含义**：FunctionCall 使用 Raw 参数。
- **直观解释**：FunctionCall 使用 Raw 参数。
- **接口**：`{"data_type":"boolean","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"bool","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["FunctionCall.raw"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["FunctionCall 使用 Raw 参数。"]`
- **实现**：`{"extraction_code":["raw=True"],"source_locations":[{"line_end":139,"line_start":139,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["FunctionCall 使用 Raw 参数。"]}`
- **源码证据**：pysc2-function-raw-flag-code @ agents/action_executor.py:139-139 (ActionExecutor.execute; code_reality)
- **直接上游**：`[{"relation_id":"rel.mapped_to.14c81e1ba7855c8e","relation_type":"mapped_to","variable_id":"environment.use_raw_actions"}]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-function-raw-flag-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"FunctionCall 使用 Raw 参数。","evidence_ids":["pysc2-function-raw-flag-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.function.raw_flag`
- **因编码损坏未注入字段**：`[]`

### `pysc2.function.target`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`target`；zh=目标参数；en=Target Argument
- **别名**：目标参数、Target Argument、target
- **简明含义**：MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。
- **直观解释**：MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。
- **接口**：`{"data_type":"object","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"dict","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"键值对象。","dimensions":[],"kind":"object"},"storm_paths":["FunctionCall.arguments.target"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。"]`
- **实现**：`{"extraction_code":["action[\"target\"]"],"source_locations":[{"line_end":160,"line_start":160,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。"]}`
- **源码证据**：pysc2-function-target-code @ agents/action_executor.py:160-160 (ActionExecutor.execute; code_reality)
- **直接上游**：`[{"relation_id":"rel.mapped_to.0fab77b818b3a885","relation_type":"mapped_to","variable_id":"action.target"},{"relation_id":"rel.mapped_to.fb03e8189ac3bcad","relation_type":"mapped_to","variable_id":"action.target_type"}]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-function-target-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["action.target","pysc2.function.target"],"concise_explanation":"越界坐标看似被裁剪，后续仍可能收到原始 target。","current_implementation":"代码计算 x/y 后直接返回 True。","evidence":[{"claim":"局部裁剪值未写回 action['target']。","line_end":525,"line_start":524,"path":"agents/response_parser.py","symbol":"ResponseParser._validate_semantics"}],"expected_or_documented_behavior":"裁剪值应写回 action['target']，或明确拒绝越界动作。","id":"issue.action_coordinate_clip_not_written_back","impact":{"code_or_experiment_risk":"越界参数可能进入转换或执行阶段。","knowledge_answer_constraint":"不得声称 Parser 已把越界坐标修正后传给执行器。"},"issue_type":"confirmed_bug","limitations":["测试未执行。"],"phenomenon":"np.clip 只修改局部 x/y，没有更新动作对象。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["提交 target=[-1,80]。","检查校验后动作对象中的 target。"],"success_criteria":"通过校验的动作实际携带 [0,63]，或被明确拒绝。"},"severity":"high","status":"open","title_zh":"坐标裁剪结果未写回 action.target","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"MOVE/BUILD 使用坐标；ATTACK 可使用目标 tag。","evidence_ids":["pysc2-function-target-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.function.target`
- **因编码损坏未注入字段**：`[]`

### `pysc2.function.unit_tags`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`unit_tags`；zh=单位标签参数；en=Unit Tags Argument
- **别名**：单位标签参数、Unit Tags Argument、unit_tags
- **简明含义**：经验证和映射的 tag 列表。
- **直观解释**：经验证和映射的 tag 列表。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["FunctionCall.arguments.unit_tags"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["经验证和映射的 tag 列表。"]`
- **实现**：`{"extraction_code":["action[\"units\"]"],"source_locations":[{"line_end":160,"line_start":160,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["经验证和映射的 tag 列表。"]}`
- **源码证据**：pysc2-function-unit-tags-code @ agents/action_executor.py:160-160 (ActionExecutor.execute; code_reality)
- **直接上游**：`[{"relation_id":"rel.mapped_to.2a0107d045b91be1","relation_type":"mapped_to","variable_id":"action.units"}]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-function-unit-tags-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"经验证和映射的 tag 列表。","evidence_ids":["pysc2-function-unit-tags-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['identity_and_affiliation', 'actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.function.unit_tags`
- **因编码损坏未注入字段**：`[]`

### `pysc2.move.function_id`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`function_id`；zh=MOVE 函数编号；en=MOVE Function ID
- **别名**：MOVE 函数编号、MOVE Function ID、function_id
- **简明含义**：MOVE 使用编号 13。
- **直观解释**：MOVE 使用编号 13。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["FunctionCall.function"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["MOVE 使用编号 13。"]`
- **实现**：`{"extraction_code":["13, arguments=args, raw=True"],"source_locations":[{"line_end":162,"line_start":162,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["MOVE 使用编号 13。"]}`
- **源码证据**：pysc2-move-function-id-code @ agents/action_executor.py:162-162 (ActionExecutor.execute; code_reality)
- **直接上游**：`[{"relation_id":"rel.mapped_to.7331879112b7e344","relation_type":"mapped_to","variable_id":"action.type"}]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-move-function-id-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["pysc2.attack.function_id","pysc2.build.function_id","pysc2.move.function_id","pysc2.no_op.function_id","pysc2.train.function_id"],"concise_explanation":"静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。","current_implementation":"执行器直接用常量构造 FunctionCall。","evidence":[{"claim":"BUILD/TRAIN 函数编号以常量形式硬编码。","line_end":15,"line_start":7,"path":"agents/action_executor.py","symbol":"BUILD_CALLS/TRAIN_CALLS"},{"claim":"NO_OP、MOVE、ATTACK 调用使用数值 ID 0、13、3。","line_end":162,"line_start":139,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute_actions"}],"expected_or_documented_behavior":"应从当前 PySC2/SC2 ActionSpec 核对 ID、名称和参数签名。","id":"issue.function_ids_require_runtime_actionspec_check","impact":{"code_or_experiment_risk":"版本或动作可用性差异可能导致无效调用。","knowledge_answer_constraint":"回答 ID 时须标注为当前源码硬编码值、尚未运行核验。"},"issue_type":"needs_runtime_test","limitations":["本步骤未启动 SC2。"],"phenomenon":"ActionExecutor 硬编码 NO_OP/MOVE/ATTACK/BUILD/TRAIN 函数编号。","recommended_verification":{"execution_status":"not_executed","method":"runtime_sc2_test","steps":["启动 Raw API 环境。","读取 ActionSpec。","逐项比对并做最小冒烟测试。"],"success_criteria":"所有 ID 与参数签名匹配且调用可被环境接受。"},"severity":"high","status":"open","title_zh":"硬编码 FunctionCall ID 尚未核验","truth_status":"needs_verification"}]}`
- **事实边界**：`{"code_reality":[{"claim":"MOVE 使用编号 13。","evidence_ids":["pysc2-move-function-id-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.move.function_id`
- **因编码损坏未注入字段**：`[]`

### `pysc2.no_op.function_id`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`function_id`；zh=No-op 函数编号；en=No-op Function ID
- **别名**：No-op 函数编号、No-op Function ID、function_id
- **简明含义**：空动作返回编号 0。
- **直观解释**：空动作返回编号 0。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["FunctionCall.function"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["空动作返回编号 0。"]`
- **实现**：`{"extraction_code":["init_with_validation(0, arguments=[], raw=True)"],"source_locations":[{"line_end":139,"line_start":139,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["空动作返回编号 0。"]}`
- **源码证据**：pysc2-no-op-function-id-code @ agents/action_executor.py:139-139 (ActionExecutor.execute; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-no-op-function-id-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["pysc2.attack.function_id","pysc2.build.function_id","pysc2.move.function_id","pysc2.no_op.function_id","pysc2.train.function_id"],"concise_explanation":"静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。","current_implementation":"执行器直接用常量构造 FunctionCall。","evidence":[{"claim":"BUILD/TRAIN 函数编号以常量形式硬编码。","line_end":15,"line_start":7,"path":"agents/action_executor.py","symbol":"BUILD_CALLS/TRAIN_CALLS"},{"claim":"NO_OP、MOVE、ATTACK 调用使用数值 ID 0、13、3。","line_end":162,"line_start":139,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute_actions"}],"expected_or_documented_behavior":"应从当前 PySC2/SC2 ActionSpec 核对 ID、名称和参数签名。","id":"issue.function_ids_require_runtime_actionspec_check","impact":{"code_or_experiment_risk":"版本或动作可用性差异可能导致无效调用。","knowledge_answer_constraint":"回答 ID 时须标注为当前源码硬编码值、尚未运行核验。"},"issue_type":"needs_runtime_test","limitations":["本步骤未启动 SC2。"],"phenomenon":"ActionExecutor 硬编码 NO_OP/MOVE/ATTACK/BUILD/TRAIN 函数编号。","recommended_verification":{"execution_status":"not_executed","method":"runtime_sc2_test","steps":["启动 Raw API 环境。","读取 ActionSpec。","逐项比对并做最小冒烟测试。"],"success_criteria":"所有 ID 与参数签名匹配且调用可被环境接受。"},"severity":"high","status":"open","title_zh":"硬编码 FunctionCall ID 尚未核验","truth_status":"needs_verification"}]}`
- **事实边界**：`{"code_reality":[{"claim":"空动作返回编号 0。","evidence_ids":["pysc2-no-op-function-id-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.no_op.function_id`
- **因编码损坏未注入字段**：`[]`

### `pysc2.train.function_id`
- **层级**：category=`pysc2_function_call`；source_layer=`executor_mapping`；derivation=`validated`
- **名称**：canonical=`function_id`；zh=TRAIN 函数编号；en=TRAIN Function ID
- **别名**：TRAIN 函数编号、TRAIN Function ID、function_id
- **简明含义**：TRAIN 按 subtype 查询 TRAIN_CALLS。
- **直观解释**：TRAIN 按 subtype 查询 TRAIN_CALLS。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["FunctionCall.function"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["TRAIN 按 subtype 查询 TRAIN_CALLS。"]`
- **实现**：`{"extraction_code":["TRAIN_CALLS[subtype]"],"source_locations":[{"line_end":236,"line_start":236,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute"}],"transformation_formula":["TRAIN 按 subtype 查询 TRAIN_CALLS。"]}`
- **源码证据**：pysc2-train-function-id-code @ agents/action_executor.py:236-236 (ActionExecutor.execute; code_reality)
- **直接上游**：`[{"relation_id":"rel.mapped_to.5e6688ba4a1f0835","relation_type":"mapped_to","variable_id":"action.type"},{"relation_id":"rel.mapped_to.bd8599d690aa888a","relation_type":"mapped_to","variable_id":"action.subtype"}]`
- **直接下游**：`[]`
- **限制**：`["硬编码编号和参数顺序尚未对安装中的 PySC2 ActionSpec 做运行时核验。"]`
- **已知问题**：`{"record_level":[{"description":"FunctionCall 编号可能受 PySC2 版本和动作表影响。","evidence_ids":["pysc2-train-function-id-code"],"id":"pysc2_function_id_version","status":"needs_verification"}],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["pysc2.attack.function_id","pysc2.build.function_id","pysc2.move.function_id","pysc2.no_op.function_id","pysc2.train.function_id"],"concise_explanation":"静态代码只能确认这些值被使用，不能证明与当前 ActionSpec 一致。","current_implementation":"执行器直接用常量构造 FunctionCall。","evidence":[{"claim":"BUILD/TRAIN 函数编号以常量形式硬编码。","line_end":15,"line_start":7,"path":"agents/action_executor.py","symbol":"BUILD_CALLS/TRAIN_CALLS"},{"claim":"NO_OP、MOVE、ATTACK 调用使用数值 ID 0、13、3。","line_end":162,"line_start":139,"path":"agents/action_executor.py","symbol":"ActionExecutor.execute_actions"}],"expected_or_documented_behavior":"应从当前 PySC2/SC2 ActionSpec 核对 ID、名称和参数签名。","id":"issue.function_ids_require_runtime_actionspec_check","impact":{"code_or_experiment_risk":"版本或动作可用性差异可能导致无效调用。","knowledge_answer_constraint":"回答 ID 时须标注为当前源码硬编码值、尚未运行核验。"},"issue_type":"needs_runtime_test","limitations":["本步骤未启动 SC2。"],"phenomenon":"ActionExecutor 硬编码 NO_OP/MOVE/ATTACK/BUILD/TRAIN 函数编号。","recommended_verification":{"execution_status":"not_executed","method":"runtime_sc2_test","steps":["启动 Raw API 环境。","读取 ActionSpec。","逐项比对并做最小冒烟测试。"],"success_criteria":"所有 ID 与参数签名匹配且调用可被环境接受。"},"severity":"high","status":"open","title_zh":"硬编码 FunctionCall ID 尚未核验","truth_status":"needs_verification"}]}`
- **事实边界**：`{"code_reality":[{"claim":"TRAIN 按 subtype 查询 TRAIN_CALLS。","evidence_ids":["pysc2-train-function-id-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution']；data_chains=['llm_action_to_function_call']
- **原始记录引用**：`knowledge/variables/actions.yaml#id=pysc2.train.function_id`
- **因编码损坏未注入字段**：`[]`

## swm：SWM 预测与重验证

### `swm.candidate_index`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`candidate_index`；zh=候选动作编号；en=Candidate Index
- **别名**：候选动作编号、Candidate Index、candidate_index
- **简明含义**：多候选预测的零基编号。
- **直观解释**：多候选预测的零基编号。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["swm.candidate_index"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["candidate_index=SWM input/output field"]`
- **实现**：`{"extraction_code":["result[\"candidate_index\"] = i"],"source_locations":[{"line_end":189,"line_start":189,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["candidate_index=SWM input/output field"]}`
- **源码证据**：swm-candidate-index-code @ ontology/swm_predictor.py:189-189 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[{"relation_id":"rel.stored_as.a6ab4e0be2bdd05e","relation_type":"stored_as","variable_id":"swm.predictions"}]`
- **直接下游**：`[]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"多候选预测的零基编号。","evidence_ids":["swm-candidate-index-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.candidate_index`
- **因编码损坏未注入字段**：`[]`

### `swm.confidence`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`confidence`；zh=预测置信度；en=Prediction Confidence
- **别名**：预测置信度、Prediction Confidence、confidence
- **简明含义**：SWM 返回的置信度。
- **直观解释**：SWM 返回的置信度。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["swm.confidence"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["confidence=SWM input/output field"]`
- **实现**：`{"extraction_code":["\"confidence\": 0.75"],"source_locations":[{"line_end":119,"line_start":119,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["confidence=SWM input/output field"]}`
- **源码证据**：swm-confidence-code @ ontology/swm_predictor.py:119-119 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["swm.confidence"],"concise_explanation":"该值当前是预测元数据，不是自动决定采用预测的开关。","current_implementation":"校验器规范化 confidence；非数值字符串还可能触发 float 异常。","evidence":[{"claim":"confidence 有默认和裁剪，但直接 float 转换。","line_end":427,"line_start":413,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor._validate_prediction"},{"claim":"RawAgent 在成功日志中读取该值。","line_end":731,"line_start":731,"path":"agents/raw_agent.py","symbol":"RawAgent._run_swm_prediction"}],"expected_or_documented_behavior":"若需要门控，应定义阈值、分支和日志。","id":"issue.swm_confidence_not_a_gate","impact":{"code_or_experiment_risk":"可能被误当成安全门控；格式漂移也可能引发转换异常。","knowledge_answer_constraint":"只能说它被默认、裁剪、记录和传递；不得声称存在采用阈值。"},"issue_type":"implementation_quirk","limitations":["未调用外部 SWM。"],"phenomenon":"confidence 缺失时默认 0.5 并裁剪到 0..1；RawAgent 记录它，但未见阈值分支。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["测试 0、0.5、1 和非数值输入。","跟踪后续路径是否因阈值改变。"],"success_criteria":"门控可测试或文档明确仅为元数据；非法类型被结构化处理。"},"severity":"medium","status":"open","title_zh":"SWM confidence 被规范化但不是硬阈值门控","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"SWM 返回的置信度。","evidence_ids":["swm-confidence-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.confidence`
- **因编码损坏未注入字段**：`[]`

### `swm.input.abox_state`
- **层级**：category=`swm`；source_layer=`abox_runtime`；derivation=`direct_read`
- **名称**：canonical=`abox_state`；zh=ABox 状态文本；en=ABox State Text
- **别名**：ABox 状态文本、ABox State Text、abox_state
- **简明含义**：当前 ABox 序列化文本输入。
- **直观解释**：当前 ABox 序列化文本输入。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["swm.input.abox_state"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["abox_state=SWM input/output field"]`
- **实现**：`{"extraction_code":["abox_state: str"],"source_locations":[{"line_end":95,"line_start":95,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["abox_state=SWM input/output field"]}`
- **源码证据**：swm-input-abox-state-code @ ontology/swm_predictor.py:95-95 (SWMPredictor.predict / compute_prediction_error; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.predicts.a0ea292153fc8012","relation_type":"predicts","variable_id":"swm.raw_response"}]`
- **限制**：`["输入格式由当前 STORM 约定；来源层表示输入在进入 SWM 前的事实边界。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前 ABox 序列化文本输入。","evidence_ids":["swm-input-abox-state-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph', 'swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.input.abox_state`
- **因编码损坏未注入字段**：`[]`

### `swm.input.planned_actions`
- **层级**：category=`swm`；source_layer=`validated_action`；derivation=`direct_read`
- **名称**：canonical=`planned_actions`；zh=候选动作；en=Planned Actions
- **别名**：候选动作、Planned Actions、planned_actions
- **简明含义**：待预测的候选动作列表。
- **直观解释**：待预测的候选动作列表。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["swm.input.planned_actions"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["planned_actions=SWM input/output field"]`
- **实现**：`{"extraction_code":["planned_actions: List"],"source_locations":[{"line_end":96,"line_start":96,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["planned_actions=SWM input/output field"]}`
- **源码证据**：swm-input-planned-actions-code @ ontology/swm_predictor.py:96-96 (SWMPredictor.predict / compute_prediction_error; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.predicts.16708c888f83f500","relation_type":"predicts","variable_id":"swm.raw_response"}]`
- **限制**：`["输入格式由当前 STORM 约定；来源层表示输入在进入 SWM 前的事实边界。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"待预测的候选动作列表。","evidence_ids":["swm-input-planned-actions-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution', 'swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.input.planned_actions`
- **因编码损坏未注入字段**：`[]`

### `swm.predicted_relations`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`predicted_relations`；zh=预测关系；en=Predicted Relations
- **别名**：预测关系、Predicted Relations、predicted_relations
- **简明含义**：预测步内的关系列表。
- **直观解释**：预测步内的关系列表。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["swm.predicted_relations"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["predicted_relations=SWM input/output field"]`
- **实现**：`{"extraction_code":["\"predicted_relations\":"],"source_locations":[{"line_end":116,"line_start":116,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["predicted_relations=SWM input/output field"]}`
- **源码证据**：swm-predicted-relations-code @ ontology/swm_predictor.py:116-116 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[{"relation_id":"rel.stored_as.f936b1133a5c4dee","relation_type":"stored_as","variable_id":"swm.predictions"}]`
- **直接下游**：`[{"relation_id":"rel.evaluated_by.693cf5dbfed13d74","relation_type":"evaluated_by","variable_id":"metric.swm.relation_accuracy"}]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"预测步内的关系列表。","evidence_ids":["swm-predicted-relations-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph', 'swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.predicted_relations`
- **因编码损坏未注入字段**：`[]`

### `swm.predicted_unit_states`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`predicted_unit_states`；zh=预测单位状态；en=Predicted Unit States
- **别名**：预测单位状态、Predicted Unit States、predicted_unit_states
- **简明含义**：预测步内的单位状态变化列表。
- **直观解释**：预测步内的单位状态变化列表。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["swm.predicted_unit_states"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["predicted_unit_states=SWM input/output field"]`
- **实现**：`{"extraction_code":["\"predicted_unit_states\":"],"source_locations":[{"line_end":115,"line_start":115,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["predicted_unit_states=SWM input/output field"]}`
- **源码证据**：swm-predicted-unit-states-code @ ontology/swm_predictor.py:115-115 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[{"relation_id":"rel.stored_as.f017b608b692f609","relation_type":"stored_as","variable_id":"swm.predictions"}]`
- **直接下游**：`[{"relation_id":"rel.evaluated_by.0c2d98ef632a14eb","relation_type":"evaluated_by","variable_id":"metric.swm.health_rmse"},{"relation_id":"rel.evaluated_by.4ae4484eb47be5c4","relation_type":"evaluated_by","variable_id":"metric.swm.position_rmse"},{"relation_id":"rel.stored_as.0f3958f73bf09086","relation_type":"stored_as","variable_id":"swm.unit.health_delta"},{"relation_id":"rel.stored_as.b89e4662d219ae11","relation_type":"stored_as","variable_id":"swm.unit.position_delta"}]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"预测步内的单位状态变化列表。","evidence_ids":["swm-predicted-unit-states-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.predicted_unit_states`
- **因编码损坏未注入字段**：`[]`

### `swm.prediction.step`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`step`；zh=预测相对步；en=Prediction Step
- **别名**：预测相对步、Prediction Step、step
- **简明含义**：预测项相对当前状态的步号。
- **直观解释**：预测项相对当前状态的步号。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["swm.prediction.step"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["step=SWM input/output field"]`
- **实现**：`{"extraction_code":["\"step\": 1"],"source_locations":[{"line_end":114,"line_start":114,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["step=SWM input/output field"]}`
- **源码证据**：swm-prediction-step-code @ ontology/swm_predictor.py:114-114 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[{"relation_id":"rel.stored_as.6dca7aa166697e8e","relation_type":"stored_as","variable_id":"swm.predictions"}]`
- **直接下游**：`[]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"预测项相对当前状态的步号。","evidence_ids":["swm-prediction-step-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction', 'environment_and_timing']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.prediction.step`
- **因编码损坏未注入字段**：`[]`

### `swm.prediction_steps`
- **层级**：category=`swm`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`prediction_steps`；zh=预测步数；en=Prediction Steps
- **别名**：预测步数、Prediction Steps、prediction_steps
- **简明含义**：预测未来多少个 STORM 步。
- **直观解释**：预测未来多少个 STORM 步。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["swm.prediction_steps"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["prediction_steps=SWM input/output field"]`
- **实现**：`{"extraction_code":["n_steps = prediction_steps or self.prediction_steps"],"source_locations":[{"line_end":129,"line_start":129,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["prediction_steps=SWM input/output field"]}`
- **源码证据**：swm-prediction-steps-code @ ontology/swm_predictor.py:129-129 (SWMPredictor.predict / compute_prediction_error; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.predicts.590e39747a7e5630","relation_type":"predicts","variable_id":"swm.raw_response"}]`
- **限制**：`["输入格式由当前 STORM 约定；来源层表示输入在进入 SWM 前的事实边界。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"预测未来多少个 STORM 步。","evidence_ids":["swm-prediction-steps-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction', 'environment_and_timing']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.prediction_steps`
- **因编码损坏未注入字段**：`[]`

### `swm.predictions`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`predictions`；zh=逐步预测列表；en=Step Predictions
- **别名**：逐步预测列表、Step Predictions、predictions
- **简明含义**：未来各步预测对象列表。
- **直观解释**：未来各步预测对象列表。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"可变长度序列。","dimensions":[],"kind":"sequence"},"storm_paths":["swm.predictions"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["predictions=SWM input/output field"]`
- **实现**：`{"extraction_code":["\"predictions\": ["],"source_locations":[{"line_end":112,"line_start":112,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["predictions=SWM input/output field"]}`
- **源码证据**：swm-predictions-code @ ontology/swm_predictor.py:112-112 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.stored_as.6dca7aa166697e8e","relation_type":"stored_as","variable_id":"swm.prediction.step"},{"relation_id":"rel.stored_as.a6ab4e0be2bdd05e","relation_type":"stored_as","variable_id":"swm.candidate_index"},{"relation_id":"rel.stored_as.f017b608b692f609","relation_type":"stored_as","variable_id":"swm.predicted_unit_states"},{"relation_id":"rel.stored_as.f936b1133a5c4dee","relation_type":"stored_as","variable_id":"swm.predicted_relations"}]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"未来各步预测对象列表。","evidence_ids":["swm-predictions-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.predictions`
- **因编码损坏未注入字段**：`[]`

### `swm.raw_response`
- **层级**：category=`swm`；source_layer=`llm_output`；derivation=`predicted`
- **名称**：canonical=`raw_response`；zh=预测原始响应；en=Prediction Raw Response
- **别名**：预测原始响应、Prediction Raw Response、raw_response
- **简明含义**：预测模型原始返回文本。
- **直观解释**：预测模型原始返回文本。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["swm.raw_response"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["raw_response=SWM input/output field"]`
- **实现**：`{"extraction_code":["parsed[\"raw_response\"] = raw_response"],"source_locations":[{"line_end":147,"line_start":147,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["raw_response=SWM input/output field"]}`
- **源码证据**：swm-raw-response-code @ ontology/swm_predictor.py:147-147 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[{"relation_id":"rel.predicts.16708c888f83f500","relation_type":"predicts","variable_id":"swm.input.planned_actions"},{"relation_id":"rel.predicts.590e39747a7e5630","relation_type":"predicts","variable_id":"swm.prediction_steps"},{"relation_id":"rel.predicts.a0ea292153fc8012","relation_type":"predicts","variable_id":"swm.input.abox_state"}]`
- **直接下游**：`[]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"预测模型原始返回文本。","evidence_ids":["swm-raw-response-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.raw_response`
- **因编码损坏未注入字段**：`[]`

### `swm.token_usage`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`token_usage`；zh=预测 Token 用量；en=Prediction Token Usage
- **别名**：预测 Token 用量、Prediction Token Usage、token_usage
- **简明含义**：SWM LLM 调用 token 用量对象。
- **直观解释**：SWM LLM 调用 token 用量对象。
- **接口**：`{"data_type":"object","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"dict","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"键值对象。","dimensions":[],"kind":"object"},"storm_paths":["swm.token_usage"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["token_usage=SWM input/output field"]`
- **实现**：`{"extraction_code":["parsed[\"token_usage\"] = self.client.last_usage"],"source_locations":[{"line_end":146,"line_start":146,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["token_usage=SWM input/output field"]}`
- **源码证据**：swm-token-usage-code @ ontology/swm_predictor.py:146-146 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"SWM LLM 调用 token 用量对象。","evidence_ids":["swm-token-usage-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction', 'evaluation_and_tokens']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.token_usage`
- **因编码损坏未注入字段**：`[]`

### `swm.unit.health_delta`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`health_delta`；zh=预测生命变化；en=Predicted Health Delta
- **别名**：预测生命变化、Predicted Health Delta、health_delta
- **简明含义**：预测单位生命变化量。
- **直观解释**：预测单位生命变化量。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["swm.unit.health_delta"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["health_delta=SWM input/output field"]`
- **实现**：`{"extraction_code":["pred_unit.get(\"health_delta\", 0)"],"source_locations":[{"line_end":272,"line_start":272,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["health_delta=SWM input/output field"]}`
- **源码证据**：swm-unit-health-delta-code @ ontology/swm_predictor.py:272-272 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[{"relation_id":"rel.stored_as.0f3958f73bf09086","relation_type":"stored_as","variable_id":"swm.predicted_unit_states"}]`
- **直接下游**：`[]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"预测单位生命变化量。","evidence_ids":["swm-unit-health-delta-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.unit.health_delta`
- **因编码损坏未注入字段**：`[]`

### `swm.unit.position_delta`
- **层级**：category=`swm`；source_layer=`swm_prediction`；derivation=`predicted`
- **名称**：canonical=`position_delta`；zh=预测位置变化；en=Predicted Position Delta
- **别名**：预测位置变化、Predicted Position Delta、position_delta
- **简明含义**：预测单位二维位置变化。
- **直观解释**：预测单位二维位置变化。
- **接口**：`{"data_type":"array","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"list","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"二维 [x, y] 向量。","dimensions":[2],"kind":"vector"},"storm_paths":["swm.unit.position_delta"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["position_delta=SWM input/output field"]`
- **实现**：`{"extraction_code":["pred_unit.get(\"position_delta\", [0, 0])"],"source_locations":[{"line_end":276,"line_start":276,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.predict / compute_prediction_error"}],"transformation_formula":["position_delta=SWM input/output field"]}`
- **源码证据**：swm-unit-position-delta-code @ ontology/swm_predictor.py:276-276 (SWMPredictor.predict / compute_prediction_error; needs_verification)
- **直接上游**：`[{"relation_id":"rel.stored_as.b89e4662d219ae11","relation_type":"stored_as","variable_id":"swm.predicted_unit_states"}]`
- **直接下游**：`[]`
- **限制**：`["该值由外部 LLM 预测或随预测流程生成；本步骤未调用模型验证实际输出。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"预测单位二维位置变化。","evidence_ids":["swm-unit-position-delta-code"],"status":"needs_verification"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"needs_verification","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry', 'swm_prediction']；data_chains=['swm_prediction_and_revalidation']
- **原始记录引用**：`knowledge/variables/swm.yaml#id=swm.unit.position_delta`
- **因编码损坏未注入字段**：`[]`

## experiment_metric：实验与模型指标

### `metric.action.decision_failure_rate`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`decision_failure_rate`；zh=决策动作失败率；en=Decision Action Failure Rate
- **别名**：决策动作失败率、Decision Action Failure Rate、decision_failure_rate
- **简明含义**：当前代码计算或聚合的决策动作失败率。
- **直观解释**：当前代码计算或聚合的决策动作失败率。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.action.decision_failure_rate"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["failure_stats.action_failure_rate"]`
- **实现**：`{"extraction_code":["decision_failure_rate = float"],"source_locations":[{"line_end":146,"line_start":146,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["failure_stats.action_failure_rate"]}`
- **源码证据**：metric-action-decision-failure-rate-code @ examples/ablation_experiment.py:146-146 (run_variant; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.3a670f6775ddef19","relation_type":"aggregated_into","variable_id":"metric.action.failure_rate"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的决策动作失败率。","evidence_ids":["metric-action-decision-failure-rate-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'actions_and_execution', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.action.decision_failure_rate`
- **因编码损坏未注入字段**：`[]`

### `metric.action.delayed_failure_rate`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`delayed_failure_rate`；zh=延迟动作失败率；en=Delayed Action Failure Rate
- **别名**：延迟动作失败率、Delayed Action Failure Rate、delayed_failure_rate
- **简明含义**：当前代码计算或聚合的延迟动作失败率。
- **直观解释**：当前代码计算或聚合的延迟动作失败率。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.action.delayed_failure_rate"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["failure_stats.delayed_failure_rate"]`
- **实现**：`{"extraction_code":["delayed_failure_rate = float"],"source_locations":[{"line_end":147,"line_start":147,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["failure_stats.delayed_failure_rate"]}`
- **源码证据**：metric-action-delayed-failure-rate-code @ examples/ablation_experiment.py:147-147 (run_variant; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.e21f7eb491c500ab","relation_type":"aggregated_into","variable_id":"metric.action.failure_rate"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的延迟动作失败率。","evidence_ids":["metric-action-delayed-failure-rate-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'actions_and_execution', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.action.delayed_failure_rate`
- **因编码损坏未注入字段**：`[]`

### `metric.action.failure_rate`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`action_failure_rate`；zh=动作失败率；en=Action Failure Rate
- **别名**：动作失败率、Action Failure Rate、action_failure_rate
- **简明含义**：当前代码计算或聚合的动作失败率。
- **直观解释**：当前代码计算或聚合的动作失败率。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.action.failure_rate"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["min(1,decision_failure_rate+delayed_failure_rate)"]`
- **实现**：`{"extraction_code":["action_failure_rate_list.append"],"source_locations":[{"line_end":150,"line_start":150,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["min(1,decision_failure_rate+delayed_failure_rate)"]}`
- **源码证据**：metric-action-failure-rate-code @ examples/ablation_experiment.py:150-150 (run_variant; code_reality)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.3a670f6775ddef19","relation_type":"aggregated_into","variable_id":"metric.action.decision_failure_rate"},{"relation_id":"rel.aggregated_into.e21f7eb491c500ab","relation_type":"aggregated_into","variable_id":"metric.action.delayed_failure_rate"}]`
- **直接下游**：`[]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的动作失败率。","evidence_ids":["metric-action-failure-rate-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'actions_and_execution', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.action.failure_rate`
- **因编码损坏未注入字段**：`[]`

### `metric.episode.final_score`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`final_score`；zh=回合最终得分；en=Episode Final Score
- **别名**：回合最终得分、Episode Final Score、final_score
- **简明含义**：当前代码计算或聚合的回合最终得分。
- **直观解释**：当前代码计算或聚合的回合最终得分。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.episode.final_score"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["终止步 score_cumulative[0]"]`
- **实现**：`{"extraction_code":["final_score = float(score_cumulative[0])"],"source_locations":[{"line_end":133,"line_start":133,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["终止步 score_cumulative[0]"]}`
- **源码证据**：metric-episode-final-score-code @ examples/ablation_experiment.py:133-133 (run_variant; code_reality)
- **直接上游**：`[{"relation_id":"rel.stored_as.93de4079427da478","relation_type":"stored_as","variable_id":"timestep.score_cumulative_0"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.f45c20869c360521","relation_type":"aggregated_into","variable_id":"metric.experiment.avg_score"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的回合最终得分。","evidence_ids":["metric-episode-final-score-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.episode.final_score`
- **因编码损坏未注入字段**：`[]`

### `metric.experiment.avg_score`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`avg_score`；zh=平均回合得分；en=Average Episode Score
- **别名**：平均回合得分、Average Episode Score、avg_score
- **简明含义**：当前代码计算或聚合的平均回合得分。
- **直观解释**：当前代码计算或聚合的平均回合得分。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.experiment.avg_score"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["sum(score_list)/len(score_list)"]`
- **实现**：`{"extraction_code":["avg_score = sum(score_list)"],"source_locations":[{"line_end":178,"line_start":178,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["sum(score_list)/len(score_list)"]}`
- **源码证据**：metric-experiment-avg-score-code @ examples/ablation_experiment.py:178-178 (run_variant; code_reality)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.f45c20869c360521","relation_type":"aggregated_into","variable_id":"metric.episode.final_score"}]`
- **直接下游**：`[]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的平均回合得分。","evidence_ids":["metric-experiment-avg-score-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.experiment.avg_score`
- **因编码损坏未注入字段**：`[]`

### `metric.llm.avg_decision_time`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`avg_decision_time`；zh=平均决策耗时；en=Average Decision Time
- **别名**：平均决策耗时、Average Decision Time、avg_decision_time
- **简明含义**：当前代码计算或聚合的平均决策耗时。
- **直观解释**：当前代码计算或聚合的平均决策耗时。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.llm.avg_decision_time"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"second"}}`
- **公式/转换**：`["total_decision_time/decision_calls"]`
- **实现**：`{"extraction_code":["self.avg_decision_time = self.total_decision_time / self.decision_calls"],"source_locations":[{"line_end":321,"line_start":321,"path":"agents/raw_agent.py","symbol":"RawAgent.step"}],"transformation_formula":["total_decision_time/decision_calls"]}`
- **源码证据**：metric-llm-avg-decision-time-code @ agents/raw_agent.py:321-321 (RawAgent.step; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的平均决策耗时。","evidence_ids":["metric-llm-avg-decision-time-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.llm.avg_decision_time`
- **因编码损坏未注入字段**：`[]`

### `metric.llm.avg_tokens_per_decision`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`avg_total_tokens_per_decision`；zh=每决策平均 Token；en=Average Tokens per Decision
- **别名**：每决策平均 Token、Average Tokens per Decision、avg_total_tokens_per_decision
- **简明含义**：当前代码计算或聚合的每决策平均 Token。
- **直观解释**：当前代码计算或聚合的每决策平均 Token。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.llm.avg_tokens_per_decision"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["total_tokens/decision_calls；零调用为 0"]`
- **实现**：`{"extraction_code":["avg_total_tokens_per_decision = total_tokens / total_decision_calls"],"source_locations":[{"line_end":172,"line_start":172,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["total_tokens/decision_calls；零调用为 0"]}`
- **源码证据**：metric-llm-avg-tokens-per-decision-code @ examples/ablation_experiment.py:172-172 (run_variant; code_reality)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.5b1a618563ece33c","relation_type":"aggregated_into","variable_id":"metric.llm.decision_calls"},{"relation_id":"rel.aggregated_into.dc6050c33fba6198","relation_type":"aggregated_into","variable_id":"metric.llm.total_tokens"}]`
- **直接下游**：`[]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的每决策平均 Token。","evidence_ids":["metric-llm-avg-tokens-per-decision-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.llm.avg_tokens_per_decision`
- **因编码损坏未注入字段**：`[]`

### `metric.llm.completion_tokens`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`completion_tokens`；zh=补全 Token 数；en=Completion Tokens
- **别名**：补全 Token 数、Completion Tokens、completion_tokens
- **简明含义**：当前代码计算或聚合的补全 Token 数。
- **直观解释**：当前代码计算或聚合的补全 Token 数。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.llm.completion_tokens"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["各决策 completion_tokens 求和"]`
- **实现**：`{"extraction_code":["total_completion_tokens +="],"source_locations":[{"line_end":154,"line_start":154,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["各决策 completion_tokens 求和"]}`
- **源码证据**：metric-llm-completion-tokens-code @ examples/ablation_experiment.py:154-154 (run_variant; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的补全 Token 数。","evidence_ids":["metric-llm-completion-tokens-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.llm.completion_tokens`
- **因编码损坏未注入字段**：`[]`

### `metric.llm.decision_calls`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`decision_calls`；zh=决策调用次数；en=Decision Calls
- **别名**：决策调用次数、Decision Calls、decision_calls
- **简明含义**：当前代码计算或聚合的决策调用次数。
- **直观解释**：当前代码计算或聚合的决策调用次数。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.llm.decision_calls"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["决策调用次数求和"]`
- **实现**：`{"extraction_code":["total_decision_calls +="],"source_locations":[{"line_end":156,"line_start":156,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["决策调用次数求和"]}`
- **源码证据**：metric-llm-decision-calls-code @ examples/ablation_experiment.py:156-156 (run_variant; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.5b1a618563ece33c","relation_type":"aggregated_into","variable_id":"metric.llm.avg_tokens_per_decision"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的决策调用次数。","evidence_ids":["metric-llm-decision-calls-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.llm.decision_calls`
- **因编码损坏未注入字段**：`[]`

### `metric.llm.prompt_tokens`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`prompt_tokens`；zh=提示 Token 数；en=Prompt Tokens
- **别名**：提示 Token 数、Prompt Tokens、prompt_tokens
- **简明含义**：当前代码计算或聚合的提示 Token 数。
- **直观解释**：当前代码计算或聚合的提示 Token 数。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.llm.prompt_tokens"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["各决策 prompt_tokens 求和"]`
- **实现**：`{"extraction_code":["total_prompt_tokens +="],"source_locations":[{"line_end":153,"line_start":153,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["各决策 prompt_tokens 求和"]}`
- **源码证据**：metric-llm-prompt-tokens-code @ examples/ablation_experiment.py:153-153 (run_variant; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的提示 Token 数。","evidence_ids":["metric-llm-prompt-tokens-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.llm.prompt_tokens`
- **因编码损坏未注入字段**：`[]`

### `metric.llm.total_tokens`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`total_tokens`；zh=总 Token 数；en=Total Tokens
- **别名**：总 Token 数、Total Tokens、total_tokens
- **简明含义**：当前代码计算或聚合的总 Token 数。
- **直观解释**：当前代码计算或聚合的总 Token 数。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.llm.total_tokens"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["各决策 total_tokens 求和"]`
- **实现**：`{"extraction_code":["total_tokens +="],"source_locations":[{"line_end":155,"line_start":155,"path":"examples/ablation_experiment.py","symbol":"run_variant"}],"transformation_formula":["各决策 total_tokens 求和"]}`
- **源码证据**：metric-llm-total-tokens-code @ examples/ablation_experiment.py:155-155 (run_variant; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.dc6050c33fba6198","relation_type":"aggregated_into","variable_id":"metric.llm.avg_tokens_per_decision"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的总 Token 数。","evidence_ids":["metric-llm-total-tokens-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['counts_and_aggregation', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.llm.total_tokens`
- **因编码损坏未注入字段**：`[]`

### `metric.swm.health_rmse`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`health_rmse`；zh=生命预测均方根误差；en=Health RMSE
- **别名**：生命预测均方根误差、Health RMSE、health_rmse
- **简明含义**：当前代码计算或聚合的生命预测均方根误差。
- **直观解释**：当前代码计算或聚合的生命预测均方根误差。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.swm.health_rmse"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["sqrt(mean((pred_hp-actual_hp)^2))"]`
- **实现**：`{"extraction_code":["health_rmse = float"],"source_locations":[{"line_end":288,"line_start":288,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"}],"transformation_formula":["sqrt(mean((pred_hp-actual_hp)^2))"]}`
- **源码证据**：metric-swm-health-rmse-code @ ontology/swm_predictor.py:288-288 (SWMPredictor.compute_prediction_error; code_reality)
- **直接上游**：`[{"relation_id":"rel.evaluated_by.0c2d98ef632a14eb","relation_type":"evaluated_by","variable_id":"swm.predicted_unit_states"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.449bd405041b8423","relation_type":"aggregated_into","variable_id":"metric.swm.overall_error"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["metric.swm.health_rmse","metric.swm.overall_error","metric.swm.position_rmse"],"concise_explanation":"health 误差退化为 delta²，position 误差退化为预测位移模长。","current_implementation":"函数没有接收 t 时刻单位基线。","evidence":[{"claim":"health 与 position 都从 actual_state 构造预测值。","line_end":282,"line_start":272,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"},{"claim":"训练器记录下一帧快照。","line_end":292,"line_start":285,"path":"agents/raw_agent.py","symbol":"RawAgent._record_swm_ground_truth"}],"expected_or_documented_behavior":"预测绝对值应由 t 状态加 delta，再与 t+1 真值比较。","id":"issue.swm_error_uses_future_state_as_baseline","impact":{"code_or_experiment_risk":"实验指标可能无法反映真实预测误差。","knowledge_answer_constraint":"不得称这些值为严格未来状态 RMSE；须提示基线缺陷及其传播到 overall_error。"},"issue_type":"confirmed_bug","limitations":["未重跑历史实验。"],"phenomenon":"误差函数用 actual(t+1) 同时构造预测值和真实值。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造 t、delta、t+1 的已知样例。","手算并回归三个指标。"],"success_criteria":"误差等于预测未来绝对状态与 t+1 真值之差。"},"severity":"critical","status":"open","title_zh":"SWM health/position 误差基线错误","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的生命预测均方根误差。","evidence_ids":["metric-swm-health-rmse-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['health_and_survivability', 'swm_prediction', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.swm.health_rmse`
- **因编码损坏未注入字段**：`[]`

### `metric.swm.overall_error`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`overall_error`；zh=SWM 综合误差；en=SWM Overall Error
- **别名**：SWM 综合误差、SWM Overall Error、overall_error
- **简明含义**：当前代码计算或聚合的SWM 综合误差。
- **直观解释**：当前代码计算或聚合的SWM 综合误差。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.swm.overall_error"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["0.4*health_rmse+0.3*position_rmse+0.3*(1-relation_accuracy)"]`
- **实现**：`{"extraction_code":["overall = 0.4 * health_rmse"],"source_locations":[{"line_end":311,"line_start":311,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"}],"transformation_formula":["0.4*health_rmse+0.3*position_rmse+0.3*(1-relation_accuracy)"]}`
- **源码证据**：metric-swm-overall-error-code @ ontology/swm_predictor.py:311-311 (SWMPredictor.compute_prediction_error; code_reality)
- **直接上游**：`[{"relation_id":"rel.aggregated_into.1ee16adfb01da5aa","relation_type":"aggregated_into","variable_id":"metric.swm.relation_accuracy"},{"relation_id":"rel.aggregated_into.449bd405041b8423","relation_type":"aggregated_into","variable_id":"metric.swm.health_rmse"},{"relation_id":"rel.aggregated_into.b2576700953925e4","relation_type":"aggregated_into","variable_id":"metric.swm.position_rmse"}]`
- **直接下游**：`[]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["metric.swm.health_rmse","metric.swm.overall_error","metric.swm.position_rmse"],"concise_explanation":"health 误差退化为 delta²，position 误差退化为预测位移模长。","current_implementation":"函数没有接收 t 时刻单位基线。","evidence":[{"claim":"health 与 position 都从 actual_state 构造预测值。","line_end":282,"line_start":272,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"},{"claim":"训练器记录下一帧快照。","line_end":292,"line_start":285,"path":"agents/raw_agent.py","symbol":"RawAgent._record_swm_ground_truth"}],"expected_or_documented_behavior":"预测绝对值应由 t 状态加 delta，再与 t+1 真值比较。","id":"issue.swm_error_uses_future_state_as_baseline","impact":{"code_or_experiment_risk":"实验指标可能无法反映真实预测误差。","knowledge_answer_constraint":"不得称这些值为严格未来状态 RMSE；须提示基线缺陷及其传播到 overall_error。"},"issue_type":"confirmed_bug","limitations":["未重跑历史实验。"],"phenomenon":"误差函数用 actual(t+1) 同时构造预测值和真实值。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造 t、delta、t+1 的已知样例。","手算并回归三个指标。"],"success_criteria":"误差等于预测未来绝对状态与 t+1 真值之差。"},"severity":"critical","status":"open","title_zh":"SWM health/position 误差基线错误","truth_status":"code_reality"},{"affected_noncanonical_fields":[],"affected_variable_ids":["metric.swm.overall_error","metric.swm.relation_accuracy"],"concise_explanation":"它不等同于覆盖假阴性的完整关系准确率。","current_implementation":"实现遍历 predicted_relations；无预测时保留 1.0。","evidence":[{"claim":"只用预测关系作分母且空预测为 1.0。","line_end":309,"line_start":291,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"},{"claim":"当前下一帧关系真值为空。","line_end":290,"line_start":290,"path":"agents/raw_agent.py","symbol":"RawAgent._record_swm_ground_truth"}],"expected_or_documented_behavior":"应明确 precision/recall/F1 或定义空集合与漏报规则。","id":"issue.swm_relation_accuracy_is_prediction_precision","impact":{"code_or_experiment_risk":"overall_error 可能偏乐观。","knowledge_answer_constraint":"应称预测关系命中比例，并披露空预测=1.0与当前真值为空。"},"issue_type":"implementation_quirk","limitations":["未重跑 SWM 实验。"],"phenomenon":"指标只以预测关系为分母；不惩罚漏报，空预测返回 1.0，当前真值快照 relations 为空。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造命中、误报、漏报和空预测案例。","比较 precision/recall/F1。"],"success_criteria":"指标名、公式和空集合规则一致。"},"severity":"high","status":"open","title_zh":"relation_accuracy 更接近预测关系命中率","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的SWM 综合误差。","evidence_ids":["metric-swm-overall-error-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['swm_prediction', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.swm.overall_error`
- **因编码损坏未注入字段**：`[]`

### `metric.swm.position_rmse`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`position_rmse`；zh=位置预测均方根误差；en=Position RMSE
- **别名**：位置预测均方根误差、Position RMSE、position_rmse
- **简明含义**：当前代码计算或聚合的位置预测均方根误差。
- **直观解释**：当前代码计算或聚合的位置预测均方根误差。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"needs_verification"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.swm.position_rmse"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["sqrt(mean(dx^2+dy^2))"]`
- **实现**：`{"extraction_code":["position_rmse = float"],"source_locations":[{"line_end":289,"line_start":289,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"}],"transformation_formula":["sqrt(mean(dx^2+dy^2))"]}`
- **源码证据**：metric-swm-position-rmse-code @ ontology/swm_predictor.py:289-289 (SWMPredictor.compute_prediction_error; code_reality)
- **直接上游**：`[{"relation_id":"rel.evaluated_by.4ae4484eb47be5c4","relation_type":"evaluated_by","variable_id":"swm.predicted_unit_states"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.b2576700953925e4","relation_type":"aggregated_into","variable_id":"metric.swm.overall_error"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["metric.swm.health_rmse","metric.swm.overall_error","metric.swm.position_rmse"],"concise_explanation":"health 误差退化为 delta²，position 误差退化为预测位移模长。","current_implementation":"函数没有接收 t 时刻单位基线。","evidence":[{"claim":"health 与 position 都从 actual_state 构造预测值。","line_end":282,"line_start":272,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"},{"claim":"训练器记录下一帧快照。","line_end":292,"line_start":285,"path":"agents/raw_agent.py","symbol":"RawAgent._record_swm_ground_truth"}],"expected_or_documented_behavior":"预测绝对值应由 t 状态加 delta，再与 t+1 真值比较。","id":"issue.swm_error_uses_future_state_as_baseline","impact":{"code_or_experiment_risk":"实验指标可能无法反映真实预测误差。","knowledge_answer_constraint":"不得称这些值为严格未来状态 RMSE；须提示基线缺陷及其传播到 overall_error。"},"issue_type":"confirmed_bug","limitations":["未重跑历史实验。"],"phenomenon":"误差函数用 actual(t+1) 同时构造预测值和真实值。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造 t、delta、t+1 的已知样例。","手算并回归三个指标。"],"success_criteria":"误差等于预测未来绝对状态与 t+1 真值之差。"},"severity":"critical","status":"open","title_zh":"SWM health/position 误差基线错误","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的位置预测均方根误差。","evidence_ids":["metric-swm-position-rmse-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['position_and_geometry', 'swm_prediction', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.swm.position_rmse`
- **因编码损坏未注入字段**：`[]`

### `metric.swm.relation_accuracy`
- **层级**：category=`experiment_metric`；source_layer=`experiment_aggregate`；derivation=`aggregated`
- **名称**：canonical=`relation_accuracy`；zh=关系预测准确率；en=Relation Accuracy
- **别名**：关系预测准确率、Relation Accuracy、relation_accuracy
- **简明含义**：当前代码计算或聚合的关系预测准确率。
- **直观解释**：当前代码计算或聚合的关系预测准确率。
- **接口**：`{"data_type":"number","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"float","range":{"description":"当前代码能证明的范围；其余范围待核验。","maximum":1,"maximum_inclusive":true,"minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["metric.swm.relation_accuracy"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"1"}}`
- **公式/转换**：`["correct/total；total=0 时为 1"]`
- **实现**：`{"extraction_code":["relation_accuracy = relation_correct / relation_total"],"source_locations":[{"line_end":309,"line_start":309,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"}],"transformation_formula":["correct/total；total=0 时为 1"]}`
- **源码证据**：metric-swm-relation-accuracy-code @ ontology/swm_predictor.py:309-309 (SWMPredictor.compute_prediction_error; code_reality)
- **直接上游**：`[{"relation_id":"rel.evaluated_by.693cf5dbfed13d74","relation_type":"evaluated_by","variable_id":"swm.predicted_relations"}]`
- **直接下游**：`[{"relation_id":"rel.aggregated_into.1ee16adfb01da5aa","relation_type":"aggregated_into","variable_id":"metric.swm.overall_error"}]`
- **限制**：`["本步骤未重跑实验，只确认定义和计算代码；不能把历史数值当作本次结果。"]`
- **已知问题**：`{"record_level":[],"step09":[{"affected_noncanonical_fields":[],"affected_variable_ids":["metric.swm.overall_error","metric.swm.relation_accuracy"],"concise_explanation":"它不等同于覆盖假阴性的完整关系准确率。","current_implementation":"实现遍历 predicted_relations；无预测时保留 1.0。","evidence":[{"claim":"只用预测关系作分母且空预测为 1.0。","line_end":309,"line_start":291,"path":"ontology/swm_predictor.py","symbol":"SWMPredictor.compute_prediction_error"},{"claim":"当前下一帧关系真值为空。","line_end":290,"line_start":290,"path":"agents/raw_agent.py","symbol":"RawAgent._record_swm_ground_truth"}],"expected_or_documented_behavior":"应明确 precision/recall/F1 或定义空集合与漏报规则。","id":"issue.swm_relation_accuracy_is_prediction_precision","impact":{"code_or_experiment_risk":"overall_error 可能偏乐观。","knowledge_answer_constraint":"应称预测关系命中比例，并披露空预测=1.0与当前真值为空。"},"issue_type":"implementation_quirk","limitations":["未重跑 SWM 实验。"],"phenomenon":"指标只以预测关系为分母；不惩罚漏报，空预测返回 1.0，当前真值快照 relations 为空。","recommended_verification":{"execution_status":"not_executed","method":"static_unit_test","steps":["构造命中、误报、漏报和空预测案例。","比较 precision/recall/F1。"],"success_criteria":"指标名、公式和空集合规则一致。"},"severity":"high","status":"open","title_zh":"relation_accuracy 更接近预测关系命中率","truth_status":"code_reality"}]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码计算或聚合的关系预测准确率。","evidence_ids":["metric-swm-relation-accuracy-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['ontology_and_graph', 'swm_prediction', 'evaluation_and_tokens']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/metrics.yaml#id=metric.swm.relation_accuracy`
- **因编码损坏未注入字段**：`[]`

## environment_config：环境配置

### `environment.decision_interval`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`decision_interval`；zh=决策间隔；en=Decision Interval
- **别名**：决策间隔、Decision Interval、decision_interval
- **简明含义**：当前代码将 decision_interval 配置为 10。
- **直观解释**：当前代码将 decision_interval 配置为 10。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.decision_interval"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"known","value":"environment step"}}`
- **公式/转换**：`["decision_interval=10"]`
- **实现**：`{"extraction_code":["decision_interval: int = 10"],"source_locations":[{"line_end":50,"line_start":50,"path":"agents/raw_agent.py","symbol":"RawAgent.__init__"}],"transformation_formula":["decision_interval=10"]}`
- **源码证据**：environment-decision-interval-code @ agents/raw_agent.py:50-50 (RawAgent.__init__; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 decision_interval 配置为 10。","evidence_ids":["environment-decision-interval-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['evaluation_and_tokens', 'environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.decision_interval`
- **因编码损坏未注入字段**：`[]`

### `environment.map_name`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`map_name`；zh=地图名；en=Map Name
- **别名**：地图名、Map Name、map_name
- **简明含义**：当前代码将 map_name 配置为 'DefeatRoaches'。
- **直观解释**：当前代码将 map_name 配置为 'DefeatRoaches'。
- **接口**：`{"data_type":"string","enum_values":{"description":"不使用或未声明枚举。","status":"unknown","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"str","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.map_name"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["map_name='DefeatRoaches'"]`
- **实现**：`{"extraction_code":["map_name=\"DefeatRoaches\""],"source_locations":[{"line_end":77,"line_start":77,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["map_name='DefeatRoaches'"]}`
- **源码证据**：environment-map-name-code @ examples/llm_agent_example.py:77-77 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 map_name 配置为 'DefeatRoaches'。","evidence_ids":["environment-map-name-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.map_name`
- **因编码损坏未注入字段**：`[]`

### `environment.raw_resolution`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`raw_resolution`；zh=Raw 坐标分辨率；en=Raw Resolution
- **别名**：Raw 坐标分辨率、Raw Resolution、raw_resolution
- **简明含义**：当前代码将 raw_resolution 配置为 64。
- **直观解释**：当前代码将 raw_resolution 配置为 64。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.raw_resolution"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["raw_resolution=64"]`
- **实现**：`{"extraction_code":["raw_resolution=64"],"source_locations":[{"line_end":86,"line_start":86,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["raw_resolution=64"]}`
- **源码证据**：environment-raw-resolution-code @ examples/llm_agent_example.py:86-86 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 raw_resolution 配置为 64。","evidence_ids":["environment-raw-resolution-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.raw_resolution`
- **因编码损坏未注入字段**：`[]`

### `environment.realtime`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`realtime`；zh=实时模式；en=Realtime Mode
- **别名**：实时模式、Realtime Mode、realtime
- **简明含义**：当前代码将 realtime 配置为 False。
- **直观解释**：当前代码将 realtime 配置为 False。
- **接口**：`{"data_type":"boolean","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"bool","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.realtime"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["realtime=False"]`
- **实现**：`{"extraction_code":["realtime=False"],"source_locations":[{"line_end":90,"line_start":90,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["realtime=False"]}`
- **源码证据**：environment-realtime-code @ examples/llm_agent_example.py:90-90 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 realtime 配置为 False。","evidence_ids":["environment-realtime-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.realtime`
- **因编码损坏未注入字段**：`[]`

### `environment.step_mul`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`step_mul`；zh=环境步长倍数；en=Environment Step Multiplier
- **别名**：环境步长倍数、Environment Step Multiplier、step_mul
- **简明含义**：当前代码将 step_mul 配置为 8。
- **直观解释**：当前代码将 step_mul 配置为 8。
- **接口**：`{"data_type":"integer","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"int","range":{"description":"当前代码能证明的范围；其余范围待核验。","minimum":0,"minimum_inclusive":true,"status":"known"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.step_mul"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["step_mul=8"]`
- **实现**：`{"extraction_code":["step_mul=8"],"source_locations":[{"line_end":89,"line_start":89,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["step_mul=8"]}`
- **源码证据**：environment-step-mul-code @ examples/llm_agent_example.py:89-89 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 step_mul 配置为 8。","evidence_ids":["environment-step-mul-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.step_mul`
- **因编码损坏未注入字段**：`[]`

### `environment.use_raw_actions`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`use_raw_actions`；zh=启用 Raw Actions；en=Use Raw Actions
- **别名**：启用 Raw Actions、Use Raw Actions、use_raw_actions
- **简明含义**：当前代码将 use_raw_actions 配置为 True。
- **直观解释**：当前代码将 use_raw_actions 配置为 True。
- **接口**：`{"data_type":"boolean","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"bool","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.use_raw_actions"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["use_raw_actions=True"]`
- **实现**：`{"extraction_code":["use_raw_actions=True"],"source_locations":[{"line_end":85,"line_start":85,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["use_raw_actions=True"]}`
- **源码证据**：environment-use-raw-actions-code @ examples/llm_agent_example.py:85-85 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[{"relation_id":"rel.mapped_to.14c81e1ba7855c8e","relation_type":"mapped_to","variable_id":"pysc2.function.raw_flag"}]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 use_raw_actions 配置为 True。","evidence_ids":["environment-use-raw-actions-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['actions_and_execution', 'environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.use_raw_actions`
- **因编码损坏未注入字段**：`[]`

### `environment.use_raw_units`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`use_raw_units`；zh=启用 Raw Units；en=Use Raw Units
- **别名**：启用 Raw Units、Use Raw Units、use_raw_units
- **简明含义**：当前代码将 use_raw_units 配置为 True。
- **直观解释**：当前代码将 use_raw_units 配置为 True。
- **接口**：`{"data_type":"boolean","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"bool","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.use_raw_units"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["use_raw_units=True"]`
- **实现**：`{"extraction_code":["use_raw_units=True"],"source_locations":[{"line_end":84,"line_start":84,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["use_raw_units=True"]}`
- **源码证据**：environment-use-raw-units-code @ examples/llm_agent_example.py:84-84 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 use_raw_units 配置为 True。","evidence_ids":["environment-use-raw-units-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.use_raw_units`
- **因编码损坏未注入字段**：`[]`

### `environment.visualize`
- **层级**：category=`environment_config`；source_layer=`environment_config`；derivation=`direct_read`
- **名称**：canonical=`visualize`；zh=可视化开关；en=Visualization Flag
- **别名**：可视化开关、Visualization Flag、visualize
- **简明含义**：当前代码将 visualize 配置为 False。
- **直观解释**：当前代码将 visualize 配置为 False。
- **接口**：`{"data_type":"boolean","enum_values":{"description":"不使用或未声明枚举。","status":"not_applicable","values":[]},"nullable":false,"pysc2_path":{"note":"直接接口路径或当前代码的位置索引表达。","status":"not_applicable"},"python_type":"bool","range":{"description":"当前代码能证明的范围；其余范围待核验。","status":"unknown"},"shape":{"description":"单个标量值。","dimensions":[],"kind":"scalar"},"storm_paths":["SC2Env.visualize"],"unit":{"note":"按当前代码记录；未声明时保持未知。","status":"unknown"}}`
- **公式/转换**：`["visualize=False"]`
- **实现**：`{"extraction_code":["visualize=False"],"source_locations":[{"line_end":91,"line_start":91,"path":"examples/llm_agent_example.py","symbol":"main"}],"transformation_formula":["visualize=False"]}`
- **源码证据**：environment-visualize-code @ examples/llm_agent_example.py:91-91 (main; code_reality)
- **直接上游**：`[]`
- **直接下游**：`[]`
- **限制**：`["只证明当前 STORM 代码含义；未用 SC2 运行时或外部官方资料核验。"]`
- **已知问题**：`{"record_level":[],"step09":[]}`
- **事实边界**：`{"code_reality":[{"claim":"当前代码将 visualize 配置为 False。","evidence_ids":["environment-visualize-code"],"status":"code_reality"}],"design_intent":[],"verification":{"external_sources_checked":false,"notes":"已通过步骤05严格静态 Schema、关系与证据校验；未启动 SC2，未调用外部 LLM/SWM，未检查外部官方资料。","sc2_executed":false,"status":"static_verified","tests_executed":[{"name":"步骤05严格静态 Schema、关系与证据校验","result":"passed"}],"verified_at":"2026-09-03"}}`
- **检索分片**：topics=['environment_and_timing']；data_chains=['environment_and_evaluation']
- **原始记录引用**：`knowledge/variables/raw_api.yaml#id=environment.visualize`
- **因编码损坏未注入字段**：`[]`
