# Seedance / Video Generation Tool 稳定生成合约

Use this reference after all task-relevant references have been read and before any video-generation call or handoff.

本文件负责把商品、达人、脚本、平台、品类、表演、文字、物理、光影、运镜和质检规则，编译成视频生成工具可直接执行的内部生成包。用户默认只看到达人参考图和简洁脚本；完整生成包直接传给 Seedance / video generation tool。

## Core Contract

Before video generation, create one internal `seedance_generation_package`.

The package contains:

1. `material_manifest`
2. `product_identity_lock`
3. `creator_identity_lock`
4. `global_visual_bible`
5. `audio_and_text_bible`
6. `shot_instructions`
7. `continuity_ledger`
8. `final_render_checks`

The package is an internal tool payload. Keep it out of the normal user-facing answer. Show it only when the user explicitly asks for the full model prompt, tool payload, audit details, or generation contract.

## Reference Compilation Gate

Every relevant reference must change a concrete field in the generation package.

- `input-consistency-rules.md` -> `material_manifest`, `product_identity_lock`, exact facts and claims
- `portrait-image-rules.md` and `creator-persona-library.md` -> `creator_identity_lock`
- `production-scenarios.md` -> shot structure and allowed adaptation freedom
- `creative-strategy-focus.md` and `creative-type-library.md` -> hook, proof method, scene progression and shot purpose
- `hook-library.md` -> shot 1 action, expression and spoken line
- `benefit-voiceover-library.md` -> proof actions and benefit lines
- `cta-library.md` -> final action and CTA line
- `category-strategy.md` -> product handling, proof form, scale anchor and category-specific detail
- `platform-rules.md` -> aspect ratio, pacing, framing, text safe area and CTA behavior
- `performance-rules.md` -> product continuity, hand/body motion, physical causality, audio sync and transitions
- `text-accuracy-rules.md` -> exact text source, placement, timing and subtitle behavior
- `marketing-expression-rules.md` -> main selling point, human benefit, proof and conversion logic
- `diversity-rules.md` -> controlled differences between variants
- `seedance-prompt-rules.md` -> positive executable wording
- `quality-checklist.md` -> `final_render_checks`

A reference is not considered applied when it is only summarized. Its conclusion must appear in a global field, a shot field, or a final check.

## Material Manifest / 素材清单

Assign a stable ID and role to every input asset before prompt writing.

```text
material_manifest:
  product_ref_1:
    source:
    role: primary_product_identity
    authoritative_for: silhouette, color, package, logo, label, material, cap/nozzle/button layout
  product_ref_2:
    source:
    role: secondary_angle_or_variant
    authoritative_for:
  detail_ref_1:
    source:
    role: texture_or_detail
  ui_ref_1:
    source:
    role: price_coupon_order_or_app_evidence
  creator_ref_1:
    source: creator_portrait_image
    role: protagonist_identity
```

Rules:

- User product assets define product appearance.
- `creator_portrait_image` defines the protagonist only.
- Screenshot/UI assets define verified page facts and layout evidence.
- Reference-video assets define rhythm, framing or creative structure only; current user product assets define product identity.
- Each shot lists the exact asset IDs it uses.
- A shot with the physical product includes at least one `product_ref_*`.
- A creator shot includes `creator_ref_1`.
- A UI shot includes the relevant `ui_ref_*` and returns to the physical product in the next beat.
- A UI shot uses one authoritative screenshot or one device page at a time.
- Screenshot sequences use separate shots or sequential device-page changes. Each frame has one readable page plane instead of a collage, tiled layout, layered stack or multiple overlapping screenshots.

## Product Identity Lock / 商品身份锁

Build a detailed product fingerprint from user assets.

```text
product_identity_lock:
  product_name:
  brand:
  category:
  exact_sku_or_variant:
  object_count:
  silhouette_and_proportions:
  dominant_and_secondary_colors:
  material_and_surface_finish:
  package_structure:
  logo_position_and_orientation:
  label_layout_and_key_graphics:
  cap_nozzle_handle_button_port_layout:
  included_accessories:
  product_vs_package_relationship:
  real_world_scale_anchor:
  visible_distinctive_details:
  allowed_states:
  allowed_variants:
  exact_offer_and_claim_facts:
  source_asset_ids:
```

