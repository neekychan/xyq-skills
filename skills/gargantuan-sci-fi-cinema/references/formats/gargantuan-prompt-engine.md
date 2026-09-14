# Gargantuan Prompt Engine

> 本文件定义整个项目的标准Prompt生成规则。所有Prompt必须来自已确认的 Visual_Assets.md，不得脱离视觉资产。不允许临时增加巨物、不允许改变配色、发光颜色、尺度比例。

## 目录
1. Prompt总结构
2. 全局电影风格Prompt
3. 机甲图片Prompt
4. 怪兽图片Prompt
5. 场景图片Prompt
6. 视频Prompt核心结构
7. 视频Prompt写作规则（11条）
8. 图片Negative Prompt模板
9. 视频Negative Prompt模板
10. Prompt自动拼接规则
11. 统一检查

---

## 1. Prompt总结构

统一采用：**主体 → 环境 → 天气/光线 → 动作/镜头 → 摄影技术参数 → 画质 → 风格 → Negative Prompt**

标准格式：Subject, Environment, Weather/Lighting, Action/Camera Motion, Camera/Technical, Quality, Style, --ar XX:XX, Negative Prompt

## 2. 全局电影风格Prompt

整个项目统一固定：

```
Pacific Rim kaiju sci-fi cinema, epic gargantuan scale, low-angle worship shot, industrial heavy mecha, bioluminescent kaiju, deep sea atmosphere, storm rain weather, volumetric fog, cinematic realism, IMAX anamorphic, 35mm film grain, teal and orange color grading, desaturated disaster tone, masterpiece, best quality
```

全片不得修改。

## 3. 机甲图片Prompt

**统一格式：**
Mecha Name, Color Scheme, Armor Texture, Battle Damage State (factory-new/light damage/heavy damage/rust), Eye Window Status (dark/lit/color), Action/Posture, Environment, Lighting, Camera Angle, Lens, --ar 16:9, Negative Prompt

**战损状态规则（根据剧情阶段动态选择）：**
- 出厂/部署阶段：factory-new, pristine metal finish
- 首次战斗后：light battle damage, scratches
- 持续战斗或重伤后：heavy battle damage, oil stain, rust
- 同一镜头内不得混合不同战损阶段的外观

**示例（全新状态）：**
```
VANGUARD mecha, red black gold heavy industrial armor, white surface stripes, pristine factory-fresh metal finish no battle damage, rectangular white light eye window glowing, standing upright in ultra-high factory interior, cold industrial lighting, low-angle worship shot, 14mm ultra-wide lens, deep focus, Pacific Rim sci-fi cinema, cinematic realism, 8K
```

**示例（重度战损）：**
```
VANGUARD mecha, red black gold heavy industrial armor, white surface stripes, heavy battle damage weathered rust oil stain, rectangular white light eye window glowing, standing upright in stormy sea, cold industrial lighting, low-angle worship shot, 14mm ultra-wide lens, deep focus, Pacific Rim sci-fi cinema, cinematic realism, 8K
```

机甲固定信息来自Visual Assets，不得修改。

## 4. 怪兽图片Prompt

**统一格式：**
Kaiju Name, Skin Texture, Bioluminescent Vein Color, Eye Glow Color, Mouth State, Action/Posture, Environment, Lighting, Camera Angle, Lens, --ar 16:9, Negative Prompt

**示例：**
```
HOLLOW kaiju, dark gray petrified wood skin texture, sharp bone spines on spine, blue-green fluorescent veins pulsing across entire body, glowing cyan-blue eyes, massive jaws slightly open, towering over small fishing boat on stormy sea, low-angle worship shot, 16mm wide lens, deep focus, Pacific Rim kaiju horror cinema, cinematic realism, 8K
```

怪兽固定信息来自Visual Assets，不得修改。

## 5. 场景图片Prompt

**统一格式：**
Location, Weather, Time, Landscape Layers (foreground/middle/background), Scale Reference Visible, Lighting, Camera Angle, Lens, --ar 16:9, Negative Prompt

**示例：**
```
Deep sea stormy surface, heavy rain, dark thunderclouds, massive waves, foreground choppy water, middle ground fishing boat tiny scale, background thick fog hiding kaiju silhouette, blue-green bioluminescence pulsing faintly in fog, low-angle wide shot, 24mm lens, deep focus, Pacific Rim cinema, 8K
```

始终采用：Environment First, Scale Reference Visible。

## 6. 视频Prompt核心结构（关键）

视频Prompt必须包含**时间轴精确到秒**的动作描述。采用三层并行写法：

- **第一层：主体动作（巨物/参照物）**
- **第二层：环境反馈（天气/水面/地面/烟雾变化）**
- **第三层：镜头状态（运动/静止/震颤/晃动）**

