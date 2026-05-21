# 中文字体栈 & 字号尺度

> 中文长文 PPT 与英文有本质差异：方块字密度高、笔画复杂，**行高需要 1.6-1.85**（西文常用 1.4-1.5），字号下限也更高（小于 12px 中文几乎无法阅读）。
> 这份文档定义所有可用字体栈与字号档位，生成时按需选择。

---

## 一、中文字体栈

### 衬线（宋体类）

| 字体 | Google Fonts URL | 适用 |
|------|------------------|------|
| **Noto Serif SC** | `family=Noto+Serif+SC:wght@400;500;700;900` | 默认 · 标准宋体，最广泛 |
| **Source Han Serif SC** | 同上（思源宋体即 Noto Serif SC）| 同上 |
| **LXGW WenKai 霞鹜文楷** | CDN: `https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/style.css` | 古典 · 国学 · 文人调 |
| **Smiley Sans 得意黑** | CDN: `https://cdn.jsdelivr.net/npm/smiley-sans@2.0.1/index.css` | 张扬 · 营销 · 海报感 |

### 无衬线（黑体类）

| 字体 | Google Fonts URL | 适用 |
|------|------------------|------|
| **Noto Sans SC** | `family=Noto+Sans+SC:wght@300;400;500;700;900` | 默认 · 现代清晰 |
| **HarmonyOS Sans SC** | 通常本地系统字体，fallback 用 | 工业 · 简洁 · 苹果味 |
| **Source Han Sans SC** | 同 Noto Sans SC（即思源黑体）| 同上 |

### 西文（中英混排时的西文部分）

| 字体 | 用途 | Google Fonts |
|------|------|--------------|
| `Cormorant` / `Cormorant Garamond` | 高端衬线 · 斜体角注 | ✓ |
| `Fraunces` | 杂志风衬线 | ✓ |
| `Bodoni Moda` | 编辑感衬线 | ✓ |
| `Source Serif 4` | 文学衬线 | ✓ |
| `Inter` | 现代无衬线（仅西文）| ✓ |
| `Plus Jakarta Sans` | 友好无衬线 | ✓ |
| `Outfit` | 圆润无衬线 | ✓ |
| `Manrope` | 几何无衬线 | ✓ |
| `Archivo Black` / `Archivo` | 厚重显示 | ✓ |
| `Anton` | 高瘦显示 | ✓ |
| `JetBrains Mono` | 等宽 / 代码 / 数字 | ✓ |
| `Orbitron` | 赛博 / 未来 | ✓ |
| `Space Grotesk` / `Space Mono` | 几何 / 极客 | ✓ |
| `Syne` | 创意 / 张扬 | ✓ |

---

## 二、推荐字体组合（按风格）

| 风格 | 中文标题 | 中文正文 | 西文 |
|------|----------|----------|------|
| 暗夜电光 | Noto Serif SC 900 | Noto Sans SC 300/400 | JetBrains Mono |
| 黑金专访 | Noto Serif SC 700 | Noto Sans SC 300 | Cormorant + Cormorant Garamond Italic |
| 深空墨蓝 | Noto Serif SC 700 | Noto Sans SC 400 | Crimson Pro + Inter |
| 霓虹赛博 | Noto Sans SC 900 (黑体当标题) | Noto Sans SC 400 | Orbitron + Space Grotesk |
| 终端绿屏 | Noto Sans SC 700 | Noto Sans SC 400 | JetBrains Mono（全等宽）|
| 米黄手账 | Noto Serif SC 700 | Noto Sans SC 400 | Bodoni Moda + DM Sans |
| 暖米杂志 | Noto Serif SC 900 | Noto Sans SC 400 | Fraunces + Work Sans |
| 瑞士极简 | Noto Sans SC 900 | Noto Sans SC 300 | Archivo + Nunito |
| 报刊编辑 | Noto Serif SC 700 | Noto Sans SC 400 | Cormorant Garamond + Source Serif 4 |
| 宣纸古卷 | LXGW WenKai 700 | LXGW WenKai 400 / Noto Serif SC | Cormorant Garamond Italic |
| 水墨留白 | Noto Serif SC 900 | Noto Sans SC 300 | （极少使用）|
| 故宫赤红 | Noto Serif SC 900 | Noto Sans SC 400 | Cormorant |
| 得意黑潮 | Smiley Sans Bold | Noto Sans SC 400 | Anton / Archivo Black |
| 玻璃拟态 | Noto Sans SC 500/700 | Noto Sans SC 300 | Inter |
| 极简日式 | Noto Serif SC 500（弱化粗细）| Noto Sans SC 300 | Cormorant Garamond 300 |