Seedance-facing execution:

- Every physical-product shot repeats the same product fingerprint and its source asset IDs.
- The product keeps the same silhouette, proportion, color, material, package structure, logo position, label composition and distinctive parts across wide, medium and close shots.
- The product remains the exact selected SKU or variant for the whole connected action.
- Package and usable item remain clearly identified as two related objects when both appear.
- Product scale remains stable relative to the same hand, face, table, shelf, plate, bag, room or device.
- Label and logo face the intended direction established in the hero shot.
- One shot manipulates one selected item or one visibly supported group.
- Variant changes use an explicit reset shot and list the new variant asset ID.

For each shot, include:

```text
product_state:
  asset_id:
  selected_sku:
  orientation:
  screen_side_or_label_side:
  holder_or_support:
  location_in_frame:
  scale_anchor:
  state_at_start:
  state_at_end:
```

## Creator Identity Lock / 达人身份锁

```text
creator_identity_lock:
  source_asset_id: creator_ref_1
  role:
  age_band:
  face_identity:
  hairstyle:
  makeup_or_grooming:
  outfit:
  body_proportion:
  speaking_tone:
  product_relationship:
  default_hand_dominance:
  scene_relationship:
```

Seedance-facing execution:

- All creator shots use the same face, age impression, hairstyle, outfit logic, body proportion and role.
- The creator’s expression changes naturally while identity remains stable.
- On-camera speech uses the current `spoken_line`.
- Hands connect visibly to the same creator’s wrists and forearms.
- Default product interaction uses one visible hand. Two-handed actions show a natural left-right pair from the same person.
- Each visible hand has five aligned fingers, readable joints, natural scale and a comfortable product-use angle.
- The lens-facing foreground remains clear. Hands stay on the product interaction plane at a natural distance from the camera, with wrists and forearms visibly connected to the creator.
- A cut occurs after the hand action reaches a stable end state; the next shot begins from an established composition with the correct number of hands.

## Global Visual Bible / 全局视觉圣经

Define one global visual system before writing shots.

```text
global_visual_bible:
  aspect_ratio:
  duration:
  platform:
  content_type:
  visual_texture:
  primary_scene:
  background_layout:
  color_palette:
  wardrobe_palette:
  key_light:
  fill_light:
  practical_lights:
  color_temperature:
  exposure_and_white_balance:
  contrast_and_skin_tone:
  depth_of_field:
  camera_height:
  lens_feel:
  stabilization:
  motion_style:
  product_hero_orientation:
  text_safe_area:
  foreground_clarity:
  ui_display_mode:
```

Default domestic UGC visual system:

- Real phone-camera texture with natural detail and moderate sharpening.
- One believable home, office, store, vanity, kitchen, travel or product-use setting.
- The same scene keeps the same wall, table, furniture, window direction and practical-light position.
- Skin tone stays natural and exposure remains stable.
- Product colors remain neutral and faithful to source assets.
- Camera movement feels like one person filming a real recommendation.
- Foreground clarity stays readable throughout the video; face, mouth, product and product label remain visible during speech and proof.
- UI display mode defaults to one device and one page per shot, with the device plane facing the camera at a readable angle.

## Lighting Instructions / 光影指令

Each shot must specify lighting as physical information, not an abstract mood word.

Required fields:

```text
lighting:
  key_source:
  key_direction:
  key_softness:
  color_temperature:
  fill_level:
  practical_source:
  subject_exposure:
  product_highlight_control:
  background_brightness:
  continuity_from_previous_shot:
```

Execution rules:

- Choose one primary light source for a connected scene: window daylight, ceiling ambient light, vanity light, store light, desk lamp or outdoor daylight.
- State the light direction relative to the creator and product: front-left, front-right, side, back-side or overhead.
- State softness: curtain-filtered soft light, cloudy soft light, broad indoor ambient light or controlled direct sunlight.
- Keep color temperature and white balance consistent inside the same scene.
- Keep face and product readable in the same exposure range.
- Product highlights reveal material while preserving package color and printed details.
- Reflective products use broad soft highlights with readable edges.
- Matte products use gentle side light to reveal surface texture.
- Transparent bottles use side or back-side light plus a readable front label.
- Food uses soft side light to reveal texture and moisture while preserving natural color.
- Screens and phone UI use lower surrounding exposure so screen content remains readable.
- Connected shots inherit the previous light direction, shadow direction and background brightness.

