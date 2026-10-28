# 知识扩张

把公开课、新发布的方法和标准**去重归档**，和我们自己的构建逐项对比找差距，再按课程原版评分表学到“会”。

- 可视化页面：https://claude.ai/artifact/7tTk3PTuohyXK94BL5Nox4 （由 `知识扩张.html` 发布，私有）
- 起因：[[2026-10-28-斯坦福CS146S作业公开与名校课程]]

## 文件
| 文件 | 内容 | 谁来改 |
|---|---|---|
| `raw/日期_批次.json` | 每次调研的原始结果（保留出处，不手改） | 调研 |
| `catalog.json` | 去重后的资源目录（K-001…） | `kx.py merge` |
| `dedupe_log.json` | 链接级去重的合并记录 | `kx.py merge` |
| `topics.json` | 主题级去重：每个主题的首选 / 补充 / 不用学 | 手改 |
| `capabilities.json` | 15 项能力：当前级、目标级、权重、依据、短板、升级记录 | 手改 + `kx.py level` |
| `plan.json` | 学习队列：每个单元的来源、评分表（满分 100）、交付物、状态、得分 | 手改 |
| `template.html` → `知识扩张.html` | 可视化页面 | `kx.py build` |
| `作业/` | 每个学习单元的交付物与自评 | 学习时 |

## 两层去重
1. **链接去重**（自动）：规范化后的主链接、同一 GitHub 仓库、同一短名，或同机构且标题相似度 ≥ 0.88，视为同一条，合并时取并集。
2. **主题去重**（人工）：讲同一件事的资源归入一个主题，只学“首选”（有评分标准 > 免费 > 一手且最新 > 中文或篇幅短），其余标“不用学”。

## 评级与“学到什么程度”
- 能力 0–4 级：0 没接触 / 1 了解 / 2 能做 / 3 熟练（有可复用工具并反复用过）/ 4 有验证（有测试或评测，评分 ≥80）
- 差距分 =（目标级 − 当前级）× 权重（3 核心 / 2 在做的项目 / 1 以后）
- 每个学习单元用来源课程原版评分表（满分 100），**≥80 分算达标**：先自评并附证据（文件、提交号、测试输出），用户复核；达标后 `python3 kx.py level C4 2 "L01 82 分，提交 abc123"`，并把 plan.json 里的状态改为“已达标”、填 score

## 每月更新（定时任务）
1. 按 4 类调研新资源（大学课程 / 业界课程 / 新方法与标准 / 领域课程），只找上次之后的新内容或新一期，写成 `raw/日期_批次.json`（字段见下）
2. `python3 kx.py merge raw/日期_*.json`（已并入的批次会自动跳过）
3. 新条目归入 `topics.json` 的主题；出现更好的首选就替换并在 why 里写原因
4. 检查 `capabilities.json` 依据是否过时；`python3 kx.py relink` 重算与事实卡片的关联
5. `python3 kx.py build`，提交推送，并重新发布页面

raw 条目字段：id_hint、title、title_zh、provider、kind（大学课程/业界课程/方法指南/标准规范/官方文档）、url、alt_urls、edition、published、cost、format、language、effort_hours、areas（C1–C15）、units[{name,areas,url,rubric}]、summary_zh、why_for_us_zh、rubric_zh、evidence、confidence（高/中/低）。
