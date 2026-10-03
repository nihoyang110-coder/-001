# FactCheck 新闻溯源库 (Obsidian Vault)

用 Obsidian 打开 `FactCheck/` 目录。推荐装 **Dataview** 插件（事实清单自动汇总）。

## 目录
| 位置 | 放什么 |
|---|---|
| `事实清单.md` | 总清单：所有事实卡片一览（我们自己的“事实库”） |
| `Facts/F-xxxx.md` | **一个命题一张卡**：命题、状态、置信度、来源、更新记录 |
| `Notes/YYYY-MM-DD-关键词.md` | 每条新闻一篇：搜索日志、拆解、攻击、结论，引用事实卡 |
| `Templates/` | 新闻模板、事实卡模板 |

## 每条新闻的流程
1. 截图 → 提取标题/来源/日期
2. 5–10 次**不重复角度**的搜索（原始源、二手报道、当事人、反方、行业背景、口径…）
3. 拆文：主观点 + 依据
4. 红队攻击：逐条找漏洞
5. 补证据：支持 / 反驳
6. 出结论 → **把每个可验证命题落成事实卡**：
   - 先在 `事实清单.md` 搜一下，已有卡片就更新 `status`/`last_checked`/更新记录
   - 没有就新建 `F-下一个编号`
7. 新闻笔记里只写 `[[F-xxxx]]` 链接 + 本次判断

这样新闻会过时，但事实清单会越积越厚，下次看到相关新闻能直接对照。

## 工具 & 技能
- Claude 技能：`.claude/skills/news-factcheck/`（在本仓库开 Claude Code 会话，发截图即自动触发）
- 脚本：`python3 .claude/skills/news-factcheck/scripts/factdb.py search|next-id|rebuild|due`
  - `due`：列出到期该回看的预测卡
