# Examples · 参考产出

> 这些是 longtext-to-slides 实际生成的 HTML 示范。
> **直接双击 / 浏览器打开**即可查看，作为生成质量参考基线。

## 当前示例

### yiren-dark-botanical.html

| 项 | 内容 |
|---|---|
| **输入** | 《一个人 + AI + 一群人：亦仁十周年直播分享整理》PDF（19 页，约 1 万字，公开演讲整理）|
| **输出** | 17 张 Dark Botanical 风格 HTML |
| **风格** | 黑金专访 Dark Botanical（深黑 + 暖金 + Cormorant 衬线）|
| **大纲详略** | 标准 |
| **版式比例** | 100vh 滚动（**旧版引擎**）|

**⚠ 引擎版本说明：**
此示例使用早期 `viewport-base.css` 引擎（100vh + scroll-snap）。当前 skill 已升级到 `deck.css` 舞台引擎（1280×720 fit-to-viewport + `data-state` 翻页）。
**示例的内容压缩思路仍可参考**，但 CSS 类名（`.slide` / `.chrome` / `.reveal`）与最新 `.frame` / `.runner` / `.unfold` 体系不同。

### 结构对照（输入 vs 输出）

| 原文章节 | PPT 张数 | 版式 |
|---------|---------|------|
| 封面 | 1 | cover |
| 开场（3 个原因）| 1 | opener |
| 目录 | 1 | toc |
| PART 01 工具清单 | 3 | part + tools-grid + opener |
| PART 02 四步框架 | 6 | part + framework + two-col + tools-grid + cases + opener |
| PART 03 心法 & 人机合一 | 3 | part + three-cards + stages |
| PART 04 2026 八大方向 | 2 | eight-grid + trends |
| PART 05 生财四站 | 1 | framework |
| 尾声四心法 | 1 | mindsets cols-2 |
| 收尾「乾坤未定」 | 1 | finale |

---

## 自己生成 demo

```bash
# Phase 1: 提取文本
python ../scripts/extract.py /path/to/file.pdf out/source.md

# Phase 2-5: 在 Claude Code 里触发 skill
# 「把这个文档做成 PPT」
```

输出会落到 `$LONG2PPT_OUTPUT/<title>-slides.html`（默认 `~/long2ppt/`）。
