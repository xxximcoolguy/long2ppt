---
name: longtext-to-slides
description: |
  把任意"长文内容"转换为精美的 HTML 演示文稿（单文件、零依赖）。

  输入支持四种：
  - A 本地文件（PDF/DOCX/EPUB/MD/HTML/TXT）
  - B 对话粘贴长文本（≥ 300 字）
  - C URL 链接（含微信公众号特殊处理）
  - D 主题方向自创

  专为「中文长文」场景优化（字体栈/行高/字距/版式 ≠ 英文 PPT 工具）。
  用户 DIY 7 维：风格 / 配色 / 字号尺度 / 版式比例 / 大纲详略 / 主标题字体 / 动画强度。
  支持中文 / 英文 / 双语，纯英文输入自动翻译。
  内置 14 位视觉大师 skill 路由（Carson / Vignelli / Hara / Tufte 等）。

  触发场景：
  - 「这本书转 PPT」「PDF 做成演示」「长文本生成幻灯片」
  - 提供长文档 / 粘贴长文 / 给 URL 要求"做成 PPT"
  - 给主题方向"做一个关于 X 的 PPT"希望自由生成
  - /longtext-to-slides 命令
  - 直播笔记 / 研究报告 / 文献综述 / 产品白皮书 / 聊天记录 / 公众号文章可视化

  不触发：
  - 需要 mood-based 风格探索 → frontend-slides
  - 从 PPTX 转 HTML → frontend-slides Phase 4
  - 单页 Web / 海报 / 卡片 → ljg-card / canvas-design
---

# Longtext → Slides

把任意长文档智能压缩成一份精美的 HTML 演示文稿。**单文件、零依赖、浏览器直接打开。**

---

## 30 秒概览

```
输入识别 → 准备原文 → 通读+大纲 → DIY 配置 → 生成 HTML → 交付
  Phase 0    Phase 1    Phase 2     Phase 3    Phase 4   Phase 5
```

**输出位置（按优先级）：**
1. 用户当次明确指定的路径 → 用之
2. 环境变量 `$LONG2PPT_OUTPUT` （如设置）→ 用之
3. 默认 `~/long2ppt/<title>-slides.html` （Windows: `%USERPROFILE%\long2ppt\`）
4. 目录不存在则创建。同名冲突追加日期 `-YYYYMMDD`

**核心理念：**
1. **智能压缩 ≠ 切片** —— 通读后提炼主线+论据，凝练 15-30 张
2. **中文优先** —— 字体/行高/字距都为中文调过
3. **DIY 至上** —— 7 维度每维有默认值
4. **舞台引擎** —— 1280×720 + fit-scale + `data-state` 翻页（不是滚动）
5. **大师美学加持** —— 14 位视觉大师作美学指导，**自包含**在 [aesthetics/](aesthetics/) 子目录（不依赖外部 skill）

---

## Phase 0 · 识别输入类型

| 模式 | 触发条件 | 下一步 |
|---|---|---|
| **A 文件路径** | 消息含 `.pdf` `.docx` `.epub` `.md` `.html` `.txt` 路径 | Phase 1.A `extract.py` 提取 |
| **B 粘贴文本** | 消息含 ≥ 300 字连续文本 | Phase 1.B 直接写入 source.md |
| **C URL** | 消息含 `http(s)://...` | Phase 1.C 公众号用 baoyu-url-to-markdown，其他用 defuddle |
| **D 主题自创** | 只给主题方向，无原文 | 跳到 [mode-d-original.md](mode-d-original.md) |

模糊用 AskUserQuestion 让用户明确。

---

## Phase 1 · 准备原文

### 1.A 文件提取
```bash
python scripts/extract.py <input> <out>/source.md
```
支持 PDF/DOCX/EPUB/MD/HTML/TXT + 自动图片提取到 `assets/`。

### 1.B 对话粘贴
直接写入 `source.md`，构造简化 `meta.json`（`format: "pasted"`），跳过 extract。

### 1.C URL（按类型分支）

| URL 类型 | 优先级链 |
|---|---|
| `mp.weixin.qq.com/s/...` 公众号 | ① `baoyu-url-to-markdown`（Chrome CDP）② `anything-to-notebooklm` ③ `defuddle` |
| 普通博客 / 新闻 / 文档 | ① `defuddle` ② `WebFetch` ③ `baoyu-url-to-markdown` |
| `*.pdf` 链接 | 下载 → 转模式 A |
| YouTube / B 站 | 用 `anything-to-notebooklm` 取字幕 |

**全部失败时**：让用户改用模式 B / A。

### 1.5 语言检测（自动）
读 `meta.json.dominant_lang`：
- `zh` → 单语中文
- `bilingual` → 文中已有中英对照，启用 `.bilingual-*` 版式
- `en` → Claude 边读边翻，输出 `{en, cn}` 配对

---

## Phase 2 · 通读 + 标题 + 大纲

**禁止跳读**。完整读取 `source.md`。

### 2.0 标题候选（必经）
提出 **3 个候选 + 自定义输入**（AskUserQuestion, header: `Title`）：
- A 抽象提炼 / B 直白描述 / C 金句式

### 2.1 生成大纲
按主题/逻辑骨架（不是章节顺序）压缩。**每张 slide 有明确观点 + 论据**。

- **图片**：从 meta.json 读，分配到合适版式（image-hero / image-split / image-grid / part-image）
- **金句**：扫描全文找 3-12 条 → 3 条最强成 `.aphorism` 单页 / 8-12 条进 `.maxims` 墙
- **双语**：按 dominant_lang 处理

