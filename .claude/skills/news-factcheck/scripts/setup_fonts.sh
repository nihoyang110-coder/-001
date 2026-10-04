#!/usr/bin/env bash
# 下载卡片所需的开源中文字体（GitHub 可达即可），并在目标目录写 fonts.css。
# 用法：bash setup_fonts.sh <内容目录>
set -euo pipefail
OUT="${1:?用法: setup_fonts.sh <内容目录>}"
CACHE="${XDG_CACHE_HOME:-$HOME/.cache}/news-factcheck-fonts"
mkdir -p "$CACHE"
get() { [ -s "$CACHE/$2" ] || curl -sSfL -m 300 -o "$CACHE/$2" "$1"; echo "  $2 $(du -h "$CACHE/$2" | cut -f1)"; }
echo "字体缓存：$CACHE"
get "https://raw.githubusercontent.com/google/fonts/main/ofl/notosanssc/NotoSansSC%5Bwght%5D.ttf" NotoSansSC.ttf
get "https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/NotoSerifSC%5Bwght%5D.ttf" NotoSerifSC.ttf
get "https://raw.githubusercontent.com/google/fonts/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf" JetBrainsMono.ttf
cat > "$OUT/fonts.css" <<CSS
@font-face { font-family: "NSans"; src: url("file://$CACHE/NotoSansSC.ttf"); font-weight: 100 900; }
@font-face { font-family: "NSerif"; src: url("file://$CACHE/NotoSerifSC.ttf"); font-weight: 200 900; }
@font-face { font-family: "JBMono"; src: url("file://$CACHE/JetBrainsMono.ttf"); font-weight: 100 800; }
CSS
echo "已写入 $OUT/fonts.css"