Avoid sending vague phrases such as `高级光影`, `电影感打光`, or `氛围感强` alone. Convert them into the required physical fields.

## Camera And Motion Instructions / 镜头与运镜指令

Each shot has one defined camera state and at most one primary camera movement.

Required fields:

```text
camera:
  shot_size:
  camera_angle:
  camera_height:
  lens_feel:
  framing:
  subject_position:
  product_position:
  focus_target:
  depth_of_field:
  stabilization:
  movement:
  movement_start:
  movement_end:
  movement_speed:
  movement_distance:
  hold_before_or_after_motion:
```

Recommended executable choices:

- Shot size: wide, medium, waist-up, chest-up, close-up, macro detail.
- Angle: eye-level, slight high angle, tabletop top-down, 30-degree product angle, low product hero angle.
- Lens feel: phone wide, natural phone main-camera, portrait-like medium focal length, macro detail.
- Stabilization: stable tripod-like phone, supported handheld, gentle handheld, controlled gimbal-like follow.
- Movement: static hold, slow push-in, short pull-back, horizontal pan, small tilt, hand-follow tracking, product-follow tracking, rack focus.

Execution rules:

- Write a visible start composition and visible end composition for every movement.
- State movement speed and distance: for example, `0.8秒缓慢推近约15厘米，然后稳定停留1秒`.
- Camera movement follows a story purpose: reveal product, follow hand, move from face to product, reveal result or land on CTA.
- Product identity remains readable during movement.
- Focus stays on one target or changes once through an explicit rack focus.
- Camera height and horizon remain stable inside one connected scene.
- Close-ups follow a medium shot that establishes product location and handling.
- Proof shots hold long enough for the action and result to be read.
- Transition cuts happen after the action reaches a stable end state.
- During transitions, the foreground remains clear and the lens view stays readable. The next shot starts from a stable product, creator and camera state.

Avoid sending vague phrases such as `镜头高级`, `丝滑运镜`, `快速切换`, or `多角度展示` alone. Replace them with exact shot size, movement, start, end, speed and purpose.

## Shot Instruction Schema / 逐镜指令

Compile every script beat into this schema:

```text
shot_instructions:
  - shot_id:
    time_range:
    duration:
    narrative_purpose:
    source_asset_ids:
    creator_state:
    product_state:
    scene_and_background:
    composition:
    lighting:
    camera:
    main_action:
    action_cause_and_effect:
    hand_and_body_mechanics:
    spoken_line:
    voice_delivery:
    lip_sync_or_voiceover_mode:
    product_sound:
    bgm_behavior:
    in_frame_text:
    ui_state:
    transition_in:
    transition_out:
    continuity_anchor:
    end_frame_state:
```

Each shot:

- lasts long enough to complete one action and one spoken line
- binds the exact product asset and creator asset
- starts from a defined physical state
- completes one visible cause-and-effect action
- ends in a stable state used by the next shot
- specifies light and camera independently
- uses one spoken line
- uses optional short in-frame text from verified source text
- uses at most one UI screenshot/page plane when a UI asset is required

## Physical Action And Hand Detail / 动作与手部细节

Write actions as a sequential chain:

```text
起始姿态 -> 手接近商品 -> 接触点 -> 拿起/打开/按压/倒出/涂抹/穿戴/点击 -> 商品响应 -> 可见结果 -> 商品放稳或人物反应
```

Include:

- which hand acts
- where the hand enters from
- exact grip or contact point
- product support surface
- product orientation before and after action
- object count being manipulated
- visible result

Use real support for groups: table, tray, box, basket, shelf, hanger, bag, plate, bowl, cart, two hands or packaging insert.

For every hand-visible shot, specify:

