# 提示词模板库

## 核心风格关键词

### 英文核心关键词（所有提示词必须包含）
```
8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette
```

### 可补充关键词
```
sprite sheet, idle pose, walk cycle frames, jump frame, attack frame, transparent background, pixel-perfect edges, nearest-neighbor upscaling, no anti-aliasing, authentic retro game screenshot
```

### 中文通用风格句
```
8bit 像素风，复古街机游戏画面，横版卷轴游戏视角，限制色板，低分辨率像素块，清晰统一的像素边缘，tile-based 关卡结构，角色轮廓简单清楚，像早期游戏 sprite，不要写实，不要高清 3D，不要普通插画，不要马赛克滤镜。
```

## 负面提示词

### 中文负面提示词
```
高清 3D，写实，真实人物，真实摄影，电影摄影感，复杂景深，复杂光影，平滑插画，普通卡通，现代动画，马赛克滤镜，伪像素化，像素颗粒不统一，边缘模糊，抗锯齿，渐变过多，角色比例错误，sprite 比例变化，UI 混乱，文字乱码，过度细节，复杂材质，真实阴影，镜头乱飞，3D 旋转。
```

### 英文负面提示词
```
high-definition 3D, realistic rendering, real photography, cinematic lighting, depth of field, smooth illustration, modern cartoon, mosaic filter, fake pixelation, inconsistent pixel size, blurry edges, anti-aliasing, too many gradients, wrong character proportions, changing sprite scale, messy UI, broken text, excessive details, realistic materials, realistic shadows, flying camera, 3D rotation.
```

---

## 图片提示词模板

### 主角 sprite 模板

**中文模板：**
```
生成一个 8bit 像素风游戏主角 sprite。
角色设定：【填写角色身份、外观、服装、武器、性格特征】
画面要求：角色为横版卷轴游戏主角 sprite，正面或 3/4 侧面站姿，轮廓清晰，适合在复古街机游戏中使用。角色比例简单可读，头部、身体、武器和关键特征必须清楚。使用限制色板，低分辨率像素块，清晰统一的像素边缘，不要平滑插画，不要真实光影。
风格关键词：8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette。
输出要求：单个角色 sprite，干净背景或透明背景，像素颗粒统一，边缘不要模糊，适合作为游戏角色资产。
```

**英文模板：**
```
Create an 8bit pixel art game hero sprite.
Character: [describe the hero, outfit, weapon, personality, key visual features]
Image requirements: A side-scrolling retro arcade game hero sprite, front view or 3/4 side view, simple readable silhouette, clear head, body, weapon and iconic details. Use a limited color palette, low resolution pixel blocks, clean pixel edges, pixel-perfect shape, no smooth illustration, no realistic lighting.
Style keywords: 8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette.
Output: Single character sprite, clean background or transparent background, consistent pixel size, sharp pixel edges, suitable as a game sprite asset.
```

**主角 sprite 生成要求：**
- 轮廓简单，一眼能识别
- 颜色鲜明
- 适合 32x32 或 48x48
- 不要复杂五官、复杂衣褶、真实材质、写实头发、过多细节
- 可以有一个明确识别点（红围巾、蓝披风、发光剑、猫耳、宇航头盔等）

### sprite sheet 模板

**中文模板：**
```
生成一张 8bit 像素风角色 sprite sheet。
角色：【填写角色设定】
动作帧：待机 2 帧，走路 4 帧，跳跃 1 帧，攻击 2 帧，受伤 1 帧，胜利 1 帧。
画面要求：所有动作帧排列在同一张 sprite sheet 中，每个格子大小一致，角色比例一致，像素颗粒大小一致，限制色板，清晰像素边缘，无抗锯齿，适合横版卷轴复古街机游戏。角色轮廓必须简单可读，动作夸张但帧数少，像早期 8bit 游戏逐帧动画。
风格关键词：8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette。
负面要求：不要高清 3D，不要写实，不要普通插画，不要平滑卡通，不要复杂光影，不要角色比例变化，不要像素大小不统一，不要文字乱码。
```

