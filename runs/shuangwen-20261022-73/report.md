# 账本 生成报告

slug：`shuangwen-20261022-73`
档位：爽文　闸门模式：observe
章数：10　总字数：19289
LLM 调用：97 次，累计 437.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 墨迹与铜钱 | 1818 | normal | 40.0 | 0 |  | 2 |
| 2 | 账本上的铜钱印记 | 2174 | normal | 92.9 | 0 |  | 0 |
| 3 | 账本上的双签名 | 2203 | normal | 37.2 | 0 |  | 1 |
| 4 | 掌心抚过名册纹路 | 1746 | normal | 93.3 | 0 |  | 0 |
| 5 | 铜尺划破账页 | 1791 | normal | 90.8 | 0 |  | 2 |
| 6 | 账本末页的歪斜字迹 | 1704 | normal | 93.0 | 0 |  | 0 |
| 7 | 账本上的铜钱印记 | 1610 | normal | 93.8 | 0 |  | 3 |
| 8 | 账本摊开的刹那 | 2148 | normal | 88.2 | 0 |  | 2 |
| 9 | 签字的纸条 | 1572 | normal | 93.6 | 0 |  | 1 |
| 10 | 掌心抚过名册纹路 | 2513 | long | 90.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「说道“你」×4
  - [observe] attr_adv_pct 35.3 > 25.0（结构塌缩）
- 第 3 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 2.8 低于目标 5.0
  - dialogue_run_mean 17.5 高于目标 14.0
- 第 7 章：
  - 命中套话收尾句
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「账本上的铜钱印记」已存在
- 第 8 章：
  - narration_para_pct 3.6 低于目标 5.0
  - dialogue_run_mean 26.5 高于目标 14.0
- 第 9 章：
  - 单条套路句式超限：「他知道这」×3
- 第 10 章：
  - 单条套路句式超限：「李二点了点头」×3
  - [observe] 标题重复：「掌心抚过名册纹路」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18312
chapter_chars_mean: 1831
chapter_chars_median: 1707
chapter_chars_cv: 0.16
paragraphs_mean: 40.8
dialogue_chars_pct: 49.1
dialogue_para_pct: 86.8
interiority_para_pct: 4.3
narration_para_pct: 8.9
turn_under20_pct: 66.3
turn_over200_pct: 0.0
attr_say_pct: 23.1
attr_adv_pct: 12.4
scenes_per_chapter: 2
dialogue_run_mean: 9.8
turn_len_median: 15
```
