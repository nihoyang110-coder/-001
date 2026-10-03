# Vault 格式

```
FactCheck/
├── README.md
├── 事实清单.md          # 总表（Dataview 自动表 + 脚本生成的静态表）
├── Facts/F-xxxx.md      # 一个命题一张卡
├── Notes/YYYY-MM-DD-关键词.md
└── Templates/
```

## 事实卡片 frontmatter
```yaml
id: F-0005
type: 数字          # 事实 / 数字 / 观点 / 预测
claim: "2026年9月 Higgsfield 宣称年化收入运行率突破10亿美元"
status: 公司自述     # 见下表
confidence: 中       # 高 / 中高 / 中 / 低
subject: Higgsfield  # 公司/人物/行业，便于聚合
first_seen: 2026-10-03
last_checked: 2026-10-03
review_by:           # 预测类必填：到期回看日期
sources: [一手：官方博客, 二手：TechCrunch]
news: ["[[2026-10-03-xxx]]"]
tags: [fact, Higgsfield]
```
正文：`## 证据`（支持/反驳）、`## 口径/注意`、`## 更新记录`（每次改动追加一行日期+原因）。

## status 取值
| status | 含义 | 引用规则 |
|---|---|---|
| 已证实 | ≥2 个独立可靠来源一致 | 可直接引用 |
| 公司自述 | 只有当事方说 | 必须写“据公司称” |
| 部分属实 | 核心对，细节/口径有问题 | 带注释引用 |
| 存疑 | 找不到原始来源或互相矛盾 | 不引用 |
| 证伪 | 有证据证明错误 | 作反例 |
| 观点 | 某人的判断 | 写明“谁认为” |
| 待验证 | 预测，尚未到期 | 写明到期日 |

## 命题写法
- 可证伪、带主语、带时间点：好 “2026-08 Higgsfield 披露年化收入7亿美元”；差 “Higgsfield 收入很高”。
- 被证伪的说法也建卡，claim 写原说法并加引号，status=证伪——下次再见到能秒判。