**英文模板：**
```
Create an 8bit pixel art character sprite sheet.
Character: [describe the character]
Animation frames: 2 idle frames, 4 walking frames, 1 jump frame, 2 attack frames, 1 hurt frame, 1 victory frame.
Image requirements: All frames arranged in a clean sprite sheet grid, consistent frame size, consistent character proportions, consistent pixel size, limited color palette, clean pixel edges, no anti-aliasing, suitable for a side-scrolling retro arcade game. The silhouette must be simple and readable, the motion should feel like early 8bit frame-by-frame animation.
Style keywords: 8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette.
Negative prompt: No high-definition 3D, no realism, no smooth illustration, no modern cartoon rendering, no complex cinematic lighting, no changing character proportions, no inconsistent pixel size, no broken text.
```

### 横版关卡模板

**中文模板：**
```
生成一个 8bit 像素风横版卷轴游戏关卡画面。
关卡主题：【森林关 / 城堡关 / 宇宙关 / 地下城关 / 城市夜景关 / 自定义主题】
关卡内容：前景有可跳跃平台、地面 tile、金币、道具、障碍物。中景有主角站位区域和敌人巡逻区域。背景有主题环境元素，例如森林树木、城堡墙体、星空、地下城石墙、城市霓虹灯。画面上方有复古游戏 UI，包括血条、金币数、分数和关卡名。
画面要求：横版 side-scrolling game view，tile-based environment，低分辨率像素块，限制色板，像素颗粒统一，清晰像素边缘，角色和平台位置关系明确，画面像一张真正可玩的复古街机游戏截图。
风格关键词：8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette。
负面要求：不要高清 3D，不要写实，不要电影镜头，不要普通插画，不要马赛克滤镜，不要复杂景深，不要像素颗粒混乱，不要 UI 乱码。
```

**英文模板：**
```
Create an 8bit pixel art side-scrolling game level.
Level theme: [forest level / castle level / space level / dungeon level / neon city level / custom theme]
Level content: Foreground jump platforms, ground tiles, coins, props and obstacles. Midground hero position and enemy patrol area. Background elements matching the theme, such as trees, castle walls, stars, dungeon stones or neon city lights. Retro arcade UI at the top, including health bar, coin count, score and level name.
Image requirements: Side-scrolling game view, tile-based environment, low resolution pixel blocks, limited color palette, consistent pixel size, clean pixel edges, clear relationship between character, platforms and enemies. The image should look like a playable retro arcade game screenshot.
Style keywords: 8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette.
Negative prompt: No high-definition 3D, no realism, no cinematic camera, no smooth illustration, no mosaic filter, no complex depth of field, no inconsistent pixel size, no broken UI text.
```

**关卡生成要求：**
- 左侧是起点，右侧是目标
- 中间有平台、金币、小怪、障碍
- 上方有 UI
- 地面和平台符合 tile-based 逻辑
- 场景不要像普通插画背景
- 必须像能玩的游戏截图

### 首帧模板

**中文模板：**
```
生成一张 8bit 像素复古街机游戏短视频首帧。
画面主题：【填写游戏主题】
画面构图：主角位于画面左侧或中下方，面对关卡前方。前方有平台、金币、敌人和目标物。背景展示完整关卡氛围，例如森林、城堡、宇宙、地下城或城市夜景。画面上方有复古游戏 UI，包括血条、金币数、分数、生命数和关卡标题。整体像一张 80 年代街机游戏开场截图。
视觉要求：8bit 像素风，复古街机游戏画面，横版卷轴游戏视角，限制色板，低分辨率像素块，清晰统一的像素边缘，tile-based 关卡结构，角色轮廓简单清楚，平台和道具布局明确。
英文关键词：8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette, authentic retro arcade game screenshot。
负面要求：不要高清 3D，不要写实，不要普通插画，不要马赛克滤镜，不要电影摄影感，不要复杂光影，不要 UI 混乱，不要文字乱码。
```

**英文模板：**
```
Create an 8bit pixel art retro arcade game opening frame.
Theme: [describe the game theme]
Composition: The hero stands on the left side or lower center of the screen, facing forward into the level. Platforms, coins, enemies and the goal object appear ahead. The background shows the full level atmosphere, such as forest, castle, space, dungeon or neon city. Retro game UI appears at the top, including health bar, coin count, score, lives and level title. The whole image should look like an authentic 1980s arcade game opening screenshot.
Visual requirements: 8bit pixel art, retro arcade game, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment, simple readable silhouette, clear platform and prop layout.
Negative prompt: No high-definition 3D, no realism, no smooth illustration, no mosaic filter, no cinematic photography, no complex lighting, no messy UI, no broken text.
```

