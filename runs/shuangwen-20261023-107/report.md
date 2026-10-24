# 旧账单 生成报告

slug：`shuangwen-20261023-107`
档位：爽文　闸门模式：observe
章数：10　总字数：18623
LLM 调用：97 次，累计 437.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账单上的红印 | 1836 | normal | 39.7 | 0 |  | 3 |
| 2 | 账单上的红印 | 1993 | normal | 37.4 | 0 |  | 4 |
| 3 | 账单上的墨线 | 1844 | normal | 94.2 | 0 |  | 3 |
| 4 | 香灰里的裂痕 | 1700 | normal | 92.8 | 0 |  | 2 |
| 5 | 毛笔坠地 | 1820 | normal | 92.2 | 0 |  | 1 |
| 6 | 账单上的签字权 | 1808 | normal | 37.2 | 0 |  | 4 |
| 7 | 账单上的红印 | 1534 | normal | 94.2 | 0 |  | 3 |
| 8 | 账单上的红印 | 1588 | normal | 91.5 | 0 |  | 4 |
| 9 | 账单上的红印 | 2135 | normal | 92.9 | 0 |  | 4 |
| 10 | 账单上的墨线 | 2355 | long | 91.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「镇文化馆」×8、「沈怀远的」×4、「林秋实站在」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「林秋实站在镇文化馆的柜台前，手里攥着一张泛黄的纸…」）
- 第 2 章：
  - 单条套路句式超限：「沈怀远的」×3、「镇文化馆」×3
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「账单上的红印」已存在
- 第 3 章：
  - 单条套路句式超限：「沈怀远的」×4
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题与《账单上的红印》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈怀远的」×6
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「沈怀远的」×11、「镇文化馆」×3
- 第 6 章：
  - 单条套路句式超限：「沈怀远的」×4
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题与《账单上的红印》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「镇文化馆」×4
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「账单上的红印」已存在
- 第 8 章：
  - 单条套路句式超限：「沈怀远的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「账单上的红印」已存在
- 第 9 章：
  - narration_para_pct 4.1 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 15.3 高于目标 14.0
  - [observe] 标题重复：「账单上的红印」已存在
- 第 10 章：
  - 单条套路句式超限：「沈怀远的」×9、「说道“你」×3
  - [observe] 标题重复：「账单上的墨线」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17778
chapter_chars_mean: 1778
chapter_chars_median: 1752
chapter_chars_cv: 0.13
paragraphs_mean: 34.8
dialogue_chars_pct: 51.7
dialogue_para_pct: 86.9
interiority_para_pct: 4.7
narration_para_pct: 8.4
turn_under20_pct: 68.1
turn_over200_pct: 0.0
attr_say_pct: 41.9
attr_adv_pct: 17.8
scenes_per_chapter: 1.2
dialogue_run_mean: 9.0
turn_len_median: 14
```