---

## 三、字号尺度三档（用户可选）

均通过 `viewport-cn.css` 的 `:root.density-*` 类切换。

### 紧凑 (compact)
- 标题 1.4-3.5rem · 正文 0.78-1rem
- 适合：知识点密集的教程、信息量大的内容页
- HTML 设置：`<html class="density-compact">`

### 标准 (normal) — 默认
- 标题 1.6-4rem · 正文 0.85-1.1rem
- 适合：演讲、分享、汇报、大多数场景
- HTML 设置：`<html>` (无 class)

### 宽松 (loose)
- 标题 1.8-4.5rem · 正文 0.95-1.2rem
- 适合：金句墙、思想性内容、留白多的封面 / 收尾
- HTML 设置：`<html class="density-loose">`

---

## 四、中文排版细节铁律

1. **行高最低 1.6** —— 中文方块字密度高，1.4 行高会让正文极度压抑。
2. **中文不要 letter-spacing < 0** —— 西文用 -0.005em 让字母更紧凑；中文绝不允许，最低 0。
3. **数字 / 英文专用斜体或等宽** —— 中文不能用 italic（思源宋没有真正的斜体）。中英混排时，斜体保留给西文。
4. **粗细：中文以 700 / 900 为主标题，300/400 为正文**。500 在中文里是过渡值，慎用。
5. **避免连续 3 个不同字体** —— 一份 PPT 最多 1 主标 + 1 正文 + 1 数字 / 西文。
6. **标点收紧** —— 中文标点占一格，可用 `text-spacing: trim-start trim-end` 实验（不支持则忽略）。
7. **避免居中正文** —— 居中适合标题，正文（>20 字）应左对齐，否则视线疲劳。
8. **字距 letter-spacing：** 标题正常或 -0.005em（西文）；正文中文 0 - 0.01em。
9. **大字号反而要 line-height 紧一点** —— 标题 1.1-1.3 即可，正文才需要 1.6+。
10. **整段中文用 `text-align: justify` 慎用** —— 中文两端对齐很容易产生大空隙，左对齐 + 内容压缩更舒服。

---

## 五、混合中英文示例

```html
<h2 class="cn"><span class="en">2026</span> 八大方向</h2>
<!-- "2026" 用西文字距 -0.005em，"八大方向" 用中文字距 0.01em -->

<p class="cn">
    我去年 <span class="en">9</span> 月在深圳 <span class="en">AI</span> 大会发了条朋友圈：
    "<span class="en">AI</span> 视频仍然远远被低估了"。
</p>
```

CSS 已在 viewport-cn.css 中通过 `.cn` / `.en` 工具类与 `[lang^="zh"]` 选择器分别处理。

---

## 六、字体加载策略

**只用 `<link rel="preconnect">` + `<link href="...">` 加载 Google Fonts，不要内嵌大字体文件**：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700;900&family=Noto+Sans+SC:wght@300;400;500&family=Cormorant+Garamond:ital,wght@1,400;1,500&display=swap" rel="stylesheet">
```

霞鹜文楷 / 得意黑用 CDN：

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/smiley-sans@2.0.1/index.css">
```

**fallback 链：** `'Noto Serif SC', 'Source Han Serif SC', 'Songti SC', serif`
