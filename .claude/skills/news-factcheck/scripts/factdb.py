#!/usr/bin/env python3
"""事实卡片小工具。

用法:
  factdb.py search <关键词...>   查找已有卡片（匹配 claim/subject/tags/正文）
  factdb.py next-id              下一个可用编号
  factdb.py rebuild              按卡片重新生成 事实清单.md 的静态表
  factdb.py due [--days N]       列出 N 天内到期的预测卡（默认 7）和超过 90 天未核实的数字卡
  factdb.py supersede 旧ID 新ID [原因]  新事实推翻旧事实：旧卡标“已过时”并指向新卡，不删除
  factdb.py entities             按 Entities/*.md 的 aliases 重新生成各实体页的“相关卡片”区
  factdb.py import <暂存目录>     批量模式：把 TMP-xx 卡片正式编号、改写链接并移入 Facts/ 与 Notes/
search 会按 别名表.md 和实体页 aliases 自动扩展同义词（Meta=Facebook 等）。
可选 --vault <FactCheck 目录>；默认从当前目录向上查找 FactCheck/事实清单.md。
"""
import argparse, datetime, pathlib, re, signal, sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # 允许 | head

START, END = "<!-- facts:start -->", "<!-- facts:end -->"


def find_vault(arg):
    if arg:
        return pathlib.Path(arg)
    here = pathlib.Path.cwd().resolve()
    for d in [here, *here.parents]:
        for cand in (d / "FactCheck", d):
            if (cand / "事实清单.md").exists():
                return cand
    sys.exit("找不到 FactCheck/事实清单.md，请用 --vault 指定")


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    body = text
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep and not line.startswith(" "):
                v = v.split("  #")[0].strip().strip('"')
                meta[k.strip()] = v
    meta["_body"] = body
    meta["_path"] = path
    return meta


def cards(vault):
    out = []
    for p in sorted((vault / "Facts").glob("F-*.md")):
        c = parse(p)
        if c.get("id") and c["id"] != "F-0000":
            out.append(c)
    return out


def as_list(v):
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    return [x.strip().strip('"\'') for x in v.split(",") if x.strip()]


def entity_pages(vault):
    return [parse(p) for p in sorted((vault / "Entities").glob("*.md"))] if (vault / "Entities").exists() else []


def alias_groups(vault):
    """别名表.md 每行“- A = B = C”；实体页 frontmatter 的 aliases 也算一组。"""
    groups = []
    tbl = vault / "别名表.md"
    if tbl.exists():
        for line in tbl.read_text(encoding="utf-8").splitlines():
            line = line.strip().lstrip("-*").strip()
            if "=" in line and not line.startswith("#"):
                groups.append([x.strip() for x in line.split("=") if x.strip()])
    for e in entity_pages(vault):
        names = as_list(e.get("aliases"))
        if names:
            groups.append(names)
    return groups


def expand(term, groups):
    t = term.lower()
    out = {t}
    for g in groups:
        if t in (x.lower() for x in g):
            out |= {x.lower() for x in g}
    return out


def flags(c):
    f = ""
    if c.get("value"):
        f += f" [{c['value']}]"
    if c.get("superseded_by"):
        f += f" [→{c['superseded_by']}]"
    return f


def cmd_search(vault, terms):
    groups = alias_groups(vault)
    sets = [expand(t, groups) for t in terms]
    for t, st in zip(terms, sets):
        if len(st) > 1:
            print(f"（{t} 按别名扩展为：{' / '.join(sorted(st))}）")
    hits = 0
    for c in cards(vault):
        hay = " ".join([c.get("claim", ""), c.get("subject", ""), c.get("tags", ""), c["_body"]]).lower()
        if all(any(x in hay for x in st) for st in sets):
            hits += 1
            print(f"{c['id']} | {c.get('status','')} | {c.get('confidence','')}{flags(c)} | {c.get('claim','')}")
    if not hits:
        print("（无匹配卡片）")


def cmd_next(vault):
    nums = [int(c["id"][2:]) for c in cards(vault) if re.fullmatch(r"F-\d+", c["id"])]
    print(f"F-{(max(nums) if nums else 0) + 1:04d}")


def cmd_rebuild(vault):
    rows = ["| ID | 类型 | 命题 | 状态 | 置信度 | 主题 | 事实时间 | 最近核查 |", "|---|---|---|---|---|---|---|---|"]
    for c in cards(vault):
        st = c.get("status", "")
        if st in ("证伪", "存疑"):
            st = f"**{st}**"
        if c.get("superseded_by"):
            st = f"~~{st}~~ → [[{c['superseded_by']}]]"
        if c.get("value"):
            st += f" ({c['value']})"
        claim = c.get("claim", "").replace("|", "\\|")
        rows.append(f"| [[{c['id']}]] | {c.get('type','')} | {claim} | {st} | {c.get('confidence','')} | {c.get('subject','')} | {c.get('as_of','')} | {c.get('last_checked','')} |")
    table = "\n".join(rows)
    idx = vault / "事实清单.md"
    text = idx.read_text(encoding="utf-8")
    block = f"{START}\n{table}\n{END}"
    if START in text and END in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    else:
        text = re.sub(r"## 静态清单.*\Z", "", text, flags=re.S).rstrip() + "\n\n## 静态清单（脚本生成，勿手改）\n" + block + "\n"
    idx.write_text(text, encoding="utf-8")
    print(f"已重建 {len(rows) - 2} 张卡片 → {idx}")


