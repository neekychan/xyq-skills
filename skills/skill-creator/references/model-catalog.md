# 可选模型字段与支持的模型清单

> **何时读本文件：** 仅当需要给产出技能设置 `image_model` / `video_model` 时才读——即 ① 用户显式要求指定模型；② 用户输入 / 上传的技能内容里出现了模型相关信息；③ 需要把支持的模型清单反问给用户。**其余情况不必读，也不要设置这两个字段。**

## 目录

1. 字段语义与硬规则
2. 支持的图片模型（`image_model`）
3. 支持的视频模型（`video_model`）
4. 取值匹配与反问话术
5. 写法示例
6. 自检

## 1. 字段语义与硬规则

产出技能的 frontmatter 支持两个**可选**字段，用于把该技能的生成模型固定下来：

| 字段 | 作用 | 取值 |
|---|---|---|
| `image_model` | 指定该技能生成图片时使用的模型 | 取自第 2 节表格的 `value` 列，单个值 |
| `video_model` | 指定该技能生成视频时使用的模型 | 取自第 3 节表格的 `value` 列，单个值 |

硬规则：

1. **两个字段都是可选的，默认不写。** 缺省时由平台按默认模型执行——这在绝大多数技能里都是正确选择。**绝不主动替用户设置模型。**
2. **取值必须逐字命中白名单的 `value`（大小写敏感）。** 不得自造、不得写 `label`（如写 `Seedream 5.0 Lite` 是错的，应写 `seedream_5.0`）、不得写版本号变体。
3. **每个字段只允许一个值**（字符串，不是列表）。
4. **必须与 `tools` 自洽**：写了 `image_model` 则 `tools` 必须含图片生成工具；写了 `video_model` 则 `tools` 必须含视频三件套。否则校验失败。
5. **模型名只允许出现在这两个 frontmatter 字段里。** SKILL.md 正文与所有 references 一律以能力方式描述（"生成一张图片" / "生成一段视频"），不得点名任何模型。
6. 用户要求的模型不在白名单里时，**不要就近替换、不要静默降级**，按第 4 节把支持的清单反问给用户，等其选定后再写。

## 2. 支持的图片模型（`image_model`）

| 展示名（label） | 取值（value，写进 frontmatter） |
|---|---|
| Seedream 5.0 Pro | `seedream_5.0_pro` |
| Seedream 5.0 Lite | `seedream_5.0` |
| Seedream 4.0 美感版 | `seedream_4.3` |
| 旗舰生图模型 V2-Flash | `nova2` |
| Seedream 4.5 | `seedream_4.5` |
| Seedream 4.1 | `seedream_4.1` |
| Seedream 4 | `seedream_4` |
| Nano Banana Pro | `nano_banana_pro_1` |

## 3. 支持的视频模型（`video_model`）

| 展示名（label） | 取值（value，写进 frontmatter） |
|---|---|
| Seedance 2.5 | `Seedance_2.5` |
| Seedance 2.0 Mini 体验版 | `Seedance_2.0_mini_lite` |
| Seedance 2.0 Mini | `Seedance_2.0_mini` |
| Seedance 2.0 Fast VIP | `seedance2.0_fast_vision` |
| Seedance 2.0 VIP | `seedance2.0_vision` |
| Seedance 2.0 Fast | `seedance_2.0_fast` |
| Seedance 2.0 | `seedance2.0_direct` |

> ⚠️ 视频模型的 `value` 大小写与分隔符**不统一**（`Seedance_2.5` 与 `seedance2.0_direct` 并存），务必从表格逐字复制，不要按规律推断。

## 4. 取值匹配与反问话术

拿到用户提到的模型说法后按顺序处理：

1. **能唯一对应白名单的 label 或 value**（含常见写法差异：大小写、空格与下划线、`Seedream 5.0 Lite` ↔ `seedream_5.0`）→ 直接写入对应 `value`，无需确认。
2. **说法笼统但范围唯一**（如只说"用 Nano Banana Pro"）→ 命中唯一条目即可写入。
3. **说法笼统且对应多个条目**（如只说"Seedream 5.0"、"Seedance 2.0"）→ 列出该系列的候选项请用户选一个，不要自行挑一个。
4. **不在白名单内**（如某个未支持的版本或其他厂商模型）→ 明确说明不支持，并给出当前支持的清单请其改选。

反问模板（按图片 / 视频取用对应清单，只列相关那一类）：

```
你指定的模型「<用户原话>」暂不在支持范围内。当前支持的<图片 / 视频>模型有：
- <展示名 1>
- <展示名 2>
- …
选一个我就写进技能；不指定的话我就不设置这个字段，走平台默认模型。
```

> 反问时只展示**展示名（label）**，取值（value）由你负责翻译成 frontmatter，不必让用户记。

## 5. 写法示例

只生图、且用户明确要求 Seedream 5.0 Lite：

```yaml
---
name: product-poster
display_name: 商品海报
description: 根据商品素材生成营销海报；当用户提供商品图与卖点并要求出海报时触发。
tools: ["sandbox_generate_image"]
image_model: seedream_5.0
---
```

图片 + 视频，且用户对两者都指定了模型：

```yaml
---
name: product-promo
display_name: 商品短片
description: 根据商品素材生成营销图与短视频；当用户提供商品图并要求做推广短片时触发。
tools: ["sandbox_generate_image", "render_video", "sandbox_generate_video", "sandbox_process_video"]
image_model: seedream_5.0_pro
video_model: Seedance_2.0_mini
---
```

用户没提模型（**默认情况**）——两个字段都不写：

```yaml
---
name: product-poster
display_name: 商品海报
description: 根据商品素材生成营销海报；当用户提供商品图与卖点并要求出海报时触发。
tools: ["sandbox_generate_image"]
---
```

## 6. 自检

- 用户没提模型时，是否**没有**擅自写入 `image_model` / `video_model`？
- 写入的值是否逐字来自上面表格的 `value` 列（而非 label、而非推断出的写法）？
- 字段与 `tools` 是否自洽（图片模型配图片工具、视频模型配视频三件套）？
- 用户提的模型不在清单内时，是否已把支持的清单反问给用户，而不是就近替换？
- 模型名是否只出现在 frontmatter 的这两个字段，正文与 references 里没有任何模型名？
