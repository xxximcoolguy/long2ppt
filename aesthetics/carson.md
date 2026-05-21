---
name: david-carson-skill
description: |
  David Carson 视觉操作系统 —— 解构主义平面设计先锋的"视觉认知 DNA"。
  五层蒸馏：① 视觉哲学（Typography is never neutral · Form follows feeling）② 版式手法（越界 / 错位 / 重叠 / 撕裂 / 反构图）③ 颜色字体启发式（黑白先行 · 最多三色 · Template Gothic 系）④ 视觉禁忌（拒绝 Swiss 网格 / Helvetica 中性 / 居中对齐 / 完美对齐线）⑤ 局限（数据可视化、法务医疗、企业模板不适用）。

  触发场景：
  - 用户说「Carson 风」「卡森式」「Ray Gun 风格」「解构主义版式」「破规则设计」
  - 用户说「让设计更冲」「打破网格」「文字越界」「不要那么乖」
  - 用户说「用 Carson 视角看这个设计」/「Carson 会怎么改这个 PPT」
  - 长文本→PPT 时用户选择"解构"风格预设
  - longtext-to-slides 等设计类 skill 调用本 skill 作为美学指导
---

# David Carson · 视觉操作系统

> 「**Don't mistake legibility for communication.** Just because something is legible doesn't mean it communicates, and more importantly, doesn't mean it communicates the right thing.」
> —— David Carson, TED 2003

---

## 蒸馏对象

| 项 | 内容 |
|---|---|
| **人物** | David Carson (b. 1955) |
| **领域** | 平面设计、版式设计、杂志设计 |
| **代表作** | Ray Gun, Beach Culture, Transworld Skateboarding, *The End of Print*, Nine Inch Nails 视觉 |
| **流派** | Anti-grid / Deconstruction / Grunge Typography |
| **核心冲突** | 对 Swiss / 现代主义网格派（Vignelli, Tschichold, Helvetica）的反叛 |

---

## ① 视觉哲学 · Mental Models（怎么看）

### MM-1 · Typography is never neutral
排版从来不是中性载体。**在读者读完文字前，字体的形态 / 间距 / 错位已经把情绪先传达了。**
→ 推论：选择字体 = 选择情绪。安全的字体 = 没情绪 = 没人读。

### MM-2 · Don't mistake legibility for communication
能读 ≠ 在传达 ≠ 传达对了。
- "能读"是低层级目标
- "情绪 / 态度 / 议题传达"是高层级目标
- 当两者冲突时，**牺牲 legibility 换取 communication**

### MM-3 · Form follows feeling
不是 form follows function。Carson 动手前做的是**情绪解码**：
- 读完文章 / 听完音乐
- 决定它"把我带到哪里"
- 让版面长成这个情绪的样子

→ 推论：**没有 Carson 模板**。每页都是 one-off。**禁止复制粘贴他的版式**。

### MM-4 · Computers make you lazy
设计软件的"对齐辅助线" / "网格吸附"是认知陷阱。
- "Snap to guides" 一开就被工具规训
- 默认设置 = 默认审美 = 平庸

→ 推论：动手前先关掉所有辅助线，强迫眼睛判断。

### MM-5 · Of-its-time，not timeless
Vignelli 追求 timeless universal grid。Carson 反对："Design needs to be, and should be, of its time."
- 他举例：Vignelli 死后几个月，他做的 American Airlines 标识就被换了
- 推论：拒绝"永恒经典" tropes（衬线 + 居中 + 大量留白 = 高级感）；拥抱当下文化的具体性

---

## ② 版式操作系统 · Heuristics（怎么排）

> 这是这份蒸馏最可操作的部分。每条都给出**可写进 CSS** 的方式。

### H-1 · 文字越出边界（Overflow / Bleed）
**规则**：每张 frame 至少一处元素越出画面 **≥ 30%**。
- 字母级越界：单字母左 / 右半边被画框切掉 30-50%
- 单词级越界：单词的尾部消失在画外
- 正文级越界：body text 撞进 gutter / 切掉底部一行

**CSS 配方：**
```css
.bleed-left {
    transform: translateX(-35%);
}
/* 父容器需要 overflow: hidden */
.frame { overflow: hidden; }
```

