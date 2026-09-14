# MV Maker 工程执行、音频桥接与成片合成 (mv-render.md)

本文件定义音频预检、黑屏 MP4 临时桥接、原生分段无缝直拼与基于 `beats.md` 歌词时间轴的 FFmpeg 成片合成规范。

---

## 一、音频预检与 25MB 压缩门 (Music Preflight)

当用户上传音频时，若文件超过 25MB，必须使用 FFmpeg 无损降码率压缩并用 FFprobe 校验：

```bash
MV_INPUT_AUDIO="/workspace/upload/input.wav"
MV_COMPRESSED_AUDIO="/workspace/upload/input_compressed.mp3"

# 1. 验证输入音频信息
ffprobe -v error -select_streams a:0 \
  -show_entries format=duration,size:stream=codec_type,codec_name,sample_rate,channels \
  -of json "$MV_INPUT_AUDIO"

# 2. 压缩至 128k MP3
ffmpeg -y -i "$MV_INPUT_AUDIO" -map 0:a:0 -vn \
  -c:a libmp3lame -b:a 128k -ar 44100 -ac 2 \
  "$MV_COMPRESSED_AUDIO"

# 3. 验证压缩文件小于 25MB 且时长未被截断
ffprobe -v error -select_streams a:0 \
  -show_entries format=duration,size:stream=codec_type,codec_name,sample_rate,channels \
  -of json "$MV_COMPRESSED_AUDIO"
```

---

## 二、黑屏 MP4 极速分段切片桥接 (Ultra-Fast Black Audio Bridge)

为了给 Seedance 提供精确的节拍与唱演时间轴，当用户有上传音频时，**必须**将对应分段的音频精确切片制作为黑屏 MP4 并传入 `VideoList`：

```bash
# ⚠️ 极速生成铁律与防卡顿优化（540p @ 1fps + ultrafast 瞬发，耗时 ~0.3s）：
# 1. 严格符合模型最低分辨率门槛（>= 480p/540p），同时兼顾极速编码：
#    - 横屏 16:9：采用 960x540 @ 1fps (540p)
#    - 竖屏 9:16：采用 540x960 @ 1fps (540p)
#    配合 -preset ultrafast -tune stillimage，单段 30s 编码仅需 ~0.3 秒，既完美通过模型输入质检，又杜绝 CPU 软解压卡顿！
# 2. 严禁生成全曲无用的完整黑屏 MP4！多段流程中仅需生成各分段切片；
# 3. 必须使用 -ss 精确偏移到该分段的起始整数秒；
# 4. 最后一小段尾巴若时长不足模型最低限制（通常 >= 4s），直接向上取整生成（如 Duration 设为 4 或 5 秒），
#    通过 apad 补齐静音，末尾多出一两秒画面定格/回味空镜完全合规，不影响母带对齐！

# 单段极速切片标准命令（16:9 横屏示例，耗时约 0.3s）：
ffmpeg -y -ss START_SECONDS -t SEGMENT_DURATION -i "$INPUT_AUDIO" \
  -f lavfi -i color=c=black:s=960x540:r=1 \
  -filter_complex '[0:a:0]apad=whole_dur=GENERATION_SECONDS[a]' \
  -map 1:v:0 -map '[a]' -t GENERATION_SECONDS \
  -c:v libx264 -preset ultrafast -tune stillimage -pix_fmt yuv420p \
  -c:a aac -strict -2 -movflags +faststart "$OUTPUT_SEG_BLACK_MP4"
```

### 多段一次性极速切片单行脚本（16:9 横屏 4 段总耗时 ~1 秒）：
```bash
# 示例：根据 beats.md 规划的 4 段 30 秒分段，单行极速全部切完：
for i in 0 1 2 3; do
  start=$((i * 30))
  ffmpeg -y -ss $start -t 30 -i "/workspace/upload/input.mp3" \
    -f lavfi -i color=c=black:s=960x540:r=1 \
    -map 1:v:0 -map 0:a:0 -t 30 \
    -c:v libx264 -preset ultrafast -tune stillimage -pix_fmt yuv420p \
    -c:a aac -strict -2 -movflags +faststart "/workspace/assets/project/seg_$((i+1))_audio.mp4" 2>/dev/null
done
```

---

## 三、原生视频直拼不剪辑法则（以视频为准，严禁二次硬裁切）

1. **天然对齐，绝不二次剪辑**：
   - 因为我们使用精确切片的黑屏音频驱动生成，视频生成模型产出的画面与音频在节拍、唱演口型上天然严格对齐；
   - **【核心铁律】严禁对模型生成的视频做二次 `-t` 硬裁切或重新编码（`-an`）**！直接将生成的原生视频片段无损串联拼接；
   - **【末端容错法则】如果视频总长与音频母带末端存在轻微毫秒级 gap（例如视频多出 0.5s 或音频稍短），统一「以视频为准」**，保留完整生成的画面，音频自然对齐，杜绝黑屏死画补齐问题。

2. **FFmpeg 纯脚本合成规范**：
   - 成片拼接、原曲母带替换与字幕烧录均在 sandbox 中通过 `sandbox_bash` 执行 FFmpeg 脚本完成，保证合成链路完全透明可控。

---

## 四、全流程 FFmpeg 拼接、歌词字幕烧录与最终交付

### 1. 无字幕模式（极速无损直拼，耗时 < 0.5 秒）

