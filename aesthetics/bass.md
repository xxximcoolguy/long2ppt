---
name: saul-bass-skill
description: |
  Saul Bass 视觉操作系统 —— 电影片头设计鼻祖 / 海报与 logo 大师 / 与希区柯克长期合作。
  五层蒸馏：① 视觉哲学（Symbols not stories / 复杂概念简化为单一几何剪影 / 片头作为序章而非演职员表）② 版式（几何剪影 / 撞色块 / 撕纸感 / 字体作为图形 / 黑底 + 单亮色块 / 不对称重心偏侧 / 标志性形态优先于装饰）③ 颜色字体（高饱和单色 + 黑 + 米 / 朱红橙黄宝石蓝 / 粗 sans serif / 手绘剪贴字）④ 视觉禁忌（反信息平铺 / 反 ornament / 反"看完就忘" / 必须有记忆点）⑤ 局限（不适合数据密集 / 多概念并列 / 多页 deck 易疲劳 / 静态海报转 PPT 挑战）。

  触发场景：
  - 用户说「Bass 风」「希区柯克片头风」「Anatomy of a Murder 风」「几何剪影」「电影海报感」
  - 长文本→PPT 需要"撞色块 + 几何标志性"封面 / 章节扉
  - 设计类 skill 需要"标志性形态 / 海报感"美学时调用
---

# Saul Bass · 视觉操作系统

> 「**Symbols, not stories.** 用单一标志性图像传达整部电影。」 — Saul Bass

| 项 | 内容 |
|---|---|
| **人物** | Saul Bass (1920-1996) |
| **代表作（片头）** | Vertigo (1958) · North by Northwest (1959) · Psycho (1960) · Casino (1995) |
| **代表作（海报）** | The Man with the Golden Arm (1955) · Anatomy of a Murder (1959) · Vertigo |
| **代表作（Logo）** | AT&T (1969) · United Airlines (1974) · Continental · Quaker Oats · Bell System |
| **核心** | 复杂叙事 → 单一几何剪影 · 撞色块 · 撕纸感 · 字体即图形 |

---

## 1. 视觉哲学

### MM-1 · Symbols, Not Stories
**用单一标志性图像传达整部电影**。
- *The Man with the Golden Arm* —— 不规则黑色手臂剪影 = 整部毒瘾电影的精神
- *Anatomy of a Murder* —— 红色尸体轮廓被切成几段 = 谋杀案的解剖
- *Vertigo* —— 螺旋线 = 心理眩晕

复杂叙事 → **复杂概念 → 简单几何形态**。

### MM-2 · Design is Thinking Made Visual
设计 = 思考的可视化。先想清楚"这件事的核心精神是什么"，再去画。

### MM-3 · 电影片头作为"序章"而非"演职员表"
Bass 革命：把电影片头从演职员表，变成**电影的视觉前奏**，定调整部影片情绪。
- *Psycho* 片头：横竖线条交错切割，预示"分裂 / 切割 / 母亲与儿子"
- *North by Northwest* 片头：白线在绿底上演变成纽约摩天楼网格

### MM-4 · 简化到几何剪影的能力
Bass 能把任何复杂主题压缩到 **2-5 个几何形态**：
- 圆 + 三角形 + 线段 = 大多数 Bass 海报的全部元素
- 剪影是"形态的本质"，不是"形状的细节"

---

## 2. 版式操作系统

### H-1 · 几何剪影承载所有信息
**规则：** 每张 frame 只用一个核心 shape 承载所有信息。
- 圆 / 三角形 / 矩形 / 线段 —— 不超过 3-4 个基本元素
- 复杂内容 → 提炼成 1 个核心标志性形态

### H-2 · 撞色块（Color Blocking）
**纯色矩形 / 几何形互相硬切**：
- 黑色背景 + 单一明亮色块
- 朱红 vs 黑 / 橙黄 vs 黑 / 宝石蓝 vs 米
- **无渐变，无过渡**

```css
.bass-frame {
  background: #1a1a1a;  /* 黑底 */
  position: relative;
}
.bass-shape {
  background: #c41e3a;  /* 朱红 */
  clip-path: polygon(...);  /* 几何剪影 */
}
```

### H-3 · 撕纸感 / 手工剪贴感
**vs 数字精确：** 故意保留边缘的"撕裂感" / "手剪的不规则"。
- CSS 实现：用 SVG `<feTurbulence>` 制造不规则边缘
- 或用真实剪纸扫描作为底图

```css
.torn-edge {
  filter: url(#torn-paper);  /* SVG turbulence */
}
```

### H-4 · 字体作为图形
Bass 的字体处理：
- **手绘字** —— 标题常自己画（如 *The Man with the Golden Arm*）
- **剪贴字** —— 字母被切割、拼接、错位
- **粗 sans serif** —— 海报常用 Akzidenz-Grotesk / Helvetica Bold 系
- 字体本身**就是图形元素**，不是"信息载体"

### H-5 · 不对称构图（重心偏侧）
- 视觉重心**绝不居中**
- 主形态在画面 1/3 或 2/3 位置
- 大量留白集中在一侧

### H-6 · 标志性形态 vs 装饰性
- 一张 frame **只有一个主形态**作为视觉钩子
- 其余元素（标题、字幕、副标）都从属于这个形态
- **绝不堆叠多个"亮点"**

---