### H-2 · 错位 / 反对齐（Misalignment）
**规则**：**禁止**任何统一对齐线。每个文字块独立摆放。
- 列与列**不齐顶不齐底**
- 段落轻微旋转 **3-15°**（不是 45/90° 大旋转 —— 那是造型而非破坏）
- 文字块的"重心"应有 1-2 处明显偏移

**CSS 配方：**
```css
.askew-1 { transform: rotate(-3deg); }
.askew-2 { transform: rotate(5deg); }
.askew-3 { transform: rotate(-8deg) translateY(-12px); }
```

### H-3 · 重叠图层（Overlap / Layering）
**规则**：图文重叠率 **≥ 40%**（不是 10% 那种保守叠加）。
- 满版照片做底 + 半透明大号标题压在主体上（**脸 / 中心物体**）
- 文字叠文字：两段不同字体 / 字号的文字 60-80% 重叠
- 极端做法：dark text on dark background（迫使观众凑近）

**CSS 配方：**
```css
.layer-bg { position: absolute; inset: 0; z-index: 1; }  /* 照片 */
.layer-title {
    position: absolute; top: 30%; left: 0; right: 0;
    z-index: 2;
    color: rgba(255, 255, 255, 0.78);    /* 半透明 */
    mix-blend-mode: difference;           /* 或 multiply */
}
.layer-body {
    position: absolute;
    z-index: 3;
    /* 与 .layer-title 重叠 60% */
}
```

### H-4 · 字体撕裂 / 切割 / 损毁
**规则**：故意留 1-2 处"瑕疵"。
- **Negative leading**：行距小于字体高度，行间互相侵入
- 字母被矩形色块 / 照片 / 其他字母遮盖一部分
- 用"半坏"的字体：Template Gothic 风格 —— 印刷光晕、磨损弧线
- **空洞**：本该有标点 / 装饰的位置直接留空，不补救

**CSS 配方：**
```css
.tight-leading { line-height: 0.78; }  /* 负行距感 */
.title-cut {
    position: relative;
}
.title-cut::after {
    content: '';
    position: absolute;
    width: 60%; height: 30%;
    background: var(--bg);  /* 用背景色块切掉一部分字 */
    top: 35%; left: 22%;
    mix-blend-mode: normal;
}
```

### H-5 · 反构图（不是乱来，是张力）
**核心规则：内容驱动构图。**
- 情绪激烈 → 版面密集冲突
- 空灵安静 → 大面积留白 + 单点焦点
- **禁止"安全中等密度"**

中间状态最少 —— **要么塞满，要么空旷**。

### H-6 · 字号极端对比
**规则**：标题 : 正文 **≥ 20:1**（极端时 50:1）。

参照 Ray Gun 视觉判读：
- 标题占 frame 高度 **40-70%**（折算 240-400pt）
- 正文压到 **6-8pt**（小到刻意"为难读者"）

**CSS 配方：**
```css
.title-huge { font-size: clamp(8rem, 24vw, 18rem); line-height: 0.85; }
.body-tiny { font-size: 0.55rem; line-height: 1.1; max-width: 12ch; }
/* 字号差约 30 倍 */
```

### H-7 · 字体混排
**规则**：单页混 **2-3 种字体**（衬线 + sans + 实验字体）。
- 同一单词里混衬线与 sans（hybrid letterform）
- 数字 / 标点 / 字母可分别用不同字体
- 标题与正文字体差异**极大**（不是 Light + Regular 那种）

### H-8 · 留白偏侧
**规则**：留白**不居中**，偏向某一侧，形成视觉重量不平衡。
- 元素挤到左下角，右上 70% 空
- 单个小词放在巨大空白中央偏一侧
- **禁止上下左右等距留白**

---

## ③ 颜色与字体启发式 · DNA（怎么选）

### 配色规则

| 规则 | 内容 |
|------|------|
| **先黑白** | 起手只用 black & white，确定 form 后再加色 |
| **最多 3 色** | "Never exceeds more than three colors in a graphic design piece." — Carson 原话 |
| **去饱和摄影** | 照片常 desaturate 或纯黑白，让 type 成为色彩主体 |
| **强调色高饱和** | 番茄红 / 电光黄 / 洋红 / 电光蓝 取其一 |

