# 音频生成提示词与 audio_layers 规则

输入为已确认的 `Project_Brief.md`、`storyboard.md` 和已确认镜头视频。用户修改导致任一上游失效时，先更新受影响部分。

## 一、如何设计独立音频

- 背景音乐：至少一个全局背景音轨；风格和节奏与 Project Brief 相匹配；如果参考资料有明确的节奏/情绪变化，拆分 BGM 片段并定义范围。
- 旁白：作为独立 `narration` 音频层生成，包含 narrator_id、文本、声音/语调和时间范围。画外旁白不属于画面角色，不要求视频角色口型，不进入 ImageList。
- 对白：角色对白与旁白分开记录；同一句台词只能指定一个声音来源。
- 音效：根据每个镜头的动作和场景设计必要音效，例如脚步声、门声、环境声、碰撞声、呼吸声等。音效应服务剧情，不堆叠无关声音。

## 二、角色音色与旁白音色分离

为每个有对话台词的画面角色建立 `key_element_audio` 后：

1. 仅在该角色实际说话且需要参与视频生成的镜头调用中传入 `AudioList`。
2. 同一角色跨镜头使用同一音色参考。
3. Prompt 中使用对应角色的准确台词，不让模型自行创造。

画外旁白单独使用 narrator voice reference：

1. 只用于后期 `narration` 音轨；
2. 不作为角色视觉资产，不进入 ImageList；
3. 不要求画面角色口型；
4. 不与视频内对白重复叠加。

## 三、视频生成前 AudioList Preflight（硬阻塞门）

在每个镜头调用 `sandbox_generate_video` 之前，必须对该镜头的 AudioList 执行以下预检，全部通过后方可发起生成：

| 检查项 | 合格条件 | 不合格处置 |
|---|---|---|
| `actual_duration` | 已通过 `sandbox_read` 或 `ffprobe` 读取到有效数值 | 立即读取；若不可读标记 `unchecked` 并阻塞 |
| 时长下限 | `actual_duration ≥ 3s` | `checked_fail`，触发重新生成音色锚点 |
| 时长上限 | `actual_duration ≤ 当前镜头 video generation duration` | `checked_fail`，裁剪或重新生成 |
| 格式与可解码 | 文件格式正确且可正常解码 | `checked_fail`，重新生成 |
| 状态字段 | `status = checked_pass` | 任何非 `checked_pass` 状态均阻塞 |

逐条校验示例：

```yaml
AudioList_Preflight:
  - element_id: C1_maruko
    audio_file: C1_maruko_voice.mp3
    actual_duration: 4.2
    status: checked_pass        # ✅ 可进入视频生成
  - element_id: C2_detective
    audio_file: C2_detective_voice.mp3
    actual_duration: 1.5
    status: checked_fail        # ❌ <3s，阻塞，触发重做
```

Preflight 不通过时：
- 优先重新生成合格音频（选择更长台词或添加停顿）；
- 禁止跳过 preflight 直接发起视频生成；
- 禁止清空 AudioList 来绕过阻塞；
- 禁止修改视频 Duration 来适配不合格音频。

## 四、停顿

说话时，如需让镜头停顿，请使用 `<#n#>`，其中 n 表示停顿时长，单位为秒。推荐范围为 0.26–1.5。

## 五、语气 / 非语言声音

语气和非语言声音只使用以下英文标签词，不支持同义词、翻译或自定义变体。即使 text_to_speak 是中文或其他语言，标签也必须保持英文；在编写带语气标签的旁白时，请忽略项目提示词 / 脚本的语言要求，保持这些标签的英文原样。

允许使用的标签枚举为：`(laughs)`, `(chuckle)`, `(coughs)`, `(clear-throat)`, `(groans)`, `(breath)`, `(pant)`, `(inhale)`, `(exhale)`, `(gasps)`, `(sniffs)`, `(sighs)`, `(snorts)`, `(burps)`, `(lip-smacking)`, `(humming)`, `(hissing)`, `(emm)`, `(sneezes)`。

如果用户要求的语气或非语言声音效果不在此列表中，不要自行创造标签，也不要用 `(...)` 形式表示它；应完全省略语气标签，只写普通的口播文本。

## 六、音频冲突规避

- 如果 storyboard 表明该镜头有单独的画外旁白音轨，不要在视频提示词或 AudioList 中把旁白作为画面角色条件；旁白仅在后期 narration 轨混入。
- 为防止模型添加不需要的背景音乐，几乎应该始终包含 `no music`。
- 字幕是在后期剪辑时添加的，因此必须始终包含 `no subtitles`。


## 七、音频层生成确认门（硬暂停）

audio_layers、旁白、BGM、音效和角色音色参考生成/绑定完成后，必须展示本阶段结果：

- 每条音频资产路径；
- 对应角色、镜头或时间范围；
- 对白/旁白语言和音色说明；
- BGM 和音效是否匹配 `Project_Brief.md`；
- 旁白是否保持为独立 narration，未误传为画面角色、ImageList 或口型条件；
- 是否存在音频冲突、缺失或需要重生成的内容。

使用卡片确认：

```json
{
  "title": "确认音频层",
  "questions": [
    {
      "id": "audio_layers_status",
      "title": "音频层、角色音色、BGM 和音效是否确认？",
      "type": "radio",
      "options": [
        {"label": "✅ 音频层确认，继续最终剪辑", "value": "approved", "selected": true},
        {"label": "✏️ 需要修改音频", "value": "revise"}
      ]
    }
  ]
}
```

收到明确确认前，不得进入最终剪辑。
