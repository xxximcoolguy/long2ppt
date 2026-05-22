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

**标题三检**（每个候选必须标注命中项，命中 ≥ 2 才提交给用户；全 0 命中重写）：
- **冲突感** — 含张力/反差/矛盾词，例：「克制是最大的奢侈」「慢就是快」
- **具体感** — 含数字/专有名词/强动词 ≥ 1，例：「7 年从亏损到 10 亿」「让 1 万人离开舒适区」
- **金句感** — ≤ 14 字，可独立成立、可被单独引用

输出示例：`A.「克制是最大的奢侈」[冲突✓ 金句✓] / B.「Less is More 设计哲学」[具体✓ 金句✓] / C....`

### 2.05 骨架卡（拦截逻辑漂移，必经）

通读后**先不展开大纲**，先输出骨架卡让用户确认主线抓对了：

```
核心主张：[1 句话，≤ 30 字]
支撑论点：
  1. [论点 A] ← 论据：[a1] [a2] [a3]
  2. [论点 B] ← 论据：[b1] [b2]
  3. [论点 C] ← 论据：[c1] [c2] [c3]
（3-5 个论点最佳，>5 个说明没抓主线，回去再读）
```

**等用户确认骨架卡，才进 2.1 展开大纲。** 用户说"主线不对/漏了 X" → 回 Phase 2 重抽，不要在大纲阶段硬补。

### 2.1 生成大纲
按 2.05 骨架卡展开（**不是章节顺序、不照搬目录**）。每张 slide 必须有 1 个明确观点 + 1-4 个论据。

