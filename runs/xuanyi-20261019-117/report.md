# 红单 生成报告

slug：`xuanyi-20261019-117`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13840
LLM 调用：68 次，累计 223.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 面单覆盖的瞬间 | 1845 | short | 100.0 | 0 |  | 2 |
| 2 | 蓝色标签的疑云 | 3178 | normal | 93.8 | 0 |  | 4 |
| 3 | 文件夹边缘的折痕 | 3581 | normal | 89.1 | 0 |  | 2 |
| 4 | 面单被覆盖的瞬间 | 3354 | normal | 90.6 | 0 |  | 4 |
| 5 | 摩挲面单的指尖 | 1877 | short | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×6
  - narration_para_pct 11.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×4、「为什么会」×4
  - narration_para_pct 9.1 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「如果这是一个系统故障，为什么会偏偏是这个编号？…」）
- 第 3 章：
  - 单条套路句式超限：「周晓芸的」×6、「”周晓芸轻」×3、「说道“我」×3
  - narration_para_pct 11.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×4、「“我不知道」×3
  - narration_para_pct 19.5 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
  - [observe] 标题与《面单覆盖的瞬间》近似 0.93 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 12.1 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13164
chapter_chars_mean: 2633
chapter_chars_median: 3031
chapter_chars_cv: 0.3
paragraphs_mean: 57.6
dialogue_chars_pct: 40.3
dialogue_para_pct: 78.8
interiority_para_pct: 8.2
narration_para_pct: 13.0
turn_under20_pct: 75.0
turn_over200_pct: 0.0
attr_say_pct: 27.3
attr_adv_pct: 11.4
scenes_per_chapter: 1.2
dialogue_run_mean: 5.7
turn_len_median: 15
```
