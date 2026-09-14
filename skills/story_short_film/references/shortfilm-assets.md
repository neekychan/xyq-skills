# 元素资产生成

本阶段输入为已确认的 `Project_Brief.md`。开始前检查其 `project_revision` 和确认状态；未确认或已失效时停止。

## 一、元素资产生成总规则

- 如果用户已经上传了元素资源（例如角色图像或引用的参考角色），直接将其绑定为相应 key_elements 的资产。
- 否则，只为 Project Brief 中明确需要视觉资产的画面元素生成图像。
- 用户提供或预先存在的媒体必须优先绑定到适当的关键元素位置；避免重复生成用户已提供的内容。
- 资产记录必须保留 `entity_type`、`visual_presence`、`audio_presence` 和使用场景，不能从有声音推断为需要角色图。

## 二、关键元素范围与 element_id 规划

始终包含 Project Brief 已确认的画面关键主体、关键地点/场景和关键道具（如有）。声音实体单独登记，不自动视为画面主体。

实体分离规则：

- `character + on_screen`：按需要生成角色视觉资产；
- `narrator + off_screen`：只生成或绑定 voice reference，不生成角色图，不进入 ImageList；
- `sound_only`：只建立声音资产；
- `conditional`：仅在 Project Brief 明确出镜的场景使用视觉资产。

如何规划 element_id：当每个画面角色、道具或场景是独立实体时，为每个实体分配一个 element_id（例如 [Element_Detective_Li]，[Element_Boss_Zhao]；[Element_Observation_Room]，[Element_Chief_Office]）。画外旁白使用 narrator/audio ID，不分配角色视觉 element_id。

如何编写描述：

- 角色：只描述 `visual_presence=on_screen` 的画面角色。如果角色在项目中具有多种状态或外观（例如不同服装、年龄），清晰描述每一种。包括画面角色的声音/音色，以便后续音频生成匹配。画外旁白不得编造外貌、服装或动作。
- 关键地点/场景：描述场景中重要物体的位置和朝向，特别是道具或发生主要动作/表演的区域。
- 用户提供的资产：如果用户提供了参考媒体并将其指定为关键元素，则描述必须与该资产匹配；不要与所见或所听到的内容相矛盾。

## 三、图像资产生成

- 图像：对于同一角色在不同外观或年龄下的表现，后续的外观应参考之前生成的图像以保持一致性。
- 角色图像：只为 `visual_presence=on_screen` 的画面角色生成参考图。画外旁白不生成角色图。每个画面角色生成 1 张参考图像：使用水平并排布局。画面左侧显示头像，右侧显示全身照。
- 场景图像：为需要跨镜头复用的地点/布景生成参考图像，明确重要物体的位置和朝向。
- 道具图像：为剧情中会被反复引用、影响动作或叙事结果的关键道具生成参考图像，明确形状、材质、颜色、尺寸、状态和独特标记。

## 四、角色声音、旁白声音与 key_element_audio

为每个有对话台词的画面角色建立 `key_element_audio`（音色锚点），以保证跨镜头音色一致性。画外旁白单独建立 narrator voice reference，用于后期 narration，不作为画面角色的 `key_element_audio` 或 ImageList 条件：

- 询问用户是否有对应的 voice reference 文件可上传。
- 用户已上传：将音色参考注册并绑定到正确的角色或 narrator_id。
- 用户未上传：从 Project Brief 中选取一段约 3–5 秒的对白或旁白文本，生成对应语音并绑定。
- 资产记录必须明确 `entity_type`、`visual_presence`、声音用途（dialogue/narration）及使用范围。
- 不得因为旁白存在声音资产，就生成旁白角色图或把旁白加入画面实体。

### 音色锚点时长即时校验（强制）

每条 voice reference 或 key_element_audio **生成或绑定后，必须立即执行时长校验**，流程如下：

1. 使用 `sandbox_read` 读取音频文件元数据，提取 `actual_duration`。
2. 若 `sandbox_read` 无法返回 duration，改用 `sandbox_bash` 执行 `ffprobe -v quiet -show_entries format=duration -of csv=p=0 <audio_path>`。
3. 校验规则：
   - `actual_duration ≥ 3s`：状态标记为 `checked_pass`，可用于后续视频生成。
   - `actual_duration < 3s`、格式异常或不可解码：状态标记为 `checked_fail`。
4. `checked_fail` 处置：
   - 自动选取更长的台词片段（≥5 字或添加 `<#0.5#>` 停顿）重新生成音色锚点。
   - 重新生成后再次执行步骤 1–3 校验。
   - 连续 3 次仍不合格时暂停，向用户报告并提供选项（上传音频 / 修改文本 / 跳过）。
5. **只有所有音色锚点状态为 `checked_pass` 后，才允许进入元素资产确认门。**

资产记录示例：

```yaml
- element_id: C1_maruko
  audio_file: C1_maruko_voice.mp3
  actual_duration: 4.2
  status: checked_pass
  entity_type: character
  audio_presence: dialogue
```

## 五、元素资产确认点（确认门）

元素资产（图像和音色）生成/绑定完成后，必须展示所有画面角色图像、场景图像、道具图像、角色声音与旁白声音说明，并明确检查：画外旁白没有角色图、没有视觉 element_id、不会进入 ImageList。

使用卡片确认：

```json
{
  "title": "确认元素资产",
  "questions": [
    {
      "id": "element_assets_status",
      "title": "角色形象、场景方向、道具状态和音色是否满意？",
      "type": "radio",
      "options": [
        {"label": "✅ 元素资产确认，继续故事板设计", "value": "approved", "selected": true},
        {"label": "✏️ 需要修改元素资产", "value": "revise"}
      ]
    }
  ]
}
```

只有在收到“元素资产确认，继续故事板设计”的确认后，才进入故事板阶段。
