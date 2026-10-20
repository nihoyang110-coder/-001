---
date: 2026-10-20
source: 视频号截图（三次方AIRX）「Codex 变身专业 3D 建模师：22 个 Blender Skill 一口气喂给 Agent，建模、材质、拓扑、灯光、动画等全覆盖」（转引 X 用户 Hakimi Eiqbal 帖子）；用户要求：找评价高的开源 Blender skill/工具，列作用，并提出我们自己能做哪些工具
verdict: 技能包真实存在且脚本实测可用（46/50 测试通过）；“Codex 变身专业建模师”夸大
confidence: 高（主要项目均克隆直读，核心技能包实跑测试）
facts: [F-0228, F-0229, F-0230, F-0231, F-0232]
tags: [调研, Blender, 3D建模, MCP, 技能包, 开源]
---
# Blender AI 建模：开源工具调研与自研方向

> 利益说明：本调研由 Anthropic 的 Claude 完成；部分工具与 Claude 有关（Anthropic 的 Blender 连接器、Claude Code 插件）。评价只依据仓库内容、实测和外部来源。

## 0. 视频核对
| 说法 | 结论 | 卡片 |
|---|---|---|
| 22 个 Blender Skill，覆盖建模、材质、拓扑、灯光、动画 | 属实：EL4CTEO/blender-skills，MIT，22 个技能，10-14 才建 | [[F-0228]] |
| 能用 | 我们实跑：50 项测试 46 过、1 败（环境原因）、3 跳过（需显卡） | [[F-0229]] |
| Codex 变身专业 3D 建模师 | 夸大：不是 Codex 专属；技能管“操作规范”，成品好坏看模型 | [[F-0230]] |

## 1. 工具怎么分类
- **连接器（MCP 服务器）**：让 AI 能“摸到”正在运行的 Blender——读场景、执行代码、截图
- **技能包（Skills）**：教 AI“正确的做法”——流程、参数、现成脚本、检查清单
- **闭环插件**：连接 + 技能 + 自动检查 + 渲染回看，打包成一个插件

## 2. 评价较高的开源项目
| 项目 | 类型 | 热度/许可 | 作用详情 | 注意 |
|---|---|---|---|---|
| **MCP for Blender**（ahujasid，原 blender-mcp） | 连接器 | 约 2.9 万星，MIT（[[F-0231]]） | 读场景信息；执行任意 Python；搜索并导入 Poly Haven 材质/HDRI/模型、Sketchfab 模型；调用 Hyper3D、混元3D 等生成 3D；一条命令装到 Claude Desktop/Code、Codex、Cursor 等 | 2026 年两个漏洞（执行代码无沙箱；Poly Haven 路径穿越，1.6.5 修复）；生成类功能要第三方账号 |
| **Blender Lab MCP**（Blender 官方实验室） | 连接器 | GPL-3.0+，v1.0.0 于 2026-04-27（[[F-0232]]） | 刻意做小：读场景、调试、跑脚本；Anthropic 的 Claude Blender 连接器用它；需 Blender 5.1+ | 不做“生成艺术”；官方仓库本次未直读 |
| **EL4CTEO/blender-skills** | 技能包 | MIT，新项目（[[F-0228]]） | 22 个技能：`blender-core` 总入口与 5.x API 规则；建模（硬表面/雕刻/几何节点）；重拓扑+UV（贴图密度）；PBR 材质自动接线；烘焙法线/AO/曲率/ORM；Rigify 绑定、ARKit 52 表情；动画与根运动；LOD 与面数预算；导出 Roblox/Unity/Unreal/Godot/网页/USD；渲染、灯光、天气、模拟；**资产质检**（穿插闪烁、悬空零件、法线翻转、非流形、重复点、n 边面、权重） | 实测 46/50 通过（[[F-0229]]）；可无界面后台跑，也可配合 MCP |
| **Blender Agent Studio**（ifBars） | 闭环插件 | MIT | 给 Claude Code / Codex 用：交付可编辑 `.blend` + 生成它的 Python + 渲染图；自检安装；参考图多角度比例对比；招牌/标签 2D 设计；可录建模过程延时视频 | 作者自己说“自动检查抓坏几何，抓不了审美”；需 Bun |
| **dream-loop**（achimala） | 技能（方法） | MIT | “先用生图模型画出目标效果图 → AI 按图搭建 → 另一个 AI 评审员对比截图给意见 → 循环” | 作者只在 GPT-6 Astra + Codex 上测过；需要生图和看图能力 |
| **Blender-Bonsai-IfcOpenShell-Sverchok 技能包**（Impertio / OpenAEC） | 技能包（BIM） | MIT | 73 个技能，覆盖建筑 IFC 模型（Bonsai）、IfcOpenShell、Sverchok 参数化；含 MCP 配置 | 偏建筑行业 |
| MCP4IFC / ifc-bonsai-mcp | 连接器（BIM） | 研究原型 | 让大模型读写 IFC 建筑模型 | 见 [[F-0224]] |
| arjun988/blender-skills、cli-anything-blender 等 | 技能包 | 小众 | 23 个技能 / 命令行 JSON 场景描述 | 星数少、未细看 |

