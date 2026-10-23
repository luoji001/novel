# 名册撕毁 生成报告

slug：`shuangwen-20261022-140`
档位：爽文　闸门模式：observe
章数：10　总字数：19811
LLM 调用：97 次，累计 463.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 供奉名册滑落 | 1892 | normal | 40.0 | 0 |  | 2 |
| 2 | 铜钱落案 | 1941 | normal | 94.1 | 0 |  | 2 |
| 3 | 印章摩挲 | 1832 | normal | 94.0 | 0 |  | 0 |
| 4 | 墨笔断纸 | 2454 | normal | 92.9 | 0 |  | 2 |
| 5 | 铜钱滚落 | 1680 | normal | 94.0 | 0 |  | 4 |
| 6 | 铜钱摩挲 | 2079 | normal | 87.9 | 0 |  | 4 |
| 7 | 铜钱滚落 | 1809 | normal | 93.6 | 0 |  | 2 |
| 8 | 账本掀开 | 1697 | normal | 93.8 | 0 |  | 1 |
| 9 | 墨笔划痕 | 1957 | normal | 93.2 | 0 |  | 0 |
| 10 | 账本掀开 | 2460 | long | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀安的」×6、「沈知远的」×3
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李怀安的」×7
  - attr_adv_pct 14.8 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李怀安的」×5、「为什么会」×3
  - attr_adv_pct 21.7 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「沈知远的」×3
  - narration_para_pct 3.3 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题与《铜钱落案》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「李怀安的」×6
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
  - dialogue_run_mean 38 高于目标 14.0
- 第 7 章：
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「铜钱滚落」已存在
- 第 8 章：
  - 单条套路句式超限：「李怀安的」×7
- 第 10 章：
  - 单条套路句式超限：「李怀安的」×6
  - [observe] 标题重复：「账本掀开」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18815
chapter_chars_mean: 1882
chapter_chars_median: 1812
chapter_chars_cv: 0.14
paragraphs_mean: 43.2
dialogue_chars_pct: 47.4
dialogue_para_pct: 84.6
interiority_para_pct: 5.7
narration_para_pct: 9.8
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 32.0
attr_adv_pct: 15.3
scenes_per_chapter: 1.4
dialogue_run_mean: 9.6
turn_len_median: 12
```