**推荐 Carson 风色板（基于 Ray Gun 视觉判读，**非官方**）：**
```css
:root {
    --carson-void: #000000;
    --carson-paper: #ffffff;
    --carson-ink: #1a1a1a;
    /* 强调色四选一 */
    --carson-tomato: #ff3a1f;
    --carson-volt: #f5ff00;
    --carson-magenta: #ff00aa;
    --carson-electric: #00aaff;
}
```

### 字体规则

| 标志字体 | 设计师 | 何时用 |
|---------|-------|--------|
| **Template Gothic** | Barry Deck, 1990 (CalArts) | Ray Gun 时期标志字体。Web 替代：League Gothic / Bebas Neue + 失真滤镜 |
| **Zapf Dingbats** | Hermann Zapf | 作为反讽武器（Bryan Ferry 采访整篇用它） |
| **GarageFonts 系** | Fehsenfeld 等 | 实验字体 |
| **手绘 / 草字** | Carson 自己画 | 标题，用 SVG / 图片 |
| **失真 sans** | — | Web 替代：Anton + 文字阴影错位 / League Gothic |

**Carson 风 Web 字体栈推荐：**
```css
font-family: 'League Gothic', 'Bebas Neue', 'Anton', sans-serif;  /* 失真 sans 标题 */
font-family: 'IBM Plex Mono', 'Courier Prime', monospace;          /* 等宽点缀 */
font-family: 'Crimson Text', 'EB Garamond', serif;                 /* 古旧衬线 */
```

---

## ④ 视觉禁忌 · Anti-patterns（什么不做）

Carson 明确反对的清单：

1. ❌ **Swiss 完美网格对齐**（Vignelli 那套）
2. ❌ **Helvetica 中性 / 客观哲学**（他在 *Helvetica* 纪录片是反方代表）
3. ❌ **Invisible typography**（"看不见的字 = 看不见的文章"）
4. ❌ **跟模板 / 跟趋势**（独立杂志"长得都一样"）
5. ❌ **依赖电脑的"安全工具"**（snap to guides / 自动对齐）
6. ❌ **过度对齐的 corporate design**（"逃避立场"）
7. ❌ **居中对齐**（自动平庸的标志）
8. ❌ **统一行距 + 统一字号**（节奏感死亡）
9. ❌ **AI slop 配色**：紫渐变白底、indigo `#6366f1`、generic teal、所有"调色板生成器"产物

---

## ⑤ 局限性 · Honest Boundaries（什么场景不要用）

| 不适用场景 | 原因 |
|----------|------|
| **数据可视化 / 仪表盘** | 牺牲 legibility 与"快速准确读数"目标冲突 |
| **严肃报告 / 财报 / 法务 / 医疗** | 法规要求清晰、无歧义、可追溯 |
| **政府 / 公共服务** | WCAG 可达性强制（对比度、字号、对齐） |
| **企业 brand guideline** | Carson 风每页 one-off，无法系统化复用 |
| **国际化 / CJK 文字** | 错位 / 撕字 / 字体混排在中文 / 阿拉伯文中几乎不可行 —— **重要：中文版式套用时要降低强度** |
| **公文 / 教学 / 入门科普** | 受众优先目标是"读懂"，不是"被震撼" |

**对中文场景的特别说明：**
Carson 是为拉丁字母（特别是英文）发明这套语言的。中文字符是"方块"，本身已经很重，再叠加 Carson 风**容易塞死**。
- **字号极端对比**：可用（中文也吃 30:1 对比）
- **越界 / 切边**：可用，但只切英文 / 数字部分，**不切中文方块字主体**
- **错位旋转**：减弱到 2-5°（中文方块字 8° 已经歪到不舒服）
- **字体混排**：中文标题 + 中文正文用同一家族，西文用 Carson 风实验字体作为标志
- **空洞 / 撕裂**：保留，作为视觉钩子

---

## ⑥ 经典作品与可参考案例

