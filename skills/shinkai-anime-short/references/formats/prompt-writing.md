# Prompt 编写规范

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 统一风格关键词

所有 prompt 末尾必须附加（按需增减，不逐字照搬）：

Makoto Shinkai Animated Film, Beautiful Sky, Volumetric Light, Cinematic Anime Lighting, Emotional Atmosphere, Ultra Detailed Background, Masterpiece

## 元素图 Prompt

### 角色图

结构：
```
[角色名] full body portrait, [外观描述], [服装描述], [性格暗示的动作/表情], cinematic anime film still, Japanese animation style, [统一风格关键词], 2K
```

要点：
- 全身构图，非三视图
- 电影静帧感，非设定稿
- 外观描述具体到发色/发型/体型/衣着
- 不写否定式（用"自然朴素"代替"不华丽"）

### 场景图

结构：
```
[场景名], [天气+光线], [时间], [氛围描述], ultra detailed anime background, realistic environment, [统一风格关键词], 2K
```

要点：
- 高精度背景，动画电影级美术
- 天气和光线必须具体（如"黄昏，夕阳从左侧照射，体积光穿透云层"）
- 氛围词与色彩系一致（黄昏系→"warm golden, nostalgic"，雨天系→"cool blue-gray, melancholic"）

### 道具图

结构：
```
[物件名], [材质+细节], [情绪含义], cinematic prop, ultra detailed, [统一风格关键词], 2K
```

要点：
- 道具必须是情绪物件（信件、雨伞、项链、车票等），非功能工具
- 材质描述具体（"worn leather journal with faded ink stains"而非"old book"）

## 视频生成 Prompt

结构：
```
[M0x镜头语言] [运镜方向] [天气等级+具体天气] [色彩系] [主光源/次光源/环境光] [画面内容] [角色动作] [情绪], [统一风格关键词]
```

示例：
```
M06 逆光镜头, slow dolly forward, S级黄昏, 黄昏系, 夕阳主光/窗户反射次光/空气透视环境光, 少女站在天桥上望向远方的列车, 头发被风吹起, 离别与怀念, Makoto Shinkai Animated Film, Beautiful Sky, Volumetric Light, Cinematic Anime Lighting, Emotional Atmosphere, Ultra Detailed Background, Masterpiece
```

要点：
- 以镜头语言起手
- 天气必须具体到等级+类型
- 三种光源必须声明
- 正向措辞，不堆否定式约束
- 时长 ≤15s 的 shot 一次生成完整片段，多段 beat 写在同一条 prompt 内的时间轴

## 关键帧融合 Prompt

将同镜头的角色图 + 场景图 + 道具图合成为一张关键帧参考图：

结构：
```
[角色] standing in [场景], [天气+光线], [动作+情绪], [道具如有], cinematic anime film frame, [统一风格关键词], 2K
```

## 落 prompt 前自检

- 是否以镜头语言/主体类型起手？
- 天气+光源是否具体？
- 措辞是否正向（无"不要""禁止""无"等否定词）？
- 末尾是否附加统一风格关键词？
- 分辨率是否标明？