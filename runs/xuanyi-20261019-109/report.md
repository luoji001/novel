# 钢笔的痕迹 生成报告

slug：`xuanyi-20261019-109`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13422
LLM 调用：68 次，累计 224.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸纸页边缘 | 1648 | short | 97.6 | 0 |  | 3 |
| 2 | 钢笔对签名的质疑 | 3436 | normal | 92.5 | 0 |  | 3 |
| 3 | 数着药盒的缺口 | 3190 | normal | 84.5 | 0 |  | 2 |
| 4 | 抚摸印章的裂痕 | 3602 | normal | 90.5 | 0 |  | 2 |
| 5 | 签名与账本的错位 | 1541 | short | 86.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林素云的」×3
  - narration_para_pct 12.1 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陈启明的」×4
  - narration_para_pct 4.9 低于目标 20.0
  - [observe] attr_adv_pct 26.7 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 13 句（如「如果他知道这份签名背后还有更深的秘密，也许他会像…」）
- 第 4 章：
  - 单条套路句式超限：「不仅仅是」×3
  - narration_para_pct 5.8 低于目标 20.0
- 第 5 章：
  - [observe] 章内自我复读 16 句（如「她想起陈启明前几天说过的话：“那些记录都是过去的…」）

## 整书结构指标

```
chapters: 5
total_chars: 12821
chapter_chars_mean: 2564
chapter_chars_median: 3063
chapter_chars_cv: 0.38
paragraphs_mean: 51.8
dialogue_chars_pct: 35.7
dialogue_para_pct: 74.3
interiority_para_pct: 12.9
narration_para_pct: 12.8
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 7.6
attr_adv_pct: 10.0
scenes_per_chapter: 2.6
dialogue_run_mean: 5.4
turn_len_median: 12
```
