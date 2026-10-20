# 分科表 生成报告

slug：`xiaoyuan-20261020-85`
档位：校园青春　闸门模式：observe
章数：9　总字数：19925
LLM 调用：100 次，累计 418.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 名字消失的瞬间 | 1041 | short | 34.9 | 0 |  | 3 |
| 2 | 系鞋带的姿势 | 2993 | normal | 94.2 | 0 |  | 2 |
| 3 | 粉笔划过黑板 | 2305 | normal | 92.1 | 0 |  | 0 |
| 4 | 触摸外套肩线 | 2613 | normal | 0.0 | 0 |  | 4 |
| 5 | 磁带边缘的指纹 | 2518 | normal | 85.4 | 0 |  | 2 |
| 6 | 触摸空白的位置 | 2220 | normal | 89.7 | 0 |  | 1 |
| 7 | 触摸空白的位置 | 2214 | normal | 20.8 | 0 |  | 5 |
| 8 | 空鞋带的重量 | 2620 | normal | 0.0 | 0 |  | 3 |
| 9 | 触碰旧信的褶皱 | 1392 | short | 52.8 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈知远的」×6、「林晓阳站在」×3
  - dialogue_chars_pct 14.8 低于目标 20.0
  - [observe] 章内自我复读 13 句（如「林晓阳停下脚步，望着公告栏上新贴出来的分科表，那…」）
- 第 2 章：
  - 单条套路句式超限：「沈知远的」×5、「林晓阳的」×5、「”沈知远低」×4
  - narration_para_pct 12.7 低于目标 15.0
- 第 4 章：
  - 单条套路句式超限：「沈知远的」×3
  - [observe] 章内自我复读 23 句（如「他低头看向储物柜缝隙里露出的一小部分外套肩线，那…」）
  - [observe] dialogue_chars_pct 6.8 < 8.0（结构塌缩）
  - [observe] attr_adv_pct 100.0 > 22.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林晓阳的」×5
  - dialogue_chars_pct 16.1 低于目标 20.0
- 第 6 章：
  - 单条套路句式超限：「林晓阳的」×3
- 第 7 章：
  - 单条套路句式超限：「沈知远的」×7、「林晓阳站在」×3、「林晓阳的」×3
  - dialogue_chars_pct 10.5 低于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 24 句（如「林晓阳的目光落在公告栏上，那里原本挂着他和沈知远…」）
  - [observe] 标题重复：「触摸空白的位置」已存在
- 第 8 章：
  - 单条套路句式超限：「他知道这」×6、「知道自己」×4、「声音在他」×3
  - [observe] 章内自我复读 27 句（如「他低头看着自己沾着粉笔灰的球鞋，鞋面上还有几点不…」）
  - [observe] dialogue_chars_pct 7.3 < 8.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「说道“我」×3
  - dialogue_chars_pct 18.4 低于目标 20.0
  - narration_para_pct 13.6 低于目标 15.0
  - [observe] 章内自我复读 17 句（如「他悄悄打开那份皱巴巴的信件，读到了最后一行字：“…」）
  - [observe] attr_adv_pct 60.0 > 22.0（结构塌缩）

## 整书结构指标

```
chapters: 9
total_chars: 19083
chapter_chars_mean: 2120
chapter_chars_median: 2207
chapter_chars_cv: 0.28
paragraphs_mean: 38.8
dialogue_chars_pct: 16.8
dialogue_para_pct: 48.3
interiority_para_pct: 22.6
narration_para_pct: 29.1
turn_under20_pct: 90.5
turn_over200_pct: 0.0
attr_say_pct: 43.7
attr_adv_pct: 18.9
scenes_per_chapter: 2.1
dialogue_run_mean: 2.3
turn_len_median: 10
```
