# 铜珠 生成报告

slug：`xuanyi-20261019-164`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14870
LLM 调用：68 次，累计 233.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的凹凸痕迹 | 1668 | short | 99.6 | 0 |  | 1 |
| 2 | 摩挲铜珠的手指 | 3602 | normal | 89.7 | 0 |  | 1 |
| 3 | 钥匙转动的瞬间 | 4245 | normal | 81.5 | 0 |  | 4 |
| 4 | 摩挲柜门的手指 | 3283 | normal | 88.5 | 0 |  | 4 |
| 5 | 摩挲面粉的手指 | 2067 | short | 91.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈志强的」×4、「赵美兰的」×3
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4、「心中充满了疑」×3、「深吸一口气」×3
  - dialogue_chars_pct 17.2 低于目标 20.0
  - interiority_para_pct 21.1 高于目标 20.0
  - [observe] 章内自我复读 16 句（如「他开始思考，每一个人都有自己的秘密，而他要做的，…」）
- 第 4 章：
  - 单条套路句式超限：「赵美兰的」×9、「点了点头」×4、「为什么会」×4
  - narration_para_pct 10.6 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
  - [observe] 标题与《摩挲铜珠的手指》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 7.4 低于目标 20.0
  - [observe] 标题与《摩挲柜门的手指》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14171
chapter_chars_mean: 2834
chapter_chars_median: 3136
chapter_chars_cv: 0.37
paragraphs_mean: 61.8
dialogue_chars_pct: 30.4
dialogue_para_pct: 69.7
interiority_para_pct: 12.4
narration_para_pct: 17.9
turn_under20_pct: 81.5
turn_over200_pct: 0.0
attr_say_pct: 40.2
attr_adv_pct: 5.8
scenes_per_chapter: 3.6
dialogue_run_mean: 5.0
turn_len_median: 13
```
