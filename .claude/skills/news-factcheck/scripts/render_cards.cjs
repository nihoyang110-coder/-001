#!/usr/bin/env node
// 把 HTML 里每个 <section class="card">（1080×1440）截成 PNG，用于小红书/视频号素材。
// 用法：node render_cards.cjs <cards.html> <输出目录>
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [html, out] = process.argv.slice(2);
  if (!html || !out) { console.error('用法: node render_cards.cjs <cards.html> <输出目录>'); process.exit(1); }
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1600 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(html));
  await page.evaluate(() => document.fonts.ready);
  const cards = await page.$$('section.card');
  for (let i = 0; i < cards.length; i++) {
    const f = path.join(out, `${String(i + 1).padStart(2, '0')}.png`);
    await cards[i].screenshot({ path: f });
    // 溢出检查：内容超出卡片高度时提示
    // 只检查“有文字的元素”是否超出卡片边界；故意出血的装饰元素加 data-bleed 跳过
    const overflow = await cards[i].evaluate(card => {
      const box = card.getBoundingClientRect();
      return [...card.querySelectorAll('*')].some(el => {
        if (el.closest('[data-bleed]')) return false;
        const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
        if (!own) return false;
        const r = el.getBoundingClientRect();
        return r.bottom > box.bottom + 1 || r.right > box.right + 1 || r.left < box.left - 1 || r.top < box.top - 1;
      });
    });
    console.log(`${f}${overflow ? '  ⚠️ 内容溢出，需删字' : ''}`);
  }
  await browser.close();
})();
