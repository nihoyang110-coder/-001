#!/usr/bin/env bash
# 核查前自检：哪些新闻源能直接打开。用法：bash check_network.sh
hosts="en.wikipedia.org web.archive.org apnews.com www.reuters.com www.npr.org www.bbc.com www3.nhk.or.jp www.nikkei.com www.japantimes.co.jp www.jiji.com www.congress.gov www.supremecourt.gov www.kantei.go.jp www.mofa.go.jp www.iea.org"
ok=0; total=0
for h in $hosts; do
  total=$((total+1))
  code=$(curl -s -o /dev/null -m 8 -w "%{http_code}" "https://$h/" 2>/dev/null)
  if [ "$code" != "000" ]; then ok=$((ok+1)); echo "✅ $h ($code)"; else echo "❌ $h"; fi
done
echo "可达 $ok/$total"
[ "$ok" -lt 3 ] && echo "⚠️ 网络受限：结论只能依据搜索摘要，所有置信度降一级，并在笔记“局限”里写明。"
exit 0
