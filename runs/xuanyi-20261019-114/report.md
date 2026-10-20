# 蓝布 生成报告

slug：`xuanyi-20261019-114`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14629
LLM 调用：68 次，累计 237.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 算盘拨动的瞬间 | 1808 | short | 94.9 | 0 |  | 1 |
| 2 | 铜尺丈量的秘密 | 4001 | normal | 89.1 | 0 |  | 3 |
| 3 | 木牌与账簿对照 | 3623 | normal | 91.9 | 0 |  | 3 |
| 4 | 布料被移走的夜晚 | 3367 | normal | 92.5 | 0 |  | 3 |
| 5 | 布料消失的账页 | 1825 | short | 91.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 16.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈德昌的」×4、「陈德昌点了点头」×3
  - narration_para_pct 16.2 低于目标 20.0
  - [observe] 章内自我复读 23 句（如「他回头看向周玉兰，语气低沉：“你知道这件布料是从…」）
- 第 3 章：
  - 单条套路句式超限：「为什么会」×3、「老城区仓库」×3
  - narration_para_pct 13.4 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「老城区仓库」×3
  - narration_para_pct 15.2 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「这确实是蓝色棉布没错…」）
- 第 5 章：
  - narration_para_pct 9.5 低于目标 20.0
  - [observe] attr_adv_pct 23.5 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13932
chapter_chars_mean: 2786
chapter_chars_median: 3193
chapter_chars_cv: 0.35
paragraphs_mean: 61.6
dialogue_chars_pct: 43.1
dialogue_para_pct: 79.6
interiority_para_pct: 6.0
narration_para_pct: 14.4
turn_under20_pct: 71.8
turn_over200_pct: 0.0
attr_say_pct: 33.8
attr_adv_pct: 12.6
scenes_per_chapter: 4.2
dialogue_run_mean: 5.5
turn_len_median: 13
```
