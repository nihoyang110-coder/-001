# 给本地 Claude Code 的提示词（中文版）

> 基于 [cleanyourtv/PROMPT.md](https://github.com/Gathin23/cleanyourtv/blob/main/PROMPT.md)（MIT，© 2026 Gathin）改写，加入了你的电视信息和更严格的安全规则。
> 用法：在 Mac 上先 `cd` 进克隆好的 cleanyourtv 文件夹再启动 `claude`，然后把下面两条分隔线之间的内容复制进去。把 `【型号】`、`【Android 版本】`、`【IP】` 换成实际值（不知道的就写“不知道”）。

---（从这里开始复制）---

请用中文、白话和我交流，我不是程序员。

我想给家里的电视去广告，并在可行时换成一个干净的 Apple TV 风格桌面。
- 电视：海信 Hisense，日本购入（日本版），型号【型号】，系统【Google TV / Android TV】，Android 版本【Android 版本】。
- 电视 IP：【IP】（不知道就帮我在局域网里找，或者告诉我去哪里看）。
- 电脑：Mac，和电视在同一个 Wi-Fi。
- 当前文件夹是 cleanyourtv 仓库，请复用里面的 tools/、launcher/、examples/ 和 docs/TROUBLESHOOTING.md，不要从头重写。先读 README.md、PROMPT.md、docs/TROUBLESHOOTING.md 和 examples/hisense-smarttv-4k-ffm/debloat.txt（最接近的海信安卓清单，但它是拉美版，包名可能不同）。

必须遵守的规则：
1. **只停用，不卸载。** 只用 `pm disable-user --user 0`，绝不 uninstall 系统应用，绝不 root、刷机。
2. **先备份。** 动手前把完整软件包列表、已停用列表、getprop、全部 settings 保存到 backup/日期 文件夹，并写好能一键恢复的脚本。每一批改动前都更新备份记录。
3. **动手前先列清单让我确认。** 每一批要停用的包，用表格列出“包名 / 你判断它是做什么的 / 依据”，等我回复“确认”再执行。不确定用途的包，先用 `dumpsys package` 查它的组件，仍不确定就不动并问我。
4. **小批量、每批验证。** 每批不超过 5 个，`pm` 命令一次只执行一条；每批后截图看主页，并提醒我用遥控器测试主页键、音量、信号源切换和看电视台节目。等我说正常再继续。
5. **绝不停用：** 电视台/调谐器/HDMI 相关（日本 ISDB 数字电视、B-CAS/ACAS、TV input 服务、com.mediatek.* 等）、信号源菜单、遥控器和蓝牙配对、屏幕键盘、Google Play 商店和 Play 服务、画质/声音相关服务；海信的 `com.hisense.tv.smartsense`、`com.vt.tv.smartsense.ui`、`com.vt.tv.aiot`（另一台海信停用后开机进了恢复模式）。
6. **涉及我偏好的先问我：** 流媒体应用（Netflix、YouTube、TVer、U-NEXT、Prime Video 等）、语音助手、投屏（Chromecast）、固件更新服务，用勾选清单问我，只停用我没勾的。
7. 什么时候电视上会弹出“允许 USB 调试吗？”，提前告诉我去按“允许”。如果 macOS 的 adb 报 “No route to host”，不要调试它，直接用仓库里的 tools/tv.py。

换桌面：
- 先测试电视能不能安装外部 APK。如果出现 `INSTALL_FAILED_VERIFICATION_FAILURE`，或者带 HOME 的应用因签名被拒，就明确告诉我“这台只能去广告、不能换桌面”，停止重试。
- 能装的话，用仓库自带的 launcher（`launcher/build-and-install.sh`），只改 `config.xml`：问我底部放哪 4 个应用、什么顺序。缺 JDK 17 / Android SDK 的话，告诉我要装什么、占多少空间，等我同意再装。
- 先手动打开新桌面确认能用，再设为主屏、再停用原桌面。如果是 Google TV，按 TROUBLESHOOTING 处理 `com.google.android.tungsten.setupwraith`，并把它写进清单，保证恢复脚本能把它恢复。
- 换完后测试“Inputs”按钮能否切到地上波/BS/HDMI。

结束时：
- 给我：恢复脚本、本次停用的完整清单（debloat.txt 格式）、一份中文说明（怎么恢复某个应用、怎么改底部应用）。
- 提醒我在电视上关掉 USB 调试 / 网络调试和开发者选项。
- 最后用 5 行以内总结：做成了什么、没做成什么、原因。

---（复制到这里结束）---
