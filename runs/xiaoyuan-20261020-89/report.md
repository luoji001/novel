# 未完成的画作 生成报告

slug：`xiaoyuan-20261020-89`
档位：校园青春　闸门模式：observe
章数：9　总字数：20526
LLM 调用：100 次，累计 436.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 凝结的指纹 | 1515 | short | 92.9 | 0 |  | 1 |
| 2 | 未干的颜料 | 2567 | normal | 85.4 | 0 |  | 3 |
| 3 | 藏在口袋里的磁带 | 2588 | normal | 93.8 | 0 |  | 1 |
| 4 | 摩挲磁带边缘 | 2386 | normal | 92.4 | 0 |  | 3 |
| 5 | 摩挲磁带边缘 | 2515 | normal | 86.9 | 0 |  | 3 |
| 6 | 摩挲铅笔盒边缘 | 2547 | normal | 92.4 | 0 |  | 3 |
| 7 | 摩挲照片边缘 | 2555 | normal | 91.1 | 0 |  | 1 |
| 8 | 摩挲画布边缘 | 2282 | normal | 89.0 | 0 |  | 3 |
| 9 | 摩挲画框边缘 | 1562 | short | 87.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 16.7 低于目标 20.0
- 第 2 章：
  - dialogue_chars_pct 16.2 低于目标 20.0
  - narration_para_pct 9.8 低于目标 15.0
  - [observe] 章内自我复读 10 句（如「她的视线不由自主地回到画架上，那里还有几片未干的…」）
- 第 3 章：
  - narration_para_pct 7.7 低于目标 15.0
- 第 4 章：
  - 单条套路句式超限：「”周雨桐低」×3
  - narration_para_pct 11.3 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 5 章：
  - dialogue_chars_pct 19.9 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「你知道吗，在这个地方待久了，有时候会觉得特别孤独…」）
  - [observe] 标题重复：「摩挲磁带边缘」已存在
- 第 6 章：
  - 单条套路句式超限：「”周雨桐低」×3、「周雨桐点」×3、「周雨桐的」×3
  - narration_para_pct 8.8 低于目标 15.0
  - [observe] 标题与《摩挲磁带边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - [observe] 标题与《摩挲磁带边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - narration_para_pct 11.7 低于目标 15.0
  - [observe] 章内自我复读 13 句（如「她看着公告栏上的名单，上面密密麻麻地列着各种专业…」）
  - [observe] 标题与《摩挲照片边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「林夏点点」×3
  - interiority_para_pct 7.8 低于目标 8.0
  - [observe] 章内自我复读 20 句（如「林夏低头看了看自己的作品，叹了口气：“是啊，我一…」）
  - [observe] 标题与《摩挲画布边缘》近似 0.83 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 19513
chapter_chars_mean: 2168
chapter_chars_median: 2411
chapter_chars_cv: 0.19
paragraphs_mean: 48.8
dialogue_chars_pct: 25.5
dialogue_para_pct: 66.7
interiority_para_pct: 20.3
narration_para_pct: 13.0
turn_under20_pct: 87.4
turn_over200_pct: 0.0
attr_say_pct: 34.0
attr_adv_pct: 5.2
scenes_per_chapter: 2.2
dialogue_run_mean: 3.1
turn_len_median: 10
```
