# Offer鹅 Codex 社区适配版

校园求职辅导技能：方向探索、能力建设、简历优化、面试准备、职业测评和职业路径规划；同时保留腾讯招聘公告、岗位、JD 和部门的实时查询脚本。

这是个人维护的非官方适配版，源于 WorkBuddy 的 `offer-e` 1.0.0 专家包，不代表腾讯、WorkBuddy 或 OpenAI，也不提供官方招聘身份、内推资格或录用承诺。名称仅用于说明上游来源。

## 许可状态

原包清单声明 `author.name: WorkBuddy`、`license: MIT`。本仓库按此声明附上 [MIT 文本](LICENSE)，并记录在 [NOTICE.md](NOTICE.md) 和 [来源证据](provenance/upstream-metadata.json) 中。

**原包没有独立 LICENSE，也没有明确的原作者版权年份/法律主体声明；本地清单不是额外取得的权利人授权。公开发布前应向上游确认许可声明的真实性及覆盖范围。** 不应把适配者写成全部原始内容的作者。第三方组件条款见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## 安装

需要能运行 Python 3.10+ 的 Codex 环境。腾讯数据查询还需要出站网络访问；测评为本地单文件 HTML。

把本仓库复制为用户技能目录中的 `offer-e` 文件夹，使入口位于 `<技能目录>/offer-e/SKILL.md`。在本机使用的是 `~/.codex/skills`（或已配置的 `CODEX_HOME/skills`）。不要把 `.git` 目录复制进安装目录。

Windows PowerShell 示例（先进入克隆后的仓库根目录）：

```powershell
$skillHome = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex\skills' }
$installDir = Join-Path $skillHome 'offer-e'
if (Test-Path -LiteralPath $installDir) { throw '已存在 offer-e；请先备份并检查现有版本，再更新。' }
New-Item -ItemType Directory -Path $installDir -Force | Out-Null
$archivePath = Join-Path ([System.IO.Path]::GetTempPath()) ('offer-e-' + [guid]::NewGuid().ToString() + '.zip')
git archive --format=zip --output=$archivePath HEAD
if ($LASTEXITCODE -ne 0) { throw '导出失败，请检查仓库是否已有提交。' }
Expand-Archive -LiteralPath $archivePath -DestinationPath $installDir
Remove-Item -LiteralPath $archivePath
```

在技能列表确认 `offer-e` 已出现；若当前会话未刷新，重新打开会话。推荐明确调用主入口：

```text
$offer-e 帮我梳理求职方向
$offer-e 根据我的项目经历做一轮模拟面试
$offer-e 查询腾讯校招的后端岗位
$offer-e 我想做职业测评
```

入口也可按描述自动匹配。包内保留 6 个阶段 `SKILL.md`，部分客户端会将它们分别发现；使用主入口可统一阶段判断。

## 内容与数据

- `SKILL.md`：主入口。
- `skills/`：6 个阶段/工具模块，以及离线测评 HTML。
- `references/`：辅导方法与参考资料。
- `scripts/`：腾讯查询、简历初检、风险识别和记忆辅助脚本。
- `references/templates/career-memory.md`：空白模板，可公开。

实际求职档案写入当前工作区的 `career-memory/offer-e-memory.md`，需用户同意；该目录已被 Git 忽略。不要提交简历、个人记忆、密钥、聊天记录或接口数据快照。`.gitignore` 不能保护已被跟踪或强制添加的文件，提交前仍应检查暂存内容。

腾讯查询直接调用 `join.qq.com`，不依赖 WorkBuddy SDK。脚本许可不等于腾讯网站内容的再分发许可，也不保证接口长期可用；本仓库不附带招聘数据快照。查询失败时说明实际错误并引导官网。

测评答案留在页面内存中；完成后把结果码发回对话。原有问卷和结果码协议保留，预览与报告呈现改用当前客户端可用的本地文件预览、Markdown 或 HTML。尚未完成所有客户端的端到端界面测试，不承诺与原 WorkBuddy 界面完全一致。

## 开发与安装副本

在源码仓库维护 Git，验证后再更新本机安装副本。源码目录和 `.codex/skills/offer-e` 没有自动同步关系。原 WorkBuddy 包不属于此仓库，也不会被安装步骤修改。
