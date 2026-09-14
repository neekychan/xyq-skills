# 编译内部校验合同 JSON · 完整必填字段模版

> **本文件是三个 `validate_*.py` 校验器所需 JSON 合同的唯一权威字段模版。**
> 第 3 步 `validate_creative_contract.py`、第 4 步 `validate_story_script.py`、第 6 步 `validate_final_prompt.py` 在生成产物前都要喂一份内部 JSON 合同给对应校验器。照本文件的模版填字段即可。
>
> 用法:走到第 3/4/6 步、即将跑校验前,即时读本文件对应小节,把模版复制为一个真实 JSON 文件(内部文件,放 `_internal/`,不展示给用户),按当前项目实况填值,再执行校验。返回 `ok:false` 或非零就按 `errors` 改**产物**并重跑,不得展示失败版本、不得以"我自查通过了"代替真跑。
>
> **【禁止读校验器源码 · 本条为全 Skill 唯一权威,其它文件只指向此处、不再复述理由】** 无论是想反推字段、还是想看懂某条错误信息,**任何情况下都不允许 `Read`/`cat`/`grep` `scripts/validate_*.py`(三个校验器)源码**。原因:① 字段该怎么填,本文件模版已写全;② 校验器返回的每个 `errors[]` 都是一句**中文自然语言**,已直接写清「哪里出问题、改哪个产物、怎么改」,照着改产物、重跑即可;③ 读源码既浪费上下文,又会把内部实现当成用户可见内容泄漏,而且毫无必要。若某条错误信息一时看不懂,回到对应产物按其字面意思修正,仍不得读源码。
>
> 字段值语言:JSON 里的枚举/键名是内部机器标识,保持英文原样;它们只进校验器,绝不出现在给用户看的文本或最终产物里(见「用户可见语言隔离合同」)。

---

## 1. 第 3 步 · `validate_creative_contract.py`(融合创意合同)

调用:`python3 scripts/validate_creative_contract.py <contract.json>`(或 stdin 传入)。校验融合规格、执行落地与本地化的结构完整性。

### 1.1 完整模版

```json
{
  "current_sku_lock": {
    "object_state": "physical",
    "unresolved_conflicts": []
  },
  "selected_content_program": "<所选内容程序名>",
  "program_lock": {
    "selected_content_program": "<与上一行逐字一致>",
    "source_coverage": {
      "exact_sku_form": true,
      "duration_fit": true,
      "evidence_basis": true
    },
    "main_proof_loop": "<主证明循环的一句话描述>",
    "minimum_main_proof_seconds": 4.0,
    "auxiliary_seconds": 1.0,
    "ending_in_task": true
  },
  "hook_claims": ["<开场主张1>"],
  "proof_answer_shot": "<回应开场主张的证明镜说明>",
  "sku_eligibility": true,
  "asset_eligibility": true,
  "eligibility_conflicts": [],
  "platform": "抖音",
  "duration_seconds": 15,
  "adaptive_fusion": {
    "product_specific_tension": "<该商品特有的张力>",
    "opening_event": "<开场事件>",
    "opening_state": "<开场状态>",
    "product_causal_action": "<商品导致的因果动作>",
    "proof_state": "<证明状态>",
    "end_state": "<结束状态>",
    "selected_modules": { "hook": true, "play": true, "style": true },
    "module_observable_effects": {
      "hook": "<hook 的可观察效果>",
      "play": "<play 的可观察效果>",
      "style": "<style 的可观察效果>"
    },
    "style_modulation": "<style 落地到执行的调制说明>",
    "generic_template_skin_only": false
  },
  "human_performance": {
    "required": true,
    "trigger_source": "<触发来源>",
    "observable_response": "<可观察反应>",
    "action_intent": "<动作意图>",
    "result_response": "<结果反应>",
    "emotion_labels_only": false
  },
  "spectacle_causality": {
    "required": false,
    "spectacle_mechanism": "",
    "product_relevant_force": "",
    "visible_effect_on_character_or_task": "",
    "counteraction_or_progression": "",
    "handoff_to_proof": ""
  },
  "content_budget": {
    "main_selling_points": 1,
    "supporting_selling_points": 1,
    "auxiliary_information_beats": 2,
    "active_selling_point_ids": ["SP1", "SP2"]
  },
  "product_entity_contract": {
    "instance_budget": 1,
    "multi_instance_authority": "none",
    "immutable_signature": ["<身份锚点1>", "<身份锚点2>"],
    "shot_entity_ledger": [
      {
        "shot": "S1",
        "instance_count": 1,
        "high_risk_interactions": [],
        "left_hand_job": "",
        "right_hand_job": "",
        "other_similar_objects": [],
        "occlusion_ratio": 0.0,
        "handoff_or_flip": false,
        "reanchor_after_occlusion": true
      }
    ]
  },
  "short_form_execution": {
    "first_event_at_seconds": 0.4,
    "product_in_real_task_at_seconds": 2.5,
    "effective_visual_beats": 6,
    "native_scores": [2, 2, 2, 2, 1, 2, 1, 2],
    "static_product_intro": false,
    "platform_execution_floor_preserved": true,
    "style_native_adapter": "<风格的平台原生适配说明>",
    "main_proof_seconds": 4.5,
    "scene_sequence": ["厨房", "厨房", "特写"],
    "user_locked_circular_structure": false
  },
  "opening_hook_contract": {
    "hook_carrier": "spoken_line",
    "first_information_at_seconds": 0.4,
    "viewer_can_name_problem_or_desire_by_seconds": 0.9,
    "unframed_silence_seconds": 0.0,
    "silent_opening_authority": "none",
    "spoken_hook": "<口播 hook 原话>",
    "on_screen_hook": "",
    "visible_contrast_or_consequence": "",
    "distinctive_sound_and_causal_result": ""
  },
  "speech_rhythm_contract": {
    "language": "zh",
    "profile": "douyin_native",
    "target_rate": 6.0,
    "max_rate": 7.0,
    "line_budgets": [
      { "line": "L1", "rate": 6.0 }
    ]
  },
  "localization": {
    "target_market": "",
    "spoken_language": "",
    "character_reference_authority": "",
    "cast_localization": ""
  }
}
```

