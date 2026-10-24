# 工龄证明 生成报告

slug：`shuangwen-20261023-117`
档位：爽文　闸门模式：observe
章数：10　总字数：17585
LLM 调用：97 次，累计 381.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 按住公章的手 | 1585 | normal | 98.7 | 0 |  | 1 |
| 2 | 摩挲证明的指尖 | 2053 | normal | 92.2 | 0 |  | 1 |
| 3 | 摩挲证明的指尖 | 1664 | normal | 89.5 | 0 |  | 3 |
| 4 | 摩挲证明的指尖 | 1390 | normal | 37.0 | 0 |  | 2 |
| 5 | 摩挲证明的指尖 | 1623 | normal | 90.0 | 0 |  | 3 |
| 6 | 摩挲证明的指尖 | 2104 | normal | 37.8 | 0 |  | 3 |
| 7 | 摩挲证明的指尖 | 1501 | normal | 92.7 | 0 |  | 2 |
| 8 | 摩挲证明的指尖 | 1659 | normal | 37.0 | 0 |  | 3 |
| 9 | 摩挲缴费单的指尖 | 1700 | normal | 37.0 | 0 |  | 4 |
| 10 | 摩挲证明的指尖 | 2296 | long | 90.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李慧芳的」×3
- 第 2 章：
  - narration_para_pct 3.1 低于目标 5.0
- 第 3 章：
  - attr_adv_pct 18.8 高于目标 12.0
  - dialogue_run_mean 19 高于目标 14.0
  - [observe] 标题重复：「摩挲证明的指尖」已存在
- 第 4 章：
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「摩挲证明的指尖」已存在
- 第 5 章：
  - 单条套路句式超限：「王主任的」×4
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「摩挲证明的指尖」已存在
- 第 6 章：
  - 单条套路句式超限：「李慧芳站在」×3
  - [observe] attr_adv_pct 55.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「摩挲证明的指尖」已存在
- 第 7 章：
  - 单条套路句式超限：「王主任的」×3
  - [observe] 标题重复：「摩挲证明的指尖」已存在
- 第 8 章：
  - 单条套路句式超限：「李慧芳的」×4
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
  - [observe] 标题重复：「摩挲证明的指尖」已存在
- 第 9 章：
  - 单条套路句式超限：「李慧芳的」×4
  - [observe] 章内自我复读 2 句（如「我说的是，你要拿出一个名分，证明你在公办学校工作…」）
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题与《摩挲证明的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李慧芳站在」×3
  - [observe] 标题重复：「摩挲证明的指尖」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16665
chapter_chars_mean: 1666
chapter_chars_median: 1578
chapter_chars_cv: 0.16
paragraphs_mean: 37.9
dialogue_chars_pct: 48.0
dialogue_para_pct: 83.3
interiority_para_pct: 6.0
narration_para_pct: 10.7
turn_under20_pct: 67.0
turn_over200_pct: 0.0
attr_say_pct: 38.0
attr_adv_pct: 23.1
scenes_per_chapter: 2.3
dialogue_run_mean: 7.4
turn_len_median: 16
```
