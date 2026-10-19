---
type: entity
name: World Labs
aliases: [World Labs, Marble, image-blaster, 李飞飞]
tags: [entity]
last_reviewed: 2026-10-19
---
# World Labs

## 一句话
李飞飞创办的“空间智能”公司，产品 Marble 可从图片生成可漫游的 3D 世界（高斯泼溅），并提供 API。

## 关键事实（摘自卡片，以卡片为准）
- Marble API：1 美元 = 1250 点，生成一个世界 1500 点（约 1.2 美元）[[F-0126]]
- 开源项目 image-blaster 的作者来自 World Labs 设计团队，被官网作为展示案例 [[F-0125]]；它本身是调用 Marble 等付费 API 的调度工具 [[F-0121]] [[F-0122]]
- 产物为高斯泼溅，Blender 5.3 能导入不能导出；实测远处画质下降 [[F-0128]] [[F-0129]]

## 时间线
- 2026-04 image-blaster 首次提交，05 公开 [[F-0120]]

## 我们的判断与注意
- “一张图 5 分钟生成 3D 世界、Blender 大佬沉默”是营销放大 [[F-0130]]
- 李飞飞创始人身份为既有知识，库内暂无卡片

## 相关卡片（脚本生成，勿手改）
<!-- cards:start -->
| 卡片 | 状态 | 事实时间 | 命题 |
|---|---|---|---|
| [[F-0120]] | 已证实 | 2026-04 | image-blaster 是 GitHub 上 neilsonnn（Neilson K-S）的开源仓库，MIT 协议，首次提交 2026-04-20，公开发布约在 2026-05-14（加 LICENSE 的提交） |
| [[F-0121]] | 已证实 | 2026-10-05 | image-blaster 本身不含生成模型：它是一组 Claude Code 技能（skills/agents/脚本）加一个 React 查看器，把 World Labs Marble、nano-banana、gpt-image-2、混元3D（经 FAL）、ElevenLabs 音效等商业 API 串起来 |
| [[F-0122]] | 已证实 | 2026-10-05 | 运行 image-blaster 需要 World Labs 和 FAL 两个付费 API 密钥，并需要安装 Claude Code |
| [[F-0123]] | 公司自述 | 2026-10-05 | image-blaster README 称可在“< 5 分钟”内从一张图得到完整网格化的 3D 环境 |
| [[F-0124]] | 已证实 | 2026-10-05 | image-blaster 的产物是：静态环境为高斯泼溅（.spz，由 World Labs Marble 生成）、动态物件为 3D 模型（.glb/.obj，由混元3D生成）、外加环境与物件音效（.mp3，ElevenLabs） |
| [[F-0125]] | 已证实 | 2026-10-05 | image-blaster 作者 Neilson Koerner-Safrata 来自 World Labs 设计团队，World Labs 官网 Labs 栏目把它作为展示案例 |
| [[F-0126]] | 已证实 | 2026-10-05 | World Labs Marble API 按点数计费：1.00 美元 = 1250 点（最低购买 5 美元）；Marble 1.0/1.1 每次生成世界 1500 点（约 1.2 美元），草稿版 150 点 |
| [[F-0127]] | 已证实 | 2026-10-05 | fal.ai 上混元3D（Hunyuan 3D v3）图生 3D 标准带纹理每次 0.375 美元，开启 PBR、自定义面数等各加 0.15 美元；ElevenLabs 音效 V2 在 fal 上约 0.002 美元/秒 |
| [[F-0128]] | 已证实 | 2026-10-05 | Blender 5.3 原生支持导入并渲染高斯泼溅（PLY、SPZ），但还不能导出，编辑与变换存在限制 |
| [[F-0129]] | 部分属实 |  | 实测评价：Marble 生成的世界在中心区域之外画质明显下降，Marble 导出的网格质量差，接入实时项目需要大量技术处理 |
| [[F-0130]] | 观点 |  | “一张图5分钟生成可漫游3D世界，Blender 大佬集体沉默 / 苦练十年 Blender 的创作者……” |
| [[F-0131]] | 部分属实 | 2026-10-05 | image-blaster GitHub 星标：约 5.1k（X 帖）→ 约 5.4k（越南语文章）→ 约 6.7k、679 fork（视频截图） |
<!-- cards:end -->
