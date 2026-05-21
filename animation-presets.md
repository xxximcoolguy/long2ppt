# 动画强度 · 四档预设

> 用户在 Phase 3 Q4 选择动画强度。每档对应一组 CSS 关键帧 + JS 触发逻辑。
> 默认：**标准 (normal)**。

---

## 档位选择决策树

| 用户场景 | 推荐档位 |
|---------|---------|
| 严肃汇报 / 学术 / 文学 | 弱 (subtle) |
| 一般演讲 / 分享 / 默认 | 标准 (normal) |
| 营销 / 发布会 / 视觉冲击 | 强 (bold) |
| 减少动效偏好 / 无障碍 | 无 (none) |

---

## 一、无 (none)

```css
.unfold { opacity: 1; transform: none; transition: none; }
```

完全无动画。适合需要打印 / 截图 / 极度严肃的场景。

---

## 二、弱 (subtle)

只做 fade-in，无位移。

```css
.unfold {
    opacity: 0;
    transition: opacity 0.6s ease-out;
}
.frame[data-state="active"] .unfold { opacity: 1; }
.frame[data-state="active"] .unfold:nth-child(1) { transition-delay: 0.05s; }
.frame[data-state="active"] .unfold:nth-child(2) { transition-delay: 0.15s; }
.frame[data-state="active"] .unfold:nth-child(3) { transition-delay: 0.25s; }
.frame[data-state="active"] .unfold:nth-child(4) { transition-delay: 0.35s; }
.frame[data-state="active"] .unfold:nth-child(5) { transition-delay: 0.45s; }
.frame[data-state="active"] .unfold:nth-child(6) { transition-delay: 0.55s; }
```

---

## 三、标准 (normal) — 默认

Fade + 上移 20px，触发后顺序揭示。

```css
.unfold {
    opacity: 0;
    transform: translateY(20px);
    transition:
        opacity 0.8s ease,
        transform 0.8s cubic-bezier(.16, 1, .3, 1);
}
.frame[data-state="active"] .unfold {
    opacity: 1;
    transform: translateY(0);
}
.frame[data-state="active"] .unfold:nth-child(1) { transition-delay: 0.10s; }
.frame[data-state="active"] .unfold:nth-child(2) { transition-delay: 0.25s; }
.frame[data-state="active"] .unfold:nth-child(3) { transition-delay: 0.40s; }
.frame[data-state="active"] .unfold:nth-child(4) { transition-delay: 0.55s; }
.frame[data-state="active"] .unfold:nth-child(5) { transition-delay: 0.70s; }
.frame[data-state="active"] .unfold:nth-child(6) { transition-delay: 0.85s; }
.frame[data-state="active"] .unfold:nth-child(7) { transition-delay: 1.00s; }
.frame[data-state="active"] .unfold:nth-child(8) { transition-delay: 1.15s; }
```

---

## 四、强 (bold)

更大位移 + 模糊 + 缩放，配合动态背景元素。

```css
.unfold {
    opacity: 0;
    transform: translateY(40px) scale(0.95);
    filter: blur(8px);
    transition:
        opacity 1s ease,
        transform 1s cubic-bezier(.16, 1, .3, 1),
        filter 1s ease;
}
.frame[data-state="active"] .unfold {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
}
.frame[data-state="active"] .unfold:nth-child(1) { transition-delay: 0.15s; }
.frame[data-state="active"] .unfold:nth-child(2) { transition-delay: 0.35s; }
.frame[data-state="active"] .unfold:nth-child(3) { transition-delay: 0.55s; }
.frame[data-state="active"] .unfold:nth-child(4) { transition-delay: 0.75s; }
.frame[data-state="active"] .unfold:nth-child(5) { transition-delay: 0.95s; }
.frame[data-state="active"] .unfold:nth-child(6) { transition-delay: 1.15s; }

/* 背景额外动效：浮动渐变球 */
.frame::before {
    animation: drift 20s ease-in-out infinite;
}
@keyframes drift {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(2vw, -1vh) scale(1.05); }
}
```

---

## 触发逻辑（JS）

所有档位共用同一段 IntersectionObserver，靠 `.frame[data-state="active"]` 触发：

```javascript
const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting && e.intersectionRatio > 0.5) {
            slides.forEach(s => s.classList.remove('active'));
            e.target.classList.add('active');
        }
    });
}, { threshold: [0.5] });
slides.forEach(s => io.observe(s));
```

---

## 特殊版式的额外动画

某些版式（如 framework / stages）有自己的入场动效，**叠加在 reveal 之上**：

**framework 的 step 顶线扫入：**
```css
.step::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 100%; height: 2px; background: var(--accent-key);
    transform: scaleX(0); transform-origin: left;
    animation: stepIn 1.2s 0.3s forwards;
}
@keyframes stepIn { to { transform: scaleX(1); } }
```

**stages 的递进彩条：**
```css
.stage { border-top: 2px solid var(--line); transition: border-color 0.6s; }
.frame[data-state="active"] .stage:nth-child(1) { border-top-color: var(--muted); transition-delay: 0.3s; }
.frame[data-state="active"] .stage:nth-child(2) { border-top-color: var(--accent-3); transition-delay: 0.5s; }
.frame[data-state="active"] .stage:nth-child(3) { border-top-color: var(--accent-key); transition-delay: 0.7s; }
```

**cover 的 stamp 脉冲：**
```css
.cover .stamp::before {
    content: ''; width: 5px; height: 5px;
    background: var(--accent-key); border-radius: 50%;
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
```

这些"版式专属动画"在强档下都启用；标准档保留前 1-2 个；弱档全部关闭。

---

## prefers-reduced-motion 优先级最高

**永远保留这段**（已在 viewport-cn.css 中）：

```css
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.2s !important;
    }
    html { scroll-behavior: auto; }
}
```

即使用户选了「强」档，若系统偏好为减少动效，也会强制平滑过渡。
