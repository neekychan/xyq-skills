# 提示词工程

## 目录
1. [提示词写作总则](#提示词写作总则)
2. [提示词结构模板](#提示词结构模板)
3. [必须包含的关键词](#必须包含的关键词)
4. [条件性关键词](#条件性关键词)
5. [质感关键词优先级](#质感关键词优先级)
6. [禁止出现的关键词](#禁止出现的关键词)
7. [参考示例](#参考示例)

---

## 提示词写作总则

**语言：** 提示词一律用**英文**撰写（供模型执行）；提示词结构说明和与用户的交流用中文。

**核心姿态：** 写提示词像一个文艺片导演在向摄影师下达指令——描述的是摄影机可以看见的东西，不写人物动机、心理分析，或画面以外的叙事背景。

---

## 提示词结构模板

```
[风格锚定词] + [光线条件] + [主体/人物状态] + [具体动作（微小）] + [环境细节] + [情绪方向] + [质感词] + [运镜指令]
```

---

## 必须包含的关键词

**风格锚定词（每次至少选 3 个）：**

slow cinematic, observational, emotionally restrained, East Asian arthouse, intimate, contemplative, naturalistic

**质感词（每次至少选 2 个）：**

film grain, soft focus, natural lighting, muted palette

**运镜描述词（每次必选 1 个）：**

| 类型 | 关键词 |
|---|---|
| 静态 | static camera, still frame, no camera movement |
| 微动 | subtle handheld, gentle drift, breathing motion |
| 缓推 | very slow push-in, gradual zoom |
| 横移 | slow lateral tracking |

---

## 条件性关键词

**人物情绪段落加入：**

micro-expression, subtle emotional shift, eyes looking away, quiet contemplation, internal emotion, restrained performance

**空镜/环境段落加入：**

empty space, lingering shot, atmospheric, environmental storytelling, symbolic object, passage of time, seasonal change

**东亚人文场景加入：**

East Asian daily life, local texture, humid air, narrow alley, warm interior light, handwritten sign, aging architecture, traditional market, monsoon season, quiet neighborhood

---

## 质感关键词优先级

按优先级从高到低：

film grain > soft natural light > shallow depth of field > muted colors > warm skin tone > gentle lens flare > atmospheric haze > subtle motion > lived-in environment > imperfect composition > quiet intimacy

---

## 禁止出现的关键词

| 禁止词 | 原因 |
|---|---|
| dramatic, intense, explosive | 触发模型生成剧烈动作 |
| fast, rapid, dynamic, energetic | 触发快速运动导致画面崩溃 |
| cinematic action, thriller | 风格漂移至商业类型片 |
| perfect skin, beautiful, glamorous | 触发修图审美，失去真实感 |
| neon, cyberpunk, futuristic | 色彩体系完全偏离 |
| drone shot, aerial view | 触发不稳定高空视角 |

---

## 参考示例

**人物独处情绪段落：**

> Slow cinematic, static camera, low angle, a woman sitting alone at a small kitchen table at night, cold meal untouched in front of her, fluorescent light overhead casting pale shadows, she stares at nothing, subtle breathing motion in her shoulders, cluttered kitchen background with aging wallpaper, quiet stillness, film grain, muted cool tones, shallow depth of field, East Asian apartment interior

**声画分离空镜（情绪爆发时的替代画面）：**

> Slow cinematic, static camera, an empty hallway in an old apartment building, afternoon sunlight coming through a dusty window, dust particles floating in the light beam, complete stillness, no people, worn tiles on the floor, a pair of old slippers by a door, atmospheric silence, film grain, warm muted tones

**东亚日常情感动作（不拍脸，只拍手）：**

> Slow cinematic, soft morning window light, close-up of aged hands carefully placing food into a lunch box, steam rising from freshly cooked rice, worn cutting board and familiar utensils in background, no face visible only hands and food, gentle and meticulous movements, warm muted tones, film grain, subtle handheld breathing motion, intimate domestic atmosphere

**结尾情绪释放镜头：**

> Slow cinematic, very slow push-in, a figure seen from behind standing at an open window, morning light flooding in, curtain gently moving with breeze, the person takes a deep breath and their shoulders drop slightly in release, atmospheric haze from morning air, film grain, soft warm tones fading toward gentle overexposure, contemplative and hopeful
