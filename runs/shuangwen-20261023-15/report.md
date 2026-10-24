# 旧版设备清单 生成报告

slug：`shuangwen-20261023-15`
档位：爽文　闸门模式：observe
章数：10　总字数：18609
LLM 调用：97 次，累计 418.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔划痕 | 1698 | normal | 39.2 | 0 |  | 2 |
| 2 | 签字笔传递 | 1806 | normal | 91.7 | 0 |  | 1 |
| 3 | 签字笔划痕 | 1686 | normal | 94.0 | 0 |  | 1 |
| 4 | 签字笔画圈 | 1552 | normal | 93.8 | 0 |  | 3 |
| 5 | 签字笔画圈 | 2406 | normal | 92.6 | 0 |  | 5 |
| 6 | 签字笔画圈 | 1709 | normal | 93.2 | 0 |  | 3 |
| 7 | 签字笔画圈 | 1576 | normal | 93.6 | 0 |  | 3 |
| 8 | 签下新合同 | 2255 | normal | 91.5 | 0 |  | 2 |
| 9 | 撕碎确认书 | 1791 | normal | 36.8 | 0 |  | 2 |
| 10 | 旧版清单对比 | 2120 | long | 92.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×5
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
- 第 2 章：
  - [observe] 标题与《签字笔划痕》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 标题重复：「签字笔划痕」已存在
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李建国的」×3、「他知道这」×3
  - [observe] 标题与《签字笔传递》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 3.7 低于目标 5.0
  - attr_adv_pct 21.7 高于目标 12.0
  - dialogue_run_mean 17 高于目标 14.0
  - [observe] 标题重复：「签字笔画圈」已存在
- 第 6 章：
  - 单条套路句式超限：「周晓芸的」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「签字笔画圈」已存在
- 第 7 章：
  - 单条套路句式超限：「李建国的」×5
  - narration_para_pct 3.6 低于目标 5.0
  - [observe] 标题重复：「签字笔画圈」已存在
- 第 8 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）

## 整书结构指标

```
chapters: 10
total_chars: 17704
chapter_chars_mean: 1770
chapter_chars_median: 1678
chapter_chars_cv: 0.15
paragraphs_mean: 38.2
dialogue_chars_pct: 52.1
dialogue_para_pct: 87.3
interiority_para_pct: 4.0
narration_para_pct: 8.7
turn_under20_pct: 65.1
turn_over200_pct: 0.0
attr_say_pct: 25.5
attr_adv_pct: 16.5
scenes_per_chapter: 1.5
dialogue_run_mean: 8.9
turn_len_median: 15
```
