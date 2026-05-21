# 风格预设 · 15 套（中文长文场景专设）

> 每套预设包含：vibe / 字体栈 / 默认色板 / 备选色盘 / 招牌装饰元素。
> 字体均来自 Google Fonts / Fontshare / jsDelivr CDN，免费可商用。
> 配色用 CSS 变量定义，便于 HEX 自定义注入。
>
> **CSS 变量约定（与 deck.css 配套）：**
> - `--stage-void`：舞台外框（视口背景）
> - `--stage-bg`：舞台主背景
> - `--stage-paper`：主文字（最亮）
> - `--stage-ink`：常规文字
> - `--stage-faint`：弱化文字
> - `--accent-key`：核心强调色
> - `--accent-soft`：次强调色
> - `--accent-warn`：警示色 / 第三色
> - `--type-display-cn`：中文显示字体
> - `--type-body`：正文字体
> - `--type-latin`：西文字体

---

## 一、夜色系（4 套）

### 01 · 金箔残夜 (Gilded Dusk)

**Vibe：** 高端访谈 · 博物馆夜场 · 思想性

**字体：**
```css
--type-display-cn: 'Noto Serif SC', 'Source Han Serif SC', serif;
--type-body: 'IBM Plex Sans', 'Noto Sans SC', sans-serif;
--type-latin: 'Cormorant Garamond', serif;
```

**默认色板：**
```css
--stage-void: #050505;
--stage-bg: #0f0c08;
--stage-paper: #f1ede5;
--stage-ink: #e8e0d2;
--stage-faint: #968d7a;
--accent-key: #d4a574;        /* 金箔 */
--accent-soft: #b89165;
--accent-warn: #e8b4b8;
```

**备选色盘：**
- 暑金（默认）
- 古铜：`#cd853f` + `#a0826d` + `#f5deb3`
- 翡翠：`#5fb89c` + `#a8d4c5` + `#f7e2c8`

**招牌装饰：** 右上单根金线 + 角落柔和金光晕 + 副语使用 Cormorant Garamond 斜体

---

### 02 · 电流 (Voltline)

**Vibe：** AI 时代 · 极客 · 黑马气质

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'JetBrains Mono', monospace;
```

**默认色板：**
```css
--stage-void: #000;
--stage-bg: #0a0d0a;
--stage-paper: #f5f1e8;
--stage-ink: #e0dccf;
--stage-faint: #7a7770;
--accent-key: #b5ff3a;        /* 电流绿 */
--accent-soft: #ffd23f;
--accent-warn: #ff6b3d;
```

**备选色盘：**
- 电流绿（默认）
- 电流蓝：`#3affff` + `#ffaa00` + `#ff3a8c`
- 电流紫：`#c5a3ff` + `#ffd23f` + `#3affff`

**招牌装饰：** 极细网格背景（径向遮罩，中心可见边缘淡出）+ 等宽数字角标 + 圆点带光晕

---

### 03 · 夜潮 (Tidal Night)

**Vibe：** 学术 · 思想性 · 深度长文

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Crimson Pro', serif;
```

**默认色板：**
```css
--stage-void: #02041a;
--stage-bg: #0a0f24;
--stage-paper: #f0eee6;
--stage-ink: #d8d3c4;
--stage-faint: #5a6680;
--accent-key: #f5d76e;        /* 月光黄 */
--accent-soft: #a6c5e8;       /* 银蓝 */
--accent-warn: #c89bf0;       /* 紫罗兰 */
```

**备选色盘：**
- 月夜（默认）
- 极光：`#7df0c1` + `#a6e3ff` + `#c89bf0`
- 银河：`#f5f5f5` + `#a6a6c5` + `#ffd23f`

**招牌装饰：** 满天星 dot pattern（CSS background-image）+ 一道弧形渐变 + 月光黄强调

---

### 04 · 霓虹脉冲 (Pulse Neon)

**Vibe：** 未来 · 赛博朋克 · 技术感

**字体：**
```css
--type-display-cn: 'Noto Sans SC', sans-serif;  /* 用粗黑体 */
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Orbitron', sans-serif;
```