- **字数预算**（必查）：按版式查 [layouts.md 字数预算表](layouts.md#字数预算表phase-21-必查)
  - 超上限 → 拆 2 页 或 换更密版式
  - 不足下限 → 合并 或 换稀疏版式（`.aphorism` / `.chapter-plate`）
  - 双语版字数 × 1.7 后再比对预算
- **图片**：从 meta.json 读，分配到合适版式（image-hero / image-split / image-grid / part-image）
- **金句五诊**（命中 ≥ 3 才入选）：
  - **独立性** — 脱离上下文也能成立
  - **反常识** — 违背直觉的洞见
  - **高密度** — < 25 字浓缩一个完整观点
  - **韵律** — 对仗 / 排比 / 押韵 / 反复
  - **普适** — 不依赖特定领域黑话
  - 入选后：3 条最强成 `.aphorism` 单页 / 8-12 条进 `.maxims` 墙；命中 < 3 的句子一律不放金句版式
- **双语**：按 dominant_lang 处理

大纲模板见 [layouts.md](layouts.md) 末尾。

### 2.2 用户确认大纲
汇报总张数 / 章节划分 / 关键节点 / 字数预算自检结果（"X 页全部在预算内"或"X 页需要调整"）。**等用户确认才进 Phase 3**。

---

## Phase 3 · 七维 DIY 配置

一次 AskUserQuestion 最多 4 问，分两批。

### Q0 · 使用模式分流（必问 · 第一个问题 · 不可跳过）

**问句**："选一下使用模式："
- 🚀 **快速模式**（推荐 · 适合首次/不会做 PPT 的用户）：我说场景，AI 帮我选风格
- 🎨 **进阶模式**（懂设计或想自己挑/二次以上使用）：我自己挑预设/混搭

**判定规则：**
- 用户在 Phase 0-2 完全没提及风格关键词 → **默认推快速模式**，不要硬推进阶
- 用户提到「我想要 Carson 风 / Tufte 风 / Brody 风 / Wabi Sabi 风」等任何具体大师/美学词 → **直接进进阶模式**，跳过本 Q0
- 用户说「随便」「你看着办」「都行」 → **默认快速模式 + 后台推 Rams**（最稳）

---

### Q1 · 风格选择（分支执行）

#### 🚀 Q1·快速模式（场景化推荐）

**Q1a 场景**（一次 AskUserQuestion · 4 选 1）：
- 🏢 工作汇报 / 演示 / 公司内部
- 📖 读书笔记 / 文献综述 / 知识分享
- 📱 朋友圈分享 / 社媒爆款 / 营销文案
- 🎤 演讲 Keynote / TED / 个人故事

**Q1b 推荐 + 验收**（按 Q1a 结果查 [routing.md 场景→大师推荐路由](routing.md#场景--大师推荐路由phase-3-q1-快速模式必查)）：

1. 取**主推大师**，从 `routing.md` 一句话理由库取对应文案
2. 输出格式：「AI 给你推荐这套风格：『[一句话理由]』，要试试吗？」
3. **绝不暴露大师名字给小白用户**（Carson/Brody/Crouwel 等术语对小白零信息量）
4. 用户回应：
   - 「就用这个」/「好」/「可以」 → 后台加载对应 `aesthetics/<name>.md`，继续 Q2
   - 「换一个看看」 → 给次推，重复步骤 1-3
   - 「再换」 → 给备选
   - 连续 3 次说换 → 提示「你可能更适合进阶模式，要不要自己挑？」转进阶
   - 「我想要 X 感觉」（用户自己描述） → 当前阶段（M1）转进阶模式；M3 完成后调用混搭引擎

5. **中国风互斥拦截**：用户场景为「读书笔记」且推到 Hara 时，**先追问偏哪一种东方**（见 [routing.md 中国风互斥提示](routing.md#中国风互斥提示)）

6. **数据覆盖规则**：原文含 > 30% 数据/表格/图表 → **强制覆盖推 Tufte**（不论用户场景选什么），并说明"你这份内容有大量数据，Data-Ink 风格最不浪费信息"

#### 🎨 Q1·进阶模式（M2 上线 · 浏览器预览页）

调用 `scripts/style_preview.py` 起本地服务，浏览器自动打开 `templates/preview.html` 让用户在网页里看 14 大师卡片 + 三张代表截图。

**调用命令**（Claude 执行 Bash）：
```bash
python scripts/style_preview.py \
    --title "<Phase 2.0 用户确认的标题>" \
    --words <source.md 总字数> \
    --scene <Phase 2 检测到的场景 · 可省略> \
    --output <work_dir>/style_config.json \
    --timeout 600
```

**等待 server 退出。判定优先看 `style_config.json` 是否已生成 —— 不要只信退出码**（脚本可能写完 JSON 后因终端编码等原因非 0 退出）：

| 判定（按顺序） | 含义 | 下一步 |
|----------------|------|--------|
| `style_config.json` 存在且能解析出 `master` 字段 | 用户已成功选定 | 读 `master_file` 字段继续 Q2 —— **无视退出码** |
| 文件不存在 · exit code 1 | 超时 / 用户取消 | **fallback 回对话模式**（列预设文字选） |
| 文件不存在 · exit code 2 | 环境错误（找不到 html/python 等）| 报错给用户，建议升级 / 回退快速模式 |

**收到的 style_config.json 结构：**
```json
{
  "master": "rams",
  "master_file": "aesthetics/rams.md",
  "display_name": "克制专业",
  "scene": "business",
  "china_mutex": false,
  "mutex_option": null,
  "timestamp": "2026-05-21T10:23:00Z"
}
```

**特殊处理：**
- 收到 `china_mutex: true` → 用户已在预览页内确认了东方派别（`mutex_option` 字段），不再追问
- 进阶模式用户也可以直接在对话里说「我要 Carson 风」「我要 Tufte 风」**绕过预览页**，直接加载对应 `aesthetics/<name>.md`
- 用户没浏览器环境 / 无桌面 GUI → 自动 fallback 回快速模式或文字预设选
- M3 混搭引擎上线后，`style_config.json` 会新增 `mix: {...}` 字段（见 [mix-engine.md](mix-engine.md)，M3 规划）

---

### Q2 / Q3（保持原逻辑，仅次序提示）

**第一批问完 Q0+Q1 后继续：** Q2 配色（默认 / 预设色盘 / 自定义 HEX）· Q3 大纲详略（见下表）

**Q3 详略 → 内容取舍映射**（用户选档位后按表砍/留，不允许"想加什么加什么"）：

| 档位 | 必保 | 可选 | 砍掉 |
|------|------|------|------|
| **12 张 · 极简** | 封面 + 终章 + 3-5 核心观点 + 2-3 金句 | — | 章节扉 / 案例 / 物料网格 / 阶段递进 |
| **18 张 · 主线** | + 章节扉（2-3）+ 1 个核心案例 | 局部图集 / 信条卡 | 物料网格 / 阶段递进 / 对话双栏 |
| **28 张 · 完整** | + 每章 2-3 页论据 + 2-3 案例 | 信条卡 / 对话双栏 / 阶段递进 | — |
| **40 张 · 详尽** | + 每个论据独立成页 + 物料网格 + 阶段递进 | 全图主视觉 / 全图章节扉 / 多图集 | — |

回到 Phase 2.1 按所选档位重新校准张数（差超过 ±3 张 → 调整 2.05 骨架卡的论点粒度，不要靠"硬塞水页"或"硬砍论据"凑数）。

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
- ❌ **快速模式下绝不暴露大师名字给用户**（Carson/Brody/Tufte 等术语对小白零信息量；只用一句话感受性描述）
- ❌ **小白用户禁止用 AskUserQuestion 直接列 15 个预设让他选** —— 这是回到盲选老路
- ✅ 永远遵守用户的 DIY 选择
- ✅ 中文为主时，西文当点缀（数字、术语）
- ✅ 模式 B/C/D 走相同的 Phase 1.5 / 2 / 3，**只有 Phase 1 来源分支不同**
- ✅ **Phase 3 Q0 模式分流是入口铁律 —— 没经过 Q0 就跳到 Q1，重写**

---

## 支持文件索引

| 文件 | 何时读 |
|---|---|
| [routing.md](routing.md) | Phase 4.0 找大师美学路由 |
| [aesthetics/](aesthetics/) | Phase 4.0 读 `<name>.md` 加载大师美学（14 位） |
| [mode-d-original.md](mode-d-original.md) | Phase 0 识别为 D 时 |
| [presets.md](presets.md) | Phase 3 选风格 / Phase 4 取色板 |
| [typography.md](typography.md) | Phase 4 字体栈 |
| [layouts.md](layouts.md) | Phase 2.1 字数预算表 + Phase 4 版式（17 种）+ 大纲模板 + HTML 骨架 |
| [deck.css](deck.css) | Phase 4 完整内联 |
| [deck.js](deck.js) | Phase 4 完整内联 |
| [animation-presets.md](animation-presets.md) | Phase 4 动画 |
| [scripts/extract.py](scripts/extract.py) | Phase 1.A 提取 |
| [scripts/style_preview.py](scripts/style_preview.py) | Phase 3 Q1 进阶模式 · 启动浏览器风格预览页 |
| [scripts/export_pptx.py](scripts/export_pptx.py) | Phase 5 导出 PPTX |
| [scripts/generate_demos.py](scripts/generate_demos.py) | **一次性脚本** · 用 3 份 demo 范文生成 14 大师 demo deck + 42 张代表截图 |
| [templates/preview.html](templates/preview.html) | Phase 3 Q1 进阶模式 · 浏览器渲染的风格预览页 |
| [templates/preview-data.json](templates/preview-data.json) | preview.html 数据源 · 14 大师元数据 + 场景路由 + 中国风互斥规则 |
| [demo-decks/](demo-decks/) | 14 大师预生成的 demo deck（每个目录含 cover/chapter/body 三张代表截图 + full.html）|
| [examples/](examples/) | 参考产出 |
