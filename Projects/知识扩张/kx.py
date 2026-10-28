#!/usr/bin/env python3
"""知识扩张：课程/方法目录的去重、差距计算和可视化页面生成。

用法（在 Projects/知识扩张/ 下运行）：
  python3 kx.py merge raw/*.json     把新调研结果并入 catalog.json（自动去重，记录合并日志）
  python3 kx.py relink               事实卡片有新增后，重算资源与卡片的关联
  python3 kx.py gap                  按“(目标级-当前级)×权重”列出能力差距
  python3 kx.py level C4 3 "依据"    学完达标后给能力升级（写进 capabilities.json 的 history）
  python3 kx.py build                生成 知识扩张.html（数据嵌入页面）
  python3 kx.py currency cur/*.json  写入时效复核结果，已淘汰的移出学习主题
  python3 kx.py study                把 lessons/*.json 生成 学习室.html

去重规则：同一主链接（规范化后）、同一 id_hint、同一 GitHub 仓库，
或同一机构且标题相似度 ≥ 0.88，视为同一条；合并时取并集，保留置信度更高的那条的文字。
"""
import datetime, difflib, json, pathlib, re, sys
from urllib.parse import urlparse, parse_qs

HERE = pathlib.Path(__file__).resolve().parent
CAT, CAP, PLAN, LOG = (HERE / n for n in ("catalog.json", "capabilities.json", "plan.json", "dedupe_log.json"))
FACTS = HERE.parent.parent / "FactCheck" / "Facts"
CONF = {"高": 3, "中": 2, "低": 1}
TODAY = datetime.date.today().isoformat()


