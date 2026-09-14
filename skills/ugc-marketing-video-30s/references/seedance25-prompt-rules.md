# Seedance 2.5 UGC Prompt Rules

Use this provisional reference for 30-second Seedance 2.5 UGC marketing, seeding, review, local-service, group-buying, product demo, game/IP/event conversion, reference remake, and sales-script-to-video prompts.

## Default Contract

- Follow the user's explicit duration first.
- If duration is not specified, use `30秒，9:16竖版`.
- Default platform remains Douyin when unspecified.
- Use 5-6 stable shots by default.
- Keep one primary selling point. 30 seconds allows more evidence, not more claims.
- Product should appear early when possible, usually within the first 3 seconds.
- Use Chinese spoken lines by default; subtitles only when the user requests them.

## Prompt Opening

Use:

```text
生成一条30秒9:16竖版UGC营销短视频，平台原生真实拍摄质感，苹果原相机拍摄风格，自然光，真实生活场景，轻微手持晃动。
```

Do not mention the model name inside the fenced `video_generation_prompt` unless the user explicitly asks.

## 30-Second Rhythm

```text
0-3s：强hook / 优惠 / 痛点，商品或结果尽早出现
3-8s：真实人物和场景可信度，建立为什么需要
8-14s：商品出现为行动，主卖点变清楚
14-21s：证明1，实操/流程/对比/门店/屏幕桥接
21-27s：证明2，结果/反应/社会证明/前后状态确认
27-30s：商品名 + 价值确认 + 一个自然CTA
```

Each shot should include one camera state, one main physical action, one short spoken line, and one clear endpoint.

## Positive Stability Blocks

Use compact positive control blocks when relevant:

- 商品外观全片保持与用户素材一致，包括形状、颜色、包装、logo位置、材质纹理、尺寸比例和已提供款式。
- 全片使用稳定5到6镜结构，每镜承载一个主要动作、一句短口播和一个产品证明点；镜头在动作完成、口播结束、产品放稳、表情变化或结果出现后自然切换。
- 主体1使用已确认的 creator_portrait_image 或用户提供的人像作为角色参考，全片保持同一脸部、发型、穿搭风格、身体比例和达人身份。
- 所有物体和人体动作符合真实物理与空间关系，多个物品按顺序拿起、放下或由双手、桌面、包装、托盘、货架、容器等稳定支撑承载。
- 每个镜头一句短 spoken_line，主体1口播时嘴型、表情和轻微头部动作自然同步；BGM 音量低于口播。
- 全片只突出一个主卖点，卖点通过可见动作证明，CTA 与平台和转化目标一致，并且只给一个下一步动作。

## Final Self-Check

- Prompt clearly says `30秒9:16竖版`.
- It has 5-6 shots unless the user asked otherwise.
- Product appears early or the reason for delayed reveal is built into the hook.
- There are two proof moments at most; both support the same selling point.
- CTA appears in the final 3 seconds and contains one next action.
- The visible prompt uses positive execution wording.
