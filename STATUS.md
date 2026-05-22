# longtext-to-slides · 项目状态 & 交接档

> 这份文档是 **跨会话连续性档案**。新会话开始时先读它，能立刻接上 v0.2 的所有工作。
> 维护人：船长 · 协作者：Claude
> 最近会话：2026-05-22（v0.3 — 补完 11 个大师 demo + frame-4/5 全量审计修复 + README 分发优化）

---

## 一句话状态

**14 个大师 demo deck 全部完成。rams/hara/scher 为 18 帧全量版；其余 11 个为 5 帧精简样张（船长定的降级标准：够截图传 DNA 即可）。每个大师 3 张代表截图（cover/chapter/body），preview-data.json 14 个 demo_ready 全 true，preview.html 14 卡片全绿 READY、36 图 0 损坏。v0.3 续已对 11 个 deck 做 frame-4/5 全量审计、修复 bass/carson 共 4 处遮挡裁切 bug。M3 混搭引擎仍未启动。**

---

## v0.3 会话改动（2026-05-22）

### 做了什么

补完 STATUS.md P1 挂着的「剩余 11 个大师 demo」。船长定的降级标准：剩余 11 个**不用** rams/hara/scher 那样的 18 帧全量 + 标题三检 + 骨架卡，只需 **5 帧精简样张**，够截图传递大师 DNA 即可。

| 步骤 | 做法 |
|------|------|
| 生成 11 份 full.html | Agent Teams（team `demo-decks`）+ Tasks API 跟踪，3 批并行（5+5+1），每个 agent 逐行读 `aesthetics/<master>.md` 五层 DNA + 以 rams 为 HTML 骨架、CSS 完全按各自大师重写 |
| 5 帧统一结构 | frame-1 封面 / frame-2 章节扉 / frame-3 正文主体 / frame-4 正文或金句 / frame-5 终章 |
| 截图 | chrome-devtools 逐个 navigate + 设 1280×720 + 隐藏 .rail/.hotkey-hint + 截 frame-1/2/3 → cover/chapter/body.png |
| 更新 JSON | preview-data.json 11 个 demo_ready → true |

### 完成的 11 个大师

crouwel / vignelli / tufte（source-A 数据型）· tschichold / zhuyingchun / eastern-book / hanjiaying（source-C 东方型）· bass / sagmeister / carson / brody（source-B 演讲型）

### 验收中发现并修复的问题

- **bass body 帧**：`.body-frame` 米底 + 正文黑字，左侧盖黑色撕纸块 → 黑字压黑块隐形。修复：body-frame 改黑底 + 正文改米色（黑底米字双向可读）+ 红块改右侧全高粗条。
- **brody body 帧**：`.story .glyph-mark`（红 ● 26rem）设 `z-index:1`，story 帧正文元素未设 z-index → 定位元素压住普通流内容，红圆盖正文。修复：glyph z-index 改 -1 沉到底层。
- **carson body 帧**：DROPOUT 巨字压标题 = Carson「越界叠压」招牌特征，保留；底部 body-kicker 出血裁切问题已在 v0.3 续修复（见下）。
- **crouwel 封面**：巨字硬边几何偏移，初看像投影，核查无 `shadow` 属性，构成主义可接受，**保留**。

### 验收结果

11 个大师每个抽查 cover+body，全部体现各自 DNA（tufte sparkline+无竖线数据表 / crouwel 电网风+网格列 / vignelli 黑白红 / tschichold 古典对称衬线 / zhuyingchun 巨字大留白 / eastern-book 朱砂印密度 / hanjiaying 巨汉字海报 / bass 撞色撕纸 / sagmeister 手写便利贴 / carson 解构错位 / brody 红黑构成）。preview.html 经本地 HTTP 服务验证：14 卡片全 READY、36 图 0 损坏、0 PENDING。

---

## v0.3 续 · frame-4/5 全量审计 + README 分发优化（2026-05-22 同会话续）

### 触发
船长发现 bass 金句页（frame-4）黑色撕纸块遮挡文字。追根：11 个 demo 当初**只截 frame 1-3 就标 `demo_ready: true`**，frame-4/5 从没人看过。

### frame-4/5 全量审计（11 新 deck × 2 帧）
方法：CSS 代码审查（查绝对定位装饰块 / 高 z-index 元素压文字），可疑项再 chrome-devtools 截图复核。发现并修复 4 处遮挡/裁切 bug：

