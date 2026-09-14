#!/usr/bin/env python3
"""手指取景框检测：逐帧定位双手拇指+食指围成的四边形，输出追踪模板。

用法:
    python3 detect_frame.py <输入视频> [--job 任务名]

输出 /tmp/finger_frame/<job>/template.json，stdout 末行为产物凭证:
    wrote <路径> frames=N coverage=P% segments=K duration=Ss

追踪逻辑移植自 sophiamyang/finger-frame-effect-ai 的 composite.py:
解剖学角点排序、张开度/面积滞后门控、瞬移拒绝、速度自适应平滑、
丢帧保持与 presence 淡入淡出。分段逻辑为本 skill 新增:
取景框"合拢→重新张开"的手势事件作为风格切换边界。
"""
import argparse
import json
import math
import sys
from pathlib import Path

# MediaPipe 手部关键点索引
WRIST, THUMB_TIP, INDEX_TIP, MIDDLE_MCP = 0, 4, 8, 9

# 门控阈值（acquire 严 / keep 松，滞后防抖）。
# keep 刻意压得很低：接近捏合的窄条框也要维持显示（实测捏拢时张开度 0.08~0.18），
# 只有完全合拢（<0.1）才判定手势结束。
SPREAD_ACQUIRE, SPREAD_KEEP = 0.75, 0.1      # 拇指-食指张开度 / 手部尺度
AREA_ACQUIRE, AREA_KEEP = 0.005, 0.0002      # 四边形面积 / 画面面积
THIN_RATIO = 0.02                            # 仅拦零面积退化，窄条框正常显示

# 追踪稳定化
JUMP_FRACTION = 0.3          # 平均位移超画宽此比例视为瞬移
JUMP_CONFIRM_FRAMES = 2      # 瞬移需连续确认帧数
MAX_LOST_FRAMES = 2          # 检测丢失后角点保持帧数（消失要干脆）
PRESENCE_IN, PRESENCE_OUT = 0.12, 0.4
ALPHA_MIN, ALPHA_MAX, ALPHA_SCALE = 0.35, 0.85, 0.05

# 拉线手势：双手同时捏合且相距足够远时，框收束为连接两捏合点的光缝线
LINE_KEEP_DIST_FRAC = 0.25   # 两捏合点最小距离 / 画宽

# 手势分段
MIN_PHASE_SEC = 2.0          # 短于此的风格相位向前合并

# 内外反转手势：手指交叉（四边形自交成蝴蝶结）触发一次反转切换
CROSS_CONFIRM_FRAMES = 3     # 连续自交帧数确认
CROSS_REFRACTORY_SEC = 0.8   # 两次切换的最小间隔

WORK_DIR = Path("/tmp/finger_frame")  # 模板与中间产物不落 /workspace


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def polygon_area(pts):
    n = len(pts)
    s = 0.0
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


def angle_sorted(pts):
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    return sorted(pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))


