# 风格 → 视觉大师美学路由

> Phase 3 用户选定风格后，Phase 4 生成前**完整读取**对应大师 `aesthetics/<name>.md` 文件。
> **本 skill 自包含 —— 不依赖任何外部 skill。**

---

## 场景 → 大师推荐路由（Phase 3 Q1 快速模式必查）

> 用户在快速模式选定场景后，按本表推荐 **1 个主推大师 + 一句话理由**。
> 用户说"换一个看看" → 给次推；再换 → 给备选；再换 → 提示进入进阶模式自选。
> **小白用户绝不暴露大师名字，只暴露"一句话理由+预览效果"。**

| 场景 | 主推（首选） | 次推 | 备选 | 不推荐 |
|------|-------------|------|------|--------|
| 🏢 工作汇报 | **Rams** 克制专业 | Crouwel / Vignelli | Tufte（含数据时） | Carson / Brody / Scher |
| 📖 读书笔记 | **Hara** 侘寂留白 | Tschichold / Zhuyingchun | Eastern-book / Rams | Scher / Brody |
| 📱 朋友圈分享 | **Scher** 视觉冲击 | Bass / Hanjiaying | Carson / Brody | Tufte / Crouwel |
| 🎤 演讲 Keynote | **Sagmeister** 手工大字 | Bass / Scher | Hanjiaying / Hara | Tufte / Crouwel |

### 一句话理由库（推荐时附带，不要说大师名字给小白用户）

| 大师 | 给小白用户看的"一句话" |
|------|---------------------|
| Rams | 「中性专业、不会丢人 — 适合需要可信感的汇报」 |
| Crouwel | 「极致网格、数字电网风 — 工业理性气质」 |
| Vignelli | 「黑白红配色 + 出版物网格 — 经典权威感」 |
| Tufte | 「数据墨水比 — 财报/学术/数据密集型专属」 |
| Tschichold | 「新排版 + 古典 Sabon — 文学的优雅书卷气」 |
| Hara | 「侘寂留白、暖白宋体 — 读书的沉静感」 |
| Zhuyingchun | 「慢设计、宋体大字夸张 — 自然观察的禅意」 |
| Eastern-book | 「朱砂方印 + 宣纸纹理 — 国学密度东方」 |
| Hanjiaying | 「汉字独占画面 — 当代中国海报感」 |
| Scher | 「字即图像、强烈视觉冲击 — 让人一眼记住」 |
| Bass | 「几何剪影 + 海报感 — 章节扉视觉重锤」 |
| Sagmeister | 「手写大字 + 物质媒介 — TED 演讲的情感感」 |
| Carson | 「越界错位、解构破碎 — 反规则的创意感」 |
| Brody | 「红黑构成 + 80s 实验 — 亚文化政治感」 |

### 中国风互斥提示

当用户选「读书笔记」且未明确东方倾向时，**主动追问偏哪一种**（一次 AskUserQuestion，不展示大师名字）：

| 选项 | 加载哪个 |
|------|---------|
| A 留白 · 暖白宋体 · 茶道感 | `aesthetics/hara.md` |
| B 禅意 · 慢生长 · 自然观察 | `aesthetics/zhuyingchun.md` |
| C 国学 · 宣纸朱砂 · 信息密度 | `aesthetics/eastern-book.md` |
| D 海报 · 汉字独占 · 现代张力 | `aesthetics/hanjiaying.md`（不推荐用于长读书笔记）|

### fallback 与覆盖规则

- 用户无法判断场景 → **默认推 Rams**（最稳，跨场景容错最高）
- 用户原文含 > 30% 数据/表格/图表 → **强制覆盖推 Tufte**（不论场景）
- 用户明确说"我要 X 风格" → 跳过本表，进入进阶模式（M2 预览页 / 当前仍走 15 预设）
- 用户连续 3 次说"换一个" → 提示「要不要进入进阶模式自己挑？」

---

## 路由表（14 位大师 · 进阶模式 / Phase 4 加载用）

