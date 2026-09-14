# 图像生成提示词文法

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录
1. 主导画风标签
2. 线条与人物质感（对应镜头动能的画风缩放）
3. 人设三视图提示词规范
4. 场景四宫格提示词规范
5. 书法大字定格卡提示词规范
6. 五行特效画风质感标签
7. 写意碎落粒子与焦墨烟尘渲染标签

## 1. 主导画风标签（首部写入）

```
Wu Shan Wu Xing (雾山五行) anime style, traditional Chinese ink wash painting, dynamic ink splash (泼墨写意), gorgeous mineral pigment splash colors (泼彩叠彩: emerald green, malachite blue, cinnabar red, ochre, rich gold).
```

## 2. 线条与人物质感

### 静态/慢速镜头
```
refined fine-line ink wash painting, elegant delicate outlines (工笔细描, 纤细匀称线条), smooth wet-on-wet ink gradients, clean paper texture, peaceful posture.
```

### 动态/高能打击镜头
```
rough hand-drawn keyframe animation style, extremely thick charcoal ink lines (粗犷焦墨勾线), dry-brush scratch marks (枯笔飞白排线), massive explosive ink splatters (爆裂泼墨喷溅), raw sketch aesthetic, high-velocity action.
```

## 3. 人设三视图提示词规范

生成/重塑人物三视图时，额外追加：
```
character sheet, three-views study, front view, side view, back view, standing, white background
```
在提示词前部结合用户参考图特征进行融合重绘设计，确保生成的重塑概念图结构规整、干净，正面/侧面/背面三视图清晰，便于后续多模态理解与视频生成绑定。

## 4. 场景四宫格提示词规范

生成四宫格场景图时，提示词中必须强制加入：
```
scene design sheet, 4-grid layout (四宫格布局), no characters, no humans (无人物), clear white border separators, traditional Chinese ink wash style.
```
对四宫格固定分配内容显式量化声明：
```
Grid 1 (top-left) shows a panoramic establishing shot of the entire landscape (全景定场);
Grid 2 (top-right) shows a detailed close-up of scenic objects and furnishings like ancient trees, tables, or stone monuments (陈设特写);
Grid 3 (bottom-left) shows deep perspective lines and multi-layered depth of the scene (纵深透视);
Grid 4 (bottom-right) shows dramatic atmospheric lighting with gorgeous mineral pigment splash and heavy ink contrast (气氛光效).
```

## 5. 书法大字定格卡提示词规范

生成纯文字/大字定格图时，提示词必须使用极简黑白灰或高对比度泼彩设计：
```
gigantic traditional Chinese calligraphy characters in heavy black ink (重墨书法大字), bold aggressive calligraphic brushstrokes showing furious energy, bleeding ink on aged Xuan paper (宣纸宿墨渗透), splashing cinnabar red mineral pigment, dynamic black ink splatters, hyper-detailed traditional Chinese art style, extreme high-contrast, epic martial arts movie title cards, negative space (留白)
```
提示词中需用英文双引号和中文括号将要呈现的字重叠括起（例如：the words "【万火归一】" written on the center），确保文字边缘带有狂草干裂笔锋（dry-brush calligraphy edges），严禁生成任何人物、现代英文字体或 CGI 立体特效字。

## 6. 五行特效画风质感标签

### 金行特效及爆发态
基础："glowing gold calligraphy ink lines, metallic golden slashes, sharp gold dust, bright white light trails, physical weapon slashes"

爆发态追加："50% blinding white glowing razor-sharp metallic edges with blinding specular glints and lightning-fast linear weapon slashes (亮白镜面高光锋芒与线性极速光轨), 35% explosive shimmering gold foil flakes scattering dynamic golden sparkles (漫天激射流金与金箔碎屑), 15% stark pitch-black heavy charcoal outlines and heavy iron-ink skeletons (深黑重色焦墨骨架), dynamic metal grinding sparks, sharp metallic rim lights, dramatic extreme high-contrast lighting, traditional ink-wash action style"

### 木行特效及爆发态
基础："emerald green vines resembling wild cursive calligraphy brushstrokes, flying emerald energy leaves, vibrant green organic energy flows"

爆发态追加："65% vibrant emerald and malachite green organic energy flows with green subsurface scattering and ambient moss glow (带次表面散射与微光自发光的翠绿能量流), 20% heavy wild cursive pitch-black ink vines in whip-like motion (狂草焦墨鞭打藤蔓骨架), 15% glowing gold flying leaves with sharp calligraphy brush splits and sparkling gold wood splinters (洒金飞叶与木屑), high-contrast dynamic backlight, dappled rim light filtering through leaves, traditional ink-wash action style"