### 1.2 关键约束(填值时先看这些,避免必然报错)

- `current_sku_lock.object_state`:实体商品填 `physical`;数字/虚拟/品牌本身填 `digital`/`virtual`/`brand`/`数字/虚拟`/`品牌本身` —— 非实体时整个 `product_entity_contract` 可省略。
- `program_lock.selected_content_program` 必须与顶层 `selected_content_program` **逐字一致**。
- `program_lock.source_coverage` 三个子项 `exact_sku_form`/`duration_fit`/`evidence_basis` **都要为 `true`**。
- `program_lock.minimum_main_proof_seconds` **> 0**;`auxiliary_seconds` **≤ 1.2**;`ending_in_task` 必须 `true`。
- `hook_claims` 非空时必须给 `proof_answer_shot`。
- `adaptive_fusion`:六个状态字段(`product_specific_tension`/`opening_event`/`opening_state`/`product_causal_action`/`proof_state`/`end_state`)缺一即报错;`selected_modules` 里为 `true` 的模块必须在 `module_observable_effects` 里有对应非空效果;`style` 为 `true` 还需 `style_modulation`;`generic_template_skin_only` 必须 `false`。
- `human_performance.required=true` 时,`trigger_source`/`observable_response`/`action_intent`/`result_response` 都要非空,`emotion_labels_only` 必须 `false`(不能只堆情绪标签)。
- `spectacle_causality.required=true` 时,五个字段(`spectacle_mechanism`/`product_relevant_force`/`visible_effect_on_character_or_task`/`counteraction_or_progression`/`handoff_to_proof`)都要非空;不用奇观时 `required=false` 其余留空即可。
- `content_budget`:`main_selling_points` **恒为 1**;`main+supporting` 不超过时长预算(见下表);`active_selling_point_ids` 若给,其长度必须等于 `main+supporting`;时长 ≤15s 时 `auxiliary_information_beats` **≤ 2**。
- **卖点数量随时长上限**:≤8s→1;≤20s→2;≤30s→3;≤45s→4;≤60s→5;更长→`max(5, (时长+14)//15)`。
- `product_entity_contract`(实体商品必填):`instance_budget ≥ 1`;`instance_budget > 1` 时 `multi_instance_authority` 不能是 `none`;`immutable_signature` **至少 2 个**身份锚点;`shot_entity_ledger` 非空。每个 shot:`instance_count` 不超预算;`>1` 需授权;`high_risk_interactions` 最多 1 项;有交互必须给 `left_hand_job` 或 `right_hand_job`;`other_similar_objects` 每项要有 `name` 和 `role`;`occlusion_ratio > 0.4` 或 `handoff_or_flip=true` 时必须 `reanchor_after_occlusion=true`。
- **短平台短视频专属门**(平台含"抖音"/"tiktok" 且 `0 < duration ≤ 20`):
  - `first_event_at_seconds` **≤ 0.5**;`product_in_real_task_at_seconds` **≤ 3.0**;`static_product_intro` 必须 `false`。
  - 时长 ≤15s 时 `effective_visual_beats` **在 5–8 之间**。
  - `native_scores` **恰好 8 个**,每个 0–2,不能有 0,且**总和 ≥ 12**。
  - `platform_execution_floor_preserved` 必须 `true`;`style_native_adapter` 非空。
  - `main_proof_seconds` **≥** `program_lock.minimum_main_proof_seconds`。
  - `scene_sequence` 不得离开某场景后又重开(除非 `user_locked_circular_structure=true`)。
  - `opening_hook_contract`(短平台必填):`hook_carrier` ∈ `spoken_line`/`on_screen_text`/`self_evident_visual`/`distinctive_sound`;`first_information_at_seconds` **≤ 0.5**;`viewer_can_name_problem_or_desire_by_seconds` **≤ 1.0**;`unframed_silence_seconds > 0.4` 时 `silent_opening_authority` 必须 ∈ `user_locked_asmr`/`user_locked_visual_hook`/`user_locked_sound_hook`;carrier 与其配套字段绑定(`spoken_line`→`spoken_hook`;`on_screen_text`→`on_screen_hook`;`self_evident_visual`→`visible_contrast_or_consequence`;`distinctive_sound`→`distinctive_sound_and_causal_result`)。
  - `speech_rhythm_contract`(短平台必填):中文(`language` ∈ `zh`/`中文`/`chinese`)且 `profile=douyin_native` 时 `target_rate` **在 5.5–6.5**;`max_rate` **≤ 7.2**;每条 `line_budgets[].rate` 不超过 `max_rate`。