- **bass frame-4**：金句黑色撕纸块 `64%×78%` 压住「别浪费它」→ 缩到 `58%×46%` + 金句字色改米。
- **bass frame-5**：`.accent-red`（「若愚」）是纯 inline span，背景在 `line-height:0.92` 压紧行距下纵向漫到上一行盖住「求知若饥」→ 改 `display:inline-block`+`line-height:0.95` 收口，coda-headline 行高 0.92→1.0。
- **carson frame-5**：`.coda-thanks`（「虚心若愚。」）`bottom:-36px` 被底边裁掉约一半 → 改 `bottom:46px`。
- **carson frame-3**：`.body-kicker`（「凭好奇心撞上的东西…」）`bottom:-28px` 同款裁切 → 改 `bottom:30px`。

其余 9 个 deck（zhuyingchun/vignelli/sagmeister/eastern-book/tufte/hanjiaying/crouwel/tschichold + brody）frame-4/5 干净。全部修复已 chrome-devtools 截图验证。

### 重截 3 张过时缩略图
bass/carson/brody 的 `body.png`（=frame-3）是修 frame-3 之前截的 → 重截 + Pillow 裁剪缩放到 1922×1080（与同批一致）覆盖。

### README 分发优化
船长目标：外部用户「拉下来就能用、别太麻烦」。改 `README.md`：
- 安装拆「方式一手动 clone / 方式二让 AI 帮装」，Windows(PowerShell) + macOS/Linux 命令分别给全。
- 顶部强调：核心功能 clone 即用、不装任何 Python 包；仅本地 PDF/DOCX/EPUB 输入才需 `pip install`。
- 删除 `npx skills add`（无法确认该 CLI 真实可用，船长要求 100% 可靠）。
- 使用段补 Windows/macOS 双平台文件路径写法。

### 教训沉淀
**「只截 frame 1-3 就判 demo 做完」= 验收标准本身有缺陷。** bass/carson 共 4 个 bug 全在没截的 frame-4/5 里。与 CLAUDE.md「AI 自评 confirmation bias」同源 —— 抽查 ≠ 全验。后续补 demo 必须**逐帧**截图或审查。

### 仍待办
- 确认 GitHub 仓库 `xxximcoolguy/long2ppt` 是否已 push 且 public（没 push 则 README 所有安装方式对外失效）。

---

## 本次会话改动总览（v0.2）

### 触发的根本问题

- 船长想把 skill 从「私人工具」打磨成「能分享给小白用户的真好用工具」
- 私董会会议（7 位顾问 + 2 场交锋）核心结论：
  1. 风格选择当前是失败的——14 大师名字对小白零信息量
  2. 不能正面跟 Gamma 拼「AI 生成 PPT 更快」
  3. 14 大师是潜在差异化资产，但用户感知不到
  4. 最大风险是分发不是产品（Munger 灾难清单第六条）
- 拍板路径：**毛选「分阶段融合」**——新手层场景化推荐 + 进阶层浏览器预览页 + 未来 M3 混搭引擎

### 实际落地的功能

