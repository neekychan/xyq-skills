#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""render_storyboard.py — 关键帧故事版绘制（JSON → 每段一张 PNG）

用法:
  python3 gen_storyboard.py --input storyboard.json --out-dir assets/marketing [--font /path/to/cjk.ttf]

输入 JSON 结构:
{
  "title": "整条视频的标题",
  "consistency": "角色与一致性说明（跨镜形象/音色锚点）",
  "visual_mood": "视觉与情绪说明",
  "tech_spec": "技术规格说明（分镜数/总时长/画幅/字幕策略，字幕只在渲染阶段添加）",
  "segments": [
    {
      "segment_index": 1,
      "time_range": "00:00-00:15",
      "shots": [
        {
          "index": 1,
          "time_range": "00:00-00:02.5",
          "image": "assets/marketing/keyframe_1.png",
          "shot_size": "近景",
          "beat": "Hook 悬念提问",
          "action": "画面动作……",
          "product": "产品露出……",
          "transition": "镜头转场……",
          "sound": "声音……",
          "voiceover": "口播……"
        }
      ]
    }
  ]
}

输出: <out-dir>/storyboard_seg1.png、storyboard_seg2.png …（每个生成段一张）
"""
import argparse
import json
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

COL_W = 560          # 每列宽
FOOTER_MIN_W = 620   # 底部总结块每块最小宽度（保证三块横排时内容完整可见）
PAD = 24             # 画布外边距
GAP = 16             # 列间距
HEADER_H = 64        # 序号+时间条
BEAT_H = 56          # 景别+节拍行
FIELDS = [("画面动作", "action"), ("产品露出", "product"),
          ("镜头转场", "transition"), ("声音", "sound"), ("口播", "voiceover")]
BG = "#ffffff"
DARK = "#1f2430"
LABEL = "#6b7280"
ACCENT = "#b91c1c"
LINE = "#e5e7eb"


def find_cjk_font():
    try:
        out = subprocess.run(["fc-list", ":lang=zh", "file"],
                             capture_output=True, text=True, timeout=15).stdout
        for line in out.splitlines():
            p = line.strip().rstrip(":")
            if p and os.path.exists(p):
                return p
    except Exception:
        pass
    for p in ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
              "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.otf",
              "/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc",
              "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
              "/usr/share/fonts/truetype/arphic/uming.ttc"):
        if os.path.exists(p):
            return p
    return None


def wrap(draw, text, font, max_w):
    """按像素宽逐字符换行（兼容无空格的中文）。"""
    lines = []
    for para in str(text or "").split("\n"):
        if not para:
            lines.append("")
            continue
        cur = ""
        for ch in para:
            if draw.textlength(cur + ch, font=font) <= max_w:
                cur += ch
            else:
                lines.append(cur)
                cur = ch
        lines.append(cur)
    return lines


def text_h(draw, text, font, max_w, lh):
    return len(wrap(draw, text, font, max_w)) * lh


def render_segment(seg, spec, font_path, out_path, is_last):
    shots = seg["shots"]
    f_num = ImageFont.truetype(font_path, 30)
    f_time = ImageFont.truetype(font_path, 24)
    f_beat = ImageFont.truetype(font_path, 24)
    f_label = ImageFont.truetype(font_path, 22)
    f_body = ImageFont.truetype(font_path, 22)
    f_title = ImageFont.truetype(font_path, 34)
    lh = 34  # 正文行高

    probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    inner_w = COL_W - 2 * 20

    # 关键帧图统一缩放到列宽，取最高的一张定图区高度
    imgs = []
    img_h_max = 0
    for s in shots:
        im = Image.open(s["image"]).convert("RGB")
        h = round(im.height * COL_W / im.width)
        im = im.resize((COL_W, h))
        imgs.append(im)
        img_h_max = max(img_h_max, h)

    # 字段区高度按本段最高的一列计算
    fields_h = 0
    for s in shots:
        h = 0
        for label, key in FIELDS:
            h += lh  # label 行
            h += text_h(probe, s.get(key, ""), f_body, inner_w, lh)
            h += 10
        fields_h = max(fields_h, h)

    footer_h = 0
    n = len(shots)
    # 列数够时底部总结块三块横排，太窄（如单镜段）时竖排全宽
    footer_stack = n < 3
    # 仅横排模式需要画布宽度下限：每块至少 FOOTER_MIN_W 宽，保证内容完整可见
    W = PAD * 2 + n * COL_W + (n - 1) * GAP
    if not footer_stack:
        W = max(W, PAD * 2 + 3 * FOOTER_MIN_W + 2 * GAP)
    bw = (W - PAD * 2 - GAP * 2) // 3
    if is_last:
        if footer_stack:
            bw = W - PAD * 2
            for key in ("consistency", "visual_mood", "tech_spec"):
                footer_h += lh + text_h(probe, spec.get(key, ""), f_body, bw - 20, lh) + 14
        else:
            blk = 0
            for key in ("consistency", "visual_mood", "tech_spec"):
                blk = max(blk, text_h(probe, spec.get(key, ""), f_body, bw - 20, lh))
            footer_h = blk + lh + 14
        footer_h += 2 * PAD

    title_h = 72
    H = title_h + HEADER_H + img_h_max + BEAT_H + 40 + fields_h + PAD + footer_h
    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)

    # 标题行
    d.text((PAD, 20), spec.get("title", ""), font=f_title, fill=DARK)
    seg_label = "段 %d/%d  %s" % (seg["segment_index"], spec["_seg_total"], seg.get("time_range", ""))
    d.text((W - PAD - d.textlength(seg_label, font=f_time), 28), seg_label, font=f_time, fill=LABEL)

    y0 = title_h
    for i, s in enumerate(shots):
        x = PAD + i * (COL_W + GAP)
        # 序号 + 时间条
        d.rectangle([x, y0, x + COL_W, y0 + HEADER_H], fill=DARK)
        d.text((x + 16, y0 + 14), "%02d" % s.get("index", i + 1), font=f_num, fill="#ffffff")
        tr = s.get("time_range", "")
        d.text((x + COL_W - 16 - d.textlength(tr, font=f_time), y0 + 18), tr, font=f_time, fill="#ffffff")
        # 关键帧图（顶部对齐，不足高度补白）
        im = imgs[i]
        canvas.paste(im, (x, y0 + HEADER_H))
        if im.height < img_h_max:
            d.rectangle([x, y0 + HEADER_H + im.height, x + COL_W, y0 + HEADER_H + img_h_max], fill="#f3f4f6")
        # 景别 + 节拍行
        yb = y0 + HEADER_H + img_h_max
        d.rectangle([x, yb, x + COL_W, yb + BEAT_H], fill="#f8fafc")
        d.text((x + 16, yb + 13), s.get("shot_size", ""), font=f_beat, fill=DARK)
        beat = s.get("beat", "")
        d.text((x + COL_W - 16 - d.textlength(beat, font=f_beat), yb + 13), beat, font=f_beat, fill=ACCENT)
        # 结构化字段
        yf = yb + BEAT_H + 20
        for label, key in FIELDS:
            d.text((x + 20, yf), label, font=f_label, fill=LABEL)
            yf += lh
            for line in wrap(d, s.get(key, ""), f_body, inner_w):
                d.text((x + 20, yf), line, font=f_body, fill=DARK)
                yf += lh
            yf += 10
        # 列分隔线
        if i > 0:
            d.line([x - GAP // 2, y0, x - GAP // 2, y0 + HEADER_H + img_h_max + BEAT_H + 20 + fields_h], fill=LINE, width=1)

    # 底部总结块（只画在最后一段；列数太窄时竖排全宽，保证内容完整可见）
    if is_last and footer_h:
        yf0 = H - footer_h - PAD + 10
        d.rectangle([0, yf0 - 10, W, H], fill=DARK)
        labels = (("角色与一致性", "consistency"), ("视觉与情绪", "visual_mood"), ("技术规格", "tech_spec"))
        if footer_stack:
            yy = yf0 + 8
            for label, key in labels:
                d.text((PAD, yy), label, font=f_label, fill="#9ca3af")
                yy += lh
                for line in wrap(d, spec.get(key, ""), f_body, bw - 20):
                    d.text((PAD, yy), line, font=f_body, fill="#f9fafb")
                    yy += lh
                yy += 14
        else:
            for i, (label, key) in enumerate(labels):
                x = PAD + i * (bw + GAP)
                d.text((x, yf0 + 8), label, font=f_label, fill="#9ca3af")
                yy = yf0 + 8 + lh
                for line in wrap(d, spec.get(key, ""), f_body, bw - 20):
                    d.text((x, yy), line, font=f_body, fill="#f9fafb")
                    yy += lh

    canvas.save(out_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--font", default=None)
    a = ap.parse_args()
    spec = json.load(open(a.input, encoding="utf-8"))
    font = a.font or find_cjk_font()
    if not font:
        print("ERROR: 找不到 CJK 字体，请用 --font 显式指定", file=sys.stderr)
        sys.exit(2)
    segs = spec.get("segments", [])
    if not segs:
        print("ERROR: segments 为空", file=sys.stderr)
        sys.exit(2)
    spec["_seg_total"] = len(segs)
    os.makedirs(a.out_dir, exist_ok=True)
    for i, seg in enumerate(segs):
        out = os.path.join(a.out_dir, "storyboard_seg%d.png" % seg.get("segment_index", i + 1))
        render_segment(seg, spec, font, out, is_last=(i == len(segs) - 1))
        print(out)


if __name__ == "__main__":
    main()