- `localization`:目标市场泰国(`target_market` ∈ `thailand`/`泰国`,或 `spoken_language` ∈ `thai`/`泰语` 且平台含 tiktok)时,若 `character_reference_authority` 不是 `locked_by_user`,则 `cast_localization` 必须 ∈ `thai`/`thai_local`/`thailand_local`。

---

## 2. 第 4 步 · `validate_story_script.py`(故事脚本合同)

调用:`python3 scripts/validate_story_script.py <故事脚本.md> --contract <contract.json>`。**它直接扫实际的 `故事脚本.md` 文本**,`--contract` 只是补充校验依据(可省,但建议给)。

> **本校验器只做确定性结构检查(本轮重构)**:它只验证脚本的格式骨架、内部标签泄漏、时长自洽——这些是「写法正确的脚本一定能通过」的检查。**开场钩子是否成立、首镜是否抓人、场景是否回访这类创意/语义约束,脚本无法可靠判定(换个说法就误伤正确脚本、导致反复改写卡死),已从校验器移除,改由你依据 `contract-creative-and-script.md`「Hook 脚本合同」「空间定位与位置连续性合同」等正文自行保证。**

### 2.1 `--contract` JSON 模版

```json
{
  "duration_seconds": 15
}
```

`--contract` 现在只用到 `duration_seconds`(用于校验分镜时长之和是否对得上)。可省;省略时跳过时长对齐检查。

### 2.2 校验器对 `故事脚本.md` 正文的硬性结构要求(全部为确定性检查)

