# 签条 生成报告

slug：`shuangwen-20261022-145`
档位：爽文　闸门模式：observe
章数：10　总字数：19931
LLM 调用：97 次，累计 430.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签下的最后一笔 | 1886 | normal | 38.4 | 0 |  | 2 |
| 2 | 伪造的离职证明 | 2077 | normal | 92.6 | 0 |  | 1 |
| 3 | 划掉的名字 | 2243 | normal | 92.5 | 0 |  | 2 |
| 4 | 登记簿上的裂痕 | 2087 | normal | 92.9 | 0 |  | 1 |
| 5 | 签字笔的重量 | 1785 | normal | 91.1 | 0 |  | 0 |
| 6 | 签字笔的重量 | 2004 | normal | 92.2 | 0 |  | 2 |
| 7 | 签字笔的重量 | 1808 | normal | 90.6 | 0 |  | 1 |
| 8 | 签字笔的重量 | 1608 | normal | 37.1 | 0 |  | 5 |
| 9 | 签字笔的重量 | 1972 | normal | 91.3 | 0 |  | 4 |
| 10 | 签字笔的重量 | 2451 | long | 91.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×7
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周文远的」×5
- 第 3 章：
  - narration_para_pct 3.9 低于目标 5.0
  - attr_adv_pct 14.8 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「周文远的」×3
- 第 6 章：
  - narration_para_pct 4.9 低于目标 5.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 7 章：
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国强的」×4
  - narration_para_pct 2.9 低于目标 5.0
  - [observe] attr_adv_pct 66.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 9 章：
  - narration_para_pct 4.7 低于目标 5.0
  - attr_adv_pct 12.8 高于目标 12.0
  - dialogue_run_mean 20.5 高于目标 14.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 10 章：
  - 单条套路句式超限：「周文远的」×3
  - [observe] 标题重复：「签字笔的重量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18897
chapter_chars_mean: 1890
chapter_chars_median: 1890
chapter_chars_cv: 0.12
paragraphs_mean: 44.1
dialogue_chars_pct: 44.4
dialogue_para_pct: 81.7
interiority_para_pct: 6.4
narration_para_pct: 11.9
turn_under20_pct: 74.8
turn_over200_pct: 0.0
attr_say_pct: 33.0
attr_adv_pct: 13.5
scenes_per_chapter: 1.9
dialogue_run_mean: 7.8
turn_len_median: 12
```