| Milestone | 状态 | 产出 |
|-----------|------|------|
| **M1 场景过滤** | ✅ | SKILL.md Phase 3 加 Q0 模式分流 + Q1 快速/进阶分支 / routing.md 加场景→大师推荐表 + 一句话理由库 + 中国风互斥提示 / presets.md 加 scenes + master 索引 |
| **M2.1 三份 demo 范文** | ✅ | `demo-decks/source-A.md` AI 编辑器市场报告 2400 字（数据型）/ `source-B.md` 乔布斯演讲精华中英对照（叙事型）/ `source-C.md` 茶之书节选中英对照（东方型） |
| **M2.2 截图脚本** | ✅ | `scripts/generate_demos.py`（需 playwright）·`--check` `--master` `--all` 三模式 |
| **M2.3 大师元数据** | ✅ | `templates/preview-data.json` · 14 大师 + 4 场景 + 推荐路由 + 互斥规则 + demo_ready 标记 |
| **M2.4 预览页** | ✅ | `templates/preview.html` 单文件零依赖，中文优雅排版，卡片墙 + 场景过滤 + 混搭占位 |
| **M2.5 本地服务** | ✅ | `scripts/style_preview.py` Python 标准库零依赖，随机端口、超时 fallback、跨平台 |
| **M2.6 SKILL.md 接入** | ✅ | Phase 3 Q1 进阶模式调用 style_preview.py + 退出码分支 + fallback 路径 + 支持文件索引 |
| **M2.7a Rams demo** | ✅ | `demo-decks/rams/full.html` 18 张 deck + `cover.png` `chapter.png` `body.png` 三张代表截图 |
| **M2.8 体验降级** | ✅ | preview-data.json 加 demo_ready 字段 / preview.html 添加 READY/PENDING 角标 + 友好「📷 预览待生成」占位 + 看大图按钮 disabled 防 404 |
| **M2.7b Hara demo** | ✅ | `demo-decks/hara/full.html` 18 张 deck · 茶之书节选 · 「一只茶杯盛人间」+ 3 张代表截图（封面/章节扉/Sukiya 三义）+ preview-data.json demo_ready=true |
| **M2.9 卡片缩略图修复** | ✅ | preview.html 卡片缩略图改 cover 单图 + object-fit:contain（原 2fr/1fr/1fr + cover 把大留白裁成空白条）/ 加 hover 浮窗大图（脱离卡片裁切框、scale 1.9、阴影、center origin）/ 最左最右卡片浮窗会略溢出屏幕，留给后期 UX 优化 |
| **M2.7c Scher demo** | ✅ | `demo-decks/scher/full.html` 18 张 deck · 乔布斯演讲 · 主标「Stay Hungry Stay Foolish」+ 3 张代表截图（4 单词撞色封面 / 黑黄章节扉 / 红黑「信」单字撞色）+ preview-data.json demo_ready=true |
| **M2.7 其他 11 个大师 demo** | ✅ | 2026-05-22 完成（v0.3）· Agent Teams 并行生成 5 帧精简版 + chrome-devtools 截图，详见上方「v0.3 会话改动」 |
| **M3 混搭引擎** | ⏳ pending | 设计层规划已定，实现未启动 |

### 改动/新增的文件清单

```
SKILL.md                          [大改] · Phase 2.0/2.05/2.1/2.2 + Phase 3 Q0/Q1 + 决策铁律 + 文件索引
routing.md                        [大改] · 顶部新增场景→大师路由表 + 一句话理由库 + 中国风互斥
presets.md                        [改]   · 顶部新增 scenes + master 索引 + 已知缺口/Bug 标注
layouts.md                        [改]   · 索引后新增字数预算表
templates/preview.html            [新]   · ~600 行 HTML+CSS+JS
templates/preview-data.json       [新]   · 14 大师 metadata
scripts/style_preview.py          [新]   · Python HTTP server
scripts/generate_demos.py         [新]   · Playwright 批量截图
demo-decks/source-A.md            [新]   · 范文 A 数据型
demo-decks/source-B.md            [新]   · 范文 B 演讲型
demo-decks/source-C.md            [新]   · 范文 C 东方型
demo-decks/README.md              [新]   · 工作流说明 + 大师×范文映射
demo-decks/rams/full.html         [新]   · Rams demo deck（验证标杆）
demo-decks/rams/cover.png         [新]   · Rams 封面代表截图
demo-decks/rams/chapter.png       [新]   · Rams 章节扉代表截图
demo-decks/rams/body.png          [新]   · Rams 数据网格代表截图
STATUS.md                         [新]   · 本档案
```

---

## 当前可用能力

### 快速模式（小白路径）

```
1. 进入 Phase 3 Q0 → AskUserQuestion 问「快速 / 进阶」
2. 快速 → Q1a 问场景（工作汇报 / 读书笔记 / 朋友圈 / 演讲）
3. 后台查 routing.md 场景→大师推荐表 → 推主推大师
4. 输出「AI 推荐：『一句话理由』，要试试这个吗？」
   绝不暴露大师名字（如 "Rams" "Carson" "Brody"）
5. 用户「换一个」→ 给次推；连续 3 次换 → 转进阶
6. 读书笔记 + Hara → 自动追问东方派别（hara/zhuyingchun/eastern-book/hanjiaying）
7. 数据 > 30% → 强制 Tufte
```

### 进阶模式（HTML 预览页）

