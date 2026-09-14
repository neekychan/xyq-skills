# 混音与母带工程：动态侧链避让、防爆音与响度标准化

基于 FFmpeg 的工业级多轨音频合成、智能侧链闪避 (Sidechain Ducking) 与声学母带规范。

---

## 一、声学混音铁律

1. **拒绝业余的静态固定音量**：若仅将 BGM 粗暴固定在 0.2 甚至更低，会导致无人声处配乐软弱无力，有人声处又频段打架。**专业制作必须使用动态侧链压缩 (Sidechain Ducking)**：人声出现时 BGM 自动下潜 10~14 dB；人声换气与停歇时 BGM 在 350ms 内平滑回弹。
2. **`amix` 必须显式声明 `normalize=0`**：否则 FFmpeg 会自动将每轨音量除以输入流数量（如两轨各除以 2），导致精心调整的动态电平全盘崩溃。
3. **末端强制串接硬限幅器 (alimiter)**：所有多轨混音管道最终输出前，必须串接限幅器，将 True-Peak 锁定在 -0.45 dBFS (`limit=0.95`)，彻底杜绝数字削波 (Clipping) 爆音。
4. **BGM 收尾必须平滑淡出 (afade ≥ 2s)**：硬切 BGM 是最显眼的业余破绽；拼接段落必须在乐句呼吸点并做微淡化。

---

## 二、双轨工业级混音模板 (旁白 + BGM)

### 1. 动态侧链压制滤镜链 (推荐主干命令)
人声自动触发侧链，控制 BGM 自动避让与呼吸回弹：

```bash
ffmpeg -y -i assets/audio/voice/narration.mp3 -i assets/audio/music/bgm.mp3 -filter_complex \
  "[1:a]volume=0.85[bgm_full]; \
   [0:a]asplit=2[v_mix][v_sc]; \
   [bgm_full][v_sc]sidechaincompress=threshold=0.08:ratio=8:attack=25:release=350[bgm_ducked]; \
   [v_mix]volume=1.0[voice]; \
   [voice][bgm_ducked]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[mix]; \
   [mix]alimiter=limit=0.95:attack=5:release=50:asc=1[master]" \
  -map "[master]" -c:a libmp3lame -b:a 320k assets/audio/mix/final_master.mp3
```

**参数解构**：
- `asplit=2`：将人声一分为二，一路作为主听觉通道，另一路作为侧链触发探测信号。
- `threshold=0.08:ratio=8`：当探测到人声电平，BGM 立即执行 8:1 的强力压缩（衰减约 12dB）。
- `attack=25:release=350`：25ms 极速下潜（不压人声字头），人声结束后 350ms 平滑升回原音量，听感自然如呼吸。
- `duration=first`：整体混音时长对齐第 0 轨（旁白人声），旁白结束即结束。
- `alimiter=limit=0.95`：输出母带防削波保护。

### 2. 静态包络降级回退模板 (Fail-Safe Fallback)
若环境异常或特殊音频引发 sidechain 滤镜错误，回退至经过精准计算的静态平滑包络：

```bash
# 获取人声时长 DUR
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 assets/audio/voice/narration.mp3)
FADE_ST=$(awk "BEGIN {print ($DUR > 2.5) ? $DUR - 2.5 : 0}")

ffmpeg -y -i assets/audio/voice/narration.mp3 -i assets/audio/music/bgm.mp3 -filter_complex \
  "[1:a]volume=0.22,afade=t=in:st=0:d=1.0,afade=t=out:st=${FADE_ST}:d=2.5[bgm_bed]; \
   [0:a]volume=1.0[voice]; \
   [voice][bgm_bed]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[mix]; \
   [mix]alimiter=limit=0.95[out]" \
  -map "[out]" -c:a libmp3lame -b:a 320k assets/audio/mix/final_fallback.mp3
```

---

## 三、三轨混音模板 (旁白 + 关键音效 SFX + BGM)

适用于播客片头、广告短片、广播剧高潮：

```bash
ffmpeg -y -i assets/audio/voice/narration.mp3 \
          -i assets/audio/sfx/impact.mp3 \
          -i assets/audio/music/bgm.mp3 -filter_complex \
  "[0:a]volume=1.0[voice]; \
   [1:a]volume=0.45[sfx]; \
   [2:a]volume=0.8[bgm_raw]; \
   [voice]asplit=2[v_play][v_sc]; \
   [bgm_raw][v_sc]sidechaincompress=threshold=0.08:ratio=7:attack=25:release=350[bgm_duck]; \
   [v_play][sfx][bgm_duck]amix=inputs=3:duration=longest:dropout_transition=0:normalize=0[mix]; \
   [mix]alimiter=limit=0.95:attack=5:release=50:asc=1[master]" \
  -map "[master]" -c:a libmp3lame -b:a 320k assets/audio/mix/final_master.mp3
```

---

## 四、时长适配与无缝平滑循环 (Seamless Looping)

### 1. BGM 短于目标时长（循环拼接）
严禁使用直接 concat 硬拼（接缝处必有断音与节拍撞击）。必须使用 `acrossfade` 进行 1.5s 声学交叉叠化：

```bash
# 两次循环并在中间做 1.5s 叠化（适用于 30s BGM 扩充为 ~58s）
ffmpeg -y -i bgm_short.mp3 -i bgm_short.mp3 -filter_complex \
  "[0:a][1:a]acrossfade=d=1.5:c1=tri:c2=tri[loop]; \
   [loop]afade=t=in:st=0:d=0.05[out]" \
  -map "[out]" -c:a libmp3lame -b:a 320k assets/audio/music/bgm_extended.mp3
```

### 2. 拼接防爆音微淡化
多段音频在切合点若波形不在零点跨越，会出现“咔哒”爆音。每段首尾必须施加 30ms 超微淡入淡出：
```bash
ffmpeg -y -i raw_clip.mp3 -af "afade=t=in:st=0:d=0.03,afade=t=out:st=<时长-0.03>:d=0.03" clean_clip.mp3
```

---

## 五、母带响度标准化 (EBU R128 Loudness)

对于高要求商业客户或播客交付，可对混音成片执行单 pass 响度目标校准（目标 -14 LUFS，适配大多数现代流媒体平台）：

```bash
ffmpeg -y -i assets/audio/mix/final_master.mp3 -af \
  "loudnorm=I=-14:TP=-1.0:LRA=9:measured_I=-20.0,alimiter=limit=0.95" \
  -c:a libmp3lame -b:a 320k assets/audio/mix/final_lufs14.mp3
```

---

## 六、交付前参数核验脚本 (ffprobe)

在执行 `present_sandbox_file` 推送前，执行以下命令获取确切参数以填充交付报告：

```bash
ffprobe -v error -show_entries format=duration,size,bit_rate:stream=sample_rate,channels -of json assets/audio/mix/final_master.mp3
```
- 确认时长与人声/画面时间轴吻合；
- 确认比特率达到 192~320 kbps 高清规格；
- 确认无空文件或 0 字节损坏。