**默认色板：**
```css
--stage-void: #03061a;
--stage-bg: #0a0f1c;
--stage-paper: #ffffff;
--stage-ink: #d8e0e8;
--stage-faint: #5a6680;
--accent-key: #00ffcc;        /* 青光 */
--accent-soft: #ff00aa;       /* 品红 */
--accent-warn: #ffd23f;
```

**备选色盘：**
- 青粉（默认）
- 黄紫：`#fff200` + `#9d4dff` + `#00d9ff`
- 红蓝：`#ff3838` + `#0094ff` + `#00ff88`

**招牌装饰：** 扫描线 / 边角发光 box-shadow / glitch 文字效果 / Orbitron 标题

---

### 05 · 磷火显像 (Phosphor Tube)

**Vibe：** Hacker · CRT 复古 · 开发者

**字体：** **全等宽**
```css
--type-display-cn: 'Noto Sans Mono CJK SC', 'Noto Sans SC', monospace;
--type-body: 'JetBrains Mono', 'Noto Sans Mono CJK SC', monospace;
--type-latin: 'JetBrains Mono', monospace;
```

**默认色板：**
```css
--stage-void: #050805;
--stage-bg: #0d1117;
--stage-paper: #c9d1d9;
--stage-ink: #b8c0c8;
--stage-faint: #6e7681;
--accent-key: #39d353;        /* 磷绿 */
--accent-soft: #ffd700;
--accent-warn: #ff7b72;
```

**备选色盘：**
- 磷绿（默认）
- 琥珀 CRT：`#ffb000` + `#ff7800` + `#ffd700`
- Solarized：`#268bd2` + `#b58900` + `#d33682`

**招牌装饰：** 扫描线（CSS repeating gradient）+ 闪烁光标 + `>` 前缀

---

## 二、中国风（5 套，扩大）

### 06 · 宣纸古卷 (Rice Scroll)

**Vibe：** 古典 · 文人 · 温润

**字体：**
```css
--type-display-cn: 'LXGW WenKai', 'Noto Serif SC', serif;
--type-body: 'LXGW WenKai', 'Noto Sans SC', sans-serif;
--type-latin: 'Cormorant Garamond', serif;
```

**字体加载：**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/style.css">
```

**默认色板：**
```css
--stage-void: #d8c8a5;
--stage-bg: #ede2cc;          /* 宣黄 */
--stage-paper: #2a1810;
--stage-ink: #3a2a1a;
--stage-faint: #6e5a3e;
--accent-key: #b32d2d;        /* 朱砂 */
--accent-soft: #8b6914;       /* 古铜 */
--accent-warn: #2a4d3a;       /* 松绿 */
```

**备选色盘：**
- 朱砂（默认）
- 青绿：`#2a4d3a` + `#8b6914` + `#ede2cc`
- 黛色：`#2a3845` + `#b32d2d` + `#ede2cc`

**招牌装饰：** 纸张纤维肌理（CSS turbulence filter 或 noise）+ 朱砂方印 + 卷轴边框

---

### 07 · 水墨留白 (Ink Wash)

**Vibe：** 极简 · 留白 · 禅意

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
```

**默认色板：**
```css
--stage-void: #e0ddd5;
--stage-bg: #f5f3ee;
--stage-paper: #1a1a1a;
--stage-ink: #2a2a2a;
--stage-faint: #88847a;
--accent-key: #1a1a1a;        /* 浓墨即强调 */
--accent-soft: #6a655a;       /* 灰墨 */
--accent-warn: #b32d2d;       /* 朱印 */
```

**备选色盘：**
- 纯墨（默认）
- 朱印：`#b32d2d` + `#1a1a1a` + `#6a655a`
- 雪夜（深色版）：`#1a1a1a` 底 + `#f5f3ee` 字 + `#888`

**招牌装饰：** 大量留白 / 单一墨色横扫 / 一颗朱印作为视觉焦点

---

### 08 · 故宫赤红 (Crimson Court)

**Vibe：** 庄重 · 宫殿 · 传统 · 鲜明

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Cormorant', serif;
```

**默认色板：**
```css
--stage-void: #4d0a0a;
--stage-bg: #8b1e1e;           /* 朱红 */
--stage-paper: #f5e6c8;        /* 米黄 */
--stage-ink: #f0d8a8;
--stage-faint: #d4b8a0;
--accent-key: #d4a017;         /* 金 */
--accent-soft: #f5e6c8;
--accent-warn: #2a4d3a;        /* 翠玉 */
```

**备选色盘：**
- 朱金（默认）
- 墨金：`#1a1a1a` 底 + 金 + 米黄
- 青绿：`#2a4d3a` 底 + 金 + 米黄

