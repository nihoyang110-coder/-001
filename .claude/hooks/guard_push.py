#!/usr/bin/env python3
"""PreToolUse 钩子：只允许 git push 到本仓库的工作分支，推到其他分支一律拦下（退出码 2）。"""
import json, re, shlex, subprocess, sys

ALLOWED = "claude/news-fact-check-analysis-q0n5cs"


def current_branch(cwd):
    try:
        return subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd,
                              capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


def check(cmd, cwd):
    """返回错误说明；没问题返回 None。"""
    for seg in re.split(r"&&|\|\||;|\n|\|", cmd):
        try:
            toks = shlex.split(seg)
        except ValueError:
            toks = seg.split()
        if "git" not in toks or "push" not in toks:
            continue
        i = toks.index("push")
        if i < toks.index("git"):
            continue
        args, skip = [], False
        for a in toks[i + 1:]:
            if skip:
                skip = False
                continue
            if re.fullmatch(r"\d*(>>?|<)(&\d+)?", a):   # 单独的重定向符号，后面跟文件名
                skip = not a.endswith(tuple("0123456789"))
                continue
            if re.match(r"^\d*(>>?|<)", a) or a.startswith("&>"):   # 2>&1、>/dev/null 之类
                continue
            args.append(a)
        if any(a in ("--all", "--mirror", "--tags", "-d", "--delete") for a in args):
            return f"不允许 `{seg.strip()}`：只能推送分支 {ALLOWED}"
        pos = [a for a in args if not a.startswith("-")]
        refspecs = pos[1:]  # 第一个位置参数是远程名
        if not refspecs:
            br = current_branch(cwd)
            if br != ALLOWED:
                return f"当前分支是 {br or '未知'}，只能推送 {ALLOWED}"
            continue
        for r in refspecs:
            dst = r.split(":")[-1].lstrip("+")
            dst = dst.removeprefix("refs/heads/")
            if dst == "HEAD":
                dst = current_branch(cwd)
            if dst != ALLOWED:
                return f"不允许推送到 {dst or '（空）'}：只能推送 {ALLOWED}"
    return None


if __name__ == "__main__":
    data = json.load(sys.stdin)
    err = check(data.get("tool_input", {}).get("command", ""), data.get("cwd") or ".")
    if err:
        print(err, file=sys.stderr)
        sys.exit(2)
