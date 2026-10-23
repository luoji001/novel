# 当票 生成报告

slug：`shuangwen-20261022-132`
档位：爽文　闸门模式：observe
章数：10　总字数：17912
LLM 调用：97 次，累计 433.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧书换令牌 | 1791 | normal | 99.1 | 0 |  | 2 |
| 2 | 旧书换令牌 | 1788 | normal | 94.3 | 0 |  | 4 |
| 3 | 签字留痕 | 1837 | normal | 93.6 | 0 |  | 1 |
| 4 | 令牌对峙 | 1511 | normal | 92.0 | 0 |  | 1 |
| 5 | 旧书紧抱在怀中 | 1635 | normal | 92.0 | 0 |  | 3 |
| 6 | 令牌落入作废箱 | 1311 | normal | 94.5 | 0 |  | 2 |
| 7 | 令牌坠入作废箱 | 2007 | normal | 36.8 | 0 |  | 3 |
| 8 | 令牌对峙 | 1732 | normal | 37.6 | 0 |  | 3 |
| 9 | 铜钱与钢笔对决 | 1822 | normal | 94.2 | 0 |  | 3 |
| 10 | 令牌压住契约 | 2468 | long | 93.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「青云阁」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「青云阁」×3
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「旧书换令牌」已存在
- 第 3 章：
  - 单条套路句式超限：「青云阁」×3
- 第 4 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「青云阁」×3
  - dialogue_chars_pct 29.1 低于目标 30.0
- 第 6 章：
  - 单条套路句式超限：「青云阁」×6
  - attr_adv_pct 12.5 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「青云阁」×7
  - [observe] 章内自我复读 4 句（如「林远感到一阵无力，他知道无论如何都无法改变这个事…」）
  - [observe] 标题与《令牌落入作废箱》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「青云阁」×5
  - [observe] attr_adv_pct 31.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「令牌对峙」已存在
- 第 9 章：
  - 单条套路句式超限：「青云阁」×5
  - narration_para_pct 3.2 低于目标 5.0
  - dialogue_run_mean 15 高于目标 14.0
- 第 10 章：
  - 单条套路句式超限：「周承泽的」×4、「他知道这」×3、「青云阁」×3
  - attr_adv_pct 14.3 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 16834
chapter_chars_mean: 1683
chapter_chars_median: 1684
chapter_chars_cv: 0.17
paragraphs_mean: 46.6
dialogue_chars_pct: 48.9
dialogue_para_pct: 83.8
interiority_para_pct: 4.5
narration_para_pct: 11.7
turn_under20_pct: 79.6
turn_over200_pct: 0.0
attr_say_pct: 29.0
attr_adv_pct: 13.5
scenes_per_chapter: 1.3
dialogue_run_mean: 7.5
turn_len_median: 12
```
