# 故事板设计

输入为已确认的 `Project_Brief.md` 和已确认元素资产。开始前检查 `project_revision` 和上游状态；失效时停止并回到对应环节。

（告诉 AI 怎么写故事板，包括怎么设计镜头，以及如何描述画面和镜头语言。）

## 一、脚本忠实度（最高优先级）

- 用户上传了剧本时：分镜中的对话、旁白、动作结果和场景顺序必须与上传脚本及已确认的 `Project_Brief.md` 严格一致。仅允许技术性编辑：拆分镜头（≤15s）或添加镜头语言字段。不要虚构情节或改写台词。
- 由 agent 代写剧本时：以用户确认后的 `Project_Brief.md` 为唯一依据展开分镜设计，同样不得擅自修改情节或台词；如发现逻辑问题应先暂停并向用户确认。

## 二、关键元素引用

故事板只引用已在元素资产阶段确认过的画面关键元素和 element_id，不在本阶段重新规划 element_id。

每个镜头必须分别列出：

- `visible_entities`：当前镜头物理可见的画面角色、场景和道具；
- `audio_entities`：当前镜头的对白角色、画外旁白、环境声和音效；
- `ImageList`：只能引用 `visible_entities` 对应的视觉资产；
- `AudioList`：只能引用当前实际说话且需要参与视频生成的角色音频。

`off_screen narrator` 只进入 `audio_entities` / narration，不进入 `visible_entities` 或 ImageList。若故事板发现其需要真实出镜，必须先回到 Project Brief 更新 `visual_presence`，再补齐画面角色资产并重新确认。

每个镜头必须引用相关画面角色、场景、道具的 element_id；如果发现缺少必要元素，不得自行新增并继续，应回到元素资产阶段补齐并重新确认。

## 三、如何设计镜头

- 每个镜头描述必须包含：场景（元素）、故事和表演（具体台词）、画面实体、音频实体、镜头语言（景别、角度、运动）。
- 视觉设计和故事事实必须与 `Project_Brief.md` 相符。如果剧本省略镜头覆盖范围，可以从类型和基调中专业推断构图和运动，但绝不能改变情节事实或对话。
- 倾向于使用内部剪辑的长镜头（例如每个镜头10–15秒）。在镜头**内部**设计剪切，而不是拆分为许多短镜头；剪切频率应遵循故事节奏。每个镜头不得超过当前视频生成能力上限。
- 当镜头有内部剪切时：在场景/设定之后，按剪切顺序排列故事内容和镜头语言。使用明确的时间和剪切标记，例如 **"Shot1 (0–4s): [场景], [角色]做X，特写。Shot2 切至 (4–8s): … Shot3 切至 (8–12s): …"**
- 每个镜头描述必须包含：
  - 场景：引用地点/布景（使用场景元素ID，例如 [Element_Office_Noir]）。
  - 故事内容：画面角色和关键物体的动作与动态；写出确切角色台词。画外旁白单独写入 narration/audio_entities，不使用角色元素 ID，不描述其外貌或画面动作。
  - 画面/声音实体：分别列出 `visible_entities`、`audio_entities`、ImageList 和 AudioList。
  - 镜头语言：景别、角度、运动。

## 四、角色出现矩阵

`storyboard.md` 必须包含：

```markdown
| entity_id | entity_type | visual_presence | appears_in_shots | speaks_in_shots | narration_in_shots | visual_asset | voice_reference |
|---|---|---|---|---|---|---|---|
```

规则：每个 `visible_entity` 必须能回查元素资产；`off_screen narrator` 不进入 visible_entities；新增画面角色必须返回 Project Brief 和元素资产阶段；实际说话角色与旁白分别记录。

## 五、故事板输出与确认

故事板列表（storyboard.md）生成后，必须展示所有分镜段落，并检查旁白没有进入画面角色、角色图或 ImageList。

使用卡片确认：

```json
{
  "title": "确认故事板",
  "questions": [
    {
      "id": "storyboard_status",
      "title": "分镜、内部剪辑节奏、元素引用和音频层规划是否确认？",
      "type": "radio",
      "options": [
        {"label": "✅ 故事板确认，继续镜头视频生成", "value": "approved", "selected": true},
        {"label": "✏️ 需要修改故事板", "value": "revise"}
      ]
    }
  ]
}
```

只有在用户通过故事板审阅后，才能进入镜头视频生成阶段。
