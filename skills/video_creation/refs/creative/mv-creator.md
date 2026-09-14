# MV 音乐视频创作指南

## 红线（高频翻车点）

| 错误写法 | 后果 | 正确写法 |
|---------|------|---------|
| 各段 Prompt 中不写"禁止生成BGM" | 拼接后各段 BGM 冲突、音乐断裂 | 所有段 Prompt 末尾写"禁止生成BGM"，最终通过 ffmpeg 嵌入统一音乐 |
| 音频直接放 AudioList 参考 | 口型对齐成功率低，音频节奏随机性大 | 将音频转为黑屏视频放入 VideoList，口型对齐率极高 |
| 视频时长与音频时长不匹配 | 口型错位、音画不同步 | 每段视频 Duration 必须与对应音频段时长严格一致 |
| 不做歌词分段直接生成 | 画面与歌词节奏脱节 | 先按歌词结构分段，再逐段生成 |
| Prompt 中不写歌词原文 | 口型无锚点，同步精度下降 | Prompt 中必须附上该段歌词原文：`口型严格同步: "{歌词}"` |

## 强制规则

1. **音频转黑屏视频**：用户提供的 mp3/音频文件必须转为黑屏视频后放入 VideoList，作为音频节奏和口型的参考源
2. **时长严格对齐**：每段视频的 Duration 必须与对应音频段的时长完全一致
3. **歌词驱动分段**：按歌词结构（主歌/副歌/间奏/前奏/尾奏）拆分镜头，不按画面拆

Prompt 格式规则（禁 BGM / 歌词锚点 / 音频驱动句式）→ `storyboard/mv-prompt.md`

## 创作流程

### 第一步：音频准备

用户提供音频文件后（mp3/wav/m4a 等），用 `sandbox_bash` 将其转为黑屏视频：

```bash
# 获取音频时长
ffprobe -v error -show_entries format=duration -of csv=p=0 assets/{project}/song.mp3

# 转为黑屏视频（分辨率与目标视频一致）
ffmpeg -f lavfi -i color=c=black:s=1280x720:r=30 \
  -i assets/{project}/song.mp3 \
  -shortest -c:v libx264 -tune stillimage -c:a aac \
  assets/{project}/song_black.mp4
```

如果歌曲需要分段（不同段配不同画面），按歌词时间码切割黑屏视频：

```bash
# 切割某一段（例如 0:15 到 0:30，时长 15 秒）
ffmpeg -ss 15 -t 15 -i assets/{project}/song_black.mp4 -c copy \
  assets/{project}/song_segment_01.mp4
```

### 第二步：歌词分段与规划

根据歌词结构将歌曲拆分为多个镜头段落，写入 `creative_design.md`：

```markdown
# {歌曲名} MV

## 全局约束
- 风格：{统一风格关键词}
- 比例：16:9
- 总时长：{歌曲时长}
- 音频来源：assets/{project}/song.mp3

## 歌词分段
第1段 前奏 (0:00-0:12, 12s)：纯空镜，场景建置
第2段 主歌A (0:12-0:27, 15s)：{歌词内容} → {画面概述}
第3段 主歌B (0:27-0:42, 15s)：{歌词内容} → {画面概述}
第4段 副歌 (0:42-0:57, 15s)：{歌词内容} → {画面概述}
第5段 间奏 (0:57-1:09, 12s)：纯空镜/情绪过渡
...
```

**分段原则**：
- 每段 4-15 秒（Seedance 单次上限）
- 按歌曲结构（前奏/主歌/副歌/间奏/Bridge/尾奏）自然分段
- 副歌重复时画面可复用或做变体
- 间奏/前奏/尾奏适合空镜、转场、情绪铺垫
- 有歌词的段落优先安排角色出镜+口型演唱

### 第三步：参考素材生成

同 video_creation 标准流程，重点注意：

- **角色参考图**：需要唱歌的角色必须有面部特写（口型生成依赖清晰的面部参考）
- **场景参考图**：根据歌词意境准备不同场景
- **风格统一**：所有素材使用相同的风格关键词

### 第四步：逐段生成视频

Prompt 格式、调用示例与四类 MV Prompt 模板 → `storyboard/mv-prompt.md`（分镜规划阶段加载）

### 第五步：合成

```
render_video(
  video_paths: ["assets/{project}/shot_01.mp4", "assets/{project}/shot_02.mp4", ...],
  output_path: "assets/{project}/output_silent.mp4"
)
```

合成后用 ffmpeg 嵌入完整歌曲音频：

```bash
ffmpeg -i assets/{project}/output_silent.mp4 \
  -i assets/{project}/song.mp3 \
  -c:v copy -c:a aac -b:a 192k \
  -map 0:v:0 -map 1:a:0 -shortest \
  assets/{project}/output.mp4
```

## 不同 MV 类型处理

| MV 类型 | 角色是否唱歌 | 黑屏视频用法 | 要点 |
|--------|------------|------------|------|
| 角色演唱 MV | 是，口型同步 | 每段黑屏视频→VideoList，Prompt 写"口型与音乐精准同步" | Duration 必须与音频段严格一致 |
| 画面故事 MV | 否，纯画面配歌 | 不需要黑屏视频，直接按歌词节奏分段 | 最后用 ffmpeg 嵌入音频即可 |
| 混合型 MV | 部分唱、部分画面叙事 | 只有演唱段传黑屏视频 | 演唱段和叙事段分别处理 |

## 歌曲结构速查

| 段落类型 | 画面建议 | 运镜 | 节奏 |
|---------|---------|------|------|
| 前奏 | 空镜/场景建置/角色剪影 | 缓推/航拍/渐显 | 慢，铺氛围 |
| 主歌 | 角色日常/叙事/情绪铺垫 | 中景跟拍/横移 | 中，叙事为主 |
| 副歌 | 情感爆发/视觉高潮/群像 | 快切/环绕/特写交替 | 快，动感强 |
| Bridge | 情绪转折/回忆闪回 | 慢速/特殊效果 | 变化，反差 |
| 间奏 | 空镜过渡/情绪呼吸 | 缓慢升降/固定 | 慢，留白 |
| 尾奏 | 渐远/留白/循环/定格 | 缓拉远景/定格 | 渐慢收尾 |

## 失败模式

| 失败 | 后果 | 修法 |
|------|------|------|
| 直接用音频参考不转黑屏视频 | 口型对齐率低 | mp3 转黑屏视频后放 VideoList |
| Duration 与音频段时长不匹配 | 音画错位 | 用 ffprobe 测时长，Duration 严格一致 |
| 不按歌词结构分段 | 画面与音乐节奏脱节 | 按前奏/主歌/副歌/间奏分段 |
| 所有段都让角色唱歌 | 画面单调无变化 | 混合使用演唱段+叙事段+空镜段 |
| 忘记最后嵌入音频 | 输出的成片是静音的 | render_video 后必须 ffmpeg 嵌入歌曲 |

## 协同

- 角色一致性 → `assets/character-lock.md`
- 风格与情绪 → `creative/style-master.md`
- 叙事弧线 → `creative/narrative-arc.md`
- Prompt 编写 → `storyboard/mv-prompt.md`
