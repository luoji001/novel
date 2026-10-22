# 青云令 生成报告

slug：`shuangwen-20261022-12`
档位：爽文　闸门模式：observe
章数：10　总字数：19579
LLM 调用：97 次，累计 376.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 令牌裂痕 | 1855 | normal | 98.9 | 0 |  | 1 |
| 2 | 残片入匣 | 2218 | normal | 93.5 | 0 |  | 3 |
| 3 | 令牌裂痕 | 1935 | normal | 90.9 | 0 |  | 3 |
| 4 | 签字交令牌 | 1758 | normal | 93.1 | 0 |  | 2 |
| 5 | 雪夜赌令牌 | 1676 | normal | 93.6 | 0 |  | 1 |
| 6 | 令牌现真容 | 2057 | normal | 92.9 | 0 |  | 2 |
| 7 | 残片入匣 | 1908 | normal | 94.5 | 0 |  | 4 |
| 8 | 签字换名次 | 1964 | normal | 92.6 | 0 |  | 2 |
| 9 | 朱砂笔落纸 | 1773 | normal | 93.6 | 0 |  | 2 |
| 10 | 签字落笔 | 2425 | long | 94.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏怀安的」×4
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「玄机阁」×8
  - attr_adv_pct 13.6 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「玄机阁」×11
  - dialogue_run_mean 16.7 高于目标 14.0
  - [observe] 标题重复：「令牌裂痕」已存在
- 第 4 章：
  - 单条套路句式超限：「玄机阁」×8、「苏怀安的」×4
  - attr_adv_pct 22.2 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「玄机阁」×6
- 第 6 章：
  - 单条套路句式超限：「苏怀安的」×3
  - narration_para_pct 4.7 低于目标 5.0
- 第 7 章：
  - 单条套路句式超限：「玄机阁」×6
  - narration_para_pct 2.1 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「残片入匣」已存在
- 第 8 章：
  - 单条套路句式超限：「玄机阁」×5、「苏怀安的」×3
  - attr_adv_pct 21.4 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「玄机阁」×4
  - attr_adv_pct 14.3 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「苏怀安的」×7、「玄机阁」×7

## 整书结构指标

```
chapters: 10
total_chars: 18544
chapter_chars_mean: 1854
chapter_chars_median: 1808
chapter_chars_cv: 0.12
paragraphs_mean: 45
dialogue_chars_pct: 48.1
dialogue_para_pct: 83.4
interiority_para_pct: 5.4
narration_para_pct: 11.2
turn_under20_pct: 74.4
turn_over200_pct: 0.0
attr_say_pct: 23.4
attr_adv_pct: 11.9
scenes_per_chapter: 2.1
dialogue_run_mean: 7.4
turn_len_median: 12
```