| 作品 | 年份 | 视觉关键词 |
|------|------|----------|
| Transworld Skateboarding | 1984-88 | Dirty type · 业余摄影 · 早期实验 |
| Beach Culture | 1989-91 | 越出边界 · 撕裂字 · 150+ 设计奖 |
| Ray Gun | 1992-95 | 巅峰期 · Bryan Ferry/Zapf Dingbats · Morrissey 跨页 |
| The End of Print（书）| 1995 | 无页码 · 字号剧变 · 文字流入装订缝 |
| Nine Inch Nails - The Fragile | 1999 | 海洋意象 · 细胞分裂 · 水波纹畸变 |
| Nike / Pepsi / Microsoft / Sony 广告 | 90s-00s | 商业化期，克制保留越界感 |

---

## 七个最少必要元素 · 让 Web 渲染出"卡森味"

```
1. 一张满版黑白照片做底
2. 一个超大标题（视口高度 60%+）压在主体上，半透明 60-80%
3. 标题有一个字母被边缘裁切，或被另一个元素遮挡
4. 旁边一段超小正文（10-12px），斜 5-8°，与图叠 40%
5. 三色：黑 + 白 + 一个高饱和强调色
6. Template Gothic 或 League Gothic 等失真 sans
7. 没有任何元素居中对齐，重心偏向画面一侧
（可选 8）一两个"空洞"—— 本该有标点 / 装饰的位置留空
```

---

## 调用方式（被其他 skill 嵌入时）

当 `longtext-to-slides` 等 skill 选择 Carson 风格时，**完整读取本 SKILL.md**，按以下顺序应用：

1. 先用 **MM-3（Form follows feeling）** —— 读懂内容情绪
2. 用 **H-5（反构图）** —— 决定塞满 or 空旷
3. 用 **H-6（字号极端对比）** —— 标题:正文 ≥ 20:1
4. 用 **H-1 + H-2**（越界 + 错位）—— 至少一处越 30%、所有元素错位
5. 用 **H-3 + H-4**（重叠 + 撕裂）—— 至少 1 处图文重叠 40%、留 1-2 处"空洞"
6. 用 **③ 配色规则** —— 黑白 + 1 个高饱和强调色
7. 用 **⑤ 中文场景特别说明** —— 中文场景要降强度
8. 检查 ④ 禁忌清单 —— **凡是符合一条禁忌的都重做**

---

## 诚实声明

- ✅ **可信高**：视觉哲学（MM-1 到 MM-5）来自 Carson 原话 / TED / MasterClass / 多次采访
- ✅ **可信高**：版式手法 H-1 到 H-8 来自 Ray Gun 实物 + Joe Clark 技术分析
- ⚠️ **启发式而非硬规则**：字号比例 20:1 / 50:1 是基于 Ray Gun 视觉判读的工程化推断，**Carson 本人未公布精确规则**
- ⚠️ **启发式**：3-15° 旋转角度同上
- ❌ **不可信编造**：精确 hex 色板 —— 我给出的 Carson 风色板是从图片观察推断，**Carson 没有官方调色板**
- 🚫 **绝不模仿**：Carson 的"个人直觉" / "情绪解码"是不可蒸馏的部分。本 skill 只能给规则，不能给灵感

---

## 参考资料（References）

完整调研报告与原始引用见：
- [references/research-source.md](references/research-source.md) - 一手 + 二手调研报告全文
- [references/visual-recipes.md](references/visual-recipes.md) - HTML/CSS 配方书（待后续补充）

**主要一手 / 权威来源：**
- davidcarsondesign.com - Carson 个人网站
- davidcarsonstudio.com - Carson 工作室
- TED Talk 2003 "Design and Discovery"
- *Helvetica* (2007) 纪录片 - Carson 是反方代表
- MasterClass "Send a Message With Typography"
- *The End of Print* (1995) - Carson 与 Lewis Blackwell 合著
- AIGA Eye on Design 多篇深度采访
- Joe Clark 技术分析（joeclark.org/design/davidcarson.html）

---

## 蒸馏元信息

- **蒸馏框架**：仿 nuwa-skill 五层结构（Mental Models / Heuristics / DNA / Anti-patterns / Boundaries）
- **蒸馏日期**：2026-05-21
- **调研深度**：单 Agent 深度调研（vs nuwa 6 Agent 并行）—— 设计师信息相对集中，单 Agent 足够
- **下次更新**：当 Carson 公开发布新作品 / 新访谈时
