# 旧账本 生成报告

slug：`shuangwen-20261023-140`
档位：爽文　闸门模式：observe
章数：10　总字数：19222
LLM 调用：97 次，累计 441.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字的手指 | 1769 | normal | 98.0 | 0 |  | 3 |
| 2 | 盖章的手势 | 1911 | normal | 91.5 | 0 |  | 4 |
| 3 | 翻出旧存根 | 2065 | normal | 91.7 | 0 |  | 3 |
| 4 | 账本与报表的对峙 | 1804 | normal | 94.3 | 0 |  | 1 |
| 5 | 手指摩挲旧账本边缘 | 1719 | normal | 37.7 | 0 |  | 1 |
| 6 | 账本与报表的对峙 | 1706 | normal | 93.4 | 0 |  | 3 |
| 7 | 手指摩挲旧账本边缘 | 1909 | normal | 93.6 | 0 |  | 3 |
| 8 | 手指摩挲证书边缘 | 1683 | normal | 37.8 | 0 |  | 3 |
| 9 | 手指摩挲名册边缘 | 2281 | normal | 94.6 | 0 |  | 3 |
| 10 | 手指摩挲账本边缘 | 2365 | long | 90.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 16.5 高于目标 14.0
- 第 2 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
- 第 3 章：
  - narration_para_pct 2.7 低于目标 5.0
  - attr_adv_pct 21.4 高于目标 12.0
  - dialogue_run_mean 17.5 高于目标 14.0
- 第 4 章：
  - 单条套路句式超限：「李国强的」×11、「他知道这」×3、「林小满的」×3
- 第 5 章：
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「账本与报表的对峙」已存在
- 第 7 章：
  - 单条套路句式超限：「李国强的」×9
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题重复：「手指摩挲旧账本边缘」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题与《手指摩挲旧账本边缘》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - narration_para_pct 3.8 低于目标 5.0
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题与《手指摩挲证书边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国强的」×3
  - [observe] 标题与《手指摩挲旧账本边缘》近似 0.94 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18199
chapter_chars_mean: 1820
chapter_chars_median: 1758
chapter_chars_cv: 0.13
paragraphs_mean: 42
dialogue_chars_pct: 50.8
dialogue_para_pct: 85.4
interiority_para_pct: 4.7
narration_para_pct: 9.8
turn_under20_pct: 69.2
turn_over200_pct: 0.0
attr_say_pct: 29.7
attr_adv_pct: 18.6
scenes_per_chapter: 1.6
dialogue_run_mean: 9.2
turn_len_median: 14
```
