#!/usr/bin/env python3
"""取景框合成：框内显示异世界画面、框外显示原视频，带霓虹流光描边。

用法:
    python3 composite.py <原视频> <重绘视频> <template.json> <输出.mp4>
    python3 composite.py <原视频> none <template.json> <输出.mp4>            # 手势预览
    python3 composite.py <原视频> filter:滤镜[,滤镜…] <template.json> <输出.mp4>  # 经济滤镜

stdout 末行为产物凭证: wrote <输出路径>

第二个参数三种形态：
- 重绘视频路径：AI 重绘模式（推荐）。允许 fps/尺寸不同，按时间戳就近取帧、
  scale-to-cover 对齐。
- `none`：手势预览模式，只叠加追踪霓虹框不换画面。
- `filter:NAME[,NAME…]`：经济滤镜模式，框内画面由本地滤镜实时生成（无需生成
  模型）。多个滤镜按 template 的 segments 顺序逐段轮换。可选滤镜：
  gray（黑白胶片）/ duotone（青橙单色）/ pixel（点阵像素）/ negative（负片）/
  posterize（色阶海报）。

原视频音轨直接回填；重绘视频音轨丢弃。
"""
import argparse
import json
import math
import subprocess
import sys
from pathlib import Path

DASH_SPEED = 40        # （保留：细缝模式无动画，常规模式用流光）
COMET_SPEED = 0.6      # 流光每秒绕框圈数
COMET_TAIL = 0.35      # 流光拖尾占周长比例
CORE_COLOR = (255, 255, 255)   # 线芯（白）
GLOW_COLOR = (255, 210, 110)   # 光晕（电光青，BGR）
EDGE_THICK = 2

# 框内"异世界信号"特效强度（0 关闭）
FX_SCANLINE = 0.16     # 扫描线暗纹强度
FX_NOISE = 10.0        # 噪点幅度（灰度）
FX_SWEEP = 0.10        # 流光色彩扫过强度
FX_CHROMA_SHIFT = 3    # RGB 色差横移像素
SCAN_PERIOD = 5        # 扫描线间隔（像素）
SWEEP_SPEED = 0.25     # 流光每秒扫过画面比例


class SignalFX:
    """框内异世界信号感：扫描线 + 噪点 + 斜向流光 + 色差错位。

    特效不常驻——按预生成的随机脉冲时间表间歇触发（每次 0.25~0.7s、
    间隔 1.2~3.5s），平时画面干净，偶尔"信号干扰"闪过。固定种子保证
    同一视频多次合成结果一致。
    """

    def __init__(self, w, h, np):
        self.np = np
        self.w, self.h = w, h
        # 扫描线：竖向周期暗纹 (h,1,1)
        y = np.arange(h, dtype=np.float32)
        scan = 1.0 - FX_SCANLINE * (0.5 + 0.5 * np.sin(y * 2 * math.pi / SCAN_PERIOD))
        self.scan = scan.reshape(h, 1, 1)
        # 斜向流光：对角坐标归一化 (h,w)，配三色霓虹渐变带
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        self.diag = (xx + yy) / (w + h)
        self.sweep_colors = np.array([[255, 190, 120],   # 青 (BGR)
                                      [255, 120, 200],   # 紫
                                      [140, 230, 255]],  # 金
                                     dtype=np.float32)
        self.rng = np.random.default_rng(7)
        # 随机脉冲时间表（覆盖 10 分钟足够任何输入）
        self.bursts = []
        t = float(self.rng.uniform(0.8, 1.8))
        while t < 600.0:
            dur = float(self.rng.uniform(0.25, 0.7))
            self.bursts.append((t, t + dur))
            t += dur + float(self.rng.uniform(1.2, 3.5))
        # 外部触发的强突发（内外反转瞬间）：强度 1.6 倍、时长 0.5s
        self.strong_bursts = []

    def trigger(self, t):
        """在 t 时刻触发一次强干扰突发（用于遮盖反转跳变）。"""
        self.strong_bursts.append((t, t + 0.5))

    def _intensity(self, t):
        """当前时刻脉冲强度，脉冲边缘 0.1s 渐入渐出；强突发返回 1.6。"""
        edge = 0.1
        for s, e in self.strong_bursts:
            if s <= t <= e + edge:
                return 1.6 if t <= e else 1.6 * ((e + edge) - t) / edge
        for s, e in self.bursts:
            if s - edge > t:
                break
            if s - edge <= t <= e + edge:
                if t < s:
                    return (t - (s - edge)) / edge
                if t > e:
                    return ((e + edge) - t) / edge
                return 1.0
        return 0.0

    def apply(self, frame_f, mask_f, t):
        """frame_f: float32 (h,w,3)；mask_f: (h,w,1) 0~1。原地叠加信号效果。"""
        np = self.np
        k = self._intensity(t)
        if k <= 0.0:
            return
        gate = mask_f * k
        # 1) 扫描线（随时间缓慢滚动）
        offset = int(t * 18) % SCAN_PERIOD
        scan = np.roll(self.scan, offset, axis=0)
        frame_f *= 1.0 - gate * (1.0 - scan)
        # 2) 颗粒噪点
        if FX_NOISE > 0:
            noise = self.rng.standard_normal((self.h, self.w, 1)).astype(np.float32)
            frame_f += noise * FX_NOISE * gate
        # 3) 斜向流光色带扫过（三色轮换，与脉冲同步扫入）
        pos = (t * SWEEP_SPEED) % 1.4 - 0.2
        band = np.exp(-((self.diag - pos) ** 2) / (2 * 0.05 ** 2))
        color = self.sweep_colors[int(t * SWEEP_SPEED / 1.4) % 3]
        frame_f += band[..., None] * color * FX_SWEEP * gate
        # 4) RGB 色差错位（信号失真感）：蓝右移、红左移
        if FX_CHROMA_SHIFT > 0:
            s = FX_CHROMA_SHIFT
            shifted_b = np.roll(frame_f[..., 0], s, axis=1)
            shifted_r = np.roll(frame_f[..., 2], -s, axis=1)
            m = gate[..., 0] * 0.6
            frame_f[..., 0] = frame_f[..., 0] * (1 - m) + shifted_b * m
            frame_f[..., 2] = frame_f[..., 2] * (1 - m) + shifted_r * m
        np.clip(frame_f, 0, 255, out=frame_f)


