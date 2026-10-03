# 搜索角度矩阵

每条新闻从下面挑 5–10 个不同角度，每个角度一次搜索。前 4 个基本每次都要。

| # | 角度 | 目的 | 查询示例 |
|---|---|---|---|
| 1 | 原始来源 | 找到第一个说这句话的人/文件 | `<公司> <数字> announcement` / `<人名> interview <节目名>` |
| 2 | 当事方自述 | 官网博客、新闻稿、CEO 社交帖 | `site:<公司官网> <关键词>`、`<CEO> LinkedIn <关键词>` |
| 3 | 数字口径 | ARR/GMV/用户数到底怎么算 | `<公司> "run rate" how calculated`、`<公司> annualized revenue definition` |
| 4 | 反方/质疑 | 投诉、做空、批评、诉讼 | `<公司> criticism / skeptic / lawsuit / complaints` |
| 5 | 主流媒体独立报道 | 有没有不只转述新闻稿的报道 | `<公司> TechCrunch / The Information / Bloomberg` |
| 6 | 时间线 | 前后数字是否连贯 | `<公司> revenue 2025` 、`<公司> funding history` |
| 7 | 人物背景 | 说话者是谁、利益关系 | `<人名> background previous company` |
| 8 | 商业模式/成本 | 收入≠利润、依赖谁 | `<公司> gross margin / costs / dependency` |
| 9 | 观点原话 | 标题里的“金句”原文是什么 | `<人名> "<英文关键词>" quote` |
| 10 | 行业背景 | 观点是否只是行业流行叙事 | `<观点关键词> 2026 analysis` |
| 11 | 竞品/对照 | 同类公司数据作参照 | `<竞品> ARR` |
| 12 | 中文转述源 | 编译文章从哪里翻译来的 | `<公众号名> <标题关键词>` |

## 判定重复
一次搜索若满足下面任一条，算“重复”，需补一次：
- 结果里没有新域名，且没有新事实
- 只是把同一新闻稿换了媒体转载

## 抓取失败
记录被拦截的域名。可尝试：搜索摘要、`web.archive.org/web/<url>`、同一内容的其他转载。都不行就降置信度。
