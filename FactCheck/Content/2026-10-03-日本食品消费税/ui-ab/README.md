# UI 盲评素材
- `content.js`：五套共用的文字和数字
- `A.html`…`E.html`：五套设计；`A/`…`E/`：渲染出的 1080×1440 PNG
- `对比/`：封面对比和每套全套缩略图
- `评审表.md`：打分表
- `answer.b64`：答案（评完再解码：`base64 -d answer.b64`）
- 重新渲染：`node ../../../../.claude/skills/news-factcheck/scripts/render_cards.cjs A.html A`
  （字体文件放在会话临时目录，见 `fonts.css`；换环境需重新下载 Noto Serif/Sans SC、霞鹜文楷、站酷快乐体、JetBrains Mono）