**招牌装饰：** 屋顶飞檐 SVG + 金线边框 + 方形朱印 + 篆体角注

---

### 09 · 青瓷釉色 (Celadon Glaze)

**Vibe：** 雅致 · 釉光 · 宋瓷

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Cormorant Garamond', serif;
```

**默认色板：**
```css
--stage-void: #c5d6c2;
--stage-bg: #d8e3d0;            /* 青瓷青 */
--stage-paper: #1a2a25;
--stage-ink: #2c3e36;
--stage-faint: #6a7d70;
--accent-key: #8b2d2d;          /* 古玺红 */
--accent-soft: #5a7d5a;
--accent-warn: #c9b896;
```

**备选色盘：**
- 默认青瓷
- 影青：`#bfd4cf` + `#3a4a45` + `#a08560`
- 龙泉绿：`#4a7d6a` + `#1a2a25` + `#d4a574`

**招牌装饰：** 釉色渐变（瓷光感）+ 极细金线分隔 + 一颗古玺印

---

### 10 · 碑刻金石 (Stele Cut)

**Vibe：** 金石学 · 古意 · 沉郁

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Cormorant', serif;
```

**默认色板：**
```css
--stage-void: #2a2620;
--stage-bg: #3a3530;             /* 暖灰石 */
--stage-paper: #e8dcc4;
--stage-ink: #d4c8b0;
--stage-faint: #7a7060;
--accent-key: #c4a444;            /* 鎏金 */
--accent-soft: #8b6914;
--accent-warn: #a83a3a;
```

**备选色盘：**
- 默认鎏金
- 拓片：`#1a1a1a` 底 + `#e8dcc4` 字（黑底白字拓本风）
- 唐三彩：`#a83a3a` + `#c4a444` + `#5a7d6a`

**招牌装饰：** 石材纹理（CSS noise）+ 边缘风化效果（box-shadow inset）+ 篆刻方块

---

## 三、纸本系（3 套）

### 11 · 档案本 (Archive Folio)

**Vibe：** 编辑感 · 整理质感 · 民国档案

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Bodoni Moda', serif;
```

**默认色板：**
```css
--stage-void: #1a1a1a;
--stage-bg: #f8f6f1;            /* 米黄纸 */
--stage-paper: #1a1a1a;
--stage-ink: #2a2a2a;
--stage-faint: #6a665e;
--accent-key: #98d4bb;          /* 薄荷 tab */
--accent-soft: #f4b8c5;
--accent-warn: #ffe6a7;
```

**备选色盘：**
- 春色五 tab（默认 · 薄荷 / 粉 / 奶油 / 薰衣草 / 天空）
- 秋色：赭石 / 砖红 / 苔藓 / 黄褐 / 黛绿
- 冬雪：低饱和五色，蓝灰主调

**招牌装饰：** 纸张容器 + 右侧多彩 tab（竖向文字）+ 左侧装订孔（CSS dots）

---

### 12 · 单刊 (Monomag)

**Vibe：** 独立出版 · 杂志风 · 文人态度

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Fraunces', serif;
```

**默认色板：**
```css
--stage-void: #1a1a1a;
--stage-bg: #f5f3ee;
--stage-paper: #1a1a1a;
--stage-ink: #2a2a2a;
--stage-faint: #6a655a;
--accent-key: #c2410c;           /* 暑粉橙 */
--accent-soft: #92400e;
--accent-warn: #2d5f3f;
```

**备选色盘：**
- 暑粉橙（默认）
- 朱红：`#c41e3a` + `#1a1a1a` + `#f5f3ee`
- 墨绿：`#2d5f3f` + `#d4a574` + `#1a1a1a`

**招牌装饰：** 抽象几何（圆轮廓 + 线段 + 点）+ 厚边角块 + 大字号开篇

---

### 13 · 读本 (Reader's Edition)

**Vibe：** 文学 · 思想性 · 严肃可读

**字体：**
```css
--type-display-cn: 'Noto Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Cormorant Garamond', 'Source Serif 4', serif;
```

