#!/usr/bin/env python3
"""
style_preview.py · 启动本地风格选择预览页

启动一个临时 HTTP server 服务 skill 根目录，自动打开浏览器到
preview.html，等待用户在网页里挑选风格 → POST /select →
把 payload 写入 --output 指定的 style_config.json 后退出。

usage:
  python scripts/style_preview.py \\
      --title "我的文档" \\
      --words 2500 \\
      --scene business \\
      --output /tmp/style_config.json

Phase 3 Q1 进阶模式调用本脚本：
  1. server 在随机端口起来
  2. webbrowser.open 打开 preview.html
  3. wait 用户选择（超时 600s）
  4. 收到 POST /select → 写 JSON → 退出 0
  5. 超时 / 用户关页面 → 退出 1 fallback 回对话模式

exit codes:
  0  正常收到选择
  1  超时无选择
  2  环境问题（preview.html 找不到等）
"""

import argparse
import json
import os
import socket
import sys
import threading
import time
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import Optional
from urllib.parse import urlencode

# Windows GBK 终端无法编码 ✓ ⏱ 等非 GBK 字符 —— 强制 stdout/stderr 走 UTF-8。
# 否则成功提示里的 print 会抛 UnicodeEncodeError 让脚本崩溃、误退出码 1，
# SKILL.md 会把它当成"用户取消"，丢掉用户已经写入 JSON 的风格选择。
# line_buffering=True：管道下也按行刷新，启动横幅(含 URL)立即可见，不被块缓冲卡住。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding='utf-8', line_buffering=True)
    except Exception:
        pass


# ============ STATE ============

class State:
    def __init__(self, output_path: str, skill_root: str):
        self.output_path = output_path
        self.skill_root = skill_root
        self.received = False
        self.payload = None


# ============ HTTP HANDLER ============

class Handler(SimpleHTTPRequestHandler):
    state: State = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=Handler.state.skill_root, **kwargs)

    def log_message(self, fmt, *args):
        # 静音访问日志（避免污染终端）
        return

    def do_POST(self):
        if self.path == '/select':
            length = int(self.headers.get('Content-Length', 0))
            try:
                body = self.rfile.read(length).decode('utf-8')
                payload = json.loads(body)
            except (UnicodeDecodeError, json.JSONDecodeError) as e:
                # 请求体非 UTF-8 或非合法 JSON —— 干净地回 400, 不让 handler 崩
                self._json_response(400, {'error': f'invalid request body: {e}'})
                return

            try:
                os.makedirs(os.path.dirname(Handler.state.output_path) or '.', exist_ok=True)
                with open(Handler.state.output_path, 'w', encoding='utf-8') as f:
                    json.dump(payload, f, ensure_ascii=False, indent=2)
            except OSError as e:
                self._json_response(500, {'error': f'write failed: {e}'})
                return

            Handler.state.received = True
            Handler.state.payload = payload
            self._json_response(200, {'ok': True})
        else:
            self.send_response(404)
            self.end_headers()

    def _json_response(self, status: int, payload: dict):
        body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)


# ============ HELPERS ============

def find_free_port() -> int:
    with socket.socket() as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def resolve_skill_root(explicit: Optional[str]) -> str:
    if explicit:
        return os.path.abspath(explicit)
    # script lives in <skill_root>/scripts/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, '..'))


# ============ MAIN ============

def main():
    parser = argparse.ArgumentParser(description='启动风格预览页')
    parser.add_argument('--title', default='示例文档', help='文档标题（显示在预览页 Hero）')
    parser.add_argument('--words', type=int, default=2500, help='文档字数（显示在 Hero）')
    parser.add_argument('--scene', default=None,
                        choices=['business', 'reading', 'social', 'speech', None],
                        help='预选场景（可选 · 用户仍可改）')
    parser.add_argument('--output', required=True, help='style_config.json 输出路径')
    parser.add_argument('--skill-root', default=None,
                        help='skill 根目录路径（默认从脚本位置推断）')
    parser.add_argument('--timeout', type=int, default=600,
                        help='等待用户选择的超时秒数（默认 600s）')
    parser.add_argument('--no-browser', action='store_true',
                        help='不自动打开浏览器（CI/测试用）')
    parser.add_argument('--port', type=int, default=0,
                        help='指定端口（0 = 随机）')
    args = parser.parse_args()

    skill_root = resolve_skill_root(args.skill_root)
    preview_html = os.path.join(skill_root, 'templates', 'preview.html')
    preview_data = os.path.join(skill_root, 'templates', 'preview-data.json')

    if not os.path.isfile(preview_html):
        print(f'ERROR: preview.html not found at {preview_html}', file=sys.stderr)
        sys.exit(2)
    if not os.path.isfile(preview_data):
        print(f'ERROR: preview-data.json not found at {preview_data}', file=sys.stderr)
        sys.exit(2)

    Handler.state = State(args.output, skill_root)

    port = args.port or find_free_port()
    try:
        server = HTTPServer(('127.0.0.1', port), Handler)
    except OSError as e:
        print(f'ERROR: cannot bind 127.0.0.1:{port} · {e}', file=sys.stderr)
        sys.exit(2)

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    params = {'title': args.title, 'words': args.words}
    if args.scene:
        params['scene'] = args.scene
    url = f'http://127.0.0.1:{port}/templates/preview.html?{urlencode(params)}'

    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'  longtext-to-slides · 风格预览服务')
    print(f'  地址：{url}')
    print(f'  等待用户选择（超时 {args.timeout}s）...')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

    if not args.no_browser:
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f'WARN: 自动打开浏览器失败：{e}', file=sys.stderr)
            print(f'      请手动复制上面的地址打开。', file=sys.stderr)

    deadline = time.time() + args.timeout
    try:
        while time.time() < deadline:
            if Handler.state.received:
                print()
                print('[OK] 收到选择，写入到', args.output)
                print(json.dumps(Handler.state.payload, ensure_ascii=False, indent=2))
                server.shutdown()
                sys.exit(0)
            time.sleep(0.4)
    except KeyboardInterrupt:
        print('\n中断 · 用户取消')
        server.shutdown()
        sys.exit(1)

    print(f'\n[TIMEOUT] 超时（{args.timeout}s 无选择） · fallback 回对话模式',
          file=sys.stderr)
    server.shutdown()
    sys.exit(1)


if __name__ == '__main__':
    main()
