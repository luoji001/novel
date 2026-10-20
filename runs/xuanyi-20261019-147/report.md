# 砚台 生成报告

slug：`xuanyi-20261019-147`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14195
LLM 调用：68 次，累计 231.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台轻如羽 | 1694 | short | 92.4 | 0 |  | 2 |
| 2 | 触纸生凉 | 3756 | normal | 90.5 | 0 |  | 3 |
| 3 | 铜印照光 | 3537 | normal | 86.3 | 0 |  | 3 |
| 4 | 木尺对砚 | 3542 | normal | 88.8 | 0 |  | 3 |
| 5 | 拂数寻砚 | 1661 | short | 91.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 12.5 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「老周缓缓将砚台托起，转向光线，“像这样细腻入微的…」）
- 第 2 章：
  - 单条套路句式超限：「沈墨生的」×13
  - narration_para_pct 4.2 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「那你有没有想过，那个地方到底是什么地方？…」）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3
  - narration_para_pct 1.6 低于目标 20.0
  - dialogue_run_mean 20.3 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「陆怀远的」×10
  - narration_para_pct 14.9 低于目标 20.0
  - attr_adv_pct 19.0 高于目标 10.0
- 第 5 章：
  - narration_para_pct 8.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13513
chapter_chars_mean: 2703
chapter_chars_median: 3356
chapter_chars_cv: 0.38
paragraphs_mean: 59.8
dialogue_chars_pct: 46.4
dialogue_para_pct: 85.2
interiority_para_pct: 7.2
narration_para_pct: 7.6
turn_under20_pct: 66.4
turn_over200_pct: 0.0
attr_say_pct: 22.8
attr_adv_pct: 10.3
scenes_per_chapter: 2.4
dialogue_run_mean: 8.5
turn_len_median: 14
```
