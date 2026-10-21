# 画室清晨 生成报告

slug：`xiaoyuan-20261020-49`
档位：校园青春　闸门模式：observe
章数：9　总字数：19532
LLM 调用：100 次，累计 423.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎课表 | 1421 | short | 90.2 | 0 |  | 2 |
| 2 | 磁带刻痕 | 2456 | normal | 92.9 | 0 |  | 3 |
| 3 | 画笔悬空 | 2313 | normal | 52.5 | 0 |  | 2 |
| 4 | 画框边缘摩挲 | 2221 | normal | 93.2 | 0 |  | 2 |
| 5 | 磁带边缘摩挲 | 2278 | normal | 85.0 | 0 |  | 4 |
| 6 | 画笔悬空 | 2393 | normal | 89.6 | 0 |  | 2 |
| 7 | 保温杯边缘摩挲 | 2526 | normal | 90.6 | 0 |  | 2 |
| 8 | 画框边缘摩挲 | 2288 | normal | 84.9 | 0 |  | 4 |
| 9 | 校服袖口颜料痕 | 1627 | short | 90.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林晚晴的」×3
  - [observe] 章内自我复读 15 句（如「她蹲下身，捡起其中一片，手指触碰到纸面的褶皱，像…」）
- 第 2 章：
  - 单条套路句式超限：「沈子墨的」×5、「沈子墨点」×3、「林晚晴的」×3
  - interiority_para_pct 5.1 低于目标 8.0
  - narration_para_pct 10.2 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「林晚晴的」×4
  - dialogue_chars_pct 14.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林晚晴站在」×4
  - narration_para_pct 7.7 低于目标 15.0
- 第 5 章：
  - 单条套路句式超限：「沈子墨的」×3、「他知道这」×3
  - interiority_para_pct 4.0 低于目标 8.0
  - [observe] 章内自我复读 16 句（如「周老师看着她，眼中闪过一丝惊讶，随即又恢复平静，…」）
  - [observe] 标题与《画框边缘摩挲》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「林晚晴站在」×4
  - [observe] 标题重复：「画笔悬空」已存在
- 第 7 章：
  - 单条套路句式超限：「沈子墨的」×5、「他知道自己」×3
  - [observe] 标题与《画框边缘摩挲》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「林晚晴点了点头」×3
  - dialogue_chars_pct 18.2 低于目标 20.0
  - [observe] 章内自我复读 13 句（如「林晚晴的手指无意识地摩挲着画框边缘，那里有轻微的…」）
  - [observe] 标题重复：「画框边缘摩挲」已存在
- 第 9 章：
  - dialogue_chars_pct 18.7 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 18585
chapter_chars_mean: 2065
chapter_chars_median: 2188
chapter_chars_cv: 0.18
paragraphs_mean: 44.6
dialogue_chars_pct: 23.5
dialogue_para_pct: 65.8
interiority_para_pct: 15.7
narration_para_pct: 18.5
turn_under20_pct: 89.8
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 3.0
scenes_per_chapter: 2.9
dialogue_run_mean: 3.9
turn_len_median: 9
```