```bash
cd ~/.claude/skills/longtext-to-slides
python scripts/style_preview.py \
    --output /tmp/style_config.json \
    --title "你的文档标题" \
    --words 2500 \
    --scene business
# 浏览器自动打开预览页 → 用户选 → JSON 写入 → 退出
```

预览页能：
- 4 个场景卡片过滤候选
- 主推卡片红色徽章
- 每张卡显示一句话理由 + vibe tags
- **demo_ready=true** 卡片：3 张缩略图 + 绿色 ● READY + 看大图可点
- **demo_ready=false** 卡片：📷 预览待生成占位 + 灰色 ○ PENDING + 看大图 disabled
- 折叠展开「全部 14 个大师」
- M3 混搭输入框（disabled 占位）

### 完整一次跑通的样板（Rams）

```bash
# 看 Rams demo
start ~/.claude/skills/longtext-to-slides/demo-decks/rams/full.html

# 启预览页（rams 卡片显示真实缩略图）
python ~/.claude/skills/longtext-to-slides/scripts/style_preview.py \
    --output /tmp/x.json \
    --title "测试" --words 2500
```

---

## 待办优先级

### P0 · 立刻该做（让 preview.html 实用）

- [x] **跑 hara demo**（2026-05-21 完成）
  - ✅ 标题三检 + 骨架卡走完，主标定「一只茶杯盛人间」（命中 3/3）
  - ✅ 完整覆盖 layouts.md 默认装饰：暖白 #fafaf7 / 反 Bold / 反分隔线 / 留白 70%+ / 字号克制（display ≤ 2.6rem）/ 唯一点缀茶釉青绿 #5a6f6a
  - ✅ 截图三帧（封面 / PART 01 章节扉 / Sukiya 三义 trinity）
  - ✅ preview-data.json hara.demo_ready = true

- [x] **修 preview.html 卡片缩略图**（2026-05-21 完成）
  - 问题：原 `2fr 1fr 1fr` 三列拼图 + `object-fit:cover` 把 Hara 大留白裁成空白条，Rams 数字网格也只剩残片
  - 修：缩略图改 cover 单图 + `object-fit:contain` 完整等比；hover 时弹出 1.9x 浮窗大图脱离卡片裁切框
  - 遗留：最左/最右卡片浮窗 origin: center 会略溢出屏幕，船长 OK 留给后期 UX 优化

- [x] **跑 scher demo**（2026-05-21 完成）
  - ✅ 主标定「Stay Hungry Stay Foolish」（命中 3/3）
  - ✅ 全套 Scher DNA：4 色块封面（亮黄/黑/红/奶白）+ Bowlby One/Oswald Condensed 巨字 + 黑黄章节扉撞色 + 单字「信」红底奶白撞色（Type is Image）
  - ✅ 截图三帧（4 单词封面 / CONNECTING THE DOTS 章节扉 / 信 单字撞色）
  - ✅ preview-data.json scher.demo_ready = true

### P1 · 短期（让产品立得住）

- [x] **剩余 11 个大师 demo**（2026-05-22 完成）：crouwel / vignelli / tufte / tschichold / zhuyingchun / eastern-book / hanjiaying / bass / sagmeister / carson / brody — 全部 5 帧精简版 + 3 截图，preview.html 已验收
- [ ] **找 3-5 个真实小白用户测试 M1+M2**（PG 的核心建议）
  - 让他们走完一遍快速模式 → 看 Q0 模式分流是否被理解
  - 让他们看预览页 → 看缩略图能否传递大师 DNA
- [ ] **分发问题方案**（Munger 灾难清单第六条）
  - 怎么让目标用户搜到这个 skill？
  - 当前是 Claude Code 自带生态，外部用户搜不到

### P2 · 长期（建立护城河）

- [ ] **M3 混搭引擎**
  - 写 `mix-engine.md` 定义混搭语法（base + accent + modifier）
  - 写 `examples/mix-cases.md` 5-10 个示例混搭（few-shot）
  - 在 preview.html 启用混搭输入框（M2 占位）
  - 进阶用户可以输入「冷静但有点叛逆」→ LLM 解析 → Crouwel × Brody 混搭参数 → 生成专属命名 deck
- [ ] **审美身份护城河**（Buffett 建议）
  - 用户每次混搭存到 `~/.longtext-to-slides/my-variants.json`
  - 下次预览页顶部显示「我的风格库」
  - 支持 `.style-card` 文件导出/导入分享
