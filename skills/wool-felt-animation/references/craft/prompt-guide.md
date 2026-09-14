# 羊毛毡风格提示词写法规范
## 核心风格锚定词（所有图像/视频提示词必须开头注入）
```
wool felt animation style, real-world scene and characters rendered entirely in wool felt material, visible fiber texture covering all surfaces, soft rounded forms with no sharp edges, smooth and fluid motion, natural movement, warm muted color palette — full-size felt world at realistic scale, NOT miniature, NOT diorama, NOT puppet, NOT toy figurine; characters have clearly defined facial features (eyes, nose, mouth fully visible and readable)
```

---

## 元素图提示词规范（角色/场景/道具参考图）
### 结构顺序
风格锚定词 → 主体描述 → 材质细节 → 色彩 → 构图/背景 → 光线

### 写法要点
1. **主体描述**：用`felt [物体名]`开头，根据风格分级选择对应描述：
   - 写实感可爱（主要角色）：`natural proportions, clearly defined facial features (eyes, nose, mouth fully visible), soft round face, realistic body ratio`，禁用chibi、super deformed、big head small body、doll-like、puppet、toy figurine
   - 适度Q版（次要角色）：`slightly stylized proportions, rounded features, clear facial expression`
   - 高度Q版（人群/群像）：`chibi style, simplified but readable facial features, large head small body`
   - 场景/道具/食物：`full-size felt world, true-to-shape felt [物体名]`，还原实物造型，禁用miniature scale、diorama、puppet stage；避免要求渲染文字/字体
2. **材质细节**：必须包含至少2项：`visible wool fibers, slightly uneven handmade surface, soft fabric sheen, felted texture`
3. **色彩**：使用暖哑色描述，如`warm terracotta, dusty rose, muted sage green, creamy off-white`，避免高饱和纯色（bright red, neon等）
4. **构图（固定）**：`three-view character sheet, front view / side view / three-quarter back view, left to right, white background, clean studio lighting`
5. **光线（固定）**：`soft diffused lighting, no harsh shadows, warm ambient glow`

### 角色示例
```
wool felt animation style, real-world character rendered in wool felt material, visible fiber texture on all surfaces, soft rounded forms with no sharp edges, smooth and fluid motion, natural movement, warm muted color palette — felt elderly woman, natural body proportions, chubby round face with clearly defined eyes, nose and mouth, wearing dusty rose apron over cream knitted sweater, short white hair, rosy cheeks, holding a felted dumpling tray, visible wool fibers, slightly uneven handmade surface, soft fabric sheen — three-view character sheet, front view / side view / three-quarter back view, left to right, white background, soft diffused lighting, no harsh shadows, NOT a puppet, NOT a doll, NOT a toy figurine, NOT miniature scale
```

---

## 视频提示词规范（逐镜头生成）
### 结构顺序
参考图绑定 → 风格锚定词 → 场景氛围 → 分段动作脚本（时间区间顺序排列）→ 音效提示 → 反向约束

### 写法要点
1. **参考图绑定**：首行注明参考图对应关系，格式：`<<<image_1>>> is the felt character [角色名], <<<image_2>>> is the felt scene background`，按顺序绑定角色正面图、场景全景图
2. **分段动作脚本（核心）**：对应故事板镜头内部分段，按时间顺序逐段写出，格式：`[0–4s] ..., [4–10s] ..., [10–14s] ...`
   - 每段必须包含：主体动作 + 运镜方式
   - 时间区间与故事板分段严格对齐，不得合并或超出总时长
   - 动作描述：使用流畅柔和的动作词汇（walks smoothly, gently reaches out, turns around softly, nods with a warm smile等），避免僵硬卡顿词（jerky, stiff, stuttering motion）或过度剧烈动作（swings arms wildly, jumps frantically）
   - 运镜：使用自然流畅的镜头运动（smooth slow push in, gentle tracking shot, soft pan等），禁止handheld shake, fast zoom, rapid cuts, jerky camera
3. **场景氛围**：补充`warm soft light filling the scene, shallow depth of field, full-size felt world, immersive real-world scale`，禁用miniature scale diorama feel / puppet stage
4. **音效（SFX）**：用`<...>`标注自然音效，如`<soft fabric rustling>, <gentle tap on wooden counter>, <quiet ambient kitchen hum>`；若有独立旁白音轨，标注`<no dialogue, narration on separate track>`，不写台词内容
5. **固定反向约束（末尾必须追加）**：`no subtitles, no text overlay, no sharp edges, no realistic human skin, no CG glossy material, no puppet, no doll figurine, no miniature diorama, no toy stage`

### 视频镜头示例
```
<<<image_1>>> is the felt elderly woman character, <<<image_2>>> is the felt dumpling restaurant scene background — wool felt animation style, real-world scene rendered entirely in wool felt material, smooth and fluid motion, natural movement, warm muted color palette — cozy full-size felt dumpling restaurant interior at realistic scale, warm amber light, steamy atmosphere —
[0–4s] the felt elderly woman stands at the counter, both hands gently lifting a tray of dumplings, camera holds at medium shot with a subtle slow push in;
[4–10s] she sets the tray down softly, slowly raises her head, eyes crinkling with a warm smile, camera continues pushing toward her face;
[10–14s] close-up on her expression, slight head tilt, soft ambient steam drifts across frame, camera locks off on her face as the shot settles —
<soft clinking of ceramic plate>, <gentle kitchen ambient hum> — no subtitles, no text overlay, no sharp edges, no realistic human skin, no CG glossy material, no puppet, no doll figurine, no miniature diorama, no toy stage
```

---

## BGM/旁白提示词规范
### BGM（纯音乐）
结构：情绪描述 + 乐器 + 节奏 + 适配场景
示例：`warm and heartwarming instrumental, soft piano and light acoustic guitar, gentle slow tempo, cozy nostalgic mood, suitable for a handcraft wool felt animation short`
要求：时长与视频总时长对齐，风格温暖柔和，匹配羊毛毡手工质感

### 旁白（配音）
结构：语速 + 情感基调 + 旁白文案
要求：
- 语速默认`slow and warm`，情感基调根据内容调整（gentle, sincere, slightly nostalgic, cheerful等）
- 脚本内容直接使用故事板中各镜头的旁白文案，原文不做改动
- 逐段生成，绑定到对应镜头