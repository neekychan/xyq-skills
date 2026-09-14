# 输出规范与 beat 结构

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## Final_Video_Spec.md 格式

```
主题方向（vlog_theme）：
美术风格（art_style）：
色彩基调（color_palette）：
光照偏好（lighting_style）：
画面比例（output_ratio）：9:16
是否连续剧（is_series）：false
集数（若连续剧）：
输出语言：中文
```

所有后续阶段以此文件为参数锚点，art_style 和 color_palette 必须**逐字复制**到每条 prompt。

## 故事板格式

### key_elements

```
key_elements:
  - id: CHAR_01
    type: character
    description: [发型/发色/瞳色/肤色/标志性五官/体型]
    looks:
      - id: LOOK_01
        description: [服装款式与配色]
      - id: LOOK_02
        description: [服装款式与配色]

  - id: SCENE_01
    type: scene
    description: [空间布局/标志性道具摆放/光源位置与色温/整体色调]

  - id: PROP_01
    type: prop
    description: [外观/材质/色彩]
```

### shots

每个 shot 对应一个场景内的一段生活片段，建议时长 6–10s，不超过 15s。

```
shots:
  - id: S01
    scene: SCENE_01
    character: CHAR_01 / LOOK_01
    duration: 8s
    action: [叙事动作，具体到肢体与表情]
    camera: [景别/机位/运镜方式]
    light: [光位方向与色温]
    prev_shot_ref: [可选，前一 shot ID，仅同场景动作连续时]
```

### audio_layer

```
audio_layer:
  - type: music
    mood: [氛围描述]
    description: [风格/乐器/节奏感]
```

- 至少设置一条全局 BGM 轨，风格为治愈系轻音乐/氛围音乐，无人声，低频柔和。
- 连续剧模式中，若不同集的情绪差异明显，可按集拆分为多条 BGM 轨。
- 不使用旁白/narration 轨，Vlog 叙事依靠画面与音乐传递。

## 连续剧模式规则

- is_series=true 时，一次性设计所有集数的 shots（每集对应各自场景）。
- 角色 key_element 全局复用，只生成一次角色参考图。
- 场景图、镜头视频按集遍历。
- 完成全部集数后统一合成，或按集分别输出。

## 合成与剪辑规范

### 节奏与过渡

- 治愈系 Vlog 整体节奏舒缓，镜头间避免快切。
- 默认使用柔和淡入淡出过渡（dissolve），时长 0.5–1s。
- 每个 shot 按故事板规划时长放置，不额外压缩。
- 连续剧集与集之间使用较长的淡出→淡入过渡（约 1.5s）。

### 音频混合

- BGM 贯穿全片，音量设为主音轨的 40–60%，保证不压盖视频内的自然环境音。
- 视频素材自带的环境音效保留，不完全静音；若与 BGM 冲突则略微压低。
- 首尾各做 1s 音量淡入/淡出，避免硬开硬结。

### 输出设置

- 画面比例遵循 Final_Video_Spec.md 中的 output_ratio（默认 9:16）。
- 单集成片时长 30s–90s。
- 连续剧每集独立输出，不强制拼接为长视频（除非用户明确要求）。

## 视频生成方式

时长 ≤15s 的成片用一次视频生成即可拿到完整片段。shots 中的 beat 时间轴（如 0-3s/3-7s/7-12s）是同一条 prompt 内的时间描述，不是分段多次生成。只有成片 >15s 时，才拆成若干 ≤15s 片段分别生成，再做后处理拼接、配乐、字幕。

## 暂停节点

以下节点完成后必须暂停并等待用户确认再继续：

1. Final_Video_Spec.md 锁定后
2. 故事板设计完成后
3. 角色元素图生成完成后
4. 所有镜头视频生成完成后

## 落 prompt 前自检

- [ ] Final_Video_Spec.md 是否已写入并经用户确认？
- [ ] 每个 shot 时长是否 ≤15s？
- [ ] 成片 >15s 时是否已拆成多片段分别生成？
- [ ] 暂停节点是否全部执行？
- [ ] 合成过渡是否柔和（无快切）？
- [ ] BGM 音量是否在 40–60%？
- [ ] 输出画幅是否与 Final_Video_Spec.md 一致？