- [ ] **补 5 套缺口预设**（presets.md 已标注）
  - sagmeister 缺手作笔记本预设
  - bass 缺几何切片预设
  - crouwel 缺 Stedelijk 工业预设
  - tufte 缺数据报告预设（M2 优先级最高！）
  - 现有 presets.md 第 14 号编号重复需修复
- [ ] **重新定位为「设计教育型工具」**（Naval 建议）
  - 每个大师做一个 90 秒展示页 / 代表作叙事
  - 让用户在选风格前先看到大师 DNA 的 hero 故事

---

## 操作指南

### 给新大师补 demo（人工 + chrome-devtools 协作流程）

**Step 1：写 full.html**

在 Claude Code 里：

```
我要用 longtext-to-slides 给 <master_name> 大师生成 demo deck。
- 源文件：~/.claude/skills/longtext-to-slides/demo-decks/source-<A|B|C>.md
  （按 demo-decks/README.md 的大师×范文映射查 A/B/C）
- 风格：进阶模式 · 我要 <master_name> 风
- 详略：18 张主线版
- 输出到：~/.claude/skills/longtext-to-slides/demo-decks/<master_name>/full.html

跑完整 Phase 2-4 流程：
- Phase 2.0 标题三检（命中 ≥2 才提交）
- Phase 2.05 骨架卡（核心主张 + 3-5 论点）
- Phase 2.1 字数预算自检 + 金句五诊
- Phase 4 完整读取 aesthetics/<master_name>.md + deck.css + deck.js + layouts.md + 对应预设
- 关键：layouts.md 的默认 CSS 装饰要按大师视觉禁忌覆盖（如 Rams 反渐变 / Hara 反阴影 / Tufte 反色块）
```

**Step 2：截图 3 张代表帧**

```bash
# 用 chrome-devtools MCP 启动并截图（不需要 playwright！）
# 1. navigate file://path/full.html
# 2. evaluate_script: 隐藏 .rail / .hotkey-hint，等 1500ms 字体就位
# 3. take_screenshot to %TEMP%/<master>_cover.png  （封面，frame-1）
# 4. evaluate_script: location.hash = '#frame-3'  （PART 01 章节扉）
#    wait 1300ms
# 5. take_screenshot to %TEMP%/<master>_chapter.png
# 6. evaluate_script: location.hash = '#frame-4'  （atlas/preface 第一个正文）
#    wait 1300ms
# 7. take_screenshot to %TEMP%/<master>_body.png
# 8. Bash copy %TEMP%/<master>_*.png 到 demo-decks/<master>/
```

**Step 3：preview-data.json 把对应 demo_ready 改 true**

```json
"name": "<master_name>",
...
"demo_ready": true,   // 从 false 改成 true
```

**Step 4：验证**

```bash
python scripts/style_preview.py --output /tmp/x.json --title "验证" --words 2500
```

打开预览页，找该大师卡片，应该：
- 右上角 `● READY` 绿章
- 三张真实缩略图
- 「看大图」可点击

### 改 SKILL.md / 改预设要注意

- **铁律**：Phase 3 Q0 模式分流是入口，没经过 Q0 直接跳 Q1 = 违规重写
- **铁律**：快速模式下不能暴露大师名字（"Rams" "Brody" 等术语对小白零信息量）
- **铁律**：禁止用 AskUserQuestion 列 15 个预设让小白选（回到盲选老路）

详见 SKILL.md「决策铁律」段落。

---

## 已知问题/坑

### 1. preset.md 编号 bug

第 14 号预设编号重复（解构 Anti-grid 和 网格主义 Gridism）。M2 阶段先用 14a/14b 内部区分，**M3 修复时**重新编号为 14/15，并把现有 15（黑潮）改为 16。

### 2. chrome-devtools 截图超时

第一次 `take_screenshot` 经常 timeout，**第二次重试就能成功**。这是 MCP 工具的已知小毛病，不影响功能。

### 3. style_preview.py timeout 退出码 1

服务超过 `--timeout` 秒没收到用户选择 → 退出码 1。在脚本日志里显示 "exit code 1 failed" 但**这是预期 fallback 行为**，不是 bug。SKILL.md Phase 3 Q1 进阶模式分支已经处理：退出码 1 = fallback 回文字预设选。

