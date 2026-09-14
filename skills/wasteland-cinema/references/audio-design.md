# 废土工业音频设计规范

> 这些是可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录

1. 旁白配音与声学语调设计规范
2. 背景音乐生成规范
3. 公路对撞物理声学资产规范

## 1. 旁白配音与声学语调设计规范

### 声音画像（narration_speaker_profile）
定义为"沙哑、粗粝、饱经风沙与柴油熏陶的低沉废土生存者之音"。声线必须具备强烈磨砂般的颗粒感，宛如喉咙中夹杂着干涸的沙粒，绝不使用干净、温润、播音腔式的完美音色。

### 冷酷荒凉语调（Desolate & Detached Tone）
旁白语调需呈现出麻木、疲惫、冰冷无情且去情感化的极简主义，像是一个在末日废土上见证了无数次毁灭的冷酷旁观者。每一个字都充满着对宿命的冰冷接受，拒绝煽情，用死寂的反差衬托公路狂飙的狂暴。

### 生理换气与叹息（Organic Breath & Heavy Sighs）
设计极度逼真的生理质感。字里行间必须包含重度吸气声、长叹息与喉音震颤，模仿因缺水、极度疲惫或戴着防尘面具而产生的干哑呼吸。让吸气与换气成为叙事节奏的一部分。

### 大留白缓节奏（Measured Pacing & Void Pauses）
旁白语速必须极慢，短句之间预留大片物理静默（2-3 秒气口留白）。这种声学上的"空白"能赋予字句如墓碑般沉重的力量，并为重工业 BGM 与引擎嘶吼预留绝佳的冲突让位空间。

### 配音参数与声学处理细化

**极度沧桑与磨砂感（Gravelly Texture）**：音色描述词中必须包含并强调 gravelly male voice, sand-worn raspy timber, dry gravelly throat, weary desert survivor, seasoned and hardened，消除任何圆润或温暖干净的声线特质。

**生理换气与叹息**：
- 在旁白文本过渡处插入换气标签（如 [heavy weary sigh] 或 [inhales deeply]），引导生成逼真的疲倦喘息、叹息及沙哑的吸气重音。

**声学后处理参数**：
- **高通滤波除噪**：对旁白音轨施加 80Hz 高通滤波器，消除低频低噪与录音室房颤驻波。
- **中高频齿音与呼吸增益**：在 2.5kHz - 3.5kHz 频段进行 +3dB 均衡提升，极大强化唇齿音、喉部沙哑擦音以及生理喘息的微观细节，塑造贴耳的荒凉压迫感。
- **中频去暖处理**：在 300Hz - 500Hz 频段进行 -2dB 缓降衰减，消除人声中温暖、饱满的"温室共鸣"，使其听觉上显得干瘪、冰冷、脱水且饱受风沙侵蚀。
- **高比例动态压限**：设定压缩比 4:1，启动时间 10ms，释放时间 50ms，配合化妆增益将微弱的吸气声、声带微颤和干哑叹息拉升至与台词主体相同的响度水平。

**冷酷荒凉语调执行参数**：设定为极低语速（slow delivery），语调采取去情感化的极简主义（cold, detached, monotone desolation, lifeless acceptance of fate）。

## 2. 背景音乐生成规范

生成工业重金属与硬核拟音音乐（Industrial Concrete Foley & Heavy Metal Music）。

### 声部频段织体规划

提示词中必须高密度堆叠工业噪音、拟音和暴力金属打击乐描述，严禁生成平庸、温和的常规摇滚。BGM 必须在声部织体与物理频段上执行严格的分层规划：

**低频重音底座（Sub-Bass & Heavy Drums, 30Hz - 100Hz）**：高密度堆叠低频重鼓与部落战鼓重拍。关键词：apocalyptic tribal war drums, colossal thudding floor toms, massive sub-bass drone。

**中低频重装撕裂（Low-Mid Grid & Distorted Riffs, 100Hz - 400Hz）**：使用重度失真的下调弦 8 弦吉他或重载合成器锯齿波。关键词：heavy-distorted down-tuned 8-string guitar riffs, aggressive crushing low-end chugs, buzzing hyper-saturated fuzz bass。

