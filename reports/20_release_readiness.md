# 步骤 20 完成报告：准备 GitHub 开源与持续维护

- 执行日期：2026-09-07
- 状态：**本地发布材料完成；GitHub 上传已获授权，等待最终提交与 push**
- 版本：`0.1.0`
- 发布边界：只允许候选文件来自 `knowledge/`
- 外部账号访问：未执行
- GitHub 建仓或 push：未执行
- STORM 业务源码：未修改

## 1. 简明结论

步骤 20 已完成 GitHub 首页、贡献指南、Issue/PR 模板、版本路线图、维护流程和公众号文章草稿。为落实“只能上传 knowledge 文件夹”的附加要求，增加了候选上传白名单和离线校验脚本。

后续授权更新（2026-09-07）：

1. 用户已提供空仓库 `https://github.com/darlinlecc123/sc2-knowledge-base.git`；
2. 用户已选择 Apache License 2.0；
3. `knowledge/` 已作为独立 Git 仓库初始化，远程仓库只读检查成功且为空；
4. 上传仍必须通过白名单、敏感信息扫描和暂存路径审计。

## 2. 读取的关键证据

- `knowledge/prompts/20_prepare_github_release.md`
- `knowledge/reports/18_build_release_package.md`
- `knowledge/reports/19_acceptance_checklist.md`
- `knowledge/reports/19_acceptance_result.yaml`
- `knowledge/reports/19_open_issues.md`
- `knowledge/release/MANIFEST.json`
- `knowledge/release/README_RELEASE.md`
- `knowledge/CHANGELOG.md`
- `knowledge/CITATION.cff`
- `knowledge/LICENSE_CANDIDATE.md`
- `knowledge/reports/multi_model_evaluation/multi_model_test_report.md`

发布事实以已有机器可读数据、源码证据、测试和评测报告为依据，没有把步骤提示词当作变量事实来源。

## 3. 新建文件

### 指定产物

- `knowledge/github/README_GITHUB.md`
- `knowledge/github/CONTRIBUTING.md`
- `knowledge/github/ROADMAP.md`
- `knowledge/github/ISSUE_TEMPLATE/variable_request.md`
- `knowledge/github/ISSUE_TEMPLATE/bug_report.md`
- `knowledge/github/PULL_REQUEST_TEMPLATE.md`
- `knowledge/docs/wechat_article_draft.md`
- `knowledge/reports/20_release_readiness.md`

### 安全辅助产物

- `knowledge/github/PUBLISH_ALLOWLIST.txt`：候选上传白名单；路径均相对 `knowledge/`。
- `knowledge/scripts/validate_github_release.py`：离线检查必需文件、路径越界、禁止目录、缓存、日志、密钥形态和私人 Windows 路径。

增加辅助文件的原因：单靠人工执行 `git add` 无法可靠保证“只上传 knowledge 文件”，白名单与脚本提供可重复的机器门禁。

## 4. 仓库首页与对外口径

发布首页明确说明：

- V0.1 只覆盖当前 STORM 主路径使用的 Raw API 变量及直接衍生量；
- 当前规模为 135 个正式变量、1430 条关系和 11 个已知问题；
- 知识事实区分 `design_intent`、`code_reality`、`runtime_observation` 和 `needs_verification`；
- 本项目不是 Blizzard Entertainment、DeepMind、PySC2 或 StarCraft II 权利人的官方产品或官方背书；
- 当前仅存在许可证候选说明，未擅自宣称 MIT、Apache-2.0 或其他许可证生效；
- RAG 有明显价值，但 challenge v0.6 首次盲测尚未通过全部冻结门槛。

## 5. 贡献与维护流程

变量新增或修改 PR 被要求提供：

1. 稳定 ID 和层级；
2. 当前 STORM 相对源码路径与类、函数或符号；
3. 接口类型、形状、单位、范围或枚举；
4. 来源、归一化、映射、派生、校验和动作执行关系；
5. 别名、查询模式和歧义反例；
6. Schema、检索、关系端点和证据绑定测试；
7. 事实状态与待验证项；
8. 安全检查和实际执行的验证命令。

维护职责建议分为：

- 知识记录维护者：Schema、变量、血缘和文档一致性；
- 检索维护者：别名、变量族、公式依赖和范围外拒答；
- 评测维护者：冻结题集、哈希、首次盲测和回归集边界；
- 发布维护者：许可证状态、安全扫描、确定性打包和版本说明；
- STORM 业务代码负责人：处理需要修改原项目实现的 SWM、Function ID 和 ontology cache 问题。

## 6. 发布边界设计

建议后续把 `knowledge/` 本身作为独立 Git 仓库根目录，而不是在 `storm111/` 根目录执行全量暂存。这样父目录中的 `agents/`、`ontology/`、`examples/`、`main.py` 等文件在结构上就无法进入提交。

即使如此，也不能盲目上传 `knowledge/` 的全部内容。`evals/configs/`、`evals/results/`、缓存、日志和可能包含私人路径的历史文件应继续排除。候选上传必须以 `github/PUBLISH_ALLOWLIST.txt` 为准，并在提交前运行离线校验。

## 7. 验证命令与结果

已实际执行：

```powershell
python -m py_compile knowledge\scripts\validate_github_release.py
python knowledge\scripts\validate_github_release.py
```

第一次验证发现并拦截了两类不适合公开的内容：现有《知识库使用说明》中的私人绝对路径/配置示例，以及 Python `__pycache__`。处理方式不是放宽规则，而是将该历史说明移出候选白名单，并在目录展开时排除缓存。

修正后验证结果：

```text
GITHUB_RELEASE_VALIDATION_OK
allowlisted_files=95
outside_knowledge_files=0
network_accessed=false
uploaded=false
```

结论：95 个候选文件全部位于 `knowledge/`，未命中禁止目录、缓存、日志、私人 Windows 路径或密钥形态。该检查没有访问网络、调用模型 API或启动 StarCraft II。

## 8. 未解决问题

- 已解决：用户选择 Apache License 2.0，并提供目标 GitHub 仓库。
- 待后续完善：个人作者列表和版权主体展示信息仍可补充，但不再阻塞本次 Apache-2.0 初始发布。
- full 包干净目录测试仍存在 `ModuleNotFoundError: sc2kb`。
- Windows 默认 GBK 下 CLI 完整 JSON 仍可能发生编码错误。
- `environment.step_mul` 的自然语言改写仍有漏召回。
- 尚未在 Python 3.12 + uv 环境执行本轮发布验收。
- GitHub Actions 离线发布边界检查已生成，待 push 后由 GitHub 首次执行。

## 9. 远程操作记录

- GitHub 登录：**未执行**
- 创建远程仓库：**未执行**
- Git 初始化：**已执行，仅在 knowledge/.git**
- Git 暂存/提交：**未执行**
- Git push：**未执行**
- GitHub Release：**未执行**
- 公众号发布：**未执行**

## 10. 建议下一步

1. 使用已确认的 Apache License 2.0 和目标空仓库；
2. 以 `knowledge/` 为独立仓库根目录，按白名单生成候选提交；
3. 在暂存后检查 `git diff --cached --name-only`，要求所有路径都属于候选知识库文件；
4. 通过安全校验后再提交和 push；
5. 上传 minimal/full ZIP 时使用 GitHub Release 附件，而不是把二进制包混入源码提交。