### 4. Windows GBK 终端编码 —— style_preview.py 崩溃 bug ✅ 已修复（2026-05-22 v0.3 续）

**原判断是错的**（曾写「只影响调试可读性，功能正常」）。实情：`style_preview.py` 收到用户选择、写完 JSON 后 `print('✓ ...')`，`✓`(U+2713) 无法被 Windows GBK 终端编码 → `UnicodeEncodeError` → 脚本崩溃、退出码 1 → SKILL.md 旧逻辑把 exit 1 误判为「用户取消」→ 丢掉用户已经选好的风格。**等于进阶模式在 Windows 上整个是坏的。**

**修复**：
- `style_preview.py` 开头强制 `sys.stdout/stderr.reconfigure(encoding='utf-8')`，并把 `✓`/`⏱️` 换成 ASCII（双保险）。
- SKILL.md Phase 3 Q1 退出码逻辑改为「优先看 style_config.json 是否生成，不只信退出码」。
- 教训：「只影响可读性、功能正常」这种乐观判断必须实跑验证，不能拍脑袋写进 STATUS。

### 5. demo-decks/<master>/full.html 体积

每份 demo deck HTML 约 40KB（CSS + 18 frame + JS 内联）。14 份 demo 总 ~600KB；加上 42 张 PNG（每张 ~150KB）总 ~7MB。**可接受**，必要时 PNG 压成 WebP 降到 < 1MB。

### 6. Rams demo 还差 layouts.md 渐变文字效果覆盖

当前 Rams demo 已经在内联 CSS 里覆盖了部分 layouts 默认装饰（chapter-title 移除 linear-gradient），但 `.coda-headline` 还有渐变文字。**不影响 Rams 看起来「克制」的判断**，但严格说违反 Rams 反装饰原则。优先级：低。

---

## 关键决策档案（私董会通过的）

### 风格选择从「列大师让用户挑」改成「场景化推荐」

**通过**：南添 + Jobs + PG + 毛选
**反对**：Naval（认为应该让大师走到前台）
**调和**：毛选「分阶段融合」—— 新手层场景化，进阶层（用过 3+ 次或显式选择）才看到全部 14 大师

### 14 大师是潜在护城河，但当前用户感知不到

**通过**：全员同意
**Naval 加注**：14 大师不是 14 个固定选择，是 14 个**设计语言原子**，可以组合出 N! 种变体。M3 混搭引擎是真正的护城河。

### 接下来 4 周该做什么？产品 vs 分发

**PG**：先观察 5 个真实小白用户使用
**Munger**：最大风险是分发，做再好用户搜不到也是死
**南添调和**：PG 的 5 用户观察不需要 4 周，2 天就够；改完立刻小范围发，看数据再决定下一轮

**结论**：当前已经完成产品骨架（M1 + M2 大部分）。**下一步是 P1.2 找真实用户测试**，不是继续加功能。

### Demo 范文用 3 份不同（不是 1 份通用）

**理由**：每个大师在最适合它的内容上发挥，预览图传递的是「大师 DNA 的最佳状态」不是平均效果
- A 数据型：Rams / Crouwel / Vignelli / Tufte
- B 演讲型：Sagmeister / Bass / Carson / Brody / Scher
- C 东方型：Hara / Zhuyingchun / Eastern-book / Hanjiaying / Tschichold

---

## 下次会话「冷启动」推荐流程

如果你（或新会话的 Claude）打开这份 STATUS.md 想接着干：

1. **先读这份 STATUS.md 整篇**
2. **核对当前状态**：
   ```bash
   ls ~/.claude/skills/longtext-to-slides/demo-decks/
   # 看哪些大师有 full.html / cover.png
   ```
3. **14 个大师 demo 已全部完成**，无需再补。若某个大师效果想重做，按上方「重新生成单个大师」流程（demo-decks/README.md）
4. **如果是改 preview.html / SKILL.md**：先用 `python scripts/style_preview.py --output /tmp/x.json --title 测试 --words 2500` 跑一遍当前体验找问题
5. **如果是做 M3 混搭引擎**：先写 `mix-engine.md` 设计文档，得到船长拍板再动手

---

**这份 STATUS.md 由本会话生成。下次会话开始时如果有新进展，请追加更新到「本次会话改动」表格，把已完成项移到「关键决策档案」做归档。**
