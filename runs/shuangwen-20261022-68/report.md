# 账本撕页 生成报告

slug：`shuangwen-20261022-68`
档位：爽文　闸门模式：observe
章数：10　总字数：19210
LLM 调用：97 次，累计 441.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胸牌摩挲 | 1930 | normal | 39.7 | 0 |  | 2 |
| 2 | 账本核对 | 1833 | normal | 38.0 | 0 |  | 2 |
| 3 | 印章压纸 | 1545 | normal | 95.7 | 0 |  | 2 |
| 4 | 胸牌敲桌 | 1852 | normal | 93.2 | 0 |  | 1 |
| 5 | 名册摩挲 | 1971 | normal | 88.8 | 0 |  | 2 |
| 6 | 合同圈数 | 1786 | normal | 94.7 | 0 |  | 1 |
| 7 | 折痕藏真相 | 1812 | normal | 91.7 | 0 |  | 4 |
| 8 | 撕纸对胸牌 | 2091 | normal | 37.2 | 0 |  | 2 |
| 9 | 墨迹压合同 | 2121 | normal | 93.8 | 0 |  | 2 |
| 10 | 纸角掀胸牌 | 2259 | long | 92.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×4
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 2.7 低于目标 5.0
  - [observe] attr_adv_pct 35.7 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 2.9 低于目标 5.0
- 第 4 章：
  - 单条套路句式超限：「李国强的」×8
- 第 5 章：
  - 单条套路句式超限：「李国强的」×3
  - dialogue_run_mean 35 高于目标 14.0
- 第 6 章：
  - narration_para_pct 2.2 低于目标 5.0
- 第 7 章：
  - 单条套路句式超限：「李国强的」×5
  - narration_para_pct 3.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
- 第 8 章：
  - 单条套路句式超限：「李国强的」×8
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「李国强的」×7
  - attr_adv_pct 12.5 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「李国强的」×7
  - narration_para_pct 2.4 低于目标 5.0
  - [observe] 标题与《撕纸对胸牌》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18298
chapter_chars_mean: 1830
chapter_chars_median: 1804
chapter_chars_cv: 0.11
paragraphs_mean: 38.9
dialogue_chars_pct: 49.2
dialogue_para_pct: 86.9
interiority_para_pct: 5.7
narration_para_pct: 7.3
turn_under20_pct: 70.5
turn_over200_pct: 0.0
attr_say_pct: 32.0
attr_adv_pct: 19.3
scenes_per_chapter: 1.5
dialogue_run_mean: 11.0
turn_len_median: 14
```
