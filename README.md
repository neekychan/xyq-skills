# xyq-skills

小云雀内部使用的 AI 视频生成 / AI 短剧 / Agent 工作流 skill 集合。

这里的 skills 不是可执行代码。它们是一套提示词工程文件、工作流配置和风格参考。每个 skill 包含 `SKILL.md`，说明它能解决什么问题、输入输出是什么、何时触发。

## 仓库结构

| 路径 | 内容 | 数量 |
|---|---|---|
| `skills/` | 短剧、风格化视频、营销视频、提示词模板等生成类 skills | 176 个 |
| `agents/skills/` | Agent 工作流、工具类 skills | 28 个 |

## skills 示例

### 短剧 / 风格化视频

| skill | 说明 |
|---|---|
| `3d-ancient-drama new` | 制作 3D 古风短剧，覆盖剧本、分镜、角色一致性、逐镜生成到成片 |
| `chinese-mythology-style` | 统一套上「东方神话梦境插画」画风 |
| `hongkong-noir-night-style` | 港夜迷离 / 王家卫复古胶片风格滤镜 |
| `shaw-brothers-wuxia-style` | 邵氏武侠风格视频 |
| `botanical-documentary` | 45 秒植物博物学纪录片 |
| `linglong-cinematic` | 《灵笼》风格半写实 3D CG 末日废土科幻长视频 |
| `cute-3d-healing-animation` | 软萌 3D 治愈动画短片 |
| `cat-workday-story` | 小猫职场拟人化短视频 |
| `depth_video` | 深度视频 / 运镜复刻，换人物或场景翻拍同款 |
| `anime-style-forge` | 二次元 / 动漫 / 角色风格化图片生成与转换 |

### 营销 / 商业视频

| skill | 说明 |
|---|---|
| `story-commerce-video` | 短剧风创意带货视频，含商品一致性约束 |
| `brand-film-30s` | 30 秒品牌大片 / TVC |
| `marketing-video-creator` | 营销视频创作器，从意图到成片 |
| `video_creation` | 通用视频创作，覆盖剧本、生成、编辑、合成 |
| `expert-product-promotion` | 专家型商品种草 / 卖点拆解视频 |

### Agent 工作流

| skill | 说明 |
|---|---|
| `hyperframes` | 用 HTML 渲染视频的入口 skill |
| `embedded-captions` | 给口播视频加字幕 / 特效字幕 |
| `captions-overlay` | 字幕排版覆盖层规则 |
| `talking-head-recut` | 给访谈 / 口播视频加动态图形包装 |
| `product-launch-video` | 产品发布 / 宣传视频 |
| `remotion-to-hyperframes` | 把 Remotion 源文件迁移到 HyperFrames |

## 来源

- `skills/`：主要来自 `skills_collection.zip` 短剧 / AI 视频生成 skill 合集。
- `agents/skills/`：来自内部 Agent 工作流 skill 集合。

## 注意事项

- 仓库内含字体、示例素材等二进制资源，工作区约 50 MB，完整克隆约 80 MB。
- 部分 skill 目录名包含空格，Windows 环境请注意路径兼容。
- skill 内容会随模型和平台能力持续更新，建议定期拉取最新版。


## 关键词

小云雀、xiaoyunque、AI 短剧、AI 视频生成、Seedance、Agent skills、短剧提示词、视频风格化、营销视频、Remotion、Hyperframes、视频工作流。