直接使用 FFmpeg `concat` 协议串联所有原生视频片段，并一次性合入原曲母带音轨：

```bash
# 步骤 1：写入 concat 列表文件
cat << 'EOF' > /workspace/assets/concat_list.txt
file '/workspace/assets/project/seg_01.mp4'
file '/workspace/assets/project/seg_02.mp4'
file '/workspace/assets/project/seg_03.mp4'
file '/workspace/assets/project/seg_04.mp4'
EOF

# 步骤 2：FFmpeg 极速混流（视频流无损 copy + 母带音频直接合入）
mkdir -p /workspace/output
ffmpeg -y -f concat -safe 0 -i /workspace/assets/concat_list.txt \
  -i "$ORIGINAL_AUDIO" \
  -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart /workspace/output/final_mv.mp4
```

---

### 2. 电影级左下角先锋动态字幕模式（基于 beats.md 事实源直接烧录）

若用户要求添加歌词字幕，**严禁依赖平台 ASR 自动转写**（ASR 易出错别字或时间轴漂移），直接根据 Phase 1 已校准的 `beats.md` 歌词时间轴生成 `.ass` 高阶动态字幕文件（或 `.srt`），并通过 FFmpeg 烧录**左下角先锋排版与毫秒级淡入淡出动效**：

#### 方案 A（推荐）：ASS 格式（支持左下对齐 + 250ms 丝滑淡入淡出 + 柔和暗阴影）

```bash
# 步骤 1：根据 beats.md 歌词时间轴生成 /workspace/assets/lyrics.ass
cat << 'EOF' > /workspace/assets/lyrics.ass
[Script Info]
Title: Modern Left-Aligned MV Subtitles
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
; MV_Left (中文): 左下角对齐(Alignment=1)，思源黑体Noto Sans CJK SC，字号40，字距2.0，细黑边+柔暗阴影
Style: MV_Left,Noto Sans CJK SC,40,&H00FFFFFF,&H000000FF,&H00151515,&H70000000,-1,0,0,0,100,100,2.0,0,1,1.2,2.0,1,100,100,90,1
; MV_Left_JP (日文/J-Pop/动态漫): Noto Sans CJK JP
Style: MV_Left_JP,Noto Sans CJK JP,40,&H00FFFFFF,&H000000FF,&H00151515,&H70000000,-1,0,0,0,100,100,2.0,0,1,1.2,2.0,1,100,100,90,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
; \fad(250,200) 实现 250ms 丝滑淡入 + 200ms 优雅淡出
Dialogue: 0,0:00:06.04,0:00:11.44,MV_Left,,0,0,0,,{\fad(250,200)}小满那天 你带了一瓶酒
Dialogue: 0,0:00:11.44,0:00:15.94,MV_Left,,0,0,0,,{\fad(200,200)}说要请南方的风 喝一杯
Dialogue: 0,0:00:17.40,0:00:21.70,MV_Left,,0,0,0,,{\fad(200,200)}我攒了一口袋的话要讲
Dialogue: 0,0:00:22.68,0:00:27.66,MV_Left,,0,0,0,,{\fad(200,250)}风一吹 全撒了
EOF

# 步骤 2：FFmpeg 拼接并烧录 ASS 动态字幕
mkdir -p /workspace/output
ffmpeg -y -f concat -safe 0 -i /workspace/assets/concat_list.txt \
  -i "$ORIGINAL_AUDIO" \
  -vf "ass=/workspace/assets/lyrics.ass" \
  -map 0:v:0 -map 1:a:0 \
  -c:v libx264 -preset fast -crf 18 -c:a aac -b:a 320k \
  -movflags +faststart /workspace/output/final_mv.mp4
```

#### 方案 B：SRT + force_style 左下角现代排版（兼容回退）

```bash
# 步骤 1：生成 /workspace/assets/lyrics.srt
cat << 'EOF' > /workspace/assets/lyrics.srt
1
00:00:06,040 --> 00:00:11,440
小满那天 你带了一瓶酒

2
00:00:11,440 --> 00:00:15,940
说要请南方的风 喝一杯
EOF

# 步骤 2：FFmpeg 烧录左下角先锋排版（Alignment=1, MarginL=100, MarginV=90, Spacing=2）
ffmpeg -y -f concat -safe 0 -i /workspace/assets/concat_list.txt \
  -i "$ORIGINAL_AUDIO" \
  -vf "subtitles=/workspace/assets/lyrics.srt:force_style='Fontname=Noto Sans CJK SC,FontSize=20,PrimaryColour=&H00FFFFFF&,OutlineColour=&H00151515&,BackColour=&H70000000&,Outline=1.2,Shadow=2.0,Alignment=1,MarginL=60,MarginV=50,Spacing=2.0'" \
  -map 0:v:0 -map 1:a:0 \
  -c:v libx264 -preset fast -crf 18 -c:a aac -b:a 320k \
  -movflags +faststart /workspace/output/final_mv.mp4
```

---

### 3. 最终交付门禁

成片合成完毕后，执行检查并推送：
- [ ] 检查 `/workspace/output/final_mv.mp4` 存在且体积正常；
- [ ] 确认全部分段首尾相接、画音同步、无黑屏空洞；
- [ ] 调用 `present_sandbox_file(filepath="/workspace/output/final_mv.mp4", interrupt=true)` 向用户交付最终 MV！
