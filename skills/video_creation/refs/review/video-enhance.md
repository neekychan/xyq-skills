# 视频增强（超分 / 擦除字幕）

> 由 `review/post-delivery.md` §E1/§E2 路由至此。两类操作都是对现有视频的一次 `sandbox_process_video` 调用。

## sandbox_process_video

| 参数 | 说明 |
|------|------|
| `VideoList` | 待处理视频文件路径列表（sandbox 路径，非 URL） |
| `ToolName` | 超分填 `video_super_resolution`；擦字幕填 `erase_video_subtitle` |
| `Description` | 本次操作描述 |
| `ToolParam.VideoSuperResolutionToolParam.OutputResolution` | 仅超分时使用，枚举 `720p/1080p/2k/4k` |

## 使用规则

- **超分**：`OutputResolution` 必须高于源视频分辨率，仅支持向上超分。源分辨率不明时先用 `sandbox_bash` ffprobe 探查：`ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1 {视频路径}`。用户要求的目标 ≤ 源分辨率时不可调用，如实告知。**超分只走本工具，禁止用 ffmpeg scale 拉伸像素冒充超分**——放大不增加细节，属于欺骗性交付。**一次调用直达用户要求的目标分辨率即停**，用户未要求时默认 1080p；禁止链式追加超分（1080p→2K→4K），超出目标的追加处理浪费用户等待时间且用户未授权
- **擦字幕**：无需额外参数。仅擦除画面内已烧录的字幕；`render_video` 叠加的字幕走 `post-delivery.md` §A3 开关重拼，不走本工具
- 调用返回未报错即视为成功，禁止 ffprobe 复核结果后自行重试或换 ffmpeg 降级实现
- 本工具仅用于 AI 增强类处理（超分、擦字幕）。降分辨率/缩放/转码等常规操作不属于成片后处理范围，不走本工具
- 处理完成后用 `present_sandbox_file` 将结果发送给用户
