@AGENTS.md

## Claude Code 专用
- 用户发来新闻、截图或说法要核查，或要做发布内容时，使用技能 `news-factcheck`（`.claude/skills/news-factcheck/`），先读它的 SKILL.md 再动手。只是查已有卡片、取编号，直接用上面的命令，不必读技能。改了技能文件要重新打包仓库根目录的 `news-factcheck.skill`
- 定时任务（每周一回看事实库、每月 1 日更新知识扩张）都发到常驻会话“事实清单每周回看（常驻）”，因为只有挂了本仓库的会话才能推送。不要归档这个会话。任务的提示词改动要记进 `FactCheck/变更记录.md`
- 知识扩张页面 https://claude.ai/artifact/7tTk3PTuohyXK94BL5Nox4 由 `Projects/知识扩张/知识扩张.html` 发布，运行 `kx.py build` 后重新发布到这个地址
- 多条新闻同时核查时，用子智能体并行，各自只写 `FactCheck/_staging/<英文短名>/`，最后由主会话统一 `import`
