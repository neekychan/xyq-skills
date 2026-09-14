---
name: zhiyu-vlog-maker
display_name: 治愈系Vlog
description: 制作治愈系生活方式Vlog视频的全流程技能。当用户想创作节奏舒缓、画面温暖、以日常片段传递安心感的竖版Vlog视频时触发。覆盖从全局参数锁定、故事板设计、参考素材生成、逐镜头视频生成到合成成片的完整流程，支持单集与连续剧模式。目标市场为中国大陆/抖音，产出中文内容。
tools: ["sandbox_generate_image", "render_video", "sandbox_generate_video", "sandbox_process_video"]
---

# 治愈系Vlog制作

## 核心原则

不要只做"好看的画面拼接"，而要做"有呼吸感的生活叙事"——每个镜头都让观众觉得自己也在那个空间里慢下来。

持久引擎（因果链）：

**生活场景 → 氛围张力 → 情绪钩子（安静/期待/满足）→ 叙事动作 → 治愈感确认 → 画面与音乐共振 → 成片**

### 质量测试（可证伪）

如果关闭声音、只看画面，观众仍能在 3 秒内感受到"这是一个让人想慢下来的空间"——则创意成立。若画面只是"人在做事"而无氛围包裹感，则重做。

## 输入诊断

生产前，识别或合理假设以下维度：

- vlog_theme：主题方向（如"周末独居日记""雨日咖啡馆""秋日山林散步"）
- art_style：美术风格（如"吉卜力上色""水彩绘本""柔焦胶片"）
- color_palette：色彩基调（如"低饱和暖米调，莫兰迪配色"）
- lighting_style：光照偏好（如"柔和窗光""暖黄台灯光""自然晨光"）
- output_ratio：画面比例（默认 9:16）
- is_series：是否连续剧（默认 false）及集数
- output_language：输出语言（默认中文）
- 参考素材：用户是否已上传角色图、场景图、风格参考图
- 合规敏感点：治愈系内容通常无高敏感，但需注意不美化孤独/封闭、不暗示逃避现实

若用户只给了一个模糊方向（如"想做一个温馨的Vlog"），做合理假设并继续。仅当主题方向完全无法推断时才发问。

## 路由表

针对具体任务，只读取匹配的 references：

| 输入特征 | 必读 reference |
|---|---|
| 任何任务 | `references/formats/consistency-rules.md` |
| 编写图像/视频 prompt | `references/formats/prompt-writing.md` |
| 确认输出格式与 beat 结构 | `references/formats/output-spec.md` |
| 治愈系场景/情绪/氛围/道具/色彩/音乐用词 | `references/industries/healing-lifestyle.md` |

静默使用 references；除非用户问起，否则不提及。

## 强制加载 reference

写任何最终产出前，先按路由结果读取对应 references。

必读：
1. `references/formats/consistency-rules.md`
2. `references/formats/prompt-writing.md`

条件读取：
- 涉及治愈系场景/情绪/氛围描述时读 `references/industries/healing-lifestyle.md`
- 确认输出格式时读 `references/formats/output-spec.md`

硬规则：若最终产出包含视频生成 prompt，则本回合必须已读过 `references/formats/prompt-writing.md`。

## 工作流（步骤）

### 阶段一：锁定全局参数

1. 解析用户输入，提取或推断 vlog_theme、art_style、color_palette、lighting_style、output_ratio、is_series 等维度。
2. 若用户上传了参考素材，读取本技能下的 `references/formats/prompt-writing.md` 中「参考素材分析」部分，提取角色/场景/风格的结构化描述，填入对应参数。
3. 将全部参数写入 `Final_Video_Spec.md`，作为全流程参数锚点。
4. **暂停节点**：向用户展示 Final_Video_Spec.md 内容，等待确认后继续。

### 阶段二：设计故事板

5. 按 `Final_Video_Spec.md` 中的参数，设计故事板：
   - **key_elements**：主角（含换装变体）、全部场景、跨场景复用道具。
   - **shots**：按集/场景排列的分镜列表，每个 shot 包含场景引用、叙事动作、镜头语言、光氛说明。
   - **audio_layer**：BGM 轨道描述。
6. 一致性锁定：key_element 的描述字段是唯一权威来源，shot 描述中仅引用 element ID，不重写任何已在 key_element 中定义的属性。
7. 连续剧模式：is_series=true 时，一次性设计所有集数的 shots（每集对应各自场景），角色 key_element 全局复用。
8. **暂停节点**：向用户展示故事板，等待确认后继续。