**标准格式：**
```
【主体描述】+【环境描述】+【镜头描述】
【动作时序·精确到秒】
00:00-00:0X（阶段名）
主体动作：xxx
环境反馈：xxx
镜头状态：xxx
00:0X-00:0Y（阶段名）
...
【技术参数】+【负面提示词】
```

## 7. 视频Prompt写作规则（11条）

### 规则1：时间轴必须精确到秒
禁止写"前期/中期/后期"。必须写"00:00-00:03""00:03-00:06"。

### 规则2：三层并行，每秒都有事发生
每个时间段必须同时描述：巨物动作 + 环境反馈 + 镜头状态。禁止只有单一动作描述。

### 规则3：物理反馈必须有因果链
例如：巨手砸下 → 海面凹陷 → 环形巨浪 → 冲击波扩散。每一步都是上一步的结果。

### 规则4：发光变化必须写过程，不能只写结果
例如：眼窗"从黑暗→微弱脉动→突然点燃→亮度爬升→稳定发光"，5个阶段，不能只写"眼窗亮了"。

### 规则5：压迫感必须递进，不能一上来就满
按时间段递增：未知恐惧（轮廓）→ 局部揭露（部分身体）→ 全貌暴露（完整尺度）→ 终极压迫（俯视/对视）。

### 规则6：负面提示词=反向锁定关键动作
不仅写"不要什么"，还要锁定"必须发生什么"。例如：镜头分段剪辑 → 锁定一镜到底；巨人不转向镜头 → 锁定最终对视。

### 规则7：禁止AI无法理解的抽象词
禁止写："巨物感核心指令""史诗感""震撼感"。只写纯视觉动作描述。

### 规则8：材质细节必须具体
禁止写："钢缆紧绷"。必须写："钢缆被拽至极致紧绷、金属表层轻微扭曲变形"。

### 规则9：天气/大气必须全程存在
禁止在视频中段"天气消失"。暴雨/大雾/烟雾必须贯穿全程，或有明确的"消散/加重"叙事理由。

### 规则10：镜头语言必须匹配动作
- 巨物出现 → 缓慢后拉
- 冲击瞬间 → 镜头剧烈抖动
- 压迫感 → 极低角度仰拍不动
- 时间冻结 → 镜头突然静止

### 规则11：每个视频Prompt必须包含Negative Prompt
图片和视频都要有Negative Prompt，且内容不同。视频Negative Prompt必须包含反向锁定词。

## 8. 图片Negative Prompt（统一模板）

```
cartoon, anime, low quality, blurry, bright saturated color, smooth monster skin without texture, tiny scale, high-angle overhead shot, modern city, sunny weather, no fog no rain, floating object, suspended in air, incorrect scale reference, extra limbs, bad anatomy, watermark, text, logo, 3D render, CGI plastic look
```

## 9. 视频Negative Prompt（统一模板）

```
shot cut, multi-shot editing, stable static frame no camera motion, high-angle overhead shot, bright sunny weather, no rain no fog, mecha/monster disappears from frame, scale reference missing, tiny mecha/monster, cartoon anime style, low quality blurry, floating suspended in air, no physical interaction with water/ground, no splash no impact, no light change no glow process, eye window stays dark, gentle soft lighting no strong contrast, bright high-saturation color, modern building, 3D render, watermark text logo
```

## 10. Prompt自动拼接规则

系统按照固定顺序自动组合：
全局风格 → 主体Prompt → 环境Prompt → 动作/时序Prompt → 镜头Prompt → 摄影Prompt → 画质Prompt → Negative Prompt

输出格式：Image Prompt、Video Prompt、Negative Prompt 分别输出，不得混合。

## 11. 统一检查

生成Prompt后自动检查：
- 巨物外观一致
- 配色一致
- 发光元素一致
- 战损状态与剧情阶段匹配
- 天气一致
- 光线方向一致
- 海面波浪方向一致
- 参照物比例一致
- 镜头方向一致
- 摄影参数一致
- 色彩一致

若存在冲突，重新生成Prompt。

输出文件：Prompt_Bible.md，确认后进入视频生成阶段。

---

## 落 prompt 前自检

- [ ] 全局风格Prompt是否未修改
- [ ] 机甲/怪兽/场景Prompt是否来自已确认的Visual Assets
- [ ] 战损状态是否与剧情阶段匹配
- [ ] 视频Prompt是否包含精确到秒的时间轴
- [ ] 视频Prompt是否三层并行（主体动作+环境反馈+镜头状态）
- [ ] 物理反馈是否有因果链
- [ ] 发光变化是否写过程而非只写结果
- [ ] 压迫感是否递进
- [ ] 是否无抽象词（史诗感/震撼感等）
- [ ] 材质细节是否具体
- [ ] 天气是否全程存在
- [ ] 镜头语言是否匹配动作
- [ ] 是否包含Negative Prompt且内容正确
- [ ] 统一检查是否通过
