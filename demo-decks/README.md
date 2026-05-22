# demo-decks/ · 14 大师风格预览资料

本目录存放：
- `source-A.md` / `source-B.md` / `source-C.md` — 三份预生成 demo 范文
- `<master>/full.html` — 每位大师用对应范文跑出的完整 deck（**M2.7 后人工生成**）
- `<master>/cover.png` `chapter.png` `body.png` — 三张代表截图（**自动生成**，见 `../scripts/generate_demos.py`）

---

## 大师 × 范文映射表

每位大师都有最适合发挥它 DNA 的内容类型，对号入座，避免"用书法风跑财报"这种低效错配：

| 大师 | 用哪份 source | 为什么 |
|------|--------------|--------|
| rams | source-A | 中性专业，数据/技术内容能体现"克制美" |
| crouwel | source-A | 极致网格，工业数据最契合 |
| vignelli | source-A | 出版物网格 + 数据，黑白红配色凸显结构 |
| tufte | source-A | 数据墨水比，必须配数据型内容 |
| tschichold | source-C | 古典 Sabon 派最适合文学/思想性长文 |
| hara | source-C | 茶道哲学契合侘寂留白 |
| zhuyingchun | source-C | 茶之书的禅意适配慢设计 |
| eastern-book | source-C | 东方哲学正好用宣纸朱砂 |
| hanjiaying | source-C | 茶字汉字本身可作画面主体 |
| scher | source-B | 演讲金句适合"字即图像" |
| bass | source-B | 三段叙事配几何剪影海报感 |
| sagmeister | source-B | 个人故事配手作大字 TED 风 |
| carson | source-B | 演讲情绪起伏适合解构错位 |
| brody | source-B | "Stay Hungry"金句配红黑构成 |

---

## 工作流（M2.7 执行）

### STEP 1 · 人工生成 14 份 full.html（每个大师跑一次）

在 Claude Code 里：

```
我要用 longtext-to-slides 生成一份 demo deck。
- 源文件：~/.claude/skills/longtext-to-slides/demo-decks/source-A.md
- 风格：进阶模式 · 我要 rams 风
- 详略：18 张主线版
- 输出：~/.claude/skills/longtext-to-slides/demo-decks/rams/full.html
```

重复 14 次，每次换大师 + 对应 source（按上表）。

> **小技巧**：可以让 Claude 一次会话连续跑，把"再来一个 X 大师，源文件还是 X"作为后续提示。

### STEP 2 · 脚本批量截图

```bash
cd ~/.claude/skills/longtext-to-slides
python scripts/generate_demos.py --check       # 看缺哪几个
python scripts/generate_demos.py --all          # 一次截 14 大师 × 3 张
```

依赖：
```bash
pip install playwright
playwright install chromium
```

### STEP 3 · 验收

打开 `templates/preview.html`（直接双击，或用 `scripts/style_preview.py` 启动）：

```bash
python scripts/style_preview.py --output /tmp/test.json --title "验收" --words 2500
```

逐个大师卡片看 3 张截图：能不能传递大师 DNA？看起来怪/丑/平的 → 回到 STEP 1 重新生成 HTML。

---

## 已知问题与对策

| 问题 | 现象 | 对策 |
|------|------|------|
| 字体未加载完成 | 截图出现 fallback 字体 | `generate_demos.py` 已有 2s wait，必要时改 3s |
| 章节扉 frame 找不到 | 某些大师 deck 没有 `.chapter-plate` | 脚本自动 fallback 用当前帧 |
| 翻页过快字体闪烁 | 翻页 350ms 太短 | 调脚本里 `wait_for_timeout` 数值 |
| Chinese mutex 大师只选 1 个 | hara/zhuyingchun/eastern-book/hanjiaying 都做完了 | 全部做完，预览页根据用户选项展示 |

---

## 重新生成单个大师

某个大师效果不满意：

```bash
# 删掉旧的
rm demo-decks/rams/*.png demo-decks/rams/full.html

# 重新跑 Claude 生成 HTML（人工）
# ...

# 重新截图
python scripts/generate_demos.py --master rams
```
