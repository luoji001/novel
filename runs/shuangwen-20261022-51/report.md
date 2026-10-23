# 账本的签名 生成报告

slug：`shuangwen-20261022-51`
档位：爽文　闸门模式：observe
章数：10　总字数：19198
LLM 调用：97 次，累计 451.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本的空白处 | 1660 | normal | 93.1 | 0 |  | 3 |
| 2 | 签字笔的较量 | 2082 | normal | 94.9 | 0 |  | 0 |
| 3 | 账本的缺失处 | 1802 | normal | 37.8 | 0 |  | 4 |
| 4 | 账本的空白处 | 1964 | normal | 86.0 | 0 |  | 3 |
| 5 | 账本的缺口处 | 1887 | normal | 91.1 | 0 |  | 1 |
| 6 | 文书的缺口处 | 2138 | normal | 37.4 | 0 |  | 3 |
| 7 | 账本的数目 | 1873 | normal | 36.0 | 0 |  | 1 |
| 8 | 账本的对峙 | 1864 | normal | 93.4 | 0 |  | 4 |
| 9 | 账本的空白处 | 1871 | normal | 93.2 | 0 |  | 1 |
| 10 | 表决书的褶皱 | 2047 | long | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 37 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「李怀远的」×7
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题与《账本的空白处》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 38 高于目标 14.0
  - [observe] 标题重复：「账本的空白处」已存在
- 第 5 章：
  - [observe] 标题与《账本的缺失处》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 命中套话收尾句
  - [observe] attr_adv_pct 38.5 > 25.0（结构塌缩）
  - [observe] 标题与《账本的缺口处》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀远的」×3
  - narration_para_pct 4.5 低于目标 5.0
  - [observe] 标题与《账本的数目》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - [observe] 标题重复：「账本的空白处」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×7
  - attr_adv_pct 13.6 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 18244
chapter_chars_mean: 1824
chapter_chars_median: 1788
chapter_chars_cv: 0.08
paragraphs_mean: 40.3
dialogue_chars_pct: 54.4
dialogue_para_pct: 88.4
interiority_para_pct: 4.3
narration_para_pct: 7.3
turn_under20_pct: 65.3
turn_over200_pct: 0.0
attr_say_pct: 15.9
attr_adv_pct: 14.2
scenes_per_chapter: 2.4
dialogue_run_mean: 14.5
turn_len_median: 16
```
