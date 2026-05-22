# 长文版式 · 13 种 + 4 种图片版式

> 与 deck.css 配套，类名体系：`.frame` / `.stage` / `.runner` / `.cue` / `.unfold` / `.lede` 等。
> 每种版式有：用途 · 内容密度上限 · HTML 骨架 · 关键 CSS 片段。
> 生成时按大纲的 `类型` 字段选用。

---

## 索引

| # | 版式 | 类名 | 内容上限 | 用途 |
|---|------|------|---------|------|
| 1 | 封面 | `.front-frame` | 主标 + 副标 + 标识 | 首页 |
| 2 | 序章 | `.preface` | 标题 + 引语 + 3 卡 | 开场 / 章节引入 |
| 3 | 目录 | `.index-card` | 6-8 条 | 全篇导览 |
| 4 | 章节扉 | `.chapter-plate` | 章节号 + 标题 + 引语 | PART 起始 |
| 5 | 物料网格 | `.atlas` | 1 标题 + 6 卡 | 工具 / 资源 / 清单 |
| 6 | 对话双栏 | `.dialog` | 1 标题 + 左右各 5 条 | 对比 / 多面 |
| 7 | 步骤流 | `.steps` | 1 标题 + 4 步 | 流程 / 飞轮 |
| 8 | 样本双联 | `.specimens` | 1 标题 + 2 案例 | 案例 / 故事 |
| 9 | 阶段递进 | `.phases` | 1 标题 + 3 阶段 | 演进 / 等级 |
| 10 | 星座网格 | `.constellation` | 1 标题 + 8 项 + 底座 | 八大 / 集合 |
| 11 | 信条卡 | `.tenets` | 1 标题 + 2-4 信条 | 心法 / 原则 |
| 12 | 箴言墙 | `.maxims` | 8-12 条 | 金句 |
| 13 | 终章 | `.coda` | 主语 + 副语 + 落款 | 末页 |
| 14 | 全图主视觉 | `.frame--vista` | 1 大图 + 角标 | 重磅画面 |
| 15 | 图文对位 | `.frame--diptych` | 1 图 + 1 文区 | 图文左右 |
| 16 | 图集 | `.gallery` | 1 标题 + 2/3/4 图 | 图集 |
| 17 | 章节图扉 | `.chapter-plate--vista` | part + 背景虚化图 | 章节带图 |

---

## 字数预算表（Phase 2.1 必查）

> 这是「**整页文字总量**」上下限，不是版式槽位数（槽位数见各小节"内容上限"列）。
> 超上限 → 拆 2 页 或 换更密版式；不足下限 → 合并 或 换稀疏版式。
> 字数 = 中文字符数 + 英文 word × 1.5 估算；双语版 (zh+en) 字数 × 1.7 后再比对。

| # | 版式 | 字数下限 | 字数上限 | 细则 |
|---|------|---------|---------|------|
| 1 | `.front-frame` 封面 | 10 | 30 | 主标 ≤ 14 字 / 副标 ≤ 16 字 |
| 2 | `.preface` 序章 | 80 | 180 | 引语 ≤ 50 / 每卡 20-40 |
| 3 | `.index-card` 目录 | 60 | 140 | 每条 6-14 字 × 6-8 条 |
| 4 | `.chapter-plate` 章节扉 | 20 | 60 | 章节标题 ≤ 14 / 引语 ≤ 40 |
| 5 | `.atlas` 物料网格 | 80 | 180 | 每卡 12-25 字 × 6 |
| 6 | `.dialog` 对话双栏 | 100 | 220 | 每条 8-20 字 × 10 |
| 7 | `.steps` 步骤流 | 80 | 180 | 每步：标题 ≤ 12 + 说明 ≤ 30 |
| 8 | `.specimens` 样本双联 | 120 | 240 | 每案例 60-120 |
| 9 | `.phases` 阶段递进 | 80 | 180 | 每阶段 25-55 |
| 10 | `.constellation` 星座网格 | 80 | 180 | 每项 8-20 字 × 8 |
| 11 | `.tenets` 信条卡 | 60 | 160 | 每信条 15-40 |
| 12 | `.maxims` 箴言墙 | 80 | 200 | 每条 8-18 字 × 8-12 |
| 13 | `.coda` 终章 | 20 | 60 | 主语 + 副语 + 落款 |
| 14 | `.frame--vista` 全图主视觉 | 0 | 30 | 仅角标 / 短标题 |
| 15 | `.frame--diptych` 图文对位 | 60 | 160 | 文字区 |
| 16 | `.gallery` 图集 | 20 | 80 | 标题 + caption |
| 17 | `.chapter-plate--vista` 章节图扉 | 20 | 60 | 同 `.chapter-plate` |
| ⭐ | `.aphorism` 单句金句 | 8 | 40 | 单句 ≤ 28 / 落款 ≤ 12 |

