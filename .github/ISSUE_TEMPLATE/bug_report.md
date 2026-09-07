---
name: 知识库缺陷报告
about: 报告错误变量、错误证据、漏召回、误召回或工具故障
title: "[Bug] "
labels: ["bug", "needs-triage"]
assignees: []
---

## 缺陷类型

- [ ] 变量定义错误
- [ ] 接口形式错误
- [ ] 源码证据错误或过时
- [ ] 自然语言漏召回
- [ ] 无关变量误召回
- [ ] 证据绑定错误
- [ ] CLI/QA Agent 故障
- [ ] 文档与机器记录不一致
- [ ] 发布包或跨平台问题

## 复现问题

请提供完整查询、命令或最小输入。删除 API Key、访问令牌和个人路径。

## 实际结果

粘贴必要的非敏感输出，并说明使用的知识库版本。

## 期望结果

请给出预期变量 ID、行为或证据。

## 证据

- STORM 相对源码路径与符号：
- 知识库记录路径：
- PySC2/SC2 版本（如相关）：
- 操作系统和 Python 版本：

## 事实状态

该问题涉及 design_intent、code_reality、runtime_observation 还是 needs_verification？

## 安全检查

- [ ] 已移除 API Key、Bearer token、Cookie 和私人绝对路径
- [ ] 未上传 StarCraft II 游戏资产
