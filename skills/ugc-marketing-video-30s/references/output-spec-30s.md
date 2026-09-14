# UGC Marketing Video 30s Output Spec

Use this as the final output contract for the Seedance 2.5 / 30-second UGC chain. It overrides copied 30-second output wording in older references.

## Default Chat Shape

For normal requests, return:

````text
思路简述：
{1-3 sentences explaining creator, hook, proof chain, and CTA.}

creator_portrait_image
{supplied or generated creator image reference when available/needed}

script
```text
0-3s: {hook / offer / pain trigger; spoken_line: "..."; optional text: "..."}
3-8s: {creator context and need; spoken_line: "..."; optional text: "..."}
8-14s: {product action and main selling point; spoken_line: "..."; optional text: "..."}
14-21s: {proof 1; spoken_line: "..."; optional text: "..."}
21-27s: {proof 2 / reaction / result; spoken_line: "..."; optional text: "..."}
27-30s: {value confirmation + CTA; spoken_line: "..."; optional text: "..."}
```

video_generation_prompt
```text
{paste-ready 30-second prompt}
```

确认后即可开始生成视频；也可以继续调整达人形象、卖点、风格、台词、尺寸或平台。
````

If the user says `只要 prompt`, output only `video_generation_prompt` and the fenced prompt.

## Prompt Contract

The visible prompt must include:

- duration and ratio: `30秒，9:16竖版`
- platform/content assumption, default Douyin UGC sales video if unspecified
- visual texture: phone-shot realism, natural light, real environment, slight handheld movement
- one primary selling point
- product visible early unless delayed reveal is structurally necessary
- active creator portrait reference when a person appears
- user product assets as product appearance source of truth
- 5-6 shot script rhythm
- two proof moments at most, both supporting the same selling point
- final CTA in 27-30s with one next step
- product, protagonist, text, lip-sync, physics, and marketing consistency controls

## 30s Rhythm

```text
0-3s: 钩子 / 优惠 / 痛点，商品或结果尽早出现
3-8s: 真实人物和场景可信度
8-14s: 商品动作 + 主卖点
14-21s: 证明1
21-27s: 证明2 / 结果 / 反应
27-30s: 价值确认 + 商品名 + CTA
```

## Guardrail

30 seconds should feel more convincing, not more crowded. Keep the creative spine simple:

`hook -> need -> product action -> proof -> reaction/result -> CTA`