**默认色板：**
```css
--stage-void: #e8e4d8;
--stage-bg: #faf9f7;
--stage-paper: #1a1a1a;
--stage-ink: #2a2a2a;
--stage-faint: #6a655a;
--accent-key: #c41e3a;           /* 朱红 */
--accent-soft: #a8927a;
--accent-warn: #1a1a1a;
```

**备选色盘：**
- 朱红（默认）
- 全墨（无彩）：`#1a1a1a` + `#a8927a` + `#6a655a`
- 国家地理：`#ffd900` + `#1a1a1a` + `#c41e3a`

**招牌装饰：** 首字下沉 / 引文加粗 / 水平细线分隔 / 报头风标题

---

## 四、实验与几何（3 套，含 1 套大师蒸馏专属）

### NEW · 解构 (Deconstruction) ⭐ 由 david-carson-skill 驱动

**Vibe：** Anti-grid · 解构主义 · Ray Gun 风 · 视觉冲击

**美学大师**：David Carson —— **生成时必须读取 `david-carson-skill/SKILL.md`** 完整应用其视觉操作系统。

**字体：**
```css
--type-display-cn: 'Noto Serif SC', 'Source Han Serif SC', serif;
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'League Gothic', 'Bebas Neue', 'Anton', sans-serif;
--type-mono: 'IBM Plex Mono', monospace;
```

**字体加载：**
```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700;900&family=Noto+Sans+SC:wght@300;400;700&family=League+Gothic&family=Bebas+Neue&family=Anton&family=IBM+Plex+Mono:wght@400;700&display=swap" rel="stylesheet">
```

**默认色板（黑白主导 + 三色之一强调）：**
```css
:root {
    --stage-void: #000000;
    --stage-bg: #ffffff;             /* 白底版本 */
    --stage-paper: #000000;
    --stage-ink: #1a1a1a;
    --stage-faint: #8a8a8a;
    --accent-key: #ff3a1f;           /* 番茄红（强调色四选一） */
    --accent-soft: #000000;
    --accent-warn: #f5ff00;
}
```

**备选色盘（4 个，每个都是"黑白 + 1 高饱和"）：**
- 番茄红（默认）：`#ff3a1f`
- 电光黄：`#f5ff00`
- 洋红：`#ff00aa`
- 电光蓝：`#00aaff`
- **暗黑版本**：`--stage-bg: #000` + `--stage-paper: #fff`，强调色不变

**Carson 风核心生成规则**（必须强制执行）：
1. **字号比例 ≥ 20:1** —— 标题 `clamp(8rem, 24vw, 18rem)` + 正文 `0.55rem`
2. **每页至少一处越界 ≥ 30%** —— 标题字母被边裁切、单词消失在画外
3. **禁止居中对齐** —— 所有元素重心偏向一侧
4. **所有元素错位旋转 2-15°**（中文方块字段落降到 2-5°）
5. **图文重叠 ≥ 40%** —— 满版照片 + 半透明大标题压脸
6. **留 1-2 处空洞** —— 该有标点 / 装饰的位置直接留空
7. **极端两极留白** —— 要么塞满，要么空旷

**中文场景特别降级**（必须遵守）：
- 错位旋转：中文段落 2-5°（不是 3-15°）
- 越界 / 切边：**只切英文 / 数字部分**，不切中文方块字主体
- 字体混排：中文用单一家族（思源宋或思源黑），西文用 League Gothic 等失真 sans 作为视觉冲击
- 重叠 / 空洞 / 极端字号 —— 全保留

**何时不选这套：** 数据可视化 / 严肃报告 / 法务医疗 / 公文公教 / 多语言国际化场景。

**招牌装饰：** 满版黑白照片 + 半透明大标题压主体 + 一字越界 + 一处空洞 + 一段失真 sans 文字斜插

---

### 14 · 网格主义 (Gridism)

### 14 · 网格主义 (Gridism)

**Vibe：** 包豪斯 · 瑞士平面 · 克制

**字体：**
```css
--type-display-cn: 'Noto Sans SC', sans-serif;   /* 黑体当标题 */
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Archivo', 'Nunito', sans-serif;
```

