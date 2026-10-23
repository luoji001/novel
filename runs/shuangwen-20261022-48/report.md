# 账本 生成报告

slug：`shuangwen-20261022-48`
档位：爽文　闸门模式：observe
章数：10　总字数：22546
LLM 调用：97 次，累计 477.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本的秘密泄露 | 2175 | normal | 39.7 | 0 |  | 2 |
| 2 | 账本摊开的瞬间 | 2886 | normal | 92.6 | 0 |  | 2 |
| 3 | 账本递向陈会计 | 2267 | normal | 91.4 | 0 |  | 1 |
| 4 | 账本与旧手表的对峙 | 2050 | normal | 90.5 | 0 |  | 1 |
| 5 | 账本撕出的缺口 | 2111 | normal | 92.8 | 0 |  | 0 |
| 6 | 账本上的数字对决 | 2124 | normal | 91.9 | 0 |  | 2 |
| 7 | 账本递向陈会计 | 1847 | normal | 92.4 | 0 |  | 2 |
| 8 | 账本递向老张 | 2427 | normal | 91.7 | 0 |  | 2 |
| 9 | 工牌的褶痕浮现 | 2048 | normal | 93.2 | 0 |  | 1 |
| 10 | 账本拍案的瞬间 | 2601 | long | 93.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 4.1 低于目标 5.0
  - [observe] attr_adv_pct 45.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×6、「县供销社」×4
  - attr_adv_pct 12.9 高于目标 12.0
- 第 3 章：
  - attr_adv_pct 15.0 高于目标 12.0
- 第 4 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「县供销社」×3
  - narration_para_pct 4.3 低于目标 5.0
- 第 7 章：
  - 单条套路句式超限：「县供销社」×4
  - [observe] 标题重复：「账本递向陈会计」已存在
- 第 8 章：
  - 单条套路句式超限：「县供销社」×6
  - [observe] 标题与《账本递向陈会计》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 10 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题与《账本摊开的瞬间》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 21326
chapter_chars_mean: 2133
chapter_chars_median: 2038
chapter_chars_cv: 0.13
paragraphs_mean: 52.9
dialogue_chars_pct: 50.3
dialogue_para_pct: 86.8
interiority_para_pct: 4.8
narration_para_pct: 8.4
turn_under20_pct: 75.9
turn_over200_pct: 0.0
attr_say_pct: 30.4
attr_adv_pct: 13.4
scenes_per_chapter: 1.9
dialogue_run_mean: 8.2
turn_len_median: 12
```
