# 多样性规则 / Diversity Rules

Use this reference when generating multiple videos, revisions, variants, or when the user asks for more creativity. The goal is to reduce repeated scripts, repeated hooks, repeated creator roles, and repeated CTA wording while keeping product facts stable.

## Variation Dimensions

When creating more than one output, vary at least three dimensions:

1. creator persona
2. hook mechanism
3. proof action
4. scene
5. benefit wording
6. CTA wording
7. camera framing
8. music mood
9. product handling pattern
10. optional text style

Do not vary product identity, user-provided offer, or factual claims unless the user asks.

## Creator Variation

Rotate creator types when appropriate:

- 通勤女生
- 真实宝妈/家庭照顾者
- 美妆护肤测评朋友
- 男性实测/数码桌搭达人
- 小红书生活方式达人
- 快手实在型生活用户
- 探店/本地生活达人
- 游戏/IP 活动玩家
- 服饰穿搭/试穿达人

Each creator variation must still plausibly match product category and buyer.

## Hook Variation

Rotate hook types:

- 痛点直击
- 结果前置
- 价格/福利
- 实测挑战
- 朋友提醒
- 日常场景
- 探店到场
- 游戏/活动福利

Do not reuse the same first `spoken_line` across variants.

## Proof Variation

Change proof action instead of only changing words:

- hand demo
- close-up texture
- before/after comparison
- try-on movement
- package layout
- phone screen bridge
- store process
- bite/sip reaction
- setup/test result
- scale comparison

## CTA Variation

Use platform-matched CTA, but vary wording:

- 商品卡 / 领券 / 同款
- 收藏 / 评论 / 慢慢对比
- 团购券 / 预约 / 到店
- 咨询 / 了解详情
- 预约 / 下载 / 领福利

Keep one next action per variant.

## Multi-Version Output Contract

For 2-3 options, each option should include:

```text
方案名:
达人设定:
hook:
主利益点:
证明动作:
CTA:
script:
internal_generation_route:
```

`internal_generation_route` is a short route summary for compiling a separate `seedance_generation_package`; it is not shown unless the user requests model instructions. Keep each option distinct enough that the generated videos would not feel like the same template with changed wording.

## Anti-Repetition Check

Before final output, compare variants:

- First spoken lines differ.
- Creator roles differ or scenes differ.
- The main proof action differs.
- CTA wording differs.
- Optional text differs.
- The camera does not start the same way every time.