大纲模板见 [layouts.md](layouts.md) 末尾。

### 2.2 用户确认大纲
汇报总张数 / 章节划分 / 关键节点。**等用户确认才进 Phase 3**。

---

## Phase 3 · 七维 DIY 配置

一次 AskUserQuestion 最多 4 问，分两批。

**第一批（必问）：** Q1 风格（15 套预设见 [presets.md](presets.md)）· Q2 配色（默认 / 预设色盘 / 自定义 HEX）· Q3 大纲详略（12/18/28/40 张）

**第二批（按需）：** Q4 字号尺度 / 版式比例 / 主标题字体 / 动画强度 —— **默认全跟风格走，用户主动要更多自定义才问**

---

## Phase 4 · 生成 HTML

### 4.0 加载大师美学（强制）
按用户选定风格，**完整读取** `aesthetics/<name>.md`（如 `aesthetics/carson.md`）。详见 [routing.md](routing.md) 路由表。
**不再依赖任何外部 skill**，本目录自包含 14 位大师美学操作系统。

### 4.1 组合生成
**必读文件：**
- [deck.css](deck.css) —— 完整内联到 `<style>`
- [deck.js](deck.js) —— 完整内联到 `<script>`
- [layouts.md](layouts.md) —— 17 种版式
- [presets.md](presets.md) —— 选定风格色板 + 字体
- [typography.md](typography.md) —— 中文字体栈
- [animation-presets.md](animation-presets.md) —— 动画强度

### 4.2 图片嵌入策略（自动）
```python
use_base64 = len(images) <= 5 and total_bytes <= 2 * 1024 * 1024
```
- 满足 → base64 内联（单文件）
- 否则 → 保留 `assets/` 文件夹（HTML+assets 一起交付）

### 4.3 双语适配
- `dominant_lang == zh` → 单语
- `bilingual / en` → 所有 frame 加 `.bilingual` 修饰类，字号尺度收紧一档
- 详见 layouts.md 双语版式

### 4.4 验证（必经）
**生成后用 chrome-devtools MCP 或 `start *.html` 至少验证 3 张关键 frame**：封面 / 章节扉 / 收尾。检查关键文字是否可见。

---

## Phase 5 · 交付

1. 自动打开 HTML
2. 汇报：文件位置 / 张数 / 风格 / 配色 / 图片嵌入方式
3. 导航说明：← / → / Space / Click / Esc 全屏 / 滚轮翻页
4. 可选导出：
   - PPTX：`python scripts/export_pptx.py <html> [out.pptx]`（Playwright 截图 + python-pptx）
   - PDF：浏览器 Ctrl+P
   - 截图集：`--keep-frames`

## Phase 6 · 局部修改

用户反馈"第 X 页太挤"/"换配色"/"加一页讲 Y"：
1. Read 已生成的 HTML
2. 定位 frame（`data-title` 或序号）
3. **修改前检查内容密度**（避免溢出 1280×720）
4. 修改后报告

---

## ⚠️ CSS 陷阱（必避）

1. **绝不写 `position: relative` / `static` 覆盖 `.frame`** —— `.frame` 基础是 `position:absolute; inset:0`，覆盖会让 height 坍缩为 0，所有 `bottom:N%` 子元素失位（Carson 版踩过这个坑）
2. **大字号 + 负偏移要给中文留安全区** —— 中文方块字主体必须在 deck 80%×80% 内可见。英文/数字可以越界
3. **生成后必须浏览器验证 ≥ 3 张** —— Carson / Bass 这类多 absolute 定位的风格尤其要看

## 决策铁律

- ❌ 不照搬原文（A/B/C 模式）—— 智能压缩是核心
- ❌ 不让 frame 溢出 1280×720 —— 溢出 = 拆页
- ❌ 不用泛 AI 配色（紫渐变、Inter/Arial 系）
- ❌ 不用旧 `.slide` `.chrome` `.reveal` 类名，用 `.frame` `.runner` `.unfold`
- ❌ 模式 D 不跳过草稿审核
- ✅ 永远遵守用户的 DIY 选择
- ✅ 中文为主时，西文当点缀（数字、术语）
- ✅ 模式 B/C/D 走相同的 Phase 1.5 / 2 / 3，**只有 Phase 1 来源分支不同**

---

## 支持文件索引

| 文件 | 何时读 |
|---|---|
| [routing.md](routing.md) | Phase 4.0 找大师美学路由 |
| [aesthetics/](aesthetics/) | Phase 4.0 读 `<name>.md` 加载大师美学（14 位） |
| [mode-d-original.md](mode-d-original.md) | Phase 0 识别为 D 时 |
| [presets.md](presets.md) | Phase 3 选风格 / Phase 4 取色板 |
| [typography.md](typography.md) | Phase 4 字体栈 |
| [layouts.md](layouts.md) | Phase 4 版式（17 种）+ 大纲模板 + HTML 骨架 |
| [deck.css](deck.css) | Phase 4 完整内联 |
| [deck.js](deck.js) | Phase 4 完整内联 |
| [animation-presets.md](animation-presets.md) | Phase 4 动画 |
| [scripts/extract.py](scripts/extract.py) | Phase 1.A 提取 |
| [scripts/export_pptx.py](scripts/export_pptx.py) | Phase 5 导出 PPTX |
| [examples/](examples/) | 参考产出 |
