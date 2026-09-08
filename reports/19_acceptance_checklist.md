# 步骤 19：内部验收清单

## 后续状态更新（2026-09-07）

本文件保留步骤 19 执行当时的验收快照。此后项目负责人已选择 Apache License 2.0，并提供 GitHub 空仓库；因此许可证阻塞已解决。下文 `public_github_release: no_go` 不应改写为当时已经通过，剩余技术限制仍按公开已知问题披露。

- 验收日期：2026-09-07
- 验收对象：STORM PySC2 Raw API 变量知识库 V0.1（`0.1.0`）
- 验收范围：当前 STORM 主路径实际使用的 Raw API 变量及直接衍生量
- 总体结论：**conditional_go**
- 外部 API：本步骤未调用
- SC2：本步骤未启动

## 1. 目标验收表

| ID | 目标 | 验收方法 | 结果 | 证据与说明 |
|---|---|---|---|---|
| A01 | 根据自然语言找到变量 | 7 个代表性查询，覆盖字段、别名、公式、歧义和范围外问题 | **有条件通过** | 血量、矿物、SWM 公式、ABox armor 消歧、动作延迟消歧及范围外拒答有效；“环境每次决策跨多少游戏步”未召回 `environment.step_mul` |
| A02 | 解释变量物理含义 | 检查 135 条正式记录的 `definition` | **通过** | 135/135 均有定义；未知单位/护甲等问题附带限制 |
| A03 | 给出接口形式 | 检查 135 条记录的 `interface` | **通过** | 135/135 均有类型、形状、范围状态、PySC2/STORM 路径或不适用说明 |
| A04 | 定位代码实现 | 检查 `implementation.source_locations` | **通过** | 135/135 均有相对仓库路径和 symbol；抽样与当前源码一致 |
| A05 | 给出依据 | 检查每条记录的 `evidence` 和关系/已知问题 | **通过** | 135/135 均有证据；步骤 17 统计 source references=135 |
| A06 | 支持论文写作 | 抽查高频量、公式及事实状态 | **有条件通过** | 可用于变量定义和代码现实引用；`needs_verification` 和开放缺陷不得写成官方/运行时已证实事实 |
| A07 | 支持代码开发 | minimal/full 干净解包，运行 CLI 与包内测试 | **有条件通过** | 两个包的 CLI 可运行；full 包中原仓库测试脚本离开目录布局后不能直接导入 `sc2kb` |
| A08 | 适合交给 LLM Agent | 汇总 v0.6 首次盲测和三条件评测 | **有条件通过** | RAG 明显优于 no-KB/full-context，但首次盲测 variable hit rate 84.03% 和 native JSON 98% 未达到预设门槛 |
| A09 | 范围外不乱答 | 查询 feature-layer 像素变量 | **通过** | “feature_screen 像素变量”返回 `not_found` |
| A10 | 发布安全 | 步骤 18 ZIP 安全与哈希验证 | **通过** | 无密钥、私人路径、日志、缓存、结果/配置目录；SHA-256 稳定 |
| A11 | 可以公开开源 | 检查正式 LICENSE 和版权信息 | **不通过** | 当前只有候选说明，未获得负责人确认的正式许可证 |

## 2. 自然语言查询抽样

| 查询 | 期望 | 实际 | 判定 |
|---|---|---|---|
| 单位当前血量对应哪个字段 | 找到 Raw/ABox/TBox 血量层 | `raw_unit.health`、`abox.unit.hp`、`tbox.entity.hp` | 通过 |
| ABox armor 当前实际保存的是什么 | 提示 TBox/ABox 歧义并指出 shield 映射 | 返回 `ambiguous`，候选含两层 armor | 通过 |
| 动作延迟步数的接口字段和范围 | 找到 `action.delay_steps`，必要时消歧 | 返回 `ambiguous`，候选含目标字段 | 通过 |
| 环境每次决策跨多少游戏步 | 找到 `environment.step_mul` | `not_found` | 不通过 |
| 玩家矿物数量在哪里读取 | 找到 `player.minerals` | 精确召回 | 通过 |
| SWM overall error 的计算公式 | 找到 `metric.swm.overall_error` | UTF-8 环境下召回；默认 GBK CLI 输出崩溃 | 有条件通过 |
| feature_screen 像素变量 | 范围外拒答 | `not_found` | 通过 |

抽样功能通过 5 项，有条件通过 1 项，不通过 1 项。这里不把“候选中包含目标变量”夸大成所有自然语言表达都能稳定命中。

## 3. 高频变量与当前源码抽样