## 3. 颜色与字体启发式

### 配色（高饱和单色 + 黑 / 米）
**Bass 标志色板：**

| 色 | HEX | 典型作品 |
|---|---|---|
| 朱红 | `#c41e3a` / `#d4341d` | *Anatomy of a Murder* / *The Man with the Golden Arm* |
| 橙黄 | `#f5a623` / `#ff8c00` | *Bunny Lake* 等 |
| 宝石蓝 | `#0066a2` | 部分海报 |
| 黑 | `#1a1a1a` | 大多数海报背景 |
| 米 / 浅黄 | `#f5e6c8` | 海报底色变体 |

**配色铁律：**
- **每张作品 1 主色 + 1 黑 + 1 中性**（米 / 白 / 浅灰）
- **绝不超过 3 色**
- 主色饱和度极高（不用莫兰迪 / 不用渐变）

### 字体
- **海报**：粗 sans serif（Akzidenz-Grotesk Bold / Helvetica Bold / 自定义粗体）
- **标题**：手绘字 / 剪贴字（Web 替代：League Gothic + 手绘 SVG 描边）
- **数字 / 字幕**：Bell Gothic / Trade Gothic 等几何 sans

---

## 4. 视觉禁忌

1. ❌ **信息平铺** —— 每个信息平等 = 没有焦点。必须有**一个核心 shape**
2. ❌ **Ornament（装饰）** —— 不画花边、不加装饰、不用渐变
3. ❌ **"看完就忘"的设计** —— 必须有记忆点，看一眼记三十年
4. ❌ **多焦点** —— 一张作品只能有一个视觉钩子
5. ❌ **柔和过渡** —— 撞色 / 硬边，不要 fade
6. ❌ **数字精确** —— 反 Swiss 完美几何，保留手工不规则
7. ❌ **过度饱满** —— 留白必须存在，重心偏侧
8. ❌ **居中对齐** —— Bass 几乎从不居中

---

## 5. 局限性

### 不适用场景
- **数据密集** —— 一个 shape 装不下表格
- **多概念并列** —— 必须选一个"最具代表性的"，无法平等呈现多个观点
- **多页 deck 易疲劳** —— 同样的"几何剪影 + 撞色块"做 30 页会单调
- **静态海报美学转 PPT** —— Bass 是为"一张图"设计的，转动态/多页有挑战
- **中文场景** —— 剪影 + 中文方块字难配合（拉丁字母可作图形，方块字"图形化"难度大）

### 中文降级建议
- 中文标题用粗黑体（思源黑 Heavy / 得意黑），把单字当几何形态
- 几何 shape 保留，但配文用极简中文（≤ 8 字标题）
- 强调"撞色块 + 剪影"，弱化"字体作为图形"
- **适合中文 PPT 的封面 / 章节扉 / 转场页，不适合正文页**

---

## 6. 经典作品

### 电影海报
- *The Man with the Golden Arm* (1955) —— 不规则黑手臂剪影 + 朱红
- *Anatomy of a Murder* (1959) —— 红色尸体被切几段 + 黑底
- *Vertigo* (1958) —— 螺旋线 + 红黄
- *Bunny Lake is Missing* (1965)
- *The Shining* (1980)

### 电影片头
- *North by Northwest* (1959) —— 绿底白线演变成摩天楼网格
- *Psycho* (1960) —— 横竖线条交错切割
- *Casino* (1995, Scorsese) —— 红黄火焰几何
- *Cape Fear* / *Goodfellas* / *The Age of Innocence*（Scorsese 后期合作）

### Logo
- AT&T (1969) —— 经典横条蓝色球（Bass 1983 重设计成简化版）
- United Airlines (1974) —— Tulip 形态
- Continental Airlines —— 地球网格简化
- Quaker Oats —— Quaker man 简化
- Bell System Logo Evolution —— 从 1889 到 1969 的精炼史

---

## 蒸馏到 PPT skill 的核心准则

1. **一页一形态** —— 每张 frame 只有一个核心几何 shape
2. **撞色块** —— 黑底 + 1 高饱和色 + 1 中性，硬边切割
3. **剪影优先** —— 主体用纯色剪影，不用照片细节
4. **撕纸感** —— SVG turbulence 给边缘加不规则
5. **字体作图** —— 标题用粗 sans 或手绘，参与构图
6. **重心偏侧** —— 不居中，留白偏向一边
7. **配色封顶 3 色**：朱红/橙黄/宝石蓝 + 黑 + 米，其一
8. **适用边界**：封面 / 章节扉 / 转场 / 重磅画面；不用于正文密集页

---

## 诚实声明

- ✅ 视觉哲学（MM-1 到 MM-4）和经典作品基于公开资料（Wikipedia / IMDb / Art of the Title）
- ⚠️ 精确字号 / hex 值是基于海报视觉判读的推断，**Bass 没有公开品牌色板**
- 🚫 Bass 与希区柯克具体合作细节、片头逐帧分析可能不完整（agent 调研超时失败）
- 📚 建议进一步参考：*Saul Bass: A Life in Film & Design* (Jennifer Bass + Pat Kirkham, 2011)

---

**调研日期：** 2026-05-21
**蒸馏方式：** 公开资料 + Claude 已有知识（agent 超时 fallback）
**建议后续：** 用户可触发 huashu-nuwa 重新蒸馏获得更深内容
