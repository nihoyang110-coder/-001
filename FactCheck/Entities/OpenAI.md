---
type: entity
name: OpenAI
aliases: [OpenAI, ChatGPT, GPT-6, GPT-5, Codex, Sora, Altman]
tags: [entity]
last_reviewed: 2026-10-19
---
# OpenAI

## 一句话
ChatGPT 的开发商；产品线覆盖聊天（ChatGPT）、编程（Codex）、视频（Sora，API 已关停）和 API，2026 年主推 GPT-6 系列。

## 关键事实（摘自卡片，以卡片为准）
- 用户规模：自称 ChatGPT 每周约 12 亿用户（2026-09，公司自述）[[F-0164]]
- 模型：GPT-6 Astra（约 2026-09 初）→ GPT-6 Sol/Luna（09-22）→ GPT-6.1 Sol（09-29）[[F-0163]]
- 2026-10-07 起 ChatGPT 聊天里上线 GPT-6 + Intelligent UI，付费先、免费 10-08 起分批 [[F-0160]] [[F-0161]] [[F-0162]]
- 订阅：09-29 起新购 $200 Pro 限额约减半，新增 $500 Pro 500 [[F-0153]]
- Codex 2026-03 推出插件系统 [[F-0217]]（用户判定该话题“无用”）

## 时间线
- 2026-03 Codex 插件系统
- 2026-09 GPT-6 系列陆续发布；09-29 DevDay、$200 档限额调整
- 2026-10-07 GPT-6 + Intelligent UI 进入普通聊天

## 我们的判断与注意
- 用户数是周活口径的公司自述，不等于“推送人数”
- 模型命名多、迭代快：引用时写清具体型号和日期
- “生成式界面”不是 OpenAI 首创 [[F-0165]]

