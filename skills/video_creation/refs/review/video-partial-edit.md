# 段内区间局部编辑

> 由 `review/post-delivery.md` §E3 路由至此。**仅适用于单段直出视频或用户上传的现有视频**——多段项目成片的段内修改走 §R/§B1 处理该段，禁止用本流程肢解已拼接的成片。

对视频中间某个时间段重新生成并替换。以下以源视频 `input.mp4` 共 15s、编辑 4s–8s 区间为例，ffmpeg 命令**逐字复制，只替换路径与数值**。

## 流程

1. **切分**：用 ffmpeg 把源视频切成 头段 / 待编辑段 / 尾段，全部放 `assets/`：

```bash
ffmpeg -hide_banner -loglevel error -y -ss 0 -to 4 -i input.mp4 -c copy assets/pre.mp4
ffmpeg -hide_banner -loglevel error -y -ss 4 -to 8 -i input.mp4 -c copy assets/mid.mp4
ffmpeg -hide_banner -loglevel error -y -ss 8 -i input.mp4 -c copy assets/post.mp4
```

切分后用 ffprobe 确认各段实际时长（`-c copy` 切点吸附到最近关键帧，与指定时间可能有零点几秒偏差）：

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1 assets/pre.mp4
```

2. **编辑中间段**：调用 `sandbox_generate_video`：
   - `VideoList`：填待编辑片段路径，即 `assets/mid.mp4`
   - `Prompt`：格式为 `对@视频1进行编辑：{用户要求的编辑描述}`
   - 输出：`assets/mid_edited.mp4`
   - 调用未报错即视为成功，直接进入下一步；禁止换写法/换参数重复生成多版后自行挑选

3. **拼接**：用 `render_video` 收口（禁止用 ffmpeg concat 拼接）：

```
render_video(
  video_paths: ["assets/pre.mp4", "assets/mid_edited.mp4", "assets/post.mp4"],
  output_path: "assets/output.mp4"
)
```

按 `post-delivery.md` 成片状态账本继承 `show_subtitle` / `bgm_audio_path`（如有）。

4. **校验与交付**：ffprobe 确认输出总时长符合预期；`render_video` 产物已自动发送，无需再调 `present_sandbox_file`。

## 规则

- 所有 ffmpeg 命令统一加 `-hide_banner -loglevel error`，只保留错误信息
- ffmpeg 只用于切分与探参；拼接一律走 `render_video`
- 编辑区间在片头（从 0s 起）或片尾（到末尾）时，退化为两段拼接，省略对应的 pre/post 切分