### 阶段三：绑定与生成参考素材

9. 若用户已上传角色图/场景图，将其注册并绑定到对应 key_element 槽位，跳过该元素的生成。
10. 为主角及换装变体生成参考图（横版双联：左侧头肩特写，右侧全身正面），使用 `Final_Video_Spec.md` 中的 art_style 和 color_palette 作为风格锚点。
11. 为每个场景生成无人物全景参考图，画面中留出人物自然站立/坐立的位置区域。
12. **暂停节点**：向用户展示全部参考素材图，等待确认后继续。用户确认后的参考图即为全流程绑定的稳定素材，后续不得替换。

### 阶段四：逐镜头生成视频

13. 按故事板顺序，为每个 shot 生成视频片段：
    - 每个视频片段时长 6–10s，不超过 15s，用一次视频生成即可拿到完整片段。
    - 引用已审核通过的角色元素图和场景元素图作为参考输入。
    - 同一场景且动作连续时，可引用前一 shot 的视频；跨场景切换时不引用。
    - prompt 开头点明美术风格与色调基调，与 Final_Video_Spec.md 保持一致。
    - prompt 中只描述动作与表情，严禁重新描述已在参考图中锁定的外观属性。
14. 成片总时长 >15s 时，拆成若干 ≤15s 片段分别生成，再做后处理拼接。
15. 连续剧模式中，跨集不引用前集视频，只复用 key_element 图。
16. **暂停节点**：向用户展示全部镜头视频，等待确认后继续。

### 阶段五：生成 BGM 与合成成片

17. 按 storyboard audio_layer 的氛围描述生成背景音乐。治愈系轻音乐/氛围音乐，无人声，低频柔和。
18. 合成与剪辑：
    - 镜头间使用柔和淡入淡出过渡（dissolve），时长 0.5–1s。
    - BGM 贯穿全片，音量设为主音轨的 40–60%。
    - 首尾各做 1s 音量淡入/淡出。
    - 画面比例遵循 Final_Video_Spec.md 中的 output_ratio。
    - 单集成片时长 30s–90s；连续剧每集独立输出。
19. 交付成片。

## 输出契约

### Final_Video_Spec.md 格式

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

### 故事板格式

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

shots:
  - id: S01
    scene: SCENE_01
    character: CHAR_01 / LOOK_01
    duration: 8s
    action: [叙事动作，具体到肢体与表情]
    camera: [景别/机位/运镜方式]
    light: [光位方向与色温]
    prev_shot_ref: [可选，前一 shot ID，仅同场景动作连续时]

audio_layer:
  - type: music
    mood: [氛围描述]
    description: [风格/乐器/节奏感]
```

### 图像 prompt 结构

```
{art_style} → {主体/角色描述} → {场景/环境描述} → {道具与细节} → {色彩基调} → {光影描述} → {构图说明}
```

### 视频 prompt 结构

```
{art_style + color_palette 一句话} → <<<image_1>>>角色参考图 + <<<image_2>>>场景参考图 → {镜头运动} → {角色动作（肢体+表情微动）} → {环境氛围细节} → no music, no subtitles
```

> 时长 ≤15s 的成片用一次视频生成即可拿到完整片段，多段 beat 写在同一条 prompt 内的时间轴上；只有成片 >15s 时才拆成若干 ≤15s 片段分别生成再做后处理拼接。

## 静默自检

交付前内部跑清单并重写弱项；除非用户要求点评，否则不外显。

- 因果链是否每一环都成立（场景→氛围→情绪→动作→治愈感）？
- 质量测试是否通过（关闭声音只看画面，3 秒内能否感受到"想慢下来"）？
- Final_Video_Spec.md 中的参数是否与所有 prompt 保持一致（art_style/color_palette 逐字复制）？
- key_element 描述是否唯一权威（shot prompt 中有无重新描述外观属性）？
- 每个 shot 是否包含场景引用、叙事动作、镜头语言、光氛说明四要素？
- 参考图是否已通过用户审核并绑定稳定？
- 视频生成是否正确引用角色+场景参考图，跨场景切换时是否避免了错误引用？
- 镜头间过渡是否柔和（无快切）？BGM 是否无突兀的人声？
- 全文语言是否与目标市场一致（中文）、无中英混杂？
- 暂停节点是否全部执行（参数锁定/故事板/参考图/镜头视频）？