- 全文有且仅有一个一级标题,且必须是 `# 故事脚本`。
- 有且仅有一个 **8 列表格**,表头逐字为:`镜号 | 时长 | 画面描述 | 景别 | 光影氛围 | 对白·旁白 | 音效 | 运镜`;表头下一行是分隔行;每个数据行必须 8 列。
- 有且仅有一行以 `**全片 BGM**` 开头。
- **除**标题、这一个表格、这一行 BGM 之外,不得有任何其它用户可见段落。
- **禁止泄漏内部标签**:正文不得出现 `Hook Scope`/`Bridge`/`Body takeover`、内部机制编号(形如 `BH04`/`S03`/`R01` 等两位数字编号)、内部字段名(`selected_content_program`/`program_lock`/`opening_hook_contract`)。
- 每个数据行时长可解析(形如 `3s`/`3秒`);给了 `duration_seconds` 时,全片时长之和与它差 **≤ 0.2**。

---

## 3. 第 6 步 · `validate_final_prompt.py`(最终方案合同)

调用:`python3 scripts/validate_final_prompt.py <视频生成Prompt.md> --contract <contract.json>`(`--contract` **必填**)。**它直接扫实际的 `视频生成Prompt.md` 文本**。

> **本校验器只做确定性结构 + 禁止项检查(本轮重构)**:它只验证「能否解析出带时间戳的分镜」「禁用词不能出现」「字幕指令不自相矛盾」——都是「写法正确的 Prompt 一定能通过」的检查。**此前那些「首拍必须出现某关键词/某句口播原话」「必须出现『恰好一把产品1』这类单实例锁定措辞」「主证明关键词累计秒数」「静态收尾 vs 真实动作分类」「尺寸类比」「场景重开」等检查已全部移除**——它们靠有限关键词表匹配正向措辞,一个写法正确的 Prompt 换个说法就永远匹配不上,会让你反复改写却过不了、无限卡死(真实故障:曾因此反复读校验器源码想反推该塞哪些魔法字符串)。这些开场钩子、单实例、主证明时长、平台原生收尾、尺寸真实、场景连续等约束,改由你依据 `contract-platform-and-execution.md`「首秒信息可读合同」、`contract-product-truth.md`「产品真实形态与使用逻辑合同」、`contract-creative-and-script.md`「空间定位与位置连续性合同」等正文自行保证,不再交给脚本裁决。

### 3.1 `--contract` JSON 模版

```json
{
  "forbidden_sku_terms": ["<禁止出现的错误型号/材质1>"],
  "unsupported_claim_terms": ["<无依据的夸大宣称词1>"],
  "forbidden_imports": ["<禁止串入的他程序元素1>"]
}
```

三个字段都是**禁止项列表**(可为空数组或省略):列出的词一旦在 Prompt 里出现即报错。不再有任何"必须出现某措辞"的正向字段。

### 3.2 校验器对 `视频生成Prompt.md` 正文的硬性要求(全部为确定性检查)

- **时间轴结构门**:正文必须含**可解析的时间戳分镜节拍**(形如 `0-3s`/`3s-6秒`);解析不到就报错。
- **禁止项缺席门**:`forbidden_sku_terms`、`unsupported_claim_terms`、`forbidden_imports` 里的词一个都不能出现。(注意:不再校验 `required_sku_terms`/身份锚点等"必须出现"项——那些改由你按契约正文自行保证。)
- **字幕冲突门**:不得同时出现"无字幕/不要字幕"与"花字/字幕出现/屏幕文字"。

---

## 4. 通用执行须知

1. **三个合同 JSON 都是内部文件**:建议写到 `video-projects/<项目目录>/_internal/` 下,不进任何用户可见产物,不在对话里贴出来。
2. **先写产物、再填合同、再校验**:合同 JSON 是对产物的断言;`故事脚本.md`/`视频生成Prompt.md` 的字段(如时长、首镜台词、SKU 术语)必须与合同值真实对应,不能为了过校验而在合同里瞎填。
3. **失败即改产物**:返回 `ok:false`/非零时,按 `errors` 定位是**产物**哪里不达标,改产物(或必要时改合同以如实反映产物),再重跑,直到 `ok:true`。不得展示未过校验的版本。
4. **字段值缺证据就别编**:凡涉及商品尺寸/材质/型号/卖点等关键事实,合同里要么填已确认的真值,要么把上游标 `unknown` 并回到第 2/5 步问用户——绝不为过校验而臆造。

