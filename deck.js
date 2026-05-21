/* ============================================================================
   deck.js · longtext-to-slides 舞台引擎运行时

   功能：
   1. fit-to-viewport：把 1280×720 的 .deck 容器整体 transform: scale() 到当前视口
   2. 翻页：通过 data-state="active|past|next" 管理 frame 状态
   3. 键盘 / 滚轮 / 触摸 / hash 路由
   4. 极窄视口降级为 stack 模式
   ========================================================================== */

(function () {
    'use strict';

    const DECK_W = 1280;
    const DECK_H = 720;
    const STACK_THRESHOLD = 640;  // 视口窄于此值切到 stack 模式

    function init() {
        const marquee = document.querySelector('.marquee');
        const deck = document.querySelector('.deck');
        if (!deck) return;

        const frames = Array.from(deck.querySelectorAll('.frame'));
        if (frames.length === 0) return;

        const rail = document.querySelector('.rail');
        let cursor = 0;
        let stackMode = false;

        // -----------------------------------------------------------------
        // 视口自适配：transform scale
        // -----------------------------------------------------------------
        function fit() {
            const w = window.innerWidth;
            const h = window.innerHeight;

            // 极窄视口降级
            if (w < STACK_THRESHOLD) {
                if (!stackMode) {
                    document.body.classList.add('deck-mode--stack');
                    deck.classList.add('deck-mode--stack');
                    stackMode = true;
                }
                deck.style.setProperty('--fit-scale', 1);
                return;
            } else if (stackMode) {
                document.body.classList.remove('deck-mode--stack');
                deck.classList.remove('deck-mode--stack');
                stackMode = false;
            }

            const scale = Math.min(w / DECK_W, h / DECK_H);
            deck.style.setProperty('--fit-scale', scale);
        }

        // -----------------------------------------------------------------
        // 状态管理：把 cursor 之前的标 past，之后的标 next，当前标 active
        // -----------------------------------------------------------------
        function applyStates() {
            frames.forEach((f, i) => {
                if (i < cursor) f.dataset.state = 'past';
                else if (i === cursor) f.dataset.state = 'active';
                else f.dataset.state = 'next';
            });
            if (rail) {
                Array.from(rail.children).forEach((pip, i) => {
                    pip.setAttribute('aria-current', i === cursor ? 'true' : 'false');
                });
            }
            // 更新 url hash
            history.replaceState(null, '', `#frame-${cursor + 1}`);
        }

        function goto(n) {
            cursor = Math.max(0, Math.min(frames.length - 1, n));
            applyStates();
        }
        function next() { goto(cursor + 1); }
        function prev() { goto(cursor - 1); }

        // -----------------------------------------------------------------
        // 构建 rail（导航点）
        // -----------------------------------------------------------------
        if (rail) {
            rail.innerHTML = '';
            frames.forEach((f, i) => {
                const pip = document.createElement('button');
                pip.className = 'rail-pip';
                pip.type = 'button';
                pip.title = f.dataset.title || `Frame ${i + 1}`;
                pip.addEventListener('click', () => goto(i));
                rail.appendChild(pip);
            });
        }

        // -----------------------------------------------------------------
        // 键盘：→ Space PageDown 下一页，← PageUp 上一页，Home/End 首尾
        // -----------------------------------------------------------------
        window.addEventListener('keydown', (e) => {
            // 排除输入框
            if (e.target.matches('input, textarea, [contenteditable]')) return;

            const k = e.key;
            if (k === 'ArrowRight' || k === ' ' || k === 'PageDown' || k === 'ArrowDown') {
                e.preventDefault(); next();
            } else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'ArrowUp') {
                e.preventDefault(); prev();
            } else if (k === 'Home') {
                e.preventDefault(); goto(0);
            } else if (k === 'End') {
                e.preventDefault(); goto(frames.length - 1);
            } else if (k === 'Escape') {
                // 全屏切换
                if (document.fullscreenElement) document.exitFullscreen();
                else document.documentElement.requestFullscreen?.();
            }
        });

        // -----------------------------------------------------------------
        // 滚轮：节流后切换页（不连续触发）
        // -----------------------------------------------------------------
        let wheelLock = false;
        window.addEventListener('wheel', (e) => {
            if (stackMode) return;
            if (wheelLock) return;
            if (Math.abs(e.deltaY) < 30) return;
            wheelLock = true;
            if (e.deltaY > 0) next(); else prev();
            setTimeout(() => { wheelLock = false; }, 450);
        }, { passive: true });

        // -----------------------------------------------------------------
        // 触摸滑动
        // -----------------------------------------------------------------
        let touchStartY = 0, touchStartX = 0;
        window.addEventListener('touchstart', (e) => {
            touchStartY = e.touches[0].clientY;
            touchStartX = e.touches[0].clientX;
        }, { passive: true });
        window.addEventListener('touchend', (e) => {
            if (stackMode) return;
            const dy = e.changedTouches[0].clientY - touchStartY;
            const dx = e.changedTouches[0].clientX - touchStartX;
            if (Math.abs(dy) > Math.abs(dx) && Math.abs(dy) > 50) {
                if (dy < 0) next(); else prev();
            } else if (Math.abs(dx) > 50) {
                if (dx < 0) next(); else prev();
            }
        }, { passive: true });

        // -----------------------------------------------------------------
        // 点击 frame 区域右半边 → 下一页；左半边 → 上一页（仅 deck 内部）
        // -----------------------------------------------------------------
        deck.addEventListener('click', (e) => {
            if (stackMode) return;
            // 排除可交互元素
            if (e.target.closest('a, button, input, textarea, .rail, .no-tap-nav')) return;
            const rect = deck.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width;
            if (x > 0.66) next();
            else if (x < 0.34) prev();
        });

        // -----------------------------------------------------------------
        // hash 路由：#frame-N 跳转
        // -----------------------------------------------------------------
        function readHash() {
            const m = /^#frame-(\d+)$/.exec(location.hash);
            if (m) goto(parseInt(m[1], 10) - 1);
        }
        window.addEventListener('hashchange', readHash);

        // -----------------------------------------------------------------
        // 启动
        // -----------------------------------------------------------------
        window.addEventListener('resize', fit, { passive: true });
        fit();
        readHash();
        applyStates();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
