# 音频提示词模板

> 可适配的模式与句式，按场景改写，不要逐字照搬。

## 目录

1. 背景音乐（BGM）提示词编写
2. 主题曲与声乐歌词路径
3. 跨镜头旁白（Narration）路径
4. 三大分支 BGM 提示词

---

## 1. 背景音乐（BGM）提示词编写

围绕乐器、节奏、流派、情绪氛围组合，采用中英文描述，严格避免出现人名。

### 新派古典武侠
Epic cinematic Chinese martial arts soundtrack, frantic and high-tempo, traditional Guzheng, intense Pipa solo, high-pitched Shakuhachi, heavy Chinese war drums, dramatic percussion, surging and heroic male vocal chants, dynamic, cinematic sweep.

### 聊斋玄幻鬼片
Eerie ambient Chinese fantasy horror music, slow and haunting, low Xun, ethereal bamboo flute, spectral Guqin, lingering synthesizer drones, haunting reverb, irregular woodblock knocks, chilling female vocal humming, spooky and mystic.

### 近代功夫
High-spirited energetic Southern kung fu soundtrack, rapid tempo, loud Suona, high-pitched Banhu, traditional lion dance drums and gongs, intense brass, martial arts orchestration, powerful shouts, heroic and patriotic tone.

---

## 2. 主题曲与声乐歌词路径（若需带歌词的歌曲）

将大气的武侠歌词（如"沧海一声笑"流派）合成为完整的男女声演唱音轨。

### 歌词要求
使用古典绝句、新武侠乐府诗或豪放派词风，结构包含 [Verse] 和 [Chorus]。

### 风格提示
Wuxia theme song, traditional Chinese instrumental, classical vocals, male and female duet, epic martial arts ballad, dramatic string section, heroic and emotional.

---

## 3. 跨镜头旁白（Narration）路径

生成旁白音色需精准对应故事板中的 narration_speaker_profile 描绘。

- 中文及多语言高表现力 narration 优先使用高表现力语音合成。
- 若有特定英文电影感音色，可选用对应风格音色。

### narration_speaker_profile 示例
- [沧桑沙哑男声]：低沉、沙哑、饱经风霜，语速缓慢但有力
- [清冷孤傲侠女声]：清亮、冷冽、略带疏离，语调平稳而克制

### 旁白与对白分离规则
- 镜头对白（dialogue）：由视频模型在多模态视频中同步渲染出声，音色由 key_element_audio 克隆。
- 跨镜头旁白（narration）：在独立音频轨道中批量合成。
- 两者生成路径与绑定位置严格区分，防止声音源相互污染。