| 用户选定的风格 / 场景 | 加载文件 | 关键启发 |
|---|---|---|
| **解构** / Carson 风 | `aesthetics/carson.md` | 越界 / 错位 / 重叠 / 撕裂 / 字号 ≥ 20:1 |
| **网格主义** Gridism | `aesthetics/vignelli.md` | 6 字体足矣 + 严格 grid + 黑白红 |
| **现代主义起源** / 新排版 / Penguin 风 | `aesthetics/tschichold.md` | 双模式：early 不对称 / late Sabon 古典 |
| **极致网格** / Stedelijk 风 / 工业 | `aesthetics/crouwel.md` | Unit=8 / 数字电网 / New Alphabet |
| **黑潮** / 营销 / 社媒爆款 | `aesthetics/scher.md` | 字即图像 / 字号 ≥ 6:1 / 颜色分块 |
| **The Face 风** / 80s 实验 / 政治议题 | `aesthetics/brody.md` | 红黑构成主义 / 巨型符号 / 拉宽字距 |
| **手工感** / TED / 个人叙事 / 文化 | `aesthetics/sagmeister.md` | 手写大字 / 物质媒介作字 / Style=Fart |
| **海报感** / 几何剪影 / 章节扉视觉冲击 | `aesthetics/bass.md` | 撞色块 / 一页一形态 / 撕纸感 |
| **水墨留白** / **侘寂** / **青瓷釉色** | `aesthetics/hara.md` | Emptiness 70-90% / 暖白绝非纯白 / 偏左下 |
| **慢设计** / 留白东方 / 禅意 / 自然观察 | `aesthetics/zhuyingchun.md` | 60-80% 留白 / 宋体 / 字号 2-3 级夸张 |
| **宣纸古卷** / **碑刻金石** / **故宫赤红** | `aesthetics/eastern-book.md` | 朱砂方印 / 宣纸纹理 / 直排+横排 |
| **汉字即图形** / 当代中国海报 / 文人调 | `aesthetics/hanjiaying.md` | 汉字独占 50-80% / 朱砂1枚 / 大留白 |
| 数据 / 图表 / 财报 / 学术 | `aesthetics/tufte.md` | Data-Ink Ratio / 删 chartjunk |
| **磷火显像** / **雾凇** / **电流** / 克制 | `aesthetics/rams.md` | 4 级字号 / 12 列网格 / 留白≥35% |

## 执行规则

1. 用户选定风格后，**立刻** 完整读取对应 `aesthetics/<name>.md`
2. 把 5 层框架全部带入生成上下文：视觉哲学 / 版式手法 / 颜色字体 / 视觉禁忌 / 局限
3. **凡是违反大师禁忌的写法，重做**
4. 大师文件中"中文场景特别说明"部分，必须按其降级建议处理
5. 大师互斥提示（如 hara vs zhuyingchun vs eastern-book 三种"中国风"），用户没明确时**主动询问**

## 三种"中国风"分野（必读）

| 调用哪个 | 哲学 | 适合 |
|---|---|---|
| `aesthetics/eastern-book.md`（杉浦+吕敬人）| **密度的东方** | 正文章节页、详细说明、信息丰盈 |
| `aesthetics/hanjiaying.md` | **形式的东方** | 单页海报、章节扉、引用页 |
| `aesthetics/zhuyingchun.md` | **留白的东方** | 文学诗、自然观察、内观随笔 |

## 大师互斥关系（同页禁混）

- **Vignelli vs Carson**：网格 vs 解构。不能同页混用
- **Rams vs Sagmeister**：Less but better vs Emotion。不能同页混用
- **Crouwel vs Brody**：1972 Fodor 辩论的两派对立。不能同页混用
- **Hara vs Eastern-book**：留白派 vs 密度派的东方。用户必须二选一
- **Hara vs Zhuyingchun**：MUJI 极简 vs 慢生长，两种留白哲学。需问用户

混用规则：可以**封面一种 + 正文另一种**，但**单页内只能一种**大师指导。

## fallback 策略

若 `aesthetics/<name>.md` 不存在（不应发生 —— 14 位齐全），fall back 到 `presets.md` 的风格描述。
