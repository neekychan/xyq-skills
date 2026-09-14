# 提示词模板规范

## 通用基础前缀（所有提示词必须包含）
```
Charlie Chaplin style,
silent film,
1920s vintage cinema,
black and white,
35mm film grain,
high contrast monochrome,
humanistic realism,
no color,
no CGI,
no 3D render,
no modern objects,
no digital devices
```

## 角色图提示词模板
```
[通用基础前缀]
full body shot of [角色描述，例如：a kind tramp in ill-fitting suit, bowler hat, small mustache, cane],
1920s working class costume,
standing in [简单背景描述，例如：1920s urban street],
soft side lighting,
classic silent film character portrait,
sharp focus on face and costume details,
2K resolution
```
*负面提示词统一添加：no close up, no cropped body, no modern clothing, no color*

## 场景图提示词模板
### 普通街景/室内场景
```
[通用基础前缀]
silent film establishing shot,
[场景描述，例如：1920s New York street, old brick buildings, cobblestone road, vintage street lamps],
realistic architecture,
period accurate details,
high contrast lighting,
deep depth of field,
2K resolution
```
### 情感场景
```
[通用基础前缀]
emotional silent film moment,
[场景描述，例如：empty park bench at sunset, soft light filtering through trees],
soft natural side lighting,
cinematic composition,
warm human atmosphere,
shallow depth of field,
2K resolution
```
### 喜剧场景
```
[通用基础前缀]
physical comedy scene,
[场景描述，例如：busy factory assembly line, machines and conveyor belts],
dynamic composition,
bright even lighting,
vaudeville comedy atmosphere,
2K resolution
```

## 视频提示词模板
```
[通用基础前缀]
silent film motion,
[镜头描述，例如：medium shot, the tramp slips on a banana peel and tries to regain his balance comically, physical comedy performance],
[运镜描述，例如：static camera, eye level angle],
authentic 1920s silent film acting style,
exaggerated body language,
cinematic movement,
smooth natural motion,
720p resolution,
5-10 seconds duration
```
*连续性提示：若为连续镜头，添加"consistent with previous shot, same character costume and setting"*

## 字幕卡提示词模板
```
silent film title card,
[文字内容，例如："THE END" 或 中文对应文字],
white vintage serif font centered on solid black background,
thin white border around the edge,
35mm film grain,
scratches and dust marks matching vintage film,
1920s cinema title design,
2K resolution
```
*负面提示词统一添加：no color, no images, no decorations, no modern fonts*

## 提示词编写规则
1. 所有提示词以英文编写，专有名词可保留中文（例如字幕卡文字）
2. 按"风格→主体→动作→环境→光影→技术参数"的顺序排列
3. 避免使用否定句堆砌，负面提示词统一放在末尾
4. 角色提示词必须明确服装特征，确保前后一致性
5. 视频提示词必须明确景别、角度、运镜方式，符合分镜设计要求
6. 所有提示词必须强调年代准确性，禁止出现任何1920年代以后的元素