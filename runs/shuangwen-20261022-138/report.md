# 旧规副本 生成报告

slug：`shuangwen-20261022-138`
档位：爽文　闸门模式：observe
章数：10　总字数：18754
LLM 调用：97 次，累计 430.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜炉底部的厚度 | 1481 | normal | 100.0 | 0 |  | 1 |
| 2 | 铜炉上的凹陷 | 2175 | normal | 93.1 | 0 |  | 0 |
| 3 | 验单上的红叉 | 1994 | normal | 91.6 | 0 |  | 2 |
| 4 | 补正说明的签署 | 1649 | normal | 91.5 | 0 |  | 3 |
| 5 | 铅笔划破验收入单 | 1846 | normal | 91.7 | 0 |  | 1 |
| 6 | 副本与铜炉的对峙 | 1880 | normal | 92.0 | 0 |  | 2 |
| 7 | 铜炉底部的厚度 | 1713 | normal | 92.6 | 0 |  | 4 |
| 8 | 铜锤敲击裂痕 | 2268 | normal | 36.4 | 0 |  | 2 |
| 9 | 旧规副本的摩擦声 | 1680 | normal | 90.7 | 0 |  | 2 |
| 10 | 铜炉上的旧规副本 | 2058 | long | 90.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「周振国的」×3、「林远站在」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 5 章：
  - narration_para_pct 2.8 低于目标 5.0
- 第 6 章：
  - 单条套路句式超限：「镇工艺协会」×4
  - attr_adv_pct 23.5 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「镇工艺协会」×3
  - narration_para_pct 3.4 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「铜炉底部的厚度」已存在
- 第 8 章：
  - 单条套路句式超限：「周振国的」×4
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「镇工艺协会」×5
  - narration_para_pct 3.4 低于目标 5.0
- 第 10 章：
  - 单条套路句式超限：「周振国的」×4、「镇工艺协会」×3
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17869
chapter_chars_mean: 1787
chapter_chars_median: 1773
chapter_chars_cv: 0.13
paragraphs_mean: 36.2
dialogue_chars_pct: 45.3
dialogue_para_pct: 82.3
interiority_para_pct: 6.6
narration_para_pct: 11.0
turn_under20_pct: 64.7
turn_over200_pct: 0.0
attr_say_pct: 23.1
attr_adv_pct: 15.5
scenes_per_chapter: 1.3
dialogue_run_mean: 6.1
turn_len_median: 16
```
