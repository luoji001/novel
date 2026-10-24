# 旧账单 生成报告

slug：`shuangwen-20261023-50`
档位：爽文　闸门模式：observe
章数：10　总字数：19468
LLM 调用：97 次，累计 444.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧账单的验证 | 1800 | normal | 96.6 | 0 |  | 1 |
| 2 | 旧账单摊开 | 1758 | normal | 92.4 | 0 |  | 2 |
| 3 | 旧账单摊开 | 1771 | normal | 93.1 | 0 |  | 3 |
| 4 | 旧账单摊开 | 1722 | normal | 93.9 | 0 |  | 3 |
| 5 | 旧账单摊开 | 1600 | normal | 91.3 | 0 |  | 2 |
| 6 | 旧账单被泼墨 | 2120 | normal | 92.1 | 0 |  | 3 |
| 7 | 账单被泼墨 | 2117 | normal | 92.9 | 0 |  | 2 |
| 8 | 旧账单摊开 | 1875 | normal | 91.4 | 0 |  | 2 |
| 9 | 旧账单摊开 | 2023 | normal | 92.5 | 0 |  | 1 |
| 10 | 摊开旧账单 | 2672 | long | 91.0 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4
- 第 3 章：
  - 单条套路句式超限：「李国忠的」×7、「林永年的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「旧账单摊开」已存在
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国忠的」×4
  - [observe] 标题重复：「旧账单摊开」已存在
- 第 5 章：
  - dialogue_run_mean 17.5 高于目标 14.0
  - [observe] 标题重复：「旧账单摊开」已存在
- 第 6 章：
  - 单条套路句式超限：「山门登记处」×4、「李国忠的」×3
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「李国忠的」×7
  - [observe] 标题与《旧账单被泼墨》近似 0.91 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「旧账单摊开」已存在
- 第 9 章：
  - [observe] 标题重复：「旧账单摊开」已存在
- 第 10 章：
  - 单条套路句式超限：「李国忠的」×4
  - narration_para_pct 4.5 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 21.3 高于目标 14.0
  - [observe] 标题与《旧账单摊开》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18463
chapter_chars_mean: 1846
chapter_chars_median: 1755
chapter_chars_cv: 0.16
paragraphs_mean: 43
dialogue_chars_pct: 47.6
dialogue_para_pct: 87.3
interiority_para_pct: 4.0
narration_para_pct: 8.7
turn_under20_pct: 77.3
turn_over200_pct: 0.0
attr_say_pct: 31.9
attr_adv_pct: 13.4
scenes_per_chapter: 1.6
dialogue_run_mean: 9.3
turn_len_median: 13
```
