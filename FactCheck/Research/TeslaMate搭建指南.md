---
date: 2026-10-23
tags: [指南, 特斯拉, TeslaMate]
---
# TeslaMate 搭建指南（中文简版）

> 依据：TeslaMate 官方文档（仓库 website/docs，2026-10-23 直读）；卡片 [[F-0240]] [[F-0241]] [[F-0242]] [[F-0244]]

## 0. 先搞清楚
- **不在车上改任何东西**：TeslaMate 跑在你自己的设备上，像特斯拉 App 一样通过特斯拉云端读数据。车本身不刷机、不装东西。
- 需要：一台 24 小时开机的设备（NAS、小主机、64 位树莓派 3 及以上），内存至少 1GB（建议 2GB），能上网访问特斯拉服务器；装好 Docker。

## 1. 安装（Docker）
1. 新建文件夹，放一个 `docker-compose.yml`（内容抄官方文档 Docker install 页：teslamate、postgres 数据库、grafana 看板、mosquitto 消息服务 4 个容器）
2. 改三处：`ENCRYPTION_KEY`（加密你的特斯拉令牌，随便设一长串）、`DATABASE_PASS` 和 `POSTGRES_PASSWORD`（同一个强密码）
3. **国内账号**：在 teslamate 的 environment 里加
   - `TESLA_API_HOST=https://owner-api.vn.cloud.tesla.cn`
   - `TESLA_WSS_HOST=wss://streaming.vn.cloud.tesla.cn`
4. 运行 `docker compose up -d`

## 2. 登录
1. 用令牌工具生成访问令牌：官方文档推荐 Tesla Auth（电脑版，TeslaMate 作者做的）或 iOS 的 Auth app for Tesla；用你的特斯拉账号登录，拿到 access token 和 refresh token
2. 浏览器打开 `http://设备IP:4000`，粘贴两个令牌
3. 看板在 `http://设备IP:3000`，默认账号 admin / admin，**立刻改密码**
4. 在 TeslaMate 设置 → URLs 里填好网页和看板地址

## 3. 安全（最重要）
- 只在家里网络访问；在外面看用 Tailscale / ZeroTier / VPN，或 Cloudflare Tunnel + 登录验证
- **不要**直接在路由器上把 4000、3000 端口映射到公网（2022 年有人因此被远程控制车辆，后来还扫到 1300+ 个暴露实例）
- 只从官方仓库和 Docker Hub 官方镜像安装，不用来路不明的“汉化版”“一键包”App

## 4. 以后可能要改的：Fleet API
特斯拉在逐步关闭旧接口。到时要：
1. 在 developer.tesla.cn 注册开发者账号并创建应用（中国区需 +86 手机号）
2. 准备一个自己的域名，在 `/.well-known/appspecific/com.tesla.3p.public-key.pem` 放公钥
3. 在车上批准“虚拟钥匙”（这是唯一需要在车上操作的一步）
4. 按 TeslaMate 文档 configuration/api.md 改 `TESLA_API_HOST` 为中国区 Fleet 地址 `https://fleet-api.prd.cn.vn.cloud.tesla.cn`，填入应用的 client ID
5. 注意：Fleet API 自 2025-02 起按调用量收费

## 5. 在车机屏幕上看
车机浏览器能打开网页看 Grafana 看板，但车走的是移动网络，要能安全地从外网访问你的 TeslaMate（见第 3 节的 Tailscale / Cloudflare Tunnel 方案），不要为此把端口直接暴露到公网。
