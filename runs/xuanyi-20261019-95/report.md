# 表停时 生成报告

slug：`xuanyi-20261019-95`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14307
LLM 调用：68 次，累计 222.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 停滞的机械表 | 1708 | short | 69.5 | 0 |  | 3 |
| 2 | 机械表秒针异常 | 4144 | normal | 90.2 | 0 |  | 2 |
| 3 | 机械表秒针重启 | 3579 | normal | 89.1 | 0 |  | 3 |
| 4 | 转动表壳的秘密 | 3235 | normal | 93.0 | 0 |  | 2 |
| 5 | 止痛药与灰色外套 | 1636 | short | 80.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 9.1 低于目标 20.0
  - interiority_para_pct 24.1 高于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「他知道这」×6、「市立医院」×4
  - [observe] 章内自我复读 12 句（如「他知道，这个信息绝对不是巧合，而是有人故意告诉他…」）
- 第 3 章：
  - 单条套路句式超限：「林婉如的」×6、「他知道这」×3、「为什么会」×3
  - attr_adv_pct 15.8 高于目标 10.0
  - [observe] 标题与《机械表秒针异常》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×4、「陈志远的」×3、「为什么会」×3
  - narration_para_pct 14.1 低于目标 20.0
- 第 5 章：
  - dialogue_chars_pct 14.9 低于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5

## 整书结构指标

```
chapters: 5
total_chars: 13610
chapter_chars_mean: 2722
chapter_chars_median: 3064
chapter_chars_cv: 0.39
paragraphs_mean: 60
dialogue_chars_pct: 31.5
dialogue_para_pct: 64.4
interiority_para_pct: 11.0
narration_para_pct: 24.5
turn_under20_pct: 80.3
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 4.8
scenes_per_chapter: 3.2
dialogue_run_mean: 3.3
turn_len_median: 11
```
