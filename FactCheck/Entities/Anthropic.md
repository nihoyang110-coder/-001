---
type: entity
name: Anthropic
aliases: [Anthropic, Claude, Opus, Sonnet, Fable, Claude Code, Cowork]
tags: [entity]
last_reviewed: 2026-10-19
---
# Anthropic

## 一句话
Claude 系列模型的开发商；产品包括 Claude 聊天、Claude Code（编程智能体）、Cowork 和 API。

## 关键事实（摘自卡片，以卡片为准）
- 订阅：SemiAnalysis 测算 $200 档 Opus 5.5 的“API 等价价值”约为 OpenAI 同档 5 倍（价值≠额度）[[F-0152]]；用满额度时建模毛利约 -369% [[F-0154]]
- Opus 5.5 发布时 API 降价约 20%、缓存读取约 -60% [[F-0155]]；第三方价格表 Opus 5.5 约 4/20 美元每百万 token [[F-0176]]
- 与 SpaceX 关系：每月约付 12.5 亿美元租算力（招股书报道）[[F-0177]]；对马斯克称 Grok Bot 将调用 Claude 尚未回应 [[F-0172]]
- 生态：Claude Code 被大量用于开源项目（CADCraft 约 82% 提交带 Claude 标记 [[F-0186]]；电视改造 [[F-0211]]）

## 时间线
- 2026-03-12 Claude 聊天内联交互图表 beta [[F-0165]]
- 2026-05 与 SpaceX 签算力协议
- 2026-10 Opus 5.5 发布（API 降价、额度上调）

## 我们的判断与注意
- **利益说明**：本库由 Anthropic 的 Claude 维护，涉及 Anthropic 的卡片只依据外部来源，对竞品同一标准
- 订阅“价值倍数”是按 API 牌价换算，不能说成额度倍数