def load(p, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def canon(url):
    if not url or not isinstance(url, str):
        return None
    u = urlparse(url if "://" in url else "https://" + url)
    host = u.netloc.lower().removeprefix("www.")
    parts = [p for p in u.path.split("/") if p]
    if host == "github.com" and len(parts) >= 2:
        parts = parts[:2]
        parts[1] = parts[1].removesuffix(".git")
    key = host + "/" + "/".join(parts).lower()
    if "youtube.com" in host and "list" in parse_qs(u.query):
        key += "?list=" + parse_qs(u.query)["list"][0]
    return key.rstrip("/")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def keys(it):
    ks = {"u:" + canon(it.get("url"))} if canon(it.get("url")) else set()
    if it.get("id_hint"):
        ks.add("i:" + slug(it["id_hint"]))
    for a in it.get("alt_urls") or []:
        c = canon(a)
        # 只用足够具体的备用链接做去重键，避免“同一站点首页”把不同课程并在一起
        if c and (c.startswith("github.com/") and c.count("/") == 2 or c.count("/") >= 3):
            ks.add("u:" + c)
    return ks


def similar(a, b):
    if slug(a.get("provider")) != slug(b.get("provider")):
        return False
    return difflib.SequenceMatcher(None, (a.get("title") or "").lower(), (b.get("title") or "").lower()).ratio() >= 0.88


def union_list(a, b):
    out = list(a or [])
    for x in b or []:
        if x not in out:
            out.append(x)
    return out


def merge_two(base, new):
    """base 是已有条目；new 并入。文字取置信度高者。"""
    seen = union_list(base.get("seen_in"), new.get("seen_in"))
    if CONF.get(new.get("confidence"), 0) > CONF.get(base.get("confidence"), 0):
        keep = {k: base[k] for k in ("id", "first_seen") if k in base}
        base, new = {**new, **keep}, base
    base["seen_in"] = seen
    for k in ("areas", "format", "alt_urls"):
        base[k] = union_list(base.get(k), new.get(k))
    if new.get("url") and canon(new["url"]) != canon(base.get("url")):
        base["alt_urls"] = union_list(base["alt_urls"], [new["url"]])
    names = {(u.get("name") or "").lower() for u in base.get("units") or []}
    base["units"] = list(base.get("units") or []) + [u for u in new.get("units") or [] if (u.get("name") or "").lower() not in names]
    for k, v in new.items():
        if base.get(k) in (None, "", []) and v not in (None, "", []):
            base[k] = v
    return base


def cmd_merge(files):
    cat = load(CAT, [])
    log = load(LOG, [])
    before = len(cat)
    added = merged = 0
    done = {b for c in cat for b in c.get("seen_in", [])}
    for f in files:
        batch = pathlib.Path(f).stem
        if batch in done:
            print(f"跳过 {batch}：这批已经并入过")
            continue
        for it in json.loads(pathlib.Path(f).read_text(encoding="utf-8")):
            it = dict(it, seen_in=[batch])
            ks = keys(it)
            hit = next((c for c in cat if ks & keys(c) or similar(c, it)), None)
            if hit:
                why = "相同链接/短名" if ks & keys(hit) else "同机构、标题相似"
                log.append({"date": TODAY, "kept": hit["id"], "merged": it.get("title"), "from": batch, "why": why})
                cat[cat.index(hit)] = merge_two(hit, it)
                merged += 1
            else:
                it["id"] = "K-%03d" % (max([int(c["id"][2:]) for c in cat] or [0]) + 1)
                it["first_seen"] = TODAY
                cat.append(it)
                added += 1
    link_cards(cat)
    save(CAT, cat)
    save(LOG, log)
    print(f"目录 {before} → {len(cat)} 条：新增 {added}，合并重复 {merged}（合并明细见 dedupe_log.json）")


def link_cards(cat):
    """和事实卡片关联：卡片正文里出现该条目的链接（规范化后）或专属域名就算关联。"""
    cards = {p.stem: p.read_text(encoding="utf-8").lower() for p in FACTS.glob("F-*.md")} if FACTS.exists() else {}
    broad = {"github.com", "youtube.com", "x.com", "medium.com", "google.com", "support.google.com", "anthropic.com",
             "openai.com", "huggingface.co", "deeplearning.ai", "learn.deeplearning.ai", "web.stanford.edu", "maven.com",
             "coursera.org", "poynter.org", "developer.apple.com", "storage.googleapis.com", "thepaper.cn"}
    for c in cat:
        needles = {canon(u) for u in [c.get("url"), *(c.get("alt_urls") or [])] if canon(u)}
        needles = {n.split("/", 1)[1] if n.startswith("github.com/") else n for n in needles}
        # 主链接是专属域名（如课程官网）时，卡片里出现主机名就算关联
        main = (canon(c.get("url")) or "/").split("/")[0]
        if main not in broad and "." in main:
            needles.add(main)
        c["cards"] = sorted(cid for cid, txt in cards.items() if any(n and n in txt for n in needles))


def cmd_relink():
    cat = load(CAT, [])
    link_cards(cat)
    save(CAT, cat)
    print(f"已重算 {sum(1 for c in cat if c['cards'])} 条资源的卡片关联")


def gaps():
    cap = load(CAP, {})
    rows = [dict(a, score=(a["target"] - a["now"]) * a["weight"]) for a in cap.get("areas", [])]
    return sorted(rows, key=lambda a: (-a["score"], a["id"]))


def cmd_gap():
    for a in gaps():
        print(f"{a['id']:>3} {a['name']:<14} 现在 {a['now']} → 目标 {a['target']} ×权重 {a['weight']} = {a['score']}  | {a['gap']}")


def cmd_level(args):
    if len(args) < 3:
        sys.exit("用法：level C4 3 依据（如提交号和评分）")
    cap = load(CAP, {})
    a = next(x for x in cap["areas"] if x["id"] == args[0])
    a.setdefault("history", []).append({"date": TODAY, "from": a["now"], "to": int(args[1]), "why": " ".join(args[2:])})
    a["now"] = int(args[1])
    cap["as_of"] = TODAY
    save(CAP, cap)
    print(f"{a['id']} {a['name']}：→ {a['now']} 级")


def cmd_build():
    data = {"generated": TODAY, "capabilities": load(CAP, {}), "gaps": gaps(),
            "catalog": load(CAT, []), "plan": load(PLAN, {}), "dedupe": load(LOG, []),
            "topics": load(HERE / "topics.json", {"groups": []})}
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = HERE / "知识扩张.html"
    out.write_text(tpl.replace("/*__DATA__*/null", blob), encoding="utf-8")
    print(f"已生成 {out.name}：{len(data['catalog'])} 条资源，{len(data['plan'].get('items', []))} 个学习单元")


def cmd_currency(files):
    """把时效复核结果（[{id,currency,note_zh,outdated_parts_zh,superseded_by,evidence,last_updated}]）写进目录；
    已淘汰的条目从 topics.json 的 pick/also/alts 移到该主题的 retired。"""
    cat = load(CAT, [])
    by = {c["id"]: c for c in cat}
    n = {"适用": 0, "部分过时": 0, "已淘汰": 0}
    for f in files:
        for r in json.loads(pathlib.Path(f).read_text(encoding="utf-8")):
            c = by.get(r.get("id"))
            if not c or r.get("currency") not in n:
                print("跳过", r.get("id"), r.get("currency"))
                continue
            c.update({"currency": r["currency"], "currency_note": r.get("note_zh"),
                      "outdated_parts": r.get("outdated_parts_zh"), "superseded_by": r.get("superseded_by"),
                      "currency_evidence": r.get("evidence"), "last_updated": r.get("last_updated"), "checked": TODAY})
            n[r["currency"]] += 1
    save(CAT, cat)
    tp = HERE / "topics.json"
    t = load(tp, {"groups": []})
    gone = {c["id"] for c in cat if c.get("currency") == "已淘汰"}
    for g in t["groups"]:
        moved = [k for k in g["pick"] + g["also"] + g["alts"] if k in gone]
        if moved:
            g["retired"] = sorted(set(g.get("retired", [])) | set(moved))
            for k in ("pick", "also", "alts"):
                g[k] = [x for x in g[k] if x not in gone]
            if not g["pick"]:
                print(f"注意：主题 {g['id']} {g['name']} 的首选全部被淘汰，需要重新选")
    save(tp, t)
    print("时效复核：" + "，".join(f"{k} {v}" for k, v in n.items()) + f"；已淘汰的 {len(gone)} 条移出学习主题")


def cmd_study():
    """把 lessons/*.json 嵌进 study_template.html，生成 学习室.html。"""
    ls = [json.loads(f.read_text(encoding="utf-8")) for f in sorted((HERE / "lessons").glob("*.json"))]
    ls.sort(key=lambda x: x.get("order", 99))
    for l in ls:
        for k in ("id", "title", "material", "key_points", "quiz", "assignment", "sources"):
            assert k in l, f"{l.get('id')} 缺少 {k}"
        assert sum(r["points"] for r in l["assignment"]["rubric"]) == 100, f"{l['id']} 作业评分表不是 100 分"
        for q in l["quiz"]["mcq"]:
            assert 0 <= q["answer"] < len(q["options"]), f"{l['id']} 选择题答案越界：{q['q'][:20]}"
    blob = json.dumps({"generated": TODAY, "lessons": ls}, ensure_ascii=False).replace("</", "<\\/")
    tpl = (HERE / "study_template.html").read_text(encoding="utf-8")
    (HERE / "学习室.html").write_text(tpl.replace("/*__DATA__*/null", blob), encoding="utf-8")
    print(f"已生成 学习室.html：{len(ls)} 个主题")


if __name__ == "__main__":
    cmd, *rest = sys.argv[1:] or ["gap"]
    {"merge": lambda: cmd_merge(rest), "relink": cmd_relink, "gap": cmd_gap, "level": lambda: cmd_level(rest), "build": cmd_build, "study": cmd_study, "currency": lambda: cmd_currency(rest)}[cmd]()