## 3. 怎么组合用（推荐）
**连接器 1 个 + 技能包 1 套 + 质检**：官方 Blender Lab MCP 或 MCP for Blender，配 EL4CTEO 技能包，每次交付前强制跑它的 `blender-asset-qa`。要做建筑再加 Impertio 的 BIM 技能包。

## 4. 我们自己可以做的工具（按优先级）
现有工具已经覆盖“会操作 Blender”和“通用流程”，空白在 **中文用户场景、尺寸与可信度、安全、内容发布**：

| # | 工具 | 解决什么 | 怎么做 | 难度 |
|---|---|---|---|---|
| 1 | **尺寸核验器** | AI 建的东西“看着对、尺寸错”是最常见问题 | 把用户要求（“长 120mm、孔径 8mm”）解析成清单，建完自动量 `dimensions`、孔径、壁厚，输出偏差表，超差就退回重做 | 低：bpy 现成；可复用 EL4CTEO 的 QA 脚本 |
| 2 | **安全执行层** | MCP 的“执行任意代码”有 CVE | 在执行前做代码检查：只放行 bpy/bmesh/mathutils/math，禁止文件系统越界、网络、子进程；自动先存档；所有执行留日志 | 中 |
| 3 | **参考图比对评审器** | dream-loop 的评审靠 AI 主观判断 | 多角度渲染剪影，与参考图做轮廓重合度（IoU）和比例对比，给数字分 + 文字意见 | 中：需离屏渲染（可用 Workbench/EEVEE） |
| 4 | **转台视频/封面出图器** | 接我们的小红书/视频号发布流程 | 一键 360° 转台 MP4（9:16、3:4）+ 封面 PNG + 线框对比图，套我们 J 模板的字体配色 | 低 |
| 5 | **国内平台导出预设** | 现有导出覆盖 Roblox/Unity/Unreal/Godot，缺国内 | 微信/抖音小游戏、Cocos Creator、网页 three.js 的面数/贴图/格式预算，导出前自动检查 | 中：需查各平台规范 |
| 6 | **同题评测台** | 核查“快 99 倍”“变身专业建模师”这类说法 | 固定 20 道中文建模题，分别在“装/不装技能包”“不同模型”下跑，自动打分（质检通过率、尺寸偏差、轮廓重合度、耗时、费用），结果写进事实清单 | 中：1、3 做完后组装 |

建议顺序：**1 → 4 → 2 → 3 → 6 → 5**。1 和 4 一两天就能出原型，直接用在内容生产上；6 能反过来服务事实核查。

## 5. 白话版
- **连接器**像“遥控器”：让 AI 能按 Blender 的按钮
- **技能包**像“操作手册”：告诉 AI 每一步怎么做才专业
- 视频里的 22 个技能就是一本手册，我们实际跑过，里面的脚本是能用的；但有了手册不等于成了专业建模师，最后做得好不好还看 AI 本身
- 我们能补的，是“验收员”（量尺寸、比照片、查安全）和“宣传部”（自动出转台视频和封面）

## 6. 搜索与实测日志
| # | 动作 | 关键发现 | 级别 |
|---|---|---|---|
| 1 | 搜原帖仓库 | EL4CTEO/blender-skills；另见 blender-agent-studio、dream-loop 等 | 二手 |
| 2 | 搜热门 MCP | 官方 Blender Lab MCP、MCP for Blender、多个 200+ 工具的社区版 | 二手 |
| 3 | 搜技能包 | Impertio BIM 73 技能、arjun988、cli-anything | 二手 |
| 4 | 搜官方背景 | Blender Lab MCP v1.0.0、Anthropic 连接器、基金会表态 | 二手 |
| 5 | 克隆 4 个仓库直读 | 许可、技能清单、工具定义、首次提交日期 | 一手 |
| 6 | 安装 bpy 5.2.2 实跑测试 | 46 过 / 1 败 / 3 跳过 | 一手 |
| 7 | 搜热度 | MCP for Blender 约 2.9 万星 | 二手 |
| 8 | 搜安全 | 两个 CVE、审计建议 | 二手 |

## 7. 局限
- 没有显卡，渲染相关测试跳过；没有让 AI 真正用这些工具建一个完整模型
- 官方 Blender Lab MCP 仓库未直读；多数星数为第三方统计时点数
- 推特原帖作者 Hakimi Eiqbal 是转发者还是作者，未核实（仓库作者为 EL4CTEO）