**默认色板：**
```css
--stage-void: #e8e8e8;
--stage-bg: #ffffff;
--stage-paper: #000000;
--stage-ink: #1a1a1a;
--stage-faint: #888888;
--accent-key: #ff3300;            /* 朱红 */
--accent-soft: #000000;
--accent-warn: #ffd900;
```

**备选色盘：**
- 朱红（默认）
- 海军蓝：`#003366` + `#ffd900` + `#000000`
- 森林绿：`#0d6e3a` + `#ff3300` + `#000000`

**招牌装饰：** 可见网格线 / 非对称构图 / 厚边角块 / 大量留白

---

### 15 · 黑潮 (Onyx Wave)

**Vibe：** 营销 · 社交媒体 · 张扬冲击力

**字体：**
```css
--type-display-cn: 'Smiley Sans', 'Noto Sans SC', sans-serif;  /* 得意黑 */
--type-body: 'Noto Sans SC', sans-serif;
--type-latin: 'Anton', 'Archivo Black', sans-serif;
```

**字体加载：**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/smiley-sans@2.0.1/index.css">
```

**默认色板：**
```css
--stage-void: #1a1a00;
--stage-bg: #ffd900;            /* 大黄 */
--stage-paper: #000000;
--stage-ink: #1a1a1a;
--stage-faint: #5a5a3a;
--accent-key: #ff0040;           /* 大红 */
--accent-soft: #000000;
--accent-warn: #00d9ff;
```

**备选色盘：**
- 黄红（默认）
- 黑荧光：`#000` 底 + `#b5ff3a` + `#ff00aa`
- 粉绿：`#ffafd4` + `#0d6e3a` + `#000000`

**招牌装饰：** 超大字号 / 颜色块满铺 / 标签贴纸 / 高对比

---

## 配色 DIY 注入逻辑

用户在 Phase 3 选「输入主色 HEX」时：

```javascript
// 用户提供 hex
const userKey = '#xxxxxx';
// 自动派生
const softer  = lighten(userKey, 0.15);  // 主色调亮
const warmer  = rotateHue(userKey, 35);  // 色相旋转 +35°
// 注入：
:root {
    --accent-key: ${userKey};
    --accent-soft: ${softer};
    --accent-warn: ${warmer};
}
```

`--stage-bg` / `--stage-paper` 保持所选风格的原值。

---

## 禁止清单（绝不使用）

- **字体：** Inter（单独用）/ Arial / Roboto / 系统字体作显示标题
- **配色：** `#6366f1`（generic indigo）/ 白底紫渐变 / 黑底粉紫
- **装饰：** 真人插画 / 廉价 emoji / 阴影泛用 / 无意义的玻璃拟态

---

## 风格快速对照表

| # | 风格 | 主基调 | 适配 |
|---|------|--------|------|
| 01 | 金箔残夜 (Gilded Dusk) | 黑+暖金 | 思想 / 访谈 / 高端 |
| 02 | 电流 (Voltline) | 黑+电流绿 | AI / 创业 / 演讲 |
| 03 | 夜潮 (Tidal Night) | 蓝+月黄 | 学术 / 深度 |
| 04 | 霓虹脉冲 (Pulse Neon) | 蓝+青粉 | 科技 / 未来 |
| 05 | 磷火显像 (Phosphor Tube) | 黑+磷绿 | 开发者 / Hacker |
| 06 | 宣纸古卷 (Rice Scroll) | 宣黄+朱砂 | 国学 / 古典 |
| 07 | 水墨留白 (Ink Wash) | 白+墨 | 禅意 / 极简 |
| 08 | 故宫赤红 (Crimson Court) | 朱红+金 | 传统 / 庄重 |
| 09 | 青瓷釉色 (Celadon Glaze) | 青瓷+古红 | 雅致 / 宋韵 |
| 10 | 碑刻金石 (Stele Cut) | 灰石+鎏金 | 金石 / 沉郁 |
| 11 | 档案本 (Archive Folio) | 纸黄+多 tab | 笔记 / 学习 |
| 12 | 单刊 (Monomag) | 米+暑粉橙 | 杂志 / 文人 |
| 13 | 读本 (Reader's Edition) | 暖白+朱红 | 文学 / 严肃 |
| 14 | 网格主义 (Gridism) | 白+朱红 | 几何 / 设计 |
| 15 | 黑潮 (Onyx Wave) | 大黄+大红 | 营销 / 社媒 |
