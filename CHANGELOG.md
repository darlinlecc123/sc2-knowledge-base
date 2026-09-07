# Changelog

本文件记录 STORM PySC2 Raw API 变量知识库的公开发布变化。

## [0.1.0] - 2026-09-07

### Added

- 收录当前 STORM 主路径实际使用的 135 个正式变量。
- 建立 Raw API、TBox、ABox、派生状态、动作、SWM 与实验指标之间的 1430 条关系。
- 记录 11 个已知问题，并区分 `design_intent`、`code_reality`、`runtime_observation` 和 `needs_verification`。
- 提供确定性的本地自然语言检索、关系查询和证据返回。
- 提供面向 LLM 的上下文、QA Agent、离线题集、自动评分工具与人类可读文档。
- 提供 minimal/full 两种本地发布包、包内清单和 SHA-256 校验和。

### License

- 负责人已选择 Apache License 2.0，完整许可证写入根目录 `LICENSE`。
- 发布仓库：`https://github.com/darlinlecc123/sc2-knowledge-base`。

### Validation

- 步骤 17 文档验证通过：5 份文档、135 个正式变量、1430 条关系、11 个已知问题。
- 步骤 18 将在构建后实际解包 minimal 包并执行离线检索冒烟测试。
- 步骤 18 打包过程不调用外部模型 API，不启动 StarCraft II，也不上传文件。

### Known limitations

- V0.1 只覆盖当前 STORM 使用的 PySC2 Raw API 变量及直接衍生量，不是完整 PySC2/StarCraft II 百科。
- 需要真实 SC2 运行才能最终确认的内容继续标记为 `needs_verification`。
- 项目采用 Apache License 2.0；第三方名称、接口和资产仍受各自权利人的条款约束。
- 旧的步骤 16 planned-state 验证器与后来已经执行的真实模型评测状态不兼容，不作为本次发布门禁。