---

## 视频提示词模板

### 5 秒图生视频模板

**中文模板：**
```
请基于输入首帧生成 5 秒 8bit 像素复古街机风图生视频。
视频风格：保持 8bit 像素风，复古街机游戏画面，横版卷轴游戏视角，限制色板，低分辨率像素块，清晰统一的像素边缘，tile-based 关卡结构，角色轮廓简单清楚。画面必须像早期横版游戏，不要变成高清动画。
动作设计：主角保持 sprite 比例稳定，以低帧率逐帧动画的方式完成【填写动作：走两步 / 跳一下 / 挥剑 / 捡金币 / 打开宝箱 / 进入传送门】。动作要简洁、清楚、有复古游戏感，不要过于丝滑。
场景与 UI：关卡背景保持稳定，平台、金币、敌人和 UI 不要乱变。UI 可以轻微变化，例如金币数 +1 或分数增加。可以加入轻微屏幕闪烁和街机屏幕刷新感。
镜头：镜头保持横版 side-scrolling 视角，只允许轻微从左向右卷轴移动，不要镜头乱飞，不要 3D 旋转，不要电影运镜。
负面要求：不要高清 3D，不要写实，不要普通插画，不要丝滑动画，不要复杂光影，不要电影摄影感，不要像素颗粒不统一，不要角色比例变化，不要 UI 乱码，不要镜头乱飞。
```

**英文模板：**
```
Generate a 5-second image-to-video clip based on the input frame.
Video style: Keep the authentic 8bit pixel art style, retro arcade game look, side-scrolling game view, limited color palette, low resolution pixel blocks, clean pixel edges, tile-based environment and simple readable silhouette. The video must look like an early retro side-scrolling game, not a high-definition animation.
Action: The hero sprite keeps the same proportions and performs [walk two steps / small jump / sword attack / collect a coin / open a chest / enter a portal] with low-frame-rate frame-by-frame animation. The motion should be simple, readable and game-like, not smooth or realistic.
Scene and UI: Keep the level background stable. Platforms, coins, enemies and UI should not randomly change. The UI may slightly update, such as coin count +1 or score increase. Add subtle arcade screen flicker and low-frame-rate refresh feeling.
Camera: Keep a fixed side-scrolling view with only a slight horizontal scrolling movement from left to right. No flying camera, no 3D rotation, no cinematic camera movement.
Negative prompt: No high-definition 3D, no realism, no smooth illustration, no overly smooth animation, no complex cinematic lighting, no cinematic photography, no inconsistent pixel size, no changing character proportions, no broken UI text, no flying camera.
```

### 15 秒视频提示词结构

每个镜头的视频提示词必须包含以下 9 个字段：

```
视频时长：【填写秒数】
画面比例：【16:9 / 9:16 / 1:1】
使用资产：【@资产编号】
画面：【描述当前镜头画面】
动作：【主角动作、敌人动作、道具反馈】
UI：【血条、金币数、分数、关卡名、STAGE CLEAR 等变化】
镜头：保持横版卷轴游戏视角，镜头只做轻微【向右 / 固定 / 屏幕闪烁】移动，不要复杂运镜。
风格保持：保持 8bit 像素风，复古街机游戏画面，低分辨率像素块，限制色板，清晰统一的像素边缘，tile-based 关卡结构，角色轮廓简单清楚，动作像低帧率逐帧动画。
负面要求：不要高清 3D，不要写实，不要普通插画，不要丝滑动画，不要电影摄影感，不要复杂光影，不要 3D 旋转，不要镜头乱飞，不要角色比例变化，不要 UI 乱码，不要像素颗粒混乱。
```

**视频生成方式说明：**
- ≤15s 的视频用一次生成即可拿到完整成片
- beat 分镜（0-3s/3-7s/…）是同一次生成内部的时间轴描述，不等于要多次调用
- 只有成片超过 15 秒时，才拆成多个 ≤15s 片段分别生成，再做后处理拼接