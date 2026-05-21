# longtext-to-slides

> 把任意长文档 / 粘贴文本 / URL / 主题方向，**智能压缩**成一份精美的 HTML 演示文稿。
> 单文件、零依赖、浏览器直接打开。
> 专为「中文长文」场景优化（字体栈 / 行高 / 字距 / 版式都为中文调过）。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)

---

## ✨ 特色

- **4 种输入**：本地文件（PDF/DOCX/EPUB/MD/HTML/TXT）/ 对话粘贴文本 / URL（含微信公众号特殊处理）/ 主题方向自创
- **15 套风格预设** + **7 维 DIY**（风格 / 配色 / 字号 / 版式比例 / 大纲详略 / 主标题字体 / 动画强度）
- **14 位视觉大师美学指导** 内嵌（Carson / Vignelli / 原研哉 / Tufte / Rams / 吕敬人 / 韩家英 ...），**自包含、不依赖外部 skill**
- **舞台引擎**：1280×720 fit-to-viewport scale + `data-state` 翻页（更接近真正 PPT 体验，不是滚动）
- **中英双语支持**：自动检测语言；纯英文输入自动翻译；双语版式齐全
- **图片自动处理**：提取 → 智能 base64 或 assets/ 文件夹
- **可导出 PPTX**：Playwright 截图法（每张 frame → 1920×1080 PNG → 嵌入 PPTX）

---

## 🚀 安装

### 通过 skills CLI（推荐）

```bash
npx skills add xxximcoolguy/long2ppt
```

> **命名说明：** GitHub 仓库名为 `long2ppt`，但 skill 内部名（`SKILL.md` 内 `name:`）为 `longtext-to-slides`。两者解耦：安装命令用仓库名，skill 系统识别和触发用内部名。

### 手动安装

```bash
# 1. clone 到 Claude Code skill 目录
git clone https://github.com/xxximcoolguy/long2ppt.git \
  ~/.claude/skills/longtext-to-slides

# 2. 装 Python 依赖
pip install -r ~/.claude/skills/longtext-to-slides/requirements.txt

# 3.（可选）PPTX 导出需要 Playwright
pip install playwright python-pptx
playwright install chromium
```

### 设置输出目录（可选）

```bash
# Mac / Linux
export LONG2PPT_OUTPUT=~/Documents/slides

# Windows (PowerShell)
$env:LONG2PPT_OUTPUT = "$env:USERPROFILE\Documents\slides"

# 不设置则默认 ~/long2ppt/
```

---

## 📖 使用

在 Claude Code 中：

```
> 把这本书转成 PPT
  /path/to/book.pdf

> 这个 URL 做成演示文稿
  https://mp.weixin.qq.com/s/xxxxxx

> 做一个关于"团队管理 12 条"的 PPT
```

或显式触发：

```
> /longtext-to-slides /path/to/file.pdf
```

---

## 🎨 14 位视觉大师风格

| 系列 | 大师 |
|---|---|
| **现代主义**（5）| Vignelli · Tschichold · Crouwel · Rams · Tufte |
| **解构 / 反叛**（3）| Carson · Brody · Scher |
| **情绪 / 海报**（2）| Sagmeister · Saul Bass |
| **东方留白**（2）| 原研哉 Kenya Hara · 朱赢椿 |
| **东方密度**（2）| 杉浦+吕敬人 · 韩家英 |

每位大师按 5 层框架（视觉哲学 / 版式手法 / 颜色字体 / 视觉禁忌 / 局限）封装。详见 [aesthetics/README.md](aesthetics/README.md)。

---

## 📂 项目结构

```
longtext-to-slides/
├── SKILL.md                  ← 主流程（入口）
├── routing.md                ← 风格→大师美学路由
├── mode-d-original.md        ← 主题自创流程
├── presets.md                ← 15 套风格预设
├── layouts.md                ← 17 种版式（cover/preface/toc/...）
├── typography.md             ← 中文字体栈
├── animation-presets.md      ← 动画强度
├── deck.css                  ← 舞台引擎基线 CSS
├── deck.js                   ← 翻页 / 缩放 / 输入控制 JS
├── aesthetics/               ← 14 位大师美学（自包含）
│   ├── README.md
│   ├── carson.md  vignelli.md  hara.md  ...
├── scripts/
│   ├── extract.py            ← 文本+图片提取
│   └── export_pptx.py        ← HTML → PPTX
├── examples/                 ← 参考产出
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🎯 何时不用本 skill

- **需要 mood-based 风格探索**（看 3 个预览选）→ 用 `frontend-slides`
- **从 PPTX 转 HTML** → 用 `frontend-slides` 的 Phase 4
- **单页 Web / 海报 / 卡片** → 用 `ljg-card` / `canvas-design`

---

## 🛠️ 路线图

- [x] 4 种输入模式（A 文件 / B 粘贴 / C URL / D 主题自创）
- [x] 15 套风格预设 · 7 维 DIY
- [x] 14 位视觉大师美学嵌入
- [x] 中英双语支持
- [x] 图片自动处理（base64 / assets）
- [x] PPTX 导出（Playwright + python-pptx）
- [x] 微信公众号 URL 抓取（baoyu-url-to-markdown）
- [ ] 主题自创模式的多语言 prompt
- [ ] aesthetics/ 大师生成的「视觉风格预览图」
- [ ] CI 测试

---

## 🤝 贡献

欢迎 Issue / PR。蒸馏新的视觉大师 skill 推荐方法：

1. 用 [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 蒸馏出独立 skill
2. 复制 `SKILL.md` 到本仓库 `aesthetics/<name>.md`
3. 更新 `routing.md` 路由表
4. 更新 `aesthetics/README.md` 索引

---

## 📜 License

MIT —— 见 [LICENSE](LICENSE)。

## 🙏 致谢

- 14 位视觉大师方法论的提炼参考了大量一手 / 二手公开资料（每位 `aesthetics/<name>.md` 末尾标注 sources）
- 蒸馏方法论框架来自 [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 的 5 层结构
- 公众号 URL 抓取依赖 [baoyu-url-to-markdown](https://github.com/) 的 Chrome CDP 方案