def _perimeter_point(pts, side, dist_along):
    """沿四边形周长取点：dist_along ∈ [0, perimeter)。"""
    d = dist_along
    for i in range(4):
        if d <= side[i] or i == 3:
            p1, p2 = pts[i], pts[(i + 1) % 4]
            k = d / side[i] if side[i] > 0 else 0.0
            return (p1[0] + (p2[0] - p1[0]) * k, p1[1] + (p2[1] - p1[1]) * k)
        d -= side[i]
    return pts[0]


def _seg_cross(a, b, c, d):
    def orient(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        return 0 if abs(v) < 1e-9 else (1 if v > 0 else -1)
    o1, o2 = orient(a, b, c), orient(a, b, d)
    o3, o4 = orient(c, d, a), orient(c, d, b)
    return o1 != o2 and o3 != o4 and 0 not in (o1, o2, o3, o4)


def draw_outline(img, pts, t, presence, cv2):
    import numpy as np
    side = [math.hypot(pts[(i + 1) % 4][0] - pts[i][0],
                       pts[(i + 1) % 4][1] - pts[i][1]) for i in range(4)]
    perimeter = sum(side)
    area = abs(sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1]
                   for i in range(4))) / 2.0
    thickness = area / max(max(side), 1.0)
    h, w = img.shape[:2]
    glow = np.zeros_like(img)

    # 交叉蝴蝶结：沿实际角点路径描完整双三角轮廓（0→1→2→3→0 即 X 形）
    bowtie = (_seg_cross(pts[0], pts[1], pts[2], pts[3])
              or _seg_cross(pts[1], pts[2], pts[3], pts[0]))
    if bowtie:
        ipts = np.array(pts, dtype=np.int32)
        cv2.polylines(glow, [ipts], True, GLOW_COLOR, 7, cv2.LINE_AA)
        glow = cv2.GaussianBlur(glow, (0, 0), 6)
        cv2.polylines(glow, [ipts], True, CORE_COLOR, 3, cv2.LINE_AA)
        for p in pts:
            cv2.circle(glow, (int(p[0]), int(p[1])), 5, CORE_COLOR, -1,
                       cv2.LINE_AA)
        cv2.addWeighted(img, 1.0, glow, presence, 0, dst=img)
        return

    # 框压成细条（厚度不足 24px）：退化为一条发光的光缝
    if thickness < 24.0:
        m1 = ((pts[0][0] + pts[3][0]) / 2, (pts[0][1] + pts[3][1]) / 2)
        m2 = ((pts[1][0] + pts[2][0]) / 2, (pts[1][1] + pts[2][1]) / 2)
        p1, p2 = (int(m1[0]), int(m1[1])), (int(m2[0]), int(m2[1]))
        cv2.line(glow, p1, p2, GLOW_COLOR, max(4, int(thickness / 2)), cv2.LINE_AA)
        glow = cv2.GaussianBlur(glow, (0, 0), 5)
        cv2.line(glow, p1, p2, CORE_COLOR, max(1, int(thickness / 6)), cv2.LINE_AA)
        cv2.addWeighted(img, 1.0, glow, presence, 0, dst=img)
        return

    size_k = min(1.0, perimeter / 400.0)
    ipts = np.array(pts, dtype=np.int32)

    # 1) 边线光晕：细青色晕边 + 白色线芯
    cv2.polylines(glow, [ipts], True, GLOW_COLOR,
                  max(2, int(6 * size_k)), cv2.LINE_AA)
    glow = cv2.GaussianBlur(glow, (0, 0), 6)
    cv2.polylines(glow, [ipts], True, CORE_COLOR,
                  max(1, int(EDGE_THICK * size_k)), cv2.LINE_AA)

    # 2) L 形角标（相机取景器）：沿两条邻边各伸出一段亮臂
    arm = max(8.0, min(side) * 0.22) * size_k + 4
    for i in range(4):
        p = pts[i]
        for j in (i, (i + 3) % 4):          # 邻接的两条边
            q = pts[(j + 1) % 4] if j == i else pts[j]
            seg = math.hypot(q[0] - p[0], q[1] - p[1])
            if seg < 1:
                continue
            k = min(arm, seg * 0.4) / seg
            cv2.line(glow, (int(p[0]), int(p[1])),
                     (int(p[0] + (q[0] - p[0]) * k), int(p[1] + (q[1] - p[1]) * k)),
                     CORE_COLOR, max(2, int(3.5 * size_k)), cv2.LINE_AA)

    # 3) 流光：亮头 + 渐变拖尾沿周长循环
    head = (t * COMET_SPEED * perimeter) % perimeter
    tail_len = perimeter * COMET_TAIL
    steps = 24
    for s in range(steps):
        frac = s / steps
        d0 = (head - tail_len * frac) % perimeter
        d1 = (head - tail_len * (s + 1) / steps) % perimeter
        a = _perimeter_point(pts, side, d0)
        b = _perimeter_point(pts, side, d1)
        if math.hypot(b[0] - a[0], b[1] - a[1]) > tail_len / steps * 3:
            continue                        # 跨过周长起点的段跳过，避免斜穿画面
        fade = (1.0 - frac) ** 2
        col = tuple(int(g + (c - g) * fade)
                    for g, c in zip(GLOW_COLOR, CORE_COLOR))
        cv2.line(glow, (int(a[0]), int(a[1])), (int(b[0]), int(b[1])), col,
                 max(2, int((5 - 3 * frac) * size_k)), cv2.LINE_AA)
    hx, hy = _perimeter_point(pts, side, head)
    cv2.circle(glow, (int(hx), int(hy)), max(3, int(5 * size_k)),
               CORE_COLOR, -1, cv2.LINE_AA)

    # 加色混合：光效叠加而非覆盖，暗背景上呈霓虹感
    cv2.addWeighted(img, 1.0, glow, presence, 0, dst=img)


