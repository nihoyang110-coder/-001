# 第二轮 UI 盲评素材（F–J）
- `content.js`：共用文字和数字；`icons/`：Microsoft Fluent Emoji 3D 图标（MIT）；`icons.js`：图标内嵌数据（给 AntV 用）
- `F.html`…`J.html`：五套设计；`F/`…`J/`：渲染出的 1080×1440 PNG；`对比/`：封面对比和全套缩略图
- `评审表.md`：打分表；`answer.b64`：答案（`base64 -d answer.b64`）
- 渲染：`node ../../../../.claude/skills/news-factcheck/scripts/render_cards.cjs F.html F`
  - 字体在会话临时目录（见 `fonts.css`）；H 还需要 `npm install @antv/infographic@0.2.20`（路径见 H.html 的 script 标签）
