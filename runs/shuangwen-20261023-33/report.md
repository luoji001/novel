# 铜钥匙 生成报告

slug：`shuangwen-20261023-33`
档位：爽文　闸门模式：observe
章数：10　总字数：18435
LLM 调用：97 次，累计 420.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本对峙 | 2020 | normal | 99.9 | 0 |  | 1 |
| 2 | 纸灰重燃 | 1760 | normal | 36.6 | 0 |  | 2 |
| 3 | 抽屉开启 | 1953 | normal | 91.7 | 0 |  | 1 |
| 4 | 铜钥交握 | 1785 | normal | 92.4 | 0 |  | 1 |
| 5 | 墨迹显现 | 1790 | normal | 91.6 | 0 |  | 2 |
| 6 | 纸条现身 | 1495 | normal | 91.8 | 0 |  | 2 |
| 7 | 账本递交 | 1878 | normal | 91.6 | 0 |  | 1 |
| 8 | 账本翻页 | 1694 | normal | 93.4 | 0 |  | 1 |
| 9 | 账本藏柜 | 1750 | normal | 37.8 | 0 |  | 2 |
| 10 | 签字轻点 | 2300 | long | 94.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀安的」×6、「他知道自己」×3
- 第 2 章：
  - 单条套路句式超限：「李怀安的」×7
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 3 章：
  - 命中套话收尾句
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀安的」×9
- 第 6 章：
  - 单条套路句式超限：「李怀安的」×4
  - attr_adv_pct 14.3 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「李怀安的」×6、「他知道这」×3
- 第 8 章：
  - 单条套路句式超限：「李怀安的」×6
- 第 9 章：
  - 单条套路句式超限：「李怀安的」×3
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 10 章：
  - 单条套路句式超限：「李怀安的」×7

## 整书结构指标

```
chapters: 10
total_chars: 17503
chapter_chars_mean: 1750
chapter_chars_median: 1696
chapter_chars_cv: 0.12
paragraphs_mean: 39.1
dialogue_chars_pct: 44.0
dialogue_para_pct: 81.4
interiority_para_pct: 6.6
narration_para_pct: 12.0
turn_under20_pct: 74.5
turn_over200_pct: 0.0
attr_say_pct: 25.8
attr_adv_pct: 13.2
scenes_per_chapter: 2.5
dialogue_run_mean: 5.7
turn_len_median: 12
```
