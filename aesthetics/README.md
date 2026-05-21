# aesthetics/ · 14 位视觉大师美学操作系统

> longtext-to-slides 内嵌的美学指导库。**与 ~/.claude/skills/ 下的独立 skill 内容相同**，但作为本 skill 自包含的一部分，**不依赖外部 skill 调用**。

## 加载方式

Phase 4.0 加载大师美学时，**优先读本目录下的文件**（相对路径），失败再 fall back 到独立 skill。

```python
aesthetic_path = f"aesthetics/{style_alias}.md"
# 例：aesthetics/carson.md
```

## 14 位大师索引

### 西方现代主义系（5 位）
| 文件 | 大师 | 核心 |
|---|---|---|
| [vignelli.md](vignelli.md) | Massimo Vignelli | 六字体足矣 · 黑白红 · 永恒论 |
| [tschichold.md](tschichold.md) | Jan Tschichold | 双模式：早期不对称 / 后期 Sabon 古典回归 |
| [crouwel.md](crouwel.md) | Wim Crouwel | 极致网格 Unit=8 / New Alphabet |
| [rams.md](rams.md) | Dieter Rams | "Less, but better" |
| [tufte.md](tufte.md) | Edward Tufte | 数据墨水比 / 反 PowerPoint |

### 解构 / 反叛系（3 位）
| 文件 | 大师 | 核心 |
|---|---|---|
| [carson.md](carson.md) | David Carson | 越界 / 错位 / Ray Gun |
| [brody.md](brody.md) | Neville Brody | The Face / 构成主义 / FUSE |
| [scher.md](scher.md) | Paula Scher | Make it Bigger / 字即是图 |

### 情绪 / 海报系（2 位）
| 文件 | 大师 | 核心 |
|---|---|---|
| [sagmeister.md](sagmeister.md) | Stefan Sagmeister | 身体作字 / Style=Fart |
| [bass.md](bass.md) | Saul Bass | 几何剪影 / 撞色块 |

### 东方留白系（2 位）
| 文件 | 大师 | 核心 |
|---|---|---|
| [hara.md](hara.md) | 原研哉 Kenya Hara | MUJI / Emptiness / 70-90% 留白 |
| [zhuyingchun.md](zhuyingchun.md) | 朱赢椿 | 慢 / 留白的东方 / 不动声色 |

### 东方密度系（2 位）
| 文件 | 大师 | 核心 |
|---|---|---|
| [eastern-book.md](eastern-book.md) | 杉浦康平 + 吕敬人 | 密度的东方 |
| [hanjiaying.md](hanjiaying.md) | 韩家英 | 汉字即图形 / 形式的东方 |

## 互斥关系（同页禁混）

- **Vignelli vs Carson** —— 网格 vs 解构
- **Rams vs Sagmeister** —— Less vs Emotion
- **Crouwel vs Brody** —— 1972 Fodor 辩论的两派
- **Hara vs Eastern-book** —— 留白派 vs 密度派的东方
- **Hara vs Zhuyingchun** —— MUJI 极简 vs 慢生长，两种留白哲学

混用规则：**封面一种 + 正文另一种** OK；**单页内只能一种**大师指导。

## 三种"中国风"分野

| 调用哪个 | 哲学 | 适合 |
|---|---|---|
| [eastern-book.md](eastern-book.md) | 密度的东方 | 正文章节页、详细说明、信息丰盈 |
| [hanjiaying.md](hanjiaying.md) | 形式的东方 | 单页海报、章节扉、引用页 |
| [zhuyingchun.md](zhuyingchun.md) | 留白的东方 | 文学诗、自然观察、内观随笔 |
