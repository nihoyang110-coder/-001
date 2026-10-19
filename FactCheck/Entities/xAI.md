---
type: entity
name: xAI
aliases: [xAI, SpaceXAI, Grok, Grok Bot, SuperGrok, SpaceX, 马斯克, Musk]
tags: [entity]
last_reviewed: 2026-10-19
---
# xAI

## 一句话
马斯克的 AI 公司（并入 SpaceX 后常称 SpaceXAI），产品为 Grok 模型、SuperGrok 订阅和 Grok Bot 智能体。

## 关键事实（摘自卡片，以卡片为准）
- Grok Bot：2026-08 测试版，每个 Bot 一台云电脑，可多 Bot 协作、定时任务 [[F-0170]]
- 马斯克 2026-10-07 称 Grok Bot 将按任务调用 Claude Opus 5.5、Midjourney、Suno 等，细节未公布 [[F-0169]]
- 按牌价 Grok 4.7 约 2/6 美元每百万 token，比 Opus 5.5 便宜 2–3 倍 [[F-0176]]
- 向 Anthropic 出租算力，每月约 12.5 亿美元（招股书报道）[[F-0177]]

## 时间线
- 2025 Anthropic 曾切断 xAI 经 Cursor 使用 Claude [[F-0172]]
- 2026-05 SpaceX 招股书披露 Anthropic 算力协议
- 2026-08 Grok Bot 测试版；2026-10-07 宣布多模型路由

## 我们的判断与注意
- “我已把 Grok Bot 当模型路由用”的演示其实是 Bot 间转发 [[F-0171]]
- 预测待回看：2027-01-08 前官方文档是否列出 Claude [[F-0175]]

## 相关卡片（脚本生成，勿手改）
<!-- cards:start -->
| 卡片 | 状态 | 事实时间 | 命题 |
|---|---|---|---|
| [[F-0150]] | 已证实 | 2026-10 | SemiAnalysis 于 2026-10-05 发布《Anthropic Subscriptions Offer 5x+ More Value Than OpenAI》，实测 Anthropic、OpenAI、Meta、SpaceXAI、MiniMax、Moonshot、Zdotai、Cursor、Cognition 等订阅方案；方法是把《战争与和平》文本分块喂给付费账号，记录 5 小时与每周窗口的用量百分比，再按公开 API 价换算成“API 等价价值” |
| [[F-0169]] | 已证实 | 2026-10 | 马斯克 2026-10-06/07 在 X 发帖：今后 SpaceX 会为 Grok Bot 的每个任务选择最合适的后端模型，包括 Claude Opus 5.5、Midjourney、Suno 等主流 API；未公布哪些任务走哪个模型，官方文档也尚未写明 |
| [[F-0170]] | 已证实 | 2026-08 | Grok Bot 是 xAI（SpaceXAI）2026-08 推出的测试版智能体产品：每个 Bot 有自己的云电脑和记忆，多个 Bot 可并行、在同一线程里互相交接任务，可设一个“主管 Bot”调度其他 Bot；支持定时或事件触发的 Routines、插件和 MCP |
| [[F-0171]] | 存疑 | 2026-10-08 | 截图里被称为“模型路由”的演示，画面实际显示的是主 Bot（SuperGrok）给另一个 Bot（indigo-mind）发消息、再把对方回复转给用户——这是 Grok Bot 官方的多 Bot 协作功能；画面本身无法证明调用了其他厂商的模型（唯一线索是会话名“Gemini 润色版”）；有资料称用户不能在 Grok Bot 里手动选底层模型 |
| [[F-0172]] | 已证实 | 2026-10 | 截至 2026-10-08，未见 Anthropic 就 Grok Bot 调用 Claude 公开回应；Anthropic 商业条款限制客户用 Claude 构建竞品，2025 年曾切断 xAI 经 Cursor 使用 Claude 的权限；2026-05 Anthropic 与 SpaceX 签了算力协议，两家已有商业往来 |
| [[F-0175]] | 待验证 |  | 到 2027-01-08，xAI/SpaceXAI 会在 Grok Bot 官方文档或发布说明里明确列出会调用的第三方模型（如 Claude Opus 5.5），且 Anthropic 不公开反对 |
| [[F-0176]] | 已证实 | 2026-10 | 第三方价格汇总（2026-10-11）显示：Claude Opus 5.5 API 每百万 token 输入约 4 美元、输出约 20 美元；Grok 4.7 输入约 2 美元、输出约 6 美元（≤20 万上下文）。按牌价，同样的活交给 Opus 输入约贵 2 倍、输出约贵 3.3 倍 |
| [[F-0177]] | 已证实 | 2026-05 | 据 SpaceX 招股书（S-1，2026-05-20 提交）的报道：Anthropic 每月向 SpaceX 支付约 12.5 亿美元，租用 Memphis 的 Colossus 1/2 算力，约定至 2029 年 5 月，总额约 450 亿美元，双方可提前 90 天通知终止；马斯克另称这只是 180 天租约，路透指出招股书未提及 6 个月期限 |
<!-- cards:end -->
