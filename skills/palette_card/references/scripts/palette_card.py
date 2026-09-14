#!/usr/bin/env python3
"""Extract a cinematic palette from a video clip or images, render a PNG card.

The card is a 1920x1140 horizontal layout: up to six equal-width color columns
labelled with hex + share, and a paper-tone bottom bar carrying an
auto-generated poetic title (bottom-left) and an optional logo (bottom-right).

The color pipeline mirrors what the yeguozi archive statistics suggest:
sample pixels in CIE Lab, damp near-black/near-white influence, run a
weighted k-means, merge近似色 by CIEDE2000, then softly compress chroma so
swatches stay inside the muted, film-like gamut observed on the site
(per-lightness chroma envelope; almost no bright saturated colors).

Dependencies: numpy + Pillow; ffmpeg/ffprobe only for video input.
See `--help` for usage examples.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

VIDEO_SUFFIXES = {".mp4", ".mov", ".mkv", ".avi", ".webm", ".m4v", ".mpg", ".ts"}
ANALYSIS_WIDTH = 240
MAX_SAMPLES = 200_000

# ---------------------------------------------------------------------------
# Color math (vectorized sRGB <-> Lab, CIEDE2000)
# ---------------------------------------------------------------------------

_D65 = np.array([0.95047, 1.0, 1.08883])
_RGB_TO_XYZ = np.array(
    [
        [0.4124564, 0.3575761, 0.1804375],
        [0.2126729, 0.7151522, 0.0721750],
        [0.0193339, 0.1191920, 0.9503041],
    ]
)
_XYZ_TO_RGB = np.linalg.inv(_RGB_TO_XYZ)


def rgb_to_lab(rgb: np.ndarray) -> np.ndarray:
    v = np.asarray(rgb, dtype=np.float64) / 255.0
    lin = np.where(v <= 0.04045, v / 12.92, ((v + 0.055) / 1.055) ** 2.4)
    xyz = lin @ _RGB_TO_XYZ.T / _D65
    d = 6.0 / 29.0
    f = np.where(xyz > d**3, np.cbrt(xyz), xyz / (3 * d**2) + 4.0 / 29.0)
    return np.stack(
        [116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])],
        axis=-1,
    )


def lab_to_rgb(lab: np.ndarray) -> np.ndarray:
    lab = np.asarray(lab, dtype=np.float64)
    fy = (lab[..., 0] + 16) / 116
    fx = fy + lab[..., 1] / 500
    fz = fy - lab[..., 2] / 200
    d = 6.0 / 29.0
    f = np.stack([fx, fy, fz], axis=-1)
    xyz = np.where(f > d, f**3, 3 * d**2 * (f - 4.0 / 29.0)) * _D65
    lin = xyz @ _XYZ_TO_RGB.T
    srgb = np.where(lin <= 0.0031308, 12.92 * lin, 1.055 * np.clip(lin, 0, None) ** (1 / 2.4) - 0.055)
    return np.clip(np.rint(srgb * 255), 0, 255).astype(np.uint8)


def delta_e_2000(lab1: np.ndarray, lab2: np.ndarray) -> np.ndarray:
    """CIEDE2000 between two broadcastable arrays of Lab triplets."""
    l1, a1, b1 = lab1[..., 0], lab1[..., 1], lab1[..., 2]
    l2, a2, b2 = lab2[..., 0], lab2[..., 1], lab2[..., 2]
    c1, c2 = np.hypot(a1, b1), np.hypot(a2, b2)
    cbar = (c1 + c2) / 2
    g = 0.5 * (1 - np.sqrt(cbar**7 / (cbar**7 + 25.0**7)))
    a1p, a2p = (1 + g) * a1, (1 + g) * a2
    c1p, c2p = np.hypot(a1p, b1), np.hypot(a2p, b2)
    h1p = np.degrees(np.arctan2(b1, a1p)) % 360
    h2p = np.degrees(np.arctan2(b2, a2p)) % 360
    dl = l2 - l1
    dc = c2p - c1p
    dh = h2p - h1p
    dh = np.where(np.abs(dh) > 180, dh - np.sign(dh) * 360, dh)
    dh = np.where(c1p * c2p == 0, 0.0, dh)
    dbig = 2 * np.sqrt(c1p * c2p) * np.sin(np.radians(dh / 2))
    lbar = (l1 + l2) / 2
    cbarp = (c1p + c2p) / 2
    hsum = h1p + h2p
    hbar = np.where(
        c1p * c2p == 0,
        hsum,
        np.where(
            np.abs(h1p - h2p) <= 180,
            hsum / 2,
            np.where(hsum < 360, (hsum + 360) / 2, (hsum - 360) / 2),
        ),
    )
    t = (
        1
        - 0.17 * np.cos(np.radians(hbar - 30))
        + 0.24 * np.cos(np.radians(2 * hbar))
        + 0.32 * np.cos(np.radians(3 * hbar + 6))
        - 0.20 * np.cos(np.radians(4 * hbar - 63))
    )
    dtheta = 30 * np.exp(-(((hbar - 275) / 25) ** 2))
    rc = 2 * np.sqrt(cbarp**7 / (cbarp**7 + 25.0**7))
    sl = 1 + 0.015 * (lbar - 50) ** 2 / np.sqrt(20 + (lbar - 50) ** 2)
    sc = 1 + 0.045 * cbarp
    sh = 1 + 0.015 * cbarp * t
    rt = -np.sin(np.radians(2 * dtheta)) * rc
    return np.sqrt(
        (dl / sl) ** 2 + (dc / sc) ** 2 + (dbig / sh) ** 2 + rt * (dc / sc) * (dbig / sh)
    )


# ---------------------------------------------------------------------------
# Input loading
# ---------------------------------------------------------------------------


def _letterbox_crop(pixels: np.ndarray) -> np.ndarray:
    luma = pixels.astype(np.float32) @ np.array([0.2126, 0.7152, 0.0722], dtype=np.float32)
    h, w = luma.shape

    def dark_run(means: np.ndarray, limit: int) -> int:
        n = 0
        for m in means[:limit]:
            if m <= 14.0:
                n += 1
            else:
                break
        return n

    top = dark_run(luma.mean(axis=1), h // 5)
    bottom = dark_run(luma.mean(axis=1)[::-1], h // 5)
    left = dark_run(luma.mean(axis=0), w // 5)
    right = dark_run(luma.mean(axis=0)[::-1], w // 5)
    if max(top, bottom, left, right) < 2:
        return pixels
    return pixels[top : h - bottom or h, left : w - right or w]


def _downscale(image: Image.Image) -> np.ndarray:
    image = image.convert("RGB")
    if image.width > ANALYSIS_WIDTH:
        h = max(2, round(image.height * ANALYSIS_WIDTH / image.width))
        image = image.resize((ANALYSIS_WIDTH, h), Image.Resampling.LANCZOS)
    return _letterbox_crop(np.asarray(image))


def load_image_pixels(paths: list[Path]) -> list[np.ndarray]:
    frames = []
    for path in paths:
        with Image.open(path) as img:
            frames.append(_downscale(img))
    return frames


def load_video_pixels(path: Path, frame_count: int | None) -> list[np.ndarray]:
    for tool in ("ffprobe", "ffmpeg"):
        if not shutil.which(tool):
            sys.exit(f"error: {tool} not found on PATH (required for video input)")
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height:format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    if probe.returncode != 0:
        sys.exit(f"error: ffprobe failed: {probe.stderr.strip()}")
    try:
        fields = [f for f in probe.stdout.replace(",", "\n").split() if f and f != "N/A"]
        width, height = int(fields[0]), int(fields[1])
        duration = float(fields[2])
    except (IndexError, ValueError):
        sys.exit("error: could not read video dimensions/duration")
    count = frame_count or int(np.clip(round(duration / 2.0), 24, 120))
    start, end = duration * 0.02, duration * 0.98
    span = max(end - start, 0.1)
    target_h = max(2, round(height * ANALYSIS_WIDTH / width / 2) * 2)
    result = subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error",
         "-ss", f"{start:.4f}", "-t", f"{span:.4f}", "-i", str(path),
         "-map", "0:v:0", "-an", "-sn",
         "-vf", f"fps={count / span:.10f}:round=up,scale={ANALYSIS_WIDTH}:{target_h}:flags=lanczos",
         "-frames:v", str(count), "-pix_fmt", "rgb24", "-f", "rawvideo", "pipe:1"],
        capture_output=True,
    )
    if result.returncode != 0:
        sys.exit(f"error: ffmpeg failed: {result.stderr.decode(errors='replace').strip()}")
    frame_bytes = ANALYSIS_WIDTH * target_h * 3
    n = len(result.stdout) // frame_bytes
    if n < 1:
        sys.exit("error: ffmpeg decoded zero frames")
    raw = np.frombuffer(result.stdout[: n * frame_bytes], dtype=np.uint8)
    frames = raw.reshape(n, target_h, ANALYSIS_WIDTH, 3)
    return [_letterbox_crop(frames[i]) for i in range(n)]


# ---------------------------------------------------------------------------
# Palette extraction
# ---------------------------------------------------------------------------


def collect_observations(frames: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    """Stack all frame pixels into Lab points with per-frame-equal weights."""
    labs, weights = [], []
    for pixels in frames:
        flat = pixels.reshape(-1, 3)
        lab = rgb_to_lab(flat)
        # Yeguozi palettes give near-black less share than its true pixel
        # area, and almost never keep blown-out whites: damp both extremes.
        damp = np.interp(lab[:, 0], [0, 8, 18, 85, 95, 100], [0.4, 0.55, 1.0, 1.0, 0.6, 0.45])
        labs.append(lab)
        weights.append(damp / (len(flat) * len(frames)))
    lab = np.concatenate(labs)
    weight = np.concatenate(weights)
    if len(lab) > MAX_SAMPLES:
        stride = len(lab) // MAX_SAMPLES + 1
        lab, weight = lab[::stride], weight[::stride]
    return lab, weight


def weighted_kmeans(points: np.ndarray, weights: np.ndarray, k: int, iters: int = 30) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(20260801)
    centers = [points[rng.integers(len(points))]]
    for _ in range(k - 1):
        d2 = np.min(
            np.stack([((points - c) ** 2).sum(axis=1) for c in centers]), axis=0
        )
        prob = d2 * weights
        total = prob.sum()
        if total <= 0:  # fewer distinct colors than k (e.g. flat test clips)
            break
        centers.append(points[rng.choice(len(points), p=prob / total)])
    c = np.array(centers)
    k = len(c)
    for _ in range(iters):
        dist = ((points[:, None, :] - c[None, :, :]) ** 2).sum(-1)
        label = dist.argmin(1)
        new_c = np.array(
            [
                np.average(points[label == i], axis=0, weights=weights[label == i])
                if (label == i).any()
                else c[i]
                for i in range(k)
            ]
        )
        if np.allclose(new_c, c, atol=1e-3):
            c = new_c
            break
        c = new_c
    dist = ((points[:, None, :] - c[None, :, :]) ** 2).sum(-1)
    label = dist.argmin(1)
    share = np.array([weights[label == i].sum() for i in range(k)])
    keep = share > 0
    return c[keep], share[keep]


def merge_by_delta_e(centers: np.ndarray, shares: np.ndarray, threshold: float) -> tuple[np.ndarray, np.ndarray]:
    """Agglomerative merge of cluster centers whose CIEDE2000 gap < threshold."""
    centers = [c.copy() for c in centers]
    shares = list(shares)
    while len(centers) > 1:
        arr = np.array(centers)
        de = delta_e_2000(arr[:, None, :], arr[None, :, :])
        np.fill_diagonal(de, np.inf)
        i, j = np.unravel_index(np.argmin(de), de.shape)
        if de[i, j] >= threshold:
            break
        total = shares[i] + shares[j]
        centers[i] = (centers[i] * shares[i] + centers[j] * shares[j]) / total
        shares[i] = total
        del centers[j], shares[j]
    return np.array(centers), np.array(shares)


def soften(lab: np.ndarray) -> np.ndarray:
    """Compress chroma/lightness into the muted gamut seen across yeguozi.

    The archive shows the chroma envelope depends on lightness (p90 by L band):
    shadows and highlights stay quiet, midtones may reach the mid 30s.
    """
    l, a, b = lab
    chroma = float(np.hypot(a, b))
    knee = float(np.interp(l, [0, 15, 30, 45, 60, 75, 90, 100], [14, 26, 35, 38, 35, 25, 20, 16]))
    if chroma > knee:
        scale = (knee + (chroma - knee) * 0.35) / chroma
        a, b = a * scale, b * scale
    l = float(np.clip(l, 3.5, 91.0))
    return np.array([l, a, b])


def largest_remainder(weights: np.ndarray, decimals: int = 1) -> list[float]:
    scale = 10**decimals
    ticks = weights / weights.sum() * 100 * scale
    base = np.floor(ticks).astype(int)
    for index in np.argsort(-(ticks - base), kind="stable")[: round(100 * scale - base.sum())]:
        base[index] += 1
    return [v / scale for v in base]


def extract_palette(frames: list[np.ndarray], colors: int, merge_threshold: float) -> list[dict]:
    points, weights = collect_observations(frames)
    centers, shares = weighted_kmeans(points, weights, k=max(colors + 6, 12))
    centers, shares = merge_by_delta_e(centers, shares, merge_threshold)
    order = np.argsort(-shares)[:colors]
    centers, shares = centers[order], shares[order]
    pcts = largest_remainder(shares)
    palette = []
    for lab, pct in zip(centers, pcts):
        rgb = lab_to_rgb(soften(lab))
        palette.append(
            {"hex": "#{:02X}{:02X}{:02X}".format(*rgb), "rgb": tuple(int(v) for v in rgb), "pct": pct}
        )
    return palette


def random_palette(colors: int, seed: int | None = None) -> list[dict]:
    """Invent a film-like palette inside the same muted gamut as real extractions.

    Colors share an analogous hue arc with an occasional counter-hue accent,
    lightness spans dark-to-light, and chroma stays under the per-L envelope.
    """
    rng = np.random.default_rng(seed)
    base_hue = rng.uniform(0, 360)
    arc = rng.uniform(35, 80)  # analogous spread
    accents = rng.random() < 0.6  # some palettes get a complementary accent

    labs = []
    for i in range(colors):
        if accents and i > 0 and rng.random() < 0.18:
            hue = (base_hue + 180 + rng.normal(0, 20)) % 360
        else:
            hue = (base_hue + rng.uniform(-arc, arc)) % 360
        # bias lightness toward shadows/midtones like real film palettes
        l = float(np.clip(rng.beta(1.7, 2.2) * 95, 5, 90))
        knee = float(np.interp(l, [0, 15, 30, 45, 60, 75, 90, 100], [14, 26, 35, 38, 35, 25, 20, 16]))
        chroma = rng.uniform(0.15, 1.0) * knee
        rad = np.radians(hue)
        labs.append([l, chroma * np.cos(rad), chroma * np.sin(rad)])

    # descending weights with a dominant head, like real extractions
    raw = np.sort(rng.dirichlet(np.full(colors, 1.1)))[::-1] * 100
    pcts = largest_remainder(raw)
    palette = []
    for lab, pct in zip(labs, pcts):
        rgb = lab_to_rgb(np.array(lab))
        palette.append(
            {"hex": "#{:02X}{:02X}{:02X}".format(*rgb), "rgb": tuple(int(v) for v in rgb), "pct": pct}
        )
    return palette


# ---------------------------------------------------------------------------
# Poetic title generation
# ---------------------------------------------------------------------------

# Titles are composed as 「<prefix>的<noun>与<noun>」, e.g. 暮色的港湾与信笺.
# Prefixes follow the palette's lightness tier; nouns follow its hue families.
# All entries are concrete two-character imagery words chosen to combine
# naturally in this pattern; picks never repeat a character across the title.
_TIER_PREFIXES = (
    ("夜航", "深巷", "暮色", "雨夜", "炉边", "长夜", "子夜", "灯下", "晚风", "暗房"),  # dark
    ("黄昏", "雾中", "午后", "旧城", "晚照", "巷口", "薄暮", "渡口", "老街", "途中"),  # mid
    ("清晨", "初晴", "薄雾", "晴日", "春晓", "微光", "破晓", "晨风", "假日", "雪后"),  # light
)
_FAMILY_NOUNS = {
    "neutral": ("墨痕", "银盐", "石阶", "素笺", "灰瓦", "卵石", "炊烟", "旧照"),
    "red":     ("胭脂", "蔷薇", "红叶", "绛纱", "石榴", "朱砂", "灯笼", "砖墙"),
    "amber":   ("琥珀", "陶土", "焦糖", "麦浪", "旧书", "胡桃", "落叶", "皮箱"),
    "yellow":  ("蜂蜜", "稻田", "烛火", "柠檬", "金箔", "麦穗", "暖灯", "杏子"),
    "green":   ("苔径", "青梅", "山林", "薄荷", "新叶", "松针", "竹影", "橄榄"),
    "cyan":    ("青瓷", "湖心", "汽水", "浅滩", "潮汐", "冰川", "水岸", "雾凇"),
    "blue":    ("港湾", "深海", "信笺", "蓝调", "星图", "远洋", "群岛", "夜空"),
    "purple":  ("紫藤", "丁香", "暮霭", "云母", "夜曲", "鸢尾", "葡萄", "暮雨"),
    "pink":    ("樱雨", "蜜桃", "山茶", "绯云", "苏打", "杏花", "珊瑚", "晚霞"),
    "contrast": ("季风", "霓虹", "日落", "灯火", "潮声", "烟火", "车站", "码头"),
}


def _pick(words, seed: int, used_chars: set[str], exclude: frozenset[str] = frozenset()) -> str:
    """Deterministic pick avoiding used characters and excluded words."""
    pool = [w for w in words if w not in exclude and not (set(w) & used_chars)]
    if not pool:
        pool = [w for w in words if not (set(w) & used_chars)] or list(words)
    return pool[seed % len(pool)]


# Night-flavored nouns clash with morning/daylight prefixes (light tier).
_NIGHT_NOUNS = frozenset({"夜空", "夜曲", "星图", "烛火", "暖灯", "灯笼", "灯火", "霓虹", "暮霭", "暮雨", "晚霞"})


def _hue_family(hue_deg: float) -> str:
    for family, upper in (("red", 15), ("amber", 45), ("yellow", 70), ("green", 160),
                          ("cyan", 200), ("blue", 250), ("purple", 290), ("pink", 345)):
        if hue_deg < upper:
            return family
    return "red"


def poetic_title(palette: list[dict]) -> str:
    """Compose a deterministic title as 「<prefix>的<noun>与<noun>」.

    The prefix follows the palette's lightness tier; the two nouns follow the
    dominant and secondary hue families, so the title mirrors what the card
    actually contains.
    """
    weights = np.array([s["pct"] for s in palette], dtype=float)
    labs = rgb_to_lab(np.array([s["rgb"] for s in palette], dtype=float))
    chroma = np.hypot(labs[:, 1], labs[:, 2])
    l_avg = float(np.average(labs[:, 0], weights=weights))

    chromatic = chroma >= 10.0
    family_share: dict[str, float] = {}
    warm = cool = 0.0
    import colorsys

    for swatch, w, is_chromatic in zip(palette, weights, chromatic):
        if not is_chromatic:
            family_share["neutral"] = family_share.get("neutral", 0.0) + w
            continue
        r, g, b = (v / 255 for v in swatch["rgb"])
        hue = colorsys.rgb_to_hsv(r, g, b)[0] * 360.0
        family = _hue_family(hue)
        family_share[family] = family_share.get(family, 0.0) + w
        if family in ("red", "amber", "yellow", "pink"):
            warm += w
        else:
            cool += w

    total = float(weights.sum())
    ranked = sorted(family_share.items(), key=lambda kv: -kv[1])
    first = ranked[0][0]
    # Strong warm/cool split reads as a contrast palette.
    if first != "neutral" and ranked[0][1] < total * 0.5 and warm > total * 0.3 and cool > total * 0.3:
        first = "contrast"
    # Secondary noun: next family with a meaningful share, else same family.
    second = next(
        (name for name, share in ranked if name != first and share >= total * 0.12),
        first,
    )

    tier = 0 if l_avg < 32 else (1 if l_avg < 58 else 2)
    flat = [v for s in palette for v in s["rgb"]]
    seed_prefix = sum(v * (i + 1) for i, v in enumerate(flat))
    seed_a = sum(flat)
    seed_b = sum(v * v for v in flat)

    prefix = _TIER_PREFIXES[tier][seed_prefix % len(_TIER_PREFIXES[tier])]
    exclude = _NIGHT_NOUNS if tier == 2 else frozenset()
    noun_a = _pick(_FAMILY_NOUNS[first], seed_a, set(prefix), exclude)
    noun_b = _pick(
        [n for n in _FAMILY_NOUNS[second] if n != noun_a],
        seed_b,
        set(prefix) | set(noun_a),
        exclude,
    )
    return f"{prefix}的{noun_a}与{noun_b}"


# ---------------------------------------------------------------------------
# Card rendering
# ---------------------------------------------------------------------------

PAPER = (245, 241, 231)
INK = (56, 52, 44)
MUTED = (138, 131, 117)


def _font(size: int, mono: bool = False, cjk: bool = False) -> ImageFont.FreeTypeFont:
    # Entries are either "path" or ("path", ttc_index). Noto CJK .ttc files
    # pack JP/KR/SC/TC/HK faces in that order, so SC needs index 2.
    if cjk:
        candidates = [
            # macOS: Songti SC (serif, matches the card's paper tone)
            "/System/Library/Fonts/Supplemental/Songti.ttc",
            "/System/Library/Fonts/Hiragino Sans GB.ttc",
            "/System/Library/Fonts/STHeiti Light.ttc",
            # Linux: Noto Serif CJK SC preferred, then Sans, then WQY
            ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 2),
            ("/usr/share/fonts/noto-cjk/NotoSerifCJK-Regular.ttc", 2),
            ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 2),
            ("/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc", 2),
            "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
            "/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc",
        ]
    elif mono:
        candidates = [
            "/System/Library/Fonts/Menlo.ttc",
            "/System/Library/Fonts/Monaco.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
            "/usr/share/fonts/dejavu/DejaVuSansMono.ttf",
        ]
    else:
        candidates = [
            "/System/Library/Fonts/HelveticaNeue.ttc",
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        ]
    for entry in candidates:
        path, index = entry if isinstance(entry, tuple) else (entry, 0)
        if Path(path).is_file():
            try:
                return ImageFont.truetype(path, size=size, index=index)
            except OSError:  # e.g. requested ttc index missing in this build
                continue
    return ImageFont.load_default(size=size)


def render_card(
    palette: list[dict],
    output: Path,
    logo: Path | None = None,
    title: str | None = None,
) -> str:
    """Horizontal share card: up to 6 equal-width columns + title/logo bar.

    Returns the title actually drawn on the card (may be "" when disabled),
    so callers can echo it to stdout — downstream agents must copy it
    verbatim instead of inventing one.
    """
    width, height = 1920, 1140
    bar_h = 120  # bottom strip holds the logo (or stays blank)
    block_h = height - bar_h
    swatches = palette[:6]

    card = Image.new("RGB", (width, height), PAPER)
    draw = ImageDraw.Draw(card)

    hex_font = _font(45, mono=True)
    pct_font = _font(39)
    col_w = width / len(swatches)
    for i, swatch in enumerate(swatches):
        x0 = round(i * col_w)
        x1 = width if i == len(swatches) - 1 else round((i + 1) * col_w)
        draw.rectangle([x0, 0, x1, block_h], fill=swatch["rgb"])
        # readable label color against this swatch
        r, g, b = (v / 255 for v in swatch["rgb"])
        luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
        label = (246, 240, 231) if luma < 0.45 else (35, 32, 27)
        cx = (x0 + x1) // 2
        hex_text = swatch["hex"]
        pct_text = f"{swatch['pct']:.1f}%"
        hw = draw.textbbox((0, 0), hex_text, font=hex_font)[2]
        pw = draw.textbbox((0, 0), pct_text, font=pct_font)[2]
        draw.text((cx - hw // 2, block_h - 162), hex_text, font=hex_font, fill=label)
        draw.text((cx - pw // 2, block_h - 93), pct_text, font=pct_font, fill=label)

    if title is None:
        title = poetic_title(palette)
    if title:
        cjk = any("⺀" <= ch <= "鿿" for ch in title)
        title_font = _font(42, cjk=cjk)
        if not cjk:
            title = title.upper()
        bbox = draw.textbbox((0, 0), title, font=title_font)
        draw.text(
            (60, block_h + (bar_h - (bbox[3] - bbox[1])) // 2 - bbox[1]),
            title,
            font=title_font,
            fill=INK,
        )

    if logo and logo.is_file():
        with Image.open(logo) as mark:
            mark = mark.convert("RGBA")
            target_h = 60
            target_w = round(mark.width * target_h / mark.height)
            mark = mark.resize((target_w, target_h), Image.Resampling.LANCZOS)
            card.paste(
                mark, (width - target_w - 60, block_h + (bar_h - target_h) // 2), mark
            )

    output.parent.mkdir(parents=True, exist_ok=True)
    card.save(output, format="PNG")
    return title or ""


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


# Naming-family boundaries and word pools mirror references/palette-usage.md
# §四 exactly: agents copy the printed family AND pick only from the printed
# candidates instead of recalling the vocabulary (recall drifts near borders).
_NAMING_FAMILIES = (
    ("橙/棕", 15, 45), ("黄", 45, 70), ("绿", 70, 160), ("青", 160, 200),
    ("蓝", 200, 250), ("紫", 250, 290), ("粉", 290, 345),
)
_FAMILY_WORDS = {
    "红": "绯红/酒红/砖红/朱砂",
    "橙/棕": "焦糖/陶土/琥珀/暖铜棕/胡桃棕/咖啡棕/枯棕",
    "黄": "芥末黄/蜂蜜金/奶油黄",
    "绿": "橄榄绿/薄荷绿/苔绿/松针绿/橄榄褐绿",
    "青": "青瓷/湖蓝/雾青",
    "蓝": "钴蓝/藏蓝/蓝灰/江墨蓝",
    "紫": "雾紫/薰衣草紫/葡萄紫",
    "粉": "烟粉/蜜桃粉/珊瑚粉",
    "中性": "炭灰/暖米灰/灰绿/雾灰/浅沙",
}
_PALE_WORDS = "米白/浅沙/奶油黄/雾白"  # high-lightness colors read pale, not deep


def naming_family(rgb) -> tuple[str, str, str]:
    """Return (hls_label, family, candidates) for stdout.

    e.g. ('H341 L34 S33', '粉', '烟粉/蜜桃粉/珊瑚粉'). The candidates string is
    the ONLY pool the agent may name the color from.
    """
    import colorsys

    r, g, b = (v / 255 for v in rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    hue, light, sat = h * 360, l * 100, s * 100
    label = f"H{hue:03.0f} L{light:02.0f} S{sat:02.0f}"
    if light < 12:
        return label, "近黑", "墨黑/炭灰（禁叠明度前缀）"
    if light > 92:
        return label, "近白", "雾白/米白（禁叠明度前缀）"
    if sat < 10:
        return label, "中性", _FAMILY_WORDS["中性"]
    family = "红"
    for name, lo, hi in _NAMING_FAMILIES:
        if lo <= hue < hi:
            family = name
            break
    if light > 75:  # pale tints read as cream/off-white, not as deep hues
        return label, family, _PALE_WORDS
    return label, family, _FAMILY_WORDS[family]


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Extract a film-style palette from a video clip or images and render "
            "a shareable PNG card (up to 6 equal-width colors, hex + share labels, "
            "poetic title bottom-left, logo bottom-right)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  %(prog)s clip.mp4 -o card.png              analyze one video
  %(prog)s a.jpg b.png c.webp -o card.png    analyze several images
  %(prog)s clip.mp4 --frames 120             denser video sampling
  %(prog)s a.jpg --title "花样年华"           custom title
  %(prog)s a.jpg --title '' --logo ''        no title, no logo
  %(prog)s --random -o card.png              invent a random palette
  %(prog)s --random 42 -o card.png           reproducible random palette

notes:
  - video needs ffmpeg/ffprobe on PATH; images only need numpy + Pillow
  - the terminal prints the full extracted palette; the card shows top 6
  - default logo: pippit-logo.png next to this script (missing file = blank)
""",
    )
    parser.add_argument("inputs", nargs="*", help="one video file, or one or more image files")
    parser.add_argument("-o", "--output", default="palette-card.png", help="output PNG path (default: %(default)s)")
    parser.add_argument("--colors", type=int, default=10, help="colors to extract; card shows top 6 (default: %(default)s)")
    parser.add_argument("--frames", type=int, default=None, help="video frames to sample (default: auto, ~1 per 2s, 24-120)")
    parser.add_argument("--merge", type=float, default=10.0, help="CIEDE2000 merge threshold; higher = fewer, broader colors (default: %(default)s)")
    parser.add_argument(
        "--random",
        nargs="?",
        const=-1,
        default=None,
        type=int,
        metavar="SEED",
        help="invent a palette instead of reading inputs; optional integer seed for reproducibility",
    )
    parser.add_argument(
        "--logo",
        default=str(Path(__file__).with_name("pippit-logo.png")),
        help="PNG logo for the bottom-right corner; '' disables (default: pippit-logo.png beside the script)",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="bottom-left text; default auto-generates a poetic name from the palette, '' disables",
    )
    args = parser.parse_args()

    if args.random is not None:
        if args.inputs:
            sys.exit("error: --random takes no input files")
        seed = None if args.random == -1 else args.random
        palette = random_palette(colors=max(2, args.colors), seed=seed)
        print("invented a random palette" + (f" (seed={seed})" if seed is not None else ""))
    else:
        if not args.inputs:
            sys.exit("error: pass input files, or use --random")
        paths = [Path(p).expanduser() for p in args.inputs]
        for path in paths:
            if not path.is_file():
                sys.exit(f"error: input does not exist: {path}")
        is_video = [p.suffix.lower() in VIDEO_SUFFIXES for p in paths]
        if any(is_video):
            if len(paths) > 1:
                sys.exit("error: pass exactly one video, or multiple images (not both)")
            frames = load_video_pixels(paths[0], args.frames)
        else:
            frames = load_image_pixels(paths)
        print(f"sampled {len(frames)} frame(s)")
        palette = extract_palette(frames, colors=max(2, args.colors), merge_threshold=args.merge)

    for swatch in palette:
        hls, family, words = naming_family(swatch["rgb"])
        print(f"  {swatch['hex']}  {swatch['pct']:5.1f}%  {hls}  {family}  可选色名:{words}")

    output = Path(args.output).expanduser()
    card_title = render_card(
        palette,
        output,
        logo=Path(args.logo).expanduser() if args.logo else None,
        title=args.title,
    )
    if card_title:
        print(f"title: {card_title}")
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