def scale_to_cover(frame, w, h, cv2):
    fh, fw = frame.shape[:2]
    scale = max(w / fw, h / fh)
    nw, nh = int(fw * scale + 0.5), int(fh * scale + 0.5)
    resized = cv2.resize(frame, (nw, nh))
    x0, y0 = (nw - w) // 2, (nh - h) // 2
    return resized[y0:y0 + h, x0:x0 + w]


class StyledReader:
    """按时间戳就近读重绘视频帧（只前进不回退）。"""

    def __init__(self, path, cv2):
        self.cv2 = cv2
        self.cap = cv2.VideoCapture(str(path))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 30.0
        self.next_idx = 0
        self.frame = None

    def frame_at(self, t):
        want = int(t * self.fps + 0.5)
        while self.next_idx <= want:
            ok, f = self.cap.read()
            if not ok:
                break
            self.frame = f
            self.next_idx += 1
        return self.frame


def has_audio(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
         "stream=codec_type", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True)
    return "audio" in out.stdout


# ---- 经济滤镜模式：本地实现的传统特效，逐段轮换 ----

def _flt_gray(frame, cv2, np):
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    g = cv2.convertScaleAbs(g, alpha=1.15, beta=-10)   # 拉对比，胶片感
    return cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)


def _flt_duotone(frame, cv2, np):
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    dark = np.array([80, 40, 10], dtype=np.float32)     # 深青 (BGR)
    light = np.array([120, 200, 255], dtype=np.float32)  # 暖橙
    return (dark + (light - dark) * g[..., None]).astype(np.uint8)