## 相关卡片（脚本生成，勿手改）
<!-- cards:start -->
| 卡片 | 状态 | 事实时间 | 命题 |
|---|---|---|---|
| [[F-0121]] | 已证实 | 2026-10-05 | image-blaster 本身不含生成模型：它是一组 Claude Code 技能（skills/agents/脚本）加一个 React 查看器，把 World Labs Marble、nano-banana、gpt-image-2、混元3D（经 FAL）、ElevenLabs 音效等商业 API 串起来 |
| [[F-0122]] | 已证实 | 2026-10-05 | 运行 image-blaster 需要 World Labs 和 FAL 两个付费 API 密钥，并需要安装 Claude Code |
| [[F-0137]] | 已证实 | 2026-10-05 | 运行 Vibe-Trading 需要自己配置大模型（OpenRouter/OpenAI/Anthropic/DeepSeek 等 API，或本地 Ollama）；行情多来自 Yahoo、Stooq、腾讯、东方财富等公开接口 |
| [[F-0150]] | 已证实 | 2026-10 | SemiAnalysis 于 2026-10-05 发布《Anthropic Subscriptions Offer 5x+ More Value Than OpenAI》，实测 Anthropic、OpenAI、Meta、SpaceXAI、MiniMax、Moonshot、Zdotai、Cursor、Cognition 等订阅方案；方法是把《战争与和平》文本分块喂给付费账号，记录 5 小时与每周窗口的用量百分比，再按公开 API 价换算成“API 等价价值” |
| [[F-0152]] | 已证实 | 2026-10-07 | SemiAnalysis 测算：在 agentic 编程负载下，Claude $200 档的 Opus 5.5 订阅“API 等价价值”约为 OpenAI GPT-6.1 Sol 的 5 倍（不同报道写约 4 倍、5.6 倍） |
| [[F-0154]] | 已证实 | 2026-10-07 | SemiAnalysis 建模：$200 档用户若把 Opus 5.5 额度用满，Anthropic 在该用户上的毛利率约 -369%；用满 Fable 5.1 约 +1%；订阅约占收入 10% 却占推理算力 40% 以上 |
| [[F-0155]] | 已证实 | 2026-10-07 | Opus 5.5 发布时 Anthropic API 降价（输入/输出约 -20%、缓存读取约 -60%），并把 Max 档 Opus 额度提高约 20%、Pro 档约 50%；GPT-6.1 Sol 缓存读取降价 50% 但 $200 档 token 限额未变，API 等价价值下降约 30% |
| [[F-0157]] | 存疑 | 2026-10-07 | “OpenAI 没有 Claude 那种 5 小时滚动限制” |
| [[F-0158]] | 观点 |  | “AI 厂商把付费用户当猴耍”“Anthropic 捏着鼻子疯狂补贴、OpenAI 早就把水龙头拧死”“Fable 5.1 补贴明显收紧，两边都在准备收水关闸” |
| [[F-0159]] | 待验证 |  | 评论观点：OpenAI 的 $500 档与 Opus 用满时约 -369% 的毛利“不可能长期并存”，主要厂商的高价订阅额度将进一步收紧 |
| [[F-0165]] | 已证实 | 2025-11 | 在回答里直接生成可交互界面并非 OpenAI 首创：Google 于 2025-11-18 随 Gemini 3 推出“动态视图”生成式界面；Anthropic 于 2026-03-12 在 Claude 聊天中推出内联交互图表（beta）；ChatGPT 此前也已有 Visualizations 预览和 2025-10 的 Apps SDK（第三方应用界面嵌入对话） |
| [[F-0169]] | 已证实 | 2026-10 | 马斯克 2026-10-06/07 在 X 发帖：今后 SpaceX 会为 Grok Bot 的每个任务选择最合适的后端模型，包括 Claude Opus 5.5、Midjourney、Suno 等主流 API；未公布哪些任务走哪个模型，官方文档也尚未写明 |
| [[F-0172]] | 已证实 | 2026-10 | 截至 2026-10-08，未见 Anthropic 就 Grok Bot 调用 Claude 公开回应；Anthropic 商业条款限制客户用 Claude 构建竞品，2025 年曾切断 xAI 经 Cursor 使用 Claude 的权限；2026-05 Anthropic 与 SpaceX 签了算力协议，两家已有商业往来 |
| [[F-0175]] | 待验证 |  | 到 2027-01-08，xAI/SpaceXAI 会在 Grok Bot 官方文档或发布说明里明确列出会调用的第三方模型（如 Claude Opus 5.5），且 Anthropic 不公开反对 |
| [[F-0176]] | 已证实 | 2026-10 | 第三方价格汇总（2026-10-11）显示：Claude Opus 5.5 API 每百万 token 输入约 4 美元、输出约 20 美元；Grok 4.7 输入约 2 美元、输出约 6 美元（≤20 万上下文）。按牌价，同样的活交给 Opus 输入约贵 2 倍、输出约贵 3.3 倍 |
| [[F-0177]] | 已证实 | 2026-05 | 据 SpaceX 招股书（S-1，2026-05-20 提交）的报道：Anthropic 每月向 SpaceX 支付约 12.5 亿美元，租用 Memphis 的 Colossus 1/2 算力，约定至 2029 年 5 月，总额约 450 亿美元，双方可提前 90 天通知终止；马斯克另称这只是 180 天租约，路透指出招股书未提及 6 个月期限 |
| [[F-0182]] | 已证实 | 2026-04 | Higgsfield 官方 MCP 服务器（mcp.higgsfield.ai，OAuth 登录，无需 API 密钥）约 2026-04-30 上线，可在 Claude 网页版、Cowork、Claude Code 等环境调用 Higgsfield 的 30 多个图像/视频模型；需要 Higgsfield 付费订阅 |
| [[F-0184]] | 存疑 | 2026-10-14 | 帖子称 Claude 通过 Higgsfield MCP 生成后“档案直接存进我的资料夹”：未见官方说明；在 Cowork、Claude Code 这类能读写本地文件的环境里可以做到，网页版 Claude 通常要手动下载 |
| [[F-0186]] | 已证实 | 2026-10-16 | “老外用 Claude 做的”：CADCraft 首次提交者为 ArtCraft 作者 Brandon Thomas；491 次提交中约 403 次带 Claude 共同作者标记，仓库有专门写给 AI 代理的 CLAUDE.md，路线图用“Opus 5.5 代理小时”估算剩余工作量；另有约 10 位社区贡献者 |
| [[F-0191]] | 已证实 | 2026-10-16 | FreeCAD 没有官方 MCP；社区有多个 MCP 插件（如 neka-nat/freecad-mcp、theosib/FreeCAD-MCP-Server、spkane/freecad-mcp），可让 Claude 等通过自然语言建模，但通常需要打开 FreeCAD 图形界面并安装插件 |
| [[F-0211]] | 已证实 | 2026-10 | tv-vibehack（10-19 改名 cleanyourtv）由 Gathin23 于 2026-10-17 发布：他用 Claude Code 通过 Wi-Fi ADB 连上父母的小米电视 4A（国际版，Android TV 10），停用 25 个小米预装包，并写了一个仿 Apple TV 主屏的启动器；MIT 开源，不 root、不卸载（只用 pm disable-user），可一键恢复；到 10-20 已有 202 次提交、37 位贡献者、30 多个机型清单 |
| [[F-0214]] | 已证实 | 2026-10-19 | 这不是首创：2026 年 9 月初，开发者 Mert Cobanov 已公开用 Claude Code 通过 ADB 清理一台 4 年旧 Android TV 的提示词，做法同样是只停用不卸载，并安装第三方启动器 FLauncher |
| [[F-0221]] | 已证实 | 2026-10-20 | “CAD 行业迎来 Claude 时刻”的说法：SKY-001 由 Skyfall AI 开发，与 Anthropic 和 Claude 无关；“Claude 时刻”是借 Claude Code 在编程领域的影响做比喻。“干翻几乎所有前沿模型”只基于公司自家测试，暂无独立评测 |
| [[F-0228]] | 已证实 | 2026-10-20 | GitHub EL4CTEO/blender-skills（视频里的“22 个 Blender Skill”）：MIT 许可，首次提交 2026-10-14，要求 Blender 5.2+；22 个技能覆盖场景设置、硬表面建模、雕刻、重拓扑与 UV、PBR 材质、烘焙、几何节点、绑定、表情、动画、游戏优化、导出（Roblox/Unity/Unreal/Godot/网页/USD）、渲染、灯光、模拟、天气、插件开发、批处理、资产质检等；可装进 Claude Code、Codex、Gemini CLI、Copilot、Cursor 等 |
| [[F-0231]] | 已证实 | 2026-09 | 社区项目 MCP for Blender（原名 blender-mcp，作者 Siddharth Ahuja，MIT）：约 2.9 万星（2026-09-20），让 Claude、Codex、Cursor 等通过 MCP 读取场景、执行 Python、搜索导入 Poly Haven/Sketchfab 素材、调用 3D 生成服务；2026 年披露两个漏洞：execute_blender_code 不做沙箱即执行代码（CVE-2026-10688）、Poly Haven 下载路径穿越可写任意文件（CVE-2026-66004，1.6.5 修复） |
| [[F-0232]] | 已证实 | 2026-04 | Blender 官方实验室（Blender Lab）MCP 服务器 v1.0.0 于 2026-04-27 发布，GPL-3.0+，需要 Blender 5.1+，定位“刻意做小”、偏分析调试和脚本；Anthropic 的 Claude Blender 连接器使用它；Blender 基金会主席称 Blender 目前没有、也不计划内置生成式 AI |
| [[F-0254]] | 已证实 | 2026-10-26 | CS146S 2026 秋季版前 5 周作业：①用 mitmproxy 抓包拆解一次真实 Claude Code 会话的请求；②给第三方 API 写 MCP 服务器，评分看“模型能否选对工具、调对参数、出错后恢复”，并要求 OAuth；③写一个技能（Skill），评分 流程 15/技能 60/测试 25，要求 3 个应触发和 1 个“不该触发”的测试；④给陌生开源仓库写 AGENTS.md 或 CLAUDE.md；⑤用 Factory 的 Droid 给 3 个开源仓库跑“智能体就绪度”报告并比较 |
| [[F-0256]] | 已证实 | 2026-01-12 | MIT《The Missing Semester of Your CS Education》2026 年 1 月改版：保留 4 讲修订、新增 5 讲，其中一讲是 Agentic Coding（智能体编程，讲 Claude Code、Codex CLI、opencode、MCP、AGENTS.md、子智能体、沙箱），并单列 AI 使用礼仪 |
| [[F-0257]] | 公司自述 | 2026-03-02 | Anthropic Academy 提供免费课程（据报道 2026-03-02 上线、13 门、托管在 Skilljar、邮箱注册、有结课证书），包括 Claude Code in Action、Introduction to Model Context Protocol、Building with the Claude API |
<!-- cards:end -->