def cmd_due(vault, days=7):
    today = datetime.date.today()
    horizon = (today + datetime.timedelta(days=days)).isoformat()
    stale = (today - datetime.timedelta(days=90)).isoformat()
    n = 0
    for c in cards(vault):
        if c.get("superseded_by") or c.get("value") == "无用":
            continue
        rb = c.get("review_by", "")
        if rb and c.get("last_checked", "") >= rb:
            rb = ""  # 到期后已回看过，不再重复列出
        if rb and rb <= horizon:
            n += 1
            print(f"{c['id']} | {'已到期' if rb <= today.isoformat() else '即将到期'} {rb} | {c.get('claim','')}")
        elif c.get("type") == "数字" and c.get("last_checked", "9999") < stale:
            n += 1
            print(f"{c['id']} | 久未核实（{c.get('last_checked')}） | {c.get('claim','')}")
    if not n:
        print(f"（{days} 天内没有到期或久未核实的卡片）")


def set_field(text, key, value):
    if re.search(rf"^{key}:.*$", text, re.M):
        return re.sub(rf"^{key}:.*$", f"{key}: {value}", text, count=1, flags=re.M)
    return re.sub(r"^(tags:.*)$", rf"{key}: {value}\n\1", text, count=1, flags=re.M)


def log_line(text, line):
    return text.rstrip("\n") + f"\n- {line}\n"


def cmd_supersede(vault, args):
    if len(args) < 2:
        sys.exit("用法：supersede 旧ID 新ID [原因]")
    old, new, why = args[0], args[1], " ".join(args[2:]) or "新事实推翻旧事实"
    today = datetime.date.today().isoformat()
    po, pn = vault / "Facts" / f"{old}.md", vault / "Facts" / f"{new}.md"
    if not (po.exists() and pn.exists()):
        sys.exit("找不到卡片")
    t = po.read_text(encoding="utf-8")
    prev = parse(po).get("status", "")
    t = set_field(t, "status", "已过时")
    t = set_field(t, "superseded_by", new)
    t = set_field(t, "last_checked", today)
    t = log_line(t, f"{today} 已过时（原状态：{prev}），被 [[{new}]] 取代：{why}")
    po.write_text(t, encoding="utf-8")
    t = pn.read_text(encoding="utf-8")
    t = set_field(t, "supersedes", old)
    t = log_line(t, f"{today} 取代 [[{old}]]：{why}")
    pn.write_text(t, encoding="utf-8")
    print(f"{old} → 已过时，由 {new} 取代")


def cmd_entities(vault):
    cs = cards(vault)
    for e in entity_pages(vault):
        names = [x.lower() for x in as_list(e.get("aliases"))]
        if not names:
            continue
        rows = []
        for c in cs:
            hay = " ".join([c.get("claim", ""), c.get("subject", ""), c.get("tags", "")]).lower()
            if any(n in hay for n in names):
                rows.append(f"| [[{c['id']}]] | {c.get('status','')}{flags(c)} | {c.get('as_of','')} | {c.get('claim','').replace('|', '/')} |")
        block = "<!-- cards:start -->\n| 卡片 | 状态 | 事实时间 | 命题 |\n|---|---|---|---|\n" + "\n".join(rows) + "\n<!-- cards:end -->"
        p = e["_path"]
        text = p.read_text(encoding="utf-8")
        text = re.sub(r"<!-- cards:start -->.*?<!-- cards:end -->", lambda _: block, text, flags=re.S)
        p.write_text(text, encoding="utf-8")
        print(f"{p.stem}: {len(rows)} 张相关卡片")


def cmd_import(vault, dirs):
    nums = [int(c["id"][2:]) for c in cards(vault) if re.fullmatch(r"F-\d+", c["id"])]
    nxt = (max(nums) if nums else 0) + 1
    for d in map(pathlib.Path, dirs):
        tmps = sorted(d.glob("TMP-*.md"))
        mapping = {}
        for t in tmps:
            mapping[t.stem] = f"F-{nxt:04d}"
            nxt += 1
        pat = re.compile(r"(?<![A-Za-z0-9])TMP-\d+(?!\d)")
        files = [f for f in d.glob("*.md")]
        for f in files:
            txt = pat.sub(lambda m: mapping.get(m.group(0), m.group(0)), f.read_text(encoding="utf-8"))
            if f.stem in mapping:
                (vault / "Facts" / f"{mapping[f.stem]}.md").write_text(txt, encoding="utf-8")
                f.unlink()
            else:
                f.write_text(txt, encoding="utf-8")
        for f in d.glob("*.md"):
            dest = vault / "Notes" / f.name
            f.rename(dest)
            print(f"笔记 → {dest.name}")
        for k, v in mapping.items():
            print(f"  {d.name}: {k} → {v}")
        try:
            d.rmdir()
        except OSError:
            print(f"  （{d} 还有其他文件，未删除）")
    cmd_rebuild(vault)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["search", "next-id", "rebuild", "due", "import", "supersede", "entities"])
    ap.add_argument("terms", nargs="*")
    ap.add_argument("--vault")
    ap.add_argument("--days", type=int, default=7)
    a = ap.parse_args()
    v = find_vault(a.vault)
    {"search": lambda: cmd_search(v, a.terms), "next-id": lambda: cmd_next(v),
     "rebuild": lambda: cmd_rebuild(v), "due": lambda: cmd_due(v, a.days),
     "import": lambda: cmd_import(v, a.terms), "supersede": lambda: cmd_supersede(v, a.terms),
     "entities": lambda: cmd_entities(v)}[a.cmd]()


if __name__ == "__main__":
    main()