| 变量/问题 | 当前源码证据 | 复核结论 |
|---|---|---|
| `raw_unit.health` | `agents/raw_agent.py::RawAgent.parse_raw_units`，索引 2 | 与记录一致 |
| `raw_unit.health_ratio` | 同函数，`unit[7] / 255` | 与记录一致；不是绝对生命值 |
| `raw_unit.shield` / ratio | 同函数，索引 3、8/255 | 与记录一致 |
| `raw_unit.x/y/tag` | 同函数的位置索引读取 | 与记录一致；仍需 PySC2 版本核验 |
| `abox.unit.hp` | `ontology/bridge.py::_add_unit_instance/_update_unit_instance` | 使用实时 `raw_unit["health"]`，未知单位静态 hp=100 不覆盖它 |
| `abox.unit.armor` | `ontology/bridge.py` 第 201、268 行附近 | 当前实际写入 shield，已知问题记录正确 |
| `action.target` | `agents/response_parser.py::_validate_semantics` 第 524–525 行附近 | `np.clip` 结果未写回，已知 bug 仍开放 |
| `action.delay_steps` | `agents/response_parser.py` 第 245–266 行附近 | 默认 0，限制/修正到 0..9 |
| Raw Function IDs | `agents/action_executor.py` 的映射和 `FunctionCall.init_with_validation` | 静态实现存在；实际 ActionSpec 兼容性仍需 SC2 运行确认 |
| SWM health/position error | `ontology/swm_predictor.py::compute_prediction_error` 第 270–289 行附近 | 当前以 actual future state 同时作为基线，critical bug 记录正确 |
| SWM relation accuracy | 同函数第 291–309 行附近 | 实际更接近预测关系 precision，空预测返回 1.0 |

抽样的 14 个变量/问题均能回指当前源码；这只是高风险抽样，不等价于重新人工阅读全部 135 个实现。

## 4. 离线测试

运行方式：逐个启动 `knowledge/tests/*.py`，并在子进程环境中移除常见 API Key 和模型端点环境变量。

| 指标 | 数量 |
|---|---:|
| 发现并执行 | 21 |
| 通过 | 20 |
| 失败 | 1 |
| 超时 | 0 |

唯一失败：`validate_step16.py` 仍断言步骤 16 状态为 `planned`，而当前协议/结果已经是 executed。它是旧验证器过时，不是本轮真实模型调用失败，但必须修复或替换，不能伪装成全绿。

机器可读结果：`knowledge/reports/19_offline_test_results.json`。

## 5. 干净发布包验收

### minimal

- SHA-256 和包内 manifest：通过；
- 解压后 CLI：通过；
- 核心查询首项 `raw_unit.health`：通过。

### full

- SHA-256 和包内 manifest：通过；
- 解压后 CLI：通过；
- 解压后直接执行包内 `tests/validate_step17.py`：**失败**；
- 失败原因：`ModuleNotFoundError: No module named 'sc2kb'`。

含义：full 包携带了测试源码，但部分测试仍假设原仓库的 `knowledge/` 目录层级或预先配置的 `PYTHONPATH`，目前不能称为完全独立的“一键复现包”。

## 6. 已完成模型评测汇总（本步骤未重跑）

### challenge v0.6 唯一一次首次盲测

| 指标 | 结果 | 预设门槛 | 判定 |
|---|---:|---:|---|
| behavior accuracy | 91.67% | >=85% | 通过 |
| variable hit rate | 84.03% | >=85% | 未通过 |
| variable precision | 94.67% | >=90% | 通过 |
| evidence hit rate | 96.06% | >=90% | 通过 |
| refusal accuracy | 98.33% | >=90% | 通过 |
| native JSON compliance | 98.00% | >=99% | 未通过 |

因此，按照预先约定，不能宣称“有效 RAG”已经全部达标。

### challenge v0.6 post 三条件

| 条件 | 行为准确率 | 变量召回率 | 证据命中率 | 总 Token |
|---|---:|---:|---:|---:|
| no-KB | 25.00% | 10.00% | 0.00% | 29,271 |
| full-context | 56.67% | 70.00% | 58.33% | 1,779,558 |
| RAG | 90.00% | 84.03% | 96.06% | 178,867 |

RAG 是当前默认知识注入方式的最佳选择，但仍是 conditional，而不是无条件生产可用。

## 7. 验收结论

### controlled internal LLM Agent use：conditional_go

在以下条件下可以交给 LLM Agent 内部使用：

1. 默认使用 RAG，不使用 no-KB；
2. 回答必须返回变量 ID、接口和证据；
3. 对 `needs_verification`、11 个已知问题和范围外问题保守回答；
4. Windows CLI 显式启用 UTF-8；
5. 论文引用前由研究者复核源码证据；
6. 不能把 v0.6 描述为已越过全部“有效 RAG”门槛。

### public GitHub release：no_go

阻断原因是正式许可证、版权主体和作者列表尚未确认；此外 full 包测试可移植性、Windows CLI 编码和 RAG 两个未达标指标应在公开推广前处理。

## 8. 步骤 19 完成报告

- 状态：**完成，结论为 conditional_go**
- 读取的关键证据：步骤 01–18 结构化产物、发布清单、当前 STORM 源码、11 个已知问题、v0.6 首次盲测及三条件报告。
- 新建或修改的文件：三份指定验收报告，以及离线测试总运行器和机器可读测试结果。
- 执行的验证：135 条记录完整性、14 项源码抽样、21 个离线脚本、minimal/full 干净解包、CLI、安全清单、历史模型指标汇总。
- 主要发现：知识库已经能支持有依据的内部 LLM Agent 查询；RAG 显著优于 no-KB/full-context，但仍有两个预设指标未达标。
- 未解决问题：正式许可证、full 测试可移植性、Windows CLI 编码、自然语言漏召回、SWM critical bug、SC2 运行时验证。
- 建议下一步：先修复严重级和一般级发布问题，再用全新冻结 v0.7 验证 RAG；许可证确认后才进入公开发布步骤。