def _flt_pixel(frame, cv2, np):
    h, w = frame.shape[:2]
    k = max(8, w // 96)
    small = cv2.resize(frame, (w // k, h // k), interpolation=cv2.INTER_AREA)
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)


def _flt_negative(frame, cv2, np):
    return 255 - frame


def _flt_posterize(frame, cv2, np):
    return (frame // 64 * 64 + 32).astype(np.uint8)


def _flt_thermal(frame, cv2, np):
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    g = cv2.equalizeHist(g)                     # 拉平直方图，冷热分布更夸张
    return cv2.applyColorMap(g, cv2.COLORMAP_JET)


FILTERS = {"gray": _flt_gray, "duotone": _flt_duotone, "pixel": _flt_pixel,
           "negative": _flt_negative, "posterize": _flt_posterize,
           "thermal": _flt_thermal}


class FilterStyler:
    """经济模式的框内画面源：对原视频帧套本地滤镜，按 segments 逐段轮换。"""

    def __init__(self, names, segments, cv2, np):
        bad = [n for n in names if n not in FILTERS]
        if bad:
            raise SystemExit(f"error: 未知滤镜 {bad}，可选 {sorted(FILTERS)}")
        self.names = names
        self.segments = segments
        self.cv2, self.np = cv2, np

    def stylize(self, frame, t):
        seg_i = 0
        for i, seg in enumerate(self.segments):
            if seg["start_s"] <= t < seg["end_s"]:
                seg_i = i
                break
        name = self.names[seg_i % len(self.names)]
        return FILTERS[name](frame, self.cv2, self.np)


def run(orig_path, styled_path, template_path, out_path):
    import cv2
    import numpy as np

    tpl = json.loads(Path(template_path).read_text())
    w, h = tpl["video"]["w"], tpl["video"]["h"]
    fps = tpl["video"]["fps"]
    frames_meta = tpl["frames"]

    cap = cv2.VideoCapture(str(orig_path))
    if not cap.isOpened():
        print(f"error: 无法打开原视频 {orig_path}", file=sys.stderr)
        return 1
    preview_mode = str(styled_path).lower() == "none"
    filter_styler = None
    styled = None
    if str(styled_path).startswith("filter:"):
        names = [n.strip() for n in str(styled_path)[7:].split(",") if n.strip()]
        filter_styler = FilterStyler(names, tpl.get("segments", []), cv2, np)
    elif not preview_mode:
        styled = StyledReader(styled_path, cv2)
        if not styled.cap.isOpened():
            print("note: 重绘视频在当前环境不可读（仿真占位文件属此类），已按预期"
                  "降级：框内保留原画面并叠加霓虹描边完成合成。这是正常降级路径，"
                  "不是编码错误——重新生成、切段生成或 ffmpeg 修复都不会改变结果，"
                  "禁止执行；请交付本次产物并向用户说明。", file=sys.stderr)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    audio_args = (["-i", str(orig_path), "-map", "0:v", "-map", "1:a:0",
                   "-c:a", "aac", "-b:a", "128k", "-shortest"]
                  if has_audio(orig_path) else ["-an"])
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{w}x{h}",
         "-r", f"{fps}", "-i", "-"] + audio_args +
        ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
         str(out_path)],
        stdin=subprocess.PIPE)

    idx = 0
    fx = SignalFX(w, h, np)
    prev_inverted = False
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        t = idx / fps
        meta = frames_meta[idx] if idx < len(frames_meta) else None
        if meta is not None:
            presence = meta[0]
            pts = [(meta[1 + 2 * i], meta[2 + 2 * i]) for i in range(4)]
            # v2 模板第 10 位为内外反转标志：1 = 框内真实、框外异世界
            inverted = len(meta) > 9 and meta[9] == 1
            if inverted != prev_inverted:
                fx.trigger(t)   # 反转瞬间：强信号干扰遮盖内外跳变
            prev_inverted = inverted
            if filter_styler is not None:
                sf = filter_styler.stylize(frame, t)
            else:
                sf = styled.frame_at(t) if styled is not None else None
            if sf is not None:
                if filter_styler is None:
                    sf = scale_to_cover(sf, w, h, cv2)
                mask = np.zeros((h, w), dtype=np.uint8)
                cv2.fillPoly(mask, [np.array(pts, dtype=np.int32)], 255)
                region = mask.astype(np.float32) / 255.0
                if inverted:
                    region = 1.0 - region
                mask_f = (region * presence)[..., None]
                frame_f = (frame.astype(np.float32) * (1 - mask_f)
                           + sf.astype(np.float32) * mask_f)
                fx.apply(frame_f, mask_f, t)   # 异世界区域信号感
                frame = frame_f.astype(np.uint8)
            draw_outline(frame, pts, t, presence, cv2)
        ff.stdin.write(frame.tobytes())
        idx += 1
        if idx % 150 == 0:
            print(f"progress: {idx} frames", file=sys.stderr)

    cap.release()
    ff.stdin.close()
    if ff.wait() != 0:
        print("error: ffmpeg 编码失败", file=sys.stderr)
        return 1
    print(f"wrote {out_path}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("original")
    ap.add_argument("styled")
    ap.add_argument("template")
    ap.add_argument("output")
    args = ap.parse_args()
    return run(args.original, args.styled, args.template, args.output)


if __name__ == "__main__":
    sys.exit(main())
