# 步骤 19：开放缺陷与修复责任

- 日期：2026-09-07
- 总体结论：`conditional_go`
- 责任人使用角色而非虚构姓名；由项目负责人后续分配到个人。

## 1. 阻断级（Blocker）

### B-001 正式开源许可证和版权主体未确认

- 状态：open
- 影响：阻断 GitHub 公开发布、第三方复制和再分发授权。
- 证据：只有 `LICENSE_CANDIDATE.md`，没有已生效的 `LICENSE`；`release/MANIFEST.json` 为 `pending_owner_confirmation`。
- 修复负责人：项目负责人 / 导师 / 机构知识产权负责人。
- 完成标准：确定版权主体、作者列表、第三方兼容性和正式许可证；同步更新 LICENSE、CITATION、README 和 manifest。

## 2. 严重级（Severe）

### S-001 RAG 未越过全部预设有效性门槛

- 状态：open
- 影响：不能宣传为已经通过无偏泛化门槛的“有效 RAG”。
- 证据：v0.6 首次盲测 variable hit rate=84.03%（门槛 85%），native JSON=98%（门槛 99%）。
- 修复负责人：知识库检索负责人 / QA Agent 负责人。
- 建议：只在非 challenge 开发集修复多变量展开、公式依赖和歧义；随后冻结全新 v0.7，仅做一次首次盲测。
- 完成标准：新冻结题集全部预设门槛通过。

### S-002 full 包中的离线测试不能在干净解压目录直接运行

- 状态：open
- 影响：full 包目前不是完全独立的一键复现包。
- 证据：解压后执行 `tests/validate_step17.py` 返回 `ModuleNotFoundError: No module named 'sc2kb'`。
- 修复负责人：发布工程负责人。
- 建议：将包做成可安装 Python project，或让测试按包根动态添加 `src`；统一去除对外层 `knowledge/` 目录的硬编码。
- 完成标准：在全新临时目录安装依赖后，可直接运行发布包声明的全部离线测试。

### S-003 Windows 默认 GBK 下 CLI 完整 JSON 可能崩溃

- 状态：open
- 影响：某些包含数学字符的变量记录无法从普通 PowerShell 稳定输出。
- 证据：查询“SWM overall error 的计算公式”时，`json.dumps` 输出触发 `UnicodeEncodeError`；设置 `PYTHONIOENCODING=utf-8` 后通过。
- 修复负责人：本地检索/CLI 负责人。
- 建议：CLI 启动时安全设置 UTF-8 输出，或提供 ASCII fallback；补 Windows 编码回归测试。
- 完成标准：默认 Windows PowerShell 中所有 135 条变量的 JSON 输出不崩溃。

### S-004 SWM error 使用 future state 作为预测基线

- 状态：open
- 影响：SWM health/position RMSE 可能无法衡量真正预测误差，论文指标解释风险高。
- 证据：`ontology/swm_predictor.py::compute_prediction_error` 第 270–289 行附近；对应 `issue.swm_error_uses_future_state_as_baseline`，severity=critical。
- 修复负责人：STORM/SWM 业务代码负责人。
- 建议：保存预测起点状态，并用起点 + delta 与未来真值比较；补静态和端到端测试。
- 完成标准：公式、实现、测试和知识库记录一致，重新运行相关实验。

## 3. 一般级（General）

### G-001 自然语言改写对 environment.step_mul 存在漏召回

- 状态：open
- 证据：“环境每次决策跨多少游戏步”返回 `not_found`；显式包含 `step_mul` 时可以召回。
- 修复负责人：检索与别名字典负责人。
- 完成标准：在非 challenge 改写集稳定命中，且不造成明显过度展开。

### G-002 validate_step16.py 已经过时

- 状态：open
- 证据：21 个离线测试中唯一失败，仍断言 `status == planned`。
- 修复负责人：评测工程负责人。
- 完成标准：改为验证 executed manifest/结果，或将 planned 协议验证器明确归档，不再进入当前测试套件。

### G-003 未在仓库指定的 Python 3.12 + uv 环境完成本轮验收

- 状态：open
- 证据：本机 `uv` 不可用，`.python-version` 为 3.12，本轮实际使用 Python 3.13.5。
- 影响：知识包本身要求 Python >=3.11 且测试通过，但尚缺目标工具链复核。
- 修复负责人：环境/发布负责人。
- 完成标准：CI 或干净机器使用 Python 3.12、`uv sync` 重跑离线套件和发布包验收。

### G-004 两类运行时兼容性尚未验证

- 状态：open
- 内容：硬编码 Raw Function IDs 需对当前 PySC2 ActionSpec 验证；ontology pickle 可能与源码不一致。
- 修复负责人：SC2 环境负责人 / ontology 负责人。
- 完成标准：在已固定版本的 SC2/PySC2 环境中执行 ActionSpec 和 ontology cache 一致性测试。

## 4. 建议级（Suggestion）

### P-001 更新或归档旧 knowledge/README.md

旧 README 仍声称制作和模型评测未执行。建议改为指向 `release/README_RELEASE.md`，避免维护者误判进度。

### P-002 完善 CITATION.cff 作者和永久链接

当前使用组织作者占位，没有编造个人、DOI 或 GitHub URL。正式发布时由负责人补齐。

### P-003 建立跨平台 CI

建议至少覆盖 Windows/Python 3.12 和一个 UTF-8 Linux 环境，自动执行 schema、检索、challenge freeze、发布包 clean-room 和安全扫描。

## 5. 结论与责任边界

- 知识库维护者可处理：S-001、S-002、S-003、G-001、G-002、P-001～P-003。
- STORM 业务代码负责人处理：S-004、G-004。
- 项目负责人处理：B-001。
- 在 B-001 未解决前，公开发布保持 `no_go`；内部受控 LLM Agent 使用保持 `conditional_go`。
