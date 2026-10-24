# 旧契 生成报告

slug：`shuangwen-20261023-68`
档位：爽文　闸门模式：observe
章数：10　总字数：19148
LLM 调用：97 次，累计 441.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 笔断木牌 | 1991 | normal | 39.4 | 0 |  | 2 |
| 2 | 木牌对契约 | 2215 | normal | 92.8 | 0 |  | 1 |
| 3 | 铜令牌对旧契 | 1677 | normal | 36.4 | 0 |  | 3 |
| 4 | 玉佩对旧契 | 1821 | normal | 91.6 | 0 |  | 1 |
| 5 | 契约上的凹痕 | 1745 | normal | 36.4 | 0 |  | 2 |
| 6 | 旧契对木牌 | 1768 | normal | 93.5 | 0 |  | 2 |
| 7 | 指纹浮于木牌 | 1561 | normal | 91.8 | 0 |  | 2 |
| 8 | 旧契对木牌 | 2170 | normal | 93.7 | 0 |  | 3 |
| 9 | 契约覆木牌 | 1980 | normal | 93.4 | 0 |  | 2 |
| 10 | 契约覆木牌 | 2210 | long | 91.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李长风的」×4
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
- 第 2 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李长风的」×6、「他知道这」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「李长风的」×5
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「周守义的笔尖悬在契约上方，迟迟没有落下…」）
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「李长风的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「旧契对木牌」已存在
- 第 9 章：
  - 单条套路句式超限：「李长风的」×3
  - [observe] 标题与《旧契对木牌》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「李长风的」×7
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「契约覆木牌」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18148
chapter_chars_mean: 1815
chapter_chars_median: 1796
chapter_chars_cv: 0.12
paragraphs_mean: 42.9
dialogue_chars_pct: 43.1
dialogue_para_pct: 79.4
interiority_para_pct: 6.8
narration_para_pct: 13.8
turn_under20_pct: 75.0
turn_over200_pct: 0.0
attr_say_pct: 22.2
attr_adv_pct: 20.0
scenes_per_chapter: 1
dialogue_run_mean: 4.9
turn_len_median: 12
```
