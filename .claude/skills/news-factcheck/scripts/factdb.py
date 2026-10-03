#!/usr/bin/env python3
"""事实卡片小工具。

用法:
  factdb.py search <关键词...>   查找已有卡片（匹配 claim/subject/tags/正文）
  factdb.py next-id              下一个可用编号
  factdb.py rebuild              按卡片重新生成 事实清单.md 的静态表
  factdb.py due                  列出 review_by 已到期的预测卡
  factdb.py import <暂存目录>     批量模式：把 TMP-xx 卡片正式编号、改写链接并移入 Facts/ 与 Notes/
可选 --vault <FactCheck 目录>；默认从当前目录向上查找 FactCheck/事实清单.md。
"""
import argparse, datetime, pathlib, re, sys

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


def cmd_search(vault, terms):
    terms = [t.lower() for t in terms]
    hits = 0
    for c in cards(vault):
        hay = " ".join([c.get("claim", ""), c.get("subject", ""), c.get("tags", ""), c["_body"]]).lower()
        if all(t in hay for t in terms):
            hits += 1
            print(f"{c['id']} | {c.get('status','')} | {c.get('confidence','')} | {c.get('claim','')}")
    if not hits:
        print("（无匹配卡片）")


def cmd_next(vault):
    nums = [int(c["id"][2:]) for c in cards(vault) if re.fullmatch(r"F-\d+", c["id"])]
    print(f"F-{(max(nums) if nums else 0) + 1:04d}")


def cmd_rebuild(vault):
    rows = ["| ID | 类型 | 命题 | 状态 | 置信度 | 主题 | 最近核查 |", "|---|---|---|---|---|---|---|"]
    for c in cards(vault):
        st = c.get("status", "")
        if st in ("证伪", "存疑"):
            st = f"**{st}**"
        claim = c.get("claim", "").replace("|", "\\|")
        rows.append(f"| [[{c['id']}]] | {c.get('type','')} | {claim} | {st} | {c.get('confidence','')} | {c.get('subject','')} | {c.get('last_checked','')} |")
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


def cmd_due(vault):
    today = datetime.date.today().isoformat()
    for c in cards(vault):
        rb = c.get("review_by", "")
        if rb and rb <= today:
            print(f"{c['id']} | 到期 {rb} | {c.get('claim','')}")


def cmd_import(vault, dirs):
    nums = [int(c["id"][2:]) for c in cards(vault) if re.fullmatch(r"F-\d+", c["id"])]
    nxt = (max(nums) if nums else 0) + 1
    for d in map(pathlib.Path, dirs):
        tmps = sorted(d.glob("TMP-*.md"))
        mapping = {}
        for t in tmps:
            mapping[t.stem] = f"F-{nxt:04d}"
            nxt += 1
        pat = re.compile(r"\bTMP-\d+\b")
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
    ap.add_argument("cmd", choices=["search", "next-id", "rebuild", "due", "import"])
    ap.add_argument("terms", nargs="*")
    ap.add_argument("--vault")
    a = ap.parse_args()
    v = find_vault(a.vault)
    {"search": lambda: cmd_search(v, a.terms), "next-id": lambda: cmd_next(v),
     "rebuild": lambda: cmd_rebuild(v), "due": lambda: cmd_due(v),
     "import": lambda: cmd_import(v, a.terms)}[a.cmd]()


if __name__ == "__main__":
    main()
