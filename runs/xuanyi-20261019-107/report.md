# 端砚 生成报告

slug：`xuanyi-20261019-107`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13586
LLM 调用：68 次，累计 232.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲砚台纹路 | 1679 | short | 98.7 | 0 |  | 1 |
| 2 | 摩挲伤疤思索 | 3446 | normal | 86.4 | 0 |  | 3 |
| 3 | 摩挲旧收据纹路 | 3375 | normal | 91.2 | 0 |  | 2 |
| 4 | 摩挲铜牌铭文 | 3411 | normal | 94.2 | 0 |  | 4 |
| 5 | 摩挲书页残标 | 1670 | short | 93.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 7.5 低于目标 20.0
- 第 2 章：
  - interiority_para_pct 20.4 高于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
  - [observe] 章内自我复读 23 句（如「雨声渐渐变小，天色渐暗，他依旧坐在那里，手中的《…」）
- 第 3 章：
  - 单条套路句式超限：「沈砚生的」×5
  - [observe] 标题与《摩挲砚台纹路》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周怀远的」×4、「”周怀远轻」×3、「微微一笑」×3
  - narration_para_pct 5.2 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 12980
chapter_chars_mean: 2596
chapter_chars_median: 3232
chapter_chars_cv: 0.35
paragraphs_mean: 53
dialogue_chars_pct: 34.0
dialogue_para_pct: 70.2
interiority_para_pct: 13.2
narration_para_pct: 16.7
turn_under20_pct: 69.6
turn_over200_pct: 0.0
attr_say_pct: 25.0
attr_adv_pct: 10.3
scenes_per_chapter: 1.8
dialogue_run_mean: 4.4
turn_len_median: 13
```