```text
hand_and_body_mechanics:
  acting_hand:
  visible_hand_count:
  entry_direction:
  wrist_and_forearm_connection:
  grip_or_contact_point:
  distance_from_lens:
  product_support:
  anatomically_natural_angle:
  stable_end_pose:
```

Use one visible hand for one-handed product actions. Use one natural left-right pair for two-handed actions. Keep each hand connected to a visible wrist/forearm and keep five aligned fingers readable when fingers are visible.

## Audio, Speech And Text / 声音、口播与文字

```text
audio_and_text_bible:
  spoken_language:
  voice_character:
  speech_rate:
  pause_length:
  bgm_style:
  bgm_level:
  product_sound_priority:
  subtitle_mode:
  in_frame_text_style:
  exact_text_source:
  spoken_line_uniqueness:
  articulation:
```

Execution:

- One short spoken line per shot.
- Each shot uses a distinct spoken sentence. Adjacent shots differ in wording and meaning while advancing hook, proof, result and CTA.
- On-camera mouth movement matches the exact current spoken line.
- Off-camera voiceover pairs with the matching product action or proof.
- Speech uses clear standard Mandarin, complete syllables and natural phrase endings.
- Default Chinese speech rate is a natural medium pace of about 3.5 to 4.5 Chinese characters per second. Keep one short pause after each line for the action to finish.
- The audio track speaks only the current shot's `spoken_line`; previous and next lines remain silent outside their own time ranges.
- BGM remains lower than speech.
- Product sounds appear at contact, opening, pouring, clicking, spraying or placement moments.
- Default `subtitle_mode` is `none`. When subtitles are explicitly requested, render one subtitle layer that reuses the exact current `spoken_line`, start time and end time.
- In-frame text uses verified product names, offers, results or CTA wording.
- Text appears after the related visual evidence enters frame and remains stable long enough to read.

For UI/screenshot shots, include:

```text
ui_state:
  source_asset_id:
  display_surface: phone_or_tablet_or_laptop_or_single_pip_panel
  page_count_in_frame: 1
  screen_orientation:
  readable_region:
  camera_motion: static_or_very_slow
  return_target_next_shot: physical_product_or_creator_or_store
```

## Continuity Ledger / 连续性账本

Track connected states across shots:

```text
continuity_ledger:
  shot_1_to_2:
    creator_position:
    hand_position:
    product_position:
    product_orientation:
    product_state:
    scene:
    light_direction:
    camera_height:
    gaze_direction:
    audio_bridge:
  shot_2_to_3:
  shot_3_to_4:
```

The next shot either:

1. inherits the listed state, or
2. uses a clear reset shot that establishes the new state.

## Internal Tool Payload Template

```text
seedance_generation_package:
  material_manifest: ...
  product_identity_lock: ...
  creator_identity_lock: ...
  global_visual_bible: ...
  audio_and_text_bible: ...
  shot_instructions:
    - shot 1 ...
    - shot 2 ...
    - shot 3 ...
    - shot 4 ...
  continuity_ledger: ...
  final_render_checks:
    - each physical-product shot cites a product source asset
    - product fingerprint is identical across connected shots
    - creator identity is identical across creator shots
    - lighting direction and color temperature remain continuous
    - every camera movement has a start, end, speed and purpose
    - every action has a start state, contact, response and end state
    - speech, mouth movement, action and optional text describe the same beat
    - every shot has a unique spoken line and natural medium speech rate
    - default subtitle mode is none; requested subtitles exactly match the current spoken line
    - each UI shot contains one readable page plane and one authoritative UI source
    - foreground remains clear during transitions and hands remain connected to natural wrists and forearms
    - visible hand count and angles remain anatomically natural for the defined action
    - final CTA uses one next action
```

## User-Facing Separation

Default user-facing output stays simple:

```text
达人参考图
[image]

脚本
0-3s: 画面动作；口播：“……”
3-7s: 画面动作；口播：“……”
7-12s: 画面动作；口播：“……”
12-15s: 画面动作；口播：“……”
```

The detailed `seedance_generation_package` is passed to the video generation tool. It is not appended to the normal user-facing script.
