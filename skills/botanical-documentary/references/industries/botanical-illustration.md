# 植物科学解析图工艺规范 / Botanical Illustration Craft

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 生成规格

- 方式：文生图
- 分辨率：2K
- 比例：3:4 竖版
- 风格：复古羊皮纸纹理，18 世纪博物学水墨水彩风格

## 解析图六面板结构

每张植物解析图必须包含以下六个面板，缺一不可：

| 面板 | 内容 | 在图中的位置 |
|---|---|---|
| 整体形态大图 | 植物完整形态，根茎叶花果全貌 | 居中主体 |
| 放大截面细节 | 茎/果实/根茎横截面，放大镜框样式 | 右上或左上 |
| 叶形与花序解剖 | 叶片形状、花序结构、花瓣分解 | 右侧或左侧 |
| 产地小地图 | 原产地与引种区域标注 | 左上或右上小图 |
| 分子结构示意 | 核心活性成分分子式或结构简图 | 右下或左下 |
| 生命周期序列图 | 播种→萌发→生长→开花→结果的阶段序列 | 底部横排 |

## 提示词模板

```
Chinese botanical illustration of [植物学名]（[中文名]）,
retro vintage parchment paper texture, scientific botanical chart,
detailed ink and watercolor sketch, multipanel layout.
Central large [主要器官描述],
detailed cross-section under a magnifying glass,
anatomical diagrams of leaves and flowers,
small regional map, molecular structure diagrams,
step-by-step life cycle diagram at the bottom.
Elegant Chinese calligraphy headers and labels.
Highly detailed, accurate botanical drawing,
18th-century naturalist style, sepia tones, muted colors, aesthetic composition.
no watermarks, no modern UI, no neon colors.
```

## 色调约束

- 主色调：赭石暖褐 + 哑光草绿，占比 ≥ 90%
- 辅助色：暗金、深棕、墨黑（用于标注与线条）
- 禁止色：霓虹色、现代 UI 色、高饱和度亮色
- 质感：羊皮纸纹理底，水墨晕染与水彩层叠交替

## 示例（以华东覆盆子为参照）

```
Chinese botanical illustration of Rubus chingii（华东覆盆子）,
retro vintage parchment paper texture, scientific botanical chart,
detailed ink and watercolor sketch, multipanel layout.
Central large compound leaves and aggregate fruit,
detailed cross-section of drupelet under a magnifying glass,
anatomical diagrams of palmate leaves and white flowers,
small regional map of eastern China,
molecular structure diagrams of flavonoids and ellagic acid,
step-by-step life cycle diagram at the bottom.
Elegant Chinese calligraphy headers and labels.
Highly detailed, accurate botanical drawing,
18th-century naturalist style, sepia tones, muted colors, aesthetic composition.
no watermarks, no modern UI, no neon colors.
```

## 解析图作为全片视觉锚点的使用规范

Plant_Asset_01 生成后，在后续所有阶段中承担以下约束功能：
- **形态一致性基准**：三组视频中的植物叶形、花色、茎秆形态、根系外观必须与解析图一致
- **色彩弧光基色来源**：解析图中识别的主导色（赭石暖褐、哑光草绿等）作为 Section B/C 视频调色参考底色
- **科学标注内容来源**：解析图中的学名、科属、产地、成分信息作为 Section A 信息卡片文案素材
- **生命周期节点来源**：解析图底部生命周期序列图作为 Section B 生长过程的节拍划分依据

## 落 prompt 前自检

- [ ] 六面板是否全部涵盖？
- [ ] 色调是否以赭石暖褐与哑光草绿为主（≥ 90%）？
- [ ] 是否包含中文书法标注？
- [ ] 是否为 3:4 竖版？
- [ ] 负向词是否包含 no watermarks, no modern UI, no neon colors？
- [ ] 植物学名与中文名是否准确？
