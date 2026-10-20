# 错位钥匙 生成报告

slug：`xuanyi-20261019-26`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14105
LLM 调用：68 次，累计 219.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻动日志的指尖 | 1591 | short | 99.2 | 0 |  | 0 |
| 2 | 钥匙牌的错位 | 3778 | normal | 91.0 | 0 |  | 3 |
| 3 | 翻动单据的指尖 | 3696 | normal | 88.7 | 0 |  | 4 |
| 4 | 墨水染透纸页 | 3283 | normal | 11.7 | 0 |  | 4 |
| 5 | 锈蚀螺丝藏玄机 | 1752 | short | 50.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陆婉秋的」×4、「他知道这」×3
  - narration_para_pct 15.6 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「他说，语气坚定了一些…」）
- 第 3 章：
  - 单条套路句式超限：「陆婉秋的」×10、「点了点头」×4、「他知道这」×4
  - narration_para_pct 19.3 低于目标 20.0
  - attr_adv_pct 19.2 高于目标 10.0
  - [observe] 标题与《翻动日志的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 9.2 低于目标 20.0
  - interiority_para_pct 30.6 高于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 15 句（如「这些钥匙牌似乎每天都会被人重新摆放一次，但奇怪的…」）
- 第 5 章：
  - dialogue_chars_pct 5.0 低于目标 20.0
  - interiority_para_pct 33.3 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5

## 整书结构指标

```
chapters: 5
total_chars: 13531
chapter_chars_mean: 2706
chapter_chars_median: 3171
chapter_chars_cv: 0.38
paragraphs_mean: 49.6
dialogue_chars_pct: 21.2
dialogue_para_pct: 54.7
interiority_para_pct: 18.9
narration_para_pct: 26.3
turn_under20_pct: 84.4
turn_over200_pct: 0.0
attr_say_pct: 29.2
attr_adv_pct: 7.1
scenes_per_chapter: 2.8
dialogue_run_mean: 2.4
turn_len_median: 10
```