## 相关卡片（脚本生成，勿手改）
<!-- cards:start -->
| 卡片 | 状态 | 事实时间 | 命题 |
|---|---|---|---|
| [[F-0008]] | 已证实 | 2026-10-03 | Higgsfield 主要是聚合第三方视频模型（Veo、Kling、Seedance、WAN 等，曾含 Sora 2），不以自研大模型为主 |
| [[F-0012]] | 部分属实 | 2026-10-03 | Sora 2 API 已关停，Higgsfield 已下架 Sora 2 |
| [[F-0015]] | 待验证 |  | 到2027年10月，Google/OpenAI 的免费或广告补贴版本将明显压缩每月约20美元的个人（prosumer）AI 订阅市场 |
| [[F-0137]] | 已证实 | 2026-10-05 | 运行 Vibe-Trading 需要自己配置大模型（OpenRouter/OpenAI/Anthropic/DeepSeek 等 API，或本地 Ollama）；行情多来自 Yahoo、Stooq、腾讯、东方财富等公开接口 |
| [[F-0150]] | 已证实 | 2026-10 | SemiAnalysis 于 2026-10-05 发布《Anthropic Subscriptions Offer 5x+ More Value Than OpenAI》，实测 Anthropic、OpenAI、Meta、SpaceXAI、MiniMax、Moonshot、Zdotai、Cursor、Cognition 等订阅方案；方法是把《战争与和平》文本分块喂给付费账号，记录 5 小时与每周窗口的用量百分比，再按公开 API 价换算成“API 等价价值” |
| [[F-0152]] | 已证实 | 2026-10-07 | SemiAnalysis 测算：在 agentic 编程负载下，Claude $200 档的 Opus 5.5 订阅“API 等价价值”约为 OpenAI GPT-6.1 Sol 的 5 倍（不同报道写约 4 倍、5.6 倍） |
| [[F-0153]] | 已证实 | 2026-09 | OpenAI 自 2026-09-29 起新购 $200 Pro 限额约减半（此前购买者保留旧限额至 10-29）；同时推出 $500 的 Pro 500（含 Astra Ultrafast 等），其 Astra 额度只比旧 $200 档多约 21%；Pro 100/200/500 每美元 token 数基本相同 |
| [[F-0155]] | 已证实 | 2026-10-07 | Opus 5.5 发布时 Anthropic API 降价（输入/输出约 -20%、缓存读取约 -60%），并把 Max 档 Opus 额度提高约 20%、Pro 档约 50%；GPT-6.1 Sol 缓存读取降价 50% 但 $200 档 token 限额未变，API 等价价值下降约 30% |
| [[F-0157]] | 存疑 | 2026-10-07 | “OpenAI 没有 Claude 那种 5 小时滚动限制” |
| [[F-0158]] | 观点 |  | “AI 厂商把付费用户当猴耍”“Anthropic 捏着鼻子疯狂补贴、OpenAI 早就把水龙头拧死”“Fable 5.1 补贴明显收紧，两边都在准备收水关闸” |
| [[F-0159]] | 待验证 |  | 评论观点：OpenAI 的 $500 档与 Opus 用满时约 -369% 的毛利“不可能长期并存”，主要厂商的高价订阅额度将进一步收紧 |
| [[F-0160]] | 已证实 | 2026-10 | OpenAI 于 2026-10-07 发布《GPT-6 and Intelligent UI for everyone》：ChatGPT 的普通聊天（Chat）里上线 GPT-6，回答可按问题自动组合文字、图表、按钮、表单、地图以及计算器、分账器、小游戏等临时小工具；OpenAI 自己承认模型的“设计判断仍需改进” |
| [[F-0161]] | 部分属实 | 2026-10 | GPT-6 + Intelligent UI 在 ChatGPT 中是分批推送：2026-10-07 先给 Plus、Pro、Business、Enterprise（企业版视管理员设置），Free 和 Go 从 10-08 起陆续推送；并非“10 月 7 日全员覆盖” |
| [[F-0162]] | 已证实 | 2026-10-08 | 在 ChatGPT 聊天中，付费档用 GPT-6 Sol、Free/Go 档用 GPT-6 Luna；免费档的用量上限 OpenAI 未公布 |
| [[F-0163]] | 已证实 | 2026-10 | “GPT-6”不是 2026-10-07 才首发：GPT-6 Astra 约 2026-09-03/04 发布；GPT-6 Sol 与 Luna 于 2026-09-22 在 ChatGPT Work、Codex 和 API 上线（免费用户只能在桌面 App 用 Luna）；GPT-6.1 Sol 于 09-29 DevDay 发布。10-07 的新变化是把 GPT-6 带进普通聊天并配上 Intelligent UI |
| [[F-0164]] | 公司自述 | 2026-09 | OpenAI 称 ChatGPT 每周约有 12 亿用户（DevDay 2026，2026-09-29；AFP 报道引用）；这是周活口径，且 OpenAI 未给出免费/付费拆分 |
| [[F-0165]] | 已证实 | 2025-11 | 在回答里直接生成可交互界面并非 OpenAI 首创：Google 于 2025-11-18 随 Gemini 3 推出“动态视图”生成式界面；Anthropic 于 2026-03-12 在 Claude 聊天中推出内联交互图表（beta）；ChatGPT 此前也已有 Visualizations 预览和 2025-10 的 Apps SDK（第三方应用界面嵌入对话） |
| [[F-0166]] | 观点 |  | “功能单一的小工具 App 护城河一夜清零” |
| [[F-0167]] | 待验证 |  | 到 2027-04，单一功能工具类 App（计算器、单位换算、分账等）的全球下载量或使用量将因聊天机器人内置交互工具而明显下滑 |
| [[F-0168]] | 观点 |  | “AI 正式从聊天框跨向操作系统层” |
| [[F-0180]] | 已证实 | 2026-01 | Meta 自 2026-01-15 起禁止“以 AI 为主要功能”的通用聊天机器人（如 ChatGPT、Perplexity）使用 WhatsApp Business API；企业用 AI 做客服不在禁止范围；搜索中未见 Messenger 有同类禁令 |
| [[F-0207]] | 公司自述 | 2026-10-19 | OpenAI 支持的 AI 辅助动画长片《Critterz》计划预算不到 3000 万美元、制作 9 个月（大厂动画长片通常 1–2 亿美元、约 3 年），目标 2026 年 5 月戛纳首映；约 30 名贡献者按定制模式分享利润；仍使用人类配音、原画和剧本 |
| [[F-0217]] | 已证实 [无用] | 2026-03 | OpenAI Codex 于 2026-03 推出插件系统（把技能、应用和 MCP 服务器打包安装）；首批官方插件约 12 个，据报道包括 Box、Cloudflare、Figma、GitHub、Gmail、Google Drive、Hugging Face、Linear、Notion、Sentry、Slack、Vercel |
| [[F-0218]] | 部分属实 [无用] | 2026-10-19 | “8 个技能包让 Codex 自动干活”：GitHub、Figma、Sentry、Vercel、Linear 有官方 Codex 插件；Supabase 有插件但是否在官方名单说法不一；Context7（文档查询）和 Playwright（浏览器操作）主要以 MCP 服务器形式接入，Playwright 也在 OpenAI 精选技能里；各项功能描述大体正确 |
<!-- cards:end -->