### 水行特效及爆发态
基础："flowing sapphire blue ink washes, translucent liquid water splash, freezing crystal ice shards, dark ink cracks in ice"

申屠子夜爆发态追加："60% deep indigo ink wash and viscous sapphire blue liquid ink splash (高粘滞深蓝水墨流体), 25% stark white frost and hoarfrost negative space on Xuan paper (白霜写意留白), 15% razor-sharp glowing crystalline ice blades showing internal light refraction and icy rim light (带内部折射与冰冷边缘轮廓反光的极寒冰刃), ultra-sharp brittle icy cracks, characters outlined in stark pitch-black heavy charcoal calligraphy brushstrokes (焦墨骨架), extreme high-contrast cold cinematic lighting, overwhelming chilling presence"

### 火行特效及爆发态
"blazing cinnabar red (朱砂红) and molten gold flames with high-frequency flickering convective motion (高频舔舐熔金流体烈焰), 70% explosive fiery energy and thermal wave space distortion (高热对流空间扭曲) contrasted with 30% stark pitch-black heavy charcoal outlines and dynamic flickering shadows (焦墨重色与极速闪烁硬边缘阴影), self-illuminating core casting dynamic crimson backlight on characters (烈焰强自发光反照), flying charcoal soot as black ink dots, extreme high-contrast traditional ink-wash action style"

### 土行特效及爆发态
基础："shattering rocks outlined in thick heavy dry-brush (飞白) black ink, floating dust storm, heavy ochre stone pillars"

爆发态追加："55% heavy shattering rocks outlined in thick dry-brush black ink and dry flying-white strokes with hard relief shadows (具硬朗阳角浮雕阴影的枯笔飞白焦墨巨石), 35% rich mineral ochre pigments and swirling golden dust clouds causing ray attenuation and heavy light scattering (造成光线遮挡衰减的赭石泼彩与漫天黄沙), 10% glowing white and hot gold seismic fracture lines casting under-light projection (亮白与暗金自发光地裂纹底光返照), highly textured rough paper surface, colossal weight and earth-shattering pressure, traditional ink-wash action style"

## 7. 写意碎落粒子与焦墨烟尘渲染标签

### 写意碎落粒子
严禁使用任何 CGI、魔法粒子或日漫光效词汇，必须从物理介质的写意破碎感出发：

- **矿物碎彩与碎屑**："shattered mineral pigment flakes (矿物泼彩碎屑), floating raw azurite particles (悬浮石青色粉微粒), raw cinnabar splinters (朱砂色斑碎屑), vibrant mineral pigment dust (矿物颜料飞落尘埃)"
- **神兵崩毁与金屑激射**："exploding shimmering gold foil flakes (金箔爆裂碎屑), scattering liquid gold dust particles (流金粒子), razor-sharp metallic silver spark flecks (刀剑撞击的银白锐利碎屑)"
- **书法笔痕与飞白碎痕**："sharp calligraphy brush-splinters (书法枯笔碎落屑), flying dry-brush charcoal flakes (飞散的焦墨纸屑), translucent dynamic ink splashes (半透明水墨飞溅飞落点)"

### 焦墨烟尘与妖煞毒雾
严禁使用平滑的 3D 立体烟雾、粒子体积烟等词，烟雾必须被赋予炭黑与枯笔摩擦的有机粗粝质感：

- **焦墨烟云与飞灰**："rough textured charcoal-ink smoke clouds (粗粝焦墨烟尘), swirling pitch-black carbon dust (飞舞的焦黑炭尘), fluttering burnt paper ash (飞落的焦灼宣纸纸灰), dense heavy carbon soot dispersion (浓稠焦墨烟灰扩散)"
- **妖煞毒雾**：妖兽攻击命中的破空痕迹使用"黑色、深紫（ochre/purple）或剧毒幽绿（toxic emerald green）的写意水墨破空痕迹"。

## 落 prompt 前自检

- 主导画风标签是否在提示词首部写入？
- 画风缩放是否与镜头动能匹配（静态工笔/动态焦墨）？
- 三视图提示词是否包含 front view, side view, back view, white background？
- 四宫格提示词是否包含 no characters 和四格固定分配声明？
- 书法大字卡是否用双引号+中文括号括起目标文字？
- 五行特效标签是否与角色属性对应？
- 爆发态追加标签是否包含色彩配比百分比？
- 粒子是否使用物理介质描述而非 CGI/魔法词汇？
- 烟尘是否使用焦墨/炭黑质感而非 3D 立体烟雾词汇？
