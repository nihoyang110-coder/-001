---
date: 2026-10-16
source: 视频号截图（开源工具社，已声明原创，江苏）「老外用 Claude 做了个全开源的 CAD 软件：全开源具备 MCP 方便 AI 调用」
claim: CADCraft 是 ArtCraft 团队用 Rust 做的开源 CAD，操作参考 AutoCAD，用过的人基本不用重新适应；具备 MCP
verdict: 项目、团队、Rust、开源、MCP、仿 AutoCAD 操作均属实；“直接上手”只成立于手感，项目自评仅 pre-alpha（可实用约 38%，几乎没有 3D）
confidence: 高（直接读了源码仓库）；FreeCAD 部分为中（搜索摘要）
facts: [F-0185, F-0186, F-0187, F-0188, F-0189, F-0190, F-0191]
tags: [factcheck, CAD, 开源软件, Claude, MCP, FreeCAD]
---
# CADCraft：老外用 Claude 做的开源 CAD？对比 FreeCAD

> **利益说明**：本核查由 Anthropic 开发的 Claude 完成，项目大量使用 Claude 编写。只依据仓库公开数据和外部来源。

## 0. 截图信息
- 账号“开源工具社”（已声明原创），评论 7；口号“每天精选一个开源项目”
- 画面：CADCraft 打开公寓平面图（LIVING/DINING、BEDROOM、BATH、ROOM SCHEDULE），即官方 README 的示例图 `examples/apartment.dxf`
- 热评：“那是不是 CAD 的软件费就不需要了”

## 1. 原子命题与结论
| # | 说法 | 结论 | 状态 | 卡片 |
|---|---|---|---|---|
| 1 | ArtCraft 团队、Rust、全开源 | 属实：storytold/cadcraft，纯 Rust，MIT/Apache-2.0 | 已证实 | [[F-0185]] |
| 2 | 老外用 Claude 做的 | 属实：Brandon Thomas 首提交；491 次提交中约 403 次有 Claude 共同作者标记；另有社区贡献者 | 已证实 | [[F-0186]] |
| 3 | 具备 MCP 方便 AI 调用 | 属实：官方内置 MCP、JSON 通道、CLI | 已证实 | [[F-0187]] |
| 4 | 操作参考 AutoCAD，基本不用重新适应 | 手感属实；但自评 pre-alpha，可实用约 38%、3D 约 2%，保存会丢未支持实体 | 部分属实 | [[F-0188]] |
| 5 | （评论）CAD 软件费不需要了 | 目前不能替代正式工作 | 观点 | [[F-0188]] |
| — | 附加发现：同名假镜像仓库 | 有不明账号上传“Download CADCraft”仓库，安装包格式与官方不同 | 已证实（风险提示） | [[F-0189]] |

## 1.5 搜索日志
| # | 角度 | 关键发现 | 级别 | 有效 |
|---|---|---|---|---|
| 0 | 原始来源直读 | clone storytold/cadcraft：README、ROADMAP（pre-alpha，38%）、CLAUDE.md、git log（10-05 起 491 提交，403 带 Claude） | 一手 | ✓ |
| 1 | 定位仓库 | 正主 storytold/cadcraft；多个同名 fork/镜像 | 二手 | ✓ |
| 2 | 当事人/Claude 角色 | TechRepublic：Brandon Thomas 用 Claude 做 ArtCraft 系列 | 二手 | ✓ |
| 3 | 对照对象现状 | FreeCAD 1.1（2026-03）、1.1.3（2026-07-25） | 一手 + 二手 | ✓ |
| 4 | 对照对象 AI 接口 | FreeCAD 社区 MCP 插件多个，需开 GUI | 二手 | ✓ |
| 5 | 对照对象文件兼容 | FreeCAD DWG 需 ODA 转换器或 LibreDWG（GPLv3） | 一手（wiki） | ✓ |
| 6 | 反方/风险 | 假 GitHub 仓库投毒手法（Arctic Wolf 等）；直读 cadcraft-app 镜像 README | 二手 + 一手 | ✓ |