**中高频金属撞击（Mid-High Foley & Percussion, 1kHz - 4kHz）**：高频堆叠粗砺的物理拟音打击乐。关键词：deafening iron anvil beats, clashing rusted sheets of scrap metal, high-pitch iron pipe bashing。

**极高频气流噪声（High-End Air Sibilance, 6kHz - 12kHz）**：融入高压喷火、排气或泄压的高频嘶鸣声。关键词：screeching scrap power drills, high-pressure pneumatic air valve hiss, incandescent metallic spark sizzling。

### 英/中文核心词库

**重型金属打击**：heavy iron oil drum clangs（铁筒重击声）, metallic rust pipe bashing（锈铁管撞击）, clashing sheets of scrap metal（废旧铁皮摩擦碰撞）, anvil sledgehammer strikes（铁砧重锤砸击）, deafening industrial anvil beats（震耳的工业铁砧节奏）。

**机械运行拟音**：screeching scrap power drills（废旧电钻尖锐嘶鸣）, high-pressure heavy pneumatic air pumps hissing and thumping（高压重型气泵排气与抽击律动）, rhythmic mechanical grinding gears（机械齿轮磨损律动）, hydraulic piston rhythmic stamps（液压活塞节奏性盖印撞击）。

**摇滚风格与速度**：industrial metallic rock, aggressive wasteland drums, roaring distorted electric guitar riffs, pounding tribal war beats, extreme high-speed chase tempo, 140 BPM, apocalyptic cinematic soundtrack。

### 混响与空间感建模参数

提示词与混音方案中必须强制混合两种截然相反的空间质感：

- **干枯拟音层**：发动机运转、钻头和漏气的拟音必须锁定在极低混响（reverb mix 0%-10%）的干枯空间内，使其产生逼真、贴脸的尖锐感与细节粗糙度。
- **宏大打击乐层**：重金属铁锤敲击、重音鼓点和电吉他 Riff 必须注入大混响（reverb mix 45%-60%，衰减时间 decay time 2.5s-3.5s，预延迟 pre-delay 30ms-50ms）的庞大空间，模拟废土巨型工字钢起重机、集装箱群落与旷野据点反射出的带有金属颤音回响的废土史诗声场。

### 推荐经典模板

```
industrial metallic rock, apocalyptic cinematic soundtrack, heavy iron oil drum clangs, screeching scrap power drills, high-pressure pneumatic air pumps hissing, rhythmic mechanical grinding gears, roaring distorted electric guitar riffs, aggressive wasteland tribal war drums, 140 BPM, high-speed chase tempo, vast concrete warehouse reverb mixed with bone-dry mechanical grit, heavy-distorted down-tuned 8-string guitar chugs, high-contrast dynamic drops, wide industrial soundstage
```

### 合规安全红线
严禁在提示词中出现任何真实歌手、乐队或音乐家的名字，仅以流派名词、打击拟音和乐器特征进行风格描述。

## 3. 公路对撞物理声学资产规范

### 车辆刮擦（Vehicle Scraping）声学特征
侧重中高频摩擦细节与金属延展撕裂感。声学描述必须堆叠：piercing high-frequency metallic screech, razor-sharp iron friction, high-pitch raw steel grinding，强制产生在 1kHz - 4kHz 频段极具能量的尖锐摩擦声，为刮擦的生理牙酸感提供核心渲染源。

### 底盘撕裂（Chassis Tearing）声学特征
侧重低频轰鸣、结构折断与重工业骨架扭曲。声学描述必须堆叠：bone-shaking chassis-tearing roar, massive low-end metal ripping, heavy chassis fracturing and low-frequency steel crunching，确保提供 150Hz 以下极具压迫感和重量感的重低音撕裂信号。

### 爆炸冲击波（Explosion Shockwave）声学特征
追求多相变高压瞬间爆发、低频真空陷落与气流扫频。声学描述必须堆叠：deafening shockwave blast, multi-phase heavy explosion roar with sweeping air-shear, high-pressure stereo shockwave panning, low-frequency atmospheric vacuum，形成极宽频带与高动态范围的爆炸音频，为后期的全频降避与声学耳鸣留足空间。
