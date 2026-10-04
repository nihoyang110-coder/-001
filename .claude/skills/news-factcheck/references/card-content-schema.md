# 卡片内容文件 content.js（新粗野主义模板）

一条新闻一个 `content.js`，模板 `assets/neobrutal/template.html`（8 张 3:4）和 `video-cover.html`（视频号 9:16 封面）都只读它。
示例：`FactCheck/Content/2026-10-03-日本食品消费税/content.js`。每个数字都要能在该话题的 `事实对照.md` 里找到卡片。

```js
window.CONTENT = {
  handle: '@账号名',
  video: { lines: ['第一行', '第二行', '高亮行'], sub: '黄条副标题', tag: '左上角标签' },   // 视频号封面，可省略
  cover: {                                   // 第1张：封面
    tag, lines: ['行1','行2','最后一行会高亮'], big: '9%', bigNote: '税后',
    sub: '蓝条一句话', src: '底部来源',
    icon: 'bento_box',                       // 右上角 3D 贴纸，可省略
    pills: [{ label, value, icon, color }]   // 0–2 个对比块；color: r 红 g 绿 y 黄 b 蓝 v 紫 w 白
  },
  facts: { tag, title, rows: [{ k, v, hi }] ×4, src },           // 第2张：2×2 事实块，hi 为大字
  chart: { tag, title, titleHi, unit: '%',                         // 第3张：分组柱状图
           groups: [{ label, dine, take, gapLabel, gapNum }] ×2,
           legend: { dine, take }, src },
  gain:  { tag, title, titleHi, stats: [{ label, n, unit }] ×2, points: [...] ≤3, src },   // 第4张
  loss:  { tag, title, rows: [{ who, what, icon }] ×3, kicker, src },                      // 第5张
  chain: { tag, title, steps: [{ t, d, pred }] ×4, compare, src },                         // 第6张；pred:true 自动标“预测”
  block: { tag, title, hero: { label, big, icon }, fillerIcon, items: [{ t, d }] ×4, src }, // 第7张；items[0] 放红色大字块
  end:   { tag, quote: ['行1','行2','行3','行4'], highlightFrom: 2, watch: [['时间','事件']] ×3, src }  // 第8张
};
```

## 可用图标（assets/neobrutal/icons，Microsoft Fluent Emoji 3D，MIT）
bento_box, takeout_box, fork_and_knife_with_plate, convenience_store, shopping_cart, house,
classical_building, bank, yen_banknote, chart_increasing, balance_scale, warning, hourglass_not_done,
magnifying_glass_tilted_left

需要新图标：从 `https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/<英文名>/3D/<小写下划线名>_3d.png` 下载到 icons/。

## 写法要点
- 标题行每行 ≤6 个字（封面 100px 大字），超过会难看；高亮行同理
- `rows`/`items` 的 `d`/`v` 一句话，≤30 字
- 柱状图 `dine`/`take` 是数值；同一图里最大值占满高度
