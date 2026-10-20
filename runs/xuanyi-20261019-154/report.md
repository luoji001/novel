# 蓝布的去向 生成报告

slug：`xuanyi-20261019-154`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14265
LLM 调用：68 次，累计 220.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲铁皮盒边缘 | 1748 | short | 95.5 | 0 |  | 0 |
| 2 | 算盘上的暗码 | 3742 | normal | 91.2 | 0 |  | 1 |
| 3 | 摩挲纸片边缘 | 3542 | normal | 91.8 | 0 |  | 4 |
| 4 | 摩挲蓝布边缘 | 3612 | normal | 0.0 | 0 |  | 5 |
| 5 | 摩挲登记簿边缘 | 1616 | short | 92.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈国栋的」×6、「周素云点」×5、「周素云的」×5
  - narration_para_pct 7.3 低于目标 20.0
  - [observe] 标题与《摩挲铁皮盒边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「点了点头」×3
  - interiority_para_pct 26.9 高于目标 20.0
  - [observe] 章内自我复读 18 句（如「就在这个时候，他不经意间瞥见了一个模糊的身影一闪…」）
  - [observe] dialogue_chars_pct 5.8 < 6.0（结构塌缩）
  - [observe] 标题与《摩挲纸片边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 标题与《摩挲蓝布边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13654
chapter_chars_mean: 2731
chapter_chars_median: 3364
chapter_chars_cv: 0.38
paragraphs_mean: 53.4
dialogue_chars_pct: 28.4
dialogue_para_pct: 60.3
interiority_para_pct: 15.1
narration_para_pct: 24.6
turn_under20_pct: 82.1
turn_over200_pct: 0.0
attr_say_pct: 17.9
attr_adv_pct: 3.1
scenes_per_chapter: 4
dialogue_run_mean: 3.8
turn_len_median: 12
```