**信息密度自检（每页必过）：**
1. **1 个核心观点 + 1-4 个论据** 是标准。只有观点没论据 → 找原文补 或 合并到邻页。
2. **3+ 个不同观点挤一页** → 拆。拆后两页都不足下限 → 说明拆法错了，改回合并 + 换稀疏版式。
3. **金句版式特殊**：`.aphorism` `.maxims` 命中 [SKILL.md 金句五诊](SKILL.md#21-生成大纲) ≥ 3 才能用。

---

## 公共元素

### .runner（页脚徽章带）

```html
<div class="runner runner--bottom">
    <span class="runner-mark">PROLOGUE</span>
    <span class="latin">01 / 17</span>
</div>
```

### .cue（小标题）

```html
<div class="cue">CONTENTS · 导览</div>
```

### .lede（大标题）+ .deck-meta（副语）

```html
<h2 class="lede unfold">主标题</h2>
<p class="deck-meta unfold">副语 / 说明</p>
```

---

## 1 · 封面 · `.front-frame`

```html
<section class="frame front-frame" data-title="封面">
    <div class="stage">
        <div class="cover-top unfold">
            <span class="latin">DECK · 2026</span>
            <span class="latin">EP · 01</span>
        </div>
        <div class="cover-core unfold">
            <span class="cover-stamp"><span class="latin">●</span> 标识徽章</span>
            <h1 class="cover-title">主<span class="accent-key">标</span>题</h1>
            <p class="cover-sub">一句副标 · 一句注释</p>
        </div>
        <div class="cover-bottom unfold latin">— SCROLL DOWN —</div>
    </div>
</section>
```

**关键 CSS：**
```css
.front-frame .stage { justify-content: space-between; align-items: center; text-align: center; }
.cover-core { display: flex; flex-direction: column; align-items: center; gap: 28px; }
.cover-title {
    font-family: var(--type-display-cn);
    font-weight: 700;
    font-size: var(--type-display);
    line-height: var(--leading-tight);
    color: var(--stage-paper);
}
.cover-stamp {
    display: inline-flex; align-items: center; gap: 0.6em;
    padding: 0.4em 0.9em; border-radius: 2em;
    border: 1px solid var(--accent-key);
    color: var(--accent-key);
    font-family: var(--type-latin); font-style: italic;
    font-size: var(--type-small);
}
```

---

## 2 · 序章 · `.preface`

```html
<section class="frame preface" data-title="序章">
    <div class="stage">
        <div class="preface-label unfold latin">// PROLOGUE</div>
        <h2 class="lede unfold">主标题（一两行）</h2>
        <p class="deck-meta unfold">引语 / 楔子（一两句）</p>
        <div class="trinity">
            <article class="trinity-card unfold">
                <div class="trinity-num latin">01</div>
                <h3 class="trinity-title">小标</h3>
                <p class="trinity-desc">描述...</p>
            </article>
            <article class="trinity-card unfold">...</article>
            <article class="trinity-card unfold">...</article>
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.preface .stage { justify-content: center; gap: var(--stage-gap); }
.preface-label {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-h3); font-weight: 400;
    letter-spacing: var(--track-tag);
}
.trinity {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 18px; margin-top: 18px;
}
.trinity-card {
    border-left: 1px solid var(--accent-key);
    padding: 18px 22px;
    background: linear-gradient(90deg,
        color-mix(in srgb, var(--accent-key) 6%, transparent),
        transparent 80%);
}
.trinity-num {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: 2.4rem; font-weight: 500;
    line-height: 1;
    margin-bottom: 0.3em;
}
.trinity-title {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3); line-height: var(--leading-snug);
    color: var(--stage-paper);
    margin-bottom: 0.4em;
}
.trinity-desc {
    font-size: var(--type-small);
    color: var(--stage-faint);
    line-height: var(--leading-cozy);
}
```

---

## 3 · 目录 · `.index-card`

```html
<section class="frame index-card" data-title="目录">
    <div class="stage">
        <div class="cue unfold">CONTENTS · 导览</div>
        <h2 class="lede unfold">本篇导览</h2>
        <p class="deck-meta unfold">副标说明</p>
        <ol class="index-list">
            <li class="unfold"><span class="index-t">条目 1</span><span class="index-d latin">PART 01</span></li>
            <li class="unfold"><span class="index-t">条目 2</span><span class="index-d latin">PART 02</span></li>
            ...
        </ol>
    </div>
</section>
```

**关键 CSS：**
```css
.index-list {
    list-style: none; counter-reset: idx;
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 14px 56px; margin-top: 18px;
}
.index-list li {
    counter-increment: idx;
    display: flex; align-items: baseline; gap: 1em;
    padding-bottom: 12px;
    border-bottom: 1px dashed
        color-mix(in srgb, var(--accent-key) 40%, transparent);
}
.index-list li::before {
    content: counter(idx, decimal-leading-zero);
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-h3); font-weight: 500;
    min-width: 2.4em;
}
.index-t {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3); flex: 1;
    color: var(--stage-paper);
}
.index-d {
    font-family: var(--type-latin); font-style: italic;
    font-size: var(--type-small); color: var(--stage-faint);
}
```

---

## 4 · 章节扉 · `.chapter-plate`

```html
<section class="frame chapter-plate" data-title="PART 01">
    <div class="stage">
        <div class="chapter-num unfold latin">PART · 01</div>
        <h2 class="chapter-title unfold">章节标题</h2>
        <div class="chapter-en unfold latin">EN SUBTITLE</div>
        <p class="chapter-lead unfold">章节引语 / 定调</p>
    </div>
</section>
```

**关键 CSS：**
```css
.chapter-plate .stage { justify-content: center; }
.chapter-num {
    display: flex; align-items: center; gap: 0.9em;
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-body); font-weight: 500;
    letter-spacing: var(--track-tag);
}
.chapter-num::after {
    content: ''; flex: 1; max-width: 100px;
    height: 1px; background: var(--accent-key); opacity: 0.5;
}
.chapter-title {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h1); line-height: 1.1;
    background: linear-gradient(180deg,
        var(--stage-paper) 20%,
        var(--accent-key) 95%);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
}
.chapter-en {
    font-family: var(--type-latin); font-style: italic;
    color: var(--stage-faint);
    font-size: var(--type-h3); margin-top: 1em;
    letter-spacing: var(--track-tag);
}
.chapter-lead {
    font-size: var(--type-body); color: var(--stage-ink);
    margin-top: 1.6em; max-width: 50ch;
    line-height: var(--leading-roomy);
    border-left: 1px solid var(--accent-key); padding-left: 1.2em;
}
```

---

## 5 · 物料网格 · `.atlas`

```html
<section class="frame" data-title="物料">
    <div class="stage">
        <div class="cue unfold">CATALOG</div>
        <h2 class="lede unfold">主标题</h2>
        <div class="atlas">
            <article class="atlas-item unfold">
                <div class="atlas-tag latin">01 · TAG</div>
                <h3 class="atlas-name">名称</h3>
                <div class="atlas-role">角色/定位</div>
                <div class="atlas-desc">描述</div>
            </article>
            ... × 6
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.atlas {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 18px; margin-top: 24px;
}
.atlas-item {
    border-top: 1px solid var(--accent-key);
    padding: 16px 14px 16px 0;
    background: linear-gradient(180deg,
        color-mix(in srgb, var(--accent-key) 5%, transparent),
        transparent 70%);
}
.atlas-tag {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-small);
    letter-spacing: var(--track-tag);
}
.atlas-name {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3); line-height: var(--leading-snug);
    color: var(--stage-paper);
    margin: 0.3em 0 0.3em;
}
.atlas-role {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-warn);
    font-size: var(--type-body);
}
.atlas-desc {
    font-size: var(--type-small); color: var(--stage-faint);
    line-height: var(--leading-cozy);
    margin-top: 0.4em;
}
```

---

## 6 · 对话双栏 · `.dialog`

```html
<section class="frame" data-title="对话">
    <div class="stage">
        <div class="cue unfold">COMPARISON</div>
        <h2 class="lede unfold">主标题</h2>
        <p class="deck-meta unfold">一句副标</p>
        <div class="dialog">
            <div class="dialog-pane unfold">
                <h3 class="dialog-head">左栏标</h3>
                <ul class="dialog-list">
                    <li>条目 1</li>
                    <li>条目 2</li>
                </ul>
            </div>
            <div class="dialog-pane unfold">
                <h3 class="dialog-head">右栏标</h3>
                <ul class="dialog-list">...</ul>
            </div>
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.dialog {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: var(--col-gap); margin-top: 18px;
}
.dialog-head {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-body); font-weight: 500;
    letter-spacing: var(--track-tag);
    border-bottom: 1px solid var(--accent-key);
    padding-bottom: 0.5em;
    margin-bottom: 0.8em;
}
.dialog-list { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.dialog-list li {
    font-size: var(--type-body); color: var(--stage-ink);
    line-height: var(--leading-cozy);
    padding-left: 1.2em; position: relative;
    font-weight: 300;
}
.dialog-list li::before {
    content: ''; position: absolute;
    left: 0; top: 0.55em;
    width: 6px; height: 6px;
    border: 1px solid var(--accent-key);
    transform: rotate(45deg);  /* 菱形 */
}
.dialog-list li b {
    color: var(--accent-soft);
    font-style: italic; font-family: var(--type-latin); font-weight: 500;
}
```

---

## 7 · 步骤流 · `.steps`

```html
<section class="frame" data-title="步骤">
    <div class="stage">
        <div class="cue unfold">THE PROCESS</div>
        <h2 class="lede unfold">主标</h2>
        <p class="deck-meta unfold">副标</p>
        <div class="steps">
            <div class="step-tile unfold">
                <div class="step-mark latin">01</div>
                <h4 class="step-name">步骤名</h4>
                <p class="step-body">描述</p>
            </div>
            ... × 4
        </div>
        <p class="steps-coda unfold latin">▽ 一句话总结 ▽</p>
    </div>
</section>
```

**关键 CSS：**
```css
.steps {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 12px; margin-top: 24px;
}
.step-tile {
    border-top: 1px solid color-mix(in srgb, var(--accent-key) 30%, transparent);
    padding: 16px 8px 8px 0;
    position: relative;
}
.step-tile::before {
    content: ''; position: absolute; top: -1px; left: 0;
    width: 30%; height: 1px; background: var(--accent-key);
}
.step-mark {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: 2rem; line-height: 1;
}
.step-name {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3); line-height: var(--leading-snug);
    color: var(--stage-paper);
    margin: 0.5em 0 0.3em;
}
.step-body {
    font-size: var(--type-small);
    color: var(--stage-faint);
    line-height: var(--leading-cozy);
}
.steps-coda {
    text-align: center; margin-top: 22px;
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-soft);
    font-size: var(--type-body);
    letter-spacing: var(--track-tag);
}
```

---

## 8 · 样本双联 · `.specimens`

```html
<section class="frame" data-title="案例">
    <div class="stage">
        <h2 class="lede unfold">主标</h2>
        <div class="specimens">
            <article class="specimen unfold">
                <div class="specimen-tag latin">CASE 01 · 副标</div>
                <h4 class="specimen-title">案例标题</h4>
                <p class="specimen-body">案例描述...</p>
            </article>
            <article class="specimen unfold">...</article>
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.specimens {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 24px; margin-top: 16px;
}
.specimen {
    border-left: 1px solid var(--accent-key);
    padding: 18px 22px;
    background: linear-gradient(90deg,
        color-mix(in srgb, var(--accent-key) 6%, transparent),
        transparent 80%);
}
.specimen-tag {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-small);
    letter-spacing: var(--track-tag);
    font-weight: 500;
}
.specimen-title {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3); line-height: var(--leading-snug);
    color: var(--stage-paper);
    margin: 0.5em 0;
}
.specimen-body {
    font-size: var(--type-body); color: var(--stage-faint);
    line-height: var(--leading-roomy);
}
```

---

## 9 · 阶段递进 · `.phases`

```html
<section class="frame" data-title="阶段">
    <div class="stage">
        <h2 class="lede unfold">主标</h2>
        <div class="phases">
            <article class="phase unfold">
                <div class="phase-roman">I</div>
                <div class="phase-formula latin">公式</div>
                <h4 class="phase-name">阶段名</h4>
                <p class="phase-desc">描述</p>
            </article>
            <article class="phase unfold">II ...</article>
            <article class="phase unfold">III ...</article>
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.phases {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 18px; margin-top: 28px;
}
.phase {
    padding: 22px 18px;
    border-top: 2px solid var(--stage-faint);
}
.phase:nth-child(2) { border-top-color: var(--accent-warn); }
.phase:nth-child(3) { border-top-color: var(--accent-key); }
.phase-roman {
    font-family: var(--type-display-cn); font-style: italic;
    color: var(--stage-faint);
    font-size: var(--type-body);
    letter-spacing: var(--track-tag);
    margin-bottom: 0.5em;
}
.phase-formula {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key); font-size: var(--type-body);
    margin-bottom: 0.6em;
}
.phase-name {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3);
    color: var(--stage-paper);
    line-height: var(--leading-snug);
    margin-bottom: 0.5em;
}
.phase-desc {
    font-size: var(--type-body); color: var(--stage-faint);
    line-height: var(--leading-cozy);
}
```

---

## 10 · 星座网格 · `.constellation`

```html
<section class="frame" data-title="八大">
    <div class="stage">
        <h2 class="lede unfold">主标</h2>
        <div class="constellation-base unfold">底座说明（一行文字）</div>
        <div class="constellation">
            <article class="star unfold"><div class="star-num latin">01</div><div class="star-name">方向</div><div class="star-tag">一句</div></article>
            ... × 8
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.constellation {
    display: grid; grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 1fr; gap: 10px; margin-top: 14px;
}
.star {
    border: 1px solid color-mix(in srgb, var(--accent-key) 25%, transparent);
    padding: 14px;
    background: color-mix(in srgb, var(--accent-key) 3%, transparent);
    transition: background 0.4s, border-color 0.4s;
}
.star:hover {
    background: color-mix(in srgb, var(--accent-key) 10%, transparent);
    border-color: var(--accent-key);
}
.star-num {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key); font-size: var(--type-small);
}
.star-name {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3); color: var(--stage-paper);
    margin: 0.2em 0;
}
.star-tag {
    font-size: var(--type-small); color: var(--stage-faint);
    line-height: var(--leading-cozy);
}
.constellation-base {
    padding: 14px 20px;
    background: linear-gradient(90deg,
        color-mix(in srgb, var(--accent-key) 12%, transparent),
        transparent);
    border-left: 2px solid var(--accent-key);
    font-size: var(--type-body); color: var(--stage-ink);
    line-height: var(--leading-cozy);
}
.constellation-base b { color: var(--accent-key); font-weight: 500; }
```

---

## 11 · 信条卡 · `.tenets`

```html
<section class="frame" data-title="心法">
    <div class="stage">
        <h2 class="lede unfold">主标</h2>
        <div class="tenets tenets--2">
            <article class="tenet unfold">
                <div class="tenet-label latin">PRINCIPLE 01 · 关键词</div>
                <h4 class="tenet-name">心法名</h4>
                <p class="tenet-body">详述</p>
            </article>
            ... (2/3/4 张)
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.tenets { display: grid; gap: 18px; margin-top: 22px; }
.tenets--2 { grid-template-columns: 1fr 1fr; }
.tenets--3 { grid-template-columns: repeat(3, 1fr); }
.tenets--4 { grid-template-columns: repeat(2, 1fr); }
.tenet {
    padding: 18px 24px;
    border-left: 1px solid var(--accent-key);
    background: linear-gradient(90deg,
        color-mix(in srgb, var(--accent-key) 5%, transparent),
        transparent 90%);
}
.tenet-label {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-small);
    letter-spacing: var(--track-tag);
    margin-bottom: 0.5em; font-weight: 500;
}
.tenet-name {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h3); line-height: var(--leading-snug);
    color: var(--stage-paper);
    margin-bottom: 0.5em;
}
.tenet-body {
    font-size: var(--type-body); color: var(--stage-faint);
    line-height: var(--leading-roomy);
}
```

---

## 12 · 箴言墙 · `.maxims`

```html
<section class="frame" data-title="金句">
    <div class="stage">
        <h2 class="lede unfold">主标 · 金句备忘</h2>
        <div class="maxims">
            <div class="maxim unfold">金句 1</div>
            <div class="maxim maxim--hl unfold">特别强调</div>
            <div class="maxim unfold">金句 3</div>
            ... (8-12 条)
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.maxims {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 14px; margin-top: 16px;
}
.maxim {
    padding: 12px 16px 12px 1.6em;
    border-bottom: 1px solid color-mix(in srgb, var(--accent-key) 25%, transparent);
    font-family: var(--type-display-cn);
    font-size: var(--type-body); font-weight: 500;
    line-height: var(--leading-snug);
    color: var(--stage-ink);
    position: relative;
}
.maxim::before {
    content: '"'; position: absolute; left: 0; top: -0.15em;
    color: var(--accent-key);
    font-size: 2em; line-height: 1;
    font-family: var(--type-latin); font-style: italic;
}
.maxim--hl { color: var(--accent-key); }
.maxim--hl::before { color: var(--accent-warn); }
```

---

## 13 · 终章 · `.coda`

```html
<section class="frame coda" data-title="终章">
    <div class="stage">
        <div class="coda-pre unfold latin">END · 2026 / 04 / 15</div>
        <h1 class="coda-headline unfold">乾坤未定<br>你我皆是<span class="accent-key">黑马</span></h1>
        <p class="coda-post unfold">"一句副语 / 短引"</p>
        <div class="coda-sign unfold latin">— A LONG-TEXT DECK —</div>
    </div>
</section>
```

**关键 CSS：**
```css
.coda .stage { justify-content: center; text-align: center; align-items: center; }
.coda-pre {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-body);
    letter-spacing: var(--track-tag);
    margin-bottom: 24px;
}
.coda-headline {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-display); line-height: var(--leading-tight);
    background: linear-gradient(180deg,
        var(--stage-paper) 10%,
        var(--accent-key) 90%);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.6em;
}
.coda-post {
    font-family: var(--type-display-cn); font-weight: 400;
    font-size: var(--type-h3); color: var(--stage-ink);
    max-width: 32ch; line-height: var(--leading-roomy);
}
.coda-sign {
    margin-top: 40px;
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-small);
    letter-spacing: var(--track-tag);
}
.coda-sign::before, .coda-sign::after {
    content: ''; display: inline-block;
    width: 36px; height: 1px;
    background: var(--accent-key);
    vertical-align: middle;
    margin: 0 12px;
}
```

---

## 14 · 单句金句 · `.aphorism` ⭐ 双语友好

**用途：** 一条金句独占一页，大字居中。英文原文 + 中文译文堆叠。最适合演讲的"高光时刻"。

```html
<section class="frame aphorism" data-title="金句">
    <div class="stage">
        <div class="aphorism-mark unfold latin">EPIGRAPH · 02</div>
        <blockquote class="aphorism-quote unfold">
            <p class="quote-en">There are cracks in everything,<br>and that's how the light gets in.</p>
            <p class="quote-cn">万物皆有裂痕<br>那是光照进来的地方</p>
        </blockquote>
        <div class="aphorism-attr unfold latin">— Leonard Cohen</div>
    </div>
</section>
```

**关键 CSS：**
```css
.aphorism .stage { justify-content: center; text-align: center; align-items: center; gap: 36px; }
.aphorism-mark {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-body);
    letter-spacing: 0.4em;
    text-transform: uppercase;
}
.aphorism-quote {
    position: relative;
    max-width: 32ch;
    padding: 0 1em;
}
.aphorism-quote::before {
    content: '\201C';
    position: absolute; top: -0.4em; left: -0.3em;
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: 6rem; line-height: 1; opacity: 0.35;
}
.aphorism-quote .quote-en {
    font-family: var(--type-latin); font-style: italic; font-weight: 500;
    font-size: 2.4rem;
    line-height: var(--leading-snug);
    color: var(--stage-paper);
    margin-bottom: 0.8em;
}
.aphorism-quote .quote-cn {
    font-family: var(--type-display-cn); font-weight: 400;
    font-size: 1.5rem;
    line-height: var(--leading-cozy);
    color: var(--stage-faint);
    letter-spacing: 0.05em;
}
/* 单语版本（无 en 时） */
.aphorism-quote.cn-only .quote-cn {
    font-size: 2.6rem;
    color: var(--stage-paper);
    font-weight: 700;
}
.aphorism-attr {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-key);
    font-size: var(--type-body);
    letter-spacing: 0.2em;
    margin-top: 16px;
}
.aphorism-attr::before {
    content: ''; display: inline-block;
    width: 36px; height: 1px;
    background: var(--accent-key);
    vertical-align: middle; margin-right: 16px;
}
```

---

## 15 · 双语修饰类 · `.bilingual-*`

为现有版式（cover / chapter-plate / tenets / specimens / coda）增加双语呈现能力。

### 15.a · 双语封面 `.front-frame.bilingual`

```html
<section class="frame front-frame bilingual" data-title="封面">
    <div class="stage">
        ...
        <h1 class="cover-title">
            <span class="cn">61 岁那年我确信的事</span>
            <span class="en latin">12 Truths I Learned from Life and Writing</span>
        </h1>
        ...
    </div>
</section>
```

```css
.front-frame.bilingual .cover-title .cn { display: block; font-size: 5rem; line-height: 1.1; }
.front-frame.bilingual .cover-title .en {
    display: block; margin-top: 0.4em;
    font-family: var(--type-latin); font-style: italic; font-weight: 500;
    font-size: 1.6rem;
    color: var(--stage-faint);
    letter-spacing: 0.02em;
    line-height: 1.4;
}
```

### 15.b · 双语章节扉 `.chapter-plate.bilingual`

```html
<section class="frame chapter-plate bilingual" data-title="PART 01">
    <div class="stage">
        <div class="chapter-num latin">PART · 01</div>
        <h2 class="chapter-title">
            <span class="cn">关于自我</span>
            <span class="en latin">On the Self</span>
        </h2>
        <p class="chapter-lead">
            <span class="en latin">"...EN quote..."</span>
            <span class="cn">中文译文 ——</span>
        </p>
    </div>
</section>
```

```css
.chapter-plate.bilingual .chapter-title {
    display: flex; flex-direction: column; gap: 0.2em;
}
.chapter-plate.bilingual .chapter-title .en {
    font-family: var(--type-latin); font-style: italic; font-weight: 500;
    font-size: 2rem;
    color: var(--accent-key);
    -webkit-text-fill-color: var(--accent-key);
    background: none;
}
.chapter-plate.bilingual .chapter-lead {
    display: flex; flex-direction: column; gap: 0.6em;
}
.chapter-plate.bilingual .chapter-lead .en {
    font-family: var(--type-latin); font-style: italic;
    color: var(--accent-soft);
}
```

### 15.c · 双语信条卡 `.tenet.bilingual`

```html
<article class="tenet bilingual">
    <div class="tenet-num latin">06</div>
    <div class="tenet-label">BIRD BY BIRD</div>
    <h4 class="tenet-name">
        <span class="cn">一只鸟一只鸟地写</span>
        <span class="en latin">Take it bird by bird</span>
    </h4>
    <p class="tenet-body">中文正文（主）...</p>
    <p class="tenet-body-en latin">English body text below as supplement...</p>
</article>
```

```css
.tenet.bilingual .tenet-name { display: flex; flex-direction: column; gap: 0.3em; }
.tenet.bilingual .tenet-name .en {
    font-family: var(--type-latin); font-style: italic; font-weight: 500;
    font-size: 1rem;
    color: var(--accent-key);
}
.tenet-body-en {
    font-family: var(--type-latin); font-style: italic;
    font-size: 0.86rem;
    color: var(--stage-faint);
    line-height: var(--leading-cozy);
    margin-top: 0.7em;
    padding-top: 0.7em;
    border-top: 1px dashed
        color-mix(in srgb, var(--accent-key) 30%, transparent);
}
```

### 15.d · 双语样本双联 `.specimen.bilingual`

```html
<article class="specimen bilingual">
    <div class="specimen-tag latin">CASE 01</div>
    <h4 class="specimen-title">
        <span class="cn">中文标题</span>
        <span class="en latin">English Subtitle</span>
    </h4>
    <blockquote class="specimen-quote">
        <p class="quote-en">"English original..."</p>
        <p class="quote-cn">"中文译文..."</p>
    </blockquote>
    <p class="specimen-body">补充说明...</p>
</article>
```

```css
.specimen.bilingual .specimen-title { display: flex; flex-direction: column; gap: 0.2em; }
.specimen.bilingual .specimen-title .en {
    font-family: var(--type-latin); font-style: italic; font-weight: 500;
    font-size: 1rem;
    color: var(--accent-soft);
}
.specimen-quote {
    border-left: 2px solid var(--accent-key);
    padding-left: 1em; margin: 0.8em 0;
}
.specimen-quote .quote-en {
    font-family: var(--type-latin); font-style: italic;
    font-size: 1.05rem; color: var(--stage-paper);
    line-height: 1.5; margin-bottom: 0.4em;
}
.specimen-quote .quote-cn {
    font-family: var(--type-display-cn);
    font-size: 0.95rem; color: var(--stage-faint);
    line-height: 1.6;
}
```

### 15.e · 双语终章 `.coda.bilingual`

```html
<section class="frame coda bilingual" data-title="终章">
    <div class="stage">
        <div class="coda-pre latin">END · TED 2017</div>
        <h1 class="coda-headline">
            <span class="en latin">All walking each other home.</span>
            <span class="cn">我们只是互相把对方送回家。</span>
        </h1>
        <p class="coda-attr latin">— Ram Dass</p>
    </div>
</section>
```

```css
.coda.bilingual .coda-headline { display: flex; flex-direction: column; gap: 0.4em; }
.coda.bilingual .coda-headline .en {
    font-family: var(--type-latin); font-style: italic; font-weight: 700;
    font-size: 4rem; line-height: 1.15;
    color: var(--accent-key);
    -webkit-text-fill-color: var(--accent-key);
    background: none;
}
.coda.bilingual .coda-headline .cn {
    font-family: var(--type-display-cn); font-weight: 500;
    font-size: 2.4rem; line-height: 1.3;
    color: var(--stage-paper);
}
```

---

## 双语处理逻辑（生成时）

```python
lang = meta.get("dominant_lang", "zh")

if lang == "en":
    # Claude 自己翻译，生成大纲时输出 {cn, en} 双字段
    use_bilingual_class = True
elif lang == "bilingual":
    # 文本中已有中英对照，直接配对
    use_bilingual_class = True
elif lang == "zh":
    # 单语中文，无需双语版式
    use_bilingual_class = False
```

启用双语模式时：
- 所有 `.front-frame` / `.chapter-plate` / `.tenet` / `.specimen` / `.coda` 加 `.bilingual` 修饰类
- `.aphorism` 默认就支持双语
- 字号尺度自动收紧一档（双语内容比单语多 50%，需更紧凑）

---

## 16 · 全图主视觉 · `.frame--vista`

```html
<section class="frame frame--vista" data-title="主视觉">
    <img src="assets/img-001.png" class="vista-image unfold" alt="..." />
    <div class="vista-veil unfold">
        <div class="cue">EYEBROW</div>
        <h2 class="vista-headline">标题</h2>
        <p class="vista-sub">一两句副语</p>
    </div>
</section>
```

**关键 CSS：**
```css
.frame--vista { position: relative; padding: 0; overflow: hidden; }
.vista-image {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
    object-fit: cover; z-index: 0;
}
.vista-veil {
    position: absolute; bottom: 0; left: 0; right: 0;
    padding: var(--frame-pad);
    background: linear-gradient(0deg,
        rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.55) 60%, transparent 100%);
    z-index: 2; color: #fff;
}
.vista-headline {
    font-family: var(--type-display-cn); font-weight: 700;
    font-size: var(--type-h1); line-height: var(--leading-tight);
}
.vista-sub {
    font-size: var(--type-body); margin-top: 0.5em;
    line-height: var(--leading-cozy); opacity: 0.85;
}
```

---

## 15 · 图文对位 · `.frame--diptych`

图位于左 (`.diptych--left`) 或右 (`.diptych--right`)。

```html
<section class="frame frame--diptych diptych--left" data-title="图文">
    <div class="diptych-wing diptych-image unfold">
        <img src="assets/img-001.png" alt="..." />
    </div>
    <div class="diptych-wing diptych-text">
        <div class="stage">
            <div class="cue unfold">EYEBROW</div>
            <h2 class="lede unfold">标题</h2>
            <p class="deck-meta unfold">说明...</p>
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.frame--diptych { flex-direction: row; padding: 0; }
.frame--diptych.diptych--right { flex-direction: row-reverse; }
.diptych-wing { flex: 1; overflow: hidden; position: relative; }
.diptych-image {
    background: var(--stage-void);
    display: flex; align-items: center; justify-content: center;
}
.diptych-image img {
    width: 100%; height: 100%;
    object-fit: cover;
}
.diptych-text { padding: var(--frame-pad); display: flex; }
.diptych-text .stage { justify-content: center; }
```

---

## 16 · 图集 · `.gallery`

```html
<section class="frame" data-title="图集">
    <div class="stage">
        <h2 class="lede unfold">标题</h2>
        <div class="gallery gallery--3">
            <figure class="unfold">
                <img src="assets/img-001.png" alt="..." />
                <figcaption>图 1 说明</figcaption>
            </figure>
            <figure class="unfold">...</figure>
            <figure class="unfold">...</figure>
        </div>
    </div>
</section>
```

**关键 CSS：**
```css
.gallery {
    display: grid; gap: 16px; margin-top: 22px;
}
.gallery--2 { grid-template-columns: repeat(2, 1fr); }
.gallery--3 { grid-template-columns: repeat(3, 1fr); }
.gallery--4 { grid-template-columns: repeat(4, 1fr); }
.gallery figure {
    display: flex; flex-direction: column; gap: 8px;
}
.gallery figure img {
    width: 100%; aspect-ratio: 4/3;
    object-fit: cover;
    border: 1px solid color-mix(in srgb, var(--accent-key) 20%, transparent);
}
.gallery figcaption {
    font-size: var(--type-small); color: var(--stage-faint);
    font-family: var(--type-latin); font-style: italic;
}
```

---

## 17 · 章节图扉 · `.chapter-plate--vista`

```html
<section class="frame chapter-plate chapter-plate--vista" data-title="PART 01">
    <img src="assets/cover-01.png" class="chapter-bg" alt="..." />
    <div class="stage">
        <div class="chapter-num unfold latin">PART · 01</div>
        <h2 class="chapter-title unfold">章节标题</h2>
        <div class="chapter-en unfold latin">EN SUBTITLE</div>
        <p class="chapter-lead unfold">引语</p>
    </div>
</section>
```

**关键 CSS：**
```css
.chapter-plate--vista .chapter-bg {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    opacity: 0.22;
    filter: saturate(0.85);
    z-index: 0;
}
```

---

## 图片嵌入策略（Phase 4 决策代码）

```python
total_bytes = sum(i["size"] for i in meta["images"])
use_base64 = len(meta["images"]) <= 5 and total_bytes <= 2 * 1024 * 1024
# True  → 把 assets/img-NNN 全部转 base64 内联到 HTML，最终单文件
# False → 保留 assets/ 引用，与 HTML 同目录交付
```

---

## HTML 整体结构

```html
<!doctype html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8" />
    <title>{title}</title>
    <link href="<选定风格 Google Fonts URL>" rel="stylesheet">
    <style>
        /* === deck.css 完整内联 === */
        /* === 选定风格的色板 + 字体（写入 :root） === */
        /* === 长文版式 CSS（按本文件） === */
    </style>
</head>
<body>
    <div class="marquee">
        <div class="deck" data-title="...">
            <section class="frame front-frame" data-title="封面" data-state="active">...</section>
            <section class="frame preface" data-title="序章">...</section>
            ...
            <section class="frame coda" data-title="终章">...</section>
        </div>
    </div>

    <nav class="rail" aria-label="frame navigation"></nav>
    <div class="hotkey-hint">← / → · SPACE · CLICK · F</div>

    <script>
        /* === deck.js 完整内联 === */
    </script>
</body>
</html>
```