## 2. 先立后破
**最强版本**：一个人带着 AI 代理，十天做出能画平面图、标注、出 PDF、读写 DXF/DWG、还能被 AI 直接操控的 AutoCAD 风格软件，且完全开源免费——这说明 AI 写软件的速度已经能威胁“老牌软件的操作习惯护城河”。

| 攻击点 | 判断 |
|---|---|
| **范围放大**：“用过的人直接上手”≈“能替代 AutoCAD”？项目自评可实用约 38%，2D 绘图员约 28% | 成立（[[F-0188]]） |
| **文件交换风险**：DXF/DWG 只写 R2000，未支持实体保存即丢 | 成立（[[F-0188]]） |
| **项目太新**：10 天历史，稳定性自评 35% | 成立 |
| **下载安全**：热门后出现同名镜像仓库 | 成立（[[F-0189]]） |
| “老外用 Claude 做的”是否夸大 | 不成立：提交记录可证 |
| 开源与 MCP 是否真实 | 不成立：许可证与代码可证 |

## 3. 对比表：CADCraft vs FreeCAD
| 维度 | CADCraft | FreeCAD |
|---|---|---|
| 定位 | AutoCAD 风格 **2D 绘图**（仿 AutoCAD 命令行操作） | **参数化 3D 建模**为主，另有 2D Draft 与工程图 |
| 成熟度 | 2026-10-05 起步，v0.7.0，自评 pre-alpha、可实用约 38% | 2002 年起，20+ 年，1.x 稳定版（1.1.3，2026-07） |
| 开发方式 | 一人主导 + Claude 代理大量编写（约 82% 提交），少量社区 | 大型社区长期协作 |
| 编程语言 | 纯 Rust（egui 界面） | C++ + Python（Qt 界面） |
| 许可证 | MIT 或 Apache-2.0（宽松，可闭源商用改造） | LGPL-2.1+（修改库本身需开源） |
| 平台 | macOS、Windows、Linux、FreeBSD、浏览器 | macOS、Windows、Linux |
| 操作习惯 | 对 AutoCAD 用户友好：命令、别名、对象捕捉、夹点 | 工作台式，需重新学习 |
| 3D | 约 2%（几乎没有） | 强项：实体、钣金、装配、FEM、CAM、BIM |
| DWG | 原生读写（读 R13–2018，写 R2000），未支持实体保存会丢 | 需另装 ODA 转换器（免费闭源）或 LibreDWG |
| DXF | 读 R12–2018，写 R2000 | 原生读写 |
| AI / MCP | **官方内置** MCP + JSON 通道 + CLI，可无界面调用 | **社区插件** MCP（需开 GUI）；原生 Python 脚本很强 |
| 生态 | 极少（自评 10%，无 AutoLISP） | 大量插件、教程、论坛 |
| 风险 | 太新、可能丢数据、已有假镜像 | 学习曲线陡、DWG 依赖外部工具 |
| 适合谁 | 想试 AI 自动出 2D 图、尝鲜者 | 机械/产品/建筑 3D 建模、需要稳定开源工具的人 |

## 4. 一句话结论
**视频说的基本都对：确实是开源、Rust、内置 MCP、照着 AutoCAD 做的，而且确实大部分代码由 Claude 写出；但它才 10 天大，项目自己说只完成约四成，还几乎没有 3D——现在是“有意思的新玩具”，不是 AutoCAD 或 FreeCAD 的替代品。**

## 5. 白话版
CADCraft 像一家照着名店（AutoCAD）装修的新餐馆：菜单、摆台、点菜方式都一模一样，老顾客进门不用适应；而且它有个“外卖窗口”（MCP），AI 可以直接下单。但它开业才 10 天，后厨自己说只会做四成的菜，“立体菜”（3D）几乎没有，打包带走（存成 DWG 给别人）时还可能漏掉几样。FreeCAD 是一家开了 20 多年的老店，菜系不同（擅长 3D），装修和点菜方式要重新学，外卖窗口靠热心食客自己搭。

## 6. 落入事实清单
新建 [[F-0185]]–[[F-0191]] 共 7 张。

## 7. 局限
- 未实际编译运行 CADCraft（需 Rust 工具链与图形环境）；功能状态来自项目自评
- FreeCAD 资料为搜索摘要；成立年份与许可证为既有知识
- 未下载、未检测镜像仓库的安装包
