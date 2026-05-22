#!/usr/bin/env python3
"""
generate_demos.py · 批量截图 14 大师 demo deck 的三张代表帧

这是 **M2 一次性辅助脚本**，用于把已经生成好的 demo HTML 批量截图。

────────────── 完整 demo-decks 生成工作流（人工 + 脚本协作）──────────────

  STEP 1 · 人工：用 longtext-to-slides skill 在 Claude Code 里跑 14 次

    对每个大师跑一次：
      - 用 demo-decks/source-A/B/C.md 之一作为输入（按大师类型分配，见
        preview-data.json 的 source_file 字段）
      - 进阶模式直接说"我要 <master_name> 风"
      - 生成完整 HTML
      - 把 HTML 重命名为 full.html
      - 移到 demo-decks/<master_name>/full.html

  STEP 2 · 脚本：本脚本批量截图

    python scripts/generate_demos.py --all

    会遍历每个 demo-decks/<master>/full.html：
      - Playwright headless Chromium 加载
      - 等 2s 让字体 + 动画就位
      - 截图当前 frame（封面） → cover.png
      - 翻页找到 .chapter-plate 类型 frame → chapter.png
      - 翻页找到 .preface/.atlas/.specimens 类型 frame → body.png

  STEP 3 · 验收：人工在 templates/preview.html 检查

    打开 templates/preview.html，确认每个大师的三张截图能传递 DNA
    不行的大师 → 回到 STEP 1 重新生成 HTML

────────────── 依赖 ──────────────

  pip install playwright
  playwright install chromium

────────────── usage ──────────────

  # 单个大师
  python scripts/generate_demos.py --master rams

  # 全部 14 个
  python scripts/generate_demos.py --all

  # 列出当前缺失 full.html 的大师
  python scripts/generate_demos.py --check

────────────── exit codes ──────────────
  0  全部成功
  1  部分失败（仍有截图未生成）
  2  环境问题（缺依赖 / 路径错）
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path


# ============ DEPENDENCY CHECK ============

def check_playwright():
    try:
        import playwright  # noqa: F401
        return True
    except ImportError:
        print('ERROR: playwright 未安装', file=sys.stderr)
        print('  pip install playwright', file=sys.stderr)
        print('  playwright install chromium', file=sys.stderr)
        return False


def resolve_skill_root():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, '..'))


def load_master_list(skill_root):
    path = os.path.join(skill_root, 'templates', 'preview-data.json')
    with open(path, encoding='utf-8') as f:
        return json.load(f)


# ============ CAPTURE ============

BODY_FRAME_CLASSES = ['preface', 'atlas', 'specimens', 'phases', 'dialog', 'steps', 'tenets']


async def capture_frame(deck_handle, out_path):
    """截图当前 active frame 的 .deck 区域（1280x720）"""
    await deck_handle.screenshot(path=str(out_path))


async def find_frame_by_classes(page, class_list, max_tries=10):
    """从当前 active frame 出发，向右翻页直到找到匹配某个 class 的 frame。"""
    for _ in range(max_tries):
        matched = await page.evaluate(
            '''(classes) => {
                const active = document.querySelector('.frame[data-state="active"]');
                if (!active) return false;
                return classes.some(c => active.classList.contains(c));
            }''',
            class_list,
        )
        if matched:
            return True
        await page.keyboard.press('ArrowRight')
        await page.wait_for_timeout(350)
    return False


async def capture_master(master_name, skill_root, viewport_scale=2):
    from playwright.async_api import async_playwright

    deck_dir = Path(skill_root) / 'demo-decks' / master_name
    html_path = deck_dir / 'full.html'

    if not html_path.is_file():
        print(f'  SKIP {master_name}: full.html not found')
        return False

    deck_dir.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            ctx = await browser.new_context(
                viewport={'width': 1280, 'height': 720},
                device_scale_factor=viewport_scale,
            )
            page = await ctx.new_page()
            await page.goto(html_path.as_uri())
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(2000)  # 字体 + 动画

            deck = await page.query_selector('.deck')
            if not deck:
                print(f'  FAIL {master_name}: .deck not found in HTML')
                return False

            # 1. 封面（默认 active）
            await capture_frame(deck, deck_dir / 'cover.png')

            # 2. 章节扉
            if await find_frame_by_classes(page, ['chapter-plate']):
                await capture_frame(deck, deck_dir / 'chapter.png')
            else:
                print(f'  WARN {master_name}: 找不到 chapter-plate frame，用当前帧凑数')
                await capture_frame(deck, deck_dir / 'chapter.png')

            # 3. 正文
            if await find_frame_by_classes(page, BODY_FRAME_CLASSES):
                await capture_frame(deck, deck_dir / 'body.png')
            else:
                print(f'  WARN {master_name}: 找不到正文 frame，再翻一页凑数')
                await page.keyboard.press('ArrowRight')
                await page.wait_for_timeout(300)
                await capture_frame(deck, deck_dir / 'body.png')

            print(f'  OK   {master_name}: cover / chapter / body 已保存')
            return True
        finally:
            await browser.close()


# ============ MAIN ============

async def main_async(args):
    if not check_playwright():
        return 2

    skill_root = resolve_skill_root()
    data = load_master_list(skill_root)
    all_masters = [m['name'] for m in data['masters']]

    if args.check:
        print('检查 demo-decks/ 下每个大师的 full.html：')
        missing = []
        for name in all_masters:
            html = Path(skill_root) / 'demo-decks' / name / 'full.html'
            status = 'OK ' if html.is_file() else 'MISSING'
            print(f'  [{status}] {name}')
            if not html.is_file():
                missing.append(name)
        print()
        print(f'共 {len(all_masters)} 个大师，缺失 {len(missing)} 个：{missing or "无"}')
        return 0 if not missing else 1

    if args.master:
        targets = [args.master]
    elif args.all:
        targets = all_masters
    else:
        print('请用 --master <name> 或 --all 或 --check', file=sys.stderr)
        return 2

    print(f'开始批量截图 · 目标 {len(targets)} 个大师 · viewport 1280x720 @{args.scale}x')
    success = 0
    for name in targets:
        ok = await capture_master(name, skill_root, args.scale)
        if ok:
            success += 1

    print()
    print(f'完成 {success}/{len(targets)}')
    return 0 if success == len(targets) else 1


def main():
    parser = argparse.ArgumentParser(description='批量截图 14 大师 demo deck')
    parser.add_argument('--master', help='单个大师名（如 rams / hara）')
    parser.add_argument('--all', action='store_true', help='截所有 14 大师')
    parser.add_argument('--check', action='store_true', help='列出缺失 full.html 的大师')
    parser.add_argument('--scale', type=int, default=2,
                        help='截图像素密度倍数（默认 2x retina）')
    args = parser.parse_args()

    sys.exit(asyncio.run(main_async(args)))


if __name__ == '__main__':
    main()