def _seg_cross(a, b, c, d):
    """线段 ab 与 cd 是否真交（不含共端点）。"""
    def orient(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        return 0 if abs(v) < 1e-9 else (1 if v > 0 else -1)
    o1, o2 = orient(a, b, c), orient(a, b, d)
    o3, o4 = orient(c, d, a), orient(c, d, b)
    return o1 != o2 and o3 != o4 and 0 not in (o1, o2, o3, o4)


def is_bowtie(pts):
    """解剖学顺序四边形是否自交（手指交叉时对边相交成蝴蝶结）。"""
    return (_seg_cross(pts[0], pts[1], pts[2], pts[3])
            or _seg_cross(pts[1], pts[2], pts[3], pts[0]))


def compute_line(hands, w):
    """拉线手势：双手各自捏合、且两捏合点相距足够远 → 返回两端点。"""
    if len(hands) != 2:
        return None
    mids = []
    for hd in hands:
        if dist(hd["thumb"], hd["index"]) > hd["scale"] * 0.35:
            return None
        mids.append(((hd["thumb"][0] + hd["index"][0]) / 2,
                     (hd["thumb"][1] + hd["index"][1]) / 2))
    a, b = sorted(mids, key=lambda m: m[0])
    if dist(a, b) < w * LINE_KEEP_DIST_FRAC:
        return None
    return a, b


def compute_quad(hands, w, h, frame_active):
    """hands: [{index, thumb, wx, scale}]。返回 (四角点, 是否交叉) 或 (None, False)。

    角点固定为 左手食指→右手食指→右手拇指→左手拇指，帧间索引一一对应，
    便于逐角点平滑；手指交叉时四边形自交成蝴蝶结，作为"内外反转"手势信号。
    """
    if len(hands) != 2:
        return None, False
    need = SPREAD_KEEP if frame_active else SPREAD_ACQUIRE
    for hd in hands:
        if dist(hd["thumb"], hd["index"]) < hd["scale"] * need:
            return None, False
    a, b = sorted(hands, key=lambda d: d["wx"])
    pts = [a["index"], b["index"], b["thumb"], a["thumb"]]
    min_area = AREA_KEEP if frame_active else AREA_ACQUIRE
    area = polygon_area(angle_sorted(pts))
    if area < w * h * min_area:
        return None, False
    # 细条退化拒绝：双手各自捏合时四角塌成细线（面积/最长边 = 等效厚度），
    # 视为"合拢"手势而非有效取景框
    max_side = max(dist(pts[i], pts[(i + 1) % 4]) for i in range(4))
    if max_side > 0 and area / max_side < max_side * THIN_RATIO:
        return None, False
    return pts, is_bowtie(pts)


class FrameTracker:
    """逐帧接收候选四边形，维护平滑角点、presence 与激活状态机。"""

    def __init__(self, w, h, fps):
        self.w, self.h = w, h
        self.fps = fps
        self.corners = None
        self.presence = 0.0
        self.frame_active = False
        self.lost = 0
        self.jump_frames = 0
        self.last_valid_t = None
        self.activations = []    # 每次 off→on 的时间戳（秒）
        self.gap_starts = []     # 每次失活前最后有效检测的时间戳

    def update(self, target, t):
        if target is None:
            self._on_lost()
            return
        if self.corners is None:
            self.corners = [list(p) for p in target]
        else:
            moved = sum(dist(c, p) for c, p in zip(self.corners, target)) / 4.0
            if moved > self.w * JUMP_FRACTION:
                self.jump_frames += 1
                if self.jump_frames < JUMP_CONFIRM_FRAMES:
                    self._on_lost()
                    return
                self.corners = [list(p) for p in target]
                self.jump_frames = 0
            else:
                self.jump_frames = 0
                alpha = min(ALPHA_MAX, max(ALPHA_MIN, moved / (self.w * ALPHA_SCALE)))
                self.corners = [
                    [c[0] + (p[0] - c[0]) * alpha, c[1] + (p[1] - c[1]) * alpha]
                    for c, p in zip(self.corners, target)
                ]
        self.lost = 0
        self.presence = min(1.0, self.presence + PRESENCE_IN)
        if not self.frame_active:
            self.frame_active = True
            self.activations.append(t)
        self.last_valid_t = t

    def _on_lost(self):
        self.lost += 1
        if self.lost > MAX_LOST_FRAMES:
            self.presence = max(0.0, self.presence - PRESENCE_OUT)
            if self.presence <= 0.0 and self.frame_active:
                self.frame_active = False
                self.gap_starts.append(self.last_valid_t)
                self.corners = None
        elif self.corners is not None:
            self.presence = min(1.0, self.presence + PRESENCE_IN)


def build_segments(activations, gap_starts, duration):
    """手势事件 → 风格相位边界。首次激活不算切换；边界取合拢间隙中点。"""
    boundaries = []
    for i, act_t in enumerate(activations[1:]):
        gap_start = gap_starts[i] if i < len(gap_starts) else act_t
        boundaries.append((gap_start + act_t) / 2.0)
    cuts = [0.0] + sorted(boundaries) + [duration]
    # 短相位向前合并（首段过短则并入后段）
    merged = [cuts[0]]
    for c in cuts[1:-1]:
        if c - merged[-1] >= MIN_PHASE_SEC:
            merged.append(c)
    if duration - merged[-1] < MIN_PHASE_SEC and len(merged) > 1:
        merged.pop()
    merged.append(duration)
    return [
        {"start_s": round(merged[i], 2), "end_s": round(merged[i + 1], 2)}
        for i in range(len(merged) - 1)
    ]


def hands_to_px(result, w, h):
    hands = []
    for lm in result.hand_landmarks:
        def px(i):
            return (lm[i].x * w, lm[i].y * h)
        hands.append({
            "index": px(INDEX_TIP),
            "thumb": px(THUMB_TIP),
            "wx": px(WRIST)[0],
            "scale": dist(px(WRIST), px(MIDDLE_MCP)) + 1.0,
        })
    return hands


def run(video_path, job):
    import cv2
    import mediapipe as mp
    from mediapipe.tasks import python as mp_python
    from mediapipe.tasks.python import vision

    model = Path(__file__).parent / "models" / "hand_landmarker.task"
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"error: 无法打开视频 {video_path}", file=sys.stderr)
        return 1
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0

    landmarker = vision.HandLandmarker.create_from_options(
        vision.HandLandmarkerOptions(
            base_options=mp_python.BaseOptions(model_asset_path=str(model)),
            running_mode=vision.RunningMode.VIDEO,
            num_hands=2,
        ))
    tracker = FrameTracker(w, h, fps)
    frames = []
    # 内外反转状态机：手指交叉（蝴蝶结）连续确认后翻转 inverted，带不应期防抖
    inverted = False
    cross_streak = 0
    last_flip_t = -1e9
    flips = 0
    line_presence = 0.0
    idx = 0
    while True:
        ok, bgr = cap.read()
        if not ok:
            break
        t = idx / fps
        img = mp.Image(image_format=mp.ImageFormat.SRGB,
                       data=cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
        result = landmarker.detect_for_video(img, int(t * 1000))
        hands = hands_to_px(result, w, h)
        quad, crossed = compute_quad(hands, w, h, tracker.frame_active)
        cross_streak = cross_streak + 1 if (quad is not None and crossed) else 0
        if (cross_streak == CROSS_CONFIRM_FRAMES
                and t - last_flip_t >= CROSS_REFRACTORY_SEC):
            inverted = not inverted
            last_flip_t = t
            flips += 1
        # 交叉的蝴蝶结照常追踪显示：fillPoly 对自交四边形填出双三角"交叉方格"，
        # 是本手势的标志性画面；若冻结会导致 presence 塌零、误判成合拢切段
        tracker.update(quad, t)
        inv_bit = 1 if inverted else 0
        if tracker.corners is not None and tracker.presence > 0:
            line_presence = 0.0
            frames.append([round(tracker.presence, 3)]
                          + [round(v, 1) for pt in tracker.corners for v in pt]
                          + [inv_bit])
        else:
            # 无框时看拉线手势：双手捏合拉开 → 退化四边形 [a,b,b,a]，
            # composite 的细条分支自然渲染成连接光缝
            line = compute_line(hands, w)
            line_presence = (min(1.0, line_presence + 0.3) if line
                             else max(0.0, line_presence - 0.4))
            if line and line_presence > 0:
                (ax, ay), (bx, by) = line
                frames.append([round(line_presence, 3),
                               round(ax, 1), round(ay, 1), round(bx, 1),
                               round(by, 1), round(bx, 1), round(by, 1),
                               round(ax, 1), round(ay, 1), inv_bit])
            else:
                frames.append(None)
        idx += 1
        if idx % 150 == 0:
            print(f"progress: {idx} frames", file=sys.stderr)
    cap.release()
    try:
        landmarker.close()
    except Exception:
        pass

    duration = idx / fps if fps else 0.0
    coverage = sum(1 for f in frames if f is not None) / max(idx, 1)
    segments = build_segments(tracker.activations, tracker.gap_starts, duration)

    out_dir = WORK_DIR / job
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "template.json"
    out_path.write_text(json.dumps({
        "version": 2,
        "video": {"w": w, "h": h, "fps": round(fps, 3),
                  "frames": idx, "duration": round(duration, 2)},
        "frames": frames,
        "segments": segments,
    }, ensure_ascii=False))

    for i, seg in enumerate(segments, 1):
        print(f"segment {i}: {seg['start_s']}s - {seg['end_s']}s")
    print(f"wrote {out_path} frames={idx} coverage={coverage * 100:.0f}% "
          f"segments={len(segments)} inversions={flips} duration={duration:.1f}s")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--job", default=None)
    args = ap.parse_args()
    job = args.job or Path(args.video).stem
    return run(Path(args.video), job)


if __name__ == "__main__":
    sys.exit(main())
